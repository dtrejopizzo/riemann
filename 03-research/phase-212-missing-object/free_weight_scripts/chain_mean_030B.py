# Ronda 030 B: m(tau)=Re psi(1/4+i tau/2)-log pi; medias de m sobre [0, pi/log n] y raiz de m.
from mpmath import mp, psi, log, pi, quad, findroot, mpc, re
mp.dps=20
m=lambda t: re(psi(0,mpc(0.25,t/2)))-log(pi)
print("m(0)",m(0)); print("root",findroot(m,6.3))
for t in [2,4,4.532,6,6.7,8]: print("m",t,m(t))
for n in [2,3,4,5]:
    L=pi/log(n); print("n",n,"L",L,"mean",quad(m,[0,L])/L)
# chequeo: m(t)=C0+int_0^inf (1-cos ut)K(u)du en t=3
K=lambda u: 1/(2*mp.sinh(u/2))+1/(2*mp.cosh(u/2))
print("check",m(3), m(0)+quad(lambda u:(1-mp.cos(3*u))*K(u),[0,1,10,mp.inf]))
