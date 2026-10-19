# Paper 46, Part III — adversarial confirmation pass (round 2)

*Reviewer of record: adversarial reviewer, 2026-09-14.  Target: `main.md` (10182 lines)
after the repairs listed in `PART_III_NOTES.md` §6.  Sources read for this pass:
`03-research/phase-140-row-d-frobenius-square/R140_001_ROUND1.md`,
`R140_005_CLOSING_DECISION.md`, and the `scripts/` directory of that phase.
`main.md` was not edited.*

## Verdict

**ACCEPT**, subject to five residual defects, all `MINOR` except finding 1,
which is a `MAJOR`-class overstatement of record but is repaired by deleting or
rewording one clause in two places.  No statement needs re-proving; no proof read
in this pass was found incomplete; the round-1 `MAJOR` (finding 1 of R1) is
discharged in full.

---

## A. §19bis, read in full against phase 140

All 23 statements (19bis.1–19bis.23, no gaps) were read with their proofs.  The
section is faithful to `R140_001`/`R140_005`, including the round-2 repairs, and
in three places it is stronger than the source.

**The R140 `FATAL` (H1) does not recur, and is proved against.**  Definition
19bis.4 sets `L_S := ∏_{𝔓∈S_f}O_𝔓`, calls it "a topological ring, **not** a
projective `O_K`-module", and identifies it as the literal transport of Paper 44
Definition 6bis.1.  The paragraph "*A ring of `S`-integers is the wrong object
here*" shows why `O_{K,S}` kills the object (`𝔫O_{K,S} = O_{K,S}` for every
admissible `𝔫`, cone acyclic, `H^0` and `deg_det` both `0`), and the same
statement is carried as a withdrawn row.  Theorem 19bis.5's proof is genuinely
local — each clause is proved at one place where `𝔓^kO_𝔓 = (π_𝔓^k)` is
principal — so no Dedekind invertibility and no projectivity is used; `H^0 ≅
O_K/𝔫` of order `N𝔫` follows by CRT, and (iv)'s `Tor_1 ≅ O_𝔓/π^{min(a,b)} ≠ 0`
is correct.  The avoidance of the class group is by construction (`ι` built from
uniformizers place by place), is stated as such, and the one clause that does
**not** transport — injectivity of `𝔫 ↦ Frob_𝔫`, Paper 44 Thm 3ter.4(iv) — is
marked `OPEN` and shown to be used nowhere.  This is better than the source.

**The Pólya-realization collapse is stated only for the realization.**  Corollary
19bis.10 attaches two qualifications inside the statement (the canonical class
does **not** match, `K_S = −2(f_1+f_2)` against `K = +½(F_1+F_2)`; and reading
`Δ^W·Δ^W = 2 = 2−2g` as `g = 0` applies a curve formula to a surface diagonal,
carried under Finding 13.8's explicit refusal), and the boxed note plus the first
withdrawn row `REFUTE` the reading of the collapse as a statement about the
Frobenius family or the square.  Definition 19bis.7 says in advance that `r`
deletes the weights `Λ_K(𝔫)N𝔫^{−½}` and that `Δ ↦ 2K` is a choice of
representative, "and **none of them is asserted to be a regularized value of
`δ_1⋆δ_1`**".  Correct and sufficient.

**The three Gram forms carry residue R2 as `R140_005` §3 directs.**  Theorem
19bis.12(ii) contains the required sentence verbatim in substance: Paper 44's
`Q_fin` is "a **quadratic form on radial profiles**", `G^{Frob}` is "the
**discrete Gram matrix** of the family … which has no diagonal at all", and "the
indefiniteness of the first … is not a statement about the diagonal of the
second".  The (A)/(B)/(C) row contents match `R140_005` §1 (D.23.12) including
the K1 correction (complement of the **intersection**), Remark 8bis.1c (the
diagonal does not exist), and the colimit quantifier on (B).

**`χ = 1/8` optimal; `χ = ¼` withdrawn.**  Theorem 19bis.16's region analysis was
checked line by line: the six regions cover `R²` up to `a ↔ b`, each computation
is correct, `inf g_1 = ½` at `(1,0)`, `(0,1)`, and the scaling `g_c = c²g_1(·/c)`
gives `c²/2`.  Clause (ii)'s `g(u,u) = u² − u/2 + ¼`, minimum `3/16` at `u = ¼`,
is right, and the falsification of `χ = ¼` ("`1/8 ≥ 3/16`, false by `1/16`") is
exact.  The refuted value sits in the withdrawn table and in §23.3.  The script
`certify_chi.py` exists in `phase-140/scripts`, and the paper correctly demotes
its grid sweep to a consistency check ("uses no Lipschitz or interval bound …
nothing depends on the script"), with a further withdrawn row retiring the word
"certifying".  This is the right treatment under the author's numerics rule.

**Theorems 19bis.19, 19bis.22 and Corollary 19bis.23, and the PROVED/GUIDANCE
split.**  19bis.19's proof is complete and unconditional: the sign case `a < 0`
or `b < 0` is disposed of by Lemma 19bis.18, the primitive `F = Πg = −g''+¼g` has
`Φ_F(s) = s(1−s)Φ_g(s)` hence `M(F) = 0` and `Φ_F(ρ_1) ≠ 0`, and the
contradiction is `|Φ_{E'}(ρ_1)| ≤ max(a,b)` against the choice of `t`.  Lemma
19bis.18's log-convexity step (Hölder with exponents `1/(1−β)`, `1/β`) is correct
and the bound `b^{1−β}a^{β} ≤ max(a,b)` is used only in that form.  19bis.22 is
one line from 19bis.8(ii) and is correctly extended to the transport-invariant
variants (`ab` is preserved because `λ_−λ_+ = 1`).  Corollary 19bis.23 splits
exactly as `R140_005` requires: the separation statement is `PROVED` (it is the
19bis.19 witness), and the prescription "must read `Z(E)` through pairings
`I_∞(E,X)` with `Z(X) ≠ 0`" is `GUIDANCE`.  No guidance is smuggled into a
`PROVED` clause.

**Nine (in fact ten) withdrawn rows, complete against `R140_005`.**  Present:
the ruling-plane/`NS(P¹×P¹)` misreading; `χ = ¼`; the "lower bound on `W`"
misreading; the false biconditional (`ψ ≡ 0`); "`F_1,F_2` are the rulings `e_∓`"
(against Paper 43 Thm 9.14c); the needless coprimality hypothesis; "`L_S :=
O_{K,S}`" (the `FATAL`); the `T_n`-separates-the-models hope; the
Connes–Consani candidate as a *refutation* (kept `OPEN` with U1 and U2, as
`R140_005` §1 records for candidate (β)); and "certifying" for the grid sweep.
Nothing on `R140_005`'s withdrawn list is missing.  (`PART_III_NOTES.md` §6 says
"nine rows"; the table has ten.  The notes, not the paper, are wrong.)

**Vocabulary.**  Clean.  Every hit for process vocabulary /
adversarial inside lines 6507–7275 is in the italic provenance note or a file path.
No RH-conditional statement is stated unconditionally: 19bis.17(ii) opens
"Assume RH", and the (i)/(ii)/(iii) split is exactly D.24.5 / D.24.5a.

---

## B. Residual defects

### 1. Corollary 19bis.6 and §23.1 item 8 — **MAJOR (one clause, two places)**

> Cor. 19bis.6: "The question left open in **§14.5**, whether the Frobenius
> construction of Paper 44 survives the passage from `Q` to a general number
> field, is therefore answered affirmatively and in full."
> §23.1 item 8: "… — which settles for a general number field the question
> **§14.5** left open there."

**§14.5 contains no such item.**  Its open list is (16)–(23); a grep of the whole
subsection (lines 3838–3947) for "field" returns only two hits, both inside
"function-field model" in items (20) and the preamble.  The question actually
closed is **O-9 of the research record** (`R140_005` §1, "O-9 closed"), which is
not a numbered item of this paper.  As printed, the paper claims to close a
numbered open question of its own that does not exist.  Worse, the §14.5
bookkeeping paragraph (line 3909) still reads "Items (16)–(19) and (21) are
unchanged", while §19bis's own opening declares itself to be about "the one route
that Remark 14.5a and **§14.5 item (18)** single out" — so a reader can take
§23.1 item 8 to close item (18), which §19bis does **not** do: Theorem 19bis.19
closes the bidegree-function subfamily, not "a `h⁰` built from
`Frob_n ⋆ Frob_n^† = Δ^{(n)}`" in general.

*Fix (one of):* (a) delete "the question §14.5 left open there" in both places and
say instead "the passage from `Q` to a general number field for the Frobenius
family of Paper 44"; or (b) add the transport question to §14.5 as a numbered
item and record it as settled in the bookkeeping paragraph.  In either case add
one sentence to that paragraph stating what §19bis does and does not do to item
(18) — it narrows it to the non-bidegree part and leaves it `OPEN`.

### 2. §19bis, introductory paragraph (line 6535) — **MINOR**

> "**no nonzero `h⁰` that factors through `M` satisfies (b′)** (Theorem
> 19bis.18)"

19bis.18 is *Lemma* 19bis.18 (the moment bound).  The theorem is **19bis.19**.
This is the only dangling statement number in §§17–23 after the mechanical scan
(see D below).

### 3. §23.6 Reproduction — **MINOR**

The block lists the scripts of phases 137, 142, 143, 144, 145, 146 and omits
`03-research/phase-140-row-d-frobenius-square/scripts/certify_chi.py`, which
§19bis cites twice (the `g`-sweep and the two `\log 3` constants of the
Connes–Consani remark).  *Fix:* add the two lines, in phase order before the
phase-142 block.

### 4. §23.4 — **MINOR** (the open items §19bis creates are not carried)

§19bis records three `OPEN`s that §23.4 does not list: (i) injectivity of
`𝔫 ↦ Frob_𝔫` for general `K` (the box after Theorem 19bis.3); (ii) **the
description of the moment cone `𝔐`** (Proposition 19bis.21), which the
proposition itself calls "the whole remaining content of (b′)" — this is close to,
but not the same as, item (32) (the sufficiency half of the exponential moment
problem), and the difference should be visible; (iii) the Connes–Consani
candidate at clause (c), open behind U1 (the degree dictionary) and U2
(`\dim_S` against a real functional).  *Fix:* add items (37)–(39), or fold (ii)
into item (32) with an explicit cross-reference and add the other two.

### 5. Front matter, line 9 — **MINOR**

The Part III summary paragraph enumerates §§17–23 by content and does not mention
§19bis, so the one section added by this revision is invisible in the paper's own
opening description.  *Fix:* one clause after "(§19)".

---

## C. The nine minor repairs of round 1 — all verified

| R1 finding | site | state |
|---|---|---|
| 2 | 5964 | "Step 1 of **Theorem 19.25**'s proof" — correct |
| 3 | 8637 | "**Lemma 19.17** in the model" — correct |
| 4 | 5697 | "By **Lemma** 13.5b" — correct |
| 4 | 7335 | "the proof of **Lemma** 20.4" — correct |
| 4 | 8374 | "**Theorem** 21.20 below" — correct |
| 4 | 4811 | "the second method constraint, **Theorem 18.16**" — correct |
| 5 | 9034 | Proposition 21.21 now `PROVED` + `RESTATEMENT`, frame-internal — consistent with §23.2 |
| 6 | 10021–10022 | "for every `E` with `Φ_E(0) > 0`, `t_n(E) > 0` for all `n ≥ N(E)`, unconditionally (Proposition 20.26(i),(ii))" — hypothesis restored, and the citation now names the two unconditional clauses only |
| 7 | 9942 | "…`= \log\#(L_S/mnL_S)`, **which is all that is used here**" — the dangling §22.7 pointer is gone |
| 8 | 6461–6486, 7608–7768, 10022 | 17 occurrences of `(T1_cone)`/`(T2_cone)`; **no bare `(T1)`/`(T2)` survives anywhere after line 6400**, and `(T1′)` remains distinct.  Remark 20.17a now reads unambiguously |
| 9 | 2722–2745 | the §12.2 note is rewritten in paper language: no phase, round, adversarial or lead; the mathematics, the constant `s_1`, the degree-400 witness and the numbers `199.7248 > 199.6920` are unchanged; it now cites Theorem 19.25, Lemma 19.17, Theorem 19.2, Theorem 19.28 and Restatement 19.29, and states the two repair routes.  It does not overstate: "Theorem 12.3 keeps its label — its proof is correct — and loses its use" |
| 10 | 3966 | the (X19) row now heads the Part III import block, directly under the sentence that explains it |
| 1, consequence | 5994 | Proposition 19.7 is now "the bidegree witness of Theorem 19bis.19 does not reach this candidate" — the witness is named and defined, and the naming sentence after Theorem 19bis.19 closes the loop |
| 1, consequence | 9999–10013, 10055, 10066–10067 | §23.1 item 8 added and items 8–11 renumbered 9–12 (verified: items 9–12 are the frame defect theorem, the trace side, the function-field model, the degree form); §23.2 gained the Restatement 19bis.13 row; §23.3 gained the rows for Theorem 19bis.19/Corollary 19bis.20 and for `χ = ¼` |

Two remarks on the renumbering choice.  `19bis` rather than a global renumber is
the right call — the paper already uses `bis`/`ter` numbering, and a renumber
would have moved every equation tag in §§20–23; and the numbering `19bis.2bis`
for the orbit restatement is consistent with that convention.  The section
placement is also right: §19bis is cited forward from Proposition 19.7 (§19.2)
and backward from §20's opening demand, and both cross-references resolve.

---

## D. Mechanical cross-reference scan (§§17–23 and §19bis)

A scan of every `Theorem|Lemma|Corollary|Proposition|Definition|Restatement|
Remark|Observation|Problem N.M` reference in lines 3900–10182, matched against
every numbered statement declared anywhere in the file (including the
`Definition–Theorem` form and the `19bis.*` series), reports **exactly one
defect**: the `19bis.18`-for-`19bis.19` reference of finding 2.  Every
kind error of R1 finding 4 is gone, `19bis.1`–`19bis.23` are all declared with no
gaps and no duplicates, and the four external citations (`Paper 45 Theorem 10.4`,
Hartshorne `V.1.6`/`V.1.9`, `Paper 43 Theorem 9.1`/`9.14c`, `Theorem 3.7`) are
the only "missing" hits and are all genuinely external.

## E. Unchanged from round 1

Nothing in §§17–23 outside the repaired sites was altered in a way that affects
the round-1 confirmations: the withdrawn tables of §§17–22, the label table, the
imports (X19)–(X29a) — §19bis correctly adds **none**, and its "Imports used"
paragraph says so explicitly and labels its classical inputs (product formula,
CRT, norm multiplicativity, Hölder, Bochner, Bohr, `P¹×P¹`) `CLASSICAL` at the
point of use — the seven Parts I–II corrections, and the §23 lists remain as
confirmed, with the four §23 amendments of finding 1 added correctly.
