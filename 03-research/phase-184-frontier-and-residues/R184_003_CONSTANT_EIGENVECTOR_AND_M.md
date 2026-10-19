# R184.003 — Is the constant an eigenvector? (Part A) and the estimate (M) (Part B)

RH is not claimed, nor the closure of D. Minimal script: `scratchpad/r184_003_par.py` (session d9ffd571…),
which reuses `r183_030_inertia.py` (the same one as R183_030/032).

## 0. Verdict

* **Part A: hypothesis REFUTED; identity EXPLAINED.** The constant (its Riesz representative e
  of ℓ in 𝒫_T) is **not** an eigenvector of Q_T. Its weight is |⟨e,v₁⟩|² ≈ 0.50–0.53 and |⟨e,v₃⟩|² ≈ 0.19–0.21.
  The identity λ₁(Q_T|ker ℓ ∩ 𝒫_T) = λ₂(Q_T|𝒫_T) to 8 digits comes from **parity**:
  * the form, the metric and 𝒫_T are invariant under h ↦ h(−·), and ℓ is even;
  * the second eigenvector is **odd**, and therefore belongs to ker ℓ;
  * the even sector of ker ℓ starts far above λ₂.
  Theorem A.1 (PROVED) gives the structure and Corollary A.2 the exact condition, which is an
  inequality between sectors. The consequences "exact rank-one correction" and "collapse of
  a_min" are **false**. With the prime 2 the identity ceases to hold, because the ground state
  becomes odd.
* **Part B: (M) remains OPEN.** I prove three things:
  * (B.1) an exact equivalence: (E′_loc) ⟺ the smoothing of r_p at scale 1/T is in L²(ds),
    with a positive kernel;
  * (B.2) the bound |r_p ∗ K| ≤ C log(2+|s|), which gives κ_p ∈ H^{−1/2−η}(−2T,2T) for all η > 0 and is
    CONDITIONAL on a trace bound cited from CC;
  * the reduction to a single estimate (M_w), weaker than (M).

## 1. Normalization (that of R183_030)

* h = ½ξ − ξ′, with ξ ∈ H¹_0(−T,T), and the metric is ‖ξ‖² = ∫|ξ|². By Plancherel,
  ‖ξ‖² = (1/2π)∫|ĥ(s)|²/(¼+s²) ds.
* Archimedean form: Q_T(h) = E_∞(h) = (1/2π)∫ m(s)|ĥ(s)|² ds, with m(s) = Re ψ(¼+is/2) − log π
  (R183_015/018).
* 𝒫_T = {h ∈ L²(−T,T) : ∫h e^{±t/2} = 0}. One restriction is automatic because h = (½−D)ξ with ξ of
  compact support; the other is `cp` in the script.
* ℓ(h) = ∫h = ĥ(0) = ½ξ̂(0). It is `cl` in the script.
* In this normalization, λ₂(𝒫_{0.78}) = 1.05229954 (M = 28).

## 2. Part A

### 2.1 Data (M = 28 / 40; same quadrature as R183_032)

| T | λ₁ | λ₂ | λ₃ | parity v₁..v₄ | \|⟨e,v_k⟩\|², k=1..4 | even min ∩ ker ℓ | min ker ℓ |
|---|---|---|---|---|---|---|---|
| 0.60 | −0.1611 | 17.0882 | 67.35 | + − + − | 0.532, 0, 0.192, 0 | 48.69 | 17.0882 |
| 0.70 | −3.4447 | 5.96938550 | 36.88 | + − + − | 0.517, 0, 0.203, 0 | 25.09 | 5.96938550 |
| 0.78 | −4.6931 | 1.05229954 | 22.57 | + − + − | 0.502, 0, 0.214, 0 | 14.14 | 1.05229954 |

For M = 40 the figures change (λ₂(0.78) = 1.0193), but the structure is the same and the equality is
kept exact for every M. In the eigenbasis, e has **identically zero** odd coefficients.
The even ones are not: e is not an eigenvector.

### 2.2 Theorem A.1 (PROVED): reflection symmetry

Let (Rh)(t) = h(−t).

(a) R is an isometry of 𝒫_T in the ξ metric, and also in L²(h).

(b) Q_T(Rh) = Q_T(h). The same holds for the full semilocal form W_S = E_∞ + Σ prime terms.

(c) ℓ∘R = ℓ.

Consequently, 𝒫_T = 𝒫⁺ ⊕ 𝒫⁻ (even and odd), and the decomposition is orthogonal for the metric
and for the form. Moreover 𝒫⁻ ⊂ ker ℓ and e ∈ 𝒫⁺.

*Proof.*
* (a): ∫(Rh)e^{±t/2} = ∫h e^{∓t/2}, so R permutes the two Tate restrictions and preserves
  𝒫_T. Also (Rh)^(s) = ĥ(−s), and the weight 1/(¼+s²) is even, so the ξ metric is preserved. In the
  ξ variable, R acts as ξ ↦ (½−D)^{−1}R(½−D)ξ, which has support in (−T,T) precisely because
  Rh ∈ 𝒫_T.
* (b): m is even, which gives the archimedean part. For the primes, c_{Rh}(a) = ∫h(−x)h(−x−a)dx =
  c_h(−a) = c_h(a), because h is real.
* (c): immediate.
* Orthogonality: R is a unitary involution that commutes with the operator of the form. If h is even and
  g odd, ℓ(g) = ℓ(Rg) = −ℓ(g), so ℓ(g) = 0. ∎

### 2.3 Corollary A.2 (PROVED): exact count and criterion for the equality

Let μ₁ be the minimum of Q_T over ker ℓ ∩ 𝒫_T. Let λ₁^± be the minima of Q_T on 𝒫^± and μ₁⁺ the
minimum on ker ℓ ∩ 𝒫⁺. Then:

(i) μ₁ = min(λ₁⁻, μ₁⁺) and n₋(ker ℓ ∩ 𝒫_T) = n₋(𝒫⁻) + n₋(ker ℓ ∩ 𝒫⁺), with
    n₋(𝒫⁺) − 1 ≤ n₋(ker ℓ ∩ 𝒫⁺) ≤ n₋(𝒫⁺).

(ii) **Criterion.** μ₁ = λ₂(𝒫_T) holds **exactly** if and only if min(λ₁⁻, μ₁⁺) = λ₂. In
     particular it holds if:
     * λ₁ is even, with λ₁ = λ₁⁺;
     * λ₂ = λ₁⁻, i.e. the second eigenvector is odd;
     * μ₁⁺ ≥ λ₁⁻.

     By interlacing in 𝒫⁺, μ₁⁺ ≥ λ₁⁺ and μ₁⁺ ≤ λ₂⁺.

(iii) **Without parity the equality would be non-generic.** In general, μ = λ_k is a root of the secular
      equation Σ_k |e_k|²/(λ_k − μ) = 0 only if e_k = 0, which has codimension 1. Parity
      forces e_k = 0 at **all** odd indices simultaneously. That is why the coincidence is exact
      for every M and every symmetric quadrature: the Gauss–Legendre rule is symmetric and the
      Legendre basis respects parity.

*Proof.* (i) is the orthogonal decomposition of Theorem A.1 plus the codimension-1 Cauchy interlacing
within 𝒫⁺ (ℓ|_{𝒫⁺} ≠ 0, because e ∈ 𝒫⁺ \ {0}). (ii) follows from (i). ∎

**Status of the hypotheses of (ii) in the observed regime:**
* They are NUMERICAL for T ∈ [0.6, 0.80]: v₁ is even, v₂ is odd, and μ₁⁺ ≈ 14–49 ≫ λ₂.
* They are not proved analytically.
* "v₁ is even" is plausible by a Perron–Frobenius/Courant-type argument (the fundamental mode
  has no nodes), but the form is not local, so it remains **OPEN**.

### 2.4 Refutation of the "constant = eigenvector" hypothesis (NO-GO)

* **Statement refuted:** P_{𝒫} m(D) 1 = λ·1 + a e^{t/2} + b e^{−t/2}.
* **Refutation:** if this held, e would be an eigenvector and |⟨e,v_k⟩|² would be 0 for k ≥ 2. The data
  give a weight ≈ 0.20 at v₃ (stable in M, T and the quadrature) and ≈ 0.5 at v₁. This is incompatible.
* **Structural reason:** the kernel of E_∞ in t is the archimedean Weil distribution, W_∞(x) =
  (finite part of) −e^{|x|/2}/(e^{|x|}−1)·(…) + log π·δ. Applied to 1_{(−T,T)}, it gives an even
  function of t that is **not constant**: it grows toward the edges because of the 1/|x| singularity
  of W_∞ at 0 when integrating over a truncated window. The difference from a constant is not in
  span{e^{t/2}, e^{−t/2}}, which is a 2-dimensional space that cannot absorb a profile with a
  logarithmic singularity at ±T. This sentence is heuristic; the refutation is the one from the data.
* **Reconciliation with CC (Fact 6.5, α ≈ 0.94865):** there the operator (K_I) and the metric are
  different, and α ≠ 1. There too the constant is not an eigenvector. **There is no natural metric in which
  it is.** For any metric G invariant under R, Theorem A.1 only guarantees e ⊥ 𝒫⁻. The
  observed exactness does not depend on the metric: parity holds equally in L²(h) and in the ξ metric.

### 2.5 Corrected consequences (the ones requested, with their label)

1. "On ker ℓ ∩ 𝒫_T the form is ≥ λ₂": **false in general**. It is true exactly under
   criterion A.2(ii). What is indeed PROVED is the Cauchy inequality μ₁ ≥ λ₁.
2. "n₋(ker ℓ) = n₋(𝒫_T) − 1 while λ₁ < 0 < λ₂": this is true, but trivial, by interlacing. It does not
   need alignment.
3. "The exact rank-one correction of CC on ĝ(0) is exact and the a_min formula collapses": **NO-GO**.
   e is not an eigenvector. a_min keeps its secular form, which simplifies only upon removing the
   odd modes (e_k = 0 for odd k).
4. **True mechanism of T₂.** The threshold on ker ℓ is the T at which the **odd fundamental**
   λ₁⁻(T) crosses 0. "A single aligned direction" means that the negative archimedean direction
   is even, and the functional ℓ, which is also even, removes it while it is the only one. The
   odd directions are not seen by any even functional. Hence the correct threshold is T₂ = inf{T : λ₁⁻(T) < 0},
   with the numerical bound T₂ < 0.8027 of R183_032, which has not converged.

### 2.6 Semilocal (with primes)

* Theorem A.1(b) holds for W_S. The equality, however, **fails** when the prime changes the
  parity of the fundamental.
* T = 0.60, S = {∞,2} (M = 28): λ₁ = −2.75494381, and the minimum on ker ℓ is **−2.75494381**, which is
  equal to λ₁ and not to λ₂. The fundamental is odd (ℓ does not see it) and n₋(ker ℓ) = n₋ − 1 = 1.
* There the "aligned direction" ceases to exist: the term for 2 makes an odd direction more negative.
* With the full S(T) at T = 0.75 and 0.80, n₋ = 0 and the coincidence min ker ℓ = λ₂ returns
  (1.2509·10⁻⁷ versus 1.2509·10⁻⁷). This is compatible with A.2(ii).
* The question "is B_p 1 = c_p·1 + boundary terms removed by Tate?" becomes moot. The
  boundary terms c_h(a) in the window are not a combination of e^{±t/2}: 1_{(−T,T)} ∗ (δ_a + δ_{−a})
  is a step function with jumps at ±(T−a). But this is unnecessary: parity explains everything.

## 3. Part B: the estimate (M) of R183_029

Notation from R183_029: S = {∞,p}, a = log p, ε = p^{−1/2}, r_p = ρ_E − μ_D and κ_p = F^{−1}r_p. ρ_E is
bounded and F^{−1}ρ_E = aΣ_k ε^{|k|}δ_{ka}.

### 3.1 Lemma B.1 (PROVED): equivalence via positive smoothing

* Let ψ ∈ C_c^∞ real, with ψ > 0 on (−T−η, T+η) and support in [−T−2η, T+2η].
* Let φ = ψ ∗ ψ̃. Then φ̂ = |ψ̂|² ≥ 0, φ > 0 on [−2T,2T] and supp φ ⊂ [−2T−4η, 2T+4η].
* Let K := φ̂/2π.

For every tempered distribution r with κ = F^{−1}r:

  κ ∈ L²(−2T−4η, 2T+4η) ⟹ r ∗ K ∈ L²(ℝ, ds) ⟹ κ ∈ L²(−2T, 2T).

*Proof.* r ∗ K = F(φκ). By Plancherel, ‖r ∗ K‖² ≍ ‖φκ‖², and 0 < φ ≤ ‖ψ‖² on the support. φ is
bounded below on [−2T,2T]. ∎

Since T can be enlarged slightly, **(E′_loc) for all T' < T₀ ⟺ (M_w) for all T' < T₀**:

  **(M_w)** ∫ |(μ_D − ρ_E) ∗ K(s)|² ds < ∞.

(M_w) is weaker than (M): it does not require phase structure and does no integration by parts. It is
also necessary. The reduction is exact.

### 3.2 Proposition B.2 (CONDITIONAL on CC (43)/(83) uniform): logarithmic bound

  |r_p ∗ K (s)| ≤ C_{T,p} log(2+|s|).

Hence κ_p ∈ H^{−1/2−η}(−2T,2T) for all η > 0 (by B.1 with weight (1+s²)^{−1/2−η}).

*Proof.*
* **Upper bound.** Since K ≥ 0, Prop 3.1(b) of 029 gives r_p ∗ K ≤ a(1+ε)/(1−ε)·∫K.
* **Lower bound.**
  * Prop 3.1(c) of 029, without the positive term, gives r_p ≥ ρ_E − μ_{K'}, and hence
    r_p ∗ K ≥ −μ_{K'} ∗ K.
  * With g_s := ψ e^{is·}, one has μ_{K'} ∗ K(s) = Tr(ϑ(g_s)Π_{K'}ϑ(g_s)^*)/2π.
  * By Theorem A(i) of 029, Π_{K'} ≤ PP̂_bP, so μ_{K'} ∗ K(s) ≤ Tr(ϑ(g_s)PP̂_bPϑ(g_s)^*)/2π.
  * The trace on the right is that of CC (43) plus the archimedean term of density θ′(s)/π ~
    (1/2π)log|s|. **CITED:** CC (43)/(83). The uniformity in s of the remainder for modulated g_s is
    taken from the explicit Weil form in CC and has not been reverified here. That is why the label
    is CONDITIONAL.
* **Conclusion.** |r_p ∗ K| ≤ C log(2+|s|), and ∫ log²(2+|s|)(1+s²)^{−1/2−η} ds < ∞. ∎

### 3.3 What is missing (OPEN): the single estimate

Between B.2 and (M_w) one must still gain half a derivative plus the logarithm. Equivalently, one must prove:

  **(M_w′)** (μ_D − ρ_E) ∗ K ∈ L²(ds), i.e. that the "boundary Sonin" D reproduces, after
  smoothing at scale 1/T, the density ρ_E with a square-integrable error.

The two-boundary model (Prop 3.3 of 029) suggests an error ≍ |s|^{−1}. That error is L² and also
satisfies (M_w′) **with margin**: the oscillating part e^{−L(s)/2}cos(…), upon convolving with K of
support |t| ≤ 2T < L(s), becomes O(|s|^{−N}) in the model. This is what justifies (M_w′) over
(M): the non-integrable amplitude |s|^{−1/2} of 029 §3.4 **disappears** upon smoothing.

The missing step is a trace comparison, in frequency windows of width O(1/T), between
Π_D and the model with L = L(S):

  Σ_S ‖ 1_{[S,S+1]}(ϑ-frequency)(Π_D − Π_{D_{L(S)}}) ‖_1² < ∞.

For that comparison one still needs Γ = 1 − Y to be bounded below at high
frequency (R183_029 §3.2). Neither that bound nor the comparison is proved. **Neither zeros
nor other primes are involved.**

### 3.4 What I do NOT prove

* I do not prove κ_p ∈ L² away from t = 0 nor outside a neighborhood of ±log p. Without (M_w′), bound B.2 does not
  localize in t: it is a global Sobolev-type bound.
* I do not attempt a stronger statement, for lack of a proof.

## State

| Statement | Label |
|---|---|
| A.1: reflection invariance of 𝒫_T, ξ metric, E_∞ and W_S; 𝒫⁻ ⊂ ker ℓ | PROVED |
| A.2(i): μ₁ = min(λ₁⁻, μ₁⁺); count n₋ by sectors | PROVED |
| A.2(ii): exact criterion for μ₁ = λ₂ | PROVED |
| v₁ even, v₂ odd, μ₁⁺ ≫ λ₂ for T ∈ [0.6, 0.8], S = {∞} | NUMERICAL (M = 28, 40) |
| v₁ even in general (no nodes) | OPEN |
| "The constant is an eigenvector of P_𝒫 m(D) P_𝒫 mod Tate" | NO-GO (refuted: weight 0.2 at v₃) |
| Exact rank-one correction / collapse of a_min | NO-GO |
| T₂ = first crossing of the odd fundamental | PROVED (as identification); value only numerical, < 0.8027 |
| Semilocal equality {∞,2}, T = 0.6 | fails: fundamental odd, min ker ℓ = λ₁ (NUMERICAL) |
| B.1: (E′_loc) ⟺ (M_w) | PROVED |
| B.2: \|r_p ∗ K\| ≤ C log; κ_p ∈ H^{−1/2−η}_loc | CONDITIONAL (uniformity of CC (43)/(83), CITED) |
| (M), (M_w′) | OPEN (single estimate: trace comparison Π_D vs L(S) model by windows + Γ bounded below) |
| Row D | OPEN; not claimed |

## For the audit

1. **Parity in the variable ξ.** R is not the reflection of ξ. Check that ξ_R = (½−D)^{−1}R(½−D)ξ
   has support in (−T,T) **only** because Rh satisfies both Tate restrictions. Also that the
   script, which imposes a single explicit restriction (`cp`), describes exactly 𝒫_T.
2. **Symmetric quadrature.** The exactness to 8 digits requires the discretization to respect R.
   Gauss–Legendre and Legendre × (1−u²)² are symmetric. Check that the discretization of R in the
   basis (which mixes coefficients through (½−D)^{−1}) does not break parity at the matrix level. The
   data e_k = 0 (k even) to machine precision suggest it does not break it.
3. **A.2(ii) is not a theorem for all T.** If for some T the fundamental were odd in S = {∞},
   the identity would fail. Look for it at T > 0.8, where the numerics are not reliable.
4. **B.2:** verify the uniformity in the modulation s of the cited trace formula. If the remainder
   is not O(1) uniformly, the bound loses the logarithm or worse, and B.2 falls to OPEN.
5. **B.1** uses that the window is enlarged by 4η. Check that Corollary C′ of 029 tolerates T' > T
   (the restriction T < ½log(next prime) is open).
6. Under (M_w′), the atom −log 2/√2 at ±log 2 is in ρ_S − ρ_∞ and not in r_p (editor's note of 029).
   This file does not change that.

## Note (R184_091)

* "T₂ = first crossing of the odd fundamental" is downgraded to CONDITIONAL (μ₁⁺ ≥ 0 up to that point is only numerical). λ₁, λ₂ not converged in M (λ₂(0.78): 1.0523 → 1.0193 with M=40).
* (M_w′) must include that μ_D exactly cancels the atoms of F⁻¹ρ_E at 0 and ±k log p.
