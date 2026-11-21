"""Band-limited Weil form: C(d,T0)=lambda_max(P_F,A_Phi) on a 29-dim sinc span at T0 (Section 2-3)."""
import numpy as np, mpmath as mp, sys
from scipy.linalg import eigh
from scipy.special import digamma
def Phi(r):
    return np.real(digamma(0.25+0.5j*r))-np.log(np.pi)
def lam(n):
    for p in range(2,n+1):
        if n%p==0:
            m=n
            while m%p==0: m//=p
            return np.log(p) if m==1 else 0.0
def tails(d,rj,lo,hi):
    # int of S_i S_j Phi over r>hi and r<lo, using
    # S_i S_j = (-1)^(i-j) sin^2(d(r-r_1)) / (d^2 (r-r_i)(r-r_j)),  sin^2 x = (1-cos 2x)/2
    from scipy.integrate import quad
    N=len(rj); r1=rj[0]; T=np.zeros((N,N)); w=2*d
    for i in range(N):
        for j in range(i,N):
            ri,rk=rj[i],rj[j]; tot=0.0
            # right tail r = s, s>hi
            g=lambda s: Phi(s)/((s-ri)*(s-rk))
            sm=quad(g,hi,np.inf,limit=500)[0]
            c=quad(g,hi,np.inf,weight='cos',wvar=w)[0]; sn=quad(g,hi,np.inf,weight='sin',wvar=w)[0]
            tot+=sm/2-(np.cos(w*r1)*c+np.sin(w*r1)*sn)/2
            # left tail r = -s, s>-lo ; cos(w(-s-r1)) = cos(ws)cos(wr1) - sin(ws)sin(wr1)
            g2=lambda s: Phi(-s)/((-s-ri)*(-s-rk))
            sm=quad(g2,-lo,np.inf,limit=2000)[0]
            c=quad(g2,-lo,np.inf,weight='cos',wvar=w)[0]; sn=quad(g2,-lo,np.inf,weight='sin',wvar=w)[0]
            tot+=sm/2-(np.cos(w*r1)*c-np.sin(w*r1)*sn)/2
            T[i,j]=T[j,i]=(-1)**(i-j)*tot/d**2
    return T
def engine(d,T0,N=29,R=400.0,M=400001,tail=True):
    # archimedean Gram: trapezoid on [T0-R,T0+R] plus the exact tails beyond (if tail)
    rj=T0+(np.arange(N)-(N-1)/2)*np.pi/d
    r=np.linspace(T0-R,T0+R,M); dr=r[1]-r[0]
    S=np.sinc(d*(r[None,:]-rj[:,None])/np.pi)
    A=(S*Phi(r))@S.T*dr
    if tail: A=A+tails(d,rj,T0-R,T0+R)
    # F part: exact Fourier: int S_i S_j cos(u r) dr, via t-integral
    P=np.zeros((N,N))
    for n in range(2,int(np.exp(2*d))+1):
        l=lam(n)
        if l==0: continue
        u=np.log(n)
        # I(u)=2pi/(4d^2) int_{t in[-d,d], t+u in[-d,d]} e^{-i t ri + i(t+u) rj} dt
        a,b=max(-d,-d-u),min(d,d-u)
        if b<=a: continue
        D=rj[None,:]-rj[:,None]   # rj - ri
        Dz=np.where(D==0,1.0,D)
        J=np.where(D==0,b-a,(np.exp(1j*b*D)-np.exp(1j*a*D))/(1j*Dz))
        I=2*np.pi/(4*d*d)*np.exp(1j*u*rj)[None,:]*J
        P+=2*l/np.sqrt(n)*np.real(I)   # cos = Re of e^{iur} (symmetric)
    return A,P
if __name__=="__main__":
    T0=float(sys.argv[1]) if len(sys.argv)>1 else 1000
    for d in [1,2,2.5,3,5]:
        A,P=engine(d,T0)
        w=eigh(P,A,eigvals_only=True)
        print("d=%.1f  x=%.3f  C=%.6f  lambda_min(A_Phi)=%.2f"%(d,2*d/np.log(T0),w[-1],np.linalg.eigvalsh(A).min()))
