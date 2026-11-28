# Paper 52 — The Spanning Theorem: sieve systems at the real and finite places and Siegel's step

Fourth companion of row D. It proves the local statements on which the main term of the second moment in Paper 51 rests.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `spanning-theorem-sieve-systems-siegel-step.pdf` | The paper (58 pages). |

## The paper

In the proof of the Spanning Theorem the main term of the second moment of a Poincaré map, on a
unitary group over a CM field, is obtained from the open cell of a relative trace formula by
Siegel's formula followed by repeated Poisson summation.

What the paper proves:

- **Sieve systems.** At every real place, for the Bessel function of a discrete series with a
  large parameter, and at every finite set of finite places, for the characteristic function of
  a congruence subgroup twisted by a unipotent character, the paper constructs a family of forms
  on pairs of sequences of numbers, linked by integration over one entry, positive at the top,
  of prescribed mass at the bottom and decaying in the frequency.
- **Correlations along two frames.** A theory of correlations of a Bessel function along two
  frames, common to all places, on which the construction rests.
- **Siegel's step.** A bound for sums of squares of orbital integrals over the rational points of
  a sphere by the top forms, with the constant of Siegel's formula.

## Place in the series

The series carries the four rows of Weil's proof to $\mathrm{Spec}\,\mathbb Z$: rows A, B, C
(Papers 43, 44, 45), row D ([Paper 46](../46-row-d-sign-radial-intersection-form/)) and its eight companions (Papers 49–56).
[Paper 46](../46-row-d-sign-radial-intersection-form/) deduces that no Dirichlet $L$-function vanishes in $\Re s>1/2$ from three
theorems on integral algebraic modular forms: the Short Forms Theorem, the Spanning Theorem and
the Covolume Theorem. The companions prove the propositions from which the three theorems are
deduced. [Paper 57](../57-riemann-hypothesis-along-the-rows-of-weils-proof/) is a guide to the whole chain.

- **Role.** Local part of the proof of the Spanning Theorem; read together with [Paper 51](../51-spanning-theorem-second-moment-poincare-map/).
- **Uses.** Statements quoted from [Paper 46](../46-row-d-sign-radial-intersection-form/), [Paper 51](../51-spanning-theorem-second-moment-poincare-map/); they are reproduced in an appendix, so the paper can be read on its own.

**Credit and status.** The mathematics that the three theorems organise, and the way from them to
the zero-free half-plane, come from the work of Levent Alpoge (Lean 4 formalization,
<https://alpo.ge/remark.pdf>), which is by itself a complete route to the Riemann hypothesis. The
division into three theorems and the proofs as written here are this series' way of putting it
on paper. The paper has not been refereed.

## Building

```
pdflatex -jobname=spanning-theorem-sieve-systems-siegel-step main.tex
```

three times.
