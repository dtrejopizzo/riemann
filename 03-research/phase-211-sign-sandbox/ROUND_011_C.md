# Round 011 C — The packet margin m − P^ρ_T on the high range: a finite reduction, the computed minima, and the direct packet values

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). Notation of ROUND_011_A: λ = e^T, N = λ², v_n = 2Λ(n)/√n,
m(τ) = Re ψ(¼ + iτ/2) − log π (the archimedean symbol; m(0) = C_0 of tools/galerkin_mp.py),
P^ρ_T(τ) = Σ_{n<N} v_nρ(log n/T)cos(τ log n), ρ the normalised autocorrelation of a profile β on [−1, 1],
packet g₀ = β(x/T)cos(τ₀x), high range τ₀ ≥ Ω_lo := 2πN(1 + δ), δ = 0.1 unless stated.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check

Searched: ROUTES-TRIED-INDEX rows P211-10A, P211-11A (its "next" column names exactly this computation), ledger C24–C25,
ROUND_010_A §3.4 (RMS competition 2T vs 2T + O(1)), ROUND_011_A §§1, 3, 4. This memo is the numerical step prescribed
there plus one elementary observation (§1); no indexed route is retried. Not a sign step: nothing below is offered as a
proof of (★); falsifier test in §5 for the one PROVED statement.

## 1. The high range is finite for every fixed κ (PROVED, elementary)

**Lemma 1.1.** (i) m is strictly increasing on (0, ∞). (ii) Put Σ^ρ_T := P^ρ_T(0) = Σ_{n<N}v_nρ(log n/T). For κ ≥ 0 let
τ*_κ be the solution of m(τ*_κ) = Σ^ρ_T + κ (if Σ^ρ_T + κ > m(0)). Then m(τ) − P^ρ_T(τ) ≥ κ for every τ ≥ τ*_κ.
(iii) Consequently the family (1.2) of ROUND_011_A with a fixed κ is a statement on the compact range
[Ω_lo, τ*_κ] only, with log τ*_κ = Σ^ρ_T + κ + log 2π + O(e^{−Σ^ρ_T}) ≤ Σ₀ + κ + 2, Σ₀ = Σ_{n<N}v_n = 4λ(1 + o(1)).
*Proof.* (i) d/dτ Re ψ(¼ + iτ/2) = −½Im ψ′(¼ + iτ/2) = Σ_{k≥0}(k + ¼)(τ/2)/|k + ¼ + iτ/2|⁴ > 0 for τ > 0, from
ψ′(z) = Σ_k(k + z)^{−2}. (ii) v_n ≥ 0 and 0 ≤ ρ ≤ 1, so P^ρ_T(τ) ≤ Σ^ρ_T for all τ; by (i), m(τ) ≥ Σ^ρ_T + κ for
τ ≥ τ*_κ. (iii) m(τ) = log(τ/2π) + O(1/τ²) (Stirling, CITED). ∎
Reading. For the O(1)-margin form (1.2) the upper end of the open range of ROUND_011_A drops from
log Ω_B ≍ (64/(eϑ²))Te^{2T} (Theorem 3.1 there) to log τ* ≤ 4e^T(1 + o(1)); Theorem 3.1 is still what gives the
coercivity of size ≍ m (Corollary 3.2), which Lemma 1.1 does not. Whenever Σ^ρ_T + κ ≤ m(Ω_lo) the range is empty and
(1.2) holds on the whole high range with no computation. The numbers (NUMERICAL, double precision; tools/packet_margin.py):

| T | N | m(Ω_lo) | Σ^ρ_T ind / cos² / bump | log τ*_0 ind / cos² / bump | log N⁴ |
|---|---|---|---|---|---|
| 0.8 | 4.95 | 1.695 | 0.957 / 0.293 / 0.416 | 2.80 / 2.13 / 2.25 | 6.4 |
| 1.0 | 7.39 | 2.095 | 1.585 / 0.588 / 0.782 | 3.42 / 2.43 / 2.62 | 8.0 |
| 1.2 | 11.02 | 2.495 | 2.348 / 0.950 / 1.222 | 4.19 / 2.79 / 3.06 | 9.6 |
| 1.4 | 16.44 | 2.895 | 3.231 / 1.370 / 1.731 | 5.07 / 3.21 / 3.57 | 11.2 |
| 1.5 | 20.09 | 3.095 | 3.710 / 1.601 / 2.010 | 5.55 / 3.44 / 3.85 | 12.0 |
| 2.0 | 54.60 | 4.095 | 6.815 / 2.971 / 3.681 | 8.65 / 4.81 / 5.52 | 16.0 |
| 2.5 | 148.4 | 5.095 | 11.30 / 4.744 / 5.880 | 13.14 / 6.58 / 7.72 | 20.0 |
| 3.0 | 403.4 | 6.095 | 17.81 / 7.018 / 8.760 | 19.65 / 8.86 / 10.60 | 24.0 |
| 4.0 | 2981 | 8.095 | 41.27 / 13.70 / 17.53 | 43.11 / 15.54 / 19.36 | 32.0 |

Profiles: "ind" = 1_{[−0.95,0.95]} mollified at width 0.05 (C_c^∞, ρ ≈ triangle 1 − |u|/2), "cos²" = cos²(πx/2),
"bump" = exp(−1/(1 − x²)). So (1.2) holds with κ ≥ m(Ω_lo) − Σ^ρ_T > 0 on the whole high range by Lemma 1.1 alone: for cos² at every
T ≤ 2.5 (κ ≥ 1.40, 1.51, 1.55, 1.53, 1.49, 1.12, 0.35 at T = 0.8, …, 2.5), for bump at T ≤ 2.0 (κ ≥ 1.28, 1.31, 1.27,
1.16, 1.09, 0.41), for ind at T ≤ 1.2 (κ ≥ 0.74, 0.51, 0.15).
For larger T the range [Ω_lo, τ*_0] is nonempty but, for T ≤ 2.5 (all profiles) and T = 3 (cos², bump), it lies
inside the reach of a direct grid; for T = 3 with ind (log τ*_0 = 19.65, ≈ 2·10¹⁰ grid points × 98 terms) it is scanned only in part (§2).

## 2. The minima of m − P^ρ_T on the high range (NUMERICAL)

Method (tools/packet_margin.py). Grid of spacing h = 1/(20T) on [Ω_lo, τ_hi]; the 40 smallest grid values of
m − P^ρ_T are refined by a bounded Brent search on ±1/(10T). Grid error before refinement: P^ρ_T has frequencies
< 2T, so |(P^ρ_T)″| ≤ 4T²Σ^ρ_T and the error at a missed minimum is ≤ 4T²Σ^ρ_T h²/8 = Σ^ρ_T/3200. Range: τ_hi = τ*_0
when τ*_0 > Ω_lo (by Lemma 1.1 this is the whole high range, so the minimum below is the infimum over [Ω_lo, ∞)),
otherwise τ_hi = N⁴ (T ≤ 1.5) and the infimum over (N⁴, ∞) is ≥ m(N⁴) − Σ^ρ_T > 0. m by the complex digamma
function (scipy), double precision; the comb sums have at most 98 terms.

Table 2.1. inf_{τ ≥ Ω_lo}(m − P^ρ_T), its location τ_min, τ_min/(2πN), and P^ρ_T(τ_min)/Σ^ρ_T.

| T | profile | inf (m − P^ρ_T) | τ_min | τ_min/2πN | P^ρ_T(τ_min) | P^ρ/Σ^ρ | range scanned |
|---|---|---|---|---|---|---|---|
| 0.8 | ind | 1.0418 | 45.52 | 1.46 | 0.9386 | 0.98 | [Ω_lo, N⁴] |
| 0.8 | cos² | 1.4900 | 35.80 | 1.15 | 0.2500 | 0.85 | [Ω_lo, N⁴] |
| 0.8 | bump | 1.4015 | 35.73 | 1.15 | 0.3364 | 0.81 | [Ω_lo, N⁴] |
| 1.0 | ind | 0.8679 | 62.96 | 1.36 | 1.4367 | 0.91 | [Ω_lo, N⁴] |
| 1.0 | cos² | 1.7363 | 63.18 | 1.36 | 0.5718 | 0.97 | [Ω_lo, N⁴] |
| 1.0 | bump | 1.5499 | 63.15 | 1.36 | 0.7578 | 0.97 | [Ω_lo, N⁴] |
| 1.2 | ind | 0.8356 | 109.07 | 1.57 | 2.0186 | 0.86 | [Ω_lo, N⁴] |
| 1.2 | cos² | 1.8446 | 90.94 | 1.31 | 0.8277 | 0.87 | [Ω_lo, N⁴] |
| 1.2 | bump | 1.6518 | 90.91 | 1.31 | 1.0203 | 0.83 | [Ω_lo, N⁴] |
| 1.4 | ind | 0.9642 | 136.38 | 1.32 | 2.1134 | 0.65 | [Ω_lo, τ*_0] = all |
| 1.5 | ind | 0.6035 | 171.65 | 1.36 | 2.7041 | 0.73 | [Ω_lo, N⁴] ⊃ [Ω_lo, τ*_0] |
| 1.5 | cos² | 1.8313 | 171.81 | 1.36 | 1.4772 | 0.92 | [Ω_lo, N⁴] |
| 1.5 | bump | 1.4858 | 171.78 | 1.36 | 1.8226 | 0.91 | [Ω_lo, N⁴] |
| 2.0 | ind | 0.3409 | 416.87 | 1.22 | 3.8541 | 0.57 | [Ω_lo, τ*_0] = all |
| 2.5 | ind | 0.4188 | 1268.78 | 1.36 | 4.8892 | 0.43 | [Ω_lo, τ*_0] = all |
| 2.5 | bump | 1.1485 | 1178.45 | 1.26 | 4.0856 | 0.69 | [Ω_lo, τ*_0] = all |
| 3.0 | cos² | 1.1939 | 2819.16 | 1.11 | 4.9124 | 0.70 | [Ω_lo, τ*_0] = all |
| 3.0 | bump | 0.5444 | 2819.17 | 1.11 | 5.5619 | 0.63 | [Ω_lo, τ*_0] = all |
| 3.0 | ind | 0.3614 | 2927.65 | 1.15 | 5.7826 | 0.32 | [Ω_lo, 2·10⁶] only (log τ*_0 = 19.65) |

Rows without a scan: at T = 1.4 (cos², bump), 2.0 (cos², bump) and 2.5 (cos²) Lemma 1.1 alone gives the lower bounds
of §1 (the scanned values on a unit interval after Ω_lo are 2.98, 2.84, 3.42, 3.11, 4.53; these are values, not infima).

Observations (NUMERICAL).
(a) No negative value anywhere: for every (T, profile) computed, inf_{τ≥Ω_lo}(m − P^ρ_T) > 0, and for T ≤ 2.5 (all three
profiles) and T = 3 (cos², bump) this infimum is over the entire high range [Ω_lo, ∞) (Lemma 1.1 closes the tail).
Smallest margin found: 0.341 (T = 2.0, ind).
(b) Location: the minimum is always at the bottom of the high range, τ_min/(2πN) ∈ [1.11, 1.57], i.e. within the first
few cells after Ω_lo; never in the upper part of [Ω_lo, τ*_0]. The upper part is where the torus model of ROUND_011_A
§4(b) predicted danger; at these T the cost of the logarithm in m beats every alignment the comb reaches there.
(c) Size of the competing peak: P^ρ_T(τ_min) ≈ 0.43–0.98·Σ^ρ_T, decreasing in T for ind (0.98 → 0.43); in absolute terms
P^ρ_T(τ_min) for ind is 0.94, 1.44, 2.02, 2.11, 2.70, 3.85, 4.89 at T = 0.8, …, 2.5, i.e. ≈ 1.2T to 1.96T, against
m(τ_min) ≈ 2T + 0.1 to 2T + 0.4. This is exactly the O(1) competition of ROUND_010_A §3.4(i) and ROUND_011_A Prop 4.1:
both sides are ≍ 2T and the margin is the O(1) difference.
(d) Trend in T (ind, the profile with the largest Σ^ρ): 1.04, 0.87, 0.84, 0.96, 0.60, 0.34, 0.42 at T = 0.8, 1.0, 1.2,
1.4, 1.5, 2.0, 2.5, and 0.36 at T = 3.0 on [Ω_lo, 2·10⁶] — decreasing on average, not monotone, no evidence of a crossing up to T = 3. The smoother profiles
keep margin ≥ 0.54 (bump, T = 3) and ≥ 1.19 (cos², T = 3). The trend is NOT a proof of anything and is too short to
extrapolate: with peaks growing like ≈ 2T and m(Ω_lo) = 2T + log(1 + δ) + O(1/N²), a crossing at larger T is neither
excluded nor indicated by these data.

## 3. Direct values of W_T on the worst packets (NUMERICAL)

Method (tools/packet_direct.py). f := projection of g₀ onto P_T = {A(f) = B(f) = 0}, A(f) = ∫f e^{x/2}, B(f) = ∫f e^{−x/2};
W_T(f) = (1/2π)∫m|f̂|² − Σ_n v_n c_f(log n) (form (3.1) of ROUND_010_A, with A = B = 0). The archimedean part by
zero-padded FFT quadrature of f̂ (2¹⁸ samples on I_T, padding ×16); c_f(u) = ∫f(x)f(x + u)dx exactly on the same grid.
Convergence: doubling the samples changes W/‖f‖² by ≤ 5·10⁻³ at T = 2.5 (2¹⁶ → 2¹⁸) and by < 10⁻⁶ at T = 1.0.

Table 3.1. W_T(f)/‖f‖² against the packet prediction m(τ₀) − P^ρ_T(τ₀) at the minimisers of Table 2.1.

| T | profile | τ₀ | W_T(f)/‖f‖² | m − P^ρ_T | difference | ‖g₀ − f‖/‖g₀‖ |
|---|---|---|---|---|---|---|
| 1.0 | ind | 62.965 | 0.86562 | 0.86794 | −2.3·10⁻³ | 1.4·10⁻³ |
| 1.0 | bump | 63.153 | 1.54950 | 1.54990 | −3.9·10⁻⁴ | 8.8·10⁻⁵ |
| 1.4 | ind | 136.378 | 0.96399 | 0.96416 | −1.7·10⁻⁴ | 1.6·10⁻⁴ |
| 1.5 | ind | 171.647 | 0.60340 | 0.60350 | −1.0·10⁻⁴ | 1.7·10⁻⁵ |
| 1.5 | cos² | 171.809 | 1.83133 | 1.83134 | −1.9·10⁻⁵ | 8.4·10⁻⁸ |
| 1.5 | bump | 171.778 | 1.48576 | 1.48577 | −1.6·10⁻⁵ | < 10⁻⁸ |
| 2.0 | ind | 416.874 | 0.34086 | 0.34085 | +3.9·10⁻⁶ | 3.5·10⁻⁷ |
| 2.5 | ind | 1268.78 | 0.41903 | 0.41887 | +1.7·10⁻⁴ | < 10⁻⁸ |
| 2.5 | bump | 1178.45 | 1.14864 | 1.14850 | +1.4·10⁻⁴ | < 10⁻⁸ |
| 3.0 | cos² | 2819.16 | 1.19530 | 1.19390 | +1.4·10⁻³ | < 10⁻⁸ |
| 3.0 | bump | 2819.17 | 0.54610 | 0.54445 | +1.6·10⁻³ | < 10⁻⁸ |
| 3.0 | ind | 2927.65 | 0.36190 | 0.36144 | +4.6·10⁻⁴ | < 10⁻⁸ |

(At T = 3.0 the difference is at the quadrature resolution, τ₀·Δx ≈ 0.065.)
Error terms of Lemma 1.1 of ROUND_011_A, measured. (a) Projection to P_T: ‖g₀ − f‖/‖g₀‖ ≤ 1.4·10⁻³ at the worst case
(T = 1, ind, the least smooth profile at the smallest τ₀T ≈ 63), ≤ 2·10⁻⁴ for T ≥ 1.4. (b) Window truncation (the
oscillatory second term of c_{g₀} and the cross term β̂_T(τ − τ₀)β̂_T(τ + τ₀)): below the 10⁻⁵ level except at T = 1.0.
(c) Cell smearing ε₂ ≍ m″/T² and m′-odd cancellation: of order 1/(τ₀T)² ≤ 3·10⁻⁴. Total |W/‖f‖² − (m − P^ρ_T)| ≤ 2.4·10⁻³
in every case, two orders below the smallest margin 0.34.

## 4. Decision

The alternative posed by the task does not arise in the computed range: m − P^ρ_T never goes negative on the high range
(T ≤ 2.5 all profiles, T = 3 cos² and bump: over all of [Ω_lo, ∞); T = 3 ind: on [Ω_lo, 2·10⁶], log 2·10⁶ = 14.5 of log τ*_0 = 19.65, minimum 0.361 at 1.15·2πN; the remaining
[2·10⁶, 3.4·10⁸] is not scanned), and the packet approximation is
accurate to ≤ 2.4·10⁻³, so the computed packet values W_T(f)/‖f‖² are positive with margins 0.34–1.8. In particular there
is no tension with λ_A(T) ≥ 0 on the certified (T ≤ ½log 5) or resolved (T ≤ 1.4) ranges, and none at T = 1.5–3.0 either.
Consequences for the formulation.
(i) (HR)(a) in its pointwise form (1.2) of ROUND_011_A is the right formulation at these T: it is consistent (no packet
violates it), the packet approximation is sharp (error ≪ margin), and the worst centre is not a near-coincidence high
in the range but a cell just above the plunge, τ₀ ≈ (1.1–1.6)·2πN. No coupling of high-frequency packets is forced by
the data: single packets already see the worst value, and since the minimum sits at the bottom of the range, the
near-coincidence structure (simultaneous alignment of many log p) is not what produces the smallest margin here.
(ii) The open part of (HR)(a) is therefore a statement about the first cells above the plunge (Table 2.1, column
τ_min/2πN) plus the finite range [Ω_lo, τ*_κ] of Lemma 1.1, log τ*_κ ≤ Σ₀ + κ + 2. The torus-model heuristic of ROUND_011_A
§4(b) (failure possible for log τ < 8T²) covers the whole finite range at every computed T (log τ*_0 ≤ 19.7 < 8T²),
yet nothing fails. Reason (ARGUED, elementary): the Gaussian extreme value 2T√(2L) used there ignores the cap
P^ρ_T ≤ Σ^ρ_T; at L = log τ ≤ log τ*_0 it exceeds Σ^ρ_T (e.g. T = 2.5, L = 13: 25 against 11.3), so the heuristic is
vacuous there. The two constraints give the danger zone log τ ≲ min(8T², Σ^ρ_T + log 2π); the torus bound is the
binding one only once 8T² < Σ^ρ_T, i.e. only for T ≳ 6.5 with ind (Σ^ρ_T = 41, 93, 207 against 8T² = 128, 200, 288 at T = 4, 5, 6). The computed range (T ≤ 3) is
entirely in the cap-limited regime, and there the observed peaks P^ρ_T(τ_min) ≈ 1.2T–2T sit far below both caps.
(iii) What the data do not decide: whether inf(m − P^ρ_T) stays bounded below uniformly in T. The ind margins 0.34 / 0.42
at T = 2.0 / 2.5 are the smallest; the competition is O(1) between two quantities ≍ 2T.

## 5. Falsifier note

Lemma 1.1 is not a sign step and survives every falsifier of BRIEF rule 4: it uses only v_n ≥ 0, ρ ∈ [0, 1] and the
monotonicity of m. For cΛ, Σ^ρ_T scales by c and log τ* grows by (c − 1)Σ^ρ_T; for c large (1.2) fails already at the
bottom of the range (ROUND_011_A Prop 4.1), consistent with (c) of §2: the margin is an O(1) difference of two ≍ 2T
quantities and is destroyed by multiplying the comb by c ≈ 1 + margin/(2T). For ind at T = 2.0, c = 1 + 0.341/3.854
≈ 1.09 already makes m − cP^ρ_T vanish at τ_min (NUMERICAL, from Table 2.1). So the computed positivity is Λ-specific
only in the weak sense of a ≈ 9% budget; it is not evidence of a mechanism.

## Result

PROVED piece + NUMERICAL. PROVED (elementary): for every T, profile and κ the packet condition (1.2) is a statement on
the finite range m(τ) < Σ^ρ_T + κ, log τ* ≤ Σ₀ + κ + 2 ≍ 4e^T (Lemma 1.1). NUMERICAL: m − P^ρ_T > 0 on the whole high
range for T = 0.8–2.5 (three profiles) and T = 3 (cos², bump); smallest margin 0.341 (T = 2, mollified indicator); the
worst centre is always just above the plunge (1.1–1.6·2πN); direct packet values W_T(f)/‖f‖² match m − P^ρ_T to
≤ 2.4·10⁻³. (HR)(a) in pointwise form is consistent and correctly formulated at these T; no coupling of high packets is
forced by the data.

### What was proved
- Lemma 1.1: m strictly increasing; P^ρ_T ≤ Σ^ρ_T; (1.2) with κ holds for τ ≥ τ*_κ, m(τ*_κ) = Σ^ρ_T + κ. For O(1)
  margins this shortens the open range of ROUND_011_A from log τ < log Ω_B ≍ Te^{2T} to log τ < Σ^ρ_T + κ + log 2π.

### What failed and why
- Nothing failed numerically: no negative packet margin was found; hence no test of "packet approximation fails vs W
  genuinely negative" was needed — the approximation was checked anyway and is sharp (errors ≤ 2.4·10⁻³ ≪ margins).
- The data do not show a uniform-in-T lower bound: margins for the mollified indicator decrease on average
  (1.04 → 0.34–0.42) as two ≍ 2T quantities compete; the cΛ budget is ≈ 9% at T = 2.
- The torus-model danger zone of ROUND_011_A §4(b) is vacuous for T ≲ 6.5 (the cap Σ^ρ_T binds first).
- T = 3 with the mollified indicator: [2·10⁶, 3.4·10⁸] not scanned (cost).

### Next concrete step
Prove (1.2) on the first cells above the plunge, τ ∈ [2πN(1 + δ), C·2πN], uniformly in T: there m(τ) = 2T + log(τ/2πN)
+ O(N⁻²) and the target is sup_{τ∈[2πN(1+δ), C2πN]} P^ρ_T(τ) ≤ 2T + log(1 + δ) − κ, a large-values statement for a
Dirichlet polynomial of length N at height ≍ N (the Montgomery–Vaughan regime, not the near-coincidence regime);
complete the T = 3 ind scan on [2·10⁶, 3.4·10⁸] if a uniform statement is attempted numerically first.
