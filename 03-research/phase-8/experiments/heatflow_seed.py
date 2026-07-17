#!/usr/bin/env python3
"""
Phase 8 seed (Gate A) — couple the de Bruijn-Newman zero dynamics to our Carleson constant.

We use the identity  C = 1 - lambda_min(Z, A_Phi),  Z = sum_rho v_rho v_rho^T (zero-side Gram,
v_rho[j]=S_j(z_rho)), A_Phi the archimedean Gram.  So C is driven DIRECTLY by the zeros z_rho(t),
which move under the (local) Coulomb-gas flow of the de Bruijn-Newman heat evolution:

    zdot_j = 2 * sum_{k!=j} 1/(z_j - z_k)        (forward t: increasing, the all-real regime t>=Lambda)

Questions:
 (A) real zeros: is C<=1, and what is the sign of dC/dt along the forward flow? (Gate A)
 (B) THE ATTRACTOR: inject an off-line pair tau +/- i*delta -> C>1; evolve forward -> does delta
     shrink (zeros heal onto the line) and C drop back to <=1?  (the rigorous 'critical line is the
     attractor' mechanism the heat flow gives, replacing the hand-wavy PT-symmetry intuition.)

Honest: this is the LOCAL finite Coulomb model (windowed sum), not the exact dBN flow (which has a
smooth background from the infinitely many zeros). It is a Gate-A probe of the mechanism, not a proof.
"""
import numpy as np, mpmath as mp
import sys; sys.path.insert(0, "../../phase-7/experiments")
import carleson_band_engine as e
mp.mp.dps = 22

def zeros_near(T0, halfspan, maxn=2000):
    g=[]; n=1
    while n<=maxn:
        t=float(mp.im(mp.zetazero(n)))
        if t>T0+halfspan: break
        if t>=T0-halfspan: g.append(t)
        n+=1
    return np.array(g)

def Amat(d,T0,N,grid_pts=40000,span=None):
    sp=np.pi/d; centers=T0+sp*np.arange(-N,N+1)
    if span is None: span=(N+50)*sp
    r=np.linspace(T0-span,T0+span,grid_pts); w=r[1]-r[0]
    S=np.sinc(d*(r[None,:]-centers[:,None])/np.pi)
    Phi=e.Phi_vec(r)
    A=(S*w)@(Phi[:,None]*S.T); A=(A+A.T)/2
    return A, centers

def svec(centers,d,z):
    zz=d*(z-centers)/np.pi
    return np.where(np.abs(zz)<1e-12, 1.0+0j, np.sin(np.pi*zz)/(np.pi*zz))

def carleson_from_zeros(zlist, centers, d, A, Ainv_chol):
    """C = 1 - lambda_min(Z, A_Phi).  Z = sum_rho Weil term = sum outer(S(z), conj(S(conj z))),
    Hermitian-symmetrized.  For REAL z this is v v^* (PSD).  For a complex conjugate pair it is the
    INDEFINITE Weil quartet (matches B1 second_order_offline.py) -> can drive C>1."""
    M=len(centers); Z=np.zeros((M,M),complex)
    for z in zlist:
        v=svec(centers,d,z); vc=svec(centers,d,np.conj(z))
        Z=Z+np.outer(v, np.conj(vc))
    Z=(Z+Z.conj().T)/2
    Li=Ainv_chol
    Mm=Li@Z@Li.conj().T; Mm=(Mm+Mm.conj().T)/2
    lammin=np.linalg.eigvalsh(Mm)[0].real
    return 1.0-lammin

def coulomb_vel(z):
    """zdot_j = 2 sum_{k!=j} 1/(z_j-z_k); z complex array."""
    v=np.zeros_like(z,dtype=complex)
    for j in range(len(z)):
        dz=z[j]-z; dz[j]=np.inf
        v[j]=2.0*np.sum(1.0/dz)
    return v

def rk4_step(z, dt):
    k1=coulomb_vel(z); k2=coulomb_vel(z+0.5*dt*k1)
    k3=coulomb_vel(z+0.5*dt*k2); k4=coulomb_vel(z+dt*k3)
    return z+(dt/6.0)*(k1+2*k2+2*k3+k4)

if __name__=="__main__":
    d,T0,N = 1.5, 100.0, 9
    A,centers=Amat(d,T0,N)
    L=np.linalg.cholesky(A); Li=np.linalg.inv(L)
    # include MORE zeros than the basis window to reduce edge effects in the Coulomb sum
    zr=zeros_near(T0, 60.0)
    in_win = np.abs(zr-T0)<N*np.pi/d
    print("="*82)
    print(f" Phase 8 SEED (Gate A): heat-flow zero dynamics x Carleson constant.  d={d} T0={T0}")
    print(f" {len(zr)} zeros in Coulomb window; {in_win.sum()} inside the detector window")
    print("="*82)

    # ---- (A) real zeros: C and dC/dt along forward flow ----
    z=zr.astype(complex)
    C0=carleson_from_zeros(z, centers, d, A, Li)
    dt=2e-4
    Cs=[]
    zz=z.copy()
    for s in range(6):
        Cs.append(carleson_from_zeros(zz, centers, d, A, Li))
        zz=rk4_step(zz, dt)
    Cs=np.array(Cs)
    print(f"\n (A) REAL zeros:  C(t=0) = {C0:.6f}   (<=1 ? {'YES' if C0<=1+1e-9 else 'NO'})")
    print(f"     C along forward flow (dt={dt}):  " + "  ".join(f"{c:.6f}" for c in Cs))
    print(f"     dC/dt ~ {(Cs[1]-Cs[0])/dt:+.4f}   (sign-definite? watch over steps: "
          + ",".join(f"{(Cs[i+1]-Cs[i])/dt:+.3f}" for i in range(len(Cs)-1)) + ")")

    # ---- (B) THE ATTRACTOR: inject off-line pair, evolve forward, watch healing ----
    print(f"\n (B) ATTRACTOR test: inject off-line pair at tau={T0:.1f} +/- i*delta, evolve forward.")
    tau=T0+0.3
    for delta0 in [0.05, 0.15, 0.30]:
        # remove a nearby real zero, add the conjugate pair (mimic a zero leaving the line)
        zc=list(zr.astype(complex))
        jnear=int(np.argmin(np.abs(zr-tau))); zc.pop(jnear)
        zc=np.array(zc+[tau+1j*delta0, tau-1j*delta0])
        Cinj=carleson_from_zeros(zc, centers, d, A, Li)
        # evolve forward and track max |Im z| (off-line-ness) and C
        zz=zc.copy(); traj=[]
        for s in range(40):
            im=np.max(np.abs(zz.imag)); Cc=carleson_from_zeros(zz, centers, d, A, Li)
            traj.append((s*dt, im, Cc)); zz=rk4_step(zz, dt)
        t_end,im_end,C_end=traj[-1]
        print(f"   delta0={delta0:.2f}: C_inj={Cinj:8.4f} -> after t={t_end:.3f}: "
              f"max|Im z|={im_end:.4f} (was {delta0:.2f})  C={C_end:.4f}  "
              f"{'HEALING (Im down, C down)' if im_end<delta0 and C_end<Cinj else 'no-heal'}")
    print("="*82)
    print(" READ: (A) sign of dC/dt = is C a Lyapunov candidate along the flow.  (B) if injected off-line")
    print(" zeros heal (|Im| shrinks, C drops) under FORWARD flow, the critical line is the attractor and")
    print(" the marginal C~1 is the Lambda=0 shadow.  Next (Gate B): prove dC/dt sign from the ODE, or find")
    print(" the true Lyapunov functional; check uniformity in T0 (Gate C).")
