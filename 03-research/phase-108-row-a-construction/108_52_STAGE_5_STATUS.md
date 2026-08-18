# 108.52 — Stage 5 status

## 1. Verdict

> **Stage 5 is partially closed, with an exact boundary.** The naive
> comparison map between the graded quotient of Stage 2 and the numerical
> quotient $V$ of Stage 0 is **proved impossible**, in both directions
> (108_50). A regularized route around that impossibility is
> **architecturally available** and passes 108_90's design-condition
> pre-test (108_51 §4), but its central analytic requirement — convergence
> of the regularized pairing — is **not established**, and a toy model
> gives concrete evidence that it is a genuine open problem, not a
> formality (108_51 §3). Stage 3's assembly is therefore **not shown to be,
> and not shown not to be, an intersection number**: 108_51 §2 states
> exactly the three conditions (I, II, III) whose joint truth would make it
> one.

| item | status |
|---|---|
| comparison map at generator level, forward direction | **impossible, proved** (108_50 Thm 1.2) |
| comparison map at generator level, reverse direction | **impossible, proved** (108_50 Thm 2.2) |
| regularized route: existence of a cutoff family (Condition I) | architecturally clear, not formally constructed in Stage 0's own terms |
| regularized route: convergence of the regularized pairing (Condition II) | **open**; toy model diverges (108_51 Prop.\ 3.1) |
| regularized route: correspondence of radicals (Condition III) | **open**, and not examinable here (Stage 0's radical data outside read scope) |
| design-condition pre-test on the regularized route | **passes** (108_51 §4) |
| Stage 3's assembly shown to be an intersection number | **no** |
| Stage 3's assembly shown *not* to be an intersection number | **no** — only the naive route is excluded |

## 2. Answering the four deliverables directly

**(1) Comparison map.** Constructed the two natural candidate maps (graded
witness $\to$ correspondence divisor, and its converse) and showed both
fail, by two independent and elementary mechanisms: an unbounded-orbit
lemma (108_50 Lemma 1.1) applied to the character-covariant graded family
$f_s$ (108_37 §2, read from source), and an explicit worked example showing
the Mellin transform of a compactly supported function has infinitely many
zeros (108_50 Fact 2.1), obstructing the reverse direction. **The pairings
are not shown to correspond**, because no map through which "correspond"
could be tested exists at this level.

**(2) Impossibility and obstruction.** 108_50 Theorem 3 is the precise
impossibility statement. The exact obstruction, named: Stage 0's category
requires **compact support**; the graded family Stage 2 is built from is a
**dilation eigenfunction under an unbounded group/semigroup**
($\mathbb N^\times$ or the relevant local analogue, per 108_90 §2 instance
7), and Lemma 1.1 shows these two properties are mutually exclusive for any
nonzero function. This is the same clash 108_90 tabulated for Stage 3 as
posed (instance 7), now proved — not retrodicted — for the Stage 0/Stage 2
comparison specifically. The candidates listed in the task (different
test-function categories; disjoint domains) are both confirmed; the
candidate about radicals being "described by different data" is **not
examined**, because this note does not have access to
$\mathrm{rad}\,I_{\mathrm{partial}}$'s generating description (108_50
§5 Scope) — that comparison is left explicitly open, not claimed either
way.

**(3) What would have to be true.** 108_51 §2, Conditions I–III, stated with
named objects: a compactly supported regularizing family $f_{s,T}$
(Condition I); convergence of $I_{\mathrm{partial}}(D_{f_{s,T}},D_{g_T})$ to
$c_g(s)\Phi(s)$ as $T\to\infty$ (Condition II); and correspondence of the
two radicals under the resulting limiting map (Condition III). If and only
if all three hold, Stage 3's identity $L_g=c_g\Phi$ is literally an
intersection number on $V$.

**(4) Design-condition pre-test on this note's own construction.** Applied
in 108_51 §4: the regularized route puts equivariance on the untruncated
family $f_s$ and finiteness on the cutoff family $f_{s,T}$, and regularizes
the **pairing** via the $T\to\infty$ limit — exactly the prescribed escape.
**It passes.** But 108_51 §3's toy computation (Proposition 3.1, verified
numerically: a mass-zero cutoff pairing diverging as $T^{0.7}$) shows that
passing the architectural pre-test does not supply Condition II's
convergence; that remains to be proved or disproved by genuine analysis,
most plausibly requiring an $s$-dependent renormalization on top of the
cutoff, which is not attempted here.

## 3. Why "partially closed" and not "obstructed"

The naive route is fully and permanently closed: 108_50's theorems do not
depend on unknowns and will not be revisited by further information about
Stage 0's internal definitions, because they use only the one property
(compact support) that the task specification itself supplies. That part of
Stage 5 is **closed**. What remains open is a genuinely different question
— whether a *regularized* comparison exists — that 108_50's impossibility
theorems do not touch and 108_51 does not resolve. This is a boundary, not
a dead end: 108_51 §2 names exactly the three theorems that would need to
be proved to move it, and §4 confirms the one architectural constraint
(the design condition) they must additionally satisfy is already met.

## 4. Unsparing list of what remains open

* Condition I: no explicit cutoff family $f_{s,T}$ has been constructed
  inside Stage 0's own formalism (only argued to be unproblematic in
  principle).
* Condition II: not proved, not disproved for the actual
  $I_{\mathrm{partial}}$; the toy model's divergence is evidence of
  difficulty, not a proof of failure for the real operator, whose
  definition this note did not read.
* Condition III: not examined at all; requires access to
  $\mathrm{rad}\,I_{\mathrm{partial}}$'s generating description, which
  lies in Stage 0's own paper(s), outside this note's read scope.
* The candidate "radicals described by different data" (zeros of $\Phi$
  versus whatever generates $\mathrm{rad}\,I_{\mathrm{partial}}$),
  flagged in the task as worth checking, is **not checked** here, for the
  same reason.
* Off-real-segment zeros of $\Phi$ remain unexamined (inherited from
  108_38, unchanged).
* No renormalization scheme analogous to 108_36's removal of the constant
  $(\log p)\sum_pC_p$ has been proposed for the $T$-divergence found in
  108_51 §3; finding one (or showing none exists) is the natural next step
  if Stage 5 is to be pursued further.
* Nothing here bears on $\mathrm{RH}$. `ROW_A_STATUS` is not promoted.

## 5. Scope

This note is a synthesis of 108_50 and 108_51, written in this session; it
introduces no new mathematical content beyond aggregating their verdicts
into the closing table above. Its own Scope restrictions are exactly the
union of 108_50 §5 and 108_51 §5: Stage 0's internal definitions
($D_f$, $T(\cdot)$, $\mathrm{rad}\,I_{\mathrm{partial}}$) were not read
and are not reconstructed; every claim above is traceable to a proved
theorem, a numerically verified closed form, or an explicit statement of
what is not known.

## 6. Verifier

`108_52_stage_5_status.py` re-runs `108_50_no_comparison_map_at_generator_level.py`
and `108_51_toy_regularized_pairing_divergence.py` as subprocesses and
confirms both exit 0, then re-prints the closing table of §1 as a
machine-checked consistency summary (it checks that the two prerequisite
scripts exist and ran cleanly; it does not re-derive their mathematical
content, which lives in those two files and the corresponding `.md`
documents).
