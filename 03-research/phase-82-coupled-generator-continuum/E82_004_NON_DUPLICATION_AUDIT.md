# E82.004 - Non-duplication audit against the prolate leakage route

## 1. Objects being compared

Phase 80 isolated

```text
DIRECTIONAL-TAIL-CONTINUITY:
the normalized bordered Cauchy response tends to zero on the actual
PROLATE and WEIL residual directions.                                (1.1)
```

The earlier prolate leakage program isolated successively

```text
BTE:
  trace closeness of the actual and prolate bordered pencils;

Weyl-reduced leakage:
  closeness tested only against Cauchy resolvent functionals and one
  derivative;

scalar WRL:
  annihilation of the single Weyl--Feshbach kernel after Abel reduction.
                                                                    (1.2)
```

## 2. Exact implication comparison

The response in (1.1) is evaluated only through a Cauchy row and its safe
normalization.  It does not require trace-norm convergence of the entire
bordered pencil.  Therefore it is weaker than full `BTE`.

However, it has the same testing class as Weyl-reduced leakage: one Cauchy
resolvent functional, its derivative when a logarithmic derivative is needed,
and the actual prolate residual direction.  After inserting the radical
decomposition, the scalar to be controlled is the same signed pairing that the
earlier route called scalar `WRL`.

Thus the dependency relation is

```text
BTE => Weyl-reduced leakage
    = directional tail continuity in the safe Cauchy topology
    => SAFE-PROLATE-BRIDGE.                              (2.1)
```

The equality in (2.1) is equality of proof obligations, not equality of every
auxiliary norm used in the two presentations.

## 3. Historical obstruction that still applies

The earlier Abel expansion of scalar WRL produced resonance vectors.  Its
audit established:

```text
1. prime-number-theorem scale bounds do not annihilate an off-line maximal
   resonance;
2. a zero-independent scalar Mellin annihilator becomes a zero filter;
3. an admissible proof therefore needs a new finite arithmetic spectral
   coboundary or an equivalent null-vector identity.                   (3.1)
```

Changing from leakage language to directional-tail language does not alter
the scalar after the safe Cauchy pairing.  Hence (3.1) applies unchanged.

## 4. Route decision

Path A of Phase 82 is not a new untried method.  It is the endpoint of the
earlier prolate leakage program in the corrected safe topology.  It remains a
valid theorem target, but reopening its sequence of BTE, leakage and Abel
reductions would duplicate completed work.

The only branch not already reduced in that history is

```text
SOURCE-RETAINING-TWO-TERM:
h_N=t_N k_L+r_N,

with an equation for r_N obtained before division by t_N and an exact
implication from its Cauchy profile to RDI-ANCHOR.                       (4.1)
```

This branch is admissible only if it avoids applying the unknown complement
inverse to define `r_N`; otherwise it is the old reduced leakage written as a
remainder.

## 5. Status

```text
proved by crosswalk:
  directional radical-tail continuity is the Weyl-reduced leakage obligation
  already reduced to scalar WRL;

archived as duplicate:
  a new phase that merely repeats BTE, Feshbach leakage or Abel-WRL;

live:
  a source-retaining two-term expansion with an independently constructed
  correction;

hard condition:
  the correction must not be defined through the unknown inverse or a zero
  filter.
```

