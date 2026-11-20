"""Constants and checks for the proof of the tapered prolate leakage bound (ROUND_009_A).
(1) Ritz upper bounds for the Sturm-Liouville eigenvalues theta_k(c) (Legendre basis), check theta_8(6pi) < (6pi)^2.
(2) delta_0 = 1 - sqrt(chi_0(2pi)).  (3) moments mu_j, nu_4 of the cubic B-spline mollifier.
(4) 1 - chi_k(2piN) and the threshold N_0.  (5) sanity checks of the exterior/sliver pointwise bounds."""
import mpmath as mp, numpy as np
from prolate_defect import prolate, evalP, one_minus_chi0
from prolate_defect_k import omc
mp.mp.dps=40
def ritz(c,K=120):
    c=mp.mpf(c); res=[]
    for par in (0,1):
        ks=list(range(par,K,2)); m=len(ks)
        A=mp.zeros(m)
        for i,k in enumerate(ks):
            A[i,i]=k*(k+1)+c**2*mp.mpf(2*k*(k+1)-1)/((2*k+3)*(2*k-1))
            if i<m-1:
                A[i,i+1]=A[i+1,i]=c**2*mp.mpf((k+2)*(k+1))/((2*k+3)*mp.sqrt(mp.mpf((2*k+1)*(2*k+5))))
        ev=mp.eigsy(A,eigvals_only=True); res+= [ev[j] for j in range(m)]
    return sorted(res)
c=6*mp.pi; th=ritz(c)
print("theta_k(6pi) Ritz upper bounds k=0..10:",[mp.nstr(x,8) for x in th[:11]]," c^2=",mp.nstr(c**2,8))
print("margin c^2-theta_8 =",mp.nstr(c**2-th[8],6))
d=one_minus_chi0(2*mp.pi,dps=40); chis=1-d; d0=1-mp.sqrt(chis)
print("1-chi_0(2pi)=",mp.nstr(d,8)," delta_0=",mp.nstr(d0,8))
k8=lambda s: (mp.sin(mp.pi*s/2)/(mp.pi*s/2))**4 if s!=0 else mp.mpf(1)
dk8=lambda s: mp.diff(k8,s)
mu={j:2*mp.quad(lambda s: s**j*k8(s)**2,[0,2,4,8,16,32,mp.inf])/2 for j in (0,2,4,6)}
nu4=mp.quad(lambda s: s**4*dk8(s)**2,[0,2,4,8,16,32,64,128])+mp.mpf(0)
print("mu:",{j:mp.nstr(v,8) for j,v in mu.items()}," nu4:",mp.nstr(nu4,8))
th_=1/(8*mp.pi**2)
Bst=(4*mu[2]+8*nu4)*th_**-3*mp.mpf(3)**-8+8*(2*mp.pi)**4*mu[4]*th_**-5*mp.mpf(3)**-2+8*(2*mp.pi)**4*mu[6]*th_**-7
print("B_* =",mp.nstr(Bst,8))
for dd,kk in ((5,8),(3,4)):
    C1=1024*mp.pi**2*dd*Bst/d0; print("d=%d C_1 (R <= C_1 N^14 (1-chi_%d)) ="%(dd,kk),mp.nstr(C1,6))
    for N in range(3,13):
        o=omc(kk,2*mp.pi*N,40)
        lhs=256*16*mp.pi*2*mp.pi*dd*8*mp.pi**2*mu[0]*N**3*o
        print("  N=%d 1-chi_%d=%s  thresholdLHS/delta0^2=%s"%(N,kk,mp.nstr(o,6),mp.nstr(lhs/d0**2,4)))
# sanity: pointwise bounds; exterior values via phi(x) = alpha^{-1} int_{-1}^{1} phi(t) e^{-icxt} dt (Legendre series diverges off [-1,1])
for cc in (6*mp.pi,12*mp.pi):
    for k in (0,4,8):
        ks,D=prolate(cc,dps=40,parity=k%2,nfun=k//2+1); f=lambda t: evalP(ks,D[k//2],mp.mpf(t))
        o=omc(k,cc,40); chi=1-o
        g=lambda x: mp.quad(lambda t: f(t)*(mp.cos(cc*x*t) if k%2==0 else mp.sin(cc*x*t)),mp.linspace(-1,1,41))
        al=g(mp.mpf('0.3'))/f(mp.mpf('0.3')); p1=f(1)
        print("c=%s k=%d check phi(1) vs integral: %s; |alpha|^2 c/(2pi chi)=%s"%(mp.nstr(cc,5),k,mp.nstr(g(1)/al/p1,8),mp.nstr(al**2*cc/(2*mp.pi*chi),8)))
        ts=[1+mp.mpf(j)/(4*cc) for j in range(1,120)]
        r0=max(abs(g(t)/al)/abs(p1) for t in ts)
        r1=max(abs(mp.diff(lambda x:g(x)/al,t))/(cc**2*t*abs(p1)) for t in ts[:40])
        tin=[1-mp.mpf(j)/(160*cc**2) for j in range(21)]   # sliver of length 1/(8c^2)
        r2=max(abs(f(t))/abs(p1) for t in tin); r3=max(abs(mp.diff(f,t))/(cc**2*abs(p1)) for t in tin[1:])
        print("   phi(1)^2/(8c^2(1-chi)/chi)=%s phi(1)^2/(c(1-chi))=%s ext max|phi|/|phi(1)|=%s ext max|phi'|/(c^2t|phi(1)|)=%s sliver max|phi|/|phi(1)|=%s sliver max|phi'|/(c^2|phi(1)|)=%s"%tuple(mp.nstr(x,4) for x in (p1**2/(8*cc**2*o/chi),p1**2/(cc*o),r0,r1,r2,r3)))
