# Phase 110 — Plan: does ξ-divisibility supply the principal subspace Row (d) needs?

## 0. What this phase is, in one paragraph

Row (d) (Hodge index) needs Riemann–Roch, which needs linear (not merely
numerical) equivalence, which needs a principal subspace $\mathcal P$ with
$\mathcal P\subseteq\mathrm{rad}\,I_\partial$, where $I_\partial$ is the
zero-free corner pairing whose radical a source theorem identifies as
$\{f:\hat f(0)=\hat f(1)=0,\ \hat f(\rho)=0\ \forall\text{ zeros }\rho\text{ of
}\xi\}$. The source rule forbids defining $\mathcal P$ using a zero of $\xi$,
but permits using $\xi$ itself. The candidate this phase tests is
**ξ-divisibility**: $\mathcal P\subseteq\{f:\hat f=\xi\cdot\hat g\text{ for
some admissible }g\}$, for which $\hat f(\rho)=\xi(\rho)\hat g(\rho)=0$ is
immediate. Three tasks: (1) show the existing graded-family principal
witnesses are *not* of this form; (2) characterize the ξ-divisible class
concretely; (3) determine candidly whether arranging $\mathcal
P\subseteq\{\hat f=\xi\hat g\}$ for a geometrically defined $\mathcal P$ is
possible without smuggling in RH, or without smuggling in the definition
itself.

## 1. Standing facts taken as given (quoted from the prompt / cited without
re-derivation)

* $I_\partial(D_f,D_g)=\hat f(0)\overline{\hat g(0)}+\hat f(1)\overline{\hat
  g(1)}-\sum_\rho \hat f(\rho)\overline{\hat g(\rho)}$, sum over zeros $\rho$
  of $\xi$ with multiplicity (Weil explicit formula, cited from the phase
  prompt, not re-derived here).
* $\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$, entire, functional
  equation $\xi(s)=\xi(1-s)$, $\xi(0)=\xi(1)=\tfrac12$ (standard normalization;
  verified numerically below, not re-derived from first principles of
  analytic continuation, which we take as known).
* The graded family $\mathcal G=\{\mathcal L_s\}_{s\in\mathbb R}$,
  $f_s(r)=c\,r^s$, and the principal witnesses
  $\mathrm{Prin}'(\mathcal G)=\bigcup_s\mathrm{div}(\mathcal
  L_s)$ at every weight $s\in\mathbb R$, including mass-zero differences
  $f_{s_0}-f_{s_1}$: read from 108\_03 and 108\_31 (the only two files this
  phase is permitted to open), not re-derived.
* 108\_31 §5 already flags, and this phase inherits as a standing fact, that
  a single weight-$s$ witness is a **point mass in the grade** (not smooth,
  not compactly supported, not balanced) and hence not literally an element
  of the corner pairing's admissible domain (which the source material
  describes as smooth, compactly supported, balanced profiles). This phase
  treats "admissible" test data as: smooth, compactly supported on a bounded
  sub-interval of $(0,\infty)$ (109/108-style corner-pairing input). This is
  stated as a **named assumption** (ADM), since the phase-108 files define
  the domain by cross-reference to 108\_24, which this phase was not
  permitted to open.

**Named assumption (ADM).** *Admissible test data $f$ for the corner pairing
are smooth, compactly supported functions on $(0,\infty)$ (equivalently, on
$\mathbb R$ after $r=e^x$), so that $\hat f$ denotes the (bilateral) Mellin
transform $\hat f(w)=\int_0^\infty f(r)r^{-w}\,d^\times r$, entire in $w$.*

This is the weakest reading consistent with 108\_31 §5's own description
("smooth, compactly supported profile") and is the reading under which the
Weil explicit formula sum in $I_\partial$ literally converges term by term
(entire $\hat f,\hat g$ of finite exponential type, decaying rapidly on
verticals, matching known unconditional bounds on $\#\{\rho:|\mathrm{Im}\,\rho|\le T\}$
so the zero-sum converges absolutely). Nothing in Task 1–3 below depends on
sharpening (ADM); a strictly *smaller* admissible class only makes the
negative results of this phase easier to obtain, never harder — see Lemma
110.2.3.

## 2. Pre-registered refutation criteria (written BEFORE any computation)

This section is written first, before Task 1's computation, per the
governing instructions. It commits, in advance, to what outcome would count
as a **refutation** of the hypothesis that ξ-divisibility is a viable,
non-circular route to $\mathcal P\subseteq\mathrm{rad}\,I_\partial$, and
what would count as *support* — so that the later verdict cannot be steered
by the result.

**H (the hypothesis under test):** *ξ-divisibility can be established, for a
geometrically/algebraically defined nonzero candidate $\mathcal P$
(intersected with the admissible test class (ADM)), as a **theorem** rather
than a definition, and without appeal to the location of any zero of $\xi$ or
to RH.*

**What would REFUTE H (count as a positive, non-circular result for the
programme):** an explicit, nonzero subspace $\mathcal P_0$ of admissible test
data, defined by a condition that does **not** mention $\xi$-divisibility,
does **not** mention a zero of $\xi$, and does **not** simply repackage
"$\hat f=\xi\hat g$" under a new name — together with a *proof* that every
$f\in\mathcal P_0$ satisfies $\hat f=\xi\hat g$ for some admissible $g$. If
Task 1 exhibits such a $\mathcal P_0$ (e.g. if the graded family's witnesses,
or some finite combination of them, turned out to satisfy $\hat f=\xi\hat g$
for elementary reasons), that refutes the "this is empty/circular" concern
and the phase would report H as *supported*, proceeding to characterize
$\mathcal P_0$ in Task 2 as a genuine candidate for Row (d).

**What would CONFIRM the negative (H fails, and phase stops or narrows)**:
either

* (N1, *circular*) every attempt to name a nonzero $\mathcal P_0\subseteq$
  (ADM) with $\hat f=\xi\hat g$ forces the defining condition on $\mathcal
  P_0$ to *be* "$\hat f\in\xi\cdot(\text{admissible})$" itself, with no
  independent geometric handle — i.e. the only way to write down elements is
  to solve for them by division by $\xi$ after the fact; or
* (N2, *vacuous*) it is proved, from classical unconditional facts about
  $\xi$ (order, type — **not** from the location of its zeros), that
  $\{\hat f=\xi\hat g: f,g\in(\text{ADM})\}=\{0\}$, i.e. no nonzero
  admissible $f$ is ξ-divisible by an admissible $g$ at all. This is a
  **stronger** and more informative outcome than "RH in disguise": it would
  mean the route is closed for a reason that has *nothing to do with where
  the zeros are*, hence provably not equivalent to (a disguised form of) RH.

**What would show H is specifically "RH in disguise"** (the outcome the
prompt asks to watch for and, if found, to stop at): a demonstration that the
*only* way to secure $\mathcal P_0\subseteq\{\hat f=\xi\hat g\}$ — after
excluding (N1) and (N2) — requires, at some step, information about *where*
the zeros $\rho$ lie (e.g. that they lie on $\mathrm{Re}=1/2$), or a
positivity statement classically known to be equivalent to RH (e.g. a
sign-definite quadratic form built from the same data as RH's classical
Weil-positivity criterion). This is logically distinct from (N2): (N2) is an
unconditional impossibility that holds regardless of RH's truth; "RH in
disguise" would be a *conditional* equivalence.

**Non-vacuity check on the test itself (mandatory before proceeding).** All
three of "refuted", "N1/circular", "N2/vacuous", and "RH in disguise" are
outcomes reachable by the computations of Task 1–3 below, and each is
distinguishable from the others by an explicit, falsifiable computation (a
growth-rate estimate for N2; an explicit attempted construction for N1 and
for refutation; a search for zero-location dependence for "RH in disguise").
In particular the test is **not** rigged to output only one answer: Task 1's
computation on the graded family could, in principle, have come out positive
(some $f_{s_0}-f_{s_1}$ could a priori have satisfied $\hat f=\xi\hat g$ for
elementary reasons — e.g. if $\xi$ had a real zero at some rational-looking
point, or if the delta-function transform were compatible with entire
divisibility in some limiting sense). That it does not is a computed fact,
not a foregone conclusion. The test is therefore non-vacuous and the
pre-registration stands.

## 3. What follows

* Task 1 (110\_01): compute whether the graded family's point-mass
  witnesses are ξ-divisible. Expected outcome per the prompt: no; this
  section proves it and identifies the precise mechanism (two independent
  obstructions are found: a category mismatch — point masses are
  distributions, not entire functions, so "$\hat f=\xi\hat g$" is not even
  well-posed for them — Lemma 110.1.2/110.1.3).
* Task 2 (110\_02): characterize $\{\hat f=\xi\hat g\}$ within (ADM). Main
  result: $\xi$ is entire of order $1$ but **infinite (non-finite) type**
  (Theorem 110.2.2, proved from Stirling's asymptotic for $\Gamma$, an
  unconditional fact having nothing to do with zero locations), while every
  admissible (compactly supported) $\hat g$ has **finite** exponential type;
  consequently $\hat f=\xi\hat g$ forces $f$ itself to be non-compactly
  supported for every nonzero admissible $g$ (Theorem 110.2.4). So
  $\{\hat f=\xi\hat g\}\cap(\text{ADM})=\{0\}$: outcome **(N2, vacuous)**.
* Task 3 (110\_03): the candor check. Given Task 2's Theorem 110.2.4, the
  verdict is delivered: **not** RH in disguise (the obstruction is proved
  from $\Gamma$'s growth alone, with $\zeta$'s value replaced by a dummy
  bounded factor, showing the zeros play no role at all in the impossibility
  argument) — and also not simply "circular" in the (N1) sense, since (N2)
  is a stronger, unconditional, unconditionally-verified closure. Both
  outcomes are recorded candidly; neither is softened.

## 4. Scope of this document

Proved here: nothing yet (this is the plan). Numerically verified here:
nothing yet.

Not established, and explicitly not claimed: any conclusion about Task 1–3;
those are computed in 110\_01–110\_03 and are binding only once verified by
the accompanying `.py` scripts.

## 5. Verifier

None for this file; `110_00` contains no numerical claims. (No `.py` is
produced for this file, matching the deliverables list, which pairs `.py`
files only with 110\_01–110\_03 and 110\_99.)
