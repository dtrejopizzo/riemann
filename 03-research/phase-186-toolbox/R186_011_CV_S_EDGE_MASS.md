# R186.011 — (CV_S), edge mass and boundedness of ε_S for S = {∞,2}

Framework and notation of R186.009 (λ = ½, P = 1_{(0,λ]}, F_S self-adjoint involutive, A_S = PF_SP, ξ_n, ζ_n, ϑ). Kernel of F_S in convergent form: K_S(x,y) = Σ_{k≥0} c_k − c_{−1}, c_k := cos(2π2^k xy) (rearrangement of Σ_k(2c_k − c_{k−1}); ‖Pc_kP‖ ≤ ½·2^{−k/2}, converges in norm; the exact truncation Σ_{k≤K}c_k − c_{−1} removes the spurious term 2c_K of R186.093).
Nothing here touches the sign.

## Status

| # | Statement | Label |
|---|---|---|
| R | **Weight reconciliation.** With ξ_n^♯ := λ_n^{−1}F_Sξ_n (= ξ_n on (0,λ]), ζ_n = λ_n(1−P)ξ_n^♯/√(1−λ_n²) and, for ρ ≥ 1, ε_S(ρ) = Σ_n λ_n/√(1−λ_n²)·⟨ξ_n\|ϑ(ρ⁻¹)ζ_n⟩ = Σ_n **λ_n²/(1−λ_n²)**·ρ^{1/2}∫_{λ/ρ}^{λ} ξ_n(x)ξ_n^♯(ρx)dx. The two forms (R186.009 and CC (84)/Lemma 5.4) are the same | PROVED |
| S | **No alternation.** The effective weight λ_n²/(1−λ_n²) is ≥ 0: the sign of λ_n cancels against the λ_n of ζ_n. The "Leibniz" mechanism does not exist | PROVED |
| Q | **Dyadic quasi-covariance.** K_S(2^j x,y) = K_S(x,y) − B_j(x,y), B_j := Σ_{i=0}^{j−1}(2c_i − c_{i−1}) (entire kernel). Hence ξ_n^♯(2^j x) = ξ_n^♯(x) − λ_n^{−1}(B_jξ_n)(x) | PROVED |
| Sp | A_S ∈ S_p (Schatten) for every p > 2; Σλ_n^4 < ∞ | PROVED |
| NH | For every interval I ⊂ (0,λ] of positive length, 1_I A_S is not Hilbert–Schmidt: Σ_n λ_n² ‖1_Iξ_n‖² = ∞ | PROVED (adaptation of R186.093 §5) |
| Div2 | At ρ = 2^j (j ≥ 1) series (84)_S **diverges to +∞**: ε_S(2^j) = 2^{j/2}Σ_n λ_n²/(1−λ_n²)‖1_{[2^{−j}λ,λ]}ξ_n‖² − (absolutely convergent series) = +∞ | PROVED (given R, Q, NH) |
| M | Edge mass: ‖1_{[λ/2,λ]}ξ_n‖² → ≈ ½, ‖1_{[λ(1−δ),λ]}ξ_n‖² ≈ δ on average, no decay in n; ξ_n(λ)² very irregular (0.003–14) with no trend; the ξ_n spread uniformly (wavelet-like, level 2^k), they **do not** concentrate at the edge nor at the points 2^{−k}λ | NUMERICAL |
| CV_S | Σ_n\|λ_n\|·(edge mass) < ∞ | **NO-GO** (regime (a): mass O(1)·δ, \|λ_n\| ≍ n^{−1/2}; moreover Div2 shows ε_S ∉ L^∞_loc near 2^j: no L^∞ form of CV_S can hold) |
| Prof | Profile: ε_S continuous at ρ = 1 with ε_S(1) = 0 and a one-sided derivative with a logarithmic divergence (ε_S(ρ) ≈ (ρ−1)(a + b log(1/(ρ−1))), b ≈ 0.17·λ⁻¹·½); bounded and rapidly convergent on compacta avoiding {2^{±j}}; **positive** logarithmic singularity ε_S(ρ) ≈ β_j log(1/\|ρ − 2^j\|) at ρ = 2^j, β₁ ≈ 0.15, β_j increasing ≈ ∝ 2^{j/2}(1−2^{−j}) | NUMERICAL |
| Atom | No atom −log2·2^{−1/2} appears in ε_S − ε_∞ at ρ = 2: a positive logarithmic peak appears, of integrated weight converging to a finite value, with no atom in the limit K → ∞ | NUMERICAL |
| L2 | ε_S ∈ L²_loc(ℝ*₊) (only logarithmic singularities), and hence R′_S Hilbert–Schmidt on L²(I_T) | OPEN (next lemma §6; supported NUMERICALLY) |

**Verdict.** (CV_S) in its L^∞ form is **NO-GO**, and not for lack of technique: series (84)_S diverges exactly at the dyadic points ρ = 2^j (Div2, PROVED). The mechanism is the dyadic quasi-covariance Q: at ρ = 2^j the cross coefficient turns into the mass ‖1_{[2^{−j}λ,λ]}ξ_n‖² (≈ constant), and Σλ_n²·(mass) is the HS norm of 1_I A_S, infinite. The diagonal cancellation of R186.009 Prop. C occurs at ρ = 1; dilation by 2 re-imports the same non-HS divergence at each 2^j. There is no alternating cancellation (S). Numerically the singularities are logarithmic: ε_S ∈ L^p_loc ∀p < ∞, which suffices for compactness (HS) of R′_S — the route remains alive in L² form, not L^∞.

## 1. Reconciliation (R, S: PROVED)

F_Sξ_n ∈ L²(ℝ₊) and P F_Sξ_n = A_Sξ_n = λ_nξ_n. Defining ξ_n^♯ := λ_n^{−1}F_Sξ_n gives ξ_n^♯ = ξ_n on (0,λ] and (1−P)F_Sξ_n = λ_n(1−P)ξ_n^♯, hence ζ_n = λ_n(1−P)ξ_n^♯/√(1−λ_n²). Substituting into ε_S(ρ) = Σλ_n(1−λ_n²)^{−1/2}⟨ξ_n|ϑ(ρ⁻¹)ζ_n⟩ (ρ ≥ 1):
 ε_S(ρ) = Σ_n λ_n²/(1−λ_n²) · ρ^{1/2}∫_{λ/ρ}^{λ} ξ_n(x) ξ_n^♯(ρx) dx,
because ξ_n lives on x ≤ λ and (1−P)ξ_n^♯(ρx) ≠ 0 only if ρx > λ. This is exactly CC Lemma 5.4 (ξ_n^{an} = ξ_n^♯; there Fξ_n is entire, here ξ_n^♯ is continuous at λ because the jump of ξ_n at λ makes c_kξ_n(y) = O(2^{−k}) uniformly for y ≥ λ/2). Both forms coincide: λ/√(1−λ²) is the weight with normalized ζ_n; λ²/(1−λ²) the weight with the continuation ξ^♯. The sign of λ_n disappears (S). The formal one-sided derivative: ε_S′(1⁺) = λΣ_n λ_n²/(1−λ_n²)ξ_n(λ)² (CC: Σλ²ξ(1)²/(1−λ²) ≈ 23, convergent by (100) and Slepian).

## 2. Quasi-covariance and divergence at 2^j (Q, Sp, NH, Div2: PROVED)

Q: K_S(2x,y) = Σ_{k≥1}c_k − c_0 = K_S(x,y) − (2c_0 − c_{−1}); iterate. For x ∈ [2^{−j}λ, λ], 2^j x ≥ λ and ξ_n^♯(2^jx) = λ_n^{−1}(F_Sξ_n)(2^jx) = ξ_n^♯(x) − λ_n^{−1}(B_jξ_n)(x), with ξ_n^♯(x) = ξ_n(x). Hence, with I_j = [2^{−j}λ, λ] and m_n := ‖1_{I_j}ξ_n‖²,
 T_n(2^j) = 2^{j/2}[λ_n²/(1−λ_n²) m_n − λ_n/(1−λ_n²)⟨1_{I_j}ξ_n, B_jξ_n⟩].
(Verified numerically term by term: error 1.4·10⁻⁴.)
Second summand absolutely convergent: B_j has an entire kernel on [0,λ]², hence B_j = B′B″ with B′,B″ HS, and Σ_n|⟨1_Iξ_n,B′B″ξ_n⟩| ≤ ‖B′^*1_IP‖_HS‖B″P‖_HS < ∞ (ξ_n an orthonormal basis of ran P including ker A_S); λ_n/(1−λ_n²) bounded.
NH: if 1_I A_S were HS it would have a kernel k ∈ L²(I×(0,λ)); taking χ ∈ C_c^∞(I°×(δ,λ−δ)), χ ≥ 0, the proof of R186.093 §5 (non-stationary phase + Riemann–Lebesgue with the distributional sum Σ_k c_k) gives ⟨k, χc_m⟩ → ½∫χ ≠ 0 and → 0 simultaneously. ∎ Hence Σ_nλ_n²m_n = ‖1_{I_j}A_S‖²_HS = ∞ and, since λ_n²/(1−λ_n²) ≥ λ_n², the first series (of nonnegative terms) diverges: ε_S(2^j) = +∞. ∎
Sp: ‖Pc_kP‖_{S_p}^p ≤ ‖Pc_kP‖^{p−2}‖Pc_kP‖²_HS ≤ (½2^{−k/2})^{p−2}λ², summable in k for p > 2; triangle inequality in S_p. ∎
Warning: Div2 concerns the pointwise value of the series at 2^j; that ε_S is unbounded in a neighborhood (not just at the point) is NUMERICAL (§3), not proved (uniform control of the tail in ρ is missing).

## 3. Numerics (NUMERICAL)

Code: scratchpad `cv.py`, `cv2.py`, `chk2.py`, `l1.py`. Gauss–Legendre Nyström on (0,½], n = 6000 (K = 10, 12), 14000 (K = 14, only λ_1); exact truncated kernel Σ_{k≤K}c_k − c_{−1}; ξ_n^♯ by Nyström interpolation; overlap integrals with 600 nodes. The resolvable index at K = 12 is n ≲ 1000.

λ_1(K): K = 6, 8, 10, 12, 14 → 0.9245, 0.9648, 0.9797, 0.9849, 0.9867; 1−λ_1 converges geometrically (ratio ≈ 0.35 per 2 steps) to ≈ 0.012: λ_1 ≈ 0.988, weight λ_1²/(1−λ_1²) ≈ 40 (dominates ε_S at generic ρ and explains the drift in K of generic values). λ_2 ≈ −0.511, λ_3 ≈ 0.302. |λ_n| (K = 12): n = 10, 30, 100, 300 → 0.145, 0.085, 0.039, 0.015 (≈ n^{−1/2}…n^{−0.8}, the excess decay is a truncation effect). Σ_{n≤N}λ_n² grows ≈ 0.093 per unit of log N (non-HS).

Edge mass (K = 12, n = 1..20): ‖1_{[λ/2,λ]}ξ_n‖² = 0.09, 0.62, 0.51, 0.51, …, 0.53 (→ ½: uniform spreading); mass on [0.9λ,λ]: 0.007–0.23 (mean ≈ 0.1); on [0.99λ,λ]: 10⁻⁴–0.07 (mean ≈ 0.01); ξ_n(λ)²: 0.13, 2.4, 3.7, 0.83, 5.2, 0.42, 0.95, 0.34, 8.4, …, 14.3 (n = 17), 0.003 (n = 13): no trend, no √n-type growth as in (100), no decay. D(N) := Σ_{n≤N}λ_n²ξ_n(λ)²/(1−λ_n²): 5.99, 6.27, 6.75, 7.18, 7.36 (N = 10, 30, 100, 300, 1000) — growing with log N and with K (5.90 → 7.48 from K = 10 to 12): derivative at 1⁺ logarithmically infinite.

Partial sums of ε_S(ρ) (K = 12; N = 10, 30, 100, 300, 1000):

| ρ | N=10 | 30 | 100 | 300 | 1000 | comment |
|---|---|---|---|---|---|---|
| 1.001 |.0030 |.0031 |.0034 |.0035 |.0034 | converges; ε/(ρ−1) = 3.4 |
| 1.01 |.0297 |.0307 |.0298 |.0301 |.0302 | ε/(ρ−1) = 3.0 |
| 1.1 |.245 |.247 |.248 |.247 |.247 | ε/(ρ−1) = 2.5 |
| 1.5 |.913 |.915 |.915 |.915 |.915 | converges |
| 1.9 | 1.477 | 1.439 | 1.436 | 1.435 | 1.436 | converges |
| 1.99 | 1.650 | 1.783 | 1.810 | 1.776 | 1.780 | converges (oscillates) |
| **2** | 1.658 | 1.805 | 1.951 | 2.074 | 2.167 | **grows ≈ 0.10·log N** (saturates at N ≈ resolution of K) |
| 2.01 | 1.661 | 1.796 | 1.824 | 1.789 | 1.793 | converges |
| 3 | 1.131 | 1.134 | 1.132 | 1.134 | 1.135 | converges |
| **4** | 1.511 | 1.824 | 2.130 | 2.384 | 2.545 | **grows ≈ 0.2·log N** |
| **8** | 1.557 | 2.071 | 2.570 | 2.968 | 3.188 | **grows ≈ 0.3·log N** |

Same code with K = 10: identical pattern (ε_S(2) = 1.71 saturated at N ≈ 300). Peak height above the shoulder, ε(2) − ε(1.9): 0.56 (K = 10), 0.74 (K = 12): grows with K. Profile: ε(2±0.01) − ε(1.9) ≈ 0.35, ε(1.97) − ε(1.9) ≈ 0.19 ⇒ β₁ ≈ 0.15 in log(1/|ρ−2|). Archimedean (kernel 2c_0, same code): ε_∞(1.1, 1.5, 2, 2.5, 4) = 0.200, 0.767, 1.027, 0.969, 0.458, convergence in 2–3 terms, no peaks.
Comparison with the linear prediction: no atom appears at ρ = 2 in ε_S − ε_∞; there is a positive logarithmic peak whose integrated weight converges as K increases. The prime comb is, as stated by R186.009 Δ, in the linear part; in ε_S what remains is its "non-HS shadow" (Div2).

## 4. Regimes (target point 4)

(a) edge mass O(1)·δ with |λ_n| ≍ n^{−1/2}: this is the observed regime. Absolute convergence of (84)_S at generic ρ fails for the trivial bound, but the series converges (fast) numerically through **decorrelation**: for fixed ρ ∉ {2^j}, ξ_n(x) and ξ_n^♯(ρx) oscillate at level-2^k frequencies that are incompatible, and the overlap decays; at ρ = 2^j the quasi-covariance Q exactly aligns the oscillations and the decorrelation disappears. There is no sign cancellation (S).
(b) edge mass n^{−a}, a > ½: refuted numerically (M) and, at ρ = 2^j, refuted by the proof (Div2): the relevant mass there is that of a fixed-length interval, ≈ ½, not an edge mass.
Obstacle to a proof of convergence at generic ρ: a theory of oscillation for lacunary cosine kernels is missing (there is no commuting Sturm–Liouville operator for A_S as in Slepian); the natural tool is the Littlewood–Paley decomposition by levels k and non-stationary phase between levels with frequency ratios ρ·2^{k−l} ≠ 1. OPEN.

## 5. Consequence

The positive part of the semilocal Sonin space Π_S **does** produce an unbounded remainder ε_S (at the dyadic points), but the defect is intrinsic to Π_S relative to the linear part and is not fixed by replacing the positive part with another one that differs from Π_S in trace: (Q₁Q₂Q₁)^N = Π_S + Σ_nλ_n^{2N}|ζ_n⟩⟨ζ_n| and, by Sp, for N ≥ 2 the difference is trace class with density bounded by Σλ_n^{2N} — this corrects the diagonal (Prop. d of R186.009) but **not** the dyadic peaks. For (M), however, it suffices that the kernel of R′_S on L²(I_T) be L²: logarithmic singularities are admissible.

## 6. Next lemma (precise formulation)

**Lemma L2_S (OPEN).** Let N ≥ 2 and Π^{(N)} := (Q₁Q₂Q₁)^N (positive, Π^{(N)} − Π_S trace class by Sp, ‖Π^{(N)} − Π_S‖ = λ_1^{2N}). Then for every T > 0:
 (i) Tr ϑ(f)Π^{(N)} = W_∞(f) − comb₂(f) + ∫ f(ρ⁻¹) ε_S^{(N)}(ρ) d*ρ, with ε_S^{(N)} = ε_S + Σ_n λ_n^{2N}⟨ζ_n|ϑ(ρ⁻¹)ζ_n⟩, the second summand continuous and bounded by ‖A_S‖_{S_{2N}}^{2N};
 (ii) ε_S^{(N)} ∈ L²([e^{−2T}, e^{2T}], d*ρ); concretely ε_S = Σ_{|j|≤ 2T/log2} β_j log⁺(1/|ρ−2^j|) + O_T(1) with β_j ≥ 0;
 (iii) consequently the remainder R′_S(h) = −∫c_h ε_S^{(N)} defines a **Hilbert–Schmidt** operator (in particular compact) on L²(I_T), and E_S = (positive form) − (HS).
Proof route: near 2^j, Q reduces T_n(ρ) to 2^{j/2}λ_n²/(1−λ_n²)⟨1_{I_j}ξ_n|ϑ(ρ2^{−j})-overlap with ξ_n^♯⟩ + absolutely convergent; it then suffices that (ii′) σ ↦ t(σ) := Σ_n λ_n²/(1−λ_n²)⟨1_{I_j}ξ_n|ϑ(σ)ξ_n^♯⟩ is in L² near σ = 1, a statement about the "diagonal kernel" of the non-HS operator 1_{I_j}A_S(1−A_S²)^{−1}A_S, which by levels k contributes O(1) in a window |σ−1| ≲ 2^{−k}: the sum Σ_k 1_{|σ−1|<2^{−k}} ≍ log(1/|σ−1|) ∈ L². What is missing: the uniform bound by levels (near-orthogonality between levels) — the same Littlewood–Paley lemma of §4.
Alternative if (ii) fails: there is no trace-equivalent positive part to Π_S with a regular remainder; one would have to change the semilocalization (truncate the comb: S_K with E_K = Σ_{k≤K}D_{2^k}, A_{S_K} trace class) and control K → ∞ in the quadratic form.

## Audit notes

- R is one line of algebra; the only analytic point is the continuity of ξ_n^♯ at λ (tail Σ_k O(2^{−k}) uses that ξ_n has bounded variation near λ, ARGUED via ξ_n = λ_n^{−1}A_Sξ_n and regularity on compacta of (0,λ]; not used in Div2).
- Div2 uses: R, Q (kernel identity verifiable by hand), NH (literal copy of R186.093 §5 with χ supported on I×(δ,λ−δ)), factorization B_j = B′B″ (entire kernel ⇒ trace class). It is divergence of the series at a point, not ε_S ∉ L^∞ in a neighborhood (that is NUMERICAL).
- Numbers with finite K: λ_1 drifts with K (weight 32 → ~40); the generic values of ε_S are not converged in K (error ~25%), but the profiles are stable; the peaks grow with K and saturate at N ≈ resolution of K, consistent with log-divergence in the limit.
- The slope β₁ ≈ 0.15 and the coefficient ≈ 0.10 in log N have not been reconciled exactly (factor ≈ 1.5; likely a nonlinear relation N ↔ |ρ−2|^{−1}). No limiting value is claimed.
- Neither (M), nor (TC_S), nor anything about the sign is claimed. No equivalence with RH.

## Note (R186_096)

* R, S, Q, Sp, NH, Div2 PROVED. Overclaim: Div2 is pointwise divergence at 2^j (measure zero); ε_S ∉ L^∞_loc is only NUMERICAL; L²_loc convergence OPEN. Absolute CV_S NO-GO PROVED via NH.
* Reconciliation with R183_025/029: no contradiction; the atom is the comb that (84)_S separates out; ε_S is the remainder by definition (an atom in ε_S would be double counting). The two-edge model measures something else. Record: "exact prime + continuous remainder" → "exact prime + remainder in L²_loc with peaks at 2^j" (CONDITIONAL). (M) ⟸ L2_S stated as L²_loc convergence of (84)_S + trace/series exchange CC (85)–(90).
