# Paper 54 — The Covolume Theorem: one theta lift, Hecke L-values and test forms of least valuation

Sixth companion of row D. It treats a single theta lift in Weil's range, one of the inputs of the Covolume Theorem.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `covolume-theorem-one-theta-lift-hecke-l-values.pdf` | The paper (99 pages). |

## The paper

For a theta lift in Weil's range from a unitary group to a definite unitary group over a CM field,
formed with a character twisted by a tamely ramified character $\vartheta$:

- **Determinant and $L$-values.** The Gram determinant of the lift, multiplied by the determinant
  of an explicit operator compressed to the space of lifts, is a constant times a power of a
  product of values of Hecke $L$-functions twisted by $\vartheta$. The operator is integral away
  from the conductor of $\vartheta$, and its determinant is bounded at each prime by the
  congruences between lifts and other forms.
- **Heights.** A bound for the heights of the ratios of twisted to untwisted Hecke values: their
  valuation at every prime is determined, for suitable twists, by the divisibility of Taylor
  coefficients of theta functions with complex multiplication.
- **Test forms of least valuation.** This divisibility is attained by an integral test form,
  which gives the sharpness needed on the lower side.

## Place in the series

The series carries the four rows of Weil's proof to $\mathrm{Spec}\,\mathbb Z$: rows A, B, C
(Papers 43, 44, 45), row D ([Paper 46](../46-row-d-sign-radial-intersection-form/)) and its eight companions (Papers 49–56).
[Paper 46](../46-row-d-sign-radial-intersection-form/) deduces that no Dirichlet $L$-function vanishes in $\Re s>1/2$ from three
theorems on integral algebraic modular forms: the Short Forms Theorem, the Spanning Theorem and
the Covolume Theorem. The companions prove the propositions from which the three theorems are
deduced. [Paper 57](../57-riemann-hypothesis-along-the-rows-of-weils-proof/) is a guide to the whole chain.

- **Role.** Supplies to [Paper 53](../53-covolume-theorem-exchange-identities-chain-determinant/) the ratio of determinants for one lift.
- **Uses.** Statements quoted from [Paper 46](../46-row-d-sign-radial-intersection-form/), [Paper 49](../49-short-forms-theorem-theta-lifts-complex-multiplication/), [Paper 51](../51-spanning-theorem-second-moment-poincare-map/), [Paper 53](../53-covolume-theorem-exchange-identities-chain-determinant/), [Paper 55](../55-covolume-theorem-regular-families-of-twists/); they are reproduced in an appendix, so the paper can be read on its own.

**Credit and status.** The mathematics that the three theorems organise, and the way from them to
the zero-free half-plane, come from the work of Levent Alpoge (Lean 4 formalization,
<https://alpo.ge/remark.pdf>), which is by itself a complete route to the Riemann hypothesis. The
division into three theorems and the proofs as written here are this series' way of putting it
on paper. The paper has not been refereed.

## Building

```
pdflatex -jobname=covolume-theorem-one-theta-lift-hecke-l-values main.tex
```

three times.
