# Paper 57 — The Riemann hypothesis along the rows of Weil's proof: a guide to the series

A guide for a reader who has opened none of the papers. It proves nothing new: it describes the
logical chain of the twelve papers that carry the four steps of Weil's proof, row by row, to
$\mathrm{Spec}\,\mathbb Z$ (Papers 43, 44, 45, 46 and 49–56).

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `riemann-hypothesis-rows-weil-proof-guide.pdf` | The paper (10 pages). |

## The paper

Weil's proof of the Riemann hypothesis for a curve over a finite field has four steps: the ring
of correspondences with its intersection pairing, the Frobenius correspondences, the trace
formula, and the index inequality. The guide explains:

- **Weil's proof for a curve**, in four rows.
- **Rows A, B and C over $\mathrm{Spec}\,\mathbb Z$**: what replaces each row, and what Papers 43,
  44 and 45 establish (the correspondence algebra with its trace and form; the Frobenius family
  with contacts $\Lambda(n)/\sqrt n$; Weil's explicit formula).
- **Row D**: how the index inequality becomes the sign of a Hermitian form on functions supported
  in an interval, and why that sign on every window is equivalent to the Riemann hypothesis.
- **The one-sided criterion** for a sum over primes.
- **The arithmetic data and the three theorems** (Short Forms, Spanning, Covolume), stated with
  the constants of Paper 46 and explained in words, with the ideas of their proofs.
- **From the three theorems to the Riemann hypothesis**: the main inequality and the one-sided
  bound.
- **The companion papers**: where each of Papers 49–56 enters.
- **The logical structure of the series**: a diagram of which paper proves what, and an order of
  reading.

## The papers of the series

| Row | Paper |
|---|---|
| A | [43](../43-row-a-correspondence-algebra/): correspondence algebra, trace, form, Tate functionals |
| B | [44](../44-row-b-arithmetic-family/): the Frobenius family |
| C | [45](../45-row-c-explicit-formula/): the explicit formula |
| D | [46](../46-row-d-sign-radial-intersection-form/): the sign, the criterion, the data, the three theorems, the main inequality |
| D, Short Forms Theorem | [49](../49-short-forms-theorem-theta-lifts-complex-multiplication/), [50](../50-elementary-divisors-edge-hecke-operator/) |
| D, Spanning Theorem | [51](../51-spanning-theorem-second-moment-poincare-map/), [52](../52-sieve-systems-siegel-step/) |
| D, Covolume Theorem | [53](../53-covolume-theorem-exchange-identities-chain-determinant/), [54](../54-covolume-theorem-one-theta-lift-hecke-l-values/), [55](../55-covolume-theorem-regular-families-of-twists/), [56](../56-explicit-cup-exponents-local-galois-representations/) |

Order of reading suggested in the guide: Paper 46 can be read directly; among the companions,
Paper 49 first, then Paper 50, the pair 51–52, and the group 53–56 in that order, independently
of one another.

**Credit and status.** The guide states that the mathematics organised by the three theorems, and
the way from them to the zero-free half-plane, are the work of Levent Alpoge (Lean 4
formalization, <https://alpo.ge/remark.pdf>), which is by itself a complete proof; the three
theorems, their names and their proofs on paper are the formulation of this series. Nothing in
the series has been refereed.

## Building

```
pdflatex -jobname=riemann-hypothesis-rows-weil-proof-guide main.tex
```

three times (the diagram needs TikZ).
