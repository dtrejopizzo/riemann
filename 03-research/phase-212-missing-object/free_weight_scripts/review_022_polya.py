# Control de ROUND_022_A Obs. 1.1 (revisión 022-027): K_Po de P46 thm:K frente a S_zeta g_0.
# (1) cociente puntual K_P46 / S_zeta g_0 en tres t; (2) Mellin en la recta crítica, usando paridad:
#     Phi(1/2+iz) = 2 int_0^inf S_zeta g_0(t) cos(z t) dt, comparado con xi(1/2+iz).
from mpmath import mp, mpf, exp, pi, quad, gamma, zeta, mpc, cos, log
mp.dps = 25
def g0(t): return (2*pi**2*exp(9*t/2) - 3*pi*exp(5*t/2))*exp(-pi*exp(2*t))
def Szg0(t): return sum(n**mpf(-0.5)*g0(t+log(n)) for n in range(1,40))
def KP46(t): return sum((4*pi**2*n**4*exp(9*t/2)-6*pi*n**2*exp(5*t/2))*exp(-pi*n**2*exp(2*t)) for n in range(1,40))
for t in [mpf(-0.7), mpf(0), mpf(0.4)]:
    print('t=',t,' K_P46/S_zeta g0 =', KP46(t)/Szg0(t))
xi = lambda s: s*(s-1)/2*pi**(-s/2)*gamma(s/2)*zeta(s)
for z in [0, 3, 10]:
    M = 2*quad(lambda t: Szg0(t)*cos(z*t), [0,0.5,1,1.5,2.5])
    print('z=',z,' Phi_{S g0}(1/2+iz)/xi(1/2+iz) =', M/xi(mpc(0.5,z)))
