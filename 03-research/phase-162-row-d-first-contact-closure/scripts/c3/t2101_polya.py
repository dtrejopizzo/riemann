# R162_2101: test the xi-radical primitive vector F1=(1/4-d^2/dt^2)Phi_Polya truncated to [-T,T]. UNCERTIFIED float.
import sys,numpy as np, scipy.special as sp
from numpy.polynomial.legendre import leggauss
import t2001_typeI_search as S
def Phi(t,d=0):
    # Phi(t)=sum_n (2pi^2 n^4 e^{9t/2}-3pi n^2 e^{5t/2}) exp(-pi n^2 e^{2t}); numeric 2nd derivative
    def f(t):
        return sum((2*np.pi**2*n**4*np.exp(4.5*t)-3*np.pi*n**2*np.exp(2.5*t))*np.exp(-np.pi*n*n*np.exp(2*t)) for n in range(1,8))
    if d==0: return f(t)
    h=1e-3; return (f(t+h)-2*f(t)+f(t-h))/h**2
def coeffs(T,K,F):
    x,w=leggauss(200); t=T*x
    return np.array([np.sqrt((2*l+1)/(2*T))*T*np.sum(w*sp.eval_legendre(l,x)*F(t)) for l in range(0,K,2)])
K=34
for (T,s2,s3) in [(float(a),float(b),float(c)) for a,b,c in zip(*[iter(sys.argv[1:])]*3)]:
    (A0,A2,A3),ph,P0=S.pieces(T,K); A=A0-s2*A2-s3*A3
    ev,U=np.linalg.eigh(A); U=U*np.sign(P0@U)
    for name,F in [('Phi',lambda t:Phi(t)),('F1',lambda t:0.25*Phi(t)-Phi(t,2))]:
        c=coeffs(T,K,F); n=np.linalg.norm(c); c=c/n
        print(T,s2,s3,name,'rayleigh %.3e'%(c@A@c),'<.,phi^> %+.3e'%(c@ph),'|<.,u2>| %.6f'%abs(c@U[:,1]),'mu2 %.2e'%ev[1],'<u2,phi^> %+.2e'%(U[:,1]@ph))
