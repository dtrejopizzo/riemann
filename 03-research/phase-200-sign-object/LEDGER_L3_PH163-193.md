# LEDGER L3 — insight on the sign, phases 163–193 (phase 200, stage 1)

Analyst L3. Sources: ROUTES-TRIED-INDEX (04_PHASES_100-189 Part I-c; README §§190–193, audit and re-examinations),
AUDIT_PHASE193_CERTAINTY, phase-189 README/NT_SYNTHESIS, phase-193 CAMPAIGN_LEDGER and CA_*_SYNTHESIS, Paper 47
(thm:shape §20, thm:X).
NO-GO / NUMERICAL / REF-D (exact reformulation of D: valid target, not closure).

## 1. Positive structural facts about the sign

**F1. Shape theorem (P47 thm:shape, closure).** PROVED except where noted.
- (A) Every deduction class closed under O1–O4(∀c), O6–O8, O13–O15 (within the lemmas' ranges) contains no valid proof.
- (A′) O4^ε, O5 CONDITIONAL (κ_T≠0, c_{F*}(log n₀)≠0); O10 CITED (full form)/ARGUED (primitive background); O11 ARGUED; O12 falsifier OPEN.
- (B) Every valid proof: margin ≤ 4·10⁹·T·e^{−15.449T} for T≥1 (simple exponential; the scale exp(−e^{2T}) is only NUMERICAL/Zhu,
  retracted as a premise); exact at the center, at integer resolution and at the density ceiling; is not a symmetrization of D_σ;
  in multiplier calculus is a measure identity on (−2T,2T) + Bochner; is not an arithmetic sum-of-squares decomposition for
  T ≥ ½log3; **jointly uses the Euler product over ℕ and the conductor-1 FE**.
- (B′) "It is not an estimate": (i)–(ii) PROVED, (iii) CONDITIONAL, general reading ARGUED.
- (B″) No valid identity for every weight vector carries a sign (lem:shape-ident, PROVED).
- (C) Every proof uses, in a load-bearing line, a property of ζ destroyed by each modification in (A). Problem (R), clause (11):
  the sign step must be ζ-specific by construction.
Positive reading: the sign is an **exact fact, joint Euler+FE, of exponential precision, not arithmetic-quadratic**.

**F2. Theorem X (P47 thm:X; R186_045–047).** Identity (i) PROVED; (ii) if λ_A(T)≥0, the new primes between T₀ and T must
**cancel σ_{T₀} on its negative set U_{T₀} at resolution π/T** (averaged; PROVED mod Landau–Widom); (iii) on E_η(U₀)∩P_T
(codim ≤2) the leak is ≤ η; (iv) the pointwise form is false. Converse NO-GO (M₁ satisfies X and is negative). Insight: the sign is a
**compensation mechanism of future primes over the present negative region**, not a property of an isolated window.

**F3. "Functional of h*, not of σ" (phases 183–186, 191).** Every first-order discriminant (flowdet, Hellmann–Feynman, births,
frozen witnesses, W-coh coherence: a 1e-5 perturbation flips λ_A) is a functional of the minimizer h*. PROVED in the instances
(R186_045/050/051). Insight: the sign is not readable in the symbol σ_T; it lives in the pair (σ_T, h*) and only the nonlinearity h*(Λ) sees it
(EI_003: every exact identity on σ_T is affine in Λ — tautology, not NO-GO, but the structural fact holds).

**F4. Cancellation on the line (CA_M, PROVED).** m(τ) + 2Re(ζ′/ζ)(½+iτ) = 0 for every real τ off the ordinates (FE + reality of
ξ). The primes contribute no density surplus: they cancel C₀ exactly; holds for the whole FE class. Corollary: the
**anti-diamagnetism** (CA_K; λ_A(0.7; no comb) < 0 < λ_A(0.7; Λ), with Zhu CITED) — adding primes RAISES the background — is real and
ζ-specific on P_T, but its density part is exactly zero. The sign is not in the density but in the **discrete remainder**.
Parallel: NT_006 (PROVED) — the curve symbol is regular at σ=1 for Λ and has a pole for every finite modification/truncation:
Λ-specific regularity.

**F5. Separability (CA_E_001 Thm 1, PROVED).** D ⟺ positivity on Euler-product vectors; positive = completely
positive. Thm 2: the Bochner measure on the solenoid is concentrated on the Kronecker line ι(ℝ); there is no Schur
factorization. FKG: the equality class is exactly the Euler vectors. Insight: the sign is "classical/commutative," concentrated
on a measure-zero curve of the infinite torus; **Near = Kronecker line minus Haar** (anatomy CA_H, PROVED).

**F6. Anatomy (CA_H, PROVED).** Each term of the form = (weight purely additive in log q) × (coefficient purely of the q-monoid),
linear in Λ. The nonlinearity can only come from the minimizer or from a new input that is neither the minimizer nor a comb property.

**F7. Frustration (CA_J Thm 1.3, PROVED).** No ±1 gauge makes 𝔸_M ferromagnetic: the additive cycle m→m+1→…→2m closed by the
multiplicative edge (m,2m) is frustrated. Holonomy ℤ/2 = sgn 𝖡(log(m/k)), insufficient (counterexample). Insight: + and · meet
on a **cycle with nontrivial holonomy**; GKS/Ginibre/FK have no input; the object carrying the sign must be natively frustrated (not reducible to a ferromagnetic system).

**F8. Site independence (CA_K, CA_M Thm 3.1/Cor 3.2, PROVED).** D ⟺ 𝖡 PSD on any real set of sites with consecutive ratios
→ 1; at prime sites Div ≡ 0 and D is Arch ≥ Near; the truth value is the same at sites p+θ_p with independent irrational θ_p → parity, residues, singular series, sieve **do not exist** in the problem. Bounded-shift configurations
have weight 0.

**F9. Guiding principle, corrected form (CA_M; labels ARGUED as a guide, G1 PROVED via (R)(10)).** Multiplicative alone is not enough
(G1: free ℕ^× is indistinguishable from Beurling/ideals); additive alone is not enough (Epstein x²+5y², ARGUED). The "+" of p − n·p′ is cosmetic;
the only (+,·) content is **the structure of the comb on log ℕ — positions log n with weights v_n — read through the form**,
e.g. Erdős's successor property (S⁺) (CA_H_002: comb on prime powers with sum of divisors continuous at successors
⟺ cΛ; separates ζ from O1–O3,O5,O6,O8,O10–O12,O15, not from O7).

**F10. Other exact pieces with content.**
- Markov (CA_I_001, PROVED): without the polar term the form is Markov; λ₀ < λ_A ≤ λ₂; Thm 3: every FE-symmetric rational torsion with entire ξE
  stops being Markov for T ≥ T_E (ξ(σ)>0 CITED); 𝖯⋆ = {(S⁺), polar residue, entire+FE+Γ_ℝ, Markov ∀T} separates ζ from every
  declared modification (O14 closed afterward) — separation, REF-D as a route. Every F ∈ P_T has ≥2 sign changes (PROVED).
- C3 (phase 190, PROVED): on s=m^{−½} the balance against Arch is carried only by defects N=2,3,4; every atom n≥5 cancels its Div
  (Riemann-sum). λ_min(A_M) ≍ M^{−3} and A_M ⪰ 0 up to M=3000 (NUMERICAL). Correction CA_C_005: the M^{−3} criticality of s_w with η>2/3
  was a normalization artifact.
- Height-flow base (NT_002, PROVED class): D(σ) for σ ≥ 3/2 + O(T₀/log(1/T₀)); the flow is monotone because h(r)=log(ab) is
  conditionally negative definite; D = ∩_{σ>0} D(σ).
- Prop R4.1/R4.2 (CA_R4_001, PROVED): at the first contact ½log5→½log7 the −du half and the polar part contribute exactly 0; what is
  missing is the near-cancellation of four shifted copies Σ_{n=2..5}Λ(n)n^{−½}h*(t∓log n) at precision ~1.6·10⁻⁶ in the dual
  collar norm (OPEN; neither a zero-side statement nor an estimate: exact transcendental evaluation).
- Thm N2 (PROVED, T>½log3): no unimodular transfer of an analytic signal positivizes the form.
- Semilocal Sonin (183/R186_010–015): chain PROVED ∀S finite, no sign; ρ*(T) < 1 ⟺ positivity (REF-D); λ_A>0 ⟺ S_{T,k}≻0 finite (Thm A/B).

## 2. Common failure signature

Every route from 163–193 dies through one of three doors that are the same one: (a) **comb genericity** — the tool holds
for every weight vector or for the whole FE class (Epstein, O7 quartets, Beurling), so (B″)/thm:shape(A) exclude it; (b)
**reformulation** — when the tool really is specific, it is because it passes through the spectrum of the target form (minimizer h*,
determinant, index, Floer, Maslov, polar capacities, Γ-moments), and then it is REF-D; (c) **zero side / estimate** —
transfers that cross the pole at 1 or the strip (1,3/2], or estimates with a remainder operating at the error scale of primes against
an exponential margin. In one line: every property found is **linear in Λ and read on σ** (hence generic) or
**nonlinear but read on h*** (hence circular); no quantity was found that is at once nonlinear in Λ, ζ-specific
and external to the minimizer. The audit sharpens the scope: "0 admissible" only holds for the seeds exactly as formulated;
~1/3 of the discards are REF-D (valid targets) and ~1/4 are one-line or ARGUED.

## 3. Seeds to reopen (with the new reason supplied by 194–199)

S1. **Height flow on the exterior pair form (189 × 199-E).** PROOF_L_SHARP_E_001 Thm E.1 (PROVED) writes 𝒲_ext[Zr] as
a sum over pairs (m,n) regrouped by ratio m/n = α/β — i.e., over ℚ_{>0} with its height. NT_001's height flow
(positivity-preserving, monotone, PROVED) was never applied to that exterior form, only to A_M. New reason: the object of 199 is the
residue of Lemma L′♯ (not the window form), and the den^{−2σ} denominator damping acts on it differently
(the distant pairs are outside the collar). Risk: REF-D if the flow reduces to Near; check against INV_C_001 (off-diagonal h⁰
closed).

S2. **D_∃c (CA_R1_001, OPEN) with the concavity from 198.** BB_001 proved λ(c) concave in c and Π non-decreasing. With concavity,
∀T ∃c>0 with λ_A(T;cΛ) ≥ 0, and nesting in T reduce D_∃c to a common c* and to the slope at c=1. New reason: the tool
(concavity) did not exist when the residue was left open; the O4^ε question (κ_T≠0) remains the only door, and the κ Hessian from CC_001
(≼0) is a direct input.

S3. **SPEC_A with identities only, proved margin + Lemma M (191 × 199).** Reopened by the audit (the earlier death used the retracted
double-exponential scale). PATTERN_001/MECH_001 give: piecewise certificates between contacts (Lemma M, PROVED: λ_A non-increasing
in T), margin ~exp(−4πμ)μ^{9/2} with a **sawtooth at the contacts** (NUMERICAL, new). New reason: the sawtooth is
exactly the step variable L*_j(θ) and is now observable; the gap (θ) — where log ℕ enters ‖ℓ_e‖_{𝔄_j^{−1}} — can
be checked against the four copies of CA_R4_001.

S4. **Regularity at σ=1 as a ζ-specific property (NT_006) + "Target E" (NT_SYNTHESIS).** Never exploited: the curve symbol
is regular on the ℓ² line for Λ and has a pole for every finite modification — a property destroyed by O1–O3 without touching zeros.
New reason: 197 (D1) proved that the tangent of the conductor-1 FE locus at ζ is {0} and gave the exact Bohr defect in
Euler deformations; combining regularity-at-1 with tangent rigidity is a candidate for a property of (C) that is not REF-D.

S5. **Non-unimodular transfers (front N, OPEN).** Thm N2 only closed the unimodular ones. 195-T (INV_T_001) classified unimodular
gauges: contractive NO-GO, expansive = certificate. New reason: the 195 dichotomy leaves the non-unimodular case with variable |q|
as the only remaining gap and parametrizes it by def:PD's (ν,β).

S6. **Gap G-F / MW-5 with the Sonin trace (193-F × 199-D).** PROOF_L_SHARP_D_001 Thm 2.1: W_T = Son ≥ 0 + break term 𝔅
(‖primitive‖², ≥0) − ⟨K_s⟩ − ⟨C_p⟩ + pole. This is the first writing with **two** free positive pieces; the object polarized
over ℤ (CA_F_003) was looking for exactly an ample class with quadratic h⁰. New reason: a concrete candidate for "h⁰"
(Son) and for "ample class" (𝔅) now appears.

S7. **Campaign items never developed:** Salié/Kuznetsov variant of the metaplectic package (CA_A_004, low priority); off-diagonal
form of the metaplectic package (CA_A_003 §4, OPEN); LP of prime sites on the torus for |X|>5 (CA_L_002, exact up to 5 via
elliptope; never attempted beyond that); PF₄ (OPEN); paired vectors built with primes; an inequality using Δ≡0 (CA_B_003
residual); non-graph MW-5 correspondences (CA_H). Priority per the audit: 𝖯⋆ → already REF-D; CA_L_002 and PF₄ remain.

S8. **(S⁺) versus O7.** (S⁺) separates ζ from everything except the O7 quartets (which preserve the comb). Combined with 𝖯⋆ (Markov ∀T, which does
break quartets by Thm 3) the conjunction separates; what was never looked for is an **inequality** (not a separation) using (S⁺) and
Markov rigidity simultaneously. Check against F-M_m and Mori's extremal (μ=15).

## 4. The most distinctive property of the sign object (from this stretch)

If the object were to be invented using only what was learned in 163–193, its defining trait would be: **being a nonlinear functional of the comb
over log ℕ (positions log n, weights v_n) that "sees" the Kronecker line inside the solenoid without going through the minimizer**, and
whose exact value expresses that the atoms entering at each contact compensate the previous negative region (Theorem X) — the
compensation that density cannot provide because on the line density cancels exactly (m + 2Re ζ′/ζ = 0). That is:
a **discrete-remainder** object, natively frustrated (holonomy on the cycle m→2m), valued in a "classical" category
(separable over Euler vectors), whose positivity is structural (Markov/amplitude type, rigid under FE-symmetric torsions)
and not an estimate, and which loses its property under any comb modification that preserves the FE (quartets) or the monoid
(Beurling) — the Euler × conductor-1-FE conjunction that thm:shape(B) demands, materialized as an exact equality, not as
a bound.
