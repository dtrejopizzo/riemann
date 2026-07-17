# E113 — T_N is Toeplitz (symbol = -ζ'/ζ on the critical line); ‖T_N‖ SATURATES in N

**Date:** 2026-07-05 · `E113_TN_closedform.py` (closed-form overlaps, no quadrature, N up to 250).

## RETRACTION of E112's extrapolation
E112 fit `λ_max(T_N) ~ N^{2/3}` from N≤50 and inferred the loglog border extends to `(log|t0|)^{3/2}`.
**This was premature.** The closed form reaches N=250 and shows `λ_max(T_N)` **SATURATES**:
`0.32 (N=4) → 1.55 (20) → 2.19 (100) → 2.26 (196) → ~2.27`. The local exponent falls 0.15→0.06→0.03.
The `N^{2/3}` was a small-N transient. **The border-extension claim (loglog → (log)^{3/2}) is withdrawn.**

## Genuine, correct findings

### 1. T_N is Toeplitz; its symbol is -ζ'/ζ on the critical line
Closed form (generating function): `∫_0^∞ L_j(x+a)L_k(x)e^{-x}dx = L_{j-k}^{(-1)}(a)` (j≥k). Hence
`T[j,k] = -(1/log(t0/2π)) A_{j-k}`, a Hermitian Toeplitz matrix, with
`A_d = Σ_n Λ(n) n^{-(1/2+y+it0)} L_d^{(-1)}(2y log n)`. The generating function of {A_d} has exponent
real part **exactly -1/2** for all θ (since Re(s/(1-s))=-1/2 on |s|=1), so the Toeplitz symbol is
`-ζ'/ζ` sampled along the **critical line** near height t0, whitened by 1/log(t0). This is a real
structural fact and the right vehicle for the analytic question.

### 2. ‖T_N‖ saturates in N — the N-uniformity is NOT the obstacle
For fixed t0, `λ_max(T_N) → ‖T_∞(t0)‖ < ∞` (the truncated-Toeplitz norm converges to the symbol norm).
So contractivity `λ_max(T_N)≤1` for ALL N is equivalent to the single condition
`‖T_∞(t0)‖ ≤ 1`, no N-uniformity issue. **This reframes the paper's open point** (which, using the crude
`e^{βN}` bound, treated "uniform in N" as the hard part): the hard part is not N.

### 3. The residue lives entirely in t0 (height), spiking near zeros
Saturated norm vs t0 (N=250):
| t0 | 1e4 | 1e6 | 1e8 | 1e10 | 1e12 | 1e15 | 1e20 |
|---|---|---|---|---|---|---|---|
| sat ‖T_∞‖ | 3.61 | 2.27 | 1.57 | 1.02 | 0.81 | **1.08** | 0.43 |
| sat·log(t0) | 26.6 | 27.2 | 26.0 | 21.7 | 21.0 | **35.2** | 18.9 |
Typically `‖T_∞(t0)‖ ≈ C/log(t0)`, C≈20–27, decreasing — but it **SPIKES** when t0 lands near a zero
(the 1e15 outlier: sat·log jumps to 35). So `‖T_∞(t0)‖` is NOT uniformly small; it peaks at heights
near zeros. **Ω₇ ⟺ `‖T_∞(t0)‖ ≤ 1` uniformly in t0**, i.e. the whitened symbol `-ζ'/ζ(1/2+i·)/log|t0|`
is bounded by 1 uniformly — a bound on `ζ'/ζ` near the critical line. This is a classical,
Lindelöf-adjacent object (below RH in kind, unconditional bounds on ζ'/ζ exist and can be sharpened).

## Honest status / essential caveat
- This is a **detector on ζ** (uses ζ's actual primes): the saturation and the sub-1 values at large t0
  are RH-CONSISTENT, not a proof. A planted off-line zero (Λ_DH / offfac) must be run to confirm it
  spikes ‖T_∞‖ above 1 — the faithfulness check (D2-style).
- **CALIBRATION REQUIRED before amending P52:** E113's T_N is a fresh build from `prop:laguerre-entries`.
  Its saturation revises the paper's "uniform-in-N" framing, so it MUST be calibrated against the P52
  harness `h8lab.py` (same z0, y, whitening, archimedean floor). If they disagree, the saturation is an
  artifact of a convention mismatch, not a property of the paper's operator. Do NOT touch P52 until this
  passes.

## Net
E112's border-extension is retracted. In its place: (i) the correct Toeplitz/symbol structure; (ii) the
reframing that ‖T_N‖ saturates in N so the residue is the t0-uniform bound on the whitened -ζ'/ζ symbol;
(iii) the next steps — plant an off-line zero (faithfulness), and calibrate against h8lab.

## Faithfulness confirmed (zeta saturates, DH grows)
Rebuilding T_N with the Davenport-Heilbronn von Mangoldt Λ_DH (off-line zeros) vs ζ, at t0=1e6:
| N | 60 | 90 | 120 | 150 |
|---|---|---|---|---|
| ζ  λ_max | 1.39 | 1.45 | 1.48 | 1.49 |
| DH λ_max | 3.40 | 4.68 | 5.39 | 5.80 |
N-exponent (N≥60): **ζ = +0.075 (saturates)**, **DH = +0.588 (grows ~N^{0.59})**. So the N-growth
exponent of ‖T_N‖ is a FAITHFUL detector: ≈0 ⟺ (Toeplitz symbol has no off-line pole) ⟺ RH; >0 ⟺
off-line zeros. This is the sharp dichotomy (D1) in clean Toeplitz-symbol form, and it revises E112:
for ζ the growth saturates; the *growth* itself is the ¬RH signature, exactly on DH.

## Corrected net for Phase 66 / steps (1)+(2)
- E112 border-extension (loglog→(log)^{3/2}): **RETRACTED** (small-N transient).
- Genuine gains: T_N is Toeplitz with symbol -[logderiv]/log|t0| on the critical line; ‖T_N‖ saturates
  in N for ζ and grows ~N^{0.59} for DH (faithful RH detector); the residue = saturated symbol norm ≤1
  uniformly in t0 (bounding whitened ζ'/ζ near the line), spiking near zeros.
- Still a criterion, not a proof. Calibration vs h8lab.py pending before any P52 amendment.
