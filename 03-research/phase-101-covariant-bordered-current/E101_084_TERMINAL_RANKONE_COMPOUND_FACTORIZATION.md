# E101.084 - Terminal rank-one compound factorization

## 1. Decision

The terminal matrix left open in E101.079 has the exact form

```text
T_B=C-b_B a^T,                                     (1.1)
```

where `C` and `a` are fixed by the safe evaluations and the jet frame, while
all build dependence is contained in the boundary-value vector `b_B`.

This common rank-one direction collapses every exterior compound much more
strongly than its ambient degree suggests.  Every minor of every fixed order
is affine in `b_B`.  In particular,

```text
C_3(T_B)=C_3(C)-L_3 b_B                            (1.2)
```

for one fixed linear map `L_3`.  The squared exterior detector is therefore
only a quadratic function of the terminal boundary values:

```text
P_3(T_B)=||C_3(C)-L_3b_B||^2.                     (1.3)
```

It is not a transported version of the isolated degree-six quartet
detector.

There are three consequences.

```text
full compound vector:
  under a transparent rank condition, it is an injective linear encoding of
  b_B and hence returns to boundary identification;

squared compound norm:
  it loses the direction of that encoding and need not vanish for an
  all-real divisor;

compound of a build difference:
  it vanishes identically in every order at least two because the difference
  has rank at most one.                              (1.4)
```

Thus `TERMINAL-RANKONE-COMPOUND` is closed as an independent bypass of
`DIRECTIONAL-IDENT`.  This does not prove IDENT or Omega7.  It proves that
the terminal exterior construction contains no unaccounted rank-four datum:
after the moving row is included, it contains only the already exposed
boundary vector and its fixed finite-dimensional conditioning.

## 2. Exact terminal notation

Work over `F=R` or `C`.  Let

```text
C in F^(q x r),
a in F^r,
b in F^q,
T(b)=C-ba^T.                                       (2.1)
```

For the terminal system of E101.079,

```text
C=C_ZJ_R,
a^T=ell_NJ_R,
b=B_B(Z),                                          (2.2)
```

and (2.1) is exactly E101.079(10.2).  The case `a=0` is build-blind, so it
cannot carry a discriminant.  Hence assume `a!=0` below.

For equal-cardinality row and column sets `I,J`, write

```text
Delta_(I,J)(b)=det T(b)[I,J].                      (2.3)
```

Let `C_k(T)` denote the vector of all `k x k` minors of `T`, in any fixed
order.  This is a coordinate representation of the exterior map
`wedge^k T`; changing the order or bases only multiplies it by fixed
invertible matrices.

## 3. Rank-one minors are affine

### Lemma 3.1 - Singular matrix determinant lemma

For every square matrix `M` and vectors `u,v` of the matching size,

```text
det(M-uv^T)=det M-v^T adj(M)u.                    (3.1)
```

No invertibility assumption on `M` is required.

### Proof

The determinant is multilinear in its columns.  In the expansion of
`M-uv^T`, a term which selects the update in two different columns has two
proportional columns and vanishes.  Hence only the term with no update and
the terms with exactly one updated column remain.  Their cofactor expansion
is the right side of (3.1). `QED`

Apply the lemma to every selected minor.

### Theorem 3.2 - Exact affine compound formula

For every order `k`, define `L_k:F^q->F^(binom(q,k)binom(r,k))` by

```text
(L_kb)_(I,J)
 =a_J^T adj(C_(I,J))b_I.                           (3.2)
```

Then

```text
Delta_(I,J)(b)
 =det C_(I,J)-a_J^T adj(C_(I,J))b_I,              (3.3)

C_k(T(b))=C_k(C)-L_kb.                            (3.4)
```

Consequently, for all `b_0,b_1`,

```text
C_k(T(b_1))-C_k(T(b_0))
 =-L_k(b_1-b_0).                                   (3.5)
```

### Proof

For fixed `I,J`, the selected update is `b_Ia_J^T`.  Formula (3.3) is (3.1),
and collecting the coordinates gives (3.4)--(3.5). `QED`

The exact second finite difference is therefore zero:

```text
C_k(T(b+h_1+h_2))-C_k(T(b+h_1))
-C_k(T(b+h_2))+C_k(T(b))=0.                       (3.6)
```

This is the precise form of the terminal collapse.  The entries of a third
compound have ambient degree three in a generic matrix, but only degree one
along the actual build family (2.1).

## 4. Kernel and injectivity of the compound encoding

The map `L_3` is often injective.  Its kernel has a simple exterior-algebra
description.

Choose `Q in GL_r(F)` such that

```text
a^TQ=e_1^T.                                        (4.1)
```

Write

```text
CQ=[c_1,w_2,...,w_r],
W=span{w_2,...,w_r}=C(ker a^T).                   (4.2)
```

Then

```text
T(b)Q=[c_1-b,w_2,...,w_r].                        (4.3)
```

Every compound column not using the first column is independent of `b`.
Every compound column which uses it changes by

```text
-b wedge w_(j_2) wedge ... wedge w_(j_k).         (4.4)
```

Right multiplication by `Q` induces the invertible map `wedge^kQ` on
compound coordinates, so (4.4) computes the kernel of `L_k` without changing
its injectivity.

### Theorem 4.1 - Exact compound kernel

Let `W=C(ker a^T)`.  Then

```text
ker L_k=
  F^q, if dim W<=k-2;
  W,   if dim W=k-1;
  {0}, if dim W>=k.                                (4.5)
```

In particular,

```text
dim C(ker a^T)>=3  =>  L_3 is injective.           (4.6)
```

### Proof

Suppose `L_kb=0`.  By (4.4),

```text
b wedge w_1 wedge ... wedge w_(k-1)=0             (4.7)
```

for every `k-1` vectors in `W`.  If `dim W<=k-2`, every such wedge is zero,
so `L_k=0`.  If `dim W=k-1`, one nonzero top wedge spans
`wedge^(k-1)W`; equation (4.7) is then equivalent to `b in W`.  If
`dim W>=k`, choose independent `u_1,...,u_k in W`.  For each `j`, equation
(4.7) applied to all but `u_j` places `b` in the span of those `k-1`
vectors.  The intersection of these `k` coordinate hyperplanes inside
`span{u_1,...,u_k}` is `{0}`.  Hence `b=0`. `QED`

A convenient sufficient condition is

```text
C is injective and r>=k+1.                         (4.8)
```

Indeed, `ker a^T` then has dimension `r-1>=k`, and its image under `C` has
the same dimension.

### Lemma 4.2 - Safe evaluations can realize (4.8)

Fix a finite jet depth for which the columns of `J_R` are independent.  A
finite set of evaluations `Z`, chosen inside a safe set with an accumulation
point, can be chosen so that

```text
C_ZJ_R:F^r->F^q                                   (4.9)
```

is injective.

### Proof

For `u!=0` in the finite jet space, the Cauchy transform

```text
z -> c_zJ_Ru                                       (4.10)
```

is a nonzero rational function: if it vanished on a set with an accumulation
point, all of its residues would vanish, contradicting independence of the
jet columns.  The functions (4.10) form an `r`-dimensional analytic function
space.  By induction on its dimension, one can choose `r` safe evaluation
points whose evaluation functionals are independent.  Their evaluation
matrix is (4.9). `QED`

For each fixed jet depth `R>=3`, the infinite Fourier jet columns are
independent: a relation among them is the Fourier transform of
`P(x)k(x)=0`, and uniqueness on an interval where `k` is nonzero forces the
polynomial `P` to vanish.  A sufficiently large finite Fourier section then
preserves one nonzero maximal minor.  Thus the injective regime is available
section by section.  No uniform lower bound for its smallest singular value
is asserted.

## 5. The exterior norm is only quadratic in the boundary data

Let `m_0=C_3(C)` and `L=L_3`.  For real terminal matrices define

```text
D_3(b)=||C_3(T(b))||_2^2.                          (5.1)
```

For complex matrices use the Hermitian norm of the vector of minors.  In
both cases Theorem 3.2 gives

```text
D_3(b)=||m_0-Lb||_2^2,                             (5.2)

D_3(b_0+h)-D_3(b_0)
 =-2 Re <m_0-Lb_0,Lh>+||Lh||_2^2.                (5.3)
```

The symmetric second difference removes the complete baseline term exactly:

```text
D_3(b_0+h)+D_3(b_0-h)-2D_3(b_0)
 =2||Lh||_2^2.                                     (5.3a)
```

Thus the Hessian in the build coordinate is the fixed positive semidefinite
matrix

```text
2L^*L.                                             (5.4)
```

The nominal degree-six polynomial in the entries of `T` has degree at most
two along the terminal family.  If (4.6) holds, it is a strictly convex
quadratic, but one scalar value does not determine `b`: its level sets are
ellipsoids after translation.

Equation (5.3a) is a genuine positive boundary energy.  It still does not
recover the isolated quartet discriminator: for a nonzero on-line boundary
increment `h`, injectivity gives `||Lh||^2>0`.  The symmetric cancellation
removes the baseline but not this all-real false positive.

More importantly, no rank-two statement is available for the complete
terminal baseline `C-b_Ba^T` under RH.  Distinct on-line spectral orbits have
already been aggregated, so the baseline can have rank at least three.
Consequently,

```text
RH does not imply D_3(b_B)=0                       (5.5)
```

from the terminal algebra.  Treating (5.1) as a nonnegative RH discriminator
would repeat the aggregate false positive of E101.078.

Three finite examples separate the claims.

First, with `C=I_4` and `a=e_1`, direct enumeration of the third minors gives

```text
D_3(b)=1+3|1-b_1|^2+|b_2|^2+|b_3|^2+|b_4|^2.    (5.6)
```

The Hessian has full rank, so the complete compound does not depend on one
scalar functional.  Nevertheless `b=0` and `b=2e_1` both give `D_3=4`.
Equality of one compound norm does not identify the boundary vector.

Second, for `C=I_3` and `a=e_1`, the only maximal minor is

```text
det(I_3-be_1^T)=1-b_1.                             (5.7)
```

It ignores `b_2,b_3`; one selected minor need not be injective even when a
larger compound family would be.

Third, put

```text
C_epsilon=diag(1,1,1,epsilon), a=e_1.             (5.8)
```

For every `epsilon>0`, `dim C_epsilon(ker a^T)=3`, so `L_3` is injective.
But some compound coefficients are proportional to `epsilon`, and

```text
sigma_min(L_3)->0 as epsilon->0.                   (5.9)
```

This is an explicit model of finite injectivity without cofinal coercivity.

## 6. Exact return to boundary identification

Let `b_B` be the terminal boundary vector and let `b_ref` be a declared
comparison vector.  Equation (3.5) gives

```text
C_3(T_B)-C_3(T_ref)=-L_3(b_B-b_ref).              (6.1)
```

If (4.6) holds, exact equality of the complete third-compound vectors is
equivalent to

```text
b_B=b_ref.                                         (6.2)
```

For approximate identification, let `sigma_min(L_3)` be the smallest
singular value.  Then

```text
sigma_min(L_3)||b_B-b_ref||
 <=||C_3(T_B)-C_3(T_ref)||
 <=||L_3||||b_B-b_ref||.                           (6.3)
```

Sectionwise positivity of `sigma_min` follows from injectivity.  A cofinal
deduction in the reverse direction requires the scaled lower bound

```text
||compound error||/sigma_min(L_3)->0.              (6.4)
```

This is an inf-sup requirement of the same type as E101.045(4.5).  Bare
finite injectivity supplies no cofinal estimate.

In the actual notation, (6.2) identifies the sampled values `B_B(Z)`.  On a
cofinal determining family of safe sets, upgrading those samples to the
required boundary-to-model convergence is precisely the analytic content of
`DIRECTIONAL-IDENT`, together with its normality and denominator controls.
The compound does not estimate those values independently; it applies the
fixed map `L_3` to them.

### Theorem 6.1 - Canonical normalized terminal energy

Let `k` be the normalized comparison column,

```text
ell_Nk=1,
e=M_Bk,
B_k(z)=c_zk.                                       (6.5)
```

Choose `q>=3` distinct nonzero safe points `Z=(z_1,...,z_q)` with
`B_k(z_a)!=0`, and assume `q<=dim ker ell_N`.  Put

```text
D=diag(B_k(z_1),...,B_k(z_q)).                    (6.6)
```

There are columns `U=(u_1,...,u_q)` in `ker ell_N` such that

```text
D^(-1)C_ZU=I_q.                                   (6.7)
```

For the moving terminal rows `p_(B,Z)`, define

```text
That_B
 =D^(-1)[p_(B,Z)M_Bk, p_(B,Z)M_BU].               (6.8)
```

Then

```text
That_B=[delta_B,I_q],

delta_B(a)
 =p_(B,z_a)e/B_k(z_a)
 =1-B_B(z_a)/B_k(z_a).                            (6.9)
```

The complete third-compound norm is exactly

```text
P_3(That_B)
 =binom(q,3)+binom(q-1,2)||delta_B||_2^2.         (6.10)
```

In particular, for `q=3`,

```text
P_3(That_B)
 =1+sum_(a=1)^3
   |p_(B,z_a)e/B_k(z_a)|^2.                       (6.11)
```

### Proof

First prove (6.7).  The functionals

```text
ell_N,c_(z_1),...,c_(z_q)                         (6.12)
```

are independent when the mesh has more than `q` points.  Indeed, a linear
relation evaluated on the mesh coordinates would make

```text
F(x)=beta+sum_(a=1)^q alpha_a z_a/(z_a-x)         (6.13)
```

vanish at more than `q` mesh points.  After multiplication by
`product_a(z_a-x)`, its numerator has degree at most `q`; hence it vanishes
identically.  Distinctness and nonvanishing of the `z_a` then make every
residue `alpha_a` zero, followed by `beta=0`.  Thus the restrictions of the
`c_(z_a)` to `ker ell_N` are independent, so

```text
C_Z:ker ell_N->F^q                                (6.14)
```

is onto.  Solve `C_ZU=D` to obtain (6.7).

The exact moving-row identity gives

```text
p_(B,z)M_B=c_z-B_B(z)ell_N.                       (6.15)
```

Applying it to `u_j in ker ell_N` and to `k` proves (6.9).  It remains to
enumerate the third minors of `[delta,I_q]`.  Minors using three identity
columns contribute one for each three-element row set, giving `binom(q,3)`.
A minor using the `delta` column and two identity columns equals, up to sign,
the remaining component of `delta`.  Each component occurs
`binom(q-1,2)` times.  All other minors vanish.  Summing their modulus squares
proves (6.10)--(6.11). `QED`

The normalized excess

```text
P_3(That_B)-binom(q,3)
 =binom(q-1,2)sum_a
  |1-B_B(z_a)/B_k(z_a)|^2                         (6.16)
```

is literally a finite sampled IDENT energy.  A Gamma--Euler theorem forcing
this excess to zero, or to zero cofinally on determining safe sets, would be
a proof of IDENT in these coordinates.  It would not reopen an independent
compound mechanism.

## 7. Why the isolated quartet cannot survive through this channel

Between two builds,

```text
T(b_1)-T(b_0)=-(b_1-b_0)a^T                       (7.1)
```

has rank at most one.  Hence

```text
C_k(T(b_1)-T(b_0))=0 for every k>=2.              (7.2)
```

The nonzero isolated rank-four matrix of E101.079(9.4) therefore cannot be
the terminal build difference after the dual row moves.  It appears only in
the additive term before the exact cancellation with the row variation.

One might instead square (6.1).  If a labelled decomposition

```text
b_B=sum_omega b_omega                             (7.3)
```

were available, then

```text
||L_3b_B||^2
 =sum_(omega,nu)<L_3b_omega,L_3b_nu>.             (7.4)
```

Phase averaging could remove the unequal labels in this quadratic sum.  The
surviving atom is `||L_3b_omega||^2`, not the isolated exterior-cube atom of
E101.078.  There is no algebraic reason for it to vanish on an on-line orbit.
Thus it is a labelled boundary energy, not a rank-two/rank-four
discriminator.

This separates two operations which had been conflated:

```text
take the compound of an isolated orbit before aggregation:
  detects the rank jump but needs the diagonal lift;

take the compound after the moving terminal row:
  gives an affine boundary encoding plus baseline terms.            (7.5)
```

## 8. Terminal trilemma

Every use of the terminal third compound now falls into one of three cases.

```text
use all compound coordinates:
  this is an injective linear change of the finite boundary coordinates when
  (4.6) holds, and its cofinal inverse requires IDENT conditioning;

use only P_3 or another norm:
  direction is lost and the aggregate baseline gives all-real false
  positives;

apply the compound to a build difference:
  it vanishes identically by rank one.                              (8.1)
```

A further nonlinear function of the full compound vector is merely a
nonlinear function of `b_B` through (1.2).  It remains admissible only if a
new Gamma--Euler identity proves the needed relation for the actual Xi
boundary values.  The compound factorization itself supplies no such
identity.

## 9. Nonduplication gate

The matrix determinant lemma, exterior compounds and the kernel calculation
in Theorem 4.1 are classical finite-dimensional algebra.  No novelty is
claimed for them.

A recent adjugate-based treatment of determinant dynamics under singular
low-rank perturbations is:

```text
Vrabel:
  https://arxiv.org/abs/2604.04650                  (9.1)
```

It reinforces that the affine rank-one determinant formula is antecedent
algebra, not a new theorem of this program.

The potentially new content is their application to the exact moving
terminal identity of E101.079: the baseline mixed terms are now computed
rather than left as an unspecified nonlinear remainder.  They form the
quadratic boundary expression (5.2), and the complete compound vector is the
affine boundary encoding (6.1).

This result does not duplicate the isolated rank-four theorem of E101.078 or
the phase diagonalization of E101.079.  It proves that neither reaches the
moving terminal row through an exterior-power shortcut.

## 10. Revised targets and stop rule

The target

```text
TERMINAL-RANKONE-COMPOUND as an independent discriminator             (10.1)
```

is closed negatively.

The following remain live:

```text
DIRECTIONAL-IDENT:
  prove the boundary comparison with the required cofinal inf-sup scale;

MIXED-BIDEGREE-GAMMA-EULER:
  construct the conjugate same-zero current before aggregation;

NONLINEAR-MATCHED-EVENT-TRANSPORT:
  derive that current from marked prime events without a tensor power of a
  mixing one-level transform;

SINGULAR-DIAGONAL-PULLBACK:
  prove an ordered nonnormal limit with all mixed terms controlled.   (10.2)
```

Freeze:

```text
calling P_3(T_B) a degree-six function of the build coordinate;
claiming that a rank-one terminal difference preserves the compound itself;
using the norm of the aggregate terminal compound as an on-line/off-line
rank discriminator;
claiming that finite compound injectivity supplies a cofinal lower bound;
reintroducing the isolated rank-four response after the moving-row term has
cancelled it.                                                        (10.3)
```

## 11. Status

```text
proved:
  exact affine formula for every terminal compound;
  exact kernel and injectivity criterion for the complete compound vector;
  realization of that criterion by sufficiently many safe evaluations;
  exact quadratic formula for the squared third compound;
  canonical normalized compound equal to a constant plus sampled IDENT
  energy;
  equivalence of complete compound matching and sampled boundary matching
  under the finite injectivity hypothesis;
  vanishing of all higher compounds of a terminal build difference;

closed negatively:
  TERMINAL-RANKONE-COMPOUND as an independent route around IDENT;
  aggregate terminal P_3 as an RH discriminator;

still open:
  cofinal DIRECTIONAL-IDENT;
  MIXED-BIDEGREE-GAMMA-EULER;
  NONLINEAR-MATCHED-EVENT-TRANSPORT;
  SINGULAR-DIAGONAL-PULLBACK;
  Omega7.
```
