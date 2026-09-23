import sys, math, numpy as np
sys.path.insert(0,'../round4')
import r4core as C4, r5core as C5
from scipy.integrate import quad
T=0.58
tt=np.array([0.0,0.3,1.7,7.3,33.0,137.0,500.0])
print("g0h diff", np.max(np.abs(C5.g0h(tt,T)-C4.g0h(tt,T))))
print("g1h diff", np.max(np.abs(C5.g1h(tt,T)-C4.g1h(tt,T))))
for t in [0.0,1.7,33.0]:
    q0=quad(lambda u: math.cosh(u/2)*math.cos(u*t),-2*T,2*T,limit=200)[0]
    q1=quad(lambda u: u*math.sinh(u/2)*math.cos(u*t),-2*T,2*T,limit=200)[0]
    d0=quad(lambda u: -u*math.cosh(u/2)*math.sin(u*t),-2*T,2*T,limit=200)[0]
    d1=quad(lambda u: -u*u*math.sinh(u/2)*math.sin(u*t),-2*T,2*T,limit=200)[0]
    print(t, abs(C5.g0h(np.array([t]),T)[0]-q0), abs(C5.g1h(np.array([t]),T)[0]-q1),
          abs(C5.g0hp(np.array([t]),T)[0]-d0), abs(C5.g1hp(np.array([t]),T)[0]-d1))
# derivative of nuhat and f by finite differences
rng=np.random.default_rng(0)
us=np.arange(24,200)*(2*T/24); a=rng.normal(0,0.1,len(us))
h=1e-6
for t in [0.5, 5.0, 40.0]:
    x=np.array([t-h,t+h])
    print("nuhatp",abs(C5.nuhatp(np.array([t]),us,a)[0]-(C5.nuhat(x,us,a)[1]-C5.nuhat(x,us,a)[0])/(2*h)))
# H0,H1 vs quad
print("H0",abs(C5.H0(T)-quad(lambda u:u*u*math.cosh(u/2),-2*T,2*T)[0]))
print("H1",abs(C5.H1(T)-quad(lambda u:abs(u)**3*math.sinh(abs(u)/2),-2*T,2*T)[0]))
print("G0",abs(C5.G0(T)-quad(lambda u:abs(u)*math.cosh(u/2),-2*T,2*T)[0]))
