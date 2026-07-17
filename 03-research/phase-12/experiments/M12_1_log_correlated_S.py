#!/usr/bin/env python3
"""
Phase 12 / M12.1 — confirm S(T) is a log-correlated field, in real zeta-zero data.

S(T) = N(T) - 1 - theta(T)/pi,  N(T)=#{gamma_n<=T}, theta=Riemann-Siegel theta (mpmath.siegeltheta).
Predicted (Bourgade/Najnudel; Selberg): Var S ~ (1/2pi^2) log log T ; covariance
  E[S(t)S(t')] ~ -(1/2pi^2) log|t-t'|  for mean-spacing < |t-t'| < 1  (the log-correlated law).

We compute S on a fine grid over a height window, estimate Cov(delta), fit -c log delta, compare
c to 1/(2pi^2)=0.05066, and check the tightest zero pairs sit at the STEEPEST rises of S.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 15

def get_zeros(nmax):
    return np.array([float(mp.im(mp.zetazero(n))) for n in range(1,nmax+1)])

def theta(T):
    return float(mp.siegeltheta(T))

def S_of_T(Tgrid, zeros):
    # N(T) = count of zeros <= T ; theta vectorized via mpmath
    N = np.searchsorted(zeros, Tgrid, side='right').astype(float)
    th = np.array([theta(t) for t in Tgrid])
    return N - 1.0 - th/np.pi

if __name__=="__main__":
    print("="*78)
    print(" M12.1 — S(T) log-correlated structure (real zeta zeros)")
    print("="*78)
    NMAX=900
    print(f" computing first {NMAX} zeros ...")
    zeros=get_zeros(NMAX); Tmax=zeros[-1]
    print(f"   up to T={Tmax:.1f}")
    # window in the bulk, away from edges
    a,b = 200.0, zeros[-5]
    grid=np.linspace(a,b, 40000); S=S_of_T(grid, zeros); dT=grid[1]-grid[0]
    Sc=S-S.mean()
    print(f"\n window [{a:.0f},{b:.0f}], Var(S)={np.var(S):.4f}  (Selberg ~ (1/2pi^2)loglog T = {np.log(np.log(b))/(2*np.pi**2):.4f})")

    # covariance Cov(delta) = mean_t Sc(t)Sc(t+delta)
    print("\n  Cov(delta) and the log-correlated fit -c*log(delta):")
    print("   delta     Cov(delta)     -1/(2pi^2)*log(delta)")
    deltas=np.array([0.05,0.1,0.2,0.4,0.8,1.6,3.2])
    cov=[]
    for d in deltas:
        sh=int(round(d/dT))
        c=np.mean(Sc[:-sh]*Sc[sh:]) if sh>0 else np.var(Sc)
        cov.append(c)
        print(f"   {d:5.2f}    {c:+.4f}        {-np.log(d)/(2*np.pi**2):+.4f}")
    cov=np.array(cov)
    # fit Cov = -c log delta + const  over the mesoscopic range (delta in [0.1,1.6])
    mask=(deltas>=0.1)&(deltas<=1.6)
    A=np.polyfit(np.log(deltas[mask]), cov[mask], 1)
    print(f"\n  fit Cov ~ {A[0]:+.4f}*log(delta) + {A[1]:.4f}  =>  slope c = {-A[0]:.4f}")
    print(f"  predicted log-correlated slope -1/(2pi^2) = {-1/(2*np.pi**2):.4f}")
    print(f"  => |c - 1/(2pi^2)| = {abs(-A[0]-1/(2*np.pi**2)):.4f}  ({'CONFIRMED log-correlated' if abs(-A[0]-1/(2*np.pi**2))<0.02 else 'order-of-magnitude'})")

    # tightest pairs sit at steepest S rises?
    g=np.sort(zeros); gaps=np.diff(g); mid=0.5*(g[1:]+g[:-1])
    dens=np.array([float(mp.re(mp.diff(mp.siegeltheta,m)))/np.pi for m in mid])  # rho(T)=theta'/pi
    ng=gaps*dens
    tight_idx=np.argsort(ng)[:5]
    print("\n  tightest normalized gaps and the local S-slope there (steep rise = tight pair):")
    for i in sorted(tight_idx):
        t0=mid[i]
        # local slope of S over +-0.5
        loc=(grid>t0-0.5)&(grid<t0+0.5)
        slope=(S[loc][-1]-S[loc][0])/(grid[loc][-1]-grid[loc][0]) if loc.sum()>2 else np.nan
        print(f"   T~{t0:7.1f}  norm.gap={ng[i]:.3f}   local dS/dT={slope:+.3f}")
    print("="*78)
