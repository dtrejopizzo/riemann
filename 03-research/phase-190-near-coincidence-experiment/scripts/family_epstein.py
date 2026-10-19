"""CA_C_007: eta-family test for FE-class objects: Epstein zeta of x^2+y^2 (=4 zeta_{Q(i)}, Euler) and x^2+5y^2 (class number 2, no Euler).
Archimedean symbol m_Q(tau) = 2 Re psi(1/2+i tau) + 2 log(sqrt|D|/2pi); comb v_n = 2 Lambda_f(n)/sqrt n from -f'/f, f = Z_Q/r(1).
Family span: c * a(m) m^{-1/2} on m<=eta M, free on (eta M, M]; lattice log m, m<=M.  Gram-normalised minima."""
import sys, numpy as np, scipy.linalg as sl
import profile as prof
from scipy.special import digamma
T0=0.3; eta=float(sys.argv[1]); Ms=[int(t) for t in sys.argv[2].split(',')]; which=sys.argv[3]
D={'Qi':4,'Q5':20}[which]; A5={'Qi':1,'Q5':5}[which]
prof.m_arch=lambda tau: 2*digamma(0.5+1j*tau).real+2*np.log(np.sqrt(D)/(2*np.pi))
from profile import Profile
from am import AM
P=Profile(T0,1.0)
def coeffs(N):
    r=np.zeros(N+1); L=int(np.sqrt(N))+1
    for x in range(-L,L+1):
        for y in range(-L,L+1):
            v=x*x+A5*y*y
            if 0<v<=N: r[v]+=1
    a=r/r[1]; lam=np.zeros(N+1)
    for n in range(2,N+1):
        s=a[n]*np.log(n)
        for d in range(2,n):
            if n%d==0: s-=lam[d]*a[n//d]
        lam[n]=s
    return a,lam
for M in Ms:
    X=int(M*np.exp(2*T0))+2; a,lam=coeffs(X)
    pos=np.log(np.arange(2,X+1)); w=2*lam[2:]/np.sqrt(np.arange(2,X+1)); keep=np.abs(w)>1e-14; pos,w=pos[keep],w[keep]
    m=np.arange(1,M+1).astype(float); x=np.log(m); Am=AM(P,x,pos,w); A=Am.A; G=Am.Gram
    k=int(eta*M); B=np.zeros((M,M-k+1)); B[:k,0]=a[1:k+1]*m[:k]**-0.5
    for j in range(k,M): B[j,j-k+1]=m[j]**-0.5
    Gs=B.T@G@B; fam=sl.eigh(B.T@A@B,Gs+1e-10*np.trace(Gs)/len(Gs)*np.eye(len(Gs)),eigvals_only=True)[0]
    full=sl.eigh(A,G+1e-10*np.trace(G)/M*np.eye(M),eigvals_only=True)[0]
    u=B[:,0]; print(f"{which} eta={eta} M={M} full={full:.3e} family={fam:.3e} bulk Q(u)/|F_u|^2={u@A@u/(u@G@u):.3e}",flush=True)
