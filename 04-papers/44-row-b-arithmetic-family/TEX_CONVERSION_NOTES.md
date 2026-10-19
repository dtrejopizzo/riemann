# Conversion notes: `main.md` → `main.tex`

Target: `main.tex` (amsart 11pt), compiled to `main.pdf`, 45 pages, clean
compile (no errors, no warnings, no overfull boxes).

Title: *An Arithmetic Frobenius Family and its Integral Shadow on a
Correspondence Algebra of the Idele Class Group — Inverse semigroup structure,
two Gram forms, and the von Mangoldt function as a shell volume.*
The Riemann Hypothesis is nowhere mentioned. Zeros of zeta appear only in
Lemma 12.4 (`lem:singlefreq`), which is literally a statement about them, and
in Proposition 2.4/Remark 9.9 only as the digamma asymptotics of the
archimedean symbol.

## (a) Included statements: Markdown source → LaTeX label

### Imported from the companion paper (stated, not reproved)

| Markdown | LaTeX | form |
|---|---|---|
| Paper 43 Lemma 3.3 (valuation splitting) | `prop:splitting` | cited proposition |
| Paper 43 (9.5b) (slice maps) | `prop:slices` | cited proposition |
| Paper 43 Def. 8.5, 8.6, (8.5), (8.5∞), Lemma 8.2, Thm 8.8, Thm 8A.7c, Rem. 8.11 | `prop:trace` | cited proposition, (a)–(d) |
| Paper 43 Thm 9.1, (9.2), (9.11), (9.12b), (9.13), Thm 9.7 | `prop:tate` | cited proposition |
| Paper 43 Thm 9.8, 9.14, 9.14a0, 9.14b | `prop:completion` | cited proposition |
| Paper 43 Thm 7.1(c), Thm 8A.9 | `prop:shadow` | cited proposition |
| P123.022 §2 Proposition (no `Z/p` from a `C`-linear additive functor) | `prop:noZp` | **restated with full proof** (two lines) |

### Proved here

| Markdown | LaTeX |
|---|---|
| Lemma 3bis.1 | `lem:classunit` |
| Prop. 3bis.2 | `prop:noslice` |
| Remark 3bis.2a | `rem:minimalchart` |
| Cor. 3bis.3 | `cor:liftnotcontact` |
| Lemma 3bis.3b | `lem:notideal` |
| Def. 3bis.4 | `def:normclass` |
| Remark 3bis.4a | `rem:whatthecosetis` |
| Remark 3bis.4b | `rem:multiplier` |
| Thm. 3bis.5 | `thm:radmonoidal` |
| Remarks 3bis.5a, 3bis.5b, 3bis.5c (merged) | `rem:whatisrealized` |
| Def. 3bis.6 | `def:smeared` |
| Lemma 3bis.6a | `lem:smeared` |
| Thm. 3bis.7 | `thm:radtrace` |
| Def.–Thm. 3bis.8 | `thm:repmeasures` |
| Thm. 3bis.8 type warning (F2 block) | `rem:typewarning` |
| Thm. 3bis.7′ | `thm:contactlocus` |
| Remark 3bis.8a | `rem:typesdiffer` |
| Remark 3bis.8b | `rem:lambdaderived` |
| Thm. 8.3 (norm classes in `N_A^dist`) | `thm:radincompletion` |
| Def. 3ter.1 | `def:localfrob` |
| Def. 3ter.2 | `def:frob` |
| Lemma 3ter.3 | `lem:frobsupport` |
| Thm. 3ter.4 | `thm:frobmonoidal` |
| Remark 3ter.4a (no interpolation) | `rem:nointerp` |
| Prop. 3ter.5 | `prop:avgtorad` |
| Thm. 3ter.6 | `thm:frobdagger` |
| Remark 3ter.6a | `rem:weildegree` |
| Thm. 3ter.7 (inverse semigroup, incl. the (iv) counterexample) | `thm:invsemigroup` |
| Def. 3ter.8 | `def:smearedfrob` |
| Lemma 3ter.9 | `lem:smearedfrobinDA` |
| Thm. 3ter.10 | `thm:frobcontact` |
| Cor. 3ter.10b | `cor:frobnoarch` |
| Remark 3ter.10a | `rem:profilevalue` |
| Cor. 3ter.11 | `cor:frobinvariant` |
| Remarks 3ter.11a, 8bis.8c (merged) | `rem:lambdaisownvolume` |
| Thm. 3ter.12 | `thm:compositedisjoint` |
| Def.–Prop. 3ter.13 | `prop:archflow` |
| Remark 3ter.13a | `rem:twoflows` |
| Thm. 3ter.14 (Frobenii in `N_A^dist`) | `thm:frobincompletion` |
| Lemma 3.1 (deformation) | `lem:deformation` |
| Thm. 3.3 | `thm:separation` |
| Thm. 3.3 `[REBUILT]` block on the lift; Cor. 3.4 | `rem:aboutthelift` |
| Remarks 3.5, 3.6 (merged) | `rem:whatsep` |
| Lemma 4.5 | `lem:tauinv` (Remark 4.7 folded into the following paragraph) |
| Def. 4.1 | `def:labelcat` |
| Thm. 4.3 | `thm:realization` |
| Thm. 4.4 | `thm:unittransphalf` |
| Lemma 5.1 | `lem:mobiuscube` |
| Def. 5.2 | `def:degdet` |
| Thm. 5.3 | `thm:degreelaw` |
| Cor. 5.3a | `cor:ghost` |
| Thm. 5.4 | `thm:notmonoidal` |
| Cor. 5.5a | `cor:notadditive` |
| Cor. 5.5 | `cor:structurethatholds` |
| Thm. 6.1 | `thm:indexcomplex` |
| Remark 6.2 | `rem:complexshadow` |
| Thm. 6.3 (four models) | `thm:fourmodels` |
| Thm. 6.4 | `thm:discriminating` |
| Thm. 6.5 | `thm:carrierside` |
| Remarks 6.5a′, 6.5a (merged) | `rem:nomapsupplied` |
| Thm. 3bis.10 | `thm:degreematching` |
| Remarks 3bis.10a, 3bis.10b | `rem:whatdegmatchdoesnotsay` |
| Def. 6bis.1 | `def:shadow` |
| Lemma 6bis.2 | `lem:shwelldef` |
| Thm. 6bis.3 | `thm:shstructure` |
| Thm. 6bis.4 | `thm:shdegrees` |
| Lemma 6bis.3a | `lem:shfunctor` |
| Def. 6bis.3b | `def:dirichletpolycorr` |
| Thm. 6bis.3c | `thm:additiveext` |
| Remarks 6bis.3d, 6bis.5 (merged) | `rem:shadowlimits` |
| §8bis (C1), (C2) conventions | unnumbered paragraphs opening §9 |
| Thm. 8bis.1 | `thm:gramoff` |
| Thm. 8bis.1b | `thm:gramdiag` |
| Cor. 8bis.1b′ | `cor:gramdiagconv` |
| Remark 8bis.1c | `rem:nodiagonal` |
| Cor. 8bis.1d | `cor:onlyfinite` |
| Thm. 8bis.1e | `thm:fullweil` |
| Thm. 8bis.1′ | `thm:twohalves` |
| Def. 8bis.3 (complex profiles, (8bis.8c)) | `lem:complexprofiles` |
| Def. 8bis.3 (primitivity, (8bis.9)) | `def:primitive` |
| Thm. 8bis.4(iv)(a) | `prop:formsdiffer` |
| Thm. 8bis.4a | `thm:qfinpositive` |
| Remark 8bis.4b(1) | `rem:qfinscope` |
| Thm. 8bis.2 | `thm:infgenus` |
| Cor. 8bis.2a, Remark 8bis.2b (merged) | `rem:infinitegenus` |
| Thm. 8bis.8 | `thm:tateresidue` |
| Cor. 8bis.8a | `cor:uniquenorm` |
| Remark 8bis.8b | `rem:notchartinv` |
| Lemma 8bis.5 | `lem:traceontinuity` |
| Lemma 8bis.6 | `lem:riemannsum` |
| Lemma 8bis.6a | `lem:C1control` |
| Lemma 8bis.6b | `lem:singlefreq` (+ scope note `rem:singlefreqscope`) |
| §7 tables + checks 1–4 | §13, two tables + three structural facts |
| Prop. 7.1 | `prop:bystructure` |

## (b) Excluded items, with reason

- **Header banner, status blocks, `[phase …]` / `[REBUILT …]` / `[CORRECTED …]`
  annotations, §9bis (W1–W23 withdrawals), §10 (verdict and clause ledger),
  §10.4 (decision of record), §11 (dependencies), §2 (acceptance contract
  B.1–B.9), §9 (handover to row C):** provenance and project bookkeeping, not
  mathematics. Their mathematical content, where any, is already in the
  theorems listed above.
- **Theorem 8bis.4(ii) (explicit formula as an import) and 8bis.4(iii) (Weil's
  criterion, the equivalence with RH):** cited-classical, and the title
  constraint forbids the RH statement; neither is proved in the source.
- **Theorem 8bis.4(v), (vi) and the boxed "row D target":** marked `OPEN` /
  programme statement.
- **Theorem 8bis.7 (conditional transfer theorem):** its hypothesis `(H_L)` is
  `OPEN` and part (c) is `OPEN`; the statement as a whole is not a theorem. Its
  *proved* analytic machinery — Lemmas 8bis.5, 8bis.6, 8bis.6a, 8bis.6b — is
  fully included as §12.
- **Remark 8bis.7a (what fails, and by how much), incl. the indicative
  threshold `2α < δ + 1/4`:** explicitly labelled in the source as "an
  indicative threshold on the natural sizes, not a theorem".
- **Theorem 8.2 (independence of zeros/positivity):** a meta-statement about
  the paper's own dependency list, not a mathematical theorem; its substance is
  carried by the absence of such inputs.
- **Theorem 8.1(i)–(iv):** (i)–(ii) are restatements of Theorem 4.3 and of the
  definition of the pairing; (iii)–(iv) are corrections of withdrawn earlier
  claims whose surviving positive content is Theorem 3bis.5(iii) and Theorem
  3bis.7 — both included. Nothing is lost.
- **§6.2a and §6.2a′ (the amended clause B.4 box):** contract text. Its
  mathematics is exactly Theorem 6.3a, which is in turn subsumed by
  `thm:repmeasures` + `thm:degreematching` + `thm:shdegrees`, all included with
  full proofs. Theorem 6.3a itself is therefore not duplicated.
- **Remark 6.5a's "dictionary entry" and Remark 3bis.7′a:** explicitly
  non-theorems in the source.
- **§9.4 (history of a withdrawn cross-reference to Paper 45 §11):** project
  history.
- **Numerical verification script reference:** replaced by the tables, which
  are stated to be checks and not sources.

## (c) Statements whose Markdown proof was incomplete

All six items below were flagged in the first conversion; after the review of
 four of them are resolved, one is corrected as a genuine error of
the source, and one remains a stated import.

1. **`thm:gramoff`, the convolution constant — this was a genuine mathematical
   error of the source, now corrected in both `main.tex` and `main.md`.** The
   source's constant `∏_{s∈S_f∖(P(m)∪P(n))} vol(1+s^N Z_s)`, and the claim that
   it equals `1` in the flat convention, are false whenever `P(m) ≠ P(n)`: at a
   place of `P(m) △ P(n)` one factor carries a coset indicator and the other
   carries no condition, and their convolution contributes a further
   `vol(1+s^N Z_s)`. The correct constant is
   `∏_{s∈S_f∖(P(m)∩P(n))} vol(1+s^N Z_s)` (`eq:gramconst`), the proof now
   contains the four-case computation, `V_N^{(m,n)}` in `cor:onlyfinite` is
   redefined accordingly, and the flat-convention value is
   `∏_{s∈S_f∖F} vol(1+s^N Z_s)^{-1}`, which is `1` only when `F = S_f`. My
   earlier diagnosis of this flag ("shifted cosets") was itself wrong: the
   failure is at the places of the symmetric difference. The atom mass
   `eq:gramfinite`, the archimedean indicator `eq:gramarch` and the index set
   `F = P(m)∪P(n)` are unaffected, so `thm:twohalves` and `thm:fullweil` stand.
   `main.md` Theorem 8bis.1 and Corollary 8bis.1d are corrected in place and
   the correction is recorded in the new `main.md` §12 as **K1**.
2. **`thm:frobincompletion`(ii), uniformity in `N` — resolved.** The proof now
   fixes `B` first, hence `N_B` and `d_{N_B}`, observes that every `G ∈ B` is
   `U_{N_B}`-invariant so that the integrand is supported on the same
   `d_{N_B}` components for every `N ≥ N_B`, and exhibits the constant
   `C_B := d_{N_B} C''_B max(A_S,B_S)`, independent of `N`. The joint limit is
   then legitimate.
3. **`lem:singlefreq`(ii), the Laplace sizes — resolved by weakening to what
   is proved.** The `≍` claims and the saddle-point sentence (which is correct
   only for one order of vanishing of `ψ` and was in any case never computed)
   are deleted. What is now stated and proved is the exponential scale alone:
   with `a = inf supp ψ`, `b = sup supp ψ`,
   `lim (1/L) log ĝ_L(ρ_0) = δb` and `lim (1/L) log ĝ_L(1−ρ̄_0) = −δa`, hence
   the resonant pair has scale `δ(b−a) ≤ δ/2`. Part (iii) now claims only that
   the mismatched pair is bounded in modulus by the resonant one, and the
   hypothesis `0 < δ < 1/2` is explicit.
4. **`thm:fourmodels`(c),(d) — proofs supplied by me, and (d) restated.** The
   proofs of (c) and (d) are mine rather than the source's, and were verified
   independently in review. Statement (d) was additionally wrong as framed:
   `[Z[t] → Z[t]]` is not an object of `D(Z)`. The preamble now says that
   (a)–(c) agree in `D(Z)` while (d) is the complex `K_n ⊗_Z Z[t]` of
   `Z[t]`-modules whose specialisation at every `t = c ∈ Z` is `K_n`.
5. **`thm:degreelaw`, `log|Φ_n(1)| = Λ(n)` — proof supplied by me.** It is now
   a separate numbered statement, `lem:cyclotomicvalue`, with the restriction
   `n > 1` explained by `Φ_1(1) = 0`.
6. **`prop:shadow`, `prop:trace`(b),(c), `prop:tate` — stated imports.** These
   are load-bearing and are not proved here, by design. The phase
   normalization `ζ_p = p^{−1/2−iτ}` on the principal component, used by
   `thm:qfinpositive`, was used in the first version without being imported;
   it is now part of `prop:tate` (`eq:zetap`, `eq:nophase`) with the precise
   pointer, the carrier paper establishing `θ_p = arg ∏_{q≠p} κ_q(p)` and
   `θ_p = 0` on the principal component, where every `κ_q` is trivial.

## Repairs after review R1

Every finding of the adversarial review was applied. Grouped by kind.

**Blocking.**
- *A1.* The former §13 ("Nine labels, as a check"), including its two tables,
  its three "structural facts" and the defensive proposition, is deleted, as is
  the announcement of it in §1.5. A single unnumbered **Examples** table of
  seven values, prefaced by one sentence, now closes the integral-models
  section.
- *B1.* `Prim_n` now has a numbered definition (`def:prim`): the total cofiber
  of the radical cube indexed by subsets of `P(n)`, with its edge maps and a
  remark that the squares commute strictly. `thm:shstructure`(v) is restated
  for the radical cube and the apologetic parenthesis in its proof is replaced
  by the comparison-of-cubes argument.
- *B2.* New `lem:primstructure`: `Prim(N,P) ≃ Z/q` in degree `0` for
  `P = {q}`, `≃ 0` for `|P| ≥ 2`, by induction on `|P|`, hence
  `Prim_n ≃ [Z → Φ_n(1) → Z]`. `thm:degreelaw` is reduced to the degree
  identity and cites the lemma; `thm:fourmodels`(a), `thm:notmonoidal` and
  `thm:degreematching`(iii) now cite the lemma. The citation loop is gone.
  Mirrored into `main.md` as Definition 5.1a and Lemma 5.1b (record: §12 K2).
- *B5.* See §(c) item 1.

**Major.**
- *A2.* "Label" is replaced by "index" throughout (24 sites); `def:labelcat`
  is now `def:indexcat`, "The label category" is "The index category".
- *A3.* All six meta sentences deleted or reduced to their mathematical
  content.
- *B3.* `degdet` is redefined as `Σ_i (−1)^i log #H^i` on complexes of finite
  type, with a new `lem:degdetadd` proving additivity on direct sums, shifts
  and exact triangles from the long exact sequence. The ad hoc `m = 0` clause
  is deleted, and `eq:degreelaw` is no longer partly a stipulation.
- *B4.* `eq:cram` is now derived (`Ω = O·dz/z`, `π_n^*(dz/z) = n dz/z`, pull
  back along the identity section) with citations to Illusie and the Stacks
  Project; `eq:cfix` is honestly a **definition** — the Koszul complex of the
  fixed equation `w^{n−1} = 1` linearised at `w = 1` — and the ambient affine
  line is dropped, nothing downstream using it.
- *B6.* See §(c) item 6; the monotonicity of `2Re(ζ/(1−ζ))` in `cos θ` is also
  written out, so that `A_S = ω̂_fin(0)` is proved and not asserted.
- *B7.* `thm:tateresidue`(iv) and its proof paragraph are deleted; the theorem
  now has three parts, all proved, and `cor:uniquenorm` needs no more.
  `rem:notchartinv` is rewritten to use (i)–(ii) only.
- *B8.* See §(c) item 3.
- *B9.* `eq:diagdivnorm` now reads `−log(1/ε) + O(1)`; `C_φ` is deleted and a
  sentence says why no limiting constant is available.
- *B10.* See §(c) item 4.
- *B12.* See §(c) item 2.
- *C3.* This section.

**Minor.** `lem:traceontinuity` now cites the pointwise vanishing of the unit
packets established inside `thm:radtrace`'s proof, rather than the theorem,
whose support hypothesis does not hold here (B13); `thm:invsemigroup`(iii)
minimality is proved by exhibiting `Δ^{(F)}` and `Frob_{r,F}` as words in the
`Frob_n` (B14); `prop:trace` now defines `E_x` for a point of the carrier and
for an idele, with `E_x ⋆ E_y = E_{xy}` (B15); the companion paper carries a
year and a form of availability (C4); the five unused macros `\Div`, `\divv`,
`\Gr`, `\GL`, `\rk` are deleted (E1); §12's opening no longer claims
anything about the rest of the paper and §1.4 says that `lem:singlefreq` is
used by no other statement (F1); `lem:singlefreq` opens "Assume, for this
lemma only" and carries `0 < δ < 1/2` (F2); `lem:cyclotomicvalue` records that
`Φ_1(1) = 0` forces `n > 1` (B11).

**Compile after repair.** `pdflatex` three times from a clean state: 0 errors,
0 undefined references, 0 LaTeX or package warnings, 0 overfull or underfull
boxes, 47 pages. Ten pre-existing overfull display boxes (present in the
reviewed version and not reported by the review) were removed by rebreaking
the offending displays and one table.
