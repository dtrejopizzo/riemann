# META_200_BARRIER_001 — Meta-audit of phase 200 (rounds 1–6): barrier theorem 𝒦_200 and what remains. This memo closes nothing:
it delivers a tool (barrier theorem) and an inventory of what a proof of L′♯ can still use.

Sources read: README, LEDGER_L1–L5, SPEC_SIGN_OBJECT_001–003, AUDIT_200_SPEC_001–003, K1_OSG_001, K3_GAMMA_001,
Q2_LADDER_001, C1_DUPLICATION_001, B1_FLAT_001, A_MU_FACTORIZATION_001, AUDIT_200_AMU_001, PI_MU_001, AUDIT_200_PIMU_001,
PI4_JUMPS_001, Z_CARRIER_001; ROUTES-TRIED-INDEX/README.md §"Phase 200"; phase-199 AUDIT_CONSTRAINTS_001; phase-197
BARRIER_001_TRICHOTOMY_AND_ADMISSIBLE_CLASS (the file `proof-L-sharp/BARRIER_001.md` does not exist; the trichotomy is in
phase-197-barrier-theorem/).

## Summary (≤250 words)

The six phase 200 constraints (R-K1, R-Q2, R-Q6, R-Π, R-Π4, R-Z1) combine into a barrier theorem for the class 𝒦_200 of
"form inequalities on the leak quotient 𝒬_μ = L²(λ,∞)/𝒢̄_T that read Λ only through (i) Z's symbol at Re s = ½,
(ii) quotient/level/divisor/p-class coordinates, (iii) projectors with kernel 𝒢̄_T, (iv) the gap c_N = 0". Theorem M200:
every proof of L′♯ in 𝒦_200 whose conclusion is uniform is either comb-generic (killed by DH, Beurling, a_P or cΛ) or
REF-D (its statement is 𝒲 ≥ 0 on 𝒬_μ). Label: **PROVED** for pieces (ii), (iii) and (iv), which rest on PROVED
constraints (Lemma R, SQ.0, A.1, Π.0–Π.1, Lemma Z.2′); **ARGUED** for piece (i), because R-Z1 is ARGUED (the DH
transportability of every inequality that uses only the symbol is not proved as a class theorem). What remains outside
𝒦_200 reduces to four virgin or near-virgin ingredients: (β) **quantitative** Guo L4.4 (stability of the gauge ⊂
radical inclusion), the leak scale in the smooth sector (B.1 and K3.1 with constants), the Tate mode as a coupled
term, and the edge channel W* ≈ J²·(ξ′/ξ)(1)/2. Three concrete yes/no questions (§3). New facts from this phase:
c_N = −μ(N), T.1, T.3, Lemma R, A.1, Π.0–Π.3, jumps of f♯ and tail with Tate mode, stacking falsifier, R-Z1. None gives
sign; two change the map: (1) the exact Λ is now localized to two places (Guo's inclusion and the Z intertwiner) and the
factorization architecture A_μ = B∘Π_μ is closed; (2) uniform B.1 is false, so every induction in μ by leak transport
dies.

## 1. The phase 200 barrier theorem

### 1.1 Setting

Fix μ ≥ 5, T = log μ (Paper 47's exterior convention), λ the window parameter. 𝒟 = exterior domain; r ↦ 𝒲[r] the
form (★★) (eq:ext-starstar), ℓ(r) the leak. By A.1 (PROVED given Guo L4.4; AUDIT_200_SPEC_003) the exterior-summation
radical is the gauge 𝒢_T, and 𝒬_μ := L²(λ,∞)/𝒢̄_T with norm ℓ/2. L′♯ (in its exterior form, prob:ext-L) is: 𝒲 ≥ −C μ^{−A}
dist² …; for this memo the qualitative form suffices: "𝒲 descends to 𝒬_μ and is ≥ 0 there at the leak scale".

For a comb a (Λ, a_P, cΛ, Beurling 𝒫, DH) let 𝒲_a be the form built with a instead of Λ (same archimedean m_T, same
λ). Facts that fix the setting:

- **(F1) Common gauge** (PI_MU Π.0′, correction of AUDIT_200_PIMU, PROVED): 𝒢̄_T = Q𝓕(L²₀[−1/λ,1/λ]) is the same set
  for Λ, a_P, cΛ, 𝒫, DH. The relations are two Fourier intervals, with no ℕ.
- **(F2) Exact Λ in two places** (AUDIT_200_PIMU §final, PROVED): (β) the inclusion 𝒢̄_T ⊂ rad 𝒲_a (Guo L4.4 = the
  comb a's explicit formula) and (Z) the intertwiner Z (Poisson over ℤ with a_n ≡ 1). For a ≠ Λ, (β) fails (R-Q6) and Z
  does not exist as an intertwiner with a.
- **(F3) Closed architecture** (AUDIT_200_PIMU, PROVED): A_μ = B∘Π_μ with Π_μ the projector onto 𝒦_T rewrites
  eq:ext-starstar on 𝒦_T; it adds no information.

### 1.2 The class 𝒦_200

**Definition (phase 200 method).** A method 𝔐 = (𝒮, Φ) consists of
(a) a class of combs 𝒮 ∋ Λ, defined by the premises 𝔐 uses;
(b) a conclusion Φ: "𝒲_a[r] ≥ Ψ_a(r) for r ∈ 𝒟", holding for all a ∈ 𝒮, with Ψ_a ≥ 0 in the direction that decides
L′♯; and 𝔐 ∈ 𝒦_200 if every dependence of Φ on the comb goes through one of four channels:

- **(i) symbol**: Z (or Z_log = −ζ′, or Z′/Z) used only via its Mellin symbol at Re s = ½ — multiplier, FE, AFE
  (smooth, Riemann–Siegel, with a dependent cutoff), moments, commutators [𝒫, θ′], [𝒫, iZ′/Z];
- **(ii) coordinates**: mollifier levels Y, classes p | N, S-coprime parts, divisor bands, quotients N′/N,
  blocks 𝔅_k = Σ c_N c_{kN}, zero-coordinates z_ρ, bridge ι between windows;
- **(iii) projectors**: any Π with ker Π ⊇ 𝒢̄_T, followed by an arbitrary B that uses no comb beyond (i)–(ii);
- **(iv) gap**: the vanishing c_N = 0 for 2 ≤ N < μ (and c_N = −μ(N) on [μ,2μ)), used in Hankel/product forms.

The operations admitted on these inputs are those of phase 197's trichotomy (O-lin, O-conv, O-id, O-sq, O-est). The
conclusion is *uniform* if Ψ_a does not depend on a ∈ 𝒮 ("premises ⇒ 𝒲 ≥ Ψ" deduction).

### 1.3 Channel lemmas

**Lemma M.ii (coordinates = radical).** Every type-(ii) coordinate is either constant on the fibers of 𝒟 → 𝒬_μ or
comb-generic. *Proof.* Lemma R (Q2_LADDER, PROVED given Guo L4.4): (ζP)(∂)g ∈ rad for A(g)=0 and P finite; hence
levels, p-classes, S-coprime parts and bands are translates within the radical (R-Q2). SQ.0 (SPEC_002, PROVED):
complete Ramanujan combs are radicals. Π.2 (PROVED): rough/mollified/sieve represent the same point of 𝒬_μ. Bridge ι:
identity on zero-coordinates, preserves 𝒲 (A.5 PROVED). Blocks 𝔅_k: Lemma Z.2′ (PROVED trivially from the formula
c_N = Σ_{m|N, m<μ} μ(m)) says c_N depends on N only via {m<μ : m|N}, a multiplicative structure that the Beurling
system reproduces with μ_𝒫 ⇒ comb-generic. ∎ **PROVED** (modulo Guo L4.4, CITED).

**Lemma M.iii (projectors are archimedean).** If ker Π ⊇ 𝒢̄_T, then Π factors through the orthogonal projector Π_μ
onto 𝒦_T, which is independent of the comb (F1). Any B∘Π that uses no other channel is, by (F3), either a rewriting of
eq:ext-starstar (REF-D) or an archimedean form identical for every comb (comb-generic). ∎ **PROVED** (R-Π + AUDIT_PIMU).

**Lemma M.iv (gap = products).** Every Hankel form using c_N = 0 on [2,μ) has NN′-product structure
(exact K1.1′: the reflected contribution is Σ_P (c∗c)(P)P^{−½}G(log(μn/P)) ≠ 0, a comb-generic Möbius correlation);
𝒲's sign (Toeplitz in Ψ̌, thm:ext-half) lives in quotients N′/N, which fall under (ii). ∎ **PROVED** (R-K1).

**Lemma M.i (symbol = DH-transportable).** An inequality that uses Z only via its symbol on the line holds equally for
the Davenport–Heilbronn function (same FE, same Γ factor, no Euler product). **ARGUED** (R-Z1): the argument is
structural (the FE and the smooth AFE carry over to DH; IK 5.3), but "every inequality" is not proved as a class
theorem: a transfer lemma is missing, one saying that an inequality valid for Z on the line and not using Euler
remains valid for DH on the same 𝒬_μ. Technical obstacle: 𝒲_DH descends to 𝒬_μ only if DH satisfies inclusion (β),
which fails (R-Q6); hence "holds equally for DH" must be read on 𝒟, not on 𝒬_μ.

**Lemma M.Π4 (minimal leak outside the domain).** The minimal-leak representative f♯ has jumps at ±1/λ and a tail with
Tate mode −½f♯(0)e^{−y/2}; σ(g)² and f♯(0)² are not bounded by ℓ (plateaus, PI4 PROVED). Hence no method in 𝒦_200
can choose f♯ as a canonical representative and apply the prime-side formula: (2.3) is CONDITIONAL. ∎ **PROVED**
(R-Π4) for the negative part.

### 1.4 Theorem M200

**Theorem M200 (phase 200 barrier).** Let 𝔐 = (𝒮, Φ) ∈ 𝒦_200 with a conclusion uniform or linear in the sense of
𝓛_lin (phase 197). Then exactly one of the following holds:
1. **comb-generic**: 𝒮 contains a falsifier f ∈ {a_P, cΛ (c≠1), 𝒫 Beurling, DH} with 𝒲_f < 0 at some r with ℓ(r)
   at leak scale; 𝔐 does not decide;
2. **dual certificate**: Φ ∈ 𝓛_lin, and then its value is bounded by λ_P (thm:D1) — it gives nothing beyond Paper 47;
3. **REF-D**: Φ's statement restricted to Λ is "𝒲 ≥ 0 on 𝒬_μ (at leak scale)", i.e. L′♯ itself.

*Proof.* By the channel lemmas, each channel is either (a) constant on quotient fibers and common to every comb
(M.ii, M.iii), or (b) comb-generic (M.ii blocks, M.iv), or (c) DH-transportable (M.i). If Φ uses only (a), the
information Φ carries on 𝒬_μ is the same for every comb except for the descent, and the descent uses inclusion (β)
(R-Q6): either 𝔐 includes (β) as an exact premise — then 𝒮 restricted to the window is {Λ} by pinning (Möbius on the
window, phase 197 Lemma 2(c)) and a uniform conclusion is REF-D (3) — or it does not include it, and then a_P, cΛ, 𝒫
are in 𝒮 and the conclusion, being uniform, is ≤ inf_𝒮 < 0 (1). If it uses (b) or (c), 𝒮 contains the corresponding
falsifier (1). If Φ ∈ 𝓛_lin, phase 197 Theorem 3(ii) gives (2). ∎

**Label.** **PROVED** for the subclass 𝒦_200^{ii,iii,iv} (without channel (i)), given Guo L4.4 (CITED) and the
certified falsification of a_P, cΛ at fixed scale (CERT_FALSIFIERS, phase 197; for c → 1 CONDITIONAL on κ_T ≠ 0,
O_4^ε). **ARGUED** for the complete 𝒦_200, by M.i/R-Z1. What would make the complete version PROVED: a **DH transfer
lemma** — "if an inequality 𝒲 ≥ Ψ on 𝒟 is deduced using from ζ only the FE, the Γ factor and symbol estimates at
Re s = ½, then its version with L_DH is deducible by the same steps" — which is a statement about proof calculus, not
analysis; it is the exact form of what is missing and it is OPEN.

**What the theorem does NOT say.** (a) It does not exclude non-uniform, nonlinear conclusions (door D2 of phase 197:
Łojasiewicz stability along the defect); (b) it does not exclude premises that use (β) **quantitatively** without
using it as an exact identity (refined door D1, §2); (c) it does not exclude information that the form has **outside**
the quotient (the Tate mode and f♯(0), which R-Π4 removes from the domain but not from the form). This is exactly §2.

**Relation to phase 197.** M200 is phase 197's trichotomy *restricted to the exterior carrier* with phase 200's
atoms: (ii)⊂A1, (iii)⊂A1, (iv)⊂A1 (gap = Möbius identity valid for every comb with μ_a), (i)⊂A9-without-A4. The
novelty is channel (β): phase 197 treated "exact explicit formula on flat-top tests" as atom P (pinning); M200 shows
that on the exterior carrier the explicit formula enters only as an inclusion of subspaces, that (β)-exact is pinning,
and that (β)-quantitative is none of 𝒜's atoms.

## 2. What remains OUTSIDE 𝒦_200: inventory

For each ingredient: what it says, which constraint touches it, status from an index grep (keys "Guo L4.4" 6 hits,
"Tate mode" 2, "smooth sector" 1, "admissibility" 1, "FE-defect"/"Łojasiewicz" 0, "residue 1" 3, "conductor 1" 6,
"𝒦₁" 3, "J²" 4).

| # | ingredient | what touches it | status |
|---|---|---|---|
| E1 | **(β) quantitative Guo L4.4**: not "𝒢̄_T ⊂ rad 𝒲" but "dist(𝒢̄_T, rad 𝒲_a) controls 𝒲_a from below", or the dimension of the admissibility-condition space defining rad | R-Q6 only kills the exact-as-premise version (pinning). Z_CARRIER: "the only living place". Index: 6 hits, all as an identity, none quantitative | **VIRGIN** |
| E2 | **conductor 1 / Γ_ℝ** as a global datum | phase 197 Lemma 2: with A4 and ζ-type FE ⇒ pinning; R-Z1: without Euler ⇒ DH | **DEAD** except combined with E1 (the FE enters the form via the common archimedean m_T, identical for every comb) |
| E3 | **residue 1 / Tate mode**: pole s=1 ↔ e^{−y/2}; term 2AB; −½f♯(0) | constraint 10 (phase 199): 2AB ≡ 0 on basis FF.1/GG; R-Π4: f♯(0)² is not at leak scale; c_J = +0.01158 (CONDITIONAL/NUMERICAL) with sign change at c ≈ 1.12 for cΛ (ARGUED) | **NEARLY VIRGIN** as a coupled term: what was not studied is f♯(0) as a coordinate *on the core* (Π.5 |f♯(0)|² ≤ Cℓ, OPEN) |
| E4 | **gauge ⊂ radical inclusion** as a *subspace* (not as an identity) | A.1, Π.0′, F2 | = E1 (same thing; the quantification is the virgin part) |
| E5 | **smooth sector saturating K3.1** (Mori's f* saturates the leak bound ℓ ≥ d₄‖f‖²/(1+r²); 0.7306 = 0.7306) | K3: comb-generic Γ-limit (Λ only in Q₁ = O(1)); B1_FLAT: uniform B.1 false but the stacking falsifier lives at |t|>1.4, outside the smooth sector | **VIRGIN** in the form "B.1 on the smooth sector" and "uniform bound on Q₁" (OPEN in K3 and B1_FLAT) |
| E6 | **edge channel W* ≈ J²·Σ 1/(ρ(1−ρ))** (1.02 at μ=15) | AUDIT_PIMU: NUMERICAL at a single μ, unused; Z_CARRIER: Tate mode explains J²·0.0231 | **VIRGIN** as a question (never tested at another μ). Note: Σ 1/(ρ(1−ρ)) = (ξ′/ξ)(1)·… is an unconditional identity from the polar side; it should be written that way and not as Σ|ρ|^{−2} |
| E7 | **universal scenario 𝒦₁** (form inequality common to every μ) | R-Z1 (channel (i) dead in 𝒦₁), Z.2′ (blocks dead) | lives only with E1 or E3 inside; on its own **DEAD** |
| E8 | **regularity of Z_log (Kummer, log singularities on ℤ)** | PI4: a_P jumps on p^{−k}ℤ ⇒ separates a_P; integer-valued cΛ and 𝒫 are not separated | **PARTIAL**: separates a_P, not integer Beurling; not virgin (PI4, HH_001, TEST_KINKS) |
| E9 | **non-uniform conclusions (door D2)**: λ_A(T;a) ≥ −C_T Δ_T(a), Δ = FE defect | phase 197 §6; 0 hits for "Łojasiewicz" | **VIRGIN** — but note that on 𝒬_μ the FE is common (E2), so Δ_T must measure the defect of (β), not of the FE: D2 and E1 are the same object on the exterior carrier |
| E10 | **c_N = −μ(N) on [μ,2μ) as a new block in doubling** | C1: sandwich ⇒ REF-D; C3′ diverges within the radical | **DEAD** |
| E11 | **Levinson/Conrey (proportion of distinct zeros) for injectivity of z_ρ** | AUDIT_SPEC_003: required for dim 𝒬_μ = ∞ | CITED tool, not a sign source |

**Conclusion of §2.** Outside 𝒦_200 there really remain three things, which reduce to two: **(E1≡E4≡E9)** the
quantitative version of the gauge ⊂ radical inclusion — the only place where, on the exterior carrier, the exact Λ
enters and where DH/a_P/cΛ/Beurling fail *by a measurable amount*; and **(E3+E5+E6)** the smooth/edge sector, where
Mori's extremal lives (saturates K3.1, W* ≈ edge channel) and where no phase 200 constraint is HARD (B1_FLAT
falsifies outside the smooth sector; R-Π4 removes f♯(0) from the domain, not from the form).

## 3. The three yes/no questions

### P1. Is 𝒲 at the extremal exactly the edge channel?
Verifiable statement: **does R(μ) := W*(μ) / (J(μ)²·S), S = Σ_ρ 1/(ρ(1−ρ)) (polar side, unconditional), tend to 1 with
error ≤ ℓ*(μ)/J² — and does W* − J²S have a definite sign?**
- How: recompute the certified extremal at μ = 10, 12, 15, 20 with the MORI15_EXTREMAL_001 pipeline (vector g*,
  J = g*(T)); S is a constant (≈ 0.0231). At μ = 15 only R = 1.02 is available.
- Existing datum: μ = 15 (W* = 4.66e−70, J = −1.42e−34, ℓ*/J² ∈ [0.0218, 0.0421]).
- If **yes** (R → 1, W* − J²S with fixed sign and |W* − J²S| ≪ ℓ*): the extremal has rank one in the Tate mode; L′♯
  reduces to two separate lemmas: (a) J² S ≳ ℓ (trace bound in the smooth sector: E5) and (b) the remainder is ≥ −o(ℓ).
  (a) is an archimedean + polar lemma, without a comb; (b) is where E1 lives. It splits the problem into a comb-free half.
- If **no** (R oscillates or moves away from 1): the coincidence at μ = 15 is accidental, E6 closes and the Tate mode
  is not the carrier; it is recorded as a NO-GO in the index and attention goes entirely to E1.

### P2. Does the codimension of the admissibility conditions separate Λ from DH?
Verifiable statement: let 𝒜_a(T) = rad 𝒲_a ∩ 𝒟 restricted to a finite block of d Legendre modes (d = 832 at μ=15).
**Is dim(𝒢̄_T ∩ block) − dim(rad 𝒲_a ∩ block) equal to 0 for a = Λ and ≥ 1 for a ∈ {DH, cΛ c≠1, a_P}, with the
principal angle between 𝒢̄_T and rad 𝒲_a bounded below by leak-scale?**
- How: Gram matrix of 𝒲_a on the block (already exists for Λ in GRAM_INERTIA_001 / ROUGH_COMPLEMENT_001); compute the
  numerical kernel and the angle with 𝒢̄_T (Π.0's prolate basis). For DH, just substitute the comb for L_DH's
  coefficients in the truncated explicit formula.
- If **yes** and the angle is ≳ (leak scale)^{½}: there exists a functional Δ_T(a) = sin∠(𝒢̄_T, rad 𝒲_a), the "distance
  from (β)", and L′♯ takes the form of a stability inequality 𝒲_a ≥ −C·Δ_T(a)·‖·‖² (door D2 = E1), with Δ_T(Λ) = 0
  by Guo L4.4. A concrete objective outside 𝒦_200.
- If **no** (the codimension is the same for DH, or the angle is exponentially smaller than the leak): (β)-quantitative
  does not separate at the relevant scale; E1 closes with a PROVED/NUMERICAL NO-GO and M200 ends up covering the
  entire exterior carrier (forcing a departure from the exterior carrier).

### P3. Does B.1 hold on the smooth sector?
Verifiable statement: **for g ∈ core_{T′} with ĝ supported on |t| ≤ 1.4 (sector ψ_{4j}, K3.1's), is ℓ_{T′}(g) ≥ θ₀ ℓ_T(g)
with θ₀ > 0 independent of μ?**
- How: this is a comb-free prolate-concentration problem (B.1.a/B.1.b of C1_DUPLICATION give the structure; B1_FLAT's
  stacking falsifier peaks at |t|>1.4, so it does not apply). Test with Slepian asymptotics (CITED) or an eigenvalue
  test on the restriction to two annuli.
- Datum: K3.1 exact at μ=15; β_μ ≤ C/log μ in general (B1_FLAT).
- If **yes**: on the smooth sector the leak transports via ι without loss; combined with K3.1 and the bridge ι (which
  preserves 𝒲), it gives induction in μ restricted to the sector where the extremal lives; the residual stays in the
  oscillating sector, which is where E1 must act. A comb-free tool, publishable in Paper 47.
- If **no**: induction in μ dies even on the smooth sector (NO-GO PROVED); the base case μ ≤ 15 (Mori) stops being
  propagable by any leak-transport argument and must be recorded in the index.

## 4. Honesty about the process

### 4.1 New PROVED facts of phase 200 (and whether they are truly new)

| fact | status | new relative to 194–199? |
|---|---|---|
| c_N = −μ(N) on [μ,2μ) | PROVED | classical; new only as a record (AUDIT_SPEC_001) |
| T.1: 𝓕Ψ̌ = ĝ·D_μ, D_μ = ζM_μ − 1 | PROVED | corollary of thm:ext-half (AUDIT_SPEC_002) |
| T.3: Σ c_N c_{nN} N^{−s} = ζS_n − c_n; S₁(1) ≥ 0 (Selberg) | PROVED | new as an identity; no useful sign |
| Lemma Q2.1 (M_μ = M°_μ − 2^{−s}M°_{μ/2}) | PROVED | new, elementary |
| Lemma R: (ζP)(∂)g radical | PROVED given Guo | **new and structural** (underlies R-Q2) |
| SQ.0: complete Ramanujan combs are radicals | PROVED | new, elementary |
| A.1: exterior radical = gauge 𝒢_T | PROVED | reorganization of lem:ext-mob + prop:ext-gauge |
| A.5 / ι | PROVED | = lem:monoT exterior (duplicate) |
| Π.0, Π.0′, Π.1–Π.3 | PROVED | **new**: the gauge contains no ℕ; ‖Π_μ r‖² = ℓ/2 in closed prolate form |
| jumps of f♯ at ±1/λ; exact tail with Tate mode | PROVED | **new** (not in HH_001/TEST_KINKS: L² projection, not Möbius) |
| harmonic-stacking falsifier (β_μ ≤ C/log μ) | PROVED | **new**, negative, changes the map |
| Theorem D (semiring derivative) | PROVED | chain rule; duplicates σ-derivatives |
| Lemma Z.2′ | PROVED | trivial by definition |
| R-Z1 | ARGUED | new as a constraint; partially contained in EI/J.3 |

### 4.2 Does the map change?
Yes, at three points, none of them a sign:
1. **Localization of the exact Λ** (F2): on the exterior carrier Λ enters only via the inclusion 𝒢̄_T ⊂ rad 𝒲 and via
   the intertwiner Z. Before phase 200, the phase 199 list (constraint 5) spoke of "a_n ≡ 1, residue 1, Γ_ℝ, aliasing
   together" (SOFT, ARGUED). Now it is a PROVED localization of where the sign can lie, and M200 turns it into a barrier.
2. **Closure of the factorization architecture** (F3): A_μ = B∘Π_μ is eq:ext-starstar; "inventing A_μ" stops being a
   goal. SPEC_003's operational definition of the sign object becomes empty in its literal form; what survives is E1.
3. **Death of uniform leak transport** (B1_FLAT): β_μ ≤ C/log μ PROVED; no chain of doublings with polynomial loss
   closes. This was not in 194–199 and is a clean NO-GO.

What did **not** change: L′♯ OPEN; row D OPEN; Mori's extremal remains the only quantitative datum, and phase 200
only added two observations about it (saturation of K3.1, edge channel), both NUMERICAL at μ = 15.

### 4.3 Critique of the process
- Six rounds, ~20 candidates; most die by rewriting (tautology P10 or an index duplicate). The cost of discovering
  that a candidate was REF-D was high because P10 was only formulated in round 2 and localization (F2) only in round
  5. Rule for phase 201: **every candidate declares up front which channel of Λ it uses (β-quantitative, Z beyond
  the symbol, or outside the quotient) and the falsifier that kills it if it does not use it**; if the channel is
  (i)–(iv), M200 discards it without construction.
- The numerics of the extremal (P1, P2) are now *strictly necessary*: the three questions of §3 are cheap relative to
  a construction round and decide whether E1/E6 deserve a phase.

## 5. Entry for the index (proposal; the meta-auditor does not edit the index)

- **META_200_BARRIER_001:** Theorem M200: methods on 𝒬_μ that read Λ only via Z's symbol, quotient/level/divisor
  coordinates, projectors with kernel 𝒢̄_T, or the gap c_N=0, with a uniform or 𝓛_lin conclusion, are comb-generic,
  dual certificate, or REF-D. PROVED without channel (i); ARGUED with channel (i) (missing a DH transfer lemma).
  Outside 𝒦_200: (β) quantitative Guo L4.4 (= phase 197's door D2 on the exterior carrier), smooth sector/Tate
  mode/edge channel. Questions P1 (edge channel at several μ), P2 (gauge–radical angle for DH), P3 (B.1 on the
  smooth sector).

Final labels: M200 PROVED (subclass) / ARGUED (complete class). L′♯ OPEN. Row D OPEN.

---

## Addendum round 15: Φ200, Φ.12, Φ.14, C-𝔖 (editor, round 16)

Source: SPEC_SIGN_OBJECT_006 §B–§D. Checks made against P47 (l.112 v_n = 2Λ(n)/√n; l.121 P_T = {A = B = 0};
lem:K/eq:m; thm:A eq:Aform; def:W/eq:nuw; lem:shape-epstein).

### A1. Theorem Φ200 (statement)
For 𝔒 ∈ 𝒦_Φ (inputs I1–I10, operations from 197's trichotomy plus 𝒦_NL's nonlinear ones, finite composition) with
output Ψ holding on S ∋ Λ and Ψ(T;Λ) ≥ 0, at least one of these branches occurs: (1) comb-generic; (2) REF-D (𝔞_T ≥ 0
on P_T, 𝒲 ≥ 0 on 𝒬_μ, or dual certificate ≤ λ_P, thm:D1); (3) functional of h*; (4) blind to ζ; (5) equality between
data (C-data). Labels by piece: Φ.1, Φ.5, Φ.6, Φ.7, Φ.8, Φ.10 PROVED; Φ.2, Φ.4 PROVED given Guo L4.4 (CITED); Φ.3
(channel I3) ARGUED; Φ.9 PROVED except for τ (CONDITIONAL); Φ.11 PROVED piecewise, ARGUED as a list; Φ.12 PROVED
(below); Φ.13 ARGUED; Φ.14 PROVED with explicit hypothesis (below). Branch-composition rule: ARGUED.
**Φ200: ARGUED as a class, PROVED piecewise.** L′♯ OPEN. Row D OPEN.

### A2. Φ.12 transfer additivity — verified, PROVED
Statement: for L = L₁L₂ (in particular ζ·L′ with L′ entire) and F ∈ P_T, 𝔞_T^{L₁L₂}(F) = 𝔞_T^{L₁}(F) + 𝔞_T^{L₂}(F).
Verification against P47:
1. *Archimedean.* eq:m: m(τ) = Re ψ(¼ + iτ/2) − log π = 2Re(Γ_ℝ′/Γ_ℝ)(½+iτ), i.e. m is the real part of the
   logarithmic derivative of the Γ factor with a ×2 normalization. For Γ_L = ∏Γ_ℝ(s+μ_j) the logarithmic derivative is
   the sum, so m^L = Σ_j m_{μ_j}. By thm:A, C₀ and the kernel K are linear in m (C₀ = m(0), K the Lévy measure of
   m − C₀), so they add. Explicit check: Γ_ℝ(s) gives K₀ = ½/sinh(u/2) + ½/cosh(u/2) (lem:K) and Γ_ℝ(s+1) gives
   K₁ = 2Σe^{−(2k+3/2)u} = ½/sinh(u/2) − ½/cosh(u/2); K₀ + K₁ = 1/sinh(u/2), which is lem:shape-epstein's kernel.
2. *Conductor.* With the same ×2 normalization, q^{s/2} contributes log q to m, additive under conductor products.
   Check: C₀ + log 20 + ψ(¾) − log π = (−4.2274535 − 1.1447299) + 2.9957323 + (−1.0858609 − 1.1447299) = −4.6070419 =
   lem:shape-epstein's C₀^Q. ✓ (ζ_{ℚ(√−5)} = ζ·L(χ₋₂₀) has the same Γ and conductor as Ξ_Q.)
3. *Comb.* −(L₁L₂)′/(L₁L₂) = −L₁′/L₁ − L₂′/L₂ ⇒ Λ_{L₁L₂} = Λ_{L₁} + Λ_{L₂}; with v_n = 2Λ_L(n)/√n (the same factor 2
   as in m, l.112) the weights add. The sign of Λ_{L′} (e.g. χ_D(n)Λ(n)) is irrelevant: the identity is linear.
4. *Pole.* The polar term depends on (A,B) and on the pole's order (Lemma O1), not on the residue; on P_T, A = B = 0
   and it is null. L′ entire ⇒ total order = that of ζ. P_T is the same for every factor (moment conditions e^{±t/2},
   only T).
5. *Multiplicative constants* (e.g. the ½ or w of the completion) do not touch the logarithmic derivative.
Subtlety recorded: P47 defines the window form of a general L only descriptively (in lem:shape-epstein); Φ.12 uses
that definition, now made explicit in rem:shape-additive. No other normalization or sign subtleties.
**Correct consequence (one direction):** for D ∈ 𝒟₁ (h(D) = 1), 𝔞^ζ ≥ 0 ∧ 𝔞^{L(χ_D)} ≥ 0 on P_T ⟹ 𝔞^{ζ_K} ≥ 0. The
converse does NOT follow (𝔞^{L(χ_D)} has no controlled sign). Corollary Φ.12′ (no degree change by product with ζ
gives information about the sign of 𝔞^ζ): ARGUED, as in SPEC_006.
**Integration:** P47 rem:shape-additive (after lem:shape-epstein), backup main_pre_phi12.tex, pdflatex 0 errors, 187 pp.

### A3. Φ.13 Łoś dichotomy — ARGUED (Łoś CITED)
(a) ∗𝒲 ≥ 0 ⟺ 𝒲_μ ≥ 0 for 𝒰-almost every μ (branch 2). (b) Normalization by the leak ⇒ K3's Γ-limit (branch 1).
Comb-independent normalization ⇒ divergent or archimedean limit (branch 1). An internal non-standard ν is left
uncovered (gap Ξ2). It rises to PROVED if Lemma Ξ2.1 turns out negative.

### A4. Φ.14 transversality — verified against 197 Thm 5 / lem:degen
The derivation is correct and, in fact, exact: for a real minimizer F⋆, a ↦ 𝔞^{(a)}(F⋆) is affine, so
λ_A(T;a) ≤ 𝔞^{(a)}(F⋆) = λ_A(T;Λ) − ⟨a−Λ, w_T⟩ for every a (lem:degen, without Taylor). If a(x) = Λ + (x−1)a′(1) +
o(x−1), then λ_A(T;a(x)) < 0 when (x−1)⟨a′(1),w_T⟩ > λ_A(T;Λ) + |⟨o(x−1),w_T⟩|. For linear families (cΛ) there is no
remainder and it holds globally. Corrections to SPEC_006's wording:
- the hypothesis ⟨a′(1),w_T⟩ ≠ 0 implies w_T ≠ 0 (AUDIT_197's degenerate case (e) is excluded by hypothesis);
- for nonlinear families the conclusion requires the scale λ_A(T;Λ)/|⟨a′,w_T⟩| to fall within the region where the
  remainder is smaller than the linear term; since λ_A(T;Λ) ≤ 4·10⁹ T e^{−15.449T} (PROVED, CITED inputs) this holds
  for large T;
- H_T depends on the choice of F⋆ (uniqueness is unknown): the statement holds for each real minimizer.
- the **examples** (cΛ, Λn^{−α}, x^n) are CONDITIONAL: ⟨a′(1),w_T⟩ ≠ 0 in each one requires sign information about
  Σ_n a′(n)c_{F⋆}(log n)/√n, the same condition AUDIT_197 (e) flagged for cΛ (type O_4^ε/O_5).
Label: **Φ.14 PROVED** as a statement with hypothesis ⟨a′(1),w_T⟩ ≠ 0; its application to rows 5, 11, 12 of
SPEC_006 §C is CONDITIONAL until that transversality is verified for each family.

### A5. Constraint C-𝔖 (new in table A)
**C-𝔖.** A discontinuous weight 𝔖(D) = h(D) − 1 on the class defect contributes no sign. By A.5 + Φ.12, Ξ3's tower
functional is exactly 𝒯_T(g) = 𝔞_T^ζ(g) + inf_D 𝔇^{(D)}(g)/h(D), and by Lemma 13.1 𝔇^{(D)} is indefinite in g, so
𝒯 ≥ −ε is stronger than L′♯, and if the infimum is attained only at D ∈ 𝒟₁ the functional is 𝔞^ζ (branch 2). The
reduction is PROVED (given Φ.12 and A.5) and the NO-GO is ARGUED.

### A6. What remains outside 𝒦_Φ (SPEC_006 §B.3 and §C)
- (a) objects whose inputs are not in I1–I10: forms (F1)–(F10) of SPEC_006 §C.2;
- (b) non-uniform conclusions that are neither stability nor certificate (refined door D2) with a non-concave-Lipschitz
  dependence on a;
- (c) Φ.13's non-standard internal normalization → **Ξ2** (Loeb/Ẑ, OPEN);
- row 4 of §C, positivity by categorical dimension (von Neumann ax+b over ℚ, sensitive to Cl) → **Ξ1** (virgin);
- row 15 extended with (ℚ,+): absorbed into Ξ1;
- rows 16 (Lorscheid blueprints) and 17 (arithmetic Monge–Ampère): virgin, no concrete object, not launched;
- indexed residues, not virgin: row 6 (Theorem A uniform in T) and row 10 (κ-band).
Everything else in §C (rows 1, 2, 5, 7, 8, 9, 11, 12, 13, 14, 18) is NO-GO; Ξ3 is NO-GO ARGUED (C-𝔖).

Final addendum labels: Φ200 ARGUED (class) / PROVED (pieces); Φ.12 PROVED; Φ.12′ ARGUED; Φ.13 ARGUED;
Φ.14 PROVED (with hypothesis), examples CONDITIONAL; C-𝔖 reduction PROVED, NO-GO ARGUED. L′♯ OPEN. Row D OPEN.

## Correction (O1_COMPOSITION_001, phase 204p)
The "branch-composition rule" (Addendum A1, ARGUED) is **REFUTED as a barrier**: lem:transfer only excludes
conjunctions of premises that a single falsifier satisfies; the conjunction E (Euler over ℕ) ∧ F (degree-1 FE,
conductor 1) ∧ I3 has ζ as its only model (Kaczorowski–Perelli, Hamburger), and for it branches 1, 4, 5 do not apply
and branch 2 is the thesis. Φ200 in its class version is withdrawn in favor of **Φ200′ (PROVED piecewise)**: every
proof of D with inputs I1–I10 uses in its sign step at least two channels with no certified falsifier in common, and
F is mandatory. Chaining/composing criterion: Def. O1.2 (PROVED). No conjunction in the corpus composed;
specification (S1)–(S4) OPEN.
Correction (INTEGRATION_O1_001): Φ200′(b) — quartets preserve the FE and break E as a Dirichlet series over ℕ; a_P
preserves E and breaks F. Both channels are mandatory in the sign step, each by a different falsifier.
