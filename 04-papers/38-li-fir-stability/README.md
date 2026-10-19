# Paper 38 — The Li Sequence as a Sampled Control System: FIR Window Stability, Off-Line Modes, and the Arithmetic Closure Problem

The paper treats the Li–Keiper sequence as the sampled output of a discrete-time spectral system. Under the Cayley map w_ρ = 1 − 1/ρ a zero on the critical line becomes a unit-circle mode and a zero to the right becomes an unstable mode; the symmetric zero orbit has the exact response 4 − 4cosh(na_ρ)cos(nθ_ρ), and permanent cancellation of an unstable mode is impossible. For every fixed window length L the moving sum Y_L(N) is subexponential if and only if RH holds, and RH is equivalent to eventual nonnegativity of every sliding output. Window averaging is a cascade of FIR filters whose zeros lie on the unit circle, so no such cascade can cancel an off-line mode; an adjacent-window bank with no blind spot is constructed. The arithmetic side is expressed through a prime–Laguerre FIR identity, and the closure problem is stated as an arithmetic window criterion.

## Main results

- No-cancellation FIR criterion; sliding-window stability; cascade invariance — PROVED.
- Eventual moving-window positivity equivalent to RH — PROVED.
- Adjacent-bank coercivity |H_L|² + |H_{L+1}|² ≥ ½|z|^{2L} and the two-channel energy criterion — PROVED.
- Exact quartet response; global exponential rate; two-sided syndetic excursions; marginal-stability criterion — PROVED.
- Prime–Laguerre FIR identity and exact arithmetic window criterion — PROVED.
- Linear-cascade limitation — NO-GO for linear cascades.
- Vanishing-trim, geometric-growth and block spectral-radius criteria — PROVED.
- The arithmetic closure problem (verifying a window criterion from the primes) — OPEN.

## Files

- `main.tex` — LaTeX source; `main.pdf` — compiled paper; `main.aux`, `main.log`, `main.out`, `main.toc` — build files.

## Relation to other papers

Reformulates the Li–Keiper endpoint of Papers 36–37.
