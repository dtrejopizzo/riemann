# R162_1803: numerics for O1701.1-3 (N2, C2, sign of <u2,phi> on {mu2^ev=0}). UNCERTIFIED float.
# Base: t1601_nodal_rerun.py (fixed tail sign). Comb scaled by s (a = s*Lambda); 'del' = Lambda*1_{n>=5}.
import numpy as np, scipy.special as sp, sys
from scipy.integrate import quad
from scipy.optimize import brentq
import t1601_nodal_rerun as B
def build(T,K,model,s=1.0,tmax=3000.):
    nmin=5 if model=='del' else 2
    ns=[n for n in range(nmin,400) if np.log(n)<2*T and B.Lam(n)>0]
    V={n:s*2*B.Lam(n)/np.sqrt(n) for n in ns}
    m=lambda t: sp.digamma(0.25+0.5j*t).real-np.log(np.pi)
    f=lambda t: m(t)-sum(v*np.cos(t*np.log(n)) for n,v in V.items())
    X,W=B.grid(tmax)
    J=np.array([sp.spherical_jn(l,X*T) for l in range(K)])
    G=(J*(f(X)*W))@J.T
    tail=quad(lambda t: m(t)/(2*t*t*T*T),tmax,np.inf)[0]
    l=np.arange(K); sq=np.sqrt(2*l+1)
    sign=np.array([[0 if (a-b)%2 else (1 if ((b-a)//2)%2==0 else -1) for b in l] for a in l])
    A=(2*T/np.pi)*np.outer(sq,sq)*sign*(G+sign*tail)
    vec=lambda a: np.sqrt((2*l+1)/(2*T))*2*T*sp.spherical_in(l,a*T)
    return A,vec,l
def sc(f):
    g=f[np.abs(f)>1e-6*np.abs(f).max()]; return int(np.sum(np.sign(g[1:])!=np.sign(g[:-1])))
def mono(r):
    d=np.diff(r); sg=np.sign(np.median(d)); bad=d*sg<0
    return bad.mean(), (np.max(-d*sg)/np.ptp(r) if bad.any() else 0.0), int(sg)
def analyze(T,K,model,s=1.0,N=4001):
    A,vec,l=build(T,K,model,s)
    tt=np.linspace(0,T,N)[1:-1]
    Pl=np.array([sp.eval_legendre(k,tt/T)*np.sqrt((2*k+1)/(2*T)) for k in l])
    out={}
    for par,base in ((0,np.cosh),(1,np.sinh)):
        idx=np.arange(par,K,2); ev,U=np.linalg.eigh(A[np.ix_(idx,idx)])
        def fn(i):
            co=np.zeros(K); co[idx]=U[:,i]; f=co@Pl
            if f[0]<0: co,f=-co,-f
            return co,f
        c1,f1=fn(0); c2,f2=fn(1)
        fr,mv,sg=mono(f1/base(tt/2))
        out[par]=dict(mu1=ev[0],mu2=ev[1],pos=bool((f1>0).all()),minr=f1.min()/f1.max(),S1=sc(f1),S2=sc(f2),
                      mfrac=fr,mviol=mv,mdir=sg,ov=c2@vec(0.5)/np.linalg.norm(vec(0.5)[idx]) if par==0 else c2@vec(0.5))
    return out
def fmt(T,K,s,model,o,N):
    e,d=o[0],o[1]
    return (f"| {model} | {s} | {T:.4f} | {K} | {N} | {e['mu1']:.3e} | {e['mu2']:.3e} | {e['S2']} | {e['pos']} | {e['mfrac']:.4f} | {e['mviol']:.1e} | {e['mdir']:+d} | {e['ov']:+.4f} "
            f"| {d['mu1']:.3e} | {d['mu2']:.3e} | {d['pos']} | {d['S1']} | {d['S2']} | {d['mfrac']:.4f} | {d['mviol']:.1e} |")
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='scan':
        model=sys.argv[2]; s=float(sys.argv[3]); Ts=np.linspace(float(sys.argv[4]),float(sys.argv[5]),int(sys.argv[6]))
        for T in Ts:
            for K in (34,46):
                for N in ((4001,16001) if K==46 else (4001,)):
                    print(fmt(T,K,s,model,analyze(T,K,model,s,N),N)); sys.stdout.flush()
    else:  # crossing of mu2^ev
        model=sys.argv[2]; s=float(sys.argv[3]); a,b=float(sys.argv[4]),float(sys.argv[5])
        for K in (34,46):
            g=lambda T: analyze(T,K,model,s,801)[0]['mu2']
            ga,gb=g(a),g(b)
            if ga*gb>0: print(f"| {model} | {s} | K={K} | no crossing in [{a},{b}]: mu2({a})={ga:.3e}, mu2({b})={gb:.3e} |"); continue
            Tc=brentq(g,a,b,xtol=1e-7); o=analyze(Tc,K,model,s,16001)[0]
            print(f"| {model} | {s} | K={K} | T*={Tc:.6f} | mu2={o['mu2']:.1e} | S2={o['S2']} | <u2,phi^>={o['ov']:+.5f} | C2 frac={o['mfrac']:.4f} |"); sys.stdout.flush()
