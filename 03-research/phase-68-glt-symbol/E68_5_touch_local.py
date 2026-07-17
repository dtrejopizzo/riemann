"""
E68.5 -- local structure of the touch point theta* and gauge-dependence of the margin.

Omega_7 concentrates near theta ~ pi/2 (E68.4). Characterize:
  (1) theta*(gauge), sigma_min(gauge), local curvature of sigma = sigma_A - sigma_P for zeta;
  (2) how sigma_min depends on the HEIGHT t0 -- the uniformity crux of Omega_7 (delta_N >= 0 must hold
      uniformly in the gauge). Does sigma_min stay bounded > 0, or squeeze to 0 as t0 grows?
  (3) the off-line dip vs beta (distance off the line).
"""
import os, sys
import numpy as np
import mpmath as mp

H8 = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../04-papers/P52-riemann-proof-audit"))
sys.path.insert(0, H8)
import h8lab as H
mp.mp.dps = 40

def mp2np(M):
    return np.array([[complex(M[i,j]) for j in range(M.cols)] for i in range(M.rows)], dtype=complex)

def planted(z0, rho):
    s0=mp.mpf(1)/2+mp.mpc(0,1)*z0; r,rc=rho,1-rho
    def g(j,s): return {0:(s-r)*(s-rc),1:(s-r)+(s-rc),2:mp.mpf(2)}.get(j,mp.mpf(0))
    return lambda k: sum(mp.binomial(k,j)*mp.zeta(s0,1,j)*g(k-j,s0) for j in range(k+1))

def sym(M, th):
    N=M.shape[0]; s=np.zeros(len(th),dtype=complex)
    for d in range(-(N-1),N):
        s+=np.mean([M[j,j+d] for j in range(max(0,-d),min(N,N-d))])*np.exp(1j*d*th)
    return np.real(s)

def gap(t0,y,N,xd):
    z0=mp.mpc(mp.mpf(str(t0)),-mp.mpf(str(y)))
    A_N,Plam,_=H.arithmetic_jets(z0,N,xd)
    th=np.linspace(-np.pi,np.pi,4000)
    g=sym(mp2np(H.herm(A_N)),th)-sym(mp2np(H.herm(Plam)),th)
    return th,g

def main():
    N=14
    print("(1)-(2) zeta: touch point and margin vs HEIGHT t0 (y=1):")
    print("   t0     theta*     sigma_min   curvature(2a)")
    for t0 in (30,50,100,200,400):
        th,g=gap(t0,1.0,N,None)
        i=int(np.argmin(g)); th0=th[i]
        win=np.abs(th-th0)<0.3
        c=np.polyfit(th[win]-th0,g[win],2)
        print(f"  {t0:4d}   {th0:+.4f}    {g[i]:+.5f}     {2*c[0]:+.4f}")
    print("   => if sigma_min stays > 0 and ~const: uniform margin (big). if -> 0: the squeeze.")

    print("\n(3) off-line dip vs beta (t0=100, y=1):")
    print("   beta    sigma_min     (depth of the violation)")
    for beta in (0.55,0.65,0.80,0.95):
        z0=mp.mpc(mp.mpf('100'),-mp.mpf('1'))
        th,g=gap(100,1.0,N,planted(z0,mp.mpf(str(beta))+mp.mpc(0,1)*mp.mpf('100')))
        print(f"   {beta:.2f}   {g.min():+.3f}")
    print("\n(varying y at t0=100):")
    print("   y      sigma_min")
    for yy in (0.5,1.0,2.0,4.0):
        th,g=gap(100,yy,N,None)
        print(f"   {yy:.1f}    {g.min():+.5f}")

if __name__ == "__main__":
    main()
