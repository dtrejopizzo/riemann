# R186_040 — The head block of the bundle (Neg_T, Pos_T)|𝒫_T: what its directions are, what decides 1 − β_j, and the falsifier at T = 0.9, 1.0 in multiple precision

Phase 186, round 19. Redirection received mid-round (audit R186_112): verify the vanishing at zeros, decide whether the "leakage" has a part that does not go through the zeros, run the falsifier at T = 1 with mpmath, honest label.
Sources: R186_039 (Lemma 2.1, Lemma H, §2.4), R186_112 (MAJOR-1/2/3), R186_034 (Thm 2.1–2.2), R186_024/104 (E_k, piecewise Tate), Paper 47 (prop:band, prop:negtrace, lem:roughEF, lem:mbounds, thm:Z), Zhu 2608.24827v2 local text (§9 l. 984–1010: T* = 2πe^{2L} is the height where the zero density (1/2π)log(t/2π) equals the Jensen budget L/π; N(T*) = count of zeros of ζ up to T*; §14.2 "low-zero sampling operator").
Scripts (standalone, in the folder): `r040_head.py [M=40] [M_big=60] [*.npz]` (double precision: bundle, head, decompositions, prolates, piecewise Tate, vanishing at zeros; 30 s + ~1 min per window for the vanishing) and `r040_head_mp.py T M dps [out.npz]` (mpmath, dps 40; T = 1, M = 70: ~25 min). Zeros: `zeros150.npy` (first 150 γ, mpmath zetazero, dps 20; CITED real). Output of the mp runs copied into `r040_mp_outputs.txt`.

## 0. Verdict

1. **The head directions vanish at û at the low zeros (CONFIRMED, NUMERICAL).** At ½log5, u₁ (1 − β₁ = 1.73·10⁻¹¹) has |û₁(γ_k)|² = 5·10⁻²³, 2·10⁻²¹, 3·10⁻²⁰, 2·10⁻¹⁸ at γ₁…γ₄ ≤ T*; u_j for j ≤ N(T*)+1 interpolates with the level growing by ~10⁴ per step; u₇ (1 − β = 0.75) no longer interpolates. At T = 0.9 (mp): |û₁(γ_k)|² ≤ 2·10⁻²⁵ at the six zeros ≤ T*. R186_112 MAJOR-1 is confirmed: the head block is the near-kernel of the sampling at the low zeros.
2. **But 1 − β_j is NOT the singular value of the low sampling (quantitative correction to R186_112 §1.3).** By lem:roughEF, 𝔞_T(u_j) = Σ_ρ |û_j(γ)|² exactly (PROVED, see §2) and at ½log5: 2Σ_{γ≤T*} = 3.7·10⁻¹⁸ against 𝔞_T(u₁) = 3.86·10⁻¹² — **the zeros ≤ T* contribute 10⁻⁶ of the total**; 91% comes from the zeros γ ∈ (T*, γ₁₅₀ = 319) and the remaining 9% from the tail γ > 319 (estimated by density; closure at 0.5%: 3.53·10⁻¹² + 3.5·10⁻¹³ = 3.88·10⁻¹²). At T = 0.9: 2Σ_{γ≤T*} = 4.8·10⁻²⁵ against 5.75·10⁻¹⁷. **What fixes 1 − β₁ is the mass of |û₁|² at the zeros above T*, not the quality of the interpolation below**: the interpolation is 6–8 orders finer than the margin.
3. **Geometric side: three-term cancellation (NUMERICAL).** 𝔞_T(u₁) = 𝔞_[0,T*] + 𝔞_[T*,τ_last] + 𝔞_far = −3.613·10⁻⁹ + 3.615·10⁻⁹ + 1.52·10⁻¹² (½log5): below T* the form on u₁ is **negative** and a thousand times larger than the total; the strip [T*, τ_last] cancels it to three figures; the trivially positive leakage beyond τ_last (σ > 0) is 40% of the total (15% at T = 0.9). **There is no archimedean part of the leakage that avoids the zeros**: the identity of point 2 has no further terms on 𝒫_T, and the only manifestly positive piece (𝔞_far) is smaller than the error of the cancellation between the other two. Total inheritance (§4).
4. **The "prolate leakage weighted by σ₊" does not exist as a mechanism (NO-GO in the declared class, §3).** The head directions have L_in = spectral mass inside {σ<0} ∈ [0.50, 0.75] (½log5: 0.507, 0.516, 0.602, 0.547, 0.536, 0.599): half inside, half outside; Pos(u_j) and Neg(u_j) are two O(0.2–0.4) numbers equal to 11 digits. No Slepian concentration inequality (leakage ≍ e^{−2c}) describes a 0/0 ratio between O(1) masses. The prolate structure appears only in the **shape** of the directions (exact alternating parity even/odd/even/…, increasing spectral centroid 7.0, 8.3, 9.9, 11.8, 12.7, 14.3 at ½log5, the whole head supported at τ ≲ T*), not in the magnitude.
5. **Falsifier at T = 0.9, 1.0 in multiple precision (NUMERICAL, §5):** count #(1 − β_j < 10⁻³) = **6 and 9** against N(T*) = 6 and 8 (N_Sh = 13.9 and 24.1; negative components 19 and 44; #(1−β<e⁻¹) = 8 and 11; #(1−β<10⁻⁴) = 5 and 8). **Lemma H "K ≤ N(T*) + O(1)" survives; "≈ 14" (Zhu's constant 2π² with steps ≤ 6) is refuted for λ_A.** But the **slope** of Lemma H (π²/log N_Sh = 3.75, 3.10) is **refuted**: the deep steps rise with T (5.38, 5.78, 6.05 at ½log5, 0.9, 1.0 and 5.78, 6.45, 6.97 for the second) while π²/log N_Sh falls. λ_A(1.0) ≤ 4.2·10⁻²³ (M = 70; not converged in M: 5.4·10⁻²⁰, 1.0·10⁻²¹, 1.5·10⁻²² at M = 50, 60, 70), λ_A(0.9) = 5.75·10⁻¹⁷ (M = 56).
6. **Intrinsic reading of T* (ARGUED, §1.3):** m(T*) = log(T*/2π) = 2T = typical deviation of the comb (½Σv_n² = 2Σ_{n<e^{2T}}Λ(n)²/n ~ 4T²), and (1/2π)∫₀^{T*} m = e^{2T}(2T−1) + O(T) = main term of N(T*) of Zhu. Thus "the count tracks N(T*)" can be stated without zeros: **the dimension of the head is the archimedean mass of the symbol below the crossing m = rms(comb)**; why that mass coincides with the number of directions that interpolate zeros is, on 𝒫_T, the content of lem:roughEF (the zeros have density m/2π).

**Contact with the sign: none.** All computed windows have β_max < 1 and λ_A > 0 (T = 0.9, 1.0 in mp confirm what float64 gave as negative noise in R186_112). Nothing in this memo bounds 1 − β_j from below; everything that describes it (zeros, the three geometric terms) inherits it.

## 1. Definition and geometry of the head block

**1.1 Definition.** With β₁ ≥ β₂ ≥ … the eigenvalues of the bundle Neg_T u = β Pos_T u on 𝒫_T (R186_034 Thm 2.1) and u_j its eigenvectors (‖u_j‖ = 1), H_T^δ := span{u_j : 1 − β_j < δ}. Thresholds: δ = 10⁻³ (count K₃), e⁻¹ (K_e). Table (M = 40 up to ½log5; mp M = 56/70 at 0.9/1.0):

| T | N(T*) | #comp | N_Sh | K₄ | K₃ | K₂ | K_e | 1 − β₁ | steps −log(1−β_j) |
|---|---|---|---|---|---|---|---|---|---|
| 0.62 | 2 | 6 | 4.59 | 1 | 1 | 2 | 3 | 7.6e-5 | 4.2, 3.8 |
| log 2 | 3 | 6 | 5.13 | 2 | 2 | 3 | 4 | 4.2e-7 | 4.7, 4.9, 3.1 |
| 0.75 | 3 | 8 | 6.57 | 2 | 3 | 4 | 5 | 3.5e-9 | 4.95, 5.53, 3.94, 3.29 |
| ½log5 | 4 | 8 | 7.05 | 4 | 4 | 5 | 6 | 1.73e-11 | 5.38, 5.78, 4.26, 4.08, 3.40 |
| 0.9 (mp) | 6 | 19 | 13.94 | 5 | 6 | 7 | 8 | 1.71e-16 | 5.78, 6.45, 5.22, 5.47, 4.28, 3.95, 2.93 |
| 1.0 (mp) | 8 | 44 | 24.08 | 8 | 9 | 9 | 11 | ≤1.5e-22 | 6.05, 6.97, 5.42, 5.49, 4.93, 5.33, 4.47, 4.05, 3.43, 2.58 |

K_δ = N(T*) + c with c ∈ {−1, 0, +1} (δ = 10⁻⁴…10⁻²) and N(T*) + 2…3 (δ = e⁻¹), in agreement with R186_112; never N_Sh nor #comp (at T = 1: 24 and 44 against 8–11). **Decision (question 1):** neither "one per negative interval" nor "one per unit of N_Sh"; one per unit of N(T*) + O(1), i.e. §1.3.

**1.2 Directions (NUMERICAL, ½log5; mp and double agree).** (a) Parity: exactly alternating — u₁ even, u₂ odd, u₃ even, u₄ odd, u₅ even, u₆ odd (in every window; at T = 1 the order of the first two, degenerate to 10⁻²², is swapped). PROVED: 𝔞_T, Pos_T, Neg_T commute with the reflection t ↦ −t (even symbol; 𝒫_T is invariant because the reflection swaps the two Tate functionals), so the eigenvectors of the bundle are even or odd. (b) Frequency: peak 6.9, 8.2, 10.4, 17.1, 8.9, 10.5; centroid 7.05, 8.30, 9.93, 11.75, 12.65, 14.3; **the head lives below T* = 31.4** (Pos_far(u_j) < 10⁻⁴ and 𝔞_[T*,τ_last](u_j) = O(10⁻⁹…10⁻⁴) for j ≤ 6); the next two (1 − β = 0.75, 0.78) live in the components of 27–46 and 45–64 and are not balanced (σ₊ ~ log there: s̄₊ = 1.4–1.7). At T = 1 the same: centroids 5.5–21 for K₃, up to 32 for K_e, T* = 46. (c) Mass in the Shannon subspace of S_T (k = ⌈N_Sh⌉ prolates of the negative set, projected onto 𝒫_T): 0.9995, 0.999, 0.995, 0.978, 0.992, 0.974 — the head lives in the Shannon subspace, but spread over several prolates (u₁: 0.07/0.11/0.79 across prolates 2, 4, 5), never in one. (d) Piecewise Tate (R186_024): mass in E₉ = 0.996, 0.994, 0.982, 0.993, 0.943, 0.944; in E₅: 0.945, 0.984, 0.851, 0.748, 0.663, 0.762 — an approximation, not structure (R186_104).

**1.3 T* and N(T*) read off σ_T (ARGUED).** (i) Comb variance: ½Σ_{n<e^{2T}} v_n² = 2Σ Λ(n)²/n = 2·(2T)²/2·(1+o(1)) = 4T²(1+o(1)) (Σ_{n≤x}Λ(n)²/n ~ ½log²x, CITED elementary); rms = 2T. (ii) m(τ) = log(τ/2π) + O(1/τ) (lem:mbounds), hence m(T*) = 2T: **T* is the height where the archimedean level equals the comb's typical deviation**; below it σ_T changes sign with probability O(1), above it only in rare alignments (which explains why the head does not use the far components even though they are 36 of the 44 at T = 1). (iii) (1/2π)∫₀^{T*} m(τ)dτ = (T*/2π)(log(T*/2π) − 1) + O(log T*) = e^{2T}(2T − 1) + O(T): the archimedean mass below T* is Zhu's main term of N(T*) (Riemann–von Mangoldt, CITED). This is the head statement without zeros; its identification with "directions that interpolate zeros" goes through lem:roughEF. Jensen budget T·T*/π = 4Te^{2T} (8.0, 10.9, 14.8) overestimates the count by a factor ≈ 2T/(2T−1); the one that fits is N(T*).

## 2. The quantity that decides: exact decomposition of 1 − β_j

**2.1 Identity (PROVED).** For u ∈ 𝒫_T, a Legendre polynomial of degree < M on I_T: 1 − β(u) := 𝔞_T(u)/Pos_T(u) with 𝔞_T(u) = Pos_T(u) − Neg_T(u) = Σ_ρ Φ_u(ρ)Φ_u(1−ρ) (lem:roughEF: (a) |û|² = O(τ⁻²) and (b) the sum converges absolutely because |Φ_u(s)| ≤ e^{T|Re s − ½|}‖u‖_{L¹} in the strip and Σ_ρ |ρ|⁻² < ∞). For ρ = ½ + iγ real, the term is |û(γ)|². Hence, with u_j an eigenvector: **1 − β_j = Σ_ρ Φ_{u_j}(ρ)Φ_{u_j}(1−ρ) / Pos_T(u_j)**. Note: Pos(u_j) ∈ [0.20, 0.42] across all heads; this is the "O(1) normalization" of R186_112.

**2.2 Partition by symbol (NUMERICAL, ½log5, M = 40; full table in the script).** With Pos = Pos_∞ + Pos_P (symbols m·1_{σ>0}, −comb·1_{σ>0}) and Neg = Neg_∞ + Neg_P (−m·1_{σ<0}, comb·1_{σ<0}), comb := Σv_n cos(τ log n):

| j | 1−β_j | Pos = Pos_∞ + Pos_P | Neg = Neg_∞ + Neg_P | 𝔞_∞ = ∫m|û|²/2π | 𝔞_P = −∫comb|û|²/2π | L_in | s̄₊ | s̄₋ |
|---|---|---|---|---|---|---|---|---|
| 1 | 1.7e-11 | 0.2245 = 0.028 + 0.196 | 0.2245 = −0.034 + 0.258 | +0.062 | −0.062 | 0.507 | 0.455 | 0.443 |
| 2 | 3.8e-9 | 0.1999 = 0.107 + 0.093 | 0.1999 = −0.135 + 0.335 | +0.242 | −0.242 | 0.516 | 0.413 | 0.387 |
| 3 | 1.2e-6 | 0.2765 = 0.118 + 0.159 | 0.2765 = −0.237 + 0.513 | +0.355 | −0.355 | 0.602 | 0.694 | 0.460 |
| 4 | 8.7e-5 | 0.3688 = 0.246 + 0.123 | 0.3688 = −0.261 + 0.629 | +0.506 | −0.506 | 0.547 | 0.814 | 0.674 |
| 5 | 5.1e-3 | 0.3741 = 0.187 + 0.187 | 0.3722 = −0.354 + 0.726 | +0.541 | −0.539 | 0.536 | 0.805 | 0.695 |

Readings. (i) In the first direction **both sides are of primes**: Pos_P = 0.196 out of 0.2245 and Neg_P = 0.258; the archimedean part of the negative set is negative (Neg_∞ < 0: m > 0 on almost all of {σ<0} except (0, 2)) and that of the positive set is small. The Pos/Neg partition by the sign of σ does not separate "archimedean versus primes": the natural partition is 𝔞 = 𝔞_∞ + 𝔞_P with 𝔞_∞(u_j) = −𝔞_P(u_j) to 11 digits, and the cancelled magnitude **grows along the staircase** (0.06, 0.24, 0.36, 0.51, 0.54). (ii) L_in ≈ ½ and s̄₊ ≈ s̄₋: the balanced direction splits its spectral mass equally between {σ<0} and {σ>0} and the weighted averages coincide. There is no small leakage: **the question ("does a pure archimedean term carry the sign, the mass outside the negative set weighted by σ₊?") has a negative answer**: Pos_∞(u₁) = 0.028 is the smallest of the four terms. (iii) Pos_far (τ > τ_last = 109) < 10⁻⁴ across the whole head: the head does not see the region where σ₊ ~ log τ (R186_025 Thm B is irrelevant to it).

**2.3 Partition by height and vanishing at zeros (NUMERICAL; the core of the round).** 𝔞_T(u_j) = 𝔞_[0,T*] + 𝔞_[T*,τ_last] + 𝔞_far (geometric side) = 2Σ_{0<γ≤T*}|û_j(γ)|² + 2Σ_{T*<γ≤γ₁₅₀}|û_j(γ)|² + tail (zero side; tail := (1/π)∫_{γ₁₅₀}^∞ m|û_j|² by density):

| T | j | 1−β_j | 𝔞_T(u_j) | 2Σ_{γ≤T*} | 2Σ_{150 zeros} | tail | 𝔞_[0,T*] | 𝔞_[T*,τ_last] | 𝔞_far | |û_j(γ_k)|², γ_k ≤ T* |
|---|---|---|---|---|---|---|---|---|---|---|
| ½log5 | 1 | 1.7e-11 | 3.858e-12 | 3.7e-18 | 3.529e-12 | 3.5e-13 | −3.613e-9 | +3.615e-9 | 1.52e-12 | 5e-23, 2e-21, 3e-20, 2e-18 |
| ½log5 | 2 | 3.8e-9 | 7.541e-10 | 7.3e-15 | 6.735e-10 | 8.9e-11 | −9.876e-8 | +9.931e-8 | 2.09e-10 | 6e-19, 1e-17, 1e-16, 4e-15 |
| ½log5 | 3 | 1.2e-6 | 3.380e-7 | 3.5e-11 | 3.113e-7 | 2.5e-8 | −7.377e-6 | +7.605e-6 | 1.10e-7 | 6e-15, 3e-13, 9e-13, 2e-11 |
| ½log5 | 4 | 8.7e-5 | 3.206e-5 | 3.2e-8 | 2.887e-5 | 3.6e-6 | −1.591e-4 | +1.819e-4 | 9.24e-6 | 1e-11, 9e-10, 2e-9, 1e-8 |
| ½log5 | 5 | 5.1e-3 | 1.921e-3 | 1.9e-5 | 1.816e-3 | 9.5e-5 | −2.814e-3 | +4.389e-3 | 3.46e-4 | 5e-7, 2e-6, 1e-6, 6e-6 |
| ½log5 | 7 | 0.75 | 0.616 | 0.195 | 0.613 | 2.8e-3 | +0.276 | +0.330 | 9.4e-3 | 4e-4, 4e-3, 2e-2, 8e-2 |
| 0.75 | 1 | 3.5e-9 | 7.679e-10 | 1.4e-15 | 7.061e-10 | 6.1e-11 | −4.618e-8 | +4.677e-8 | 1.84e-10 | 2e-18, 6e-17, 7e-16 |
| log 2 | 1 | 4.7e-7 | 1.042e-7 | 1.2e-11 | 9.651e-8 | 7.4e-9 | −1.927e-6 | +2.005e-6 | 2.60e-8 | 3e-14, 7e-13, 5e-12 |
| 0.9 (mp) | 1 | 1.7e-16 | 5.75e-17 | 4.8e-25 | 4.93e-17 | 8.5e-18 | −2.95e-12 | +2.95e-12 | 8.5e-18 | ≤ 2e-25 (six zeros) |

Check of the identity: Σ_{150} + tail = 𝔞_T(u_j) to 0.5–3% in every row (lem:roughEF with the 150 real CITED zeros; the tail by density is an approximation). Conclusions: (a) **the head directions interpolate the zeros ≤ T* at a level 10⁶–10⁸ times below 1 − β_j**; direction j interpolates worse than j−1 by a factor of ~10⁴ per step, and stops interpolating at j = K_e + 1. (b) **1 − β_j·Pos = Σ_{γ>T*}|û_j(γ)|²(1 + o(1))**: the margin is set by the zeros between T* and ~10T* (where 85–91% of it lives). (c) Geometrically, [0, T*] is negative and a thousand times larger than the total (−3.6·10⁻⁹ against 3.9·10⁻¹²; −2.95·10⁻¹² against 5.7·10⁻¹⁷ at 0.9: five orders), cancelled by the strip [T*, τ_last] to 3–5 digits; 𝔞_far is 40% (½log5), 24% (0.75, log 2) and 15% (0.9) of the total, decreasing in T.

## 3. A leakage lemma? NO-GO in the declared class, and what remains

**3.1 Statement requested.** "For each head direction, the spectral mass outside the negative set weighted by σ₊ exceeds the mass inside weighted by |σ₋|, with Slepian-type concentration structure." The first half is the definition of β_j < 1 (prop:negtrace(iv)) rewritten; the second is false in the data: the leakage L_out = 1 − L_in ∈ [0.25, 0.50] is not exponentially small (§2.2), so no time-band concentration bound (Slepian/Fuchs/Widom: 1 − λ_n ≍ c^{n+½}e^{−2c}; Landau–Widom: log transition) enters the inequality. **NO-GO (class: inequalities bounding 1 − β_j by functions of the unweighted leakage L_out and invariants of S_T):** by prop:negtrace(v) there are symbols with the same {σ<0}, the same σ₋ and the same L_out for each u with β > 1; and in the data L_out is O(1) while 1 − β_j ranges over 10⁻²²…10⁻¹: there is no function of L_out that captures it. This is R186_039 §2.3(d) with L_out in place of λ_j(S_T).
**3.2 Staircase (NUMERICAL; no law).** Deep steps per window: 5.38/5.78 (½log5), 5.78/6.45 (0.9), 6.05/6.97 (1.0); growing with T. Against: π²/log N_Sh = 5.05, 3.75, 3.10 (**refuted**: opposite trend); 2π²/log N(T*) = 14, 11, 9.5 (no); single-interval Slepian with c = T·T*: log(8c/1) = 5.31, 5.61, 5.92 (first step within 1–5%; second step 4.6–5.2 against 5.8–7.0 observed: no); prolates of the full negative set: steps 0.0–1.1 (no). Alternating parity ⇒ staircase by sector: even steps ≈ 11, 8.4 (½log5), 13.0, 10.9, 10.3, 8.5 (1.0). Record, not model.
**3.3 What does survive as a head statement (OPEN, formulated):** *Lemma H′.* For T ≥ 0.6, K_δ(T) = N(T*) + O(1) for δ ∈ [10⁻⁴, 10⁻²] and the directions u_j, j ≤ K, satisfy Σ_{γ≤T*}|û_j(γ)|² ≤ 10⁻⁶ (1 − β_j) Pos(u_j) and 1 − β_j = (1+o(1)) 2Σ_{γ>T*}|û_j(γ)|²/Pos(u_j). What would make it PROVED: a lower bound on Σ_{γ>T*}|û(γ)|² over the near-kernel of the low sampling — which is row D for that direction, with real γ (CONDITIONAL). It is not proposed as a route.

## 4. Honesty: where it inherits

The "leakage weighted by σ₊" IS 1 − β_j by definition: Pos(u_j) − Neg(u_j) = 𝔞_T(u_j) = λ_A at j = 1 (R186_034 Thm 2.2). Exact step of the inheritance: **identity 2.1** (lem:roughEF) converts the difference Pos − Neg into Σ_ρ Φ(ρ)Φ(1−ρ); everything computed from there onward (vanishing at the low zeros, dominance of the zeros > T*, 40/15% of 𝔞_far) describes u_j, which was already obtained by diagonalizing the bundle. There is no "from σ and Slepian" computation giving 1 − β_j: the bundle restricted to the Shannon subspace of S_T (without λ_A) gives 1 − β^Sh = 2.2·10⁻³ (½log5), 5.7·10⁻⁶ (0.9), 1.9·10⁻⁷ (1.0) — positive, but 8, 10 and 15 orders above the truth, because the 0.05% of mass outside the Shannon subspace carries the whole cancellation (the same as R186_024/104 for E_k). Label of the leakage lemma: **NO-GO as a mechanism; total inheritance as an identity.**

## 5. Falsifier (NUMERICAL, mpmath dps 40)

| T | M | λ_A | 1−β₁ | K₄/K₃/K₂/K_e | N(T*) | N_Sh | steps |
|---|---|---|---|---|---|---|---|
| ½log5 | 40 | 3.886e-12 | 1.731e-11 | 4/4/5/6 | 4 | 7.05 | 5.38 5.78 4.26 4.08 3.40 1.58 |
| 0.9 | 56 | 5.751e-17 | 1.714e-16 | 5/6/7/8 | 6 | 13.94 | 5.78 6.45 5.22 5.47 4.28 3.95 2.93 1.63 |
| 1.0 | 50 | 1.53e-20 | 5.42e-20 | 8/9/9/11 | 8 | 24.08 | 5.6 6.45 5.12 4.93 2.74 4.8 3.35 3.9 3.37 2.59 |
| 1.0 | 60 | 2.93e-22 | 1.04e-21 | 8/9/9/11 | 8 | 24.08 | 6.01 6.65 5.02 5.10 4.50 5.20 4.33 3.99 3.40 2.58 |
| 1.0 | 70 | 4.17e-23 | 1.48e-22 | 8/9/9/11 | 8 | 24.08 | 6.05 6.97 5.42 5.49 4.93 5.33 4.47 4.05 3.43 2.58 |

½log5 reproduces R186_034/039 (1.72·10⁻¹¹) to 4 digits. At T = 1 the Legendre Galerkin does not converge in the first two eigenvalues (factor of 7 per +10 in M): λ_A(1) ≤ 4.2·10⁻²³ is a variational upper bound; −log λ_A(1) ≥ 51.5 (Zhu: −ln λ_W(1.0) = 67 for the full form; λ_W ≤ λ_A). Counts and steps j ≥ 3 are stable in M. **Verdict:** K₃(1.0) = 9 = N(T*) + 1; "≈ 14" refuted; slope π²/log N_Sh refuted; Lemma H survives only in the count (Lemma H′, §3.3). The incompatibility flagged by R186_112 §1.3(c) is resolved as follows: Zhu's constant 2π² does not describe λ_A at T ≤ 1 (−log λ_A(1) ≈ 52–55 against 2π²·8/log 8 = 76), and the steps grow with T (6 → 7 at the bottom) instead of being fixed ≤ 6.

## 6. Audit notes
- Everything is NUMERICAL except 2.1 (identity, PROVED mod lem:roughEF) and 1.2(a) (commutation with the reflection, PROVED). 1.3 is ARGUED (elementary asymptotics), not a theorem about the head.
- The "zeros ≤ T* / > T*" partition uses 150 real zeros (CITED) and a tail by density; the closure to 0.5–3% is a check on the identity, not certification.
- The mp runs use the same Galerkin as r034 (Gauss nodes in mpf, spherical Bessel functions via descending Miller recursion, Neg by 100-node quadrature per component, endpoints of {σ<0} refined with findroot); control at ½log5 to 4 digits against double precision. The non-convergence in M at T = 1 affects λ_A and 1 − β₁,₂, not the counts.
- The vanishing at zeros in multiple precision was verified only for u₁ at T = 0.9 (the post-processing of the 12 vectors at T = 1, with τ_last = 1550, was left unfinished for cost reasons); the counts and staircases at T = 1 come from the complete mp runs.
- No equivalence with other statements is used; the sum over zeros appears as an unconditional identity (lem:roughEF) with the individual terms positive only where γ is real (CITED for the 150 used).
