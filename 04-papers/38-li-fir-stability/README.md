# The Li Sequence as a Sampled Control System: FIR Window Stability, Off-Line Modes, and the Arithmetic Closure Problem

The paper reads the Li–Keiper coefficients λ_n of the Riemann zeta function as the sampled output of a discrete-time system. Under the Cayley map w_ρ = 1 − 1/ρ, zeros on the critical line become unit-circle modes and zeros to the right become unstable modes. Moving windows of the sequence are FIR filters, and the paper studies which filtered outputs still detect an off-line zero and how these outputs are expressed in the von Mangoldt weights.

## What the paper proves

- For any FIR filter with no zero outside the unit circle (in particular every moving window and every finite cascade of moving windows), RH holds if and only if the filtered output is subexponential (Theorem 3.1, Corollaries 3.2, 3.3).
- For each fixed window length L, RH is equivalent to eventual nonnegativity of the sliding sums Y_L(N) (Theorem 4.1).
- The elementary bound |H_L|² + |H_{L+1}|² ≥ ½|z|^{2L}: two adjacent windows have no common zero (Proposition 5.1).
- The exact response 4 − 4cosh(na)cos(nθ) of an off-line quartet, and the exponential rate and two-sided excursions of λ_n when RH fails (Section 6; classical).
- Vanishing-trim, geometric-mean and block spectral-radius criteria for RH (Section 9).
- A prime–Laguerre identity for the window sums, and an explicit form of the prefix sums with the kernel L^{(3)} and the remainder of Mertens' formula (Sections 7 and 10).
- An explicit off-line quartet showing that negative signed block averages do not bound the block pointwise (Proposition 8.1).
- The arithmetic inequalities that would close the argument are stated exactly; each is equivalent to RH and none is proved.

## Known and new

The growth of λ_n off the critical line and the arithmetic formula are classical (Li; Bombieri–Lagarias). The window, cascade, robust-statistic and block-norm criteria and the Laguerre window identities are elementary reformulations given here.

## Files

- [`main.tex`](main.tex) — LaTeX source.
- [`li-fir-stability.pdf`](li-fir-stability.pdf) — compiled paper (16 pages).
- [`scripts/fir_window_bank_check.py`](scripts/fir_window_bank_check.py) — exact checks of the Laguerre window identity, the adjacent-window bound, the cascade survival of an off-unit mode and the rational quartet example (algebraic identities only).
