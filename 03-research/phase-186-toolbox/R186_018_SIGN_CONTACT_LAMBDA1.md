# R186.018 — Sign contact at λ = 1 (S = {∞,2}): converged A_S, ε_S^{(1)}, single-direction test

Scripts (scratchpad, not versioned): `eg.py` (Galerkin in basis f = E g), `epsg.py` (ε via resolvent), `grid.py`, `win18.py`.

## Status

| # | Statement | Label |
|---|---|---|
| A1 | A_S (λ=1, S={∞,2}) converged in basis f = E g: 1−λ₁ = 2.617e-6, λ₂ = −0.992626 (6 digits, two bases) | NUMERICAL |
| A2 | Cause of L1 (R186.017): log(1/x) singularity at 0 not representable in the Legendre basis in f; resolved, L1 closed | NUMERICAL + ARGUED |
| V | ε pipeline validated: ε_∞′(1⁺) = 22.99650 (CC 22.9965) | NUMERICAL |
| C0 | ½log2 control: −C_ε (∞ and S) has n₋ = 0 in 𝒫_T: trivial dominance, no contact | NUMERICAL |
| C1 | ½log3, λ=1: n₋(−C_{ε_S}) = **2** (−0.0824, −0.0397); at v₁: C = 0.0824, E_S = 0.130, Son_S = 0.212 | NUMERICAL |
| C2 | min E_S = 9.89e-4 (reproduces the certified gap of R186.017); at h*: Son_S = 0.0174, C = 0.0164 | NUMERICAL |
| H | Independent Son_S via Π_S (Halmos) | OPEN (not done) |

**Verdict.** (i) Pipeline validated against CC (ε′(1⁺)); the ½log2 control is trivial (remainder with no negative direction), it does not directly reproduce CC's constants K_I from (134)–(137) — that comparison was not done. (ii) At ½log3, λ=1: the remainder has two negative directions; Son_S dominates them with margin (0.212 vs 0.082; 0.304 vs 0.040). (iii) **Sign contact: NOT observed.** The certified gap lives at h*, orthogonal (to 1e-3) to v₁, where Son_S(h*) = 0.0174 and the remainder 0.0164 nearly cancel: E_S/Son_S = 5.7%. Positivity at ½log3 is cancellation, not dominance in the remainder's negative direction.

## 1. Converged A_S at λ = 1 (NUMERICAL)

Key: basis f_i = E g_i, E = Σ_k D_{2^k}, g_i piecewise Legendre on a dyadic mesh of (0,1]. Since the top
eigenvector has a log(1/x) singularity at 0 (kernel ~ log₂(1/(xy))), in the f basis E absorbs that singularity
and g = E⁻¹f is regular. Matrix: ⟨Eg_i,F_SEg_j⟩ = Σ_{d∈ℤ} 2·2^{−max(0,−d)} Γ_d, Γ_d = ∫∫g_ig_j 2cos(2π2^dxy);
Γ_d ~ c·2^{−d} ⇒ exact geometric closure at first order; convergence in D as ~ 4^{−D}.
(The Legendre basis in f from R186.017 converged only as 2^{−K}: that is the cause of the "non-convergence" L1.)

| basis (lev,p,sub), n | 1 − λ₁ | λ₂ | λ₃ |
|---|---|---|---|
| (3,6,1) 24, D=12 | 2.674e-6 | −0.9926096 | 0.617072 |
| (3,8,1) 32, D=14 | 2.6175e-6 | −0.99262607 | 0.6174991 |
| (5,8,1) 48, D=14 | 2.6172e-6 | −0.99262608 | 0.6174991 |
| (5,10,2) 120, D=14 (D not conv.) | 2.586e-6 | −0.992713 | 0.619738 |

λ₁, λ₂ stable to ≥ 6 digits in bases without subdivision (λ₃ depends on resolution to 2e-3: OPEN for
non-extreme eigenvalues). ‖A_S‖ < 1 (R186.015 PROVED) consistent: 1 − λ₁ ≈ 2.62e-6, 1 − |λ₂| ≈ 7.37e-3.
Archimedean comparison λ = 1: 1 − λ₀(A_∞) = 2.862e-5.

## 2. Validation of the ε pipeline against CC (NUMERICAL)

Same code (`epsg.py`, ∞ mode): ε_∞′(1⁺) = 22.996504 (CC Lemma 5.4: 22.9965 ✓); ε_∞(2) = 1.0998043
(= R186.016 grid to 1e-7). δ(1) = 2.2375 already validated in R186.017 D1.

## 3. ε_S^{(1)} (NUMERICAL)

Resolvent form ε(ρ) = √ρ∫_{1/ρ}^1 f(t)ᵀ A(1−A²)⁻¹ (F_Sf)(ρt) dt (generalized with Gram), F_Sf(v) = Σ_k Fg(2^kv).
Convergence under the outer truncation KE: ε_S(1.6) = 1.084990 / 1.084948 / 1.084946 (KE 8/10/12). Bases (3,8,1) vs (5,8,1): ≤ 1e-5;
basis (3,6,1) differs by ~2% (λ₃ unresolved): declared basis uncertainty ~1e-2 relative in ε, 2e-7 in the window C between the two good bases.
Values: ε_S(1.2) = 2.917, (1.5) 1.463, (1.9) 3.090, (1.99) 3.598, (2.01) 3.627, (2.5) 0.525, (3.0) 0.625; ε_∞: 2.954, 1.549, 1.056, 1.100, 1.099, 0.648, 0.710. κ_S = ε_S − ε_∞ with a peak at ρ = 2 (≈ +2.5). The coefficient β₁ = 0.510 was not fitted (OPEN).

## 4. Single-direction test (𝒫_T, L²(h) metric, primitive constraint cp; M = 16/20/24)

Son_S = E_S + C, C(h) = ∫c_hε_S^{(1)} (D3 at λ=1).

| T | M | form | n₋(−C) | eigenvalues of −C | C(v₁) | E(v₁) | Son(v₁) | min E | min Son |
|---|---|---|---|---|---|---|---|---|---|
| ½log2 | 24 | ∞ | 0 | — | — | — | — | 0.5487 | 0.1831 |
| ½log2 | 24 | S | 0 | — | — | — | — | 0.5487 | 0.2589 |
| ½log3 | 16 | ∞ | 1 | −0.0325 | 0.0325 | 0.674 | 0.707 | 0.0864 | 0.0142 |
| ½log3 | 24 | ∞ | 1 | −0.0345 | 0.0345 | 0.710 | 0.744 | 0.0845 | 0.0140 |
| ½log3 | 16 | S | 2 | −0.0815, −0.0390 | 0.0815 | 0.1270 | 0.2085 | 1.047e-3 | 0.0148 |
| ½log3 | 20 | S | 2 | −0.0820, −0.0395 | 0.0820 | 0.1282 | 0.2102 | 1.018e-3 | 0.0147 |
| ½log3 | 24 | S | 2 | −0.0824, −0.0397 | 0.0824 | 0.1297 | 0.2120 | 9.89e-4 | 0.0146 |

M = 24, S, ½log3: v₂: C = 0.0397, E = 0.264, Son = 0.304. Minimizer h* of E_S: E = 9.89e-4, C = 0.0164, Son = 0.0174 (⟨h*,v₁⟩ ≈ 0).
With both constraints (cp, cl): n₋ = 2 the same, min E = 0.036, min Son = 0.072.
The archimedean case reproduces R186.099 (n₋ = 1, −0.032…−0.034).

## Audit notes

1. The identity Son_S = E_S + C holds by construction (D3); the test is not independent of (83)/(84)_S. Verification via Π_S (Halmos) **was not done**: OPEN.
2. The ½log2 control does not compare against CC's λ_max(K_I) ≈ 1.0516 (a different normalization/form): the claim "pipeline validated" rests only on ε′(1⁺) and ε(2).
3. ε_S depends on the basis by ~2% in the smallest basis; the two bases used agree to 1e-5. 1/(1−λ₁²) ≈ 1.9e5: large amplification; λ₁ error at 1e-8 relative.
4. Geometric closure in D (Γ_d ~ c2^{−d}) is ARGUED, observed (4^{−D}).
5. No sign claim about E_S beyond the numbers; "dominance at v₁" implies nothing about h*.

## Note (R186_101)

* FATAL-1: apparent convergence of A_S (only p mattered; with p=10–16 and refinement at x=1 and 2^{−m}: 1−λ₁ → 2.592e-6, λ₂ → −0.992727, λ₃ → 0.6201). FATAL-2: n₋(−C) not robust (2 → 6 at ½log3; 0 → 1 at ½log2) due to the log singularity at ρ=2: rows C0/C1 withdrawn, n₋ OPEN. MAJOR: the peak at ρ=2 is a resolution ceiling (3.6 → 4.62), compatible with β₁=0.510; ε_S not converged away from the peak. What stands: min E_S = 9.89e-4, C(h*) = 0.0164, Son_S(h*) = 0.0174, "no contact". Agreement with CC at ½log2: λ_max 1.0504/1.05158, ⟨ξ₀|ζ⟩ 0.9488/0.94865, λ₂ 0.684/0.6865.
* Part 2: two-regime conjecture FALSE (C(s₀) = +0.0103 > 0). Invariant: ρ*(T) = sup_{𝒫_T} C/Son_S; ½log2: ≈0; ½log3: 0.9437 (maximizer = h*; stable to 1e-4). Positivity ⟺ ρ* < 1. RB(T): C ≤ (1−η)Son_S, CONJECTURE (reformulation modulo separate bounds). OPEN: is the maximizer of C/Son_S = the minimal-Sonin-mass direction s₀ as M→∞ (overlap 0.996)?
