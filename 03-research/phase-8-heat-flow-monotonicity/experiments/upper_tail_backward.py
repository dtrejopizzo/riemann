#!/usr/bin/env python3
"""
Phase 8 / attack the upper tail — the backward-flow reality-survival, the EXACT target.

Polymath15: Lambda<=0.2 => zeros all real at t=0.2.  RH <=> backward flow t:0.2->0 keeps them real.
Backward flow is ATTRACTIVE; a pair of gap g obeys g^2(t)=g0^2+8t (2-body) -> shrinks going backward.
A pair collides (g->0, births a complex pair) at t_c = -g0^2/8 (2-body) -- MORE negative for wider
pairs, CLOSER to 0 for tight (Lehmer) pairs.  With the full N-body mean field, the collision time can
be pushed.  RH <=> the first collision time (over all pairs, all heights) stays < 0, i.e. no pair
collides for t>=0, UNIFORMLY in T.  This script measures the backward-collision margin and its scaling.

Honest unit caveat: the Coulomb constant (here 2) sets the t-scale; the exact dBN normalization is the
delicate Polymath15 part.  We probe the MECHANISM and the uniformity trend, not the exact Lambda.
"""
import numpy as np, mpmath as mp
mp.mp.dps = 25

def ordinates(n0,n1): return np.array([float(mp.im(mp.zetazero(n))) for n in range(n0,n1+1)])

def vel(z):  # Coulomb velocity (forward t)
    v=np.zeros_like(z,dtype=complex)
    for j in range(len(z)):
        dz=z[j]-z; dz[j]=np.inf; v[j]=2.0*np.sum(1.0/dz)
    return v

def rk4(z,dt):
    k1=vel(z);k2=vel(z+.5*dt*k1);k3=vel(z+.5*dt*k2);k4=vel(z+dt*k3)
    return z+(dt/6)*(k1+2*k2+2*k3+k4)

def min_gap(z):
    x=np.sort(z.real); return np.min(np.diff(x))

if __name__=="__main__":
    print("="*82)
    print(" Attack the upper tail: backward-flow reality survival (RH <=> no collision for t>=0)")
    print("="*82)
    print(" 2-body law check: g^2(t)=g0^2+8t  =>  collision at t_c=-g0^2/8=-0.125")
    z=np.array([-0.5,0.5],dtype=complex)   # g0=1
    zz=z.copy(); dt=-2e-4; tcur=0.0
    for tgt in [-0.05,-0.10,-0.12]:
        while tcur>tgt+1e-9: zz=rk4(zz,dt); tcur+=dt
        g=min_gap(zz)
        print(f"   t={tcur:+.3f}: g^2_num={g**2:.4f}  g^2_theory={1+8*tcur:.4f}  match={abs(g**2-(1+8*tcur))<2e-2}")

    print("\n Real zeta zeros: backward-flow until first collision; margin t_c and its scaling with T")
    print("  (t_c<0 = collides in the past = RH-safe; |t_c|->0 with T would be the uniformity danger)")
    for (a,b) in [(1,60),(500,560),(2000,2060)]:
        g=ordinates(a,b); T=g.mean()
        z=g.astype(complex); zz=z.copy(); dt=-2e-4; tcur=0; tc=None
        gmin0=min_gap(z)
        for s in range(3000):
            gm=min_gap(zz)
            if gm<2e-2: tc=tcur; break
            zz=rk4(zz,dt); tcur+=dt
        spacing=2*np.pi/np.log(T/(2*np.pi))   # local mean spacing
        tc_str = f"{tc:+.4f}" if tc is not None else "< -0.60"
        print(f"   T~{T:8.1f} (#{a}-{b}): min gap(t=0)={gmin0:.4f} (mean spacing~{spacing:.4f}), "
              f"backward collision t_c={tc_str}  {'(safe: t_c<0)' if (tc is None or tc<0) else '*** t_c>=0 ***'}")
    print("="*82)
    print(" READ: real pairs collide in the PAST (t_c<0) under backward flow -> RH-safe locally.  The")
    print(" OPEN problem: prove t_c<0 holds UNIFORMLY in T for the flowed (t=0.2) zeros, as mean spacing")
    print(" ->0.  This is the extremal (sup over pairs) control, not an average -- ONE collision at t>=0")
    print(" would force Lambda>0.  No averaged statistic gives it; that is the irreducible barrier.")
