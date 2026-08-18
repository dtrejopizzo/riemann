# E101.067 - Binomial Abel backshift and exact cancellation autopsy

## 1. Question

E101.066 leaves open a source-first relation between the zeroth Abel pairing
and its radial shifts.  The canonical universal candidate is the binomial
backshift, because it replaces the Cauchy kernel `1/n` by shifted kernels
`1/(n+m)` plus a high-order beta remainder.

This document proves the exact identity and then shows the limitation of the
canonical binomial candidate:

```text
after shifted-column transfer, the terminal action cancels from both sides;
in the symmetric finite falsifier, every fixed order leaves the same
singular dual mode in the shifted sum and the opposite mode in the beta
remainder.                                                                 (1.1)
```

Thus the binomial identity is useful finite algebra but does not supply
`RADICAL-SOURCE-BACKSHIFT` without an additional arithmetic shift-covariance
theorem.

## 2. Universal beta decomposition

Let

```text
F(t)=P_A(t)C(t)-P_B(t)D(t)                          (2.1)
```

satisfy

```text
integral_0^1 |F(t)|dt/t<infinity,                   (2.2)
```

and define

```text
I_m=1/pi integral_0^1 t^(m-1)F(t)dt,
m>=0.                                               (2.3)
```

For an integer `K>=1`, put

```text
gamma_(K,m)=(-1)^(m+1) binom(K,m),
1<=m<=K.                                            (2.4)
```

### Theorem 2.1 - Binomial backshift

One has

```text
I_0=sum_(m=1)^K gamma_(K,m)I_m+R_K,                 (2.5)

R_K=1/pi integral_0^1
                  (1-t)^K F(t)dt/t.                (2.6)
```

### Proof

The binomial theorem gives

```text
sum_(m=1)^K gamma_(K,m)t^m
=1-(1-t)^K.                                         (2.7)
```

Multiply (2.7) by `F(t)/t`, integrate, and use (2.3). `QED`

Suppose now that

```text
P_A(t)=sum_(r=0)^R a_rt^r,
P_B(t)=sum_(r=0)^R b_rt^r,
C(t)=sum_(j>=1)c_jt^j,
D(t)=sum_(j>=1)c_js_jt^j,                           (2.8)
```

with finite support.  Then

```text
R_K=1/pi sum_(r,j)c_j(a_r-s_jb_r)
                  Beta(r+j,K+1),                   (2.9)

Beta(n,K+1)
=K!/[n(n+1)...(n+K)].                              (2.10)
```

Thus the remainder replaces the Hilbert kernel by an order-`K+1` Cauchy
product.  This decay is pointwise in `r+j`; it is not yet a bound after the
dual coefficients are inserted.

For the actual right-bordered terminal current, take

```text
F_rb(t)
=A^+(t)C^+(t)-B^+(t)D^+(t)
 -A^-(t)C^-(t)+B^-(t)D^-(t),                       (2.11)
```

where the positive source begins at `j=2` and the negative source at `j=1`,
as in E101.065.  Define `I_(m,rb)` and `R_(K,rb)` by (2.3) and (2.6) with
`F=F_rb`.  Theorem 2.1 applies verbatim and

```text
I_(0,rb)=Acal_(N,z)(kappa).                         (2.12)
```

The two-channel parity form (2.8) is used below only for the symmetric finite
falsifier.  No parity reduction is needed for (2.11).

### Theorem 2.2 - Classification of finite linear backshifts

Let `eta_1,...,eta_K` be arbitrary and define

```text
G_eta(t)=sum_(m=1)^K eta_m t^m,
q_eta(t)=1-G_eta(t).                                (2.13)
```

Then every finite linear backshift with no zeroth term has the unique exact
remainder

```text
I_0=sum_(m=1)^K eta_m I_m+R_eta,

R_eta=1/pi integral_0^1 q_eta(t)F(t)dt/t.          (2.14)
```

### Proof

Subtract `G_eta(t)` from `1`, multiply by `F(t)/t`, and integrate.  Uniqueness
follows because the identity must hold for every integrable polynomial
source `F`; hence its multiplier is pointwise `1-G_eta`. `QED`

The binomial choice is canonical under one precise criterion.  Among all
polynomials `q` of degree at most `K` satisfying

```text
q(0)=1,                                             (2.15)
```

the unique one with a zero of order `K` at `t=1` is

```text
q(t)=(1-t)^K.                                       (2.16)
```

Indeed, the multiplicity and degree force `q(t)=c(1-t)^K`, and (2.15) gives
`c=1`.  Thus the beta remainder is the maximally endpoint-vanishing member of
the finite linear class; it is not the only conceivable nonlinear or
infinite backshift.

## 3. Shift-operator form on one exterior face

Use the positive-face notation of E101.066.  For a finite sequence `c`, let
`T` denote the right shift

```text
(T^m c)_(j+m)=c_j.                                  (3.1)
```

Let

```text
Ecal(c)=sum_j c_jm(d_(N+j)),                        (3.2)

Scal_m(c)=a sum_j c_j[s_(N+j+m)-s_(N+j)]
                    V_z(d_(N+j+m))/b.              (3.3)
```

E101.066(3.3) is

```text
I_m^+(c)=p_zEcal(T^m c)/b-Scal_m(c).                (3.4)
```

Define

```text
G_K(T)=sum_(m=1)^K gamma_(K,m)T^m
      =I-(I-T)^K,                                   (3.5)

Scal_K(c)=sum_(m=1)^K gamma_(K,m)Scal_m(c).         (3.6)
```

### Theorem 3.1 - Exact cancellation identity

The one-face beta remainder satisfies

```text
R_K^+(c)
=p_zEcal((I-T)^Kc)/b+Scal_K(c).                    (3.7)
```

### Proof

Sum (3.4) with the weights (2.4) and use (3.5):

```text
sum_m gamma_(K,m)I_m^+(c)
=p_zEcal(G_K(T)c)/b-Scal_K(c).                     (3.8)
```

The zeroth pairing is

```text
I_0^+(c)=p_zEcal(c)/b.                              (3.9)
```

Subtract (3.8) from (3.9), apply Theorem 2.1, and use
`I-G_K(T)=(I-T)^K`. `QED`

Equation (3.7) is the autopsy.  The apparent high-order remainder is exactly
the dual action on the high finite difference of the source, plus the full
symbol-increment correction.  Substituting (3.7) into (2.5) recovers (3.9)
identically.  No radical term has been created.

For the negative face, reverse the mesh, retain the leading signs
`-A^-C^-+B^-D^-`, and apply the same proof.  The right-bordered bilateral
identity is the sum of that formula over `j>=1` and (3.7) over the positive
face `j>=2`.  Equivalently it follows directly by applying Theorem 2.1 to
(2.11).  The selected column `N+1` is never inserted into the exterior sum;
using a symmetric `j>=1` formula instead requires the correction E101.065(4.4).

The same autopsy classifies every finite linear choice in Theorem 2.2.  Put

```text
Scal_eta(c)=sum_(m=1)^K eta_m Scal_m(c).            (3.10)
```

Equations (3.4) and (2.13)--(2.14) give

```text
sum_(m=1)^K eta_m I_m^+(c)
=p_zEcal(G_eta(T)c)/b-Scal_eta(c),                  (3.11)

R_eta^+(c)
=p_zEcal(q_eta(T)c)/b+Scal_eta(c).                 (3.12)
```

Substitution into (2.14) recovers (3.9).  Hence no universal finite linear
combination of radial shifts creates a new radical identity.  New content
must relate the particular arithmetic source or test module to the shift;
changing the coefficients `eta_m` only changes the polynomial partition of
the same scalar.

## 4. Fixed-order singular-mode test

In the symmetric finite family of E101.061--E101.066, the singular mode

```text
P=p_(-1)+p_1                                        (4.1)
```

has coefficient

```text
-m/[2b(m+2)(m+3)]                                   (4.2)
```

in `I_m^+`.  The following sum is exact.

### Lemma 4.1

For every `K>=1`,

```text
sum_(m=1)^K gamma_(K,m)
                 m/[(m+2)(m+3)]
=2K/[(K+1)(K+2)(K+3)].                             (4.3)
```

### Proof

Use

```text
m/[(m+2)(m+3)]=-2/(m+2)+3/(m+3)                   (4.4)
```

and the beta identity

```text
sum_(m=0)^K(-1)^m binom(K,m)/(m+a)
=Beta(a,K+1).                                       (4.5)
```

The `m=0` contribution in (4.3) is zero.  Equations (4.4)--(4.5) reduce the
left side to

```text
2Beta(2,K+1)-3Beta(3,K+1),                          (4.6)
```

which is (4.3). `QED`

### Corollary 4.2

The singular coefficient in the shifted sum of (2.5) is

```text
-K P/[b(K+1)(K+2)(K+3)].                           (4.7)
```

For every fixed `K`, it diverges like `1/delta`.  Since the singular mode in
`I_0^+` cancels, `R_K^+` contains the opposite divergent coefficient.

This is a universal finite-algebra falsifier using the symmetric right-border
coordinate.  It does not exclude a relation special to the true arithmetic
exterior source.  It proves that the beta factor in (2.10), by itself, cannot
be promoted to a cofinal estimate.

## 5. Growing order does not close automatically

The coefficient in (4.7) is of order `P/K^2`, but the absolute binomial mass
is

```text
sum_(m=1)^K |gamma_(K,m)|=2^K-1.                   (5.1)
```

Allowing `K=K_N` to grow is therefore not ruled out, but it requires a signed
source theorem which controls the complete combination before absolute
values.  Separate estimates on the `K_N` shifted pairings replace one
ill-conditioned scalar by an exponentially weighted family and are rejected.

Likewise, pointwise decay of `Beta(r+j,K+1)` does not control (2.9) when the
dual polynomial coefficients grow.  The exact family in Section 4 shows that
the remainder can retain the entire singular mode.

There is nevertheless one valid fixed-integrand statement which must not be
discarded.

### Proposition 5.1 - Fixed-integrand beta convergence

If `F` satisfies (2.2), then

```text
R_K->0 as K->infinity.                              (5.2)
```

### Proof

For every `0<t<=1`, `(1-t)^K->0`, while

```text
|(1-t)^K F(t)/t|<=|F(t)|/t.                         (5.3)
```

The right side is integrable by (2.2), so dominated convergence applied to
(2.6) proves (5.2). `QED`

This proposition does not apply directly to the cofinal terminal family,
because its integrand depends on `N,z` through the dual row.  A sufficient
uniform replacement is the following.  Let `F_u`, `u in U`, be a family such
that

```text
sup_(u in U) integral_0^1 |F_u(t)|dt/t<infinity,    (5.4)

lim_(epsilon->0) sup_(u in U)
 integral_0^epsilon |F_u(t)|dt/t=0.                (5.5)
```

Then

```text
sup_(u in U) |R_K(F_u)|->0.                         (5.6)
```

Indeed, split the integral at `epsilon`.  The first part is uniformly small
by (5.5), while the second is at most

```text
(1-epsilon)^K/pi
  sup_(u in U) integral_epsilon^1 |F_u(t)|dt/t.    (5.7)
```

The same criterion applied to `partial_z F_u` gives one safe derivative.
Thus a cofinal choice `K=K_N` needs a predeclared uniform-integrability
estimate for the complete signed four-channel family, including its
`z` derivative.  A value of `K_N` fitted after inspecting the terminal row
or its scalar pairing supplies no such theorem.  Uniform boundedness in
`L^1(dt/t)` alone is insufficient: mass can concentrate at `t=0`, precisely
where `(1-t)^K` has not decayed.

The archive already contains the structural warning behind this result.
E73.276--E73.277 reject a second Abel transform when its residual slot merely
restates the target; E82.005 and E83.004--E83.007 reject termwise tail
estimates which destroy the signed recombination; E84.003--E84.004 isolate
the same endpoint concentration; E91.004 and E96.005 reject exact
coboundaries whose boundary value is the original scalar.  The beta formula
is a new terminal-exterior coordinate for that issue, not a new principle
which bypasses it.  Its genuinely additional content is the exact
classification in Theorems 2.2 and 3.1 and the explicit singular-mode test
in Section 4.

## 6. Refined source-shift target

The entire universal finite linear class has now been evaluated.  This does
not classify nonlinear backshifts, infinite series, or identities special to
the arithmetic source.  What is missing is a bilinear operator identity
special to the full arithmetic source class and valid on a test module fixed
before the terminal dual row.

Let `S_rad` and `T_rad` be source and test modules fixed independently of
`N,z,p`.  For a build `B`, `x in S_rad` and `phi in T_rad`, let

```text
J_(B,m)^(N)(x,phi)                                  (6.1)
```

denote the unnormalized four-channel Abel shift obtained from the exterior
coefficients of `x` and the row coefficients of `phi` in build `B`.  For the
arithmetic source `kappa_Z` and

```text
phi_(B,N,z)=R_N^*[p_(B,N,z)/b_(B,N,z)],             (6.2)
```

the normalized terminal moment is

```text
I_(B,m)=J_(B,m)^(N)(kappa_Z,phi_(B,N,z))/alpha_N.   (6.3)
```

A non-reversible theorem must use one construction rule for every build `B`.
It must construct in advance an explicit test operator
`A_(N,K):T_rad->T_rad` and explicit bilinear boundary forms
`Bcal_(B,N,K):S_rad x T_rad->C` such that, for every `x,phi`,

```text
sum_(m=1)^K gamma_(K,m)J_(B,m)^(N)(x,phi)
=Q_B(x,A_(N,K)phi)+Bcal_(B,N,K)(x,phi).            (6.4)
```

Existence alone is vacuous: one could take `A=0` and define `Bcal` to be the
left side.  The admissible construction must satisfy all of

```text
A_(N,K) is a prescribed composition of source-independent shifts,
compressions and endpoint maps;

Bcal_(B,N,K) is derived by the same build-covariant rule as the corresponding
explicit endpoint, border and shell commutator before x or phi is selected;

the formula for Bcal contains no J_(B,m), Abel dual polynomial, terminal
Cauchy kernel, p_(N,z), q_(N,z), or fitted safe value;

Bcal has an independently proved source estimate on S_rad x T_rad;

A_(N,K)phi is admissible for the radical identity.                  (6.5)
```

For `B=Z` and `x=kappa_Z`, the first term on the right of (6.4) then vanishes.
Keeping the same `kappa_Z` and setting `B=P` must replace it by the explicit
quartet evaluation of `A_(N,K)phi`.  The difference between the two boundary
forms must also be explicit and independently controlled.  Nonvanishing of
the total controlled-build response for the actual tests remains a separate
obligation.

In addition, the right-bordered beta remainder from (2.11) needs an
independent one-way certificate.  Merely naming the assertion
`R_(K_N,rb)->0` does not reduce the problem: once the shifted sum is known to
vanish, (2.5) makes that assertion exactly equivalent to `I_(0,rb)->0`.

An admissible certificate must derive, before the terminal row is selected,
an explicit boundary-local representation or a quantitative estimate in a
predeclared source/test topology which contains neither `I_(0,rb)` nor the
terminal Cauchy kernel.  Theorem 3.1 shows that separate estimates do not
follow from universal algebra and may destroy cancellation.  It does not
exclude special arithmetic estimates which independently make both terms in
(3.7) small.

This refines `RSB-1`--`RSB-5` into two concrete open modules:

```text
RSB-SHIFT:
  prove the bilinear shifted-test representation (6.4)--(6.5), with the
  normalization (6.2)--(6.3);

RSB-BETA:
  construct the independent one-way beta certificate just specified,
  retaining (3.7) as one signed object unless arithmetic estimates prove
  its two terms separately small.                                      (6.6)
```

If both modules hold for the four-channel current (2.11), with the
normalization (6.2)--(6.3) and a nonzero actual quartet response, Theorem 2.1
and E101.065 yield the terminal secant.  Without the independent beta
certificate, `RSB-BETA` is only DIRECTIONAL-IDENT in another coordinate.
Neither module currently follows from the radical identity or from formal
multiple-orthogonality theory.

E101.068 subsequently constructs the finite shifted-test representation in
(6.4) by an exact bilateral Loewner factorization.  Its boundary contains the
entire complement of each face and, on the radical, equals the shifted sum
itself.  Thus the representation part is closed while the locality and
independent-estimate clauses of (6.5) remain open under the sharper name
`ARITHMETIC-LOEWNER-DISCRIMINANT`.  E101.069 imports the existing Pearson,
Christoffel and Geronimus machinery and confirms that none of it supplies
that arithmetic discriminant.

## 7. Status

```text
proved:
  universal binomial backshift identity;
  beta-product formula for its remainder;
  classification of every universal finite linear backshift;
  exact shifted-source cancellation identity;
  fixed-order survival of the singular dual mode;
  fixed-integrand beta convergence and its uniform cofinal gate;

rejected:
  every universal finite linear backshift as new force-bearing content;
  separate absolute estimates on its shifted rows;
  beta-kernel decay without the coupled source and dual coefficients;

open:
  the estimate and discrimination part of RSB-SHIFT, RSB-BETA,
  the actual quartet response,
  DIRECTIONAL-IDENT and Omega7.
```
