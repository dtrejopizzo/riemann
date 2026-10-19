# N_BUILD_002 — The polar term is the Dirichlet resolvent; (N^♯) on the finite space H^♯_η; the Chebyshev segment expansion

Pen and paper. Notation of N_BUILD_001 and L2_BUILD_006/007. 𝒯₀ (ground-state test) is left to the track (L2).

## Corpus check
grep (whole corpus + MAP_D + grid): "Dirichlet resolvent", "(¼−∂²)^{-1}", "resolvente", "H_η", "Schur on archimedean
eigenspace", "Stieltjes", "E(u)", "segment", "ψ(y) − y", "Euler factor bound".
- No memo writes 𝔭 as the quadratic form of the Dirichlet resolvent of ¼−∂² (found only the Fourier form, 114_d_133 (2.2)).
- L2_BUILD_007 §3: Schur on H_η = span{μ_j(𝔞_∞|P_T) < η}, η > A_T (variant of thm:coer-schur). Used, not rebuilt.
- R160_PD_R1 Thm E(iii): Stieltjes kernel ω = ½c − c′ (corpus-known; used in §3).
- phase-146 R146_003 §D.47: single-prime Euler bound τ_p ≥ 2/(√p+1) (known; only cited in §4).

## 1. Resolvent identity — NEW, PROVED
Let R := (¼ − ∂²)^{-1} with Dirichlet conditions on I_T (positive, compact; eigenvalues r_j = (¼ + (πj/2T)²)^{-1}, j ≥ 1,
eigenvectors sin(πj(t+T)/2T)). For F ∈ P_T: 𝔭(F) = ⟨F, RF⟩. Hence on P_T ∩ D_T
  **𝔞_T(F) = ⟨F,(A_∞ + R)F⟩ − 𝓕_T(F)**, A_∞ the operator of 𝔞_∞ = C₀‖F‖² + 𝔈(c_F).
*Proof.* F = (¼−∂²)G with G ∈ H²_0(I_T) (thm:nyq-cone), so G = RF (G satisfies the Dirichlet problem; uniqueness since
¼−∂² ≥ ¼ on H¹_0). ⟨F,RF⟩ = ⟨(¼−∂²)G, G⟩ = ¼‖G‖² + ‖G′‖² = 𝔭(F) (N_BUILD_001 (A)). ∎
Remark. Off P_T the identity fails (F ∉ Ran(¼−∂²)|_{H²_0} — exactly the two Tate directions e^{±t/2}, which span
ker(¼−∂²)); so P_T = the domain on which the polar kernel e^{|t−s|/2} acts as −R. Equivalently: the Green kernel of
¼−∂² on I_T with Dirichlet conditions equals e^{−|t−s|/2} minus a rank-2 kernel in span{e^{±t/2}}⊗span{e^{±s/2}}, and P_T
annihilates that rank-2 part.
Consequence (PROVED): with μ^♯_j the eigenvalues of (A_∞ + R)|_{P_T}, μ_j ≤ μ^♯_j ≤ μ_j + r_1 ≤ μ_j + 4 (min–max, 0 ≤ R ≤ 4).

## 2. (N^♯) on a finite space — PROVED reduction
Let η > A_T + 4 and H^♯_η := span{eigenvectors of (A_∞+R)|_{P_T} with μ^♯_j < η} (finite by §1 and L2_007 §1).
(a) On (H^♯_η)^⊥ ∩ P_T ∩ D_T: 𝔞_T ≥ (η − A_T − 4)‖F‖², since |𝓕_T(F)| = |Σv_n w(log n) + 𝔭(F)| ≤ (A_T + 4)‖F‖².
(b) Hence (thm:coer-schur (i)–(iii) verbatim, as in L2_007 §3): λ_A(T) ≥ 0 ⟺ the Schur complement 𝒮^♯_η of 𝔞_T onto
H^♯_η is ⪰ 0, and its diagonal gives the necessary signed tests 𝓕_T(φ^♯_j) ≤ μ^♯_j for each eigenvector.
(c) The tests with μ^♯_j ≥ 0 are not empty conditions only through the off-diagonal Schur coupling; the tests with
μ^♯_j < 0 are signed: the fluctuation must be strictly negative there. Since μ^♯_j ≥ μ_j and μ^♯_0 ≥ … the number of
strictly signed tests n^♯_− ≤ n_∞(T) (L2_007), and by N_BUILD_001(E) every such μ^♯_j ≥ C₀ + 4 = −1.372…
(using A_∞ + R ⪰ (C₀+4) on P_T, which is N_BUILD_001(B)). So **on the signed part, the fluctuation must be ≤ −|μ^♯_j|
with |μ^♯_j| ≤ 1.372…, never more**: the required anti-correlation is O(1), uniformly in T. PROVED.
Link (L2): 𝒮^♯_η is L2_007's Schur complement after moving the polar term into the archimedean operator; the
η-threshold rises by 4, the signed demand drops from ≤ |C₀| to ≤ |C₀+4|.

## 3. The Chebyshev segment expansion with the actual Λ (PROVED)
Let E(u) := e^{−u/2}(ψ(e^u) − e^u). For F ∈ P_T real, w = c_F (N_BUILD_001, R160 Thm E):
  𝓕_T(F) = 2w(0) + 2∫₀^{2T} E(u)(½w − w′)(u) du.
On each interval [log q_i, log q_{i+1}) between consecutive prime powers, ψ = ψ_i constant, so
E(u) = ψ_i e^{−u/2} − e^{u/2}, and (ψ_i e^{−u/2} − e^{u/2})(½w − w′) = −ψ_i e^{u/2}·(e^{−u}w)′·e^{0}… is an exact
derivative plus ψ_i-free terms (e^{u/2}(½w − w′) = −e^{u}(e^{−u/2}w)′); summing the exact derivatives telescopes and returns Σ_n v_n w(log n) + 2∫₀^{2T} w e^{u/2}: the expansion is the
identity itself (no information gained). Recorded as a NEGATIVE check: segmentwise use of the true Λ inside
the Stieltjes form is tautological; any gain must come from an inequality, not from re-summation.

## 4. Attempted signed input with the actual Λ: per-prime Euler bounds — NO-GO (PROVED)
For each p the untruncated local symbol P_p(τ) = Σ_k 2 log p p^{−k/2} cos(kτ log p) satisfies
−2log p/(√p+1) ≤ P_p ≤ 2 log p/(√p−1) (Poisson-kernel form, CITED phase-146). These are the only pointwise signed
facts on the comb symbol available prime by prime. Upper side summed over p < e^{2T}: ≍ e^{T}, against the O(1) demand of
§2(c). So per-prime pointwise bounds cannot give (N^♯) on the signed part: they are pointwise in τ (W-loc class on the
symbol) and lose the correlation with F. NO-GO within the class "Σ_p (pointwise bound on P_p) paired with |F̂|²".

## Barrier position
§1–§2 exact (inherit the margin, no claim). §4 lies in W-loc/W-lin and is recorded as such. The surviving target
(stated below) escapes W-coh because it is not a Lipschitz functional of the coherence but a correlated inequality on a
fixed finite space; it escapes W-mom (no traces) and W-loc (it uses the full symbol through φ^♯_j), but it is not yet a proof.

## Self-review
1. §1: is G = RF? F ∈ P_T ⇒ F = (¼−∂²)G with G ∈ H²_0 (thm:nyq-cone, PROVED there); G ∈ H¹_0 ∩ H², so G is the Dirichlet
solution. Correct. Eigenvalue bound r_1 = (¼+(π/2T)²)^{-1} < 4. Correct.
2. §2(a): |Σ v_n w| ≤ A_T‖F‖² (|w| ≤ ‖F‖²) and 0 ≤ 𝔭 ≤ 4‖F‖²: |𝓕| ≤ A_T + 4. Correct. (b) needs the closed-form domain
and compactness — L2_007 §1. Correct.
3. §2(c): "μ^♯_j ≥ C₀+4" follows from m^♯ ≥ m^♯(0) on all of P_T. Correct. The claim "O(1) uniformly in T" concerns the
signed demand, not the size of 𝒮^♯ coupling terms, which are not bounded here. Honest scope stated.
4. §3 originally hoped for a gain; review shows the derivative identity telescopes. Downgraded to NEGATIVE check.
5. §4: correct but weak; labelled NO-GO in a declared class.
No sign contact; no negative value of 𝔞_T.

## Next construction (precise)
(N^♯_fin): for the finitely many eigenvectors φ^♯_j of (A_∞+R)|_{P_T} with μ^♯_j < 0, prove
Σ_n v_n c_{φ}(log n) + ⟨φ,Rφ⟩ ≤ μ^♯ for φ in their span, jointly with the Schur coupling. Arithmetic input needed: a
correlated inequality between Λ and the autocorrelations of ξ-normalised archimedean ground states — candidates not
yet in the corpus: (i) Selberg-sieve majorants restricted to the lag set of c_φ with c_φ ≤ 0 regions, (ii) the
reflection n ↔ e^{2T}/n of the anti-periodic sector (where the extremal vector lives, R186_052 §5.2).
