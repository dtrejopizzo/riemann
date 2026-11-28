# Paper 51 — The Spanning Theorem: the second moment of a Poincaré map

Third companion of row D. It proves the Spanning Theorem, the second of the three theorems, through an estimate for a second moment.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `spanning-theorem-second-moment-poincare-map.pdf` | The paper (105 pages). |

## The paper

The Spanning Theorem says that a few translates, under a finite group acting through the level,
of the image of a Poincaré map from algebraic modular forms on a definite unitary group to cusp
forms of discrete series type on a larger unitary group span almost all of the target.

What the paper proves:

- **The second moment of the map over the group**, with the main term obtained with its exact
  constant. The estimate comes from a relative trace formula for Poincaré series of Bessel type:
  the main term is extracted from the open cell by Siegel's formula and repeated Poisson
  summation, and the remaining terms are bounded through the decay of the Bessel functions of
  discrete series with large parameters and a count of pairs of terms.
- **Equality of multiplicities.** Hecke eigensystems occur with the same multiplicities on
  unitary groups that are isometric at all finite places.
- **Harish-Chandra's formula** for the elliptic orbital integrals of the coefficients used.

## Place in the series

The series carries the four rows of Weil's proof to $\mathrm{Spec}\,\mathbb Z$: rows A, B, C
(Papers 43, 44, 45), row D ([Paper 46](../46-row-d-sign-radial-intersection-form/)) and its eight companions (Papers 49–56).
[Paper 46](../46-row-d-sign-radial-intersection-form/) deduces that no Dirichlet $L$-function vanishes in $\Re s>1/2$ from three
theorems on integral algebraic modular forms: the Short Forms Theorem, the Spanning Theorem and
the Covolume Theorem. The companions prove the propositions from which the three theorems are
deduced. [Paper 57](../57-riemann-hypothesis-along-the-rows-of-weils-proof/) is a guide to the whole chain.

- **Role.** Proves the Spanning Theorem. The local statements behind its main term are in [Paper 52](../52-sieve-systems-siegel-step/); the equality of multiplicities is also used by Papers 53–55.
- **Uses.** Statements quoted from [Paper 46](../46-row-d-sign-radial-intersection-form/), [Paper 49](../49-short-forms-theorem-theta-lifts-complex-multiplication/), [Paper 52](../52-sieve-systems-siegel-step/); they are reproduced in an appendix, so the paper can be read on its own.

**Credit and status.** The mathematics that the three theorems organise, and the way from them to
the zero-free half-plane, come from the work of Levent Alpoge (Lean 4 formalization,
<https://alpo.ge/remark.pdf>), which is by itself a complete route to the Riemann hypothesis. The
division into three theorems and the proofs as written here are this series' way of putting it
on paper. The paper has not been refereed.

## Building

```
pdflatex -jobname=spanning-theorem-second-moment-poincare-map main.tex
```

three times.
