# CA_C_000 — Seed generation, front C (local–global and adelic structure of the window form)

Phase 193, round 6. Pen and paper; no numerics.
**No certified negative value for ζ anywhere on this front.**

Read before seeding: CA_A_SYNTHESIS, CA_B_SYNTHESIS ((P1)–(P6)), CAMPAIGN_LEDGER (erratum: Paper 47 O-labels), P47 §20
(def:shape-ops, lem:transfer, prop:shape-inputs, lem:shape-est, lem:shape-ident, thm:shape, cor:shape, prob:region),
P47 prop:nearfree, rem:boxes, prop:AM, prop:shape-family, cor:Qp, lem:cpos; ROUTES-TRIED-INDEX README, 03 (MW-3, NG-C1, NG-C2),
04 (P122_009-010 product formula; Bohr-torus rows NT_003/005, G2_B7, F41; condensed polarizations G1_B3; adelic Maslov;
p-adic Sonin; G_p indefinite), 06 (R8 §28.4, MW-3 row).

Screen key. Idx = corpus/index retry? (R)k = clause k of prob:region. (P)k = CA_B conditions. O-labels are Paper 47's
(O2 amplification, O6 a_P, O7 quartets, O8 f_t, O10 Epstein/DH, O11 Beurling, O12 ζ_K, O15 Poisson). B′ = estimate with a
remainder; B″ = identity valid for every comb; REF-D = restatement of the target. "✗" = seed fails the screen there.

## Common fact used by several screens (PROVED, P47 cor:Qp + def. of 𝔞_T)
On P_T the window form splits over places with no remainder:
  𝔞_T(F) = 𝔞_∞(F) − Σ_{p<e^{2T}} 𝔮_{p,T}(F),  𝔮_{p,T}(F) = Σ_{k: k log p<2T} v_{p^k} Re c_F(k log p),
where 𝔞_∞ is the Γ_ℝ (conductor 1) term with its polar part, and each 𝔮_{p,T} is the Euler-factor log-derivative of L_p tested on F.
Each 𝔮_{p,T} is indefinite on P_T (cor:Qp), and 𝔞_∞ is indefinite on P_T for T ≥ 0.60 (cor:Tarch). So **on the prime side the
form factors exactly; Wall A of MW-3 (non-factorization) is a zero-side statement only.** Every "local–global" seed below
has to say what couples the summands, because the summands themselves carry no sign.

---

## C1. Weighted Hasse–Minkowski: a prime-local convex splitting
**Seed.** Find weights c_p ≥ 0, Σ_p c_p ≤ 1, with c_p 𝔞_∞ − 𝔮_{p,T} ⪰ 0 on P_T for every p < e^{2T}. Summing gives 𝔞_T ⪰ 0.
"Local positivity" is then positivity of the form at the pair of places {∞, p}, and the global coupling is the budget Σc_p ≤ 1.

| screen | result |
|---|---|
| Idx | ✗ retry: convex decomposition (CA_B_007, EXCLUDED: REF-D / class (D)); termwise bounds (P47 cor:directbound, lem:shape-misc) |
| (R)(5),(8) | ✗ each piece is decided by a bounded functional of one local symbol; no correlation across places |
| O-screens | for T ≥ 0.60, 𝔞_∞ has a negative direction F₀; then each piece needs 𝔮_{p,T}(F₀) ≤ c_p𝔞_∞(F₀) < 0 for **every** p with c_p > 0, and every local form must be negative on the whole negative cone of 𝔞_∞. cor:Qp makes each 𝔮_p indefinite on any infinite-dimensional subspace built from a contact, so this is a strong extra condition, unproved and implausible |
| (P1) | ✗ the split is a lower bound on 𝔞^{ν_ζ} through its own pieces (CA_B_008 §2) |
**Verdict: DISCARD** (retry + REF-D).

## C2. Per-place Lévy–Khintchine / Dirichlet-form splitting
**Seed.** Since 1 − cos ≥ 0, σ_T(τ) = [m(τ) − M_T] + Σ_p ψ_{p,T}(τ), with ψ_{p,T} = Σ_k v_{p^k}(1 − cos(kτ log p)) ≥ 0 pointwise and
M_T = Σ_{n<e^{2T}} v_n. Equivalently, with F extended by 0 and τ_a the translation,
  𝔞_T(F) = 𝔞_∞(F) − M_T‖F‖² + Σ_{n<e^{2T}} (v_n/2)‖F − τ_{log n}F‖²   (exact; ‖F‖² − Re c_F(a) = ½‖F − τ_aF‖²).
Each place contributes a nonnegative Dirichlet (jump) form, and the global coupling would be a Poincaré inequality on P_T
(Tate constraints) beating the constant M_T ≈ 4e^T.

| screen | result |
|---|---|
| Idx | partial retry: P60-1 (Ω CND, Lévy–Khintchine; gave simplicity, not sign) |
| B″ | ✗ the identity holds for every nonnegative comb |
| O7, O11, O15 | ✗ a Poincaré inequality for a positive jump measure on (0,2T) is a property of the measure; O7 keeps the comb, O11 and O15 keep positivity and density |
| (R)(7) | ✗ M_T is the density; the jump forms win only from the density ceiling (thm:ceiling) |
**Verdict: DISCARD** as a mechanism; the identity is kept as a coordinate (PROVED, one line).

## C3. The product formula as the global coupling condition
**Seed.** For n ∈ ℚ^×, log|n|_∞ + Σ_p log|n|_p = 0. For n ∈ ℕ this is Σ_p v_p(n) log p = log n, which is **the divisor-sum identity
Σ_{d|n} Λ(d) = log n**: the Euler-product condition (E) of prop:shape-inputs, restricted to the window, is the product formula.
Global coupling condition (PF_T): Σ_{d|n, d≥2} a(d) = log n for all n < e^{2T}, possibly in a relaxed form (one-sided, with
tolerance, or only at prime powers, which is the "local" product formula). Holds for ℚ. Fails for a_P (O6) and for Epstein (O10), f_t
beyond λ₁ (O8), Beurling (O11) and Poisson (O15).

| screen | result |
|---|---|
| Idx | P122_009-010 "flat product formula has no curvature" (geometric use, DEAD). The **divisor-class** use (one-sided, tolerance, local-only) is not in the index. Partial: P47 prop:shape-family uses PF exactly on the integer family |
| (R)(1),(2),(10) | exact PF_T + Γ_ℝ pins the form (Möbius inversion), so it passes (1), (2), (10) |
| O2, O6 | one-sided relaxations: ✗ (to be proved in CA_C_001) |
| O4ε, O5 | tolerance relaxations: ✗ conditional on κ_T ≠ 0 (lem:shape-est(iii)) |
| O7 | ✗ comb-only (quartets keep the comb), unless coupled to the form (P3) |
| B′/B″ | the exact PF is not comb-generic; a PF with tolerance is an estimate (B′) |
| REF-D | exact PF_T: the class is a singleton, so its content is the target (to be checked) |
**Verdict: SURVIVES (narrowly) for development**, with a precise question: is there a relaxation of PF_T that is neither
a singleton (REF-D) nor closed under O2/O6/O4ε/O7? → **CA_C_001**.

## C4. Tate's two constraints as the residues of the global zeta integral
**Seed.** For f = f_∞ ⊗ 1_Ẑ with Mellin transform F̂ at the archimedean place, Z(f,s) = Z_∞(f_∞,s)·ζ(s), and the poles of the completed
integral at s = 0, 1 carry the residues f(0), f̂(0). P_T is the space on which the global zeta integral is entire. Global coupling =
Poisson summation for ℚ ⊂ 𝔸.

| screen | result |
|---|---|
| Idx | ✗ Connes adèle class space / trace formula (L05, R158: restatement); Tate-port rows 121; "Tate not transported" L2_016 |
| REF-D | ✗ the space {f(0) = f̂(0) = 0} with the Weil distribution is Connes' formulation of the target |
| (P6) | the Poisson coupling enters 𝔞_T only through the polar terms, which vanish on P_T, and through the local Γ_ℝ (common-fact box) |
**Verdict: DISCARD** (REF-D). Kept fact: on P_T the global Poisson coupling is invisible in the prime-side window form, which is a sum of
local terms; (F) enters the window form only as "Γ_ℝ at conductor 1 plus the complete set of places" (used in CA_C_001 §4).

## C5. Hasse–Minkowski in its classical form: local isometry invariants decide the sign
**Seed.** Give the form (or its finite Schur sections S_{T,k}, or A_M) a ℚ-structure, compute ℚ_p-invariants (determinant, Hasse
invariant) at every p, and conclude definiteness from local data plus a global reciprocity (Π_v ε_v = 1). Condensed/solid variant: the
same over ℤ̂ in condensed abelian groups.

| screen | result |
|---|---|
| Idx | MW-3 OPEN "no theorem either way"; condensed polarizations DEAD (integer-weight wall, G1_B3_R2/R3) |
| category | ✗ definiteness of a ℚ-form is a condition at the place ∞ alone; finite-place invariants never decide it (to be proved in CA_C_002) |
| ℚ-structure | ✗ the entries of Div_M involve Λ(n) = log p; the log p are ℚ-linearly independent, so there is no rational structure in which the comb is defined over ℚ |
**Verdict: DISCARD as a route; survives as a closure question for MW-3.** The question "what is the only well-posed local–global
reading of MW-3?" is developed in **CA_C_002** because it re-labels an OPEN item of the index.

## C6. Torus/line splitting on multiplicative boxes (Kronecker sum against the Kronecker line)
**Seed.** On a multiplicative box S = Π_p {p^0,…,p^{K_p}}, Div_M|_S is a Kronecker sum of one-prime Toeplitz operators (rem:boxes), so it is a
**Haar integral over the torus 𝕋^S** of the symbol Σ_p δ_p(θ_p). Arch_M|_S is an integral over the **Kronecker line** θ_p = τ log p.
The line is the product formula (one archimedean τ drives every place). Local = torus (independent places); global coupling = line.

| screen | result |
|---|---|
| Idx | partial: Bohr torus (NT_003/005; G2_B7 Haar-null; F41 log p independence: REF-D); boxes rem:boxes; prop:nearfree |
| B″ | the torus/line representation holds for every comb supported on prime powers; ✗ as a mechanism |
| (S) | Near_M is the failure of the box structure; positivity of Arch − Div − Near is (S), an exact restatement |
**Verdict: no mechanism; merged into CA_C_002** as the explicit form of MW-3's only well-posed reading.

---

## Ranked survivors
1. **C3** (product formula as global coupling): a definite mathematical question with checkable answers (classes of relaxations).
2. **C5 + C6** (closure question for MW-3): no mechanism expected; the deliverable is a correct label for MW-3 and the explicit identification
   of what is local and what is global in the window form.
Discarded: C1 (retry, REF-D), C2 (B″, O7/O11/O15), C4 (REF-D).
If both developments end without a mechanism, a second batch from a different part of the area is needed (§ in the final report).
