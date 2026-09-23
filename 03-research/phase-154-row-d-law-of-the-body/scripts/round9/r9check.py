"""Round 9 sanity checks (seconds): column transforms, the Levy identity for m, monotonicity."""
import math, sys
import numpy as np
from scipy.integrate import quad
sys.path.insert(0, '../round5')
import r5core as C
import r9tail as R9

T = 0.58; twoT = 2*T
print("== column transform vs quadrature ==")
for s, k in [(0.05,0),(0.5,0),(3.0,0),(50.0,0),(0.5,1),(2.0,2)]:
    for tau in [0.0, 1.3, 17.0, 59.5, 300.0]:
        U = 200/s
        g = lambda t: (t**k)*math.exp(-s*t)
        ic = quad(g, 0, U, weight='cos', wvar=tau, limit=900)[0] if tau else quad(g,0,U,limit=900)[0]
        isn = quad(g, 0, U, weight='sin', wvar=tau, limit=900)[0] if tau else 0.0
        num = math.cos(tau*twoT)*ic - math.sin(tau*twoT)*isn
        ex = float(R9.nuhat_col(tau, T, s, k))
        cap = float(R9.tailcap(tau, s, k))
        assert abs(num-ex) < 1e-7*max(1,abs(ex))+1e-8, (s,k,tau,num,ex)
        assert abs(ex) <= cap*(1+1e-12)
    print(f"  s={s:6.2f} k={k}  OK   TV={math.factorial(k)/s**(k+1):.4g}")

print("== derivative check ==")
for s,k in [(0.5,0),(2.0,1)]:
    t=7.3; h=1e-6
    fd=(R9.nuhat_col(t+h,T,s,k)-R9.nuhat_col(t-h,T,s,k))/(2*h)
    print(f"  s={s} k={k}: exact {float(R9.nuhat_col_p(t,T,s,k)):.10f} fd {float(fd):.10f}")

print("== Levy identity  m(tau) = m(0) + int_0^oo (1-cos tau u) K(u) du ==")
K = lambda u: 0.5/math.sinh(u/2) + 0.5/math.cosh(u/2)
m0 = float(C.m(0.0))
for tau in [0.7, 3.0, 17.0, 59.544]:
    I = quad(lambda u: (1-math.cos(tau*u))*K(u), 0, 60, limit=900)[0]
    print(f"  tau={tau:8.3f}  m={float(C.m(tau)):.10f}  m0+I={m0+I:.10f}")
print("  m(0) =", m0)
cK = quad(K, twoT, 80, limit=900)[0]
print(f"  c_K = int_{{2T}}^oo K = {cK:.10f}   (T={T});  K(u)/(2e^(-u/2)) at u=6: {K(6.0)/(2*math.exp(-3)):.6f}")

print("== archimedean floor: m(tau) >= log(tau/2)-log pi-1/(12.5 tau^2) on [2,1e6] ==")
tt = np.exp(np.linspace(math.log(2), math.log(1e6), 200000))
print("  min margin:", float(np.min(C.m(tt) - (np.log(tt/2)-math.log(math.pi)-1/(12.5*tt**2)))))

print("== Sv, tau1 flat solution ==")
v = C.vdict(T); Sv = sum(v.values()); print("  v:", v, " Sv=", Sv)
for extra in [0.0, 0.1, 0.5, 1.0, 2.0]:
    lo, hi = 2.0, 1e7
    for _ in range(200):
        mid=(lo+hi)/2
        if float(R9.L_floor(mid,T,Sv)) - extra >= 0: hi=mid
        else: lo=mid
    print(f"  extra budget {extra:4.2f}  ->  tau1 = {hi:.4f}")
