# R163_203: Euler-gate stress test. UNCERTIFIED float. Operator as t2001_typeI_search (tail sign fixed R162_1590).
# Even primitive form A = arch - sum_j s_j w(x_j) cos(t log x_j), w(x)=2 log x/sqrt x, Legendre basis on [-T,T].
import sys, numpy as np, scipy.special as sp
from numpy.polynomial.legendre import leggauss, legval
from scipy.integrate import quad
from scipy.optimize import brentq
sys.path.insert(0,'/home/trabajo/Documentos/research/riemann/03-research/phase-162-row-d-first-contact-closure/scripts/c3')
import t1601_nodal_rerun as B
K=30
def mats(T,atoms):
    m=lambda t: sp.digamma(0.25+0.5j*t).real-np.log(np.pi)
    X,W=B.grid(1000.); J=np.array([sp.spherical_jn(l,X*T) for l in range(K)])
    l=np.arange(K); sq=np.sqrt(2*l+1)
    sign=np.array([[0 if (a-b)%2 else (1 if ((b-a)//2)%2==0 else -1) for b in l] for a in l])
    pre=(2*T/np.pi)*np.outer(sq,sq)*sign
    tail=quad(lambda t: m(t)/(2*t*t*T*T),1000.,np.inf)[0]
    s=m(X)-sum(c*2*np.log(x)/np.sqrt(x)*np.cos(X*np.log(x)) for x,c in atoms if np.log(x)<2*T)
    A=pre*((J*(s*W))@J.T+sign*tail)
    idx=np.arange(0,K,2); phi=(np.sqrt((2*l+1)/(2*T))*2*T*sp.spherical_in(l,0.5*T))[idx]
    return A[np.ix_(idx,idx)], phi/np.linalg.norm(phi), idx
def contact(T,atoms):
    A,ph,idx=mats(T,atoms)
    Q,_=np.linalg.qr(ph.reshape(-1,1),mode='complete'); P=Q[:,1:]
    ev,V=np.linalg.eigh(P.T@A@P); return ev[0], P@V[:,0], idx, ev[:3]
gx,gw=leggauss(400)
def F_on(T,c,idx,u):  # F(u) on [-T,T]
    coef=np.zeros(K); coef[idx]=c*np.sqrt((2*idx+1)/(2*T)); return legval(u/T,coef)
def modes(T,c,idx,ell,ks):
    u=T*gx; w=T*gw; g=np.exp(u/2)*F_on(T,c,idx,u)
    return np.array([np.sum(w*g*np.exp(1j*2*np.pi*k/ell*u)) for k in ks]), np.sum(w*g*g)
def Eper(T,c,idx,ell):  # ||P_ell g||^2_[0,ell] / ||g||^2 = sum_k |K_F(1+2pi i k/ell)|^2/(ell ||g||^2)
    v=np.linspace(0,ell,4001)[:-1]; S=np.zeros_like(v)
    for mm in range(-5,6):
        uu=v+mm*ell; ins=np.abs(uu)<=T
        S[ins]+= (np.exp(uu/2)*F_on(T,c,idx,uu))[ins]
    u=T*gx; g2=np.sum(T*gw*(np.exp(u)*F_on(T,c,idx,u)**2))
    return np.mean(S**2)*ell/g2
def stab(T,ells,n=20000):
    # lambda_min of sum_p P_p^*P_p on L^2[-T,T]: orbit-graph matrices; inf over base points
    best=np.inf
    for u0 in np.linspace(-T,T,n):
        # orbit of u0 under lattice Z ell_1+Z ell_2 inside window (BFS)
        pts=[u0]; seen={round(u0,12)}; q=[u0]
        while q:
            v=q.pop()
            for e in ells:
                for mm in range(-4,5):
                    w=v+mm*e
                    if mm and abs(w)<=T and round(w,12) not in seen: seen.add(round(w,12)); pts.append(w); q.append(w)
        pts=np.array(pts); M=np.zeros((len(pts),len(pts)))
        for e in ells:
            r=np.round((pts[:,None]-pts[None,:])/e,9); M+= (np.abs(r-np.round(r))<1e-7)
        best=min(best,np.linalg.eigvalsh(M)[0])
    return best
def run(name,atoms,lo,hi,extra=()):
    f=lambda T: contact(T,atoms)[0]
    Ts=np.linspace(lo,hi,8); vals=[f(T) for T in Ts]; T=None
    for a,b,va,vb in zip(Ts,Ts[1:],vals,vals[1:]):
        if va>0 and vb<=0: T=brentq(f,a,b,xtol=1e-6); break
    tag='contact'
    if T is None: T=Ts[int(np.argmin(vals))]; tag='no contact, min-lam T'
    lam,c,idx,ev=contact(T,atoms)
    print('==',name,tag,'T=%.5f lam=%.3e lowest=%s'%(T,lam,np.array2string(ev,precision=4)),flush=True)
    for lab,ell in [('p=2',np.log(2)),('p=3',np.log(3))]+list(extra):
        md,g2=modes(T,c,idx,ell,range(0,5))
        print('  ',lab,'|K_F(1+2pi ik/l)|/||g|| k=0..4:',' '.join('%.3e'%x for x in np.abs(md)/np.sqrt(g2)),' E=%.4f'%Eper(T,c,idx,ell),flush=True)
if __name__=='__main__':
    run('typeI s2=0.99976781,s3=0',[(2,0.99976781),(3,0.)],0.57,0.62)
    for s2 in (0.999,0.9995,1.0,1.0005):
        run('row s2=%.4f,s3=0'%s2,[(2,s2),(3,0.)],0.55,0.65)
    run('deletion (0,0)',[(2,0.),(3,0.)],0.57,0.62)
    run('zeta n<=3 (1,1)',[(2,1.),(3,1.)],0.56,0.69)
    run('beurling x=1.6 s=1.412',[(1.6,1.412)],0.70,0.77,[('x=1.6',np.log(1.6))])
    for T in (0.593,0.5958,0.733,0.8047,0.89):
        print('stab {2,3} T=%.4f lam_min=%.4e'%(T,stab(T,[np.log(2),np.log(3)],3000)),' {1.6,3}: %.4e'%stab(T,[np.log(1.6),np.log(3)],1500),flush=True)
