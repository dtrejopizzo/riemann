# R155.049 DIAGNOSTIC: sup_tau |2 ghat0(tau) - T_d(tau)| / d  vs  (4/pi) cosh T
import numpy as np
def ghat0(xi, T):
    # 2*int_0^{2T} cosh(u/2) cos(xi u) du  = 4*[ .5*sinh T*cos(2T xi) + xi*cosh T*sin(2T xi) ]/(xi^2+1/4)
    return 4*(0.5*np.sinh(T)*np.cos(2*T*xi) + xi*np.cosh(T)*np.sin(2*T*xi))/(xi**2+0.25)
for T in (0.5*np.log(3), np.log(2)):
    for M in (16,64,256,1024):
        d = 2*T/M; P = 2*np.pi/d
        j = np.arange(-M, M+1); kap = np.ones_like(j, dtype=float); kap[0]=kap[-1]=0.5
        nodes = j*d; h = 2*np.cosh(nodes/2)
        tau = np.linspace(0, P/2, 20000)
        Td = d*(kap*h) @ np.cos(np.outer(nodes, tau))
        err = np.max(np.abs(ghat0(tau,T) - Td))
        # plain (no endpoint correction): kappa=1 at +-M
        kap2 = np.ones_like(j, dtype=float)
        Td2 = d*(kap2*h) @ np.cos(np.outer(nodes, tau))
        err2 = np.max(np.abs(ghat0(tau,T) - Td2))
        print(f"T={T:.6f} M={M:5d} corr={err/d:.4f} plain={err2/d:.4f} "
              f"(4/pi)coshT={4/np.pi*np.cosh(T):.4f} (2+4/pi)coshT={(2+4/np.pi)*np.cosh(T):.4f}")
