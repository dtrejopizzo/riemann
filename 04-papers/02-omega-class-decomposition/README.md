# The ω-class decomposition of Dirichlet polynomials: elementary bounds and computations

Paper 02. The paper splits the Dirichlet polynomial
$D(t;N)=\sum_{2\le n\le N} n^{-1/2-it}$ into the sub-sums $S_k(t;N)$ over the integers with
$\omega(n)=k$ distinct prime factors, and compares $|D|^2$ with $E=\sum_k|S_k|^2$ through the
ratio $1+r=|D|^2/E$. It records the elementary inequalities between $D$ and the class sums,
a conditional bound for $\zeta(\tfrac12+it)$ in terms of the largest class sum, and
computations of the class sums for $N\le 1.5\times10^5$.

## What the paper contains

Proved:

- $|D|^2\le K_N\,E\le K_N^2\max_k|S_k|^2$, where $K_N\le\log_2 N$ is the number of classes
  (Theorems 3.1 and 4.1; Cauchy–Schwarz), and the refinement
  $1+r\le(\sum_k\sqrt{p_k})^2$ with $p_k=|S_k|^2/E$ (Theorem 6.1).
- $K_N\sim\log N/\log\log N$ (Theorem 5.1; classical).
- If $B(N)=\max_{t\in[N/10,N],\,k}|S_k(t;N)|^2\le N^\alpha$ for all large $N$, then
  $\zeta(\tfrac12+it)\ll t^{\alpha/2}\log t$ (Theorem 7.1). In particular the bound
  $B(N)\le C_\varepsilon N^\varepsilon$ for every $\varepsilon>0$ implies the Lindelöf
  hypothesis (Corollary 4.2). This is an implication in one direction only, and it uses only
  the number of classes. The hypothesis is not known to follow from Lindelöf, and for $k=1$
  it is expected to be as strong as the Riemann hypothesis.
- The mean square of each $S_k$ over $[0,T]$ is $\sum_{\omega(n)=k,\,n\le N}1/n+O(\pi_k(N)/T)$,
  and this sum is at most $(\log\log N+c_0)^k/k!$ (Proposition 4.3; mean value theorem of
  Montgomery and Vaughan).
- A variant of the conditional bound with class sums of length $\sqrt{t/2\pi}$
  (Proposition 7.3).

Numerical (grid of spacing $\pi/\log N$ in $t\in[N/10,N]$ with local refinement of the
largest maxima; all maxima are lower bounds), for $N=10^4,\ 5\times10^4,\ 10^5,\ 1.5\times10^5$:

- $B(N)\ge 52.08,\ 84.40,\ 121.57,\ 148.40$, so $\log B/\log N = 0.429,\ 0.410,\ 0.417,\ 0.420$:
  between 0.41 and 0.43, with no monotone trend.
- The class attaining the maximum changes from $k=2$ to $k=3$ between $N=5\times10^4$ and
  $N=10^5$.
- The largest value found of $1+r$ is $4.15,\ 4.55,\ 4.77,\ 4.87$, that is 17–24% below $K_N$.
- At $N=1.5\times10^5$ the grid mean of $|S_k|^2$ agrees with $\sum 1/n$, and the largest
  values found exceed the mean by factors from 8.6 ($k=1$) to 131 ($k=5$).
- At the point $t^*=100799.243$ where the largest $|S_3|^2$ was found, the contributions of
  the five decades of $n$ have nearly equal arguments (resultant length 0.95); the classes
  $k=2,3,4$ are all large there, while $1+r=0.022$, so the classes cancel one another.
- For the Liouville function, $|\sum_{n\le10^5}\lambda(n)n^{-1/2-it}|=46.88$ at $t=7563.5$,
  next to three close zeros of $\zeta$.

The data do not determine the behaviour of $B(N)$ as $N\to\infty$.

## Known and new

The inequalities are the Cauchy–Schwarz and triangle inequalities; the asymptotic for $K_N$,
the approximation of $\zeta(\tfrac12+it)$ by a partial sum (Titchmarsh, Theorem 4.11) and the
mean value theorem are classical. What the paper adds is the bookkeeping by $\omega$-classes,
the precise statement of the conditional bound, and the computations.

## Files

- [main.tex](main.tex) — source.
- [omega-class-decomposition.pdf](omega-class-decomposition.pdf) — the paper, 15 pages.
- [reproduce.py](reproduce.py) — computes the class sums for the four values of $N$ and
  writes all tables' data, the four figures and the results file (about one hour with 16
  processes; `--quick` runs $N=10^4$ only; `--validate` adds the comparison with `mpmath`).
- [reproduce_colab.py](reproduce_colab.py) — short single-file version: grid values for one
  $N$, without refinement.
- [figures/](figures/) — `fig1_alpha_B_trend`, `fig2_crossover`, `fig3_peak_to_mean`,
  `fig4_resonance` (PDF and PNG), written by `reproduce.py`.
- [results/computation_results.json](results/computation_results.json) — output of
  `reproduce.py`; the numbers in the paper are taken from this file.

## Related papers of the series

Paper 03 studies the sign of $r$; Paper 05 continues the study of the $\omega$-classes.
