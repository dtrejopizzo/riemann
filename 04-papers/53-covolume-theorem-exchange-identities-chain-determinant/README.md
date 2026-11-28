# Paper 53 — The Covolume Theorem: exchange identities and the determinant of a chain of theta lifts

Fifth companion of row D. It deduces the Covolume Theorem, the third of the three theorems, from its inputs.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `covolume-theorem-exchange-identities-chain-determinant.pdf` | The paper (161 pages). |

## The paper

The paper studies a chain of $m$ theta lifts between unitary groups over a CM field, which carries
forms of discrete series type on an indefinite group to algebraic modular forms on a definite
group, the $j$-th lift being formed with the $j$-th power of a tamely ramified character
$\vartheta$.

What the paper proves:

- **Injectivity and the determinant.** The chain is injective, and the ratio
  $Z(1)/Z(\vartheta)$ of its Gram determinants is the product of the corresponding ratios for
  $m$ single lifts in Weil's range and of explicit ratios of values of Hecke $L$-functions.
- **The exchange identity.** An identity between theta integrals over two unitary groups of
  complementary ranks, which holds up to a constant whose absolute value is given by Hecke
  $L$-values. It is the main tool.
- **A spanning set.** By lifts through two grids of hermitian spaces, a spanning set of forms
  whose images under the chain are short and become integral, after every twist, on
  multiplication by an explicit scalar.
- **Galois conjugation** of the lifts of characters.

## Place in the series

The series carries the four rows of Weil's proof to $\mathrm{Spec}\,\mathbb Z$: rows A, B, C
(Papers 43, 44, 45), row D ([Paper 46](../46-row-d-sign-radial-intersection-form/)) and its eight companions (Papers 49–56).
[Paper 46](../46-row-d-sign-radial-intersection-form/) deduces that no Dirichlet $L$-function vanishes in $\Re s>1/2$ from three
theorems on integral algebraic modular forms: the Short Forms Theorem, the Spanning Theorem and
the Covolume Theorem. The companions prove the propositions from which the three theorems are
deduced. [Paper 57](../57-riemann-hypothesis-along-the-rows-of-weils-proof/) is a guide to the whole chain.

- **Role.** Proves the Covolume Theorem from its inputs; the inputs on one lift, on the twists and on the local Galois representations are in Papers 54, 55 and 56, to be read in that order.
- **Uses.** Statements quoted from [Paper 46](../46-row-d-sign-radial-intersection-form/), [Paper 49](../49-short-forms-theorem-theta-lifts-complex-multiplication/), [Paper 51](../51-spanning-theorem-second-moment-poincare-map/), [Paper 54](../54-covolume-theorem-one-theta-lift-hecke-l-values/), [Paper 55](../55-covolume-theorem-regular-families-of-twists/); they are reproduced in an appendix, so the paper can be read on its own.

**Credit and status.** The mathematics that the three theorems organise, and the way from them to
the zero-free half-plane, come from the work of Levent Alpoge (Lean 4 formalization,
<https://alpo.ge/remark.pdf>), which is by itself a complete route to the Riemann hypothesis. The
division into three theorems and the proofs as written here are this series' way of putting it
on paper. The paper has not been refereed.

## Building

```
pdflatex -jobname=covolume-theorem-exchange-identities-chain-determinant main.tex
```

three times.
