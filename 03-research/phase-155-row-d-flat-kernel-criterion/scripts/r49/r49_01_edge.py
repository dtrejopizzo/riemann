import numpy as np
def g0hat(tau,T):  # 2*int_0^{2T} cosh(u/2) cos(tau u) du
    b=0.5;a=2*T
    return 2*(b*np.sinh(b*a)*np.cos(tau*a)+tau*np.cosh(b*a)*np.sin(tau*a))/(b*b+tau*tau)
for T in [0.5*np.log(3), np.log(2)]:
  print("T=",T,"2cosh T=",2*np.cosh(T))
  for M in [8,16,32,64,128,256]:
    d=2*T/M; P=2*np.pi/d
    j=np.arange(-M+1,M)
    tau=np.linspace(0,P/2,20001)
    DM=d*np.sum(2*np.cosh(j[:,None]*d/2)*np.cos(j[:,None]*d*tau[None,:]),axis=0)
    err=2*g0hat(tau,T)-DM
    Td=err+d*2*np.cosh(T)*2*np.cos(2*T*tau)*0.5*2  # T_d - D_M = d*2coshT*2cos(2T tau)? check below
    print(f"  M={M:4d} d={d:.4f}  sup|2g0-DM|={np.max(abs(err)):.5f}  /d={np.max(abs(err))/d:.4f}  err(0)={err[0]:.5f} 2d coshT={2*d*np.cosh(T):.5f}")

print("half-weight (trapezoid) version")
for T in [0.5*np.log(3), np.log(2)]:
  for M in [16,64,256]:
    d=2*T/M; P=2*np.pi/d
    j=np.arange(-M+1,M); tau=np.linspace(0,P/2,20001)
    DM=d*np.sum(2*np.cosh(j[:,None]*d/2)*np.cos(j[:,None]*d*tau[None,:]),axis=0)
    Td=DM+d*2*np.cosh(T)*np.cos(2*T*tau)
    e=2*g0hat(tau,T)-Td
    print(f"  T={T:.4f} M={M:4d} sup|2g0-Td|/d={np.max(abs(e))/d:.4f}  (4/pi)coshT={4/np.pi*np.cosh(T):.4f}")
