import numpy as np, time
from profile import Profile
from am import *
P = Profile(0.3, 1.0)
M = 300
pos, w, ns = lambda_comb(int(M*np.exp(2*P.T0))+2)
t=time.time(); A = AM(P, np.log(np.arange(1, M+1)), pos, w); print('build', time.time()-t)
s = A.summary(); print({k: v for k, v in s.items() if k not in ('vec','lam')})
# independent check: B(d) from grid-interpolated X(d)  (comb part on the FFT grid)
d = A.x[:,None]-A.x[None,:]
X = np.zeros_like(d)
for xa, wa in zip(pos, w):
    X += 0.5*wa*(P.c0(xa - d) + P.c0(xa + d))
B = A.Arch - X
print('max |A - (Arch - X)| =', np.abs(A.A - B).max(), ' max|A|=', np.abs(A.A).max())
# quadratic form check via prop:AM(ii) spectral integral for a random vector
rng = np.random.default_rng(1); s_ = rng.normal(size=M)
tau = P.h*np.arange(P.N); 
from profile import m_arch
V = np.zeros(P.N)
for xa, wa in zip(pos, w):
    if xa < np.log(M)+2*P.T0: V += wa*np.cos(tau*xa)
Ps = np.zeros(P.N, complex)
for mm in range(M): Ps += s_[mm]*np.exp(1j*tau*np.log(mm+1))
F2 = P.Fhat_grid**2
f = F2*np.abs(Ps)**2*(m_arch(tau) - V); f[0]*=0.5
q = (P.h/np.pi)*f.sum()
print('spectral integral', q, ' matrix form', s_@A.A@s_)
print('Div symmetric check', np.abs(A.Div-A.Div.T).max(), 'Near diag', np.abs(np.diag(A.Near)).max())
