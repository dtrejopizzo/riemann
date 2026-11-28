# Paper 58 — The sign of the radial intersection form on the idele class group: row D in full

Row D of the Weil-type route over $\mathrm{Spec}\,\mathbb Z$ in a single volume. It carries the
same title as [Paper 46](../46-row-d-sign-radial-intersection-form/) and the same study of the
form $W_T$. In the series the argument is divided: Paper 46 states the three theorems and deduces
them from propositions proved in the eight companion papers (Papers 49–56). Here the whole chain,
from published theorems to the Riemann hypothesis, is in one document.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper (a single file). |
| `sign-radial-intersection-form-idele-class-group-complete-proofs.pdf` | The paper (659 pages). |
| `verification/row-d-verification.ipynb` | Colab notebook: the numerical checks and the falsification attempts applied to the statements of the chain, with their outputs. |
| `verification/README.md` | How to open and run the notebook. |

## The paper

The radial trace on the idele class group of $\mathbb Q$ defines a Hermitian form $W_T$ on
functions supported in $(-T,T)$; on smooth tests it equals $\sum_\rho|\Phi_F(\rho)|^2$ over the
nontrivial zeros of $\zeta$.

**The form (Sections 2–11).** The archimedean multiplier, duality and certificates, the explicit
formula on flat-top weights, the two Tate directions, the equivalence of the sign on all windows
with positive semidefiniteness in every degree of one sequence of explicit matrices, and lower
bounds on bounded windows: $10^{-18}$ for the complete form and $2.5\cdot10^{-12}$ for its
primitive restriction when $T\le\tfrac12\log 5$, and an explicit positive bound up to $T=2.8022$
from finite-height zero data. $W_T\ge 0$ on every window is equivalent to the Riemann hypothesis.

**The zero-free half-plane (Sections 12–80).** The paper proves that no Dirichlet $L$-function
vanishes in $\Re s>1/2$ (Theorem `thm:GRH-half`). The chain has four links.

1. **A one-sided criterion of Landau type** (Theorem `an:thm-criterion`). For a modulus $q$ and
   an imaginary quadratic field $K=\mathbb Q(\sqrt{-d})$, let $R_q(x)$ be the prime sum over
   $n\equiv 1 \pmod q$ weighted by $(1-\chi_K(n))(1/n-1/x)$, minus its main term. If
   $R_q(x)\le x^{\beta-1}$ for all large $x$ and every prime $d$ in a residue class, then no
   $L(s,\psi)$ with $\psi$ modulo $q$ vanishes in $\Re s>\beta$.
2. **Admissible data** (Theorem `an:thm-data`): for every large $x$, scales, a CM field
   $E=K(\zeta_{q_1})$ of degree between $x^{11}$ and $x^{12}$ over $K$, a sparse set of its
   infinite places, weights and three primes.
3. **Three theorems on integral algebraic modular forms** on a chain of theta lifts between
   definite unitary groups over $E$: Theorem A (integral forms with short images span),
   Theorem B (few translates of these images span almost everything) and Theorem C (a lower bound
   for covolume plus index). In the series they are called the Short Forms Theorem, the Spanning
   Theorem and the Covolume Theorem. They carry the weight of the argument. They are deduced from a list
   of propositions on the theta lifts, their divisibility at every prime, their archimedean size,
   the second moment of a Poincaré map, the determinant of the chain of lifts and the existence
   of regular families of twists; the proofs of these propositions are the larger part of the
   paper.
4. **The main inequality** (Theorem `an:thm-main`), which combines the three theorems and gives
   $R_{q_0}(y)\le y^{-1/2+\varepsilon}$, the hypothesis of the criterion for every
   $\beta>\tfrac12$.

**Conclusion (Section 81).** The Riemann hypothesis (Theorem `thm:RH`) is the case of the trivial
character, and with it $W_T(F)=\sum_\rho|\Phi_F(\rho)|^2\ge 0$ on every window
(Corollary `cor:all-windows`): the sign in Weil's programme over $\mathrm{Spec}\,\mathbb Z$. The
results are not effective, because of the theorem of Siegel and Walfisz.

**On what the proof rests.** The proof of the Riemann hypothesis in this paper does not use
Papers 43, 44 or 45; they enter only in the reading of the result as an index inequality. From
the literature the paper uses published theorems, cited where they are needed: classical theorems
on Dirichlet $L$-functions and Heath-Brown's large sieve for real characters, and, in the
automorphic part, the Weil representation and Howe duality, the Siegel–Weil formula, complex
multiplication with the Chowla–Selberg formula, the discrete series of real groups, Green's
parametrisation of the characters of finite general linear groups, standard monomial theory, the
Galois representations attached to automorphic forms on unitary groups, Bloch–Kato Selmer groups
and Poitou–Tate duality, Fontaine's theory of $p$-adic representations, and Hecke's non-vanishing
theorem on $\Re s=1$.

**Credit.** The mathematics behind Theorems A, B and C, and the way from them to the zero-free
half-plane, come from the work of Levent Alpoge (Lean 4 formalization,
<https://alpo.ge/remark.pdf>), which is by itself a complete route to the Riemann hypothesis and
does not depend on this series. The division of the argument into these three theorems, and
their proofs as written here, are this paper's way of organising it as mathematics on paper. The
independent compilation of his archive is recorded in
[`../../06-alpoge-verification/`](../../06-alpoge-verification/).

**Status.** The paper has not been refereed. There may be mistakes; the notebook below records
which statements were tested and which were not.

## Relation to the series

| | Papers 46 and 49–56 | Paper 58 |
|---|---|---|
| Theory of the form $W_T$, bounds on bounded windows | Paper 46 | here |
| Criterion, admissible data, main inequality | Paper 46 | here |
| The three theorems | stated and deduced in Paper 46; called Short Forms, Spanning, Covolume | stated and deduced here; called Theorems A, B, C |
| Proofs of the propositions behind them | Papers 49–56, each readable on its own | Sections 15–80 |
| Length | 54 pages and eight companions (677 pages) | 659 pages |

The two presentations were edited separately; where they differ in wording, the series
(Papers 46 and 49–56) is the later text. [Paper 57](../57-riemann-hypothesis-along-the-rows-of-weils-proof/)
is a guide to the chain.

## Notebook: stress tests of the proof chain

[`verification/row-d-verification.ipynb`](verification/row-d-verification.ipynb) documents the
numerical consistency checks and the falsification attempts applied to individual statements of
the chain "three theorems ⇒ main inequality ⇒ one-sided bound ⇒ criterion ⇒ GRH ⇒ RH". The
notebook names the three theorems as in the series (Short Forms, Spanning, Covolume) and refers
to statements by their labels, which are the same in this paper and in Papers 46 and 49–56. Each
test states the statement tested and the outcome that would have refuted it; then the script is
written to disk, run, and its output checked by assertions.

- **Map of the chain.** The links of the chain and the nodes N1–N8 into which the automorphic
  part is divided.
- **Falsifiers of the whole argument.** A proof that did not use the Euler product would also
  "prove" false statements; the notebook records where the argument uses it, with the
  Davenport–Heilbronn function as the example, and four analytic variations (K1–K4) of the
  argument that do not yield false consequences.
- **Numerical tests, node by node.** Elementary divisors of the scaled Hecke operator (N1);
  archimedean ingredients of the seesaw identity (N2b); conjugates of CM theta values and the
  Chowla–Selberg constant, to 30–50 digits (N3); lemmas beneath the second moment of the Poincaré
  map (N4); the combinatorial skeleton of the exchange identities (N5); the grid statements for
  the determinant of the comparison operator (N6b); Wach modules and the local loss in rank one
  and two (N7c); the count of $p$-divisibility for the test form (N8).
- **Results table.** In the saved run, 39 executed tests passed; 15 further rows are
  illustrations, results recorded only, analytic arguments, or statements that were not tested.

**What it does not do.** It proves nothing. Every test checks a statement in a few small
instances, far below the range in which the theorems are asserted (ranks of order $x^5$, moduli
larger than $b^{20}$). Several statements that carry weight have no numerical test at all, among
them the seesaw identity (N2), the Spanning Theorem itself (N4) and the determinant of the comparison
operator (N6); the notebook lists them in its last section.

**Running it.** Open the notebook in Google Colab and run all cells. It needs `numpy`, `sympy`
and `mpmath`, which Colab provides. A full run with the default parameters takes about 10–15
minutes on a CPU runtime. The saved notebook contains the outputs, so the results can be read
without running anything.

## Building

```
pdflatex -jobname=sign-radial-intersection-form-idele-class-group-complete-proofs main.tex
```

three times.
