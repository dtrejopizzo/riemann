# Paper 46, Part IV (§§24–28) — adversarial review, round 1

*Reviewer of record: adversarial reviewer, 2026-09-19.  Target:
`04-papers/46-intersection-frame-defect/archive/main.md`, lines 10210–11940, with the writer's
record `PART_IV_NOTES.md`.  Sources of truth read in full:
`R147_005_CLOSING_DECISION.md`, `R148_005_CLOSING_DECISION.md`,
`R149_005_CLOSING_DECISION.md` (including §4 amendments),
`R149_003_REPAIRS.md`, `R150_005_CLOSING_DECISION.md`,
`R150_004_CONFIRMATION.md`; spot-reads of `R149_001` §§5–6,
`R147_003b` provenance rows, `main.md` §1.12 and §23.4.  Format modelled on
`PART_III_ADVERSARIAL_REVIEW_R1.md`.  No file other than this one was written;
`main.md` was **not** edited.*

## Verdict

**ACCEPT WITH REPAIRS.**  Three `MAJOR` findings must be discharged before Part
IV can stand as the closing record of row D.  All three are places where a
defect **that the phase-150 confirmation round or the phase-149 repair round
explicitly identified** was carried into the printed text rather than repaired;
none of them is a mislabelling that would convert a restatement into a
reduction, and none of them touches the decision of §28.4.

Everything the brief asked to be checked against the decisions of record
**matches**, with the exceptions listed below.  In particular: D.59 is framed as
a Hölder inequality and explicitly disclaimed as a transfer of Weil I 3.2
(Remark 26.4a); D.61.10 is restated as "no transport of the polar/positivity
structure" with the two classical transports written out (Theorem 26.17);
(P149) is reclassified as the Hardy–Littlewood `k`-tuple conjecture with
square-root error on average (Problem 26.20); D.62.2's sharp half is attributed
to Granville 2007 Thm 1A + Corrigendum 2008, with Bhowmik–Ruzsa as the quasi-RH
half only (Corollary 26.19); D.60.7′ is rescoped to `k = 1`, `c > 1/2` by
Siegel–Walfisz, with the Ω-check recorded (Remark 26.10a); (E) holds for all
`c < 1` and `(C′)` is `OPEN` (Lemma 26.3); T5's scope is narrow and large-value
counting is explicitly untouched (Remark 27.7a); Theorems 27.10–27.11 carry
`CLASSICAL`; Proposition 27.7 prints the round-one identity `‖b*b‖₂² = E(b)`
for every complex `b` with the archimedean family removed; T3 is a remark
conditional on (H-DMV) with the blocking open item (41) = O-150.1; Theorem 4.7,
Corollary 4.7a and Corollary 5.5 appear **only** in the §27 withdrawn table and
nowhere in the running text.  The §28.2 boxed statement cites only T1, T2, T5
and the classification (plus Corollary 18.17, which is part of T2's package in
§18) and claims nothing about the location of any zero.  No forbidden
vocabulary and no sentence hinting a sign was found; every section closes with
the explicit disclaimer.

---

## Findings

### 1. Theorem 27.11 (line 11476) and §28.2, fifth bullet (lines 11805–11807) — **MAJOR**

**The overstatement that `R150_004` D-2 ordered repaired is printed twice, once
inside a theorem and once inside the boxed statement of the wall.**

Theorem 27.11 concludes:

> "the hypothesis `A(x) ≪ x^{θ+ε}` is compatible with **any** prescribed zero
> configuration in `\mathrm{Re}\,s > θ`, and implies no statement whatever about
> the location of zeros."

The proof does not give this.  `P_{s_0}(s) = 1 − 2^{s_0}2^{-s}` vanishes on the
entire progression `s_0 + 2πik/\log 2`, so every planted point drags in
infinitely many companions, and multiplication by a Dirichlet polynomial can
never **remove** a zero of `D_a`.  `R150_004` D-2 states this and supplies the
one-line repair.  Remark 27.11a (line 11492) records the scope restriction
correctly — but a remark after the fact does not repair a theorem whose own
statement is false as written, and §28.2 then repeats the unmitigated form
("for which any prescribed zero configuration is compatible with the same power
saving") inside the one boxed display that is the paper's closing statement.

*Fix.*  Restate the conclusion of Theorem 27.11 in the form `R150_004` fixes:
"for **any finite** `S ⊂ \{\mathrm{Re}\,s > θ\}` there is such a `b` whose
Dirichlet series vanishes on `S`; the hypothesis `A(x) ≪ x^{θ+ε}` therefore
implies no constraint on the zero set."  Delete "any prescribed zero
configuration" from both the theorem and the §28.2 bullet, replacing the latter
by "for which any prescribed finite set of points in `\mathrm{Re}\,s > θ` can be
added to the zero set at the same power saving."  Remark 27.11a then becomes
what it should be — a note on why only "add" is available — rather than the
place where the theorem is silently corrected.

### 2. Corollary 26.19 (lines 11186–11211) — **MAJOR**

**The corollary is labelled `PROVED` and its first step is not proved; the
corollary contradicts itself four lines later.**

The displayed deduction is "`H(2,c)` implies, by Parseval in `d`,
`𝒞_4(0) = Σ_{|d|≤2N}|𝒞_2(d)|² ≪ (\log N)^{B_2}N²`".  By Proposition 26.18,
`M_4(N) = Σ_d κ_Q(d)𝒞_4(d)` with `κ_Q(0) ≍ Q²` and `κ_Q(d) ≪ Q^{1+ε}` for
`d ≠ 0`.  Isolating the `d = 0` term from a hypothesis bounding the **whole**
sum requires a bound on `Σ_{d≠0}κ_Q(d)𝒞_4(d)`, and `𝒞_4(d)` is complex and
unbounded in sign for `d ≠ 0`.  No such bound is supplied anywhere in §26.

That the step is missing is stated inside the same corollary: "`H(2,c)` sits at
or above RH — above, because it demands **in addition the off-diagonal
control** … neither implied by RH."  If the off-diagonal control is an
additional demand, it cannot also be a consequence of `H(2,c)` two displays
earlier.  The source has the same gap (`R149_003` §5.1 asserts the step "by
Parseval in `d` (Prop. D.62.1)" and its own difficulty verdict names
`Σ_{d≠0}κ_Q(d)𝒞_4(d)` as extra); the paper carries it faithfully, which is
exactly why it must be caught here.  As printed, the paper states `H(2,c) ⟹ RH`
as a theorem of this paper, which is the strongest implication anywhere in
Part IV and the one that makes open item (44) "at or above RH".

*Fix.*  Restate Corollary 26.19 with the hypothesis it uses:

> "`H(2,c)` **together with** the off-diagonal bound
> `Σ_{d≠0}κ_Q(d)𝒞_4(d) = o(Q²N²)` implies `𝒞_4(0) ≪ (\log N)^{B_2}N²`, hence
> `Σ_{|d|≤2N}|𝒞_2(d)| ≪ N^{3/2+o(1)}`, hence RH."

and label it `PROVED` (the implication) with the off-diagonal clause named as a
hypothesis, not as a consequence.  Then delete "neither implied by RH" from the
difficulty verdict or reword it to "the off-diagonal control is not part of
`H(k,c)` and is not implied by RH".  Open item (44) and §28.1 item 15
("implies RH at `k = 2`") must be adjusted in the same way — item 15 currently
propagates the unhedged form into the consolidation.

### 3. Theorem 27.10, proof (lines 11449–11458) — **MAJOR**

**The (⇒) step is attributed to "Landau's theorem on the abscissa", which is not
what the proof uses, and "Landau's theorem" is BE8 of the axiom list two
subsections later.**

`R150_004` D-3 is explicit: Landau's abscissa theorem requires eventually
one-signed coefficients, and `ψ(x) − x` changes sign infinitely often
(Littlewood).  The argument actually written — absolute convergence of
`∫_1^∞|ψ(x)−x|x^{-σ-1}dx` for `σ > θ`, holomorphy, and uniqueness of analytic
continuation against the pole at `ρ` — is correct and needs no one-signedness.
The misnomer is not cosmetic here: §27.4 lists **BE8 = Landau's theorem on the
abscissa** as an axiom of a Beurling system, and Theorem 26.15 uses the genuine
Landau theorem (import (X20)) on `R(n) ≥ 0`.  As printed, a reader is invited to
believe that the classification of §27.2 depends on BE8, which it does not, and
the label line "`CLASSICAL` (von Koch–Landau)" reinforces it.

*Fix.*  Replace "Landau's theorem on the abscissa, in Mellin form" by "absolute
convergence of the Mellin integral together with uniqueness of analytic
continuation" and keep the display unchanged; retain "von Koch–Landau" in the
label line only as attribution of the **statement** (1901), adding "the step
used is not Landau's abscissa theorem, whose one-signedness hypothesis
`ψ(x) − x` fails".  This is one sentence and removes a false dependency between
§27.2 and §27.4.

### 4. Remark 27.16, line 11629 — **MINOR** (a downgraded claim reprinted in its downgraded-away form)

> "Unconditionally, only the soundness half is available — `(\mathrm{ZFS}_δ)` is
> derivable from BE1–BE8 **if and only if** it holds in every model — so the
> entire conditionality sits in one place."

The em-dash clause states the biconditional as if it *were* the soundness half.
`R150_004` D-6 and `R150_005` §1 downgrade Prop. 2.6′ from `PROVED` to an
observation precisely because the ⟸ half is an unproved completeness claim with
no deductive calculus fixed and BE1–BE8 not first-order.  *Fix:* "…— if
`(\mathrm{ZFS}_δ)` is derivable from BE1–BE8 then it holds in every model
(soundness, immediate) — so…".  Drop the "if and only if".

### 5. Theorem 27.4, displayed chain, line 11333 — **MINOR** (does not parse)

    |S_{f_0}| ≤ M_{2k}^{1/2k} ≤ L(k(|ℱ|+kL)/L)^{1/2k} ≥ L k^{1/k} ≥ L

A `≤ … ≥` chain asserts nothing.  `R150_004` §1 flagged it as "minor, carried
over unfixed from round 1", and it is still unfixed in print.  *Fix:* split it:
`|S_{f_0}| ≤ M_{2k}^{1/2k} ≤ L\big(k(|ℱ|+kL)/L\big)^{1/2k}`, then on a new line
"and `L(k(|ℱ|+kL)/L)^{1/2k} ≥ L k^{1/k} ≥ L`, the last inequality using
`|ℱ|+kL ≥ kL`; so the bound never beats the trivial one."

### 6. Lemma 26.3, lines 10836–10845 — **MINOR** (a `POINTER` in the critical path, and probably unnecessary)

Lemma 26.3 is the **only** `POINTER` in Part IV whose statement is load-bearing:
Theorem 26.4's proof invokes it by name ("By Lemma 26.3,
`S̃(0;N) = ψ_w(N) − N\widehat w(0) + O_A(N^{-A})`"), and Theorem 26.4 is the
principal theorem of §26 and one of the four items of §28.1.  As printed, §26's
main theorem is not self-contained, contrary to the rule stated in the Part IV
header and in `PART_IV_NOTES` §6.

It is also redundant: Proposition 26.2(3)'s proof of (C) already ends "Taking
`q_0 = 1` gives (E) with error `O_A(QN^{-A})`", which is (E) for every `c < 1`,
proved in the text, four lines of Poisson.

*Fix.*  Delete the `POINTER` and promote the two-line argument: state Lemma 26.3
as a corollary of Proposition 26.2(3) ("the spacing at `q_0 = 1` is `Q^{-1}`, so
the Poisson step is uniform for every `c < 1`"), keeping the second half
verbatim — the `c < 1/2` restriction on (C) at `q_0 > 1` and `(C′)` `OPEN`.
Remarks 24.12 and 24.13 should **remain** `POINTER`s: neither is load-bearing
(24.12 bears only on open item (38), 24.13 is the Epstein placement), the
judgement in `PART_IV_NOTES` §5 is right, and both name their source section and
their label of record as required.

### 7. Part IV header, lines 10212–10219 — **MINOR** (an undeclared label)

The header declares `METHOD-CONSTRAINT`, `RESTATEMENT` and `HYPOTHESIS` as
additions to (1.12).  `POINTER` is **new in Part IV** (grep: first occurrence
line 10503, three occurrences total, none earlier in the paper), carries real
weight — it means "the proof is not in this paper" — and is nowhere defined.
`CERTIFIED` and `ANALOGY` are likewise absent from (1.12) but are established
usage from Parts II–III, so they are a pre-existing defect and not Part IV's.
*Fix:* add to the header "and `POINTER` for a statement whose proof is not
reproduced here, which then names its source file, section and label of record".
On the brief's question of `HYPOTHESIS` versus (1.12): the declaration in the
header is sufficient and correct, the label is confined to (H-DMV), (H-DMV) is
used only inside Remark 27.16 and Proposition 27.17(3), both of which carry the
conditionality in their own statements per (1.13), and open item (41) records it
as blocking.  No repair is needed there.

### 8. §28.1 item 14, lines 11725–11733 — **MINOR** (hypothesis dropped in the consolidation)

> "Hence the translation shadow of the mixed cone is exactly `𝓔 ∪ \{0\}`, at
> every finite rank and for both signs (Theorems 25.6, 25.7)"

Theorems 25.6 and 25.7 both carry the hypothesis "`q_w ∈ L¹(R)` at almost every
`w`", and §28.1's preamble says "every entry is unconditional except where its
own statement says otherwise".  Corollary 25.8 makes the omission defensible —
(25.2) holds on the entire domain of definition of `B` — but the summary does
not say so, and this is the same species of defect as finding 6 of the Part III
review.  *Fix:* "…is exactly `𝓔 ∪ \{0\}` on the whole domain of definition of
`B`, at every finite rank and for both signs (Theorems 25.6, 25.7,
Corollary 25.8)".

### 9. Definition 27.9 and Theorem 27.10 — **MINOR** (the "classification" is two instances)

`R150_004` D-4: `θ ∈ [½,1)` is fixed in Definition 27.9 but the
**polar-at-zeros** clause never uses it; and Theorem 27.10 is stated only for
`a = Λ`, with `μ` added in Corollary 27.10a.  The general polar statement — a
pole of `D_a` at `ρ` obstructs `A(x) ≪ x^{θ+ε}` — is true by the identical
argument but is not written, so "the classification", the phrase used in §28.2
and §28.4, currently denotes two worked instances and a definition.  *Fix:*
either state Theorem 27.10 for a general polar-at-zeros `a` (the proof is
unchanged: absolute convergence, continuation, a pole at `ρ`), with `Λ` and `μ`
as the two examples; or add one sentence saying that the class-level statement
is the same argument and that only the two instances of record are printed.

### 10. Working vocabulary outside provenance paragraphs — **MINOR** (five lines)

By the standard the Part III review applied (finding 9), the following are body
text, not provenance notes, and carry the working vocabulary:

* line 10724 (Problem 25.13): "**Phase 148** answers `𝒦' = (T) ⊕ (R)` in the
  negative on (β) and (δ)";
* line 10740 (§25 reading of record): "**Phase 148** proved *its* form on *its*
  domain trivial and zero-blind";
* line 10757 (§25 withdrawn table): "**phase 148** proved its own form trivial
  on its own domain";
* line 11851 (open item (44)): "a claim of it would trigger the **FATAL rule**";
* line 11887 (§28.4): "To these, **phase 150** adds that…".

*Fix.*  Replace the phase numbers by the statements: "Theorems 25.6 and 25.7
answer `𝒦' = (T) ⊕ (R)` in the negative…", "what is proved is that *this* form
is trivial and zero-blind on *its* domain", "§27 adds that…".  For line 11851,
"a claim of it must be presumed erroneous until every error term and the
`Q`-uniformity are re-derived" says the same thing without naming the internal
rule.  Everything else checked clean: all other hits for
process vocabulary in lines 10210–11940 lie in provenance
paragraphs or file paths (grep over the whole of Part IV).

### 11. §28.3, closing bullet, line 11865 — **MINOR** (a range that excepts nothing)

> "All remaining items of §23.4 — (24)–(34), (35) excepted, which item 13 above
> answers — stand as recorded there."

(35) is not in `(24)–(34)`, so the exception is vacuous and the range silently
drops (35) and (36) from the carried list — while (36) is then carried
separately two bullets earlier and (34) is carried separately as (P145′), so
three items are each named twice or ambiguously.  *Fix:* "All remaining items of
§23.4 — (24)–(33), together with (34) = (P145′) and (36) above — stand as
recorded there; (35) is answered negatively by item 13."

---

## What was checked and found correct

**1. Labels against the decisions of record (every numbered statement of
§§24–27, 75 in all).**  No disagreement with `R147_005` §1, `R148_005` §§1–2,
`R149_005` §1 and §4, or `R150_005` §1 was found beyond findings 1–4 above.
Spot-checks of record:

| item of record | decision | as printed | verdict |
|---|---|---|---|
| D.59.1 framing | "folklore chain, a **Hölder inequality**, not a transfer of Weil I 3.2" | Remark 26.4a, verbatim, `PROVED`/`RESTATEMENT`, plus the §26 withdrawn row | correct |
| D.61.10 | "**RESTATED**: no transport of the polar/positivity structure" | Theorem 26.17, `PROVED` for (1)–(3), `RESTATEMENT` for the framing; the two transports written out; the old wording in the withdrawn table and in the "Finding of record" | correct |
| (P149) | "**reclassified**: the `k`-tuple conjecture with square-root error on average; not the object to create" | Problem 26.20, `OPEN`, "not a new object to create", plus withdrawn row `RECLASSIFIED` | correct |
| D.62.2 | Granville 2007 Thm 1A + Corrigendum 2008 sharp half; Bhowmik–Ruzsa quasi-RH only | Corollary 26.19's citation block, with `β < 11/12` at `δ = ½` and Bhowmik–Schlage-Puchta as the Ω-calibration | correct (the citations; see finding 2 for the deduction) |
| D.60.7′ | "provably negligible" only for `k = 1`, `c > 1/2` (`k < 2c`), Siegel–Walfisz leg; Ω-check clean | Remark 26.10a, with `CERTIFIED` on the Ω-shapes and `IMPORTED` on Siegel–Walfisz; withdrawn row "`SCOPE REDUCED`" | correct |
| (E) / (C′) | (E) for **all** `c < 1`; **(C′) OPEN** | Lemma 26.3 and the §26 withdrawn row, both explicit that the large-sieve justification is false exactly where it was invoked | correct |
| T5 | `PROVED`, **scope narrow**: single-fibre extraction only; large-value counting untouched | Theorem 27.3 `METHOD-CONSTRAINT`, with Remark 27.7a naming Halász-type counting, the hybrid large sieve and Bombieri–Vinogradov as untouched, and the Heath-Brown sieve case worked | correct, and the honest `CERTIFIED` on "every published bound is Parseval-type" is carried |
| Thm 4.12 / 4.13 | `PROVED`, `CLASSICAL` | Theorems 27.10, 27.11, both `CLASSICAL`, `PROVED`; §27.2's opening and closing both say nothing in it is original | correct (attribution: finding 3) |
| Prop. 5.7 | round-one form **restored**; archimedean half of the correction retained | Proposition 27.7 with (27.1) for every complex `b`, both sides `∫|\widehat b|^4`; the archimedean family excluded in the attached remark; withdrawn row "a correction of a non-error" | correct |
| T3 | conditional meta-theorem on (H-DMV); O-150.1 blocking | Remark 27.16, `METHOD-CONSTRAINT, conditional on (H-DMV)`, recorded as a remark "precisely because open item (41) is unresolved"; (41) is O-150.1 verbatim | correct |
| Thm 4.7, Cor. 4.7a, Cor. 5.5 | **WITHDRAWN** | present only as rows of the §27 withdrawn table (lines 11685, 11689); grep finds no trace in any theorem, proof or summary | correct |
| D.55.9′ (C1 restatement) | the `χ = 1` slot is `𝓔^∞` because `f_1 = Σ_g f ≥ 0`; not the invariant-sector argument | Theorem 24.10(i),(ii), with Remark 24.10b(a) withdrawing "invariant sector, hence support function unchanged" as a non sequitur, and 24.10b(b) withdrawing "if `ρ` is a zero of `ζ_F` then `m = 1`" | correct |
| `\deg K_L` (C2) | false over a general base; `\deg K_{Q_𝔄} = ½` | Theorem 24.4(ii), restricted to `F = Q`, with the withdrawn row | correct |
| D.56.4″ / D.56.4′ | the kill at every finite rank and in **both** quadrants | Theorems 25.6, 25.7, with the `+` quadrant `CLOSED` rather than left open in the withdrawn table | correct |
| phase 148 scope | "proved *its* form trivial on *its* domain, not that the square admits no intersection theory" | §25's reading of record and the withdrawn row say exactly this | correct (vocabulary: finding 10) |

**2. Proofs read line by line.**  Theorem 27.3 (the extremal `b = \overline{ψ_{f_0}}`
realises `‖b‖_∞ = 1`, `‖b‖_2 = \sqrt L`, `‖b‖_1 = L` and `S_{f_0} = L`; the
"valid for every `b` with those norms" clause of Definition 27.2 is what the
proof consumes, and it is stated); Theorem 27.4 (correct up to the display of
finding 5: `|(b^{*k})_m| ≤ L^{k−1}`, support `≤ kL`, hence
`‖b^{*k}‖_2² ≤ kL^{2k−1}`); Proposition 27.5 (Cauchy–Schwarz on a support of
size `≤ kL` gives `E_{2k} ≥ ‖b‖_1^{2k}/(kL) ≍ L^{2k−1}/k`, hence
`(|ℱ|+kL)E_{2k} ≥ L^{2k}`, independently re-derived and confirmed);
Proposition 27.7 ((27.1) verified by Parseval in both directions);
Theorems 27.10 and 27.11 (both directions of 27.10 correct as written;
27.11's `P_{s_0}(s) = 1 − 2^{s_0}2^{-s}` has its zeros exactly where claimed,
`b = a * c` keeps `b_n ≪_S n^{ε}`, and
`B(x) = Σ_{d≤D}c_dA(x/d) ≪_{ε,S}x^{θ+ε}` with the constant depending on `S`
and `ε` only); Lemma 27.12 with (27.3) (Euler–Maclaurin, `|g'| = |γ|/x`,
`1 ≤ |2^{1−iγ}−1| ≤ 3`, and the endpoint correction `N^{1/2−ε}` in place of
`N^{1/2}` correctly applied and recorded in the withdrawn table);
Theorem 27.14.  In §26: Theorem 26.4 (the `(q,a) = (1,1)` term, `2k`-th roots,
`k > c/ε`); Corollary 26.5 (the Mellin identity, the pole with positive integer
residue, and `W` vanishing on a set with a limit point); Theorem 26.6
(Bernstein, measure `≥ 1/(4πN)`); Theorem 26.9(ii),(iii) (Farey spacing `Q^{-2}`,
Montgomery–Vaughan in the `(N+Q²)‖c‖_2²` shape, `Σ|c_n|² ≪ N\log N` by (B), and
the exact complementarity with Corollary 26.10); Theorems 26.11–26.13 (CRT and
Dirichlet densities, the multiplicativity check at `p^a`, Bochner, and the
zero-blindness statement, which is the statement of record); Theorem 26.15 (the
`σ_c = 2` computation and the contrast with Theorem 17.14 is exactly the finding
of record of `R149_005`); Theorem 26.17 (Plancherel on `(Z/q)^×` is correctly
labelled `CLASSICAL`, Goldston–Montgomery `IMPORTED`, and the three failures are
each argued); Proposition 26.21 (all three falsifiers).  In §24: Lemma 24.1,
Theorem 24.3 (all five clauses; the re-indexing is licensed by Lemma 18.4 and
that licence is stated), Theorem 24.4 (including the `K_χ ∈ D^W ⊗ C`
theta-transformation argument), Theorem 24.8 (both halves; the `≥` half's
`g^*` exists because `χ_0` surjects onto `μ_m`, and the paper notes that
`\{2πk/m\}` and `\{−2πk/m\}` coincide — which silently but correctly reconciles
the printed `θ + 2πk/m` with `R147_005`'s `θ − 2πk/m`).  In §25:
Lemmas 25.3–25.5, Theorems 25.2, 25.6, 25.7, Corollary 25.8.  **No shortened or
missing step was found in any of these beyond findings 2 and 3.**

**3. §28.2, the boxed wall statement.**  The preamble's claim — "it uses only T1
(Theorem 18.1), T2 (Theorem 18.16), T5 (Theorem 27.3) and the classification
(Theorems 27.10–27.11)" — is accurate: the five bullets cite 27.10/27.10a,
18.1, 18.16/18.17, 27.3/27.4 and 27.11, and nothing else.  Corollary 18.17 is
the Siegel-zero price attached to the A9 escape and is part of T2's package in
§18, not an extra input.  Theorem 27.4 is a quantitative appendix to T5.  The
box claims nothing about the location of any zero: the opening sentence names
the sign as an assertion, the five clauses are all about admissible derivations,
and the two readings that follow are explicitly disclaimed as "neither is a
claim about `ζ`".  The one defect is the fifth bullet (finding 1).

**4. The three `POINTER` items.**  Lemma 26.3 should be transcribed (finding 6).
Remarks 24.12 and 24.13 should not: 24.12's content (`σ(γ,m) < 1` for every
finite `m`, `S(γ,π/2,m) = 1` iff `4 ∣ m`) bears on a transfer theorem for
`ζ_L`, which is open item (38), and nothing in Part IV depends on it; 24.13 is
the placement of the Epstein falsifier on the graded carrier and is used
nowhere.  Both name their source file, section, source-item number and label of
record, and 24.12 additionally carries the withdrawal of the "first support
function to reach `1`" clause with its reason ((19.2)), so nothing load-bearing
is behind a pointer.  `PART_IV_NOTES` §5's grounds for omitting the `σ(γ,m)`
grid (lower bounds; about `L(s,χ)` and not `ζ`) are sound, and §28.5's
reproduction block correctly routes the two quoted numerics to the Part III
scripts.

**5. Open-item numbering.**  §23.4 ends at (36); Part IV opens at (37) and runs
to (44) with no gap and no collision, and each of (37)–(44) traces to a source:
(37) ← the standing qualifier of §24.3 and `R147_005`'s model caveat; (38) ←
O-47.7 and the `χ ≠ 1` sectors; (39) ← Artin holomorphy, import (X25), already
(29) in a different form but correctly narrowed here to the packet
decomposition on `𝒟_L`; (40) ← the `𝒟_L` sections functor; (41) ← O-150.1
verbatim, marked **blocking**; (42) ← O-150.2 (C6, C7), with the warning not to
presume it negative; (43) ← O-150.3 = `R150_004` D-8's two gate cells; (44) ←
O-149.1.  Item (35) is correctly answered negatively and removed, and the answer
is recorded in §28.1 item 13.  O-148.2 = O-149.5 is carried as Problem 25.13 and
is the only carried item without a bracketed number — defensible, since it is
named by its `O-` label at both ends.  The one defect is the closing bullet
(finding 11).  `PART_IV_NOTES` §1's "(36)–(44)" and §4's "items (37)–(44) are
new" are mutually consistent.

**6. Vocabulary and the sign.**  No occurrence anywhere in lines 10210–11940 of
"breakthrough", "new mathematics", "we believe", or any sentence asserting,
claiming, suggesting or hinting a sign.  §§24, 25, 26, 27 each close with the
explicit disclaimer, §26's and §27's provenance notes add "no zero-free region,
moment bound or cancellation estimate is proved", §28.5 repeats "numerics
illustrate and falsify; they prove nothing", and Part IV closes on "Row D is
closed in the map, with no label and no sign."  The two places where a reader
could be tempted — Theorem 26.4's "`ψ_w(N) − N\widehat w(0) ≪ N^{1/2+ε}`" and
Corollary 26.5's "Then RH holds" — both sit under an explicit hypothesis
(26.2), which Proposition 26.21(1) then shows is **false** for `Λ_a`, and the
"Consequence of record" after Proposition 26.8 says so in the same paragraph.
Theorem 26.16's "Contrast" and Theorem 26.12's "Warning attached" are correctly
labelled as `RESTATEMENT`-grade observations and not as progress.  The
`RESTATEMENT` label is carried on Theorem 26.12, on Theorem 26.17's framing, on
Remark 26.4a and on Remark 24.14, matching §28.1's closing paragraph.

**7. Imports.**  No new `(X)` tag is introduced, and the six reused tags —
(X20) in Theorem 26.15, (X20a) in Proposition 26.2(1), (X21) in
Proposition 26.21(2), (X22) in Theorem 26.9(ii), (X24) through Corollary 18.17
in §28.2, (X25) in open item (39) — are each used where the notes say.  The
`CLASSICAL` facts named in place (Hecke (H1)–(H3), Carmichael's Ramanujan
orthogonality, Montgomery–Hooley, Pólya–Vinogradov, Bernstein, Plancherel on
`(Z/q)^×`, Goldston–Montgomery, Siegel–Walfisz, Huxley/Schaal, Granville with
its Corrigendum, Bhowmik–Ruzsa, Bhowmik–Schlage-Puchta, von Koch–Landau) each
carry the clause they serve, as (1.12) requires, and none of them is
load-bearing for a statement about the location of a zero.  Hooley's `c_0` is
`CERTIFIED`, matching `R149_005` §1's "verify in Crelle 274/275 before
quoting" — correctly *not* upgraded.

**8. The writer's exclusions.**  With the exception of finding 6, no excluded
item is load-bearing for an included statement.  Checked individually: the
`σ(γ,m)` grid and its degree thresholds (used only by open item (38)); D.55.10′
Epstein on the graded carrier (Remark 24.13 only); the phase-147 Frobenius
constant `s_{\mathrm{Frob}} = 2/3` on `E/F_5` (§21's material, cited nowhere in
Part IV); phase 148's minor open items O-148.1, O-148.4, O-148.5 (idle; only the
principal residue is carried, as Problem 25.13); D.60.6 (Green–Tao restriction)
and the detailed Fiorilli–Martin / Hayani analysis (compressed into
Remark 26.10a, which carries the `k = 1` restriction that is the only part
anything depends on); the phase-150 instance tables (each row is
Proposition 27.6 or 27.7 with a family substituted, and the archimedean row is
withdrawn in any case); the closure plan's §§4, 7, 8 route rankings and its §9.2
reformulation (planning material; §28.4 correctly carries only the six clauses
of the plan's §6 as the reopening criterion, and names the certified-range
extension as measuring rather than moving the wall, with no number quoted).
`main.tex` is untouched and Part IV introduces no numbering collision with
Parts I–III.
