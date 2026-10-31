"""Exploratory search only: arbitrary Gaussian injection, first off-centre failure."""
import numpy as np
from scipy.special import exp1,dawsn
from scipy.optimize import brentq
from numpy.polynomial.legendre import leggauss
import json,time
from pathlib import Path

xx,ww=leggauss(48)
X=(xx+1)/2; W=ww/2

def H(z):
    return np.divide(dawsn(z),z,out=np.ones_like(z),where=z!=0)

def pabel(R,ages,jumps,eps):
    if R==0:
        return np.dot(jumps,np.log1p(ages/eps))
    z=R*R*(1-X*X)/4
    pp=exp1(z[:,None]/(ages[None,:]+eps))-exp1(z[:,None]/eps)
    return np.dot(W,pp@jumps)

def kernels(r,R,ages,eps):
    L=np.sqrt(R*R-r*r)
    u=ages+eps
    z=np.sqrt(r*r+L*L*X[:,None]**2)/(2*np.sqrt(u[None,:]))
    return L*(W@H(z))/u

def evaluate(times,levels,eps,theta,mesh):
    jumps=np.diff(np.r_[0.,levels])
    records=[]
    centre_bad=False
    for t in mesh:
        mask=times<=t+1e-14
        ages=t-times[mask]; dj=jumps[mask]
        p0=pabel(0,ages,dj,eps)
        if p0<=theta:
            records.append((t,0.,0.,0.,0.))
            continue
        hi=2*np.sqrt(t+eps)
        while pabel(hi,ages,dj,eps)>theta: hi*=2
        R=brentq(lambda rr:pabel(rr,ages,dj,eps)-theta,1e-13,hi,xtol=2e-8)
        cv=np.dot(kernels(0.,R,ages,eps),dj)
        off=[np.dot(kernels(fr*R,R,ages,eps),dj) for fr in [.1,.3,.5,.7,.9,.99]]
        minoff=min(off); frac=[.1,.3,.5,.7,.9,.99][int(np.argmin(off))]
        records.append((t,R,cv,minoff,frac))
        if cv < -1e-7:
            centre_bad=True
            return None,records,'centre_first'
        if minoff < -1e-7:
            return {'times':times.tolist(),'levels':levels.tolist(),'eps':eps,'theta':theta,
                    'failure':records[-1],'previous':records},records,'candidate'
    return None,records,'no_failure'

def run(seed=1234,n=1200):
    rng=np.random.default_rng(seed); start=time.perf_counter()
    stats={'seed':seed,'planned':n,'counts':{'centre_first':0,'no_failure':0,'candidate':0},'examples':[]}
    for trial in range(n):
        times=np.array([0.,.12,.27,.43,.58,.71,.82,.91])
        eps=float(10**rng.uniform(-2.1,-.25))
        if trial%2==0:
            levels=np.exp(rng.normal(0,.9,len(times)))
        else:
            levels=np.exp(np.cumsum(rng.normal(.08,.22,len(times))))
        jumps=np.diff(np.r_[0.,levels])
        base=np.array([pabel(0,t-times[times<=t],jumps[times<=t],eps) for t in np.r_[times[1:],1.]])
        theta=float(rng.uniform(.02,.98)*max(base))
        # Includes both sides of each jump and 4 interior times per interval.
        mesh=np.unique(np.r_[np.linspace(.005,1.,25),times[1:]-1e-7,times[1:]+1e-7,1.])
        candidate,rec,status=evaluate(times,levels,eps,theta,mesh)
        stats['counts'][status]+=1
        if candidate:
            stats['examples'].append(candidate)
            print(json.dumps({'candidate':candidate}),flush=True)
            break
        if (trial+1)%100==0:
            print(json.dumps({'completed':trial+1,'counts':stats['counts'],'seconds':time.perf_counter()-start}),flush=True)
    stats['elapsed_seconds']=time.perf_counter()-start
    Path(__file__).with_name('arbitrary_history_probe_results.json').write_text(json.dumps(stats,indent=2))
    print(json.dumps(stats),flush=True)

if __name__=='__main__':run()
