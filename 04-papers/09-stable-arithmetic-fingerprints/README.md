# Stable Local Arithmetic Fingerprints of Localized Explicit-Formula Forms

The paper studies a finite Hermitian matrix $Q(L)$ modelled on a localized explicit formula: an archimedean block minus a weighted sum of rank-one prime terms $\Lambda_L(n)n^{-1/2}w_nw_n^*$, built on Schwartz test functions with Gaussian decay of width $\sigma$. It is a model form with the shape of a localized explicit formula, not the Weil Gram matrix of Paper 07. The paper asks how much of $Q(L)$, its bottom eigenvalue and a per-prime profile is determined by the coefficients $\Lambda_L(n)$ with $n\le P$.

## Results

- Anatomy identity (Prop. 3.1): $\lambda_{\min}=R_\infty(u_0)-\sum_p R_p$, where the prime sum runs over $p^k\le X$.
- Gradient (Prop. 3.2): Hellmann–Feynman formula for $\partial\lambda_{\min}/\partial\Lambda_L(n)$ when the bottom eigenvalue is simple and the coefficients are real.
- Stability (Thm. 4.1): for an integer $P\ge2$, if $L,L'$ have the same archimedean block and $\Lambda_L(n)=\Lambda_{L'}(n)$ for $n\le P$, then $\|Q(L)-Q(L')\|$ and all eigenvalue differences are at most $(8A_0/\sigma^2)P^{1/2}e^{-\sigma^2(\log P)^2/2}$, when $\log P\ge\max(1/\sigma,1/\sigma^2)$, hence $O_\alpha(e^{-\alpha(\log P)^2})$ for every $\alpha<\sigma^2/2$; the profile satisfies an explicit $\ell^1$ bound under a spectral-gap hypothesis.
- Concavity and monotonicity (Thm. 5.1): $\lambda_{\min}$ is concave and coordinate-wise non-increasing in the real coefficients, so positivity over a coefficient box reduces to its upper corner.

Known ingredients: Weyl, Davis–Kahan, Hellmann–Feynman, concavity of $\lambda_{\min}$. What is new is their assembly into quantitative stability statements for this form. The paper contains no numerics, and the sign of $\lambda_{\min}$ is not addressed.

## Files

- [main.tex](main.tex) — LaTeX source.
- [stable-arithmetic-fingerprints.pdf](stable-arithmetic-fingerprints.pdf) — compiled paper (5 pages).
