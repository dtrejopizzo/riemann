# The localized-Weil anatomy of L-functions: Euler products, Satake power sums, and Rankin–Selberg products

The paper studies the anatomy of a Dirichlet series L in the class S^# (Selberg class without the Euler product axiom): the per-n profile R_L(n) = 2 Λ_L(n) n^{-1/2} c_0(log n) (Λ_L assumed real), where c_0 is the autocorrelation of the ground state of the localized Weil form on a Hermite–Gauss window. It asks how far the anatomy detects the multiplicative structure of L.

What the paper proves or observes:

- An Euler product forces the anatomy to vanish off prime powers (forward direction, unconditional).
- Converse under a hypothesis: if c_0(log n) ≠ 0 at every non-prime-power n (in one window, or in at least one of two windows), factorizing anatomy gives an Euler product. If the ground state is within ε of the Gaussian, the hypothesis holds for log n < 2σ√log(1/(3ε)). The unconditional converse is open.
- The autocorrelation of a window function is a polynomial times a Gaussian; for pure Hermite modes it equals 2^m m! √π σ L_m(u²/2σ²) e^{-u²/4σ²} (Laguerre).
- Positivity of the local form is restated as a conjugated operator inequality; λ_min is concave in the coefficients, so its minimum over a box is at a vertex. Whether the vertex values are positive is not addressed.
- For self-dual GL(n), where c_0(log p^k) ≠ 0: the anatomy gives the Satake power sums, hence the local factors, the number of distinct nonzero parameters (Hankel rank) and max|α_{i,p}| (limsup formula).
- Degree one: under the two-window hypothesis and the Selberg-class bounds, L is ζ or the L-function of a real primitive Dirichlet character, by the Kaczorowski–Perelli classification.
- Numerical check: the script confirms the Laguerre formula for pure Hermite modes only. It does not test the ground state of any Q_L.

Known vs new: the generating-function and power-sum identities (Newton–Girard, the log-derivative of the Euler factor, Rankin–Selberg and isobaric Satake parameters) are standard, and so is the degree-one classification (Kaczorowski–Perelli). What is new is how they are expressed through the anatomy, and the conditional converse with its quantitative near-Gaussian range.

Files:

- [main.tex](main.tex): LaTeX source
- [anatomy-local-invariant.pdf](anatomy-local-invariant.pdf): compiled paper (10 pages)
- [code.py](code.py): computes the autocorrelation zeros of pure Hermite–Gauss modes (Lemma 4.1)
- [output.txt](output.txt): output of `code.py`, included in the appendix
