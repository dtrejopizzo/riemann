# N_BUILD_003 — Route (a): sieve majorants restricted to the lags where c_φ ≤ 0. A tail-deletion theorem and a two-sided-precision theorem

Pen and paper. Target: (N^♯_fin) of N_BUILD_002, i.e. Σ_n v_n c_φ(log n) + ⟨φ,Rφ⟩ ≤ μ^♯ on the negative eigenspace of
(A_∞+R)|_{P_T}.

## Corpus check
- Paper 47 cor:void + thm:finmod: the class C_BT = {0 ≤ a ≤ Λ} (all upper-bound sieve inequalities) is closed under
  deletion; the failing member deletes **all** of Λ below N ≥ e^{2T} (empty comb). thm:finmod(ii): amplification of one
  term. prop:wit-sens: relative change ε ~ λ_A/κ_T of all weights breaks positivity.
- phase-167 (R167_101–103, R167_291): witness-weighted sieve (WS*) — a sum TWISTED at the quartet frequency γ_q, one
  scale; dead by Thm B′ (sieve blindness) and Theorem S (Beurling/DMV falsifier).
- Difference of the route proposed here: untwisted, weight c_φ (autocorrelation of an archimedean eigenvector), with the
  split lags {c_φ > 0} (upper bound needed) vs {c_φ < 0} (here a LOWER bound for the primes is needed), and the exact
  values of Λ kept for small n. cor:void as stated does not cover classes that fix Λ(n) for n < n₀ (its deletion
  member removes them). So a sharper statement is needed to decide the route: Theorems 1–2 below.

## Theorem 1 (tail deletion, NEW, PROVED)
Fix n₀ ≥ 2 and a := Λ·1_{n<n₀}. Then WP_T(a) fails for all sufficiently large T.
*Proof.* Let g ∈ C_c^∞(−1,1) be real, even, with ∫g ≠ 0; G_T(t) := T^{−1/2}g(t/T) ∈ H²_0(I_T); F_T := (¼−∂²)G_T ∈ P_T
(thm:nyq-cone). |F̂_T|² = (τ²+¼)²|Ĝ_T(τ)|², Ĝ_T(τ) = T^{1/2}ĝ(Tτ). For any continuous p with polynomial growth,
(1/2π)∫p|F̂_T|² / (1/2π)∫|F̂_T|² → p(0): substitute τ = x/T; the weight (x²/T²+¼)²|ĝ(x)|² converges dominatedly to
(1/16)|ĝ(x)|², and p(x/T) → p(0) (same argument as lem:wit-conc). Take p = m: 𝔞_∞(F_T)/‖F_T‖² → m(0) = C₀. Take
p = cos(τ log n) for each of the finitely many n < n₀: c_{F_T}(log n)/‖F_T‖² → 1. Hence
𝔞^{(a)}_T(F_T)/‖F_T‖² → C₀ − Σ_{n<n₀} v_n < 0. ∎
**Corollary 1 (NO-GO, PROVED).** Let 𝒞 be a class of arithmetic functions that contains Λ and, for some n₀, all
a with a(n) = Λ(n) (n < n₀) and 0 ≤ a ≤ Λ. No argument using only a ∈ 𝒞 proves WP_T for all T. Every upper-bound
sieve, Brun–Titchmarsh, Selberg Λ²-majorant, or any majorant restricted to the lags {c_φ > 0}, holds for every member of 𝒞.
So the "upper half" of route (a) is void, independently of the lag restriction and of the exact small values.

## Theorem 2 (two-sided precision, PROVED modulo the sign of κ_T, CITED prop:wit-sens)
Let 𝒞_ε := {a : |a(n) − Λ(n)| ≤ εΛ(n) ∀n}. If κ_T ≠ 0 (prop:wit-sens) and ε > λ_A(T)/|κ_T|, 𝒞_ε contains a member
failing WP_T: a = (1 + sgn(κ_T)ε)Λ.
*Proof.* Rayleigh with the minimizer h: λ_A(T;(1±ε)v) ≤ λ_A ∓ εκ_T. ∎
So the "lower half" (a lower bound for Σ_{c_φ<0} Λ|c_φ|) must have relative precision below λ_A/|κ_T| ≤
4·10⁹Te^{−15.449T}/|κ_T| for T ≥ 1 (cor:margin1, CITED). Lower-bound sieves have relative losses ≫ 1 (parity) — far
above. **NO-GO for route (a)** in the class "sieve upper bound on {c_φ>0} + sieve lower bound on {c_φ<0}".

## Barrier position
Theorem 1 sharpens cor:void (deletion only of the tail [n₀, ∞), keeping every small Λ(n)); it is a new barrier
"W-tail". Theorem 2 is prop:wit-sens in class form.

## Self-review
1. Thm 1: G_T ∈ H²_0(I_T) since supp g ⊂ (−1,1) — yes. Normalization cancels. Dominated convergence: |ĝ| Schwartz,
(x²/T²+¼)² ≤ (x²+¼)² for T ≥ 1, |m(x/T)| ≤ |C₀| + log(1+|x|) — yes. Conclusion holds for every n₀; T depends on n₀.
2. Does Thm 1 contradict assumed positivity of Λ? No: for Λ itself the full comb's polar mass is exactly what P_T
converts into +4 and the fluctuation (N_BUILD_001); for a = Λ1_{n<n₀} there is no main term to convert. Consistent.
3. Thm 2 needs κ_T ≠ 0: not proved in general — labelled. Numbers are CITED.
4. Difference from phase 167 is real (untwisted, lag-split, exact small values) but the conclusion is the same: dead.
No sign contact.
