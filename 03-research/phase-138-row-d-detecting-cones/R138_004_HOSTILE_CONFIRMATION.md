# R138.004 — Hostile confirmation, round 2, phase 138

*Auditor: Opus 5 (1M), hostile role. Date 2026-09-13. Objects: `R138_003_BUILDER_ROUND2.md` (ledger),
the in-place repairs in `R138_001_BUILDER_ROUND1.md` (now 1284 lines, 20 bracketed round-2 notes) and
`README.md` (79 lines). Method: each of H1–H13 checked **at the point of use in the repaired text**,
not against the ledger's description of it; then §7bis, the three new/amended `OPEN` items, and the
phase-139 recommendation audited as fresh claims.*

**Summary. All thirteen findings are correctly applied; none is cosmetic, none is mis-applied, and no
repair introduced a new error in the mathematics.** The ledger `R138_003` is accurate: I found no
discrepancy between what it says was changed and what the files contain, and no silent edit (every
change I located carries a bracketed note; I found no altered statement without one).

**Four residual findings, all in material written *after* the audit** (§7bis and the new `OPEN`
items), two MAJOR and two MINOR. None of them touches a proof; two of them retire an `OPEN` item.

---

## 1. Per-finding status

| # | sev. | applied? | verification performed |
|---|---|---|---|
| **H1** | MAJOR | **APPLIED, correctly and completely** | §D.17.2's heading is now "The triangle family detects; `E` and `C_c^∞` are detecting cones"; Theorem D.17.2 is restated "in the `h`-variable" and followed by the explicit three-part **What is proved** ((1) the family `{h_T}` detects in the `h`-variable and needs no `D^W`-membership, (2) Lemma D.17.2c produces the classes `F_T^{(δ)}`, (3) hence `E` and `C_c^∞(R)` are detecting cones); Corollary D.17.2d no longer mentions `C_Pó^{sm}`; §5 item 4, the D.17.3 ledger paragraph, §6bis row 13, the §8 table and the README row all carry "`E` and `C_c^∞`". I grepped for every remaining occurrence of `C_Pó` next to "detect": the only three are (a) the README row that says `C_Pó` is **not** a detecting cone, (b) the §5 note saying the same, (c) `OPEN` D.17-β. **No residue of the type error.** The surviving statements are exactly the two the audit asked for. |
| **H2** | MAJOR | **APPLIED, correctly** | The `REFUTED` box now refutes the blueprint through "`E` is **not absorbing at `K`** … in any topology whatsoever, since absorbing at `K` is a purely algebraic condition"; a `WITHDRAWN` box quotes the counterexample (`D^W_ε`, `‖·‖_ε`) and states that the round-1 implication is a non-sequitur; "Topology, stated precisely" now says "**No claim is made about other topologies**" and names D.15.2b(ii) as load-bearing. D.15.2b(i) is claimed for `‖·‖₁` only, as printed in the theorem and in the §8/README rows. Correct — but see **C4**: the withdrawn *statement* is in fact true in a stronger form, provable in one line, so D.15-γ should not stay open. |
| **H3** | MAJOR | **APPLIED** | The comparison carries `HEURISTIC` plus a bracketed note giving the reason (D.11 presupposes an `h⁰` the corpus lacks; no common normalization; neither direction proved). Corollary D.16.3 itself keeps `PROVED`, correctly — its proof is independent. The §8 table and the README now separate D.16.3 (`PROVED`) from D.16.3′ (`HEURISTIC`). *Residue:* the running sentence still reads "The implication D.11 ⇒ D.16.3 is immediate; the converse is false", which the note then denies. Wording, not label; fix in round 3 (**R1**). |
| **H4** | MAJOR | **APPLIED, correctly, and the quantifier order is now right** | Definition D.16.1 and Theorem D.16.1(d) let `⋆` range over convolution by members of `C_W`; the proof now reads "**Given `ρ_0`**, fix a real even `φ ∈ C_W` with `D(z_0) ≠ 0`". I re-checked the quantifier: the operation set `{p(∂)} ∪ {⋆g : g ∈ C_W}` is fixed **before** `ρ_0`, so the cone `⟨C_W⟩_{Ops}` is fixed before `ρ_0`, and `φ^{⋆N}` lies in it for *every* `φ ∈ C_W` — so "∀ρ₀ ∃F ∈ C" is satisfied. Correct. B-5 is untouched: no translation appears. |
| **H5** | MINOR | **APPLIED** | The proof of D.15.1(ii) now prints `= ½Φ_F(0) − ½Φ_F(1) = −½μ(F)`, with the note that downstream uses are of `μ²` or `μ = 0`. I re-checked D.15.3 and D.17.2: both use `μ(F)² ` or `μ(F) = 0` only. |
| **H6** | MINOR | **APPLIED** | The profile is now `exp(−c(log u)^{3/5}(loglog u)^{−1/5})` and the conclusion `R̃(T) ≫ e^{T/2}e^{−cT^{3/5}}/T`; "Finding" is replaced by "*Remark (not an independent no-go)*"; the §8 row reads "`PROVED` (the inequality only; downgraded from 'Finding', H6)". Correct, and the arithmetic still gives divergence against an `O(1)` target. |
| **H7** | MINOR | **APPLIED** | D.16.0 now states CC's **both** vanishing conditions (`\hat g(i/2)` and `\hat g(0)`), identifies the second as `Φ_F(½) = 0`, notes it is not implied by primitivity, and gives the Theorem 6.11 alternative with `13<c<17`. The independence of source (α) is stated. Correct. |
| **H8** | MINOR | **APPLIED** | Remark D.17.2e now says the criterion is "**not** claimed as new", states the precise literature question, and names Bombieri (*Remarks on Weil's quadratic functional*), Yoshida 1992, Riesz-mean/Báez-Duarte one-parameter criteria and `phase-14/ANCHOR-framework…`. The caveat is carried into the §8 table **and** the README row ("novelty `OPEN`"). Correct. |
| **H9** | MINOR | **APPLIED** | D.16.2‴(4) now reads "`ker Z = (P^W)^{⊥_{I_∞}}` **exactly** (Theorem 11.10)"; the density clause is withdrawn with a note. This is what Theorem 11.10 says and what (4) uses. |
| **H10** | MINOR | **APPLIED** | A caveat box under (D.15.2c) states that `A` is defined through `I_∞`, fails clause (ii) of **Q**, and is not by itself a usable criterion; P46-4 and the README row carry the same; `OPEN` D.15-β is cross-referenced. Correct — this is the honest status. |
| **H11** | MINOR | **APPLIED** | P46-1 now attributes the transposed phrasing to the **proof** of Proposition 12.6; I re-checked Paper 46 `main.md` and confirm the location. Recommendation unchanged, as it should be. |
| **H12** | MINOR | **APPLIED** | D.15.4b(c)⇒(b) now cites Prop. 12.6's "finite set `P ⊂ R` of simple poles with `P = 1−P`" at the point of use, with the remark that a complex `P` would give a circle. Correct. |
| **H13** | MINOR | **APPLIED** | D.16.0 now reads "**twice** CC's prime-free window", with the note that the `4` was against the blueprint's `¼log2`. §6bis row 8 was already right and is unchanged. Correct. |

**Status: 13 of 13 applied. 4 MAJOR: applied. 9 MINOR: applied. Contested: none.**

---

## 2. Assessment of §7bis ("Answer to **Q** after audit")

### C1 — §7bis's `PROVED` label over-covers the statement it is attached to, and contradicts §7bis's own last sentence. **MAJOR (label)**

*Exact text:* "**`PROVED` (as a conjunction of the labelled statements below); the answer is negative,
and the obstruction is located.**" … and, twenty lines later: "**So Q is answered negatively for every
structure the carrier currently offers** … and the remaining logical room is exactly one thing: a cone
cut out by a condition on the **zero datum** … (`OPEN` D.16-γ)."

*Why wrong.* **Q** is an existential question over cones: *is there* a cone with (i)+(ii)+(iii). A
negative answer is a non-existence theorem. What the conjunction proves is strictly weaker, and in two
different registers:

 * a genuine non-existence result, but only over one class of cones — **no inequality that is a
   function of the ruling datum `M(F)` alone can detect** (D.15.3(ii) + D.16.2‴(1)–(2)), and the one
   structurally signed zero-free cone in hand, `Λ_ξ^+`, is maximally non-detecting (D.15.4c);
 * for everything else — the Pólya/convexity route, the window, the effective cone — a *case-by-case*
   failure of one clause, each `PROVED` for that cone, which is "no such cone **is produced**" and not
   "no such cone **exists**".

The paragraph's own closing sentence concedes exactly this ("the remaining logical room"), so the
`PROVED` header is inconsistent with the body. The README is more accurate than §7bis here ("No such
cone is **produced**"), and its §"Status after round 2" then overstates in the other direction: "as
did the negative answer to **Q** (§7bis of `R138_001`)" attributes to the hostile audit an endorsement
of a paragraph written after the audit; `R138_002` confirmed round 1's §5, whose wording was the
honest one.

*Minimal repair.* Split the label. `PROVED`: "(1) no cone whose defining condition is a function of
the ruling datum alone can detect; (2) each of the four carrier structures named in **Q** — polar
block, Frobenius lattice, kernel positivity, convexity — fails clause (i) or clause (iii) at the cone
this phase exhibits for it, by the statements cited." `OPEN` (= D.16-γ, once well posed): "no cone
whatever satisfies (i)+(ii)+(iii)." And amend the README's status line to "the negative answer **as
round 1 stated it** (no such cone is produced)".

### C2 — `OPEN` D.16-γ, and recommendation 1 of §7bis, are not well posed. **MAJOR (well-posedness)**

*Exact text:* D.16-γ: "Is there a cone cut out by a condition on the **zero datum** `Z(F)` alone that
is detecting and whose defining condition is not the PNT remainder?"; §7bis(1): "is every
`I_∞`-continuous condition on `Z(F)` definable without reference to the zeros necessarily of the form
'`Z(F)` lies in a subspace containing no detection direction'?"

Four defects, in increasing order of seriousness.

 1. **"A zero-free condition on the zero datum" is prima facie self-contradictory.** `Z(F) =
    (Φ_F(ρ))_{ρ ∈ Z(ξ)}` is indexed *by the zeros*; any condition literally written in those
    coordinates mentions them. The builder half-sees this ("the *only* zero-datum condition the corpus
    can currently write without mentioning a zero is `Z(F) = 0`") — which, read plainly, says the
    question as posed is nearly vacuous. What must be specified is the **presentation class**: which
    data may the defining condition use? (Support of `F`; pointwise inequalities on `F`; values of
    `Φ_F` at real points; `Φ_F` on the critical line; convexity; finitely many moments; …)
 2. **"`I_∞`-continuous condition" is undefined.** A condition is a subset; continuity is a property
    of functions. Presumably: "a cone defined by a family of `‖·‖₁`-continuous linear or quadratic
    functionals". Say so.
 3. **"A subspace containing no detection direction" is undefined**, and "detection direction" is not
    a notion the report has introduced.
 4. **The `M`/`Z` dichotomy is not an exhaustive classification of cone-defining conditions, so
    "the remaining logical room is exactly one thing" is false.** The report's own two most important
    cones are cut by conditions that are functions of neither `M(F)` alone nor `Z(F)` alone: `C_W` by
    a **support** condition, and `E = {F ≥ 0}` by a **pointwise** condition. The splitting
    `D^W/𝓝_∞ ↪ R² ⊕ ℓ¹` classifies the *form* `I_∞`, not the *conditions* one may impose on `F`.

 *And the framing contradicts §5 item 4.* §5 item 4 says — correctly, and it is `PROVED` — that
 "(i)+(ii) is easy and is **not** where the difficulty is": `E` is already a detecting, zero-free cone.
 So the open quadrant is not "a cone cut out by the zero datum"; it is **clause (iii) on a detecting
 cone**, i.e. a structural proof of `I_∞(F,F) ≤ ½(deg F)²` on `E` (or on a zero-free sub-cone of `E`)
 that does not pass through the PNT remainder. That is a sharper and better-posed target, and it is
 the one D.17.3 actually leaves standing.

*Minimal repair.* Restate D.16-γ as: *"Fix a presentation class `𝒫` of defining conditions (support,
pointwise sign, real-point values of `Φ_F`, convexity, finitely many `‖·‖₁`-continuous functionals).
Is there a convex cone `C ⊆ D^W` cut out by conditions in `𝒫` that is detecting and on which
`I_∞ ≤ ½deg²` admits a proof not reducible to a bound on the Chebyshev remainder?"* — and note that
`E` already satisfies every clause except the last. Recommendation 1 of §7bis should be reworded
accordingly; as written it sends phase 139 after an ill-posed target.

### What is right about §7bis

The *mathematics* of §7bis is a faithful summary: every statement it strings together (D.15.1,
D.15.3, D.15.4, D.15.4b, D.15.4c, D.15.4d, D.16.2‴, D.17.2/2c/2d, D.17.3) was re-derived
independently in `R138_002` §0 and confirmed, and each is quoted with the label it actually carries,
including the `OPEN` novelty caveat on D.17.2 and the `ζ_K` ceiling on equimodularity. The FATAL
screen is correctly reasserted and is, on my re-reading, clean: the only sign-producing statements are
on cones where the zero datum vanishes identically (`Λ_ξ^+`) or where the support forbids primes
(`C_W`), and equimodularity is explicitly never used to produce a sign.

### Assessment of the phase-139 recommendation

Items 2 (equimodularity as a **classification**, never as a sign, with the `ζ_K` ceiling respected),
3 (the D.17-α attribution search — cheap, and it decides whether D.17.2 is a result or a restatement)
and 4 (the do-not-reopen list: Pólya cone, `log 2` window, ample cone without D.15-β, `h⁰` growth) are
**sound and I endorse them**; item 4 is consistent with `CORPUS_CHECK_R138` and with the standing
no-go list. Item 1 is the ill-posed one (**C2**) and should be replaced by the repaired D.16-γ. I would
add, as a zero-cost item for round 3 rather than for phase 139: enter **C3** and **C4** below, which
retire two of the seven open items outright.

---

## 3. Residual findings on material written after the audit

### C3 — `OPEN` D.17-β is not open: `√C_Pó = {0}`, in one line. **MINOR**

*Claim audited:* "Put `√C_Pó := {F ∈ D^W : F⋆F^∨ ∈ C_Pó}`. Is `√C_Pó` convex? Is it a cone? …
Only if it is a convex cone does 'the Pólya cone is detecting' become a statement in the sense of
Definition 0.1, **and then it is immediate from (1)+(2) for the mollified triangles, provided they lie
in it**."

*Finding.* Let `F ∈ √C_Pó`. Then `F ∈ D^W`, so `F⋆F^∨ ∈ D^W` (Lemma 11.2(i)), so `F⋆F^∨ ∈ C² ⊂ C¹`;
but `F⋆F^∨ ∈ C_Pó`, and `C_Pó ∩ C¹(R) = {0}` by the report's own **Theorem D.17.1b**. Hence
`F⋆F^∨ = 0`, so `Φ_F(s)Φ_F(1−s) ≡ 0`, so `Φ_F ≡ 0` (a product of entire functions vanishes only if a
factor does), so `F = 0`. **`√C_Pó = {0}`** — trivially convex, trivially a cone, and vacuously
non-detecting. The question is answered, not open, and answered by a theorem already in the report.
Moreover the subordinate clause quoted above is **false**: the mollified triangles do *not* lie in
`√C_Pó`, precisely because `F_T^{(δ)}⋆(F_T^{(δ)})^∨` is smooth and therefore (D.17.1b) not in `C_Pó`
unless zero.

*Repair.* Replace `OPEN` D.17-β by a one-line corollary of D.17.1b ("`√C_Pó = {0}`: the Pólya
condition and the Weil class are incompatible in the `h`-variable **and** in the `F`-variable"), delete
the false clause, and remove D.17-β from the README's open list. This *strengthens* the H1 repair: it
is not merely that `C_Pó` is the wrong type of object — there is no cone of classes behind it at all.

### C4 — `OPEN` D.15-γ is answerable in one line, and the answer restores round 1's withdrawn claim in a corrected and stronger form. **MINOR**

*Claim audited:* D.15-γ, "Does `E` have empty interior on all of `D^W` in a topology finer than
`‖·‖₁`? Round 1's claim is withdrawn (H2); the question is not needed downstream."

*Finding.* `E` has empty interior in **every** vector topology on `D^W`, because it is absorbing at no
point. Let `F₀ ∈ E`, with decay exponent `1+ε₀` from Definition 11.1, so `F₀(t) ≤ Ce^{−(1+ε₀)|t|}`.
Choose `G ∈ D^W` smooth with `G(t) = −e^{−(1+ε₀/2)|t|}` for `|t| ≥ 1` (admissible: `D^W` asks only for
*some* `ε > 0`). For every `ε > 0` and all large `t`,
`F₀(t) + εG(t) ≤ Ce^{−(1+ε₀)t} − εe^{−(1+ε₀/2)t} < 0`, so `F₀ + εG ∉ E`. In a topological vector space
a set with nonempty interior is absorbing at each interior point; hence `E` has empty interior. ∎

This does **not** conflict with the H2 counterexample: that counterexample lives on the *fixed-`ε`
step* `D^W_ε`, which is a proper subspace of `D^W`, and its content — that round 1's *reason* was a
non-sequitur — stands. The correct statement of record is therefore: *round 1's conclusion was right,
its argument was wrong, and the right argument is the unbounded spread of decay exponents in `D^W`,
i.e. exactly the phenomenon that makes `E` non-absorbing at `K`.* Note the two facts now have one
proof: `E` is non-absorbing **everywhere**, and `K` is merely the case the criterion needed.

*Repair.* Enter the display above as a clause (iii′) of Theorem D.15.2b (`PROVED`), retire `OPEN`
D.15-γ, and keep the `WITHDRAWN` box for the invalid round-1 argument — the withdrawal of a bad proof
is not reversed by finding a good one, and the record should show both.

### R1 — wording residue at H3. **COSMETIC**

The running sentence "The implication D.11 ⇒ D.16.3 is immediate; the converse is false" survives
above the `HEURISTIC` relabel, which then denies it. Reword to "D.11 and D.16.3 plausibly express the
same phenomenon at different strengths; neither implication is proved."

---

## 4. Verdicts

| item | verdict after round 2 |
|---|---|
| **D.15** | **CONFIRMED.** H2, H5, H10, H12 applied; D.15.2b is now correctly scoped and its load-bearing clause is the algebraic one. With **C4** entered, D.15.2b is strictly stronger than round 1 claimed and one open item closes. |
| **D.16** | **CONFIRMED.** H3, H4, H7, H9, H13 applied; D.16.1(d)'s quantifier order is now correct and B-5 survives. `OPEN` D.16-γ requires the **C2** rewrite before it is a usable target. |
| **D.17** | **CONFIRMED.** H1, H6, H8 applied; the surviving statements are exactly "the family `{h_T}` detects (in the `h`-variable)" and "`E` and `C_c^∞` are detecting cones", both proved. With **C3**, `OPEN` D.17-β closes and the H1 repair strengthens. |
| **§7bis** | **CONFIRMED WITH REPAIRS.** The mathematics is a faithful conjunction of PROVED statements; the `PROVED` **label over the negative answer to Q** over-covers (**C1**) and must be split into a proved restricted form and an open unrestricted form. |
| **Phase-139 recommendation** | **ENDORSED on items 2, 3, 4; item 1 REQUIRES THE C2 REWRITE.** The better-posed successor target is clause (iii) on `E` (or a zero-free sub-cone of it), not "a cone cut out by the zero datum". |
| **Label** | **CONFIRMED: no label change for row D.** FATAL screen re-run on the repaired text: clean. |

**Overall: CONFIRMED WITH REPAIRS (residual).** All thirteen audit findings are correctly applied and
the round-2 text is materially better than round 1. The residue is four items, none in a proof: one
MAJOR label over-coverage (**C1**), one MAJOR well-posedness defect in a *new* `OPEN` item and in the
first phase-139 recommendation (**C2**), and two MINOR items (**C3**, **C4**) that each **retire an
open question by a one-line argument from the report's own theorems** — which is the cheapest kind of
progress available and should be done in round 3, not deferred to phase 139.

*End of R138.004.*
