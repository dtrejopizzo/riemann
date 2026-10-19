# Ledger L1 — insight about the sign, from RH1–RH9 and phases 0–99 (phase 200, stage 1)

Scope: 01-context/RH1–RH9; 03-research/phase-0 … phase-99; maps ROUTES-TRIED-INDEX/01,02,03, NO-GO-LIST.md,
THE_BACKWARD_MAP.md. Target throughout: λ_A(T) ≥ 0 for the Weil window form (row D).
This is an insight ledger, not a route list (routes: ROUTES-TRIED-INDEX).

## 1. Positive structural facts about the sign

**F1. The local prime symbol is indefinite, with an exact closed form.** For the per-prime block of the window form,
G_p(r) = (2 log p / (p|1−z|²))·(√p cos(r log p) − 1), z = p^{−1/2}e^{ir log p}; G_p ≥ 0 ⟺ cos(r log p) ≥ 1/√p.
PROVED (phase-6-osterwalder-schrader-reflection/M-OS-2-S2-local-REFUTATION.md, Prop. S2.1). Insight: no single place carries the sign; each prime
contributes a positive spike near r log p ∈ 2πℤ and a negative plateau elsewhere. The sign is therefore an
*interference* between the plateaus of different primes and the archimedean symbol — never a sum of local signs.

**F2. Archimedean symbol is Lévy (CND), prime potential is positivity-preserving.** Ω(t) = −log π + Re ψ(¼+it/2)
has Lévy–Khintchine form with dν(ξ) = 2e^{−ξ/2}/(1−e^{−2ξ})dξ ≥ 0; V = Σ_{n≤λ²} Λ(n)T(n) preserves positivity
because Λ(n) ≥ 0. Hence e^{−tA_λ} is positivity-improving and the ground state of A_λ = M_θ − V (+pole rank ≤2) is
simple, even (ι: u↦u⁻¹) and nodeless. PROVED for entire L (phase-60-discriminant/H1_PROOF.md §§2–6); for ζ the even
ground state is simple by rank-one interlacing (PROVED), even-below-odd ordering NUMÉRICO (dps 50).
Insight: Λ ≥ 0 decides the *shape* (simplicity, parity, nodelessness) of the bottom eigenvector, but enters with the
sign that *lowers* the bottom. Ψ ≥ 0 coefficients are a structural ally for the eigenvector, an adversary for the eigenvalue.

**F3. The bottom of the window form is exponentially thin, not isolated.** QW_λ^N is PSD numerically with eigenvalues
decaying geometrically (1e−15 … 3); the bottom gap → 0. NUMÉRICO (H1_PROOF.md §0). Phase-10 Lorentzian envelope:
Hodge gap +0.377 at x = 2d/log T₀ = 0.43, 3e−9 at 0.87, ~0 at 1.74, with null directions appearing (signature
(1,21,0) → (1,12,9)). NUMÉRICO (phase-10-hodge-envelope-degeneration/REPORT-M10.1-to-M10.3). Insight: the sign lives at a scale that shrinks like
a prolate eigenvalue — consistent with the e^{−4πμ} margin law later found in phase 199. Any sign object must be
quantitatively *exponentially* fine in the window length; a coarse (polynomial, TV-robust) inequality cannot carry it.

**F4. Off-line zeros force negativity at second order, with low rank.** For an off-line quartet at displacement δ,
λ_min ≈ c(σ,J,T₀,m)·δ² < 0 with a rank-one/low-rank prefactor; validated to <0.001%. PROVED/NUMÉRICO
(01-context/RH7 README Front A; RH6 task32,68). Insight: the sign is *quadratic* in the defect — the positive set is a
cone tangent to the true datum, and the falsifying direction is low-rank. Any sign object must be second-order
(a Hessian-type quantity), not a first-order discriminant (matches phase 186 "W-lin" and phase 197 D1 tangent = {0}).

**F5. Davenport–Heilbronn is the standing falsifier for FE-only mechanisms.** L_DH: same functional equation, no
Euler product, off-line zero ρ ≈ 0.80852 + 85.6993i (κ ≈ 0.28408 validated). CITED + NUMÉRICO (RH1–RH5; F-01 in
index). Insight: whatever produces the sign must use the Euler product (multiplicative structure), not the FE alone.

**F6. Multiplicativity alone does not carry it; *sign organisation* of coefficients does.** Liouville L(s,λ) is fully
multiplicative yet shows the strongest, N-stable resonance (even/odd-Ω constructive interference); random
multiplicative f has the heaviest tails. NUMÉRICO (RH1 Disc.5; RH2 Disc.3; F-02). Phase-60 discriminant: multiplicativity
not separated from smooth non-multiplicative controls; only a fixed-A *relative* discriminant survived. NUMÉRICO
(phase-60-discriminant). Insight: the relevant datum is not "Euler product yes/no" but how additive and multiplicative
structure of ℕ interact (semiring principle).

**F7. Zero-only Gram matrices are PSD by construction (blind).** Kernel-of-differences φ((γ_m−γ_n)/W) is PSD iff φ is
positive-definite (Bochner); naive Hermitian Weil Gram is always PSD. PROVED (RH5 task9,25,54; RH5 Disc.4;
NO-GO-LIST NG-A8). Insight: the sign object cannot be built from ordinates; it must see the prime side.

**F8. Uniform truncation transfer is not weaker than the target.** sup_X|λ_min(Q_X) − λ_min(Q_∞)| → 0 is as strong as
the full sign statement. PROVED per README (RH7 Front C; NO-GO-LIST MW-6). Positive prime truncation ("positive
part minus small tail") FALSIFIED: finite sections negative while the full form is positive (NO-GO-LIST ES-10);
term-by-term positivity of Λ(n) destroys interprime interference (ES-9). Insight: the sign is *non-monotone in the
prime cutoff* and lives in interprime cross terms.

**F9. Cross-place interaction, not any single place, crosses zero.** ⟨K(L)·,·⟩ = R_∞ + Σ_p R_p, R_p ≈ a_p W(log p)
an explicit Toeplitz block; crossing forced only by R_∞ + ΣR_p jointly. PROVED structure / ARGUED crossing claim
(phase-5-structural/M5-classification-pure-theory.md, T3-anatomy.md). Bessel ≤ 1 bound leaves the wall unmoved.

**F10. Every unconditional positivity used gives lower bounds on the wrong side ("wrong-sign capstone").** Interlacing/
total positivity, real stability, Hodge-type definiteness at finite genus all yield the opposite orientation or
degenerate. ARGUED as a meta-theorem (phase-10-hodge-envelope-degeneration REPORT §0; phase-11-hyperbolicity-total-positivity M11.2, M11.4-5). TP of ξ refuted (phase-60 E1-VEREDICTO,
FALSIFIED). Insight: the sign must be produced by *duality* (an upper bound obtained from a positivity on a bigger
object), as Hodge index produces it on C×C — the backward map (THE_BACKWARD_MAP.md §1) names the engine as
"Riemann–Roch growth + effectivity", i.e. positivity *produced* by a counting function forced to grow quadratically.

**F11. Finite intersection toy has the right signature.** Allermann–Rau tropical square of the scaling site: toy
signature (1,2) correct; intersection numbers integral on ℒ_ℤ but real on flow correspondences (G-125.A). PROVED/
NUMÉRICO (phase-41-build-G2/125-construction-of-the-intersection-form.md). Insight: integrality is lost exactly when one passes
from the integer lattice to the continuous flow — the integer structure is where the sign is "remembered".

**F12. Operator obstruction to sl₂/Lefschetz on the zero spectrum.** Bounded L with [T,L] = cL forces arithmetic
progressions in Spec T, incompatible with ℚ-independence of ordinates. PROVED (RH9 task43). Insight: a raising
operator cannot act on the zero spectrum; any Lefschetz structure must act on the *prime/integer* side, not the zeros.

**F13. Per-place reflection positivity fails; OS at p computed.** G_p(0) > 0, G_p(π/log p) < 0 for p = 2..7. PROVED
(phase-6-osterwalder-schrader-reflection). Cross-place reflection positivity never built (NG-E1).

## 2. Common failure signature

Every route in this slice worked with one of two degraded objects: (a) a *scalar or spectrum* extracted from the form
(λ_min, Li coefficients, GEV shape, Hodge gap, a determinant, zero ordinates), or (b) a *place-wise decomposition*
(R_∞ + ΣR_p, local OS, Hasse–Minkowski, per-prime Toeplitz blocks) — and then asked a monotone, first-order or
place-additive positivity (Bochner, PF, TP, CND, Bessel, real stability, heat-flow monotonicity) to deliver the sign.
Both degradations erase precisely what F1/F8/F9 show carries the sign: the interference between different primes'
negative plateaus and the archimedean Lévy symbol, at an exponentially fine (prolate) scale, organised by how additive
shifts by log n interact with multiplicative composition. Detectors that had power (RH1–RH8) were finite-N
phenomenology with no proof path; tools that had a proof path were sign-blind because they were PSD-by-construction,
place-additive, or produced the wrong orientation (lower bounds). In short: the routes looked at *which* primes are
present and *how big* they are, never at the *signed arithmetic coupling* m ≈ kn between them.

## 3. Seeds (abandoned or undeveloped; what is different now)

**S1. Cross-place reflection positivity (NG-E1).** Dropped in phase 6 after per-place RP was computed indefinite;
the cross-place (tensor-glued, non-factorised) version was explicitly "never built". Now different: phases 194–199
established that all place-additive classes are comb-generic NO-GO (INV_Q Q3, INV_M), so the *only* surviving shape is
non-factorised — exactly the slot NG-E1 left open. Concrete: define a reflection θ on a space indexed by pairs
(p^a, q^b) with the reflection acting on log p^a − log q^b (the m ≈ kn near-coincidences), and test OS-positivity of
the induced kernel at T = ½ log 5 against the certified falsifiers (a_2, 2Λ, 1.15Λ, zero comb). Must explain
why it is not INV_V_002 (affine near-coincidence form): there the pairing was Hermitian-lifted and hit Chebyshev
rigidity; an OS reflection is not a Hermitian lift but a half-space positivity.

**S2. Positivity of the bottom eigenvector (F2) used as a *constraint* rather than a goal.** Phase 60 proved the
ground state is nodeless/even and stopped ("gives simplicity, not sign"). Now different: phase 199 needs a gauge-
minimised leakage coercivity L′♯, whose falsifier is a gauge f supported in (−1/λ,1/λ). A nodeless positive minimiser
cannot be supported in a strict sub-interval with E f = 0 on a sign-changing set; PF positivity of the minimiser is a
natural gauge-fixing. Concrete: restrict L′♯ to the PF cone (f > 0 on the window) and check whether the AUDIT_199
gauge falsifier is excluded; the cone is where the bottom vector lives, so no loss of generality for λ_A.

**S3. Fixed-A relative discriminant (phase-60-discriminant).** Retained after the absolute multiplicativity
discriminant was falsified; never developed. Now different: phase 198 shows λ(c) concave in c and the Λ bottom near-
degenerate. A relative quantity λ_A(Λ) − λ_A(cΛ) at fixed archimedean part is exactly what separates Λ from the
scaled falsifiers 0.85Λ, 1.15Λ, 2Λ; concavity + two certified negative endpoints is a constrained setup worth one round.

**S4. Lorentzian envelope degeneration curve (phase 10 M10.1).** Abandoned because the Hodge gap → 0. Now different:
phase 199 predicts that degeneration at rate e^{−4πμ}μ^{9/2}. The phase-10-hodge-envelope-degeneration data (x = 0.43, 0.87, 1.74) can be read as
the same law; the envelope with one ample archimedean direction is a concrete *finite-signature* object whose null
directions could be identified with the Mori contacts (μ = 5, 8.37, 10, 12, 15). Concrete: recompute the phase-10-hodge-envelope-degeneration
signature at the certified μ values and check whether null directions appear exactly at contacts (NUMÉRICO, cheap).

**S5. Integer vs flow intersection (G-125.A, phase 41).** Dropped because integrality fails on flow correspondences.
Now different: the semiring principle says the sign comes from (ℕ,+,·) at m ≈ kn; the integer lattice ℒ_ℤ, where
intersection numbers *are* integral and the toy signature is right, is the natural carrier. Concrete: restrict the
tropical square to integer correspondences {(m,n): m = kn ± j} and compute signature at T ≤ 1.

**S6. Unbounded raising operator (RH9 task75, OPEN).** F12 kills bounded L on zeros; the unbounded case was never
decided, and F12 suggests putting L on the prime side. Concrete: L = multiplication by log n on ℓ²(ℕ, Λ-weighted),
check [A_λ, L] against cL modulo the archimedean commutator.

**S7. Sign-organisation of ω/Ω-classes (RH1–RH4).** Constructive even/odd-Ω interference for Liouville; DH resonance
composite-driven. Dismissed as numerical-only. Now different: phase 198 split D into even/odd sectors with D_even
binding; the Ω-parity of n is a natural arithmetic analogue of the parity sector. Low priority (numerical lineage).

## 4. If the sign object had to be invented from this slice alone

It would be a *non-factorised, second-order interference quantity between distinct primes, positive on a half-space
(reflection-type) rather than on a full Hermitian space*: every local symbol G_p is a positive spike plus a negative
plateau (F1), the sign appears only at second order in the defect and in low rank (F4), it is destroyed by
place-splitting, truncation, or term-wise positivity (F8, F9), and it is invisible from zeros alone (F7). The one
structural positivity this slice actually *proved* — the Perron–Frobenius nodeless even ground state driven by Λ ≥ 0
and the Lévy archimedean symbol (F2) — says the extremal vector lives in a positive cone. So the single most
distinctive hint is: **the sign object pairs the Λ-driven positivity of the extremal *vector* (PF cone) with an
OS-type reflection across the near-coincidences log m ≈ log(kn), so that the negative plateaus of different primes are
reflected onto each other's positive spikes; its positivity is half-space (reflection) positivity of a cross-place
kernel, at prolate (exponentially fine) resolution.**
