# The Band-Limited Weil–Carleson Form: a numerically saturated generalized eigenvalue, sine-kernel structure of its spectrum, and a comparison of five reformulations

The paper looks at Weil's explicit formula for ζ restricted to test functions of exponential type d. On that class the prime side is a finite sum. On a sinc basis at height T₀ it studies, numerically, the largest generalized eigenvalue C of the prime Gram matrix relative to the archimedean Gram matrix.

## Results

- **Proved (Proposition 2.1):** for f the Fourier transform of a function of bounded variation supported in [−d, d] (a class containing the sinc basis), only n ≤ e^{2d} enter the prime side. The full identity includes the pole term 2 Re(f(i/2)·conj f(−i/2)), which in general has no sign.
- **Numerical (Observation 3.1):** at T₀ = 1000 with a 29-dimensional sinc basis, C equals 1 to five digits at the two computed values d = 3 and d = 5 (2d/log T₀ = 0.87 and 1.45) and is below 1 at d = 1, 2, 2.5 (0.339, 0.785, 0.922 for d = 1, 2, 2.5). The archimedean Gram matrix is numerically positive definite in all cases computed. C is a diagnostic only: C ≤ 1 is neither implied by RH nor known to imply it.
- **Numerical (Observation 4.1):** at d = 1.3, T₀ = 80 the spectrum has 27 eigenvalues of order one, one for each of the 27 zeros in the window (the smallest 1.2), followed by 0.5 and 0.04. The normalised zero Gram matrix agrees with the sine kernel to 7·10⁻².
- **Numerical (Observation 5.1):** a table of eigenvalues of the prolate (sinc) kernel.
- **Heuristic:** the analogy with the Connes–Consani prolate approach (Section 5) and the comparison of five reformulations (Section 6).

## Known and new

Weil's criterion, the explicit formula, the prolate eigenvalue facts (Slepian–Pollak) and the Connes–Consani archimedean positivity are known results. What is new is the band-limited generalized-eigenvalue diagnostic and the numerical observations about it.

## Files

- [main.tex](main.tex): LaTeX source
- [band-limited-weil-carleson.pdf](band-limited-weil-carleson.pdf): compiled paper (6 pages)
- [carleson_engine.py](carleson_engine.py): computes C(d, T₀) (Observation 3.1), including the archimedean tails beyond the quadrature window; output in [results/carleson_engine.txt](results/carleson_engine.txt)
- [sinekernel.py](sinekernel.py): spectrum at d = 1.3, T₀ = 80 and the comparison with the sine kernel (Observation 4.1); output in [results/sinekernel.txt](results/sinekernel.txt)
- [prolate.py](prolate.py): prolate eigenvalue table and the zero of Φ (Observation 5.1); output in [results/prolate.txt](results/prolate.txt)
