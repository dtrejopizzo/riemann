# Paper 56 — Explicit cup exponents for local Galois representations beyond the Fontaine–Laffaille range

Eighth companion of row D. A paper of integral $p$-adic Hodge theory; its bounds are the local input at $\ell$ of Paper 55.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `explicit-cup-exponents-local-galois-representations.pdf` | The paper (76 pages). |

## The paper

Let $\Gamma$ be the absolute Galois group of a finite extension of $\mathbb Q_\ell$. For two
lattices in crystalline representations of $\Gamma$ that are in duality only modulo a power of
$\ell$, the cup product of two crystalline classes need not vanish.

The paper bounds the power of $\ell$ that kills all such cup products, for every prime $\ell$
and with no restriction of Fontaine–Laffaille type, when the Hodge–Tate weights lie in a low
window around $0$ and a far window, possibly much larger than $\ell$. The bound is explicit and
is sensitive to the number of low weights and not to the size of the largest weight; for large
$\ell$ it is zero. Potentially crystalline lattices of tame type are also treated.

The proofs use lattices in $W(\mathbb C_\ell^\flat)\otimes L$ defined by orders of vanishing
along the Frobenius translates of an Eisenstein element, and a lemma that converts chains of
moves of points of these lattices into exponents for cup products.

## Place in the series

The series carries the four rows of Weil's proof to $\mathrm{Spec}\,\mathbb Z$: rows A, B, C
(Papers 43, 44, 45), row D ([Paper 46](../46-row-d-sign-radial-intersection-form/)) and its eight companions (Papers 49–56).
[Paper 46](../46-row-d-sign-radial-intersection-form/) deduces that no Dirichlet $L$-function vanishes in $\Re s>1/2$ from three
theorems on integral algebraic modular forms: the Short Forms Theorem, the Spanning Theorem and
the Covolume Theorem. The companions prove the propositions from which the three theorems are
deduced. [Paper 57](../57-riemann-hypothesis-along-the-rows-of-weils-proof/) is a guide to the whole chain.

- **Role.** Supplies to [Paper 55](../55-covolume-theorem-regular-families-of-twists/) the exponents killing cup products in the Galois cohomology of lattices, at every prime including those below the Fontaine–Laffaille range.
- **Uses.** Statements quoted from [Paper 46](../46-row-d-sign-radial-intersection-form/), [Paper 55](../55-covolume-theorem-regular-families-of-twists/); they are reproduced in an appendix, so the paper can be read on its own.

**Credit and status.** The mathematics that the three theorems organise, and the way from them to
the zero-free half-plane, come from the work of Levent Alpoge (Lean 4 formalization,
<https://alpo.ge/remark.pdf>), which is by itself a complete route to the Riemann hypothesis. The
division into three theorems and the proofs as written here are this series' way of putting it
on paper. The paper has not been refereed.

## Building

```
pdflatex -jobname=explicit-cup-exponents-local-galois-representations main.tex
```

three times.
