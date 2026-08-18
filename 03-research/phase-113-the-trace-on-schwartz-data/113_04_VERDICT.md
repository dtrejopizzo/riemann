# 113.04 — Verdict on d1: is the construction complete?

## 0. Verdict

> **d1's construction gap is closed on an explicit class.**  113_03
> Definition 4.1 gives $\mathfrak T(h)=\mathfrak T_\infty(h)+\mathfrak
> T_{\rm fin}(h)$, finite and scheme-independent for every $h$ in the
> admissible class $\mathcal A=\{\tilde h\in\mathcal S_\eta,\ \eta>1,\
> h(1)=0\}$, modulo one inherited, undischarged assumption at the
> archimedean place (Assumption T, 111_01 §3).  Compatibility with the
> $\xi$-divisible route is a **third linear condition** on an
> infinite-dimensional space, structurally the same shape as the two
> conditions already found compatible in 111_03 — plausible, not verified
> in detail here, and that gap is stated precisely in §2.

This is not "d1 fully proved."  It is: the two genuine risks phase 113 was
built to resolve — a hidden identity-value obstruction (§1), and outright
divergence of the global sum (113_02) — are both resolved, one negatively in
a way that is absorbed (an extra linear constraint, not a wall) and one
positively.  What remains is bookkeeping, named exactly in §2–3.

## 1. What was actually at stake, restated

The risk flagged before this phase launched: 107_239's local integral
carries Tate's principal-value normalization, the same apparatus that
108_12/108_17 showed forces $\varphi_0=0$ (equivalently $h(1)=0$) for the
graded family, where it was fatal because $f_a(1)=1$ *always* (108_17
Theorem 3.1: a quasi-character sends the identity to $1$).

113_01 confirmed the mechanism transfers verbatim to Schwartz $h$ — and
went further, proving (Theorem 4.1) that $h(1)=0$ is not merely what one
particular scheme needs, but what **every** scheme needs to agree.  That
is a stronger and more informative result than the risk as originally
posed, and it is why this phase's outcome is a genuine advance rather than
a rediscovery of 108_17.

**The decisive difference from phase 108.**  There, $h(1)=1$ was *forced*
— every element of the graded family is a quasi-character, and
$\chi(1)=1$ is not a choice.  Here, $h=f\star\widetilde g$ is built from
**two free functions**, and $h(1)=0$ is one **linear condition** on that
pair.  A forced nonzero value and a codimension-one constraint on an
infinite-dimensional space are different in kind: the first kills the
route outright (as it did in phase 108); the second narrows it.

## 2. Compatibility with $\xi$-divisibility — plausibility, precisely scoped

107_239 §4 (1): $h=f\star\widetilde g$, $\widehat h(w)=\widehat f(w)\cdot
\widehat{\widetilde g}(w)$.  The 110/111 route sets $\widehat f=\xi
\widehat g$ (so $f$ is determined by $g$) and, from 111_03 Proposition
1.2, requires $\widehat g(0)=\widehat g(1)=0$ for radical membership.  By
Mellin inversion, $h(1)=\frac1{2\pi i}\int\widehat h(w)\,dw$ along the
critical line, a specific linear functional $L(g):=h(1)$ of $g$ alone
(once $f$ is eliminated via $\widehat f=\xi\widehat g$).

> **The candid statement.**  Requiring $L(g)=0$ is a **third linear
> condition** on the space of admissible $g$, alongside $\widehat g(0)=0$
> and $\widehat g(1)=0$.  Three linear functionals on an
> infinite-dimensional space have a common nonzero kernel unless they are
> dependent in a way that forces a contradiction — and nothing found in
> this programme suggests such a dependency.  This is a **plausibility
> argument**, not a proof: it has not been checked computationally here,
> because doing so needs the exact convolution/$\widetilde{(\cdot)}$
> formula of 107_239 §4 in closed form on the $\xi$-divisible class, which
> is a genuine computation phase 113 did not carry out.

**What would close this properly.**  Compute $L(g)$ explicitly for the
one-parameter family of $\xi$-divisible candidates (e.g.\ Gaussian-type
$g$'s satisfying the two known linear conditions) and exhibit a member with
$L(g)=0$, or prove $L$ is a nonzero multiple of one of the two existing
conditions (which would make the three conditions dependent and change the
picture).  This is a bounded, well-posed computation — not a new
obstruction — and is the concrete next step if d1 is pursued further.

## 3. The one inherited gap: Assumption T

113_03 Definition 3.1 takes the archimedean contribution from 111_01's
Weil-formula right-hand side, under **Assumption T**: that this equals the
actual operator-trace limit for Schwartz data, not merely that the
Weil-formula expression built from it is finite.  111_01 flagged this as
open; 113 inherits it unchanged and does not discharge it.  This is the
single largest residual risk to $\mathfrak T$'s status as a genuine
operator-trace regularization, as opposed to a finite number that merely
has the right shape.

## 4. What this changes in the backward map

| item | before phase 113 | after phase 113 |
|---|---|---|
| d1 construction | gap named, not attempted | **closed on $\mathcal A$**, modulo Assumption T |
| identity-value condition | absent from the picture | **new**: $h(1)=0$, one linear condition on $(f,g)$ |
| compatibility with $\xi$-divisibility | 2 linear conditions, verified compatible | **3** linear conditions, compatibility plausible, not verified |

d1 moves from "alive, one named construction gap" to "alive, one named
computation (§2) and one inherited assumption (§3)."  Neither is a wall.
Neither is closed.  Both are precise and bounded, which is the actual
measure of progress here.

## 5. Scope

**Proved here.**  Nothing new; this note synthesizes 113_01–113_03 into a
verdict and states the two remaining gaps precisely.

**Read from source, not re-derived.**  113_01 Theorem 4.1; 113_02 Theorem
2.1; 113_03 Definition 4.1 and Theorem 4.2; 107_239 §4 (1)
($\widehat{f\star g}=\widehat f\cdot\widehat g$, quoted for §2's
functional $L$); 111_03 Propositions 1.1, 1.2 (the $\xi$-divisible probe
and its two existing linear conditions).

**Not established, and explicitly not claimed.**  That $L(g)=0$ is
achievable together with $\xi$-divisibility and the two existing
conditions (§2 — a plausibility argument, not a computation).  Assumption
T (§3, inherited from 111_01, not discharged).  That $\mathcal A$ is the
largest possible admissible class.  Anything about $\RH$.

`ROW_A_STATUS` unchanged.  Nothing here bears on $\RH$.

## 6. Verifier

`113_04_verdict.py` re-runs `113_01`, `113_02`, `113_03` as subprocesses and
confirms all three exit 0 with `VERDICT: ALL CHECKS PASS`; separately
checks the linear-independence plausibility argument of §2 on a concrete
finite-dimensional model (three generic linear functionals on $\mathbb
R^5$ have a nontrivial common kernel; three functionals constructed to be
dependent do not), illustrating — not proving — the structural point made
there.
