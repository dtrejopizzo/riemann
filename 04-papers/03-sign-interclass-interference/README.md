# On the Sign of Inter-Class Interference in Dirichlet Partial Sums: A Peak–Trough Reconciliation

Paper 03. For the ω-class decomposition $D_F=\sum_k S_k$ of a Dirichlet partial sum
$D_F(t;N)=\sum_{n\le N}a_n n^{-1/2-it}$ (the terms grouped by the number $\omega(n)$ of distinct
prime factors), the paper studies the inter-class energy ratio
$r=(|D_F|^2-\sum_k|S_k|^2)/\sum_k|S_k|^2$, which is positive when the classes add constructively
and negative when they cancel. The point of the paper is that $r$ has no characteristic sign:
the sign of a mean of $r$ depends on the set of $t$ over which the mean is taken.

## What the paper contains

- **Proved** (Proposition 3.1): for $|a_n|\le 1$, the average of the cross-term
  $X=|D_F|^2-\sum_k|S_k|^2$ over any interval of length $H$ is at most $12\pi N/H$ in absolute
  value. This is informative only for $H$ large compared with $N$, and it says nothing about the
  mean of $r=X/E$.
- **Elementary bounds** (Section 2): $E=\sum_k|S_k|^2\ge|a_1|^2$ and $-1\le r\le K_N-1$, where
  $K_N$ is the number of non-empty classes.
- **Numerical** (Observation 4.1, Table 1, Figure 1; $\zeta$, $N=10^5$, $5498$ points of
  $[100000,103000]$): the mean of $r$ over the deciles of $|D_\zeta|$ increases from $-0.998$
  (lowest decile, every point negative) to $+1.544$ (highest decile, $92\%$ of the points
  positive) and changes sign near the 69th percentile. Over the whole sample the mean of $r$ is
  $-0.26$ and $73\%$ of the points have $r<0$. A random completely multiplicative model (five
  seeds) has the same profile.
- **Numerical** (Remark 5.1): at $t=150000$, $N=10^5$, one has $r=-0.779$; the point lies $0.26$
  from a near-zero of $D_\zeta$ and in the lower half of the local distribution of $|D_\zeta|$.

The numerical statements concern one window and one value of $N$. Nothing in the paper bears on
the Riemann hypothesis or the Lindelöf hypothesis.

## Known and new

The bound for the cross-term is a direct consequence of the mean value theorem of Montgomery and
Vaughan (*Hilbert's inequality*, 1974), and the ω-class decomposition is that of Paper 02. What
is new here is the numerical decile profile of $r$ and the resulting explanation of why
single-point values and top-decile means of $r$ have opposite signs.

## Files

- [`main.tex`](main.tex) — LaTeX source.
- [`sign-interclass-interference.pdf`](sign-interclass-interference.pdf) — the paper (5 pages).
- [`reproduce_colab.py`](reproduce_colab.py) — Python script (NumPy, Matplotlib) that produces
  every numerical value in the paper and the figure; ten to thirty minutes on a desktop machine.
- [`rbar_vs_quantile.pdf`](rbar_vs_quantile.pdf), [`rbar_vs_quantile.png`](rbar_vs_quantile.png)
  — Figure 1, the decile means of $r$ for $\zeta$ and for the random multiplicative control.

## Relation to other papers

Uses the ω-class decomposition of Paper 02.
