# Tool 001: a multiprecision Galerkin engine for a_T

All values in this note are NUMERICAL. A Galerkin minimum is an upper bound for λ_A(T) up to the
stated matrix error; nothing here proves or refutes (★). Code: `tools/galerkin_mp.py`; usage:
`tools/README.md`; matrices: `tools/cache/`.

## 1. What the tool computes

Basis: the first N Dirichlet sines on (−T, T), both parities, orthonormal. Outputs: Arch, Π (true
Λ comb, all prime powers n < e^{2T}, or any comb supplied as (log n, v_n) pairs), the Tate vectors A,
B, the projector onto P_T, the per-parity bottom eigenpairs of a_T on P_T, the Galerkin λ_A(T),
Θ_T = max_μ λ_min(Arch − μΠ on P_T) with its maximiser c*, near-null cluster counts and principal
angles between subspaces.

Archimedean form: the Lévy form of STATEMENT_001 §1 was chosen over the symbol integral. With the
exact correlations of two sines, every entry of Arch is a combination of three one-dimensional
moments of K over [0, 2T] and the closed-form tail ∫_{2T}^∞ K; the integrands are analytic on the
closed interval, so composite Gauss–Legendre converges geometrically. Error control: a second
evaluation with 1.5× panels and 8 more nodes per panel; the estimated entry error is below
10⁻⁵⁶ at 40 digits (working precision 60 digits), i.e. at the precision floor. Cross-checks:
Π, A, B agree with the earlier double-precision code to 10⁻¹⁴; Arch agrees with the earlier
double-precision symbol quadrature to 10⁻⁸ (the truncation error of that code); Arch_{11} at
T = 0.9 agrees with an independent 30-digit symbol-side quadrature to 7·10⁻¹⁴, within that
quadrature's own error estimate (10⁻¹¹).

Resolution floor: at 40 digits, eigenvalues below about 10⁻⁵⁷ are noise. One case below
needed 80 digits.

## 2. Validation (40 digits)

| T | N | Galerkin λ_A | parity | reference | time (build + eig) |
|---|---|---|---|---|---|
| ½log3 | 40 | 1.058·10⁻³ | even | Theorem C lower bound 8.86·10⁻⁵ | 14 s + 3 s |
| ½log3 | 80 | 1.008·10⁻³ | even | same | 45 s + 17 s |
| log 2 | 80 | 1.1137·10⁻⁷ | even | 1.1·10⁻⁷ (Paper 47 App. C) | 44 s + 21 s |
| ½log5 + 10⁻³ | 80 | 3.088·10⁻¹² | even | 3.1·10⁻¹² (ROUND_005_B) | 44 s + 24 s |
| 0.9 | 80 | 6.03·10⁻¹⁷ | even | 4.5·10⁻¹⁵ (ROUND_005_B, double) | 45 s + 23 s |

At ½log3 the Galerkin value is an upper bound of about 1.0·10⁻³, compatible with (above) the
certified lower bound 8.86·10⁻⁵; the two numbers are not meant to coincide. At log 2 and
½log5 + 10⁻³ the double-precision values are reproduced. At T = 0.9 the double-precision value
4.5·10⁻¹⁵ was round-off: the correct N = 80 value is 6.0·10⁻¹⁷.

## 3. λ_A at T = 1.0, 1.2, 1.4 (40 digits; one 80-digit check)

Columns: bottom eigenvalue per parity sector, and the number of eigenvalues below 10⁻⁶ / 10⁻⁹ in
each sector of P_T. Bound: 4·10⁹ T e^{−15.449T} (cor:margin1).

| T | N | λ_A | parity | even: λ₁, #<10⁻⁶, #<10⁻⁹ | odd: λ₁, #<10⁻⁶, #<10⁻⁹ | bound | time |
|---|---|---|---|---|---|---|---|
| 1.0 | 60 | 2.49·10⁻²³ | even | 2.49·10⁻²³, 4, 3 | 1.27·10⁻²⁰, 3, 3 | 7.8·10² | 26 s |
| 1.0 | 90 | 1.96·10⁻²³ | even | 1.96·10⁻²³, 4, 3 | 1.03·10⁻²⁰, 3, 3 | | 72 s |
| 1.0 | 120 | 1.74·10⁻²³ | even | 1.74·10⁻²³, 4, 3 | 9.95·10⁻²¹, 3, 3 | | 156 s |
| 1.2 | 60 | 5.11·10⁻³⁷ | even | 5.11·10⁻³⁷, 7, 6 | 2.32·10⁻³⁴, 7, 6 | 4.3·10¹ | 32 s |
| 1.2 | 90 | 2.61·10⁻⁴¹ | even | 2.61·10⁻⁴¹, 7, 7 | 4.40·10⁻³⁸, 7, 6 | | 39 s |
| 1.2 | 120 | 1.26·10⁻⁴¹ | even | 1.26·10⁻⁴¹, 7, 7 | 2.09·10⁻³⁸, 7, 6 | | 142 s |
| 1.4 | 60 | 2.95·10⁻⁴⁷ | even | 2.95·10⁻⁴⁷, 10, 9 | 6.78·10⁻⁴⁵, 10, 9 | 2.3 | 37 s |
| 1.4 | 90 | 5.35·10⁻⁵⁸ | even | 5.35·10⁻⁵⁸, 12, 11 | 6.90·10⁻⁵⁶, 12, 11 | | 88 s |
| 1.4 | 120 (80 digits) | 5.67·10⁻⁶⁵ | even | 5.67·10⁻⁶⁵, 13, 12 | 7.43·10⁻⁶², 12, 11 | | 83 s |

At T = 1.4, N = 120 and 40 digits the computed value was −5·10⁻⁶⁰, below the floor; the 80-digit
rerun gives +5.7·10⁻⁶⁵ (the N = 90 value is identical at 40 and 80 digits).

Reading (NUMERICAL):
- The bottom vector is even in every case; the odd sector sits 2–3 orders of magnitude higher.
- At T = 1.0 the value is nearly stable in N (2.5 → 1.7·10⁻²³); at T = 1.2 and 1.4 it is not
  converged in N (it falls by 4 and 18 orders from N = 60 to 120), so these are upper bounds
  only, and the true λ_A may be much smaller.
- The near-null cluster (both sectors together, below 10⁻⁶) grows with T: 7 at T = 1.0,
  14 at 1.2, and 20 / 24 / 25 at 1.4 for N = 60 / 90 / 120 (so also with N at T = 1.4).
- cor:margin1 gives 7.8·10², 4.3·10¹, 2.3 at these T: the Galerkin values are far below the
  bound, so in this range the bound has no content.
- Stability of the near-null space (eigenvalues < 10⁻⁹, both sectors) between N = 90 and N = 120,
  principal angles: T = 1.0 (dims 6, 6): all ≤ 5.6·10⁻⁴; T = 1.2 (13, 13): all ≤ 2.1·10⁻³;
  T = 1.4 (22, 23): all but the largest ≤ 2.5·10⁻³, largest 0.082. The cluster is a
  well-defined subspace, with only its edge vector moving with N. (Angles computed at 15 digits.)

## 4. Θ_T (N = 60, 40 digits)

| T | Θ_T | c* | λ_A (μ = 1) | time |
|---|---|---|---|---|
| log 2 | 6.72·10⁻⁵ | 0.998277 | 1.13·10⁻⁷ | 75 s |
| 1.0 | 5.35·10⁻²⁰ | 1 − 3.3·10⁻¹⁸ | 2.49·10⁻²³ | 59 s |
| 1.2 | 5.11·10⁻³⁷ | 1 (to 10⁻³⁰) | 5.11·10⁻³⁷ | 81 s |
| 1.4 | 2.95·10⁻⁴⁷ | 1 (to 10⁻³⁰) | 2.95·10⁻⁴⁷ | 101 s |

The maximum over μ is a kink, so Θ is resolved only if the μ-tolerance is far below the target
(the tool uses 10^{-3·dps/4} and always also evaluates μ = 1). A first run with tolerance 10⁻¹²
gave spurious negative Θ ≈ −10⁻¹³; that run is discarded. From T = 1.0 on, the optimal scaling
coincides with the true comb to the resolved digits.

## 5. Limits

Upper bounds only; no interval arithmetic (python-flint 0.9.0 is installed and could be added for
certified enclosures of the matrices, not done here). N-convergence at T ≥ 1.2 is not reached at
N = 120; larger N or a different basis would be needed for values rather than bounds.
