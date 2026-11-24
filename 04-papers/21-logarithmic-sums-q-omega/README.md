# Logarithmic sums of q^omega(n) and their shifted correlations: remarks

The paper studies the weights q^omega(n), q > 0, through the logarithmic sums
M_q(N) = sum_{n<=N} q^omega(n)/n and the shifted correlations
C(h,N;q) = sum_{n<=N} q^omega(n) q^omega(n+h)/n. The Dirichlet series factors as
zeta(s)^q G_q(s), and the paper records what this factorisation gives. Nothing in it depends on,
or proves, the Riemann Hypothesis.

## Results

- Lemma 2.1: G_q is holomorphic in Re s > 1/2, and zero-free there exactly when q <= 1 + sqrt 2.
- Proposition 3.1: M_q(N) = C_q (log N)^q + O((log N)^{q-1} + 1) (Selberg-Delange); for integer q,
  M_q(N) = P_q(log N) + O(N^{-delta}) for every delta < min(1/2, 1/q).
- Theorem 4.1: the Poisson large-deviation principle for omega(n) (classical).
- Proposition 5.2: for q >= 1, log N <= C(h,N;q) << (log N)^{2q-1}, via the Nair-Tenenbaum theorem.
- Theorem 5.3: divisor expansion of C(h,N;q) into harmonic sums over arithmetic progressions.
- Theorem 7.1: positivity and an explicit formula for the local densities.
- Proposition 8.1: M_q(N)/M_1(N)^q = C_q + O(1/log N) for q >= 1.
- Numerical observations (not proofs): (log N) C(1,N;4)/M_4(N)^2 stays near 0.9 for N up to 10^7;
  the O(1/log N) rate in Proposition 8.1 for q = 2 appears to be sharp.

The asymptotics are classical consequences of the Selberg-Delange method and of the
Nair-Tenenbaum theorem; the paper collects them and states them precisely. An asymptotic for
C(h,N;q) is left open.

## Files

- [main.tex](main.tex): LaTeX source
- [logarithmic-sums-q-omega.pdf](logarithmic-sums-q-omega.pdf): compiled paper, 7 pages
