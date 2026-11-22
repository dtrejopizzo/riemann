# SPEC_SIGN_OBJECT_010 — round 20: the arithmetic Hodge index as sign object

Phase 200 ("sign object"), synthesizer for round 20.
---

## Summary (≤300 words)

The round's question is whether the Weil mechanism over 𝔽_q (Hodge index on C×C applied to the Frobenius graph),
transported to ℤ as the arithmetic Hodge index (Faltings–Hriljac) or as arithmetic Riemann–Roch (van der
Geer–Schoof, Bost), produces the object that LEDGER_L5 §4 calls for.

**Inventory (A).** Faltings–Hriljac is CITED, but only for arithmetic surfaces X → Spec O_K. It controls
Néron–Tate heights, which measure the arithmetic of the curve (L(Jac,s) at s=1), not ζ. For ζ there is no PROVED
Hodge index in any substitute: arithmetic site/scaling site, Deninger, 𝔽₁ (Deitmar, Durov, Haran, Kurokawa) nor
Weil-étale. All of them have analogies and, at most, toy signatures (P41-1).

**Phase 135 (B).** The Hodge-index transfer (P47 Thm 12.3) is no longer "conditional on h⁰": it is **unusable**.
The frame-defect theorem P47 Thm 19.25 (PROVED) shows that no h⁰: D^W → ℝ_{≥0} satisfies (a), (b′) and (c), for
any χ, real or integer values. Thm 21.15 proves it also on the curve over 𝔽_q, where the sign is a theorem. The
defect lies in the frame (D^W carries the intersection of C×C and discards its linear systems, Restatement 19.29),
not in the object. So the compatibility of specification v6 with an object "of Hodge type" **is not a new reason**:
Thm 19.25 is uniform in the nature of h⁰ (discontinuous, integer, sensitive to h(D)).

**Candidates (C).**
- H1, "arithmetic window RR" (h⁰_θ of van der Geer–Schoof): NO-GO. Prop 20.1 (PROVED): the difference
  h⁰ − h⁰(dual) is deg, linear and combless (C-pol). The candidate falls literally under D-θ (R157_002 l.219).
- H2, h⁰ of the square over 𝔽₁ with the monoid of pairs: retry of INV_C_001 (README l.390). NO-GO.
- H3, Horn A of P47 §19.9 (defect Δ in (c′)): the only unclosed residue of the frame. OPEN, with high risk of
  REF-D from the sufficiency half of the moment problem (P33-6).

**Recommendation (D).** Do not reopen phase 135. If this line is pursued, the only legitimate statement is Lemma
20.4 (Horn A, primitive gates). The real gap remains OT-5′/MW-5 (W10): linear systems over ℤ.

---

## 0. Index and corpus check (mandatory)

I grepped ROUTES-TRIED-INDEX (README, 02, 03, 04, 05, 05b, 06) with the requested terms. These are the relevant
entries, with their line number.

| term | entry | file:line | recorded status |
|---|---|---|---|
| Arakelov / arithmetic Hodge index | R9-09 Route A: L=∪ĉ₁, form = arithmetic intersection, positivity by arithmetic Hodge index | 02_PROGRAMS:34 | PARTIAL: "absolute surface Spec ℤ×_{F1}Spec ℤ unbuilt" |
| Arakelov RR vs explicit formula | R9-21 | 02_PROGRAMS:46 | only structural analogy, no term-by-term identity |
| Hodge NCG | R9-05 | 02_PROGRAMS:30 | no unconditional Hodge index |
| motivic Spec ℤ | R9-14 | 02_PROGRAMS:39 | ample class only in the smooth projective case |
| scaling site | R9-02 | 02_PROGRAMS:27 | structural NO-GO: real deg over C_p, no integer χ |
| scaling site, square | P41-1: tropical intersection form (Allermann–Rau) | 03_PHASES:162 | PARTIAL: toy signature (1,2), real, not integer |
| Castelnuovo | ES-21 Castelnuovo/Minkowski transplant | 03_PHASES:91 | NO-GO |
| arithmetic Castelnuovo–Severi | P33-6 via moments | 03_PHASES:128 | NO-GO: full equality is the target |
| Weil vs Hodge | P40-3 | 03_PHASES:161 | CIRCULAR |
| Deninger | P42-2; L28; L43 | 03_PHASES:165; 05_LIT:33, 54 | DEAD (Kähler via Hasse, circular) |
| Faltings–Hriljac | L26 | 05_LIT:31 | "Missing infinite-dimensional object" |
| Faltings–Hriljac | G4H-159 (tail wall W#) | 04_PHASES:416 | PROVED tool, no sign |
| Faltings–Hriljac over Spec ℤ | G5H-R160_S5 | 04_PHASES:580 | DEAD (MW group {0}) |
| Faltings–Hriljac | G8H-R160_S1 / phase 15 M10 | 04_PHASES:697 | DEAD: "controls heights not zeros" |
| 18 published frames (arithmetic/scaling site, Borger, Haran, AKL, Arakelov, tropical) | G8H-R158_001 §4 | 04_PHASES:722 | DEAD [OT-1/2/3/5′] |
| Arakelov–Kudla | L80 | 05b:18 | "same shape as the Hodge-index transfer theorem (phase 135, conditional on h⁰) … sign in B(f), not constructed. Do not retry without an explicit B" |
| scaling site / RR | L10 | 05_LIT:15 | "Hodge index analogue missing" |
| 𝔽₁, Haran, Kurokawa | L27 | 05_LIT:32 | low priority |
| σ_K, phase 135, h⁰ | P134–148 | 04_PHASES:208 | NO-GO / DEAD (D.24.7: (b′) fails for h⁰ by bidegree; D.34.5; Ξ_a transports literally) |
| h⁰ / carrier | W10 MW-5/OT-5′ | 04_PHASES:27 | NO-GO: "frame defect holds even over F_q" |
| Deligne / Laumon | W9=T5; T4; P149-pencil | 04_PHASES:23, 24, 197 | NO-GO / DEAD (inherits the rationality wall W8, l.20) |
| phase 145 / function field | W8 (finZ, transport from finite fields) | 04_PHASES:20 | NO-GO |
| Haran, Witt, Künneth | G5H-phase-114 | 04_PHASES:288 | DEAD (~20 no-gos) |
| site, Deninger, CC square | residues | 06_OPEN:127–133 | "h⁰-carrier MW-5/OT-5′ (W10; R142 Thm 19.25)" dead; admissible: "CC square **not via h⁰**", surface 𝔽₁ |
| quadratic h⁰, ample class | gap G-F, phase 193 | README:254 | "missing construction, not impossibility" |
| h⁰ off the multiplicative diagonal | INV_C_001 | README:390 | CLOSED; do not retry even as Farey/coprime/Möbius of h⁰ |
| surface of pairs 𝒮, Hodge/CS | INV_B_001 | README:388 | RETRY of R135_007, ES-21, P33-6, P40-3 |
| Jacobi theta with T_{p²} | G2G-R173_FINAL | 04_PHASES:986 | NO-GO (three families) |
| Kurokawa ζ⊗ζ, E101_083 | SPEC_009 X4 | README:554 | NO-GO |
| van der Geer–Schoof / Bost (D-θ) | — in the index | R157_002 l.138, l.219–222; R160_S5 l.123, l.315; R160_001_BRIEF l.404 (S-11) | **EXCL**: "D-θ falls under [P47 Thm 19.25] verbatim: F5" |

Terms without index entries: "Lichtenbaum", "Durov", "Néron", "van der Geer", "Schoof". The last two appear in the
corpus: phase 114 (`114_a_02_AN_ARITHMETIC_SURFACE_OVER_SPEC_Z_WITH_QUADRATIC_H0.md`, h⁰_θ over
P¹_ℤ with toric metric, "a4-WEAK"; `114_d3_02` Thm 2.1, van der Geer–Schoof RR); phase 136
(`NOTE_OFF_THE_PAGE_CANDIDATES.md` §2, "Candidate D-θ"); phase 157 (R157_002, cited above).

**Check conclusion.** The main candidate proposed by the objective, "arithmetic window Riemann–Roch" with h⁰_θ,
**is already in** the corpus as D-θ and is excluded by P47 Thm 19.25. Any version presented here needs a new
reason written out (§3).

---

## 1. Honest inventory (task A)

### 1.1 Faltings–Hriljac (CITED)

**Statement.** Let X → Spec O_K be a regular arithmetic surface with generic fiber X_K a curve of genus g ≥ 1.
For degree-0 divisors D on X_K, with Arakelov extension D̂ orthogonal to the fibers (vertical and at ∞),
(D̂, D̂)_Ar = −2[K:ℚ]·ĥ_NT([D]) holds (Faltings 1984; Hriljac 1985). Since ĥ_NT ≥ 0, the Arakelov intersection
is negative semidefinite on the complement of ⟨fibers, section⟩. It is negative definite modulo torsion of the
Jacobian. **CITED.**

**What it controls.** The quadratic form is the Néron–Tate height on J(K) ⊗ ℝ. Its positivity is height
positivity, and the L-function that "knows" that form is L(J/K, s) at the central point (BSD regulator), not ζ
nor its zeros. The same is said in G8H 04_PHASES:697 ("controls heights not zeros") and G5H 04_PHASES:580
("MW group {0}" over Spec ℤ with the trivial curve).

**Why it is not the analogue of Weil.** In Weil's result over 𝔽_q, the Hodge index is applied to C×C, a surface
whose **base** is the curve C, and the correspondence is the Frobenius graph. For Faltings–Hriljac the base is
Spec O_K and the fiber is an auxiliary curve. The analogue of C×C would be Spec ℤ × Spec ℤ, with Spec ℤ as a
**fiber** over itself. That does not exist as a scheme: ℤ ⊗_ℤ ℤ = ℤ, and the "square" collapses to the diagonal.
L26 (05_LIT:31) sums it up as "Missing infinite-dimensional object".

### 1.2 Substitutes for the square for ζ

| frame | PROVED Hodge index for ζ? | what exists | label | index |
|---|---|---|---|---|
| Arithmetic site / scaling site (Connes–Consani 2014–2023) | **No.** CC solved RR on the **curve** (scaling site, tropical, real dimensions) and leave the self-intersection of the diagonal in the square open | tropical RR on the scaling site; arithmetic site as a Grothendieck topos over ℕ^× ⋊ … | CITED (RR on the curve); OPEN (square) | L10 05_LIT:15; R9-02 02:27; P41-1 03:162; LEAD_NOTE l.56–57 |
| Adèle class space / BC-KMS (phase 158) | No. Phase 158 closed them as a **restatement** ("adèle class space is a restatement"), not as a surface | Connes trace = explicit formula | CITED (identity); NO-GO as an object | phase 156/158 memory; L05 |
| Deninger (foliated cohomology) | No. The Hodge index is conjectural: it requires a Kähler metric on the leaf, and in the available constructions that metric uses the conclusion | foliated dynamical systems, regularized determinant formula | CITED (program); DEAD (circular) | P42-2 03:165; L28, L43 |
| 𝔽₁: Deitmar, Durov, Haran, Kurokawa | No. Spec ℤ ×_{𝔽₁} Spec ℤ has combinatorial models (monoid ℕ^× × ℕ^×, Haran 𝔽-rings), with no arithmetic intersection theory nor signature | Kurokawa's ζ⊗ζ (comb of pairs ρ_i+ρ_j, no finite-type FE) | CITED (definitions); NO-GO (E101_083) | L27 05_LIT:32; G5H 04:288; README:554 |
| Lichtenbaum (Weil-étale) | No. It gives special-value formulas (order and leading coefficient at s = 0, 1), not a form on the zeros | Weil-étale duality | CITED (special values) | no entry; excluded by C-pol (only pole/residue) |
| Arakelov–Kudla (L80) | No. Faltings–Hriljac negativity applies to special cycles; the sign remains in a boundary term B(f) that nobody has built | unrefereed program | ARGUED (external) | 05b:18 |

**Verdict A.** None of these frames has a PROVED Hodge index that speaks about ζ. The only proved arithmetic
Hodge index (Faltings–Hriljac) lives on surfaces over Spec O_K with dimension-1 fiber, and its L-function is that
of the fiber.

---

## 2. What phases 135, 139–145 and 149 left behind (task B)

### 2.1 What h⁰ is and why phase 135 stayed "conditional"

Phase 135 (R135_007, §5; P47 Part II §§11–16):
- Weil class D^W, canonical class K with Φ_K = ξ (Pólya kernel), affine duality σ_K: E ↦ K − E and extended
  form I_∞;
- **Theorem 12.3** (conditionally PROVED): if there exists h⁰: D^W → ℝ_{≥0} with (a) h⁰ ≥ 0, (b′) h⁰(E) > 0 ⇒ E
  is equivalent modulo 𝓝_∞ to an effective class, and (c) the RR inequality h⁰(E) + h⁰(K−E) ≥ ½I_∞(E,E) −
  ½I_∞(E,K) + χ, then I_∞ ≤ 0 on primitive classes;
- h⁰_ℤ over translations by prime powers of ΠK satisfies (a) and (b′) and fails (c) in finite truncations
  (Thm 13.6). On the full lattice it remained OPEN (item 23). Falsifier Ξ_a (ruled plane of rank 4).

"Conditional on h⁰" meant that the function had yet to be built.

### 2.2 What happened afterward (and why the condition is no longer the situation)

- **Phases 139–143** (04_PHASES:208): D.24.7, clause (b′) fails for h⁰ by bidegree (the "pair-indexed" h⁰ that
  R135_007 §4 recommended); D.34.5, no primitive class has all Frobenius traces ≥ 0; the trace-positive cone
  (Horn B, P47 §20) is decided NO by T1/T2; Ξ_a transports literally.
- **P47 Thm 19.6 (PROVED):** h⁰_RR⁺ satisfies (a) and (c) **unconditionally, for every χ**, with growth ¼m².
  Clauses (a) and (c) come for free. All the weight is on (b′).
- **P47 Thm 19.25 (PROVED given (X19), first zero verified): frame defect.** No h⁰: D^W → ℝ_{≥0} satisfies
  (a), (b′) and (c), for any χ. Mechanism: for E′ ≥ 0, |Re(e^{iθ}Φ_{E′}(ρ₁))| ≤ ½s₁ deg E′ with
  s₁ = 0.99846… < 1; the certified class E = 53.11911·e^{−u²/18} sin(γ₁u) + 400K has R(E) = 10 > 0 and
  |Im Φ_E(ρ₁)| = 199.7248 > 199.6920. **Thm 12.3 keeps its label and loses its use.** Cor 19.25b extends the
  result to C_c^∞ ⊕ ℝK and P_c^∞ ⊕ ℝK.
- **P47 Thm 21.15 (PROVED): the same defect holds on the curve over 𝔽_q**, where the sign is a theorem. The
  diagnosis (Restatement 19.29): the frame D^W carries the **intersection theory** of C×C and discards its
  **linear systems**, i.e., bigness (ii), "D² > 0, D·H > 0 ⇒ nD effective".
- **Phase 145** (function-field model, computed Frobenius diagonal): confirms that on C×C positivity comes from
  H⁰(C×C, 𝒪(D)) plus bigness (Hartshorne V.1.6–1.8), not from the form (R145_001 l.579, 754, 803, 893). W8
  (04:20): transport from finite fields runs into the rationality wall.
- **Phase 149** (additive pencil, Deligne route): dead by T5 (W9, 04:23). The L² moments do not allow extracting
  a fiber, and the route inherits W8 (04:197).

### 2.3 Does phase 200 give a new reason to reopen the transfer?

List of compatibilities of specification v6:

| restriction | does an "arithmetic Hodge-type" h⁰ satisfy it? |
|---|---|
| C-τ (discontinuous in the comb) | yes, if h⁰ is integer-valued or jumps |
| C-E′ (feels Λ_cosh / class group) | partially: over O_K, h⁰_Ar depends on Cl(K) |
| C-pol (lives in P_T) | yes, if the form is the restriction to P_T |
| C-MvN (not just (ℚ,ℚ^×)) | yes: depends on geometry |
| C-data (not a positional datum) | yes |

**Decision (PROVED as a logical consequence of Thm 19.25 and Thm 21.15).** This compatibility **is not a new
reason.** Thm 19.25 is stated for **every** h⁰: D^W → ℝ_{≥0}, with no hypothesis of continuity, integrality or
dependence on Cl(K). None of the five properties changes the hypothesis the theorem uses. Moreover, by
Thm 21.15 the obstruction holds where the sign is true, so it cannot be dodged by choosing a "more arithmetic"
h⁰: one must change **the frame D^W** itself, i.e., equip it with linear systems. That is OT-5′/MW-5
(W10, 04:27; gap G-F, README:254), recorded as "missing construction, not impossibility".

**What would have to be proved exactly.** The transportable statement is Restatement 19.29(ii) in arithmetic
form, not Thm 12.3:

> **(Big♯), OPEN.** One must build a space 𝔇 ⊋ D^W with a global-sections functor Γ(𝔇, ·) of ℤ-modules (or
> Hermitian lattices) and an embedding of D^W into 𝔇 preserving I_∞, such that:
> 1. for every class E with I_∞(E,E) > 0 and deg E > 0, rank Γ(nE) → ∞;
> 2. Γ(E) ≠ 0 ⇒ E is effective in the sense of the zeros (Φ_E ≥ 0 in a region containing ρ₁).
>
> By Thm 19.25, property 2 is impossible if Γ factors through D^W. The object must have **more classes than
> D^W** (sections that are not tests).

This is MW-5. No new piece from phase 200 makes it accessible.

---

## 3. The objective's main candidate: "arithmetic window Riemann–Roch"

### 3.1 CITED data

- **van der Geer–Schoof (2000), Bost:** for a rank-1 Hermitian bundle L̄ over Spec ℤ, of degree
  deg L̄ = −log‖1‖, define h⁰(L̄) = log Σ_{n∈ℤ} e^{−π n²‖1‖²}. Then
  h⁰(L̄) − h⁰(ω̄ ⊗ L̄^∨) = deg L̄ (with ω̄ trivial over ℚ). This is Poisson: θ(1/t) = √t θ(t). **CITED.**
- Over O_K the same holds with Minkowski lattices, and h⁰ sees Cl(K) through the ideals. **CITED.**
- Phase 114 (`114_a_02`): over P¹_ℤ with a toric metric, h⁰_θ(D) = ½D·(D−K) + η(D) with 0 ≤ η exponentially
  small (PROVED in the corpus, "a4-WEAK"). It is a genuine arithmetic surface with quadratic h⁰, but ζ does not
  appear in it.

### 3.2 The proposal and its analysis

Proposal: associate to test g ∈ P_T a bundle L_g over Spec ℤ (or over the "square") with metric ‖·‖_g and write
𝔞_T(g) = h⁰(L_g) − h⁰(L_g^∨), so that positivity is a count.

**Proposition 20.1 (PROVED; elementary).** For every rank-1 Hermitian bundle over Spec ℤ, with any
g-dependent metric, h⁰(L̄_g) − h⁰(ω̄ ⊗ L̄_g^∨) = deg L̄_g = −log‖1‖_g. For rank r, with metrics on ℤ^r:
h⁰ − h⁰(dual) = deg = −log covol. In both cases the difference is a **single affine number in log covol**,
combless.

*Proof.* It is Poisson for the lattice ℤ^r ⊂ (ℝ^r, ‖·‖_g) and its dual: Σ_{v∈ℤ^r} e^{−π‖v‖²} = covol^{−1}
Σ_{w∈ℤ^{r∨}} e^{−π‖w‖^{*2}}. Take log. ∎

**Corollary 20.2 (PROVED given P46).** If 𝔞_T(g) = h⁰(L̄_g) − h⁰(L̄_g^∨) for a family of lattices over
ℤ, then 𝔞_T(g) = −log covol_g. That is a functional of the volume (polar/Tate) term, and in P_T it is null or
constant by C-pol (Theorem O3, SPEC_006 l.74 and l.165). It contradicts Lemma 13.1 and Lemma B.2: the form has
comb parts that are undefined in P_T. **NO-GO.**

*Reading.* In van der Geer–Schoof's RR, arithmetic Serre duality **is** the FE (Poisson for ℤ's theta), and the
Euler characteristic **is** deg. The comb Λ does not appear because Spec ℤ as a curve has no primes "in the
fiber". Λ would only enter through the metric's dependence on the primes, and that becomes C-data or the ∂_σ log
channel of INV_C_001.

**Variant 20.3: h⁰ alone, without a difference.** 𝔞_T(g) = h⁰_θ(Λ_g) for a lattice Λ_g. This would give trivial
positivity (θ ≥ 1 ⇒ h⁰ ≥ 0), but:
1. It falls literally under P47 Thm 19.25. Property (b′), "h⁰ > 0 ⇒ effective", is exactly what the theorem
   denies, and h⁰_θ > 0 always (θ > 1), so (b′) would require everything to be effective. R157_002 l.219–222
   already recorded this: "Integrality is never used, so D-θ falls under it verbatim".
2. By C-hom (Lemma H), 𝔞_T is 0-homogeneous in theta's coefficients. An identity 𝔞_T = log θ_Λ fixes the
   normalization r(1) and contradicts r ↦ 2r. It is inconsistent unless Λ_g depends on g without depending on
   θ_ℤ, and then it is no longer ℤ's theta.
3. 𝔞_T is quadratic in g. log θ_{Λ_g} is not, for any reasonable family of metrics. Only a linearization at
   order ε² would give the form, and then its sign is that of the Hessian of log θ, which is an undefined
   **second cumulant** as a function of the metric (cf. Lemma 13.1: the cumulant form is undefined).

**Verdict §3.** The "arithmetic window RR" is D-θ (phases 136 and 157) and there is no new reason to retry it.
Prop 20.1 also closes the version with a difference, which the corpus did not record explicitly. It is added
to the index.

### 3.3 The square over 𝔽₁ and the monoid of pairs

Suggestion from the objective: ℕ^× ⊗_{𝔽₁} ℕ^× = free monoid on pairs (p,q), i.e., the coincidences m ≈ kn.
This is exactly the object of INV_C_001 (README:390). Its fiber lemma over ℚ_{>0} says that every form of pairs
is an atomic measure on log ℚ. Thm 4 (PROVED): no measure on log ℚ equals 𝔞_T in P_T, and Λ only enters through
∂_σ log of the density (explicit formula). The metric "given by the window" does not change the class of
objects, since it is still a measure on pairs. The index forbids the retry "even as Farey/coprime/Möbius of
h⁰". **NO-GO by index** (no new reason: "h⁰ instead of the form" is exactly INV_C_001's formulation).

---

## 4. Three candidates with the full filter (task C)

Filter notation. Table A of SPEC_006, which includes C-Guo, C-E′, C-θ, C-hom, C-data, C-pol, C-τ and 13.1.
Also C-MvN, C-emb and Φ200 (branches: 1 comb-generic, 2 REF-D/certified, 3 functional of h*, 4 blind to ζ,
5 equality between data).

### H1 — arithmetic window RR (van der Geer–Schoof's h⁰_θ over Spec ℤ / O_K)

- **Definition.** L̄_g with metric ‖·‖_g; candidate 𝔞_T(g) = h⁰(L̄_g) − h⁰(L̄_g^∨), or h⁰(L̄_g) alone.
- **Λ channel.** None in the difference (Prop 20.1). In the h⁰-alone version, only through the metric:
  C-data or ∂_σ log.
- **Filter:**
  - C-pol: fails (Cor 20.2).
  - C-hom: fails (Variant 20.3.2).
  - C-τ: would pass, but there is no need to get there.
  - C-E′: over O_K it sees Cl(K), but as a volume term.
  - Φ200: branch 5 (equality between data: Poisson is the FE) and branch 2.
- **Falsifiers.** For the difference: the a_P witness (P46 prop:shape-eulerdel) and Epstein (Lemma E)
  have the same FE and the same Γ, hence the same deg, and different forms. For h⁰ alone: Thm 19.25 with the
  certified class E.
- **Index check.** D-θ: R157_002 l.138, l.219; S-11: R160_001_BRIEF l.404; W10: 04:27.
- **Test.** None needed: it is closed by proof.
- **First exact lemma.** Prop 20.1 (PROVED).
- **Risk.** None: it is closed.
- **Status.** NO-GO (PROVED in the difference version; by index in the h⁰ version).

### H2 — Arithmetic Hodge index transported from an auxiliary surface (Faltings–Hriljac)

- **Definition.** Fix an arithmetic surface 𝒳 → Spec ℤ (e.g. X₀(N), or a CM curve over O_K) and a map
  g ↦ D̂_g ∈ Pic^0 ⊗ ℝ such that 𝔞_T(g) = −(D̂_g, D̂_g)_Ar/2 + B(g). Faltings–Hriljac gives the first term ≥ 0.
- **Λ channel.** The comb must be in B(g) or in the map g ↦ D̂_g. On a fixed curve, the local Arakelov
  intersection at p gives log p times multiplicities. But the weights are those of the curve's reduction, not
  Λ(n)n^{−½} of ζ. The L-function that appears is that of the curve. SPEC_009 (structural conclusion)
  and Φ.12 show that every auxiliary object with an FE over ℚ enters additively via (comb, Γ, conductor).
- **Filter:**
  - C-MvN: passes.
  - C-emb: the map g ↦ D̂_g is an embedding channel; if linear, Φ.1.
  - C-pol: the vertical/∞ part is a volume term, null in P_T.
  - C-E′: Cl(K) does appear.
  - Φ200: branch 2, because the term B(g) that is supposed to give the sign is not constructed and its
    positivity is equivalent to the form.
- **Falsifiers.** a_P and Epstein: the same auxiliary surface works for both (the curve does not see ζ), so
  the Néron–Tate term is the same and the whole difference is in B.
- **Index check.**
  - L80: 05b:18, "do not retry without an explicit B".
  - G8H: 04:697 ("controls heights not zeros").
  - G5H: 04:580.
  - R9-09: 02:34.
  - SPEC_009 X1 (automorphic families): README:554.
- **Test.** Would be Mori μ=15 against an explicit B(g), which does not exist.
- **First exact lemma (if anyone attempts it).** "For the surface 𝒳 and embedding ι, B(g) is a quadratic form
  in P_T that can be written without 𝔞_T". OPEN and ill-posed: nobody has written ι.
- **Risk.** Very high. It is the shape of L80, which the index already blocks.
- **Status.** NO-GO by index. Only reopens with an explicit B.

### H3 — Horn A of P47 §19.9: transfer with defect Δ in (c′), primitive gates

- **Definition (P47 §19.9).** The proof of Thm 12.3 uses (c) only at degree 0 and (b′) only at degrees 0 and 1.
  So (c′) suffices: h⁰(E) + h⁰(K−E) ≥ R(E) − Δ(deg E), with Δ(0) = Δ(1) = 0, symmetric under d ↦ 1−d. The
  maximum defect is Δ(d) = max(0, d²(1−s_*²)/4 − d/4). The "gated" candidate (h⁰ turned off except in classes
  meeting necessary conditions) satisfies (c′) only by assuming the conclusion. What blocks it is the
  **sufficiency half** of the moment problem, plus the technical repair (Cauchy–Schwarz loses the polar term
  η_F(a−b) and only holds for primitive classes; F₀ is not primitive).
- **Why it is the only residue of the Hodge-transfer frame.** Thm 19.25 kills (c) at every degree, but the
  defect lives at high degrees (the witnesses of Thm 19.23 are at d_* ≫ 1), and the transfer only uses degrees
  0 and 1. Horn A is not in the index, either as NO-GO or as closed OPEN. I searched "Horn A" and "(c′)" over
  the whole ROUTES-TRIED-INDEX and there are no entries. It appears in P47 as OPEN.
- **New reason relative to phase 135.** Phase 135 sought h⁰ with full (c). Horn A changes the **hypothesis**
  to (c′) with a defect, which Thm 19.25 does not forbid because its certified class has deg = 400 ≫ 1. Phase
  200 adds the vocabulary P_T and C-pol: gating by primitive classes can be phrased as "a gate in P_T", which
  is exactly where C-pol nullifies the polar terms and repairs the Cauchy–Schwarz step that was losing
  η_F(a−b). This piece is new relative to §19.9: on P_T, A = B = 0 and η_F(a−b) = 0.
- **Λ channel.** Through R(E) = ½I_∞(E,E) − ½I_∞(E,K) + χ: I_∞ contains the full Weil form, comb included. The
  sign would have to come from h⁰ at degree 0 (inequality (c′) at E = nF).
- **Filter:**
  - C-pol: passes by construction (gate in P_T).
  - C-τ: gated h⁰ is discontinuous; passes.
  - C-E′: one must prove (c′) for ζ and that it fails for the Epstein class with Λ_cosh. If the gates are
    generic necessary conditions, they are the same for ζ and for Epstein, and then (c′) is comb-generic
    (branch 1) or holds only under the conclusion (branch 2).
  - C-MvN: passes.
  - C-data: the gates are finite predicates on positions; C1 must be extended to finite predicates
    (AUDIT_SPEC007).
  - Φ200: very likely branch 2.
- **Falsifiers.** Epstein (Lemma E, T = 8/5) and a_P in P_T. If the gate lets them through, (c′) must fail for
  them at degree 0. Ξ_a (phase 135): (c′) must fail for Ξ_a.
- **Index check.** Horn A: no entry. Neighbors: P33-6 (03:128, "full equality = target" in moments), W2
  (04:13, margins) and W10 (04:27).
- **Test.**
  1. On the Mori extremal μ = 15, evaluate R(E) at E = nF with F = g* and check whether a primitive gate
     exists that does not use the conclusion and leaves R(nF) ≤ 2h⁰(nF) + Δ(0) = 2h⁰(nF). Since Δ(0) = 0, this
     is R(nF) ≤ 2h⁰(nF).
  2. Run the same test with Lemma E (T = 8/5) and with a_P (T ∈ [0.60, ½log P]).
  NUMERICAL only as an identity check.
- **First exact lemma.**

  > **Lemma 20.4 (OPEN).** Let 𝒢_prim ⊂ P_T ⊕ ℝK be the gate of primitive classes of degree 0 or 1 with
  > A = B = 0. One must build h⁰: D^W → ℝ_{≥0} satisfying (a), (b′) restricted to 𝒢_prim and (c′) with the
  > maximum Δ of §19.9, **without** assuming 𝔞_T ≥ 0 on 𝒢_prim, and that fails for the Epstein family of
  > Lemma E.

  By Remark 19.25c(i) of P47, on the bare set 𝒢_min the hypothesis of Thm 12.3 is equivalent to the
  conclusion. So Lemma 20.4 must use the **linear extension** P_c^∞ ⊕ ℝK nontrivially, and Cor 19.25b acts on
  that extension through the pair {E_w, K−E_w}. Lemma 20.4 only survives if Δ ≠ 0 absorbs that pair. First
  subquestion decidable by proof: what degree does the pair {E_w, K−E_w} of Cor 19.25b have? If it is 0 or 1
  (where Δ = 0), Horn A dies by Cor 19.25b (NO-GO PROVED). If it is ≥ 2, it survives as a specification.
- **Risk.** Very high: it is the sufficiency half of a moment problem (P33-6).
- **Status.** OPEN as a specification. ARGUED that it falls into branch 2.

---

## 5. Ranking and recommendation (task D)

| rank | candidate | status | reason |
|---|---|---|---|
| 1 | H3 Horn A with a gate in P_T | OPEN (specification); first subquestion decidable by proof | the only unindexed residue of the Hodge-transfer frame; new reason written out (C-pol repairs the CS step of §19.9); very likely REF-D |
| 2 | H2 auxiliary Faltings–Hriljac | NO-GO by index (L80, G8H 697) | PROVED Hodge index, but of the auxiliary curve; the sign is in an unconstructed B |
| 3 | H1 window RR (van der Geer–Schoof) | NO-GO PROVED (Prop 20.1, Cor 20.2) plus index (D-θ) | arithmetic Serre duality = Poisson = FE; difference = deg, combless |
| — | 𝔽₁ square with pairs (§3.3) | NO-GO by index (INV_C_001) | atomic measure on log ℚ |

**Recommendation.**
1. **Do not reopen the phase-135 transfer.** Specification v6 is compatible with a Hodge-type object, but
   Thm 19.25 and Thm 21.15 are uniform in h⁰ and hold where the sign is true. The defect is in the frame D^W,
   not in the object.
2. If a round is devoted to this line, let it be **only the first subquestion of H3**: the degree of the pair
   {E_w, K−E_w} of Cor 19.25b, decided by proof from P47 §19. It is cheap and binary. If the degree is
   ≤ 1, Horn A becomes NO-GO PROVED and the Hodge-transfer line closes entirely.
3. The object LEDGER_L5 §4 calls for, a "square of Spec ℤ" with intrinsic positivity, has a precise shape:
   **(Big♯)** of §2.3, linear systems over a strict extension of D^W with sections that are not tests. It is
   MW-5/OT-5′ (W10) and remains OPEN as a missing construction. No published frame gives it (§1.2).
4. A lesson that stands as a new restriction, **C-RR** (PROVED, Prop 20.1): every object whose duality is
   arithmetic Serre duality over Spec ℤ (Poisson for θ_ℤ) produces, as the difference h⁰ − h⁰(dual), only deg,
   which is a polar term null in P_T. The comb can only enter individual h⁰, and that is where Thm 19.25 acts.

---

## 6. For the index (add in this session)

"SPEC_SIGN_OBJECT_010 (round 20, arithmetic Hodge index / window RR): H1, H2 and 𝔽₁-pairs NO-GO; H3 OPEN.
Inventory: Faltings–Hriljac CITED, but controls Néron–Tate (L of the curve); no substitute for the square
(arithmetic site/scaling site, BC/adeles, Deninger, 𝔽₁/Haran/Kurokawa, Weil-étale) has a PROVED Hodge index for
ζ.
Phase 135: Thm 12.3 is unusable by P47 Thm 19.25 and Thm 21.15 (frame defect uniform in h⁰, valid over 𝔽_q).
Compatibility of specification v6 ≠ new reason.
Prop 20.1 PROVED (C-RR): h⁰_θ(L̄) − h⁰(ω̄⊗L̄^∨) = deg = −log covol for every metric; Cor 20.2: the
difference is polar, null in P_T (C-pol). The window RR is D-θ (R157_002 l.219).
H2 = L80 (B not constructed). 𝔽₁-pairs = INV_C_001.
H3 (P47 §19.9 Horn A, (c′) with defect, primitive gate in P_T): OPEN; first subquestion = degree of the pair
{E_w, K−E_w} of Cor 19.25b (if ≤ 1, NO-GO).
Do not retry theta-type/van der Geer–Schoof h⁰, auxiliary Faltings–Hriljac, nor Hodge-transfer without changing
the frame D^W (Big♯ = MW-5)."
