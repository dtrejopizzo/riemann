# Round 18 A — Transport defect on the measured bottom vectors, and the R-cell complete form against the gauge-quotient leakage

Target (★): λ_A(T) ≥ 0 for every T. Notation of ROUND_016_B (F₁, 𝔇, first Poisson cell, transported functionals, ℓ_g,
D-units) and ROUND_017_C (𝒬, μ₀, μ₄, Lemmas 2.1–2.4, certification protocol). λ = e^T, L = log 2.
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check
Index rows read: P211-16B (dilation form F_N = N^{−1/2}τ_{log N}F₁; idealised R-cell problems; with the polar term the
R ≥ 3 problem is near-null in D-units; admissible near-gauge probes 1.28–1.44 in ℓ_g-units; (HR_g) OPEN), P211-17C
(first-cell certificates μ₀ ≥ 0.0696, μ₄(0.8) ≥ 0.5276, μ₄(1.0) ≥ 0.5494; "next: multi-cell compressed form with the gauge
closure as constraint family; transport defect"); ledger C34, C37. Phase 199: PROOF_L_SHARP_X_001 Theorem B (single-cell
chirp data) and PROOF_L_SHARP_Y_001 Theorem B′ (multi-cell Langer chirps, asymptotic in c, no gauge).
What differs. Nothing indexed is retried. (i) The defect measurement (§1) is the step 17C names as next; it is done on
the actual bottom vectors of 16B, not on idealised data. (ii) The R-cell problem of §2 is the idealised problem of 16B §3.1,
but measured in the gauge-quotient metric ℓ_g with the gauge closure built in (16B measured it in D-units, where it is
near-null, and tested ℓ_g only on three hand-made probes); the multi-cell Theorem B′ of phase 199 is asymptotic in c,
gauge-free and for Langer chirps, while here the form is the exact Lévy form plus comb plus polar term on arbitrary
F₁ ∈ L²(window), at fixed T. (iii) The certificate tool of 17C is extended (§3) by a piecewise-polynomial compression in
which 𝔇 and the comb shifts are exact.

## 1. The transport defect on the measured bottom vectors (NUMERICAL, plus one PROVED transfer lemma)

### 1.1 What is measured
For each bottom vector b of the constrained gauge quotient X of 15A/16B (T = 0.8: K = 56 … 96, Nb = 300, the vectors of
16B §1.3; T = 1.0: K = 68 … 100, Nb = 370, MIN = 12, recomputed for this round with the same tools), u = Σ b_k u_k is the
direct tail (Legendre–spherical-Bessel closed form, ξ ≤ 200) and F₁ = e^{−x/2}u(e^{−x}). The first-cell model of 17C
replaces (a) the whole tail by its first-cell part F₁^c := F₁·1_{(λ, 2λ)}(e^{−x}), (b) the exact admissibility conditions on f
(f(0) = f(λ) = ∫f = A(Ef) = B(Ef) = 0, satisfied by b to ≤ 1.2·10⁻³) by the four transported functionals on F₁^c, (c) the
complete tail form 𝒲[𝒯u] + 2A(𝒯u)B(𝒯u) by 𝒬[F₁^c]. The defect is measured in four numbers: in-band mass of ℱf; tail mass
beyond 2λ; value defect (exact form − 𝒬[F₁^c])/‖F₁‖²; constraint defect δ := dist(F₁^c, V)/‖F₁^c‖, V the codimension-4
space of 17C Theorem 3.3 (δ² = cᵀG_w^{−1}c, c_i = ⟨F₁^c, w_i⟩, G_w the Gram of the four weights on the cell).
Normalisation: Rayleigh quotients are per ‖F₁‖² = ½‖u‖² (so the D-unit is (λ/2)×, 16B §1.2). Tool: scratch scripts
defect.py / defect10.py built on tools/tail_direct/tail.py (ledger, polar), N ≤ 60 chirps.

| T | K | in-band mass of ℱf | tail mass beyond 2λ | exact form / ‖F₁‖² | 𝒬[F₁^c]/‖F₁^c‖² | value defect / ‖F₁‖² | δ | cosines of F₁^c with (f(0), f(λ), A, B) |
|---|---|---|---|---|---|---|---|---|
| 0.8 | 56 | < 10⁻⁴ | 0.443 | 2.373 | 2.028 | +1.243 | 0.359 | 0.004, −0.20, −0.30, −0.25 |
| 0.8 | 64 | < 10⁻⁴ | 0.029 | 1.800 | 1.774 | +0.077 | 0.156 | −0.002, −0.13, 0.06, 0.03 |
| 0.8 | 72 | < 10⁻⁴ | 0.035 | 1.623 | 1.614 | +0.066 | 0.069 | 0.003, 0.03, −0.06, −0.04 |
| 0.8 | 80 | < 10⁻⁴ | 0.184 | 1.589 | 1.494 | +0.371 | 0.048 | −0.007, 0.03, 0.03, 0.02 |
| 0.8 | 88 | < 10⁻⁴ | 0.050 | 1.472 | 1.426 | +0.118 | 0.076 | 0.001, −0.07, 0.01, 0.003 |
| 0.8 | 96* | < 10⁻⁴ | 0.350 | 1.287 | 1.372 | +0.396 | 0.184 | −0.02, −0.13, 0.10, 0.05 |
| 1.0 | 68 | < 10⁻⁴ | 0.026 | 2.269 | 2.229 | +0.099 | 0.156 | −0.0004, −0.11, 0.08, 0.05 |
| 1.0 | 76 | < 10⁻⁴ | 0.011 | 2.022 | 2.005 | +0.039 | 0.093 | 0.001, −0.07, 0.04, 0.02 |
| 1.0 | 84 | < 10⁻⁴ | 0.005 | 1.886 | 1.877 | +0.018 | 0.040 | 0.0007, −0.04, 0.01, 0.01 |
| 1.0 | 92 | < 10⁻⁴ | 0.008 | 1.764 | 1.750 | +0.028 | 0.073 | 0.001, 0.05, −0.04, −0.02 |
| 1.0 | 100 | < 10⁻⁴ | 0.006 | 1.680 | 1.655 | +0.034 | 0.028 | 0.0004, 0.02, −0.01, −0.009 |
(* past the Galerkin cap, 15A; kept for completeness. The polar part 2A(𝒯u)B(𝒯u) is ≤ 10⁻⁶ on every row. Calibration of the
recomputed T = 1.0 vectors: Galerkin D-unit / direct 𝒲 = 2.718 = λ to 0.1 % on K ≤ 92, as in 16B §1.2 at T = 0.8.)

Readings.
(a) **The in-band part is negligible** (< 10⁻⁴ of ‖f‖²) on every high-block bottom vector: defect source (i) of 17C §4(ii)(a)
is absent in practice.
(b) **The value defect is always positive**: the exact form exceeds the first-cell model by 0.02–0.12 per ‖F₁‖² on the
resolved rows (more where tail mass leaves the first cell: 0.37 at T = 0.8, K = 80, 18 % beyond 2λ). The second and later
cells and the first-cell/rest cross terms add, on these vectors, a nonnegative amount. So the first-cell model is a lower
model for the measured bottoms, and the measured Rayleigh quotients (1.47–1.80 at T = 0.8; 1.68–2.27 at T = 1.0, per ‖F₁‖²)
sit far above μ₄ (0.528 / 0.549): the bottom vectors are not near the 17C extremal.
(c) **The constraint defect is not small**: f(0) transports to 10⁻³ (cosine ≤ 0.007), but f(λ), A, B transport only to
cosines 0.01–0.13, and δ = 0.03–0.16. The reason is the support of the weights: the transported f(λ), A, B are oscillatory
functionals that see the tail beyond 2λ and the cut at 2λ, which the first-cell truncation discards.
(d) f(0) is the one constraint that transports essentially exactly (its weight 2e^{−x/2} is smooth and nonoscillatory, and
the tail beyond 2λ carries little mass): the T-free bound μ₀ of 17C Theorem 3.1 applies to F₁^c up to a cosine ≤ 0.007.

### Lemma 1.1 (transfer of a codimension-k bound to nearly-constrained data; PROVED)
Let 𝒬 be a closed quadratic form on L²(I) with 𝒬 ≥ −β (β ≥ 0), V = {⟨F, w_i⟩ = 0, i ≤ k}, 𝒬 ≥ μ on V, and
q_W := sup{(𝒬 + β)[G] : G ∈ span{w_i}, ‖G‖ = 1} < ∞. If dist(F, V) = δ‖F‖, then
    𝒬[F] ≥ ([(μ + β)(1 − δ²)]^{1/2} − q_W^{1/2}δ)₊²·‖F‖² − β‖F‖².
*Proof.* V^⊥ = span{w_i}; F = F_V + F_W with ‖F_W‖ = δ‖F‖, ‖F_V‖² = (1 − δ²)‖F‖². 𝒬 + β is a nonnegative closed form,
so its square root is a seminorm and the triangle inequality gives (𝒬 + β)[F]^{1/2} ≥ (𝒬 + β)[F_V]^{1/2} − (𝒬 + β)[F_W]^{1/2}
≥ ((μ + β)(1 − δ²))^{1/2}‖F‖ − q_W^{1/2}δ‖F‖ when the right side is ≥ 0. ∎
On the first cell, β = −(C_0 + ∫_L^∞K) = 2.3784 is rigorous (17C §1.1: the Lévy part is ≥ 0); q_W = 4.397 (T = 0.8), 4.754
(T = 1.0) (NUMERICAL, sine Galerkin Nb = 96, weights captured to 99.3–99.9 %). With μ = μ₄ the bound is positive iff
δ < δ* = 0.0752 (both T). With the numerical unconstrained bottom β = 1.2873 instead: δ* = 0.112 (NUMERICAL).
Reading. On the resolved rows δ is below δ* = 0.075 at T = 0.8, K = 72, 80 and T = 1.0, K = 84, 92, 100, and above it
elsewhere (0.156 at K = 64 / 68). So **the certified first-cell constant transfers to the measured bottom vectors only on
part of the rows**, and where it does, it transfers with a large loss (at δ = 0.07 the guaranteed value is ≈ 0.04, against
μ₄ = 0.53 and the measured 1.6). Lemma 1.1 is the honest tool, but the constraint defect (c) is the obstruction to using
the 17C constant on actual data; the fix is not a better transfer lemma but exact constraints, which in the R-cell
problem below are imposed on the full multi-cell F₁ (no first-cell truncation of the weights).

## 2. The R-cell complete form against ℓ_g (NUMERICAL)

### 2.1 The object (definitions; PROVED bookkeeping)
Window I_R = (−T − log R, −T) (centred variable y ∈ [0, log R]); F ∈ L²(I_R) is F₁ of a tail u supported in λ < ξ < Rλ
(the first R − 1 Poisson cells). By 16B Lemma 2.1, 𝒯u = 𝔇_R F := Σ_{N<R} N^{−1/2}F(· − log N)·1_{I_R}, and the complete
tail form is
    Q_R[F] := 𝒲[𝔇_R F] + 2A(𝔇_R F)B(𝔇_R F),   𝒲 = 𝒬 − c·Π,  Π[H] = Σ_{2≤m<R} 2Λ(m)m^{−1/2}⟨τ_{log m}H, H⟩,
with c = 1 for Λ (c ≠ 1 is falsifier (a)); A(H) = ∫H e^{x/2}, B(H) = ∫H e^{−x/2}. The comb enters twice: through 𝔇_R (weights
N^{−1/2} at the resonant shifts log N, 15A Theorem 3.1 / 16B Lemma 2.1) and through Π on the window. Constraints: the four
transported functionals of 17C §1.2 applied to the whole F (all cells, not only the first), V_R := {⟨F, w_i⟩ = 0, i ≤ 4}.
Gauge-quotient leakage: ℓ_g[F] := dist²_{L²(λ,∞)}(u, closure of the tails of gauge functions), u = ξ^{−1/2}F(−log ξ);
for any finite gauge family {g_j}, ℓ_g^{fam}[F] := ‖F‖² − cᵀG^{−1}c (c_j = ⟨u, ĝ_j⟩_{L²(λ,∞)} = ⟨F, ξ^{1/2}ĝ_j⟩, G the
Gram of ĝ_j on (λ, ∞)) satisfies ℓ_g ≤ ℓ_g^{fam} ≤ ‖F‖² (a larger subspace is closer). Gauge families used: the smooth
family (1 − λ²y²)³(λy)²P_{2i}(λy) with ∫ = 0 (that of 16B §3.2, J − 1 functions) and the Legendre family P_{2l}(λy)1_{|y|<1/λ}
(l < J, closed-form tails (2/λ)(−1)^l j_{2l}(2πξ/λ)); the gauge closure is the same for both (all of L²(|y| < 1/λ) in the
tail metric). The quantity measured is
    κ_R(T) := inf{Q_R[F]/ℓ_g[F] : F ∈ V_R},
and its D-unit companion inf Q_R/‖F‖² on V_R. (HR_g) restricted to R-cell data would say κ_R(T) ≥ κ_T > 0 for all R.
Tools: sine Galerkin in F (Nb), 𝔇_R, polar and constraint vectors by quadrature, generalised eigenproblem on V_R; double
precision (scratch cellRg.py) and mpmath at 50–200 digits (cellRg_mp.py, with exact Gauss–Legendre nodes); and an
independent piecewise-Legendre float tool for R = 3 (pw3.py) in which 𝔇_3 and the comb shift are exact matrices.
Galerkin in F gives upper bounds for the infimum over F; enlarging the gauge family (J) can only raise the ratio.

### 2.2 Results (NUMERICAL; T = 0.8 unless stated; best resolved values; Nb = Galerkin size, J = gauge rank)
| R | inf Q_R/‖F‖² on V_R | inf ℓ_g^{fam}/‖F‖² on V_R | κ_R = inf Q_R/ℓ_g^{fam} | (λ/2)κ_R | stability |
|---|---|---|---|---|---|
| 2 | 0.547 | 0.52–0.57 | 0.81–0.85 | 0.90–0.95 | Nb 40–48, J 20–30 |
| 3 | 1.5·10⁻³ | 1.1·10⁻³ | 0.737–0.758 (pw3: 0.859) | 0.82–0.84 | Nb 40/48/64, J 20/30/45 agree to 0.02 |
| 4 | 6.5·10⁻⁶ | 3.8·10⁻⁶ | 0.674–0.683 | 0.75–0.76 | Nb 40/48/56/64, J 20–45 |
| 5 | 3–6·10⁻⁹ | 1.0·10⁻⁸ | 0.107–0.171 | 0.12–0.19 | **Nb-dependent** (0.168 / 0.109 / 0.107 at Nb = 40/48/56); J 20→80: +0.003 |
| 6 | 2·10⁻¹² | 1.4·10⁻¹² | 0.088–0.106 | 0.10–0.12 | J 20→80: 0.103→0.106 |
| 7 | 10⁻¹⁶ | 3·10⁻¹⁵ | 5·10⁻⁵–8·10⁻⁵ | ≤ 10⁻⁴ | J 20/40/60/80: 9·10⁻⁷, 8·10⁻⁵, 5·10⁻⁵, 8·10⁻⁵ |
| 8 | 8·10⁻²⁰ | 3·10⁻¹⁸–8·10⁻¹⁵ | 5·10⁻¹² (J = 20), 1.6·10⁻⁷ (J = 80) | ≤ 2·10⁻⁷ | — |
T = 1.0: R = 2: 0.858; R = 3: 0.690–0.742; R = 4: 0.073–0.109 (J 20–45); R = 5: 0.020; R = 6: 0.0023.
(Precision: the R ≥ 5 values are below double precision and were computed at 50–150 digits; the double-precision runs return
0 or negative there. The R = 3 pw3 value is higher than the sine value because the piecewise basis resolves the cut of 𝔇₃
exactly; both are upper bounds of the infimum within their bases, and the certificate of §3 is the lower bound.)
Readings.
(a) **R = 3, 4: the ratio to ℓ_g is O(1)** (≈ 0.7 at T = 0.8), although the form is near-null in D-units (1.5·10⁻³, 6·10⁻⁶).
This is the multi-cell confirmation of the 16B probes: every near-null direction of Q_R on V_R is near-gauge.
(b) **From R = 5 (T = 0.8) and R = 4 (T = 1.0) on, the ratio collapses**: κ_R decays super-exponentially in R (to 10⁻⁴ at
R = 7 and 10⁻¹¹ at R = 8, T = 0.8), and enlarging the gauge family (J up to 80) does not lift it. So on idealised R-cell
data **no constant c > 0 is seen as R grows**; (HR_g) restricted to the idealised class fails numerically at the rate shown.
(c) What the idealisation drops (ARGUED). The class of F₁ in 2.1 is all of L²(I_R) ∩ V_R; the actual class consists of
tails of f supported in [−λ, λ] (16B Lemma 2.1, item (ii)), i.e. u = ℱf|_{(λ,∞)} with ℱf entire of exponential type 2πλ.
The bottom functions of 2.2(b) are far from this class: they are built from the ~R near-null directions of Q_R (one per
added cell, cf. 16B §3.1 table) that the four constraints and a smooth gauge cannot remove, and nothing ties them to a
band-limited f. Hence (b) says only that **the R-cell problem with the transported constraints is the wrong limit problem
beyond R ≈ 4**: the band-limitation (type 2πλ) of ℱf has to enter as a constraint family of its own. This is OPEN.

## 3. Certification for R = 2 and R = 3

### Proposition 3.1 (R = 2; PROVED, from 17C)
For first-cell data (R = 2) the polar factor B(𝔇₂F) = B(F) = ∫F e^{−x/2} is a multiple of the transported f(0)-functional,
so Q₂ = 𝒬 on V₂, and by 17C Theorem 3.3 and ℓ_g ≤ ‖F‖²:
    Q₂[F] ≥ μ₄(T)‖F‖² ≥ μ₄(T)·ℓ_g[F]  on V₂,  κ₂(0.8) ≥ 0.52763,  κ₂(1.0) ≥ 0.54941.
(NUMERICAL: the true κ₂ is ≈ 0.81–0.85; the certificate does not use the gauge.) ∎

### Lemma 3.2 (piecewise compression in which 𝔇₃ and the comb are exact; PROVED)
Split [0, log 3] into I₀ = [0, log 3/2], I₁ = [log 3/2, log 2], I₂ = [log 2, log 3] and let P be the orthogonal projection onto
functions that are polynomials of degree < n on each piece. Then (i) 𝔇₃ = 1 + 2^{−1/2}S, where S maps F|_{I₀} to
F(· − log 2) on I₂ (a unitary I₀ → I₂ that preserves polynomial degree), so P𝔇₃ = 𝔇₃P; (ii) the only comb shift on a window of
length log 3 is m = 2 (m = 3 has empty overlap), ⟨τ_{log 2}H, H⟩ = ⟨SH|_{I₀}, H|_{I₂}⟩, so Π commutes with P and has no
p–r cross term; (iii) ‖𝔇₃‖² = 2 and σ_min(𝔇₃)² = ½ (singular values of [[1, 0], [2^{−1/2}, 1]]); (iv) Lemma 2.3(ii) of 17C
holds with P in place of the global polynomial projection, in the form
    ε := ‖(1 − P)G‖ ≤ log 3·(τ*/π)(M − C_0)(τ*ℓ_max/2)^n/n!,   ℓ_max = log 3/2,
(the Taylor remainder is taken piece by piece). *Proof.* (i)–(ii): supports; S sends the Legendre basis of I₀ to that of I₂
index by index. (iii): direct. (iv): the proof of 17C Lemma 2.3(ii) with dist(e^{iτ·}, ran P) ≤ (log 3)^{1/2}·max_p
sup_{I_p}|Taylor remainder at the centre of I_p| ≤ (log 3)^{1/2}(|τ|ℓ_max/2)^n/n!. ∎

### Lemma 3.3 (three-cell lower bound against a finite gauge family; PROVED)
Let κ > 0, M = m(τ*), G = P_I Op((M − m)1_{|τ|<τ*})P_I, v = 2log 2/√2, and on ran P put
    Φ_P := 𝔇₃ᵀ(M − PGP − cΠ)𝔇₃ + αβᵀ + βαᵀ − κ(1 − C_g X C_gᵀ),
α = P𝔇₃*e^{x/2}, β = P𝔇₃*e^{−x/2}, C_g = [P(ξ^{1/2}ĝ_j)]_j, X = G_gauge^{−1}. Let W = [Pw_1 … Pw_4] (transported constraints),
δ_k ≥ ‖(1 − P)w_k‖ for every analytic weight used, η := (Σ_{i≤4}δ_i²)^{1/2}‖(WᵀW)^{−1}‖^{1/2}, δ_g := (Σ_jδ_{g,j}²)^{1/2},
δ_α = √2δ_{e^{x/2}}, δ_β = √2δ_{e^{−x/2}}, and γ > 0 with Φ_P ⪰ γ on W^⊥ ∩ ran P. Put
    X_c := ‖Φ_P‖η + 2ε + ‖α‖δ_β + ‖β‖δ_α + κ‖X‖‖C_g‖δ_g,
    Y_c := (M − ε − |c|v)/2 − κ − γη² − ‖Φ_P‖η² − 2δ_αδ_β.
If Y_c > 0 and X_c² < γY_c, then Q₃[F] ≥ κ·ℓ_g^{fam}[F] ≥ κ·ℓ_g[F] for every F ∈ V₃.
*Proof.* F = p + r, p = PF, a = ‖p‖, b = ‖r‖. By Lemma 2.2 of 17C applied to H = 𝔇₃F, 𝒬[H] ≥ M‖H‖² − ⟨GH, H⟩. By Lemma
3.2(i)–(ii), 𝔇₃p ∈ ran P, 𝔇₃r ⊥ ran P, so ‖H‖² and Π[H] split with no cross term, and
⟨GH, H⟩ ≤ ⟨G𝔇₃p, 𝔇₃p⟩ + 2ε‖𝔇₃p‖‖𝔇₃r‖ + ε‖𝔇₃r‖², with ‖𝔇₃p‖‖𝔇₃r‖ ≤ 2ab. On the r-part,
M‖𝔇₃r‖² − ε‖𝔇₃r‖² − c·Π[𝔇₃r] ≥ (M − ε − |c|v)‖𝔇₃r‖² ≥ ½(M − ε − |c|v)b² (|Π[H]| ≤ v‖H‖², Lemma 3.2(iii), and
M − ε − |c|v > 0 is implied by Y_c > 0). Polar term: A(𝔇₃F) = ⟨p, α⟩ + ⟨𝔇₃r, (1 − P)e^{x/2}⟩ with the second term
≤ √2δ_{e^{x/2}}b; expanding 2AB gives 2⟨p,α⟩⟨p,β⟩ − 2(‖α‖δ_β + ‖β‖δ_α)ab − 2δ_αδ_βb². Gauge term: with c_F = C_gᵀp + e,
|e| ≤ δ_g b, and X ⪰ 0, c_FᵀXc_F ≥ pᵀC_gXC_gᵀp − 2‖X‖‖C_g‖δ_g ab. Leakage term: −κℓ_g^{fam} = −κ(a² + b²) + κc_FᵀXc_F.
Constraints: ⟨F, w_i⟩ = 0 gives Wᵀp = −(⟨r, (1 − P)w_i⟩)_i, hence p = p₁ + p_W with p₁ ⊥ ran W, ‖p_W‖ ≤ ηb (17C Lemma 2.4),
so pᵀΦ_Pp ≥ γ(a² − η²b²) − 2‖Φ_P‖ηab − ‖Φ_P‖η²b². Summing, Q₃[F] − κℓ_g^{fam}[F] ≥ γa² − 2X_cab + Y_cb² ≥ 0. Finally
ℓ_g ≤ ℓ_g^{fam}. ∎

### Theorem 3.4 (three-cell coercivity in the gauge-quotient metric; PROVED, computer-assisted, for the stated T)
Let T ∈ {0.8, 1.0}, I₃ a window of length log 3 at (−T − log 3, −T), and F ∈ L²(I₃) satisfying the four transported
constraints of 17C §1.2 (f(0), f(λ), A, B, applied to F on all of I₃). Then for the complete three-cell tail form
    Q₃[F] = (1/2π)∫m|(𝔇₃F)^|² − (2 log 2/√2)⟨τ_{log 2}𝔇₃F, 𝔇₃F⟩ + 2A(𝔇₃F)B(𝔇₃F)
(the Λ-comb on a window of length log 3: only m = 2) one has
    Q₃[F] ≥ κ·ℓ_g[F],  κ = 0.70 at T = 0.8,  κ = 0.70 at T = 1.0,
where ℓ_g is the squared distance in L²(λ, ∞) of u = ξ^{−1/2}F(−log ξ) to the tails of all gauge functions (any finite
Legendre family P_{2l}(λy)1_{|y|<1/λ}, l < 20, already suffices). In D-units (×λ/2): ≥ 0.779 (T = 0.8), ≥ 0.951 (T = 1.0).
Certificates (tools/multi_cell/cert3.py, 128-bit arb): τ* = 100, n = 70 per piece (N = 210), J = 20, Gauss–Legendre 40/panel
for the symbol and 160 (T = 0.8) / 320 (T = 1.0) nodes per piece for the weights, each with an analytic Bernstein-ellipse
radius added to every entry. T = 0.8: ε ≤ 7.3·10⁻⁷, η ≤ 8.3·10⁻⁷, δ_g ≤ 1.9·10⁻⁷, γ = 3.757·10⁻⁴ (LDLᵀ pivots ≥ 6.7·10⁻³),
X_c = 4.44·10⁻³, Y_c = 0.1935, X_c² = 2.0·10⁻⁵ < γY_c = 7.3·10⁻⁵. T = 1.0: ε ≤ 7.3·10⁻⁷, η ≤ 1.9·10⁻¹⁶, γ = 1.330·10⁻⁴,
X_c = 1.5·10⁻⁶, Y_c = 0.1935. Also certified: κ = 0.5 at T = 1.0. Not certified: κ = 0.8 at T = 0.8 (X_c² = 2.6·10⁻⁵ >
γY_c = 1.65·10⁻⁵ — the margin, not the form: the numerical κ₃ is 0.74–0.86).
*Proof.* Lemma 3.3 with the listed enclosures, verified in ball arithmetic; ℓ_g ≤ ℓ_g^{fam}. ∎
Remark. The certificate is a genuinely multi-cell statement: the form is 1.5·10⁻³-small per ‖F‖² on V₃, so no D-unit
bound of size ≥ 0.002 exists, and the gauge term C_gXC_gᵀ is what carries the constant.

## 4. The partial (HR_g) statement
### Theorem 4.1 (partial (HR_g); PROVED for the idealised data, CONDITIONAL for the high block)
(i) PROVED. For T ∈ {0.8, 1.0} and every F₁ supported in the first R − 1 Poisson cells (u supported in λ < ξ < Rλ) with the
four transported constraints imposed on the whole of F₁:
   R = 2: complete tail form ≥ μ₄(T)·ℓ_g, μ₄(0.8) ≥ 0.5276, μ₄(1.0) ≥ 0.5494 (Prop. 3.1);
   R = 3: complete tail form ≥ 0.70·ℓ_g at T = 0.8 and at T = 1.0 (Theorem 3.4).
(ii) CONDITIONAL. If a high-block vector b has its tail in λ < ξ < 3λ and its exact admissibility conditions coincide with the
transported ones, then 𝒢[b] = λ·Q₃[F₁] ≥ 0.70λ·ℓ_g^{(F₁)} = 0.35λ·ℓ_g^S[b] in the normalisation of 15A (ℓ_g^S = 2ℓ_g):
κ_T ≥ 0.779 (T = 0.8), ≥ 0.951 (T = 1.0) in ℓ_g-units, against the measured high-block bottoms 0.80–0.83 (T = 0.8, K = 88)
and 0.98 (T = 1.0, K = 100). The hypothesis fails on the measured vectors by the defect of §1: tail mass beyond 3λ is
≤ 10⁻² on the resolved rows, but the constraint defect δ is 0.03–0.16 (for the three-cell weights the same computation
applies; with Lemma 1.1 the transfer is lossy).
(iii) NUMERICAL, negative. For R ≥ 5 (T = 0.8) and R ≥ 4 (T = 1.0) the idealised ratio κ_R collapses (§2.2(b)); (HR_g) for the
idealised class with a constant independent of R is not true at the measured rate, and the missing ingredient is the
band-limitation of the data (§2.2(c)), OPEN.

## 5. Falsifier remark
The task expected the certified constant to survive c ≠ 1 (coercivity, not sign). Measured: it survives c = 0.9 (Theorem
3.4's protocol certifies κ = 0.70 at T = 0.8, c = 0.9: γ = 7.5·10⁻³) and **fails for c = 1.1**: inf Q₃/‖F‖² on V₃ = −0.0076
(sine, Nb = 40) / −0.0088 (pw3), κ_3 = −5.8 / −7.9; the certificate with c = 1.1 returns γ < 0 (−0.021). At R = 4, both
c = 0.9 and 1.1 give negative values (−0.008, −0.087). Reason (ARGUED): on V₃ the complete form has a near-null direction
(1.5·10⁻³ per ‖F‖²) that is a cancellation between the archimedean part and the comb (Π-part ≈ O(1) on it); a change of c
by 0.1 moves Q by O(0.1)·Π on that direction, which is two orders larger than the null value. So the multi-cell near-null
directions are where the comb enters at first order, and the R = 3 constant of Theorem 3.4 is *not* weight-blind for c > 1:
it fails falsifier (a) on one side only, as a sign-carrying inequality would. It is not claimed as a sign step: (b) a_P with
P = 3 deletes the only prime acting on a window of length log 3 (Π = 0, c = 0), which by the c = 0.9 trend raises the
form; (c), (d) not run. Recorded as: the first certified bound in this phase whose constant is destroyed by cΛ, c = 1.1.

## Result
PROVED piece (computer-assisted) + NUMERICAL NO-GO for the idealised R-cell class beyond R ≈ 4.

### What was proved
- Lemma 1.1 (transfer of a codimension-k bound to nearly-constrained data via the seminorm triangle inequality).
- Proposition 3.1 (R = 2 in ℓ_g from 17C), Lemma 3.2 (piecewise compression with exact 𝔇₃ and comb), Lemma 3.3
  (three-cell lower bound against a finite gauge family, with all leakage terms).
- Theorem 3.4: on three-cell data with the transported constraints, the complete tail form is ≥ 0.70·ℓ_g at T = 0.8 and
  T = 1.0 (arb-certified); Theorem 4.1(i).

### What failed and why
- Transport defect: in-band mass < 10⁻⁴ and value defect ≥ 0 (good), but the transported f(λ), A, B miss the exact
  conditions by δ = 0.03–0.16 on the measured vectors; the 17C constant transfers only where δ < 0.075, with large loss.
- (HR_g) on idealised R-cell data: κ_R ≈ 0.81, 0.75, 0.68 for R = 2, 3, 4, then 0.11–0.17, 0.10, 10⁻⁴, 10⁻¹¹ for R = 5 … 8
  (T = 0.8); no R-uniform constant. The near-null directions for R ≥ 5 are not near-gauge (J = 80 does not lift them).
- Falsifier (a): Theorem 3.4 does not survive c = 1.1 (the expectation "coercivity survives c ≠ 1" is false here).
- First certificate run at T = 1.0 failed on a crude weight bound (sup of the weights on the Bernstein ellipse ~10¹³⁷);
  fixed by 320 nodes.

### Next concrete step
Add the band-limitation of ℱf (type 2πλ: u is the restriction of an entire function of exponential type, equivalently F₁
lies in the image of [−λ, λ]-supported f) to the R-cell problem as a constraint family — e.g. through the prolate high span
itself transported cell by cell — and remeasure κ_R for R = 5 … 8; separately run falsifiers (b)–(d) on Theorem 3.4.

## Reproducibility
tools/multi_cell/: defect.py, defect10.py (§1; NPZ=fake.npz, RES=res10.pkl for T = 1.0; coef10.py, tail10.py, run10.py
regenerate the T = 1.0 vectors from SAVE=t10.npz TOP=100 TOPS=68,76,84,92 FASTMUL=1 python3 tools/prolate_tailgram.py 1.0 370
30 148 12); qW.py (q_W of Lemma 1.1); cellRg.py R Nb T J c (double), cellRg_mp.py R Nb T J c dps NQ (mpmath), pw3.py
τ* n T J c (piecewise float) — §2, outputs runs.txt, runs2.txt, mp.txt; cert3.py τ* n T J κ [c] with QW=320 for T = 1.0
(§3; outputs out3_*.txt; ≈ 2–6 min each). Every run ≤ 20 min.
