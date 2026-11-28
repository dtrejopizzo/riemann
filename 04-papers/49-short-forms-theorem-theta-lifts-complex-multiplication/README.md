# Paper 49 — The Short Forms Theorem: theta lifts, complex multiplication and divisibility

First companion of row D, and the one that the other companions build on. It proves the statements from which the Short Forms Theorem is deduced, and it contains the foundations on the Weil representation and on discrete series of real unitary groups used in the whole series.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `short-forms-theorem-theta-lifts-complex-multiplication-divisibility.pdf` | The paper (87 pages). |

## The paper

The Short Forms Theorem concerns a Poincaré map from forms on a definite unitary group over a CM
field to forms on an indefinite one, followed by a chain of theta lifts. It says that suitable
multiples of the images are integral up to a bounded index and short at every conjugate.

What the paper proves:

- **A seesaw identity.** The chain of lifts through indefinite groups is replaced by lifts between
  definite groups, whose kernels are derivatives at the origin of products of theta functions of
  one elliptic curve with complex multiplication.
- **An upper bound at every conjugate** for these derivatives, with the Chowla–Selberg period as
  exact constant.
- **Divisibility at every prime**, in particular at the primes that do not split in the field of
  multiplication and at the prime of the level; Hecke operators through the lifts and a
  reciprocity law on one curve give integrality at the remaining primes.
- **Foundations.** The Weil representation, the archimedean theory of the lifts, archimedean
  types, constants and levels.

## Place in the series

The series carries the four rows of Weil's proof to $\mathrm{Spec}\,\mathbb Z$: rows A, B, C
(Papers 43, 44, 45), row D ([Paper 46](../46-row-d-sign-radial-intersection-form/)) and its eight companions (Papers 49–56).
[Paper 46](../46-row-d-sign-radial-intersection-form/) deduces that no Dirichlet $L$-function vanishes in $\Re s>1/2$ from three
theorems on integral algebraic modular forms: the Short Forms Theorem, the Spanning Theorem and
the Covolume Theorem. The companions prove the propositions from which the three theorems are
deduced. [Paper 57](../57-riemann-hypothesis-along-the-rows-of-weils-proof/) is a guide to the whole chain.

- **Role.** Proves the inputs of the Short Forms Theorem (the first of the three theorems). Best read first among the companions.
- **Uses.** Statements quoted from [Paper 46](../46-row-d-sign-radial-intersection-form/), [Paper 50](../50-elementary-divisors-edge-hecke-operator/), [Paper 51](../51-spanning-theorem-second-moment-poincare-map/), [Paper 53](../53-covolume-theorem-exchange-identities-chain-determinant/), [Paper 54](../54-covolume-theorem-one-theta-lift-hecke-l-values/); they are reproduced in an appendix, so the paper can be read on its own.

**Credit and status.** The mathematics that the three theorems organise, and the way from them to
the zero-free half-plane, come from the work of Levent Alpoge (Lean 4 formalization,
<https://alpo.ge/remark.pdf>), which is by itself a complete route to the Riemann hypothesis. The
division into three theorems and the proofs as written here are this series' way of putting it
on paper. The paper has not been refereed.

## Building

```
pdflatex -jobname=short-forms-theorem-theta-lifts-complex-multiplication-divisibility main.tex
```

three times.
