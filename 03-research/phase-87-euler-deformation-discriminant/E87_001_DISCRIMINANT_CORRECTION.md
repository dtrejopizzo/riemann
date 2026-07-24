# E87.001 - Correction of the sign-coherence discriminant

## 1. The proposed implication is false

E80.004 constructs real symmetric spectral-shift increments that satisfy all
of the following:

```text
real support;
single-signed cumulative shifts;
tight Stieltjes bounds;
locally uniform summable convergence.                  (1.1)
```

One positive weight in the construction can be varied while every property
in (1.1) is preserved and the limiting Poisson transform changes.

### Theorem 1.1

Neither

```text
single-signedness,
```

nor single-signedness together with build-neutral convergence, implies
`SAFE-GAMMA-IDENT`.

### Proof

Apply Theorem 3.1 of E80.004.  The family there has all the stated properties,
but its limiting transform contains a freely variable nonzero Poisson term.
`QED`

Thus the milestone described as

```text
coherence <=> SAFE-GAMMA-IDENT                          (1.2)
```

must be withdrawn unless an independent arithmetic normalization is added.

## 2. Correct hard statement

Theorems E80.003 and E81.003 give two equivalent forms of the actual
discriminant:

```text
RDI-ANCHOR:
d/ds log C_L(s)-H_L(s)->0,                             (2.1)

STIELTJES-ANCHOR:
nu_L^ev-tau_L^arith->0 in the bilateral Stieltjes
topology, with tau_L^arith constructed independently. (2.2)
```

Constructing `tau_L^arith` by inverse-transforming the desired right side is
circular.  Coherence may estimate an already identified measure, but cannot
supply the identity.

## 3. Consequence for prioritization

The open WRL and cluster clauses of Phases 84--86 are convergence
infrastructure and are required for both the arithmetic build and an off-line
control.  They cannot, by themselves, carry the separation required by
Omega7.

The force-bearing work is the independent comparison of `C_L` and `E_L`.
Phase 87 attacks that comparison by an exact arithmetic deformation rather
than by the sign of the resulting spectral cloud.

## 4. Status

```text
proved:
  sign coherence is insufficient for arithmetic identification;

corrected:
  the discriminant is RDI-ANCHOR, equivalently the independently normalized
  Stieltjes anchor;

open:
  an admissible proof of that anchor.
```

