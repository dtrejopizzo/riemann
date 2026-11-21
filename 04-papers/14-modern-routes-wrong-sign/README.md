# Hodge-index and hyperbolicity reformulations of the Riemann hypothesis as positivity statements

The paper looks at two reformulations of the Riemann hypothesis that do not look, at first sight, like quadratic-form positivity. The first is a Hodge-index picture built on the band-limited Weil–Carleson form of Paper 12. The second is hyperbolicity of the Jensen polynomials of Ξ(t) = ξ(1/2 + it). In both cases it writes down the relevant criteria as explicit positivity statements.

## Results
- **Moment identity (proved):** b(k) = (−1)^k a(k) = 2^{2k+3} m_{2k}/(2k)!, where a(k) are the Taylor coefficients of Ξ and m_{2k} are the even moments of the de Bruijn–Newman kernel Φ (normalization Ξ(t) = 8∫₀^∞ Φ(u) cos(2tu) du). Checked numerically for k ≤ 4.
- **Sine-kernel Gram (proved):** for distinct normalized zeros the Gram matrix G is positive definite, and λ_min(G) ≤ 1 − sinc(πβ_min) ≤ (π²/6) β_min². As a consequence, a uniform lower bound on λ_min(G) would imply uniform separation of the zeros. No implication between such a bound and RH is known.
- **Classical criteria (cited):** Pólya's Jensen-polynomial criterion, the Aissen–Schoenberg–Whitney–Edrei Pólya-frequency criterion, Hermite's criterion for real-rootedness, and Laguerre's theorem that the Laguerre–Pólya class is closed under differentiation (so the Jensen shift preserves hyperbolicity for every function in that class).
- **Numerical observations:** λ_min(G)/β_min² for 25 consecutive zeros at T₀ = 10², 10³, 3·10³, 10⁴, the log-concavity inequalities b(k)² > b(k−1)b(k+1) for 1 ≤ k ≤ 7 (consequences of the Turán inequalities proved by Csordas–Norfolk–Varga), and positive-definite Hermite matrices for J^{d,n}, 2 ≤ d ≤ 4, 0 ≤ n ≤ 2 (in agreement with the Griffin–Ono–Rolen–Zagier theorem for d ≤ 8). The last two are numerical confirmations of known theorems; the Gram ratios (between 0.07 and 0.62) support no asymptotic relation between λ_min(G) and β_min².
- **Heuristic summary:** both routes reduce to positivity statements. This is stated as a heuristic, not as a theorem.

## Known and new
The criteria are classical (Pólya, Edrei, Hermite, Laguerre, Csordas–Norfolk–Varga, Griffin–Ono–Rolen–Zagier). The new parts are the moment identity written in this normalization, the elementary Gram bound, and the numerical tables.

## Files
- [main.tex](main.tex): LaTeX source
- [modern-routes-wrong-sign.pdf](modern-routes-wrong-sign.pdf): the paper (5 pages)
- [gram.py](gram.py): script that produces every numerical value in the paper (uses mpmath and numpy; run `python3 gram.py > output.txt`)
- [output.txt](output.txt): output of the script
