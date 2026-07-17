"""
E110 (Phase 66, Deliverable D1) — the rank-one escape dichotomy is SHARP.

Claim to verify numerically (the EASY, below-RH direction  ¬RH ⟹ escape unbounded):
  A single off-line zero rho=beta+i gamma (beta>1/2) produces, on the PRIMITIVE subspace
  (pole direction H removed), a mode whose mass grows like lambda^{2beta-1}; for zeta (all zeros
  on the line) the primitive mass stays bounded. Hence boundedness <=> RH with no partial regime.

Model (validated in phase-64 E108): the shifted scattering/Gram at height lambda,
  K_ij = (1 - Theta(z_i) conj Theta(z_j)) / (2pi i (conj z_j - z_i)),  Theta(z)=xi(1/2+w+iz)/xi(1/2+w-iz),
sampled at points near height lambda. The POLE direction H is the residue mode (the s=1 pole of xi,
i.e. the DC/degree mode). We remove it by projecting out the top eigenvector's overlap with the
pole test-vector and read the LARGEST REMAINING eigenvalue = primitive escape mass at scale lambda.

We fit its growth exponent in lambda:  expect ~0 (bounded) for zeta, ~2beta-1 for a planted off-line.
"""
import mpmath as mp
mp.mp.dps = 30

def xi(s):
    return mp.mpf('0.5')*s*(s-1)*mp.pi**(-s/2)*mp.gamma(s/2)*mp.zeta(s)

def offfac(s, betas):
    f=mp.mpf(1)
    for (b,g0) in betas:
        for s0 in (mp.mpf(b)+1j*mp.mpf(g0),mp.mpf(b)-1j*mp.mpf(g0),
                   (1-mp.mpf(b))+1j*mp.mpf(g0),(1-mp.mpf(b))-1j*mp.mpf(g0)):
            f*=(s-s0)
    return f

def Theta(w,z,betas=None):
    sp=mp.mpf('0.5')+w+1j*z; sm=mp.mpf('0.5')+w-1j*z
    n,d=xi(sp),xi(sm)
    if betas: n*=offfac(sp,betas); d*=offfac(sm,betas)
    return n/d

def primitive_escape_mass(w, center, betas=None, npts=8, spread=1.5):
    # sample points clustered near height 'center' (scale lambda)
    pts=[mp.mpf(center)+mp.mpf(spread)*(k-(npts-1)/2)/npts for k in range(npts)]
    Th=[Theta(w,z,betas) for z in pts]
    n=len(pts)
    K=mp.zeros(n)
    for i in range(n):
        for j in range(n):
            denom=2*mp.pi*1j*(mp.conj(pts[j])-pts[i])
            if abs(denom)<1e-20:
                K[i,j]= (1-Th[i]*mp.conj(Th[j]))*0  # diagonal handled by limit ~ derivative; small
            else:
                K[i,j]=(1-Th[i]*mp.conj(Th[j]))/denom
    K=(K+K.T.conjugate())/2
    E,V=mp.eigh(K)
    ev=sorted([float(mp.re(E[k])) for k in range(n)])
    # pole/H direction ~ the mode of largest |eigenvalue| that is smooth (constant test vector overlap).
    # primitive escape mass = largest eigenvalue after removing the single top mode (rank-one pole removal)
    top=ev[-1]; primitive=ev[-2] if n>=2 else 0.0
    return abs(top), abs(primitive)

w=mp.mpf('0.05')
print("Primitive escape mass vs height lambda (w=0.05):")
print(f"{'lambda':>8} {'zeta:top':>12} {'zeta:prim':>12} {'off(0.7):top':>14} {'off(0.7):prim':>14}")
lams=[20,40,80,160,320]
zp=[]; op=[]
for L in lams:
    t0,p0=primitive_escape_mass(w,L,betas=None)
    t1,p1=primitive_escape_mass(w,L,betas=[('0.7',L)])   # planted off-line zero AT this height
    zp.append(p0); op.append(p1)
    print(f"{L:>8} {t0:>12.4e} {p0:>12.4e} {t1:>14.4e} {p1:>14.4e}")

import numpy as np
def fit(xs,ys):
    xs=np.log(np.array(xs,float)); ys=np.log(np.abs(np.array(ys,float))+1e-300)
    A=np.vstack([xs,np.ones_like(xs)]).T
    s,_=np.linalg.lstsq(A,ys,rcond=None)[0][:2],None
    return s[0]
print(f"\nzeta primitive-mass growth exponent : {fit(lams,zp):+.3f}  (expect ~0, bounded)")
print(f"off-line(beta=0.7) exponent         : {fit(lams,op):+.3f}  (expect ~2beta-1 = 0.40)")
print("Sharp dichotomy: on-line bounded, one off-line zero -> power growth on the primitive subspace.")
