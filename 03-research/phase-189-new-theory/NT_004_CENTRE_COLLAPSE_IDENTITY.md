# NT_004 — The centre collapse identity: on Euler tests at exponent ½, multiplicative near-coincidences m ≈ kn become additive
# near-coincidences a ≈ j weighted by the additive function (Λχ)*1; the ζ-test family; and why it carries no sign

Phase 189, construction step 4. Notation of NT_001–003. Labels as there.

## Corpus check
N_022 §1 (ZΔ = [L, Z]: 1*Λ = log as an integer-matrix identity, = R162_903 B2.1) and §3 (NO-GO: the identity does not reach
X_M because Near is a discretization defect); N_005/N_006 (Möbius transport; termwise truncation cost Te^T); N_016 (Gram
three-vector identity, −(ζ′/ζ)_N multiplier); L2_028 §3 (test b_m = m^{−½} with Near-free resolution, log²M cancellation);
L2_030 §3 (Ramanujan expansion of the shifted convolution); N_021 Prop 1 (Near = Ξ-kernel). grep "(Λχ)*1", "additive
neighbour", "Chowla" + "Weil", "ζ-test": no hit.
**New:** Thm 4.1 (exact collapse on truncated Euler tests at exponent ½ with NON-separated support — the near-coincidences are
kept, not avoided, and no truncation error appears because 2T₀ < log 2), Thm 4.2 (the χ = 1 comb part is O(1) uniformly in N,
by Tate's double zero), Thm 4.3 (ζ-test positivity, cheap), Prop 4.4 (twisted collapse ⇒ correlations of completely
multiplicative functions at additive shifts), the NO-GO 4.5. This is not N_022 §3's object: there the vector is arbitrary and the
identity fails off divisors; here the vector is the Euler vector, for which the b-sum is complete and the identity holds exactly
on all near-coincidences.

## 1. The identity (PROVED)
For N ≥ 1 and a completely multiplicative unimodular χ put s_a := χ(a)a^{−½} (a ≤ N) and G_N^χ := Σ_{a≤N}s_aτ_{log a}F₀ ∈ P_{T_N},
T_N = ½log N + T₀ after centring (translates of a primitive profile are primitive: L2_023 Lemma L). Let g_χ := (Λχ)*1, i.e.
g_χ(j) = Σ_{n|j}χ(n)Λ(n) = Σ_{p^e∥j}log p·Σ_{k=1}^{e}χ(p)^k (an additive function; g_1 = log).
**Thm 4.1 (centre collapse).** 𝔞(G_N^χ) = Arch_N^χ − 2Re Σ_{a≤N}Σ_{j≥2}χ(a)conj χ(j)(aj)^{−½}g_χ(j)c₀(log a − log j), with
Arch_N^χ := Σ_{a,b≤N}s_a s̄_bA(log a − log b). No prime appears outside g_χ; the near-coincidences of the multiplicative form
(a ≈ bn, a ≠ bn) have become additive near-coincidences (j = bn ≈ a), and the exact ones (a = bn) the diagonal j = a.
*Proof.* Hermitian form: comb part = Re Σ_{a,b≤N}s_as̄_bΣ_nv_nc₀(log a − log b − log n) (c₀ even, real; the two halves of B are
conjugate after a ↔ b). Put j = bn. For fixed a, c₀ ≠ 0 forces j ≤ ae^{2T₀} < 2N; every factorization j = bn with Λ(n) ≠ 0 has
n ≥ 2, hence b ≤ j/2 < N: **the constraint b ≤ N is automatic**, so the b-sum is complete. Then
Σ_{bn=j}χ̄(b)b^{−½}·2Λ(n)n^{−½} = 2j^{−½}χ̄(j)Σ_{n|j}χ(n)Λ(n) (χ̄(b) = χ̄(j)χ(n) since |χ| = 1, χ completely multiplicative). ∎

## 2. The trivial character: the ζ-tests (PROVED)
**Thm 4.2 (the comb part is bounded).** For χ = 1: |Comb_N| := |2Σ_{a≤N}a^{−½}Σ_jj^{−½}log j·c₀(log a − log j)| ≤ C(F₀) for all N.
*Proof.* f_a(x) := x^{−½}log x·c₀(log a − log x) is C² (ĉ₀ = F̂₀² = O(τ^{−4}) ⇒ c₀ ∈ C²), supported in (a/2, 2a).
∫f_a = a^{½}∫e^{−w/2}(log a − w)c₀(w)dw = a^{½}[log a·∫c₀e^{−w/2} − ∫wc₀e^{−w/2}] = 0, because ĉ₀(z) = F̂₀(z)² has a DOUBLE zero at z = ±i/2
(Tate: F̂₀(±i/2) = 0), so ∫c₀e^{−w/2} = 0 and ∫wc₀e^{−w/2} = 0. Euler–Maclaurin of order 2: |Σ_jf_a(j) − ∫f_a| ≤ (1/12)∫|f_a″|
≤ C a^{−3/2}log a. Summing a^{−½}·C a^{−3/2}log a over a converges. ∎
**Thm 4.3 (ζ-test positivity).** Let c_A := (1/2π)∫m(τ)F̂₀(τ)²/(¼ + τ²)dτ = 𝔞_∞(H₀), H₀ := (½ + ∂)G₀ (|Ĥ₀|² = F̂₀²/(¼ + τ²)).
Then 𝔞(G_N^1) = c_A·N + O(N^{½}). Moreover c_A > 0 for all admissible profiles with a ≤ a₁ (absolute a₁). Hence the Weil form is
positive on the ζ-test G_N^1 = Σ_{a≤N}a^{−½}τ_{log a}F₀ for all N ≥ N₀(F₀) — an explicit family reaching every window.
*Proof.* Arch_N = (1/2π)∫mF̂₀²|P_N|², P_N(τ) = Σ_{a≤N}a^{−½+iτ} = N^{½+iτ}/(½ + iτ) + ζ(½ − iτ) + O(N^{−½}(1 + |τ|)) for |τ| ≤ N
(Hardy–Littlewood approximation, Titchmarsh Thm 4.11, CITED); |P_N| ≤ 2√N for |τ| > N where F̂₀² ≪ τ^{−4}; |ζ(½ + iτ)| ≪ |τ|^{¼}
(convexity, CITED) is integrable against |m|F̂₀²/(1 + |τ|). Hence Arch_N = c_AN + O(√N); with Thm 4.2, 𝔞 = c_AN + O(√N).
Positivity of c_A: |Ĥ₀|² = (¼ + τ²)|ĝ|⁸ concentrates at |τ| ≍ 1/a: its mass on |τ| ≤ R is ≤ 2R(¼ + R²)‖G₀‖₁² ≍ R³a⁸, while
‖Ĥ₀‖² ≍ a⁵ (scaling of the fourfold convolution); with R = a^{−½} the low part is O(a^{3/2}) relative, and m(τ) ≥ log(1/√a) − C
on the rest (as in NT_002 Lemma 2.6). (Scaling constants not computed; PROVED up to routine bookkeeping.) ∎
**Identification.** The leading coefficient is the archimedean form of H₀ = (½ + ∂)G₀, a test supported in a window of length
2T₀ < log 2 that satisfies one Tate condition; the comb contributes nothing at order N because c₀*e^{−|u|/2} is supported in
[−2T₀, 2T₀] (Tate) and no log n (n ≥ 2) lies there. So **the ζ-test family is the prime-free-window positivity, transported to
every window by the Euler vector at exponent ½.**

## 3. Twisted characters (PROVED identity; reading ARGUED)
**Prop 4.4.** For general χ the comb part of Thm 4.1 splits into the diagonal 2Σ_{a≤N}Re g_χ(a)/a (exact coincidences: the
twisted Euler log-derivative partial sums, cf. 𝒟_σ of NT_002 at σ = 0) and the additive-shift part
  2Re Σ_{0<|h|≤2.5T₀a} Σ_{a≤N} χ(a)conj χ(a + h)·g_χ(a + h)·(a(a+h))^{−½}c₀(−log(1 + h/a)),
a weighted sum of **two-point correlations Σ_a χ(a)χ̄(a + h)g_χ(a + h)** of the completely multiplicative function χ at additive shifts h.
For real χ (χ(p) = ±1, e.g. Liouville λ) these are Chowla-type correlations; for Steinhaus random χ their mean vanishes (h ≠ 0).
*Proof.* Expand Thm 4.1 with j = a + h; |log(a/j)| ≤ 2T₀ ⟹ |h| ≤ (e^{2T₀} − 1)a ≤ 2.5T₀a (T₀ ≤ T_abs). ∎
So, inside the theory, **multiplicative near-coincidences on Euler tests = additive correlations of multiplicative functions** —
a precise Bohr–real bridge: the Bohr character χ (multiplicative structure) is correlated with itself across the additive shift h
(real/additive structure), with the additive weight g_χ produced by unique factorization (1*Λ = log twisted).

## 4. NO-GO for the centre family as a sign carrier (PROVED)
**Prop 4.5.** (i) For every comb a, every single-atom modification a + c1_{n₀} changes 𝔞(G_N^1) by O(c) uniformly in N.
(ii) Deletion a_P = Λ1_{n≥P}: Thm 4.1 holds with g replaced by log j − Σ_{p<P,p^k|j}log p, whose mean is log j − Σ_{p<P}log p/(p − 1) + o(1);
the constant shift is annihilated by Tate (∫c₀e^{−w/2} = 0) and the remainder is bounded: 𝔞(G_N^1) = c_AN + O_P(√N).
Hence the ζ-test family is positive for large N for the falsifiers too; it cannot carry the sign.
*Proof.* (i) The extra comb term is −2c n₀^{−½}Σ_{a,b≤N}(ab)^{−½}c₀(log a − log b − log n₀); the b-sum is a Riemann sum of
x^{−½}c₀(log(a/n₀) − log x), whose integral (a/n₀)^{½}∫c₀e^{−w/2} = 0 (Tate), so by Euler–Maclaurin it is O((a/n₀)^{−3/2}); summed
against a^{−½} it is O(n₀^{3/2}) independent of N. (ii) Same mechanism for each p < P (periodic weights mod p^k: split into
residue classes, each a Riemann sum with zero integral). ∎
**Reading.** The Euler direction at exponent ½ is exactly where 1*Λ = log removes Λ (Thm 4.1) — the identity is Λ-specific (it fails
for a_P, a + c1_{n₀}, Beurling primes on ℕ-indexed tests) — but the *quantity* it controls is dominated at order N by archimedean energy
and the Tate double zero makes every finite modification invisible at order N. This is the centre analogue of NT_003 Thm 3.6: along
Euler directions the flow sees only the centre, and there everything is either cheap (order N) or exactly critical (packet at τ = 0).
**Consequence for the construction.** (HEURISTIC) Non-Euler directions are a natural place to look in the band ½ ≤ σ ≤ 1 of the height flow.
The twisted collapse (Prop 4.4) shows what such directions look like at the centre: correlations χ(a)χ̄(a + h) with g_χ weights —
nonzero for curve characters χ(n) = n^{−iτ}, where χ(a)χ̄(a + h) = (1 + h/a)^{iτ} is smooth in a, so the shift sums are again
Riemann sums whose main terms are F̂₀-values at τ ± i/2 (nonzero off τ = 0): this is where the Weil symbol at height τ enters.

## 5. Requirements check
- Euler × FE × integrality: Thm 4.1 uses unique factorization (1*Λ = log, twisted: (Λχ)*χ = χ·log) and complete multiplicativity of
  χ, non-linearly (the merger j = bn). FE: only via Arch. Not joint.
- N_018: Thm 4.1 is an 𝔄_T-type identity on a specific test family (inside N_018's class); Thms 4.2–4.3 are Euler–Maclaurin + Tate.
  Restatement + cheap positivity; NO escape as a proof of D.
- Falsifiers: identity Λ-specific; conclusion class-blind (Prop 4.5). Honest NO-GO for this family.

## 6. Review
- Thm 4.1: the key step "b ≤ N automatic" needs j < 2N and n ≥ 2, both verified (2T₀ < log 2 ⇒ j ≤ ae^{2T₀} < 2a ≤ 2N). ✓ The form
  is the Hermitian one (complex tests: 𝔞(Re) + 𝔞(Im)), consistent with 025 §2. ✓
- Thm 4.2: C² regularity of c₀ from ĉ₀ = O(τ^{−4}) ✓ (|τ|²ĉ₀ ∈ L¹). Double zero of F̂₀² at ±i/2 ✓ (F̂₀(±i/2) = 0, squared).
- Thm 4.3: approximate functional formula CITED; the positivity of c_A is a scaling argument with constants not computed —
  label "PROVED up to routine bookkeeping" is honest only for sufficiently small a; stated so.
- Prop 4.5(ii): residue-class splitting for p^k ≤ … fine since P fixed.
- The "Consequence" paragraph is a reading (ARGUED), not a theorem.
- No negative value of 𝔞_T for ζ certified. **No sign contact.**


## Erratum note (after NT_001_004_REVIEW)
Prop 4.4 needs T₀ ≤ T_abs; §4 consequence downgraded to HEURISTIC (referee).
