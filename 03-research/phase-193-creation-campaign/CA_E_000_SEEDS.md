# CA_E_000 — Seed generation, front E (quantum mathematics and operator algebras)

Phase 193. Pen and paper; **no numerics were run**.
**No certified negative value for ζ anywhere on this front.**

Read before seeding: CAMPAIGN_LEDGER (O-label erratum: Paper 47 numbering used here), CA_A/B/D_SYNTHESIS, CA_C_004, CA_C_007
(+ reviews, CA_SYNTHESES_REVIEW), P47 §20 (def:shape-ops, lem:shape-est, lem:shape-ident, thm:shape, cor:shape),
prob:region (R)(1)–(11), thm:oneprofile, prop:AM; ROUTES-TRIED-INDEX README (all sections), 02 (R9-04), 03 (NG-67, P45-1, P51-1/2,
P53-1, KREIN rows), 04 (G4H-159 G1, G8H-R160_S5 #16/#20 Thm U, G4C-R177 Petz, G6C-R178 CAR/Robertson, G6B-R180 Kadison, G4C-R181,
G4B-R182, G2A-R183_008), 06. Corpus grep (03-research, 01-context) for: KMS, Bost–Connes, Tomita, Araki, Connes cocycle, flow of
weights, Haagerup, subfactor, Jones, Stinespring, completely positive, Choi, operator system, entangle, CCR/CAR, Fock, second
quantization, Schur product, GCD matrix, Kakutani, Golden–Thompson, Lee–Yang, interlacing families, de Finetti, Löwner.
Relevant prior hits: 114_d_92 (vacuum CAR), 114_d_116 (BC KMS central-temperature obstruction), 114_d_117 (Lindblad), 114_d_142
(Fock descent NO-GO), 114_d_195 (CP Poisson dilation), phase-120 P3 (BKM/modular Hessian), G1_B2_R5 Thm U (III₁ core flow carries no
arithmetic), G1_B10_R5 (standard form / natural cone), R177 (Petz), R178 (CAR cumulant / Robertson), R180 (Kadison equality),
R160_M8 Prop E (Schur products of certificates), NT_00x (Kakutani in the height flow).
Excluded by the coordinator: free probability (CA_C_006), CQG prime current (NG-67), OS / reflection positivity (CA_A_007).

Screen key. Idx = retry of an indexed route. (R)k = clause k of prob:region. (P)k = CA_B conditions. O-labels are Paper 47's.
B′ = estimate with a remainder; B″ = identity valid for every comb; FE-gen = holds for every FE series (Epstein x²+5y² included);
REF-D = exact restatement of the target; [crit] = can it resolve a bottom at relative precision M^{−3}? "✗" = fails there.

## Structural fact used by every screen (PROVED in CA_E_001)
By thm:oneprofile and prop:AM the target is the positive definiteness of the function φ(q) := 𝖡(log q) on the **abelian** discrete
group G = ℚ_{>0}^× ≅ ⊕_p ℤ. Its dual Ĝ is a compact abelian group (the solenoid ∏_p S¹ in prime coordinates), and the Kronecker line
ι: ℝ → Ĝ, τ ↦ (q ↦ q^{iτ}) is injective with dense image. Hence (CA_E_001 Thm 1): **positive = completely positive = positive on
product (separable, Euler-product) test vectors.** All quantum-information distinctions (entanglement, decomposability, CP versus
positive, Choi rank, block positivity) collapse for this object. The only non-commutativity in the target lies in the window
compression (time limit to I_T, Tate conditions), and that is the Sonin/prolate/Wiener–Hopf territory (phase 183, R186, W-*), which
is closed.

---

## E1. KMS phase transitions beyond Bost–Connes (Laca–Raeburn Toeplitz algebra of ℕ ⋊ ℕ^×; Cuntz–Li ring algebras)
**Seed.** The Toeplitz algebra 𝒯(ℕ⋊ℕ^×) has partition function ζ(β−1), a richer phase diagram (unique KMS on [1,2], measures on 𝕋
for β > 2, ground and KMS_∞ states). Use positivity of the KMS states (or of the extremal decomposition) at the critical boundary.

| screen | result |
|---|---|
| Idx | ✗ retry in substance: 114_d_116 (BC: the Gibbs state is trace class only for β > 1; at β = ½ type III, infinite energy; KMS two-point matrix diagonal in prime-power depth), R9-04, G4H-159 G1 |
| (R)(4)-like | ✗ KMS positivity holds at real β only. The window form needs s = ½+iτ for all τ; a complex inverse temperature does not give a state (same obstruction as CA_A_002: PF only at real s) |
| O11 | ✗ the ℕ⋊ℕ^× phase diagram depends on the semigroup and on the density of primes; Beurling semigroups have the same type of diagram (Thm U for the core flow) |
| (R)(2) | ✗ no Γ-factor: KMS data see only the Euler side |
**DISCARD.**

## E2. Tomita–Takesaki: Connes' Radon–Nikodym cocycle criterion ψ ≤ φ ⟺ (Dψ:Dφ)_t continues to the strip with ‖(Dψ:Dφ)_{−i/2}‖ ≤ 1
**Seed.** Read the target as the inequality "comb ≤ archimedean" between two weights on P_T and check it by analytic continuation
of the cocycle (a non-commutative tool that is new to the corpus as a criterion).

| screen | result |
|---|---|
| category | ✗ neither summand is a weight: m(0) = ψ(¼) − log π < 0 and the comb multiplier Σv_n cos(τ log n) is indefinite. Positive parts require a split, and every affine split writes the target via its own spectral data (CA_B_008 §2): REF-D |
| commutativity | ✗ both are multiplication operators in τ; the cocycle is (ψ/φ)^{it}, and the criterion becomes a pointwise symbol inequality, which is false at τ = 0 (σ_T(0) = C₀ − 𝖠 < 0; rem:shape-est(b)) |
| (R)(5) | ✗ local on the symbol (W-loc) |
**DISCARD.**

## E3. Subfactors / Jones index / Temperley–Lieb Gram positivity
**Seed.** Jones' rigidity comes from the positivity of the Markov trace on TL (Gram determinants of Chebyshev type). Find an inclusion
N ⊂ M from ζ data whose Markov-trace positivity is the window form; for example the Hecke-pair inclusions of the Bost–Connes system
(Γ₀ ⊂ Γ₀ ∩ gΓ₀g^{−1}, g = diag(n,1), index n).

| screen | result |
|---|---|
| object | ✗ no map from the window form (a continuous Toeplitz form with an infinite comb) to a TL/meander Gram is known or constructible from the data. The only natural inclusions (Hecke pairs) have index n ∈ ℕ, which is integrality (I) plus the semigroup |
| (R)(2), prop:shape-inputs(i) | ✗ no FE, no Γ; the P-rough sub-semigroup gives Hecke pairs too (O6 survives) |
| CA_A_008 | ✗ a quantized invariant along a path is the integer-invariant collapse (REF-D) |
**DISCARD.**

## E4. Complete positivity / Choi matrices / entanglement witnesses / decomposability (Størmer–Woronowicz) on ℓ²(ℕ) = ⊗′_p ℓ²(p^{ℕ₀})
**Seed.** Multiplicativity makes ℓ²(ℕ) an infinite tensor product over primes. The minimizer of 𝔸_M is close to m^{−½}w(m/M),
almost a product vector. Prove positivity on product (Euler-product) vectors, the "block positivity", then promote to positivity by
a decomposability or separability argument, as in entanglement theory.

| screen | result |
|---|---|
| Idx | not indexed as such (new framing) |
| structure | the global object is a positive-definite-function problem on the abelian group G; **CA_E_001 Thm 1 (PROVED): block positivity on product vectors is equivalent to positivity**, and positive = CP for Schur multipliers. Nothing is gained: the promotion step is free, and the block-positivity statement is the target itself |
| REF-D | ✗ exact restatement (a new restatement, recorded as a tool) |
| B″ | ✗ the equivalence holds for every continuous 𝖡 (every comb) |
**DISCARD as a sign step; developed as a tool + NO-GO in CA_E_001.**

## E5. Schur (Hadamard) multipliers: factor 𝔸_M = 𝔾 ∘ 𝔹 through a multiplicative PD kernel (GCD/Smith matrix gcd(m,k)^{2β}(mk)^{−β}, Haagerup kernels e^{−tℓ}, coherent-state kernels)
**Seed.** The Schur product theorem gives 𝔸 ⪰ 0 from 𝔾, 𝔹 ⪰ 0. The Euler product would enter as a tensor-product (GCD) factor 𝔾.

| screen | result |
|---|---|
| Idx | R160_M8 Prop E (Schur products of certificates) is a different object; GCD matrices appear only in R162_1101 / G2 (no factorization) |
| feasibility | ✗ **NO-GO PROVED (CA_E_001 Thm 2)**: no factorization φ = g·b with g, b PD on G and g having one non-degenerate atomless local factor exists, because the Bochner measure of φ is carried by the Kronecker line ι(ℝ) and μ_g * μ_b gives that line measure 0. This covers all GCD/Smith, Haagerup ℓ¹-length, Gaussian and ITPFI product kernels. Factorizations through line-type kernels 𝖡₁(log q)𝖡₂(log q) are convolution factorizations ν = ν₁ * ν₂ of the profile measure (zero side, (R)(4)) or squares with Cauchy–Schwarz ((R)(3), N_018) |
| B″ | ✗ the NO-GO holds for every comb |
**DISCARD (class NO-GO, PROVED).**

## E6. CCR quasi-free states: Robertson–Schrödinger γ + iσ ⪰ 0; second quantization Γ(C) of a contraction
**Seed.** Present the window form as the covariance γ of a quasi-free state on CCR(P_T); positivity of the state forces γ + iσ ⪰ 0,
which is stronger than γ ⪰ 0. Get the state by second quantization of an arithmetic contraction (prime gas).

| screen | result |
|---|---|
| Idx | ✗ retry: 114_d_92 (vacuum CAR types the form, does not create the sign), 114_d_142 (Fock descent unbounded: √(r!) defect), R178 (CAR cumulant / Robertson affine: NO-GO), 114_d_195 (CP dilation: defect = spectral gap = target) |
| (P1)/REF-D | ✗ the state is positive only if γ+iσ ⪰ 0 is already known; a state built from a contraction gives a positive γ only through a factorization γ = C*C, which is the global-square problem (R)(3) |
**DISCARD.**

## E7. ITPFI / Araki–Woods type of the prime product state; Kakutani dichotomy at β = ½
**Seed.** ⊗_p ρ_p with ρ_p = (1−p^{−β})Σ p^{−jβ}|j⟩⟨j| (primon gas). Its product Bochner measure on Ĝ (local Poisson kernels) is
equivalent to Haar iff Σ_p p^{−2β} < ∞ (Kakutani), so β = ½ is exactly the transition. Use the type/singularity change as the sign.

| screen | result |
|---|---|
| Idx | ✗ Thm U (G1_B2_R5): the III₁ core flow is the same for ζ, Beurling and BC; NT_00x already use Kakutani in the height flow |
| O11, O15 | ✗ the dichotomy reads only Σ_p p^{−2β}, i.e. the density of primes: any Beurling system of density one has the same transition |
| (R)(7) | ✗ wins from the density, not the fluctuation |
| CA_E_001 Thm 2 | ✗ a product state's kernel cannot be a Schur factor of φ |
**DISCARD.**

## E8. Golden–Thompson / Peierls–Bogoliubov / Gibbs variational lower bound for the ground energy λ_A
**Seed.** λ_A = −lim β^{−1} log Tr e^{−βH}, with H = arch − comb on P_T. Use Tr e^{−β(H₁+H₂)} ≤ Tr e^{−βH₁}e^{−βH₂} and the Bessel
expansion of e^{βv_n cos(τ log n)}.

| screen | result |
|---|---|
| B′ | ✗ a trace inequality is an estimate with a remainder; lem:shape-est(i) forces precision ≤ 4·10⁹Te^{−15.449T} |
| structure | ✗ H₁, H₂ are both multipliers in τ and commute before compression, so Golden–Thompson is an equality there; all its content would come from the compression (Sonin territory, closed) |
| [crit] | ✗ free-energy bounds lose O(β^{−1}log dim), far above M^{−3} |
**DISCARD.**

## E9. Kadison–Singer / Marcus–Spielman–Srivastava interlacing families; real stability; Lee–Yang
**Seed.** One-sided spectral control of sums of rank-one pieces (each contact as a rank-one or rank-two update) through the largest
root of an expected characteristic polynomial; Lee–Yang circle theorem for ferromagnetic structure.

| screen | result |
|---|---|
| Idx | ✗ phase 11 (interlacing / hyperbolicity: falls to PF₂), 104_21, R155_046/047, Lee–Yang under DBN/heat (N5, phase 33) |
| B′, cor:shape(b) | ✗ MSS bounds are averages over a family (class arguments) with remainders; existence of a good partition is not positivity of the sum |
| (R)(4) | ✗ Lee–Yang statements concern zero location |
**DISCARD.**

## E10. Araki relative entropy, data-processing monotonicity, Petz recovery
**Seed.** Monotonicity of a quantum f-divergence under coarse graining (deleting primes ≥ P) as a one-sided inequality.

| screen | result |
|---|---|
| Idx | ✗ phase-120 P3 (BKM modular Hessian: local von Mangoldt tower exact, global fusion = global square), R177 (Petz: canonical construction NO-GO PROVED) |
| direction | ✗ coarse graining raises the bottom (adding contacts lowers it; lem:monoT), so monotonicity runs the wrong way for a lower bound |
**DISCARD.**

## E11. Operator systems: spectral truncations (Connes–van Suijlekom), Toeplitz ↔ Fejér–Riesz duality, Arveson extension
**Seed.** The window is a spectral truncation; its operator system is Toeplitz, with dual the Fejér–Riesz system. Positivity in the
Toeplitz operator system is a Carathéodory–Toeplitz / extension statement; add the two Tate jets as a codimension-2 constraint.

| screen | result |
|---|---|
| Idx | ✗ Kreĭn extension indeterminacy thm:KEPdich (REF-D), ES-14, Kreĭn–Langer rows, P45-1 (Weil–Toeplitz C*-algebra NO-GO) |
| REF-D | ✗ Toeplitz positivity with extension = the target restated |
**DISCARD.**

## E12. Non-commutative SOS / Positivstellensatz hierarchies (Helton, DPS symmetric extensions, quantum de Finetti)
| screen | result |
|---|---|
| Idx | ✗ CA_C_006 (Positivstellensatz), thm:sos, N_018, arithmetic squares (empty for T ≥ ½log3) |
| (R)(3) | ✗ certificate / square classes (class (D)) |
| structure | ✗ by the commutative collapse (CA_E_001) every NC hierarchy reduces to the classical moment/SOS hierarchy on Ĝ |
**DISCARD.**

---

## Pre-screen summary
| seed | killing clause(s) | survivor? |
|---|---|---|
| E1 KMS beyond BC | real-β only; O11; (R)(2); retry 114_d_116 | no |
| E2 Connes RN cocycle | not weights; commutative ⇒ pointwise symbol (false at 0); REF-D | no |
| E3 Jones index | no object; (R)(2), O6; integer collapse | no |
| E4 CP / entanglement / decomposability | commutative collapse ⇒ REF-D, B″ (CA_E_001 Thm 1) | tool only |
| E5 Schur multipliers / GCD factorization | NO-GO PROVED (CA_E_001 Thm 2) | no |
| E6 CCR / Robertson / second quantization | retry (114_d_92, 142, 195; R178); global square | no |
| E7 ITPFI / Kakutani | O11, O15; Thm U; (R)(7) | no |
| E8 Golden–Thompson / Gibbs | B′; commuting before compression | no |
| E9 Kadison–Singer / Lee–Yang | retry; B′; (R)(4) | no |
| E10 Araki / Petz | retry (P3, R177); wrong monotonicity | no |
| E11 operator systems / truncations | REF-D (KEP) | no |
| E12 NC-SOS / de Finetti | (R)(3); commutative collapse | no |

No seed passes all screens. E4/E5 are developed in CA_E_001 because they produce PROVED statements that close a whole subarea in one
stroke (they explain *why* the quantum-information toolbox has no purchase on this object). No second batch is generated: the
untouched subareas listed in the brief are exhausted by E1–E12 together with the excluded ones (free probability, CQG, RP); see
CA_E_SYNTHESIS.md.
