# A second-moment identity for zero exponential sums and the localized Weil form

The paper studies the second moment V(d,T) of the exponential sum over the ordinates of the zeta zeros in a height window, and how it controls the window contribution to the Weil quadratic form on test functions supported in [-d,d]. It collects what can be said about V unconditionally, under RH, and under explicit hypotheses. It makes no claim about the sign of the form or about RH.

## Results

- **Theorem 2.1 (proved, elementary):** V(d,T) = ∫_{-2d}^{2d} |Σ e^{iγξ}|² dξ, with diagonal 4dN; hence 0 ≤ V ≤ 4dN².
- **Proposition 2.2 (proved):** the windowed zero sum satisfies 0 ≤ t_T[g] ≤ 2√d ‖g‖² V(d,T)^{1/2}. This is an upper bound for the window only; it gives no lower bound for the full form.
- **Proposition 3.1 (under RH):** by Montgomery's pair-correlation theorem, the low-frequency part (|α| ≤ 1) of a weighted version V_w of V is (2+o(1)) N(T) log T.
- **Proposition 3.2 (conditional):** under the hypothesis V ≪ dN(log T)^c for H ≥ 1 and d ≥ (log T)/2 (with c = 0 it fails for d = o(log T)), the window sum is ≪ d N^{1/2} (log T)^{c/2} ‖g‖².
- **Proposition 4.1 (under RH, Goldston's argument):** the integral of F over any unit interval is at most 8/3+o(1); hence V_w(d,T) ≪ dN(T) for d ≥ (log T)/2.
- **Theorem 5.1 / Corollary 5.2:** the Goldston–Montgomery equivalence (under RH) between the uniform form factor F(α) ~ 1 on [1, M] and the short-interval prime variance asymptotic; under RH and either condition, V_w = (4+o(1)) dN. No comparison between V_w and the window moment V is proved.
- **Proposition 6.2:** the relative-form-bound reduction for the negative index, as proved in Paper 11.
- **Numerics:** a quadrature check of Theorem 2.1 on one window of 80 zeros (agreement to 3.1×10⁻⁶, which measures only quadrature error), and exploratory computations on the prime tail (cutoff and near-critical counts for a few values of d), reported as numerical observations.

## What is known and what is new

Weil's explicit formula, Montgomery's theorem, Goldston's bound and the Goldston–Montgomery equivalence are known results, cited as such. The paper's contribution is the arrangement of these facts around the windowed second moment, the elementary identity and Parseval bound, and the conditional statements built on them.

## Files

- [main.tex](main.tex): LaTeX source.
- [second-moment-identity-zero-sums.pdf](second-moment-identity-zero-sums.pdf): compiled paper (11 pages).
- [code.py](code.py): both sides of the identity for zeros #1000–#1079 (Appendix A); output in [results_code.txt](results_code.txt).
- [atail.py](atail.py): extreme eigenvalues of the tail pencil for d = 4, 5 (Appendix B); output in [results_atail.txt](results_atail.txt).
- [near.py](near.py): near-critical spectrum of the full pencil for d = 3,…,6 (Appendix C); output in [results_near.txt](results_near.txt).
