# L2_BUILD_011 — The input map: which properties of Λ can carry the sign

WP_T(a): λ_A(T; a) ≥ 0 for the window form built with weights a in place of Λ (Paper 46 §subsec:finite).
A property P is KILLED if some weight sequence (or L-type object) keeps P and fails WP_T at some window T
(so no argument that uses only P proves WP_T there — transfer reading, R186_114 §1.2). SURVIVES = no falsifier
keeping P is known. UNKNOWN = not settled. Falsifiers refute proof schemes, never statements about ζ.

## Corpus check
Paper 46 thm:finmod, cor:void, rem:twohalves; crossword CROSSWORD-TO-D §3.1 table I3 (property →
falsifier), I4 (Thm O), I5 (W-identification), I6 (W-sieve), I7 (inertia), §3.2 exigencias (α)–(θ);
R186_114 (falsifier audit: M_m PROVED as form object; f_t primitive witness CONDITIONAL on (Z-strip); DH, BFdisc,
Λ̃, b_θ, ℕ∪√2ℕ, R = L(u,χ) PROVED/CITED); R186_005 (TB3-neg, degree-2 Selberg); R185_005/005B (BR).
New here: one explicit falsifier (Euler-preserving prime deletion, §1 row 8) and the joint "survivors" table.

## 1. The map
| # | property P | falsifier keeping P and failing WP_T | label |
|---|---|---|---|
| 1 | PNT with any known error term | Λ1_{n≥N} (deletion), Λ + c1_{n=2} (amplification): thm:finmod, cor:void C_PNT | KILLED (PROVED) |
| 2 | zero-free regions, zero density, all zeros and the pole | same two: ζ_a = ζ·E, E entire zero-free (cor:void C_zeros) | KILLED (PROVED) |
| 3 | finitely many verified zeros | subsumed by 2; also thm:finZ for certificates | KILLED (PROVED) |
| 4 | Beurling-type: a ≥ 0, Euler product, Λ*1 = log, without ℤ-integrality | Beurling DMV/Zhang; BFdisc (R163_803); ℕ∪√2ℕ (R184_005) | KILLED (PROVED/CITED) |
| 5 | tail behaviour of Λ (n ≥ e^{2T}) | WP_T depends only on (Λ(n))_{n<e^{2T}}; deletion below e^{2T} keeps every tail | KILLED (PROVED: form is tail-blind) |
| 6 | uniform rescaling / monotone laws in the weights | cΛ, c large (amplification argument of finmod(ii) with all n), c → 0 (deletion limit, λ_{∞,P} < 0 for T ≥ 0.60) | KILLED (PROVED for c large via finmod(ii) proof; c small CITED cor:Tarch) |
| 7 | upper-bound sieve inequalities, 0 ≤ a ≤ Λ | deletion (C_BT); b_θ (R167_102) | KILLED (PROVED) |
| 8 | Euler product over ℕ with positive local factors, support on prime powers, a(p^k) = log p on the support | **NEW: a_P := Λ·1_{p≥P}** (all powers of primes p ≥ P). ζ_{a_P} = ζ∏_{p<P}(1−p^{−s}) is an Euler product over ℕ, integral, positive coefficients, same zeros in 0<Re s<1 and same pole. For T ≤ ½log P the comb of a_P on N_T is empty, so WP_T(a_P) ⟺ λ_{∞,P}(T) ≥ 0, false for 0.60 ≤ T ≤ ½log P (cor:Tarch, CITED). It breaks the functional equation. | KILLED (PROVED, variant of finmod(i)) |
| 9 | Dirichlet convolution Λ = μ*log in a Beurling system | row 4 (holds in every Beurling system) | KILLED |
| 9′ | Λ*1 = log **over ℕ** (ℤ-integral) | identifies a = Λ (Möbius inversion on ℕ) | SURVIVES (identification, I5) |
| 10 | functional equation with Γ(s/2), pole, reality, a ≥ 0, no Euler product | Epstein (class number > 1), DH (rem:twohalves, DavenportHeilbronn1936) | KILLED (CITED) |
| 11 | ℕ-integral frequencies + FE at conductor q > 1, no Euler | f_χ (crossword I4, R163_1001) | KILLED (CONDITIONAL on f_χ zeros, as in the record) |
| 12 | ℕ-integral frequencies + FE with Γ(s/2) at q = 1 + pole | identifies cζ (Thm O, R163_1001) | SURVIVES (identification) |
| 13 | window data only (values on N_T used linearly) / all zero data as a form | f_t (data below λ₁ exact), M_m | KILLED (M_m PROVED; f_t primitive witness CONDITIONAL, R186_114 §2.4) |
| 14 | positivity + atomic counting | Λ̃ (R162_2601) | KILLED (PROVED) |
| 15 | character-sum bounds / twisted families | Λχ₂; b_θ | KILLED (record) |
| 16 | Rankin–Selberg-type positivity, generalized Selberg inequalities (degree ≤ 2) | TB3-neg (R186_005: holds for every b; b_θ satisfies it) | KILLED (PROVED) |
| 17 | Selberg class axioms, degree 1, conductor 1 | classification gives ζ(s) and shifts ζ(s+iθ) (Kaczorowski–Perelli, CITED); ζ_θ is listed as falsifier of the "extended class" in crossword I3, status not re-verified here | SURVIVES if ζ_θ ∉ class (real coefficients force θ = 0); else UNKNOWN |
| 18 | Euler product + FE at any conductor (Dirichlet L(s,χ)) | none known (L(s,χ) are not falsifiers in the record) | UNKNOWN |
| 19 | geometry axioms A1–A6 / Hodge, h⁰, two gates | Epstein; Ξ_a (phase 135) | KILLED (record) |
| 20 | field-uniform properties | ζ_K, S₃ (record) | KILLED (record) |
| 21 | inertia arithmetic of the B_p blocks, incl. Λ(p^k) = log p | I7 (R184_004 Cor 5) via M_m | KILLED (PROVED) |
| 22 | Galois/étale structure for Spec ℤ | no object exists in the record (phase 158: MW-5 open without an object) | UNKNOWN (no object) |
| 23 | exact window vector (Λ(n))_{n<e^{2T}} used non-linearly at a single T | survives trivially (WP_T is a function of it); used by the certified computations T ≤ ½log5 | SURVIVES (per-window, not uniform in T) |

## 2. Proposition (PROVED): the minimal surviving combinations
(a) Every row KILLED keeps one of: "no FE" (rows 1–9, 13–14, 21: finmod-type deletions/amplifications,
    Euler-preserving deletion), or "no Euler product over ℕ" (rows 10, 11: Epstein, DH, f_χ), or "not ℤ-integral"
    (row 4: Beurling).
(b) Hence any surviving property set must contain, jointly: an Euler product (or Λ*1 = log) **over ℕ** AND the
    functional equation with Γ(s/2) at conductor 1 — or the exact window vector at each T (row 23).
    Proof: removing either half of the pair leaves a property set kept by a falsifier of (a): drop FE → a_P
    (row 8) keeps Euler, ℕ, positivity, local values; drop Euler → Epstein/DH keep FE, pole, reality, a ≥ 0;
    drop ℤ-integrality → Beurling DMV keeps Euler and Λ*1 = log formally. ∎
(c) The minimal survivor is the coupling (Euler over ℕ) × (FE, q = 1), which is exactly the crossword's
    exigencia (δ) "couple the primes with the archimedean place" and (α)+(θ) (individual, ℤ-integral). Every
    such set identifies ζ (rows 9′, 12, 17): by I5 a proof must use it non-linearly (β), not as a class.

## 3. Review
- Row 8 is the only new falsifier. Check: Λ·1_{p≥P}(p^k) = log p for p ≥ P, 0 otherwise; its generating
  function exp(Σ a(n)n^{−s}/log n) = ∏_{p≥P}(1−p^{−s})^{−1} — an Euler product. Smallest support point is P,
  so for e^{2T} ≤ P no n ∈ N_T is charged; the form is 𝔞_∞ on P_T. Correct. Its novelty over finmod(i) is
  only that it keeps the Euler product exactly; it is a one-line variant. PROVED.
- Row 6 for c → 0 uses deletion-type reasoning only in the limit; the small-c claim "fails" needs
  continuity of λ in c: λ_A(T; cΛ) is concave? It is an infimum of affine functions of c, hence concave in c,
  and continuous; at c = 0 it is λ_{∞,P}(T) < 0 for T ≥ 0.60 — so it fails for small c. PROVED.
- Row 17: I did not re-verify ζ_θ; with real coefficients the shift is excluded, so row 17 with "real
  coefficients" SURVIVES (identification). Labelled with the caveat.
- Row 18 (Dirichlet L-functions) is UNKNOWN as a falsifier source. I did not attempt WP_T for L(s,χ): it would
  need numerics. Not a sign contact.
- The table uses falsifiers as transfer statements only (R186_114 §1.2). No row uses any equivalence
  involving row D.
- No sign certified, no negative value of 𝔞_T for ζ.

## 4. Output: the exact surviving list
SURVIVES: (9′) Λ*1 = log over ℕ; (12) ℕ-integral frequencies + FE Γ(s/2), q = 1, pole; (17) Selberg degree 1,
q = 1, real coefficients; (23) exact window vector, per window. UNKNOWN: (18) Euler + FE at q > 1; (22) étale.
Minimal combination: (Euler product over ℕ) ∧ (FE with Γ(s/2), conductor 1), used non-linearly — the sign
must come from the interaction of the two, never from either alone.

## Erratum (independent review of SHAPE_THEOREM)
- Row 13: "f_t primitive witness CONDITIONAL (R186_114 §2.4)" is superseded. Paper 46 prop:ftprim constructs the primitive witness
  directly (comb-level, no (Z-strip)); independently re-derived and CONFIRMED in 04-papers/46-row-d-dual-certificates/SECONDARY_ITEMS.md
  (review item 4). Row 13 reads: KILLED (M_m PROVED; f_t PROVED).
- §2(a): rows 13 and 21 keep the functional equation (M_m = ξ·polynomial, f_t self-dual); what they break is the Euler product over ℕ
  (M_m: polynomial factor whose logarithmic derivative is not a Dirichlet series over ℕ; f_t: frequencies m/√M ∉ ℕ). They belong to the
  "no Euler product over ℕ" branch. Conclusion (b) is unchanged.
- Row 4 / §2(a) third branch: no Beurling window form W_T exists in the record (R167_103 row 7), so the Beurling branch is ARGUED, not
  PROVED/CITED.
