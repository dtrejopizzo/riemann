# PREREG_LAW_TEST — preregistration of the candidate law for −ln λ_A(T) and test on 4 distant random windows

Phase 187. Preregistration: written BEFORE computing the 4 new windows.
"Let's formalize the law that emerges and test it with 4 more distant and random windows."
Global label of this document: **NUMERICAL**; every proposed law is CONJECTURE (fit), not theorem.
Fit data: `DATA_100_WINDOWS.csv` read at 18:12 (45 converged windows with T ≤ 1.06; the campaign continues and
may add rows: they are not used). Definitions: λ_A(T) = inf 𝔞_T over 𝒫_T (README.md); T* = 2πe^{2T};
N(T*) = #{γ ≤ T*} (zeros150.npy, exact in the range). y(T) := −ln λ_A(T) (natural log). Fit script:
scratchpad `prereg_fit.py` (numpy lstsq; unweighted).

## 1. Editor's observation and candidate law L1

Observed: y/N(T*) ≈ 6.0–6.9 from T ≈ 0.8 on (e.g. 0.8047 → 26.47/4 = 6.62; 0.90 → 37.61/6 = 6.27; 0.9730 → 48.31/8 = 6.04;
1.06 → 63.30/10 = 6.33). Mean of y/N for T ≥ 0.8 (20 windows): 6.46; "each zero below T* divides λ_A by ≈ e^{2π}."

**L1 (the "a 2π jump per zero" law):** y(T) = 2π·N(T*) + δ(T), with δ bounded or slowly growing.
Fit on the 45 windows: δ(T) = y − 2πN is tabulated below. For T ≥ 0.8 (20 windows): **δ̄ = 0.884, sd = 2.150,
min −3.27 (T = 1.0397), max +4.97 (T = 1.015)**. δ(T) is a sawtooth: it rises ≈ linearly within each stretch
of constant N and drops ≈ 2π upon entering each zero (because y is continuous in T and 2πN jumps). Linear trend for T ≥ 0.8:
δ ≈ −4.3·T + 5.0 (not significant against sd 2.15; recorded anyway). L1 has **one free parameter** (δ̄) once the
constant 2π is fixed.

Table of δ(T) (T ≥ 0.8): 0.7947: +0.29 | 0.8047: +1.34 | 0.8147: +2.40 | 0.83: −2.24 | 0.85: +0.14 | 0.87: +2.46 | 0.89: +4.86 |
0.90: −0.09 | 0.92: +2.88 | 0.94: −0.77 | 0.955: +1.56 | 0.963: +2.80 | 0.973: −1.96 | 0.983: −0.48 | 0.995: +1.49 |
1.015: +4.97 | 1.0297: +1.21 | 1.03: +1.26 | 1.0397: −3.27 | 1.0497: −1.34 | 1.06: +0.47.
(T < 0.8: δ ∈ [−4.3, +5.1], same sawtooth; not used in the fit.)

## 2. Alternative laws (fitted on the same 20 windows T ∈ [0.8, 1.06], free parameters in parentheses)

| law | form | fitted parameters | sd resid | max |resid| |
|---|---|---|---|---|
| L1 | 2π·N + δ̄ | δ̄ = 0.884 (1) | 2.150 | 4.97 |
| L2a | 2π²·N/ln N (Zhu, fixed c; its λ is λ_W, even tests) | none (0) | — | resid ∈ [−32.2, −20.7]: **already refuted for λ_A at T ≤ 1.06** |
| L2b | c·N/ln N | c = 12.69 (1) | 5.761 | 10.26 |
| L2c | c·N/ln N + d | c = 24.04, d = −41.74 (2) | 2.035 | 4.46 |
| L3 | c·e^{2T} + d | c = 11.091, d = −29.258 (2) | **0.152** | **0.276** |
| L4 | a·N·ln N + b | a = 2.006, b = 17.02 (2) | 2.168 | 4.85 |

Finding from the fit (before the test): the continuous form L3 fits y(T) with maximum residual 0.28 nats over the whole
[0.8, 1.06]; the forms stepped in N(T*) (L1, L2, L4) have residuals of ±2–5 nats that are exactly the sawtooth
between consecutive zeros. Since T ↦ λ_A is continuous (CONSTRAINTS 1.3), L1 can only hold "on average"
over stretches; the preregistered question is whether the **mean slope** of y is 2π per zero (L1) or whether it tracks e^{2T}
(L3: slope per zero ≈ 11.09·e^{2T}/(dN/dT) → 11.09/(2T−1)·(1+o(1)) with N ≈ e^{2T}(2T−1), i.e. **decreasing**
in T: 6.3 at T ≈ 1 but ≈ 5.0 at T ≈ 1.45) or N/ln N (L2: increasing in N). The three are distinguishable in the test range.

Admissibility (CONSTRAINTS §6.1): the four laws are increasing in T (λ non-increasing, 1.1), continuous except for L1/L2/L4
(stepped: valid only as an average), above the closed bound 1.5 (trivial for T ≤ 1.5), and compatible with
Thm M (1.6) in this range (none is asymptotic: all are pre-asymptotic and are not extrapolated to T → ∞).

## 3. Random choice of the 4 windows (fixed before computing)

Procedure: `random.seed(187)`; T = round(uniform(1.12, 1.45), 3) drawn successively; accepted if it is ≥ 0.06 away
from those already accepted and > 0.01 away from every boundary ½log n with n a prime power in the range (½log 9, 11, 13, 16, 17, 19, 23, 25);
until 4 are obtained. Result: **T ∈ {1.128, 1.236, 1.316, 1.447}** (none is on the campaign grid).
Exact N(T*) with zeros150.npy: T* = 59.97, 74.43, 87.35, 113.51 → **N(T*) = 13, 18, 23, 35**.

## 4. Predictions (in nats, y = −ln λ_A) and bands

Preregistered band for each law: ± (max |residual| in the fit T ≥ 0.8 + 1.0 nat margin per window). The 1.0-nat margin
covers the Galerkin error (the M-histories in the CSV show that y^{(M)} stabilizes to 0.05–0.2 nats
from M ≈ T*·T on; here M is fixed at ≈ 1.2·T*·T + 20, see §5) and the arithmetic precision (≥ 15 digits of margin).

| T | N(T*) | L1: 2πN + 0.884 (± 5.97) | L2a: 2π²N/ln N (± 33.2) | L2c: c N/ln N + d (± 5.46) | L3: c e^{2T} + d (± 1.28) | L4: a N ln N + b (± 5.85) |
|---|---|---|---|---|---|---|
| 1.128 | 13 | 82.57 | 100.04 | 80.13 | 76.61 | 83.90 |
| 1.236 | 18 | 113.98 | 122.93 | 108.00 | 102.13 | 121.38 |
| 1.316 | 23 | 145.40 | 144.79 | 134.64 | 124.93 | 161.68 |
| 1.447 | 35 | 220.80 | 194.32 | 194.96 | 171.11 | 266.63 |

(L2b: 64.3, 79.1, 93.1, 125.0 ± 11.3; recorded but already the worst in the fit.) The bands of L1 and L3 are disjoint at
all 4 windows; L1 and L2c are disjoint at T = 1.447; L1 and L4 are disjoint at T ≥ 1.316.

## 5. Success criterion (pre-established)

- L1 "holds" if all 4 observations fall within its band [2πN + 0.884 ± 5.97]; "fails" if ≥ 2 fall outside;
  with exactly 1 outside: "indeterminate" (reported, no verdict).
- The same criterion applies to L2c, L3, L4 with their bands. If the observation falls within the band of only one law at T = 1.447,
  that law remains a candidate and the others are deemed to have failed in that range.
- Drift of the constant: δ(T) = y − 2πN is recomputed at the 4 points; constant 2π "holds up" if δ stays in
  [−6, +6]; if δ grows monotonically with N (toward 2π²/ln N − 2π per zero, i.e. L2) or decreases monotonically (toward
  11.1/(2T−1) per zero, i.e. L3) the direction of the drift is declared.
- Computation: `r187_campaign.py` pipeline (run_window imported; arb arithmetic, Galerkin–Legendre, variational UPPER
  bound of λ_A, i.e. y^{(M)} ≤ y). M fixed per window (M_override: 120, 140, 160, 200), extra_digits so
  that the precision margin is ≥ 15 digits without redoing (dps ≥ −log10 λ + 15, using the largest prediction, L1/L4).
  The variation of y between the blocks M − 20 and M is reported; if relvar ≥ 10⁻² (CSV criterion) the row is marked
  NOT CONVERGED and λ_A is an upper bound: for the test it suffices that the variation of y in M be ≪ the band (0.3 nats).
  Output: `DATA_PREREG_4.csv` (same columns; stage = prereg). Budget ≈ 2 h with 4 processes.

## 6. What each result implies and does NOT imply

- If L1 holds: the "2π nats per zero below T*" law remains a **quantitative NUMERICAL conjecture** over 28 + 4
  windows in [0.8, 1.45]; it is a candidate two-sided law (CONSTRAINTS 3.2) only if it is stated as
  λ_A = e^{−2πN(T*)−δ(T)}(1+o(1)) with explicit δ and is **proved per window**. It changes no grid label.
- If L3 holds and L1 fails: the slope per zero decreases with T (≈ 11.1/(2T−1)); the constant 2π of the editor's
  observation would be a coincidence of the range T ≈ 1 (where 2T − 1 ≈ 1 and 11.1·e^{2T}/N ≈ 2π·(1+ε)). Note that L3 is
  also a pre-asymptotic law: Thm M (1.6) requires y ≥ e^{(2−ε)T} and L3 satisfies it, but d < 0 makes it incompatible with
  y ≥ 0 as T → 0; it is not extrapolated outside [0.8, 1.5].
- If L2c holds: the slope per zero grows with N (Zhu's form with c ≈ 24 ≠ 2π², and a strongly negative constant d);
  the N/ln N family would remain alive for λ_A with parameters different from those of λ_W.
- **What NO result implies:** (i) anything about λ_A(T) ≥ 0 for all T: by the non-identifiability theorem
  (Thm F + Theorem 3, CONSTRAINTS 3.1) the function f_t with N₀ = e^{2·1.45} ≈ 18.2 produces the same data for T ≤ 1.45 and
  has a finite first contact; a law fitted on a finite range only describes; (ii) anything about the sign on any
  new window (W-det: leading term + O(1) relative error); (iii) anything about λ_W (ratio λ_A/λ_W = e^{12…15} at
  ½log5, CONSTRAINTS 1.10): Zhu's constant 2π² refers to a different form; (iv) anything about T → ∞: the 4 laws are
  pre-asymptotic fits with N ≤ 35. If nneg > 0 or λ_A ≤ 0 appears in any window it is reported as a possible contact
  with the sign and checked against the noise (pipeline's nneg_flag), without changing any label.

## 7. Verdict
(completed after the computation; §1–§6 are not modified after this line)
