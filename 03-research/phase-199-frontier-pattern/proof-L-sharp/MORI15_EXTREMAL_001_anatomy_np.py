# double-precision anatomy of the archimedean part on g*: Arch = (ψ(¼)−logπ)‖g‖² + ∫_0^∞ [c(0)−c(v)] 2ν(v) dv, ν=e^{-v/2}/(1−e^{-2v})
import json,os,sys,numpy as np
from numpy.polynomial import legendre as Lg
import mpmath as mp
digamma=lambda z: float(mp.digamma(z))
D=os.environ['SP']+'/mori15'; p=int(sys.argv[1])
E=json.load(open(f'{D}/p{p}_eig.json')); v=np.array([float(x) for x in E['vectors'][0]])
N=1664; L=0.5*np.log(15); I=np.arange(p,N,2)
coef=np.zeros(N); coef[I]=v*np.sqrt((2*I+1)/(2*L))
# g on a fine grid; correlation via Gauss-Legendre in x for each lag (exact enough in double)
xg,wg=np.polynomial.legendre.leggauss(1200)
def corr(a):
    lo,hi=-L,L-a
    if hi<=lo: return 0.0
    x=(hi+lo)/2+(hi-lo)/2*xg; return np.sum(wg*Lg.legval(x/L,coef)*Lg.legval((x+a)/L,coef))*(hi-lo)/2
c0=corr(0.0)
nu=lambda v: np.exp(-v/2)/(1-np.exp(-2*v))
# Lévy interior: ∫_0^{2L}[c0−c(v)]2ν(v)dv  (integrand ~ v near 0: fine)
vv=np.linspace(1e-6,2*L,6000); lev_int=np.trapezoid([(c0-corr(a))*2*nu(a) for a in vv],vv)
# exterior: c0 ∫_{2L}^∞ 2ν
vv2=np.linspace(2*L,60,20000); lev_ext=c0*np.trapezoid(2*nu(vv2),vv2)
b_inf=digamma(0.25)-np.log(np.pi)
print('b_inf=psi(1/4)-log pi =',b_inf,' ‖g‖²=',c0)
print('Levy interior [0,2L] =',lev_int,' Levy exterior (v>2L) =',lev_ext,' Levy total =',lev_int+lev_ext)
print('Arch (x-domain) =',b_inf*c0+lev_int+lev_ext)
# Gaussian fit of g: width
x=np.linspace(-L,L,2001); g=Lg.legval(x/L,coef)
m=np.trapezoid(g,x); m2=np.trapezoid(g*x**2,x)/m; print('mass ∫g=',m,' <x²>=',m2,' sigma=',np.sqrt(m2))
# log-derivative check: is g ≈ Gaussian? print g(x)/g(0) vs exp(-x²/2σ²) at some x
for xx in [0.1,0.2,0.3,0.5,0.7,0.9,1.1,1.3]:
    print(f'x={xx}: g/g0={Lg.legval(xx/L,coef)/g[1000]:.6e}  gauss={np.exp(-xx**2/(2*m2)):.6e}')
# Fourier transform magnitude profile
for t in [0,2,4,6,8,10,12,14,16,20,25,30]:
    Ft=np.trapezoid(g*np.cos(x*t),x); print(f'Fg({t})={Ft:+.6e}')
