# Round 15 A — The high block on the gauge quotient: mollified tail Gram, long-range band, and the chirp ledger of the comb

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_012_B and ROUND_014_A: ψ_k even prolates of [−λ, λ], c = 2πN,
N = λ² = e^{2T}, d_k = 1 − χ_k, ε_k = i^k, S = diag(ε_k), u_k the out-of-band part of √χ_kφ_k, 𝒯 the tail map
𝒯h(x) = 1_{(−∞,−T)}(x)e^{−x/2}Σ_{n≥1}h(ne^{−x}), 𝒢 the tail form, M the Gram of W_T on Eψ_k, 𝒜 the admissible coefficient
space (f(λ) = f(0) = ∫f = A(Ef) = B(Ef) = 0), ℓ_g^S = Sℓ_gS the gauge-minimised leakage in the b-variable b = Sa,
H the high indices 4N < k ≤ K. m(τ) = Re ψ(¼ + iτ/2) − log π. Weil form on functions F supported in (−∞, −T]:
𝒲[F] = 𝒜_∞[F] − 2Σ_{m≥2}Λ(m)m^{−1/2}⟨τ_{log m}F, F⟩, τ_ℓF := F(· − ℓ), 𝒜_∞ the archimedean part (Lévy form with its
constant), whose Fourier form is (1/2π)∫m(τ)|F̂(τ)|²dτ. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO /
NUMERICAL.

## 0. Corpus check
Index rows read: P211-11A, P211-11C, P211-12A (Montgomery–Vaughan + Sobolev/Gallagher NO-GO for the POINTWISE packet bound
(U)), P211-12B, P211-13A, P211-14A (exact transfer, gauge collapse, chirps not packets); ledger C24–C31. Phase 199:
PROOF_L_SHARP_E_001 Theorem E.2 (prime collapse: on Poisson images the full comb is Z_logZ^{−1}, Λ ∗ 1 = log) and Theorem
E.5 (ratio classes indefinite one by one); PROOF_L_SHARP_X_001 Theorem B (single-cell chirp data: 𝔔[ρ] = ∫w(t,φ′)|a|²
+ O(ν₀^{−1}), comb = −2H₁(N)‖ρ‖² exact, log² cancellation; constraint 20 of AUDIT_20: single-cell data prove nothing about
resonances between cells). INV_V_002 (operator form V*Ш = 2log|x|Ш).
What is on record and is NOT reclaimed here. The identity of §3.1 (comb on Poisson tails = 2⟨𝒯_log u, 𝒯u⟩) is Theorem E.2
of phase 199 written for the tail map of this phase; it is used, not re-proved as new. The single-chirp average with the
comb weight −2 log N is Theorem B of X_001.
What differs. (i) The object: the tail form of the high prolate block on mollified admissible data (ROUND_009_A type), on
the exact gauge quotient, with the measurement that 14A names as next step. (ii) The multi-chirp structure: a Poisson tail
is a superposition of all dilated chirps F_N, N ≥ 1, which constraint 20 says single-cell results do not cover; here the
NON-resonant pairs N ≠ N′ are controlled by the Montgomery–Vaughan generalised Hilbert inequality (a mean-value tool in
the regime where it works: no pointwise sup, only an average along a sweep of length L ≫ number of chirps). P211-12A used
MV for a pointwise bound and failed for that reason; here MV is used only for the off-diagonal non-resonant part, never
for the sign. (iii) The task hypothesis "the long-range constant-sign band of 𝒢 is the finite-rank radical correction"
is tested and is false (§1.3). No indexed route is retried.

## 1. The tail form on mollified data: entrywise definition and the exact radical correction

### Lemma 1.0 (rank of a radical correction; PROVED, linear algebra)
Let Q₁, Q₂ be symmetric bilinear forms on a finite-dimensional space V that agree on a subspace U of codimension r. Then
R := Q₁ − Q₂ has rank ≤ 2r, and in any basis adapted to V = U ⊕ W, R = [[0, X], [Xᵀ, Y]]. Equivalently R = CΓᵀ + ΓCᵀ
+ CQCᵀ, where the r columns of C are linear functionals cutting out U. In particular PRP = 0 for every projector P with
range U, so PQ₁P = PQ₂P. *Proof.* R(u, u′) = 0 on U × U; write v = u + w; R(v, v′) = R(u, w′) + R(w, u′) + R(w, w′),
a sum of terms each of rank ≤ r in one argument; the matrix shape is immediate. ∎

### Proposition 1.1 (entrywise tail Gram on mollified prolate data; PROVED given (S), (T) of ROUND_012_B)
Take the high prolates in the mollified form of ROUND_009_A §1: ψ̃_k the k-th even prolate of [−a, a] with band b = λ²/a
(so c = 2πab = 2πN is unchanged), f_k := (ψ̃_k1_{[−a,a]}) ∗ ρ_ε, a = λ − ε, ε = θλ^{−3}, ρ(u) = (35/32)(1 − u²)³₊.
(i) ℱf_k(ξ) = ε_k ρ̂(εξ)√χ_k φ̃_k(ξ) for every real ξ ((S) for ψ̃_k, then the convolution theorem). Put
ũ_k := ρ̂(εξ)√χ_kφ̃_k1_{|ξ|>λ}, so ℱf_k = ε_kũ_k off the band.
(ii) ρ ∈ C² with a jump of ρ‴ at ±1, so ρ̂(y) = O(|y|^{−4}); φ̃_k(ξ) = O(1/ξ) ((S): finite Fourier transform of a C¹
function). Hence ũ_k = O(ξ^{−5}), the Poisson series 𝒯ũ_k converges absolutely and uniformly on (−∞, −T], and with
F_N^{(k)}(x) := 1_{x<−T}e^{−x/2}ũ_k(Ne^{−x}) one has ‖F_N^{(k)}‖² = N^{−1}∫_{Nλ}^∞ũ_k² = O(N^{−10}). By Theorem 3.1 below the comb
part of 𝒲(𝒯ũ_j, 𝒯ũ_k) is the absolutely convergent double series 2Σ_{N,N′}log N⟨F_N^{(j)}, F_{N′}^{(k)}⟩, and the
archimedean part is finite (𝒯ũ_k is bounded, decays like e^{x/2} at −∞ and is C¹ off a single jump at x = −T, so
|ℱ𝒯ũ_k(τ)| = O(1/|τ|) and ∫m(τ)τ^{−2} < ∞). So 𝒢^ρ_{jk} := 𝒲(𝒯ũ_j, 𝒯ũ_k) is defined ENTRYWISE.
(iii) f_k(λ) = f_k′(λ) = 0 automatically (ROUND_009_A §1(i)); the admissible space 𝒜^ρ is cut out by the four functionals
f(0), ∫f, A(Ef), B(Ef). 12B Theorem 1.1 applies verbatim (its proof uses only (S) and (T)): M^ρ[a] = 𝒢^ρ[Sa] on 𝒜^ρ.
(iv) By Lemma 1.0 with U = S𝒜^ρ (codim ≤ 4): R^ρ := SM^ρS − 𝒢^ρ has rank ≤ 8, is of the form CΓᵀ + ΓCᵀ + CQCᵀ with C the
four functionals (in the b-variable), and P_C(SM^ρS)P_C = P_C𝒢^ρP_C for the projector P_C onto S𝒜^ρ.
So the "radical correction" between the computable Gram SMS and the entrywise tail Gram is exactly a rank ≤ 8 term
supported on the constraint functionals; it is invisible on the constraint-compatible subspace.

### 1.1 Numerical realisation (ARGUED + NUMERICAL)
The mollifier scale ε = θλ^{−3} (θ = 1/(48π²)) is far below the Galerkin resolution: at T = 0.8 (λ = 2.226) ε = 1.9·10⁻⁴,
and on the band of frequencies resolved by the sine basis (|τ| ≲ Nbπ/(2T), i.e. ξ ≲ 45 at Nb = 300) one has
|ρ̂(εξ) − 1| ≤ 2π²(εξ)²∫u²ρ ≤ 2·10⁻⁴; the dilation a/λ − 1 = −ε/λ ≈ −9·10⁻⁵ changes ψ_k by O(kε/λ) ≤ 10⁻² in the worst
(k ≈ 100) case at the edge, below the Galerkin error of the high indices near the cap. So at this resolution M^ρ and M
agree, and every number below is computed from the raw SMS of tools/prolate_tailgram.py, compressed by P_C with the FIVE
raw functionals (f(λ) included; on the mollified family it is automatic, on the raw family it is the condition of 14A §1.0)
— by (iv) the compressed matrix is the tail Gram itself on that subspace, not a proxy. The rank ≤ 8 (raw: ≤ 10) part
Ĝ − P_CĜP_C is reported separately. Tool: tools/tailgram_quotient.py (new; reads the SAVE file of prolate_tailgram.py).

### 1.2 Gauge-quotient bottoms as K grows (NUMERICAL)
Runs: (T, Nb, KMAX) = (0.8, 300, 120) and (1.0, 370, 148), plus a resolution control (1.0, 300, 120); dps 30, MIN = 12,
gauge rank 10, each ≤ 15 min. X := S𝒜 ∩ (SDJ)^⊥ (constraint-compatible and gauge-orthogonal; on X, ℓ_g^S = D exactly,
so the D-bottom on X is the bottom in the exact quotient metric); "ℓ_g^S-bottom" = inf over S𝒜 of 𝒢/ℓ_g^S (Theorem 1.1(iii)
of 14A, the exact gauge-quotient metric without removing directions).
| T | K | dim S𝒜 | D-bottom on S𝒜 | ℓ_g^S-bottom on S𝒜 | D-bottom on X (dim X) |
|---|---|---|---|---|---|
| 0.8 | 56 | 19 | 0.981 | 1.067 | 2.640 (4) |
| 0.8 | 64 | 23 | 0.466 | 0.987 | 2.003 (8) |
| 0.8 | 72 | 27 | 0.103 | 0.870 | 1.805 (12) |
| 0.8 | 80 | 31 | 0.0177 | 0.838 | 1.764 (16) |
| 0.8 | 88 | 35 | 0.0048 | 0.799 | 1.634 (20) |
| 0.8 | 96* | 39 | 0.0017 | 0.734 | 1.277 (24) |
| 1.0 | 68 | 20 | 1.365 | 1.447 | 3.084 (5) |
| 1.0 | 76 | 24 | 1.093 | 1.247 | 2.748 (9) |
| 1.0 | 84 | 28 | 0.878 | 1.145 | 2.564 (13) |
| 1.0 | 92 | 32 | 0.552 | 1.037 | 2.396 (17) |
| 1.0 | 100 | 36 | 0.243 | 0.978 | 2.269 (21) |
| 1.0 | 108* | 40 | 0.086 | 0.525 | 0.905 (25) |
| 1.0 | 116* | 44 | 0.028 | 0.123 | 0.204 (29) |
Resolution control (*). At T = 1.0, Nb = 300 gives D-bottom on X = 2.747, 2.562, 2.366 at K = 76, 84, 92 (Nb = 370: 2.748,
2.564, 2.396) and then collapses at K = 100 (0.618) and 104 (0.273), where Nb = 370 still gives 2.269. The collapse moves
with Nb, at K ≈ 0.29–0.33·Nb: it is a Galerkin-cap artifact, not a property of the form. Rows marked * are past that point
and are discarded. On the resolved ranges (K ≤ 88 at T = 0.8; K ≤ 100 at T = 1.0) Nb = 250/300/370 agree to ≤ 0.03.
Readings. (a) The D-bottom on S𝒜 → 0 (gauge collapse of 14A) is reproduced. (b) **The gauge-quotient bottom does not
stabilise on the resolved range**: on X it falls 2.64 → 1.63 (T = 0.8) and 3.08 → 2.27 (T = 1.0), with decreasing steps
(T = 1.0: −0.34, −0.18, −0.17, −0.13 per ΔK = 8); in the ℓ_g^S metric 1.07 → 0.80 and 1.45 → 0.98. Two-parameter fits
a + b/K extrapolate to a = −0.11 / 0.54 (X) and 0.30 / −0.03 (ℓ_g^S): the data do not decide between a positive floor
and decay to 0. No K-uniform constant is shown.

### 1.3 Band structure of the tail Gram on the constraint and gauge complements (NUMERICAL)
Mean signed value / mean modulus of the D-normalised entries at offset |j − k| = 2q (T = 0.8, K = 96, all 39 indices;
T = 1.0, K = 100; the compressions are the operators themselves, entries read in the original index basis).
| T | matrix | q=1 | q=2 | q=4 | q=6 | q=8 | q=10 | q=12 |
|---|---|---|---|---|---|---|---|---|
| 0.8 | Ĝ = SMS (raw) | −1.01 | −0.29 | −0.38 | −0.34 | −0.26 | −0.19 | −0.10 |
| 0.8 | P_CĜP_C (= tail Gram on S𝒜) | −0.93 | −0.33 | −0.40 | −0.35 | −0.27 | −0.18 | −0.07 |
| 0.8 | Ĝ − P_CĜP_C (rank ≤ 10), mean modulus | 0.11 | 0.08 | 0.07 | 0.06 | 0.06 | 0.06 | 0.06 |
| 0.8 | P_XĜP_X (gauge quotient) | −1.03 | −0.32 | −0.33 | −0.27 | −0.23 | −0.22 | −0.09 |
| 1.0 | Ĝ = SMS (raw) | −1.17 | −0.36 | −0.55 | −0.49 | −0.38 | −0.26 | −0.12 |
| 1.0 | P_CĜP_C | −1.05 | −0.43 | −0.58 | −0.49 | −0.37 | −0.23 | −0.08 |
| 1.0 | Ĝ − P_CĜP_C, mean modulus | 0.18 | 0.12 | 0.10 | 0.11 | 0.09 | 0.07 | 0.08 |
| 1.0 | P_XĜP_X | −1.21 | −0.43 | −0.43 | −0.36 | −0.30 | −0.23 | −0.05 |
(Odd q have the opposite sign and comparable size: +0.28/+0.31/+0.39 at q = 5 etc.; the pattern is (−1)^q in b, i.e. one
constant sign in a, as in 14A.)
Readings. (c) **The long-range band is NOT the radical correction.** The rank ≤ 10 part removed by the constraint
compression has entries ≤ 0.06–0.11 at every offset; the long-range (−1)^q band (0.27–0.37 at q = 8) survives the
compression unchanged and survives the gauge quotient (0.23–0.30 at q = 8). Operator norm of the part at offsets ≥ 8:
4.04 raw → 3.82 compressed (T = 0.8), 4.94 → 4.58 (T = 1.0). The hypothesis "long-range constant-sign band = finite-rank
radical/polar correction" is FALSE at this resolution: the band belongs to the tail form 𝒢 itself.
(d) Edge-kernel test. All prolates share the same large-ξ tail ε_kψ_k(λ)sin(2πλξ)/(πξ) (14A §1.0), which suggests
𝒢_{jk} ≈ v_jv_kκ(max(j, k)), v_k = ε_kψ_k(λ)/√d_k. The ratio Ĝ_{jk}/(v_jv_k) at offsets ≥ 8 is small and negative
(−0.008…−0.024) for max(j, k) ≲ 56 (T = 0.8) / 66 (T = 1.0), with spread 20–40% of the mean, and ≈ 0 ± 0.008 above; the
fitted kernel misses 82% / 90% of the long-range Frobenius mass. So the edge tail explains only the lower part of the band
(and with κ < 0 it is a negative rank-one-like piece −|κ|vvᵀ, which f(λ) = vᵀb = 0 kills to leading order). The upper
long-range band is unexplained by any rank-one or edge mechanism tested.
(e) The bottom vector on X is oscillatory along k (sign changes every 2–4 steps, envelope spread over k = 24…96), unlike
the smooth gauge vector of 14A: what remains after the gauge quotient is a cancellation between neighbouring tails, the
mechanism of 12B Corollary 1.3.

### 1.4 Diagonal against the archimedean chirp average (NUMERICAL)
Ĝ_kk − m(k) (m at the turning frequency τ_* = k of the chirp, §3.4) = 0.69, 0.61, 0.68, 0.69, 0.62, 0.63 (T = 0.8,
k = 26, 38, 50, 62, 74, 86) and 1.22, 1.23, 1.36, 1.38, 1.49, 1.39 (T = 1.0, k = 36, 48, …, 96): an offset nearly
independent of k (slight upward drift at T = 1.0) that depends on T. The k-independence matches the chirp ledger of §3 (margin ⟨m⟩ − log X_k independent of k); the size does
not match the leading-order prediction of §3.4 (predicted D-normalised diagonal 2.3 vs measured 3.2 at T = 0.8, k = 80;
2.2 vs 4.1 at T = 1.0, k = 96). Possible sources, not separated: the raw diagonal includes the rank ≤ 10 correction
(only P_C-compressed quantities are the tail form); the turning-region and forbidden-zone mass; the edge jump of 𝒯u at
x = −T. Rayleigh quotients of P_Xe_k are 3.0–4.5 (T = 0.8) and 3.8–5.6 (T = 1.0), growing with k.

## 2. What the chirp analysis must deliver
For a high datum u (out-of-band part of an admissible high combination), 𝒯u(x) samples u at Ne^{−x}, N ≥ 1. Above the
plunge u is, beyond its turning point ξ_* ≈ k/(2πλ), an oscillation of local frequency ≈ 2πλξ (14A §3, ARGUED), so each
Poisson summand F_N(x) = 1_{x<−T}e^{−x/2}u(Ne^{−x}) is a chirp in x whose instantaneous frequency sweeps [≈ max(k, cN), ∞).
The questions are: (Q1) is 𝒲[𝒯u] the average of the symbol "m − comb" along these sweeps, with explicit error; (Q2) what
does the comb become along a sweep; (Q3) which coercivity criterion results, and can a mean-value theorem prove it.

## 3. The chirp ledger (pure mathematics)

### Theorem 3.1 (comb on Poisson tails; PROVED — Theorem E.2 of phase 199 written for 𝒯)
Let u be even, supported in |ξ| > λ, with Σ_{N≥1}log N·‖F_N‖ < ∞, F_N(x) := 1_{x<−T}e^{−x/2}u(Ne^{−x}) (‖F_N‖² =
N^{−1}∫_{Nλ}^∞|u|²). Then 𝒯u = Σ_NF_N in L², and with 𝒯_log u := Σ_N log N·F_N,
    2Σ_{m≥2}Λ(m)m^{−1/2}⟨τ_{log m}𝒯u, 𝒯u⟩ = 2⟨𝒯_log u, 𝒯u⟩,   hence   𝒲[𝒯u] = 𝒜_∞[𝒯u] − 2⟨𝒯_log u, 𝒯u⟩.
*Proof.* For x < −T and m ≥ 2, x − log m < −T, so (τ_{log m}F_n)(x) = e^{−(x−log m)/2}u(nme^{−x}) = m^{1/2}F_{nm}(x). As 𝒯u
vanishes on x ≥ −T, ⟨τ_{log m}F_n, 𝒯u⟩ = m^{1/2}⟨F_{nm}, 𝒯u⟩. Summing, Σ_mΛ(m)m^{−1/2}Σ_n m^{1/2}⟨F_{nm}, 𝒯u⟩ =
Σ_N(Σ_{m|N}Λ(m))⟨F_N, 𝒯u⟩ = Σ_N log N⟨F_N, 𝒯u⟩; the rearrangement is justified by Σ_{m,n}Λ(m)|⟨F_{nm}, 𝒯u⟩| ≤
‖𝒯u‖Σ_N log N‖F_N‖ < ∞. ∎
Remark (domain, PROVED). For a raw single prolate u_k = ε_kψ_k(λ)sin(2πλξ)/(πξ) + O(ξ^{−2}) one has ‖F_N‖ ≍ N^{−1}, and
Σ log N/N = ∞: the obstruction of 14A §1.0 is exactly the divergence of the collapsed comb Σ log N·F_N. It disappears
under f(λ) = 0 (u = O(ξ^{−2}), ‖F_N‖ = O(N^{−2})) or mollification (Prop 1.1).

### Corollary 3.2 (the ledger along the sweeps; PROVED)
Under Theorem 3.1, 𝒲[𝒯u] = Σ_{N,N′}B_{NN′} with B_{NN′} := 𝒜_∞(F_N, F_{N′}) − (log N + log N′)⟨F_N, F_{N′}⟩, and the
diagonal is exactly
    B_{NN} = (⟨m⟩_N − 2 log N)‖F_N‖²,   ⟨m⟩_N := ∫m dν_N,   dν_N := |F̂_N(τ)|²dτ/(2π‖F_N‖²) (a probability measure).
ν_N is the time–frequency density of the N-th chirp integrated over time (the τ-marginal of its Wigner distribution). So
the answer to (Q1)–(Q2): on the diagonal 𝒲 is EXACTLY the average of the symbol m − 2 log N along the N-th sweep. **The
comb does not average out along a sweep: it is resonant.** Shifting by log m maps the sweep of F_n onto the sweep of F_{nm}
(the dilation identity in the proof), so the comb contributes the constant 2 log N = 2(Λ ∗ 1)(N) to the symbol of the N-th
chirp, not an oscillating polynomial to be smoothed. The localisation of ν_N on the sweep (ν_N ≈ A_N²/|τ_N′| at
τ = τ_N(x)) is the stationary-phase statement; for single-cell data it is PROVED with error O(ν₀^{−1}) in Theorem B of
phase 199 X_001; for prolate tails it is ARGUED (WKB) here.

### Theorem 3.3 (non-resonant pairs by the Montgomery–Vaughan inequality; PROVED in the dilation model)
Model: G ∈ L²(ℝ), F_N := N^{−1/2}τ_{log N}G (N ≤ X), F := Σ_{N≤X}a_NF_N, F_log := Σ_{N≤X}a_N log N·F_N, with
w₀ := |Ĝ|² and w₁ := m|Ĝ|² in W^{1,1}(ℝ). Put A_j := Σ_N|a_N|²(log N)^j and ⟨m⟩_G := ∫w₁/∫w₀. Then
    𝒜_∞[F] − 2Re⟨F_log, F⟩ = ‖G‖²Σ_{N≤X}|a_N|²N^{−1}(⟨m⟩_G − 2 log N) + E,
    |E| ≤ (3/2)‖w₁′‖_{L¹}A₀ + 3‖w₀′‖_{L¹}(A₀A₂)^{1/2}.
*Proof.* F̂_N(τ) = N^{−1/2}e^{−iτλ_N}Ĝ(τ), λ_N := log N. Diagonal terms: (1/2π)N^{−1}|a_N|²∫(w₁ − 2λ_Nw₀) =
‖G‖²|a_N|²N^{−1}(⟨m⟩_G − 2λ_N). Off-diagonal archimedean terms: Σ_{N≠N′}a_Nā_{N′}(1/2π)(NN′)^{−1/2}∫w₁e^{iτ(λ_{N′}−λ_N)}dτ;
since w₁ ∈ W^{1,1}, ∫w₁e^{iτδ} = −(iδ)^{−1}∫w₁′e^{iτδ}, so the sum equals
−(1/2π)∫w₁′(τ)·Σ_{N≠N′}z_N(τ)z̄_{N′}(τ)/(i(λ_{N′} − λ_N))dτ with z_N(τ) := a_NN^{−1/2}e^{−iτλ_N}. Montgomery–Vaughan
(CITED: J. London Math. Soc. (2) 8 (1974), generalised Hilbert inequality): for distinct reals λ_r with
δ_r = min_{s≠r}|λ_r − λ_s|, |Σ_{r≠s}z_rz̄_s/(λ_r − λ_s)| ≤ (3π/2)Σ|z_r|²/δ_r. Here δ_N ≥ log(1 + 1/N) ≥ 1/(N + 1), so
Σ|z_N|²/δ_N ≤ Σ|a_N|²(N + 1)/N ≤ 2A₀, and the archimedean off-diagonal is ≤ (1/2π)‖w₁′‖₁(3π/2)2A₀ = (3/2)‖w₁′‖₁A₀.
Comb off-diagonal: 2Re Σ_{N≠N′}λ_Na_Nā_{N′}(1/2π)(NN′)^{−1/2}∫w₀e^{iτ(λ_{N′}−λ_N)}; same integration by parts; the matrix
K_{rs} = 1/(λ_r − λ_s) (r ≠ s) is antisymmetric, so δ^{1/2}Kδ^{1/2} is normal and its norm equals its numerical radius,
≤ 3π/2 by the quadratic inequality; hence the bilinear bound |Σ_{r≠s}y_rz̄_s/(λ_r − λ_s)| ≤
(3π/2)(Σ|y_r|²/δ_r)^{1/2}(Σ|z_r|²/δ_r)^{1/2}, applied with y_N = λ_Nz_N, gives ≤ 2·(1/2π)‖w₀′‖₁(3π/2)(2A₂)^{1/2}(2A₀)^{1/2}
= 3‖w₀′‖₁(A₀A₂)^{1/2}. ∎
Reading. This is the mean-value theorem in the only regime where it works: the off-diagonal is O(X·‖w′‖₁) (with
a_N ≡ 1, A₀ = X), the diagonal is ≍ ‖G‖²log X, and ‖G‖²/‖w₀′‖₁ ≍ L, the length of the sweep in τ. So the error is
relatively O(X/(L log X)): a sweep long compared with the number of chirps — "Σv_n²/length". No pointwise sup is used,
and no sign is taken from it (the sign sits in the exact diagonal).
Also (PROVED, same proof): in the dilation model the comb resonance is τ_{log m}F_N = m^{1/2}F_{Nm} exactly, so for
a ≡ 1 on N ≤ X the collapse of Theorem 3.1 holds for the pairs inside [1, X]; the model is the untruncated version of
the tail, and the truncation 1_{x<−T} of the true tail is what makes it exact for all N (Theorem 3.1).

### Corollary 3.4 (coercivity criterion: average-symbol positivity along chirps; PROVED in the model)
In the model with a_N ≡ 1 (N ≤ X), using Σ_{N≤X}1/N = log X + γ + O(1/X) and Σ_{N≤X}log N/N = ½log²X + γ₁ + O(log X/X)
(CITED, standard; γ₁ ≈ −0.0728 the first Stieltjes constant):
    𝒲^mod = ‖G‖²[(⟨m⟩_G − log X)log X + γ⟨m⟩_G − 2γ₁ + O(⟨m⟩_G/X)] + E,  |E| ≤ (3/2)X‖w₁′‖₁ + 3X log X‖w₀′‖₁.
Hence the high block is coercive in the model as soon as
    (C) ⟨m⟩_G − log X ≥ κ > 0  and  X(‖w₁′‖₁ + 2log X‖w₀′‖₁) ≤ ε₀‖G‖²κ log X,
i.e. the archimedean average along the sweep exceeds the logarithm of the number of Poisson chirps that carry the mass.
This is weaker than pointwise (U): only the average ⟨m⟩_G against ν enters; the near-coincidence peaks of the comb never
appear, because the comb has been collapsed to the constants 2 log N.

### 3.5 Application to high prolate tails (ARGUED, WKB)
For a high datum with turning point ξ_* ≈ k/(2πλ) (ϑ_k ≈ k², t_* = √ϑ_k/c), the chirps F_N with Nλ < ξ_* carry essentially
all of u (they sample u where its mass is), so X_k ≈ ξ_*/λ = k/c; each sweeps from τ_* ≈ 2πλξ_* = k upward with profile
|Ĝ|² ∝ τ^{−p} (p = 2 for a raw prolate, p ≥ 4 on f(λ) = 0), so L ≍ k and ⟨m⟩_G ≈ m(k) + 1/(p − 1). Then
    ⟨m⟩_G − log X_k ≈ log(k/2π) − log(k/c) + 1/(p − 1) = log(c/2π) + 1/(p − 1) = 2T + 1/(p − 1),
independent of k: the margin of (C) is the logarithm of c/2π = N, i.e. turning frequency over chirp count. The MV error
ratio is X_k/(L log X_k) ≍ 1/(c log X_k). So on single tail profiles the chirp model predicts a k-uniform positive
average-symbol margin ≈ 2T + O(1). This is consistent with §1.4 (k-independent diagonal offset growing with T) but not with
§1.2 (the gauge-quotient bottom drifts down): the model controls each sweep profile, while the bottom vector on X
(§1.3(e)) is an oscillating combination of neighbouring tails whose sweeps nearly coincide (they share the asymptotic
tail), and the true tail differs from the model by the truncation at x = −T (a jump of size e^{T/2}Σ_Nu(Nλ), not a chirp)
and by the turning-region mass. Neither difference is controlled here.

### 3.6 What is and is not proved for (Q3)
PROVED: the exact ledger (Theorem 3.1, Corollary 3.2), the MV control of all non-resonant pairs in the dilation model
(Theorem 3.3) and the resulting criterion (C) (Corollary 3.4). NOT proved: (i) the transfer from the dilation model to
the truncated tail (the F_N of a true tail are N^{−1/2}τ_{log N} of DIFFERENT functions G_N = G1_{(−∞,−T−log N)}, so MV
does not apply verbatim; a layer decomposition G_N = Σ_{J≥N}G^{(J)} makes the coefficients separable but its W^{1,1}
norms are not bounded here); (ii) the WKB localisation of §3.5; (iii) the extension from single profiles to the
oscillating combinations that realise the bottom on X. The claim "the high block is controlled by averages of the comb, so
mean values suffice" is CORRECTED: the comb is not averaged, it is collapsed to the resonant weights 2 log N; mean values
control only the non-resonant remainder, which is where they belong.

## 4. Falsifier test (comb-blind acceptable for the high block)
Lemma 1.0, Theorem 3.3 and the MV bound are Λ-free (linear algebra and a mean-value inequality). The Λ-dependence of the
high block, in the tail picture, sits in exactly one place: the resonant weight (Λ ∗ 1)(N) = log N of Theorem 3.1.
(a) cΛ: the weight becomes c log N; in Corollary 3.4 the bracket is (⟨m⟩_G − c log X)log X + …, i.e. with ⟨m⟩_G − log X ≈
2T + κ (§3.5): (2T + κ − (c − 1)log X)log X. For c > 1 the criterion FAILS once log X_k > (2T + κ)/(c − 1), i.e. at
k ≈ c·exp((2T + κ)/(c − 1)) (≈ e^{290} for c = 1.01, T = 0.8): this is why 1.01Λ is invisible on the high block at K ≤ 100
(14A §4) — the high block does reject c > 1, but only asymptotically (as in Cor X.7(ii) of phase 199). For c < 1 the
criterion holds with a LARGER margin: the high-block criterion survives c < 1.
(b) a_P: (Λ_P ∗ 1)(N) = log of the P-rough part of N ≤ log N: the margin increases; survives.
(c) Beurling systems: the dilation identity τ_{log m}F_n = m^{1/2}F_{nm} needs the sampling set ℕ of the Poisson tail;
for a generalised-prime system there is no tail map 𝒯 and Theorem 3.1 has no analogue: the argument does not apply.
(d) finite modification v_m → v_m + δ_m: the weight becomes log N + Σ_{m|N}δ_m m^{1/2}; on average over N ≤ X this adds
Σ_mδ_m m^{−1/2}log X·(1 + o(1)), which is absorbed by the margin if Σ_mδ_m m^{−1/2} < 2T + κ and breaks it otherwise.
Conclusion: the high-block criterion survives (a) for c < 1, (b), and small (d). By rule 4 it is NOT a sign step and must
not be used as one; the sign of (★) cannot come from the high block (consistent with 11B, 12B, 14A: falsifiers are
rejected only in LM and its coupling). Note also that under (a), (b), (d) the identity M = S𝒢S itself acquires the window
term (Π_Λ − Π_w)(Ef) (12B §3), so the falsified M is not the tail form with a modified resonant weight; the statements
above concern the tail form.
NUMERICAL: no new falsifier runs (14A §4 already measured 1.01Λ and a_3 on the same objects at T = 0.8).

## Result
PIVOT with reason, plus PROVED pieces and one falsified hypothesis.
- PROVED: Lemma 1.0 and Proposition 1.1 (entrywise tail Gram on mollified high data; SMS − 𝒢^ρ has rank ≤ 8 and vanishes
  under the constraint compression); Theorem 3.1 (comb on Poisson tails = 2⟨𝒯_log u, 𝒯u⟩, the phase-199 collapse for 𝒯;
  domain remark: the raw obstruction is Σ log N/N = ∞); Corollary 3.2 (exact ledger: diagonal = average of m − 2 log N
  along the N-th sweep); Theorem 3.3 (MV control of every non-resonant pair in the dilation model, explicit constants);
  Corollary 3.4 (criterion (C): ⟨m⟩_G − log X ≥ κ with sweep length ≫ chirp count).
- NUMERICAL: gauge-quotient bottom does not stabilise on the resolved range (2.64 → 1.63 at T = 0.8, 3.08 → 2.27 at
  T = 1.0; the apparent collapse beyond K ≈ 0.3·Nb is a Galerkin-cap artifact, shown by the Nb = 300 / 370 control);
  the long-range (−1)^q band is part of 𝒢 itself, not the rank ≤ 10 radical correction (FALSIFIED hypothesis); the edge
  kernel explains only its lower part; diagonal offset Ĝ_kk − m(k) ≈ 0.65 (T = 0.8), 1.2–1.5 (T = 1.0), k-independent.
- ARGUED: WKB margin ⟨m⟩_G − log X_k ≈ 2T + 1/(p − 1), k-independent.
Pivot reason: the comb is not averaged along chirps; it is collapsed to resonant weights, and the remaining high-block
question is the transfer from single sweep profiles (where (C) holds with margin ≈ 2T) to the oscillating neighbour
combinations that realise the bottom on the gauge quotient.

### What was proved
See the PROVED list above. The task's claim "the high block is controlled by averages of the comb along chirps, so mean
values suffice" is replaced by the exact statement: the comb enters the high block only through the resonant weights
(Λ ∗ 1)(N) = log N on the Poisson chirp index (Theorem 3.1), the symbol along the N-th sweep is m − 2 log N exactly
(Corollary 3.2), and mean values (MV) control precisely the non-resonant remainder (Theorem 3.3).

### What failed and why
- Stabilisation of the gauge-quotient bottom: not observed on the resolved range; extrapolations a + b/K give floors
  between −0.11 and 0.54; undecided.
- "Long-range band = finite-rank radical correction": false; the removed rank ≤ 10 part is ≤ 0.06–0.11 per entry, the
  band (0.27–0.37 at offset 16) survives both compressions.
- Quantitative match of the diagonal with the chirp prediction: off by a factor 1.4–1.9 (sources listed in §1.4).
- Transfer of Theorem 3.3 to truncated tails (G_N depends on N): not done.

### Next concrete step
Build the tail directly (u_k by the Legendre–spherical-Bessel formula ℱ(ψ_k1)(ξ) = Σ_l c_l(−1)^{l/2}2λ√(l+½)λ^{−1/2}j_l(2πλξ),
mollified by ρ̂(εξ)), compute the chirp matrix B_{NN′} of Corollary 3.2 for the bottom vector of X at T = 0.8, K = 80, and
measure which part — diagonal ledger (⟨m⟩_N − 2 log N), non-resonant off-diagonal, or the x = −T jump — produces the drift
of §1.2. If the drift is the jump, the edge term is a boundary form in the Poisson values u(Nλ) and can be treated as a
finite-dimensional trace; if it is the off-diagonal, prove the layer version of Theorem 3.3.

## Reproducibility
SAVE=<f.npz> TOP=<K> TOPS=<list> FASTMUL=1 python3 tools/prolate_tailgram.py T Nb 30 KMAX 12; then
python3 tools/tailgram_quotient.py <f.npz> <K list>. Runs: (0.8, 300, 120; TOP 96), (1.0, 370, 148; TOP 116),
(1.0, 300, 120; TOP 104). Edge-kernel test: ratio Ĝ_jk/(v_jv_k), v = (column f(λ) of the constraint matrix)/√d, inline
script (same npz). Each run ≤ 15 min, one core.
