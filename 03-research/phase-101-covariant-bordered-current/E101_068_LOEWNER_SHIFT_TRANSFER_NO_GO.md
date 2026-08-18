# E101.068 - Loewner shifted-test transfer and radical conservation law

## 1. Result

E101.067 leaves a precise algebraic question: can the shifted Abel rows be
transferred to a test fixed before the terminal dual row, so that the full
radical annihilates the main term?

The answer is exact and bilateral.  Such a transfer exists for every finite
linear combination of shifts.  It is forced by the Loewner kernel and uses
only a translated test plus an explicit symbol commutator.  The same
calculation also gives its limitation:

```text
on an exact radical, the whole shifted sum is conserved in the purported
boundary term.                                                       (1.1)
```

Thus the algebraic construction part of `RSB-SHIFT` is closed, but radicality
does not estimate it.  Any advance must prove a new arithmetic estimate for
the complete commutator boundary, or a build-discriminating relation which
prevents the corresponding controlled-build cancellation.

## 2. Bilateral CCM setting and its Loewner exterior

Put

```text
d_n=hn,
h=2pi/L,
a=2/L.                                               (2.1)
```

For a build `B`, let `s_B(d)` be its odd sine symbol and `c_B(d)` its even
cosine symbol.  Write

```text
s_(B,n)=s_B(d_n),
c_(B,n)=c_B(d_n).                                   (2.2)
```

At a fixed comparison level `mu`, the complete CCM kernel is

```text
M_B(n,j)=-a [s_(B,n)-s_(B,j)]/[d_n-d_j], n!=j,

M_B(n,n)=2c_(B,n)-a s_B'(d_n)-mu.                  (2.3)
```

Equivalently, if the diagonal of `Loew(s_B)` is `s_B'`,

```text
M_B=2diag(c_B)-a Loew(s_B)-mu I.                   (2.4)
```

The cosine term in (2.3) is essential whenever the full radical is used.
The exterior rectangles below contain no diagonal entries, so their transfer
algebra uses only the off-diagonal part of (2.3).  Omitting the cosine term
from the full pairing would replace the CCM operator by a different kernel
and would invalidate the radical identity in Section 5.

The finite row set and the two actual right-bordered exterior faces are

```text
I_N={-N,...,N},
T_N^+={j:j>=N+2},
T_N^-={j:j<=-N-1}.                                  (2.5)
```

Let `P_N^sigma` be the coefficient projection onto `T_N^sigma`, where
`sigma` is `+1` or `-1`.  Let `U` be the bilateral lattice shift

```text
Ue_j=e_(j+1).                                       (2.6)
```

For a finitely supported source `x` and test row `phi`, write

```text
Q_B(x,phi)=phi M_Bx.                                (2.7)
```

All identities below are first finite.  They pass to the completed source
and test modules only when the displayed pairings converge and translations
by `U` preserve the test module.

For `m>=0`, define the raw radial-shift kernel on face `sigma` by

```text
L_(B,m)^sigma(n,j)
=-a [s_(B,n)-s_(B,j)]/[d_n-d_(j+sigma m)],
j in T_N^sigma.                                     (2.8)
```

For `sigma=+1`, set `n=N-r` and `j=N+q`; for `sigma=-1`, set
`n=r-N` and `j=-N-q`.  Equation (2.8) then has denominator `r+q+m`
with exactly the signs in

```text
A^+C^+-B^+D^+-A^-C^-+B^-D^-.                       (2.9)
```

Consequently

```text
J_(B,m)^sigma(x,phi)
=phi L_(B,m)^sigma P_N^sigma x                    (2.10)
```

is the unnormalized face contribution of the `t^m` Abel pairing.  No extra
global sign is attached to the negative face.

## 3. Two exact shift factorizations

Define

```text
C_(B,m)^sigma(n,j)
=a [s_(B,j+sigma m)-s_(B,j)]
   /[d_n-d_(j+sigma m)],                            (3.1)

D_(B,m)^sigma(n,j)
=-a [s_(B,n)-s_(B,n-sigma m)]
    /[d_n-d_(j+sigma m)].                           (3.2)
```

### Theorem 3.1 - Bilateral source and test transfer

On `I_N x T_N^sigma`, one has

```text
L_(B,m)^sigma
=M_BU^(sigma m)-C_(B,m)^sigma
=U^(sigma m)M_B+D_(B,m)^sigma.                     (3.3)
```

Here the two translated kernels mean

```text
(M_BU^(sigma m))(n,j)=M_B(n,j+sigma m),
(U^(sigma m)M_B)(n,j)=M_B(n-sigma m,j).             (3.4)
```

### Proof

The first denominator in (3.4) is

```text
d_n-d_(j+sigma m),                                  (3.5)
```

the denominator of (2.8).  Subtracting its numerator from the numerator of
(2.8) leaves

```text
-a[s_(B,j+sigma m)-s_(B,j)],                        (3.6)
```

which is `-C_(B,m)^sigma`.

For the second identity, the lattice relation

```text
d_(n-sigma m)-d_j=d_n-d_(j+sigma m)                 (3.7)
```

again gives the same denominator.  The difference of the two numerators is

```text
-a[s_(B,n)-s_(B,n-sigma m)],                        (3.8)
```

which is `D_(B,m)^sigma`. `QED`

The first equality is the shifted-source formula of E101.066.  The second is
the missing shifted-test formula.  It displays the exact price for moving a
radial factor from the source column to the test row.

## 4. Arbitrary finite shifted-test transfer

Fix coefficients `eta_1,...,eta_K` before choosing `x` or `phi`, and put

```text
G_eta^sigma(U)=sum_(m=1)^K eta_m U^(sigma m),
D_(B,eta)^sigma=sum_(m=1)^K eta_m D_(B,m)^sigma.    (4.1)
```

Define the translated test

```text
A_eta^sigma phi=phi G_eta^sigma(U),
(phi U^(sigma m))_r=phi_(r+sigma m).                (4.2)
```

### Theorem 4.1 - Exact source-first representation

For every finite source and test,

```text
S_(B,eta)^sigma(x,phi)
:=sum_(m=1)^K eta_m J_(B,m)^sigma(x,phi)

=Q_B(P_N^sigma x,A_eta^sigma phi)
 +phi D_(B,eta)^sigma P_N^sigma x                  (4.3)

=Q_B(x,A_eta^sigma phi)
 +Bcal_(B,eta)^sigma(x,phi),                        (4.4)
```

where

```text
Bcal_(B,eta)^sigma(x,phi)
=-Q_B((I-P_N^sigma)x,A_eta^sigma phi)
 +phi D_(B,eta)^sigma P_N^sigma x.                 (4.5)
```

### Proof

Multiply the second factorization in (3.3) by `eta_m`, sum in `m`, and pair
with `phi` and `P_N^sigma x`.  Moving `U^(sigma m)` onto the row gives
(4.2), proving (4.3).  Add and subtract
`Q_B((I-P_N^sigma)x,A_eta^sigma phi)` to obtain
(4.4)--(4.5). `QED`

The bilateral formula is obtained by summing the two faces.  Set

```text
A_eta=A_eta^++A_eta^-,
Bcal_(B,eta)=Bcal_(B,eta)^++Bcal_(B,eta)^-,
S_(B,eta)=S_(B,eta)^++S_(B,eta)^-.                 (4.6)
```

Then

```text
S_(B,eta)(x,phi)
=Q_B(x,A_eta phi)+Bcal_(B,eta)(x,phi).             (4.7)
```

If `P_J=I-P_N^+-P_N^-`, the boundary form can be displayed without hidden
cross terms as

```text
Bcal_(B,eta)
=-Q_B((P_J+P_N^-)x,A_eta^+phi)
 -Q_B((P_J+P_N^+)x,A_eta^-phi)
 +phi D_(B,eta)^+P_N^+x
 +phi D_(B,eta)^-P_N^-x.                           (4.8)
```

This is why the two shifted tests may be added in (4.6): each full-source
action uses the same `x`, while every opposite-face cross term remains in
(4.8).

This is build-covariant and source-first.  The operators in (4.1)--(4.2) are
prescribed lattice translations.  The boundary form (4.5) is an explicit
interior-complement plus symbol-commutator formula derived before `x` and
`phi` are selected.  It contains no fitted scalar and no terminal Cauchy
kernel.

It is not yet the boundary-local object required by E101.067(6.5).
Equation (4.8) contains actions on the entire complement of each face, and
no independent estimate for their signed sum has been proved.  Moreover,
the shifted tests generally leave the finite row window.  Formula (4.7)
therefore lives naturally in the complete build; a finite compression needs
its own explicit row-collar correction.

## 5. Radical conservation no-go

Let `kappa_Z` be the complete arithmetic radical, so that

```text
Q_Z(kappa_Z,psi)=0                                  (5.1)
```

for every admissible test `psi`.  Assume the finite translations in (4.2)
preserve that admissible test module.

### Theorem 5.1 - Shifted mass is conserved in the boundary

For every finite coefficient family `eta`,

```text
S_(Z,eta)(kappa_Z,phi)
=Bcal_(Z,eta)(kappa_Z,phi).                         (5.2)
```

### Proof

Apply (5.1) to `psi=A_eta phi` in (4.7). `QED`

The conclusion is stronger than the autopsy of the binomial choice: every
finite linear shifted-test transfer has the same conservation law.  The
radical annihilates the full-source term, but does not annihilate any part of
the original shifted pairing.  It moves that pairing exactly into (4.5).

More generally, suppose any exact representation has the form

```text
S_(B,eta)(x,phi)=Q_B(x,Aphi)+Bcal_B(x,phi),         (5.3)
```

with `Aphi` admissible.  On a radical, (5.3) forces

```text
Bcal_Z(kappa_Z,phi)=S_(Z,eta)(kappa_Z,phi).         (5.4)
```

This conclusion is independent of how `A` was found.  Therefore no argument
using only exact transfer and radical annihilation can prove smallness of the
shifted sum.  Calling (4.5) a boundary or commutator does not estimate it.

The theorem is a no-go for an algebra-only proof, not for an arithmetic
estimate of (4.5).  Such an estimate would be genuine new content if it were
proved in a topology fixed before the terminal test and retained the two
faces as one signed object.

For a growing order `K_N`, admissibility is an additional obstruction.  In
the binomial case the bilateral shift on `ell^2(Z)` satisfies

```text
||G_K(U)||
=sup_(|zeta|=1)|1-(1-zeta)^K|
=2^K-1,                                             (5.5)
```

because equality is attained at `zeta=-1`.  Thus fixed-order preservation of
the test module does not imply a uniform bound for `K=K_N`.  This is the
operator form of the coefficient growth in E101.067(5.1).

## 6. Binomial specialization and the remaining scalar

Take

```text
eta_m=gamma_(K,m)=(-1)^(m+1)binom(K,m).             (6.1)
```

After choosing the normalized arithmetic exterior source and the lifted
terminal row of E101.067, Theorem 2.1 there and (5.2) give

```text
I_0
=S_(Z,gamma)+R_K
=Bcal_(Z,gamma)+R_K.                               (6.2)
```

Equation (6.2) is exact.  It proves three separate facts.

First, the shifted-test representation requested in E101.067 exists at the
finite algebraic level.  Second, the radical does not make its boundary form
small.  Third, even an independent cofinal proof `R_(K_N)->0` leaves

```text
Bcal_(Z,gamma)->0                                  (6.3)
```

as the complete remaining scalar burden.  In view of (6.2), once the beta
remainder is small, (6.3) is equivalent to `I_0->0`.  Thus growing binomial
order can close the beta module but cannot lower the force of the boundary
module.

For a fixed integrand, E101.067 proves `R_K->0` by dominated convergence.
For the cofinal family it requires uniform integrability near `t=0`, with the
same statement for one safe derivative.  That condition is a legitimate
independent beta target; it is not a substitute for (6.3).

For the infinite radical, every use of (6.2) must first truncate the source
with `N,K` fixed and then justify the completed limit.  Algebra on a finite
truncation does not supply that convergence.

## 7. Controlled-build discriminant

Keep `kappa_Z` fixed, keep the comparison level fixed, and insert a
controlled quartet into a build `P`.  Both symbols in (2.3) must be changed.
The same transfer rule gives

```text
S_(P,eta)(kappa_Z,phi)
=Q_P(kappa_Z,A_eta phi)
 +Bcal_(P,eta)(kappa_Z,phi).                        (7.1)
```

The first term is the explicit quartet functional evaluated on the shifted
test.  Subtracting (5.2) yields

```text
S_(P,eta)-S_(Z,eta)
=Quartet_P(kappa_Z,A_eta phi)
 +Bcal_(P,eta)-Bcal_(Z,eta).                       (7.2)
```

The quartet term alone does not prove discrimination: the boundary
difference in (7.2) can cancel it.  A valid forcing theorem must therefore
prove, by one build-covariant rule, either

```text
the boundary difference has a controlled limit which does not cancel the
actual quartet response; or

the arithmetic boundary satisfies an identity unavailable to the inserted
quartet build.                                      (7.3)
```

This locates the new mathematics in a build-discriminating arithmetic
commutator law, not in the universal shift transfer.

## 8. Relation to earlier no-go results

Theorem 5.1 is the terminal-exterior version of several earlier warnings.
E73.276--E73.277 show that an Abel residual slot is vacuous when it retains
the target; E82.005 and E83.004--E83.007 require the full signed source before
tail estimates; E84.003--E84.004 isolate endpoint concentration; E91.004 and
E96.005 reject exact coboundaries whose boundary value is the desired scalar.
E101.065 proves the corresponding secant circle without shifts.

What is new here is the exact bilateral identity (3.3), its arbitrary finite
linear transfer (4.7), and the conservation law (5.2) on the right-bordered
four-channel current.  What is not new is the hope that a formal transfer or
an exact coboundary estimates its own boundary.

The following family is now frozen:

```text
universal finite linear Abel shifts;
source shifts without their symbol correction;
test shifts without their Loewner commutator;
radical annihilation used as an estimate of Bcal;
quartet nonvanishing without the boundary-difference audit.            (8.1)
```

## 9. Revised target

The two open modules of E101.067 reduce to one force-bearing target and one
independent auxiliary target:

```text
ARITHMETIC-LOEWNER-DISCRIMINANT:
  derive from the complete Gamma--Euler source an identity or signed estimate
  for Bcal_(Z,eta), fixed before the terminal row, whose controlled-build
  version satisfies the noncancellation obligation (7.3);

UNIFORM-BETA-ENDPOINT:
  prove the uniform-integrability criterion of E101.067 for the complete
  four-channel cofinal family and one safe derivative.                 (9.1)
```

The second target may remove `R_(K_N)`.  Only the first can carry the
remaining force.  It may use an infinite or nonlinear shift law, but it must
survive Theorem 5.1 and the controlled-build audit.

## 10. Status

```text
proved:
  bilateral source-shift and test-shift factorizations;
  exact source-first transfer for arbitrary finite linear shifts;
  radical conservation of the complete shifted sum in the boundary form;
  exact controlled-build difference formula;

closed as algebra:
  the finite construction portion of RSB-SHIFT;

rejected:
  radicality alone as a bound for the transferred boundary;
  universal finite linear shifts as force-bearing mathematics;
  an unaudited quartet term as proof of build discrimination;

open:
  ARITHMETIC-LOEWNER-DISCRIMINANT, UNIFORM-BETA-ENDPOINT,
  DIRECTIONAL-IDENT and Omega7.

correction carried by E101.071:
  every full radical pairing uses the complete CCM kernel (2.3), including
  its cosine-symbol diagonal; the exterior shift algebra itself is unchanged.
```
