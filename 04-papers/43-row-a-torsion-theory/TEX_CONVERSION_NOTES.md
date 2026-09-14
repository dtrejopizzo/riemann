# Notes on the LaTeX conversion of `main.md`

Target: `main.tex` → `main.pdf` (amsart, 11pt, 51 pages).
Title: *A Correspondence Algebra with a Canonical Trace on the Idele Class
Group, its Tate Symbol and its Numerical Form*.

The Riemann hypothesis is not mentioned anywhere in the article — not in the
title, abstract, body, remarks or bibliography. All programme vocabulary
(phases, rows, rounds, clauses, status labels, internal note identifiers,
audit findings, ledgers) has been removed and replaced by the mathematics.

---

## (a) Markdown statements included, and their tex labels

| Markdown | tex label | tex statement |
|---|---|---|
| P123.124 §§2–5 (adapted partition, projectivity, ideal product) | `lem:partition`, `lem:projective`, `lem:idealproduct` | Lemmas 3.6–3.8 *(added in R1)* |
| P123.125 §§1–3 (Čech resolution, the two vanishings) | `lem:cech` | Lemma 3.9 *(added in R1)* |
| Theorem 8A.12, Remark 8A.12a (the category over `𝓐_tr`) | `thm:Atrcat`, `rem:whichcompletion` | Theorem 10.3, Remark 10.4 *(added in R1)* |
| §2.2–2.4 carrier, coefficients, source | `eq:carrier`, `eq:coeff`, `eq:source`, `eq:comp`, `eq:shadow` | §2 definitions |
| product formula for `Γ_S` | `lem:prodformula` | Lemma 2.1 |
| Lemma 3.3 (valuation splitting) | `thm:split` | Lemma 2.2 |
| Corollary 3.4 (Fell bundle trivial; `D_A` an algebra) | `cor:trivial` | Corollary 3.2 |
| Definition 8.5 (`D_A`, `D_A^off`) | `def:DA` | Definition 2.5 |
| Remark on the normalization dictionary (§8.2) | `rem:normdict` | Remark 2.4 |
| Definition 3.1 (the category `G`) | `def:G` | Definition 3.1 |
| (3.3) `Hom(E_a,E_b)` classification + Remark 3.6 transfer | `hyp:hom` | **stated as Hypothesis 3.1** (see (c)) |
| Proposition 3.2 (stable, closed, localized, infinitely many objects) | `prop:cat` | Proposition 3.5 |
| Remark 3.5 (type correction: `E_F ∉ C_tw(U)`) | `rem:types` | Remark 3.4 |
| Theorem 4.1 (excision triangle) | `thm:exctriangle` | Theorem 3.5 |
| Lemma 4.2 | `lem:excvanish` | Lemma 3.6 |
| Theorem 4.3 + Corollary 4.4 (two-sided excision) | `thm:excision` | Theorem 3.7 |
| Proposition 5.1 (reading of `Hom(U,N)=0`) | `prop:obstruction` | Proposition 4.1 |
| §5.2 half-density, (5.1) | `eq:graphops` | §4.2 |
| Definition 5.2, Theorem 5.3 (the dagger) | `def:dagger`, `thm:daggerthm` | Definition 4.2, Theorem 4.3 |
| Appendix B.1 (H-unitality) | `lem:hunital` | Lemma 5.1 |
| Appendix B.2 (split augmented excision) | `thm:B2` | Theorem 5.2 |
| Appendix C.1–C.2 (Künneth over places) | `thm:kunneth` | Theorem 5.3 |
| Appendix D.1 (orthogonal sums) | `lem:orthsum` | Lemma 5.4 |
| Appendix D.2 (non-unit twists), (D.1) | `lem:nonunit` | Lemma 5.5 |
| Appendix D.3 / Corollary D.4 (unit twists), (D.2) | `lem:unit` | Lemma 5.6 |
| Appendix D.4 caveat (`u ≢ 1 mod p`, `p=7`, `u=−1`) | `rem:closure` | Remark 5.7 |
| Theorem 7.1(a),(b),(c) | `thm:shadow` | Theorem 5.8 |
| Remark 7.3 (why no torsion) | `rem:notorsion` | Remark 5.9 |
| Corollary 7.5 (additive invariants blind) | `cor:blind` | Corollary 5.10 |
| Definition 8.1 (`τ_v`) | `def:tau` | Definition 6.1 |
| Lemma 8.2 | `lem:tau` | Lemma 6.2 |
| Remark 8.3 (unit-group divergence) | `rem:unitdiv` | Remark 6.3 |
| Lemma 8.4 (inversion invariance) | `lem:inv` | Lemma 6.4 |
| Remark 8.6a (8.5a), (8.5b) | `eq:tauinf`, `eq:archmeasure` | §2.3, §6.1 |
| Definition 8.6 (the trace), (8.5), (8.5∞) | `def:trace` | Definition 6.5 |
| Theorem 8.8 (absolute convergence off the identity) | `thm:absconv` | Theorem 6.6 |
| Theorem 8.9 (uniqueness off the identity) | `thm:unique` | Theorem 6.7 |
| Theorem 8.10 (comparison with the analytic regularization) | `prop:comparison` | Proposition 6.8, **with (8.10) as an explicit hypothesis** |
| Remark 8.11 (diagonal not trace class) | `rem:diagonal` | Remark 6.9 |
| Definition 8A.7d (`c := 0`) | `conv:c` | Convention 6.10 (see (b)) |
| Theorem 9.5 (separation) | `thm:separate` | Theorem 6.11 |
| Theorem 8A.9 / (8A.24)–(8A.24′) | `prop:haarrank` | Proposition 6.12 |
| Theorem 9.1 (external Tate characters) | `thm:tate` | Theorem 7.1 |
| §9.3.1 dual group, (9.6)–(9.8) | `eq:dual`, `eq:FT`, `eq:lambdaFT` | §7.2 |
| Theorem 9.7 (the symbol) incl. (9.14) | `thm:symbol`, `eq:conductor` | Theorem 7.2 |
| Remark 9.7a (what `T̂` is) | `rem:symbolshape` | Remark 7.3 |
| Theorem 9.7b (Mittag–Leffler, Tate residues, contour identities) | `thm:ML` | Theorem 7.4 |
| Remark 9.7c | `rem:MLconseq` | Remark 7.5 |
| Definition 9.2, Theorem 9.3 | `def:pairing`, `prop:bilin` | Definition 8.1, Proposition 8.2 |
| Theorem 9.4 (radical is a closed dagger ideal) + `T|𝓝 = 0` | `prop:ideal` | Proposition 8.3 |
| **Theorem 9.8 (`𝓝 = 0`)** | `thm:radical` | **Theorem 8.4** |
| Definition 9.10, Theorem 9.11 | `def:prim`, `prop:NW` | Definition 8.6, Proposition 8.7 |
| Theorem 9.12 (exact Tate sequence; primitive sector nonzero, nondegenerate) | `thm:tateseq` | Theorem 8.8 |
| Theorem 9.13(a),(b) (no splitting) | `thm:nosplit` | Theorem 8.9 |
| Remark 9.13a (a weak hyperbolic plane is not the ruling plane) | `rem:weakhyp` | Remark 8.10 |
| Theorem 9.14 (the separated completion) | `thm:completion` | Theorem 8.11 |
| Lemma 9.14a0 | `lem:Nseminorm` | Lemma 8.12 |
| Theorem 9.14a (rulings as limits of spread Tate characters) | `thm:rulings` | Theorem 8.13 |
| Theorem 9.14b (canonical splitting of the completion) | `thm:splitting` | Theorem 8.14 |
| Theorem 9.14c (rulings are the scalar radical) | `thm:rulnull` | Theorem 8.15 |
| Definition 9.14c0 (admissible approximations) | `def:admissible` | Definition 8.16 |
| Theorem 9.14c′ | `thm:rulnullclass` | Theorem 8.17 |
| Remark 9.14c″ | `rem:noextension` | Remark 8.18 |
| Remark 9.14d(1),(4) | `rem:nocontradiction` | Remark 8.19 |
| Definition 8A.1, (8A.0), (8A.0′) | `def:Corrtr`, `lem:slaws` | Definition 9.1, Lemma 9.2 |
| Theorem 8A.10 (`F ↦ E_F` faithful) | `prop:faithful` | Proposition 9.3 |
| Theorem 8A.11 (what is and is not required of a trace of cycles) | `rem:cycles` | Remark 9.4 |
| Definition 8A.2 / 8A.2′ (target, metric (8A.10″)) | `def:target` | Definition 9.5 |
| Theorem 8A.3 (additivity) | `thm:additivity` | Theorem 9.6 |
| Theorem 8A.4 (cyclicity, dagger-reality) | `thm:cyclic` | Theorem 9.7 (reality proved as Prop. 8.2) |
| Proposition 8A.8 (invariance) | `prop:invariance` | Proposition 9.8 |
| Definition 8A.7b0 (`‖·‖_tr`), (8A.15), (8A.15′) | `def:trnorm` | Definition 10.1 |
| Theorem 8A.7b(a)–(f) (Banach dagger-algebra, germ, multiplicativity) | `thm:banach` | Theorem 10.2 |
| Remark 8A.7b0a (why the corrected norm) | `rem:whynorm` | Remark 10.3 |
| Remark 8A.7b1 (two determinants) | `rem:twodets` | Remark 10.4 |
| Definition 3.7, Theorem 3.8(a)–(d) (chart system) | `def:chartsystem`, `thm:chartsystem` | Definition 11.1, Theorem 11.2 |
| Theorem 8A.5 / (8A.12) (chart comparison) | `thm:chartcomp` | Theorem 11.3 |
| Proposition 3.9 (restriction does not preserve the trace) | `prop:resnotrace` | Proposition 11.4 |
| Theorem 8A.7c(a)–(e) (colimit trace) | `thm:colimtrace` | Theorem 11.5 |
| Definition 10.1 / 10.2a (effectivity) | `def:eff` | Definition 12.1 |
| Theorem 10.2 | `thm:cone` | Theorem 12.2 |
| Proposition 10.2b | `prop:effsmear` | Proposition 12.3 |
| Theorems 10.3 / 10.3a (properness) | `thm:properness` | Theorem 12.4 |
| Theorem 10.3b (properness in the completion) | `thm:coneproper` | Theorem 12.5 |
| Theorem 10.3c | `thm:coneRR` | Theorem 12.6 |
| Remark 10.3d (two cones) | `rem:twocones` | Remark 12.7 |
| Definition 10.6a (`λ_per`) + its biextension laws | `def:lper`, `lem:lperbiext` | Definition 13.1, Lemma 13.2 |
| Definitions 10.6b, 10.6c (`L_S`, `λ_RR`), (10.9) | `def:RR` | Definition 13.3 |
| Theorem 10.8 (scalar determinant trivial on the rulings) | `thm:scalartrivial` | Theorem 13.4 |
| Remark 10.8a(1)–(3) | `rem:whyblind` | Remark 13.5 |
| Theorem 10.6a (no functor through the Tate fibre) | `rem:notafunctor` | Remark 13.6 (with its hypothesis stated, and proof) |
| **Theorem 10.7(a)–(g)** | `thm:RR` | **Theorem 13.7** |
| §10.3.3 "What A.8's closure actually consists of" | `rem:whatRRis` | Remark 13.8 |
| Theorem 10.9(a)–(c) (base change along the Tate boundary; Tor) | `thm:basechange` | Theorem 13.9 |
| Proposition 10.6 (contact determinant is blind) | `prop:contactblind` | Proposition 13.10 |
| Theorem 6.1 (classical control) | `thm:classical` | Theorem 14.1 |
| "What Theorem 6.1 does not assert" + further limitations | `rem:classicalscope`, `rem:effcone` | Remarks 14.2, 14.3 |
| §11bis item 5(i)–(iii),(v) (bidegree, normalized relation, rulings) | `rem:invertible` | Remark 14.4 |
| **Theorem 14.1 (signature)** | `thm:signature` | **Theorem 15.1** |
| Theorem 10.8b (Mertens limit in the colimit chart) | `thm:mertens` | Theorem 15.2 |
| Remark 10.8c | `rem:mertensmeaning` | Remark 15.3 |

Classical inputs imported with citations: Eilenberg–Zilber / Eilenberg–Mac Lane
(Mac Lane, *Homology*, VIII.8); Wodzicki excision and its Fréchet/bornological
form (Wodzicki 1989; Meyer 2007; Cuntz–Quillen 1997); the six-functor
formalism for perfect kernels (SGA 6); the closed form of the archimedean
Weil distribution (Weil 1952; Connes–Consani 2021); Mertens' theorem
(Mertens 1874); Tate's thesis for the local zeta functionals; Knudsen–Mumford
and Deligne for the determinant target and the biextension language;
Weil 1948 for the classical model.

---

## (b) Excluded items, one line each

* **All status vocabulary, clause ledgers, obstacle tables, verdicts, audit
  findings and dissents, panel records, owner decisions, amendment proposals
  (§§12–14 of the Markdown), and every "[phase …]"/"[REBUILT …]" note** —
  research bookkeeping, not mathematics.
* **§13.1–13.8 "What was tried and withdrawn"** — withdrawn routes, false
  intermediate statements and superseded formulations; excluded by the
  instruction to include only what is built and proved.
* **Theorem 7.4 (isomorphic shadows)** — explicitly withdrawn in the Markdown.
* **Theorem 7.1(d) (real place: `HH(E_R,E_R)` and the boundary corner bar)** —
  its proof rests on repository notes (HKR for the smooth boundary source, the
  corner bar and its dichotomy) that are neither reproduced nor citable to the
  literature, and nothing downstream uses it.
* **Theorem 8A.7 / display (8A.13)–(8A.13′) (Fredholm-determinant
  realization of `exp T`)** — depends on the imported cutoff trace theorem and
  carries an undetermined constant; the Markdown itself states that nothing in
  the paper uses it. The comparison with an analytic regularization survives as
  Proposition 6.8, with the cutoff asymptotic as an explicit hypothesis.
* **`𝓝_∞ = 0` / `𝓝_∞^W = 0` for the colimit, and the sequence (3.10)** —
  explicitly not claimed in the Markdown; a sentence in §11 records that no
  colimit radical statement is made.
* **`c_cut`** — undetermined in the Markdown; retained only as the unnamed
  constant of Proposition 6.8.
* **The "row D target" box, §14.1 items addressed to other papers, §14.1a
  ("what rows B and C may use"), and all cross-paper traffic** — programme
  material.
* **Remark 9.14d(2),(3) and the P123.007 boundary-radical comparison** —
  a comparison with an object not constructed here; the mathematical content
  (the scalar radical of the completion is exactly the ruling plane) is kept
  as Theorem 8.15(a).
* **Theorem 9.7(d′) as a separate numbered item** — merged into
  Theorem 7.2(d), where the termwise interchange is stated as `eq:plancherelv`.

---

## (c) Statements whose Markdown proof I judged incomplete — flagged, not
silently completed

1. **`Hom_{U-U}(E_a,E_b) = C·U_γ` for `a = γb`, `0` otherwise** (Markdown
   (3.3), Remark 3.6, import `Tr`). The Markdown states plainly that the
   *arguments* transfer to the source algebra `U` of (2.4) but that the
   *conclusion* rests on freeness of the lattice action on the open stratum,
   which is proved for a different coefficient algebra and **not** for `U`.
   In the article this is **Hypothesis 3.1**, stated as such, with the three
   verified properties and the unverified one named explicitly; the two
   results that use it — Proposition 3.5(iv) (infinitely many pairwise
   non-isomorphic objects), the vanishing `eq:HomUN`, and Theorem 4.3 (the
   dagger) — carry the hypothesis
   in their statements. Nothing else in the article depends on it.

2. *(Withdrawn after review R1 — the finding was wrong.)* The first issue of
   these notes stated that Theorem 8A.12 does not exist in `main.md`. It does:
   `main.md` lines ~2096–2155 state and prove it, together with
   Remark 8A.12a. It was absent from the copy of §8A.3quater read during the
   conversion. It is now in the article as Theorem~10.3 (`thm:Atrcat`) with
   its full proof, and Remark 8A.12a as Remark~10.4
   (`rem:whichcompletion`); see the repair log below.

3. *(Restated after review R1.)* **Theorem 7.1(a) (label splitting).** The collapse of the group factors and
   its continuity are justified in the Markdown by citing a crossed-product
   comparison in a repository note that is not reproduced. I have written out
   the argument to the level the Markdown supplies (label preservation by the
   twisted Hochschild boundary; collapse onto one gauge unitary; Koszul complex
   of a free abelian group of finite rank), and the continuity step is
   asserted with its reason ("finite signed sums of multiplications and gauge
   translations in each degree") rather than proved from first principles.
   After review R1 this is no longer an informal flag: the label splitting is
   proved in full, and the collapse of the label piece is carried by the
   explicit **Hypothesis 5.9** (`hyp:crossed`), with the algebraic statement
   cited to Nistor, Getzler–Jones and Brylinski. See the repair log below.

4. *(Withdrawn after review R1: the closed form is now derived in the
   article; see the repair log, M7.)* **The closed form
   `Ŵ_∞(0,τ) = log π − Re ψ(1/4 + iτ/2)`** (Markdown
   Theorem 9.7(b), quoting a repository computation). The article proves the
   asymptotic `−log|τ| + O(1)` from scratch, uniformly in the parity, and
   imports the closed form as the classical evaluation of the archimedean Weil
   distribution, with citations (Weil 1952; Connes–Consani 2021). It is used
   for the explicit constant in Theorem 15.1(c) and for the Mittag–Leffler
   expansion of Theorem 7.4(b).

5. *(Withdrawn after review R1: the freeness used there is the elementary one
   and is now proved in one line; see m1 in the repair log.)*
   **Theorem 12.2(a) (intrinsic characterization of the effective cone).** The
   Markdown's proof appeals to freeness of the lattice action on the open
   stratum of `X_S` — the same unproved input as in item 1 — for the converse
   direction. The article reproduces the argument, including that appeal; it is
   the only place outside Hypothesis 3.1 where freeness is used, and the
   forward direction (nonnegative coefficients ⇒ positive row measures) is
   unconditional.

6. **Corollary 3.2 / Proposition 12.3 (the coefficient of `E_F` at the label
   `u` is exactly `F(u)`).** This is proved in the Markdown from the strict
   trivialization of the Fell bundle by the splitting; the underlying Fell
   bundle formalism itself is not reproduced. In the article the smearing map
   is *defined* by the displayed integral in the fixed trivialization, so the
   statement is definitional there, and the second, operator-theoretic proof of
   injectivity (Proposition 9.3) is independent of it.

7. **Proposition 6.8 (comparison with an analytic regularization)** is stated
   with the cutoff asymptotic as an explicit hypothesis, since the Markdown
   imports it and declines to import its constants. No result of the article
   depends on this proposition.

---

## Compilation

`pdflatex -interaction=nonstopmode main.tex`, run three times. No errors, no
undefined references, no undefined citations, no LaTeX warnings other than the
usual rerun notice on the first pass. Four overfull `\hbox` boxes remain, all
in displayed formulas, none exceeding the text block visibly.


---

## Repairs after review R1

The hostile referee report `TEX_HOSTILE_REVIEW_R1.md` (verdict: major repairs
needed; one blocking finding B1, seven major findings M1–M7, one fidelity
finding D1, nine minor findings) has been applied in full. Line numbers refer
to the repaired `main.tex`.

### B1 — the excision inputs are now proved

The four facts that carried §3.2 (relative projectivity of `I_J` on each side,
summability of the adapted partition, `I_J ⊗^L I_K ≅ I_{J∪K}[0]`, and the Čech
resolution with its two vanishings) were asserted without proof. They are
genuinely proved in the sources `P123.124` §§2–5 and `P123.125` §§1–3, and the
proofs have been written out in the article:

| statement | tex label | location |
|---|---|---|
| the ideals `I_J`, the finite coefficient decomposition | `eq:UJ`, `eq:Ldecomp` | ll. 656–681 |
| the adapted partition and its summability estimate | Lemma 3.6 `lem:partition`, `eq:partition`, `eq:summable` | ll. 685–758 |
| relative projectivity on each side; contractibility of the bar complex | Lemma 3.7 `lem:projective` | ll. 760–796 |
| `I_J ⊗_U I_K ≅ I_{J∪K}` and the derived form | Lemma 3.8 `lem:idealproduct`, `eq:idealprod` | ll. 798–828 |
| the Čech resolution, its admissible exactness, and the two vanishings | Lemma 3.9 `lem:cech`, `eq:cechvanish` | ll. 830–893 |

Nothing had to be demoted to a hypothesis: all four are proved in the sources,
and the proofs are elementary for the shell-idempotent partition, as the
referee anticipated. Lemma 5.1 (H-unitality) now derives its contraction from
Lemma 3.7 instead of restating it, and Lemma 3.11 (`lem:excvanish`) cites
Lemmas 3.6 and 3.8 rather than an unproved display.

### M1 — the crossed-product collapse

The label splitting of the Hochschild complex is proved in full (it is
elementary). The collapse of the label-γ piece onto the coefficient complex
tensored with the group homology of `Γ_S` is the crossed-product decomposition
of Hochschild homology; the algebraic statement is now cited precisely —
Nistor, *Invent. Math.* **99** (1990), §§3–4; Getzler–Jones, *J. Reine Angew.
Math.* **445** (1993), §3; Brylinski — and the continuity of the comparison in
the complete Fréchet setting is isolated as **Hypothesis 5.9**
(`hyp:crossed`, ll. 1297–1330), on which Theorem 5.10(a) (`thm:shadow`) is now
explicitly conditional. The Koszul form of `H_*(Z^d, −)` is stated with the
differentials `α_{g_i} − 1`, rather than as a plain tensor product, so no
triviality of the lattice action is assumed. Only Corollary 5.12
(`cor:blind`) and Proposition 13.10 (`prop:contactblind`) inherit the
hypothesis; §§6–15 are independent of it, and the article says so.

### M2 — the positive-degree vanishing for a shell algebra

Removed rather than assumed. The two unproved assertions ("the untwisted
contraction, which proves `H_n(F) = 0` for `n ≥ 1`") are deleted. Lemma 5.6
(`lem:unit`) now computes `HH_0` only, which is all that is used, and
Remark 5.7 (`rem:higherdegrees`) states exactly why the positive-degree
statement is not made: the separability idempotent of the level-`N`
subalgebra is a separability idempotent for that level alone, and its size in
the seminorms (2.2) is not bounded uniformly in `N`, so the level homotopies do
not pass to an admissible contraction of the limit. Theorem 5.10(c),
Corollary 5.12 and Proposition 13.10 are rephrased through `HH_0`; the
conclusions are unchanged, since infinite-dimensional `HH_0` already kills
every finite rank, Euler characteristic and determinant line. The non-unit
case (Lemma 5.5) is unaffected: there the twisted complex is contractible in
all degrees and the contraction is exhibited.

### M3 — Wodzicki excision

Now stated as an explicitly labelled import (ll. 1168–1194): the hypotheses
(complete nuclear Fréchet algebra, closed ideal admissibly H-unital with a
continuous linear contraction of its bar complex, continuous automorphism
preserving the ideal), the conclusion (a distinguished triangle of twisted
Hochschild complexes), the attribution (Wodzicki for the algebraic untwisted
theorem, Cuntz–Quillen and Meyer for the complete bornological framework), and
a sentence saying exactly why the twisted case is the same argument. The
hypotheses are checked against §2.2 in the same paragraph.

### M4 — `Hom_{U-U}(U, N) = 0`

Now displayed as equation `eq:HomUN` and explicitly conditional on
Hypothesis 3.1, with the argument written out: centrality against the gauge
unitaries, the freeness input named as the hypothesis it is, and the vanishing
of the invariant identity coefficient derived from the seminorms (2.2).

### M5 — the count

Corrected: Hypothesis 3.1 is used in three places, now listed —
Proposition 3.5(iv), the vanishing `eq:HomUN` and the sentence after
Proposition 4.1, and Theorem 4.3.

### M6 — the duality formula for a graph

Proved, not asserted. The comparison functor is changed to the untwisted
`Φ(E_λ) = O_{Γ_{φ(λ)}}`, and part (c) is now the displayed identity
`eq:dualitygraph`, `D_h(O_{Γ_f}) ≅ O_{Γ_{f^{-1}}} ⊗ p_1^*h ⊗ p_2^*h^{-1}`,
derived from the fundamental local isomorphism for a regular embedding
(cited to Hartshorne, *Residues and Duality*, Ch. III §7), the identification
of the normal bundle of `Γ_f` with `T_C`, the relation `σ ∘ i_f = i_{f^{-1}} ∘ f`,
the projection formula and `h² = ω_C`. A short computation is added showing
that the half-density twist **cannot** be absorbed by renormalizing the functor:
for `Ψ(E_λ) = i_{f*}(h^a ⊗ f^*h^b)` equality would force `a = 1−b` and
`b = −a−1`, i.e. `0 = −2`. The statement of Theorem 14.1(c) is weakened
accordingly, and is now exactly what is proved.

### M7 — the archimedean closed form

No longer an import. `Ŵ_∞(0,τ) = log π − Re ψ(1/4 + iτ/2)` is now **derived**
from Definition 6.5 in one paragraph: substituting `u = 2t` turns the
regularized integral into `∫_0^∞ [½(e^{−αu}+e^{−ᾱu}) − e^{−u/2}]/(1−e^{−u}) du`
with `α = 1/4 + iτ/2`, and Gauss's integral representation of the digamma
function gives `ψ(1/2) − Re ψ(1/4 + iτ/2)` with `ψ(1/2) = −γ − 2log 2`; the
constant `γ + log 4π` of (6.6) then produces `log π` exactly. The monotonicity
of `Re ψ(1/4 + iτ/2)` in `|τ|`, which turns the closed form into the maximum
(15.2), is proved from the Gauss series: each subtracted term
`(n+¼)/((n+¼)² + τ²/4)` is positive and decreasing in `|τ|`. Gauss's digamma
theorem `ψ(1/4) = −γ − 3log 2 − π/2` is cited to DLMF §5.4(iii), and the
integral representation to DLMF §5.9. Flagged item 4 of §(c) above is therefore
withdrawn: the archimedean backbone is now self-contained.

### D1 — Theorem 8A.12 restored

Theorem 10.3 (`thm:Atrcat`) with parts (a)–(d) and full proof, plus
Remark 10.4 (`rem:whichcompletion`), inserted after Theorem 10.2. Proposition
9.3 (`prop:faithful`) is kept as the statement over `D_A` and now points
forward to part (b), whose proof is noted to use nothing beyond
`𝓐_tr ⊆ L¹(C_S)`. The abstract and the introduction are updated to record that
the completion carries objects and is closed under trace-norm limits of
presentations with a common finite support.

### Minor findings

* **m1** — the freeness used in Theorem 12.2(a) is the elementary one
  (`γ x_∞ = x_∞` with `x_∞ ≠ 0` and `γ ∈ Q_{>0}` forces `γ = 1`); the line is
  added, and flagged item 5 of §(c) is withdrawn.
* **m2** — the Mellin surjectivity in Theorem 7.1 is now argued from the linear
  independence of `e^{t/2}`, `e^{−t/2}`, with a cross-reference to the fuller
  argument in Theorem 13.9(c).
* **m3** — the duplicate definition of `N` is removed; Definition 10.1 now
  refers to `eq:Nsemi`.
* **m4** — `L^{(q)}(F) := L_S^{(q)}(F,F)` is defined, and the cross-effect
  identity is proved rather than attributed to part (a).
* **m5** — the bound on `B(t)` is split into its two correct regimes, and the
  profile of `H'` is renamed `η` to remove the collision with the derivative.
* **m6** — Theorem 13.9(c) now says in one clause that `Tor` and `I²` are taken
  algebraically.
* **m7** — Corollary 5.12 records that the unit classes outside `1 + pZ_p` are
  not treated.
* **m8** — Convention 6.10's list is corrected: the identity of
  Proposition 6.12 is independent of `c`, only its last display uses `c = 0`.
* **m9** — the unused macros `\Ltr`, `\dg`, `\Spec` and the unused `example`
  environment are removed.

### Compilation after the repairs

`pdflatex -interaction=nonstopmode main.tex`, three passes from a clean state:
**0 errors, 0 warnings, 0 undefined references or citations, 0 overfull and 0
underfull boxes**. All four overfull boxes reported in §4 of the review are
fixed (the shell-part display in the proof of Theorem 7.2, the `R_∂` display,
the "new places" parenthetical in Theorem 11.3, and the partial-summation chain
in Theorem 15.2). **58 pages**, 15 sections, 19 bibliography entries, all
cited.

### Remaining declared inputs

After the repairs the article contains exactly two labelled hypotheses and one
labelled import, all three stated as such and all three localized:

1. **Hypothesis 3.1** (`hyp:hom`) — the classification of morphisms between
   graph bimodules for the source algebra (2.4); used in three places, listed
   in the text.
2. **Hypothesis 5.9** (`hyp:crossed`) — continuity, in the complete Fréchet
   setting, of the crossed-product decomposition of Hochschild homology; used
   only in Theorem 5.10(a), hence only in Corollary 5.12 and
   Proposition 13.10.
3. **The excision theorem** of §5.1 — Wodzicki's theorem in its complete
   bornological, twisted form, with hypotheses checked; used only in Step 3 of
   Theorem 5.3.

In addition, Proposition 6.8 carries the cutoff asymptotic as an explicit
hypothesis, and nothing in the article depends on that proposition.
