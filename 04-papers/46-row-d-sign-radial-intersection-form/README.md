# Paper 46 — The sign of the radial intersection form on the idele class group

Row D of the Weil-type route over $\mathrm{Spec}\,\mathbb Z$: the intersection inequality.
Papers 43, 44 and 45 give rows A, B and C (correspondences, Frobenius, explicit formula); this
paper determines the sign.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper. |
| `sign-radial-intersection-form-idele-class-group.pdf` | The paper (52 pages). |
| `annex.tex` | Source of the annex. |
| `column-packages-character-families.pdf` | The annex, *Column packages for character families: the arithmetic inputs for the sign of the radial intersection form* (302 pages). |
| `positivity-radial-intersection-form.ipynb` | Colab notebook: certificates of $W_T\ge 0$ on bounded windows and the prime sum behind global positivity. |

## The paper

The radial trace on the idele class group of $\mathbb Q$ defines a Hermitian form $W_T$ on
functions supported in $(-T,T)$; on smooth tests it equals $\sum_\rho|\Phi_F(\rho)|^2$ over the
nontrivial zeros of $\zeta$. The paper does three things.

1. **Equivalence.** $W_T\ge 0$ on the entire form domain for every $T>0$ is equivalent to the
   Riemann hypothesis.
2. **Reduction.** For every $1/2<\theta<1$, a bound $G(x)\le C_\theta x^\theta$ for the smoothed
   prime sum on arbitrarily large intervals $[Y,Y^{J_\theta}]$ excludes zeros in $\Re s>\theta$.
   These bounds are reduced to an upper estimate for a finite mean difference, and that estimate
   is proved from a slope inequality for Hermitian lattices, given a family of characters carrying
   a column package with uniform constants.
3. **Conclusion.** The existence of such families is a theorem of L. Alpoge. With it the paper
   obtains the Riemann hypothesis (Theorem `thm:RH`) and, as a corollary, $W_T\ge 0$ on every
   window (Corollary `cor:all-windows`): the sign in Weil's programme over
   $\mathrm{Spec}\,\mathbb Z$.

The paper also contains the theory that does not depend on that theorem: duality and
certificates, the explicit formula on flat-top weights, the equivalence of the sign on all windows
with positive semidefiniteness in every degree of one sequence of explicit matrices, and
quantitative bounds on bounded windows. For $T\le\tfrac12\log 5$ the lower bounds on unit vectors
are $10^{-18}$ for the complete form and $2.5\cdot10^{-12}$ for its primitive restriction; they are
unconditional and computer-assisted (interval arithmetic). For $T\le 2.8022$ Theorem 9.12 proves
$W_T(F)\ge e^{-120110026807}\|F\|^2$, assuming three published facts about the zeros of $\zeta$,
among them the numerical verification that the zeros up to height $3\cdot10^{12}$ lie on the
critical line; its finite computations are done in exact integer and interval arithmetic.

**On what the proof rests.** Alpoge's theorem on families of column packages rests on his Lean
formalisation and has not yet been written out on paper in full. The paper states this in the
abstract, in the introduction and in its last section, and the annex is a first written account.

## The annex

The annex supports one step only: the existence of the families with a column package. It derives
that theorem from five arithmetic inputs, one per section:

| Section | Input |
|---|---|
| A | the loss bound |
| B | the divisor bound |
| C | level counts and almost orthogonality |
| D | the windowed bound for Selmer groups |
| E | existence of families with uniform constants |

Every step is marked as one of three kinds: proved in the annex; a published theorem, quoted with
its statement; or a new statement taken from the Lean formalisation, stated exactly and with an
outline of its formal proof. It is a first written exposition of a result that does not yet exist
complete on paper.

## Building

The two documents refer to each other's labels, so they are compiled under the names of their
PDFs and in alternation:

```
M=sign-radial-intersection-form-idele-class-group
A=column-packages-character-families
for i in 1 2 3 4; do
  pdflatex -jobname=$M main.tex
  pdflatex -jobname=$A annex.tex
done
```

## Notebook: positivity of the radial intersection form

`positivity-radial-intersection-form.ipynb` lets you run, in Google Colab, the computations that
sit on either side of the proof, and see where the proof itself is needed.

**Part 1. Certificates on bounded windows.** Two rigorous certificates in ball (interval)
arithmetic, so every `PASS` is a proved inequality and not a floating-point observation.

- *Up to $T=\tfrac12\log 5\approx 0.80$, using no zeros of zeta.* The notebook reproduces the four
  bounds of the paper and pushes the same method to $T=0.85$. You can try your own $T$. The cost
  grows doubly exponentially in $T$, so this route cannot reach large windows; when the problem
  is too large the notebook says so instead of guessing.
- *Up to $T=2.8022$.* The finite inequalities of Theorem 9.12 of the paper (17 numerical checks,
  among them the Schur comparison on 2048 cells). It is conditional on three published facts about zeros in a bounded range
  (Section 9 of the paper), among them the verification that all zeros up to height
  $3\cdot10^{12}$ lie on the critical line. These parameters stop just below $T=2.80227$.

**Part 2. The prime sum behind global positivity.** Positivity on every window does not come from
pushing Part 1 further. It comes from a bound on a smoothed sum over primes, $G(x)$, on
arbitrarily large windows; that such a bound holds is the step due to Levent Alpoge. This part
computes $G(x)$ directly from the primes, with no zeros of zeta involved, up to about
$3\cdot10^{8}$, and compares it with the bound from the theorem. In the windows computed,
$G(x)/\sqrt x$ stays below $0.025$ where the theorem allows more than $100$. This part is an
illustration, not a certificate.

**Part 3.** The chain of the paper in five lines and a summary of the run: what was certified,
what was observed, and what only the proof supplies.

**What it does not do.** It does not show that $W_T\ge 0$ for every $T$, and no computation
could: global positivity follows from the bound holding on infinitely many growing windows, far
beyond the reach of any machine. That is what the proof is for.

**Running it.** Open the notebook in Google Colab and run all cells in order. The first cell
installs `python-flint`; nothing else is needed. A full run takes about 8 minutes on a laptop
core, somewhat longer on Colab; almost all of that time is the $T=0.85$ certificate.
