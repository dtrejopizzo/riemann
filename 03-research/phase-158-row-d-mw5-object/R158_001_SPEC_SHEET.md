# R158_001 — Phase 158: the MW-5 specification sheet

Task: R158_000 round 1, row 1. Pure mathematics; no computation; **no sign is claimed, asserted or
suggested anywhere in this file.** Row D has no label, and the endpoint of record is unchanged (reduced statement §3).
Labels: `PROVED` (proved here or in a cited labelled statement of the record), `CITED` (open literature, read this
review unless marked "abstract only"; or a labelled statement of Papers 46/47 / a phase file, cited by label),
`HEURISTIC` (a reading or analogy, carrying no proof weight), `OPEN`.
Form rule (R156_004 A14): every positivity statement says whether it is the **primitive** form (`λ^A_T`, `𝔞_T` on
`P_T`) or the **complete** form (`λ^W_T`, `W_T` on `L²(I_T)`).

**Audit status:** audit `R158_003_AUDIT_SPEC.md`. Amendments A1–A20 are applied in place,
each marked "[amended per R158_003]". Struck text (~~…~~) is retained for the record.

---

## §0 Verdict in one paragraph

Weil's proof over `F_q` needs six ingredients: a surface, a Frobenius, `H¹`, a Lefschetz formula, a positive form
compatible with the Frobenius, and a uniform extraction. §1 states each of them in the P46 language (W-1…W-6). The
proved record puts 27 constraints on these ingredients (§2, C1–C27). From them I derive a 12-item **object test**,
OT-1…OT-12 (§3). One elementary statement organises the test. **Lemma T** (§3.1, `PROVED`, elementary; content
`CLASSICAL`, no novelty claimed): the Deninger/Serre data (`H¹`, a flow, the trace formula, a conformal positive form),
taken as axioms on abstract data, are satisfiable **if and only if RH holds**; the (⇐) witness is the spectral one,
defined from the zeros. **[amended per R158_003: A1 — the original wording "if the positive form may be defined from
the spectrum, then … exist iff RH" misplaced the qualifier: (⇒) holds for every realisation; only the (⇐) witness
reads the zeros. (⇒) is Serre 1960 as formalised in Deninger math/0204110 Thm 2.1 and Leichtnam 1307.3851 §2; (⇐) is
the trivial Hilbert–Pólya converse (R157_002 row 32, EQUIV).]** So the whole content of MW-5 is OT-5′: the form has
to be **defined before the spectrum and without it**, and its compatibility with the flow has to be **proved**. This is ENUNCIADO-MÍNIMO-130 of
phase 43, now pinned to the P46 forms. §4 runs eighteen published frameworks through the test. **None passes. Every
framework fails OT-1 (no `H¹` with the right spectrum is constructed), or OT-2/OT-12 (the trace formula is not ζ's
explicit formula with its archimedean place, or, for Connes' adèle class space, the global trace formula is itself
equivalent to RH), or OT-3/OT-5′ (the positivity is postulated, or it is installed from eigenvalue data).** Two
frameworks attached to arithmetic have a *derived* positivity: Deninger–Singhof's Kähler–Riemann polarization and the
Faltings–Hriljac arithmetic Hodge index (the third, tropical Hodge index, is not attached to ζ at all).
**[amended per R158_003: A17 (Connes row), A18 (count of derived positivities).]** Both live in a class where the object cannot be ζ's: a compact manifold,
where conformality forces `α = 0` and forbids fixed points, and an arithmetic surface, whose "square" over `Spec Z`
does not exist. That is the sharpest form of MW-5 on record. The cluster stays **NOT EXCLUDED, unbuilt**; this sheet is
a filter, not an object.

---

## §C Corpus check (done first, per the working rule)

Grep over `03-research/`, `04-papers/`, `05-meta-and-planning/`, `NO-GO-LIST.md` (`.md/.tex`, `.bak` excluded), file
counts: MW-5 191 · Deninger 132 · Morishita 28 · arithmetic site 43 · scaling site 29 · Riemann–Roch 133 · `H¹` 45 ·
Hodge index 194 · Rosati 92 · Lefschetz 267 · Arakelov 153 · Borger 14 · NG-107 6 · ENUNCIADO-MÍNIMO-130 3 ·
Leichtnam 1 (phase 42 Doc 128) · **Kopei 0** (new to the corpus). The load-bearing prior items:

| item | where | what it fixes for this sheet |
|---|---|---|
| MW-5 as defined | `NO-GO-LIST.md:221–232`; MAP_1:59 | needs `H¹(Spec Z,F)`, Frobenius `φ_p`, a positive intersection form. "UNBUILT (not proved impossible)" |
| MW-5 reopened | PHASE_136_MAP_SYNTHESIS l.72, l.132; MAP_5 §2 | "R16 answered only for CC's curve; the square was never tested" |
| Deninger circularity test | `phase-43-hodge-foliated-specZ/130-circularity-to-destruction-test-of-deninger-s.md` §§0–5 | **verdict INDETERMINABLE, biased to CIRCULAR**. Deninger–Singhof (math/0204111) derives the polarization from a Kähler–Riemann structure (geometry, no ζ), but in the only arithmetic case realised (math/0204194, elliptic curve) the leafwise metric is built **using Hasse `|ξ|² = q`**. ENUNCIADO-MÍNIMO-130 (§5.3) is the fire test |
| Deninger programme survey | `phase-42-hodge-dynamics/128-deninger-s-program-is-this-the-missing.md:24, 63, 166` | the space for `Spec Z` is not constructed; spectral rigidity for suspensions (1712.04181); AKL 2402.06671 proves the trace formula on closed manifolds |
| scaling-foliation "proof" audit | `phase-15-arithmetic-hodge-index/M8-front1-proof-audit-REFUTED.md` F1, F5 | the scaling action has continuous spectrum and infinite invariant measure; the Hodge identities for Riemannian foliations need finite transverse measure and finite-dimensional basic cohomology, and **fail** there |
| NG-62b, NG-63 | `NO-GO-LIST.md:362–391`; MAP_1:73–74 | on the finite window a quaternionic HR form exists but is gapless; the scaling generator **anticommutes** with `J` (antilinear). Diagnostics, not theorems (PHASE_136 §3) |
| NG-113-O1/O2/O3, NG-113-d3 **[added per R158_003: A19]** | `NO-GO-LIST.md:490–517`; `phase-113-the-trace-on-schwartz-data/113_10`–`113_13` | inside the Schwartz-data class `D`: the effective cone is scaling-stable (`h⁰(nD) = h⁰(D)`, O1); the correspondences `δ_n` have **infinite mutual intersection**, `|(n/m)^ρ| = (n/m)^{1/2}` (O2); no spectral gap on the negative part (O3); divisors and sections doubly dissociated (d3); the remaining effectivity input `(E°)` ⟺ RH (`113_10` Thms 4.2/4.3). Bears on OT-9: a two-variable carrier whose Frobenius graphs are the `δ_n` of `D` inherits O2 |
| Doc 130 quotations **[note per R158_003: A20]** | `130-circularity-to-destruction-test-of-deninger-s.md:82` | re-read in source (math/0204194, pdftotext): the Hasse sentence is verbatim; the metric is `g̃ = e^t Re(ξ η̄)` on **tangent vectors** `ξ, η ∈ C` (not the Frobenius element `ξ`), and it (with the measure `μ_ξ(ξ^ν A) = |ξ|^{−2ν}μ_ξ(A) = q^{−ν}μ_ξ(A)`) is invariant under `H`, which acts by `(z, v̂, t) ↦ (ξ^{−ν}z, ξ^{−ν}v̂, t + ν log q)`, exactly because `|ξ|² = q`. Doc 130's conclusion stands; its further "verbatim" lines at l.82 are a summariser's paraphrase, not source text |
| NG-107 | `107_242` Thm 4.1; `114_a_03` §6.1 | the Morishita bridge `Ψ_F` kills the transverse `p`-adic direction. It blocks cycles through `Ψ`, not the Deninger space |
| P122.007, phase 15 M3/M10 | P157_002 row 36 | Faltings–Hriljac cannot be imported (hypothesis mismatch; heights ≠ zeros) |
| MAP_5 §§1–4 | phase 136 | CC RR on `Spec Z̄` has integer dimensions with logarithmic growth. CC 2006.13771 names "an intersection theory of divisors on the square of the Scaling Site … still in development". No source uses Frobenius unimodularity in a positivity argument |
| P47 §§12, 17–22, 27–28 | `04-papers/47-intersection-frame-defect/archive/main.md` | read for this sheet: Thm 12.3, 12.4, Prop 12.4B, Restatement 12.4a/Rem 12.4a′, Cor 17.11, Thms 18.1, 18.14–18.16, Cor 18.17, Thm 19.25, Cor 19.25b, Rem 19.25c, Restatement 19.29, Thms 21.8, 21.15, 21.16, Rem 21.16a, §21.7, (P145′), Prop 22.5, Cor 22.9a, Thm 22.17, Thm 26.13, Thms 27.3, 27.10, 27.11, Rem 27.16, Prop 27.17, §28.2, §28.4 |
| P46 labels | `04-papers/46-row-d-dual-certificates/main.tex` | `eq:W` (l.134), `def:W`/`eq:nuw` (l.1219), `thm:Z`, `lem:Rrig`, `thm:finZ`, `thm:SC`, `thm:arena`, `thm:margin`, `cor:margin2`, `prop:finite`, `thm:finmod`, `rem:resweights`, `prop:finsupp`, `cor:void`, `prop:uniform`, `thm:parityschur`, `cor:convfail`, `lem:monoT`, `cor:mono`, `thm:O` — each checked against its statement (process rule ) |

The "§5 RESTATEMENT" named in the task is taken to be E6 of the reduced statement, i.e. P47 **Cor 17.11**
(`RESTATEMENT`): RH ⟺ the Hodge-index inequality `I_∞(F,F) ≤ ½(deg F)²` on `D^W` ⟺ it holds on any detecting cone.
P47 §5 itself (D.3, finite inertia) is retired (§9.1(13)) and supplies no constraint here.

---

## §1 Weil's proof over `F_q`, decomposed, in the language of Paper 46

Notation (P46 §1, `eq:W`): `W_T(F) = 𝔞_T(F) + 2Re(A(F)\overline{B(F)}) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ)`, with
`A(F) = ∫F e^{t/2}`, `B(F) = ∫F e^{−t/2}` (the Tate moments) and `P_T = {A = B = 0}`. P47: `I_∞ = B_pol + Ŵ`,
`Ŵ = −Σ_ρ Φ_F(ρ)Φ_G(1−ρ)`, polar plane `Λ = span(K, K_odd)` of signature `(1,1)` (A6), primitive sector `P^W`
(Thm 11.10), and the identity `I_∞ = 2Φ(0)Φ(1) − W` (P47 (11.6), quoted in Prop 22.5).

Weil's proof for a curve `C/F_q` of genus `g`, on `S = C × C` (CITED, classical: Weil 1948; Mattuck–Tate 1958;
Grothendieck 1958; Hartshorne V.1.9; as transported in P47 Thm 12.3/Rem 12.3a and Thm 21.16):

**W-1 (the surface and its hyperbolic plane).** `NS(S)_R` with the intersection form; the fibres `F_1, F_2` span a
hyperbolic plane, `F_1·F_2 = 1`, `F_i² = 0`. *Analytic form.* `D^W` with `I_∞`; the polar plane `Λ` spanned by the
canonical class and its odd partner (P47 A6, Thm 18.14 row ξ). The two Tate moments `A, B` are the pairings against
the two rulings: in the model `F_1, F_2 ∈ V_C` are honest classes (P47 §21.8, mismatch 6), whereas arithmetically
`e_∓` are the radical of the boundary form (Paper 43 Thm 9.14c). `P_T` is the window's copy of the orthogonal
complement of the hyperbolic plane. — `CITED` (P47) for the dictionary; the correspondence of *names* is `HEURISTIC`.

**W-2 (the Frobenius and its graphs).** `Γ_{π^n} ⊂ S`, with `Γ_{π^n}·Δ = N_n = #C(F_{q^n})`. *Analytic form.* The
Frobenius translates `Frob_n` (Paper 44 (1.5); P47 (1.5)); `Frob_m ⋆ Frob_n = Frob_{mn}`; the contacts `N_T` with
weights `v_n = 2Λ(n)/√n` in `s_T(τ) = m(τ) − Σ_{n∈N_T} v_n cos(τ log n)` (P46 `eq:symbol`). The curve-model dictionary
(sign `+`) is P47 Thm 21.7. — `CITED`.

**W-3 (`H¹` and its Frobenius).** `H¹_ét(C_{\bar F_q}, Q_ℓ)`, of dimension `2g`, with `π^*` having eigenvalues
`α_1,…,α_{2g}`; `H⁰`, `H²` one-dimensional with eigenvalues `1`, `q`. *Analytic form.* P46 has **no** `H¹`. The
closest object is the Gram form itself: `W_T` on `L²(I_T)`, whose "trace" is the zero sum. The Deninger shape
(Leichtnam 1307.3851 §2, axioms 4–6; `CITED`, read this review): `H⁰ = R` with `Θ = 0`, `H² = R` with `Θ = 1`, and
`H¹` infinite-dimensional with `Θ` having discrete spectrum equal to the non-trivial zeros. Normalised by `e^{−t/2}`,
the eigenvalues `0, 1` of `H⁰, H²` are the polar set `P = {0,1}` with `|p − ½| = ½`, i.e. **A3** (P47 Def 18.13).
— `CITED` (Leichtnam) + `HEURISTIC` (the A3 reading, made precise as C9 below).

**W-4 (the Lefschetz formula).** `N_n = 1 + q^n − Tr(π^{n*} | H¹)`. *Analytic form.* The Weil explicit formula,
written as P46 `eq:W`, `W_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ)`, and in dual form P46 `thm:Z` (`PROVED`): for every flat-top
`w ∈ 𝒲_T` (`def:W`), `f_w(τ)` is the right side of the explicit formula for `h_τ = w cos(τ·)`, and for `w ∈ 𝒲^reg`,
`f_w = Σ_ρ ŵ(τ − γ_ρ)`. A Lefschetz formula for an MW-5 object must be this identity, with `Tr(·|H¹)` on the zero side,
`H⁰ ⊕ H²` supplying `Φ(0) + Φ(1)`, and the fixed-point/orbit side supplying `m(τ)` (i.e. `C_0`, `K(u)`) and
`Σ v_n cos(τ log n)`. — `CITED` (P46) for the formula; the reading as a trace is `HEURISTIC`.

**W-5 (the positive form: two shapes, two proofs of Weil).**
* **(P-HI) Hodge index / Castelnuovo–Severi on `NS(S)`.** Negative definiteness on the orthogonal complement of the
  hyperbolic plane; equivalently `D² ≤ 2(D·F_1)(D·F_2)` (Castelnuovo). *Analytic form.* On the primitive sector the
  Hodge index is `I_∞ ≤ 0` on `P^W`, i.e. **primitive-form positivity** `𝔞_T ≥ 0` on `P_T` for every `T`: E2 of the
  reduced statement (P45 Thm 10.4; P47 Thm 12.3 conclusion). The Castelnuovo form `I_∞(E,E) ≤ 2Φ_E(0)Φ_E(1)` is, by
  `I_∞ = 2Φ(0)Φ(1) − W`, exactly **complete-form positivity** `W_T ≥ 0`: E1 (P47 Restatement 19.29(iv) gives the
  surface shape `D² ≤ (D·H)²/H²` at `H = 2K`). — `PROVED` (identity of record) + `CITED`.
  **[amended per R158_003: A2 — signs checked against P47 (11.6) (l.2136: `I_∞(F,G) = Φ_F(0)Φ_G(1) + Φ_F(1)Φ_G(0) −
  Σ_ρΦ_F(ρ)Φ_G(1−ρ)`, real `F, G ∈ D^W`) and P46 `eq:W`/`lem:roughEF` (`Φ_F(s) = ∫F e^{(s−½)t}`, `Φ_F(1) = A`,
  `Φ_F(0) = B` for **real** `F`, `2Φ_F(0)Φ_F(1) = 2Re(A B̄)`): both directions are correct **for real tests**; on
  primitive real tests `I_∞ = −W = −𝔞_T`, so Hodge index `I_∞ ≤ 0` ⟺ `𝔞_T ≥ 0`. The inequality
  `I_∞(E,E) ≤ 2Φ_E(0)Φ_E(1)` is E1 (= RH), **not** a theorem; Restatement 19.29(iv) is used here only for the
  *shape* of the surface inequality. (P47 19.29(iv) itself reads "the bound … is the surface inequality" after citing
  Thm 19.6(ii), which proves clause (c) only; its wording is flagged in R158_003 §6, not edited.)]**
* **(P-HS) Rosati positivity / unitarity.** `Tr(ff†) > 0` on `End(J_C)⊗Q` and `ππ† = q`, so `q^{−1/2}π` is unitary
  for a positive-definite form and `|α_i| = √q`. *Analytic form.* A Hilbert structure on `H¹` for which
  `U_t := e^{−t/2}φ^t` is unitary (Serre 1960; Deninger math/0204110 Thm 2.1: conformality
  `g(Tφ^t v, Tφ^t w) = e^{αt}g(v,w)` gives `Θ = α/2 + S` with `S` skew on `H̄¹_F`; `CITED`, read this review). Then,
  for `F ∈ L²(I_T)` and `F(U) := ∫F(t)U_t dt`, the trace formula would read `W_T(F) = ‖F(U)‖²_{HS}`. That is
  **complete-form** positivity directly, as a Hilbert–Schmidt norm, and the primitive form is its restriction.
  — the implication is `PROVED` (§3.1, Lemma T(⇒)); the identification with Rosati is `HEURISTIC`.

**W-6 (the geometric source and the extraction).** In Weil's proof the positivity of W-5 is a theorem about **every**
surface. It is proved from Riemann–Roch on `S` plus ampleness (bigness of `D` with `D² > 0`, `D·H > 0`; P47
Restatement 19.29(i)–(iii)), or, in the Rosati shape, from the ampleness of the theta divisor. It is proved **before,
and without, any knowledge of the `α_i`**. The extraction then applies W-5 to `mΓ_{π^n} + nΔ + …` for **all** `n`,
which gives `|Σ_i α_i^n| ≤ 2g q^{n/2}` for all `n`, hence `|α_i| = √q`. *Analytic form.* "For all `n`" is "for all
`T`" (P46 `prop:uniform`; R157_002 O1: `W_T` is the restriction of `W_{T'}` for `T < T'` by `lem:monoT`, so uniformity
in `T` is global Weil positivity on `C_c^∞(R)`). — `CITED` + `PROVED` (O1 is a RESTATEMENT of record).

**Remark 1.1 (infinite genus; `HEURISTIC`).** Over `F_q`, `H¹` is `2g`-dimensional, so a finite compression sees
everything. P47 Rem 21.23 reads the divergence of `I_A(Frob_n, Frob_n)` as `Δ·Δ = 2 − 2g → −∞`: "the arithmetic curve
has infinite genus". `thm:margin` (`λ^W_T ≤ λ^A_T ≤ 4·10⁹ T e^{−15.449T}` for `T ≥ 1`) and `thm:arena` (log-slow
archimedean gaps) are the analytic shadow of this. An MW-5 object must therefore work where no finite compression
decides anything (C18, C19).

---

## §2 The proved constraints, ingredient by ingredient

Each row states the constraint, its source label, and its type. "Object" means any candidate supplying W-1…W-6.

### 2.1 On the carrier and on `H¹` (W-1, W-3)

| # | constraint | source | label |
|---|---|---|---|
| C1 | `H¹` must be infinite-dimensional, and the positivity must not reduce to finitely many modes or finitely many zeros: no finite zero set carries a flat-top certificate; no finite truncation decides the even Schur complement | P46 `thm:finZ`, `thm:arena`; N5, D.53 | PROVED |
| C2 | The object's definition may not read the zeros (else it is satisfiable ⟺ RH, Lemma T below; cf. P47 Rem 19.25c(i): on the bare set `𝒢_min` the hypothesis of Thm 12.3 is satisfiable ⟺ RH; Suzuki 2301.00421 quoting Selberg, MAP_5) | Lemma T (§3.1); P47 Rem 19.25c(i) | PROVED |
| C3 | Over `Spec Z` the Frobenius cannot be an endomorphism of a one-variable object: `Hom(Spec Z, Spec Z) = {id}`; `m + n·Frob_ℓ` has no realisation by self-maps; the only additive structure on `{Frob_n}` compatible with the explicit formula is the formal one, which is zero-blind and `Ξ_a`-uniform | P47 Thm 22.17 (CLASSICAL (i),(ii); PROVED (iii)); Prop 22.5; R146 D.45.8 | PROVED **[amended per R158_003: A3 — Thm 22.17 is about `Spec Z` in the category of schemes and self-maps of the base; it does not bind a non-scheme carrier (the arithmetic site realises Frobenius correspondences `Ψ(λ)` on its square, §4). Read C3 as: no ring of self-maps of `Spec Z` contains `m + n·Frob_ℓ` (22.17(iii)); the only additive structure *available on the frame's* `{Frob_n}` is the formal `Z⟨Frob_n⟩`, whose form `Q_0` is zero-blind and `Ξ_a`-uniform (Prop 22.5(i),(ii)). "Compatible with the explicit formula" is not in the source and is dropped]** |
| C4 | Hence any object realising a sum `Frob_m + Frob_n` with content at the zeros must live on `C_S × C_S` in two independent variables, and must not be supported on shifted diagonals | P47 Cor 22.9a | PROVED given the cited obstruction P122.028, on the frame's radial carrier **[amended per R158_003: A4]** |
| C5 | The carrier must have an **archimedean place**. On a compact 3-manifold with a Riemannian foliation, a dense leaf and a transversal conformal flow, the conditions force `α = 0` (the flow is isometric), while number theory needs `α = 1`; closed-orbit lengths generate a finitely generated group unless the flow has fixed points, and ζ needs `{log p}`, which is infinitely generated. So the phase space cannot be such a manifold and needs fixed points, i.e. laminated/solenoidal spaces **[amended per R158_003: A5 — two separate statements in the source (re-read, pdftotext): Rem 2 "the conditions of the corollary force α = 0", with α ≠ 0 expected on Sullivan's generalized solenoids; Rem 3 "the group generated by the lengths of closed orbits is a finitely generated subgroup of R", and "in order to achieve an infinitely generated group the flow must have fixed points". Hypotheses: compact 3-manifold, Riemannian foliation by surfaces with a dense leaf, flow everywhere transversal and conformal (9). So: α = 1 needs a non-manifold carrier; `{log p}` needs fixed points; neither implies the other]** | Deninger math/0204110 Thm 2.1, Cor 3.5 Rem 2–3, §4 after (22) | CITED (text read) |
| C6 | At a real archimedean place the Guillemin–Sternberg contribution of a fixed point matches the explicit formula for `t > 0` and **not** for `t < 0`; Deninger's Assumption 7 (an orbifold trajectory into the fixed point) is proposed to resolve this | Leichtnam 1307.3851 Prop 2, §4.4 | CITED **[amended per R158_003: A6 — attribution corrected. Prop 2 (Deninger [De01]): 1] match for `t > 0`; 2] no match for `t < 0` (Guillemin–Sternberg `e^{2t}/(1−e^{2t})` against `e^t/(1−e^{2t})`). Assumption 7] (Comment 8) was proposed to explain the factor `−2` in `1 − e^{−2t}` for `t > 0`. The `t < 0` riddle is argued away in §4.4, formally within the axioms, by a degree-2 ramified covering `S_{Q[i]} → S_Q` at which `S_Q` has a mild singularity at `x_∞`. So OT-12 asks for a carrier that realises that singular structure; the axioms alone already accommodate it]** |
| C7 | The Morishita bridge `Ψ_F : 𝔛_F → 𝒳_F` (Deninger system → CC adelic space) sets the `p`-component to zero at points over `p`, so it cannot transport cycles | NG-107; 107_242 Thm 4.1; 114_a_03 §6.1 | PROVED (for that bridge only) |

### 2.2 On the trace formula (W-2, W-4)

| # | constraint | source | label |
|---|---|---|---|
| C8 | The prime side must be **exact** `Λ(n)`. For every class `𝒞 ∋ Λ` closed under deletion of finitely many terms (resp. amplification of one), some `a ∈ 𝒞` fails `RD_T(a)` at every `T > T_0(0) = 0.74921` (resp. `T > ½log 2`). This covers `𝒞_PNT(ε)`, `𝒞_zeros = {ζ_a = ζ·E}` (same zeros, same pole) and `𝒞_BT` | P46 `thm:finmod`, `cor:void` | PROVED |
| C9 | Quantitatively (O3), at fixed `T` with `λ^A_T > 0`, changing one weight `Λ(n₀)` by `ε > ε_* = √n₀ λ^A_T / (2|c_{F⋆}(log n₀)|)` destroys `RD_T`, and `ε_* ≤ 2·10⁹ T e^{−14.449T}/|c_{F⋆}(log n₀)|` for `T ≥ 1` (vacuous for `T ≤ 1.51`; degenerate case = Lemma D, OPEN). For the complete form, use the minimiser of `W_T` **[amended per R158_003: A7 — the change is in the direction `s = sgn c_{F⋆}(log n₀)`, with `ε ≤ Λ(n₀)` when `s = −1` (so `a ≥ 0`); it needs the OPEN non-degeneracy `c_{F⋆}(log n₀) ≠ 0`; "Lemma D" is P46 `lem:degen`]** | P46 `rem:resweights`; R157_004 §1.1, A1–A5 | PROVED (upper bound) |
| C10 | Hence the object's **axiom class** must be **rigid**: no member may carry orbit data `Λ + εδ_{n₀}`, `Λ·1_{n≥N}` or `ζ·E`. A derivation valid for every member of a class containing such data is unsound (P47 Thm 18.1(ii) schema, as used in `cor:void`) | C8 + C9 + the derivation schema | PROVED (as a method constraint) |
| C11 | The trace formula must be ζ's explicit formula **including** `m(τ)` (equivalently `C_0` and `K`, the Γ-factor) and the polar pair. `𝒞_zeros` members have ζ's zeros and pole but no functional equation (`E(s) ≠ E(1−s)`) and still fail (C8). Spectral data alone do not suffice; the archimedean term must be matched by the object | P46 `thm:finmod`(iii), `prop:finite`(iv) | PROVED |
| C12 | The polar data must be equimodular (**A3**): `Ξ_a = ξ(s+a)ξ(s−a)` satisfies A1, A2, A2⁺, A4–A9 and violates the conclusion. Infinitely many of its zeros lie on `Re s = ½ ± a` (Hardy, X16) **[amended per R158_003: A8 — "its zeros lie on" overstated; unconditionally only the images of the on-line zeros of ξ are located; P47 Prop 27.17 item 2 has the same slip]**, and Prop 12.4B turns an off-line zero into a primitive test with `I^{(a)}_∞ > 0`. So a derivation from data that `Ξ_a` shares is unsound (Restatement 12.4a) | P47 Thm 12.4, Prop 12.4B, Thm 18.14, Restatement 12.4a, Rem 12.4a′ | PROVED / RESTATEMENT (schema) |
| C13 | The object must invoke at least one of **A7** (no zero in `Re s ≥ 1`), **A8** (Euler product, `c(n) ≥ 0` on prime powers), **A9** (`Z > 0` on `R`): the Epstein `Ξ_Q` (`h(−D) > 1`) satisfies A1–A6 and A2⁺ and fails Hodge index | P47 Thm 18.10, Lemma 18.15, Thm 18.16 (T2) | METHOD-CONSTRAINT (falsifier PROVED) |
| C14 | A8 alone does not suffice: modulo (H-DMV), Beurling systems satisfy BE1–BE8 and violate `(ZFS_δ)` for every `δ > 0`. The object must use something outside BE1–BE8. The functional equation and the additive structure of `Z` (Poisson, congruences, `n ↦ n+1`) are absent from that list (Rem 27.16a) | P47 Rem 27.16 (T3), Prop 27.17 | METHOD-CONSTRAINT modulo the CITED (secondary) import (H-DMV) |
| C15 | Field uniformity: the data exist for every `ξ_K` (Thm 18.18(vi)), so a derivation from properties shared by all `ξ_K` proves GRH for every `K`. **A field-uniform object is admissible** and must be held to that standard. The A9 escape carries the Siegel-zero price | P47 Thm 18.1 (T1), Rem 18.1a, Cor 18.17; R157_004 A9 | METHOD-CONSTRAINT; CORRECTION of record (R157_007) |
| C16 | A form computed from local data alone (Euler factors, local densities `1/φ(q)`, `c_q(d)`, `log p`, `p^{−1/2}`, `Γ`) is zero-blind: it is unchanged by `ξ → Ξ_a` | P47 Prop 22.5(i),(ii), Thm 26.13, Cor 26.13a, Cor 22.9a (P122.028) | PROVED |

### 2.3 On the positive form (W-5)

| # | constraint | source | label |
|---|---|---|---|
| C17 | Not place-by-place: `Q_p(F_φ) = −v_p‖φ‖²`, and each local form is negative definite on an infinite-dimensional subspace of `P_T` for `T > ½log p` (NG-E1, strong form). Not finite-`S` or sub-comb: any contacts with total mass `A < −C_0 = 5.372…` make the primitive form negative on `P_T` for `T > T_0(A)`, and finitely supported combs fail for large `T` | R157_007 (NG-E1 proved); P47 Prop 28.4; P46 `cor:Qp`, `thm:SC`, `prop:finsupp` | PROVED **[amended per R158_003: A9 — `cor:Qp` and its following paragraph: "Indefinite summands do not forbid a positive sum … The corollary therefore gives no sign. It only rules out inferring the sign from a single local form." C17 excludes a *derivation* place by place, not a global form that is a sum of local forms. `cor:Qp` also gives `Q_p` **positive** definite on `{F⁻_φ} ∩ P_T`]** |
| C18 | No uniform margin: no `c > 0` has `λ^A_T ≥ c` for all `T` (nor `λ^W`); every lower bound lies below `4·10⁹ T e^{−15.449T}` for `T ≥ 1`. So the positivity must be **exact**, of identity type (a squared norm), and not a gap estimate. **[amended per R158_003: A10 — only "no uniform `c > 0`" and the upper bound are PROVED. The inference "must be of identity type" is HEURISTIC: `thm:margin` does not exclude a proof giving `λ_T ≥ c(T) > 0` with `c(T) → 0`]** A "gapped polarization" in the `L²(I_T)` normalisation is impossible (the NG-62b/NG-63 "gap" wish is excluded as a *theorem*, not only as a diagnostic) | P46 `thm:margin`, `cor:margin2`(i),(iii) | PROVED |
| C19 | No upward induction in `T`, and no finite truncation: nestedness gives an upper bound only (`cor:mono`, `lem:monoT`); finite-rank compressions and monotone spectral flow are closed | P46 `cor:mono`, `lem:monoT`, `thm:arena`; N5, D.53 | PROVED |
| C20 | Not termwise in the zeros: a flat-top `w` (`w ≡ 1` on `[−2T,2T]`, even, continuous, `L¹`) never has `ŵ ≥ 0`. So a certificate `f_w = Σ_ρ ŵ(τ − γ_ρ)` is never a sum of nonnegative zero contributions. Positivity can only be the **Hermitian-square** kind, `W_T(F) = Σ|F̂(γ)|²` under RH, i.e. positivity of a Gram/HS norm evaluated on `F ⋆ F̃`, never positivity of a kernel on the dual side | P46 `lem:Rrig`, `thm:Z` | PROVED (lemma); HEURISTIC (the reading "Gram, not kernel") |
| C21 | ~~Not an identity: duality holds without attainment, so no finite dual object attains `λ^P`. An MW-5 positivity cannot be a finite certificate~~ **[amended per R158_003: A11 — the struck text contradicts `thm:D1` and clashes with C18.]** No *finite dual identity*: for a finite signed `ν` on `{|u| ≥ 2T}` and finitely many annihilators, `inf_τ[s_T + ν̂ + Σβ_jĥ_j] < λ^P_T` strictly (`thm:O`), so no finite dual certificate is exact. Finite certificates **do** exist per window with value `> λ^P_T − ε`, and prove `λ^A_T > 0` whenever `λ^P_T > 0` (`thm:D1`). With C18, a positivity valid for all `T` cannot be one finite certificate. "Identity" here means a finite dual identity; it is not the Hilbert-square identity of C18/OT-7, and the flat-top certificate of `thm:Z` (infinite `ν_w`) is an identity | P46 `thm:O`, `thm:D1` | PROVED |
| C22 | Per window, the primitive and complete forms are **not** interchangeable: `λ^W_T > 0 ⟺ λ^A_T > 0 ∧ 𝔊_T ≻ 0`, and `λ^A ≥ 0 ⟹ λ^W ≥ 0` fails in comb models on `[0.4608, 0.58]` and at `½log 3` (`θ ≤ 0.8148`). E1 ⟺ E2 holds only globally. The object must say which form it delivers: (P-HS) gives the complete form, (P-HI) the primitive form | P46 `thm:parityschur`, `cor:convfail`, `prop:polarcap` | PROVED (`θ_* < 1` clause via Zhu 2026, CITED not re-verified) |
| C23 | Positivity must not factor through an `h⁰` on `D^W` with (a), (b′), (c) for any `χ` (Thm 19.25), nor on `𝒟_c = C_c^∞ ⊕ RK` or `𝒟_p = P_c^∞ ⊕ RK`, including the stable form and the finer readings (Cor 19.25b). The kill is localised to any set containing `{E_w, K − E_w}` | P47 Thm 19.25, Cor 19.25b | PROVED (given (X19), (E2), (E3d)) |
| C24 | The defect is a property of the **cone**, not of the zeros and not of the missing sections functor. It holds on a curve over `F_q`, where `h⁰` exists and RH is a theorem (Thm 21.15). Of the three substitutions, only the cone in (b′) bites: `𝓔_C = Cone{γ_n}` against `Eff(C×C)`. The missing classes are the graphs of **sums** `Γ_{m+nπ}` and the fibres: "the frame has `⋆` and no `+`" | P47 Thm 21.15, Rem 21.16a, §21.7 | PROVED |
| C25 | The bigness clause for a closed `𝓝_∞`-saturated cone with the degree gate **is** RH (Prop 21.21). The deliverable is the mechanism (P145′) (4a) sections with a scaling-invariant divisor map and `D ∈ 𝔈⊗Q`; (4b) the degree gate; (4c) bounded density over the enlarged cone. Each must be a construction with proof, and the construction must fail for `Ξ_a` and `Ξ_Q` and be field-uniform. Clause 2 (effective rulings) alone is provably insufficient (Thm 21.17) **[amended per R158_003: A12 — Thm 21.17 is PROVED for `g = 1` (the curve model) only. And (4a) ends in the bigness conclusion `⟨D,D⟩ > 0, deg D > 0 ⟹ D ∈ 𝔈⊗Q`, which is RH by Prop 21.21. So supplying (4a)–(4c) is RH-strength; it is not a filter]** | P47 Prop 21.21, §21.8 (P145′), Thm 21.17 | PROVED + OPEN (the mechanism; RH-strength) |
| C26 | Not a Deligne extraction: no `L²`-orthogonality moment extracts a single fibre beyond the trivial bound, uniformly in `k`, `|ℱ|` and the family type **[amended per R158_003: A13 — for bounds `𝔅` of Parseval type (P47 Def 27.2) valid for all `b` on `{1,…,L}` with `‖b‖_∞ ≤ 1`, in a family containing `f_0` with `ψ_{f_0} ≡ 1` or closed under the twist]** | P47 Thm 27.3 (T5), Thm 27.4, Cor 27.8; T6 | METHOD-CONSTRAINT (PROVED) |

### 2.4 On the extraction (W-6)

| # | constraint | source | label |
|---|---|---|---|
| C27 | What the object must deliver is `ψ(x) − x ≪ x^{½+ε}`, a partial-sum bound for a polar-at-zeros sequence. It is equivalent to the zero bound (Thm 27.10). Entire-at-zeros partial-sum bounds carry no zero information (Thm 27.11). Uniformity in `T` is global positivity (O1). The reopening criterion is the six clauses of §28.4: a square, positive after every twist; a polar divisor fixed by local data; zeros holomorphic to the left of it; reads phase (fails `Ξ_a`); uses `+` and `×` (fails `Ξ_Q` and Beurling); field-uniform | P47 Thms 27.10, 27.11, §28.2, §28.4; P46 `prop:uniform`; R157_002 O1 | CLASSICAL / PROVED / RESTATEMENT |

**Remark 2.1 (what the record does not constrain; `PROVED` by inspection of the labels).** No labelled statement of
the record excludes the combination (P-HS) or (P-HI) on a **two-variable** carrier (C4) that has its own effective
cone strictly larger than `𝓔` (C24) and an archimedean fixed-point structure (C5, C6), with a form defined before the
spectrum (C2). Theorem 19.25 and Corollary 19.25b are statements about functions `h⁰` on `D^W`, `𝒟_c`, `𝒟_p` and the
frame's cone (R157_004 A10). This is the MW-5 residual, stated negatively.

---

## §3 The positive list, the negative list, and the object test

### 3.1 The organising lemma

**Lemma T (the spectral construction is RH; `PROVED`, elementary).** Consider the data

 (D1) a complex Hilbert space `H¹` with a strongly continuous group `φ^t` whose generator `Θ` has discrete spectrum,
      and `H⁰ = H² = C` with `Θ = 0`, `Θ = 1`;
 (D2) the trace formula: `∫h(t) e^{tΘ}dt|_{H¹}` is trace class for `h ∈ C_c^∞(R)`, and the eigenvalues of `Θ` on
      `H¹`, with algebraic multiplicity, are the non-trivial zeros of `ζ` (Leichtnam's axiom 6], which with (D1)
      turns the Lefschetz formula into the explicit formula);
 (D3) the conformal positivity: the given inner product satisfies `⟨φ^tα, φ^tβ⟩ = e^t⟨α,β⟩` (Leichtnam axiom 5]
      with (15); Deninger Thm 2.1 with `α = 1`).

Then (D1)–(D3) are satisfiable **if and only if RH holds**, if `H¹` may be defined from the zeros.

**[amended per R158_003: A1 — corrected statement.]** *(⇒) Every realisation of (D1)–(D3), however it is
constructed, forces every non-trivial zero onto `Re s = ½`. (⇐) Under RH the spectral realisation below, defined
from the zeros, satisfies (D1)–(D3).* So (D1)–(D3), **as axioms**, are consistent exactly when RH holds; the clause
"if `H¹` may be defined from the zeros" concerns only the (⇐) witness. Label: `PROVED` (elementary); content
`CLASSICAL`: (⇒) is Serre's argument (Serre 1960), formalised in Deninger math/0204110 Thm 2.1 (read: `Θ = α/2 + S`,
`S` skew) and Leichtnam 1307.3851 §2 eq. (6) ("Therefore Deninger's formalism should imply the Riemann hypothesis …
This argument comes from an idea of Serre"), and in Leichtnam Comment 6 ("the first six Assumptions imply the
Riemann hypothesis"); (⇐) is the trivial converse of Hilbert–Pólya (Connes math/9811068 introduction; R157_002 row
32, EQUIV). **No novelty is claimed.** *Notation:* here `Φ_h(s) = ∫h(t)e^{ts}dt`; P46's `Φ_F(s) = ∫F e^{(s−½)t}dt`
is the transform against `U_t = e^{−t/2}φ^t` (used in Cor T′). *Multiplicities:* under (D3), `Θ − ½` is
skew-adjoint, hence semisimple, so algebraic and geometric multiplicities agree and a zero of order `m` needs an
`m`-dimensional eigenspace. Leichtnam's axiom 6] (`H¹⊗C = ⊕ ker(θ₁ − z_q)^{n(z_q)}`, generalised eigenspaces,
"with the same multiplicities on each side") is therefore compatible with 5] only with trivial Jordan blocks. Connes
(math/9811068 §2, after Thm 1): at a multiple zero his `D` "is not semisimple and has a non trivial Jordan form …
compatible with the almost unitary condition … but not with skew symmetry". A realisation of that kind cannot carry
(D3) as it stands, which bears on R158_002. *Trace class:* (⇐) as written is correct. `Σ_ρ m_ρ|Φ_h(ρ)| < ∞` for `h ∈
C_c^∞`, by Paley–Wiener decay uniform on the strip and `N(Γ) ≪ Γ log Γ`; the trace is Lidskii's, and it equals the
zero side of the explicit formula, which holds unconditionally. Leichtnam's 6] allows a trace "in some generalized
sense" (distributional, as in AKL). Lemma T(⇒) does not use the trace at all.

*Proof.* (⇒) By (D3), `U_t = e^{−t/2}φ^t` is unitary, so `Θ − ½ = S` is skew-adjoint and every eigenvalue has real part
`½`; by (D2) these are the zeros. (This is Serre's argument, as formalised by Deninger–Singhof and in Leichtnam §2.)
(⇐) Under RH let `H¹ = ⊕_ρ C^{m_ρ}` (orthogonal, standard inner product) with `Θ = ρ` on the `ρ`-block. For
`h ∈ C_c^∞`, `Φ_h(s) = ∫h(t)e^{ts}dt` decays faster than any power on `|Re s − ½| ≤ ½`, and `Σ_ρ m_ρ |Φ_h(ρ)| < ∞`
since `#{γ ≤ Γ} ≪ Γ log Γ`. So (D2) holds, with the Lefschetz identity being the explicit formula (Weil 1952). Since
`e^{−t/2}e^{tρ} = e^{iγt}` is unimodular exactly when `Re ρ = ½`, `U_t` is unitary and (D3) holds. ∎

**Corollary T′ (`PROVED`).** Under the hypotheses of Lemma T, with `F(U) := ∫F(t)U_t dt` and `F ∈ L²(I_T)`
(for smooth `F` by (D2); in general under absolute convergence of the zero sum, P46 `lem:roughEF`),
`W_T(F) = Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = ‖F(U)|_{H¹}‖²_{HS} ≥ 0`: the **complete** form is a Hilbert–Schmidt norm, and the
primitive form is its restriction to `P_T`. *Proof.* Under (D3), `Φ_F(1−ρ) = \overline{Φ_F(ρ)}` for real `F` and
`Re ρ = ½`; sum the diagonal of `F(U)F(U)^*` in an orthonormal eigenbasis. ∎
**[amended per R158_003: A1′ — the product formula `Σ_ρΦ_F(ρ)Φ_F(1−ρ)` is P46's expression for **real** `F`
(`prop:P`, `lem:roughEF`). For complex `F ∈ L²(I_T)`, read the middle term as `Σ_ρ Φ_{c_F}(ρ)`, with `c_F` the
autocorrelation, `= Σ_γ|F̂(γ)|²` under (D3); the identity with `‖F(U)‖²_HS` then holds as stated. `F(U)` is
Hilbert–Schmidt exactly when that sum converges, which for rough `F` is hypothesis (b) of `lem:roughEF` and is not
automatic on the form domain. The eigenvalue of `F(U)` on the `ρ`-block is `∫F(t)e^{(ρ−½)t}dt = Φ_F(ρ)` (P46
normalisation), as needed. Checked against P46 `eq:W` (l.134–138).]**

**Reading (`HEURISTIC`, supported by Lemma T and by Doc 130).** Lemma T is the Hilbert–Pólya equivalence (R157_002 row
32, EQUIV) in Deninger's coordinates. It shows that (D1)–(D3) **as axioms** carry exactly the content of RH, and that
the whole content of an MW-5 object lies in **how (D3) is obtained**. In Weil's proof (W-6) the positive form exists
for every surface and is proved without the eigenvalues. In Deninger's only realised arithmetic case (math/0204194)
the leafwise metric is built after Hasse `|ξ|² = q` is invoked (Doc 130 §2.2, quoted from source): that is the
direction Lemma T(⇐) takes, not Weil's.

### 3.2 Positive list (must have)

| P# | must have | from |
|---|---|---|
| P1 | an infinite-dimensional `H¹` with a flow or a semigroup of correspondences, `H⁰`, `H²` of rank one with eigenvalues `0, 1` (A3 built in) | W-3, C1, C12 |
| P2 | a Lefschetz formula **proved** to equal ζ's explicit formula exactly: the archimedean term `m(τ)` from a fixed-point structure, and the prime side with exact `Λ(n)/√n` at `log n`, positive multiplicities (A8) | W-4, C5, C6, C8, C11, C13 |
| P3 | a **rigid** axiom class: the defining structure forbids modified orbit data, Beurling systems, `ζ·E`, `Ξ_Q`; for `Ξ_a` it is either undefinable or visibly breaks A3 | C10, C12–C14 |
| P4 | existence for every number field `K` (a Galois-covering family `S_K → S_Q`), and hence the price: its positivity proves GRH for all `ζ_K`; no reliance on A9 unless Siegel zeros are disposed of | C15 |
| P5 | a positive-definite Hermitian form **defined from geometry prior to and independent of the spectrum**, with a **proved** compatibility with the flow: (P-HS) conformality `e^t` (complete form) or (P-HI) Hodge index on a primitive part orthogonal to a `(1,1)` polar plane (primitive form) | W-5, W-6, C2, C22, Lemma T |
| P6 | a global positivity, of Hermitian-square/identity type (a norm), valid for all `T` at once | C17, C18, C20, C21, O1 |
| P7 | if Riemann–Roch is used: a genuinely two-variable carrier with an effective cone that strictly enlarges the frame's `𝓔` by `+` classes (sums, fibres) and supplies (P145′)(4a)–(4c) as constructions | C3, C4, C24, C25 |

### 3.3 Negative list (must not have)

| N# | must not | from |
|---|---|---|
| N1 | read the zeros in its definition (spectral `H¹`, a metric fixed through `|eigenvalue|` data, a "Hasse input") | C2, Lemma T, Doc 130 |
| N2 | be a finite truncation, finite zero set, finite-rank compression or finite certificate | C1, C19, C21 |
| N3 | derive positivity place by place, from a finite `S`, from a sub-comb, or from local densities/Euler factors alone | C16, C17 |
| N4 | depend on `Λ` only through a class (PNT error term, zeros-and-pole class, upper-bound sieve class), or be stable under one-weight changes | C8–C10 |
| N5 | be definable, with the same derivation, for Beurling systems (modulo H-DMV), for `ζ·E`, for `Ξ_Q`, or for `Ξ_a` | C12–C14 |
| N6 | rest on a uniform gap or margin, or on induction in `T` | C18, C19 |
| N7 | be termwise positive in the zeros (a positive kernel on the certificate side) | C20 |
| N8 | factor through `h⁰` on `D^W`, `𝒟_c`, `𝒟_p` with (a), (b′), (c), or use the frame's cone `𝓔` in (b′) | C23, C24 |
| N9 | use a one-variable additive structure on `{Frob_n}` (the formal `Z⟨Frob_n⟩` is zero-blind) | C3, C16 |
| N10 | be a Deligne extraction or any `L²`-moment single-fibre extraction | C26 |
| N11 | live on a compact manifold with a transversal conformal flow (forces `α = 0`, no fixed points) | C5 |

### 3.4 The object test (a finite checklist, to be run before any positivity attempt)

A proposed object `𝒪` must pass every item; items are ordered so that the cheapest decisive check comes first. Each
item names the proof that must be **exhibited**, not assumed.

| OT | test | pass condition | kills (source) |
|---|---|---|---|
| **OT-1 Carrier** | Is `𝒪` constructed (not postulated), with `H¹` infinite-dimensional and `H⁰, H²` rank one, `Θ = 0, 1`? | a construction with proofs | N2; C1, C12 |
| **OT-2 Trace formula** | Is there a **proved** Lefschetz formula for `𝒪` equal to P46 `eq:W` / `thm:Z(i)` for all `h ∈ C_c^∞(R)`: archimedean term `m(τ)`, prime side `v_n = 2Λ(n)/√n`, polar pair? | theorem, with the archimedean place included | C8, C11, C13 |
| **OT-3 Definitional independence** | Does the definition of `𝒪`, and of every structure used in OT-5, avoid the zeros and every catalogued RH-equivalent (E1–E6; MW-1, MW-6, MW-7)? | inspection of the definition | N1; Lemma T |
| **OT-4 Rigidity** | Rerun the definition with `Λ + εδ_{n₀}`, `Λ·1_{n≥N}`, `ζ·E`, a DMV/Zhang Beurling system, `Ξ_Q`. Does it **fail to produce** an object satisfying OT-1, OT-2 and OT-5? | each substitution breaks a named axiom **or a named line of the positivity proof** [amended per R158_003: A14] | N4, N5; C8–C14 |
| **OT-5 `Ξ_a` gate** | For `Ξ_a`, which axiom fails? (It must: the zeros are off the line, by Hardy.) Is that axiom A3, read through `H⁰`/`H²`? | a named failing axiom | C12; Prop 12.4B + Thm 12.4 |
| **OT-5′ Prior positivity** | Is the positive form (P-HS or P-HI) defined from geometry of `𝒪` alone, and is its compatibility with the flow (conformality `e^t`, or Hodge index on the primitive part) **proved** without eigenvalue data? Would `𝒪` still exist, with the form still defined, if a zero were off the line (NC4 of Doc 119/130)? | a proof valid "whatever the position of the zeros" | Lemma T; Doc 130 §5.3; C2 |
| **OT-6 Globality** | Is the positivity global, and not *derived* as a sum of local positivities, a finite-`S` statement or a local-density Gram? [amended per R158_003: A14] | inspection | N3; C16, C17 |
| **OT-7 Exactness** | Is the positivity of identity type (a norm or an intersection-theoretic identity), needing no margin and no induction in `T`? | inspection | N6; C18, C19 |
| **OT-8 Hermitian square** | Does the positivity arise on `F ⋆ F̃` as a Gram/HS norm, and not as a termwise positive kernel on the zero side? | inspection | N7; C20 |
| **OT-9 Frame** | If a Riemann–Roch/`h⁰` route is used: is the carrier two-variable, is the effective cone strictly larger than `𝓔` (containing `+` classes), and are (P145′)(4a)–(4c) constructed? Is the route outside Thm 19.25 / Cor 19.25b / Thm 21.15? | explicit cone and mechanism | N8, N9; C3, C4, C23–C25 |
| **OT-10 Field uniformity** | Does `𝒪` exist for every number field `K`, with the same proofs, and does it avoid A9 or pay the Siegel price? | family `𝒪_K` | C15 |
| **OT-11 Form declared** | Which form does the positivity deliver, complete (`W_T`) or primitive (`𝔞_T|P_T`)? If primitive, is the polar capacity `𝔊_T ≻ 0` needed per window, or is only the global statement used? | stated | C22 |
| **OT-12 Archimedean place** | Is there a fixed-point (or equivalent) structure reproducing the Γ_R contribution for `t > 0` **and** `t < 0` (Leichtnam §4.4 riddle), on a non-manifold carrier (C5)? | proof | N11; C5, C6 |

**Remark 3.1 (on OT-5′; `HEURISTIC`).** OT-5′ is the only item that is not a filter against a proved obstruction: it
is the Weil-shaped demand itself. OT-1 to OT-4 and OT-6 to OT-12 can be checked without deciding any sign, and none of
them is RH-strength. **[amended per R158_003: A15 — two exceptions. (i) OT-9's clause "(P145′)(4a)–(4c) constructed"
is RH-strength, since (4a) ends in bigness, which is RH (Prop 21.21; C25 as amended). (ii) OT-2 is RH-strength for Connes'
adèle class space: there the global trace formula is equivalent to RH (§4, A17). The non-RH-strength part of OT-9 is
its filter part: a two-variable carrier, a cone `⊋ 𝓔`, and a route outside Thm 19.25/Cor 19.25b/Thm 21.15.]** OT-5′ is where an MW-5 object would either carry the proof or be circular. By Lemma T, an object
that passes everything except OT-3 is a Hilbert–Pólya realisation (EQUIV).

**[added per R158_003: A14] Remark 3.0 (status of each OT item).** The source of each item, with its label. "Implied"
means that a proved constraint makes the item necessary. "DESIGN" means a desideratum of the MW-5 shape, which no
theorem of record forces.

| OT | status | justification |
|---|---|---|
| OT-1 | infinite-dimensionality **implied** (there are infinitely many zeros; C1 `thm:finZ` for certificates); "constructed, `H⁰`, `H²` of rank one with `Θ = 0, 1`" **DESIGN** | the rank-one clause is Deninger's shape. That it excludes `Ξ_a` is PROVED given (D3) (see OT-5) |
| OT-2 | **DESIGN** (it is the definition of an MW-5 object); what the formula must contain is **implied** | C8, C11 (`thm:finmod`, `cor:void`, `prop:finite`(iv)), PROVED as method constraints |
| OT-3 | **implied** by Lemma T (PROVED/CLASSICAL): an object that reads the zeros has an RH-equivalent positivity and contributes nothing; the catalogue sweep is inspection | Lemma T; C2; P47 Rem 19.25c(i) |
| OT-4 | necessity of **some** break for each substitute **implied** (method constraints `cor:void`, T2, T3, Restatement 12.4a). Localising the break in an **axiom** of the definition is **stronger than the record**. Rem 12.4a′: a uniform *definition* transfers a proof, not the truth; the break may sit in a step of the positivity proof | pass condition amended: "each substitution breaks a named axiom **or a named line of the positivity proof**" |
| OT-5 | a `Ξ_a`-failing step is **implied** (Thm 12.4 + Restatement 12.4a). "That axiom is A3" is **HEURISTIC**: among A1–A9 only A3 fails for `Ξ_a` (Thm 18.14, PROVED), but an object may use axioms outside that list. Any object satisfying (D1) with rank-one `H⁰, H²` and (D3) with the single factor `e^t` excludes `Ξ_a` automatically (Lemma T(⇒) + Hardy X16). A formal `Ξ_a`-system needs `H⁰, H²` of rank 2 (`Θ ∈ {±a}`, `{1 ± a}`) and two conformal factors `e^{(1±2a)t}` on two summands. So at object level the gate is free; it bites only on the **derivation** of (D3), i.e. inside OT-5′ | PROVED (necessity, automatic pass under (D3)); HEURISTIC (A3 as *the* axiom) |
| OT-5′ | "(D3) proved, not postulated" is **implied** by Lemma T (a postulated (D3) is RH-equivalent). "Defined from geometry prior to the spectrum" is **DESIGN** (Weil's shape; Doc 130 §5.3) | Lemma T; Rem 3.1 |
| OT-6 | no *derivation* place by place, from a finite `S` or from local densities: **implied** (C16, C17). The original wording "not a sum of local forms" is **stronger than the record** (`cor:Qp`: indefinite summands do not forbid a positive sum); read "not *derived* as a sum of local positivities" | amended reading |
| OT-7 | "no uniform margin, no upward induction" **implied** (C18, C19); "identity type" **HEURISTIC** (A10) | — |
| OT-8 | "not termwise positive on the flat-top certificate side" **implied** (`lem:Rrig`); "Gram/HS norm" **HEURISTIC** (C20 label) | — |
| OT-9 | conditional on an RR/`h⁰` route. "Outside Thm 19.25/Cor 19.25b/Thm 21.15" is **implied**; "two-variable carrier" is **implied** only on the frame's radial carrier, given P122.028 (C4 as amended); "cone `⊋ 𝓔`" is **implied** in the curve model (Rem 21.16a); "(P145′)(4a)–(4c) constructed" is **RH-strength** (A12). Phase 113 O2 (NO-GO-LIST) adds: Frobenius graphs realised as the `δ_n` of the Schwartz-data class have infinite mutual intersection | PROVED parts + OPEN/RH-strength part |
| OT-10 | T1 (Thm 18.1(ii)) **implies** only a disjunction: a named property separating `ξ` from some `ξ_K`, **or** a field-uniform proof held to GRH for all `K`. The requirement "family `𝒪_K`" comes from the reopening rule P47 §28.4 clause (6) and from F4 as amended (R157_000 l.10), not from T1 alone | cite §28.4(6) for the family |
| OT-11 | **implied** (C22: `thm:parityschur`(c), `cor:convfail`) | — |
| OT-12 | **implied by OT-2**: the archimedean term `m(τ)` must be matched (C11). The fixed-point mechanism is **CITED** (Leichtnam Prop 2; §4.4 formal resolution via `S_{Q[i]} → S_Q`; A6). "Non-manifold carrier" is **CITED** (Deninger Cor 3.5 Rem 2, A5) | not independent of OT-2; kept separate as the cheapest archimedean check |

**Remark 3.2 (consistency with R157_000 F1–F5; `PROVED` by comparison).** F1 ⊂ OT-2+OT-4 (exact `Λ`); F2 ⊂ OT-7;
F3 ⊂ OT-1+OT-7+OT-8; F4 (amended) ⊂ OT-4+OT-5+OT-10; F5 ⊂ OT-9 together with N10. The object test refines the filter by
OT-3/OT-5′ (Lemma T) and OT-12 (C5, C6), which the filter did not contain.

**[added per R158_003: A16] Remark 3.3 (the reopening rule of record).** Row D is closed in the map. It reopens only
through the six clauses of P47 §28.4 (prior decision): (1) a square, positive after every twist (Rankin
sense); (2) a polar divisor fixed by local data; (3) the zero contribution holomorphic to the left of that pole; (4) it
reads phase (fails `Ξ_a`); (5) it uses `+` and `×` (fails `Ξ_Q` and every Beurling system); (6) it is uniform in the
number field. The OT list covers (4) by OT-5, (5) by OT-4 and OT-9, and (6) by OT-10, and it covers (1) only partly, by
OT-8. It does **not** contain (2) or (3). Hence **passing OT-1…OT-12 does not by itself reopen row D.** An MW-5 object
must also be checked against §28.4 (1)–(3). §28.4 is phrased for "a construction `𝒪` on the adelic square"; a
Deninger-type (P-HS) object must say what plays the role of its polar divisor and of the region to its left.

---

## §4 Known frameworks against the checklist (open literature; `CITED`)

"Read" means the text was read this review (arXiv PDF → text); "abstract" means only the abstract was read; "corpus"
means the reading is a corpus file that quotes the source. For each framework the table gives the **first failing
item** in the order of §3.4, plus other failures of record. No framework is claimed to be refutable in its future
development; each verdict concerns the framework as currently published.

| framework | what exists (CITED) | first failing item | further failures / passes |
|---|---|---|---|
| **CC, *The Arithmetic Site*** (arXiv 1405.4527, read) | a topos `N̂^×` with `N̄`, a square with Frobenius correspondences `Ψ(λ)`; Thm 4.3: `Ψ(λ)∘Ψ(λ′) = Ψ(λλ′)` for `λλ′ ∉ Q` or rational, and `= Ψ(λλ′)∘Id_ε` (the tangential deformation of the identity) when `λ, λ′` are irrational with rational product. Own words: the Weil-proof translation "would require … an adequate version of the Riemann-Roch theorem in characteristic 1" | **OT-1** (no `H¹` on the square) | OT-2 not formulated on the square; OT-5′ no form; the correspondences realise `⋆` (composition), not `+` (C24) |
| **CC, *The Scaling Site*** (1507.05818, abstract) and *Geometry of the scaling site* (1603.03191) | tropical curve over the arithmetic topos; "The Riemann-Roch formula holds and involves real valued dimensions and real degrees for divisors" (on periodic orbits) | **OT-1** at the square | the RR is on the curve (orbits), not the square; MW-5 of record: "real-valued, not integral" (NO-GO-LIST:230) |
| **CC, *The Riemann–Roch strategy / complex lift of the scaling site*** (1805.10501, read) | the strategy is exactly the Thm 12.3 shape: RH ⟺ `s(f,f) ≤ 0` on `∫f d^*u = ∫f du = 0`; `s(f,f) = D•D`, `D = ∫f(λ)Ψ_λ d^*λ`; the missing step is an RR existence statement making `D + (k)` (or `−D`) effective, which contradicts `deg = codeg = 0`. Own words: formulating RR on the square "faces a substantial difficulty… still open", namely the definition of `H¹` (as idempotent monoid), since null elements create unwanted Čech contributions | **OT-1** (no `H¹`) | **OT-9 at risk**: in P47 terms this is (b′) on the cone generated by the `Ψ_λ`. Thm 19.25/Cor 19.25b kill it on `D^W`'s nonnegative cone, and Thm 21.15 shows the gap is the cone. The strategy escapes only if its tropical effective cone on the square is strictly larger than `𝓔` and meets (P145′)(4a)–(4c): OPEN |
| **CC, RR for `Spec Z̄`** (2205.01391; MAP_5, P47 X17) | integer `dim_𝕊 H⁰(D) = ⌈(deg D + log 2)/log 3⌉ − 1_L`, logarithmic growth, Serre duality via Pontryagin | **OT-1** (curve only; no flow-`H¹` with zero spectrum) | growth type logarithmic (P47 §13.2, Finding 13.8); as `h_c` it fails (b′) (P47 Thm 19bis.19); clause (c) OPEN (U1, U2) |
| **CC, *Weil positivity and trace formula, archimedean place*** (2006.13771; MAP_5; P157_002 row 34) | positivity of `W_∞` on small intervals after a finite-codimension restriction; names "an intersection theory of divisors on the square of the Scaling Site… still in development" | **OT-2** (archimedean only) | OT-6/OT-7: archimedean positivity on `P_T` stops at `T*_{∞,P} ∈ [0.58, 0.60]` (P46 `cor:Tarch`, `thm:index`); primes necessary past `0.60` |
| **Connes' adèle class space + scaling flow** (Selecta 1999 = math/9811068, introduction read; P157 rows 31–32; phase 15 M8) | ~~trace formula = explicit formula (Connes; CITED)~~ **[amended per R158_003: A17]** the trace formula is **proved in the S-local case** (§VII); the **global** trace formula is shown equivalent to RH: "by proving positivity of the Weil distribution, we shall show that its equality with the geometric side, i.e. the global trace formula, is equivalent to the Riemann Hypothesis for all L-functions with Grössencharakter" (introduction; §VIII Thm 5). Spectral realisation as an absorption spectrum: critical zeros appear per se, non-critical ones as resonances. At multiple zeros `D` has Jordan blocks (A1) | **OT-2** (the global trace formula as a trace on the space is RH-equivalent) [amended per R158_003: A17; was OT-5′, which also fails: positivity of the trace pairing = Weil positivity, EQUIV] | the invariant measure is infinite and the spectrum continuous; the Hodge identities for Riemannian foliations need finite transverse measure and finite-dimensional basic cohomology (phase 15 M8 F1, F5). Treated in full by R158_002 |
| **Deninger's formalism as axiomatised** (surveys: *Some analogies…*, Doc. Math. Extra Vol. ICM 1998 I; *Number theory and dynamical systems on foliated spaces*, math/0204110, read; *Arithmetic geometry and analysis on foliated spaces*, math/0505354; 0709.2801, abstract; axioms as in Leichtnam 1307.3851 §4.1, read) | axioms 1]–8] (Leichtnam): 3-dimensional laminated `S_K` foliated by Riemann surfaces; closed orbits `γ_𝔓` of length `log N𝔓`; fixed points ↔ archimedean places; `H⁰ = R`, `H² = R[λ_g]` with `φ^t_*[λ_g] = e^t[λ_g]`; `H¹` infinite-dimensional; `φ^t` commutes with `⋆` and a transverse measure gives a scalar product (5]); the explicit formula as an Atiyah–Bott–Lefschetz formula (6]); archimedean orbifold trajectories (7], 8]). Leichtnam, Comment 6: "the first six Assumptions imply the Riemann hypothesis for `ζ̂_K`" | **OT-1** (the space is not constructed: "whose existence is still unknown", Leichtnam, quoted in phase 42 Doc 128:166) | **OT-5′ fails by design**: positivity is axiom 5] + (15), i.e. (D3). By Lemma T it is RH-equivalent once OT-1 and OT-2 hold. The only realised arithmetic case installs the metric from Hasse (Doc 130). Passes *structurally*: OT-5 (A3 via `H⁰`, `H²`; Serre's argument gives `Re ρ = α/2` for one conformal factor, and `Ξ_a`'s two moduli `½ ± a` cannot be produced), OT-6, OT-7, OT-8 (Cor T′), OT-10 (`S_K`, Galois coverings; Artin conjecture, Leichtnam §5), OT-12 as axioms 7]–8]. Deninger's own caveat: `(φ^t)^*g = e^t g` "might be too strong" (Leichtnam Comment 6) |
| **Deninger–Singhof, Kähler–Riemann polarization** (math/0204111; corpus Doc 130 §1, from source) | on a compact manifold with a Kähler–Riemann foliation, the reduced leafwise cohomology carries a polarizable ℝ-Hodge structure, with Hard Lefschetz and Hodge–Riemann relations, **derived** (Álvarez López–Kordyukov Hodge decomposition + Kähler–Lefschetz identities), with no zeta input | **OT-12 / OT-1** (compact manifold: conformality forces `α = 0`, no fixed points; Deninger Cor 3.5 Rem 2, C5) | the one published **derived** positivity of the right type (passes OT-5′ as a mechanism), but only in the class that cannot carry ζ's `H²` eigenvalue `1` or its archimedean place |
| **Deninger, elliptic-curve example** (math/0204194; corpus Doc 130 §2) | a 3-dimensional lamination for `E_0/F_q` from a Witt lift; RH for `E_0` "follows" from an index computation | **OT-3** (the leafwise metric `g = e^t Re(ξη̄)` is defined using Hasse `|ξ|² = q`) [amended per R158_003: A20 — re-read in source (math/0204194): `ξ, η` in the metric are tangent vectors; Hasse enters through the `H`-invariance of `g̃` and of `μ̃` under `(z, v̂, t) ↦ (ξ^{−ν}z, ξ^{−ν}v̂, t + ν log q)`. Verdict unchanged] | the proof arrow runs opposite to Weil's (Doc 130 §2.3); no archimedean place |
| **Deninger, dynamical systems for arithmetic schemes / rational Witt vectors** (1807.06400 v4 2024, read; 2508.05329; MAP_5) | for normal `X_0` flat of finite type over `Z`, infinite-dimensional ℝ-dynamical systems `X̌_0(C) ×_{Q_{>0}} R_{>0}` built from `W_rat`; compact packets of periodic orbits of length `log N x_0` ↔ closed points; connected; zeroth foliation cohomology one-dimensional. Own words: "There are no fixed points of the flow"; "the cohomological problem pointed out in [KS18] … persists"; the space is infinite-dimensional where one wants dimension `2 dim X_0` | **OT-1** (`H¹` with the zero spectrum not established) | **OT-12** (no fixed points, so no archimedean place); OT-5′ absent (no positivity anywhere in 2508.05329, MAP_5 §3); the packets are not single orbits (bijection with closed points is "a bit more involved") |
| **Morishita** (2508.15971; 107_242) | `Ψ_F : 𝔛_F → 𝒳_F`, continuous, `R_+`-anti-equivariant, Galois-equivariant; orbits `γ_p` onto circles `C_p` (Thm 3.6) | **OT-5′** (no form; not a positivity framework) | indexing dictionary only; kills the transverse `p`-adic direction (NG-107, C7) |
| **Leichtnam, laminated spaces with `p`-adic transversal** (math/0603576, abstract) | locally (disk) × `Z_p`; a Lefschetz formula for `φ^t` on leafwise Hodge cohomology resembling the explicit formula for curves over finite fields; eigenvalues of the generator on `H¹_τ` have real part `½` | **OT-2** (function-field-shaped formula, not ζ's; no archimedean term) | OT-12 fails; the "real part `½`" is internal to the model (the conformal structure is part of the construction), which is the Lemma T(⇐) direction (HEURISTIC; body unread) |
| **Álvarez López–Kordyukov–Leichtnam, trace formula for foliated flows** (2402.06671, abstract; LNM 2387, 2026) | on closed manifolds with a codimension-1 transversely oriented foliation, and a foliated flow with simple closed orbits and transversely simple preserved (compact) leaves: a Lefschetz distribution on two leafwise reduced cohomologies (conormal, dual-conormal), with a trace formula in terms of orbits and preserved leaves; "solves a conjecture of C. Deninger" | **OT-2** (not ζ's explicit formula: no arithmetic space) | OT-5′ absent (no positive form in the abstract); a closed manifold, so C5 applies to any conformal version. The analytic trace machinery exists; the arithmetic space does not (Doc 128:24) |
| **Kopei** (math/0605184, read; Abh. Math. Sem. Hamburg 81 (2011) 141–189, abstract) | a product-formula analogue for meromorphic functions on 3-dimensional foliations by Riemann surfaces with a transverse flow, on closed manifolds (`Σ l(γ_i) ord_{γ_i} f = 0`); a foliated analogue of 1- and 2-dimensional Arakelov theory (Riemann–Hurwitz-type formulas for coverings; higher-dimensional foliations "analogous to arithmetic surfaces") | **OT-2** (no explicit-formula trace for ζ) | OT-5′: no positivity in either abstract (2011 body unread, so this is CITED at abstract level). Closed manifolds, so C5 applies |
| **Borger, λ-rings and `F_1`** (0906.3146, read) | `Λ`-algebraic geometry as geometry over a deeper base; the motivation stated: `Spec Z ⊗_{F_1} Z` "a surface bearing some kind of intersection theory" to mimic Weil. Own words: "the current version of our theory says nothing about the archimedean place of `Q`, it is hard to imagine this succeeding without further ideas" | **OT-1** (no square with `H¹`/intersection theory constructed there) | OT-12 fails by the author's statement; OT-5′ absent; ring-level (NG-107 note, P157_002 row 35) |
| **Haran's arithmetical plane** (1709.05831 §10; 114_a_03 §6.2; MAP_5) | a pro-object `Spec Z ×_{F{±1}} Spec Z` containing `spec(Z ⊗_{F{±1}} Z)`, the only literal square | **OT-1** (no `H⁰`, no cohomology, no RR) | OT-5′ absent |
| **Arakelov / Faltings–Hriljac** (classical; P157_002 row 36; P122.007; phase 15 M3/M10) | an arithmetic Hodge index theorem on arithmetic surfaces `X → Spec O_K` (Faltings 1984, Hriljac 1985): a **derived** positivity | **OT-2** (no trace formula relating Arakelov intersection numbers to ζ's zeros; heights ≠ zeros) | the needed square does not exist: `Spec Z` is terminal, `Spec Z ×_{Spec Z} Spec Z = Spec Z` (P47 Thm 22.17, C3); import excluded (P122.007). Deninger (math/0204110 §4) pairs `χ_Ar(O_{spec o_K}) = −log|d_K|` with Connes' foliation Euler characteristic, which is an Euler-characteristic dictionary and not a positivity |
| **Tropical Hodge index / Hodge–Riemann** (Cartwright 1506.02023; 2007.07826; MAP_5 §§1, 3) | derived Hodge index (at most one positive eigenvalue) on tropical surfaces; Hodge–Riemann for Bergman fans | **OT-2** (not attached to ζ) | Cartwright: positive self-intersection is a *hypothesis* ("an analogue … of a projectivity or Kähler hypothesis"); a stand-in, not an object |

**Summary of §4 (`CITED` for the entries, `PROVED` for the tallies by inspection of the table).** 18 frameworks.
First failures: OT-1 in 9 (arithmetic site, scaling site, RR strategy, RR `Spec Z̄`, Deninger formalism, Deninger
`W_rat` systems, Borger, Haran, and Deninger–Singhof jointly with OT-12); OT-2 in 7 (Connes' adèle class space, CC
archimedean, Leichtnam `p`-adic, AKL, Kopei, Arakelov, tropical); OT-3 in 1 (Deninger elliptic); OT-5′ in 1
(Morishita). **[amended per R158_003: A17 — Connes moved from OT-5′ to OT-2; total still 18.]** **Derived positivity** appears only in Deninger–Singhof (compact manifolds: fails OT-12/C5), Faltings–Hriljac
(no square over `Spec Z`: fails OT-2/C3) and tropical Hodge theory (not ζ: fails OT-2). **Postulated positivity**
appears in Deninger's formalism (axiom 5]), which by Lemma T carries the content of RH. **Installed positivity**
(metric fixed through eigenvalue data) appears in Deninger's elliptic example. ~~No published framework has a
two-variable carrier with an enlarged effective cone (P7/OT-9) together with an archimedean fixed-point structure
(OT-12). That conjunction is the precise MW-5 residual, and it is `OPEN`.~~
**[amended per R158_003: A18 — the struck conclusion is too strong. "No published framework" rests on the 18 surveyed
here. OT-9 is conditional on an RR route, so OT-9 ∧ OT-12 is not the residual of the (P-HS) route. The conjunction is
necessary on one route and nowhere shown sufficient. And §0 already names OT-5′ as the whole content.]** Restated:
*among the eighteen frameworks surveyed here, none has, on the RR route, a two-variable carrier with a cone `⊋ 𝓔`
together with an archimedean fixed-point structure (OT-9 ∧ OT-12); none has, on the conformal route, a constructed
carrier with a proved, not postulated, conformal form together with the archimedean place (OT-1 ∧ OT-5′ ∧ OT-12). The
MW-5 residual is OT-5′ on a carrier that passes OT-1, OT-2 (hence OT-12) and, on the RR route, OT-9, subject to the
reopening clauses P47 §28.4 (1)–(6) (Rem 3.3). It is `OPEN`, and it is RH-strength: an object passing it proves RH by
Lemma T(⇒), resp. Prop 21.21. The survey is not exhaustive and excludes no future development.*

---

## §5 What this sheet asks of R158_002 and of the audit

1. **R158_002 (adèle class foliation).** Run OT-1, OT-2, OT-3, OT-5′ and OT-12 on the candidate first. By §4 row
   "Connes", ~~OT-2 is available in the literature (CITED)~~ **[amended per R158_003: A17]** the S-local trace
   formula is available (CITED), the global one is RH-equivalent (Connes, introduction and §VIII Thm 5), and OT-5′ is
   the Weil positivity (EQUIV) unless the transverse
   Hodge `⋆` or Kähler form is defined **without** the spectrum and its conformality with factor `e^t` is **proved**.
   Phase 15 M8 (F1, F5) records that the foliation-Hodge hypotheses (finite transverse measure, finite-dimensional
   basic cohomology) fail for the scaling foliation as it stands, so the first item to settle is which cohomology
   (leafwise reduced, conormal/dual-conormal à la AKL) replaces them. `OPEN`.
2. **Audit points.** (i) Lemma T(⇐): check trace-class and multiplicity conventions (algebraic vs geometric; Leichtnam
   6] uses generalised eigenspaces). (ii) The A3 reading of `H⁰, H²` in OT-5 (W-3) is `HEURISTIC` beyond Deninger's
   Thm 2.1; state exactly what `Ξ_a` would need: two conformal factors, or a non-conformal flow. (iii) The §4 entries
   read at abstract level only (Scaling Site, Leichtnam `p`-adic, AKL, Kopei 2011) must not be upgraded without the
   bodies. (iv) The identification (P-HI) ⟷ primitive form, (P-HS) ⟷ complete form rests on `I_∞ = 2Φ(0)Φ(1) − W` and
   Cor T′; check signs against P47 (11.6) and P46 `eq:W` (the P46 definitions, per the process rule).
3. **No sign claim.** Nothing here moves the table of the reduced statement §3. Row D: no label.

## Sources (open literature, this review)
* A. Connes, C. Consani, *The Arithmetic Site*, arXiv:1405.4527 — https://arxiv.org/abs/1405.4527
* A. Connes, C. Consani, *The Scaling Site*, arXiv:1507.05818 — https://arxiv.org/abs/1507.05818
* A. Connes, C. Consani, *Geometry of the scaling site*, arXiv:1603.03191 — https://arxiv.org/pdf/1603.03191
* A. Connes, C. Consani, *The Riemann–Roch strategy, complex lift of the Scaling Site*, arXiv:1805.10501 — https://arxiv.org/abs/1805.10501
* C. Deninger, *Number theory and dynamical systems on foliated spaces*, arXiv:math/0204110 — https://arxiv.org/abs/math/0204110
* C. Deninger, *Analogies between analysis on foliated spaces and arithmetic geometry*, arXiv:0709.2801 — https://arxiv.org/abs/0709.2801
* C. Deninger, *Arithmetic geometry and analysis on foliated spaces*, arXiv:math/0505354 — https://arxiv.org/pdf/math/0505354
* C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv:1807.06400 — https://arxiv.org/abs/1807.06400
* C. Deninger, *Rational Witt vectors and associated sheaves*, arXiv:2508.05329 — https://arxiv.org/pdf/2508.05329
* M. Morishita, arXiv:2508.15971 — https://arxiv.org/pdf/2508.15971
* E. Leichtnam, *On the analogy between L-functions and Atiyah–Bott–Lefschetz trace formulas for foliated spaces*, arXiv:1307.3851 — https://arxiv.org/pdf/1307.3851
* E. Leichtnam, *Scaling group flow and Lefschetz trace formula for laminated spaces with p-adic transversal*, arXiv:math/0603576 — https://arxiv.org/abs/math/0603576
* J. A. Álvarez López, Y. Kordyukov, E. Leichtnam, *A trace formula for foliated flows*, arXiv:2402.06671 — https://arxiv.org/abs/2402.06671
* F. Kopei, *A remark on a relation between foliations and number theory*, arXiv:math/0605184 — https://arxiv.org/abs/math/0605184
* F. Kopei, *A foliated analogue of one- and two-dimensional Arakelov theory*, Abh. Math. Semin. Univ. Hambg. 81 (2011) — https://link.springer.com/article/10.1007/s12188-011-0061-4 (abstract only)
* J. Borger, *Λ-rings and the field with one element*, arXiv:0906.3146 — https://arxiv.org/abs/0906.3146
