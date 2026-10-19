# SPEC_SIGN_OBJECT_006 — Round 15: single constraint table, barrier theorem Φ200, verified virgin space

Phase 200 ("sign object"), round-15 synthesizer. Pure mathematics; no new numerics (the numbers
cited come from already-certified or labeled memos). This file does not edit
the index or the README; the proposed entry is in §F.

## Summary (≤300 words)

**(A)** A single table with the 25 constraints of phase 200 and the 28 prior ones, grouped. For each one the
label, the class it kills, and the falsifier backing it are indicated. The hard ones from this phase are R-K1, R-Q2, R-Q6, R-Π, R-Π4,
C-Guo, C-E′, C-θ, C-hom, C-data, C-pol, 13.1 and R-F1/R-F2. R-Z1, M200 in its channel (i), and C-τ remain ARGUED or CONDITIONAL.
**(B)** Theorem Φ200. The class 𝒦_Φ is defined by its inputs (I1–I10) and its operations. Every element of 𝒦_Φ giving a
lower bound for λ_A falls into one of five branches: comb-generic, REF-D, functional of h*, blind to ζ, or equality between data.
The proof is given piece by piece, with its label at each step: PROVED by branch for the listed subclasses, ARGUED as a class
(exhaustiveness of the catalog and symbol channel). Two pieces are added. The first is the transfer additivity lemma
(PROVED): every Euler product containing ζ as a factor has the form 𝔞^ζ + 𝔞^{L′}, so that no degree change
returns sign to ζ. The second is the Łoś dichotomy for ultraproducts (ARGUED).
**(C)** Virgin space. 18 items were reviewed by grep. Twelve are already in 𝒦_Φ or in the index: raising
operator, parity of Ω, ultraproducts, (S⁺) as structure, even Theorem A, non-unimodular transfers, W⁻, dR_Λ, κ-band, additive Hankel,
chordal decomposition and transport. Three gaps remain, all outside the degree-1 window carrier: objects of dimension
or multiplicity over the pair (ℚ,+)⋊(ℚ^×,·), profinite rings with + and ·, and the function 𝔖 used as a discontinuous weight inside
an inequality.
**(D)** Three candidates with a declared Λ channel: Ξ1 (von Neumann dimension of ax+b over ℚ, sensitive to h), Ξ2 (Loeb
form over Ẑ with ring structure) and Ξ3 (relative class inequality in the Heegner tower with weight 𝔖). Each one comes with a filter,
a test, and a first lemma.
**(E)** Ranking: Ξ1 > Ξ3 > Ξ2. Round 16: first lemma of Ξ1 (trace of the Chebyshev element in L(ℚ⋊ℚ^×_{>0})), with an
audit carrying the mandate "V2.4 + Bost–Connes".

L′♯: OPEN. Row D: OPEN.

---

## 0. Corpus and index (mandatory)

Read: README; LEDGER_L1–L5; SPEC_001–005; AUDIT_200_SPEC_001–003, AUDIT_200_AMU, AUDIT_200_PIMU, AUDIT_200_EPSTEIN,
AUDIT_200_Q2; K1_OSG, K3_GAMMA, Q2_LADDER, C1_DUPLICATION, B1_FLAT, A_MU_FACTORIZATION, PI_MU, PI4_JUMPS, Z_CARRIER,
GUO_QUANT, META_200_BARRIER, P2_GAUGE_RADICAL, P3_SMOOTH_B1, LEMMA_E_EPSTEIN, COSH_DEFECT, Q2_DEGREE2, LEMMA_I3, R11_1_CUTS,
R11_2_ORIGIN, LEMMA_12_1_H3, LEMMA_13_1_CUMULANT, F0_TEST; ROUTES-TRIED-INDEX/README.md §"Phase 200" (l. 509–541),
§"Phase 197" (l. 417–437, incl. BARRIER_D2_001 and BARRIER_W_001), fronts G/H/I (l. 255–280); phase-199
AUDIT_CONSTRAINTS_001; phase-197 BARRIER_001_TRICHOTOMY; phase-199 PROOF_L_SHARP_H_001 (Thm H.4, W⁻); phase-196 INV_V_001/002.
The greps for each item in §C are in the table of §C (column "grep").

---

## A. Single constraint table

Class convention: "comb-gen." = any proof whose steps hold for some certified falsifier (a_P, cΛ c≠1,
Beurling, DH, Epstein x²+5y²); "REF-D" = the statement restricted to Λ is 𝒲 ≥ 0 (or 𝔞_T ≥ 0 on P_T).

### A.1 Phase 200 constraints

| id | statement (one line) | label | class it kills | falsifier / support |
|---|---|---|---|---|
| R-K1 | Every Hankel form using the gap c_N=0 on [2,μ) has an NN′ product structure; the sign lives in quotients N′/N | PROVED (K1.1′) | boundary OS reflections, Hankel with gap | Möbius correlation Σ(c∗c)(P)P^{−½}G ≠ 0, holds for Beurling's μ_𝒫 |
| R-Q2 | Mollifier levels, p-classes, S-coprime parts, divisor bands are translates within the radical | PROVED given Guo L4.4 (Lemma R) | ladders, mollifiers, subcombs | 𝔊_{YY′} ≡ W_T(g); mollifier difference with 𝒲=0 |
| R-Q6 | Descent of 𝒲 to the quotient by the gauge already uses exact Λ | PROVED (AUDIT_SPEC_003) | "build on 𝒬_μ as if universal" | a_P, cΛ, DH already fail in the quotient |
| R-C1.1 | Induction in μ with step = infimum over the 𝒲-orthogonal complement ≡ L′♯ at the new level | PROVED (Prop C1.1) | doubling κ(2μ) ≥ θκ(μ) | κ_new sandwich |
| R-C1.2 | In the rough representative, exact Λ of new contacts either does not align or aligns in a radical subcomb | PROVED | counts (N,pN) | C3′: 𝒞′ diverges within the radical |
| R-C1.3 | Chebyshev/Bertrand/Rosser–Schoenfeld do not close μ/2→μ (TV at scale O(log μ) vs margin e^{−4πμ}) | PROVED (CITED bounds) | prime bounds in intervals | a_P at scale e^{−4πμ} |
| R-B.1 | Transport of ℓ between levels = prolate problem without Λ; uniform B.1 FALSE | PROVED (B1_FLAT) | induction by escape transport | harmonic stacking, β_μ ≤ C/log μ |
| R-F1 | Every A_μ on the exterior form sees Λ only via Λ∗1 = log | PROVED (nearly tautological) | "semiring" factorizations | Beurling survives in the formula |
| R-F2 | On the full line every transverse convexity is annihilated by the FE; deformation n^ε = moving σ | PROVED | σ-derivatives, Theorem D, Lemma F as sign | index rule l.463, MM.1 |
| R-Π | Every Π with kernel ⊇ 𝒢̄_T is archimedean and blind to the comb | PROVED (Π.0′–Π.1) | projectors/quotients as arithmetic carrier | 𝒢̄_T identical for Λ, a_P, cΛ, Beurling, DH |
| R-Π4 | The minimal-escape representative f♯ falls outside the domain of the prime-side formula; σ², f♯(0)² not at escape scale | PROVED | jump comb, Π.4, Π.5 as sign | plateaus: σ → −(λ/2)^{½} with ℓ → 0 |
| R-Z1 | Z used only via its symbol on the line holds equally for DH; Euler enters 𝒦₁ only via (α) σ>1, (β) Guo, (γ) gap | ARGUED (missing DH transfer lemma) | AFE, commutators [𝒫,θ′], moments | DH (FE and Γ equal, no Euler) |
| C-Guo | Every use of radical/gauge/pole/Tate as sign must name which property Epstein lacks | PROVED (Prop 1.3 + Lemma 2.1) | quantitative (β), count κ, "Tate theorem" | Epstein x²+5y²: κ=2, zeros outside |
| C-E′ | If the class contains ½(Λ_K+Λ_ψ)+Λ_cosh, no ∀Λ positivity statement holds for T ≥ 1.59 | PROVED as falsifier (Lemma E); ARGUED as a principle | positivity stable under convex combination of Euler log-derivatives + comb ≥0 on composites; "Λ ≥ 0 in the window" | Lemma E certified [−0.0599398587, −0.0599398456] |
| C-θ | The form is affine in θ over L₁^{(1−θ)/2}L₂^{(1+θ)/2}; no linear/convex inequality separates the Euler extremes | PROVED (Theorem S) | interpolations, convexity in θ | polynomial 3.4172 − 3.4713t² − 0.0078t⁴ |
| C-τ | S_∞ = {τ: form ≥0 ∀T} has empty interior; S_∞ ∩ CM ⊆ {τ_D} | CONDITIONAL (Prop 4.2, DH) / ARGUED on the arc | continuous bounds in τ uniform in T | h>1 dense (Heilbronn), Bateman–Grosswald |
| C-int | (Weil = atomic measure with integer weights) ∧ Euler separates the battery, but is on the zero side | PROVED as separation; NO-GO as object | integer divisors as sign | Kaczorowski–Perelli (anchoring) |
| C-hom | The form is 0-homogeneous in the theta coefficients: no quadratic/four-point identity in θ exists | PROVED (Lemma H) | quadratic forms in θ, Bochner of θ | r ↦ 2r does not change 𝔞 |
| C-data | A relation only moves the dual value if it contains a variable of (P)/(D) | PROVED (Theorem C1) | multiplicative cuts in the LP/SDP | dual value invariant ∀M (incl. ½log5) |
| C-pol | Every candidate acting via the moments (A,B) is null in P_T | PROVED (Theorem O3) | pole, residue, Tate mode, lattice origin, 𝔊_T | witnesses of a_P and Epstein in P_T with A=B=0 |
| R-I3 | Every object on the pencil cΛ + gauge radical = indefinite comb datum ⊕ sign datum 𝒲 in the quotient | PROVED (Lemma I.3 framework) | block inertia, pencil in c | A_⊥⊥(1) gap O(1)=3.77 independent of μ |
| 13.1 | The class defect 𝔞^{Q₁} − h⁻¹Σ_χ𝔞^{L_χ} is a pure finite comb in P_T, indefinite; no Jensen/convexity under averages of L with the same Γ | PROVED | cumulants, convexity under Euler averaging | modulation + Riemann–Lebesgue; φ ∈ [−3.40, 3.26] |
| C-E (Lemma E) | every proof must feel Λ_cosh | superseded by C-E′ (correction of an overclaim) | — | AUDIT_200_EPSTEIN §6 |
| M200 | methods over 𝒬_μ with channels (i)–(iv) and uniform conclusion or 𝓛_lin → comb-gen./certificate/REF-D | PROVED without (i); ARGUED with (i) | 𝒦_200 | certified battery |
| M200′ | 𝒦_200 ∪ 𝒦_NL → comb-gen./REF-D/Theorem X/blind to ζ/identification | ARGUED as a class; PROVED by pieces | infima, det, inertia, Fredholm, four-point | Prop 2.1 (KP), Prop 2.2, Lemma I.1 |

### A.2 The 28 earlier ones (AUDIT_CONSTRAINTS_001), summarized by block

| block | items | label (post-audit) | what it kills | support |
|---|---|---|---|---|
| Hard class constraints | 1 (TV-slack ≤ λ^W in the window carrier), 2 (identity + comb-generic Bochner/CS), 8 (no antisymmetric Hilbert kernel), 12 (Eψ₀ + small repair), 17 (fix the gauge), 24(a,b) (Möbius lattice structure; invalid single-line models) | PROVED (1: qualitative; size CONDITIONAL) | TV-robust premises, comb-generic proofs, Montgomery–Vaughan, unique prolate | certified falsifiers, Slepian |
| Soft | 3 (only diagonal scalar weights at Re s=½), 4 (multipliers: ARGUED), 5 (conjunction a_n≡1/residue/Γ_ℝ/aliasing, localization ARGUED), 7, 10 (polar ≡ 0 in base FF.1), 11 (flow without virial (H)), 14, 15, 18, 19(b), 21, 25 (cancellation of 33–70 digits), 27, 28 | ARGUED/NUMERICAL | depends on formulation | reopenings II/JJ/KK/LL/MM/NN/OO already NO-GO |
| Mislabeled | 6 (target form μ^{−A}dist², is the definition of L′♯), 9, 13 (positive fact: rank-one pole), 16 (open Sonin/PW transfer), 20, 22, 23 (empty), 26 (ext-layer constants) | — | nothing | — |

### A.3 Constraints from phases 194–197 used as a filter in this round

G1 (free monoid ℕ^× does not distinguish ζ from Beurling, PROVED); EI_003 symbol rigidity (no exact identity with
FE/Euler/Mellin/Poisson is non-linear in Λ, PROVED); V2.4 Chebyshev rigidity (lattice kernel with exact transfer ⇒
rank one ⇒ no Hermitian lifting, PROVED); Theorem X (every first-order discriminant is a functional of h*);
Trichotomy Thm 3 and half-space Thm 5 (phase 197); BARRIER_D2 Thm 1–2 (Lipschitz; stability by defect ⟺ WP_T(Λ) ∧
rigidity without sign; inert continuation); BARRIER_W (Morse index/spectral flow/non-crossing); Prop 2.1 (ζ isolated in
degree 1, conductor 1, KP CITED).

---

## B. Unified barrier theorem Φ200

### B.1 The class 𝒦_Φ

Fix T ≥ 0.60 (and μ = e^T in the exterior convention). An **object** 𝔒 of 𝒦_Φ is a pair (inputs, operations) with
output Ψ(T; a) ∈ [−∞, ∞) defined on a class of combs S ∋ Λ and sound (Ψ(T;a) ≤ λ_A(T;a) ∀a ∈ S). The admitted
inputs are:

- **I1** the window form 𝔞_T^{(a)} and its restrictions to subspaces of P_T or of 𝒟 (including the Legendre block);
- **I2** the escape quotient 𝒬_μ = L²(λ,∞)/𝒢̄_T, its norm ℓ/2, and any projector Π with ker Π ⊇ 𝒢̄_T;
- **I3** the symbol of Z (or Z_log, Z′/Z) on Re s = ½: multiplier, FE, AFE (smooth, Riemann–Siegel, dependent
  cutoff), moments, commutators;
- **I4** coordinates: levels Y, classes p | N, S-coprime parts, divisor bands, quotients N′/N, blocks 𝔅_k, z_ρ,
  bridge ι, the gap c_N = 0 and c_N = −μ(N) on [μ, 2μ);
- **I5** polar moments (A, B), residue, Tate mode, Poisson constant term;
- **I6** theta and its coefficients r, in any normalization (θ, θ − 1, Jacobi, log θ, r(1)=1);
- **I7** L-function averages with the same Γ (class characters, cosh, cumulants, theta pencil);
- **I8** cuts and relations in P47's dual LP/SDP (def:PD, thm:Z);
- **I9** derivatives or families in the parameters c (comb), ε (n^ε), θ (Euler interpolation), t (cosh), τ (lattice Z_τ), T;
- **I10** Möbius, Poisson, Ramanujan, Selberg identities, Λ∗1 = log, Λ∗Λ, Hecke–Chebyshev.

Operations: the six of the trichotomy (O-lin, O-conv, O-place, O-cone, O-∂log, O-id, O-sq, O-est) plus the non-linear ones of
𝒦_NL (infimum/λ_min, det and Gram cofactors, inertia/jump index, pencil roots, functionals of the minimizer,
products and four-point forms, Fredholm/Toeplitz indices of quotients), and finite composition of all of the above.

### B.2 Statement

**Theorem Φ200.** Let 𝔒 ∈ 𝒦_Φ with sound output Ψ on S ∋ Λ, and suppose 𝔒 decides T (Ψ(T;Λ) ≥ 0). Then at
least one of the following holds:
1. **comb-generic**: S contains a falsifier f from the battery with λ_A(T;f) < 0, and Ψ is not uniform on S (it only
   reproduces already-known values of Λ);
2. **REF-D**: the statement "Ψ(T;Λ) ≥ 0" is, by a proved identity or equivalence, 𝔞_T ≥ 0 on P_T or 𝒲 ≥ 0 on 𝒬_μ,
   or is a dual certificate with value ≤ λ_P(T) (thm:D1);
3. **functional of h***: Ψ depends on Λ only through the minimizer h* (Theorem X; N2);
4. **blind to ζ**: Ψ takes the same value at ζ as on a family constant through ζ (Prop 2.1), or is a zero count null at
   ζ (Prop 2.2), or it vanishes identically at ζ (13.1(iii), 𝔇 ≡ 0 for h = 1);
5. **equality between data**: Ψ separates the battery by existence of structure (radical, 𝔖, C-int, H.3 collapse
   relations) without entering an inequality with variables (C-data).

### B.3 Proof by pieces

The strategy: each input I1–I10 has a channel lemma sending it to a branch, and the operations of §B.1 preserve the
branch or worsen it (composition of branches falls into the "worst" one, with the order 2 ≻ 5 ≻ 4 ≻ 3 ≻ 1 of information
loss). The composition clause is ARGUED: there is no formal proof calculus demonstrating it.

**Piece Φ.1 (I1, form and restrictions). PROVED.** For fixed F, a ↦ 𝔞_T^{(a)}(F) is affine. The function λ_A(T;·) is
concave and Lipschitz, |λ_A(a) − λ_A(b)| ≤ Σ_{n<N}|a(n)−b(n)|/√n (BARRIER_D2 Thm 1, = prop:wit-sens CITED). A Ψ built
only from values of 𝔞 at fixed tests and with O-lin/O-sq/O-id falls into 𝓛_lin, i.e. into branch 2 by thm:D1. If restricted
to subspaces, the infimum can only rise (C1 Prop C1.1), and a restricted infimum containing the extremal is L′♯ on that subspace
(branch 2; R-C1.1). Every stability inequality λ_A(a) ≥ −CΔ(a), with Δ(Λ) = 0, is equivalent to WP_T(Λ) together with a
rigidity without sign (BARRIER_D2 Thm 1): branch 2.

**Piece Φ.2 (I2, quotient and projectors). PROVED given Guo L4.4 (CITED).** Lemma M.iii + R-Π: Π factors through Π_μ, which is
independent of the comb (F1), and B∘Π_μ is eq:ext-starstar (F3). Branch 2 if B uses 𝒲, branch 1 if not. The descent itself already uses
exact Λ (R-Q6): with (β) as an exact premise there is pinning (branch 2), without it the class contains a_P, cΛ and Beurling (branch 1).
The quantitative version of (β) was computed and gives 𝔡_a of size O(1) against an escape of 10^{−11} to 10^{−70} (P2_GAUGE,
NUMERICAL). By Φ.1 it is a stability inequality, so it also falls into branch 2.

**Piece Φ.3 (I3, symbol). ARGUED.** Lemma M.i / R-Z1: it is DH-transportable, branch 1. The DH transfer lemma is missing,
which is a statement of proof calculus (META_200 §1.4). It is the only ARGUED piece among branches 1–2.

**Piece Φ.4 (I4, coordinates). PROVED given Guo L4.4.** Lemma M.ii + R-Q2 + SQ.0 + Π.2 + Lemma Z.2′ + M.iv (R-K1): the
coordinates are constant on the fibers of the quotient (branch 2 after descent) or comb-generic, and Beurling reproduces μ_𝒫
(branch 1). The bridge ι preserves 𝒲 (branch 2).

**Piece Φ.5 (I5, polar). PROVED.** C-pol (Theorem O3): on P_T, A = B = 0, and the witnesses of a_P and of Epstein live
there. A Ψ depending on the comb only via I5 is constant on {Λ, a_P, Epstein}: branch 1. Lemma O1: 2Re(AB̄) counts the
order of the pole, not its residue.

**Piece Φ.6 (I6, theta). PROVED.** By C-hom, Ψ is 0-homogeneous in r. If polynomial after normalizing, its order-2 term is
𝒬_g, which is indefinite (COSH_DEFECT, branch 1). Under multiplicativity it collapses to the form linear in Λ (H.3, branch 2 via
Φ.1). Bochner on θ only uses r ≥ 0 (branch 1). The conjunction Poisson ∧ multiplicativity is 𝔖 = 0 (branch 5).

**Piece Φ.7 (I7, L-function averages). PROVED.** Lemma 13.1 gives a pure finite comb, indefinite on P_T: any
uniform inequality in g is false, and one that only holds at a witness is branch 1. For ζ, 𝔇 ≡ 0 (branch 4). By Theorem S (C-θ) any
linear or convex inequality in θ holding at the h=1 extreme holds at the Epstein extreme: branch 1 by C-E′.

**Piece Φ.8 (I8, dual LP). PROVED.** Theorem C1 / C-data: if the relations are between data, the dual value does not move
(branch 5). If they are between variables, it is still 𝓛_lin and its value is ≤ λ_P (branch 2). The robust reading with variable weights
gives back thm:Z (Theorem C2, branch 2).

**Piece Φ.9 (I9, parameters).** There is one case per parameter.
- c: Lemma I.3 gives an affine pencil and a Schur complement that is 𝒲 in the quotient (branch 2, PROVED).
- ε: it is Theorem D, a chain rule that moves σ (R-F2, branch 2, PROVED).
- θ: Theorem S, affine (branch 1 via C-E′, PROVED).
- t: even polynomial, same case.
- τ: C-τ, no continuous bound works (branch 1, CONDITIONAL).
- T: Lemma M and the crossing law H.4 are generic per the H_001 table; condition (H) at the minimizer is branch 3
  (PROVED by the H_001 table). Spectral flow and non-crossing fall into BARRIER_W (branch 2).

**Piece Φ.10 (I10, identities). PROVED.** By symbol rigidity EI_003, every exact identity is linear in Λ
(branch 2 via Φ.1). Λ∗1 = log as an exact premise is pinning 𝒞_1 (branch 2). The Hecke–Chebyshev transfer has rank one
(V2.4, branch 5). The Selberg form Σφ(k)y_k² ≥ 0 gives yᵀ𝔅y = 𝒲[g] (Q1, branch 2). Λ∗Λ is an order-2 relation (C-data,
branch 5). Poisson O2 is the shadow of the deleted primes (branch 1).

**Piece Φ.11 (𝒦_NL, non-linear). PROVED by pieces, ARGUED as a list (M200′).** Infimum/inertia/det/Schur: branch 2.
Functionals of g*: branch 3. Fredholm indices of quotients: branch 4. Products/four-point forms: branch 1 (N5, ARGUED).

**Piece Φ.12 (new): transfer additivity. PROVED.** Let L = ζ·L′ be an Euler product with factor Γ
Γ_L = Γ_ℝ(s)·Γ′ and conductor q′, with L′ entire. On P_T (where A = B = 0) one has
  𝔞_T^{L}(F) = 𝔞_T^{ζ}(F) + 𝔞_T^{L′}(F),
where 𝔞^{L′} uses the archimedean term of Γ′, the term (log q′)‖F‖², and the comb Λ_{L′}.
*Proof.* −L′/L = −ζ′/ζ − L′′/L′. The archimedean term is additive under products of Γ factors (log Γ_L = log Γ_ℝ + log Γ′) and
so is the conductor. The pole of L is that of ζ, and its term is null on P_T by C-pol. The form depends on L only via
−L′/L, Γ_L and the pole. ∎
*Corollary Φ.12′ (ARGUED).* No degree change by product with ζ (base change ζ_K = ζL(χ_D), ζ², Dedekind zeta of abelian
fields) gives information about the sign of 𝔞^ζ that is not already in 𝔞^ζ: the positivity of 𝔞^L is 𝔞^ζ ≥ −𝔞^{L′}, and
𝔞^{L′} has no controlled sign. For ζ², 𝔞^{ζ²} = 2𝔞^ζ (branch 2). In degree 1 the functorial liftings of ζ are
trivial (GL₁). This **closes the channel "degree change with exact transfer to ζ"**, which was not registered as
such; the character families (Thm O, R162_1102) are a special case.

**Piece Φ.13 (new): Łoś dichotomy. ARGUED (Łoś CITED).** Let 𝒰 be a non-principal ultrafilter on {μ} and ∗𝒲 = ∏𝒲_μ/𝒰
the internal form. (a) By Łoś, "∗𝒲 ≥ 0 on ∗𝒬" is equivalent to "𝒲_μ ≥ 0 for 𝒰-almost all μ": branch 2. (b) Every
standard functional of ∗𝒲 is st(∗𝒲(x)/∗ν(x)) for an internal normalization ν. If ν is the escape, one obtains the Γ-limit of K3, which is
comb-generic because Λ enters Q₁ = O(1) only (branch 1, PROVED in K3). If ν does not depend on the comb, one obtains the
unrenormalized limit, which diverges or is archimedean (K3 §2, R-Π, branch 1). The identification "every standard functional with
internal normalization is one of the two types" is the ARGUED part: an internal ν depending on μ in a non-standard way
(for instance via ∗μ(∗N) at an unlimited N) is not covered. That is the Ξ2 gap of §D.

**Piece Φ.14: transversality of curved families. PROVED (corollary of 197 Thm 5).** Let x ↦ a(x) be a C¹ family of
combs with a(1) = Λ and ⟨a′(1), w_T⟩ ≠ 0. Then, on one side of x = 1 and for |x−1| ≫ λ_A(T;Λ)/|⟨a′(1),w_T⟩|, one has
λ_A(T;a(x)) < 0 (supergradient, lem:degen). Every class of premises containing a curve transverse to w_T^⊥ is branch 1.
Examples: cΛ (a′ = Λ), Λn^{−α} (ζ(s+α)) and the exponential family r(n) = x^n of §C. That is why a non-pointwise decisive set
must be tangent to w_T^⊥ for every T simultaneously, i.e. aligned with h*: branch 3.

**Global label of Φ200.** Branches 1, 2, and 5 are PROVED for the subclasses without channel I3 (given Guo L4.4 CITED and the
certified falsifiers; for c → 1, CONDITIONAL via O_4^ε). Branches 3 and 4 are PROVED in the listed cases (Theorem X, Prop 2.1,
Prop 2.2, 13.1). There are three ARGUED points: channel I3 (DH transfer lemma), the exhaustiveness of
the list of non-linear operations, and the branch-composition rule. **Φ200 is ARGUED as a class and PROVED piece by piece.**
It does not exclude: (a) objects whose inputs are not in I1–I10; (b) non-uniform conclusions that are neither stability nor
certificate statements, from the refined D2 gate, if their dependence on a is not concave-Lipschitz; (c) the non-standard
internal normalization of Φ.13.

---

## C. Verified virgin space

Criterion: an item only counts as virgin if (i) a grep in `ROUTES-TRIED-INDEX/` gives 0 hits, or the closest entry does not
cover it for the stated reason, and (ii) it does not fall into 𝒦_Φ via a §B.3 piece.

| # | item | grep (index) | closest entry / why | in 𝒦_Φ? | verdict |
|---|---|---|---|---|---|
| 1 | L1 S6 unbounded raising operator on the prime side (L = ·log n, [A_λ,L]) | "raising" 0, "ascenso" 0, "Mourre" 1 (G8B-P124 DEAD) | Mourre in collar is a different operator | **yes**: [𝒲, log n] = ∂_ε 𝒲[n^ε·] = moving σ (Theorem D, R-F2), Φ.9 | NO-GO (branch 2) |
| 2 | L1 S7 parity of Ω | "parity of Ω" 0; "Liouville" 6 (F-02 FALSIFIED, ES-1) | the entry is statistical, not a window form | **yes**: the λ(n) series is ζ(2s)/ζ(s), whose comb is −Λ + 2Λ(√n)1_□, linear in Λ (O-lin, A1) and in the same class G1 | NO-GO (branch 1) |
| 3 | L5 genuine ultraproducts | "ultraprod" 0, "Łoś" 0 | K3 (Γ-limit) covers the renormalized-by-escape case | yes, except for a non-standard internal normalization (Φ.13) | **narrow gap → Ξ2** |
| 4 | positivity via categorical dimension | "dimension of a Hom" 0, "von Neumann dim" 0, "Murray" 0; "categorif" 2 (AUDIT_193 #55 G4 "graded dimension", 1 line, RD) | #55 is a one-line death about graded dimension of the form, not about the dimension of a module of a group with + and · | no, if the dimension is not built from I1–I10 | **virgin → Ξ1** |
| 5 | (S⁺) Erdős as structure | "S⁺" 6 (front H l.260: separator; CA_I Cor 6) | there only as a separator invariant | **yes**: the exact version in the window is pinning 𝒞_1 (Λ∗1 = log, branch 2) and the approximate one is Lipschitz stability (Φ.1). Global (S⁺) ⟹ cΛ, a transverse curve (Φ.14, branch 1) | NO-GO |
| 6 | L2 S4 Theorem A of 153 uniform in T, even sector | "Theorem A" 4 (G4E OPEN-RESIDUE; G4E-R160_M3_R1 REF-D) | recorded as REF-D for large T | yes: polarization Ξ_a ↔ ζ and its derivative in a are σ-derivatives (R-F2, Φ.9) | indexed residue, not virgin |
| 7 | L3 S5 non-unimodular transfers | "non-unimodular" 0; INV_T_001 T1 (only q = I₂/I₁ matters; admissible ⟺ ∂_σlog\|q\| …) | INV_T classifies by q, including \|q\| ≠ 1 | yes: the gauge identities are certificates (thm:strip-T4, Φ.8/Φ.10) | NO-GO (branch 2) |
| 8 | L4 W⁻ (odd Weil distribution) | "W⁻" 1 (MORI15: "W⁻ over v* OPEN") | PROOF_L_SHARP_H_001: Thm H.4 generic in the falsifier table (PROVED); its sign at the minimizer is (H) | yes: generic identity (branch 1); (H) is a functional of h* (branch 3); restriction 11 | NO-GO as object |
| 9 | dR_Λ over the cross-correlation cone {ǧ∗Ψ̌} | "dR_Λ" 1 (REF-D identity), "cross-correlation" 1 (G1C-R161 X_T) | — | yes: "dR_Λ ∈ 𝒞_T^*" is linear in the comb for each test (Φ.1); an explicit cone 𝒦 ⊇ 𝒞_T is a certificate, ≤ λ_P (branch 2), and by 197 Thm 5 it must be aligned with w_T | NO-GO as object; survives only as a certificate program |
| 10 | κ-band | "κ-band" 4 (OPEN, lower half) | indexed residue | yes: the lower half is an inverse stability estimate (Φ.1) | indexed residue |
| 11 | additive Hankel matrix of the coefficients, [r_a(m+n)] ⪰ 0 (Hamburger moments of r) | "additive Hankel" 0, "r(m+n)" 0, "moment sequence" 0 | — | **yes** via Φ.14: A4 ∧ 𝓗⁺ ⊇ {r(n) = n^{−α}} (ζ(s+α)), transverse curve; with FE ζ-type it is pinning (Hamburger, Lemma 2(c)) | NO-GO (new, by Φ.14) |
| 12 | semiring defect r(m+n) = r(m)r(n) (exponential family x^n) | 0 | — | yes: the zero set {x^n} ∩ A4 = {ζ}; the family {Li_s(x)} is transverse (Φ.14) | NO-GO (new) |
| 13 | chordal decomposition (Agler–Helton–McCullough–Rodman) of the exterior Gram matrix over the m≈kn graph | "chordal" 0, "clique" 0 | CA_L_002 uses elliptope/Grone–Pierce–Watkins, not chordality | yes: (a) chordal PSD ⟺ Cholesky pivots with no fill-in ≥ 0 = Schur (𝒦_NL, branch 2); (b) the part outside the pattern is not null (Σc_N²/N diverges) and its size is ≫ e^{−4πμ} (restr. 1, 25) | NO-GO |
| 14 | optimal transport / Talagrand / W₁ between the comb and the density | "Talagrand" 2 (front J "no disorder") | — | yes: transport distances are weakly continuous in the comb ⇒ C-τ / restr. 1 | NO-GO |
| 15 | ×2,×3 rigidity / solenoid dynamics (Kronecker line) | "×2,×3" 1; "Furstenberg" 0 | front H: Near = Kronecker − Haar (PROVED) | yes if it only uses ℚ^×: G1 (Beurling reproduces the solenoid) | NO-GO unless (ℚ,+) enters → absorbed into Ξ1 |
| 16 | blueprints / semiring varieties (Lorscheid) | "blueprint" 0 in the index; "Lorscheid" 1 in the corpus (L5) | — | no by definition | virgin, without a concrete object: not launched |
| 17 | Monge–Ampère / arithmetic isoperimetry | "Monge" 0 | — | no by definition | virgin, without a concrete object: not launched |
| 18 | convolution powers + CLT (T → 2T descent over F⋆F) | "convolution power" 0; "Gaussian" 11 (P149 additive pencil DEAD; AUDIT_14_B Gaussian packets) | the limit is the Gaussian packet, already dead | yes: positivity on the cone {F⋆F} ⊂ P_{2T} is weaker than WP_{2T} and goes in the opposite direction (Lemma M) | NO-GO |

### C.2 Required form of a survivor

Rows 3, 4, and extended row 15 leave a form of object that does not violate table A **by construction**. The object
must satisfy these conditions:
- **(F1) Input outside I1–I10.** The object is not built from the window form or its families, but from a
  structure containing both (ℚ,+) with origin (to separate a_P and Beurling, R11.2/C.1) and (ℚ^×_{>0},·) (to not
  be purely additive, front M). The window form must appear only at the end, in an identity 𝔞_T = (object) − (error).
- **(F2) C-E′.** The object distinguishes h = 1 from h ≥ 2. The natural way is for its value to depend on Cl(K) discretely,
  e.g. via 𝔖, without averaging over Ĉl: 13.1 forbids convexity under averages.
- **(F3) C-θ.** It cannot be affine or convex in θ. An integer or rational value (dimension, index) is locally constant
  in θ and jumps.
- **(F4) C-τ.** It must be discontinuous in the comb. Dimensions are.
- **(F5) C-pol.** The error in (F1) has to live in P_T: the object is evaluated on tests with A = B = 0 and cannot
  depend on the pole.
- **(F6) C-hom.** It is invariant under r ↦ cr. Dimensions are.
- **(F7) C-data.** The final inequality has to have a free variable (the test g, or a subspace). Relations between
  coefficients alone are not enough.
- **(F8) Φ.1/Φ.14.** It is not a stability result around Λ nor a class of premises with transverse curves. The object is
  not a premise about a: it is a construction made only for Λ whose positivity is structural.
- **(F9) Phase-201 rule.** It declares its Λ channel and the falsifier that kills it if it does not use it.
- **(F10) V2.4.** If the object is Hermitian and encodes Λ∗1 = log as an exact transfer, it has rank one. The candidate
  must explain why its positivity is not that of a rank-one element.

---

## D. Three candidates in verified virgin space

### Ξ1 — von Neumann dimension of ax+b over ℚ, sensitive to the class group

**Definition.** Let G = ℚ ⋊ ℚ^×_{>0} (rational ax+b group; countable, ICC, so L(G) is a type II₁ factor with trace τ; both
facts are CITED: ICC of ax+b over an infinite field). G acts unitarily on L²(ℝ) by (b,a)·f(x) = a^{½}f(ax + b).
For g ∈ P_T set f_g := 𝓜⁻¹ of the test (variable x = e^u, INV_V_001 convention) and
  𝔐_T(g) := closed G-invariant subspace generated by f_g in L²(ℝ) ⊗ ℓ²(G) (left Hilbert module of L(G)),
  d_T(g) := dim_{L(G)} 𝔐_T(g) ∈ [0, ∞].
For an imaginary quadratic field K, the same is defined with G_K = K ⋊ K^×/𝒪_K^×. The module decomposes according to the
class group via the action of ideals on lattices 𝔞 ⊂ K (fibers of Cl(K)).

**Target theorem (OPEN).** There exists a decomposition 𝔞_T(g) = ‖g‖²·τ(P_g · E_T · P_g) − ε_T(g), with P_g the projector
onto 𝔐_T(g), E_T ≥ 0 an explicit element of L(G) not depending on g (built with the Hecke–Chebyshev transfer
V^*Ш = 2log|x|Ш and the multiplier of Γ_ℝ), and ε_T(g) ≤ C μ^{−A} dist²(g, 𝒢̄_T). Then 𝔞_T ≥ −ε_T, which is
L′♯ in the form of prob:ext-L (immediate implication: τ(PEP) ≥ 0 because E ≥ 0).

**Declared Λ channel.** It is the joint action of (ℚ,+) and (ℚ^×,·) on L(G). Λ enters through E_T via the V2.3
transfer (Λ∗1 = log as an operator identity over Ш). Falsifiers that kill it if not used:
- Beurling has no ℚ (there is no G).
- a_P loses the origin: ϑ_P has no constant term (C.1), so Ш_P is not G-invariant.
- Epstein h=2: the module of G_K has h = 2 fibers, and the normalized trace weights the principal fiber by 1/h. That is
  the C-E′ channel, discrete and without averaging over Ĉl.
- cΛ: V^*Ш ≠ 2log|x|Ш, with remainder (c−1)·2log|x|Ш, which is not positive for c < 1.
- DH has no Euler product, and E_T is defined via Euler.

**Filter A.**
- R-K1, R-Q2, R-Π: no coordinates or gauge-kernel projectors are used. The error ε_T is the only place where the
  gauge appears, and it enters as a bound, not as a sign.
- R-Z1: it is not the symbol, it is the group action.
- C-Guo: names what Epstein lacks (h = 1 ⟺ cyclic module, see the first lemma).
- C-θ and C-τ: the dimension jumps.
- C-pol: tests are in P_T.
- C-hom: τ is invariant under scaling of Ш.
- C-data: P_g depends on g, which is a variable.
- 13.1: there is no average over Ĉl.
- **Hard risks**: V2.4 (rank one) and the DEAD Bost–Connes family (index: R9-04, G4H-159 G1, G8H-R160_S5 #20, KMS #12
  of AUDIT_193).

**Index check.** "Murray" 0, "von Neumann dim" 0, "dimension of a Hom" 0, "Mackey" 2: ax+b group on ℓ²(ℕ), G5H-122,
determinant anomaly, which is a different space. Bost–Connes 9: C*(ℚ/ℤ) ⋊ ℕ^× system with KMS states at real β.

**New reason**:
- (i) The dimension of a Hilbert module (Murray–von Neumann) is used, not KMS states nor the partition function.
- (ii) The group is ℚ ⋊ ℚ^× acting on L²(ℝ) over the window tests. Bost–Connes, instead, is the Hecke
  semi-algebra over ℚ/ℤ, and G8H-R160 died because "the core flow is the same for Beurling". Here Beurling has no G.
- (iii) The sensitivity to h comes from K ⋊ K^×, which does not appear in the index.

**Test.**
- Mori μ = 15: g* ∉ core (g*(T) ≠ 0), so the exterior-form g* is used. Necessary prediction: τ(P E P) ≥ 4.98·10⁻⁷⁰
  and ε_T(g*) ≤ ℓ* ≈ 8.6·10⁻⁷⁰. Without that margin the object is empty.
- Lemma E (x²+5y², T = 8/5): the G_K object, with K = ℚ(√−20), must give a negative value at the degree-56 witness G.
  Expected mechanism: the 1/h factor leaves the cosh part of −3.479 uncovered.
- h = 3 (D = −23): the principal fiber weighs 1/3. The LEMMA_12_1 values (Q₁ +3.555, Q₂ +1.763) must be reproduced
  as relative dimensions. It is a calibrator, not evidence.

**First exact lemma (Lemma Ξ1.1, decidable, no numerics).** Compute τ(V^*Ш ⊗ 1) in L(G), i.e. the von
Neumann trace of the Chebyshev element. (a) If V2.4 forces the element encoding Λ∗1 = log to have rank one over Ш,
and Ш is not of finite trace in L(G), then τ(E_T) is 0 or ∞ and the object is **NO-GO PROVED**. (b) If τ is finite and
non-zero, one must prove d_T(g) ∈ (0,∞) for g ∈ P_T. Also, the K version (h=2) must give d = ½·d_principal + ½·d_non-principal.
In that case h = 1 ⟺ the module is cyclic and the C-E′ channel is a dimension.

**Risk.** Very high. The trace of a positive element is the positivity of a Gram factorization (G0: "squares =
Gram factorizations → REF-D or certificate"). The object is saved only if E_T is not built from 𝒲: it must come
from the structure of G (F1). If Lemma Ξ1.1 yields (a), the NO-GO is recorded and row 4 of §C is closed.

### Ξ2 — Loeb form over Ẑ with internal arithmetic normalization

**Definition.** Let 𝒰 be a non-principal ultrafilter on ℕ and ∗μ an unlimited hypernatural. Let ∗N := ∗μ! (hyperfactorial,
divisible by every standard number). At the internal window level ∗μ:
- the internal normalization is ν(x) := Σ_{N≤∗N, N | ∗N} c_N(x)²/N, a sum over the divisors of ∗N, not the escape term;
- the Loeb measure over ℤ/∗Nℤ is L_ν, whose standard part is identified with Haar measure on Ẑ (CITED: Loeb; ℤ/∗N ↠ Ẑ by the
  divisibility of ∗N);
- the functional is 𝔏(x) := st(∗𝒲(x)/ν(x)), defined on the standard quotient.

**Target theorem (OPEN).** There exists a quadratic form 𝔊 on L²(Ẑ, Haar) ⊗ L²(ℝ_{>0}), built with the + and · of Ẑ
(profinite ring), that is ≥ 0 by construction (for example, a Plancherel form of the ring Ẑ) and satisfies 𝔏 = 𝔊 in
the standard quotient. By Łoś (transfer), 𝒲_μ ≥ −o(ν) for 𝒰-almost every μ. If, moreover, the choice of 𝒰 is arbitrary,
the bound holds for every large μ, and L′♯ follows with scale ν instead of ℓ, by comparison ν ≍ ℓ (OPEN).

**Declared Λ channel.** It is the divisibility of ∗N by every standard number: the ring structure of Ẑ, with + and · at the
same time. Falsifiers:
- Beurling has no Ẑ.
- a_P: Ẑ_P = ∏_{p∉P} ℤ_p loses the places in P. The form 𝔊 must fail there, and it does if it uses the self-duality of
  Ẑ × ℝ (adeles), which a_P breaks (C.1(iv)).
- Epstein: (𝒪_K)^∧ with Cl(K) ≠ 1 has a finite class group as an obstruction of Ẑ_K^×/…, which is the C-E′ channel.

**Filter A.**
- Φ.13 is exactly the door here: ν is not the escape term, so it is not K3's Γ-limit.
- R-B.1: there is no transport between standard levels, only Łoś transfer.
- C-τ: divisibility is discontinuous.
- C-pol: ∗P_T.
- **Hard risk**: the adele class space (phase 158 "restatement"; the "Sonin/Connes/semilocal" family is closed). If 𝔊
  is the Weil form over 𝔸/ℚ^×, it is REF-D. The new reason must be that 𝔊 comes from the Plancherel transform of the ring Ẑ, not from the
  idele class group.

**Index check.** "ultraprod" 0, "Łoś" 0, "Loeb" 0 (additional grep: 0). Closest: K3 (Γ-limit, NO-GO), phase 158
(adèle class space, restatement), C5 "semilocal".

**Test.**
- Mori μ = 15 does not apply (it is standard). The test is consistency: ν(g*) ≍ ℓ* with g* extended to ∗μ. This is OPEN and is
  the first thing that can fail.
- Lemma E: the version with 𝒪_K must lose positivity. It must be shown that the Cl(K) obstruction enters 𝔊 and is not
  averaged (13.1).
- h = 3: same obstruction, with order 3.

**First exact lemma (Lemma Ξ2.1).** Prove that ν(x) is comparable to ℓ(x) on the core, with standard constants, or
refute it. If ν/ℓ is unbounded (the sum over divisors of ∗N diverges like Σc_N²/N), the functional degenerates and the
candidate is **NO-GO** (the same death as K3 without renormalization).

**Risk.** High. Most likely ν is equivalent to the escape term and 𝔏 is K3's Γ-limit. If that happens, piece
Φ.13 is upgraded to PROVED and row 3 of §C is closed. It is kept as a third candidate because the negative case closes a gap
in the barrier theorem.

### Ξ3 — Relative class inequality in the Heegner tower, with 𝔖 as a discontinuous weight

**Definition.** Let 𝒟₁ = {D fundamental, h(D) = 1} = {−3,−4,−7,−8,−11,−19,−43,−67,−163}. By Φ.12, for D ∈ 𝒟₁,
  𝔞_T^{Z_D} = 𝔞_T^{ζ} + 𝔞_T^{L(χ_D)}   (Z_D = w·ζ·L(χ_D), Γ_ℂ = Γ_ℝ(s)Γ_ℝ(s+1)).
For D with h(D) ≥ 2 and Q principal, decomposition A.5 holds: 𝔞^{Q} = 𝔞^{ζ_K} + 𝔇^{C=1}. The **tower functional** is defined as
  𝒯_T(g) := inf_{D: h(D)≤H} [ 𝔞_T^{Z_{Q_D}}(g) − 𝔞_T^{L(χ_D)}(g) − 𝔖(D)·𝔇_T^{(D)}(g)/(1+𝔖(D)) ],
where 𝔖(D) = h(D) − 1 enters as a **discontinuous weight** and 𝔇^{(D)} is the class defect of A.5.

**Target theorem (OPEN).** There exists H, with constants uniform in T, such that 𝒯_T(g) ≥ −ε_T(g) on P_T, with ε_T at escape
scale. Since for D ∈ 𝒟₁ the bracket is exactly 𝔞_T^{ζ}(g) (Φ.12, 𝔖 = 0), we have 𝒯_T ≤ 𝔞_T^{ζ}, so 𝒯_T ≥ −ε gives
𝔞^ζ ≥ −ε, which is L′♯. The object is only non-trivial if the proof of 𝒯 ≥ −ε uses the D's with h ≥ 2 at once, for instance via a
compactness argument or a bound uniform over the discrete family of orders in the lattices Z_τ. In that case the
weight 𝔖 makes the family non-affine in θ.

**Declared Λ channel.** It is the discontinuous weight 𝔖(D) combined with the exact identity Φ.12 at 𝔖 = 0. Falsifiers
that kill it if not used:
- Epstein: with weight 0 at h = 2 the bracket is 𝔞^{Q} − 𝔞^{L(χ_D)}, negative at the Lemma E witness, because
  𝔞^Q(G) = −0.062 and 𝔞^{L(χ₋₂₀)} > 0 at that witness (ARGUED: 𝔞^{L(χ₋₂₀)} is obtained from the certified values by subtracting
  𝔞^ζ, which is not certified there).
- C-τ: without 𝔖 the function is continuous in τ.

**Filter A.**
- C-E′ and C-θ: the weight is discontinuous and that is why it is not affine in θ.
- 13.1: it is not an average over Ĉl, because 𝔖 multiplies the whole defect, not an average of L_χ. One must
  verify that the infimum over D does not reintroduce convexity (risk).
- C-data: g is the variable.
- C-pol: P_T.
- **Hard risk**: branch 1 of Φ200 via Φ.12′. If the proof of 𝒯 ≥ −ε only uses D ∈ 𝒟₁, the functional is 𝔞^ζ (branch 2).
  If it uses D with h ≥ 2, the weighted bracket must be ≥ −ε for Epstein: this is a new statement, falsifiable at the
  Lemma E witness.

**Index check.** "Heegner" appears only in Q2_DEGREE2 / SPEC_005 (classifier). "Heegner tower" 0. "discontinuous
weight" 0. Character families: Thm O (R162_1102) averages over χ and is a different object.

**Test.**
- Mori μ = 15: 𝒯 at g* must give ≥ 4.98·10⁻⁷⁰ − ε, and for D ∈ 𝒟₁ it is exact (Φ.12). There is no new information at ζ:
  the test is the coherence of the infimum, which requires the h = 2 bracket ≥ 𝔞^ζ(g*) at g*.
- Lemma E (D = −20, T = 8/5): one must compute the bracket with 𝔖 = 1, i.e. 𝔞^{Q} − 𝔞^{L(χ₋₂₀)} − ½𝔇^{C=1}. With derived
  values: 𝔞^{Q} = −0.062 and 𝔇^{C=1} = −5.111, so −½𝔇 = +2.556, and 𝔞^{L(χ₋₂₀)} is missing at the witness. **If the bracket
  is < 0, weight ½ is insufficient and Ξ3 fails at h = 2**, unless the weight is changed, and an adjusted weight would be an
  ad hoc fix (forbidden by P10).
- h = 3 (D = −23): values from LEMMA_12_1 (Q₁ +3.555, 𝔇 = −0.532), same computation with 𝔖 = 2.

**First exact lemma (Lemma Ξ3.1, arithmetic, no new numerics except one evaluation of L(χ₋₂₀) at the already
certified witness).** Write 𝔞^{Q} − 𝔞^{L(χ_D)} − (𝔖/(1+𝔖))𝔇 in the LEMMA_E symmetric basis for h=2. By A.5:
𝔞^{Q} − 𝔇 = 𝔞^{ζ_K} = 𝔞^ζ + 𝔞^{L(χ_D)}, so the bracket is **exactly** 𝔞^ζ + 𝔇/(1+𝔖). Consequence
(PROVED now): 𝒯_T(g) = 𝔞_T^ζ(g) + inf_D 𝔇^{(D)}(g)/h(D). The lemma then reduces to deciding the sign of
inf_D 𝔇^{(D)}/h(D) on P_T. By 13.1, 𝔇^{(D)} is indefinite in g, so the infimum is ≤ 0 for some g and 𝒯 ≤ 𝔞^ζ.
Consequently **𝒯 ≥ −ε is stronger than L′♯** and its proof has to bound inf_D 𝔇^{(D)}(g)/h(D) ≥ −ε − 𝔞^ζ(g).
*Honest reading:* this reduction, carried out here, shows that Ξ3 is L′♯ plus a lower bound on the class defect, and
13.1 forbids that bound from being uniform when 𝔞^ζ(g) is small. **Ξ3 is NO-GO ARGUED** unless the infimum over D is
achieved only at D ∈ 𝒟₁, in which case it is branch 2. It is kept on the list for showing the complete filter. It stands
as a calibrator for any object with a discontinuous weight: "a weight 𝔖 over the class defect does not contribute sign, because
the defect is indefinite" (exact consequence of A.5 + 13.1).

---

## E. Ranking and recommendation for round 16

| rank | object | status | why |
|---|---|---|---|
| 1 | **Ξ1** von Neumann dimension of ax+b (ℚ and K) | OPEN, first lemma decidable without numerics | the only candidate with an input outside I1–I10, discrete (C-θ, C-τ), sensitive to h without averaging (C-E′), that separates Beurling and a_P by group structure |
| 2 | Ξ3 discontinuous-weight calibrator | already reduced: NO-GO ARGUED (§D, Lemma Ξ3.1) | recorded as restriction **C-𝔖**: a discontinuous weight over the class defect gives no sign |
| 3 | Ξ2 Loeb/Ẑ | OPEN; Lemma Ξ2.1 probably negative | if it falls, it closes Φ.13 (upgraded to PROVED) |
| — | items 1, 2, 5, 7, 11, 12, 13, 14, 18 of §C | NO-GO (via Φ.1, Φ.9, Φ.14, M200′, C-τ, G1, P149) | do not retry |
| — | 16 (blueprints), 17 (Monge–Ampère) | virgin without an object | do not advance construction without a written arithmetic seed |

**Recommendation:**
1. **Step Ξ1**: Lemma Ξ1.1 (trace of the Chebyshev element in L(ℚ⋊ℚ^×_{>0}); ICC and type II₁ as CITED; case (a)/(b)).
   If (b) comes out, the decomposition by fibers of Cl(K) for K = ℚ(√−20) and ℚ(√−23).
2. **Ξ1 audit** with this mandate: (i) show that E_T has rank one (V2.4) or that τ(PEP) is the Gram form of 𝒲
   (G0, REF-D); (ii) compare line by line with Bost–Connes (R9-04, G4H-159, G8H-R160 #20) and with the ax+b case of G5H-122.
3. **Step Ξ2 (short)**: Lemma Ξ2.1 (ν vs ℓ on the core). If negative, write up Φ.13 as PROVED.
4. **Barrier editor**: incorporate Φ.12 (transfer additivity) and Φ.14 (transversality) into META_200 as
   PROVED pieces, and C-𝔖 into table A. Verify Φ.12 against the definition of 𝔞_T in P47 (def:W, eq:nuw, conductor
   term), per the rule of checking against the paper's definitions.
5. (Optional) Literature reader: type of L(ℚ ⋊ ℚ^×_{>0}) and Murray–von Neumann dimensions of lattice
   modules (Connes–Marcolli). Strictly for Lemma Ξ1.1.

Not to be retried: σ-derivatives, Hankel with gap, gauge-kernel projectors, L averages with the same Γ, LP cuts,
quadratics in θ, stability around Λ, transverse curved families, degree change by product with ζ.

---

## F. Entry for the index (to be copied by the coordinator)

- **SPEC_SIGN_OBJECT_006 (round 15, synthesis):**
  - Single constraint table: 25 from phase 200 plus the 28 earlier ones, by block.
  - **Theorem Φ200** (class 𝒦_Φ, inputs I1–I10 plus the operations of 197 and 𝒦_NL). Every lower bound of λ_A in 𝒦_Φ is
    comb-generic, REF-D/certificate, functional of h*, blind to ζ, or equality between data. PROVED piece by piece, ARGUED as a
    class (symbol channel, exhaustiveness, composition).
  - New pieces:
    - **Φ.12 transfer additivity** (PROVED): 𝔞^{ζL′} = 𝔞^ζ + 𝔞^{L′} on P_T, so that the degree change via a
      product with ζ is closed.
    - **Φ.13 Łoś dichotomy** (ARGUED): internal ultraproducts give REF-D; with escape-term normalization they give K3's Γ-limit.
    - **Φ.14 transversality** (PROVED, corollary of 197 Thm 5): a curved family through Λ with ⟨a′,w_T⟩ ≠ 0 contains
      falsifiers.
  - New NO-GOs:
    - additive Hankel matrix [r(m+n)] ⪰ 0 as a premise (contains ζ(s+α));
    - semiring defect r(m+n) = r(m)r(n) (transverse family x^n);
    - chordal decomposition of the exterior Gram matrix (Schur + margin);
    - raising operator (= σ-derivative);
    - parity of Ω (linear in Λ);
    - transport/Talagrand (C-τ);
    - convolution powers/CLT (Gaussian packets).
  - Ξ3 (Heegner tower with weight 𝔖) reduced exactly to 𝔞^ζ + inf_D 𝔇^{(D)}/h(D). NO-GO ARGUED and restriction **C-𝔖**:
    a discontinuous weight over the class defect gives no sign.
  - Alive: Ξ1 (von Neumann dimension of ax+b over ℚ and K; Lemma Ξ1.1 = trace of the Chebyshev element; risks V2.4 and
    Bost–Connes) and Ξ2 (Loeb/Ẑ with normalization by divisors of ∗μ!; Lemma Ξ2.1 = ν vs ℓ).

L′♯: OPEN. Row D: OPEN.
