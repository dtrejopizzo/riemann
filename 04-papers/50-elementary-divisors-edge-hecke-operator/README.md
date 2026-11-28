# Paper 50 — Elementary divisors of an edge Hecke operator on a Frobenius cycle

Second companion of row D. A short and self-contained paper of linear algebra over a valuation ring; its theorem is used in the proof of the Short Forms Theorem.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `elementary-divisors-edge-hecke-operator-frobenius-cycle.pdf` | The paper (15 pages). |

## The paper

On the lattice of integral algebraic modular forms of large weight on a definite unitary group, a
Hecke operator at a prime $p$ has denominators and becomes integral after multiplication by a
power of $p$. The paper proves that at suitable primes inert in an imaginary quadratic field the
operator scaled in this way is nearly unimodular: the mean exponent of its elementary divisors is
a small fraction of the exponent of the scaling (Theorem `ph:thm`).

The operator is attached to a graph of Hecke neighbours and to polynomial forms in several groups
of variables, on which a general linear group acts through embeddings linked in a cycle by
Frobenius. The proof factorises the operator through lattices placed halfway along the edges of
the graph. It rests on a count of zeros with multiplicity, a lemma on the monomials of forms
with divisible translates, a count of lattice points and an averaging construction.

## Place in the series

The series carries the four rows of Weil's proof to $\mathrm{Spec}\,\mathbb Z$: rows A, B, C
(Papers 43, 44, 45), row D ([Paper 46](../46-row-d-sign-radial-intersection-form/)) and its eight companions (Papers 49–56).
[Paper 46](../46-row-d-sign-radial-intersection-form/) deduces that no Dirichlet $L$-function vanishes in $\Re s>1/2$ from three
theorems on integral algebraic modular forms: the Short Forms Theorem, the Spanning Theorem and
the Covolume Theorem. The companions prove the propositions from which the three theorems are
deduced. [Paper 57](../57-riemann-hypothesis-along-the-rows-of-weils-proof/) is a guide to the whole chain.

- **Role.** Supplies the divisibility at a set of exceptional primes needed for the Short Forms Theorem.
- **Uses.** Statements quoted from [Paper 49](../49-short-forms-theorem-theta-lifts-complex-multiplication/); they are reproduced in an appendix, so the paper can be read on its own.

**Credit and status.** The mathematics that the three theorems organise, and the way from them to
the zero-free half-plane, come from the work of Levent Alpoge (Lean 4 formalization,
<https://alpo.ge/remark.pdf>), which is by itself a complete route to the Riemann hypothesis. The
division into three theorems and the proofs as written here are this series' way of putting it
on paper. The paper has not been refereed.

## Building

```
pdflatex -jobname=elementary-divisors-edge-hecke-operator-frobenius-cycle main.tex
```

three times.
