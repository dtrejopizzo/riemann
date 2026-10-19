# R162_207 — Audit of the nonlinear two-parameter escape


Status: **NO-GO FROM THE CURRENT INPUTS / GATE 1 OPEN.** R162_206 leaves only a nonlinear mixed
construction as a possible use of the same finite anomaly. There are two natural choices for the
second parameter. The scalar choice has identically zero mixed curvature before compression; after
compression its apparent return term cancels in the complete Green expression. The active-coefficient
choice has no equality-state or positivity law in that direction. A noncommutative/root-valued lift
would be genuinely new input, not a consequence of the present `(PC-ren)` identities.

## 1. Scalar Euler/source deformation is flat

Let a scalar completed Euler factor and a compact-source transform be deformed independently:

    E_u(z)=E(z+u),              K_v(z)=K_F(z-v).                (1.1)

For their product,

    partial_u partial_v log(E_u(z)K_v(z))=0.                    (1.2)

For the unlogged product the mixed derivative is

    partial_u partial_v [E(z+u)K_F(z-v)]|_(0,0)
      =-E'(z)K_F'(z),                                          (1.3)

not `(E'/E)(z)K_F(z)` and not the regularised critical jet
`E'(rho)K_F(rho)`. On the diagonal `u=v`, division by `E` produces

    (E'/E)K_F-K_F',                                            (1.4)

which is removable at a zero of `E` exactly when `K_F` vanishes there. Thus (1.4) assumes the gate
rather than deriving it. These are the exact calculations of the phase-121 two-parameter holonomy
audit, now applied to the candidate left by R162_206.

## 2. Compression does not create curvature

One may try to evade (1.2) by compressing before differentiating. For two scalar relative Euler
factors `C_(a,r)` and `C_(b,s)`, the full Wigner connection is additive:

    (C_(a,r)C_(b,s)^epsilon)^* Q (C_(a,r)C_(b,s)^epsilon)-Q
      =a(P_(a,r)-I)+epsilon b(P_(b,s)-I).                       (2.1)

Hence its distinct-coordinate mixed derivative is identically zero. Expanding only the compressed
state displays a return block

    P U_a(I-P)U_(-b)P=P U_(a-b)P,                               (2.2)

but the mixed derivatives of the generator transport and of the unitary normalization cancel (2.2)
in the complete expression. This cancellation occurs before the Tate projection and for every
source. Physical compression therefore cannot turn the flat scalar connection into the missing
critical-jet energy.

## 3. Coefficient deformation has no first-contact law

The other candidate is

    a_u=Lambda+u eta,                                           (3.1)

paired with a physical deformation `v` (window displacement, source modulation, or Poisson
orientation). R162_204--205 show that the `u` derivative is the odd Ward defect
`b_(a_u)=u(eta*1)`. However, first contact supplies a null state only for the zeta form at `u=0`:

    H_(T,Lambda)F=0.                                           (3.2)

It supplies neither

    partial_u <F,H_(T,a_u)F>|_(u=0)=0                          (3.3)

nor a one-sided sign for this derivative. Such a sign is false for the finite-modification family
used in `thm:finmod`. Consequently a mixed derivative `partial_u partial_v` contains the desired Ward
slot but has no equality-state value that sets it to zero or gives it a sign.

Window/source modulation does not repair this. Its primitive component is the universal radical
polarization, its Tate component has the opposite-parity zero pairing, and its exterior component is
the support commutator already audited in R161_044 and R161_065. Thus the mixed coefficient--physical
Hessian either is unconstrained in `u` or returns to the existing exterior reciprocity.

## 4. What would be genuinely additional

The scalar obstruction disappears only if the two directions fail to commute before scalar trace.
The local Euler Toeplitz/Hankel root does have such a positive rank-one self-commutator. But R161_045
proves that transporting these local roots to the physical Euler--Gamma carrier requires a global
metrized determinant/anomaly trivialization identifying the two histories. The present corpus has no
such descent, and `(PC-ren)` does not construct it.

Therefore a surviving two-parameter identity would have to add one of the following genuinely new
inputs:

1. a noncommutative/root-valued lift of the finite Euler synthesis together with a proved physical
   descent preserving the crossed Gamma/Tate terms; or
2. an independent coefficient-direction equality law at `Lambda`, strong enough to replace (3.3).

Either input would have to fail for finite modifications and be unavailable for
Davenport--Heilbronn. Neither follows from first contact, the two linear PC identities, their Green
polarizations, Sonin membership, or the known polar/Tate matching.

## 5. Consequence for Gate 1

The current hypotheses determine:

- the regularised critical jet;
- both finite linear PC orientations;
- the Ward defect for modified coefficients;
- every primitive, Tate and exterior block created by compression.

They do **not** determine an equality or sign for the remaining antisymmetric exterior correlation.
That correlation is exactly the missing residue-annihilation input. The scalar nonlinear extension is
flat, and the active-coefficient extension is not stationary.

Accordingly no derivation of

    Res_(z=i gamma) H_(+,T)F=-m_rho K_F(i gamma)=0              (5.1)

has been obtained from the available assumptions.

## 6. Exact status

- scalar two-parameter curvature: **ZERO / PROVED**;
- cancellation of the apparent compressed return in the complete scalar Green law: **PROVED in the
  cited phase-121 identity**;
- coefficient-direction first-contact stationarity: **ABSENT and not implied**;
- noncommutative Euler--Gamma descent or independent coefficient equality law: **MISSING NEW INPUT**;
- Gate 1 and row D: **OPEN**.
