# Cyclotomic norm--Tate realization: a rational-vanishing no-go

## Question

Could the missing global square be the positive realization of the norm--Tate
cofiber of the cyclotomic prime actions?  Such a construction would be
attractive because restriction, transfer and Frobenius are defined before the
Weil comparison.

## Proposition (real norm--Tate vanishing)

Let `G` be a finite group and let `C` be a chain complex of real Hilbert spaces
with an isometric `G`-action.  The norm map

```
N : C_{hG} -> C^{hG}
```

is a quasi-isomorphism.  Consequently its Tate cofiber is acyclic.  More
generally, for a bounded-below genuine `G`-spectrum `X`,

```
(X^{tG}) \wedge H R = 0.
```

### Proof

Over `R`, the group algebra `R[G]` is semisimple.  Hence invariants and
coinvariants are exact.  On degree-zero modules the averaging idempotent

```
e_G = |G|^{-1} sum_{g in G} g
```

identifies the coinvariant space with the invariant space.  With the
unnormalized convention, the norm is `|G| e_G`; since `|G|` is invertible in
`R`, it is an isomorphism.  Applying this degreewise proves the chain-complex
statement.  The spectral statement follows after rational/real localization
from the same transfer splitting (equivalently, finite-group Tate cohomology
vanishes when `|G|` is invertible).  QED.

## Corollary (failure for the Weil form)

Any real Hilbert-space quadratic form obtained functorially from the
norm--Tate cofiber of the finite cyclic groups `C_p` is zero.  If the
construction is kept integral, its remaining classes are `p`-primary torsion,
and every additive realization into `R` kills them.  Therefore it cannot yield
the nonzero coefficients

```
(log p) p^{-j/2}
```

or the nonzero prime--Gamma Green form.

## Verdict

The cyclotomic norm--Tate square is categorically non-circular but has the
wrong coefficient category.  The same operation that makes its cofiber
canonical forces that cofiber to disappear under the real positive
realization required by row (d).  This rules out the route before any choice of
`THH`, `TC`, cyclotomic Frobenius or local normalization.

This is not a no-go for every cyclotomic invariant.  It is specifically a
no-go for obtaining the missing **real positive square from the finite-group
norm cofiber itself**.  A surviving route would need a genuinely
non-torsion regulator before realification; its positivity would then require
a separate theorem and is not supplied by the norm--Tate triangle.
