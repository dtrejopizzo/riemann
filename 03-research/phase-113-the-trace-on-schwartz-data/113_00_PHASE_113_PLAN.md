# 113.00 — Phase 113 plan: the trace on Schwartz data

## 0. The one remaining gap in d1

107_239 (2.1)–(2.2) writes the renormalized corner trace, for compactly
supported $h$, as a sum of *local* Tate-normalized integrals

$$\mathfrak T_S(h)=\sum_{v\in S}\int_{\mathbb Q_v^\times}'\frac{h(u^{-1})}{|1-u|_v}\,d^\times u,$$

and 107_239 §3 stabilizes this in $S$ using compact support: only finitely
many primes see a nonzero shell. Phase 111 proved every *global* convergence
question about the corner pairing (polar terms, zero sum, prime sum) is fine
on Schwartz data, but flagged (111_03 §3) that this specific finite-$S$
stabilization mechanism does not exist for Schwartz $h$: every prime power
contributes. This phase asks whether $\mathfrak T(h)$ can be constructed
directly for Schwartz $h$ by summing the local integrals over *all* places,
or whether it cannot.

## 1. Pre-registration: what would refute each task

Written before any Laurent expansion, residue computation, or numerical
integration below is run.

**Refutation of Task 1 (the central risk).** The question is whether
Tate's principal value of the finite-place local integral, for Schwartz $h$,
is the *same* object as 108_12/108_17's shell-by-shell $K$-truncation limit
(which 108_17 proves is finite iff $h(1)=0$, the exact analogue of phase
108's $\varphi_0=0$ obstruction) — or a genuinely different, and finite,
regularization.

* **Refutation (negative direction).** If *every* reasonable regularization
  of the shell-$0$ (unit-shell) contribution — not just the raw
  $K$-truncation — turns out to require $h(1)=0$ for finiteness (e.g. if an
  independent construction via meromorphic continuation in an auxiliary
  parameter also has a pole at the point of interest whose residue is
  forced nonzero whenever $h(1)\ne0$, with *no* legitimate way to discard
  the pole), the central risk resolves exactly as feared: $h(1)=0$ is a
  hard, unconditional obstruction, inherited verbatim by Schwartz $h$, and
  Task 1 fails cleanly.
* **Refutation (positive direction, of the "clean escape" reading).** If a
  genuine alternative regularization is found that is finite for every $h$
  *and* is unambiguous (scheme-independent, pinned down by the data already
  fixed in this programme with no further external input), then $h(1)=0$
  is not required at all, and the central risk resolves cleanly positive.
  This must be checked directly, not asserted: **the test is whether two
  independently reasonable parametrizations of the same regularization
  agree.** If they disagree by a nonzero, $h(1)$-proportional amount, the
  "positive" reading is refuted in its strong form (finite always, no
  further condition) and the correct statement is the intermediate one
  fixed in §2 below: finite under any fixed scheme, canonical
  (scheme-independent) iff $h(1)=0$.

This is a real fork with three live outcomes, not two: (a) hard divergence
forced, extending 108_17 verbatim; (b) fully free, no condition at all;
(c) finite under any scheme, but canonical only at $h(1)=0$. All three are
logically prior to the computation and the computation must be capable of
landing on any of them.

**Refutation of Task 2 (global sum).** If $\Sigma_p[\text{local integral at
}p]$ diverges for *every* Schwartz $h$ satisfying whatever condition Task 1
names (even after excluding the shell-0 term), by a mechanism analogous to
108_06 Theorem 4.1 (the graded family's global sum diverging throughout the
critical strip), Task 2 fails and the construction cannot proceed to Task 3.
The check must include a control case that genuinely diverges (e.g. $h$ with
only polynomial-in-$\log r$ decay, no exponential margin) so the convergence
test is not vacuous.

**Refutation of Task 3 (the construction).** If the finite-place sum
converges but the *archimedean* place's own contribution — even taking
111_01's polar-term and zero-sum results as given — cannot be shown finite
without re-opening 111_01's Assumption T (the untested claim that the
trace-side identity extends from compact support to Schwartz data), then
Task 3 cannot be closed outright; it must be reported as conditional on that
named assumption, not silently treated as closed.

**Refutation of Task 4 (compatibility).** If the condition named in Task 1
(expected candidate: $h(1)=0$ for $h=f\star\widetilde g$, i.e.
$(f\star\widetilde g)(1)=0$) is a **quadratic** condition on $g$ once
$\widehat f=\xi\widehat g$ is imposed (unlike the *linear* conditions
$\widehat g(0)=\widehat g(1)=0$ found harmless in 111_02/111_03), then
satisfiability is not automatic and must be checked, not assumed: the test
is whether $\xi(\tfrac12+it)$, weighted by $|\widehat g(\tfrac12+it)|^2$ for
$g$ ranging over a natural family, can be made to integrate to zero. If
$\xi(\tfrac12+it)$ turns out to be of one fixed sign for all real $t$ — an
entirely unconditional, RH-independent fact to check numerically, not an
assumption — the quadratic form would be sign-definite on every nonzero $g$
and the condition would be **unsatisfiable**, killing this route
permanently. This is checked directly in 113_04, with an explicit sign
computation at two points, before any claim of satisfiability is made.

**If none of the above could have gone the other way** — i.e. if the phase
had been set up so every possible computational outcome was going to be read
as success — the exercise would be circular. They are not: Refutation of
Task 1's negative direction has a live prior (it is exactly 108_17's own
finding, unmodified, for the raw construction); Refutation of Task 4 has a
live prior (sign-definiteness of $\xi$ on the critical line is a real,
checkable, a priori open possibility until computed).

## 2. What a positive Task-1 outcome is allowed to mean

Given the risk of a false "yes" reading, the phase commits in advance to the
following precise standard, chosen among the three outcomes of §1 *before*
computing which one obtains: a construction of $\mathfrak T_v(h)$ at a finite
place $v=p$ counts as achieved only if it is (i) finite for the relevant
class of $h$, and (ii) does not depend on an unstated free choice (a
regularization scheme not fixed by the sources read). A finite-but-scheme-
dependent construction is recorded candidly as *not* a construction of
$\mathfrak T_p(h)$ as a function of $h$ alone — only as evidence that
$h(1)=0$ is the right closure condition. This standard is fixed now, before
the Laurent expansion is computed, precisely so that discovering the
ambiguity cannot be spun as either a clean success or a clean failure after
the fact.

## 3. Source rule

No definition below may use a zero of $\xi$, a Li coefficient, or a
positive part of a Weil-type form. $\xi$ itself may be used. Theorems may
mention zeros (e.g. citing Hardy's unconditional theorem that $\xi$ has
zeros on the critical line, and the unconditional sign change of $\xi$
there); no *definition* does.

## 4. Deliverables

* `113_01_THE_LOCAL_INTEGRAL_FOR_SCHWARTZ_DATA.md` / `.py` — Task 1.
* `113_02_THE_GLOBAL_SUM.md` / `.py` — Task 2.
* `113_03_THE_CONSTRUCTION.md` / `.py` — Task 3.
* `113_04_VERDICT.md` / `.py` — Task 4.
* `113_99_PHASE_113_SUMMARY.md` / verifier — aggregate.

Nothing in this phase bears on RH. Riemann–von Mangoldt and Hardy's theorem
are unconditional and quoted, not used to locate any zero off the critical
line or to assume one on it.
