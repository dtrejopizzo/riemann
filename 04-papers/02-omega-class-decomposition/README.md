# Paper 02 — The ω-Class Decomposition of Dirichlet Polynomials: A New Framework for the Lindelöf Hypothesis

The paper splits the Dirichlet polynomial $D(t;N)=\sum_{n\le N} n^{-1/2-it}$ into sub-sums
$S_k(t;N)$ indexed by $\omega(n)=k$, the number of distinct prime factors, and studies the
amplification ratio $(1+r)=|D|^2/\sum_k|S_k|^2$. It proves unconditional bounds on this ratio
and a one-directional reduction: a uniform bound $B(N)=\max_{t,k}|S_k|^2\le C_\varepsilon N^\varepsilon$
implies the Lindelöf hypothesis. This sufficient condition is plausibly strictly stronger than
Lindelöf. The paper also reports computations up to $N=1.5\times10^5$.

## Main results

- `thm:CS`, `thm:Kcount`, `thm:refined`: unconditional bounds on the amplification ratio — PROVED.
- `thm:reduction`, `cor:lindelof`: $B(N)\le C_\varepsilon N^\varepsilon$ for all $\varepsilon$ implies
  Lindelöf — PROVED (as an implication; the hypothesis is OPEN).
- `prop:stronger`: the class-wise bound is one-directional (sufficient, not equivalent), and plausibly strictly stronger than Lindelöf — PROVED for the one-directional part; strictness ARGUED.
- `thm:master`: $B(N)\le N^\alpha$ gives $|\zeta(\tfrac12+it)|\ll t^{\alpha/2+\varepsilon}$ via the
  approximate functional equation — CONDITIONAL.
- `prop:sqrt_scaling` and the empirical exponents $\alpha_B$ decreasing from 0.428 to 0.395,
  the $k=2\to3$ dominance transition near $N\approx10^5$, and phase resonance with Rayleigh
  statistic $R\approx0.92$ — NUMERICAL.
- A uniform bound on $B(N)$ over all ω-classes — OPEN.

## Files

- `main.tex`, `main.pdf` — source and compiled paper.
- `reproduce.py`, `reproduce_colab.py` — reproduction code.
- `figures/`, `results/` — figures and computed data.

## Relation to other papers

Paper 03 resolves the sign of the inter-class ratio $r$; Paper 05 develops the ω-class
hierarchy for ζ.
