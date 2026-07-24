# E101.065 - Source-adapted exterior identity and the terminal secant circle

## 1. Purpose

The bilateral Abel formula of E101.060 keeps the complete exterior source
coupled to the actual dual row.  This is the correct order of operations, but
an exact source-adapted evaluation can still fail to advance the proof if it
returns the terminal secant itself.

This document proves that this is exactly what happens for the full radical
source.  It also fixes the asymmetric exterior indexing forced by the
right-bordered rectangular block.

## 2. Right-bordered decomposition

Let

```text
I_N={-N,...,N},
J_N={-N,...,N,N+1},
T_N=Z\J_N.                                           (2.1)
```

The finite row restriction of the full build is decomposed as

```text
r_N(kappa)
=M_N kappa_(J_N)+E_N kappa_(T_N),                   (2.2)

E_N kappa_(T_N)
=sum_(n in T_N) kappa_n m(d_n).                     (2.3)
```

Thus `r_N(kappa)` is the exact restricted residual of the complete source.
For an infinite coefficient source, (2.2)--(2.3) mean the limit of the finite
exterior truncations

```text
T_(N,R)=T_N intersect {-R,...,R},
E_(N,R)kappa=sum_(n in T_(N,R))kappa_n m(d_n).       (2.4)
```

The algebra below is first proved with `E_(N,R)`.  It passes to `E_N` whenever
`E_(N,R)kappa` converges in the finite row space.  Locally uniform statements
with one safe derivative additionally require convergence after pairing with
`p_(N,z)` and `partial_zp_(N,z)`.  The full Weil action supplies a completed
meaning for the arithmetic radical, but E101.060 by itself proves only the
finitely supported Abel formula.

Assume

```text
alpha_N=ell kappa_(J_N)!=0,
k_N=kappa_(J_N)/alpha_N,
b_(N,z)=c_z k_N!=0.                                 (2.5)
```

Let `y_N` be the normalized finite boundary vector and let `p_(N,z)` be its
dual row:

```text
M_N y_N=0,
ell y_N=1,
B_(y_N)(z)=c_z y_N,                                 (2.6)

p_(N,z)M_N=c_z-B_(y_N)(z)ell.                       (2.7)
```

No inverse of `M_N` occurs in these definitions.

## 3. Exact source-adapted secant theorem

Define the normalized complete exterior action

```text
Acal_(N,z)(kappa)
=p_(N,z)E_N kappa_(T_N)/(alpha_N b_(N,z)).          (3.1)
```

### Theorem 3.1

For every complete source `kappa`,

```text
Acal_(N,z)(kappa)
=p_(N,z)r_N(kappa)/(alpha_N b_(N,z))
 +B_(y_N)(z)/b_(N,z)-1.                             (3.2)
```

If `kappa` is an exact radical source for the build, so that

```text
r_N(kappa)=0,                                       (3.3)
```

then

```text
Acal_(N,z)(kappa)=B_(y_N)(z)/b_(N,z)-1.             (3.4)
```

### Proof

From (2.2),

```text
pE_N kappa_(T_N)
=p r_N(kappa)-pM_N kappa_(J_N).                    (3.5)
```

Equations (2.5) and (2.7) give

```text
pM_N kappa_(J_N)
=alpha_N[c_z k_N-B_(y_N)(z)ell k_N]
=alpha_N[b_(N,z)-B_(y_N)(z)].                       (3.6)
```

Substitution of (3.6) into (3.5), followed by division by
`alpha_N b_(N,z)`, proves (3.2).  Equation (3.4) follows from (3.3). `QED`

The theorem is build-covariant.  For discrimination, fix `kappa=kappa_Z`, the
arithmetic radical, while changing the build.  Then (3.3) holds for the
arithmetic build and generally fails after insertion of a quartet.  If the
source were changed together with the build to a new exact radical, (3.3)
would hold again and no discrimination would result.

## 4. Exact right-border correction in Abel coordinates

For the finite truncation `T_(N,R)`, the actual positive and negative exterior
source polynomials are

```text
C_(N,R)^+(t)=alpha_N^(-1)sum_(2<=j<=R-N)
                               kappa_(N+j)t^j,
C_(N,R)^-(t)=alpha_N^(-1)sum_(1<=j<=R-N)
                               kappa_(-N-j)t^j,     (4.1)

D_(N,R)^+(t)=alpha_N^(-1)sum_(2<=j<=R-N)
                         kappa_(N+j)s_(N+j)t^j,
D_(N,R)^-(t)=alpha_N^(-1)sum_(1<=j<=R-N)
                         kappa_(-N-j)s_(-N-j)t^j.   (4.2)
```

The lower bound differs on the two faces because the column `N+1` belongs to
the rectangular block.  Applying E101.060 with (4.1)--(4.2) gives the
truncated version of (3.1).  Passing `R->infinity` gives (3.1) only under the
convergence hypotheses stated after (2.4).  No infinite Abel interchange is
claimed without that passage.

Let `Acal_(N,z)^sym` denote instead the formally symmetric Abel expression
which starts both faces at `j=1`.  It includes one selected column too many.
Since

```text
p_(N,z)m(d_(N+1))
=q_(N,z),N+1,                                       (4.3)
```

the correction is

```text
Acal_(N,z)(kappa)
=Acal_(N,z)^sym
 -kappa_(N+1)q_(N,z),N+1/(alpha_N b_(N,z)).         (4.4)
```

For an exact radical, (3.4) and (4.4) give

```text
B_(y_N)(z)/b_(N,z)-1
=Acal_(N,z)^sym
 -kappa_(N+1)q_(N,z),N+1/(alpha_N b_(N,z)).         (4.5)
```

Thus the right-border term may not be hidden inside a parity convention.

## 5. Circle theorem

Put

```text
e_N=M_N k_N.                                        (5.1)
```

For an exact radical, (2.2) gives

```text
e_N=-E_N kappa_(T_N)/alpha_N.                       (5.2)
```

Consequently,

```text
Acal_(N,z)(kappa)
=-p_(N,z)e_N/b_(N,z)
=B_(y_N)(z)/b_(N,z)-1.                              (5.3)
```

### Corollary 5.1

Assume (3.3), use the same `k_N` and the complete-build block in all three
expressions, and impose the convergence after (2.4).  On every safe set on
which `b_(N,z)` is nonzero, the following assertions are identical, including
their locally uniform and one-derivative versions:

```text
Acal_(N,z)(kappa)->0;

p_(N,z)e_N/b_(N,z)->0;

B_(y_N)(z)/B_(k_N)(z)->1.                           (5.4)
```

### Proof

All three quantities in (5.4) differ only by the signs and equalities in
(5.3).  Differentiating (5.3) gives the derivative statement. `QED`

This is the exact circle.  Replacing the terminal secant by the complete Abel
integral is a useful recombination, but evaluating that integral only through
the radical equation returns the same target by a reversible identity.

## 6. What can break the circle

Theorem 3.1 does not say that the exterior representation is useless.  It
says that new content must impose a relation not already contained in

```text
pM=q,
M kappa_J+E kappa_T=0.                              (6.1)
```

Examples of genuinely additional content would be

```text
a recurrence among several source-adapted moments;
a finite telescoping concomitant with an independently small boundary;
an arithmetic divisibility relation which acquires a nonzero quartet term;
a source-specific biorthogonality relation derived before selecting p.   (6.2)
```

A norm bound, another path integral, or a second substitution of (6.1) is
not such content.

Keep the arithmetic comparison source `kappa_Z` fixed and replace only the
build by the inserted-quartet build.  Then (3.2) retains

```text
p_(N,z)r_N(kappa)/(alpha_N b_(N,z)).                (6.3)
```

The spectral form of (6.3), after the corresponding completed pairing is
justified, is the quartet evaluation from E101.056.  Hence a new theorem must
preserve (6.3), prove its arithmetic counterpart is absent, and show that the
actual selected test does not annihilate the quartet functional.

## 7. Incomplete-divisor packet audit

The earlier explicit incomplete-divisor physical kernel not yet contracted
termwise with the complete terminal secant is the formula of E83.006:

```text
R_y=M[S_y^*,Z].                                      (7.1)
```

Its exact expansion contains the moving divisor bands

```text
D_k(t),
D_k(t+y-L,t).                                       (7.2)
```

E83.007 proves that the left endpoint contains an uncancelled `k=2` wedge
with coefficient `2^(-sigma)`.  Therefore Mobius inversion by itself supplies
neither a global telescope nor operator smallness.  It does not exclude a
scalar cancellation after the actual vector, signed integration, borders and
shell have all been inserted.

A terminal Mobius packet could still be formed by pairing (7.1) with the
actual dual row.  To equal (3.1), however, it must include simultaneously

```text
the Euler-generated vector;
the signed y integration;
the row and column borders;
the complete Fourier shell;
the moving-level direction.                         (7.3)
```

The prime component alone is not the terminal source, and E101.064 already
rejects its projective disappearance.  E83.007 formulates its surviving
`SAFE-BOUNDARY-PAIRING`, while E99.004 inserts the same kernel into the path
source.  The missing operation is its contraction with the actual terminal
dual row after the complete recombination (7.3).  Thus (7.1) remains an
admissible ingredient, but the already rejected prime-only argument is not a
shortcut around the circle theorem.

Earlier Green, signed-tail and packet identities in E72.044, E72.318,
E72.343, E72.391, E73.075, E73.153 and E84.002--E84.003 supply other exact
coordinates for pieces of this contraction.  Their own audits reduce the
unclosed part to a Cauchy or reduced-leakage scalar.  None changes the
reversible equality (5.3); a useful reuse must enter the complete source in
(7.3), not merely rename its remaining scalar.

## 8. Decision

```text
proved:
  exact source-adapted exterior evaluation for finite truncations and for
  completed sources satisfying the stated convergence;
  exact asymmetric right-border correction under the same convention;
  equality of the Abel exterior action and the terminal secant when the
  fixed comparison source is radical for the complete build;
  equivalence of exterior decay and DIRECTIONAL-IDENT under those hypotheses;

rejected:
  exact radical substitution as a one-way estimate;
  symmetric j>=1 indexing for the right-bordered block;
  a prime-only Mobius closure and operator-smallness shortcut;

required for a new route:
  a non-reversible relation among several source-adapted observables which
  survives the complete terminal recombination and fails on the controlled
  inserted-quartet build;

open:
  such a relation, DIRECTIONAL-IDENT and Omega7.
```
