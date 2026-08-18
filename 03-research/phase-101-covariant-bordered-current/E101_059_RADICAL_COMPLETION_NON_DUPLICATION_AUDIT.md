# E101.059 - Radical completion non-duplication audit

## 1. Purpose

The radical identity

```text
Q_Z(k,phi)=0                                         (1.1)
```

is unconditional and genuinely distinguishes the arithmetic divisor from an
artificial divisor with an inserted quartet.  The question is whether
E101.056 introduced a new mechanism for transporting (1.1) to the finite
boundary current, or merely renamed an existing continuity obligation.

The answer is exact:

```text
the abstract completion principle is not new;
a specific finite dual estimate could still be new;
no such estimate has yet been proved.                 (1.2)
```

This document proves the crosswalk, records the relevant scales and fixes the
stopping rule for further Hardy-space reformulations.

## 2. Abstract completion is directional tail continuity

Let `X` be a normed source space, let `x_N in X`, and let
`Lambda_(N,z) in X^*` for `z` in a compact safe set `K`.

### Lemma 2.1

If

```text
sup_N sup_(z in K)||Lambda_(N,z)||_(X^*)<infinity,
||x_N||_X->0,                                        (2.1)
```

then

```text
sup_(z in K)|Lambda_(N,z)(x_N)|->0.                 (2.2)
```

### Proof

The left side of (2.2) is bounded by the product of the two quantities in
(2.1). `QED`

In E101.056 take

```text
x_N=(I-Pi_N)k,
Lambda_(N,z)(x)=Q_Z(x,phi_(N,z))/alpha_N.           (2.3)
```

Then Lemma 2.1 is exactly the proposed radical completion theorem.  In
E80.008 the same lemma is called `DIRECTIONAL-TAIL-CONTINUITY`.  E82.004
proves that, on the actual safe Cauchy direction,

```text
DIRECTIONAL-TAIL-CONTINUITY
=Weyl-reduced leakage
=scalar WRL.                                         (2.4)
```

Equality in (2.4) means equality of the scalar proof obligation, not equality
of every sufficient norm.  Choosing `H2`, `H1`, BMOA or a bounded-variation
source topology does not by itself change (2.4).

## 3. The arithmetic coboundary route was already completed algebraically

The historical response to (2.4) was not merely a proposed construction.
The following exact chain is already proved.

First, the finite Euler--Mobius representation gives

```text
M[X,Z]
=sum_(n<=exp L) Lambda(n)n^(-sigma)S_(log n).        (3.1)
```

After Fourier compression and addition of the archimedean endpoint source,
the coupled source has the rank-two form

```text
f=[D,M]g.                                            (3.2)
```

For a spectral projection `P`, `Q=I-P` and `C=QMQ`, E84.003 constructs

```text
u=-QDg,
Qf=Cu+e,
e=QD Mg.                                             (3.3)
```

Thus the construction half of the two-generator arithmetic coboundary is
closed.  Its remaining safe response is

```text
ell_z(C^(-1)QD Mg),                                  (3.4)
```

which is the same reduced leakage in (2.4).  E91.002--E91.004 prove the same
no-bypass result on a deformation line: every inverse-free explicit
corrector leaves a safe reduced leakage term.  A new source topology that
only proves `e->0` in an ambient norm therefore returns to the old wall.

## 4. Corrections forced on E101.056

Four distinctions are essential.

### 4.1 Extraction is not synthesis

The finite maps are

```text
P_N:X->C_N,
J_N:C_N->X,
Pi_N=J_NP_N.                                        (4.1)
```

The exact radical transfer uses `(I-Pi_N)k`, not `(I-P_N)k`.  With

```text
alpha_N=ell P_Nk,
k_N=P_Nk/alpha_N,                                    (4.2)
```

the normalized boundary identity is

```text
B_y(z)-c_zk_N
=Q_Z((I-Pi_N)k,phi_(N,z))/alpha_N.                  (4.3)
```

### 4.2 The source norm must be fixed independently

The rational functions `U_z,V_z` depend on the cutoff, safe point, dual row
and build.  They belong to the dual functional.  Including them in the norm
of the source makes that norm vary with the object whose boundedness is to be
proved.

### 4.3 Weak-limit uniqueness is unnecessary

Uniform dual boundedness and strong source-tail convergence imply the scalar
limit directly by Lemma 2.1.  Requiring every subsequence to have the same
weak limit adds a stronger statement with no role in that implication.

### 4.4 Nonzero quartet functional is not detected automatically

For an inserted quartet `Q`, the limiting defect has the form

```text
sum_(rho in Q)Xi(rho)Phi_(phi_z)(rho).               (4.4)
```

The functional in (4.4) is not identically zero on the full test space, but
the actual `phi_z` may lie in its kernel.  Boundedness, nonzero normalization
and weak convergence do not imply nonvanishing of (4.4).  The assertion
called `RDC-4` remains an independent discriminating problem.

## 5. Exact matrix content of the H2 proposal

Put

```text
h=2pi/L,
a=2/L,
d_n=hn.                                              (5.1)
```

Index the row nodes as `d_(N-r)`, `0<=r<=2N`, and the positive exterior
nodes as `d_(N+j)`, `j>=1`.  Let `E` be the matrix of exterior columns.
The displacement identity gives exactly

```text
E_(r,j)
=1/pi [s_(N-r)-s_(N+j)]/(r+j).                      (5.2)
```

For a dual row `p`, define

```text
alpha_r=p_(N-r)s_(N-r),
beta_r=p_(N-r),
H_(j,r)=1/(j+r),
S_e=diag(s_(N+j)).                                   (5.3)
```

Then

```text
(pE)^T=1/pi [H alpha-S_eH beta],                    (5.4)

||pE||_2^2
=1/pi^2 ||H alpha-S_eH beta||_2^2.                 (5.5)
```

Since the Hilbert matrix has `ell2` norm at most `pi`,

```text
||pE||_2
<=||p s_r||_2+C_L||p||_2                            (5.6)
```

when the symbol is bounded by `C_L` on the exterior mesh.  No hidden power
of `L` remains in (5.2): the ratio `a/h` is exactly `1/pi`.

Consequently `H2-DUAL-BOUND` is the finite quadratic condition

```text
pEE^*p^*/|b_(N,z)|^2<=C_K^2.                        (5.7)
```

Equation (5.7) is precise and may be tested.  The Hilbert bound (5.6) does
not prove it, because the normalized row norms on its right can diverge.

## 6. H2 is not CCGD and does not contain PW-Cauchy

The earlier Cauchy-channel Green decay has the exact quotient

```text
CCGD_H(s)
=a_x(s)^*C_E^(-1)K_HC_E^(-1)a_x(s)
 /[a_x(s)^*C_E^(-2)a_x(s)].                         (6.1)
```

Here `K_H` is a compressed physical projection and `a_x(s)` is one fixed
Cauchy source.  In contrast, (5.7) uses the Gram matrix `EE^*` of moving
exterior Loewner columns and the dual cofactor row `p`.  The two cutoffs and
the two normalizations are different.  No uniform Loewner comparison
between `K_H` and `EE^*` has been proved.  Hence neither condition currently
implies the other.

The Paley--Wiener target of E72.316 is stronger in a different direction:

```text
|(1-e^(zL))C_x(iz)|<=L^B(1+|Im z|)^B,
Re z>=sigma>0.                                      (6.2)
```

It requires

```text
|C_x(iz)|<=e^(-sigma L) times a polynomial.          (6.3)
```

The real exterior `ell2` bound (5.7) contains neither `1-e^(zL)` nor the
exponential gain in (6.3).  Deriving (6.2) from (5.7) would require a new
sampling or continuation theorem that supplies exactly the missing scale.

E72.391 gives the sharper exact tail identity

```text
Lcal(B_z^tail)
=-2i/L sum_w wG_x(w)
  sum_(|m|>M)(1-e^(zL))/[(iz-d_m)(w^2+d_m^2)].       (6.4)
```

Thus the Fourier tail is already governed by the nodal vector `G_x(w)`.
Replacing (6.4) by an `H2` norm is legitimate only as a sufficient estimate;
it is not a new nodal suppression mechanism.

## 7. Novelty verdict

The current classification is

```text
abstract RADICAL-DUAL-COMPLETION:  duplicate of (2.4);
H2-DUAL-BOUND:                    precise but unproved sufficient theorem;
BMOA duality:                     useful only if an H1-small source is proved;
Euler--Mobius coboundary:         construction already closed in (3.3);
RDC-4:                            open discriminating assertion.         (7.1)
```

A further norm proposal is not progress unless it satisfies both conditions:

```text
it is derived from the finite dual equation or an exact finite identity;
it proves a one-way bound for the complete recombined current without
separating cancelling regions.                       (7.2)
```

## 8. Route decision

The abstract completion route is frozen.  The `H2` and BMOA formulations are
retained only as diagnostics until one of their cofinal bounds is proved.
The arithmetic coboundary construction is not reopened.

Two finite directions remain admissible inside the current phase:

```text
1. the offset-matched coordinate of E101.058, which removes the false blind
   subspace before any estimate;

2. an exact bilateral Abel representation of the whole exterior pairing,
   with collar and far regions recombined before taking a norm.          (8.1)
```

The second direction must produce an explicit bound from the dual equation.
Merely naming its dual space would again be (2.4).

## 9. Status

```text
proved:
  abstract radical completion equals the old directional continuity schema;
  the Euler--Mobius construction half was already closed;
  exact H2 exterior matrix and scale;
  absence of an implication to or from CCGD in the available identities;
  absence of the PW exponential factor from H2;

corrected:
  source and dual topologies in E101.056;
  extraction, synthesis and normalization in the radical identity;
  uniqueness and quartet-genericity claims;

open:
  a new finite estimate for the complete exterior current;
  actual quartet detection;
  DIRECTIONAL-IDENT and Omega7.
```
