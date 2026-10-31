#!/usr/bin/env python3
"""Reproduce numerical checks for the unimodal injection locking criterion.

All examples are synthetic and dimensionless: alpha=1, f*c_p*q0=1.
Velocities omit the common positive multiplier 4*f*c_p/(pi*mu).
The fully sliding trial branch is not a physical continuation after locking.
"""
from pathlib import Path
import os
os.environ.setdefault("MPLCONFIGDIR", "/tmp/geology-mpl")
import json
import math
import numpy as np
from scipy.integrate import quad
from scipy.optimize import brentq
from scipy.special import dawsn, i0e
from numpy.polynomial.legendre import leggauss
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt


def check(condition, message="certificate check failed"):
    """Explicit check that still fails under python -O."""
    if not condition:
        raise SystemExit(message)

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "numerics"
OUT.mkdir(exist_ok=True)
GINF = np.pi**1.5/4
X, W = leggauss(80)
X, W = (X+1)/2, W/2


def dawson_quotient(z):
    z = np.asarray(z)
    with np.errstate(divide="ignore", invalid="ignore"):
        ans = dawsn(z)/z
    return np.where(z == 0, 1.0, ans)


def h(a, u, alpha=1.0):
    """The inner Abel transform of the Gaussian impulse response."""
    return dawson_quotient(np.asarray(a)/np.sqrt(4*alpha*u))/u


def G(z):
    """Integral_0^z Dawson(x)/x dx; no asymptotic series is used."""
    if z <= 12:
        return quad(lambda x: float(dawson_quotient(x)), 0, z,
                    epsabs=2e-12, epsrel=2e-12)[0]
    # Tail change of variables y=1/x removes the infinite integration limit.
    tail = np.dot(W, dawsn(z/X)/(X/z))/z
    return GINF-tail


def kernel(r, u, R, alpha=1.0):
    if r >= R:
        return 0.0
    if r == 0:
        return 2*np.sqrt(alpha/u)*G(R/np.sqrt(4*alpha*u))
    L = np.sqrt(R*R-r*r)
    return quad(lambda x: float(h(np.hypot(r, x), u, alpha)), 0, L,
                epsabs=2e-11, epsrel=3e-11)[0]


def kernel_double(r, u, R, order=220):
    """Independent positive two-dimensional quadrature, moderate ages only."""
    x, w = leggauss(order)
    x, w = (x+1)/2, w/2
    L = np.sqrt(R*R-r*r)
    exponent = -(r*r+L*L*x[:,None]**2)*(1-x[None,:]**2)/(4*u)
    return L/u*np.einsum("i,ij,j->", w, np.exp(exponent), w)


def kernel_infinite(r, u):
    return np.pi**1.5/(2*np.sqrt(u))*i0e(r*r/(8*u))


def q(t, drop=0.6, T=1.0, duration=1.0):
    return np.where(np.asarray(t)<0, 0.0,
                    1-drop*np.clip((np.asarray(t)-T)/duration, 0, 1))


def split_integral(fun, lo, hi, knots=()):
    pts = [lo]+[p for p in sorted(knots) if lo < p < hi]+[hi]
    return sum(quad(fun, a, b, epsabs=2e-10, epsrel=2e-10)[0]
               for a,b in zip(pts[:-1],pts[1:]))


def pressure_abel(a, t, drop=0.6, epsilon=0.0, T=1.0, duration=1.0):
    if a == 0 and epsilon == 0:
        return np.inf
    return split_integral(
        lambda u: float(q(t-u,drop,T,duration))*float(h(a,u+epsilon)),
        0,t,(t-T-duration,t-T))


def radius(t, theta=0.1, drop=0.6, epsilon=0.0, T=1.0, duration=1.0):
    args=(t,drop,epsilon,T,duration)
    if epsilon and pressure_abel(0,*args) <= theta:
        return 0.0
    hi=2*np.sqrt(t+epsilon)
    while pressure_abel(hi,*args)>theta:
        hi*=2
    lo=hi/2
    while pressure_abel(lo,*args)<=theta:
        lo/=2
    return brentq(lambda R:pressure_abel(R,*args)-theta,
                  lo,hi,xtol=1e-10,rtol=1e-12)


def integrate_kernel(r, lo, hi, R, epsilon=0.0):
    if hi <= lo:
        return 0.0
    # y=sqrt(u+epsilon) cancels the integrable centre singularity.
    a,b=np.sqrt(lo+epsilon),np.sqrt(hi+epsilon)
    return quad(lambda y: 2*y*kernel(r,y*y,R),a,b,
                epsabs=2e-9,epsrel=2e-9)[0]


def velocity(r,t,R,drop=0.6,epsilon=0.0,T=1.0,duration=1.0):
    ans=kernel(r,t+epsilon,R)
    if t>T:
        ans-=drop/duration*integrate_kernel(r,max(0,t-T-duration),t-T,R,epsilon)
    return ans


def centre(t,theta=0.1,drop=0.6,epsilon=0.0):
    R=radius(t,theta,drop,epsilon)
    return velocity(0,t,R,drop,epsilon)


def slip(r,t,theta=0.1,drop=0.6,epsilon=0.0):
    """Independent original static inversion, includes the 4/pi multiplier."""
    R=radius(t,theta,drop,epsilon)
    if r>=R:
        return 0.0
    L=np.sqrt(R*R-r*r)
    # The logarithmic pressure at r=0 is integrable in this x integral.
    val=quad(lambda x:pressure_abel(np.hypot(r,x),t,drop,epsilon)-theta,
             0,L,epsabs=2e-9,epsrel=2e-9)[0]
    return 4/np.pi*val


def run_checks():
    result={"description":"Synthetic quadrature checks, not observational validation",
            "normalisation":{"alpha":1,"f_c_p_q0":1,"T":1,"L":1}}
    identities=[]
    for r,u,R in [(0,.2,1),(.4,.2,1),(.9,1,1),(0,.01,2),(.8,.05,2)]:
        a=kernel(r,u,R); b=kernel_double(r,u,R)
        identities.append({"r":r,"u":u,"R":R,"one_dimensional":a,
                           "double_quadrature":b,"relative_error":abs(a-b)/a})
    result["kernel_identity_checks"]=identities
    check(max(x["relative_error"] for x in identities)<2e-10)

    # Independent numerical probe of the proved age ordering.
    min_delta=1.0
    order_count=0
    for r in [.01,.1,.3,.6,.9,.99,.999]:
        ages=np.geomspace(1e-5,1e4,110)
        ratios=np.array([kernel(r,u,1)/kernel(0,u,1) for u in ages])
        min_delta=min(min_delta,float(np.diff(ratios).min()))
        order_count+=len(ages)-1
    result["age_order"]={"comparisons":order_count,"minimum_positive_increment":min_delta}
    check(min_delta>0)

    # A counterexample to radial monotonicity of old/young response ratios.
    rr=np.linspace(0,.999,151)
    ratio=np.array([kernel(r,.01,1)/kernel(r,.001,1) for r in rr])
    im=int(np.argmax(ratio))
    result["stronger_radial_claim_counterexample"]={"centre":float(ratio[0]),
        "maximum":float(ratio[im]),"radius_of_grid_max":float(rr[im]),
        "near_rim":float(ratio[-1])}
    check(ratio[im]>ratio[-1]>ratio[0])

    cases=[]
    for theta in [.01,.05,.1,.5,1.0]:
        for epsilon in [0.0,.02]:
            grid=np.linspace(1+1e-8,1.9,45)
            grid_values=[centre(t,theta,.6,epsilon) for t in grid]
            k=next(k for k in range(1,len(grid)) if grid_values[k]<0)
            tl=brentq(lambda t:centre(t,theta,.6,epsilon),grid[k-1],grid[k],xtol=3e-10)
            R=radius(tl,theta,.6,epsilon)
            vv=[velocity(z*R,tl,R,.6,epsilon) for z in [0,.01,.05,.1,.25,.5,.75,.95,.999]]
            cases.append({"theta":theta,"epsilon":epsilon,"first_zero":tl,
                          "R_at_zero":R,"q_at_zero":float(q(tl)),
                          "positive_pre_crossing_grid_values":grid_values[:k],
                          "velocity_at_fractions_0_001_005_01_025_05_075_095_0999":vv})
            check(abs(vv[0])<3e-8 and min(vv[1:])>0)
    result["linear_taper_cases"]=cases
    result["infinite_radius_linear_taper"]={"drop":.6,
        "first_zero":(1+np.sqrt(1+1/.6**2))/2,
        "maximum_all_time_drop_for_T1_L1":1/(2*np.sqrt(2))}

    finite_diffs=[]
    t=1.23;theta=.1;epsilon=.02;R=radius(t,theta,.6,epsilon)
    for rf in [0,.2,.7]:
        r=rf*R
        target=4/np.pi*velocity(r,t,R,.6,epsilon)
        estimates=[]
        for dt in [2e-3,1e-3,5e-4]:
            fd=(slip(r,t+dt,theta,.6,epsilon)-slip(r,t-dt,theta,.6,epsilon))/(2*dt)
            estimates.append({"dt":dt,"finite_difference":fd,"absolute_error":abs(fd-target)})
        finite_diffs.append({"radius_fraction":rf,"exact_kernel":target,"approximations":estimates})
        check(estimates[-1]["absolute_error"]<2e-5)
    result["moving_boundary_derivative_check"]=finite_diffs

    # Multi-peaked trial history: positive at centre, negative in a ring.
    counter=[]
    for r in [0,.8,1.0,1.5]:
        val=i0e(r*r/8)-np.sqrt(2)*i0e(r*r/4)+.15*np.sqrt(10)*i0e(r*r/.8)
        counter.append({"r":r,"normalised_infinite_velocity":float(val)})
    result["multipeak_instantaneous_centre_counterexample"]={
        "jumps":[[0,1],[.5,-1],[.9,.15]],"time":1,"values":counter,
        "caveat":"Trial branch already failed after t=.5; this is not a physical post-locking solution."}
    check(counter[0]["normalised_infinite_velocity"]>0)
    check(counter[1]["normalised_infinite_velocity"]<0)

    # Direct finite-R analogue, set Delta to make this R an exact radius root.
    R=30.; eps=.01; t=1.
    jumps=[(0,1),(.5,-1),(.9,.15)]
    vals=[sum(amp*kernel(r,t-s+eps,R) for s,amp in jumps) for r in [0,.8,1.,1.5]]
    def qq(s): return 1. if s<.5 else (0. if s<.9 else .15)
    theta=sum(quad(lambda s:qq(s)*float(h(R,t-s+eps)),a,b)[0]
              for a,b in [(0,.5),(.5,.9),(.9,1)])
    result["finite_radius_multipeak_counterexample"]={"R":R,"epsilon":eps,
        "theta":theta,"radii":[0,.8,1.,1.5],"velocities":vals}
    check(vals[0]>0 and min(vals[1:3])<0)

    (OUT/"verification_results.json").write_text(json.dumps(result,indent=2))
    return result


def make_plots(result):
    plt.rcParams.update({"font.family":"DejaVu Sans","font.size":10,
        "axes.spines.top":False,"axes.spines.right":False,
        "axes.labelcolor":"#33302e","text.color":"#33302e",
        "axes.titleweight":"bold","figure.facecolor":"#fffdf8",
        "axes.facecolor":"#fffdf8","savefig.facecolor":"#fffdf8"})
    plum="#78375d"; ochre="#b17721"; moss="#55715a"; slate="#536471"
    fig,axs=plt.subplots(2,2,figsize=(11.5,8.3),layout="constrained")
    ages=np.geomspace(1e-3,100,100)
    for r,col in zip([.2,.5,.8],[plum,ochre,moss]):
        vals=[kernel(r,u,1)/kernel(0,u,1) for u in ages]
        axs[0,0].semilogx(ages,vals,color=col,label=f"r/R = {r:g}",lw=2)
    axs[0,0].set(xlabel="Response age u (R = 1, α = 1)",ylabel="K(r,u) / K(0,u)",
                 title="A  Relative weight increases with response age")
    axs[0,0].legend(frameon=False)
    ts=np.linspace(1.001,1.65,67)
    for theta,col in zip([.01,.1,.5],[moss,plum,ochre]):
        vs=[centre(t,theta,.6,.02) for t in ts]
        axs[0,1].plot(ts,vs,color=col,label=f"stress deficit Θ = {theta:g}",lw=1.8)
    lim=[np.pi**1.5/2*(1/np.sqrt(t+.02)-1.2*(np.sqrt(t-1+.02)-np.sqrt(.02))) for t in ts]
    axs[0,1].plot(ts,lim,color=slate,ls="--",label="Infinite radius, same Gaussian source")
    axs[0,1].axhline(0,color="#817c74",lw=.8)
    axs[0,1].set(xlabel="Time t (taper begins at 1)",ylabel="Formal centre slip rate / positive factor",
                 title="B  Finite radius advances the first loss of full sliding")
    axs[0,1].legend(frameon=False,fontsize=8)
    case=next(c for c in result["linear_taper_cases"] if c["theta"]==.1 and c["epsilon"]==.02)
    tl=case["first_zero"]
    rr=np.linspace(0,.999,100)
    for dt,col in zip([-.04,0,.04],[moss,plum,ochre]):
        t=tl+dt;R=radius(t,.1,.6,.02)
        vals=[velocity(rf*R,t,R,.6,.02) for rf in rr]
        label=f"t = {t:.3f}"+(" (onset)" if dt==0 else (" (trial only)" if dt>0 else ""))
        axs[1,0].plot(rr,vals,color=col,ls="--" if dt>0 else "-",label=label,lw=1.9)
    axs[1,0].axhline(0,color="#817c74",lw=.8)
    axs[1,0].set(xlabel="Radius r / R(t)",ylabel="Formal slip rate / positive factor",
                 title="C  The centre reaches zero first")
    axs[1,0].legend(frameon=False,fontsize=8)
    tt=np.linspace(1,10,250)
    qm=2/np.pi*np.arcsin(np.sqrt(1/tt))
    axs[1,1].plot(tt,qm,color=plum,lw=2.4,label="Minimum limiting-model continuation")
    axs[1,1].plot(tt,2/(np.pi*np.sqrt(tt)),color=ochre,ls="--",label="Asymptotic 2 / (π√t)")
    axs[1,1].set(xlabel="Time after starting unit injection (T = 1)",ylabel="Injection rate q / q₀",
                 title="D  Minimum limiting taper: infinite total volume")
    axs[1,1].legend(frameon=False,fontsize=8)
    fig.suptitle("A scalar history criterion for the first loss of full sliding\n"
                 "Dimensionless: α = q₀ = T = L = 1; 60% linear rate reduction; Gaussian ε = 0.02 in B–C",
                 fontsize=13,weight="bold")
    fig.savefig(OUT/"fault_locking_results.png",dpi=190)
    fig.savefig(OUT/"fault_locking_results.pdf")
    plt.close(fig)


if __name__=="__main__":
    results=run_checks()
    make_plots(results)
    print(json.dumps({"checks":"passed", "cases":results["linear_taper_cases"],
                      "output":str(OUT)},indent=2))
