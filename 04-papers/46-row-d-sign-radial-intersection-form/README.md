# Paper 46 — The sign of the radial intersection form on the idele class group

Row D of the Weil-type route over $\mathrm{Spec}\,\mathbb Z$: the intersection inequality.
Papers 43, 44 and 45 give rows A, B and C (correspondences, Frobenius, explicit formula); this
paper determines the sign.

## Contents of the folder

| File | What it is |
|---|---|
| `main.tex` | Source of the paper. |
| `sign-radial-intersection-form-idele-class-group.pdf` | The paper (48 pages). |
| `annex.tex` | Source of the annex. |
| `column-packages-character-families.pdf` | The annex, *Column packages for character families: the arithmetic inputs for the sign of the radial intersection form* (302 pages). |
| `version-2026-11-23/`, `version-2026-10-19/`, `main.before-final-redaction.tex` | Earlier versions of the paper, kept for reference. They are superseded by `main.tex`. |

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
certificates, the explicit formula on flat-top weights, the reduction of the sign on all windows
to positive semidefiniteness in every degree of one sequence of explicit matrices, and
quantitative bounds on bounded windows. For $T\le\tfrac12\log 5$ the lower bounds on unit vectors
are $10^{-18}$ for the complete form and $2.5\cdot10^{-12}$ for its primitive restriction, and a
certificate using finite-height zero data gives an explicit positive lower bound up to
$T=2.8022$.

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

`positivity-radial-intersection-form.ipynb` (coming shortly)

This notebook will accompany the paper and its annex. It will let anyone run, in Google Colab,
the two computations that sit on either side of the proof, and see where the proof itself is
needed.

The object is the Hermitian form $W_T(F)=\sum_\rho|\Phi_F(\rho)|^2$ on functions $F$ supported
in $(-T,T)$, where $\rho$ runs over the zeros of the completed zeta function. The paper shows
that $W_T\ge 0$ for every $T$ is equivalent to the Riemann hypothesis.

### What the notebook will contain

**Part 1. The certificate on bounded windows.** This part will reproduce, in ball (interval)
arithmetic, the rigorous lower bound for $W_T$ that the paper establishes on bounded windows, up
to $T=2.8022$. Every truncation and rounding error will be bounded, so a `PASS` will mean a
proved inequality, not a floating-point observation.

You will be able to choose your own $T$ and run the same method. If the method yields a certified
bound at that $T$, the notebook will print it. If it does not, the notebook will say so and
report which quantity failed. It will never print `PASS` without a rigorous bound behind it.

**Part 2. The prime sum behind global positivity.** Positivity on *every* window does not come
from pushing Part 1 further. It comes from a different quantity: a smoothed sum over primes,
$G(x)$. The paper shows that a bound $G(x)\le C\,x^\theta$ on arbitrarily large windows
$[Y,Y^{3/2}]$, for every $\theta>1/2$, excludes zeros with real part greater than $\theta$. That
such a bound holds is the step due to Levent Alpoge.

This part will compute $G(x)$ directly from the primes. No zeros of zeta will be used anywhere,
so nothing is circular. It will evaluate $G$ on windows as large as Colab can handle, plot
$G(x)/\sqrt x$, and compare it with the bound given by the theorem and with $C\,x^\theta$ for a
$\theta$ of your choice.

This part will be an illustration, not a certificate.

**Part 3. Putting the two together.** A short closing section will state the chain of the paper
in five lines and summarise the run: what was certified rigorously in Part 1, what was observed
numerically in Part 2, and what only the proof can supply.

### What the notebook will and will not show

It will show:

- a rigorous, reproducible certificate of $W_T\ge 0$ on the bounded windows you run;
- the prime-sum bound holding, from the primes alone, on the windows you can compute.

It will not show that $W_T\ge 0$ for every $T$, and no computation could. The theorem that makes
positivity global is an existence statement that holds on windows beyond thresholds far outside
the reach of any machine, and global positivity follows from the bound holding on infinitely many
growing windows. That is what the proof is for. The notebook will show the two pieces at work as
far as a computer reaches, and where the proof takes over.

### Running it

Open the notebook in Google Colab and run the cells in order. The only dependency beyond the
standard scientific Python stack will be `python-flint`, installed by the first cell. Expected
runtimes and the largest windows reached in testing will be listed here once the notebook is
uploaded.
