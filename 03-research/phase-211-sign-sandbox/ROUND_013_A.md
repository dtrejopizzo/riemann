# Round 013 A — The peak locking under the B-process: Type I sums are pure dual, the full μ∗log dual is the conjugate polynomial, and the constant 0.355 is not produced by any piece the method controls

Target (★) via the open statement (U) of ROUND_012_A: λ_max(A_τ) ≤ m(τ) − κ on [2πN(1+δ), 2π·exp(Σ_{n<N}v_n + κ)].
Notation of ROUND_012_A: N = e^{2T}, v_n = 2Λ(n)/√n, s = ½ + iτ, P^ρ_T(τ) = Σ_{n<N} v_n ρ(log n/T) cos(τ log n)
= 2Re D_w(s), D_w(s) = Σ_n Λ(n) n^{−s} w(n), w(x) = ρ(|log x|/T) (even in log x, supported in e^{−2T} < x < N).
Labels: PROVED / CITED / CONDITIONAL / ARGUED / OPEN / NO-GO / NUMERICAL.

## 0. Corpus check

Index rows searched: P211-A (ROUND_001_A, Poisson/approximate functional equation of Q_M), P211-12A, L2_012 and
R163_603 (AFE as a class, |P_X|² ± AFE), INV_H_001 A1–A8 (Vaughan/Heath-Brown over ℕ), G6C-R160_S5 (Vaughan,
Heath-Brown, Selberg separated squares), PROOF_L_SHARP_Y/Z (van der Corput bounds on the caustic layer). Difference
claimed for this round: none of these applies the B-process to the packet polynomial P^ρ_T at height τ ≍ 2πN, above
the stationary point of the summation range, with the target of an additive O(1) identity (rather than a bound). The
round tests whether that difference produces new information. Result (§3): it does not; the class is recorded closed.

## 1. Type I sums above the plunge are entirely dual (PROVED at leading order; NUMERICAL check)

Write Λ = μ ∗ log, so D_w(s) = Σ_m μ(m) m^{−s} S_m(s), S_m(s) = Σ_k (log k) k^{−s} w(mk).
For fixed m the inner sum has smooth amplitude supported on k < N/m and phase −(τ/2π)log k, with |phase′| = τ/(2πk)
> τm/(2πN) ≥ m(1+δ) > 1 on the whole range.

**Lemma 1.1 (PROVED, standard Poisson + stationary phase, CITED for the second-order terms).** For τ ≥ 2πN(1+δ):
(i) the j = 0 Poisson term ∫ (log x) x^{−s} w(mx) dx is O_K(τ^{−K}) (no stationary point, smooth compactly supported
amplitude; integrate by parts);
(ii) S_m(s) = χ(s) Σ_{j > τm/(2πN)} j^{s−1} (log x_j) w(m x_j) (1 + O(1/τ)), x_j = τ/(2πj), χ as in ROUND_001_A (0.1).
In particular the dual frequencies satisfy j ≥ m(1+δ): the term j = 1, the only one whose amplitude carries the
full log(τ/2π), never appears. NUMERICAL (tools/bprocess_typeI_check.py, K = 40, τ = 2πK·1.2 and 1.6): primal vs
leading dual agree to 3.6 % and 3.5 %, consistent with O(1/τ)·(derivative) corrections.

Consequence. The archimedean quantity log(τ/2π) does not arise as a boundary or stationary term of any single Type I
piece: for each m it appears only inside log x_j = log(τ/2π) − log j, multiplied by an oscillating dual sum.

## 2. Full reassembly: the dual of μ∗log is the conjugate polynomial (PROVED)

Summing Lemma 1.1 over all m and all j exactly (not to leading order) is the Mellin computation:

**Proposition 2.1 (PROVED).** Let w̃(u) = ∫_0^∞ w(x) x^{u−1} dx (entire, w ∈ C_c^∞(0,∞)). For c > ½,
D_w(s) = (1/2πi)∫_{(c)} −(ζ′/ζ)(s+u) w̃(u) du, and by the functional equation −ζ′/ζ(z) = ζ′/ζ(1−z) − χ′/χ(z),
(2.1) D_w(s) = 𝒜_w(s) + (1/2πi)∫_{(c)} (ζ′/ζ)(1−s−u) w̃(u) du, 𝒜_w(s) = −(1/2πi)∫_{(c)} (χ′/χ)(s+u) w̃(u) du.
If the second integral is moved to Re u = c′ < −½, where (ζ′/ζ)(1−s−u) = −Σ_n Λ(n) n^{−(1−s−u)} converges absolutely,
it equals −Σ_n Λ(n) n^{s−1} (1/2πi)∫ w̃(u) n^{u} du = −Σ_n Λ(n) n^{s−1} w(1/n) = −conj D_w(s) (on the line 1 − s = s̄,
and w(1/n) = w(n) by evenness in log x).
*Proof.* Mellin inversion, the functional equation (ROUND_001_A (0.1)), absolute convergence on the two lines, and
evenness. The shift of the contour from c to c′ crosses the critical strip of the integrand; call the difference
R_w(s) := (1/2πi)[∫_{(c)} − ∫_{(c′)}] (ζ′/ζ)(1−s−u) w̃(u) du. Then exactly
(2.2) D_w + conj D_w = 𝒜_w + R_w, i.e. P^ρ_T(τ) = 𝒜_w(s) + R_w(s)
(both real, since the left side is). ∎

**Lemma 2.2 (PROVED; archimedean term).** 𝒜_w(s) = (1/2π)∫ ĝ(r) m(r) dr with g(x) = ρ(x/T)cos(τx), ĝ a kernel of total mass 1
kernel of width 1/T around ±τ; hence 𝒜_w(s) = m(τ) + O(T^{−2}τ^{−2}) and m(τ) = log(τ/2π) + O(τ^{−2}).
(Proof: −(χ′/χ)(½+ir) = m(r) (ROUND_001_A (0.1)), Parseval in u = iv, m″(r) = O(r^{−2}), ρ̂ has bounded second moment
at scale 1/T.) The polar contribution of the pole of ζ at 1 sits inside R_w and is ĝ(±i/2) = O_k(e^{T}(Tτ)^{−k}),
negligible at τ ≍ e^{2T}.

Reading. The identity "Σ_{n<N}Λ(n)n^{−s} + (dual) = archimedean term" asked for does emerge at the level of a
single polynomial, but in the form (2.2): the dual of the polynomial under the complete B-process is its own conjugate
(self-duality, because ρ(|log x|/T) is even), the archimedean term is m(τ) to O(τ^{−2}), and the entire constant lives in
the strip-crossing defect: the observed locking sup P ≈ m − 0.355 (ROUND_012_A Table 4.1) is, by (2.2), exactly the
statement inf_τ R_w(s) ≈ −0.355 over the first cells. (U) for one profile is equivalent, by (2.2) and Lemma 2.2, to
R_w(½+iτ) ≤ −κ + O(τ^{−2}) on the same range — a reformulation, not a reduction to a smaller statement.

## 3. Why no truncated (zero-free) version produces the constant — NO-GO with class

Class 𝒱: decompose Λ by Vaughan's identity (or Heath-Brown's) with parameters U, V; treat Type I pieces by
Poisson/B-process (Lemma 1.1) and Type II pieces by B-process in either variable plus any bound.

**Proposition 3.1 (PROVED as a structural statement; the size claim ARGUED).**
(a) Type I pieces with m ≤ U produce, by Lemma 1.1, χ(s)-twisted bilinear sums Σ_{m≤U} μ(m) m^{−s} Σ_{j>m(1+δ)} j^{s−1}
log(τ/2πj) w(τm/2πj): their only non-oscillating part is the j-sum of log(τ/2π)·j^{s−1}, which is again a Dirichlet
polynomial of length ≍ τ/(2πm) at height τ — of the same type as the input, with no stationary boundary term (j ≥ m(1+δ)).
(b) Exact reassembly over all m and j returns (2.2), i.e. the conjugate polynomial plus R_w (Proposition 2.1); there is no
intermediate truncation level where the archimedean term separates from the strip defect, because the separation in
(2.1) is the functional equation of ζ′/ζ, and every Type I/Type II split of μ∗log is a split of that same Mellin integrand.
(c) For U, V < N the Type II remainder Σ_{U<m, V<k} a_m b_k (mk)^{−s} w(mk) is bounded in this class only by
large-sieve / mean-value / van der Corput exponent-pair estimates, all of which lose multiplicative constants or powers
(e.g. Montgomery–Vaughan constant, or τ^{θ} savings with θ < ½ against a main size ≍ √N log N). By ROUND_012_A §5 the
target is additive O(1) on a quantity ≍ 2T with budget ≈ 0.35/(2T) in the coefficient: excluded.
Hence class 𝒱 either (b) reproduces (U) verbatim, or (c) loses more than the budget. NO-GO for 𝒱.

The constant −0.35 cannot be computed inside 𝒱: Lemma 1.1 and Lemma 2.2 produce only m(τ) and O(τ^{−2}), O(τ^{−K}),
O(1/τ) terms; no O(1) constant arises from any boundary, stationary or polar term (j = 1 is excluded by j ≥ m(1+δ);
the polar term is O(e^{T}(Tτ)^{−k})). The value 0.355 is a property of R_w, which the sandbox does not evaluate.

## 4. Falsifier test

(a) cΛ: D_w ↦ cD_w; (2.2) becomes cP = c𝒜_w + cR_w, and (U) reads c·P ≤ m − κ, i.e. the margin is m − c(m + R_w)
= (1 − c)m − cR_w: it scales as stated (fails for c − 1 ≳ 0.355/(2T)). The identity (2.2) itself is linear and survives
cΛ only through the factor c on the archimedean side, which is no longer m: correct sensitivity, but the identity carries
the sign only through R_w. (b) a_P and (d) finite modification of v_n change D_w by a fixed finite Dirichlet polynomial
of size O_P(1), not cancelled by any term in (2.2): the identity fails for them (no functional equation), as required;
but nothing in §§1–3 bounds R_w, so no sign step exists to test. (c) Beurling: Λ = μ∗log and Poisson on ℤ (Lemma 1.1)
are ℕ-specific and fail for a generic Beurling system; a Beurling zeta continuing to the line with a functional equation
of the same gamma factor would reproduce (2.2) with its own R_w, so (2.2) does not by itself distinguish it. Not a sign step.

## Result

NO-GO with class (𝒱: Vaughan/Heath-Brown/μ∗log + Poisson/van der Corput B-process for the packet polynomial at
τ ≍ 2πN above the plunge), plus a PROVED identity.

### What was proved
- Lemma 1.1: above 2πN(1+δ) every Type I inner sum is entirely its Poisson dual, with dual frequencies j ≥ m(1+δ); the
  j = 0 term is O(τ^{−K}); log(τ/2π) never appears as a boundary/stationary term (NUMERICAL check 3.5 %).
- Proposition 2.1 / (2.2): P^ρ_T(τ) = 𝒜_w(½+iτ) + R_w(½+iτ), exact; the full B-process dual of μ∗log for an even profile
  is the conjugate polynomial (self-duality); Lemma 2.2: 𝒜_w = m(τ) + O(T^{−2}τ^{−2}), polar part O(e^T(Tτ)^{−k}).
- Hence the peak locking "sup P ≈ m − 0.355" is exactly "inf R_w ≈ −0.355" (a reformulation of (U), one profile at a time).

### What failed and why
- The asked identity exists but is self-dual: the dual sum is the same polynomial, so it carries no new sign; the
  constant 0.355 lies entirely in the strip-crossing defect R_w, which no Type I/II piece evaluates.
- Truncated (Vaughan) versions leave Type II remainders bounded only with constant/power losses, excluded by the
  additive-O(1) requirement (budget ≈ 0.35/(2T)).
- (U) not proved; combination with ROUND_011_C Lemma 1.1 / ROUND_012_A Theorem 2.2 therefore not reached beyond the
  already certified ranges (all profiles T ≤ log 2; cos² T ≤ 2.64).

### Next concrete step
Stop treating (U) by summation methods on the polynomial (closed: trivial bounds, mean values, B-process/Vaughan).
The only remaining non-indexed handle on R_w is operator-theoretic: compute λ_max(A_τ) (ROUND_012_A Prop 3.1) on
[1.1, 3]·2πN for T ≤ 3 and test whether the all-profile margin stays ≥ 0.3; if it does, look for a positivity
structure of m(τ)I − A_τ as a cell operator (Toeplitz symbol of the comb tail at Dirichlet frequencies) rather than of
the scalar P^ρ_T.
