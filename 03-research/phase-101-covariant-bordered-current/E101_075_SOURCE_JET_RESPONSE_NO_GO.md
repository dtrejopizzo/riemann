# E101.075 - Source-jet quartet response and differentiated-radical no-go

## 1. Decision

E101.074 shows that the fixed radical is blind on its own divisor.  The most
canonical repair is to multiply the source by powers of position, producing
derivatives of its transform.  This does remove pointwise divisor blindness:
at a zero of multiplicity `m`, the `m`-th source jet is nonzero.

The repair does not produce a second radical.  Its exact operator identity
is an inhomogeneous commutator, and subtracting that commutator returns
tautologically to the original radical equation.  Moreover, the jet responds
to critical and off-line zeros alike and carries the complete zero
background.

Thus source jets are valid auxiliary probes of multiplicity but not, by
themselves, a discriminant for Omega7.  A viable use would require a new
root-free arithmetic current which controls the full commutator and cancels
the on-line background without zero localization.

## 2. Position and translation generators are different

Use the Fourier convention

```text
K(t)=F[k](t)=integral_R k(x)exp(-itx)dx.            (2.1)
```

For the arithmetic source,

```text
K=Xi.                                               (2.2)
```

Define

```text
Xf(x)=xf(x),
Af(x)=-i partial_x f(x).                            (2.3)
```

Then

```text
F[X^r k](t)=i^r K^((r))(t),                        (2.4)

F[A^r k](t)=t^rK(t).                               (2.5)
```

Equation (2.4) follows by differentiating (2.1); equation (2.5) follows by
integration by parts.

The consequences are opposite:

```text
X^r k detects transform jets but is not a radical;
A^r k remains a radical but detects no new divisor information.       (2.6)
```

Calling `A` a source-jet generator for `Xi'` would confuse two Fourier-dual
operators.

## 3. Exact finite-interval jet source

Put

```text
a=L/2,
d_n=2pi n/L,
f_r(y)=(y-a)^r k(y-a),

kappa_n^((r))(L)
=(1/L)integral_0^L f_r(y)exp(-id_ny)dy.             (3.1)
```

Let

```text
K_L(t)=integral_(-a)^a k(x)exp(-itx)dx.             (3.2)
```

Changing variables in (3.1) gives

```text
integral_0^L f_r(y)exp(-ity)dy
=exp(-itL/2)i^r K_L^((r))(t).                      (3.3)
```

In Fourier coefficient space, multiplication by `y-a` has the bilateral
matrix

```text
(X_L)_(m,n)=1/[i(d_n-d_m)], m!=n,
(X_L)_(n,n)=0.                                     (3.4)
```

Hence, before finite compression,

```text
kappa^((r))=X_L^r kappa^((0))                      (3.5)
```

in `ell^2` on the natural domain.

For a finite projection `P_N`, one does not have

```text
P_NX_L^r=(P_NX_LP_N)^rP_N.                         (3.6)
```

Every path in `X_L^r` which leaves and re-enters the section contributes a
Fourier collar.  Therefore a finite jet formula must retain the complete
right-bordered leakage.

## 4. Exact Cauchy factor of a jet

For `p` off the real lattice, define

```text
Ccal_p(v)=sum_(n in Z)v_n/(d_n-p).                  (4.1)
```

### Theorem 4.1 - Periodic jet evaluation

One has

```text
Ccal_p(kappa^((r)))
=-i^r K_L^((r))(p)/[2sin(pL/2)].                   (4.2)
```

### Proof

The periodic Green identity of E101.050 gives

```text
sum_n exp(-id_ny)/(d_n-p)
=-iL exp(-ipy)/[1-exp(-ipL)]                       (4.3)
```

with the equivalent boundary-value convention obtained by reversing both
denominators.  Insert (3.1), interchange the absolutely convergent Cauchy
sum with the integral, and use (3.3).  The elementary identity

```text
1-exp(-ipL)=2i exp(-ipL/2)sin(pL/2)                (4.4)
```

gives (4.2). `QED`

The sign in (4.2) agrees with the convention `d_n-p` in (4.1).  Changing to
`p-d_n` changes the global sign.

## 5. Exact quartet response of a source jet

For the quartet of E101.071,

```text
delta M=sum_(p in P_zeta)K_pR_pR_p^T,

K_p=a chi[1-cos(pL)]/2,
R_p(n)=1/(d_n-p).                                   (5.1)
```

### Theorem 5.1

The action of the controlled quartet on the `r`-th source jet is

```text
delta M kappa^((r))
=-(a chi i^r/2)sum_(p in P_zeta)
  sin(pL/2)K_L^((r))(p)R_p.                        (5.2)
```

### Proof

From (5.1),

```text
delta M kappa^((r))
=sum_p K_p R_p Ccal_p(kappa^((r))).                (5.3)
```

Insert (4.2) and use

```text
[1-cos(pL)]/[2sin(pL/2)]=sin(pL/2).                (5.4)
```

This gives (5.2). `QED`

Equation (5.2) is a complete finite-interval factorization.  It is
source-first and uses no zero location in constructing `kappa^((r))`.

## 6. Multiplicity detection

Suppose `rho` is a zero of `K` of multiplicity `nu`:

```text
K(t)=(t-rho)^nu g_rho(t),
g_rho(rho)!=0.                                     (6.1)
```

Then

```text
K^((r))(rho)=0, r<nu,
K^((nu))(rho)=nu!g_rho(rho)!=0.                    (6.2)
```

Thus the first position jet which detects the point is `X^nu k`.

No fixed finite order detects arbitrary unknown multiplicity.  Selecting
`r=nu` after learning `nu` violates the source-first rule.  A
multiplicity-safe jet package must retain an infinite predetermined family,
or supply an independent uniform multiplicity bound.

Such a bound cannot be replaced by an assumption that every zero is simple.
Simplicity is not known and is stronger than what Omega7 asks.

## 7. The inhomogeneous commutator identity

Let `W_Z` denote the complete Weil operator and suppose

```text
W_Zk=0.                                             (7.1)
```

### Theorem 7.1 - Differentiated radical identity

For every `r` on the common domain,

```text
W_ZX^rk=[W_Z,X^r]k                                 (7.2)
```

and

```text
W_ZX^rk
=sum_(q=1)^r binom(r,q)
 X^(r-q) ad_X^q(W_Z)k.                             (7.3)
```

### Proof

Expand

```text
[W_Z,X^r]k=W_ZX^rk-X^rW_Zk                        (7.4)
```

and use (7.1), proving (7.2).  The standard iterated-commutator expansion
gives (7.3). `QED`

The apparently corrected identity

```text
W_ZX^rk-[W_Z,X^r]k=0                               (7.5)
```

is exactly

```text
X^r(W_Zk)=0.                                       (7.6)
```

It is a differentiated form of the original radical equation, not an
independent constraint.

In the formal spectral coordinate

```text
mu_Z=sum_rho m_rho delta_rho,                       (7.7)
```

the first commutator differentiates the divisor distribution.  Since
`K(rho)=0`, multiplication of `mu_Z'` by `K` produces the weights
`K'(rho)`.  This explains the jet response, but does not remove the full
divisor sum.

## 8. Why the jet is not a new radical

In the spectral representation,

```text
Q_Z(X^rk,phi)
=i^r sum_rho m_rho K^((r))(rho)Phi_phi(rho).        (8.1)
```

For `r>=1`, the right side generally contains contributions from every zero
whose multiplicity is at most `r`.  In particular, `Xk` responds to all
simple critical zeros as well as to simple off-line zeros.

The jet therefore has neither of the two properties needed for the proposed
repair:

```text
it does not annihilate the arithmetic build;
it does not distinguish critical from off-line zeros.                (8.2)
```

By contrast, `A^rk` remains radical because of (2.5), but multiplication of
`K` by `t^r` preserves every zero and gives no multiplicity detector.  Its
operator identity is an integration-by-parts transfer to the test.

There is also a general factorization no-go.  If an entire transform `F`
vanishes at every zero of `Xi` with at least the same multiplicity, then

```text
F=Xi G                                             (8.3)
```

for an entire `G`.  On a test module stable under the corresponding
multiplication, the purported new radical identity is the original one with
a transformed test.  Powers of `Xi`, convolutions of `k`, and derivatives
which retain a factor `Xi` fall in this reversible class.

## 9. Endpoint and domain costs

The double-exponential decay of `k` places every polynomial jet in the
natural full-line domains.  Finite intervals introduce a different issue.

For odd `r`, parity gives

```text
f_r(L)-f_r(0)=2(L/2)^r k(L/2).                     (9.1)
```

Thus, for fixed `L`, one integration by parts gives only

```text
kappa_n^((r))=O_L(1/n), r odd.                     (9.2)
```

The source need not belong to `ell^1`, although its Cauchy pairing in (4.2)
still converges absolutely.  Even orders have matched endpoint values but
retain higher derivative mismatches.

Periodizing `x^r` or cutting it off repairs (9.2), but adds endpoint
commutators and no longer produces exactly `K^((r))`.  Those terms must be
kept with the right-bordered Fourier collar.

One must also prove locally uniform convergence

```text
K_L^((r))->K^((r))                                 (9.3)
```

with the exponential weights required at nonreal poles before passing from
(5.2) to a completed divisor statement.

## 10. Prior no-go cross-check

The internal archive already blocks the obvious jet shortcuts:

```text
E72.360:
  a holomorphic test against Xi'/Xi extracts multiplicity times a value,
  not the higher Hermite slots;

E72.359:
  higher principal-part projectors require inverse Xi and zero localization;

E74.021:
  smallness of the first Cauchy order does not propagate to higher orders;

E72.100--E72.105:
  derivative-normalized root currents retain an uncontrolled background;

E72.16 and E72.355:
  a universal zero filter or node-blind identity cannot be inserted as a
  source-independent forcing step.                                  (10.1)
```

No document in the audited range constructs `X^rk` as a second radical.
That absence is consistent with Theorem 7.1: it would be mathematically
incorrect.

## 11. Surviving new-mathematics target

The only jet-sensitive target not already rejected is

```text
ROOT-FREE-JET-CURRENT:

construct from the Gamma--Euler side a signed current for the predetermined
family {X^rk} which

1. uses no inverse Xi, zero position or multiplicity input;
2. controls the complete commutator [W_Z,X^r] including both endpoints and
   every Fourier collar;
3. cancels the full critical-line background by an exact arithmetic
   identity rather than positivity;
4. leaves a nonzero response for every off-line quartet;
5. feeds the actual terminal tests in DIRECTIONAL-IDENT.              (11.1)
```

Theorem 7.1 does not supply item 3: subtracting its commutator cancels the
entire jet response.  A determinant or Wronskian coupling the radical and
jet channels is a possible form of item 3, but no such identity has been
proved.

## 12. Status

```text
proved:
  exact distinction between position jets and translation-generator powers;
  exact finite Fourier jet operator and its compression collar;
  periodic Cauchy evaluation of every source jet;
  exact rank-four quartet response formula;
  multiplicity detection order;
  inhomogeneous commutator identity and its tautological correction;
  odd-jet endpoint tail obstruction;

rejected:
  Xi' as a new radical;
  generator powers as multiplicity detectors;
  a fixed finite jet order for unknown multiplicity;
  the corrected commutator as independent information;
  jet response alone as a critical-line discriminator;

open:
  ROOT-FREE-JET-CURRENT,
  an independent background-cancelling jet relation,
  DIRECTIONAL-IDENT and Omega7.
```
