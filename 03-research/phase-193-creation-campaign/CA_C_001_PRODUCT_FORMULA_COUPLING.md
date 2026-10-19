# CA_C_001 — The product formula as a global coupling condition: classification of its relaxations

Phase 193, round 6. Seed C3 of CA_C_000. Pen and paper.
**No sign contact. No certified negative value for ζ.** All falsifiers below are *other* combs.

## 0. Notation (Paper 47)
X = e^{2T}, N_T = {2 ≤ n < X}. A comb is a real a: ℕ_{≥2} → ℝ, v_n(a) = 2a(n)n^{−1/2},
𝔞^{(a)}_T(F) = 𝔞_∞(F) − Σ_{n∈N_T} v_n(a) Re c_F(log n) on P_T (𝔞_∞ = Γ_ℝ term with polar part; c_F the autocorrelation).
λ(T;a) = bottom of 𝔞^{(a)}_T on P_T; WP_T(a) means λ(T;a) ≥ 0. Divisor sum D_a(n) := Σ_{d|n, d≥2} a(d).

## 1. The product formula is the window form of (E)
**Lemma 1 (PROVED).** For n ∈ ℕ, D_Λ(n) = Σ_p v_p(n) log p = log|n|_∞ = −Σ_p log|n|_p. So the product formula for the
integers n < X is the identity D_a(n) = log n on N_T, which is condition (E) of P47 prop:shape-inputs on the window.
*Proof.* Λ(p^k) = log p and Λ = 0 elsewhere; v_p(n) counts the prime powers p^k | n, k ≥ 1. ∎

**Lemma 2 (PROVED; exact coupling is a singleton).** If D_a(n) = log n for every n ∈ N_T, then a = Λ on N_T.
*Proof.* Put a(1) = 0. Then D_a = a * 1 and log = Λ * 1 on [1, X), and Dirichlet convolution by 1 is invertible on functions on an
initial segment of ℕ (convolution by μ). ∎
So a deduction from the exact product formula on the window is a deduction about Λ alone. Its content at T is WP_T(Λ) itself (REF-D for
the class; (P1)). This does not exclude a proof that uses the product formula exactly; it says the product formula, as a class, carries
no information beyond the comb.

## 2. Relaxations: the local/global table
Split N_T into prime powers (the "local" product formula at each place p: D_a(p^k) = k log p) and the remaining integers ("global" part,
composites with ≥ 2 distinct prime factors; written C_T). For R_loc, R_cmp ∈ {=, ≤, ≥, ∅} let
  𝒦(R_loc, R_cmp) = { a : D_a(n) R_loc log n for prime powers n ∈ N_T,  D_a(m) R_cmp log m for m ∈ C_T },
optionally intersected with {a ≥ 0}.

**Lemma 3 (contact of a chosen sign; PROVED from P47 lem:cpos).** Let n₀ ∈ N_T and ε ∈ {±1}. There is a real F ∈ P_T with
ε c_F(log n₀) > 0 and c_F(log n) = 0 for every n ∈ N_T∖{n₀}. Consequently λ(T; a + cε·1_{n=n₀}) → −∞ as c → +∞, for every comb a.
*Proof.* In the proof of lem:cpos take u₀ = log n₀ and ℓ < min(u₀, 2T − u₀, min_{n≠n₀, n∈N_T}|log n − log n₀|). Then
c_{F^±} is supported in {|u| < ℓ} ∪ {|u ∓ u₀| < ℓ}, which contains no other log n, n ∈ N_T, and c_{F^±}(u₀) = ±‖φ‖². Then
𝔞^{(a+cε1_{n₀})}_T(F^ε) = 𝔞^{(a)}_T(F^ε) − (2c/√n₀)‖φ‖², which tends to −∞. ∎

**Lemma 4 (Bertrand contact; PROVED).** For T > ½ log 2 there is a prime p₀ ∈ (X/2, X). It has no multiple in N_T other than itself.
*Proof.* Bertrand's postulate in the real form: for every real x > 1 there is a prime p with x < p < 2x (CITED, standard).
Take x = X/2 > 1. Since 2p₀ > X, p₀ is its only multiple in N_T. ∎

**Theorem 1 (the product-formula table; PROVED except the cells marked).**
For each pair (R_loc, R_cmp) and each T in the stated range, the class 𝒦(R_loc, R_cmp) either is the singleton {Λ} on N_T (REF-D) or
contains a comb with λ(T; ·) < 0. Without a sign condition on a:

| R_loc \ R_cmp | = | ≤ | ≥ | ∅ |
|---|---|---|---|---|
| = | singleton (Lemma 2) | Λ − c1_{6} (L3), T > ½log6 | Λ + c1_{6} (L3), T > ½log6 | Λ ± c1_{6}, T > ½log6 |
| ≤ | Λ − c1_{p₀} (L3, L4) | a_P (O6), T ∈ [0.60, ½log P] | Λ − c1_{p₀} (L3, L4) | Λ − c1_{p₀} (L3, L4) |
| ≥ | Λ + c1_{p₀} (L3, L4) | Λ + c1_{p₀} (L3, L4) | Λ + c1_{2} (O2) | Λ + c1_{p₀} |
| ∅ | Λ ± c1_{p₀} | Λ ± c1_{p₀} | Λ + c1_{6} or + c1_{p₀} | everything |

For T ≤ ½ log 6 the set C_T is empty and every row reduces to its R_cmp = ∅ cell.
*Proof of the cells.* A perturbation a = Λ + c1_{n₀} changes D_a exactly at the multiples of n₀ in N_T, by +c. (i) n₀ = 6: the only
multiples are composites in C_T (6 divides no prime power), so the local relations are untouched and the composite relations move by +c
(sign of c chosen to respect R_cmp ∈ {≤, ≥, ∅}). (ii) n₀ = p₀ of Lemma 4: its only multiple in N_T is p₀ itself, a prime power, so only
the local relation at p₀ moves; the sign of c is chosen to respect R_loc. In both cases Lemma 3 gives λ(T; Λ + c1_{n₀}) < 0 for |c|
large with the right sign. (iii) a_P with P > X: D_{a_P}(n) = log(P-rough part of n) = 0 ≤ log n on N_T, and WP_T(a_P) fails for
T ∈ [0.60, ½ log P] (P47 prop:shape-eulerdel). (iv) The cell (≤, ≥): Λ − c1_{p₀} lowers only the local relation at p₀ and leaves the
composites unchanged, so it lies in the class; Lemma 3 applies. (v) (≥, ≥): O2 at n₀ = 2 (P47 lem:shape-amp). ∎

**With a ≥ 0 imposed.** Every falsifier with c > 0 survives. The cells that used c < 0 change:
- (=, ≤) with a ≥ 0: D_a(m) = log m + Σ_{d|m, d∈C_T} a(d) ≤ log m forces a = 0 on C_T: **singleton** (REF-D).
- (≤, ·) with a ≥ 0 and the local relation strict at a prime power: the perturbation Λ − c1_{p₀} is admissible only for c ≤ log p₀,
  so Lemma 3 does not apply. Here the falsifier is a_P when R_cmp ∈ {≤, ∅} (PROVED), and **CONDITIONAL** (on κ_T ≠ 0 or on
  c_{F⋆}(log p₀) ≠ 0, P47 lem:shape-weight, lem:shape-scale) when R_cmp ∈ {=, ≥}.
- Tolerance classes |D_a(n) − log n| ≤ ε_n: if some ε_{n₀} > 0 is unbounded in the deduction, Lemma 3 gives a falsifier; for bounded
  tolerances the falsifier (1+δ)Λ or Λ ± ε1_{n₀} is CONDITIONAL exactly as in P47 lem:shape-est(iii).

**Corollary 1 (PROVED, with the two conditional cells).** A product-formula ("Hasse") condition on the window — any combination of local
(prime-power) and global (composite) divisor relations — is either the comb Λ itself on N_T or admits a comb with negative bottom at T.
Local product formulas at every place never suffice: the class (=, ∅) contains Λ ± c1_6 for T > ½ log 6. The "global coupling
condition specific to ℚ" in the divisor sense is exactly the vanishing a = 0 on C_T, i.e. **the comb has no composite atoms**, and
together with the local formulas it is the whole comb.

**Check of Corollary 1.** (a) Is the falsifier Λ + c1_6 legitimate? It has the local product formula at every place, nonnegative
weights and integer frequencies; it breaks the composite relation (global PF) only. It is not a Dirichlet series with an Euler product, so
it also breaks (E); that is the point: (E) = local PF + global PF. (b) Does the table exclude a *proof* of WP_T(Λ) that uses the product
formula? No. It excludes deductions whose property set is one of these classes. A proof that uses the exact product formula *together
with a further non-linear step* is not touched (cor:shape(f)). (c) Is the table a restatement of lem:shape-amp / shape-eulerdel? Partly:
the new content is the local/global split, the Bertrand contact (a perturbation that moves exactly one local relation and nothing
else), and the singleton cells (=,=) and (=,≤)+(a ≥ 0). (d) Index: P122_009-010 closed a geometric (curvature) use of the product formula;
the divisor-class use is new. Label: NO-GO for the declared classes (PROVED; two cells CONDITIONAL).

## 3. What the global coupling does on the window form (the C4 remark, PROVED)
On P_T, 𝔞^{(a)}_T = 𝔞_∞ − Σ_p 𝔮_{p,T} − Σ_{m∈C_T} v_m(a) Re c_F(log m). For a = Λ the last sum is absent. Hence, inside the window form,
- (F) enters only as the archimedean term at conductor 1 (Γ_ℝ, with the polar part) and through the Tate constraints of P_T;
- (E) enters as "local factors at every p < X, each standard" (local PF) plus "no composite atoms" (global PF).
a_P fails "every p" (incomplete set of places); O2/Λ + c1_6 fail "no composite atoms"; Epstein Ξ_Q fails both (its comb is not supported
on prime powers); quartets add an absolutely continuous term outside every local factor (lem:shape-quartet). So **the joint use of
(E)+(F) demanded by (R)(2) is, on the window, the statement that the form is the sum over a complete set of places of the standard local
terms, with nothing else.** That statement determines the form; it is the target's object, not a mechanism.

## 4. The only exact non-tautological use of the product formula, and a trade-off (new reading; OPEN statements)
P47 prop:shape-family(i) uses the product formula exactly on the test family s_w = (m^{−1/2}w(m/M))_{m≤M} (w ≡ c on [0, η], 2T₀ < log 2):
  s_w^⊤𝔸_M s_w = s_w^⊤Arch_M s_w − Σ_{2≤N<Me^{2T₀}} N^{−1/2} D_w(N)E_w(N),
  D_w(N) = 2c log N − Σ_{d|N, 2≤d<N/(ηM)} 2Λ(d)(c − w(N/(dM))),  d < e^{2T₀}/η < 2/η.
**Observation 1 (PROVED, a specialization).** If η > 2/3, only d = 2 can occur, so on this family the form depends on the primes only
through log 2: it is an explicit expression in Γ_ℝ (Arch_M), in log N (the product formula) and in Λ(2).
**Observation 2 (PROVED).** For fixed M and η, the linear span of {s_w} (w smooth on [0,1], w ≡ const on [0, η]) is the set of vectors
s with m^{1/2}s_m constant on m ≤ ηM. The span is all of ℝ^M only when ηM < 2, in which case d < 2/η runs over all primes below M.
*Proof.* The values w(m/M) for m > ηM can be prescribed independently by smooth w; for m ≤ ηM they equal c. ∎
So the product formula **trades primes for test-space rigidity**: removing the primes exactly (η large) restricts the test vectors to
those that look like c·ζ's partial sum on the initial segment m ≤ ηM, and freeing the test vectors brings back every prime.
This is a local–global statement in the precise sense: the "local" data Λ(d), d < 2/η, are exactly those not absorbed by the global
identity Σ_{d|N}Λ(d) = log N on the test family.

**Two statements left OPEN (not attempted here):**
- (Fam_η) for some η > 2/3 and all M, w: s_w^⊤𝔸_M s_w ≥ 0. It follows from the target (P47 rem:shape-ident) and, by Observation 1, it is
  an explicit inequality in Γ_ℝ, log N and log 2 only. A proof is a necessary sub-statement, not the target.
- (Span_η) the bottom of 𝔸_M is attained (to relative precision of the margin) on the span of Observation 2. P47 records that minimizers
  lie in the closed span of the family numerically when η may vary; Observation 2 shows that this is a strong rigidity statement when η is
  fixed (> 2/3): a minimizer would have to be proportional to m^{−1/2} on [1, ηM]. Nothing suggests this; I expect (Span_η) to be false
  for fixed η, which would make (Fam_η) strictly weaker than the target. Label: expectation, not a statement.
Screens for (Fam_η): (R)(1) ✓ (uses Λ(2) and the product formula exactly); (R)(2) ✓; (R)(3) ✓ (non-linear: the test is built from ℕ);
(B″) ✓ (the collapse uses Σ_{d|N} a(d) = log N, false for a_P, Λ + c1_6, Epstein); O7: the quartets keep the comb, so they satisfy the
collapse; their form differs by −kβ_z, which on this family is a smooth term — (Fam_η) for quartets is a different inequality, so O7 does
not transfer the conclusion (✓ by construction, not by a mechanism). It is not REF-D (strictly weaker if (Span_η) fails).
It is, however, a **sub-statement**, so it is not a route to D unless paired with (Span_η).

## 5. Verdict
- Product-formula classes (local, global, one-sided, tolerance): NO-GO for the declared classes (Theorem 1, Corollary 1; PROVED except two
  CONDITIONAL cells). Exact PF on the window: singleton (REF-D as a class).
- New structural reading: on the window, the "global coupling for ℚ" in the product-formula sense is *no composite atoms*; (E)+(F)
  jointly = "complete set of places, standard local terms, nothing else" (§3). No sign follows.
- New object (OPEN): (Fam_η), an explicit prime-free (log 2 only) necessary inequality, with the trade-off of Observation 2.
No YES→NO move on (R). Proposed index entries: "product formula as divisor-class coupling: NO-GO (CA_C_001 Thm 1)";
"(Fam_η): OPEN sub-statement, prime-free at η > 2/3".

## Erratum (round 7, after corpus check)
§4 is a retry. (Fam_η) is SPEC_B's T*₃(η) (phase-191/SPEC_B_SELECTED_FREQUENCY.md §1.3–1.4), and the collapse to log N plus
Λ(d), d < e^{2T₀}/η, is written out there. Observation 1 (η > 2/3 ⇒ only d = 2) is only a specialization of it. Observation 2 is
SPEC_B §1.4's dichotomy, stated as a span computation. The settlement is in CA_C_003.
