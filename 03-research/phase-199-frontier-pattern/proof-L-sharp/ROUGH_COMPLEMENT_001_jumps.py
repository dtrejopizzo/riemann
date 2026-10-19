# ROUGH_COMPLEMENT_001 step 1b (double; δ coefficients are O(1e-36) exact to ~16 digits): spatial localization of δ = g* − g*_50
# against the jump points x_n = ±log(λ/n) of the Möbius image E f (jump of Ef at x_n is e^{x_n/2} f(λ) when f(λ) ≠ 0).
import pickle,os,numpy as np
from numpy.polynomial import legendre as Lg
SP=os.environ['SP']; P=pickle.load(open(f'{SP}/rc/pvecs.pkl','rb'))['pvecs']
mu=15; L=np.log(mu)/2; lam=np.sqrt(mu); N=1664; I=np.arange(0,N,2)
dv=np.array([float(x) for x in P['delta']])
c=np.zeros(N); c[I]=dv*np.sqrt((2*I+1)/(2*L))
xx=np.linspace(0,L,200001); dd=Lg.legval(xx/L,c); tot=np.trapezoid(dd**2,xx)
xn=[np.log(lam/n) for n in range(1,16) if abs(np.log(lam/n))<=L+1e-12]
print('jump points |x_n|/T:',[round(abs(x)/L,4) for x in xn])
for w in (0.01,0.02,0.05):
    m=np.zeros_like(xx,bool)
    for x in xn: m|=np.abs(xx-abs(x))<w*L
    print(f'window ±{w}T around jump points: measure frac {m.mean():.3f}, δ² mass frac {np.trapezoid(np.where(m,dd**2,0),xx)/tot:.3f}')
# Gibbs signature: δ's local amplitude vs distance to nearest jump
dist=np.min([np.abs(xx-abs(x)) for x in xn],axis=0)
for a,b in [(0,0.002),(0.002,0.01),(0.01,0.03),(0.03,0.1),(0.1,1)]:
    m=(dist>=a*L)&(dist<b*L); print(f'dist∈[{a},{b})T: rms δ = {np.sqrt(np.mean(dd[m]**2)):.3e}, mass frac {np.trapezoid(np.where(m,dd**2,0),xx)/tot:.3f}')
# jumps of g*: estimate e^{x_n/2} f*(λ) magnitude
fst=-7.21938619188580e-35
print('expected jump size e^{x_n/2}|f*(λ)| range:',[f'{np.exp(x/2)*abs(fst):.2e}' for x in xn[:4]],' rms δ overall',np.sqrt(tot/L))
