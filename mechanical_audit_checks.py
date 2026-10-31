"""Independent finite checks of mechanical normalisations, not a formal proof."""
from pathlib import Path
import hashlib
import json
import platform
import time
import numpy as np
import scipy
from scipy.integrate import quad


def check(condition, message="certificate check failed"):
    """Explicit check that still fails under python -O."""
    if not condition:
        raise SystemExit(message)

ROOT = Path(__file__).resolve().parent


def outside_half_laplacian(radial_function, support, r):
    # In R^2, the standard half-Laplacian has constant C_(2,1/2)=1/(2*pi).
    # At exterior x, f(x)=0, so no principal-value prescription is needed.
    def integrand(rho):
        angular = quad(
            lambda theta: (r*r+rho*rho-2*r*rho*np.cos(theta))**(-1.5),
            0, 2*np.pi, epsabs=1e-10, epsrel=1e-10)[0]
        return rho*radial_function(rho)*angular
    return -quad(integrand,0,support,epsabs=1e-10,epsrel=1e-10)[0]/(2*np.pi)


def run():
    start = time.perf_counter()
    out = {
        'scope': 'Independent exterior singular-integral evaluations and exact toy-load checks; no theorem-prover verification',
        'python': platform.python_version(),
        'scipy': scipy.__version__,
    }
    cap = []
    for a,r in [(1.,1.2),(1.,2.),(2.,3.)]:
        calculated = outside_half_laplacian(lambda rho: np.sqrt(a*a-rho*rho),a,r)
        exact = np.arcsin(a/r)-a/np.sqrt(r*r-a*a)
        cap.append({'a':a,'r':r,'direct_half_laplacian':calculated,
                    'closed_form':exact,'absolute_error':abs(calculated-exact)})
    check(max(x['absolute_error'] for x in cap)<1e-9)
    out['square_root_cap'] = cap

    # g(r)=1-r^2 => A[g](a)=1-2*a^2/3 and R=sqrt(3/2).
    # The zero-SIF inversion is delta=16*(R^2-r^2)^(3/2)/(9*pi), with mu=1.
    R=np.sqrt(1.5)
    delta=lambda rho:16*(R*R-rho*rho)**1.5/(9*np.pi)
    E=lambda a,r:(2/np.pi)*(np.arcsin(a/r)-a/np.sqrt(r*r-a*a))
    exterior=[]
    for r in [1.3,1.7,3.]:
        Ldelta=.5*outside_half_laplacian(delta,R,r)
        predicted=-quad(lambda a:(-4*a/3)*E(a,r),0,R,
                        epsabs=1e-11,epsrel=1e-11)[0]
        gap=Ldelta-(1-r*r)
        rhs=-(1-2*r*r/3)+quad(lambda a:(-4*a/3)*E(a,r),R,r,
                              epsabs=1e-10,epsrel=1e-10)[0]
        exterior.append({'r':r,'direct_elastic_traction':Ldelta,
                         'cap_superposition_traction':predicted,
                         'friction_gap':gap,'eq36_rhs':rhs,
                         'max_abs_error':max(abs(Ldelta-predicted),abs(gap-rhs))})
    check(min(x['friction_gap'] for x in exterior)>0)
    check(max(x['max_abs_error'] for x in exterior)<1e-9)
    out['polynomial_load_exterior'] = exterior

    eps=.02
    T=1.
    out['gaussian_finite_volume_B']=[
        {'t':t,'B':2*(np.sqrt(t+eps)-np.sqrt(t-T+eps)),
         'B_derivative':1/np.sqrt(t+eps)-1/np.sqrt(t-T+eps)}
        for t in [1.1,10.,1000.]]
    out['elapsed_seconds']=time.perf_counter()-start
    out['exit_status']=0
    (ROOT/'mechanical_audit_checks.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':
    run()
