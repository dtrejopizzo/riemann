# R186.021 — The curve ρ*(T) in [½log2, ½log3] and the minimal-Sonin-mass direction s₀(T)

Scripts (scratchpad, not versioned): `r021.py` (pairs (C, Son) for T ∈ {½log2, 0.35, 0.40, 0.45, 0.50, ½log3}, M = 20/24/28,
grids ε_S memo `g1_S_5_8_1_10` and refined `g1_RS_3_8_6_10`, archimedean `g1_A_5_8_1_0`), `r021b.py` (overlaps, profile).
Framework: λ = 1, 𝒫_T (support [−T,T], primitive constraint cp), L²(h) metric, E_S = Son_S − C (D3), Son_S ≻ 0 over the whole range
(min ≥ 0.0145), so the generalized problem C u = ρ Son_S u is solved directly (without regularizing).

## Status

| Item | Label |
|---|---|
| Curve ρ*(T) (S = {∞,2}) and ρ*_∞(T); stable in M (20/24/28) and in the ε grid | NUMERICAL |
| Mechanism of the rise of ρ*: collapse of Son_S(u_T) (0.38 → 0.018), C(u_T) ≈ 0.014–0.026 nearly constant | NUMERICAL |
| s₀(T) ≈ s₀^∞(T) (minimal **archimedean** Sonin-mass direction): overlap ≥ 0.989 at every T | NUMERICAL |
| s₀ ≠ CC's ζ (overlap 0.03 at ½log2) | NUMERICAL — the hypothesis "s₀ = continuation of ζ" is **NO-GO** |
| λ_min(Son_S|𝒫_T) = 1 − λ₂(A_S)² | **NO-GO** (numerical coincidence at a single T; proof below) |
| Conjecture 1D(T): C(s₀(T)) < Son_S(s₀(T)) | NUMERICAL (holds, large margin: ratio ≤ 0.71) but **strictly weaker** than RB(T): 1D ⇏ RB numerically |
| maximizer u_T vs s₀(T): overlap 0.993–0.998 for T ≥ 0.45 | NUMERICAL; but the ratio at s₀ (0.71) ≠ ρ* (0.94); ρ* needs ≥ 5 Son modes |

## 1. The curve ρ*(T) (M = 24; refined RS grid; in parentheses memo grid S and M = 28)

| T | ρ*(T) | C(u_T) | Son_S(u_T) | Son_S(s₀) | C(s₀) | C(s₀)/Son_S(s₀) | ⟨u_T,s₀⟩ | ρ*_∞(T) | min Son_∞ | C_∞(s₀^∞) |
|---|---|---|---|---|---|---|---|---|---|---|
| ½log2 | +0.0010 (−0.0004; 0.0011) | +0.003 | 2.82 | 0.2570 | −0.303 | −1.18 | 0.13 | −0.0004 | 0.183 | −0.369 |
| 0.35 | +0.0026 (−0.0004; 0.0027) | +0.006 | 2.29 | 0.2511 | −0.298 | −1.19 | 0.19 | −0.0004 | 0.175 | −0.368 |
| 0.40 | 0.055 (0.036; 0.055) | +0.021 | 0.374 | 0.1389 | −0.146 | −1.05 | 0.78 | −0.0005 | 0.091 | −0.329 |
| 0.45 | 0.245 (0.241; 0.247) | +0.026 | 0.106 | 0.0635 | −0.034 | −0.53 | 0.957 | −0.0006 | 0.047 | −0.271 |
| 0.50 | 0.644 (0.645; 0.646) | +0.023 | 0.0360 | 0.0294 | +0.0073 | +0.25 | 0.993 | +0.0016 | 0.025 | −0.206 |
| ½log3 | **0.9436** (0.9437; 0.9443) | +0.0167 | 0.0177 | 0.0147 | +0.0104 | +0.71 | 0.998 | +0.084 | 0.0140 | −0.140 |

(M = 20 gives the same values to ≤ 4e-3; the only data sensitive to the ε grid is ρ* for T ≤ 0.40, where ρ* ≈ 0–0.05 anyway.)

**Answer to "how does ρ* rise from ≈0 to 0.94?"** Not by a jump in C: C(u_T) stays in [0.014, 0.026] from T = 0.40 on.
What changes is **Son_S(u_T)**, which drops from O(1) to 0.018, because the maximizer aligns with s₀ and λ_min(Son_S|𝒫_T) drops
(0.257 → 0.0147, monotone: 𝒫_T is nested in T, so λ_min is non-increasing — PROVED, trivial). The "entry" of the prime 2
(2T > log2) shows up in C(u_T) > 0 starting at T ≈ 0.35 (small, ≈ 0.003–0.006: the log peak at a = log2 sits at the edge of
the support of c_h), and grows to O(0.02) at T = 0.40; from there it is constant and the ratio rises only through the denominator.

**Comparison with the archimedean case.** ρ*_∞ ≤ 0.002 up to T = 0.50 and ρ*_∞(½log3) = 0.084. The collapse of the Sonin mass is
**the same** in both cases (min Son_∞ 0.0140 vs min Son_S 0.0147 at ½log3), and in the same direction (§2). The difference is
entirely C in that direction: C_∞(s₀) = −0.140 (the archimedean remainder **adds** mass to E_∞ at s₀), C_S(s₀) = +0.0104.
Difference ΔC(s₀) = C_S − C_∞ ≈ +0.150 = contribution of κ_S (the semilocal part of ε_S, which includes the log peak at ρ = 2).

## 2. Nature of s₀(T)

- **s₀(T) is archimedean:** |⟨s₀^S, s₀^∞⟩| = 0.998 (½log2), 0.998 (0.35), 0.994 (0.40), 0.989 (0.45), 0.994 (0.50), 0.998 (½log3).
 The minimal-Sonin-mass direction in 𝒫_T is set by the geometry (window + cp constraint + W_∞), not by the prime 2.
- **Profile (NUMERICAL, ½log3, M = 24, h normalized in L²):** even (even fraction 1.000), two sign changes at |y| ≈ 0.22,
 maximum at y = 0 (h(0) = 1.70), minima h(±0.385) ≈ −1.01, double zeros at ±T (basis (1−u²)²). Mass in |y| < T/2: 65%.
 It is the first even mode compatible with cp (∫ξe^{x/2} = 0) — a "cosine with negative shoulders". Same qualitative type at every T.
- **s₀ ≠ CC's ζ.** At ½log2, ζ (the top eigenvector of unconstrained C_∞, L²(h), max 0.0844, reproducing R186.101) has
 ⟨ζ, s₀⟩ = 0.03 (and |cp·ζ|/|cp| = 0.42: ζ is not in 𝒫_T). The hypothesis "s₀ is the T-continuation of CC's dangerous
 direction" is **NO-GO**. CC's direction is the one maximizing C_∞; s₀ is the one minimizing Son: distinct objects.
- Hypothesis "s₀ = semilocal analogue of the top prolate function" — not testable as such (‖Pϑ(g)‖_HS = ∞, see R186.101 §2.1); what
 is actually measured is that s₀ is nearly the same vector for Son_S and Son_∞: if it is a prolate function, it is the archimedean one.
- h* (certified minimizer of E_S): ⟨s₀,h*⟩ = 0.99 (T ≤ 0.35), 0.96 (0.40), 0.98–0.998 (≥ 0.45); ⟨u_T,h*⟩ = 1.0000 for T ≥ 0.50.

## 3. Is λ_min(Son_S|𝒫_T) = 1 − λ₂(A_S)²? — **NO**

Values: 1 − λ₂² = 1 − 0.992727² = 0.014493 (λ₂ refined from R186.101). λ_min(Son_S|𝒫_{½log3}) = 0.01469 / 0.01459 / 0.01451
(M = 20/24/28, memo grid), 0.01477 / 0.01467 / 0.01459 (refined): matches to ~1% at T = ½log3. But:

1. **(PROVED) It cannot be an identity in T.** 𝒫_T ⊂ 𝒫_{T′} for T < T′ (same cp), so T ↦ λ_min(Son_S|𝒫_T) is non-
 increasing, and the measured values are strictly decreasing (0.257, 0.251, 0.139, 0.063, 0.029, 0.0147). A spectral constant of
 A_S (independent of T) can only match it at one T. Moreover λ_min keeps drifting in M (−8e-5 per step of 4): its limit
 as M → ∞ is not fixed to 1e-4.
2. **(NUMERICAL) Fails in the archimedean case:** λ₂(A_∞) = −0.97948 (CC, D1) ⇒ 1 − λ₂² = 0.0406, versus λ_min(Son_∞|𝒫_{½log3})
 = 0.0140; and since s₀^S ≈ s₀^∞ and λ_min is nearly the same in both, the quantity 0.0146 is archimedean and does not see λ₂(A_S).
3. **(Structural)** In the Halmos decomposition Π_S = Q₁ − Σ|ζ_n⟩⟨ζ_n| the ζ_n are **outside** ran Π_S: an orbit
 aligned with ζ₂ gives Son = 0, not 1 − λ₂². The weights λ_n² appear in Q₁Q₂Q₁, not in Π_S; and Son_S(h) = ‖Π_Sϑ(g)‖²_HS is a
 sum over the scaling orbit, not a Rayleigh quotient of a single vector of the u-model. There is no dictionary D1 that
 turns λ_min of the window into sin²θ₂.

**Verdict: the equality 0.0146 ≈ 0.01449 is a crossing coincidence at T = ½log3. NO-GO as a structure.**

## 4. Conjecture 1D(T) and its relation to RB(T)

**Conjecture 1D(T).** C(s₀(T)) < Son_S(s₀(T)) = λ_min(Son_S|𝒫_T).
Numerical: C/Son at s₀ = −1.18, −1.19, −1.05, −0.53, +0.25, +0.71: 1D holds with margin (≥ 29%), and is trivial (C(s₀) < 0) for
T ≤ 0.45.

**1D(T) is not equivalent to RB(T)** (ρ*(T) < 1): at ½log3, ρ* = 0.944 vs 0.71 at s₀, even with ⟨u,s₀⟩ = 0.998.
Subspace test (NUMERICAL, M = 24, RS grid): ρ* restricted to span{s₀,…,s_{k−1}} (lower eigenvectors of Son_S):
k = 2 → 0.712, k = 3 → 0.738, k = 5 → 0.908, full → 0.944. The cross term C(s₀,s₁) = −7e-8 (s₁ is odd: parity), so s₁
does not help; the rise comes from higher even modes (s₂: Son = 0.42) with cross terms C(s₀,s_j) of order ‖C‖ = 0.67 against
Son(s₀) = 0.0147: a 0.4% mixing suffices. So the problem **is not** one of a single direction or of a 2×2 block: it is the relative
bound on C over a subspace of dimension ≥ 5 (weighted by 1/Son). **1D(T) is necessary, not sufficient; Conjecture 1D: NUMERICAL
(holds), but NO-GO as a reduction of RB.** The honest reformulation remains ρ*(T) < 1, with the structural fact from §2:
the minimal denominator is archimedean.

## 5. Exact inequality for an analytic proof on [½log2, ½log3]

Since s₀ is (numerically) archimedean and Son_S ≈ Son_∞ on the small-Son subspace, the natural decomposition is

 E_S(h) = E_∞(h) − [C_S(h) − C_∞(h)] + [Son_S(h) − Son_∞(h)], and at s₀: E_∞(s₀) = Son_∞ − C_∞ ≈ 0.014 + 0.140 = 0.154,

so positivity in the dangerous direction is equivalent to the **semilocal increase of the remainder on the low-Sonin-mass
subspace** not exceeding E_∞ there: ΔC = C_S − C_∞ (≈ 0.150 at s₀) versus E_∞(s₀) + ΔSon ≈ 0.154. That is, at ½log3 the
margin is 3%: the contribution of the prime 2 (κ_S: log peak at ρ = 2 plus the shift in the spectral data) consumes almost exactly the
archimedean surplus. Inequality to be proved (OPEN):

 sup_{h ∈ 𝒫_T, ‖h‖=1} [ (C_S − C_∞)(h) − (Son_S − Son_∞)(h) ] / E_∞(h) < 1, T ∈ [½log2, ½log3],

with E_∞ ≻ 0 on 𝒫_T (up to 0.596, CITED/record). This is the positivity of E_S rewritten as relative domination of the prime-2
term by the archimedean form — a **reformulation** (equivalent to E_S ≻ 0), useful only if ΔC and ΔSon are bounded
separately: ΔC from ε_S − ε_∞ (requires (CV_S), OPEN), ΔSon from Halmos/Thm C′ (exact for the comb; κ_S OPEN).

## Audit notes

1. ε_S is not converged away from the peak (R186.101 MAJOR-1); the C numbers agree to ≤ 2% between grids except ρ* for T ≤ 0.40
 (≈0.00–0.05, sensitive: 0.036 vs 0.055). The conclusion "ρ* rises through the denominator" does not depend on this.
2. s₀ and λ_min do not depend on ε_S except via Son = E + C; they do depend on ε through C(s₀) — and Son_S(s₀) changes by 0.5% between grids.
3. The NO-GO for 1 − λ₂² rests on monotonicity in T (PROVED, trivial) + the measured drift; it does not require fine convergence.
4. "s₀ ≈ s₀^∞" uses Son_∞ = E_∞ + C_∞ with the same machinery (archimedean D3, validated against CC in R186.101).
5. The inequality in §5 is a reformulation of E_S ≻ 0; it is not claimed as a reduction.

## Note (R186_102)

* No fatal issues; reproduced (ρ* = 0.9408/0.9447 with M=16/32). M1: ΔC and E_∞ at the same s₀: 0.134–0.136 vs 0.139–0.141, ΔSon ≈ −0.0008. M2: real margin sup(E_∞−E_S)/E_∞ = 0.9936 (0.65%, decreasing with M); §5 is identically E_S ≻ 0. m1: monotonicity PROVED only non-increasing in the continuum; "strict" is NUMERICAL. Labels: ρ*(T), s₀ archimedean, 1D ⇏ RB: NUMERICAL.
