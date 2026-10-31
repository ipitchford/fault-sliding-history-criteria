#!/usr/bin/env python3
"""Shared vectorised kernels for the revision check scripts.

Dimensionless units: alpha = 1, rates in units of q0, and the radius
equation is  int_0^t q(s) J_a(t-s+eps) ds = Theta,  Theta = Delta/(f c_p q0).
Velocities omit the common positive factor 4 f c_p/(pi mu).

The routines use composite Gauss-Legendre quadrature.  They are deliberately
independent of the adaptive SciPy quadrature in verify_fault_criterion.py,
which the check scripts use as a cross-check.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import dawsn
from scipy.optimize import brentq

A_STAR = math.pi ** 1.5 / 2.0      # K_infinity(0,u) = A_STAR / sqrt(u)
G_INF = math.pi ** 1.5 / 4.0

_X, _W = leggauss(64)
_X, _W = (_X + 1.0) / 2.0, _W / 2.0
_XS, _WS = leggauss(24)
_XS, _WS = (_XS + 1.0) / 2.0, _WS / 2.0


def set_resolution(nodes):
    """Change the Gauss-Legendre order used on every time/age panel."""
    global _XS, _WS
    x, w = leggauss(int(nodes))
    _XS, _WS = (x + 1.0) / 2.0, w / 2.0


def check(condition, message="check failed"):
    """Explicit check that still fails under python -O."""
    if not condition:
        raise SystemExit(message)


def round_sig(value, digits=10):
    """Round floats (recursively) to a fixed number of significant figures."""
    if isinstance(value, dict):
        return {k: round_sig(v, digits) for k, v in value.items()}
    if isinstance(value, (list, tuple)):
        return [round_sig(v, digits) for v in value]
    if isinstance(value, (np.floating, float)):
        v = float(value)
        if v == 0.0 or not math.isfinite(v):
            return v
        return float(f"{v:.{digits}g}")
    if isinstance(value, (np.integer,)):
        return int(value)
    if isinstance(value, np.bool_):
        return bool(value)
    if isinstance(value, np.ndarray):
        return round_sig(value.tolist(), digits)
    return value


def dawson_over_x(z):
    z = np.asarray(z, dtype=float)
    out = np.ones_like(z)
    nz = z != 0
    out[nz] = dawsn(z[nz]) / z[nz]
    return out


def G(z):
    """G(z) = int_0^z D(x)/x dx, vectorised."""
    z = np.atleast_1d(np.asarray(z, dtype=float))
    out = np.empty_like(z)
    small = z <= 6.0
    if np.any(small):
        zs = z[small][:, None]
        out[small] = zs[:, 0] * (dawson_over_x(zs * _X[None, :]) @ _W)
    if np.any(~small):
        zl = z[~small][:, None]
        # int_z^inf D(x)/x dx = int_0^1 D(z/tau)/tau dtau (smooth at tau=0)
        tau = _X[None, :]
        tail = (dawsn(zl / tau) / tau) @ _W
        out[~small] = G_INF - tail
    return out


def K0(R, u):
    """Centre kernel K_R(0,u) = 2 u^{-1/2} G(R/(2 sqrt u)); R may be inf."""
    u = np.asarray(u, dtype=float)
    if np.isinf(R):
        return A_STAR / np.sqrt(u)
    return 2.0 / np.sqrt(u) * G(R / (2.0 * np.sqrt(u))).reshape(np.shape(u))


def J(a, u):
    """Abel impulse / edge kernel J_a(u) = D(z)/(u z), z = a/(2 sqrt u)."""
    u = np.asarray(u, dtype=float)
    out = np.empty_like(u)
    zero = u <= 0
    out[zero] = 2.0 / (a * a)
    uu = u[~zero]
    out[~zero] = dawson_over_x(a / (2.0 * np.sqrt(uu))) / uu
    return out


def Kr(r, R, u, panels=6):
    """Interior kernel K_R(r,u) = int_0^L J_{sqrt(r^2+x^2)}(u) dx."""
    u = np.atleast_1d(np.asarray(u, dtype=float))
    if r >= R:
        return np.zeros_like(u)
    if r == 0.0:
        return K0(R, u)
    L = math.sqrt(R * R - r * r)
    edges = np.linspace(0.0, L, panels + 1)
    x = (edges[:-1, None] + (edges[1:] - edges[:-1])[:, None] * _X[None, :]).ravel()
    w = ((edges[1:] - edges[:-1])[:, None] * _W[None, :]).ravel()
    a = np.sqrt(r * r + x * x)
    z = a[None, :] / (2.0 * np.sqrt(u[:, None]))
    vals = dawson_over_x(z) / u[:, None]
    return vals @ w


class History:
    """Piecewise-C1 rate: atoms (time, jump) incl. the initial value, and
    pieces (s0, s1, derivative-function) carrying the absolutely continuous
    part of dq.  value(s) returns q(s) (right-continuous)."""

    def __init__(self, atoms, pieces, value):
        self.atoms = [(float(s), float(a)) for s, a in atoms]
        self.pieces = [(float(a), float(b), f) for a, b, f in pieces]
        self.value = value

    def breakpoints(self):
        pts = {s for s, _ in self.atoms}
        for a, b, _ in self.pieces:
            pts.add(a)
            pts.add(b)
        return sorted(pts)


def _age_panels(t, hist, scale, include_t=False):
    """Panels in age u in [0,t] split at history breakpoints and on a
    geometric ladder around the diffusive scale."""
    pts = {0.0, t}
    for s in hist.breakpoints():
        if 0.0 < t - s < t:
            pts.add(t - s)
    k = scale * 2.0 ** np.arange(-30, 41)
    for v in k:
        if 0.0 < v < t:
            pts.add(float(v))
    return np.array(sorted(pts))


def history_integral(kernel, t, hist, eps=0.0, closed=False, sqrt_sub=True,
                     scale=1.0):
    """int_{[0,t)} kernel(t-s+eps) dq(s)  (closed=True uses [0,t]).

    kernel is a vectorised function of the response age.  The absolutely
    continuous part uses age panels; with sqrt_sub the substitution u=y^2
    removes an integrable u^{-1/2} singularity at zero age."""
    total = 0.0
    for s, a in hist.atoms:
        if s < t or (closed and s == t):
            total += a * float(kernel(np.array([t - s + eps]))[0])
    for s0, s1, f in hist.pieces:
        lo, hi = max(s0, 0.0), min(s1, t)
        if hi <= lo:
            continue
        ulo, uhi = t - hi, t - lo
        if sqrt_sub:
            ylo, yhi = math.sqrt(ulo), math.sqrt(uhi)
            edges = _ladder(ylo, yhi, math.sqrt(scale))
            y = (edges[:-1, None] + (edges[1:] - edges[:-1])[:, None] * _XS).ravel()
            w = ((edges[1:] - edges[:-1])[:, None] * _WS).ravel()
            u = y * y
            total += float(np.sum(w * 2.0 * y * kernel(u + eps) * f(t - u)))
        else:
            edges = _ladder(ulo, uhi, scale)
            u = (edges[:-1, None] + (edges[1:] - edges[:-1])[:, None] * _XS).ravel()
            w = ((edges[1:] - edges[:-1])[:, None] * _WS).ravel()
            total += float(np.sum(w * kernel(u + eps) * f(t - u)))
    return total


def _ladder(lo, hi, scale):
    pts = {lo, hi}
    for v in scale * 2.0 ** np.arange(-30, 41):
        if lo < v < hi:
            pts.add(float(v))
    pts = np.array(sorted(pts))
    # refine every panel into two for safety
    mids = (pts[:-1] + pts[1:]) / 2.0
    return np.array(sorted(set(pts.tolist()) | set(mids.tolist())))


def pressure_abel(a, t, hist, eps=0.0):
    """int_0^t q(s) J_a(t-s+eps) ds  (= Abel-averaged pressure / c_p)."""
    edges = _age_panels(t, hist, max(a * a / 4.0, 1e-300))
    lo, hi = edges[:-1], edges[1:]
    u = (lo[:, None] + (hi - lo)[:, None] * _XS[None, :]).ravel()
    w = ((hi - lo)[:, None] * _WS[None, :]).ravel()
    qs = np.asarray(hist.value(t - u), dtype=float)
    return float(np.sum(w * qs * J(a, u + eps)))


def centre_pressure(t, hist, eps):
    """p_eps(0,t)/c_p for eps>0."""
    edges = _age_panels(t, hist, max(eps, 1e-12))
    lo, hi = edges[:-1], edges[1:]
    u = (lo[:, None] + (hi - lo)[:, None] * _XS[None, :]).ravel()
    w = ((hi - lo)[:, None] * _WS[None, :]).ravel()
    qs = np.asarray(hist.value(t - u), dtype=float)
    return float(np.sum(w * qs / (u + eps)))


def radius(t, hist, theta, eps=0.0, xtol=1e-13):
    """Zero-SIF radius (0 if no positive root)."""
    if eps > 0.0 and centre_pressure(t, hist, eps) <= theta:
        return 0.0
    hi = 2.0 * math.sqrt(t + eps)
    while pressure_abel(hi, t, hist, eps) > theta:
        hi *= 2.0
    lo = hi / 2.0
    n = 0
    while pressure_abel(lo, t, hist, eps) <= theta:
        lo /= 2.0
        n += 1
        if n > 200:
            return 0.0
    return brentq(lambda a: pressure_abel(a, t, hist, eps) - theta, lo, hi,
                  xtol=xtol * max(1.0, hi), rtol=4e-15, maxiter=300)


def centre_margin(t, hist, R, eps=0.0, closed=False):
    return history_integral(lambda u: K0(R, u), t, hist, eps, closed,
                            sqrt_sub=True, scale=max(R * R / 4.0, 1e-300))


def edge_response(t, hist, R, eps=0.0, closed=False):
    return history_integral(lambda u: J(R, u), t, hist, eps, closed,
                            sqrt_sub=False, scale=max(R * R / 4.0, 1e-300))


def interior_velocity(r, t, hist, R, eps=0.0, closed=False):
    return history_integral(lambda u: Kr(r, R, u), t, hist, eps, closed,
                            sqrt_sub=True, scale=max(R * R / 4.0, 1e-300))


def abel_half(t, hist, eps=0.0, closed=False):
    """int (t-s+eps)^{-1/2} dq(s)  (the Abel quantity H q for eps=0)."""
    return history_integral(lambda u: 1.0 / np.sqrt(u), t, hist, eps, closed,
                            sqrt_sub=True, scale=1.0)


def first_moment(t, hist, eps=0.0, closed=False):
    """int (t-s+eps) |dq|(s)."""
    total = 0.0
    for s, a in hist.atoms:
        if s < t or (closed and s == t):
            total += abs(a) * (t - s + eps)
    for s0, s1, f in hist.pieces:
        lo, hi = max(s0, 0.0), min(s1, t)
        if hi <= lo:
            continue
        x = lo + (hi - lo) * _X
        total += float(np.sum((hi - lo) * _W * np.abs(f(x)) * (t - x + eps)))
    return total


def taper_history(drop, T=1.0, L=1.0):
    """q = 1 until T, linear decrease by `drop` over L, then constant."""
    slope = -drop / L

    def value(s):
        s = np.asarray(s, dtype=float)
        return np.where(s < 0, 0.0, 1.0 - drop * np.clip((s - T) / L, 0.0, 1.0))

    return History([(0.0, 1.0)], [(T, T + L, lambda s: slope + 0.0 * s)], value)


def step_history(levels, times):
    """Piecewise-constant rate: level levels[k] on [times[k], times[k+1])."""
    atoms = []
    prev = 0.0
    for lev, tm in zip(levels, times):
        atoms.append((tm, lev - prev))
        prev = lev
    times_arr = np.array(times, dtype=float)
    levels_arr = np.array(levels, dtype=float)

    def value(s):
        s = np.asarray(s, dtype=float)
        idx = np.searchsorted(times_arr, s, side="right") - 1
        out = np.where(idx >= 0, levels_arr[np.clip(idx, 0, None)], 0.0)
        return out

    return History(atoms, [], value)
