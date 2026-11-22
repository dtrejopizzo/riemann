# R158_002 — Phase 158: the adèle class space as a candidate MW-5 object

Pure mathematics, no computation, no sign claim. Row D has no label and this file does not change
that. Labels: `CITED` (read in source this review, with the place), `CITED (corpus)` (a corpus file quoting the
source), `PROVED` (proved here, elementary unless stated), `RESTATEMENT`, `ANALYSIS` (argued, not a theorem), `OPEN`.
The form is always stated: **complete** = `W_T ≥ 0` on `L²(I_T)` (P46 `eq:W`, E1); **primitive** = `𝔞_T ≥ 0` on
`P_T` (E2).

---

## §0 Verdict

The adèle class space `X = A_Q/Q^×`, with the scaling flow and Meyer's nuclear function spaces, **is an object**. It
carries unconditionally almost all of Deninger's data. It has an `H¹` (the cokernel of Connes' map `E`, which is
Meyer's `H⁰_-`, and which is CCM's `H¹(A/K^×, C_K)`). It has a flow generator `Θ` whose spectrum on `H¹`, with
algebraic multiplicity, is the set of non-trivial zeros. It has a rank-2 `H⁰_+` on which `Θ = 0` and `Θ = 1`. Its
trace formula *is* the explicit formula, and it is proved. It has a Poincaré-type duality, a Rosati involution, and a
transverse measure that the flow scales by `e^t`. All of these are `CITED`. ~~In the vocabulary of R158_001 it passes
OT-1, OT-2, OT-3 (for `H¹`), OT-4, OT-5 (`Ξ_a` and `Ξ_Q` cannot be defined on it), OT-10 and OT-12. **It fails only
OT-5′, and on `X` OT-5′ is exactly Weil's criterion.**~~ **[amended per R158_004: A1]** In the vocabulary of R158_001:
* **OT-2 depends on the realisation.** On Connes' Hilbert-space realisation (`L²_δ`, `L²` with cutoff) OT-2 **fails**:
  Connes proves the S-local trace formula (Thm 4); the global one is equivalent to RH (introduction; §VIII Thm 5, proved
  in positive characteristic and stated by analogy for number fields). On Meyer's nuclear `H¹` (CCM Thm 6.1) a trace
  identity is proved unconditionally: Meyer's character identity `χ(ρ) = W` on his virtual representation. Equating it
  with the spectral computation recovers the classical explicit formula (Meyer, §1). It is not Connes' global Hilbert
  trace formula, and it costs Hilbert structure (R158_003 A17; corpus D.191: the critical Plancherel completion of the
  cokernel is zero).
* **OT-4 passes by a named line, not by undefinability.** The adelic `X` cannot be formed for `Ξ_Q`. But the nuclear
  quotient that carries every lemma of §4.6–4.7 can be (lattice Poisson summation), and those lemmas hold for it
  verbatim. For `Ξ_Q` the break sits in the Euler-product line of Meyer's character computation, i.e. in OT-2.
* **OT-5 passes vacuously** and excludes nothing by itself. It bites only on the derivation of the form, inside OT-5′
  (R158_001 OT-5 row).
* **OT-3** passes for `H¹` but **not** for Construction C's `⋆`, which is defined through the spectral splitting.
* OT-1, OT-10 and OT-12 pass as stated.
So `X` fails OT-2 in Connes' realisation. In Meyer–CCM's realisation it passes OT-2 and fails OT-5′, and there OT-5′ is
exactly Weil's criterion. Seven statements make this precise:

* **Lemma A** (`PROVED`). `X` has no leafwise `H¹` in the Álvarez López–Kordyukov/Deninger sense. The foliation of
  `C_Q` transverse to the flow has profinite leaves, and the orbit foliation has flow-invariant `H¹`. The zeros live in
  a *relative* group, the cokernel of the restriction from `X` to `C_Q`, so Deninger's leafwise `⋆` has no carrier.
  **[amended per R158_004: A2 — PROVED on `C_Q` for the two natural foliations, and (ii) holds for every coefficient
  space (Cartan's formula). "On `X`" is ANALYSIS: no leafwise complex on `X ∖ C_Q` is defined in the sources. The
  relative-group reading is CCM §5's analogy (CITED), not a consequence of (i)–(ii).]**
* **Lemma D** (`PROVED`). ~~The only involution intrinsic to `X` that is compatible with the duality is the
  functional-equation map `σ`, induced by Fourier.~~ **[amended per R158_004: A3 — uniqueness is not proved and is
  struck. Complex conjugation is another intrinsic involution: it is antilinear and commutes with `Θ`.]** The
  functional-equation map `σ` (Meyer's `J`; its range-stability comes from Fourier via Poisson) **anti-commutes** with
  `Θ − ½`. This is the phase-63 finding (MAP_3 l.33), obtained as an identity rather than a measurement, **[A3]** once
  phase 63's `J = σ∘(i⋆)` is factored (§4.6).
* **Construction C** (`PROVED`). A flow-commuting Hodge `⋆` does exist on `H¹_alg`, unconditionally. It is the Riesz
  splitting by the sign of `Im ρ`, which is available because `ξ` has no real zeros.
* **Lemma E** (the polarization lemma, `PROVED`). Every ~~`Θ`-compatible duality~~ **[amended per R158_004: A4]**
  alternating, real, `Θ`-compatible duality on `H¹_alg` (all zeros simple) has the form `B_Φ`, a residue pairing twisted
  by an even real entire multiplier `Φ`. **[A4]** Symmetric compatible forms are `B_Φ` with `Φ` odd. CCM's trace form
  is one of them: it is `B_{ξ′}(a, ā′)`. Its Hodge–Riemann form `iB_Φ(a, ā)` on `H^{1,0}` is definite **iff** RH holds,
  all zeros are simple, and `sgn(Φ(½+iγ)Ξ′(γ))` is the same at every zero. **[A4]** The necessity of "RH ∧ SZ" uses
  only compatibility, so it holds for every compatible hermitian form. It is Lemma U's argument, i.e. classical.
  * (E-i) For the canonical multiplier `Φ ≡ 1` (Grothendieck–Serre residue duality on `𝒪/(ξ)`), the form is
    **indefinite, unconditionally**. ~~This needs only the verified simplicity of `γ₁, γ₂`.~~ **[amended per R158_004:
    A5]** No verified zero is needed: Lemma E and the sign alternation of `Ξ′` at consecutive simple real zeros suffice.
  * (E-ii) For `Φ₀ = (s−½)ξ′(s)`, the pairing is the explicit-formula (log-derivative) pairing. It can be written
    from primes and Γ-data alone. Its form is **semidefinite ⟺ RH** (`RESTATEMENT`).
* **Proposition H** (`PROVED`). A definite multiplier must have an odd zero on the critical line in every gap between
  consecutive zeros. So it has infinite exponential type, and no finite-window datum polarizes `X` (Paley–Wiener).
* **Lemma U** (`PROVED`). A positive-definite inner product on `H¹_alg` that makes `e^{−t/2}φ^t` unitary (Deninger's
  Theorem 2.1 structure) exists **⟺ RH ∧ all zeros simple**. This is *strictly stronger* than RH as far as is known. It
  is an artefact of the cyclicity of `X`'s `H¹`. **[amended per R158_004: A6 — the content is CLASSICAL. It is Serre's
  argument (Leichtnam 1307.3851 §2 eq. (6), Comment 6; corpus 114 D.37 Thm 2.1, §4; 106.157 (18)) together with Connes
  1999's remark after Thm 1: at multiple zeros `D` "has a non trivial Jordan form … compatible with the almost unitary
  condition (22) but not with skew symmetry". The only new step is elementary linear algebra. No novelty is claimed. Over
  a non-abelian Galois field, "strictly stronger" becomes "false" (§4.7, A20).]**
* **Proposition B** (`CITED` + dictionary). Hodge index on the square `X × X` (CCM Prop. 7.2) and Rosati positivity
  (CCM Cor. 6.3) are Weil's criterion. For Ẑ^×-invariant tests supported in `e^{I_T}` they give the complete form
  `W_T`. Restricted to degree = codegree = 0 they give the primitive form. ~~They are P47 (18.2), i.e. E6.~~
  **[amended per R158_004: A7 — over `Q`, CCM (7.6) is `W_T(F) ≥ 0` test by test, i.e. E1, because
  `Δ•Δ = −log|a| = log D = 0`. It is Castelnuovo's form, Hodge index against the two fibre classes (degree and
  codegree). It is **not** P47 (18.2), which is Hodge index against `K` and reads `W(F) ≥ −½(Φ_F(0)−Φ_F(1))²` test by
  test, weaker per test. The two agree only globally (both ⟺ RH).]**

**Verdict: (ii). On `X`, every positivity structure on the list of §4 is one of four things:**
* **proved but not transferring** (compressions; the `L²_δ` unitarity, which sees only critical zeros);
* **a restatement of RH** (the trace pairing, Rosati, Hodge index, `B_{Φ₀}`);
* **a restatement of RH ∧ SZ** (unitarity, definite polarizations);
* **false** (the canonical residue polarization).

Label: **`RESTATEMENT` (on `X`)**. The component lemmas are `PROVED`, and exhaustiveness of the list is `ANALYSIS`.
**[amended per R158_004: A24 — the label stands.]** Lemma U, and the RH ∧ SZ half of Lemma E, are `PROVED`
(elementary), content `CLASSICAL`. Fact 4.6a.7 is corrected (A16). Prop B's matching is corrected (A12): E1 test by
test, not E6. The list gains five rows (A23), none of which escapes.
No one-round test lemma of type (i) survives. §5 names what a different object would have to add:
* a polarization that is definite for a reason prior to the spectrum (a harmonic L² norm on leaves of real dimension
  ≥ 2, or a *count*);
* a non-cyclic `H¹` (a correspondence algebra with `+`);
* global, infinite-type data.

---

## §1 Corpus check (done first, working rule)

Grep over `03-research/`, `04-papers/`, `05-meta-and-planning/` and `00-references/` for: Deninger, NG-107,
Morishita, foliat, Álvarez, Kordyukov, Meyer, "spectral realization", "adele/adèle class", "scaling action", and
Connes trace formula. Findings used below:

| source | what it says | use here |
|---|---|---|
| `phase-42-hodge-dynamics/128-deninger-s-program-is-this-the-missing.md` | Deninger route declared non-circular, verdict (a) | superseded by Doc 130 |
| `phase-43-hodge-foliated-specZ/130-circularity-to-destruction-test-of-deninger-s.md` §§0–5 | verdict (a) → **INDETERMINABLE, biased to CIRCULAR**. In math/0204111, Kähler–Riemann ⇒ polarization is pure geometry. In math/0204194 the leafwise metric uses Hasse `|ξ|²=q`. ENUNCIADO-MÍNIMO-130: a polarization built without the zero locations | Lemma E is the `X`-version of that test (§4.6) |
| `phase-43…/129-does-the-foliated-space-of-spec-admit.md` VEREDICTO-129.A/B | the leaves of the Morishita/Deninger spaces are not complex (transversal dimension 0), and the dimension mismatch is curve vs surface | agrees with Lemma A (not re-verified for 2508.15971) |
| `phase-40-close-G1/124-connes-consani-s-weil-positivity.md` §0 | CC's positivity is **spectral** (circular); intersection positivity on `NS(X×X)` is the good kind; the ingredient is absent | Proposition B |
| `phase-63-lefschetz-realization/README.md` l.30–52, `R1-VERDICT.md` | the scaling generator anti-commutes with `J`, ratio 2.000, where `J` flips `n → −n`; `F_q` control: `[F,J] = 0`; `D²` gapless | Lemma D, Construction C |
| `phase-64-connes-route/` (MAP_3 l.30) | canonical-system route, `L1 ⟺ RH` | row 4.1 |
| `phase-136-row-d-map/MAP_5`, `MAP_1:59` | MW-5 "UNBUILT (not proved impossible)"; CC Jacobian/RR carry no `h⁰` growth | §4.4 |
| `phase-145…/CORPUS_CHECK_R145.md` l.15–40, 135–161 | the `F_q` controls; do not reuse Deninger's metric as an independent input | §5 |
| `phase-157…/R157_002` rows 9, 18, 32, 34, 35, 37, 60; `R157_004` rows 35–37, M5, M6 | compressions and semilocal EXCL (F3); Hilbert–Pólya (Connes adèle class) EQUIV; the MW-5 cluster NOT EXCLUDED | §4 table |
| `phase-158…/R158_001` (parallel) Lemma T, OT-1…OT-12, §5.1 | asks R158_002 to run OT-1, OT-2, OT-3, OT-5′, OT-12 on `X`; audit point (i): algebraic vs geometric multiplicity | Lemma U answers (i); §0 runs the OT list |
| P47 §§11–12, 18, 19.7–19.9, 20.8, 21.7 | the frame `D^W, K, deg, 𝓝_∞, I_∞`; T1, T2 (A1–A9); frame defect Thm 19.25 and Cor 19.25b; the ray, Thm 20.37; Thm 20.38 (W1) "`W` is a norm iff RH"; §21.7 "the frame has `⋆` and no `+`", "must deliver the count, never the positivity" | §§3–5 |
| P46 `eq:W`, `thm:Z`, `thm:finZ`; P46 remark at l.2505 on CC 2021 | forms E1/E2, certificates, finite zero sets carry no certificate | Proposition B, Proposition H |
| **[added per R158_004: A8 — missed by the corpus check]** `phase-106…/106_157_CCM_GLOBAL_ROSATI_PSEUDO_POLARIZATION.md` §§3–7, `106_156` | the CCM hermitian trace form `𝔥([f],[g]) = τ(f*g^♯)` on the cokernel, its radical, the complex structure `J = i`, `Θ^†+Θ = I` (18); "an indefinite Hermitian form also satisfies (8), (13), (17), (18)"; the positivity gate (21) | Construction C (precedent), Fact 4.6a, Lemma E (the CCM form is `B_{ξ′}`), Lemma U |
| **[A8]** `phase-114…/114_d_37_POLARIZED_MEYER_COKERNEL_THEOREM.md` Thm 2.1, §4 | on Meyer's quotient: a compatible positive polarization ⇒ `t^{−1/2}λ_t` unitary ⇒ RH (Serre) | Lemma U, (a)⇒RH |
| **[A8]** `phase-114…/114_d_39_…MEYER_FOURIER_J_NOGO.md` §§3–6 | Meyer's `A = 𝓕J` has multiplier `γ(s)` and does **not** descend to `𝓗_-/Z𝓗_∩`; `(Jf)^(s) = f̂(1−s)` | Lemma D (the realiser of `σ` is `J`, not `J𝓕`) |
| **[A8]** `phase-114…/114_d_191_…PLANCHEREL_NO_GO.md` | the critical Plancherel completion of the cokernel is zero; the algebraic cokernel is non-Hausdorff | doubt 2, §4.1 |
| **[A8]** `phase-107…/107_204_MEYER_NUCLEAR_CONTINUATION_BRIDGE.md` | "Meyer supplies the nuclear continuation bridge, not Hodge positivity" | §2.4 |
| **[A8]** `phase-64-connes-route/RESULTS.md` Task D (l.33–47); `MAP_1` NG-63 | the parity lemma for `J e_n = sgn(n)e_{−n}`: J-linear ⟺ even symbol; NG-63 scoped "for this specific construction" | Lemma D, Construction C |

Local sources read this review: Connes, *An essay on the Riemann Hypothesis* (arXiv 1509.05576,
`00-references/papers-nuevos/A/`); Connes–Consani, *The Riemann–Roch strategy* (1805.10501, same place); Meyer
(math/0412277, `papers-nuevos/C/`); Deninger (math/0204110 and 1807.06400, `papers-nuevos/B/`); Morishita (2508.15971,
`papers-nuevos/Puente/`); CC (2006.13771, `phase-137…/cc_2006.13771_text.txt`). Fetched from arXiv this review:
Connes (math/9811068) and CCM (math/0703392), both as full text.

---

## §2 The object, as precisely as the literature allows (deliverable 1)

**2.1 The space and the flow** (`CITED`). For a global field `K`: `X_K = A_K/K^×`, with `C_K = A_K^×/K^×` acting by
multiplication (Connes 1999, Introduction and §III; essay 1509.05576, Def. "adele class space", l.700–716). For
`K = Q`, `C_Q ≅ Ẑ^× × R_+^*`, and the **scaling flow** is `R_+^* ⊂ C_Q` acting at the archimedean component. Connes
(1999, Remark c, §VIII) asks for the relation of `X` "with the hypothetical arithmetic site of Deninger". Deninger
(math/0204110, Introduction) calls the two approaches "superficially related … deeply different". Deninger
(1807.06400, the map (61)) constructs `Q^{>0}`-equivariant maps from his spaces to `A_f × R^{>0}`, and asks whether
the noncommutative point of view applies. Morishita (2508.15971, Thm 3.6) relates the `R_+`-orbits of the two sides.
None of these sources puts a cohomology or a positivity on the bridge.

**2.2 The foliated reading** (`PROVED` for Lemma A; the structure itself is `CITED`). Deninger's dictionary
(math/0204110 §§2–4) needs:
* a (laminated) space with a codimension-one foliation `𝓕` transverse to the flow;
* leafwise cohomology `H̄^•_𝓕` (Álvarez López–Kordyukov: `Ker Δ_𝓕 ≅ H̄^n_𝓕`, math/0204110 (2));
* a leafwise Hodge `⋆_𝓕`, giving a scalar product `(h,h') = tr(h ∪ ⋆_𝓕 h')` (math/0204110 (4));
* in Theorem 2.1 (3-manifolds, surface leaves): a flow conformal on `T𝓕` with factor `e^{αt}`, which gives
  `Θ = α/2 + S` with `S` skew on `H̄¹_𝓕`. Positivity comes from the L² norm of harmonic forms. The content is that
  the flow commutes with `⋆_𝓕`.

**Lemma A (no leafwise `H¹` on `X`; `PROVED`).**
(i) On the open stratum `C_Q = Ẑ^× × R_+^*`, the foliation transverse to the flow has as leaves the fibres
`{|x| = u} ≅ Ẑ^×`. These are profinite, of real dimension 0. So the leafwise de Rham complex (functions locally
constant along leaves, in Deninger's sense, 1807.06400 §10, Def. t101) is concentrated in degree 0, and `H^1_𝓕 = 0`.
(ii) For the orbit foliation (leaves = `R_+^*`-orbits), take Schwartz coefficients. Then `H^1 = S(C_Q)/x∂_x S(C_Q)`
is identified, by integration along orbits, with functions on the transversal `Ẑ^×`, and the flow acts trivially on
it. So no zero of `ζ` occurs in it.
(iii) Hence the space carrying the zeros is not a leafwise cohomology of either foliation. It is the cokernel of the
restriction from `X` to its open stratum `C_Q` (2.4 below), i.e. a relative group of the pair `(X, C_Q)`, supported
on the degenerate adèles `X ∖ C_Q`.

*Proof.* (i) A function on a profinite leaf that is locally constant is a 0-form, and there are no 1-forms along a
0-dimensional leaf. (ii) On one orbit `R_+^* ≅ R`, the map `f ↦ ∫f d^*x` identifies `S(R)/∂S(R)` with `C`, since
`∂: S → S` has image `{∫ = 0}`. Fibrewise over `Ẑ^×`, this is an isomorphism with functions of the transversal, and
`φ^t` acts trivially because `∫f(λx)d^*x = ∫f d^*x`. (iii) is the definition in 2.4 (Connes 1999 Thm III.1; CCM
§4–5), and CCM §5 interpret it as primitive (vanishing) cohomology of the complement. ∎

**[amended per R158_004: A9]**
* **(ii) holds for every coefficient space** (this answers doubt 7). Let `V` be the generator of the flow; it is
  tangent to the orbit leaves. In any leafwise complex stable under `V` (Schwartz, smooth, tempered, conormal or
  dual-conormal, reduced or not), Cartan's formula gives `L_V[g dt] = [(Vg)dt] = [d_𝓕 g] = 0` on `H¹`, and `L_V = 0` on
  `H⁰ = ker V`. So `Θ = 0` on the orbit-foliation cohomology, whatever the coefficients. Only the *size* of `H¹`
  (`C^{Ẑ^×}`-type, or `0` with tempered coefficients) depends on the choice. `PROVED`.
* **(i) and (ii) are statements on `C_Q`.** On `X ∖ C_Q` no leafwise complex is defined in the sources read, so
  "`X` has no leafwise `H¹`" is `ANALYSIS` beyond `C_Q`.
* **(iii) is CCM's analogy** (§5, `CITED` as an analogy). In that analogy `C_K` plays the role of the hypersurface
  `Y`, and `H¹ ⊆ H_c(U)` with `U` the complement. "Open stratum" (i) is this file's wording; it is not CCM's. (iii) is
  not a consequence of (i)–(ii).

Consequently, a Deninger `⋆_𝓕` acting on leafwise 1-forms has no carrier on `X`. Any `⋆` has to be built on the
cokernel, which is what §4.6 does. Connes–Consani say the same in their own terms (1805.10501 l.887): "the
self-intersection … appears as a trace taken in a relative situation … `(Tr_X − Tr_Y)(π(f))` … the spectral
realization as a cokernel of `E: 𝓕(X) → 𝓕(Y)`".

**2.3 The function spaces** (`CITED`).
* **Hilbert, `δ > 1`** (Connes 1999, §III). This is `L²_δ(X)_0`, the completion of `S(A)_0 = {f(0) = 0, ∫f = 0}` in
  the norm `∫_{C_K}|Σ_{q∈K^×}f(qx)|²(1+log²|x|)^{δ/2}|x|d^*x` (essay l.720–735).
* **Hilbert, `δ = 0`, with cutoff** (Connes 1999, §VIII). This is `L²(X)`, with projections `P_Λ, P̂_Λ` and the
  subspace `B_Λ` spanned by `f` with `f, f̂` vanishing for `|x| > Λ`. At the real place the prolate functions of
  Landau–Pollak–Slepian enter (§VIII, eq. (31)–(32)).
* **Nuclear** (Meyer math/0412277, §§2–4). Nuclear Fréchet spaces `𝓗_+, 𝓗_-, 𝓗_∩, 𝓗_∪` of functions on `R_+^*`, with
  the Zeta operator `Zf(x) = Σ_{n≥1}f(nx)` (Def. "Zeta operator"). Meyer sets `𝓗⁰_+ = 𝓗_+/𝓗_∩`,
  `𝓗⁰_- = 𝓗_-/Z𝓗_∩`, with the regular representation.
* **Cyclic** (CCM math/0703392, §4). `S(A_K)_0 → S(C_K)`, the cyclic module `H¹(A_K/K^×, C_K)` (their Def. 4.10), and
  the actions `ϑ_a` on `S(A_K)_0` and `ϑ_m` on `S(C_K)`.

**2.4 The cohomology candidate and the zeros** (`CITED`).
* **The map `E`** (Connes 1999, §VIII (18)): `E(f)(g) = |g|^{1/2}Σ_{q∈k^*}f(qg)`, a surjective isometry
  `L²(X)_0 → L²(C_k)` at `δ = 0`, with `EU(a) = |a|^{1/2}V(a)E`. In the nuclear setting the role of `E` is played by
  `Z` (Meyer); CCM (Thm 4.16, Lemma 4.17) use the range `V` ("trivial correspondences").
* **`H¹`, the critical-only version** (Connes 1999, **Theorem 1**). For `δ > 1` the generator `D_χ` on the cokernel
  sector `H_χ` "has discrete spectrum, `Sp D_χ ⊂ iR` is the set of imaginary parts of zeros of the L function … which
  have real part equal to ½", with multiplicity "the largest integer `n < (1+δ)/2`, `n ≤` multiplicity". The unitarity
  is built into the weight: `‖W(g)‖ = O(log|g|)^{δ/2}`, eq. (22).
* **`H¹`, all zeros** (Meyer, Thm "Lap_range" and Cor "Dminus_eigenvalues"). Under Laplace transform, `𝓗_-` becomes
  `𝒪` := entire `h` with `t ↦ h(s+it)` Schwartz for every `s`. `Z𝓗_∩` becomes `I` := the `h ∈ 𝒪` with `h/ζ(s)`
  Schwartz on lines `Re s ≥ ½` and `h/ζ(1−s)` on `Re s ≤ ½`. `D_-` becomes multiplication by `s`. The eigenvalues of
  `ᵗD_-` are exactly the zeros of `ξ`, and "the algebraic multiplicity … is the zero order", realised by the
  functionals `h ↦ h^{(j)}(ρ)`, `j < m_ρ`.
* **`H⁰_+`** (Meyer, §4). `𝓗⁰_+ ≅ C(x⁰) ⊕ C(x¹)`, with `D_+ = diag(0,1)`, "a spectral interpretation for the two
  poles". This is Deninger's `Θ = 0` on `H⁰` and `Θ = α = 1` on `H²` (math/0204110 Thm 2.1).
* **CCM** (Thm 4.16) show `Tr(ϑ_m(f)|H¹) = Σ_{L(χ̃,ρ)=0} f̂(χ̃,ρ)` and remark "unlike in [10] all zeros contribute …
  with their natural multiplicity. This follows from the choice of function space as in [32] [Meyer]". CCM §5 read
  `H¹` as "a noncommutative version of a primitive cohomology".

**[amended per R158_004: A10 — notation]**
* **Two different `ξ`.** Meyer's `ξ` (his (1.1)) is `π^{−s/2}Γ(s/2)ζ(s)`, with poles at `0` and `1`; his
  `ord_ξ` is positive at the poles. This file's `ξ` is Riemann's entire `½s(s−1)π^{−s/2}Γ(s/2)ζ(s)`. The non-trivial
  zeros and their orders agree. The pole terms of the explicit formula are present with Meyer's `ξ` and absent with the
  entire one.
* **Meyer's eigenvalue statement is about the transpose.** Cor "Dminus_eigenvalues" concerns `ᵗD_-` on
  `(𝓗⁰_-)′`. The eigenvectors *in* `H¹` used below are Fact 2.4a's, proved here.
* **Conventions checked.** `λ_t f(x) = f(t^{−1}x)` (Meyer l.295), so `(λ_t f)^(s) = t^s f̂(s)` and `D_- = ` multiplication
  by `s`. Hence `ρ_-(λ)e_ρ = λ^ρ e_ρ`.

Write `H¹ := 𝒪/I` for the trivial-character sector over `Q`. Let
`H¹_alg := span{[ξ/(s−ρ)^k] : ρ a zero of ξ, 1 ≤ k ≤ m_ρ}` and
`H¹_red := H¹ / ∩_{ρ, j<m_ρ} ker(h ↦ h^{(j)}(ρ))`.

**Fact 2.4a (`PROVED`, given Meyer's description).** (i) `ξ ∈ I`. (ii) The classes spanning `H¹_alg` are linearly
independent in `H¹` and in `H¹_red`, with `(Θ−ρ)[ξ/(s−ρ)^k] = [ξ/(s−ρ)^{k−1}]` for `k ≥ 2` and `= 0` for `k = 1`. So
`H¹_alg` is the algebraic sum of the generalized eigenspaces, and each has **a single Jordan block of length `m_ρ`**.
*Proof.*
* **`ξ ∈ 𝒪`.** On any vertical line, `Γ(s/2)` decays like `e^{−π|t|/4}|t|^{(σ−1)/2}` and `ζ` grows at most
  polynomially, so `ξ` is Schwartz. Cauchy estimates in a strip handle the derivatives.
* **`ξ ∈ I`.** `ξ/ζ = ½s(s−1)π^{−s/2}Γ(s/2)`. Its poles are at `−2, −4, …`, so it is Schwartz on `Re s ≥ ½`. By the
  functional equation, `ξ(s)/ζ(1−s)` equals the same function at `1 − s`, which is Schwartz on `Re s ≤ ½`.
* **The classes lie in `𝒪`.** `ξ/(s−ρ)^k ∈ 𝒪` for `k ≤ m_ρ`.
* **The functionals kill `I`.** Each `ℓ_{ρ,j}: h ↦ h^{(j)}(ρ)`, `j < m_ρ`, vanishes on `I`, because `h ∈ I` vanishes
  to order `≥ m_ρ` at `ρ`. For `Re ρ ≥ ½` use `h/ζ`. For `Re ρ < ½` use `h/ζ(1−s)` and `ord_ρ ζ(1−s) = m_{1−ρ} = m_ρ`.
* **Independence and the Jordan structure.** The matrix `(ℓ_{σ,j}([ξ/(s−ρ)^k]))` is block triangular with nonzero
  diagonal. The Jordan relations follow from `ξ ∈ I`. ∎

**2.5 The trace formula** (`CITED`).
* **Semilocal** (Connes 1999, **Theorem 4**). For finite `S` and compactly supported `h`:
  `Trace(R_Λ U(h)) = 2h(1)log′Λ + Σ_{v∈S}∫′_{k_v^*} h(u^{−1})/|1−u| d^*u + o(1)`. This is proved.
* **Global** (Connes 1999, **Theorem 5**, positive characteristic): the analogous statement with `Q_Λ` holds
  **⟺** RH for all L-functions with Grössencharakter. For number fields Connes states "the analogue of Lemma 1,
  Theorem 5, and Lemma 3" via the prolate analysis (§VIII, after (33)). This is a sketch-level statement for `Q`; see
  doubt 4.
* **Nuclear, unconditional** (Meyer, the character theorem):
  `Σ_z ord_ξ(z)f̂(z) = χ(ρ)(f) = Σ_p W_p(f) + W_∞(f)` for all `f`, with
  `W_p(f) = Σ_e f(p^{−e})p^{−e}ln p + Σ_e f(p^e)ln p` and `W_∞ = pv∫ f(x)/|1−x| + f(x)/(1+x)dx`. This is the explicit
  formula, including the archimedean place, **proved** (R158_001 OT-2 and OT-12 pass). **[amended per R158_004: A11 —
  scope.]** Meyer proves a character identity for his virtual representation on nuclear spaces (with `ord` taken for
  his non-entire `ξ`, so the pole terms are included). Equating it with the spectral side recovers the classical
  explicit formula. This is OT-2 for the Meyer–CCM realisation only. Connes' Hilbert-space global trace formula is
  RH-equivalent (next item and §0 A1), and there OT-2 fails. The character computation uses the Euler product
  (Meyer l.1184), which is the named line at which `Ξ_Q` breaks (OT-4).
* **Cohomological** (CCM, **Theorem 6.1**). `Tr(ϑ_m(f)|H¹) = f̂(0) + f̂(1) − (log|a|)f(1) − Σ_v∫′_{(K_v^*, e_{K_v})}…`,
  where the differental idele `a` supplies `log|a| = −log D`, read as `Δ•Δ` (CCM §7.1).
* **Foliated-manifold trace formulas** (Álvarez López–Kordyukov–Leichtnam 2402.06671, abstract; LNM 2387). They are
  proved on **closed manifolds** with a codimension-1 foliation, simple closed orbits and preserved leaves, and "solve
  a conjecture of C. Deninger". Leichtnam (math/0603576, abstract) treats laminations of the form disk × `Z_p^m`. `X`
  is neither, so these formulas are *models* of Meyer's theorem, not inputs to it.

**2.6 The square** (`CITED`). CCM §7.1: to `ϑ_a(γ)` "one associates the graph `Z_g` given by the pairs
`(x, g^{−1}x)` … points in the product `A_K/K^× × A_K/K^×`". The correspondences are
`Z(f) = ∫_{C_K} f(g)Z_g d^*g`, with degree `d(Z(f)) = f̂(1)` and codegree `d′(Z(f)) = f̂(0)` (Def. 7.1). The
trivial correspondences are the range `V` of the restriction map (Prop. 6.4). The combinatorial square is CC's
arithmetic/scaling-site square: the topos `N̂^× × N̂^×` with the Newton-polygon semiring and the Frobenius
correspondences `Ψ(λ)` (essay l.903–918). Connes, essay l.952: "what is missing is an intersection theory and a
Riemann–Roch theorem on the square of the arithmetic site". CC, 1805.10501 l.413: the Riemann–Roch problem on the
square "is still open … an appropriate definition of the sheaf cohomology `H¹`".

---

## §3 The positivity question made precise (deliverable 2)

**3.1 Weil's template** (`CITED`: CCM §2.3; P47 Restatement 19.29). Over `F_q`, Castelnuovo–Severi (Hodge index on
`NS(C×C)`) gives `Tr(Z⋆Z′) > 0` on correspondences. By the Lefschetz formula, that inequality is RH for `C`. The
positivity is a theorem about **all** divisors of the surface, including sums and fibres (P47 §21.7).

**3.2 On `X`: the inner product, the involution, and the equivalence** (`CITED`, CCM math/0703392).
* **Trace pairing** (Remark 4.18): `⟨f₁, f₂⟩_{H¹} := Tr(ϑ_m(f₁ ⋆ f₂)|H¹(A_K/K^×, C_K))` descends to `H¹ ⊗ H¹`,
  with radical containing `V` (Prop. 6.4(1)).
* **Rosati involution** (6.9): `f^♯(g) = |g|^{−1}f(g^{−1})`.
* **Proposition 6.2 / Corollary 6.3**: "The following conditions are equivalent: • All L-functions with
  Grössencharakter on K satisfy the Riemann Hypothesis. • The trace pairing (4.47) satisfies `⟨f, f^♯⟩ ≥ 0`, for all
  `f ∈ S(C_K)`."
* **Proposition 7.2** (Hodge index on the square): RH ⟺
  `Z(f) •_trans Z(f) ≤ 2d(Z(f))d′(Z(f)) − Δ•Δ f⋆f^♯(1)` for all `f`.
* **Connes 1999** (Remark d, §VIII): "the positivity of the inner product is of course equivalent to the positivity of
  the Weil distribution (and by the result of A. Weil to RH) but this does not give any clue how to prove this
  positivity".

**Proposition B (the positivity on `X` reduces to Weil positivity; `CITED` + dictionary, `RESTATEMENT`).** Restrict
CCM Cor. 6.3 to `Ẑ^×`-invariant `f = g ⋆ g^♯` with `g ∈ C_c^∞(R_+^*)` and `supp g ⊂ e^{I_T}`, an interval of
log-length `2T`, so that `f` is supported on `|log| ≤ 2T`. Put `F(t) := e^{t/2}g(e^t)` up to the `Δ^{1/2}`
normalisation of CCM (6.7)–(6.10) **[A12(1): no extra normalisation; the map is exactly `F(t) = e^{t/2}g(e^t)`]**. Then `⟨g, g^♯⟩_{H¹} = Σ_ρ Φ_F(ρ)Φ_F(1−ρ) = W_T(F)`, the **complete** form P46
`eq:W`. The term `2d d′ = 2f̂(0)f̂(1)` of (7.6) is P46's `2Re(A(F)\overline{B(F)})`, and the `•_trans` term is the
archimedean-plus-prime part `𝔞_T` **[A12(2): with sign, `−𝔞_T`]**. Restricting to `d(Z) = d′(Z) = 0` (P46's `A(F) = B(F) = 0`) gives the
**primitive** form on `P_T`. Hence:
* Cor. 6.3 for `ζ` ⟺ E1;
* ~~Prop. 7.2 is the Hodge-index form of E1, i.e. P47 (18.2) at `H = 2K` (`I_∞(F,F) ≤ ½(deg F)²`), which is E6;~~
  **[amended per R158_004: A12(4)]** Prop. 7.2 over `Q` is E1 test by test, in Castelnuovo form. P47 (18.2) is its
  weaker `K`-Hodge-index form. They are equivalent globally only;
* restricted to degree 0 it is E2, and E1 ⟺ E2 only globally (P45 Thm 10.4; the reduced statement §2,
  `cor:convfail`).

*Status.* The equivalences are CCM's and Weil's. The identification of normalisations (`Δ^{±1/2}`, `♯` versus `*`,
`ϑ_m = |γ|^{1/2}W`, CCM (4.41)) is `ANALYSIS`, to be checked against P46 `eq:W` per the process rule; see doubt 1. The
structural content does not depend on it: the square's inner product is the trace pairing on correspondences, and its
positivity is Weil's criterion. **It is a restatement.**

**[amended per R158_004: A12 — the normalisation check, done against CCM (4.40), (6.9), (6.3), (7.6)–(7.8), P46
`eq:W` l.134 and `lem:roughEF`, and P47 (11.6) l.2136 and (18.2) l.4826. Status: `PROVED` (the computation below); the
equivalences with RH are `CITED`.]**
1. **The map is exact.** CCM's trace is `Tr(ϑ_m(f)|H¹) = Σ_ρ f̂(ρ)`, with zeros at `ρ` and the shift already absorbed
   (4.45). Also `(g^♯)^(s) = \overline{ĝ(1−\bar s)}`. With `F(t) := e^{t/2}g(e^t)` exactly, `ĝ(s) = Φ_F(s)`, so
   `Tr(ϑ_m(g⋆g^♯)) = Σ_ρ Φ_F(ρ)\overline{Φ_F(1−\barρ)}`. For real `F` this is `W_T(F)`. No further `Δ^{±1/2}` enters.
   CCM's `Δ^{−1/2}` (Prop 6.2) is the passage from `W` to `ϑ_m`, and Cor 6.3 has already absorbed it. Also
   `g⋆g^♯(1) = ∫|g|²|x|d^*x = ‖F‖²`.
2. **Degree, codegree and the transverse term.** `d = ĝ(1) = A(F)` and `d′ = ĝ(0) = B(F)`. CCM (7.8) writes
   `2f̂(0)f̂(1)`; for complex `f` this is `2Re(A\bar B)`. The transverse term is the local part, so
   `Z•_trans Z = 2Re(A\bar B) − W_T = −𝔞_T`. ~~(`•_trans` "is" `𝔞_T`)~~ The sign was wrong: it is `−𝔞_T`.
3. **The constants.** Over `Q`, `log|a| = −log D = 0`, so the `Δ•Δ` term of (6.3)/(7.6) **vanishes**. P46's
   `C₀ = ψ(¼) − log π` is not a `Δ•Δ` term. It sits inside the archimedean principal value `∫′_{(R^*,e_R)}` (the
   additive-character normalisation). It is also unrelated to P47 §21.7's divergent `Δ·Δ = 2−2g`, which concerns
   `I_A(Frob_n, Frob_n)`.
4. **Prop 7.2 over `Q` is E1 test by test.** Hence (7.6) ⟺ `W_T(F) ≥ 0` for each `F`. That is Castelnuovo's form:
   Hodge index against the pair of fibre classes, `D² ≤ 2dd′`. P47 (18.2) is Hodge index against `K`. With
   `I_∞(F,K) = ½(Φ_F(0)+Φ_F(1))` and `I_∞(K,K) = ½`, it reads `W(F) ≥ −½(Φ_F(0)−Φ_F(1))²` test by test. That is strictly
   weaker per test, and it coincides with (7.6) on even `F`. "Prop 7.2 = P47 (18.2) = E6" is **withdrawn**. Correct
   reading: Prop 7.2 is E1 in Castelnuovo form. (18.2) is its `K`-Hodge-index weakening. The two are equivalent only
   globally.
5. **Cor 6.3 is a statement about all Grössencharaktere.** Its restriction to `Ẑ^×`-invariant `f` is Weil's criterion
   for `ζ` alone (Weil; P45 Thm 10.4; P46 §1). That restriction is not a CCM statement. Tests: `C_c^∞(R_+^*)` is dense
   in the form domain of `W_T` on `L²(I_T)`, and real `F` follows P46's convention.

**3.3 What Connes and Connes–Consani actually prove positive** (`CITED`).
* **Connes 1999, proof of Thm 5, (23)–(25).** `E(B_{Λ,0}) ⊂ S_Λ`, so `Q′_{Λ,0} ≤ S_Λ`, so
  `Δ_Λ(f) := Tr((S_Λ − Q′_{Λ,0})V(f))` is of positive type **for every Λ**. The global trace formula (a) says
  `Δ_Λ → Δ`, the Weil distribution. So the positivity is a *compression* (two nested projections), and its transfer
  to `W` is the limit `Λ → ∞`, which is ⟺ RH.
* **CC 2006.13771 (abstract, Introduction).** "The root of the positivity is the trace of the scaling action
  compressed onto the orthogonal complement of the range of the cutoff projections". `Tr(ϑ(f)S) ≥ 0` "by
  construction", and `W_∞ − Tr(ϑ(·)S)` is controlled by prolate functions "when the support … is contained in the
  interval (1/2, 2)". That is autocorrelation support `log 2`, i.e. the **complete** form at `T ≤ ½log2` (Yoshida's
  window; P46 l.160).

In both cases the positive object is proved and trivially positive, and the whole content sits in the error term,
uniformly in the cutoff. This matches the reduced statement §1: the content is uniformity. The corpus closes these
routes as compressions and finite-`S` mechanisms (R157_002 rows 9, 18, 34, 60: F3, F1/F4).

---

## §4 Structures on `X`: existence, and the source of positivity (deliverable 3)

**4.1 Hilbert completion / unitarity (`L²_δ`).** It exists (Connes Thm 1). Positivity is built in: the spectrum is on
`iR` because `‖W(g)‖` grows polynomially. The price is that only critical zeros are seen, with capped multiplicity.
Completeness (all zeros appear) is the global trace formula ⟺ RH (Thm 5). **`RESTATEMENT`** (Hilbert–Pólya, R157
row 32 EQUIV).

**4.2 Compression positivity** (`Δ_Λ ≥ 0`, CC Sonin trace). `PROVED` (`CITED`). Transfer ⟺ RH. **EXCL** under F3,
as a finite cutoff with an identity-type transfer (R157 rows 9, 18, 34, 60).

**4.3 Rosati involution `♯` and the trace pairing.** They exist (CCM (6.9), (4.47)). Positivity ⟺ RH (CCM Cor. 6.3).
This is P47 Thm 20.38 (W1), "`W` is a norm iff RH", in adelic dress. **`RESTATEMENT`**.

**4.4 Positive cone of correspondences / effective cone / Riemann–Roch on the square.**
* **The cone `{f ⋆ f^♯}`.** It is the Rosati cone, so this is 4.3 again.
* **CCM's dictionary** (§2.4) lists "Effective correspondences ↔ Epimorphism of `C^*`-modules" and
  "`deg Z(P) ≥ g ⇒ Z + (f)` effective ↔ `d(Γ) > 0 ⇒ Γ + K` onto". The paper constructs neither ("This leaves open the
  more difficult question of identifying the correct analog of the principal divisors", §1).
* **CC's five steps** (1805.10501 l.891ff.): complex lift, intersection theory, Hirzebruch–Riemann–Roch on `Γ²` with
  topological term `½s(f,f)`, an existence result for `H⁰(±D̃(f))`, tropical descent to effectivity. This is exactly
  the scheme of P47 Thm 12.3: step 3 is clause (c), steps 4–5 are clause (b′).

*F5 reading.*
* **Covered.** Thm 19.25 and Cor 19.25b kill it whenever "effective" means `𝓝_∞`-equivalent to a nonnegative class
  on `D^W`, `𝒟_c` or `𝒟_p`. A finer equivalence (linear rather than numerical) only strengthens (b′), which Cor 19.25b
  covers: "Requiring … only strengthens the hypothesis". The trace-positive enlargements are refuted by the single ray
  of Thm 20.37.
* **Not covered.** Thm 19.25 does not cover an effective cone on a genuine two-variable carrier that is **strictly
  larger** than the frame's `𝓔`, containing `+` classes (R158_001 P7/OT-9; P47 §21.7). That residual is **`OPEN`,
  unbuilt**. CC: "`H¹` … still open".
* **What any such cone must evade** (`PROVED` in P47). It must change the value of a clause along the ray `E_t`, on
  which all frame invariants are frozen (Thm 20.37). So it must read zero data: (W1) or (W2) of Thm 20.38. **[amended per R158_004: A24 — "read" should be "carry information outside the frame's invariants". Reading (W1)/(W2) fails OT-3; proving them is the open problem.]**

**4.5 Transverse measure and the conformal factor; transverse Kähler form.** The transverse measure exists and is
scaled by the flow. This is `CITED`: essay l.700, "the action of `Q^×` … is ergodic for this measure and gives the
same factor of type II_∞ as the horocycle foliation. Moreover the dual action scales the trace in the same manner".
This is the `α = 1` of Deninger's Theorem 2.1 on "`H²`", realised as `Θ = 1` on `x¹ ∈ 𝓗⁰_+`. A transverse Kähler
**form** of positive degree has no carrier, because the transversal of `C_Q` is profinite (Lemma A). A leafwise Kähler
form has no carrier either, because there are no leafwise 1-forms. The phase 15 M8 record adds two more failures
(`CITED (corpus)`, R158_001 §4 row "Connes"): the invariant measure is infinite and the basic cohomology is not
finite-dimensional, so the Álvarez López–Kordyukov Hodge hypotheses fail.

**4.6 Hodge `⋆`, Hodge decomposition, and polarization.** This is the new work of this file.

**Lemma D (the intrinsic involution reverses the flow; `PROVED`).** Let `σ: H¹ → H¹` be induced by `h(s) ↦ h(1−s)`.
This is the functional-equation map, which Meyer realises by `JF`, with `(JFf)^(z)/ζ(z) = h(z)/ζ(1−z)`, proof of
Thm "Lap_range". Then `σ` preserves `I` and `σ(Θ − ½)σ^{−1} = −(Θ − ½)`.
*Proof.* `σ(s·h) = (1−s)σh`. `I` is `σ`-stable by the symmetric definition of `I` and `ξ(s) = ξ(1−s)`. ∎

**[amended per R158_004: A13 — the realiser.]** On the Laplace side `σ` is induced by Meyer's `J`, `Jf(x) = x^{−1}f(x^{−1})`,
which satisfies `(Jf)^(s) = f̂(1−s)` (Meyer l.594). It is **not** induced by `J𝓕`. `𝓕J` has multiplier `γ(s)` and does
not descend to `𝓗_-/Z𝓗_∩` (corpus 114 D.39 §§3–6). The identity `(J𝓕f)^/ζ(z) = h(z)/ζ(1−z)` in the proof of Thm
"Lap_range" is the functional equation on `Z𝓗_∩`; it is not a realisation of `σ`. Fourier enters only through Poisson,
which makes the range `I` stable under `J`. The identity itself is unaffected. "The only involution intrinsic to `X`"
is struck (A3).

~~The `J` of phase 63 flips the frequency `n → −n` (R1-VERDICT). It is the restriction of `σ` to the critical line,
`½ + it ↦ ½ − it`, so the measured ratio `‖[D,J]‖/‖D‖ = 2.000` is Lemma D.~~ **[amended per R158_004: A14]** The `J`
of phases 62–63 is `J e_n = sgn(n) e_{−n}`, with `J² = −1` (phase-62 E94_RESULTS l.8, `E94_Jcompat.py` l.30–34). It is
not `σ` (`σ² = +1`). It factors as `J = σ∘(i⋆_win)`, where `σ e_n = e_{−n}` is the frequency flip (`σ` on the line,
`½+it ↦ ½−it`) and `i⋆_win e_n = sgn(n)e_n` is `i` times the Hilbert transform of the window, i.e. Construction C's `⋆`
on the window. `⋆_win` commutes with `D_log`, and `σ` anti-commutes with it. So `D_log J = −J D_log`: the measured ratio
`2.000` is Lemma D, carried by the `σ` factor. This is phase 64 Task D's parity lemma (`RESULTS.md` l.33–47), there
proved for this `J`. The intrinsic involution of `X` is
**Poincaré duality**: it gives `Θ + Θ^t = 1`, as in Deninger's (10). It is not a Hodge `⋆`, and nothing in the
structure of `X` makes a `⋆` out of it.

**Construction C (a flow-commuting Hodge `⋆` exists unconditionally; `PROVED`).**
* **Splitting.** `ξ` has no real zeros (`ξ(σ) > 0` on `R`: P47 A9 for `ξ`, classical). So
  `H¹_alg = H^{1,0} ⊕ H^{0,1}`, where `H^{1,0}` is the span of the generalized eigenvectors with `Im ρ > 0` and
  `H^{0,1} = conj(H^{1,0})`, with `conj: h(s) ↦ \overline{h(\bar s)}`.
* **The `⋆`.** Set `⋆ := −i` on `H^{1,0}` and `+i` on `H^{0,1}`. Then `⋆` commutes with `Θ` and with `conj`, and
  `⋆² = −1`.

On `H¹_alg`, Θ is therefore `⋆`-linear. The phase-63 "wrong type" statement is specific to ~~`J = σ`~~ **[A14]**
`J = σ∘(i⋆_win)`, and it does not survive with this `⋆`. What survives is the polarization question, which is the next
lemma.

**[amended per R158_004: A15 — the status of Construction C.]**
* **OT-3.** On `H¹_alg`, `⋆` is defined through the spectral splitting, i.e. from the zeros, so OT-3 fails. It is not
  defined at all on the topological `H¹` (doubt 2): there is no holomorphic "sign of `Im s`". On the critical-line
  window it is the Hilbert transform, which is zero-free.
* **Novelty.** It is a device. The corpus precedent is 106.157 (a complex structure `J = i` on the CCM quotient,
  trivially commuting with `Θ`).
* **Scope of phase 63.** Phase 63's obstruction is `J`-specific. The record states this correctly at `MAP_1` NG-63
  ("for this specific construction") and at R1-VERDICT ("It does not prove no Frobenius exists in a larger/true
  cohomological realization"). The unscoped phrasings "the wrong type to be Frobenius" (R1-VERDICT; `MAP_3` l.232;
  R151_001 l.553; CORPUS_CHECK_R145 l.22), and `MAP_3` row 63's "PROVED-IMPOSSIBLE" with "over-generalized? No", should
  be read as `J`-specific. No corpus statement proves a theorem beyond that `J`.

**The dualities.** For `Φ` entire with `Φ(1−s) = Φ(s)` and `Φ(\bar s) = \overline{Φ(s)}`, set, on representatives in
`H¹_alg + I`,

    B_Φ(a,b) := Σ_ρ Res_{s=ρ} Φ(s) a(s) b(1−s) / ξ(s)      (finitely many nonzero terms).

**Fact 4.6a (`PROVED`).** Let `a, b` range over `H¹_alg`.
1. `B_Φ` is well defined on classes: an element of `I` vanishes to order `≥ m_ρ` at `ρ`, so it contributes no residue.
2. `B_Φ(Θa,b) + B_Φ(a,Θb) = B_Φ(a,b)`, i.e. Deninger's cup-product relation with `α = 1`.
3. `B_Φ(a,b) = −B_Φ(b,a)`: it is alternating, like a cup product on `H¹` (substitute `s ↦ 1−s`).
4. `⋆` is a `B_Φ`-isometry, and `S_Φ(h,h′) := B_Φ(h, ⋆h′)` is real symmetric on the real part of `H¹_alg`.
5. `B_Φ(H^{1,0}, H^{1,0}) = 0`.
6. For `h = a + ā` with `a ∈ H^{1,0}`: `S_Φ(h,h) = 2i·B_Φ(a, ā)`, the Hodge–Riemann expression `i∫ω ∧ ω̄`.
7. Suppose all zeros are simple. Then every `Θ`-compatible bilinear form on `H¹_alg` is a `B_Φ`.
*Proof of 7.* Compatibility forces `E_ρ ⟂ E_σ` unless `σ = 1−ρ`. On `E_ρ × E_{1−ρ}` (both lines) the compatible forms
form a 1-dimensional space, and any values `φ(ρ)` are interpolated by an entire `Φ` (Weierstrass). ∎

**[amended per R158_004: A16 — item 7 is false as stated with `Φ` even.]**
* **The gap.** The values on `E_ρ × E_{1−ρ}` and on `E_{1−ρ} × E_ρ` are independent, since `ρ ≠ 1−ρ` because `ξ(½) ≠ 0`.
  An even `Φ` forces `B_Φ(e_{1−ρ}, e_ρ) = −B_Φ(e_ρ, e_{1−ρ})`.
* **Counterexample.** CCM's trace pairing (Rem 4.18; 106.157 (7)). On the Laplace side it is
  `h(a,a′) = Σ_ρ m_ρ a(ρ)\overline{a′(1−\barρ)} = B_{ξ′}(a, ā′)`. Its multiplier `ξ′` is **odd** (`ξ′(1−s) = −ξ′(s)`),
  so the form is symmetric, not alternating. It is compatible, and it is the canonical positivity candidate on `X`.
* **Corrected statement (`PROVED`).** Under SZ, every compatible bilinear form on `H¹_alg` is `B_Φ` for some entire
  `Φ`, with no parity condition. The alternating forms are those with `Φ` even; the symmetric ones are those with `Φ`
  odd. Real forms have `Φ` real.
* **Identity.** `B_{Φ₀} = B_{ξ′}((Θ−½)·, ·)`.

**Lemma E (the polarization lemma; `PROVED`, given Meyer's description of `H¹`).** Let `Φ` be as above with
`Φ(ρ) ≠ 0` at every zero. Then `iB_Φ(a, ā)` is definite on `H^{1,0}` if and only if all three of the following hold:
* RH;
* all zeros of `ξ` are simple;
* `Φ(½+iγ)Ξ′(γ)` has the same sign at every zero `ρ = ½+iγ` with `γ > 0`, where `Ξ(t) = ξ(½+it)`.
*Proof.*
* **Simple on-line zero.** Take `ρ = ½+iγ` with `γ > 0` simple, and `e_ρ := [ξ/(s−ρ)]`. The only residue is at `ρ`.
  There `ē_ρ(1−s) = ξ(s)/(ρ−s) → −ξ′(ρ) = iΞ′(γ)`, using `Ξ′(t) = iξ′(½+it)`. So
  `iB_Φ(e_ρ, ē_ρ) = −Φ(ρ)Ξ′(γ)`, a nonzero real number. Distinct `ρ, ρ′` give orthogonal lines.
* **Off-line zero.** Take `ρ` off the line with `Im ρ > 0`. Then `iB_Φ(e_ρ, ē_ρ) = iΦ(ρ)ξ(1−ρ)/(1−2Re ρ) = 0`, while
  `B_Φ(e_ρ, ē_{1−ρ̄}) = Φ(ρ)ξ′(1−ρ) ≠ 0` (if simple) with `1−ρ̄ ∈ H^{1,0}`. The resulting 2×2 block `[[0,c],[c̄,0]]`
  is indefinite.
* **Multiple zero.** At a multiple zero, `w = [ξ/(s−ρ)]` lies in the image of `Θ − ρ`. The computation of Lemma U
  below gives `iB(w, w̄) = 0`, so `w` is isotropic, and definiteness fails.
* **Conclusion.** Collecting the cases: definite ⟺ no off-line zero, no multiple zero, and a constant sign on the
  diagonal. ∎

**[amended per R158_004: A17 — audit of the proof, and its reach.]**
* **The sign computation is correct.** `ē_ρ(s) = ξ(s)/(s−\barρ)`, and `1−\barρ = ρ` on the line. The integrand is
  `−Φξ/(s−ρ)²`, with residue `−Φ(ρ)ξ′(ρ) = iΦ(ρ)Ξ′(γ)`, so `iB = −Φ(ρ)Ξ′(γ)`, real because `Φ` is even and real. The
  off-line block `[[0,c],[c̄,0]]` and the Jordan isotropy `H(w,w) = (1−2Reρ)H(v,w)` are correct.
* **The first two cases use only compatibility.** The off-line case and the multiple-zero case use only
  `H(Θx,y)+H(x,Θy) = H(x,y)` for `H(x,y) := iB(x,ȳ)`. So "definite ⇒ RH ∧ SZ" holds for **every** compatible hermitian
  form, including CCM's `h = B_{ξ′}(·, ·̄)` without the factor `i`. That is Lemma U, i.e. classical (A6). Only the
  sign clause is specific to `B_Φ`: for odd `Ψ` it reads "`H(e_ρ,e_ρ) = iΨ(½+iγ)Ξ′(γ)` has constant sign". CCM: `Ψ = ξ′` gives
  `Ξ′(γ)² > 0`.
* **Minor points.** The hypothesis `Φ(ρ) ≠ 0` is not needed for necessity, since a zero of `Φ` at a zero of `ξ` makes
  the form degenerate. The whole argument uses nothing about `ξ` beyond entire, even, real, and Schwartz on vertical
  lines. It therefore applies verbatim to `Ξ_Q` or to any such function, and so, by T2, it cannot carry a sign.

**Corollary E-i (the canonical duality is indefinite; `PROVED`, unconditional given verified zeros).** Take `Φ ≡ 1`.
Then `B_1` is the Grothendieck–Serre residue duality of `𝒪/(ξ)`, the one given by local duality, and `iB_1` is
indefinite on `H^{1,0}`.
*Proof.*
* `γ₁ = 14.1347…` and `γ₂ = 21.0220…` are simple on-line zeros with no ordinate between them (Platt–Trudgian; the
  input (X19) of P47 and its extension to `γ₂`).
* So `Ξ′(γ₁)` and `Ξ′(γ₂)` have opposite signs.
* By the computation above, `iB_1` restricted to `span(e_{ρ₁}, e_{ρ₂})` is `diag(−Ξ′(γ₁), −Ξ′(γ₂))`. ∎

**[amended per R158_004: A18]**
* **A proof with no verified zero (`PROVED`, unconditional).** Suppose `iB_1` were definite. Lemma E gives RH ∧ SZ,
  and `Ξ′(γ)` has constant sign at all `γ > 0`. Under RH ∧ SZ, `Ξ` is real with simple real zeros, and there are at
  least two positive ones (Riemann–von Mangoldt, or Hardy). Between consecutive ones `Ξ` keeps its sign, so `Ξ′` takes
  opposite signs at them. That is a contradiction. The numerical proof above is kept but is not needed (working rule
  ).
* **The citation was defective.** P47 (X19) certifies `γ₁` and the absence of zeros with `|Im ρ| ≤ 21`. It does not
  certify `γ₂ = 21.022…`, which would have needed a new import (Platt–Trudgian 2021 as a verified list).
* **Canonicity (doubt 3).** The conclusion holds for every `Φ` positive on the critical line, e.g. `e^{g}` with `g`
  even and real: changing the generator of `(ξ)` by such a unit does not matter. But `B_1` is not the canonical
  *positivity* candidate on `X`; that is CCM's `h = B_{ξ′}` (A16). E-i refutes a form that no source proposes as
  positive.

**Corollary E-ii (the log-derivative duality is Weil's form; `PROVED` + `RESTATEMENT`).** Take `Φ₀ := (s−½)ξ′(s)`.
It is even and real.
* **Formula.** Since `Φ₀/ξ = (s−½)ξ′/ξ` has simple poles with residues `m_ρ(ρ−½)`,
  `B_{Φ₀}(a,b) = Σ_ρ m_ρ(ρ−½)a(ρ)b(1−ρ)`, **for all multiplicities**.
* **Definiteness.** `iB_{Φ₀}(e_ρ, ē_ρ) = −γΞ′(γ)²` at simple on-line zeros. So `iB_{Φ₀}` is semidefinite on
  `H^{1,0}_alg` ⟺ RH (off-line pairs are hyperbolic; Jordan tails are null), and definite ⟺ RH ∧ SZ.
* **Definable without zeros.** `B_{Φ₀}` can be written without the zeros: by the residue theorem on a strip and the
  explicit formula, `B_{Φ₀}(a,b)` is the geometric side (`Σ_p W_p + W_∞`) of the test `(s−½)a(s)b(1−s)`. So it passes
  OT-3.
* **Restatement.** Its positivity is Weil's criterion applied through `|Θ − ½|`:
  `S_{Φ₀}(h,h) = Σ_ρ |Im ρ| Φ_g(ρ)Φ_g(1−ρ)` for on-line data. Positivity for all `h` ⟺ RH (P47 Thm 20.38 (W1)). This
  holds **globally only**: `|Θ−½|` destroys window support, just as E1 ⟺ E2 holds only globally.

**[amended per R158_004: A19]**
* **Checked.** The formula `Σ_ρ m_ρ(ρ−½)a(ρ)b(1−ρ)` holds for all multiplicities, and semidefinite ⟺ RH holds (on
  the line the form is `−Σ m_ρ γ|a(ρ)|²`; off the line it is hyperbolic). The sign orientation: with this `⋆`, `iB_{Φ₀}`
  and `S_{Φ₀}` are *negative* semidefinite; flipping `⋆` flips the sign.
* **What `B_{Φ₀}` is.** `B_{Φ₀} = B_{ξ′}((Θ−½)·,·)`, i.e. CCM's trace form composed with `Θ − ½`.
* **The zero-free definition, stated precisely.** The "geometric side" must include the pole terms: with the entire
  `ξ`, `Σ_ρ m_ρ g(ρ) = g(0) + g(1) − (Meyer's W)` in his sign convention. Meyer's character identity is proved for
  `C_c^∞(R_+^*)`. Using it for tests `g = (s−½)a(s)b(1−s)` with `a, b ∈ 𝒪` needs its extension by continuity to
  `𝓗_-`. Density, and continuity of `W` and of the zero sum there, are standard but not written out: `ANALYSIS`. OT-3
  passes on that reading.

**Proposition H (definite polarizations are of infinite type; `PROVED`).** Suppose `iB_Φ` is definite on `H^{1,0}`.
Then `t ↦ Φ(½+it)` has a zero of odd order in every gap `(γ_n, γ_{n+1})` between consecutive positive ordinates. So
its real zeros satisfy `n_Φ(T) ≥ N(T) − 1 ≍ (T/2π)log T`, and `Φ(½+it)` is not of finite exponential type. In
particular, `Φ(½+it)` is not the Fourier transform of any compactly supported distribution (a window-`T` datum), and
not a finite product of local factors and Γ-data.
*Proof.*
* By Lemma E, RH ∧ SZ hold, so consecutive real zeros of `Ξ` are simple and `Ξ′` alternates in sign along them.
* Sign coherence forces `Φ(½+iγ_n)` to alternate, so `Φ(½+it)` changes sign in each gap. That gives the count.
* An entire function of exponential type `τ` has `n(r) ≤ eτr + O(1)` by Jensen (after dividing out a zero at 0),
  which contradicts `n(r) ≫ r log r`.
* Paley–Wiener: compact support gives finite type. ∎

This is the Hodge-side analogue of P46 `thm:finZ` ("row D is intrinsically infinite"). A polarization of `X`'s `H¹`
must carry the ordering of **all** the zeros, which is the X-form of Doc 130's "the Kähler structure is the inertia".

**[amended per R158_004: A21]**
* **Checked and correct.** The Jensen step: `n(r) ≤ ∫_r^{er} n(t)dt/t ≤ log M(er) − log|G(0)| ≤ eτr + O(1)` for
  `G(z) = Φ(½+iz)` after dividing out `z^k`. The Paley–Wiener–Schwartz clause is also correct. Every representing `Φ`
  shares the sign pattern at the zeros, so the conclusion does not depend on the choice of `Φ`. The same holds for odd
  `Ψ`, with `−iΨ(½+it)` real (CCM: `Ψ = ξ′`, zeros by Rolle).
* ~~"not a finite product of local factors and Γ-data"~~ **Not covered by exponential type**, since `Γ` and `1/Γ` are
  of infinite type. Replacement (`PROVED` by zero count): `Φ(½+it)` is not any function with `O(T)` zeros on the
  critical line up to height `T`. This includes finite products of Euler polynomials `1 − c p^{−s}`
  (`T log p/2π + O(1)` zeros each) times `1/Γ(as+b)` with `a, b` real (no zeros on the line off `s = ½`) times
  `e^{polynomial}`. Complex shifts of `Γ` are not treated.
* **"Finite-window datum"** means the *multiplier*. It is not a P46 window test. P46's `W_T` is CCM's form (infinite-type
  multiplier `ξ′`) evaluated on tests supported in `I_T`, so there is no conflict. The analogy with `thm:finZ` is
  `ANALYSIS`.

**4.7 Deninger's Theorem 2.1 structure: unitarity.**

**Lemma U (`PROVED`, given Meyer's description; refines R158_001 audit point (i)).** The following are equivalent:
* (a) there are a positive-definite hermitian form on `H¹_alg` and a real `c` such that `λ^{−c}ρ_-(λ)` is isometric
  for all `λ ∈ R_+^*`;
* (b) RH holds and every zero of `ξ` is simple.
Then `c = ½`, and `Θ = ½ + S` with `S` skew, as in Deninger's Thm 2.1.
*Proof.*
* **(a) ⇒ (b), eigenvectors.** Differentiating the isometry gives `(Θv,v) + (v,Θv) = 2c(v,v)`. For an eigenvector
  `e_ρ` (Fact 2.4a) this gives `Re ρ = c`. Since `ρ` and `1−ρ̄` are both zeros, `c = ½`, which is RH.
* **(a) ⇒ (b), Jordan blocks.** Suppose `m_ρ ≥ 2`. Take `v = [ξ/(s−ρ)²]` and `w = (Θ−ρ)v = [ξ/(s−ρ)]`, so that
  `(Θ−ρ)w = 0`. Then `(Θv,w) + (v,Θw) = (v,w)` becomes `ρ(v,w) + (w,w) + ρ̄(v,w) = (v,w)`, so
  `(w,w) = (1 − 2Re ρ)(v,w) = 0`. So `w = 0`, which contradicts Fact 2.4a.
* **(b) ⇒ (a).** Under (b), `H¹_alg` has the basis `{e_ρ}`. Declare it orthonormal. Then `ρ_-(λ)` acts on `e_ρ` by
  `λ^{±ρ}`, with `|λ^{ρ}| = λ^{½}`. ∎

**[amended per R158_004: A22]**
* **Checked.** With Meyer's conventions (A10), `ρ_-(λ)e_ρ = λ^ρ e_ρ` exactly, so `c = ½` and "`±`" is `+`.
  `H¹_alg` is `ρ_-`-invariant: `λ^s` is a multiplier of `𝒪` and of `I`, because it is bounded on vertical lines.
* **Label.** `PROVED` (elementary); content `CLASSICAL` (A6).
* **Reach (doubt 2).** The direction (a)⇒(b) needs no density. A positive-definite form on `H¹`, or on any completion
  into which `H¹_alg` injects `Θ`-equivariantly, restricts to one on the invariant subspace `H¹_alg`. So the necessity
  half holds for every such realisation. Only (b)⇒(a) is confined to `H¹_alg`.
* **The unresolved part.** Whether `H¹_alg` is dense, i.e. whether `I` equals its hull ideal
  `J = {h : h^{(j)}(ρ) = 0, j < m_ρ}`, is open. It needs lower bounds for `|ζ|` in `½ ≤ Re s < 1` and may be
  RH-adjacent. Residue forms (all `B_Φ`, and CCM's `h`) vanish on `J/I` and on Jordan tails. So they live on `H¹_red`
  at best.

*Remark (ANALYSIS: a function-field falsifier for the transport).* Take `K = F_q(E)` with `E` supersingular and
Frobenius `π = ±p` over `F_{p²}`. Then `ζ_K` has a double zero, RH holds (Weil), and étale `H¹` is semisimple (`π` is
scalar). The adelic cyclic `H¹` of `K` is `C[u^{±1}]/(P(u))` per sector (the shape in Connes 1999 §VIII, Lemma 1 and
the remark "when F has multiplicity one has to be more careful"). It would carry a Jordan block, so by the analogue of
Lemma U it is **not** unitarizable although RH holds. If this is right, the Deninger unitarity reading of `X` is
miscalibrated: it proves too much (SZ), and this is visible where RH is a theorem. The Meyer-type realization in
characteristic `p` has not been re-verified here; see doubt 5.

**[amended per R158_004: A20]**
* **The zeta side of the example is real (`PROVED`, classical).** Take `E: y² = x³ − x` over `F_{p²}` with
  `p ≡ 3 (mod 4)`. It is supersingular with `a_p = 0`, and `π_p² = −p` in `End(E)`. So `Frob_{p²} = [−p]` acts on
  `H¹_ét` as a scalar, hence semisimply, and `Z(u) = (1+pu)²/((1−u)(1−p²u))`. `ζ_K` has double zeros at every `s` with
  `p^{−2s} = −1/p`, all on `Re s = ½`.
* **The Jordan block on the adelic `H¹` in characteristic `p` stays `ANALYSIS`.** CCM Thm 4.16 holds for every global
  field, so the multiplicity is right. Cyclicity needs the Laplace/ideal description of the sector as
  `C[u^{±1}]/(P(u))`, which has not been verified in a source.
* **A stronger falsifier over a number field (`PROVED` classically on the zeta side).** Let `K/Q` be Galois with group
  `S₃`, e.g. the splitting field of `x³ − 2`. Then `ζ_K = ζ·L(s, sgn)·L(s, ρ)²`, with `ρ` two-dimensional (P47 (X25a)).
  `L(s,ρ)` is the Hecke `L`-function of a cubic character of `Q(√−3)`: entire, with infinitely many zeros. Every one of
  them is a zero of `ζ_K` of order `≥ 2`.
* **What it implies (`PROVED` modulo `ANALYSIS`).** On the trivial-character sector of `X_K`, CCM Thm 4.16 gives
  generalized eigenspaces of the right dimension. Given the `K`-analogue of Meyer's Laplace-range theorem, which is
  cyclicity and is the `ANALYSIS` part (Meyer, Duke 2005; CCM Thm 4.16), these are single Jordan blocks. So the Deninger
  unitarity structure of Lemma U **does not exist on `X_K`, whatever RH says**. By T1 (field uniformity), any route that
  derives RH for `ζ` from Lemma U-type unitarity on the adelic `H¹` and runs uniformly in `K` proves something false.
  N-b rests on this, not on the function-field remark alone.

**4.8 Hard Lefschetz `sl₂`.** On the `H¹` of a "curve", `L: H⁰ → H²` is an isomorphism of lines (`x⁰ ↦ x¹` in
`𝓗⁰_+`), and Hard Lefschetz is vacuous. On `X × X` it would need a cup product and a Künneth decomposition for
cokernels of cyclic modules. Neither is constructed in the literature read (CCM work only with `Z(f)` and `V`; CC:
the square's `H¹` is open). Status: **not defined**. The corpus (Doc 129 VEREDICTO-129.B) records that tropical
Künneth does not exist. Phase 62's quaternionic PSD result and phase 63's `D²` test are finite-window shadows (MAP_3
l.32–33), both gapless.

**4.9 The filter table.** "—" means the filter does not apply to an equivalence (R157 treats EQUIV as closed without
the filter).

| structure on `X` | exists? | positivity from | F1 | F2 | F3 | F4 | F5 / Thm 19.25 | phase 63 | label |
|---|---|---|---|---|---|---|---|---|---|
| `L²_δ` unitarity (4.1) | yes, CITED | built in; completeness ⟺ RH | — | — | — | — | not `h⁰` | n/a | RESTATEMENT (EQUIV, row 32) |
| compression `Δ_Λ`, Sonin trace (4.2) | yes, PROVED/CITED | nested projections | ✓ | ✗ (cutoff Λ ↔ window) | ✗ (finite cutoff; identity-type transfer) | — | not `h⁰` | n/a | EXCL (rows 9, 18, 34, 60) |
| trace pairing and Rosati `♯` (4.3) | yes, CITED | ⟺ RH (CCM Cor 6.3) | — | — | — | — | not `h⁰` | n/a | RESTATEMENT |
| Hodge index on `X×X` (3.2, Prop B) | as an inequality, CITED | ⟺ RH (CCM Prop 7.2) = E6 | — | — | — | — | the h⁰ route is Thm 12.3 ⇒ killed by 19.25/19.25b | n/a | RESTATEMENT |
| effective cone and RR on the square (4.4) | not constructed | — | ? | ? | ? | ? | killed for cones ⊆ `𝓔` and for B4; residual = strictly larger two-variable cone | n/a | OPEN, unbuilt |
| transverse measure `e^t` (4.5) | yes, CITED | gives `Θ = 1` on `H²` only | — | — | — | A3 ✓ | — | — | PROVED structure, no sign |
| transverse / leafwise Kähler form (4.5) | **no carrier** (Lemma A) | — | — | — | — | — | — | — | PROVED absent |
| intrinsic involution `σ` (Lemma D) | yes | reverses the flow (duality) | — | — | — | — | — | = phase 63's `J` | PROVED |
| Riesz `⋆` + `B_1` (E-i) | yes, PROVED | **indefinite** | — | — | — | — | — | `⋆` is Θ-linear | PROVED false |
| Riesz `⋆` + `B_{Φ₀}` (E-ii) | yes, PROVED, zero-free definition **[A15: `B_{Φ₀}` is zero-free; the `⋆` is not]** | ⟺ RH (semidefinite) | ✓ | ✓ | ✓ | A3 ✓ (`H⁰_+`), A8 ✓ (`W_p`) | not `h⁰` | `⋆` is Θ-linear | RESTATEMENT |
| any definite `B_Φ` (Lemma E, Prop H) | ⟺ RH ∧ SZ ∧ interlacing `Φ` | `Φ` must carry the zero ordering | ✓ (uses the zeros) | ✓ | ✓ (infinite type forced) | ✓ | not `h⁰` | — | RESTATEMENT (stronger) |
| Deninger unitarity (Lemma U) | ⟺ RH ∧ SZ **[A20: impossible on `X_K` for `K` an `S₃` field, modulo cyclicity]** | — | — | — | — | — | — | — | RESTATEMENT (stronger) |
| Hard Lefschetz (4.8) | vacuous on `X`; undefined on `X×X` | — | — | — | — | — | — | — | not defined |
| **[added per R158_004: A23]** CCM hermitian trace form `h = B_{ξ′}(·,·̄)`, no `⋆` (106.157) | yes, CITED | semidefinite ⟺ RH (Cor 6.3); definite on `H¹_alg` ⟺ RH ∧ SZ (A17) | — | — | — | — | not `h⁰` | n/a | RESTATEMENT (= 4.3) |
| **[A23]** Bost–Connes KMS states; modular Hamiltonian `log n ≥ 0` (Bost–Connes, Selecta 1995; CCM §4, cooling and distillation) | yes, CITED (not re-read) | positive states, positive Hamiltonian; they see `ζ(β)` only for real `β > 1` | ✗ (zero-blind) | — | — | — | not `h⁰` | n/a | proved, zero-blind, does not transfer |
| **[A23]** dual trace on the type II_∞ factor (essay l.700); Weil distribution as a relative trace `(Tr_X − Tr_Y)(π(f))` (CC 1805.10501 l.887) | yes, CITED | each trace positive; positivity of the **difference** is the trace pairing ⟺ RH | — | — | ✗ (a compression) | — | not `h⁰` | n/a | RESTATEMENT (the 4.2/4.3 family) |
| **[A23]** ζ-cycles and prolate operators (CC 2106.01715; CCM 2310.18423, semilocal) | yes, CITED (abstract; local PDF) | self-adjointness per `L` or per `S` | — | — | ✗ (finite `L` or `S`) | — | — | — | EXCL per `L` (R157_002 row 60, R157_004 M5); the limit is row 32, EQUIV |
| **[A23]** critical Plancherel Hilbert completion of `H¹` | the completion is **zero** (114 D.191) | — | — | — | — | — | — | — | — | PROVED void |

**T1 (P47 §18.1).** Everything here is uniform in the global field (Connes 1999 and CCM work for every `K`, and the
Grössencharakter sectors come along). A positivity proof on `X` would prove GRH for all Hecke L-functions. T1
*prescribes* this; it does not exclude it (R157_004 A9).

**T2.** `X` invokes A8 intrinsically, since the local terms `W_p` are the geometric side. It invokes A3 through
`𝓗⁰_+ = C x⁰ ⊕ C x¹`, with `|0 − ½| = |1 − ½|`. `Ξ_a` and `Ξ_Q` have no adèle class space ~~(OT-4 and OT-5 pass by
undefinability)~~. **[amended per R158_004: A1/A23]** Undefinability of the adelic `X` is not a pass. `Ξ_Q` has a
Meyer-type nuclear quotient: its Zeta operator is a lattice sum, and Poisson summation holds. Lemmas D, E, U,
Construction C and Proposition H hold for it verbatim (A17). So none of them can carry the sign, and none is offered as
doing so. The break for `Ξ_Q` is the Euler-product line of the character computation (OT-2/OT-4 by a named line). OT-5
passes vacuously (R158_001 OT-5 row).

---

## §5 Verdict (deliverable 4)

**Theorem 158.2-G (classification on `X`; `RESTATEMENT`; items (a)–(f) `PROVED` or `CITED` as marked; exhaustiveness
`ANALYSIS`).** On `X = A_Q/Q^×`, with Meyer's `H¹` and CCM's trace pairing, the following hold.
* (a) Deninger's data other than definiteness exist intrinsically and unconditionally: `H¹`, `Θ`, `H⁰_+` with
  `Θ ∈ {0,1}`, the trace formula = the explicit formula **[A24: Meyer's character identity on the nuclear `H¹`; Connes' global Hilbert trace formula is RH-equivalent (A1, A11)]**, the duality `B_Φ` with the cup-product relation, a
  flow-commuting `⋆` (Construction C **[A24: defined from the spectrum, OT-3 fails for it (A15)]**), the Rosati `♯`, and the `e^t`-scaled transverse measure.
* (b) The canonical residue polarization `B_1` is indefinite (E-i).
* (c) The log-derivative polarization `B_{Φ₀}`, definable from primes and Γ-data, is semidefinite ⟺ RH, and is Weil's
  form through `|Θ−½|` (E-ii).
* (d) Any definite polarization forces RH ∧ SZ and an interlacing multiplier of infinite type (Lemma E, Prop H). **[A24: the RH ∧ SZ part holds for every compatible hermitian form, including CCM's (A17), and is classical; the infinite type is new here and `PROVED`.]**
* (e) Unitarity à la Deninger Thm 2.1 ⟺ RH ∧ SZ (Lemma U). **[A24: `CLASSICAL` content (A6). Over an `S₃` field it is impossible, modulo cyclicity (A20).]**
* (f) Compressions are positive and do not transfer (Connes Thm 5 proof; CC 2021).
* (g) ~~Rosati and Hodge index on `X × X` are E1/E6, and E2 in degree 0 (Prop B).~~ **[A24/A12]** Rosati (Cor 6.3, restricted to the trivial sector) and CCM Prop 7.2 over `Q` are both E1, test by test. P47 (18.2) is the weaker `K`-Hodge-index form, equivalent only globally. Degree 0 gives E2 (Prop B).

So `X` is a complete Deninger-type frame in which OT-5′ **is** Weil's criterion. The positivity question on `X` is
the positivity question of row D, restated. **No one-round test lemma of type (i) is offered.** Every candidate on
`X` is either equivalent to RH (or to RH ∧ SZ), or is a compression excluded by F3, or is refuted (E-i).

**What a different object would have to add** (each item is forced by a lemma above):
* **N-a (a prior reason for definiteness).** A duality `B` whose `⋆`-polarization is definite for a reason stated
  before the spectrum: an L² norm of leafwise harmonic forms (Deninger–Singhof, math/0204111, `CITED (corpus)` Doc
  130 §1), or a **count** (P47 §21.7: `deg α = #ker α`). By Lemma A this needs leaves of real dimension ≥ 2 carrying
  the zeros **[A24: `HEURISTIC` — this holds only for the harmonic-norm option; the count option needs no leaves]**. `X` has profinite transversals, and its zeros live in a relative group on `X ∖ C_Q`. By Lemma E the
  object must supply sign coherence of the multiplier without knowing the zeros. By Prop H its datum must be of
  infinite type, i.e. global.
* **N-b (a non-cyclic `H¹`).** `X`'s `H¹` is cyclic over the commutative algebra `S(C_K)` in each sector, so
  multiplicity appears as Jordan length (Fact 2.4a). The Deninger reading therefore proves SZ as well (Lemma U), and
  per the function-field remark it is false where RH is known. The right object needs a correspondence algebra with
  `+` (P47 §21.7: "the frame has `⋆` and no `+`"), so that semisimplicity and multiplicity are geometric. **[A24]** Scope:
  N-b binds only a P-HS / (D3) route (definite form, unitarity). The P-HI / Rosati route asks for **semidefiniteness**,
  which tolerates Jordan tails (they are null; E-ii, CCM). The evidence is the `S₃`-field falsifier (A20). The function-
  field remark is secondary. The link "non-cyclic ⟸ `+`" is `HEURISTIC`: §21.7's `+` concerns the effective cone, not
  module cyclicity. N-b is not on R158_001's OT list. It is proposed as an OT-1 clause for the P-HS route.
* **N-c (a larger effective cone).** An effective cone on a two-variable carrier strictly larger than `𝓔`, with
  classes whose clause value changes along the ray of P47 Thm 20.37 (R158_001 P7/OT-9). This is the residual of the
  CC Riemann–Roch strategy. `OPEN`. **[A24]** Per R158_003 A12/A15, the constructive clause ((P145′)(4a)–(4c)) is
  RH-strength. Only the filter part (a two-variable carrier, a cone `⊋ 𝓔`, outside Thm 19.25/Cor 19.25b/Thm 21.15) is not.
  In §4.4, "must read zero data: (W1) or (W2)" should read: it must carry information outside the frame's invariants
  `(a,b,deg,R)`, and Thm 20.38 names the missing facts as the zero-location statements (W1)/(W2). A cone that *reads*
  them fails OT-3; one that *proves* them is the open problem.

**Label for the MW-5 cluster after this file.** The adèle-class instantiation is **closed as a restatement**. The
cluster as a whole stays **NOT EXCLUDED, unbuilt**, now with N-a, N-b and N-c as the precise list of what is missing.
No row-D label change, no sign claim.

**Optional bounded follow-ups** (maintenance, not tests of RH):
* **[A24]** (O0) verify the `K`-analogue of Meyer's Laplace-range theorem (cyclicity), which is all that A20 needs;
* (O1) make the function-field remark rigorous, with the characteristic-`p` Meyer/CCM realisation and the Jordan
  block at a double zero;
* (O2) extend Fact 4.6a.7 and Lemma E from `H¹_alg` to continuous `Θ`-compatible pairings on `H¹_red`, including
  multiple zeros (a spectral-synthesis question for `I`).

---

## §6 Doubts for the audit

**[amended per R158_004]** All ten doubts are answered in R158_004 §2: 1 → A12; 2 → A22; 3 → A16, A18; 4 → confirmed
(Connes l.1971 Thm 5 is char `p`; l.2215 "the analogue of Lemma 1, Theorem 5, and Lemma 3" for number fields, no
proof); 5 → A20; 6 → A14, A15; 7 → A9; 8 → confirmed, A10; 9 → A23; 10 → confirmed.

1. **Normalisations.** Meyer's `λ` vs `λ^{−1}` and the sign of `D_-` (his footnote); CCM's `ϑ_m = |γ|^{1/2}W` (4.41)
   and `Δ^{±1/2}`, `♯` vs `*`; the map `g ↦ F` in Prop B. Check Prop B against P46 `eq:W` and P47 (11.6), (18.2),
   per the process rule. Do the identifications E1 ↔ Cor 6.3 and E6 ↔ Prop 7.2 hold with the stated constants,
   including CCM's `−log|a|f(1)` term versus P46's `m(τ)` constant `C₀`?
2. **`H¹_alg` vs `H¹`.** Lemmas E and U and Construction C are proved on the algebraic span of generalized
   eigenvectors. The Riesz `⋆` on the topological `H¹` (a Riesz projection for a non-normal generator) and the
   equality `H¹_red = H¹` (spectral synthesis for `I`) are **not** claimed. Could a positive form on a topological
   completion escape Lemma U? It must restrict to `H¹_alg` if continuous and if `H¹_alg` is dense. Density is not
   proved here.
3. **Canonicity of `B_1`.** E-i refutes one pairing. Its claim to be canonical is that it is the residue duality of
   `𝒪/(ξ)`. Fact 4.6a.7 shows every compatible pairing is a `B_Φ` (under SZ), so Lemma E covers them all. Check the
   sign computation `ē_ρ(1−s) → −ξ′(ρ) = iΞ′(γ)` and the claim that the alternation of `Ξ′(γ₁)`, `Ξ′(γ₂)` needs only
   simplicity of `γ₁, γ₂` and no ordinate between them.
4. **Connes Theorem 5** is proved in positive characteristic. For `Q`, Connes states the analogue after the prolate
   discussion (§VIII). I cite it as stated and use it only in 3.3 and 4.1, which are EXCL/EQUIV in the record anyway.
5. **Function-field remark (4.7).** `ANALYSIS`. The cyclicity of the adelic `H¹` in characteristic `p` is inferred
   from Connes 1999 §VIII Lemma 1 and not re-verified. If the characteristic-`p` realisation is semisimple, the
   remark fails, and N-b rests on Lemma U alone.
6. **Phase-63 reinterpretation.** I claim that phase 63's `J` is the frequency reflection, i.e. `σ` on the line, and
   that the phase-63 obstruction is specific to that `J`, because the Riesz `⋆` makes `Θ` linear. This does not
   contradict phase 63's numerics or R1-VERDICT, which itself says "It does not prove no Frobenius exists in a
   larger/true cohomological realization". Check that no corpus statement uses "no J-linear Frobenius" beyond the
   window.
7. **Lemma A (ii).** It uses Schwartz coefficients on the orbit foliation. With other coefficient spaces (conormal /
   dual-conormal, as in AKL) the orbit-foliation `H¹` could differ. The claim "no zeros in it" rests on flow-invariance
   of orbit integrals.
8. **Fact 2.4a.** `ξ ∈ 𝒪` and `ξ ∈ I` are checked against Meyer's Laplace-side description (Thm "Lap_range"), not
   against his original function-space definitions. Check the class conditions at `Re s = ½` exactly.
9. **Exhaustiveness** of the list in §4.9 is `ANALYSIS`. The candidate a skeptical reader should raise is a positive form
   on `X` defined through the type-II_∞/III factor (Connes' foliation algebra) rather than through `H¹`. I found none
   in the sources read. Connes' essay places the positivity in the trace pairing.
10. **Proposition H** uses Lemma E's conclusion (RH ∧ SZ) as its working hypothesis. It is not a statement about
    `ζ`. It says only that *if* a definite polarization existed, its multiplier would be of infinite type.

---

## §7 Sources

Open literature, read this review unless marked:
* A. Connes, *Trace formula in noncommutative geometry and the zeros of the Riemann zeta function*, Selecta Math. 5
  (1999) 29–106, arXiv math/9811068 (full text): Introduction; §III Thm 1, (22); §VII Thm 4; §VIII Thm 5, (17)–(25),
  (31)–(33); Remarks c, d.
* A. Connes, *An essay on the Riemann Hypothesis*, arXiv 1509.05576 (local), §"adele class space" (l.700–770), square
  of the arithmetic site (l.903–952).
* A. Connes, C. Consani, *The Riemann–Roch strategy, complex lift of the scaling site*, arXiv 1805.10501 (local),
  l.413, 746–772, 875–895.
* A. Connes, C. Consani, *Weil positivity and trace formula, the archimedean place*, Selecta 27 (2021), arXiv
  2006.13771 (corpus text).
* A. Connes, C. Consani, M. Marcolli, *The Weil proof and the geometry of the adeles class space*, arXiv math/0703392
  (full text): §1, §2.4, Thm 4.16, Lemma 4.17, Rem 4.18, §5, Thm 6.1, Prop 6.2, Cor 6.3, Prop 6.4, §7.1, Prop 7.2.
* R. Meyer, *A spectral interpretation for the zeros of the Riemann zeta function*, arXiv math/0412277 (local):
  abstract, §1, Thm "Zeta_estimate", Thm "Lap_range", Cor "Dminus_eigenvalues", Prop "rho_summable", the character
  theorem.
* C. Deninger, *Number theory and dynamical systems on foliated spaces*, arXiv math/0204110 (local): §2 (2)–(8),
  Thm 2.1 with proof, §5.
* C. Deninger, *Dynamical systems for arithmetic schemes*, arXiv 1807.06400 (local): (61) and the paragraph after it,
  §10 Def. t101.
* M. Morishita, *On a relation between Deninger's foliated dynamical systems and Connes–Consani's adelic spaces*, arXiv
  2508.15971 (local; abstract via arXiv).
* J. A. Álvarez López, Y. Kordyukov, E. Leichtnam, *A trace formula for foliated flows*, arXiv 2402.06671 (abstract,
  via search).
* E. Leichtnam, *Scaling group flow and Lefschetz trace formula for laminated spaces with p-adic transversal*, Bull.
  Sci. Math. 131 (2007), arXiv math/0603576 (abstract, via search).
* F. Kopei, *A remark on a relation between foliations and number theory*, arXiv math/0605184 (abstract, via search).
* Deninger–Singhof math/0204111 and Deninger math/0204194: `CITED (corpus)` via Doc 130.
* Platt–Trudgian (Bull. LMS 53, 2021), for the simplicity of `γ₁, γ₂`: via P47 (X19). **[A18: X19 covers `γ₁` only; the import is no longer needed]**
* **[added per R158_004: A25]** E. Leichtnam, arXiv 1307.3851, §2 eq. (6) (Serre's argument), axioms 5]–6], Comment 6
  (read by R158_004). R. Meyer, *On a representation of the idele class group related to primes and zeros of
  L-functions*, Duke Math. J. 127 (2005) (CCM [32]; not re-read). Corpus: 106.156/157, 107.204, 114 D.37/D.39/D.191,
  phase-64 `RESULTS.md` Task D, phase-62 `E94_RESULTS.md`.
