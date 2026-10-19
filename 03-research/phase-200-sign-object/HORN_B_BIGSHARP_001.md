# HORN_B_BIGSHARP_001 — Round 21: binary decision on Horn B and (Big♯)/MW-5

phase 200. Sources: P46 `main.md` §19.9 (Horn A, Horn B, Thm 19.30,
table B1–B5), Thm 19.25 / Cor 19.25b, Restatement 19.29, §20, §28.4; `HORN_A_001.md` (Theorem HA);
`SPEC_SIGN_OBJECT_010.md` §2.3 (Big♯); phase 158 (README, R158_001/005); ROUTES-TRIED-INDEX index.


## Summary (≤250 words)

**Horn B: NO-GO PROVED (reformulation).** Horn B (P46 §19.9) replaces the cone of non-negative classes in (b′)
with a cone 𝓔′ with the two properties used by the proof of Thm 12.3: (T1_cone) deg > 0 on 𝓔′∖{0} (mod 𝓝_∞) and
(T2_cone) C′_X < ∞ for every X. The method of Theorem HA goes through unchanged: with E_n = 2K + nG and I_∞(G,G) = c > 0,
(c) (or (c′) with any finite Δ) forces h⁰(E_n) > 0, (b′) with 𝓔′ gives E′ ∈ 𝓔′ of degree 2 with I_∞(E′,G) = nc, and
(T2_cone) bounds it by 2C′_G. **Theorem HB (PROVED): Horn B, with any admissible cone and any finite Δ,
implies (W⁰).** What Horn B adds to (W⁰) is only a sufficiency (Eff_𝓔′), of the P33-6 type. Falsifiers
(Epstein, a_P, Ξ_a) fail, but only through (W⁰): tautological.

**(Big♯)/MW-5: the statement of SPEC_010 §2.3 falls into the same theorem.** Its property 2 ("Γ(E) ≠ 0 ⇒ effective"),
restricted to D^W, defines a cone 𝓔′. If 𝓔′ satisfies (T1),(T2), then (Big♯) ⇒ (W⁰) in two lines
(Corollary HB′, PROVED). If it does not satisfy them, the transfer of Thm 12.3 does not get off the ground. That is why (Big♯), as a
*transfer tool*, is a reformulation. The only live content is **existential**: construct 𝔇 and prove,
over 𝔇, independently of the target, a Riemann–Roch inequality with control of h². Inventory of
candidates (Connes–Consani RR on the scaling site and on Spec ℤ̄, Durov, Deitmar/Soulé/𝔽₁, Borger, Haran,
Weil-étale): none has an h⁰ whose "degree" controls the window form. **(Big♯) remains OPEN without an object.** A
minimal S1–S6 SPECIFICATION is left for phase 201.

## 0. Index and corpus check

| term | entry | status |
|---|---|---|
| W10 MW-5/OT-5′ | `04_PHASES_100-189.md:27` | NO-GO (every carrier postulates positivity; the frame defect also holds over 𝔽_q) |
| OT-5′ global object | `04:987` G5H-R173_OT5 | OPEN-RESIDUE |
| Borger/Witt, scaling site, Bost–Connes | `04:418` G4H-159 G1 | DEAD [OT-5′ walls] |
| scaling site as K_geom | `02_PROGRAMS` R9-02 | structural NO-GO (real deg, no integer χ, positivity not independent) |
| square of the scaling site (Allermann–Rau) | P41-1 | PARTIAL (toy of signature (1,2), real, not integral) |
| 𝔽₁, Haran, Kurokawa, Soulé | `05_LITERATURE` L27 | COVERED |
| Connes–Consani RR | `05_LITERATURE` L10 | COVERED, "the Hodge analogue is missing" |
| SPEC_010, HORN_A_001 | `README:555–556` | Horn A NO-GO PROVED; **Horn B OPEN, not treated**; (Big♯) = MW-5 OPEN |
| phase 158 | README | "MW-5 NOT EXCLUDED, unbuilt; its instance in the adèle class space is a restatement"; "the entire content of MW-5 is OT-5′" |

**New reason to touch Horn B.** The class argument `E_n = 2K + nG` from Theorem HA (round
20b) was never applied to it. P46's table B1–B5 only tests candidates against the Thm 19.30 threshold (`C′_{F_0} ≥ G`). It does not ask whether
the hypothesis itself is weaker than the target. **New reason to touch (Big♯).** We do not retry constructing an
object (that is W10). We only decide whether the *statement* (Big♯) is a tool or a reformulation, and fix its
specification against the constraints of phase 200, which phase 158 did not have (C-MvN, C-RR, C-pol, C-τ, Φ200).

## 1. Horn B

### 1.1 Exact statement (P46 §19.9)

Horn B: "enlarge the class of representatives." A cone `𝓔′` of classes of `D^W` is fixed, playing the role of
"non-negative" in (b′):

    (b′)_𝓔′   h⁰(E) > 0  ⇒  ∃ E′ ∈ 𝓔′ ∖ 𝓝_∞  with  E − E′ ∈ 𝓝_∞ ,

with the two properties used by the proof of Thm 12.3:

    (T1_cone)  deg E′ > 0 for all E′ ∈ 𝓔′ ∖ {0} (read mod 𝓝_∞)        [Steps 2 and 4]
    (T2_cone)  C′_X := sup_{E′∈𝓔′} |I_∞(E′,X)| / deg E′ < ∞ for every X     [Step 1]

together with (a) and (c), or (c′) with defect `Δ` (Horn A+B combined). Thm 19.30 (PROVED given (X19)) shows that the
hypothesis is only satisfiable if `C′_{F_0} ≥ G`. The table's only survivor is B4 (non-negative Frobenius
traces), and P46 leaves Horn B OPEN as "a single inequality."

### 1.2 Theorem HB

**Theorem HB (PROVED).** Let `𝓔′` be a cone of classes of `D^W` with (T1_cone) and (T2_cone). Let `Δ` be any
finite defect with `Δ(2) < ∞` (including `Δ ≡ 0`, which is pure Horn B), and let `χ` be arbitrary. If there exists
`h⁰ : D^W → ℝ_{≥0}` with (a), (b′)_𝓔′ and (c′), then

    (W⁰)   I_∞(G,G) ≤ 0  for every real class G ∈ D^W with deg G = 0

holds. The same holds in `P_T ⊕ ℝK` with `G ∈ P_T`.

*Proof.* Suppose `G` is real, `deg G = 0`, and `I_∞(G,G) = c > 0`. Let `E_n := 2K + nG`. Since
`I_∞(K,G) = ½ deg G = 0`, we have `deg E_n = 2` and `R(E_n) = ½(2 + n²c) − ½ + χ → ∞`.

- **Step 1′.** `deg(K − E_n) = −1`. If `h⁰(K − E_n) > 0` held, then by (b′)_𝓔′ there would be an `E′ ∈ 𝓔′ ∖ 𝓝_∞` with
  `deg E′ = deg(K − E_n) = −1`, because deg vanishes on `𝓝_∞`. This contradicts (T1_cone). Hence
  `h⁰(K − E_n) = 0`.
- **Step 2′.** By (c′), `h⁰(E_n) ≥ R(E_n) − Δ(2) > 0` for `n` large.
- **Step 3′.** By (b′)_𝓔′ there exists `E′ ∈ 𝓔′ ∖ 𝓝_∞` with `E_n − E′ ∈ 𝓝_∞`. Then `deg E′ = 2` and
  `I_∞(E′,G) = I_∞(E_n,G) = 2I_∞(K,G) + nc = nc`, because `𝓝_∞` is the radical of `I_∞`.
- **Step 4′.** By (T2_cone), `nc = |I_∞(E′,G)| ≤ C′_G · deg E′ = 2C′_G < ∞`. This is false for `n` large. ∎

The proof uses (T1_cone) in Step 1′ and (T2_cone) in Step 4′, nothing else. These are exactly the two properties
that Horn B **declares** necessary for the Thm 12.3 transfer to work. Any cone that serves the
transfer also serves this argument.

**Corollary HB.1 (PROVED).** If `𝓔′` does not satisfy (T1_cone) or (T2_cone), the proof of Thm 12.3 does not get off the ground: it
is missing Step 1 (ampleness) or Steps 2 and 4. Therefore **every** instance of Horn B that works as a
tool implies (W⁰). Horn B is never weaker than the target.

### 1.3 Is it equivalent or strictly stronger?

With `Δ ≡ 0`, `h⁰ ≡ 0` **does not** work: under (W⁰), `R(dK + G) = (d²−d)/4 + ½I_∞(G,G)`, which is positive for
`d > 1` and small `G`. So pure Horn B is strictly stronger than (W⁰). It additionally requires:

**(Eff_𝓔′) OPEN / REF-D.** There is an `h⁰` with (c) whose classes with `h⁰ > 0` are 𝓔′-effective mod `𝓝_∞`. In
particular, every `E` with `deg E = d > 1` and `R(E) > 0` is 𝓔′-effective mod `𝓝_∞`.

This is half the sufficiency of the moment problem (P33-6), now for the cone 𝓔′ instead of the cone of
densities. Thm 19.30 is the necessary half of that sufficiency: `C′_{F_0} ≥ G`. With `Δ = Δ_♮` (Horn A+B), `h⁰ ≡ 0`
satisfies (a), (b′)_𝓔′ and (c′) under (W⁰), and Horn A+B ⟺ (W⁰), as in Theorem HA(ii).

**Conclusion.** For every admissible cone and every finite defect, Horn B ∈ {(W⁰), (W⁰) ∧ (Eff_𝓔′)}. This is the same
dichotomy as Horn A. **Horn B: NO-GO PROVED as a route (reformulation of the target).**

### 1.4 B4 in particular

B4 (`t_n(E′) ≥ 0 ∀n`) passes Thm 19.30, but that test only looks at `F_0`. For B4 to enter Theorem HB one needs
(T2_cone) for every X, and P46 does not prove it: it states "the available trace inequality gives only t_n(E′) ≥ −ARCH(E′)."
There are two cases.

- **(T2) holds for B4.** Then Theorem HB applies and Horn B with B4 ⇒ (W⁰). Reformulation.
- **(T2) fails for B4.** Then B4 does not serve Thm 12.3 (Step 1), and is not a tool.

In no case does B4 give something weaker than (W⁰). P46's observation that "B4 survives because the trace
bound reproduces the non-sharp constant √(ab) of the gate" is thereby explained: B4 survives the pointwise test on
`F_0` because the test is pointwise. The family `E_n = 2K + nG` is not pointwise: it sweeps the
direction `G` with fixed degree 2.

### 1.5 Falsifiers in the identity

- **Epstein (Lemma E, `T = 8/5`, `Z_Q`).** There is `F ∈ P_T` with `𝔞^Q_T(F) < 0`, i.e. `I^Q_∞(G,G) > 0` for a
  primitive class of degree 0 in the transported frame. The transport is ARGUED: §19.7 uses bilinearity, (11.6) and
  `C_F < ∞`, and the Epstein zeros off the line have `β < 1`. By Theorem HB, Horn B is **false** for
  `Z_Q` with every admissible cone and every finite Δ. There is a nuance: (T2_cone) for an 𝓔′ defined "without naming a zero"
  and transported to `Z_Q` is itself ARGUED, because `C′` depends on the cone.
- **`a_P`, `Ξ_a`.** Likewise: Horn B is false, consistently with Thm 12.4.

Horn B is not comb-generic, but it separates ζ from Epstein **only through (W⁰)**. C-E′ holds
tautologically, just as in HORN_A_001 §4.

## 2. (Big♯)/MW-5

### 2.1 Exact statement (SPEC_010 §2.3; P46 Restatement 19.29; phase 158)

**(Big♯).** Construct `𝔇 ⊋ D^W`, an immersion `ι : D^W ↪ 𝔇` preserving `I_∞` and deg, and a global-sections
functor `Γ(𝔇, ·)` valued in ℤ-modules (or Hermitian lattices), `h⁰ := rank Γ` (or an
arithmetic `h⁰`), such that:

1. if `I_∞(E,E) > 0` and `deg E > 0`, then `rank Γ(nE) → ∞`;
2. if `Γ(E) ≠ 0`, then `E` is effective: it belongs to a cone `𝓔_𝔇` of "zero" classes with `Φ_E ≥ 0` on a
   region containing `ρ₁`.

By Thm 19.25, property 2 is impossible if Γ factors through `D^W` with the cone of non-negative densities. Phase 158 reduced the entire content of MW-5 to OT-5′: "a positive-definite form, defined before the spectrum and without it, whose
compatibility with the flow is proved." Its instance in `A_ℚ/ℚ^×` is a restatement. MW-5 remained NOT EXCLUDED and
unbuilt.

### 2.2 Corollary HB′: the statement (Big♯) as a tool is Horn B

**Corollary HB′ (PROVED).** Let `𝓔′ := ι^{−1}(𝓔_𝔇) ⊂ D^W`, the cone of classes of `D^W` that are effective in
`𝔇`. Suppose `𝓔′` satisfies (T1_cone) and (T2_cone). Then (Big♯) ⇒ (W⁰).

*Proof.* If `I_∞(G,G) = c > 0`, take `E_n = 2K + nG ∈ D^W` with `n` such that `I_∞(E_n,E_n) = 2 + n²c > 0`
(using `I_∞(K,K) = ½ deg K = 1`, the normalization of (19.3)). Since `deg E_n = 2 > 0`, property 1 gives
`Γ(mE_n) ≠ 0` for some `m`. Property 2 gives `mE_n ∈ 𝓔_𝔇`, hence `mE_n ∈ 𝓔′`. Then
`I_∞(mE_n, G) = mnc ≤ C′_G · 2m`, which is false for `n > 2C′_G/c`. ∎

It does not even need (c): property 1 **is** the substitute for RR, and property 2 **is** (b′). The
Corollary shows the following.

- (Big♯) **restricted to `D^W`** is Horn B with the cone `𝓔′ = ι^{−1}(𝓔_𝔇)`, and Thm 19.30 forces
  `C′_{F_0} ≥ G`.
- If used as a transfer hypothesis, (Big♯) is a reformulation: NO-GO PROVED, by the same mechanism as
  Horn A and Horn B.
- If `𝓔′` does not satisfy (T2_cone), then property 2 gives no bound on `I_∞(·,G)` and no sign is
  obtained by this route.

**What the Corollary does NOT close.** It does not say that 𝔇 does not exist. In geometry the scheme is the same: RR plus
vanishing of `h²` give property 1, property 2 is tautological (a section defines an effective divisor), and
the Hodge index **follows**. There nobody assumes (1)–(2). They are proved: (1) by an RR theorem on the object and
(2) by definition. The content of MW-5 is not "(Big♯) ⇒ sign," which is trivial. It is **constructing 𝔇 and proving (1)
within 𝔇 without going through the form**. This matches the phase 158 reading (OT-5′) and sharpens it: the
property that must be *proved* in 𝔇 is an RR inequality with control of `h²` (or of the Serre dual),
`h⁰(nE) ≥ χ(nE) − h⁰(K−nE) − h²_err(nE)`, with `χ(nE) ~ ½n²I_∞(E,E)` and `h²_err = o(n²)`.

### 2.3 Properties 𝔇 MUST have (against Φ200 and the phase 200 constraints)

For an `h⁰` over 𝔇 to avoid falling into any branch of Φ200, the following is needed.

- **S1 (REF-D).** The RR of 𝔇 is proved without using `I_∞` as a form or its kernel. `χ(E)` must be a *computation*
  in 𝔇 (Euler characteristic of a complex), not the definition `χ := R(E)`. If `χ` is defined by the form, property 1
  is (W⁰) plus a sufficiency (Corollary HB′).
- **S2 (C-MvN).** Γ does not depend only on `(ℚ, ℚ^×)` nor on von Neumann/Murray–von Neumann data of the adelic pair.
  The rank must be an **integer** dimension over a ring that sees `(ℕ,+,·)` (semiring principle). A
  continuous Murray–von Neumann dimension is not enough: this is objection R9-02 ("real deg, no integer χ").
- **S3 (C-RR / Prop 20.1).** The Serre duality of 𝔇 cannot be Poisson. Prop 20.1 (PROVED):
  `h⁰ − h⁰(dual) = deg = −log covol` holds for every metric and vanishes on `P_T` (Cor 20.2). An RR of
  van der Geer–Schoof type is linear, not quadratic, and does not contain `½I_∞(E,E)`. The `χ` of 𝔇 must be
  **quadratic** in `E`, which demands a "surface" (the square), not a curve.
- **S4 (P_T / C-pol / C-τ).** 𝔇 contains `ι(P_T ⊕ ℝK)`, and RR is proved there. The pole `η_F` vanishes on
  `P_T`, so growth must come from the prime term and the archimedean one, not from the polar term. With C-τ, the
  object must be compatible with truncation to window `T` (support `[−T,T]`).
- **S5 (discontinuity in the comb).** `h⁰` cannot be continuous in the topology where the comb `Σ Λ(n)δ_{log n}`
  is the limit of smooth measures. If it were, it would transport to Epstein (Lemma E) and to `a_P`, and by Theorem HB
  it would give (W⁰) for `Z_Q`, which is false. The RR of 𝔇 has to fail for Epstein, and it must fail **for a reason
  that can be localized in 𝔇** (not in the sign).
- **S6 (Λ_cosh).** The `χ` of 𝔇 must feel the archimedean kernel `Λ_cosh`, i.e. the Γ/digamma term in
  `I_∞`. A purely non-archimedean RR (of a zeta function at integers) controls `ζ(s)` only at points, not the window
  form.

The six together are the **minimal specification of 𝔇**. They are necessary conditions, not sufficient ones.

### 2.4 Inventory of candidates (corpus and literature)

All literature claims are CITED at the level of a published statement or an index entry. They were not
re-verified.

| candidate | h⁰/RR PROVED? | what "degree" does it control? | fails |
|---|---|---|---|
| Connes–Consani, RR on the scaling site (periodic orbits, ℝ-valued divisors) | CITED: RR with a real-dimension `h⁰` (Connes–Consani 2017–2019) | degree of divisors on the orbit of period `p`; not `I_∞` | S2 (not integer), S3 (curve, linear), no Hodge (L10, R9-02) |
| Connes–Consani, RR for `Spec ℤ̄` over the sphere spectrum 𝕊 (2022–2023) | CITED: RR with an integer-logarithmic `h⁰` for Arakelov divisors | Arakelov degree; duality ≈ Poisson/theta | S3 (Prop 20.1: linear, vanishes on P_T), no square |
| Square of the scaling site (tropical Allermann–Rau, P41-1) | PARTIAL (toy of signature (1,2)) | flow correspondences | S2 (real, not integral), no RR |
| Durov, generalized rings, `Spec ℤ̄` | CITED: the compactification exists | no RR with intersection on the square | S3, S6 |
| Deitmar / Soulé / Connes–Consani 𝔽₁-schemes | CITED: zeta functions of counting functions | `ζ` of toric/counting schemes; values, not form | S6, S1 (no square of `Spec ℤ`) |
| Borger, Λ-rings / Witt | CITED: `Spec ℤ` descended to 𝔽₁ via Λ | no RR; already DEAD (G4H-159) | S1 (zero installation, Lemma T) |
| Haran, 𝔽_un, `ℤ ⊗_{𝔽} ℤ` non-trivial | CITED: the product exists | no RR or index proved | no `h⁰` |
| Weil-étale (Lichtenbaum, Flach–Morin) | CITED: special values at integers (conditional on finiteness) | `ζ(s)` at integer `s` | S6, S4 (no window) |
| Adèle class space / Meyer–CCM `H¹` (phase 158) | RESTATEMENT | spectrum = zeros | S1 (OT-5′) |
| van der Geer–Schoof `h⁰_θ` (H1, SPEC_010) | PROVED (Prop 20.1) | `deg = −log covol` | S3, NO-GO |

No candidate has an `h⁰` whose `χ` is quadratic and contains `½I_∞(E,E)` in the window form. The proved RRs
(Connes–Consani, van der Geer–Schoof) are **curve** RRs (linear in the divisor), and by Prop 20.1 they
vanish on `P_T`. The objects with a "square" (Haran, Allermann–Rau, 𝔽₁) have no proved RR. **No object in
the literature has both S1 and S3.**

### 2.5 Specification for phase 201 (SPECIFICATION, not closure)

> **SPEC-𝔇 (OPEN).** An object `𝔇`, an immersion `ι : P_T ⊕ ℝK ↪ Pic_ℝ(𝔇)` preserving `I_∞` and deg, and a
> cohomology functor `H^i(𝔇, ·)` with `h^i ∈ ℤ_{≥0}` (or lattice dimensions with a controlled
> successive minimum), such that:
> (i) **proved quadratic RR**: `h⁰(E) − h¹(E) + h²(E) = ½I_∞(E, E−K) + χ(𝒪)`, proved as a computation in 𝔇,
> not as a definition (S1, S3);
> (ii) **Serre**: `h²(E) = h⁰(K−E)` in 𝔇 (S3), with a duality that is not the single-variable Poisson
> formula;
> (iii) **tautological effectivity**: a non-zero section defines a class in a cone `𝓔_𝔇` with (T1_cone);
> (iv) **(T2_cone) for `ι^{−1}(𝓔_𝔇)`**, proved without the form;
> (v) integrality over a structure that reads `(ℕ,+,·)` at `m ≈ kn` (S2, semiring principle);
> (vi) **provable failure for Epstein**, with the failure point localized in (i) or (v), not in the sign (S5),
> and sensitivity to `Λ_cosh` (S6).

With (i)–(iv), Corollary HB′ gives (W⁰) in two lines. All the weight is on **proving (i)–(iv) within 𝔇**. That is
why SPEC-𝔇 is the exact form of OT-5′ in phase 200's language. The gate for any candidate of
phase 201 is: where is (i) proved without writing `χ := R`?

## 3. Verdicts

| object | verdict | label |
|---|---|---|
| Horn B (P46 §19.9), any cone with (T1),(T2), any finite Δ | ⇒ (W⁰) (Theorem HB). Horn B ∈ {(W⁰), (W⁰) ∧ (Eff_𝓔′)} | **NO-GO PROVED (reformulation)** |
| B4 (non-negative traces) | reformulation or non-tool, depending on (T2) | NO-GO PROVED (dichotomy) |
| (Eff_𝓔′) | sufficiency of the moment problem for 𝓔′ | OPEN / REF-D (P33-6) |
| (Big♯) as a transfer hypothesis | ⇒ (W⁰) in two lines (Corollary HB′) | **NO-GO PROVED (reformulation)** |
| (Big♯) as an existence problem (SPEC-𝔇 (i)–(vi)) | no candidate object in the corpus or the literature | **OPEN without object** (= OT-5′, W10) |
| Falsifiers Epstein / a_P / Ξ_a | Horn B and (Big♯) are false for them only via (W⁰) | ARGUED (transport), tautological |
| Row D / L′♯ | unchanged | OPEN |

**Remains OPEN by name.** (Eff_𝓔′) (REF-D); **SPEC-𝔇** (= OT-5′/MW-5 reformulated with S1–S6). The Hodge
transfer line (phase 135, Thm 12.3, Horn A, Horn B) remains **closed on all its horns**. The only residue is
existential and is not a transfer hypothesis.

## 4. Entry for ROUTES-TRIED-INDEX

> **HORN_B_BIGSHARP_001 (phase 200, r21): Horn B NO-GO PROVED; (Big♯) as transfer NO-GO PROVED; SPEC-𝔇
> OPEN without object.** Theorem HB: the method E_n = 2K + nG from HORN_A_001 holds for every cone 𝓔′ with (T1_cone)
> (Step 1′) and (T2_cone) (Step 4′) and every finite Δ ⇒ (W⁰). Horn B ∈ {(W⁰), (W⁰) ∧ (Eff_𝓔′)}, and B4 is a reformulation
> or a non-tool. Corollary HB′: (Big♯) restricted to D^W is Horn B with 𝓔′ = ι⁻¹(𝓔_𝔇) ⇒ (W⁰). The live content
> is existential: SPEC-𝔇 (i)–(vi) (proved quadratic RR, non-Poisson Serre, semiring integrality, failure
> localized at Epstein, Λ_cosh). Inventory (CC scaling site and 𝕊-RR, Durov, Deitmar/Soulé, Borger, Haran,
> Weil-étale, vdG–S): none satisfies S1 ∧ S3. Hodge-transfer line closed on all its horns.
