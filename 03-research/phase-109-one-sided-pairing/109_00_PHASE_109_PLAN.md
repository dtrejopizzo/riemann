# 109.00 — Phase 109 plan: does the one-sided assembly carry a pairing with a
# zero-determined radical?

## 0. Where this starts

Phase 108 built row (a) of a Weil-style programme over $\mathbb Z$ and closed
Stages 1–5, mostly negatively. The diagnosis, quoted in full in the mission
and not re-derived here:

* The **two-sided** Tate local integral $W_p(f_a)=\int'_{\mathbb Q_p^\times}
  f_a(u^{-1})/|1-u|_p\,d^\times u$ (108_06 Theorem 3.1) always contains the
  identity-shell constant $C_p=+\infty$ (108_12 Theorem 2.1), because the
  finiteness criterion "$\varphi_0=0$" (108_17 Theorem 2.2) is violated by
  *every* member of the graded family, unconditionally, because
  $f_a(1)=1=\chi(1)$ is forced for any quasi-character (108_17 Theorem 3.1).
* Symmetrizing $\zeta'/\zeta$ under $s\mapsto1-s$ to try to repair this
  (108_91) produces an elementary, zero-blind object $\Phi(s)$ with poles at
  $s=0,1$ and exactly one zero, at $s^*=0.301692388160422091519371$ — nothing
  to do with $\xi$.
* The object that *did* survive, cleanly, is the **one-sided** sum over
  positive shells only, 108_36 Theorem 1.1:
  $$\sum_p\sum_{k\ge1}\Gamma^{\mathrm{Tate}}_{p,k}(f_s)=\sum_{n\ge1}\Lambda(n)n^{-s}=-\frac{\zeta'}{\zeta}(s),$$
  absolutely convergent for $\Re s>1$, continued meromorphically, with poles
  at every zero of $\xi$, and no zero of $\xi$ in its *definition*.

Stage 0's pairing (107_240 Theorem D, quoted verbatim in the mission) has a
**zero-determined** radical:
$$\mathrm{rad}\,I_{\mathrm{partial}}=\{f:\hat f(0)=0,\ \hat f(1)=0,\ \hat
f(\rho)=0\ \forall\ \text{zeros }\rho\text{ of }\xi\}.$$
Stage 2's radical, by contrast, is **$\Gamma$-determined**: spanned by a
single point mass at the lone zero $s^*$ of the elementary function $\Phi$,
one-dimensional. The mismatch between these two shapes is exactly what
closed Stage 5.

## 1. The hypothesis under test

> The divergence that killed row (a)'s two-sided route came from the
> identity shell ($k=0$) alone. The one-sided sum of 108_36 excludes that
> shell by construction and starts at $k=1$. So the obstruction 108_17 proved
> *unavoidable* for the two-sided functional may simply not arise for a
> genuinely bilinear pairing built the same way — and if such a pairing
> exists, and its radical turns out to be zero-determined (Stage-0 shape,
> not Stage-2 shape), rows (a)–(d) could live on one object and row (d)
> becomes a real question.

This is tested in three steps, in order, each one gating the next.

## 2. The three steps

**Step 1.** Build a bilinear pairing $B(f,g)$ from the shell functionals
$\Gamma_{p,k}$ ($k\ge1$ only), using *only* facts already proved in 108_34
and 108_36 (allowed sources). Determine convergence domain, genuine
bilinearity, and symmetry type. A proved failure here closes the phase
immediately — no further step is owed.

**Step 2 (decisive).** Compute $\mathrm{rad}\,B$ exactly, from the actual
definition, not by analogy with either Stage 0 or Stage 2.

**Step 3.** Only if Step 2 comes out zero-determined: compute the inertia of
$B$ on the quotient by its radical, in the style of 107_241 Theorem 3.1.

## 3. Pre-registered refutation criteria — written BEFORE Step 2 is computed

This is the mandatory anti-circularity step. Two failure modes wrecked
verifiers earlier in this programme: a form *defined* to be hyperbolic and
then "proved" hyperbolic, and a vector reverse-engineered from the target
identity. Neither is caught by numerics, because both statements were true
but carried no information. To make Step 2 an actual test rather than a
restatement, here is what would refute or confirm the hypothesis, decided
**before** the radical is computed:

* **Step 1 is refuted** if no construction from $\{\Gamma_{p,k}:k\ge1\}$ is
  bilinear in two independently varying arguments — i.e. if the one-sided
  sum is only ever a function of a single complex variable $s$ (a Dirichlet
  series), with no way to split it as $B(f,g)$ linear in $f$ and in $g$
  separately, matching 108_36's number at some specialization. If every
  attempted bilinearization either fails linearity in one slot or fails to
  reduce to 108_36's actual value at any specialization, Step 1 fails and
  the phase closes there.

* **Step 2 is CONFIRMED** (hypothesis survives) only if we can *prove*,
  from $B$'s actual definition and nothing else,
  $$\mathrm{rad}\,B=\{f:\hat f(0)=0,\ \hat f(1)=0,\ \hat f(\rho)=0\ \forall\
  \text{zeros }\rho\text{ of }\xi\}$$
  in Stage 0's exact shape — using only results already established for row
  (a) (i.e. *not* invoking the archimedean completion of Stage 4, which
  row (a) has not built; 108_36 §3 says so explicitly).

* **Step 2 is REFUTED** if either:
  (a) we exhibit an explicit nonzero $f\in\mathrm{rad}\,B$ whose Mellin
  transform (or its analytic continuation) does **not** vanish at some, or
  any, zero of $\xi$ — showing $\mathrm{rad}\,B$ is not *contained in* the
  zero-determined space; or
  (b) $\mathrm{rad}\,B$ is shown to have a description with no reference to
  $\zeta$'s zeros at all (e.g. determined by evaluation at a fixed discrete
  subset of $(0,\infty)$ unrelated to $\xi$), which would make the
  zero-determined description either false or vacuous.

  A refutation via (a) is a **complete witness**: one explicit function,
  checked directly, no appeal to conjecture. This is what a real test looks
  like, and it is why Step 2 is done by direct computation, not by analogy
  with Stage 0 or Stage 2.

* If Step 2 is neither cleanly zero-determined nor cleanly $\Gamma$-
  determined (e.g. a third shape, unrelated to both), that is reported
  plainly as its own outcome, and Step 3 is skipped, since Step 3 only
  makes sense on top of a confirmed zero-determined radical (an inertia
  computation on a radical of unknown provenance would not answer anything
  about row (d)).

## 4. Source discipline

Only three phase-108 files are read: 108_36, 108_34, 108_17 (quoted above
and in the mission). Everything else needed is either quoted in the mission
verbatim or introduced here as a **named assumption**, flagged as such. No
definition below uses a zero of $\xi$, a Li coefficient, the sign of a
Weil-type form, or a positive part extracted from one; results are allowed
to mention zeros of $\xi$ (Step 2's refutation witness does, necessarily),
definitions are not.

## 5. Deliverables

* `109_01_THE_ONE_SIDED_PAIRING.md` + `.py` — Step 1.
* `109_02_THE_RADICAL.md` + `.py` — Step 2, decisive.
* `109_03_THE_SIGNATURE.md` (+ `.py` if reached) — Step 3, or the reason it
  is skipped.
* `109_99_PHASE_109_SUMMARY.md` + `.py` — verdict table.

Nothing in this phase bears on RH. No status is promoted.
