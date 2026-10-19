# Paper 04 — Absence of Power-Law Growth in Partial Sums of the Davenport–Heilbronn Function at Off-Line Zeros

The Davenport–Heilbronn function satisfies a functional equation of standard type but has no
Euler product, and it has infinitely many zeros off the critical line. The paper tests the
prediction that an off-line zero $\rho_0=\beta_0+i\gamma_0$ produces growth
$|D_{DH}(\gamma_0;N)|\sim N^{\beta_0-1/2}$ in the partial Dirichlet sum on the critical line.
It uses Kahan-compensated sums for $N$ from $10^4$ to $10^9$. The result is null. At the first
off-line zero ($\beta_0\approx0.8085$, $\gamma_0\approx85.7$) the fitted exponent is
$0.000440\pm0.000453$, against a predicted $0.3085$. Either the pre-asymptotic regime extends
beyond $N=10^9$, or critical-line partial sums do not express off-line zeros through a simple
power law.

## Main results

- Growth exponent statistically indistinguishable from zero at four off-line zeros (mean
  magnitude ≈ 0.3536, coefficient of variation 0.52%) — NUMERICAL.
- `prop:onset`: if the law $B+CN^{\alpha}$ with $\alpha=0.3085$ holds, the onset scale $N^*$
  is bounded below by the non-detection — CONDITIONAL on that law.
- Phase-resolved analysis: Davenport–Heilbronn resonances are driven by composites and have
  uniform prime phases, unlike the peaks of ζ — NUMERICAL.
- Whether partial sums detect off-line zeros at larger $N$ — OPEN.

## Files

- `main.tex`, `main.pdf` — source and compiled paper (LaTeX auxiliaries `main.aux`, `.log`,
  `.out`, `.toc` are also present).
- `reproduce_colab.py` — reproduction code.
- `figures/` — figures.

## Relation to other papers

Uses the partial-sum and phase framework of Papers 02–03.
