# Round 6, memo C: counting the near-null cluster through the joint symbol

Object. Notation of STATEMENT_001 §1 and ROUND_006_A. u_n = log n, N_T = {n ≥ 2 : u_n < 2T}, v_n = 2Λ(n)n^{−1/2},
X = e^{2T}, A_T = Σ_{N_T} v_n, M_T(τ) = Σ_{N_T} v_n cos(τu_n), m(τ) = Re ψ(¼ + iτ/2) − log π (even, increasing on
[0, ∞), m(0) = C_0 = −5.37218…; lem:mbounds, CITED), and the joint symbol

  s_T(τ) := m(τ) − M_T(τ),   q_T(F) := (1/2π) ∫ s_T |F̂|² dτ   (F ∈ L²(I_T) in the form domain).

On P_T the pole term vanishes and a_T = q_T|_{P_T} (Paper 47 prop:nodes, CITED). For δ ∈ ℝ,
m_δ^{L²}(T) and m_δ(T) count the eigenvalues below δ of q_T on L²(I_T) and on P_T (compact resolvent, CITED).
Since P_T has codimension 2, min–max gives λ_k(q_T|P_T) ≥ λ_k(q_T), hence m_δ(T) ≤ m_δ^{L²}(T).
Everything below is a size statement; it is comb-generic in the sense of §5 and carries no sign.

## 0. Corpus check

- ROUTES-TRIED-INDEX, grep "Landau", "Widom", "time-frequency", "Slepian", "almost periodic", "negative set",
  "prop:band", "Kronecker", "large values", "sublevel":
  * R186-bilateral / 06 §dead sub-routes: "Landau–Widom main term (predicts β_max > 1: NO-GO)". That entry uses the
    Landau–Widom *asymptotic* to predict the *value* of λ_A. Here Landau's trace/min–max device is used only as an
    *upper count* of eigenvalues below a level (no value of λ_A, no asymptotic main term). Different object (a count),
    different claim (an inequality); the recorded failure (wrong prediction of β_max) does not arise.
  * thm:X (P47; "PROVED mod LW, averaged") and W-loc (σ^(η) = min(σ_T, η) has the same negative set but negative
    form): both concern sign. Theorem A below is consistent with W-loc: it counts, it does not sign.
  * Slepian entries (G3A-153, R160_S4: decay/uncertainty on wells, refuted as sign tools): not used; Theorem A needs
    only the exact trace of a time–frequency limiting operator.
  * Almost periodicity (G6E-159 Bohr–Jessen, G7F-R160_S5, ES-12): those use a.p. recurrence in T or zero-side Bohr–Jessen
    to produce a sign. Theorem B below is an effective large-values bound for M_T on [0, Ω] (Montgomery–Vaughan mean
    value + sub-Gaussian torus moments); it decides no sign, uses no zero, and is not in the index (grep "Hilbert
    inequality", "Montgomery–Vaughan": no hit).
- Paper 47 prop:NC / cor:P3 (CITED): the same min–max + trace device for the archimedean form alone with a two-value
  minorant of m. Theorem A is its extension to the joint symbol with the layer-cake minorant (δ + η − s_T)_+; at
  δ = 0 and M_T ≡ 0 it reduces to prop:NC with a different constant.
- Paper 47 prop:band (CITED): {s_T < 0} is a finite union of bounded intervals inside [0, τ^lo], τ^lo > 2πe^{A_T};
  prop:negtrace(i): tr Q_T σ_−(D) Q_T = (2T/2π)∫σ_−. Theorem A is the counting companion of prop:negtrace(i).
- ROUND_006_A Theorem 5 (cap exp(2e^T(1+o(1)))) and §7 (the target lemma and the heuristic exp(O(T²))). ROUND_002_A
  Prop. M (sample identity; deep samples force near-integer coincidences): consistent with Lemma B.0 below, not used.

## 1. The scale-1/T averaging is exact, and the averaged comb is the comb (PROVED)

Lemma 1.1 (PROVED). Let φ ∈ L¹(ℝ) be even and real with ∫|φ(x)| log(2 + |x|) dx < ∞ and φ̂(u) := ∫φ(x)e^{−iux}dx = 1
for |u| ≤ 2T. Put s^φ := m∗φ − M_T. Then q_T(F) = (1/2π)∫ s^φ|F̂|² for every F ∈ L²(I_T) in the form domain, and
M_T ∗ φ = M_T.
Proof. G := |F̂|² is the Fourier transform of c_F, supported in [−2T, 2T]; φ ∗ G has transform φ̂·ĉ_F = ĉ_F, so φ∗G = G
(both continuous and integrable after the standard truncation of F to smooth compactly supported functions dense in
the form domain). Hence ∫(h∗φ)G = ∫h(φ∗G) = ∫hG for h = m (log growth, integrable against φ by the moment hypothesis)
and h = M_T. Finally M_T∗φ = Σ v_n φ̂(u_n) cos(τu_n) = M_T since u_n < 2T. ∎

Reading. The "comb averaged at scale 1/(2T)" in the target lemma of ROUND_006_A §7 is the comb itself whenever the
averaging is exact (φ̂ = 1 on the comb range). With a positive bump φ (φ̂ not ≡ 1 on [−2T, 2T]) the identity is lost
and the averaged comb Σ v_nφ̂(u_n)cos(τu_n) is strictly damped; no inequality between the two forms holds in general.
So smoothing gains nothing: the count is governed by the sublevel sets of s_T itself (or of m∗φ − M_T, which is
s_T up to an O(1/T) change of m). Theorem A is therefore stated with s_T.

## 2. Theorem A: a Landau-type count through the joint symbol (PROVED, explicit)

Theorem A (PROVED). For every T > 0, δ ∈ ℝ and η > 0,

  m_δ(T) ≤ m_δ^{L²}(T) ≤ (T/(πη)) ∫_ℝ (δ + η − s_T(τ))_+ dτ ≤ (T/(πη)) (δ + η − s_min) |{τ : s_T(τ) < δ + η}|,

where s_min := min s_T ≥ C_0 − A_T. The integral is finite: {s_T < δ+η} ⊂ {m < A_T + δ + η} is bounded.
Proof. Let E be the span of eigenvectors of q_T on L²(I_T) with eigenvalue < δ; for F ∈ E \ {0}, q_T(F) < δ‖F‖².
Since s_T ≥ (δ+η) − (δ+η−s_T)_+ pointwise and (1/2π)∫|F̂|² = ‖F‖²,
  ⟨KF, F⟩ := (1/2π)∫(δ+η−s_T)_+|F̂|² ≥ (δ+η)‖F‖² − q_T(F) > η‖F‖².
K = Q_T h(D) Q_T with h = (δ+η−s_T)_+ bounded, ≥ 0, compactly supported (s_T → +∞, since m → ∞ and |M_T| ≤ A_T). As in
the proof of prop:negtrace(i) (CITED), K = (h^{1/2}(D)Q_T)*(h^{1/2}(D)Q_T) is trace class with continuous kernel and
tr K = (2T/2π)∫h. By min–max, K has at least dim E eigenvalues > η, so η·dim E < tr K. The last inequality is
h ≤ (δ+η−s_min)1_{s_T<δ+η}; s_min ≥ C_0 − A_T because m ≥ C_0 and M_T ≤ A_T. The first inequality is interlacing. ∎

Corollary A.1 (PROVED). With h replaced by (δ+η−s^φ)_+ (Lemma 1.1) the same bound holds for every admissible φ;
the bound is the infimum over η > 0 and φ.

Corollary A.2 (recovery of the doubly exponential cap; PROVED). {s_T < δ+η} ⊂ {|τ| < τ′}, m(τ′) = A_T+δ+η, and
τ′ ≤ 2πe^{A_T+δ+η+1.172} (lem:mbounds(ii), CITED, as in ROUND_006_A Lemma 5.1). Hence
m_δ(T) ≤ (4T/η)(A_T + δ + η − C_0) e^{A_T+δ+η+1.172} = exp(4e^T(1+o(1))) — the arena scale. Theorem A is therefore
only as good as the measure of the sublevel set; §3 bounds that measure.

Evaluation (NUMERICAL, grid of 4·10⁶ points on [0, 2πe^{A_T+3}], η ∈ {0.05,…,2}): at δ = 0 the bound of Theorem A
(first form, best η = 1) is 13.98, 35.0, 174.5 at T = log 2, 0.9, 1.2; |{s_T < 0}| = 23.3, 48.6, 174.2. Against the
certified n_−(a_T|P_T) = 1, 2 at log 2, 0.9 (Paper 47 thm:index): the device loses the factor expected from a
Markov/trace count; it is not a sharp count, it is an explicit one.

## 3. Theorem B: a uniform large-values bound for the comb (PROVED, explicit)

Let P(τ) := Σ_{n∈N_T} v_n n^{iτ}, so M_T = Re P and |M_T| ≤ |P|. Group by primes: P(τ) = Σ_{p<X} h_p(τ log p),
h_p(x) := Σ_{k≥1, p^k<X} v_{p^k} e^{ikx}, a_p := h_p(0) = Σ_k v_{p^k}, S_T := Σ_{p<X} a_p². The p-blocks are handled
jointly: h_p is one trigonometric polynomial in τ log p, and Re h_p(x) ≤ a_p with a_p − Re h_p(x) ≥ 2v_p sin²(x/2).

Lemma B.0 (torus model; PROVED). For k ≥ 1 write P(τ)^k = Σ_{m<X^k} b_m m^{iτ}, b_m = Σ_{n_1⋯n_k=m} ∏v_{n_i} ≥ 0. Let
θ = (θ_p)_{p<X} be uniform on the torus 𝕋^{π(X)} and 𝒫(θ) := Σ_p h_p(θ_p). Then Σ_m b_m² = E|𝒫(θ)|^{2k}, and

  E|𝒫|^{2k} ≤ (2k)! (eS_T/k)^k ≤ e√(2k) (4kS_T/e)^k.

Proof. 𝒫^k = Σ_m b_m e^{i⟨ε(m),θ⟩}, ε(m) the exponent vector of m; distinct m give distinct characters (unique
factorization), so Parseval on the torus gives E|𝒫^k|² = Σ b_m². Write 𝒫 = U + iV. The summands Re h_p(θ_p) are
independent, of mean 0 (every frequency k ≥ 1) and with values in [−a_p, a_p]; Hoeffding's lemma (CITED) gives
E e^{λU} ≤ e^{λ²S_T/2}, likewise for V and for −U, −V. From cosh y ≥ y^{2k}/(2k)!: E U^{2k} ≤ (2k)! λ^{−2k} e^{λ²S_T/2},
and λ² = 2k/S_T gives E U^{2k} ≤ (2k)!(eS_T/2k)^k; same for V. (U²+V²)^k ≤ 2^{k−1}(U^{2k}+V^{2k}) gives the first bound;
the second is (2k)! ≤ e(2k)^{2k+1/2}e^{−2k}. ∎

Theorem B (uniform large values; PROVED). For every T > 0, Ω > 0, s > 0 and integer k ≥ 1,

  |{τ ∈ [0, Ω] : M_T(τ) > s}| ≤ |{τ ∈ [0, Ω] : |P(τ)| > s}| ≤ (Ω + 3π(X^k + 1)) · e√(2k) · (4kS_T/(e s²))^k.

Proof. Montgomery–Vaughan's mean value theorem (CITED: for distinct real λ_m with δ_m = min_{m′≠m}|λ_m − λ_{m′}|,
∫_0^Ω|Σ b_m e^{iλ_mτ}|²dτ = Σ|b_m|²(Ω + 3πϑ_m/δ_m), |ϑ_m| ≤ 1) applied to P^k with λ_m = log m, m ≤ X^k, and
δ_m ≥ log(1 + 1/m) ≥ 1/(m+1), gives ∫_0^Ω|P|^{2k} ≤ (Ω + 3π(X^k+1))Σb_m². Lemma B.0 and Chebyshev's inequality. ∎

Remark B.1 (Bohr density; PROVED). By Kronecker–Weyl (CITED; log p ℚ-independent) and the portmanteau inequality
for the closed set {Re 𝒫 ≥ s}, limsup_{Ω→∞} Ω^{−1}|{τ ≤ Ω : M_T ≥ s}| ≤ P(Re 𝒫 ≥ s) ≤ e^{−s²/(2S_T)} (Hoeffding). This is
the Gaussian tail of ROUND_006_A §7, but with no rate in Ω. Theorem B is its effective form, with the price that
the moment order k is tied to the window: the error term 3πX^k is negligible only for Ω ≳ X^k = e^{2kT}.

Size of S_T (PROVED given Mertens, CITED). a_p ≤ 2 log p · p^{−1/2}/(1 − p^{−1/2}), so
S_T = 4Σ_{p<X} log²p/p + O(1) = 2(log X)²(1+o(1)) = 8T²(1+o(1)).

## 4. The sublevel set and the cluster (PROVED given PNT and Mertens, CITED)

Corollary C (PROVED). For τ ≥ 2π put L(τ) := log(τ/2π) − 0.172 − δ − η. Then

  {τ ≥ 0 : s_T(τ) < δ + η} ⊂ [0, τ_1) ∪ {τ ∈ [τ_1, τ^lo_{δ+η}] : M_T(τ) > L(τ)},  τ_1 := 2πe^{1.172+δ+η},

(lem:mbounds(ii), CITED: m(τ) ≥ log(τ/2π) − 0.172 for τ ≥ 2π), and, with dyadic blocks [R, 2R] and any choice of k = k(R),

  |{τ ≥ 0 : s_T < δ+η}| ≤ 2τ_1 + 2 Σ_{R = 2^jτ_1 ≤ τ^lo} (2R + 3π(X^{k(R)}+1)) e√(2k) (4kS_T/(e L(R)²))^{k}.

Proof. Evenness of s_T; Theorem B with Ω = 2R and s = L(R) ≤ L(τ) on the block. ∎

Corollary D (asymptotic size; PROVED given PNT and Mertens). Choosing k(R) = ⌊log R/(2T)⌋ (so X^k ≤ R),

  |{s_T < δ + η}| ≤ exp(2e^T(1 + (log T + log 4 − 1 + o(1))/T)),   hence (Theorem A, η = 1)
  m_δ(T) ≤ exp(2e^T(1 + (log T + 0.39 + o(1))/T)).

Proof. Put ℓ = log R. With S_T = 8T²(1+o(1)) and L(R) = ℓ(1+o(1)) on the relevant range, the block term is
exp(ℓ − (ℓ/2T) log(eℓ/(16T)) + O(log ℓ)) (blocks with eℓ ≤ 16T contribute ≤ e^{O(T)}). The exponent
g(ℓ) = ℓ − (ℓ/2T)log(eℓ/16T) has g′(ℓ) = 1 − (log(eℓ/16T) + 1)/(2T) > 0 for ℓ < (16T/e)e^{2T−1}, which contains the
whole range ℓ ≤ log τ^lo = A_T + O(1) = 4e^T(1+o(1)) (PNT). So the largest block is the top one and
g(4e^T) = 4e^T − (2e^T/T)(T + 1 + log 4 − log 16 − log T) = 2e^T(1 + (log T + log 4 − 1)/T). There are O(A_T) blocks,
and the factor (T/π)(A_T + δ + 1 − C_0) of Theorem A is e^{O(T)}. ∎

Comparison.
- ROUND_006_A Theorem 5: m_δ ≤ exp(2e^T(1 + O(e^{−T/2}))). Corollary D reaches the same leading exponent 2e^T by an
  independent route (symbol sublevel + effective large values, no overlap bound), and is weaker in the second term
  by the factor exp(2e^T(log T + 0.39)/T). Neither is single exponential.
- Paper 47 cor:arena: lower count exp(4e^T(1+o(1))) for modes below A_T (a different level); Corollary A.2 is that
  scale; Corollary D halves the exponent.
- Heuristic exp(O(T²)) of ROUND_006_A §7: it uses the Gaussian tail e^{−L²/(2S_T)} of Remark B.1 at L ≈ log τ up to
  L ≈ A_T, which requires moments of order k ≈ L²/S_T ≈ e^{2T}/(4T²) at heights τ ≈ e^L; Theorem B then has error
  X^k = exp(e^{2T}/(2T)) ≫ e^{4e^T} = top of the band. So the heuristic is out of reach of every bound of the form
  "mean value on [0, Ω] with error O(X^k) for k-th powers".

Limit of this class (ARGUED; the computation is §4, the class statement is not a theorem). Within the class
"Theorem A + a moment/large-values bound for M_T whose off-diagonal error is controlled by the spacing of
{log m : m ≤ X^k}" the cap cannot go below exp(2e^T(1+o(1))): at the top block ℓ ≈ 4e^T the admissible order is
k ≤ ℓ/(2T) and the saving is exp(−k log(eℓ/16T)) = exp(−2e^T(1+o(1))). Improving it requires counting near-coincidences
m ≈ m′ (m, m′ ≤ X^k products of k elements of N_T) beyond the trivial spacing 1/(m+1), i.e. a large-sieve bound that
uses the multiplicative structure of the products — the semiring interplay at m ≈ m′, not their mere separation.

## 5. Falsifier test

Rule 4 applies to sign steps; nothing here is a sign step. Checked anyway:
(a) cΛ: Theorems A, B, Corollaries C, D hold with A_T, S_T scaled by c, c² (the Hoeffding range scales by c);
(b) a_P: deleting n < P lowers A_T, S_T; all statements hold;
(c) Beurling system with zeta continuing to the line: Theorem A holds verbatim (it uses only the symbol). Theorem B
uses integrality twice — distinct products give distinct characters (unique factorization) and the spacing
|log m − log m′| ≥ 1/(m+1) of integers — and both can fail for generalized integers (non-unique factorization,
arbitrarily close generalized integers). So Theorem B is specific to ℕ; its conclusion needs replacement, not merely
re-proof, for (c). This is a size statement, so surviving or failing (c) is not a diagnosis;
(d) finite modification of v_n: O(1) changes of A_T, S_T, same conclusions.
The bounds are size statements: they hold for all four falsifiers where proved, as they must.

## 6. What failed

- The averaged comb M̃_T at scale 1/(2T) of ROUND_006_A §7 equals M_T under exact averaging (Lemma 1.1): no smoothing
  gain exists.
- Mean-square (k = 1) gives measure ≲ ΩS_T/(log Ω)², useless at Ω ≈ e^{A_T}, as predicted in the task.
- The Gaussian tail e^{−L²/2S_T} is available only as a Bohr density (Remark B.1); every effective version tested
  (Theorem B) ties k to log Ω/(2T), giving exp(2e^T(1+o(1))), not exp(O(T²)).

## 7. Next lemma (OPEN)

Large-sieve count of near-coincident products. For k ≥ 1 and ν > 0 let
  𝒩_k(ν) := Σ_{m≠m′ ≤ X^k, |log(m/m′)| < ν} b_m b_{m′}.
Fejér-weighted, ∫ w_ν(τ−c)|P|^{2k}dτ = (2π/ν)(Σb_m² + Σ_{0<|log m/m′|<ν}(1 − |log(m/m′)|/ν)b_mb_{m′}) exactly. Target:
𝒩_k(ν) ≤ C^k Σb_m² for ν ≥ X^{−θ k} with some θ < 1 (or ν ≥ e^{−ck T²}), uniformly in k ≤ e^{2T}/T². With θ < 1 the
window shrinks to X^{θk}, the admissible order at the top block becomes k ≈ ℓ/(2θT), and the cap improves to
exp((4 − 2/θ)e^T(1+o(1))) (ARGUED, same computation as Corollary D); if the window can be taken independent of k
(ν ≥ e^{−O(T)} with constant C^k) the order k ≈ L²/S_T becomes admissible and the heuristic exp(O(T²)) follows. The object is the distribution of the ratios m/m′ of k-fold products of prime powers
below X near 1 — a multiplicative-energy problem on N_T^k, to be attacked through the p-block structure
(m/m′ = ∏p^{e_p}, |Σe_p log p| < ν with Σ|e_p|log p ≤ 2kT).

## Result

PROVED piece (size of the near-null cluster through the joint symbol; comb-generic, no sign).

## What was proved

- Lemma 1.1: exact scale-1/T averaging leaves q_T unchanged and fixes the comb (M̃_T = M_T).
- Theorem A: m_δ(T) ≤ (T/(πη))∫(δ+η−s_T)_+ ≤ (T/(πη))(δ+η−C_0+A_T)|{s_T < δ+η}| for all δ, η > 0 (explicit; numbers
  13.98, 35.0, 174.5 at δ = 0, T = log 2, 0.9, 1.2, NUMERICAL evaluation of the proved bound).
- Lemma B.0 / Theorem B: |{τ ≤ Ω : M_T > s}| ≤ (Ω + 3π(X^k+1)) e√(2k)(4kS_T/(es²))^k for every k, with p-blocks
  handled jointly (Hoeffding on the torus, Montgomery–Vaughan CITED), S_T = 8T²(1+o(1)).
- Corollaries C, D: |{s_T < δ+η}| and m_δ(T) ≤ exp(2e^T(1 + (log T + 0.39 + o(1))/T)) (given PNT, Mertens).

## What failed and why

The smoothed-symbol gain does not exist (Lemma 1.1). The effective large-values bound ties the moment order to the
window length through the integer spacing 1/(m+1), so the cap stays at exp(2e^T(1+o(1))) — the same leading order as
ROUND_006_A Theorem 5, not the heuristic exp(O(T²)). The obstruction is the off-diagonal error term X^k of the mean
value theorem (ARGUED as a class limit).

## Next concrete step

Bound the multiplicative energy 𝒩_k(ν) of k-fold products of N_T near ratio 1 (§7), beyond the trivial spacing;
any θ < 1 in ν ≥ X^{−θk} improves the cap to exp((4 − 2/θ)e^T(1+o(1))); a k-independent window gives exp(O(T²)).
