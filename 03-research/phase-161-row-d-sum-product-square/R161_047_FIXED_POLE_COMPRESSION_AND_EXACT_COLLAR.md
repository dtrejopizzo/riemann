# R161_047 — Fixed-pole compression and the exact exponential collar

## Fixed-pole calculation

Use z=s-1/2, a_m=2m+1/2, and the corrected defect W^0 of R161_017. R161_025 proves

    Res_(z=a_m) W^0(1/2+z) = K_F(a_m).

Let w be its inverse distribution. Its restriction to the open physical window is the Tate forcing r. Define the exterior remainder without multiplying a general distribution by a discontinuous function:

    v = w - E_T r,

where E_T r is the ordinary zero extension of the window Tate function. Then v vanishes on the open window; any endpoint distributions remain in v. The transform of E_T r is entire because E_T r has compact support. Consequently

    Res_(z=a_m) Mv(z) = K_F(a_m).                         (1)

This identity is exact for the meromorphic transforms already constructed in R161_017. It does not require an L2 claim for w. If multiplied by zeta(s), the residue is zeta(2m+1) K_F(a_m), since zeta is analytic and nonzero at that point.

More generally, every compactly supported distribution has an entire Laplace transform: its action on exp(-zt) is holomorphic, with derivatives obtained by inserting powers of -t. Thus neither an interior primitive test, an interior Tate correction, nor an endpoint distribution has a Laurent residue there. They can constrain the exterior through another identity, but cannot cancel (1) as separate compactly supported Laurent terms.

The compact prehistories Q_+, Q_- and the polar corrections in R161_019 are also holomorphic at these points. Therefore extracting the residue of the known defect identity returns K_F(a_m); it does not yet prove that coefficient zero.

## A literal exterior realization of a pole

For any a>0 and coefficient k, the function

    h(t) = -k exp(at) 1_(t<-T)

has transform, initially for Re z<a,

    integral h(t) exp(-zt) dt
      = k exp((z-a)T)/(z-a).

Its meromorphic continuation has residue k at z=a. This elementary model exhibits why a nonzero exterior coefficient is compatible with an identically zero interior restriction. It is not asserted to satisfy the complete physical first-contact system.

## Exact collar under a finite translation

For F supported in [-T,T], real a>0, and 0<=h<=2T, define

    ell_a(F) = integral_(-T)^T F(u) exp(-au) du,
    L_(a,h)(F) = integral_(-T)^(-T+h) F(u) exp(-au) du.

With tau_h F(t)=F(t+h) and P the window restriction/extension,

    ell_a(P tau_h F)
      = exp(ah) [ell_a(F)-L_(a,h)(F)].                    (2)

Proof: substitute u=t+h and intersect the integration interval with the support of F. For h>=2T the compressed translation is zero. At h=2T the collar is the full moment, so (2) remains valid.

The corresponding full-line translated moment is exp(ah)ell_a(F). The omitted part of that full-line moment is exactly exp(ah)L_(a,h)(F), supported to the left of the window after translation. There is no small remainder merely from writing the compressed moment as a multiple of ell_a(F).

For the finite integer synthesis S_N from R161_001, (2) gives

    ell_a(P S_N F)
      = sum_(n<=min(N,exp(2T))) n^(a-1/2)
          [ell_a(F)-L_(a,log n)(F)].                     (3)

The index condition means integers satisfying both inequalities. For K_N insert log n; for L_M insert Lambda(n). These are exact finite identities. The large factor n^(a-1/2) multiplies the collar as well as the full moment. A proposed fixed-pole contraction must control their difference, with the continuum counterterm computed separately before any limit.

## Consequence for the backward route

R161_046 reduces detection to finitely many moments on a fixed finite-dimensional radical. It does not eliminate the collars (2)-(3) or change where the residues live. The current fixed-pole calculation therefore supplies the exterior coefficient and its finite translation correction, but no annihilation law.

This agrees with the previously recorded large-moment obstruction in R161_024, section 5. It is not a new proof of logical independence from the full physical system. The remaining calculation must use the joint Fourier/Poisson relation to give a sign or a cancellation for these literal exterior terms, beyond the compressed first-contact equation.

Status: formulas (1)-(3) proved; fixed-pole annihilation from PC-ren open; D open.
