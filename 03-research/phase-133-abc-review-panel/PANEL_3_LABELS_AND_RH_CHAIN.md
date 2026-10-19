# Panel 3 — Honesty of labels, the renaming test, and the chain to RH

Panel 3 of the three-part independent review, phase 133.
Scope: Papers 43 (row A), 44 (row B), 45 (row C), the
acceptance specification `P123_A_ACCEPTANCE_SPECIFICATION.md`, the closure
plan `ABCD-CLOSURE-PLAN/PLAN.md` §§5–8, and the decisions of
record `R130.005`, `R131.019`, `R132.007`.

**No paper was edited.**  This file is an opinion only; it
grants and withdraws nothing.

**One-sentence summary.**  The three labels are *procedurally* honest —
every qualification a demanding reader would expect is written down somewhere
in the papers, usually in the papers' own words and often more harshly than
I would put it — but the **name** of the label is not, because the
specification defines "Weil-strength" as *equality of structural burden with
Weil's proof* (§1) and Paper 43 §11bis item 4 states in its own words that
that equality "is **not** established".  What is honestly closed is a
clause list, on a declared carrier, on the invertible sector, with a
declared trace.  Three clauses (A.7, C.3, and the first half of C.6) are
discharged by a definition with disclosure; two dissents (A.8, B.7) are
resolved by a ruling where the dissenting assessment is, in this judgement,
right; and the one genuinely new theorem in the whole set with respect to
the RH literature is Paper 45 Theorem 10.4.

---

## 1. Clause-by-clause: is the label honest against the text?

Conventions.  "Honest" = the recorded verdict is what a demanding reader who
has read the cited theorems would also record, **given the paper's own
reading of the clause**.  "Definitional" = the clause is discharged by
choosing a definition that makes it true, with nothing proved that could
have failed.  I grade separately: **verdict honest?** and **clause content
earned?**

### 1.1 Row A (Paper 43; recorded in §14.0b, granted in R130.005)

| clause | recorded | my grade | reason |
|---|---|---|---|
| A.1 | PROVED, with reading note | **honest, weakened by definition** | "Descent" is discharged as a *filtered chart system with retraction and a chart-invariant trace* (§3.3bis), not as effective descent along a covering.  The paper says so, and R130.002 F20 endorses the flag.  A clause that says "descent … must be constructed" and is met by renaming a colimit a descent is a definitional discharge; it is disclosed, so the verdict line is honest, but `PARTIAL` would be the more accurate word and the paper itself offers it. |
| A.2 | PROVED (Thm 8A.12) | **honest, thin** | The objects are `E_H = λ(H)`, `H` in a commutative Banach `†`-algebra `𝓐_tr`; the "category" is the regular representation of a convolution algebra on an abelian group.  A.2 demands "geometric localization on `Y` or a proved Morita-equivalent localization"; I did not find that half discharged by a theorem anywhere, and R130.005 does not cite one.  The clause is met on the reading "closed under its declared completion" only.  Not a renaming of the explicit formula — genuinely a different kind of object — but far from "admissible mixed correspondences on a noncollapsed square". |
| A.3, A.4 | PROVED on `G` | **honest** | Composition is convolution; the dagger is `F^†(u)=\overline{F(u^{-1})}` with the half-density twist (Lemma 8.4 is the one real computation).  Both are proved, both are source-defined, and A.4's prohibition ("cannot be selected from the desired sign of a later scalar form") is respected.  The clause's escape hatch — "if composition is written by pull–tensor–push on `X^3`, all functors … must be proved" — is avoided by not writing it that way.  Honest, and much lighter than the classical burden. |
| A.5 | PROVED | **honest only because the word "declared" is everywhere; the load-bearing normalization is not a theorem** | `T` is **defined** (Def 8.6) as `Σ_v W_v + c·F(1)` from the two repository-proved local formulas.  Consequences: (i) place-additivity is a definition, not a localization theorem (Paper 45 §5.1 concedes this in terms); (ii) cyclicity is automatic because the algebra is commutative; (iii) **O-A5-5** — that the local weight *is* the Lefschetz/Hochschild shadow — is a **theorem at the unit shells** and a **declared half-density–Lefschetz normalization at the non-unit shells**, and the non-unit shells `p^kZ_p^×`, `k≠0`, are exactly where `Λ(p^k)=\log p` comes from.  The ledger says this (`O-A5-5: CLOSED IN THE EXACT FORM (8A.24)–(8A.24′) … and in no stronger form`).  So the arithmetic content of the trace rests on a declared normalization at precisely the locus that produces the prime side.  Paper 44 Thm 8bis.8 softens this — `vol(Z_p^×)=\log p` is the *unique* normalization with a universal Tate residue, up to one global scale — which is a self-consistency theorem, not a geometric derivation.  The verdict `PROVED` is honest **for the declared trace**; it would not be honest for "the" trace of a geometry. |
| A.6 | PROVED under the amendment | **honest** | See §2. The amendment is recorded in the specification itself, with the refuted original wording preserved, and the refutation (Thm 9.13(a)) is a real theorem. |
| A.7 | PROVED | **honest label, definitional content** | `Eff_A` = "all coefficients real and nonnegative" (Def 10.1, Def 10.2a).  The clause asks for a cone "constructed from the source geometry" that "descends to the numerical theory to the extent needed by Riemann–Roch"; since row A's Riemann–Roch needs nothing from the cone, the second half is vacuously true.  Thm 10.2(e) (not the operator-positive cone) is the only content that could have failed.  R130.005 and the paper both call this "a thin reading of a thin clause".  **This is a clause satisfied by a definition, and it is flagged as such.** |
| A.8 | PROVED WITH TARGET `Pic_b(B_T)`; dissent recorded | **over-graded; see §3** | The honest verdict is the auditor's restatement.  Notably, Weil's `D·D' = P·P' + d_1d_2' + d_2d_1'` is *not* proved: (10.10) is, in logarithms, the decomposition of an ordered pair, and the paper says so. |
| A.9 | PASSED FOR THE FORMALISM, on the automorphism sector | **honest, and the most consequential qualification in row A** | Thm 6.1 constructs `Φ: G_Λ → Perf(C×C)` for `Λ → Aut(C)`.  It recovers composition, unit, transpose and diagonal contact — for **automorphism graphs**.  The classical falsifiers that motivated the clause (P123.021: `Γ_F⋆Γ_F^t = q·Δ`, so the transpose is not the inverse for `\deg > 1`) are not met; they are **avoided** by restricting to the invertible sector.  A.9 is called "an acceptance test for structural correctness"; the test is passed on the sub-sector from which the phenomenon Weil's proof is about has been removed.  Honest as written ("for the formalism"), weak as a control. |
| A.10 | PROVED | **honest** | I re-checked the substance: no zero, no RH, no positivity is used in §§2–11.  `Λ` is derived as a shell volume (Rem 9.7a), and Rem 9.7a's three answers are the correct ones.  The residual objection is not an A.10 objection: the local density `τ_v(x)=|x|_v^{1/2}/|1-x|_v` *is* the Weil local factor, so the construction is independent of RH but plainly not independent of knowing the answer.  No clause forbids that, and the papers do not pretend otherwise. |

**Renaming test, row A, independent verdict.**  A.2–A.4, A.6 and A.9 are
not renamings of the scalar explicit formula: a commutative correspondence
category with excision, a half-density dagger, `𝓝 = 0`, the exact Tate
sequence and the rulings-as-limits are statements the explicit formula does
not make.  A.5 is the pressure point and R130.005 §2 puts it correctly:
constructing the left-hand side of the identity from fixed-point data is not
a renaming of the identity.  This agrees — **with one qualification not otherwise made**: what is constructed is the left-hand side *by definition*
(Def 8.6), from local formulas already proved elsewhere in the repository.
The non-trivial step "these local orbital integrals assemble into a trace of
a correspondence theory" is real for the unit shells and *declared* for the
rest.  So the correct verdict on A.5 is "not a renaming, but the assembly is
partly declared", not an unqualified pass.

### 1.2 Row B (Paper 44; recorded in §10 table, granted in R131.019)

| clause | recorded | my grade | reason |
|---|---|---|---|
| B.1 | PROVED (upgraded from PARTIAL) | **honest, generous** | The upgrade holds "only on the reading 'no functor into `G` is demanded'", and the paper prints that sentence.  The inverse-semigroup completion `𝔉` (Thm 3ter.7) is real content and answers the missing-dagger objection.  A reader who reads B.1 as demanding realized divisor arrows gets `PARTIAL`; the paper gives him the material to do so. |
| B.2 | PROVED on the label monoid, non-vacuous | **honest, and an improvement** | `n ↦ Frob_n` is strong monoidal with a true unit, injective, and the object determines `(n,P(n))` (Thm 3ter.4(iv)).  Round 2's fatal objection — the radial realization factors through the modulus and therefore forgets factorization — is answered by a different object, not by rewording.  Good. |
| B.3 | PROVED, true unit | **honest** | `Frob_n⋆Frob_n^† = Δ^{(n)} ≠ Δ` is stated, not hidden.  Note what this is: the half-density-normalized form of Weil's `Γ_F⋆Γ_F^t = qΔ` with `q` divided out.  See §5. |
| B.4 | REFUTED AS STATED; PROVED AS AMENDED (accepted); PROVED ON OBJECTS since round 3 | **honest** | See §2.  The refutation is real (P123.060, P123.022), the original text is preserved verbatim, and the round-2 type error (`T(Γ_n^{rad})` undefined, naive place-wise evaluation `= 0`) is recorded in the clause row itself.  That is the right way to do this. |
| B.5 | PROVED twice, and the two proved equal | **honest** | Thm 3bis.7 (shell volume) and Thm 5.3 (`Z`-linear model) with Thm 3bis.10(iii) the bridge.  `n=1` handled as identity/excess via `c·F(1)` with `c:=0`, not by the degree formula, as the clause demands. |
| B.6 | both halves PROVED, non-vacuous | **honest** | Thm 3ter.12 (support of `Frob_n` meets no fixed-point stratum for composite `n`) is a statement about the object, not about a trace value, which is exactly what "by structure, not by extrapolation" asks for.  Thm 3ter.14 puts the classes in `N_A^{dist}` with a **nonzero** ruling component — i.e. the Frobenii are *not* primitive, stated plainly. |
| B.7 | PROVED by ruling; dissent recorded as `PARTIAL` | **over-graded; see §3** | |
| B.8 | PROVED | **honest** | Table plus `verify_131_contacts.py`; the index by places is preserved as phase 119 requires. |
| B.9 | PROVED, "with the independence inherited, not earned" | **honest, and unusually candid** | The self-qualification is correct: row B inherits `Λ = vol(p^kZ_p^×)` from Paper 43 Rem 9.7a and adds the attachment to the family and to the contact locus. |

**Renaming test, row B, independent verdict.**  Pass, and more clearly than
row A.  The Frobenius family as Haar measures of fixed-point strata with an
inverse semigroup grading, the support theorem, the integral shadow `Sh_Z`
with its transitivity triangle and Möbius cofiber, and the two-Gram-form
theorem (8bis.1e) are not statements the explicit formula contains.  The one
statement that *is* Weil's criterion (Thm 8bis.4(iii)) is labelled
`CLASSICAL`, quarantined, and used by no clause — I checked that this is
consistent with the clause rows, and it is.

### 1.3 Row C (Paper 45; recorded in §14.2, granted in R132.007)

| clause | recorded | my grade | reason |
|---|---|---|---|
| C.1 | PROVED ("by citation; nothing constructed") | **honest** | Self-describing. |
| C.2 | PROVED at the chart, rulings in the completion | **honest** | Thm 8.1 identifies the polar packet with `β_T(M,M)`; the rulings are cited from row A with the quotient/subobject distinction preserved. |
| C.3 | PROVED "as a theorem about row A's **declared** trace"; place-additivity **definitional** | **honest label, definitional content** | PLAN §7 item 3 asked for a trace identity "over a common kernel, with finite, archimedean and identity contact", *proved*.  What is delivered is: row A defined `T` place by place; row C evaluates that definition on radial classes (Thm 5.1 = Paper 44 Thm 3bis.7) and supplies Lemma 5.1a for the identity case.  Lemma 5.1a is real work (it removes the support hypothesis and is what Thm 9.6 actually needs, since `h(0)=\|F\|^2>0` always).  The rest is evaluation of a definition.  §5.1 says this in plain words and refuses to soften it, which is why the verdict is honest. |
| C.4 | PROVED, all three off one object; polar half by residue computation | **honest, real content** | Thm 9bis.2′ (chart residues `|S_f|+1` and `0`; continuation residues `1` and `1`) is a computation that could have come out otherwise, and Mertens (E8) is quarantined out of the discharge.  This is the best-earned clause in row C after C.8. |
| C.5 | PROVED; no two limits interchanged | **honest** | Nine rows with certificates; row 7's certificate correctly demoted to a named import (E3c) rather than a consequence of (E3d). |
| C.6 | first half PROVED with `c=0` unique; second half PROVED (Thm 10.4) | **split verdict** | *First half:* `I_∞ = B_nuc` is (definition of `T`) + (Thm 9.4, the classical explicit formula proved here) + rearrangement + (Thm 8.1 identifying `2Φ_F(0)Φ_F(1)` with `β_T(M,M)`).  Since `T̂` is, by Rem 9.7a, **verbatim** the prime-power-plus-Gamma side, the comparison theorem is the explicit formula transported across a definition.  The non-trivial content is Thm 9.4 itself (classical, honestly re-proved) and the `β_T` identification.  Calling this "the comparison theorem" is defensible — the identification of the polar packet with the hyperbolic ruling form is genuinely a statement about row A's objects — but it is the closest thing in the three papers to the failure mode the closure rule was written to catch, and R132.007 §3's blanket sentence "Nothing is satisfied by a definition alone" is stronger than what the table beneath it supports.  *Second half:* Thm 10.4 is the strongest result in the three papers and is not a renaming of anything.  See §4(c). |
| C.7 | PROVED; no sign proved anywhere | **honest** | Warning 8.5 imports the two standing negatives into row C rather than hiding them. |
| C.8 | PROVED in the strong form | **honest, and well done** | Thm 9.4 is a correct contour proof (reflect first, expand on `Re s = c > 1`, shift each prime term with an entire integrand), with every classical input named — (E1), (E2) incl. "no real nontrivial zeros", (E3a)–(E3d), (E4)–(E8), (R1).  The round-2 correction — round 1 had presented (E3b)/(E3c) as consequences of `N(T)=O(T\log T)`, which is false — is exactly the kind of self-catch that makes the rest of the ledger credible.  "No analytic black box" here means "the black box is unpacked into named classical facts about `ζ`", not "nothing classical is used"; the paper says which is which. |
| C.9 | PROVED; the old §11 obligation deleted, not discharged | **honest** | Deleting an obligation that never existed (Paper 44 §9bis W1–W3) and saying so is the right treatment. |

**Renaming test, row C, independent verdict.**  Pass for C.2, C.4, C.5,
C.7, C.8, C.9.  **Qualified pass** for C.3 and for the first half of C.6, on
the grounds above.  The qualification does not overturn the label; it does
overturn one sentence of R132.007 §3.

---

## 2. The two accepted amendments

### 2.1 A.6 (Paper 43 §14.2; specification §2, amendment record )

**Original demanded.**  The Hausdorff quotient `N_A` **contains** the ruling
plane and a nonzero completed mixed sector — "contains" read as "has a
subobject isomorphic to".

**Why it was refuted.**  Thm 9.13(a): a `D_A`-submodule mapping
isomorphically onto `B_T` would contain `Φ_∓ ≠ 0` with
`a⋆Φ_∓ = λ_∓(a)Φ_∓` for all `a`, i.e. `â(χ) = â(∓i/2)` on the support of
`Φ̂_∓` — a value of `â` **off** the unitary axis forced to equal one **on**
it.  Impossible.  This is a genuine refutation of the literal clause on this
carrier, not a difficulty.

**Amended clause proves.**  A canonical exact sequence
`0 → N_A^{prim} → N_A → B_T → 0` of topological modules; `B_T`
two-dimensional with the hyperbolic form `[[0,1],[1,0]]`; `†` exchanging the
two directions; `N_A^{prim}` nonzero with a nondegenerate induced pairing;
**no splitting required**.  Proved by Thms 9.8, 9.11–9.14.

**What is lost.**  Precisely this: a **single** module containing both the
test classes and the rulings, carrying one nondegenerate pairing.  In the
test sector the rulings are a **quotient** (9.13(a)) and there is provably
**no** `D_A`-module splitting; in the completion `N_A^{dist}` they are a
**subobject** and the completion splits canonically (9.14a–b) — but `I_A`
does **not** extend continuously to `N_A^{dist} × N_A^{dist}`
(Rem 9.14c″), and the value of `λ_{RR}` on the ruling plane is a definition
(Def 10.6c).  Weil's argument is run on the span
`aΔ + bΓ_{F^k} + (\text{rulings})` with one intersection form on that span.
**That span, with one form defined on all of it, does not exist here.**  The
amendment is honest, the theorems behind it are real, and the loss is
directly the loss that makes a Hodge-index argument unavailable in §4(d).
The specification's amendment record states the reason.  The mathematical cost is
larger than the amendment's wording suggests.

### 2.2 B.4 (PLAN §6 item 4; Paper 44 §6.2a′, §10 table)

**Original demanded.**  `LΔ^*Γ_n` computed in the declared category, with
its arithmetic part **identified** with the complex
`[Z --Φ_n(1)--> Z]`, every truncation explicit.

**Why it was refuted.**  Three independent reasons, all recorded: (i)
`LΔ^*Γ_n` is the **fixed-point** complex with differential `n-1`, not the
cyclotomic one (P123.060); (ii) no `C`-linear category can carry `Z/p`
(P123.022), so an object-level identification is impossible; (iii) the class
of `a_S(n)` on the carrier is `δ_S(1/n)`, not in the image of any slice map
`j_q`, so the literal clause has no object.  A fourth, found in round 2:
`T(Γ_n^{rad})` is **ill-typed** — `T` is defined on `D_A` and the class is a
measure — and naive place-wise evaluation returns `0`.

**Amended clause proves.**  An identity of **degrees**: the finite contact
of `Γ_n^{rad}` (the mass at `t = \log n` of the unique Radon measure
`ω_{fin}` representing `T` on `D_A^{rad} ∩ D_A^0`) equals
`Λ(n)n^{-1/2} = n^{-1/2}\deg_{\det}[Z→Φ_n(1)→Z]`; strengthened in round 3
to the **objects** (Thm 6bis.4): `contact_{fin}(Frob_n) = Λ(n)n^{-1/2}`
exactly, with `\deg_{\det}Sh_Z(Frob_n) = \log n` through an integral shadow
built on the object itself, whose complex realization is acyclic.

**What is lost.**  (i) Any **derived** or torsion content: the right-hand
side's `Z/Φ_n(1)` is a finite group, the left-hand side is a real number,
and only the number survives.  (ii) Any **mechanism**: the two sides are
equal, and Paper 44's own Rem 6.5a′ records that `Φ_{p^k}(1) = p` holds for
an *unrelated* reason (`Φ_{p^k}(x) = Φ_p(x^{p^{k-1}})`).  Combined with
B.7 (§3.2 below), what B.4-as-amended proves is that two numbers both equal
`\log p`.  (iii) The object-level identification is not "open" but
**refuted** on this carrier, so this amendment, unlike A.6's, closes a door
rather than relocating a theorem.  The strengthening to `Sh_Z` on objects is
real and I credit it: `Sh_Z` is an integral structure attached to the
object, and its Möbius cofiber reproducing `Λ` is more than a coincidence of
scalars.  But it is a *shadow*, and the paper says its complex realization
is acyclic — i.e. the integral content does not live in the declared
`C`-linear theory.

---

## 3. The two recorded dissents

### 3.1 A.8 — audit (R130.002) vs ruling (R130.005 / Paper 43 §10.3.3)

clause is discharged by a definition (Def 10.6c) plus bi-additivity, so the
only thing A.8 adds beyond A.6 is Thms 9.14a–c, which are already what
closes A.6."

**Lead:** `PROVED WITH TARGET Pic_b(B_T)`, the target enlargement "forced by
a theorem (10.8), not chosen"; F3 accepted in full; the requested
restatement inserted as "What A.8's closure actually consists of".

**Assessment: the audit's reading is right, and the ruling's own concessions prove
it.**  The clause asks that `λ_{RR}` **extend** the intrinsic periodic
ruling determinant to the mixed sector, with five named requirements.  What
the paper proves is:

* Thm 10.8 — the **scalar** determinant `L_S` is **trivial** on the ruling
  plane at every finite chart (`L_S(F_α,G_β) → (C,1)` while
  `λ_{per} → (C,e)`).  This is a theorem and it is a **negative** one: the
  determinant that *is* the theory's analytic determinant does **not**
  extend to the rulings in any non-trivial way.
* Def 10.6c — the ruling determinant is therefore **installed** as a second
  coordinate of a pair.  The "extension" is, at exactly the locus where an
  extension was at issue, a definition.
* Thm 10.7(e) and (10.10) — in logarithms, the decomposition of an ordered
  pair.  The paper states this itself: "the observation that the second
  component of a pair is its second component".

Consequently Weil's equality formula `D·D' = P·P' + d_1d_2' + d_2d_1'`,
which §14.2 and Thm 10.7(e) present as the equality formula obtained, is
**not obtained as a theorem of intersection theory**; it is reproduced as a
bookkeeping identity in a target chosen so that it holds.  The honest
verdict is the auditor's own restatement, which is true and modest: *the
ruling determinant is the Tate component of `λ_{RR}`, and the consistency of
that definition with the test sector is Thms 9.14a, 9.14c′.*

The counter-argument — that the target is *forced* by Thm 10.8 — is correct
and is the strongest thing that can be said, but forcing a target does not
convert a definition into an extension.  A.8 is better recorded as
**`PROVED IN THE RESTATED FORM; the clause as written is NOT EARNED`**; this is the same logical situation as A.6 and B.4, both of which
went forward as amendments.  A.8 was instead resolved by a ruling.  That inconsistency of protocol is the principal procedural finding
on row A.

### 3.2 B.7 — audit (R131.008 §4) vs ruling (R131.005 §2, adopted in Paper 44 §10)

says.  I do **not** endorse `R131.005`'s upgrade to `PROVED`: Rem 6.5a′ is
still the truth."

**Lead:** `PROVED` for test *and* mechanism on the carrier — Thm 6.5(i)–(ii)
locates the mechanism (trivial fixed-point weight on the shell; `k`-
independent Haar volume), and the passage to `Φ_{p^k}(1)` is *refuted*, not
open.

**Assessment: the audit's reading is right.**  The clause is conditional: *"if
they differ, the geometric mechanism producing the cyclotomic factor must be
located."*  They do differ — `0` versus `Z/p` in the `p`-primary part
(Thm 6.4).  What is then produced is **two** mechanisms in **two** places:
the shell volume on the carrier, and deck `μ_n` versus fixed `μ_{n-1}` on
`G_m/Z`, with **no map, functor or comparison between them**, and with a
theorem (P123.022) saying that no such map can exist in the declared
`C`-linear category.  Rem 6.5a′ — kept unchanged in the paper —
says the equality of constants holds for an unrelated
reason, and cites P123.039 §5's rule that a coincidence of constants does
not locate a mechanism.

"A refutation is not an open item" is true and is not responsive.  A refuted
bridge does not discharge a clause that demands a bridge; it shows the
clause is **unsatisfiable on this carrier** — which is precisely the
situation that produced the A.6 and B.4 amendments.  The correct dispositions
are either `PARTIAL` (per the audit, and the paper's own §6.2/§6.3 text) or
an amendment restricting B.7 to the test plus the on-carrier
weight computation.  A ruling that upgrades the verdict while leaving
the contradicting remark in place, so that "a reader who follows the audit
reads `PARTIAL` there and loses nothing", is candid but is not a resolution:
the ledger and the body of the paper disagree, and the ledger is what the
label is computed from.

**Net effect on the labels.**  Neither dissent, resolved my way, removes a
clause from the list — A.8 and B.7 would read `PROVED IN THE RESTATED FORM`
and `PARTIAL` respectively.  Under the closure rule §4 ("A.1–A.10 are
proved"), a `PARTIAL` on B.7 would make row B's label *conditional on an
amendment*, exactly as R131.005 originally had it for B.4.  That is my
recommended reading.

---

## 4. The chain to RH: what is proved unconditionally

Everything below is on Paper 43's declared carrier — a fixed finite chart
`S` (`∞ ∈ S`, `S_f ≠ ∅`), with the chart system and its colimit as
additional structure, **invertible sector only** — and for the declared
trace with `c := 0`.

### (a) The objects

Unconditionally constructed and proved:

* the graph category `G` with composition `⋆`, two-sided unit `Δ = E_1`,
  two-sided excision, and the half-density dagger (Paper 43 §§3–5;
  Prop 3.2, Lemma 8.4);
* the trace-class category `Corr_A^{tr}`, its objects `E_H = λ(H)` for `H`
  in the Banach `†`-algebra `𝓐_tr` with the corrected norm
  `\|F\|_{tr} = Λ(F)+N(F)` (Thm 8A.12, Def 8A.7b0, Thm 8A.7b);
* the numerical module: `𝓝 = 0`, hence `N_A = D_A` (Thm 9.8, import-free);
  the exact Tate sequence `0 → N_A^{prim} → N_A → B_T → 0` with `B_T`
  hyperbolic and `†`-exchanged, no splitting (Thms 9.11–9.13); the rulings
  as limits in the completion and the canonical splitting of the completion
  (Thms 9.14a–c′);
* the Frobenius family `Frob_n` — Haar measures of fixed-point strata — with
  a **true** unit `Frob_1 = Δ`, `Frob_n^† = Frob_{n^{-1}}`,
  `Frob_n⋆Frob_n^† = Δ^{(n)}`, bidegree `M(Frob_n) = (n^{1/2},n^{-1/2})`,
  injective and determining `(n,P(n))`, generating an inverse semigroup
  graded by prime sets (Paper 44 Thms 3ter.4, 3ter.6, 3ter.7, 3ter.12);
  classes in `N_A^{dist}` with nonzero ruling component (Thm 3ter.14);
* the two Gram forms and the theorem that the **Weil kernel is the Gram
  form of `Frob ⋆ Δ^{rad}`**, while the Frobenius family alone carries only
  the finite half (Paper 44 Thm 8bis.1e);
* the integral shadow `Sh_Z` on objects, with transitivity triangle and
  Möbius cofiber (Paper 44 Def 6bis.1, Lemma 6bis.2, Thm 6bis.4).

Not constructed, and required by no clause: non-invertible correspondences
as objects; effective descent along a stack covering; a continuous extension
of `I_A` to `N_A^{dist} × N_A^{dist}`.

### (b) The comparison theorem and the explicit formula

* **Paper 45 Thm 9.4** — Weil's explicit formula, **proved in the
  repository**, for real `F ∈ C_c^∞`, `h = F⋆F^†`, symmetric zero sum:
  `Σ_ρ Φ_F(ρ)Φ_F(1-ρ) = 2Φ_F(0)Φ_F(1) + \frac1{2π}∫|\hat F|^2[Reψ(¼+iτ/2) -
  \logπ]dτ - Σ_{2≤n<e^{2T}}Λ(n)n^{-1/2}[h(\log n)+h(-\log n)]`, prime sum
  finite.  Imports (E1)–(E8), (R1), each named with the clause and theorem
  it serves.  Unconditional.  This is a correct classical proof, not a new
  theorem, and the paper does not claim otherwise.
* **Paper 45 Thm 9.6 (9.9)–(9.10)** — the comparison:
  `I_∞(Γ_F,Γ_F) = T_∞(Γ_{F⋆F^†}) = β_T(M Γ_F,M Γ_F) - Σ_ρΦ_F(ρ)Φ_F(1-ρ)`,
  and on the primitive radial sector `I_∞ = -Q(F) = B_{nuc}(F,F)`.
  Unconditional **as a statement about the declared trace with `c = 0` in
  the colimit** (convention (C1)); at a fixed chart it holds only inside the
  window `R(Γ_h) < \log ℓ_{next}(S)` and is **false** outside it.
* **Paper 45 Cor 9.6a** — `c = 0` is the **unique** real constant for which
  that identity holds (identity-level uniqueness; round 3 correctly deleted
  the round-2 claim that the *sign condition* fails for `c ≠ 0`).
  Unconditional.  This upgrades Paper 43's declared `c := 0` from a
  convention to a theorem of row C, and closes D128 `C9`.
* **Paper 45 Thm 9bis.2′** — the Tate poles by residues of the continued
  Euler-product symbol: `|S_f|+1` and `0` at a chart, `1` and `1` in the
  continuation; the pair is the polar packet `2Φ_F(0)Φ_F(1) = β_T(M,M)`.
  Unconditional, and independent of Mertens.

**Honest reading of (b).**  `T` was *defined* so that `T̂` is the
prime-power-plus-Gamma side (Def 8.6, Rem 9.7a).  Therefore (9.9) =
(definition) + (classical explicit formula) + (rearrangement) + (the `β_T`
identification, which is the one piece that is a statement about the
constructed objects).  This is not fraud and the papers do not present it as
more; but anyone reading "the comparison theorem is proved" should
understand that the theorem's arithmetic content is Thm 9.4, which is
Weil's, and its structural content is Thm 8.1.

### (c) Sufficiency of primitive radial tests — Paper 45 Thm 10.4

**Statement.**  If RH is false, there exist nonzero compactly supported
**primitive** real tests `F_+` (even) and `F_-` (odd) with
`Σ_ρ Φ_{F_±}(ρ)Φ_{F_±}(1-ρ) < 0`.  Hence `q_T ≥ 0` on `P_T` for every `T`
implies RH.  Unconditional; imports (E2)'s no-real-zeros clause (used at
(10.1) and nowhere else), (E3d), (E6), and the repository construction
`106_11` Thm 1.

**Assessment.**  This is the one place in the three papers where a gap that
the corpus had been asserting as classical since `113_07` Prop 4.1 is
actually closed.  The mechanism is right: `Π = -∂_t^2 + ¼` gives
`Φ_{ΠG}(s) = s(1-s)Φ_G(s)`, kills both Tate moments, preserves support,
reality and parity, and is injective **by analyticity** (the D128 `C10`
point, correctly handled).  The `C10` fix is correct and important: the
round-1 argument "rescale the real coefficients `a_N,b_N` by `ρ(1-ρ)`" is
wrong because those coefficients must stay real, and the repair — that
`106_11`'s real-linear map `(a,b) ↦ Z_R(s_0)Φ(s_0)^N(a+bs_0^2)` is an
isomorphism iff `s_0^2 ∉ R`, i.e. iff `s_0` is neither real nor purely
imaginary, the "not real" clause being exactly `ζ(σ) ≠ 0` on `(0,1)` — is
the right argument and is traced to `106_11` (9), (20), (21).  The tail
absorption is correctly reattributed to the degree `D ↦ D+2`, not to `N`.
**I endorse Thm 10.4 without qualification, and I record that it is the
principal new mathematical contribution of phases 130–132.**

### (d) What row D must prove, and why no naive Hodge index is available

**Row D's target, with every hypothesis (Paper 45 §14.4):**

> `I_∂ ≤ 0` on every primitive radial class `Γ_g`, `g ∈ C_c^∞(R)`, on the
> **colimit** `D_A^∞` with `T_∞`, for the trace with **`c = 0`**.

By Thm 9.6 (9.10) that target equals `Σ_ρΦ_g(ρ)Φ_g(1-ρ) ≥ 0` on primitive
tests, and by Thm 10.4 the primitive class is sufficient.  So **row D's
target implies RH unconditionally**, with the explicit formula proved in the
repository.  Four hypotheses travel with it and none may be dropped: the
colimit quantifier (C1); `c = 0` (for `c ≠ 0` the correction `c\|F\|^2` does
**not** vanish on the primitive sector, Cor 9.6a(ii), so the identity route
to RH is unavailable); primitivity; radiality.

**The standing negatives.**

1. **Paper 43 Thm 14.1.**  `I_A(F,F) = \frac1{2π}∫|\hat F(χ)|^2(\hat T(χ)+c)dχ`
   is real; `m := \sup \hat T < ∞`; then (a) `I_A` has **infinite negative
   index for every `c`** (`\hat T + c → -∞` on every component, and there are
   countably many); (b) infinite **positive** index iff `c > -m`, hence
   indefinite; (c) for `c = 0`, `m ≥ \logπ + γ + 3\log 2 + π/2 ≈ 5.372 > 0`,
   so the hypothesis of (b) holds and the form **is** indefinite with
   infinite index on both sides, unconditionally; (d)
   `(D_A^{prim})^{⊥ I_A} = 0` and there is **no** `D_A`-module splitting of
   the Tate boundary.  The paper also notes the escape is closed from the
   other side: for `c ≤ -m` the form is negative **definite**, which makes
   *every* class negative, rulings included, and is equally useless.
2. **Paper 44 Thm 8bis.4a.**  At **every** finite chart,
   `\hatω_{fin}(0) = Σ_{p∈S_f}(\log p)\,2p^{-1/2}/(1-p^{-1/2}) > 0`, and
   `g_T := Π(φ(·/T))` is **primitive** with `\hat g_T` concentrated near
   `τ = 0`; hence `Q_{fin}(g_T) > 0` for large `T`: **positivity fails on
   the pure Frobenius form, unconditionally, at every chart.**  The colimit
   version is `OPEN` and is not asserted (`\hatω_{fin}^∞` is unbounded).
3. **Paper 44 Thm 8bis.7, conditional under `(H_L)`.**  (a) `PROVED`: if
   `(H_L)` holds for arbitrarily large `L` — a primitive
   `g_* ∈ C_c^∞([L/2,L])` with `Q(g_*) < 0` and
   `R(L) = L e^{-L/4}\|g_*\|_∞\|g_*\|_{C^1}/|Q(g_*)| → 0` — then positivity
   **fails** on the Dirichlet-polynomial class.  (b) `CLASSICAL`: if RH
   fails, `Q(g) < 0` for some primitive `g`.  (c) `OPEN`: whether such `g`
   can be taken in a **moving window** with `R(L) → 0`.  The import `(Wgr)`
   that round 4 used here was **withdrawn as false** (Lemma 8bis.6b): the
   resonant off-line pair contributes `2\hat g_L(ρ_0)\hat g_L(1-\barρ_0)`
   with **both factors positive reals**, of sizes `e^{δL}` and `e^{-δL/2}`,
   hence `∼ +e^{δL/2}` — positive, and with half the claimed exponent.  So
   "positivity on Dirichlet profiles ⟹ RH" is `OPEN` and not claimed.

**Why no naive Hodge-index argument exists.**  The classical index argument
needs a form of signature `(1, ρ-1)` on a finite-rank numerical group:
a hyperbolic plane spanned by the two rulings, orthogonally complemented by
a **negative definite** primitive part.  Every ingredient of that shape is
provably absent here:

* the positive index is **infinite** (14.1(b),(c)), not `1`, so there is no
  "one positive direction" to isolate;
* the primitive sector has **zero** orthogonal complement (14.1(d)), so
  "primitive ⊥ rulings" is not a decomposition of `N_A`;
* the rulings are a **quotient** of `N_A`, not a subobject (9.13(a)), and
  in the completion where they *are* a subobject, `I_A` does not extend
  (Rem 9.14c″) — so there is no single space carrying both the classes and
  the rulings with one form;
* the sign statement is a **colimit** statement and is **false at every
  finite chart** (Paper 44 (C1), M4; Paper 43 Thm 14.1), so there is no
  finite-chart or finite-rank approximation on which to run an index
  argument and pass to the limit;
* and the Frobenius self-intersection, which is what Weil's index argument
  bounds, **does not exist**: `Frob_n ∉ D_A`, so `I_A(Frob_n,Frob_n)` is
  undefined (Paper 44 Rem 8bis.1c), and `Δ·Δ = -∞` (Paper 44 §8bis.2) where
  Weil has `Δ·Δ = 2-2g` finite.

Row D therefore cannot be "the Hodge index theorem on `N_A`".  It must
either change the form (the papers' own suggestion: compose with a positive
operator, as `Π` does) or produce an entirely different source of
positivity.  Both PLAN §8 routes (D-H, D-E) remain open, and D-E's entry
point (`P122.028`'s detector, harmonicity ⟹ constant flux, not zero flux)
is unchanged by phases 130–132.

---

## 5. Weil's proof for curves over `F_q`, step by step, against `Spec Z`

| Weil's step | what it is | `Spec Z` analogue | status |
|---|---|---|---|
| **1. The surface** | `C × C`, a smooth projective surface; divisors on it | `C_S`, the idele class group of a finite chart; "correspondences" are elements of its convolution algebra.  `Y`, the "noncollapsed square", is never constructed as a surface; A.1's "descent" is a filtered chart system with retraction | **SUBSTITUTED.**  The carrier is a group, not a square.  Every operation Weil gets from geometry is here got from harmonic analysis on that group. |
| **2. Correspondences** | *all* divisor classes on `C×C`, in particular graphs of non-invertible maps of degree `q` | `G`, generated by graphs of **automorphisms** (multiplications by ideles); `Corr_A^{tr}` its trace-class completion | **CONSTRUCTED ON THE INVERTIBLE SECTOR ONLY.**  Non-invertible correspondences are `NOT CONSTRUCTED` (Paper 43 §11bis item 5(v)) and are required by no clause.  This is the single largest structural gap, and the paper states it. |
| **3. Composition, transpose, unit** | `⋆` by pull–tensor–push on `C^3`; transpose by swap; `Δ` the unit | convolution; half-density dagger; `Δ = E_1` | **PROVED** (A.3, A.4), and genuinely so.  But `Δ` is **not** trace class (Rem 8.11), so `Δ` and the `E_a` are objects of `G` while the trace, `I_A`, `M` and `λ_{RR}` live on the smeared objects `E_F` and the rulings live in `N_A^{dist}`: Weil's three ingredients live in **three different objects** joined by comparison maps (Paper 43 §11bis item 5, finding F15).  Weil has them in one group. |
| **4. Frobenius** | `Γ_F` of bidegree `(1,q)`, with `Γ_F ∘ Γ_F^t = q·Δ` and `Γ_F·Δ = \#C(F_q) = 1 + q - Σα_i` | `Frob_n` (Haar measures of fixed-point strata), bidegree `(n^{1/2},n^{-1/2})`, `Frob_n⋆Frob_n^† = Δ^{(n)}`, finite contact `Λ(n)n^{-1/2}` exactly | **CONSTRUCTED, in a normalization that divides out the degree.**  The half-density normalization is what makes the dagger an inverse (Paper 43 §11bis item 5(ii)); it is a theorem, but it removes the factor `q` that Weil's inequality is *about*.  And `I_A(Frob_n,Frob_n)` **does not exist**.  So the Frobenius exists; its self-intersection does not. |
| **5. Intersection pairing** | the intersection form on `NS(C×C)`, finite rank `ρ` | `I_A(F,G) = T(F⋆G^†)` on `N_A = D_A`, infinite rank | **CONSTRUCTED, with the wrong signature type**: indefinite, infinite index on **both** sides, no orthogonal complement for the primitive part (Thm 14.1).  The specification (§1) explicitly admits infinite rank as the coherent target; it does not follow that an index theorem survives, and 14.1 proves it does not in the naive form. |
| **6. Castelnuovo–Severi / Hodge index** | signature `(1,ρ-1)`; `D·D ≤ 0` on the primitive part | — | **ABSENT, and provably not available in the naive shape** (Thm 14.1, Thm 8bis.4a).  No polarization `H` is constructed anywhere in rows A–C.  This is row D's entire content. |
| **7. Riemann–Roch as a dimension formula** | `χ(D) = ½D·(D-K) + χ(O)`, together with `h^0 ≥ 0` and a vanishing `h^2 = h^0(K-D) = 0`, converts an **equality** of Euler characteristics into an **inequality** on `D·D` | `λ_{RR}`: a based Hermitian biextension into `Pic_b(B_T)`, with the "equality formula" (10.10) | **AMENDED INTO SOMETHING ELSE.**  There is **no section space, no `h^0`, no dimension, hence no nonnegativity, hence no inequality.**  (10.10) is an identity of based lines and, in its second slot, a definition.  All three leads say this in their own words ("the section theory with nonnegative dimension that turns Riemann–Roch into an inequality is the content of RH and belongs to row D").  Clause A.8 itself ends "This clause supplies no Hodge-index sign", so the specification was written knowing this. |
| **8. Conclusion `|α_i| = q^{1/2}`** | from 6 + 7 applied to `aΔ + bΓ_{F^k}` | RH via Thm 9.6 (9.10) + Thm 10.4, **given** row D's target | **CHAIN COMPLETE ABOVE THE SIGN; SIGN ABSENT.** |

**What exactly is missing for the sign.**  In one sentence: *a functor from
the correspondence theory to something carrying a **nonnegative** invariant
— a dimension, a rank, a trace of a positive operator — together with a
vanishing theorem, such that the determinant equality (10.10) becomes an
inequality.*  Weil gets this from `h^0 ≥ 0` plus Serre duality on a
projective surface.  Rows A–C supply the equality (a biextension identity in
`Pic_b(B_T)`) and prove that the obvious candidates for the missing
nonnegativity are unavailable: the effective cone `Eff_A` is a pointwise-
positivity condition on coefficients that is **not** the operator-positive
cone (Thm 10.2(e)) and descends to nothing the determinant uses; the
numerical form itself is indefinite on both sides; and the only sector on
which a sign has ever been exhibited — the pure Frobenius form — has been
shown to **fail** positivity unconditionally at every chart.  Nothing in
phases 130–132 narrows the distance to that missing functor; what they do is
make precise, with theorems, which shapes it cannot have.

---

## 6. Verdict per paper

### Paper 43 (row A)

> `ROW A: WEIL-STRENGTH-COMPLETE` on the declared carrier (fixed finite
> chart `S`, chart system and colimit as additional structure; invertible
> sector), A.6 amended, A.8 with target `Pic_b(B_T)`, dissent recorded,
> no sign.

**Honest as recorded: YES, with two reservations.**  Every qualification a
demanding reader needs is present in §14.0a–b, §14.1 and §11bis, usually in
sharper words than this note would use, and Thm 14.1 is published *against
interest*.  Reservations:

1. **A.8 is over-graded.**  `PROVED WITH TARGET` should read `PROVED IN THE
   RESTATED FORM; the clause as written is NOT EARNED` (§3.1).  The full
   acceptance of F3 concedes the substance; only the grading
   word differs.  A.6 and B.4 went forward as amendments in the
   same logical situation; A.8 did not.
2. **The label's name overstates.**  The specification defines Weil-strength
   as *equality of structural burden* (§1); Paper 43 §11bis item 4 states
   that this equality "is **not** established", and item 5 narrows but does
   not remove the statement (non-invertible objects absent; the three
   ingredients in three different objects).  The closure rule §4 is
   clause-based, so the grant is procedurally correct — but the phrase
   "Weil-strength-complete" will be read by anyone outside this repository
   as the thing §11bis item 4 denies.  **Recommendation: never print the
   label without "on the invertible sector" attached**, as §14.0b's SECTOR
   line already does internally.

A.1, A.5 and A.7 additionally rest on definitional readings (descent-as-
chart-system; the declared trace with a declared non-unit-shell
normalization; effectivity as coefficient nonnegativity).  All three are
disclosed in the paper, so the verdicts are honest; a reader should know
that three of the ten clauses are closed by choosing the reading that makes
them true.

### Paper 44 (row B)

> `ROW B: WEIL-STRENGTH-COMPLETE` on Paper 43's declared carrier, as a
> theorem about row A's declared trace; B.4 amended; B.7 by ruling
> with dissent recorded.

**Honest as recorded: YES, except that B.7 should read `PARTIAL`.**  Row B
is the most disciplined of the three ledgers: `(Wgr)` was withdrawn as
**false** by a counter-computation after it had been carried
for two rounds; a round-4 `PROVED` was withdrawn as a non-sequitur (W19);
the interface with Weil's criterion is declared a colimit statement and
declared **false at a finite chart**; `I_A(Frob_n,Frob_n)` is declared
non-existent rather than given a convention-dependent rate.  That is what
honest labelling looks like.  The one blemish is B.7 (§3.2): the ledger says
`PROVED`, the body of the paper says `PARTIAL`, and the body is right.
Under the closure rule that would make the label conditional on a B.7
amendment, exactly as R131.005 had it for B.4 before that decision.

### Paper 45 (row C)

> `ROW C: WEIL-STRENGTH-COMPLETE` on Paper 43's declared carrier, as a
> theorem about row A's declared trace with `c = 0`, the explicit formula
> proved in the repository (Thm 9.4).

**Honest as recorded: YES, with one sentence of the audit to be
qualified.**  This is the strongest paper of the three in proof content:
Thm 9.4 is a correct proof with every classical input named (including the
round-2 self-correction on (E3b)/(E3c), which is exactly the failure mode
clause C.8 exists to prevent); Cor 9.6a genuinely upgrades `c = 0` from a
declaration to a theorem and closes D128 `C9`; Thm 9bis.2′ is a real residue
computation; and **Thm 10.4 closes a gap that the corpus had been asserting
as classical since `113_07` and that nothing in the corpus had proved**.
The qualification: R132.007 §3's "Nothing is satisfied by a definition
alone" is too strong.  C.3's place-additivity is definitional — the paper
says so in §5.1, in italics, and refuses to soften it — and the first half
of C.6 is the classical explicit formula transported across the definition
of `T`.  The paper is honest about both; the audit's summary sentence is
not, and should read "nothing is satisfied by a definition alone **except
where §5.1 discloses that it is**".

### The three together

**What is unconditionally proved, stated without a label:** a commutative
correspondence theory on the idele class group of a finite chart, with
composition, an involution, a declared trace whose symbol is by construction
the prime-power-plus-Gamma side of the explicit formula, a vanishing
numerical radical, a canonical hyperbolic Tate boundary, a Frobenius family
with a true unit and an integral shadow reproducing `Λ` in degree, a correct
proof of Weil's explicit formula, the identification of the Weil quadratic
form with that trace on primitive radial classes for the unique constant
`c = 0`, and — new — the sufficiency of primitive radial tests for Weil's
criterion.  **What is unconditionally proved about the zeros of `ζ`:
nothing**, and all three papers say so in the same words.  The sign is row
D's, the shapes it cannot have are now theorems, and the missing object is
named precisely: a nonnegative-dimension section theory that turns the
Riemann–Roch equality into an inequality.
