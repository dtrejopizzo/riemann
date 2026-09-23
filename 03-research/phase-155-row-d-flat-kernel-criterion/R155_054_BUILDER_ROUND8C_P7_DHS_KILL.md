# R155_054 — Builder, round 8c: P7, the D-HS kill tests (hygiene)

Author: builder (Fable 5.1). Date: 2026-09-22. Task: `R155_056` row 8c; PATH-TO-D item P7
(`05-meta-and-planning/ABCD-CLOSURE-PLAN/PATH-TO-D-2026-09-22.md:324-333`).
Pure mathematics, no compute, no sign. Every statement labelled.

Paper 46 = `04-papers/46-row-d-the-sign/main.md` (P46). Paper 44 = `04-papers/44-row-b-arithmetic-family/main.md` (P44).
Lead note = `03-research/phase-136-row-d-map/LEAD_NOTE_OFF_THE_PAGE_CANDIDATES.md` (LN).

## 0. Corpus check first (owner rule): D-HS is not "never killed"

`grep -rn "D-HS\|Hilbert–Samuel\|Hilbert-Samuel\|fibrewise\|Frobenius transport" 03-research 04-papers` returns, besides
LN §1 and the phase-136/137/140 blueprints, one **existing refutation**:

* `03-research/phase-140-row-d-frobenius-square/R140_001_BUILDER_ROUND1.md:1115-1135`, §D.24.4
  "D-HS (phase 136, S4) as a variant — built only as far as needed", **Proposition D.24.10** (`PROVED`):
  isometric Frobenius transport = invariance of the bidegree product `ab` (this is `λ_−λ_+(Frob_n) = 1`, P44
  Thm 3ter.6(iii)); a transport-invariant tensor-square `h⁰` factors through `ab`, hence through `M`; so
  Theorems D.24.5(i)/D.24.7 apply: **(b′) fails and (c) is RH**. Recorded in
  `03-research/phase-140-row-d-frobenius-square/README.md:58` ("D.24.10 … refuted, PROVED").
* Transcribed into P46 as §19bis.3–19bis.4: Theorem 19bis.17 (P46:7068, (c) for a bidegree-function ⟹ RH),
  Theorem 19bis.19 (P46:7122, (b′) fails for every bidegree-function), Theorem 19bis.22 (P46:7185, pairing
  against the Pólya realization adds nothing).

**Correction of record (DIAGNOSTIC).** PATH-TO-D P7 (`PATH-TO-D-2026-09-22.md:328`) says D-HS is "the one
arithmetic-geometry candidate in the corpus never killed and never built". "Never killed" is inaccurate: the
*transport-invariant tensor-square* reading of D-HS — transport = `τ_{\log n}` on `D^W`, R140:1118-1119 — was built and
killed in phase 140 (Prop D.24.10), **in the frame's reading only**. Row (vi) (`:189`, "the never-run kill tests T1–T5
… must first clear the frame defect theorem W5") is accurate: D.24.10 ran none of LN's T1–T5 and did not touch the
fibrewise-module reading. Those tests and the check against Theorem 19.25 (which post-dates phase 140) are done below.
The verdict does not change.

## 1. Does Theorem 19.25 already exclude D-HS?  Yes, without construction.

### 1.1 What D-HS is, and what it needs

D-HS (LN §1, `LEAD_NOTE…:19-51`) proposes `h⁰(E) := \dim_S H⁰_X(E)` (or `\log\#`) for classes `E` "radial, i.e.
supported on graphs `Γ_{Frob_n} = {(x,nx)}`, smeared by `h(\log n)`", and states its purpose as feeding Theorem 12.3:
its own tests T3 = clause (b′) (`:44`), T4 = clause (c) on `mK` and `K−nF` (`:45`), T2 = the growth `h⁰(mK) ≳ m²/4`
that (c) forces (LN §0, `:9-10`; P46 Theorem 13.6(i), P46:3505-3512). Clause (a) is the nonnegativity of a dimension.

**Domain (PROVED, split).** The smeared radial classes are the objects of P46 §11: `D^W` (Definition 11.1) is the
Weil completion of the radial sector, on which `τ_a` is the archimedean Frobenius action (Theorem 14.3(ii)) and the
action of `Frob_n` on radial classes is `τ_{\log n}` (P46:3350-3351; the bidegree match is Theorem 11.8(iii),
P46:2247-2250). Theorem 12.3 (P46:2744-2797) uses `h⁰` only at `E = nF` and `E = K−nF` (Steps 2–3), so:
  * *Larger domain irrelevant:* whatever `𝒢 ⊇ D^W` D-HS defines `H⁰_X` on, the transfer reads `h⁰|_{D^W}`, and
    Corollary 1 below applies to that restriction. `PROVED`.
  * *Minimal domain:* `𝒢_{min} := \{nF, K−nF : F ∈ C_c^∞ \text{ primitive}\} ⊂ C_c^∞ ⊕ RK`. An `h⁰` defined only on
    `C_c^∞ ⊕ RK` (which contains `K`) can run Theorem 12.3 but is **not literally** in the range of Theorem 19.25: the
    witness `E = tF_0 + dK`, `F_0(u) = e^{−u²/18}\sin(γ_1u)` (P46:6203), is not compactly supported, and P46 has a
    compactly supported witness only for `Ξ_a` (Theorem 19.15, P46:6134-6136). For this domain the kill is by
    Lemma 3 (§2.3, `w ∈ \{1,t\}`, reading-dependent, no (X19)), or by a **truncation lemma** — `F_R := F_0χ_R`, smooth
    cutoff at `|u| ≤ R`; `C_F` of (11.17) is continuous in the `C²`-weighted norm of `D^W` by (11.2)+(E3d),
    `F_0 − F_R` and two derivatives are `O(e^{−R²/18}\mathrm{poly}(R))`, and the margin `G(1−s_1) = 5.79×10^{−3}`
    (P46:6288) is fixed, so some finite `R` gives `C_{F_R} < \sqrt{W_{F_R}/2}` and Theorem 19.23 runs on
    `F_R ∈ C_c^∞`. Not written here (it re-enters the computer-assisted layer through `s_1`, `L`): **`OPEN`, residual R1**
    (a residual of P46 §19.6, not of D-HS).

**Clauses needed (PROVED).** All three: (a) trivially; (b′) because Theorem 12.3 Steps 2 and 4 use it (P46:2777-2797)
and D-HS lists it as T3; (c) because Step 3 uses it and D-HS lists it as T4 and as the `m²/4` target. No weakening
is proposed in LN §1.

### 1.2 Corollary (the kill)

**Corollary 1 (D-HS on `D^W` is excluded by Theorem 19.25; `PROVED`, unconditional given (X19)).** No function
`h⁰ : D^W → R_{≥0}`, in particular none of the form `\dim_S H⁰_X(·)` or `\log\#H⁰_X(·)` for any `S`-module `H⁰_X`
whatsoever, satisfies (a), (b′), (c) of Theorem 12.3 for `ξ`, for any `χ ∈ R`.

*Proof.* Theorem 19.25 (P46:6332-6351) quantifies over **every** function `D^W → R_{≥0}`; its proof uses nothing about
how `h⁰` is defined. Step 1 (`h⁰ = 0` in degree `≤ 0`): (b′) + Theorem 11.13(i),(ii),(iv) (P46:2542-2552). Step 2
(`h⁰(E) ≥ R(E)` for `\deg E > 1`): Step 1 at `K−E`, `\deg K = 1` (Theorems 11.7, 11.8(v)), clause (c), Serre symmetry
`R(K−E) = R(E)` (Theorem 19.2, P46:5930-5943). Step 3 (witness): `E = tF_0 + dK` of Theorem 19.23 (P46:6292-6300) has
`\deg E = d > 1`, `R(E) > 0`, hence `h⁰(E) > 0`, hence by (b′) an `E' ≥ 0`, `E' ≢ 0`, `E − E' ∈ 𝓝_∞`, which
Theorem 19.23 forbids via Lemma 19.17 (`|\mathrm{Re}\,e^{iθ}Φ_{E'}(ρ_1)| ≤ ½ s_1 \deg E'`, `s_1 < 1`). (Step 2 does
not in fact need Serre symmetry: (c) at `E` with `h⁰(K−E) = 0` gives `h⁰(E) ≥ R(E)` directly.) By §1.1, D-HS needs
exactly these clauses, on a domain containing `𝒢_{min}`; on `D^W` this is the kill, on `C_c^∞ ⊕ RK` see R1. ∎

Theorem 21.15 (P46:8796-8811) gives the same on the function-field model, where RH is a theorem and the geometric
`h⁰_C` exists (Theorem 21.16): the defect is the cone `𝓔_C`, not the absence of a sections functor
(Remark 21.16a, P46:8838-8850). D-HS is a proposal for a sections functor; Theorem 21.15 says a sections functor is
not what is missing.

### 1.3 The evasion clauses, each checked

D-HS could evade Corollary 1 only by changing an ingredient of Theorem 19.25's proof. Each is checked.

**(Ev-1) Different domain.** Larger: closed by §1.1, the transfer reads only `h⁰|_{D^W}`. `PROVED`. Smaller
(`C_c^∞ ⊕ RK`): closed by Lemma 3 for the fibrewise reading; definition-free closure = residual R1 (§1.1).

**(Ev-2) Different degree function `\deg'`.** Suppose D-HS replaces `\deg` by another linear `\deg' : D^W → R`
(e.g. a CC-type Arakelov degree of the fibre divisor, cf. Finding 13.8 / R140 D.24.2 declining `\deg_{CC} = \deg`).
Theorem 12.3 needs of a degree exactly three things: `\deg' > 0` on nonzero nonnegative classes (Step 4), `\deg'`
constant on `𝓝_∞`-cosets (Steps 2, 4), and **`\deg'(nF) = 0` for primitive `F`, i.e. `\deg'` vanishes on the primitive
space `P^W`** (Step 4, P46:2793-2797; Theorem 11.13(iii) for the frame's `\deg`). Without the third there is no Step 4
and no RH to obtain, so a `\deg'` lacking it is not an evasion but an abandonment of the transfer. With it, `\deg'`
factors through `D^W/P^W ≅ R²`: `\deg' = αa + βb`, `(a,b) = M(E)`, and positivity on the nonnegative cone (where
`a,b > 0`, Lemma 19bis.18) forces `α,β ≥ 0`, not both `0`. Then `\deg' K = (α+β)/2 > 0` and
`\deg' F_0 = (α−β)η` with `|η| < 10^{−390}` (Lemma 19.20(ii), P46:6206), so Step 2's requirement `\deg'(K−E) < 0` on
the witness holds for `d ≥ 2` with no sign choice and no parity argument. Step 1 uses only the first two properties.
Step 3's conclusion "no nonnegative `E'` with `E − E' ∈ 𝓝_∞`" (Theorem 19.23, P46:6294-6296) **does not mention the
degree at all** — `\deg` enters its proof as a tool, through Theorem 11.13(ii),(iv) and the two-sided bound
`|I_∞(E,F)| ≤ C_F\deg E` of Theorem 11.14(ii). The functional `R` is defined from `I_∞` and `K`, not from `\deg`
(Definition 19.1). Hence no change of degree function evades. `PROVED`.

**(Ev-3) Different canonical class / different Serre symmetry.** Suppose D-HS runs Theorem 12.3 with some
`K' ∈ D^W` in place of `K`. Serre symmetry `R'(K'−E) = R'(E)` is automatic for every `K'` (Theorem 19.2 uses only
bilinearity, P46:5932-5934) and is in any case not needed (Corollary 1, parenthesis). `R'(E) − R(E) = −½\,I_∞(E, K'−K)`
is **linear** in `E`, hence `O(d)` on the witness family `E = tF_0 + dK`, where `t = O(d)` from
`t²W_{F_0} < d²/2 − d/2 + 2χ`. On that family `R(E) = ½(d²/2 − t²W_{F_0}) − d/4 + χ` (Theorem 19.21(i), P46:6262)
ranges over `(0, ¼d²(1−s_1²) − d/4 + χ)` as `t²W_{F_0}` runs over the window `(s_1²d²/2, d²/2 − d/2 + 2χ)`; **choose
`t` at the bottom of the window**, `t²W_{F_0} = s_1²d²/2·(1+ε)`, so that `R(E) ≥ ¼d²(1−s_1²) − O(d)`. Then for
`d ≥ \max(2, \deg K')`: Step 2 needs `\deg(K'−E) = \deg K' − d ≤ 0`, Step 3 needs `R'(E) ≥ R(E) − O(d) > 0`, both true
for `d` large, with the **same** witness. No `K'` evades. `PROVED`.

**(Ev-4) Different cone in (b′).** This is Horn B (P46 §19.9, P46:6463-6500). LN §1 T3 (LN:44) states (b′) with the
**nonnegative** cone; D-HS proposes no other cone, so Corollary 1 applies to D-HS as proposed. `PROVED` for the cone
D-HS actually uses. If a sections-type cone `𝓔_{HS} := \{E : H⁰_X(E) ≠ 0\}` were substituted, Theorem 19.30 (P46:6465)
gives the necessary condition `C'_{F_0} ≥ G` under (T1_cone),(T2_cone):
  (i) If `𝓔_{HS} ⊆ \{E ≥ 0\} + 𝓝_∞`, then `C'_{F_0} ≤ C_{F_0} < G` and Theorem 19.30 refutes (B3 row, P46:6489). The
      inclusion is what a "divisor of a section" definition suggests — effective fibre divisors, averaged to the radial
      carrier by the positive operator `Frob_n ⋆ Δ^{rad} = Γ_n^{rad}` (P44 Prop 3ter.5, P44:1541-1551) — but the divisor
      of a section is only *linearly equivalent* to `D|_{y_0}` (cf. Theorem 21.16(b′), P46:8818-8820), and the assembly
      of fibrewise linear equivalence into `𝓝_∞`-equivalence on the square is not argued. `DIAGNOSTIC`.
  (ii) If `𝓔_{HS} = B4` (trace-nonnegative), P46 §20 applies: (T2_cone) fails for `B4^g` (Theorem 20.19, P46:7719) and
      `(b′)_{B4}` for the RR candidate on `B4^{g,0}` is equivalent to RH (Theorem 20.23, P46:7866). `PROVED` for B4 only.
  (iii) A cone with `C'_{F_0} ≥ G`, (T2_cone), and `≠ B4` is not treated by P46 or here.
So Horn B stays exactly as P46 §19.9/§20 record it: B4 the one survivor of Theorem 19.30's test (P46:6491), the sign
transported onto `(b′)_{B4}` (P46:7878-7880). **Horn B is a residual of the frame, open before and after this memo,
and D-HS neither supplies nor closes it: residual R2.** It does not save D-HS, which proposes no cone.

**(Ev-5) Different pairing `I'` in (c).** Then Theorem 12.3's conclusion is not `I_∞(F,F) ≤ 0` and Paper 45
Theorem 10.4 does not deliver RH: an abandonment of the target, not an evasion. `PROVED` (one line).

**(Ev-6) Different equivalence `𝓝'` in (b′).** Theorem 12.3 Step 2 needs `I_∞(·,H')` constant on `𝓝'`-cosets, i.e.
`𝓝' ⊆ \mathrm{rad}\,I_∞ = 𝓝_∞` (Theorem 11.11, (11.14)); so `𝓝' ⊋ 𝓝_∞` is impossible, and `𝓝' ⊊ 𝓝_∞` makes (b′)
stronger, so Theorem 19.25 applies verbatim. `PROVED` (one line).

**§28.4 check of the evasion clauses.** None of (Ev-1)–(Ev-6) is one of the six clauses of §28.4 (P46:11956-11973):
they modify the *frame* (domain, degree, `K`, cone), whereas §28.4 asks for a *new object* (a square with a
local-data polar divisor reading phase and both structures). §28.4 clause-by-clause for D-HS is in §4 below.

## 2. T1 and T2 independently: the radial collapse

Definitions used (P44 Definitions 3ter.1–3ter.2, P44:1440-1470): `Frob_n` = normalized Haar measure of the coset
`c_nK_{P(n)} ⊂ C_S`, `|x|_S = 1/n` on its support; `Frob_n^†` supported on `|x|_S = n`;
`Frob_n ⋆ Frob_n^† = Δ^{(n)}`, an idempotent `≠ Δ` for `n > 1` (Theorem 3ter.6(ii),(iv), P44:1554-1580).
Graph reading (LN §1): `Γ_{Frob_n} = \{(x, nx)\}` in the square, fibred over the second factor.

### 2.1 T1 — definability, and what compatibility does

Fix `E = Σ_{n∈N} h_n\,Γ_{Frob_n}`, `N` finite (LN T1). In the class space the multiplier is the integral idele class
`c_n`, `|c_n|_S = 1/n` (P44 Def 3ter.2, P44:1462-1466), not `n ∈ Q^×` (principal, trivial on `C_S`); LN's `(x,nx)`
means `(x, c_nx)`, and `Frob_n` is the Haar measure of the coset `c_nK_{P(n)}`, so the "graph" is a graph after
`K_{P(n)}`-averaging (Lemma 2(iii)). Fibre at `y_0`: `E|_{y_0} = \{x : (x,y_0) ∈ Γ_n\} = Σ_n h_n [y_0 c_n^{−1}K_{P(n)}]`
(Haar-smeared points of the "curve" `C_S`). **Every fibre is the translate of one divisor by the group:**

    E|_{y_0} = y_0 · E|_1 .                                                        (2.1)

`PROVED` (the graphs are graphs of group homomorphisms `x ↦ c_nx`; the fibre over `y_0` is the preimage, a translate).

Compatibility (LN §1, `:36-40`) is transport of a section over the fibre at `y_0` to the fibre at `ny_0` by `Frob_n`,
required isometric. Two consequences:

**Lemma 2 (`PROVED` under the stated definition).** (i) A compatible family is determined by its value on one fibre of
each transport orbit: transport is a map `H⁰(E|_{y_0}) → H⁰(E|_{ny_0})`, and compatibility says the family is its
image. (ii) The base is the second factor `C_S ≅ R_{>0} × K^♮`, `K^♮ = \{±1\}×∏_{p∈S_f}Z_p^× = \ker|·|_S`
(P44:1548-1549, Lemma 3bis.3b). The archimedean Frobenius `τ_a`, `a ∈ R` (Theorem 14.3(ii)) — included, since the
smearing `h(\log n)` makes the classes radial and `D^W` is a `Frob_∞`-module — is transitive on `R_{>0}`;
`Frob_n`-transport translates by `c_n` and averages over `K_{P(n)}`, so compatibility with all `Frob_n` forces
`∏_pZ_p^×`-invariance (by (iii)); nothing acts on `\{±1\}`. The base modulo compatibility is `R_{>0}×\{±1\}`:
**at most two orbits** (one if the classes are even in the sign coordinate). So `H⁰_X(E) ↪ H⁰(E|_1)^{⊕2}` and
`h⁰(E) ≤ 2\dim_S H⁰(E|_1)`. (iii) Since `Frob_n ⋆ Frob_n^† = Δ^{(n)} ≠ Δ`, the
transport is a partial isometry: it is an isometry on the `K_{P(n)}`-invariant sector and annihilates the rest.
Compatibility therefore forces the non-invariant components to vanish; `Δ^{(n)} ≠ Δ` can only **shrink** `H⁰_X(E)`.

So `H⁰_X(E)` is definable (as the invariant sub-module of one fibre's CC-cohomology), is an `S`-module, and has finite
`\dim_S` when the fibre does. **T1 passes, but with the module collapsed to (a submodule of) at most two copies of one
fibre.**

### 2.2 T2 — growth: the second factor of `m` does not exist

LN §1 expects `h⁰(mK) ~ (\#\text{fibres with } \deg E|_{y_0} > 0) × (\text{fibre dimension}) ~ m × m`. Both
factors are checked.

**Fibre dimension (PROVED, conditional on the identification).** CC's `\dim_S H⁰(D) = ⌈(\deg D + \log 2)/\log 3⌉ − 1_L`
on `\overline{\mathrm{Spec}\,Z}` (P46:3353-3360, arXiv:2205.01391v2) is **linear in `\deg D`** and a function of `\deg D`
alone. D-HS never says how the Haar-smeared measure `E|_1` is a CC Arakelov divisor (LN:20-24); the statement used is
the conditional one: *whatever linear fibre degree D-HS assigns, if CC's count is a function of that degree alone, the
fibre dimension at `E = mK` is `O(m)`*, since `\deg(mK|_1) = m\deg(K|_1)`. (With the weight `t` of §2.3,
`\deg(mK|_1) = m∫K(t)t\,dt = 0` because `K` is even, Theorem 11.7(i), and the fibre dimension at `mK` is `O(1)`.) One
linear factor at most.

**Fibre count (PROVED: collapses).** The load-bearing fact is immediate: for `E = mK` every linear fibre degree
`\deg(mK|_{y_0})` scales by `m`, so the set `\{y_0 : \deg(mK|_{y_0}) > 0\}` is **independent of `m`**. Hence the
"number of fibres with positive degree" cannot supply a factor of `m`, whatever measure is put on the base. (For a
CC-type degree the shift formula `\deg(y_0·D) = \deg D + (∫E)\log|y_0|` would make that set a half-line in
`\log|y_0|`; this is not derived from any corpus definition and is not used.) Compatibility (Lemma 2(ii)) makes the
point moot anyway: the family is determined on at most two fibres, so the count of fibres is not a multiplicity at all.
Either way,

    h⁰_{HS}(mK) ≤ 2\dim_S H⁰(mK|_1) = O(m) .                                      (2.2)

**T2 FAILS: linear, not quadratic.** This is the same number as P46 Theorem 13.6(ii) (`O_Q(\log m)` on every finite
truncation of the one-parameter lattice, P46:3513-3520) and R140 D.24.2 (`λ_{CC} = 1/\log 3`): the radial carrier has
**one** modulus line, so a "fibration" over it has one parameter, and the two factors of the surface heuristic are the
same factor. The reason, recorded as the note demands: **on the radial carrier the fibres are translates of one
divisor (2.1); the Hilbert–Samuel mechanism needs `~n` independent fibres, and the carrier has one orbit.**

**The tensor square gets `m²`, and dies (PROVED, corpus).** The corpus's way to two linear factors is the product of
the two bidegree entries `M(E) = (a,b) = (Φ_E(1),Φ_E(0))` — the degrees along the two rulings (P46 §19bis.3,
Definition 19bis.14). Their product gives `h⁰_□(mK) = ¼m²` on the nose (Theorem 19bis.15, P46:6980-6996) — and then
(b′) fails (Theorem 19bis.19, P46:7122) and (c) is equivalent to RH (Theorem 19bis.17, P46:7068-7108). Prop D.24.10
shows D-HS's isometric transport lands exactly here (`ab` is the transport invariant). So D-HS has two readings:
the fibrewise-module reading (linear growth, T2 dead) and the tensor-square reading (quadratic growth, (b′) dead,
(c) = RH). Neither is a route.

### 2.3 A sharper (b′)-kill for any fibre-degree functional (new, PROVED)

Whatever CC-type degree D-HS assigns to fibres, by (2.1) the data `(\dim_S H⁰(E|_{y_0}))_{y_0}` is a function of two
continuous linear functionals of `E`: `ℓ_1(E) := \deg(E|_1)` and `ℓ_2(E) := ∫E`. Hence `h⁰_{HS} = Ψ(ℓ_1(E), ℓ_2(E))`.

**Lemma 3 (`PROVED` for `w ∈ \{1,t\}`, the case D-HS needs).** Let `h⁰ : D^W → R_{≥0}` (or on any domain containing
`E_0` and `C_c^∞`) be not identically `0` and factor through `ℓ_1(E) = ∫E(t)t\,dt` and `ℓ_2(E) = ∫E(t)\,dt`. Then
clause (b′) fails.

*Proof.* Follow Theorem 19bis.19 (P46:7128-7149). Pick `E_0` with `h⁰(E_0) > 0`; if a bidegree entry of `E_0` is
negative, `E_0` itself is the witness (Lemma 19bis.18). Otherwise choose a real `F ∈ C_c^∞(R)` with
`∫F = ∫Ft = Φ_F(0) = Φ_F(1) = 0` and `Φ_F(ρ_1) = ∫F(t)e^{iγ_1t}dt ≠ 0`. Such `F` exists: `1, t, e^{t/2}, e^{−t/2},
\cos γ_1t, \sin γ_1t` are exponential polynomials with distinct exponents `0` (multiplicity 2), `±½`, `±iγ_1`, hence
linearly independent on any interval `I`; by density of `C_c^∞(I)` in `L²(I)` the six functionals `F ↦ ∫Fφ_j` are
linearly independent on `C_c^∞(I)`, so one of the last two is nonzero on the common kernel of the first four. Then
`h⁰(E_0 + tF) = h⁰(E_0) > 0` for all `t`, `M(E_0 + tF) = M(E_0)`, and `|Φ_{E_0+tF}(ρ_1)| → ∞`, exceeding `\max(a,b)`;
by Theorem 11.11 and Lemma 19bis.18 (P46:7112-7120) no nonnegative `E'` is `𝓝_∞`-equivalent to `E_0 + tF`. Since
`E_0 + tF` lies in any domain containing `E_0` and `C_c^∞`, the argument also runs on `C_c^∞ ⊕ RK`. ∎

*General form (restated per R155_057; not load-bearing).* For arbitrary continuous weights `w_1,…,w_k` the space
`V := \mathrm{span}\{w_i, e^{±t/2}\}` may contain `\cos γ_1t, \sin γ_1t` (e.g. `w_1 = \cos γ_1t`), and the separation at
`ρ_1` fails. Repair: `V_C` is finite-dimensional and `ξ` has infinitely many zeros `ρ_j` with distinct `γ_j`, so some
`e^{(ρ_j−½)t} ∉ V_C`; Theorem 11.11 gives `Φ_{E'}(ρ) = Φ_E(ρ)` at **every** zero and Lemma 19bis.18 bounds `|Φ_{E'}(s)|`
for every `s` with `\mathrm{Re}\,s ∈ [0,1]`, so the argument runs at `ρ_j`, with no growth condition on the `w_i`. The
round-1 statement (growth `< e^{|t|/2}`) and its proof are **withdrawn**; nothing below uses the general form.

So **(b′) fails for `h⁰_{HS}` by a proof that does not go through Theorem 19.25 and does not need (X19)**: D-HS is
killed twice, once by the frame (Corollary 1) and once by its own definition (Lemma 3). `PROVED`. (Clause (c) for
such an `h⁰` gives, by the argument of Theorem 19bis.17(i)
restricted to primitive `F` with `ℓ_i(F) = 0`, `I_∞(F,F) ≤ 0` on a finite-codimension subspace of primitive tests —
`DIAGNOSTIC`; not needed for the kill and not pursued.)

## 3. T5 — `Ξ_a`, and what Remark 19.26 means for D-HS

LN T5 demands: run the definition for `Ξ_a`; (c) **must** fail, traceably to the non-isometric transport
(`(n^a + n^{−a})Δ^{(n)}`), while holding for `ξ`.

**(PROVED) The demand cannot be met by any `h⁰`.** Theorem 12.4 (P46:3006-3017): no `h⁰_a` satisfies (a),(b′),(c)
for `Ξ_a`. Theorem 19.25: none does for `ξ`. Remark 19.26 (P46:6353-6367), bullets 2–3: `Ξ_a` "satisfies the same
obstruction … while (a) and (c) hold there too", and the falsifier "was all along detecting a defect of the frame …
and not a separation between `ξ` and `Ξ_a`". So the pattern T5 asks for — the clause set holding for `ξ` and failing
for `Ξ_a` — is empty for **every** definition. D-HS's "built-in falsifier" (unimodularity entering the definition,
LN `:36-42`) cannot discriminate, because the clauses it would discriminate in are jointly false on both sides.

**(DIAGNOSTIC) Where the non-isometry actually lands.** By Prop D.24.10(i), isometric transport is the invariance of
`ab`; for `Ξ_a` the transport scales the bidegree product by `((n^a + n^{−a})/2)^2 ≠ 1`, so a transport-compatible
module is rescaled or shrunk fibre by fibre. A rescaled `\dim_S` count is still a function of the fibre-degree
functionals of §2.3, so Lemma 3 (with the `Ξ_a`-frame's `ρ_1`, Theorem 12.4's objects) kills (b′) for `Ξ_a` too, by
the same route as for `ξ`. The non-isometry changes constants, not the clause that fails. It is a **magnitude** datum
(`λ_−λ_+`), and Theorem 19bis.22 / Corollary D.24.12 say magnitude data of this kind (`Z(r(D)) = 0`) are zero-blind;
the **phase** datum of open item (36) (P46 §28.3) is not what D-HS reads.

## 4. Verdict, §28.4 check, and the state of the geometric arc

**Verdict: D-HS KILLED, by three independent routes; residuals R1, R2, neither created by D-HS nor favourable to it.**
* Route 1: **Theorem 19.25, Steps 1–3** (Corollary 1), definition-free on `D^W`, since D-HS needs (a),(b′),(c) with
  the nonnegative cone on a domain containing `K`. Confirmed on the curve by Theorem 21.15, where an `h⁰` exists and
  the defect is still the cone.
* Route 2: **T2 fails** — `h⁰_{HS}(mK) = O(m)` by the radial collapse (2.1)–(2.2) under the fibrewise reading; the
  surface heuristic's two factors are one factor (times `≤ 2`) on a carrier with at most two transport orbits.
* Route 3: **(b′) fails** for any `h⁰` built from the fibre degrees `∫E·t`, `∫E` (Lemma 3, no (X19)), and for the
  transport-invariant tensor-square reading (Prop D.24.10, Theorem 19bis.19, phase 140); in that reading **(c) is RH**
  (Theorem 19bis.17).
* T5 cannot be passed by any definition (Theorems 12.4 + 19.25, Remark 19.26).
* Evasion clauses (Ev-1)–(Ev-6) checked (§1.3). Residuals: **R1** — the small domain `C_c^∞ ⊕ RK` is killed
  definition-free only after a one-paragraph truncation of `F_0` is written into P46 §19.6 (until then, by the
  reading-dependent Lemma 3); **R2** — the cone in (b′) is Horn B, where P46 records B4 as passing Theorem 19.30's test
  and `(b′)_{B4} ⟺ RH`; open before and after this memo, unchanged by it.

**§28.4 six clauses, checked for D-HS (each `PROVED` as a reading of the definition in LN §1):**

| clause | D-HS | verdict |
|---|---|---|
| (1) a square, positive after every twist (Rankin) | a dimension count `\dim_S H⁰_X`, not a square; nonnegativity is by fiat, and it is transport-invariant in `ab` only | fails |
| (2) polar divisor determined by local data | none; the pole enters through `K` in clause (c), i.e. through the frame's `R` | fails |
| (3) zeros holomorphic left of the a priori pole | no object of which this could be asserted | fails |
| (4) reads phase (fails for `Ξ_a`) | reads `λ_−λ_+ = 1`, a magnitude; zero-blind by Theorem 19bis.22 / D.24.12; cannot separate `ξ` from `Ξ_a` (§3) | fails |
| (5) both additive and multiplicative structure | multiplicative only (radial carrier, `Frob_n`, `τ_a`); no additive input | fails |
| (6) uniform in the number field | yes (Theorem 19bis.15 / R140 (AT-3)), which by T1 (Theorem 18.1) is required — and means the route would prove GRH for every `ζ_K` | passes vacuously |

Not a reopening. D-HS moves none of the walls of §28.2.

**For the owner, plainly (DIAGNOSTIC).** After this memo, **no arithmetic-geometry candidate remains in the corpus.**
PATH-TO-D row (vi) listed D-HS as the "one residue" of the geometric arc; it is closed, and one of its two readings
was in fact already closed in phase 140. The residuals R1, R2 are the frame's own open items (P46 §19.6, §19.9/§20),
not arithmetic-geometry candidates. What remains geometric in P46 §28.3 are *open items*, not candidates:
(36) a class carrying a phase datum, (40) a sections functor with `m²`-growth on the graded carrier `𝒟_L`, (P145′) a
mechanism with `𝔈 ≠ D^W`, O-148.2 a kernel class on the square. Each must pass the same gate D-HS just failed —
Theorem 19.30 / Corollary 24.11 / Corollary 25.9 say the defect constant `s_* < 1` is unchanged by every enlargement
built so far — and none is proposed as a construction. The geometric arc is closed in the map; reopening is only by
the single object of §28.4, which nothing in this memo supplies or suggests.

## For the auditor

1. Corollary 1: verify that Theorem 12.3 evaluates `h⁰` only at `nF` and `K−nF` (P46:2777-2797), so a larger domain
   cannot matter; and that the small domain `C_c^∞ ⊕ RK` is covered only by Lemma 3 until the truncation lemma (R1)
   is written (§1.1).
2. (Ev-2): check the three-property list against Theorem 12.3 Steps 2 and 4 (P46:2777-2797), the factorisation
   `\deg' = αa + βb` through `D^W/P^W`, and `|\deg' F_0| = |α−β||η|` with Lemma 19.20(ii) (P46:6206).
3. (Ev-3): `R'(E) − R(E) = −½I_∞(E,K'−K)` linear; `t = O(d)` from `t²W_{F_0} < d²/2 − d/2 + 2χ` (P46:6294); `R(E)`
   from Theorem 19.21(i) (P46:6262); the choice of `t` at the bottom of the window.
4. (Ev-4): confirm the labels — `PROVED` for the nonnegative cone; case (i) `DIAGNOSTIC`; case (ii) `PROVED` for B4
   only (Theorems 20.19, 20.23 at P46:7719, 7866 are about `B4^g`, `B4^{g,0}`); case (iii) untreated; R2 = Horn B.
5. Lemma 2(ii): base `C_S ≅ R_{>0}×K^♮` (P44:1548-1549), `≤ 2` orbits, bound `h⁰ ≤ 2\dim_S H⁰(E|_1)`; T2's load-bearing
   fact is the `m`-independence of `\{y_0 : \deg(mK|_{y_0}) > 0\}`, not any degree-shift formula.
6. Lemma 3, `w ∈ \{1,t\}`: linear independence of the six exponential polynomials and density of `C_c^∞(I)` in
   `L²(I)`. The general form is restated with the zero chosen off `V_C` and is not load-bearing.
7. Correction of record (§0): only PATH-TO-D `:328` ("never killed") is inaccurate; `:189` is accurate. Prop D.24.10
   kills D-HS in the frame's reading (transport = `τ_{\log n}` on `D^W`) only.
8. No numerics anywhere; the only constants quoted (`s_1`, `G`, `d_0`, `η`, the margin `5.79×10^{−3}`) are P46's,
   cited by line.

## Amended per R155_057 (hostile audit, 2026-09-22)

Every change to the round-1 text, by audit item. No new claims were added; labels were lowered or split where the audit
required.

1. **§0 corpus correction.** Restricted to PATH-TO-D `:328` ("never killed"); `:189` recorded as accurate. Added that
   Prop D.24.10 kills D-HS only in the frame's reading (transport = `τ_{\log n}` on `D^W`, R140:1118-1119).
   (Audit §6.)
2. **§1.1 domain claim split.** "The domain of D-HS is `D^W`" replaced by: larger domain irrelevant (`PROVED`);
   minimal domain `𝒢_{min} ⊂ C_c^∞ ⊕ RK` not literally in the range of Theorem 19.25 because the Gaussian witness `F_0`
   is not compactly supported. Truncation lemma sketched (margin `G(1−s_1) = 5.79×10^{−3}`, P46:6288) and labelled
   `OPEN`, residual **R1**; the small-domain kill rests on Lemma 3 (`w ∈ \{1,t\}`). Citation for the `Frob_n` action
   corrected to P46:3350-3351 / Theorem 14.3(ii), with Theorem 11.8(iii) cited only for the bidegree match.
   (Audit §0, §1, §2 Ev-1.)
3. **Corollary 1.** Title restricted to `D^W`; noted that Step 2 does not need Serre symmetry; closing sentence now
   points to R1 for `C_c^∞ ⊕ RK`. (Audit §1.)
4. **(Ev-2).** Added the third property Theorem 12.3 Step 4 needs, `\deg' = 0` on `P^W`, and the resulting
   simplification `\deg' = αa + βb`, `\deg' K = (α+β)/2 > 0`, `|\deg' F_0| = |α−β||η|`, `|η| < 10^{−390}`
   (Lemma 19.20(ii)); parity/sign-of-`t` argument dropped as unnecessary; the two-sided bound Theorem 11.14(ii) named
   as the actual mechanism. (Audit §2 Ev-2.)
5. **(Ev-3).** `R(E)` written out from Theorem 19.21(i) (P46:6262) with its range over the `t`-window; the choice of
   `t` at the bottom of the window stated explicitly so that `R(E) ≥ ¼d²(1−s_1²) − O(d)`; `d ≥ \max(2,\deg K')`.
   (Audit §2 Ev-3.)
6. **(Ev-4).** Relabelled: `PROVED` only for the nonnegative cone D-HS actually uses; case (i) `DIAGNOSTIC` with the
   linear-equivalence gap named (Theorem 21.16(b′)); case (ii) `PROVED` for B4 only, with Theorems 20.19/20.23 cited as
   statements about `B4^g`/`B4^{g,0}`; case (iii) (cone with `C'_{F_0} ≥ G`, (T2_cone), `≠ B4`) recorded as untreated.
   The sentence "either fails Theorem 19.30 or is RH" withdrawn. Horn B recorded as residual **R2** of the frame, not
   of D-HS. (Audit §2 Ev-4.)
7. **(Ev-5), (Ev-6) added**, one line each: a different pairing abandons the target; a larger `𝓝'` is impossible
   (`𝓝' ⊆ \mathrm{rad}\,I_∞ = 𝓝_∞`, Theorem 11.11), a smaller one strengthens (b′). §28.4-check sentence updated to
   (Ev-1)–(Ev-6). (Audit §2.)
8. **§2.1 radial collapse.** Multiplier corrected to the integral idele class `c_n` (P44 Def 3ter.2); base corrected
   to `C_S ≅ R_{>0}×K^♮` (P44:1548-1549), joint action transitive on `R_{>0}` only, `\{±1\}` unacted on; orbit count
   `≤ 2`; bound `h⁰(E) ≤ 2\dim_S H⁰(E|_1)`; T1 sentence adjusted. (Audit §3.)
9. **§2.2 T2.** Fibre dimension relabelled `PROVED, conditional on the identification` of `E|_1` with a CC divisor;
   noted `\deg(mK|_1) = 0` for weight `t` (`K` even, Theorem 11.7(i)). Fibre count restated on the load-bearing fact —
   `m`-independence of `\{y_0 : \deg(mK|_{y_0}) > 0\}` for every linear fibre degree — with the degree-shift formula
   demoted to an unused aside. (2.2) now carries the factor `2`. "Only way to get `m²`" → "the corpus's way"; "only"
   dropped. (Audit §3.)
10. **Lemma 3.** Split: `w ∈ \{1,t\}` kept `PROVED` with the exponential-polynomial independence and `L²`-density
    argument written out, and the remark that the argument runs on `C_c^∞ ⊕ RK`. General form restated with the
    zero-choice repair (pick `ρ_j` with `e^{(ρ_j−½)t} ∉ V_C`; Theorem 11.11 and Lemma 19bis.18 hold at every zero);
    the round-1 growth clause `< e^{|t|/2}` and its proof **withdrawn**; general form marked not load-bearing.
    (Audit §4.)
11. **§4 verdict.** Reworded as the audit recommends: "KILLED by three independent routes; residuals R1, R2"; "No
    residual" withdrawn; "one-orbit carrier" → "at most two transport orbits"; owner paragraph notes R1, R2 are frame
    items, not candidates. (Audit §7.)
12. **For the auditor** list rewritten to match the amended statements (items 1–8).
