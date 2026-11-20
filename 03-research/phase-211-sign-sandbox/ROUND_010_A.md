# Round 010 A — The high-range estimate (HR) with the gauge quotient: the consistent admissible quotient, the scale of the comb-generic tools, and where the plunge sits

Target (★): λ_A(T) ≥ 0 for every T (STATEMENT_001). Object: a_T = W_T on P_T, λ_A(T) its infimum on unit vectors. Notation
of ROUND_009_B and Paper 47 §sec:ext: λ = e^T, N = λ², c = 2πN, E the summation map, ψ_k the even prolates of [−λ, λ] at
c = 2πN (normalised in L²), χ_k their concentrations, d_k = 1 − χ_k, admissible f as in def:ext (even, supported in
[−λ, λ], f(0) = ℱf(0) = f(λ) = 0), gauge 𝒢_T (even φ supported in [−1/λ, 1/λ], φ(0) = ℱφ(0) = 0), ℓ(g) the gauge-minimised
leakage. LM := prolate indices k ≤ 4N, HI := 4N < k ≤ K (K up to 3·4N). Labels: PROVED / CITED / CONDITIONAL / ARGUED /
OPEN / NO-GO / NUMERICAL.

## 0. Corpus check

Searched: ROUTES-TRIED-INDEX README rows P211-2B, P211-8E, P211-9A, P211-9B and the phase-211 ledger rows C21–C23; phase
199 memos on prob:ext-L (V_001 V.1.3–V.1.4: no ℱ-sector splitting of ℓ; T_001, U_001); ROUND_008_E §2 (constraint count),
ROUND_009_A (mollified block V_d), ROUND_009_B §2.2–2.6 ((2.1), (HR)); Paper 47 def:ext, lem:ext-mob, prop:ext-gauge,
lem:ext-ellbound, prob:ext-L, prop:ext-consol(b), lem:ext-hf and the remark after it ("the complement of that subspace has
dimension of order TΩ_*, superpolynomial in N, and contains the whole prolate range k ≲ 4N").
What differs here. (i) The quotient is computed on the admissible subspace with the full image (both parities, no
projection), which 9B did not do (9B used P_+Π_TEψ_k against the leakage of the raw, non-admissible ψ_k); §1 shows this is
not a cosmetic change: it removes the decay of α_HI that 9B read as gauge vectors. (ii) The gauge is minimised exactly on
a Legendre basis of 𝒢_T with both gauge conditions imposed. (iii) The comb-generic route of task item (2) is tested
against the scale of lem:ext-hf before it is used; §3 records a NO-GO for that class, stated with its class.
Nothing in the index is retried: (HR) itself was created in 9B and is the object here.

## 1. The consistent quotient (definitions; PROVED as bookkeeping)

For a coefficient vector a (even k ≤ K) put f_a = Σa_kψ_k. The quotient of prob:ext-L is W_T(Ef)/ℓ(Ef) over admissible f
with Ef ∈ P_T. On span{ψ_k} this is the pair
    M(a) = W_T(Ef_a)   (full image, no parity or P_T projection),
    D_g(a) = min_{φ∈𝒢_T} leak(f_a + φ) = aᵀ(D − DJH^{−1}JᵀD)a,   D = diag(d_k), H = I − Jᵀdiag(χ)J,
restricted to the subspace 𝒜_K = {a : f_a(λ) = 0, f_a(0) = 0, ∫f_a = 0, A(Ef_a) = B(Ef_a) = 0} (five linear conditions);
J holds the overlaps ⟨ψ_k, φ_j⟩ with an orthonormal basis φ_j of the gauge (even Legendre polynomials on [−1/λ, 1/λ]
with the two gauge conditions imposed). The formula for D_g is the minimisation of the quadratic
leak(f_a + φ_β) = aᵀDa + 2aᵀDJβ + βᵀHβ (by double orthogonality, leak(f) = Σ(1 − χ_k)⟨f, ψ_k⟩² for f supported in [−λ, λ]);
the gauge leaves the five conditions and Ef unchanged (lem:ext-mob, prop:ext-gauge), so (M, D_g) on 𝒜_K is exactly the
restriction of prob:ext-L to Ef with f ∈ span{ψ_k : k ≤ K} ⊕ 𝒢_T (PROVED; elementary).

**Remark 1.1 (what 9B computed instead; PROVED).** 9B §2 used h_k = P_+Π_TEψ_k against D(a) = Σd_ka_k² with no
admissibility. Three things differ, and each one can only lower the 9B quotient relative to prob:ext-L or make it
meaningless: (a) for a class-mixed or high-index combination, P_+Ef ≠ Ef and the discarded odd part carries W_T-mass
while D still charges the leakage of the whole f; the even part has its own representatives, whose leakage is not
D(a); (b) Π_TEf ≠ Ef unless A(Ef) = B(Ef) = 0; (c) raw ψ_k have ψ_k(λ) ≠ 0 (|ψ_k(λ)| = 3–5 for k > 4N, Table 1.0), so
Eψ_k jumps at x = T and is not in the core. Below 4N these effects are invisible (class +1 is parity-selected to 10⁻⁴,
ψ_k(λ) is ≤ 10⁻⁵ for k ≤ 8); above 4N they dominate.

Table 1.0 (NUMERICAL): ψ_k(λ) at T = 0.8: k = 0: 7·10⁻¹³, 8: 7.6·10⁻⁶, 16: 0.18, 24: 3.1, 32: 3.8, 40: 4.2, 48: 4.7, 56: 5.0.
Sine-Galerkin capture ‖Galerkin(Eψ_k)‖²/‖Eψ_k‖²: ≥ 0.999 for k ≤ 4N, dropping to 0.85 just above 4N and to 0.58–0.72 at
k = 3·4N (T = 0.8/1.0/1.2, Nb = 90/160/180): the jump at T is the unresolved part.

## 2. NUMERICAL: the high block with the gauge quotient (task item 1)

Tools: tools/prolate_gauge_hi.py (9B pair: P_+Π_TEψ_k against D and D_g, raw ψ_k; kept for comparison) and
tools/prolate_gauge_adm.py (the consistent pair of §1). Caches sector_T0.8_N90_K60, sector_T0.8_N160_K60,
sector_T1.0_N160_K88, sector_T1.0_N220_K88, sector_T1.2_N180_K132 (tools/prolate_sector.py). Gauge: MIN = 12 Legendre
functions (10 after the two gauge conditions); MIN = 20/30 changes no printed digit below the resolution cap (checked at
T = 1.0). Every value here is a Galerkin value: M is an upper estimate of W_T on the given span and the infima are infima
over the span, not over the space.

### 2.1 The 9B pair reproduces the 9B decay, with or without the gauge
With h_k = P_+Π_TEψ_k (raw ψ_k), the gauge-minimised α_HI still decays with K (class +1: 2.0 → 0.012 at T = 0.8, Nb = 90,
k ≤ 60; 1.86 → 0.006 at T = 1.0, k ≤ 88; 2.1 → 0.0016 at T = 1.2, k ≤ 132), and with both classes it decays faster
(to 1.5·10⁻⁴, 2.5·10⁻⁵, 1.6·10⁻⁵). The gauge changes α_HI by a factor ≤ 2 (min eig D_g/D on the class-(+1) high block is
0.48–0.50 at all three T). The decay is not stable in the resolution: at T = 0.8, k ≤ 60, class +1, α_HI = 0.012 (Nb = 90)
vs 0.111 (Nb = 160). The three-level Schur with D_g fails at the same place as in 9B (2×2 bound negative from
k = 48/56/— at T = 0.8/1.0), κ_C = 205/182 and ‖Gram‖ = 2.8/4.6 at T = 0.8/1.0 make the (2.1) value negative. So the
gauge infimum alone does not repair the 9B quotient: its decay has a different cause (Remark 1.1, and 2.2 below).

### 2.2 The consistent pair: (HR)(a) on the admissible high block
α_HI := inf over the admissible high block (4N < k ≤ K, five conditions imposed inside the block) of W_T(Ef)/ℓ_g(f);
also inf W_T/‖Ef‖² and the global infimum of W_T/ℓ_g over the whole admissible span k ≤ K.

Table 2.2a, all even k (both ℱ-classes), Λ:
| T (4N) | Nb | K = top k | K/4N | α_HI (gauge) | α_HI (fixed rep.) | inf W/‖Ef‖² on HI | global inf W/ℓ_g, k ≤ K |
|---|---|---|---|---|---|---|---|
| 0.8 (19.8) | 160 | 30 / 40 / 50 / 60 | 1.5 / 2.0 / 2.5 / 3.0 | 2.08 / 1.41 / 1.06 / 0.87 | 2.07 / 1.39 / 0.97 / 0.52 | 1.01 / 0.88 / 0.78 / 0.75 | 0.95 / 0.86 / 0.82 / 0.80 |
| 1.0 (29.6) | 220 | 40 / 50 / 60 / 70 / 82 | 1.35 / 1.7 / 2.0 / 2.4 / 2.8 | 3.09 / 2.02 / 1.52 / 1.26 / 1.05 | 3.08 / 2.01 / 1.48 / 1.17 / 0.85 | 1.01 / 0.91 / 0.85 / 0.75 / 0.72 | 1.41 / 1.09 / 1.06 / 1.03 / 0.45 |
| 1.2 (44.1) | 180 | 56 / 64 / 72 / 76 | 1.27 / 1.45 / 1.63 / 1.72 | 3.96 / 3.19 / 2.61 / 1.88 | 3.96 / 3.19 / 2.61 / 1.88 | 0.95 / 0.92 / 0.90 / 0.90 | 2.02 / 1.57 / 1.24 / 0.65 |
Class +1 alone (k ≡ 0 mod 4): α_HI = 2.31 → 2.01 (T = 0.8, k ≤ 60), 3.00 → 2.94 (T = 1.0, k ≤ 76, Nb = 220), flat in K.

Resolution cap (NUMERICAL, measured). At fixed T the consistent α_HI collapses abruptly past a threshold k_* that moves
with the number Nb of sine modes and not with T or the gauge: T = 1.0: k_* ≈ 70 at Nb = 160, k_* ≈ 84 at Nb = 220
(α_HI(72) = 0.82 vs 1.19; α_HI(80) = 0.11 vs 1.05); T = 1.2, Nb = 180: k_* ≈ 76; T = 0.8, Nb = 160: no collapse up to 60.
So k_* ≈ 0.4·Nb, and past k_* the Galerkin image of the admissible high combinations loses its mass (inf W/‖Ef‖² stays
0.70–0.73 while ℓ_g/‖Ef‖² exceeds the a-priori bound of lem:ext-ellbound's construction). Values past k_* are discarded;
the last columns of the global infimum (0.45 at T = 1.0, K = 82; 0.65 at T = 1.2, K = 76) are already within 10% of k_*
and are the least reliable entries of the table.

Reading of (HR)(a). Below the resolution cap, on the consistent pair:
(i) α_HI stays O(1) at every T: no near-gauge collapse. The 9B decay (α_HI → 0) does not occur; it came from the
inconsistent pair (Remark 1.1), and in particular from projecting non-class-separated images to the even sector.
(ii) The gauge matters little on the high block (gauge vs fixed representative differ by < 20% below 2.5·4N; the
difference grows to a factor 1.7 at 3·4N, T = 0.8): the near-gauge mechanism of 9B §2.4(iii) is not what drives the
high block.
(iii) α_HI still decreases in K, roughly like (K/4N)^{−1} on the measured range: the product α_HI·K/4N is 3.1/2.8/2.7/2.6 at T = 0.8 and 4.2/3.4/3.0/3.0/2.9 at T = 1.0. Whether it has a positive limit as K → ∞ is
not decided by these data: (HR)(a) uniformly in K is NOT confirmed numerically; it is consistent with a slow decay of
order 4N/K, and with a positive limit.
(iv) The class-(+1) high block is flat (≈ 2.0, ≈ 2.9): the decrease in (iii) comes from mixing the two ℱ-classes above
the plunge, where the class structure is void.

### 2.3 Coupling, the constants of (2.1), and the assembled Schur bound
Two-block test on the consistent pair: LM_adm = admissible span of k ≤ 4N (five conditions imposed inside LM), HI_adm
likewise for 4N < k ≤ K; κ_LM = inf W/ℓ_g on LM_adm; Γ′ = ‖D_HI^{−1/2}M_{HI,LM}D_LM^{−1/2}‖ with the diagonal blocks of
D_g (the ℓ_g-metric coupling); 2×2 bound = smallest root of (κ_LM − x)(α_HI − x) = Γ′²; μ = inf ℓ_g/‖Ef‖² on LM_adm ⊕ HI_adm;
then W_T(Ef) ≥ (2×2 bound)·D_g^{bd}(a) and the assembled lower bound for W_T/‖Ef‖² on that span is (2×2 bound)·μ
(this uses the block-diagonal part of D_g; the true infimum of W/ℓ_g with the full D_g is printed next to it).

Table 2.3 (Λ):
| T | K | α_HI | Γ′ | Γ′²/(κ_LMα_HI) | 2×2 bound | true inf W/ℓ_g | μ/d_8 | (2×2 bound)·μ/λ_A | Ritz inf W/‖Ef‖² ÷ λ_A | ‖Gram‖ |
|---|---|---|---|---|---|---|---|---|---|---|
| 0.8 (Nb 160), κ_LM = 2.12 | 30 | 2.08 | 0.33 | 0.025 | 1.77 | 1.90 | 0.59 | 0.86 | 1.46 | 2.3 |
| | 42 | 1.36 | 0.75 | 0.20 | 0.90 | 1.35 | 0.59 | 0.44 | 1.41 | 2.7 |
| | 58 | 0.91 | 1.00 | 0.52 | 0.35 | 0.91 | 0.59 | 0.17 | 1.36 | 3.0 |
| 1.0 (Nb 220), κ_LM = 3.12 | 40 | 3.09 | 0.47 | 0.023 | 2.64 | 2.87 | 0.45 | 0.86 | 1.54 | 4.1 |
| | 60 | 1.52 | 1.34 | 0.38 | 0.76 | 1.52 | 0.45 | 0.25 | 1.53 | 4.4 |
| | 80 | 1.05 | 1.73 | 0.91 | 0.075 | 1.04 | 0.45 | 0.025 | 1.49 | 5.2 |
(λ_A here is the Galerkin value at the same Nb: 5.90·10⁻¹² at T = 0.8, 1.47·10⁻²³ at T = 1.0, Nb = 220.)

Readings. (i) The constants requested for (2.1). In the consistent pair the constraint elimination of 9B Lemma 2.1 is
replaced by exact restriction to the admissible subspace, and the product "d_8/(2(1 + κ_C²)‖Gram‖)" of (2.1) is replaced
by the measured μ = inf ℓ_g/‖Ef‖²: μ = 0.59·d_8 (T = 0.8) and 0.45·d_8 (T = 1.0), flat in K (the infimum sits on the LM
survivor). For comparison, the 9B route with κ_C = 205/182 and ‖Gram‖ = 2.8/4.6 (§2.1) would give the factor
1/(2(1 + κ_C²)‖Gram‖) ≈ 4·10⁻⁶ / 3·10⁻⁶: (2.1) is correct as an implication but its constant is off by five to six
orders, and its κ is the 9B κ, which does not stabilise. REVIEW_008 item (3) stands: (2.1) as written is CONDITIONAL and
is not to be read as a lower bound for λ_A.
(ii) The assembled bound is positive on every resolved span: W_T(Ef) ≥ θ_K λ_A‖Ef‖² with θ_K = 0.86 → 0.17 (T = 0.8,
K = 30 → 58) and 0.86 → 0.025 (T = 1.0, K = 40 → 80); the Ritz bottom on the same span is 1.36–1.54 λ_A. So on the
span k ≤ K the Schur chain recovers the index-8 law λ ≍ d_8 with a constant that degrades with K.
(iii) The degradation is the coupling, not α_HI alone: Γ′ grows from 0.3–0.5 to 1.0–1.7 and Γ′²/(κ_LMα_HI) approaches
1 at the top of the resolved range at T = 1.0. (HR)(b) in the form Γ′² ≤ (1 − η)κ_LMα_HI is therefore NOT confirmed
uniformly in K; on the measured range it holds with η ≥ 0.09 (T = 1.0, K = 80) and η ≥ 0.48 (T = 0.8, K = 58).
(iv) The true infimum of W/ℓ_g on LM_adm ⊕ HI_adm equals α_HI to two digits at every K: the bottom of the quotient is
in the high block, not in LM (κ_LM = 2.1/3.1 > α_HI). The near-null direction of W_T (index 8) is in LM, where ℓ_g is
of size d_8; the bottom of the ratio is in HI, where both are O(1).

## 3. PURE MATH: can (HR)(a) for k ≥ (1+δ)4N come from lem:ext-hf and prolate decay? (task item 2)

### 3.1 The symbol form of W_T on the window (PROVED; standard)
For real g ∈ L²(I_T) extended by zero, c_g(u) = ∫g(x)g(x + u)dx vanishes for |u| ≥ 2T and c_g(u) = (1/2π)∫|ĝ(τ)|²cos(τu)dτ.
Since 2T = log N, only 2 ≤ n < N enter the comb, and (with the comb of eq:W read as Σv_nc_g(log n))
    W_T(g) = (1/2π)∫_ℝ (m(τ) − P_T(τ))|ĝ(τ)|²dτ + 2A(g)B(g),        P_T(τ) := Σ_{2≤n<N} v_n cos(τ log n).          (3.1)
*Proof.* Insert the cosine formula for c_g(log n) in the finite comb; the archimedean part is the symbol term of eq:W. ∎
P_T is a real trigonometric polynomial in τ with frequencies log n < 2T and P_T(0) = S_T := Σ_{n<N}v_n.

### 3.2 The scale of lem:ext-hf against the prolate high block (PROVED for polynomial data)
lem:ext-hf gives W_T(g) ≥ ‖g‖² − (K_T + λ + 1)‖P_<g‖², useful only when ‖P_<g‖² ≤ ‖g‖²/(2(K_T + λ + 1)), P_< the Fourier
projection onto |τ| < Ω_* = e^{K_T+λ+1} − 2.

**Lemma 3.1 (Markov in L², elementary; PROVED).** If p is a polynomial of degree ≤ K on an interval of length L, then
‖p′‖_{L²} ≤ ((K + 2)²/L)‖p‖_{L²}.
*Proof.* On [−1, 1] with orthonormal Legendre P̄_j, P_j′ = Σ_{i<j, i≢j (2)}(2i + 1)P_i gives ‖P̄_j′‖² = (2j + 1)j(j + 1)/2 ≤ (j + 1)³;
for p = Σ_{j≤K}b_jP̄_j, Cauchy–Schwarz gives ‖p′‖ ≤ ‖b‖(Σ_{j≤K}(j + 1)³)^{1/2} ≤ ((K + 2)²/2)‖p‖; rescale to length L. ∎

**Proposition 3.2 (lem:ext-hf is void on degree-K data unless K is superpolynomial in N; PROVED).** Let λ ≥ 2, f admissible,
f|_{[1/λ,λ]} a polynomial of degree ≤ K, g = Ef. Then
    ‖g′‖_{L²(I_T)} ≤ (½ + 8N(K + 2)²)‖g‖,      ‖(1 − P_<)g‖² ≤ C(1 + N²K⁴)‖g‖²/Ω_*
for an absolute C. In particular the hypothesis of lem:ext-hf (which needs ‖(1 − P_<)g‖² ≥ ½‖g‖²) fails for every such g unless
N²K⁴ ≥ c·Ω_*, i.e. unless K ≥ c′N^{−1/2}e^{(K_T+λ+1)/4}, which is superpolynomial in N. The whole range K ≤ 3·4N (indeed K ≤ N^A for any fixed A,
for T large) lies in the complement of the subspace on which lem:ext-hf says anything.
*Proof.* g′ = ½g + Σ_n e^{3x/2}nf′(ne^x) on I_T, and with u = ne^x, ‖e^{3x/2}nf′(ne^x)‖² = n^{−1}∫u²f′(u)²du ≤ (λ²/n)‖f′‖²_{[1/λ,λ]}.
By Lemma 3.1 on [1/λ, λ] (length ≥ λ/2), ‖f′‖ ≤ 2(K + 2)²λ^{−1}‖f‖_{[1/λ,λ]}, and ‖f‖_{[1/λ,λ]} ≤ 2√N‖g‖ (lem:ext-mob). Summing over
n ≤ N with Σn^{−1/2} ≤ 2√N gives the first bound. For the second: f(λ) = 0 gives g(T) = 0, while g(−T) =: J may be ≠ 0;
write g = Je + g₁ with e(x) = (T − x)/(2T) on I_T, so g₁ vanishes at ±T and ∫τ²|ĝ₁|² = 2π‖g₁′‖²; ê has a single jump
and |ê(τ)| ≤ 2/|τ| for |τ| ≥ 1/T. Hence ∫_{|τ|≥Ω}|ĝ|² ≤ 2J²·8/Ω + 2·2π‖g₁′‖²/Ω², and J² ≤ ‖g‖²/T + 2‖g‖‖g′‖ (one-dimensional
Sobolev on I_T), ‖g₁′‖ ≤ ‖g′‖ + |J|(2T)^{−1/2}. Insert the first bound. ∎
Remark. Prolate data are not polynomials, but ψ_k is within e^{−(j−k)} in L² of its Legendre truncation at degree
j ≥ k + O(c) (the Legendre coefficients of ψ_k decay super-geometrically past the turning index; ARGUED from the
three-term recursion used in tools/prolate_sector.py, whose coefficient tail at the cut-off is below 10⁻⁹⁰). So
Proposition 3.2 applies to span{ψ_k : k ≤ K} with K replaced by K + O(N) (ARGUED).

### 3.3 Why no comb-generic estimate can reach the high block (NO-GO, class stated; PROVED)
Class 𝒦_S: forms W^w_T = archimedean + rank two − Σ_{n<N}w_nc_g(log n), with w_n ≥ 0 and Σw_n ≤ S. lem:ext-hf is a
statement in this class (it uses the comb only through a norm bound).

**Proposition 3.3 (PROVED).** There are absolute C₀, T₀ such that for T ≥ T₀, every Ω₀ ≥ 10 with log(2 + 3Ω₀) ≤ S − C₀,
there exist w ∈ 𝒦_S and g ∈ P_T with ĝ concentrated on Ω₀ ≤ |τ| ≤ 2Ω₀ (up to O(T^{−1})) and W^w_T(g) < 0.
*Proof.* Take w = Sδ_2, τ₀ ∈ [Ω₀, 2Ω₀] with τ₀log 2 ∈ 2πℤ (the spacing 2π/log 2 < 10 ≤ Ω₀), β a fixed even C^∞ bump on
(−1, 1), g₀(x) = β(x/T)cos(τ₀x), and g the P_T-projection of g₀. Then c_{g₀}(log 2) = ½∫β(x/T)β((x + log 2)/T)dx + O((τ₀T)^{−M}) =
(1 − O(T^{−2}))‖g₀‖²; the archimedean term is ≤ (log(2 + 3Ω₀) + C_∞ + O(T^{−1}))‖g₀‖² because |m(τ)| ≤ log(2 + |τ|) + C_∞ and ĝ₀
is concentrated at ±τ₀ with width O(1/T); A(g₀), B(g₀) = O((τ₀T)^{−M}) by repeated integration by parts, so the P_T-projection
and the rank-two term cost O((τ₀T)^{−M})‖g₀‖². Hence W^w_T(g) ≤ (log(2 + 3Ω₀) + C_∞ − S + O(T^{−1}))‖g‖² < 0. ∎
For Λ, S_Λ(T) = Σ_{n<N}2Λ(n)n^{−1/2} = 4√N(1 + o(1)) = 4λ(1 + o(1)) (Chebyshev–PNT, CITED). So 𝒦_{S_Λ} contains combs that
make the form negative at every frequency up to e^{4λ−C}: this is exactly why lem:ext-hf needs Ω_* ≍ e^{λ+O(1)}, and it
cannot be improved inside the class.
Transfer to the high block (ARGUED). The witness with the smallest frequency, τ₀ = 2π/log 2 ≈ 9.06, has representative
f = E^{−1}g with local frequency τ₀/u on [1/λ, λ]; its prolate content sits at k ≍ τ₀N·O(1), inside (4N, 3·4N] up to the
constant. So within 𝒦_{S_Λ}, positivity fails on the high block itself.

**Consequence for task item (2) (NO-GO).** (HR)(a) for k ≥ (1+δ)4N cannot be obtained from lem:ext-hf plus prolate
concentration bounds: (i) lem:ext-hf is void on the block (Proposition 3.2); (ii) no estimate that sees the comb only
through its total mass can hold there (Proposition 3.3). The range not covered is not the plunge (width O(log N)) but
all k from the plunge up to e^{cλ}: superpolynomial, not finite-dimensional. The premise "for k > 4N the exterior data
are essentially free, so the comb-generic lemma applies" is false: freedom of the exterior data (χ_k ≈ 0) controls the
denominator ℓ, not the frequency scale at which the comb can be beaten.

### 3.4 What the high block needs instead, and where the plunge sits
(i) The tool class. By (3.1), W_T(g) ≥ 0 on a block needs the symbol m − P_T to be non-negative on average against
|ĝ|²: the comb enters through the values of the Dirichlet polynomial P_T(τ) on the frequency band of the block, not
through S_T. For Λ these values are far below S_T away from τ = 0: the mean square on a band of length U ≫ N is
(1/U)∫P_T² ≈ ½Σ_{n<N}v_n² = 2Σ_{n<N}Λ(n)²/n ≈ (log N)² = 4T² (mean-value theorem for Dirichlet polynomials,
Montgomery–Vaughan, CITED; at U ≍ N the error term is of the same order), i.e. RMS P_T ≈ 2T, against m(τ) = log(|τ|/2π) + O(1/τ)
= 2T + log(κ/2π) at |τ| = κN. On the high block both sides are 2T + O(1): the competition is decided at order one, which
matches the measured α_HI = O(1) (Table 2.2a) and says that (HR)(a) is a mean-value statement about P_T at frequencies
≲ K, sharp in its constants. This is the precise tool class to build: an L²-in-τ bound for the positive part of P_T − m
against |ĝ|² for ĝ coming from admissible high-block data (ARGUED; OPEN as a theorem).
(ii) The plunge, counted (CITED + NUMERICAL). Landau–Widom: #{n : ε < χ_n(c) < 1 − ε} = (2/π²)log c·log((1 − ε)/ε) + o(log c)
(CITED; asymptotic, constant in o(·) not explicit). Even indices: about half. At ε = 10⁻³ the measured even-index plunge
has 4, 4, 5 members (T = 0.8, 1.0, 1.2: k = 16–22, 26–32, 40–48), vs (1/π²)log(2πN)log 999 = 2.4, 2.7, 3.0 from the
leading term. So the plunge block Π_ε = span{ψ_k : ε < χ_k < 1 − ε} has dimension (1/π²)log(2πN)log(1/ε) + o(log N).
(iii) (HR) as an explicit finite-dimensional inequality on the plunge (statement; OPEN). With 𝒜(Π_ε) the admissible
subspace of Π_ε ⊕ (the five conditions) and the matrices of §1:
    (HR-Π)  M|_{𝒜(Π_ε)} ≥ κ_Π·D_g|_{𝒜(Π_ε)},    dim 𝒜(Π_ε) ≤ (1/π²)log(2πN)log(1/ε) + o(log N),
an m×m generalized-eigenvalue inequality with m = O(log N·log(1/ε)), whose entries are W_T(Eψ_j, Eψ_k) and the exact
d_k, J. It is checkable at each T. But by (ii) of the Consequence it is NOT the only remaining piece: the super-plunge
range (1+δ)4N < k < e^{cλ} carries the mean-value statement (i), which no finite-dimensional inequality replaces.

## 4. (HR)(b): the LM–HI coupling (task item 3)

**Proposition 4.1 (the cross-overlaps carry no information; PROVED).** For j ≠ k, ⟨ψ_j, ψ_k⟩_{L²(−λ,λ)} = 0 and
⟨ℱψ_j, ℱψ_k⟩_{L²(−λ,λ)} = 0 (double orthogonality, CITED), and the leakage form is diagonal: leak(Σa_kψ_k) = Σd_ka_k². The
coupling entering Proposition 2.2 of 9B is
    W_T(Eψ_j, Eψ_k) = (1/2π)∫(m − P_T)ĝ_j \overline{ĝ_k}dτ + A(g_j)B(g_k) + A(g_k)B(g_j),    g_i = Eψ_i,              (4.1)
by (3.1) polarised. *Proof.* Polarisation of (3.1); the overlaps are the classical identities. ∎
So "decay of prolate cross-overlaps across the plunge" has no object: the overlaps vanish identically for every pair,
and all of the coupling sits in the symbol pairing (4.1). Decay of (4.1) in |j − k| would need the spectra of g_j and g_k
to separate on the τ-line. They do not: Eψ_k(x) = e^{x/2}Σ_nψ_k(ne^x) has x-frequency ≈ ue·k/λ at u = ne^x, which runs from
≈ k/N near x = −T to ≈ k near x = T; a low index j ≤ 4N and a high index k > 4N both occupy the band τ ≈ 4–12 near x = −T
(ARGUED). This is the mechanism behind the measured growth of Γ′.

NUMERICAL (Table 2.3): Γ′ = 0.33 → 1.00 (T = 0.8, K = 30 → 58) and 0.47 → 1.73 (T = 1.0, K = 40 → 80) in the ℓ_g metric:
no decay; Γ′²/(κ_LMα_HI) reaches 0.52 and 0.91. In the 9B pair Γ′ saturated at 0.3–0.8 (9B §2.4) because α_HI had
already collapsed; in the consistent pair α_HI stays O(1) and the coupling becomes the binding constraint.
What a proof of (HR)(b) needs (OPEN): a bound |W_T(G_L, G_H)|² ≤ (1 − η)κ_LMα_HI ℓ(G_L)ℓ(G_H) for G_L ∈ E(LM_adm),
G_H ∈ E(HI_adm). The Cauchy–Schwarz bound |W(G_L,G_H)|² ≤ W(G_L)W(G_H) is unavailable (it presupposes W ≥ 0 on the sum,
which is the target). The available non-circular route is the symbol: by (4.1), |W_T(G_L, G_H)| ≤ (1/2π)∫|m − P_T||ĝ_L||ĝ_H|
+ rank two, and ĝ_L is concentrated (index ≤ 4N, near-null) where the LM survivor lives. No bound of this form was proved
here.

## 5. Falsifier test (BRIEF rule 4; task item 4)

NUMERICAL, consistent pair, T = 1.0, Nb = 160 (resolved range k ≤ 70):
| w | α_HI all k, K = 50 / 60 / 70 | α_HI class +1, K = 72 | global inf W/ℓ_g on the admissible span |
|---|---|---|---|
| Λ | 1.99 / 1.51 / 1.24 | 2.93 | +1.03 (K = 70) |
| 1.01Λ | 1.98 / 1.50 / 1.23 | 2.89 | −7.5·10¹⁹ |
| a_3 (prime 2 deleted) | 2.84 / 1.98 / 1.42 | 4.36 | −2.7·10²¹ |
Readings. (a) The high block does not see the falsifiers at the level tested: α_HI moves by < 1% under 1.01Λ and
increases under a_3 (deleting comb mass raises W_T). (b) Every falsifier is rejected globally, by a negative value of
order 10²⁰ d_8-units: the negative direction is the LM survivor, whose W_T drops from +κd_8 to −O(10⁻³) while its
leakage stays ≈ d_8 (9B §3.2). So the Λ-specificity sits in the low block, as stated in the task: there, through
thm:ext-half and the near-nullity of class +1 (9B §3.2, 9A Corollary 4.1).
(c) Proposition 3.3 sharpens what "comb-generic" may mean on the high block. The high-block estimate (HR)(a) survives small
perturbations of the weights (a, b, d) but not arbitrary redistributions of the same comb mass: a single atom of mass
S_Λ at n = 2 makes the form negative at τ ≈ 9 (Proposition 3.3, transfer ARGUED). So (HR)(a) is not comb-generic in the
sense of lem:ext-hf (total mass); it needs the spread of Λ over n < N (the mean-value size of P_T, §3.4(i)). It is not a
sign step either: it does not reject (a), (b), (d), and (c) Beurling systems enter only through their own P_T. The sign
step remains the low block; (HR) is the coercivity that lets it propagate.
(d) Falsifier test of the PROVED pieces. Lemma 3.1, Propositions 3.2 and 4.1 and the identity (3.1) are weight-free or
hold for every weight with the stated comb; Proposition 3.3 is a statement about a class of weights. None is a sign step,
and all survive (a)–(d), as they must.

## 6. Corrections to the record

- ROUND_009_B §2.4 reading (iii) ("the decrease of α_HI is forced by approximate gauge vectors in the high prolate span",
  ARGUED) is WITHDRAWN as the explanation. The gauge-minimised version of the 9B pair still decays (§2.1), and the
  consistent pair (admissible data, full image, five conditions) does not collapse: α_HI = O(1) on the resolved range
  (§2.2). The 9B decay came from the inconsistent pair (Remark 1.1) and, past k ≈ 0.4·Nb, from Galerkin resolution.
- ROUND_009_B (2.1): its constant 1/(2(1 + κ_C²)‖Gram‖) is now measured (κ_C ≈ 180–205, ‖Gram‖ ≈ 2.8–4.6, factor ≈ 3–4·10⁻⁶)
  and is replaced by the direct μ = inf ℓ_g/‖Ef‖² = (0.45–0.59)·d_8 on admissible data. (2.1) stays CONDITIONAL (REVIEW_008).
- (HR) is restated on the consistent pair: (a) α_HI ≥ κ_H uniformly in K (NOT confirmed: α_HI·K/4N ≈ 2.6–3.0 on the
  measured range, compatible with decay ∝ 4N/K); (b) Γ′² ≤ (1 − η)κ_LMα_HI (holds on the measured range with η ≥ 0.09,
  margin shrinking with K). The plunge is not the only remaining piece (§3.3).
- All computations here use raw prolates restricted to the admissible subspace (five linear conditions). REVIEW_008
  item (1) asks for the mollified space V_d of 9A for anything meant to support a proof; nothing in §2 is used in a proof
  here, and the restriction f(λ) = 0 removes the jump at x = T that motivated that item for the high block; the C¹
  requirement of Theorem 1.1 is not met by this space either and is not used.

## 7. Reproducibility
tools/prolate_sector.py T Nb dps KMAX (caches above); tools/prolate_gauge_hi.py T Nb dps KMAX MIN [w] (§2.1; FULL=1 keeps
both parities); tools/prolate_gauge_adm.py T Nb dps KMAX MIN [w] (§2.2–2.3, §5; KTOP caps the high block at the
resolution limit). Runs: (0.8, 160, 40, 60, 12), (1.0, 160, 40, 88, 12/30) with w ∈ {L, 1.01, a3}, (1.0, 220, 40, 88, 12),
(1.2, 180, 80, 132, 12); each ≤ 10 min except the T = 1.2 full sweep (stopped past the resolution cap).

## Result
PIVOT, with a PROVED piece and a NO-GO.
The gauge quotient was computed on the high block in the consistent form; it does not collapse (α_HI = O(1) to the
resolution limit, 2–3·4N), and the assembled two-block Schur bound is positive on every resolved span (W_T ≥ θ_Kλ_A‖Ef‖²,
θ_K = 0.86 → 0.025), but neither (HR)(a) uniformly in K nor (HR)(b) is confirmed: α_HI decreases like ~4N/K and the
coupling Γ′ grows. The proposed proof route for (HR)(a) (lem:ext-hf plus prolate decay, leaving only the plunge) is closed:
lem:ext-hf is void on the whole polynomial-index range, and no comb-mass-only estimate can hold there.

### What was proved
- Remark 1.1 and §1: the consistent finite-dimensional form of prob:ext-L on span{ψ_k} ⊕ 𝒢_T (five linear conditions, full
  image, exact gauge minimisation D_g = D − DJH^{−1}JᵀD); the 9B pair differs from it in three identified ways.
- (3.1): W_T(g) = (1/2π)∫(m − P_T)|ĝ|² + 2AB on the window, P_T(τ) = Σ_{n<N}v_ncos(τ log n).
- Lemma 3.1 (L² Markov, constant (K + 2)²/L) and Proposition 3.2: lem:ext-hf is void on E(degree-K data) unless
  K ≥ c′N^{−1/2}e^{(K_T+λ+1)/4}.
- Proposition 3.3 (NO-GO for the class 𝒦_S of comb-mass-only estimates): negative values at every frequency
  Ω₀ ≤ e^{S−C₀}; with S_Λ ≈ 4λ this is the reason for Ω_* ≍ e^{λ}.
- Proposition 4.1: prolate cross-overlaps vanish identically; the LM–HI coupling is the symbol pairing (4.1).
NUMERICAL: Tables 2.2a, 2.3, §5 (α_HI, Γ′, μ, assembled bound, falsifiers); resolution cap k_* ≈ 0.4·Nb; κ_C, ‖Gram‖ of (2.1).
CITED: Landau–Widom plunge count; Montgomery–Vaughan mean value; Chebyshev–PNT size of S_Λ; double orthogonality.

### What failed and why
- (HR)(a) uniformly in K: not confirmed (α_HI·K/4N ≈ 2.6–3 on the range; a positive limit is not excluded and not shown).
- (HR)(b): no decay mechanism; Γ′²/(κ_LMα_HI) → 0.9 at T = 1.0, K = 80.
- Task item (2) as posed: lem:ext-hf does not reach k ~ (1+δ)4N (Proposition 3.2); the remaining region is not the plunge
  but the super-plunge up to e^{cλ}, so (HR) does not reduce to a finite-dimensional inequality. (HR-Π) on the plunge is
  stated (§3.4(iii)) but it is one piece, not the remainder.
- T = 1.2 high block past k ≈ 76 and the T = 1.2 falsifier sweep: beyond the resolution cap at Nb = 180 (not reported).

### Next concrete step
Build the mean-value tool of §3.4(i): for admissible high-block data prove
    (1/2π)∫(P_T − m)_+|ĝ|² ≤ (1 − η)(1/2π)∫(m − P_T)_+|ĝ|² + C·(rank-two and gauge terms)
using (3.1), the uncertainty bound |ĝ(τ)|² ≤ 2T‖g‖², and the measure/size of {τ : P_T(τ) > m(τ)} on |τ| ≲ K (a large-values
estimate for the Dirichlet polynomial P_T, which uses the spread of Λ over n < N and fails for single-atom combs, as
Proposition 3.3 requires). In parallel, raise Nb to ≈ 2.5K (k_* ≈ 0.4Nb) to test whether α_HI·K/4N stabilises at
K = 4·4N–6·4N at T = 0.8 and 1.0.
