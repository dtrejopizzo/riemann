# R186_005 — Degree 2, two scales and the Selberg identity (TB-3−, L-TB3.0)

Phase 186, program TB-3 (R186_000 §3). Pure mathematics; no equivalences with RH. Inputs: R185_001 (Lemmas 2–4, models M1/M2), R185_002 (Thm F), R185_004 (atoms L/D/C/Q), R185_005
(Thm BR, branch (c)), R166_802 (Thm 0–3, eq. (1.1)), R167_102/103 (b_θ, Thm S).

## Status

| Result | Short statement | Label |
|---|---|---|
| Lemma S0 | Generalized Selberg identity: holds for **every** b ≥ 0 on n ≥ 2 with its own system (N_b, μ_b) | PROVED |
| Lemma S1 | Triangularity: (N_b, μ_b) on [1,Y] depend only on b on [2,Y] | PROVED |
| Thm TB3-neg | Dichotomy: a statement of any degree closed under deletion beyond X ⟹ excludes only if some U_i < 0; not closed ⟹ uses completeness beyond X ⟹ identifies the tail and the exclusion is Thm 2 of R166_802 | PROVED |
| Prop S2 | "Λ∗Λ ≥ 0" (and every inequality derived from Selberg + positivity) is a consequence of Λ ≥ 0 pointwise; its coordinates are affine in the tails of Λ over an enlarged family of tests | PROVED |
| Prop S3 | Explicit formula for g = μ∗log²: explicit polar/archimedean part; zero part with residue ζ''(ρ)/ζ'(ρ) = 2C_ρ, **not local in the witness** | PROVED (form); numerical threshold: unnecessary by S2 |
| Obs S4 | b_θ violates Selberg **with N = 1**, not the generalized Selberg; the separation is exactly a C atom | PROVED (corrects the hypothesis) |
| Verdict | L-TB3.0 closed in negative form; TB-3− positive; degree 2 (and any finite degree) closed in the class "window + Λ ≥ 0 + support + completeness on [1,X] + formal identities" | PROVED |
| Residue | Statements with completeness **beyond** X that are not total identification: OPEN, and by Thm TB3-neg(ii) they fall into (N′) | OPEN |

## 0. Framework

Let X = e^{2T_c} and K_1,…,K_m admissible tests (R166_802 §1) at scales Δ_i. By (1.1) of R166_802,
Z_{K}(Σ) = 𝔄_K − Tail_K(λ), Tail_K(λ) = Σ_{n ≥ X} λ(n) n^{−1/2} Ψ̌_K(log n). In (M1) the witness set is the orthant
O_U = {t ≤ U}, U_i = 𝔄_{K_i} − Q^{hyp}_{K_i} + S_i. For a statement B on λ, Sh(B) = {(Tail_{K_i}(λ))_i : B(λ)}.

A degree-2 statement is 𝔅(λ) = Σ a_{ij} t_i t_j + Σ b_i t_i + c ⋛ 0 with t_i = Tail_{K_i}(λ); more generally we admit
any statement in λ and in objects defined from λ.

**Definition (closed under deletion beyond X).** B is *closed under deletion* if B(λ) ⟹ B(λ·1_{[1,X)∪S^c}) for all
S ⊂ [X,∞). This is the notion of R185_002 Thm F applied to the tail.

## 1. Selberg is a formal identity (Lemmas S0, S1)

**Lemma S0. PROVED.** Let b: {2,3,…} → ℝ with Σ b(n) n^{−σ} < ∞ for large σ. Define F_b(s) = exp(Σ_{n≥2} b(n)
n^{−s}/log n) = Σ N_b(n) n^{−s} and 1/F_b = Σ μ_b(n) n^{−s}. Then

 μ_b ∗ (N_b · log²) = b · log + b ∗ b.

*Proof.* −F_b'/F_b = Σ b(n) n^{−s}. Then F_b''/F_b = (F_b'/F_b)' + (F_b'/F_b)². Coefficient by coefficient: F_b''/F_b
↔ μ_b ∗ (N_b log²); (F_b'/F_b)' ↔ b·log; (F_b'/F_b)² ↔ b∗b. ∎

For b = Λ, N_Λ = 1 (Euler) and μ_Λ = μ: this is the Selberg identity Λlog + Λ∗Λ = μ∗log². Thus **the only
Selberg information about Λ that does not hold for every b is N_b = 1**, i.e. a C atom (completeness) of R185_004.

**Lemma S1. PROVED.** N_b(n) and μ_b(n) depend only on b(2),…,b(n). In particular, if b = b' on [2,Y], then
N_b = N_{b'} and μ_b = μ_{b'} on [1,Y].

*Proof.* From F_b' = −F_b·(Σ b n^{−s}) one obtains N_b(n) log n = Σ_{d|n, d≥2} b(d) N_b(n/d), a triangular
recursion with N_b(1) = 1; μ_b is the Dirichlet inverse of N_b, also triangular. ∎

**Corollary.** "Completeness on [1,X]" (N_λ = 1 on [1,X], i.e. λ∗1 = log on [1,X]) is a statement about λ|_{[2,X]},
the window data. Deleting λ beyond X does not alter it. It is closed under deletion. It is the harmless use that TB-3
wanted, and it is harmless precisely because it does not see the tail.

## 2. Theorem TB3-neg

**Theorem TB3-neg. PROVED.** Let B be a statement (of arbitrary degree in the t_i, or non-polynomial) true for Λ_ζ.
- (i) If B is closed under deletion beyond X, then 0 ∈ Sh(B), and B excludes the witness (Sh(B) ∩ O_U = ∅) only if
 there exists i with U_i < 0. In that case the exclusion already comes from the single-test statement "Tail_{K_i} > U_i", and if Ψ̌_{K_i} ≥ 0
 beyond X it suffices to have Λ ≥ 0 (R166_802 Prop 4.1). No gain from degree 2 nor from two scales.
- (ii) If B is not closed under deletion and is obtained from: window data, λ ≥ 0, support on prime powers,
 formal identities (Lemma S0) and completeness atoms, then B contains a completeness atom at some n ≥ X.
 If it contains completeness on all of [1,Y] with Y ≥ max(Xe^{Δ_i}), then by R185_004 it identifies λ = Λ on [2,Y]; Sh(B) restricted
 to those λ is the point τ(Λ_ζ), and "B excludes" is equivalent to ∃i: Tail_{K_i}(Λ_ζ) > U_i, which by R166_802 Thm 2 is the
 zero-side inequality Z_{K_i}(Σ_ζ) < Q^{hyp}_{K_i} − S_i. This is the (N′) exclusion itself, not a proof of it.

*Proof.* (i) λ_ζ satisfies B; by closure, λ_0 := Λ_ζ·1_{[1,X)} also does. Tail_{K_i}(λ_0) = 0 ∀i, so 0 ∈ Sh(B).
0 ∈ O_U ⟺ U ≥ 0 coordinate-wise. If Sh(B) ∩ O_U = ∅, then 0 ∉ O_U, hence ∃i U_i < 0. By Lemma 2 of
R185_001, Sh(B) ⊂ ⋃{t_i > U_i}, and the forced coordinate on τ(Λ_ζ) gives the single-test statement (R185_001 reduction Thm).
(ii) The listed inputs, except completeness, are closed under deletion: window and Lemma S1 (they do not see the tail), λ ≥ 0 and
support (deletion preserves both), formal identities (Lemma S0: hold for the deleted λ with its own (N, μ)). A
conjunction of statements closed under deletion is closed under deletion, and a logical consequence of them, added as a
statement, defines a set containing the closed set; if B is not closed, its derivation uses some atom
N_λ(n) = 1 with n ≥ X (Corollary of §1: atoms with n < X are closed). The identification is R185_004 (triangular
recursion of Lemma S1: N_λ = 1 on [1,Y] ⟹ λ = Λ on [2,Y]). The rest is R166_802 Thm 2. ∎

**Remark (degree 2 in the strict sense).** The theorem does not use the quadratic form: the "moment cone" of L-TB3.0
is decided by the empty-tail point, which lies in every Sh(B) closed under deletion, independently of the rank of (a_{ij}).
This extends I13 of R166_802 (one test, power family) to arbitrary statements in the class of (ii), within (M1).

**Scope.** (M1) (test-wise bounds, R185_001 §1). In (M2) the reduction is to a single combined test K_a (R185_001 Thm 5(b))
and the argument of (i) is repeated with W_π in place of O_U: 0 ∈ W_π ⟺ 0 ∈ 𝔄 − Q^{hyp} − 𝓡 − C̄, a single-combined-scale
condition. (ρ2) of R185_001 (discreteness of the real zero set) remains as it was: OPEN and on the zero side.

## 3. Selberg + positivity: a new mechanism? (Prop S2, S3)

Let g = μ∗log² = Λlog + Λ∗Λ. The candidate inequality is Λ∗Λ ≥ 0 ⟹ for w ≥ 0 on [X,Y],
Σ_{n∈[X,Y]} g(n) w(n) ≥ Σ_{n∈[X,Y]} Λ(n) log n · w(n).

**Prop S2. PROVED.** (a) Λ∗Λ ≥ 0 is a consequence of Λ ≥ 0 pointwise; every inequality obtained from Selberg (Lemma S0)
plus positivity of b∗b holds for every b ≥ 0 with its own μ_b, hence it is closed under deletion, and Thm TB3-neg(i)
applies: it does not exclude except through a U_i < 0 of an individual test.
(b) In coordinates: for a test K and Y = Xe^{Δ},
 Tail^{Λ∗Λ}_K = Σ_{mn ∈ [X,Y]} Λ(m)Λ(n)(mn)^{−1/2}Ψ̌_K(log mn)
 = [window × window: m,n < X] + 2·Σ_{n ≤ e^Δ} Λ(n) n^{−1/2} Tail_{K(·−log n)}(Λ)|_{m ≥ X} + [tail × tail: m,n ≥ X],
 and the last block is empty if Y < X², non-negative in weight if Ψ̌_K ≥ 0. The central block is **linear** in the tail
 with window coefficients: the window × tail product with the given window is a linear statement (R185_001 Lemma 3/4),
 not rank 2. The tail × tail block only appears with Δ ≥ log X (full Eratosthenes scale) and is ≥ 0, closed
 under deletion and null at the empty tail.
(c) Tail^{g}_K = Tail^{Λlog}_K + Tail^{Λ∗Λ}_K: the coordinate g is not independent; it is affine in the tails of Λ over the
 enlarged family 𝒦⁺ = {K, K·u (weight log n = 2T_c + u), translates K(·−log n), n ≤ e^Δ}. If "Λ∗Λ ≥ 0" were to exclude, by
 Lemma 3 of R185_001 it would do so through a half-space of coefficients ≥ 0 on those tails, and by Lemma 2 through a single test of 𝒦⁺.

*Proof.* (a) Lemma S0 and closure. (b) Expansion of the convolution with mn ≥ X; if m ≥ X then n ≤ Y/X = e^Δ.
(c) Add up (b) and apply the cited lemmas. ∎

**Prop S3 (thresholds of the tail of g). PROVED as a formula; the threshold is non-local.** Σ g(n) n^{−s} = ζ''/ζ. Poles:
- s = 1: ζ''/ζ = 2/(s−1)² − 2γ₀/(s−1) + O(1) (expansion of ζ = 1/(s−1) + γ₀ + …). **Double** pole at 1: the polar
 part of 𝔄^{(g)}_K is 2·(h)'-type (derivative of the test at the polar point) − 2γ₀·h, explicit.
- simple non-trivial zeros ρ: simple pole with residue ζ''(ρ)/ζ'(ρ) = 2C_ρ, where C_ρ is the constant term of ζ'/ζ at
 ρ: C_ρ = B + Σ_{ρ'≠ρ}(1/(ρ−ρ') + 1/ρ') + (Γ part evaluated at ρ). (There are no double poles at simple zeros; the "double
 pole" at zeros appears only in (ζ'/ζ)² and cancels against (ζ'/ζ)'.)
- trivial zeros and the Γ part: analogous explicit terms.
Hence Q^{hyp,(g)}_K contains Re[2 ĥ(ρ_q) C_{ρ_q}] and C_{ρ_q} includes 1/(ρ_q − (1−ρ̄_q)) = 1/(2δ_q) (from the quartet's
companion) **plus** a sum over all other zeros. U^{(g)} is not a function of the witness parameters (t_q, G): there is no
local threshold to compare with U^{(Λ)}.

**Consequence. PROVED.** The question "is U^{(g)} < 0 for some K while U^{(Λ)} ≥ 0?" produces no new mechanism: by
Prop S2(c) any exclusion via Tail^{g} ≥ Tail^{Λlog} factors through an individual test of 𝒦⁺ on the tails of Λ,
and by Thm TB3-neg(i) it requires U^{(Λ)}_{K'} < 0 for some K' ∈ 𝒦⁺. If 𝒦⁺ ⊄ 𝒦 (K·u is not ≥ 0 in general), what
opens up is merely an enlargement of the family of tests of R166_802 Thm 1, which is already covered (Thm 1 holds for every admissible test
with margin; positivity of Ψ̌ is only needed for Prop 4.1). No gain.

## 4. Falsifiers (Obs S4)

- **b_θ (R167_102).** 0 ≤ b_θ ≤ Λ, support on prime powers, b_θ∗b_θ ≥ 0. It satisfies the generalized Selberg with
 (N_{b_θ}, μ_{b_θ}) (Lemma S0). It violates Selberg with N = 1 because N_{b_θ} ≠ 1 at the first n ≥ X where b_θ ≠ Λ (Lemma S1).
 **Record:** Selberg statements with completeness beyond X are the first class in the corpus that b_θ does not
 satisfy; but what separates it is exactly the C atom, which identifies (Thm TB3-neg(ii)). With completeness only on
 [1,X], b_θ (which coincides with Λ in the window if θ is chosen accordingly; R167_102) satisfies it.
- **Λ̃ (R162_2601)** (positive atomic measure on {±log n}): formally defines (N_{Λ̃}, μ_{Λ̃}) by Lemma S0; satisfies the
 generalized one; violates N = 1 unless Λ̃ = Λ. Same verdict.
- **M_m** (non-atomic): statements in integer coefficients are not defined; those of Lemma S0 in measure version
 (exp of the transform) are; outside the scope of (M1), as in R166_802 §8.

Conclusion: degree-2 Selberg separates from the sieve falsifiers **only through completeness beyond X**, and
that is precisely the branch that identifies.

## 5. Verdict on TB-3

- TB-3− (L-TB3.0): **PROVED in negative form** (Thm TB3-neg). In (M1), and in (M2) with a combined test, the class
 "window + Λ ≥ 0 + support + completeness on [1,X] + formal identities (generalized Selberg, type II used as a
 product)" of any degree excludes the witness only through a U_i < 0 of a single test. Degree 2 adds nothing; the
 rank of the matrix is irrelevant.
- Selberg + Λ∗Λ ≥ 0: **no new power of exclusion** (Prop S2–S3). The threshold of the tail of g is not local in the witness.
- What survives (TB-3+): only statements with **partial** completeness beyond X (N_λ(n) = 1 on a proper subset
 of [X,Y], not on all of it) or non-algebraic uses of it. General form: Σ_{n ≤ Y} λ(n)·Φ_n(N_λ|_{[X,Y]}) with
 restrictions N_λ(n) = 1 on n ∈ E ⊊ [X,Y]. By Lemma S1 each atom N_λ(n) = 1 fixes a combination of λ(n) with earlier
 data: it is pointwise identification. Whether a partial, non-total identification can exclude without already being the (N′) bound
 is **OPEN**; there is no candidate. Outside the polynomial class (S2 of R186_000) this remains the only way out.

## Audit notes

1. **Is "closed under deletion" too strong?** Check that type-II formal identities (Vaughan/Heath-Brown) are
 written as Lemma S0 for general b: Vaughan uses μ and 1 (completeness). If it uses μ, 1 on ℕ beyond X is a C
 atom and falls into (ii); if only on [1,X] it is window. Verify that no version mixes them.
2. **Prop S2(b):** the translate K(·−log n) may have no margin (support of the test shifted outside [2T_c, 2T_c+Δ]);
 check that it belongs to the admissible family of R166_802 or that Thm 1 holds for it (Thm 1 only uses (1.1)).
3. **Prop S3:** the residue 2C_ρ assumes ρ simple; with multiplicity the residue changes but the non-locality persists.
4. **(ρ2) and (M2):** the theorem does not touch the discreteness residue of R185_001; it is not sold here as closed.
5. **Reading:** "b_θ does not satisfy Selberg" is true only with N = 1; corrected in Obs S4.
6. No step uses equivalences with RH; the exclusions are formulated against the witness of R166_802.

## Note (R186_092)

* Thm TB3-neg(ii): "B not closed ⟹ atom n ≥ X" is a non sequitur; correction: if B follows from premises closed under deletion, λ₀ satisfies B and 0 ∈ Sh(B). Verdict TB-3− remains PROVED. Prop S2(c) CONDITIONAL (admissibility of 𝒦⁺). C_ρ: missing −1/(ρ−1) and log π.
