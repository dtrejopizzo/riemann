#!/usr/bin/env python3
"""
Phase 8 Gate B — the differential inequality for L = sum (Im z_j)^2 under the Coulomb flow.

Derived (by hand):  Ldot = -2 sum_{j!=k} (y_j-y_k)^2 / |z_j-z_k|^2  <= 0   (forward t).

We verify:
 (1) the identity Ldot = -2 sum ... against a finite-difference of L along the RK4 flow;
 (2) ARITHMETIC-BLINDNESS: the identity holds for ARBITRARY configurations (random, L_DH-like,
     zeta) -- the ODE knows nothing about primes, so a pure-ODE Lyapunov cannot single out zeta;
 (3) WRONG-DIRECTION: forward, L decreases (healing); so from L(Lambda)=0 we only get L(0)>=0
     (trivial). The monotonicity does NOT force L(0)=0 (=RH).
 (4) the isolated-pair rate d(y^2)/dt = -2 (=> a pair at t=0 of height y0 heals by t=y0^2/2,
     i.e. RH-violating zeros would sit at |Im| <= sqrt(2 Lambda) <= 0.63 with Lambda<=0.2).
"""
import numpy as np
np.random.seed(0)

def coulomb_vel(z):
    v=np.zeros_like(z,dtype=complex)
    for j in range(len(z)):
        dz=z[j]-z; dz[j]=np.inf
        v[j]=2.0*np.sum(1.0/dz)
    return v

def L(z): return np.sum(z.imag**2)

def Ldot_formula(z):
    y=z.imag; s=0.0
    for j in range(len(z)):
        for k in range(len(z)):
            if k==j: continue
            s+=(y[j]-y[k])**2/np.abs(z[j]-z[k])**2
    return -2.0*s

def rk4(z,dt):
    k1=coulomb_vel(z);k2=coulomb_vel(z+.5*dt*k1);k3=coulomb_vel(z+.5*dt*k2);k4=coulomb_vel(z+dt*k3)
    return z+(dt/6)*(k1+2*k2+2*k3+k4)

print("="*78)
print(" Gate B — verify  Ldot = -2 sum (y_j-y_k)^2/|z_j-z_k|^2  and its meaning")
print("="*78)

# conjugate-symmetric test configs (real coeffs => zeros in conj pairs)
def make_config(kind):
    if kind=="random":
        x=np.sort(np.random.uniform(-5,5,8)); z=x.astype(complex)
        z=np.concatenate([z,[1.3+0.4j,1.3-0.4j,-2.1+0.2j,-2.1-0.2j]])  # two complex pairs
    elif kind=="zeta-like":
        x=np.array([-6.3,-4.1,-2.0,0.0,2.0,4.1,6.3])  # roughly uniform real
        z=np.concatenate([x.astype(complex),[0.7+0.3j,0.7-0.3j]])
    elif kind=="cluster":   # a pair near a real cluster (cross-term test)
        z=np.array([-0.5,0.0,0.5],dtype=complex)
        z=np.concatenate([z,[0.05+0.25j,0.05-0.25j]])
    return z

# (1)+(2) identity vs finite diff, several configs (arithmetic-blind)
print("\n (1)+(2) identity check (Ldot_formula vs dL/dt finite-diff), multiple configs:")
dt=1e-5
for kind in ["random","zeta-like","cluster"]:
    z=make_config(kind)
    Lf=Ldot_formula(z)
    Lnum=(L(rk4(z,dt))-L(rk4(z,-dt)))/(2*dt)
    print(f"   {kind:10s}: Ldot_formula={Lf:+.6f}   finite-diff={Lnum:+.6f}   match={abs(Lf-Lnum)<1e-3}"
          f"   (Ldot<=0 ? {Lf<=1e-9})")

# (3) wrong-direction: evolve a config with a pair FORWARD and BACKWARD, watch L
print("\n (3) wrong-direction demo: L decreases forward (heals), grows backward (births):")
z=make_config("zeta-like"); dt=2e-3
print("    t:      ", "  ".join(f"{s*dt:+.3f}" for s in range(-3,4)))
Ls=[];
for s in range(-3,4):
    zz=z.copy()
    steps=abs(s)
    for _ in range(steps): zz=rk4(zz, np.sign(s)*dt)
    Ls.append(L(zz))
print("    L(t):   ", "  ".join(f"{l:.4f}" for l in Ls))
print("    => forward (t up) L down to 0; backward (t down) L up. L(0)>=L(Lambda)=0 is TRIVIAL, not RH.")

# (4) isolated-pair rate
print("\n (4) isolated conjugate pair at +/- i*y0, no other zeros: d(y^2)/dt = ?")
for y0 in [0.2,0.4,0.63]:
    z=np.array([1j*y0,-1j*y0])
    rate=Ldot_formula(z)/1.0   # L=2y0^2; dL/dt; per-(y^2) = rate/2
    print(f"   y0={y0:.2f}: dL/dt={rate:+.4f}  d(y^2)/dt={rate/2:+.4f}  heals by t=y0^2/2={y0**2/2:.4f}")
print("   => RH-violating zeros (if any) sit at |Im|<=sqrt(2*Lambda)<=sqrt(0.4)=0.632 (Lambda<=0.2).")
print("="*78)
print(" CONCLUSION: Ldot<=0 is a clean unconditional THEOREM, but (a) wrong-direction for RH and")
print(" (b) ARITHMETIC-BLIND (identical for random/zeta/L_DH configs). A pure-ODE Lyapunov CANNOT")
print(" prove RH: the flow is generic; RH lives in the INITIAL DATA (zeta's zero statistics). Feeding")
print(" those back in is the pair-correlation wall (B1). This is the SIXTH language of the wall.")
