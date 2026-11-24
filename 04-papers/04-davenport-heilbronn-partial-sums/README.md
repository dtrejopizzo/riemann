# Partial sums of the Davenport–Heilbronn function at the ordinates of its off-line zeros

Paper 04. The Davenport–Heilbronn function $L_{DH}$ is a combination of the two Dirichlet
$L$-functions of the complex characters modulo 5; it satisfies a functional equation, has no
Euler product, and has zeros off the critical line. The paper studies its partial sums on the
critical line, $D_{DH}(t;N)=\sum_{n\le N}a_n n^{-1/2-it}$, at the ordinates of four off-line
zeros. Because the coefficients are periodic with mean zero, these sums converge to
$L_{DH}(1/2+it)$; the expectation that an off-line zero $\beta_0+i\gamma_0$ makes
$|D_{DH}(\gamma_0;N)|$ grow like $N^{\beta_0-1/2}$ is therefore false, and the off-line zeros
are not visible in this observable.

## What the paper contains

- **Proved** (Proposition 2.3): for $\mathrm{Re}\,s=\sigma>0$ and every $N$,
  $|L_{DH}(s)-\sum_{n\le N}a_n n^{-s}|\le(1+\kappa)(1+|s|/\sigma)N^{-\sigma}$; in particular
  $D_{DH}(t;N)=L_{DH}(1/2+it)+O((1+|t|)N^{-1/2})$.
- **Proved** (Proposition 6.1): for $5\mid N$,
  $\sum_{n\le N}a_n n^{-s}=L_{DH}(s)-\bar A N^{-s}-E$ with $\bar A=(3+\kappa)/5=0.6568$ and
  $|E|\le\bar A|s||s+1|N^{-\sigma-1}/(\sigma+1)$. No law $B+CN^{\alpha}$ with $C,\alpha>0$ can
  hold for $|D_{DH}(\gamma_0;N)|$.
- **Proved** (Proposition 5.2): for $5\mid N$, the mean resultant length of the phases
  $\arg a_n-t\log n$ over all $n\le N$ with $5\nmid n$ is at most $5|t|\log N/(2N)$.
- **Numerical illustration** (Tables 2–3, Figures 1, 2, 5): at $t=85.70,\ 114.16,\ 166.48,\
  176.70$ and $N=10^4,\dots,10^9$ the values of $|D_{DH}(t;N)|$, computed exactly from a Hurwitz
  zeta identity, converge to $0.3568,\ 0.0959,\ 0.0287,\ 0.2283$; the least-squares slopes of
  $\log|D_{DH}|$ against $\log N$ are $0.0008\pm0.0007$, $0.0034\pm0.0022$, $-0.0154\pm0.0051$,
  $-0.0016\pm0.0011$, and $\sqrt N\,|L_{DH}-D_{DH}|=0.657$ throughout.
- **Numerical** (Tables 4–5): maxima, kurtosis and resonance score of $|D_F(t;N)|$ over
  $t\in[100,200]$ for $\zeta$, $L(s,\chi_5)$, one random multiplicative function, $L_{DH}$ and a
  perturbed $L_{DH}$. The maxima converge for the series with periodic coefficients; the
  statistics do not single out $L_{DH}$.
- **Numerical, with explanation** (Table 6, Figure 3; $N=10^6$): the mean resultant length of
  the prime phases is about $1/|1-it|$ for $\zeta$, at peaks and elsewhere, and below
  $\pi(N)^{-1/2}$ on average for $L(s,\chi_5)$ and $L_{DH}$. The difference is the main term of
  the prime number theorem (the pole of $\zeta$ at $s=1$), not the Euler product.
- **Numerical** (Tables 7–8, Figure 4; $N=10^6$): no stratum of $L_{DH}$ by number of prime
  factors has significantly non-uniform phases at $t=114.16$ or $166.48$. At $t=85.70$ the
  squarefree classes cancel, with ratio $|\sum_k S_k^\flat|/(\sum_k|S_k^\flat|^2)^{1/2}=0.217$
  ($r=-0.953$); for the full classes the ratio is $0.126$. In view of Paper 03 this is expected
  at a point where the sum is small and is not specific to $L_{DH}$.

Nothing in the paper bears on the Riemann hypothesis.

## Known and new

The function, its functional equation and its zeros are classical (Davenport–Heilbronn;
Titchmarsh, §10.25; Spira; Balanzario–Sánchez-Ortiz), and the convergence of a Dirichlet series
with periodic coefficients of mean zero for $\mathrm{Re}\,s>0$ is standard partial summation.
What the paper adds is the explicit expansion with constants, the numerical illustration at the
four ordinates, and the explanation of the prime-phase statistic by the prime number theorem.

## Files

- [`main.tex`](main.tex) — LaTeX source.
- [`davenport-heilbronn-partial-sums.pdf`](davenport-heilbronn-partial-sums.pdf) — the paper (17 pages).
- [`reproduce_colab.py`](reproduce_colab.py) — the script that produces every number, table and
  figure (numpy, scipy, mpmath, matplotlib; no external data). Exact values by the Hurwitz zeta
  identity with 30 digits; direct sums in double precision with exactly rounded block
  summation. `python reproduce_colab.py` runs the computations of the paper (direct sums to
  $10^9$, scan to $10^7$; of the order of half an hour on a 20-core desktop);
  `python reproduce_colab.py --quick` stops the direct sums at $10^7$ and the scan at $10^6$.
- [`results/results.txt`](results/results.txt) — output of the script.
- [`figures/partial_sums_rho1.pdf`](figures/partial_sums_rho1.pdf) — Figure 1,
  $|D_{DH}(85.70;N)|$ and its limit.
- [`figures/partial_sums_four_zeros.pdf`](figures/partial_sums_four_zeros.pdf) — Figure 2, the
  same at the four ordinates.
- [`figures/prime_phase_R.pdf`](figures/prime_phase_R.pdf) — Figure 3, mean resultant length of
  the prime phases for $\zeta$, $L(s,\chi_5)$, $L_{DH}$ against $1/|1-it|$.
- [`figures/omega_class_vectors.pdf`](figures/omega_class_vectors.pdf) — Figure 4, the
  squarefree classes at $t=85.70$, $N=10^6$.
- [`figures/convergence_rate.pdf`](figures/convergence_rate.pdf) — Figure 5,
  $|L_{DH}-D_{DH}|$ against $\bar A N^{-1/2}$.

## Relation to other papers

Uses the ω-class decomposition of Paper 02 and the inter-class ratio of Paper 03.
