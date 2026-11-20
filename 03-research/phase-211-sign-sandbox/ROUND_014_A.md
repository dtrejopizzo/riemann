# Round 14 A — The class-blind tail Gram 𝒢 on the high block: exact transfer, band profile, and why the index-axis sweep does not reduce to the packet margin

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_012_B: ψ_k even prolates of [−λ, λ], c = 2πN, d_k = 1 − χ_k,
ε_k = i^k, S = diag(ε_k) (real, ±1, S² = I), u_k the out-of-band part of √χ_kφ_k, 𝒯 the tail map, 𝒢_{jk} = 𝒲(𝒯u_j, 𝒯u_k),
M_{jk} = W_T(Eψ_j, Eψ_k) (the unrestricted Gram of the numerator), D = diag(d_k), ℓ_g the gauge-minimised leakage
(tools/prolate_gauge_adm.py), 𝒜 ⊂ ℝ^K the admissible coefficient space (f(λ) = f(0) = ∫f = A(Ef) = B(Ef) = 0).
m(τ) = Re ψ(¼ + iτ/2) − log π, P^ρ_T as in ROUND_011_A; (U) = the pointwise packet margin of ROUND_012_A.
High block H = {k even, 4N < k ≤ K}. Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Index rows read: P211-9B, P211-10A, P211-11A (packet reduction, Prop 1.2), P211-11B (two-block Schur NO-GO), P211-11C
(packet margin, finite reduction), P211-12A (certified (U) ranges, operator form A_τ), P211-12B (M = S𝒢S, three-block
NO-GO, "next: banded sweep in b = Sa"), P211-13A (summation methods on P^ρ_T closed). Ledger C24–C30.
What differs. The block Schur assemblies of 11B/12B cut the high range into two or three blocks and fail by one coupling.
This memo works on the whole high block in the class-blind variable b = Sa, which 12B names but does not execute, and tests
two things not on record: (i) whether 𝒢 is banded/Toeplitz-like along the index axis with a symbol that can be compared
with the packet margin, (ii) whether a Gershgorin / banded-Gårding sweep gives a K-uniform bound. No indexed route is
retried; no summation method on P^ρ_T is used (13A). Not a sign step except where the falsifier test says so (§5).

## 1. The exact transfer to the class-blind variable (pure mathematics)

### 1.0 Domain of the tail form (PROVED)
For even ψ on [−λ, λ], ℱ(ψ1_{[−λ,λ]})(ξ) = ψ(λ)sin(2πλξ)/(πξ) + O(ξ^{−2}) (one integration by parts). By (S) of ROUND_012_B,
ε_ku_k(ξ) = ℱ(ψ_k1)(ξ) on |ξ| > λ, so u_k(ξ) = ε_kψ_k(λ)sin(2πλξ)/(πξ) + O(ξ^{−2}) (ε_k = ±1 is its own inverse).
Hence a single u_k is O(1/ξ) whenever ψ_k(λ) ≠ 0, the Poisson series defining 𝒯u_k is not absolutely convergent, and the
entrywise matrix 𝒢_{jk} = 𝒲(𝒯u_j, 𝒯u_k) is **not defined on raw prolates**. For a finite vector b,
Σ_k b_ku_k = O(ξ^{−2}) ⟺ Σ_k b_kε_kψ_k(λ) = 0 ⟺ (Sb) satisfies f(λ) = 0. So the natural domain of the tail form is
class-dependent: 𝒟 = S{f(λ) = 0}, and every statement below is made on a subspace of 𝒟, never entrywise.
(The other two Poisson conditions, f(0) = ℱf(0) = 0, are needed for the boundary terms in Φ_f, (T) of 12B; they too are
imposed on a = Sb, not on b.)

### Theorem 1.1 (exact transfer; PROVED given ROUND_012_B Thm 1.1)
Let 𝒜 be the admissible coefficient space (any finite index set) and 𝒜^S := S𝒜. For b ∈ 𝒜^S put
𝒢[b] := 𝒲[𝒯(Σ_k b_ku_k)] (well defined, b ∈ 𝒜^S ⊂ 𝒟). Then for every a ∈ 𝒜, M[a] = 𝒢[Sa], and
  (i)  M ⪰ 0 on 𝒜 ⟺ 𝒢 ⪰ 0 on 𝒜^S;
  (ii) inf_{a∈𝒜} M[a]/D[a] = inf_{b∈𝒜^S} 𝒢[b]/D[b]   (SDS = D);
  (iii) inf_{a∈𝒜} M[a]/ℓ_g[a] = inf_{b∈𝒜^S} 𝒢[b]/ℓ_g^S[b], ℓ_g^S := Sℓ_gS = D − (SDJ)H^{−1}(SDJ)ᵀ
       (H = I − Σ_kχ_kJ_kJ_kᵀ is unchanged by S since it is a sum over k of rank-one terms in the k-th row of J).
*Proof.* 12B Thm 1.1 with f = g gives M[a] = Σa_ja_kε_jε_k𝒲(𝒯u_j,𝒯u_k) read as 𝒲[𝒯(Σ_k(ε_ka_k)u_k)] — the sum
Σ(ε_ka_k)u_k = ℱf off the band is O(ξ^{−2}) because f(λ) = 0, so no entrywise term is used. S is a bijection 𝒜 → 𝒜^S;
substitute b = Sa. (ii)–(iii): D and H are diagonal-in-k sums, S² = I. ∎

### Proposition 1.2 (the constraint space is not S-invariant; PROVED in form, NUMERICAL in size)
In the coefficient a the five constraint vectors are ℓ_λ = (ψ_k(λ)), ℓ_0 = (ψ_k(0)), ℓ_∫ = (ε_k√χ_kψ_k(0)) (since
φ_k(0) = ψ_k(0)), ℓ_A = (A(Eψ_k)), ℓ_B = (B(Eψ_k)). 𝒜^S = 𝒜 iff span{ℓ_•} is S-invariant. On the high block χ_k → 0,
so ℓ_∫ ≈ 0 and Sℓ_∫ ≈ 0, while Sℓ_0 = (ε_kψ_k(0)) is the alternating companion of ℓ_0; nothing forces it into the span.
NUMERICAL (high block 4N < k ≤ K): cosines of the principal angles between span{ℓ_•} and S·span{ℓ_•} are
(0.999, 0.999, 0.908, 0.228, 0.135) at T = 0.8, K = 80 and (0.999, 0.998, 0.904, 0.778, 0.729) at T = 1.0, K = 100.
So "M ⪰ 0 ⟺ 𝒢 ⪰ 0 on the constraint-compatible subspace" is exact only with the subspace 𝒜^S = S𝒜, which differs from 𝒜
by two to three directions; the gauge enters as ℓ_g^S, with the class-mixed overlaps SDJ.

### Corollary 1.3 (one-sided transfer; PROVED)
If 𝒢 ⪰ κD on some subspace X ⊂ 𝒟 with X ⊇ 𝒜^S and κ ≥ 0, then M ⪰ κD ⪰ κℓ_g on 𝒜 (ℓ_g ≤ D because
DJH^{−1}JᵀD ⪰ 0 when H ≻ 0; λ_min(H) = 0.24 in all runs). So a D-coercive bound for 𝒢 on any S-invariant enlargement of
𝒜^S inside 𝒟 (e.g. S{f(λ) = 0}) would suffice, and is K-uniform if κ is. §2 shows that such a bound is false.

## 2. Measurements (NUMERICAL)

Tool: tools/prolate_tailgram.py (same build and caches as prolate_gauge_3blk.py; dps 30; MIN = 12, gauge rank 10).
Ĝ := D^{−1/2}SMSD^{−1/2} on the high indices. Caveat (§1.0): on raw prolates SMS is NOT the tail Gram 𝒢 (𝒢 is not
defined entrywise); SMS agrees with the tail form only after restriction to 𝒜^S. The band profile below is therefore the
profile of the unrestricted numerator in the b-variable, reported because a sweep must act on some explicit matrix; the
coercivity numbers (constrained columns) are the legitimate ones (Theorem 1.1(ii)–(iii)).

### 2.1 Band profile of Ĝ (T = 0.8, k = 20..80; T = 1.0, k = 30..100). Offset q means |j − k| = 2q.
| T | diag range | q=1 mean (signed) | q=2 | q=3 | q=4 | q=5 | q=6 | q=7 | q=8 |
|---|---|---|---|---|---|---|---|---|---|
| 0.8 | 1.96 → 3.06 (increasing) | −0.94 | −0.26 | +0.10 | −0.37 | +0.28 | −0.33 | +0.29 | −0.26 |
| 1.0 | 2.71 → 4.19 (increasing) | −1.17 | −0.36 | +0.15 | −0.55 | +0.37 | −0.49 | +0.36 | −0.38 |
Readings. (a) The nearest-neighbour bond in b is negative and almost constant (−0.89…−0.90; −1.10…−1.12 in the bulk),
≈ 0.35–0.45 of the diagonal: in the a-variable it is +0.94 / +1.17, the H₊–H₋ coupling of 12B Cor 1.2.
(b) **The band does not decay**: from q = 4 on, the entries alternate (−1)^q with modulus 0.26–0.55, i.e. in the a-variable
they have the constant sign − and size ≈ 0.3–0.5 at every range — a smooth, long-range, low-rank-looking component.
(c) The diagonal is m-like but carries no comb imprint: at T = 0.8, Ĝ_kk − m(πk/2) = 0.41, 0.18, 0.11, 0.10, 0.15, 0.17,
0.21, 0.08, 0.06, 0.10, 0.07 (k = 20, 26, …, 80), smooth in k; m − P^ρ_T at the same points oscillates by ±0.3 and fits
worse. At T = 1.0 the same offset is 0.69–0.94, so τ_k = πk/2 is not a T-independent law; no clean τ_k with
Ĝ_kk = m(τ_k) − P^ρ_T(τ_k) + small was found.
(d) Gershgorin: min_k(Ĝ_kk − Σ_{j≠k}|Ĝ_jk|) = −5.69 (T = 0.8), −8.44 (T = 1.0). Banded truncation at half-width w
(entries |j−k| ≤ 2w kept): λ_min(banded) = 0.38/0.11/0.22 (w = 1/2/3) at T = 0.8 and 0.87/0.46/0.54 at T = 1.0, but the
remainder has operator norm 4.6/3.9/3.6 and 6.2/5.3/4.9. Toeplitz fit (σ̂(q) = mean of the q-th diagonal): symbol min
−0.76 (θ ≈ π, T = 0.8), −0.16 (θ ≈ 0.17, T = 1.0); ‖Ĝ − Toeplitz‖_op = 1.62 / 2.27.

### 2.2 Bottom of the form in the b-variable, sweep in K (constrained = on 𝒜^S)
| T | K | dim | D-bottom on 𝒜^S | ℓ_g^S-bottom on 𝒜^S | D-bottom on 𝒜^S ∩ (SDJ)^⊥ (dim) |
|---|---|---|---|---|---|
| 0.8 | 56 | 19 | 0.980 | 1.066 | 2.63 (4) |
| 0.8 | 64 | 23 | 0.415 | 0.986 | 2.00 (8) |
| 0.8 | 72 | 27 | 0.087 | 0.857 | 1.80 (12) |
| 0.8 | 80 | 31 | 0.0148 | 0.814 | 1.76 (16) |
| 1.0 | 68 | 20 | 1.365 | 1.447 | 3.08 (5) |
| 1.0 | 76 | 24 | 1.093 | 1.247 | 2.75 (9) |
| 1.0 | 84 | 28 | 0.878 | 1.145 | 2.56 (13) |
| 1.0 | 92 | 32 | 0.552 | 1.037 | 2.40 (17) |
| 1.0 | 100 | 36 | 0.243 | 0.978 | 2.27 (21) |
(ℓ_g^S-bottoms reproduce α_HI of 12B: 0.81 at T = 0.8, K = 80; 0.98 at T = 1.0, K = 100 — consistency check of Thm 1.1.)
Readings. (e) In D-normalisation the high block is **not** K-uniformly coercive: the D-bottom on 𝒜^S falls 0.98 → 0.015
(T = 0.8) and 1.37 → 0.24 (T = 1.0). (f) The D-bottom vector lies in the gauge span: |P_{SDJ}b| = 0.998 (T = 0.8),
0.985 (T = 1.0); it is smooth in b (one sign change near the middle of the range, amplitude ≤ 0.33): the near-null of 𝒢
is the low end of the index-axis symbol, θ ≈ 0, and it is the gauge, not the comb. (g) Orthogonal to the gauge span the
D-bottom is 1.76 / 2.27 at the top K, still drifting down (2.63 → 1.76; 3.08 → 2.27) with very small complements
(dim 4–21), so no K-uniform constant is shown there either. (h) Packet margins at the same T (11C, ind profile): 1.04
(T = 0.8), 0.87 (T = 1.0). The ℓ_g^S-bottom is below the margin at T = 0.8 (0.81 < 1.04) and above it at T = 1.0.

## 3. The sweep theorem and why it does not reduce coercivity to (U)

### Theorem 3.1 (banded Gårding / Toeplitz sweep; PROVED, linear algebra)
Let X be a finite-dimensional subspace of ℝ^H, G a symmetric matrix, D > 0 diagonal, Ĝ = D^{−1/2}GD^{−1/2}. Write
Ĝ = 𝒯_σ + E with 𝒯_σ the Toeplitz matrix of an absolutely summable even sequence σ̂ (symbol σ(θ) = Σσ̂(q)e^{iqθ}). Then
for every b ∈ D^{1/2}X,
    bᵀĜb ≥ (min_θ σ(θ) − ‖P_XEP_X‖)·|b|²,
and with the w-band split Ĝ = Δ + B_w + R_w, bᵀĜb ≥ (min_k(Δ_kk − Σ_{0<|j−k|≤2w}|Ĝ_jk|) − ‖R_w‖)|b|².
*Proof.* bᵀ𝒯_σb = (1/2π)∫σ(θ)|Σ_kb_ke^{ikθ}|²dθ ≥ min σ·|b|² (Parseval); bᵀEb ≥ −‖P_XEP_X‖|b|². The banded form is
Gershgorin on Δ + B_w plus the operator bound on R_w. ∎
Applied with G = 𝒢 on X = 𝒜^S this would reduce high-block coercivity in D-units to min σ ≥ κ plus ‖E‖ < κ, a K-uniform
statement if σ and E are K-uniform. For that to be the pointwise margin (U) one needs σ(θ) ≈ m(τ) − P^ρ_T(τ) under some
correspondence θ ↔ τ and ‖E‖ small.

### Proposition 3.2 (NO-GO for the index-axis reduction to (U); NUMERICAL, class stated)
Class: lower bounds for 𝒢 on 𝒜^S (equivalently M on 𝒜) obtained from a symbol along the prolate index axis plus a band or
Toeplitz error, in D-normalisation (Theorem 3.1 and every diagonal-dominance / banded-Gårding variant).
Failure, measured: (i) the D-bottom on 𝒜^S tends to 0 with K (0.015 at T = 0.8, K = 80) while min(m − P^ρ_T) ≈ 1.0; any
bound of Theorem 3.1 type with κ = margin − error > 0 is false, whatever the error term. (ii) The near-null direction is the
gauge (|P_{SDJ}b| ≥ 0.985), which is comb-blind (§4), so the index-axis symbol near θ = 0 is not m − P^ρ_T at any τ.
(iii) The band does not decay (|Ĝ_{k,k+2q}| ≈ 0.3–0.55 for q = 4…8), Gershgorin defects −5.7/−8.4, Toeplitz remainder
1.6/2.3 > all diagonal margins. So the requested reduction "high-block coercivity ⟸ (U) + explicit band error" does not
exist in D-units. What the data allow is only the gauge-quotient form (Theorem 1.1(iii)), whose bottom is the α_HI of
11B/12B (0.81 / 0.98, slowly decreasing in K), already on record.
Why the packet identification fails (ARGUED): for k above the plunge, u_k is not a packet of width ≍ 1/T at a centre τ_k;
its profile is a spherical-Bessel-type function of 2πλξ, so 𝒯u_k(x) = e^{−x/2}Σ_nu_k(ne^{−x}) is a chirp in x < −T with
instantaneous frequency √((2πλne^{−x})² − k²)-type, sweeping from the turning point to ∞. The diagonal 𝒲[𝒯u_k] therefore
averages m along a chirp (consistent with (c): m-like, smooth, no comb oscillation), and neighbouring tails overlap along
the whole chirp — hence the constant bond −0.9/−1.1 and the non-decaying band, instead of the O(1/T)-cell overlaps of
packets. The packet picture of 11A (Prop 1.2) gives only the necessity of (U) for coercive (HR)(a), not sufficiency.

## 4. Falsifier test
Theorem 1.1, Prop 1.2, Cor 1.3, Thm 3.1 are identities / linear algebra, not sign steps; Theorem 1.1 uses Λ through
(T) of 12B and fails for (a)–(d) (12B §3). Proposition 3.2 is a NO-GO, not a sign step.
NUMERICAL (T = 0.8, Nb = 250, K = 80): under 1.01Λ every number of §2 moves by ≤ 1% (D-bottom 0.0147, ℓ_g-bottom 0.815,
gauge-orth 1.75, bond −0.937); under a_3 (prime 2 deleted) the D-bottom is 0.0147 (identical), ℓ_g-bottom 0.614,
gauge-orth 2.45, bond −1.25. So the D-collapse of (e) and the gauge alignment of (f) are comb-blind (survive (a), (b)),
confirming that the index-axis symbol near θ = 0 carries no arithmetic; and the high block as a whole again does not
separate Λ from its falsifiers (a_3 is rejected only in LM, 12B §3). Any argument that proved (★) from the high-block
numbers of this memo would survive (a) and (b) — it would be wrong; the sign must come from LM and its coupling.

## Result
NO-GO with class (Proposition 3.2: index-axis symbol + band/Toeplitz error bounds for the high block in D-normalisation;
NUMERICAL), plus PROVED pieces: Theorem 1.1 (exact transfer on 𝒜^S = S𝒜, with the tail form defined only there — the
entrywise 𝒢 is undefined on raw prolates, §1.0), Proposition 1.2 (constraint span not S-invariant, explicit), Corollary 1.3,
Theorem 3.1 (sweep lemma).

### What was proved
- §1.0: u_k = ε_kψ_k(λ)sin(2πλξ)/(πξ) + O(ξ^{−2}); the tail form's domain is S{f(λ) = 0}, class-dependent.
- Theorem 1.1: M ⪰ 0 on 𝒜 ⟺ 𝒢 ⪰ 0 on S𝒜; generalized minima transfer exactly with D and with ℓ_g^S = Sℓ_gS.
- Proposition 1.2: S𝒜 ≠ 𝒜 (alternating companion of ℓ_0; principal-angle cosines down to 0.135 / 0.729).
- Corollary 1.3: D-coercivity of 𝒢 on any enlargement of S𝒜 transfers to M (and to ℓ_g).
- Theorem 3.1: Toeplitz/banded sweep bound with explicit error.

### What failed and why
- Reduction of high-block coercivity to (U) through the index-axis symbol: the D-bottom on S𝒜 → 0 with K (0.98 → 0.015,
  1.37 → 0.24), carried by the gauge directions (comb-blind); band non-decaying (≈ 0.3–0.55 at offsets 8–16); Gershgorin
  −5.7/−8.4; Toeplitz error 1.6/2.3. Tails above the plunge are chirps, not packets (ARGUED), so the packet margin is not
  the index-axis symbol.

### Next concrete step
Quotient the gauge exactly before any sweep: work on 𝒜^S ∩ (SDJ)^⊥ (or in the ℓ_g^S metric) and measure whether the
long-range constant-sign component of (b) is the finite-rank radical correction (SMS − 𝒢 off 𝒜^S); if so, the remaining
operator should be compared with the archimedean chirp average ∫m(τ(x))|𝒯u|² rather than with packets. Mollified data
(ROUND_009_A V_d) are needed to make 𝒢 entrywise defined before any band statement about 𝒢 itself.

## Reproducibility
TOP=<K> TOPS=<list> [SAVE=<file.npz>] FASTMUL=1 python3 tools/prolate_tailgram.py T Nb 30 KMAX 12 [w]; runs (0.8, 250, 100;
K = 80) and (1.0, 370, 148; K = 100), w ∈ {L, 1.01, a3} at T = 0.8. Each run ≤ 900 s, one core.
