# Paper 55 — The Covolume Theorem: regular families of twists, Selmer groups and Ribet's method

Seventh companion of row D. It proves that the twists needed in the Covolume Theorem exist.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `covolume-theorem-regular-families-twists-selmer-ribet.pdf` | The paper (78 pages). |

## The paper

Let $E$ be a CM field and consider the theta lifts between unitary groups over $E$ that occur in
the Covolume Theorem. The paper proves that for every prime $\ell$ there is an anticyclotomic
character of $E$ of $\ell$-power order, tamely ramified at auxiliary primes, such that after
twisting by its first $m$ powers

- the ratios of twisted to untwisted Hecke $L$-values have bounded $\ell$-adic valuation, and
- the congruences modulo powers of $\ell$ between theta lifts and other forms are bounded,

with bounds whose sum over all primes is controlled.

The twist is chosen so that Bloch–Kato Selmer groups of the Galois representations attached to
the lifts are small. The passage from Selmer groups to congruences is Ribet's method, carried
out modulo powers of every prime $\ell$ with the help of auxiliary places. The paper also
bounds the local loss above each prime and treats the odd classes and Kummer maps.

## Place in the series

The series carries the four rows of Weil's proof to $\mathrm{Spec}\,\mathbb Z$: rows A, B, C
(Papers 43, 44, 45), row D ([Paper 46](../46-row-d-sign-radial-intersection-form/)) and its eight companions (Papers 49–56).
[Paper 46](../46-row-d-sign-radial-intersection-form/) deduces that no Dirichlet $L$-function vanishes in $\Re s>1/2$ from three
theorems on integral algebraic modular forms: the Short Forms Theorem, the Spanning Theorem and
the Covolume Theorem. The companions prove the propositions from which the three theorems are
deduced. [Paper 57](../57-riemann-hypothesis-along-the-rows-of-weils-proof/) is a guide to the whole chain.

- **Role.** Supplies to Papers 53 and 54 the regular family of twists. The local input at $\ell$ is in [Paper 56](../56-explicit-cup-exponents-local-galois-representations/).
- **Uses.** Statements quoted from [Paper 46](../46-row-d-sign-radial-intersection-form/), [Paper 49](../49-short-forms-theorem-theta-lifts-complex-multiplication/), [Paper 53](../53-covolume-theorem-exchange-identities-chain-determinant/), [Paper 54](../54-covolume-theorem-one-theta-lift-hecke-l-values/), [Paper 56](../56-explicit-cup-exponents-local-galois-representations/); they are reproduced in an appendix, so the paper can be read on its own.

**Credit and status.** The mathematics that the three theorems organise, and the way from them to
the zero-free half-plane, come from the work of Levent Alpoge (Lean 4 formalization,
<https://alpo.ge/remark.pdf>), which is by itself a complete route to the Riemann hypothesis. The
division into three theorems and the proofs as written here are this series' way of putting it
on paper. The paper has not been refereed.

## Building

```
pdflatex -jobname=covolume-theorem-regular-families-twists-selmer-ribet main.tex
```

three times.
