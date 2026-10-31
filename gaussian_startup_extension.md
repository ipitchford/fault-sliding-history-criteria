# Historical centre criterion for a finite Gaussian source

> **Status (31 October 2026).** This supporting note is superseded by Appendix C of the revised manuscript wherever the two differ. Changes there: (i) the primary startup hypothesis is nonnegative latent forcing $H_{\rm pre}\ge0$ before nucleation with $H_{\rm pre}(t_n)>0$, and nondecreasing injection is a sufficient condition; (ii) rates may be piecewise $C^1$ with jumps of either sign, using right-continuous centre margins and their left limits; (iii) the existence of the crack radius after nucleation is proved rather than assumed (Proposition 4.1). The statements below remain correct for the class they state. Equation labels (G1)--(G13) are those of this note.


Research proof supplement, 28 October 2026. This note extends the historical centre theorem to a fixed Gaussian source under a monotone-pressure startup through transverse nucleation. It uses the exact Dawson-kernel order properties proved in `arbitrary_history_extension.md`. The Gaussian width is physical and fixed; no singular limit is taken here.

## 1. Statement and precise startup assumptions

Fix \(\varepsilon>0\), and retain the positive constants and circular scalar fault model of the manuscript. Let \(q\in C^1([0,T])\), \(q\ge0\), extended by zero before time zero. Thus \(dq=q(0)\delta_0+q'(s)ds\). The pressure is

\[
p_\varepsilon(r,t)=c_p\int_0^t q(s)
\frac{\exp[-r^2/(4\alpha(t-s+\varepsilon))]}{t-s+\varepsilon}\,ds.
\tag{G1}
\]

The derivative at time zero, when used, is the right derivative.

Let \(t_n\in(0,T)\) be the first time at which \(p_\varepsilon(0,t_n)=\Delta/f\). Assume

\[
\partial_t p_\varepsilon(0,t)\ge0\quad(0\le t\le t_n),
\qquad
\partial_t p_\varepsilon(0,t_n)>0.
\tag{G2}
\]

Suppose the unique positive zero-SIF trial radius exists on \((t_n,T]\), and define \(R(t)=0\) for \(0\le t\le t_n\). For \(t>t_n\), define the trial responses

\[
C(t)=\int_{[0,t]}K_{R(t)}(0,t-s+\varepsilon)\,dq(s),
\qquad
V(r,t)=\int_{[0,t]}K_{R(t)}(r,t-s+\varepsilon)\,dq(s).
\tag{G3}
\]

The physical velocity is \(4fc_pV/(\pi\mu)\). Endpoints in (G3) are harmless for the continuous histories assumed here.

**Theorem G.** Under these assumptions,

\[
V(r,t)\ge0\quad\text{for every }0\le r<R(t),\ t_n<t\le T
\]

if and only if

\[
C(t)\ge0\quad\text{for every }t_n<t\le T.
\]

Whenever these equivalent conditions hold, every noncentral interior velocity and the edge-normalised velocity is strictly positive, and \(R'(t)>0\). Earlier tangential centre-velocity zeros after birth are allowed. Thus the first threshold contact is central, and the whole centre history detects any first loss of forward-slip admissibility.

No positive initial injection jump or immediate ramp is required here; a dormant initial interval is permitted. The actual startup assumptions are (G2). A sufficient practical condition is that \(q\) be nondecreasing through first nucleation. Subsequent rate reversals are unrestricted. The theorem makes no assertion for arbitrary pressure-decreasing prebirth histories or tangential nucleation.

## 2. A normalized kernel through the zero-radius interval

For \(0\le s\le v\le T\), set

\[
a(v,s)=
\begin{cases}
\displaystyle\frac{K_{R(v)}(0,v-s+\varepsilon)}{K_{R(v)}(0,\varepsilon)},&R(v)>0,\\[6pt]
\displaystyle\frac{\varepsilon}{v-s+\varepsilon},&R(v)=0.
\end{cases}
\tag{G4}
\]

Since \(K_R(0,u)\sim R/u\) as \(R\downarrow0\), this is a continuous positive extension, with \(a(v,v)=1\) and \(a(v,s)\le1\). Define

\[
H(v)=\int_{[0,v]}a(v,s)\,dq(s).
\tag{G5}
\]

For positive radius, \(H(v)=C(v)/K_{R(v)}(0,\varepsilon)\). Before and at birth,

\[
H(v)=\varepsilon\int_{[0,v]}\frac{dq(s)}{v-s+\varepsilon}
=\frac{\varepsilon}{c_p}\partial_vp_\varepsilon(0,v).
\tag{G6}
\]

The last identity follows by integration by parts, or by differentiating (G1): both expressions equal
\(\varepsilon[q(v)/\varepsilon-\int_0^v q(s)/(v-s+\varepsilon)^2ds]\).
The history \(H\) is continuous across nucleation. It is a normalized forcing history before birth; it is not the physical centre slip velocity, which is zero on the locked prebirth fault.

Consequently, (G2) and a nonnegative postbirth centre history give \(H\ge0\) throughout the elapsed interval. Transversality and continuity give a nonempty prebirth time interval on which \(H>0\).

## 3. Strict positive transfer along a nondecreasing radius

Temporarily prescribe a continuous nondecreasing path \(R\ge0\), including its prebirth zero interval, and fix \(t>t_n\). The centre logarithmic age slope

\[
\ell_R(u)=\partial_u\log K_R(0,u)
\]

increases in both \(u\) and \(R>0\), and extends at zero radius to \(\ell_0(u)=-1/u\). These are the centre-kernel lemmas of the point-source supplement. Row normalization in (G4) does not alter the logarithmic derivative with respect to response age.

Choose an output kernel \(b(u)=K_{R(t)}(r,u)\) for fixed \(0<r<R(t)\), or \(b(u)=J_{R(t)}(u)\) for the edge-normalised response. Put

\[
d_t=K_{R(t)}(0,\varepsilon)>0,
\qquad
\Phi(u)=\frac{b(u)}{K_{R(t)}(0,u)}.
\]

In either case, \(\Phi'(u)>0\). There is a continuous strictly positive kernel \(h(t,s)\) satisfying

\[
b(t-s+\varepsilon)
=b(\varepsilon)a(t,s)+\int_s^t h(t,v)a(v,s)\,dv.
\tag{G7}
\]

Indeed, solve the backward Volterra equation

\[
\begin{aligned}
h(t,s)&=d_ta(t,s)\Phi'(t-s+\varepsilon)
+\int_s^t P(s,v)h(t,v)\,dv,\\
P(s,v)&=a(v,s)
\left[\ell_{R(t)}(t-s+\varepsilon)
-\ell_{R(v)}(v-s+\varepsilon)\right].
\end{aligned}
\tag{G8}
\]

The kernel is continuous and satisfies \(0\le P\le1/\varepsilon\), while the forcing is continuous and strictly positive. The uniformly convergent Volterra Neumann series therefore gives a bounded continuous \(h>0\). Differentiation with respect to \(s\), after division by \(a(t,s)\), verifies (G7); its terminal value is \(b(\varepsilon)\). This is exactly the earlier positive-transfer construction with a unit diagonal, so no division by a vanishing radius and no limiting regularisation are involved.

Integrating (G7) against the finite signed increment measure gives

\[
\int_{[0,t]}b(t-s+\varepsilon)\,dq(s)
=b(\varepsilon)H(t)+\int_0^t h(t,v)H(v)\,dv.
\tag{G9}
\]

All kernels are bounded on the compact time triangle, so Fubini is immediate. If \(H\ge0\) throughout the elapsed interval and \(H>0\) on any nonempty subinterval before \(t\), the right side is strictly positive. Under (G2), the required positive interval is available before nucleation. Thus a nonnegative postbirth centre history along a nondecreasing radius gives strictly positive noncentral and edge responses, regardless of later centre tangencies.

## 4. Transverse birth and automatic radius growth

At birth,

\[
\partial_{rr}p_\varepsilon(0,t_n)
=-\frac{c_p}{2\alpha}\int_0^{t_n}
\frac{q(s)}{(t_n-s+\varepsilon)^2}\,ds<0.
\tag{G10}
\]

The strict inequality follows because the positive nucleation pressure requires nonzero injection history. Radial smoothness gives

\[
\mathcal A p_\varepsilon(R,t)
=p_\varepsilon(0,t)+\frac13\partial_{rr}p_\varepsilon(0,t)R^2+O(R^4).
\]

Apply the implicit function theorem to the zero-SIF equation in the variable \(R^2\). Assumption (G2) gives

\[
R(t)^2
=\frac{-3\partial_t p_\varepsilon(0,t_n)}{\partial_{rr}p_\varepsilon(0,t_n)}
(t-t_n)+o(t-t_n),
\tag{G11}
\]

with a strictly positive coefficient. More precisely, the implicit function theorem gives a \(C^1\) branch for \(R^2\) with this positive derivative at birth. Continuity of that derivative therefore gives \(R'>0\) just after nucleation. Equivalently, its edge response

\[
E(t)=\int_{[0,t]}J_{R(t)}(t-s+\varepsilon)\,dq(s)
\]

extends continuously to
\(E(t_n)=\partial_t p_\varepsilon(0,t_n)/c_p>0\), since \(J_R(u)\to1/u\) as \(R\downarrow0\).

For positive radius, differentiating the zero-SIF equation gives

\[
R'(t)=-\frac{fc_pE(t)}{F_a(R(t),t)},\qquad F_a<0.
\tag{G12}
\]

Suppose the centre history is nonnegative on \((t_n,T]\). If \(E\) had a first zero \(t_e>t_n\), then \(R\) would be nondecreasing up to \(t_e\), including its prebirth zero interval. Equations (G6) and (G2) give \(H\ge0\) on that entire history, with \(H>0\) on a prebirth interval. The strict transfer (G9), applied to the edge output at \(t_e\), would give \(E(t_e)>0\), a contradiction. Hence \(E>0\) and \(R'>0\) throughout the interval. Applying (G9) at each time proves all noncentral velocities strictly positive. This establishes sufficiency in Theorem G; necessity follows by taking \(r=0\).

## 5. A directly checkable startup condition and scope

If \(q\) is nondecreasing on \([0,t_n]\), then \(dq\) is a nonnegative measure there, and

\[
\partial_t p_\varepsilon(0,t)
=c_p\int_{[0,t]}\frac{dq(s)}{t-s+\varepsilon}\ge0.
\tag{G13}
\]

At nucleation the history is nontrivial, so this derivative is strictly positive. Thus nondecreasing injection through first nucleation is sufficient for all startup conditions in Theorem G. This sufficient condition permits a dormant initial interval and allows any subsequent smooth nonnegative rate history.

The theorem also permits prebirth rate reductions if the central pressure nevertheless remains nondecreasing. General pressure-decreasing prebirth histories are outside the proved scope: physical centre slip is zero then, while the latent history (G6) can be negative. The unit-diagonal continuation makes that distinction explicit. Tangential birth with zero pressure derivative is also left open here.

The normalization and generic Volterra mechanism are mathematical equivalences within the existing kernel framework. Any prospective novelty belongs to the exact kernel properties, the resulting finite-width historical centre criterion, and its stated geological startup conditions; the separate novelty audit controls historical-priority claims.
