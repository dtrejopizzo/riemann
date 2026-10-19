# R9 — Phase 2.3.F-CLOSE-II: three new fronts (N1 Lanczos · N2 traces · N3 Liouville-Green)

Engine:** `engine_cache.py` (50-digit cache of `build` from E70), dps=40,
DH falsifier on all three. **Goal:** attack 2.3.F-Loc with **intrinsic and robust** tools
that do NOT repeat the 8 dead shortcuts (R3–R8). λ ∈ {7,9,11,13,15(,17,19,21)}.

## N1 — Intrinsic Jacobi via exact Lanczos on the Weil `A` (`E79_lanczos_intrinsic.py`)

**POSITIVE RESULT (real methodological gain).** Exact Lanczos (mpmath, full
reorthogonalization) on the Weil matrix `A`, starting from a cyclic vector of **both parities**:

- **Reproduces the ladder EXACTLY in the `e^{−cL}` residual**: at λ=9, the spectrum of the Lanczos
  tridiagonal matrix = `[1, 3.998, 9.026, 16.056, 25.22, 36.386]` ≈ `(k+1)²`, with `rep_err = 0` (exact).
  **This DEFEATS the E76 obstacle**: E76 injected an external sine basis (error O(1), 19 orders
  above the residual) and broke; Lanczos is an *internal* orthogonal reduction → stable, reaches
  the residual without an external basis.
- **Parity subsector:** an even starting vector excites only the even sector → ladder
  `1, 9.05, 25.4, 50.7 ≈ (2k+1)²` (consistent, confirms the structure).
- **New structural insight (mechanism, measured):** the intrinsic Jacobi has coefficients
  `αₙ, βₙ = O(1)`, **bounded** and **parity-alternating** (`α≈[0.79, 3.69, 0.85, 3.68, 0.88,…]`).
  They do NOT grow like Connes's **bare** prolate Jacobi (Prop 3.5, `bₙ ≈ 2πλ²·8n`, linear
  growth `~n¹`). **The Weil + Doob balance ELIMINATES the `2πλ²` scale**, leaving a Jacobi
  operator with bounded coefficients whose low spectrum is the `(k+1)²` ladder. Reframe of route A: prove
  that the **bounded** intrinsic Jacobi operator → Dirichlet `(k+1)²` asymptotically.
- **DH falsifier:** ratios `[1, 0.67, 0.62, 0.54, …]` (garbage), `αₙ` with flipped sign. Fails cleanly.

## N2 — Spectral zeta / heat trace (`E80_spectral_zeta.py`)

**POSITIVE RESULT (robustness) + NEGATIVE (no clean rate law).** `μ_k = eps_k/eps_0`:

| λ | μ (target 1,4,9,16,25) | ladder_err | Z(1) err | Θ(0.7) err |
|---|---|---|---|---|
| 7  | 1, 4.07, 9.05, 16.40, 25.40 | 0.025 | 0.0048 | 0.0053 |
| 9  | 1, 4.00, 9.03, 16.06, 25.22 | 0.009 | 0.0005 | 0.0001 |
| 11 | 1, 3.90, 9.02, 15.65, 25.14 | 0.024 | 0.0048 | 0.0075 |
| 13 | 1, 4.04, 9.01, 16.20, 25.12 | 0.013 | 0.0025 | 0.0031 |
| 15 | 1, 3.93, 9.01, 15.76, 25.08 | 0.017 | 0.0033 | 0.0051 |

- **The traces reproduce the Dirichlet invariants to <0.5%** (aggregated), much more robust than
  any individual `e^{−cL}` eigenvalue. Confirms 2.3.F-Loc at the level of a spectral invariant.
- **CATASTROPHIC DH falsifier** (clean instrument): `ladder_err=0.98`, `Z(s) err = 4.3, 10.8, 19.9`.
- **BUT the λ-dependence is OSCILLATORY, not monotone**: `μ_1` bounces around 4
  (4.07→4.00→3.90→4.04→3.93), `μ_3` around 16. The Richardson rates come out **inconsistent**
  across observables (ladder_err `p=+0.80` converges, but `Z(s=2) p=−2.85`). ⟹ **there is NO clean
  power law**: the residual relative to `(k+1)²` **fluctuates arithmetically in λ** (an echo of the
  prime oscillation in the band `L=2logλ`). The ladder is exact **on average**; the convergence is
  Cesàro/averaged, not pointwise-smooth.

### Envelope at high λ (`E82_envelope.py`, λ up to 21)

| λ | L | μ_1 | μ_3 | \|dev μ1\| | \|dev μ3\| | ladder_err |
|---|---|---|---|---|---|---|
| 7  | 3.89 | 4.070 | 16.40 | 0.070 | 0.404 | 0.025 |
| 9  | 4.39 | 3.998 | 16.06 | 0.002 | 0.056 | 0.009 |
| 11 | 4.80 | 3.904 | 15.65 | 0.096 | 0.346 | 0.024 |
| 13 | 5.13 | 4.041 | 16.20 | 0.041 | 0.202 | 0.013 |
| 15 | 5.42 | 3.934 | 15.76 | 0.066 | 0.240 | 0.017 |
| 17 | 5.67 | 4.034 | 16.16 | 0.034 | 0.160 | 0.010 |
| 19 | 5.89 | 3.978 | 15.93 | 0.022 | 0.071 | 0.006 |
| 21 | 6.09 | 3.928 | 15.73 | 0.072 | 0.271 | 0.018 |

**The envelope does NOT decay cleanly:** the deviation from `(k+1)²` **oscillates in a roughly stable
band** (ladder_err bounces 0.025, 0.009, 0.024, 0.013, 0.017, 0.010, 0.006, **0.018**). The "decay"
fits (`p≈1.45, 0.85`) are dominated by the low λ values and a lucky λ=19; λ=21 goes back to 0.018.
Conclusion: **exact ladder ON AVERAGE + irreducible ~1–2% arithmetic fluctuation that does not
vanish at reachable λ.** That is the obstacle, precisely.

## N3 — Carrier `θ(y)` via Liouville–Green + 1/L rate (`E81_liouville_green.py`)

**NEGATIVE RESULT (no derivable law).** Two approaches: (a) `cosθ=(f_1/u_0)/2` from measured
modes; (b) Liouville–Green `θ=∫√(w/C)dy` with measured `C`.

- Affinity residual **small** (modes 0.5–1%, LG ~2.3–2.6%) but **flat**: the LG rate in `1/L`
  comes out `≈ 0` (does not converge cleanly); the mode rate is noisy (`p≈0.55` dominated by one point).
- **DH falsifier:** modes 17.4%, LG 6.0% (much worse). Fails.
- Verdict: consistent with the N2 oscillation — the affinity is good (~2%) but its trend with λ
  is dominated by the arithmetic fluctuation, not by an extractable `1/L^p` law.

## R9 consolidated verdict

**The three new tools ARE real progress, but do NOT close 2.3.F:**

1. **Solid gain (N1):** Lanczos gives a **STABLE intrinsic tridiagonalization** that reaches the
   `(k+1)²` ladder in the `e^{−cL}` residual (where E76 failed) — a new usable tool.
2. **New structural insight (N1):** in the intrinsic frame the operator is a **Jacobi operator with
   bounded O(1) coefficients** (the Weil balance erases the `2πλ²` scale of the bare prolate).
   Clean reframe of route A: "bounded intrinsic Jacobi → Dirichlet `(k+1)²`".
3. **Robust triple confirmation of 2.3.F-Loc** (Lanczos, traces, carrier) + **clean DH falsification
   on all three** (faithful instrument).
4. **Sharpened obstruction (N2/N3):** the `(k+1)²` residual **oscillates arithmetically in λ** (there
   is no power law `1/L^p`); the convergence to the ladder is **on average**, not pointwise. That is
   why no rate fit closes it: the remaining content is an **averaged asymptotic** (Cesàro) of the
   prolate/Sonin deformation = exactly the Connes/Consani machinery.

**Status of 2.3.F unchanged at the THEOREM level, but with a better map:** it remains REDUCED to
2.3.F-Loc; now with (i) a stable computational route (Lanczos), (ii) a sharper statement of the crux
(bounded Jacobi → Dirichlet, on average over λ), and (iii) confirmation that the obstruction is the
**arithmetic fluctuation** of the residual, not a missing shortcut.
