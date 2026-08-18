# 108.25 — Stage 1 reformulated: what extends, what does not, and the
# criterion delivered to Stage 2

## 0. Purpose

108_21 closed Stage 1 as originally posed (substitution of $f_a$ into
107_239 (2.1)) as terminal: outcome (ii), the constant $\sum_pC_p$ is a
genuine, unrepairable obstruction. 108_05 diagnosed *why* the original move
was suspect — a category error, pairing a non-member of the test class — and
proposed extension by continuity/density as the alternative not yet tried.
108_22–108_24 carried that alternative out completely: to a clean negative
result on the object it was hoped would rescue Stage 1 (108_22, 108_23), and
to a positive, restricted, usable deliverable for Stage 2 (108_24). This
note is the synthesis the mission's closing instruction asks for. It
resolves no open item beyond what 108_22–108_24 already proved; it only
assembles the picture.

`ROW_A_STATUS` remains `partial`. No zero of $\xi$ enters any definition in
108_22–108_24 or here. Nothing here bears on RH.

## 1. What extends

* **The mean-zero smeared pairing $\Lambda_g^0$** (108_24 Theorem 2.1): a
  genuine, forced, zero-free-defined, finite pairing exists on **balanced**
  smearing profiles $\varphi$ (those with $\int_0^1\varphi\,da=0$) — a
  restriction of the graded family's "test directions," not of $\mathcal G$
  itself. It is forced by an *exact* algebraic cancellation of 108_21's
  $a$-independent divergent constant, holding at every finite regularization
  depth, not merely asymptotically — so it needs no knowledge of, bound on,
  or regularization of $\sum_pC_p$.
* **The convergence of the formal zero-sum expression** (108_23 Theorem
  2.1): $\sum_\rho\varphi(\mathrm{Re}\,\rho)\overline{\hat g(\rho')}$
  converges absolutely for bounded, compactly-supported $\varphi$ and
  Gaussian-or-faster decaying $\hat g$, unconditionally (classical
  $0<\mathrm{Re}\,\rho<1$ and $N(T)=O(T\log T)$ only — no zero location, no
  RH-adjacent input).
* **108_11's closed $a$-dependent object and 108_19's nonvanishing witness**
  survive unchanged and are exactly what 108_24's criterion is built from;
  their status is not altered by this note.

## 2. What does not extend

* **No pointwise pairing on individual $f_a$** (108_22 Theorem 3.1): for
  every topology in which convergence to $f_a$ recovers its actual value
  $f_a(1)=1$ — the minimum required for "$f_a\in E$" to mean what it says,
  shown to hold automatically for $A_\delta$, its natural enlargements, and
  nuclear/Schwartz-type spaces (108_22 Lemma 2.3) — $\Lambda_g$ is not
  continuous at $f_a$ along the one net (Burnol's cutoff, 108_05 Thm 3.1)
  this program has ever used to give $f_a$ operative meaning. This is not a
  new obstruction: it is 108_21 Theorem 1.1 itself, viewed as a statement
  about extension rather than substitution, and it defeats extension for the
  identical reason.
* **The general-$\varphi$ smeared object of the mission's task (2)** is
  **not** the forced continuous extension of $\Lambda_g$ (108_23 Corollary
  4.1): no such extension exists to compare it to, so writing it down by
  substituting the formal delta-reading of $\hat f_a$ into the zero-sum term
  of the explicit formula is a *definition* that routes through the zero
  side — inadmissible under 108_00 §2 — not a theorem. On the arithmetic
  side, the candid smeared quantity diverges for any $\varphi$ with
  $\int\varphi\,da\ne0$, for the same $a$-independent-constant reason as the
  pointwise case.
* **The value, finiteness, or vanishing of $\sum_pC_p$** remains completely
  open. 108_24's construction cancels its contribution exactly on balanced
  profiles; it never determines what that contribution *is*. 108_21's
  terminal verdict on the unsmeared, non-balanced problem is untouched.

## 3. The dichotomy of task (2), stated once, plainly

General $\varphi$: **case (ii)** — a zero-sourced definition, not forced,
not admissible as a definition (108_23 §4). Balanced $\varphi$: a genuine
**case (i)** — a forced, zero-free, density-and-continuity consequence of
$\Lambda_g$ (108_24 Theorem 2.1) — but only on that restricted subspace, and
whether it agrees with the (also convergent, 108_23 Theorem 2.1) formal
zero-sum restricted to balanced $\varphi$ is an explicitly open question
(108_23 Remark 4.2), not needed for, and not claimed by, 108_24's
self-contained arithmetic-side construction.

## 4. The criterion delivered to Stage 2, restated once more without hedges
   removed

Criterion 3.1 of 108_24: represent a candidate principal element $\pi$ of
108_03/108_04's graded divisor group by a balanced profile $\varphi_\pi$
(Remark 1.2 there, an explicitly flagged, unverified structural reading —
degree-zero divisors are principal candidates by classical analogy, not by
anything checked against 108_03/108_04's literal definitions in this Phase).
Compute $\Lambda_g^0(\varphi_\pi)$ (108_24 Theorem 2.1) for admissible $g$.
Zero: not detected non-invariant. Nonzero for some $g$: certified
non-invariant, by an explicit, finite, zero-free-computed number.

**What it certifies:** a working, non-vacuous (§4 of 108_24, via likely —
not proved — identification with 108_19's nonvanishing witness), computable
test, entirely avoiding $\sum_pC_p$.

**What it does not certify:** anything pointwise in $a$; anything about
profiles or divisor-group elements outside the balanced subspace; anything
about $\sum_pC_p$ itself; sufficiency (only a necessary-looking consistency
check) for whatever precise notion of invariance 107_240/108_03/108_04
intend; any relation to 107_240 §5's numerical quotient, an alternative
route the mission also named and which this Phase does not connect to
$\Lambda_g^0$.

## 5. Candid accounting of what remains open

1. Remark 1.2's reading of "balanced profile = principal element" against
   108_03/108_04's actual definitions — the single largest gap between
   "a criterion exists" and "Stage 2 can use it as stated."
2. §4's identification of 108_11's $L_g$ with 108_06's $c_g$.
3. 108_23 Remark 4.2's open equality between the formal zero-sum restricted
   to balanced $\varphi$ and 108_24's arithmetic-side construction.
4. 108_22 §3.4's un-excluded case: a coherence-violating topology (§3.4
   there) is not ruled out, only set aside as not obviously still answering
   the question asked.
5. The relation, if any, between $\Lambda_g^0$ and 107_240 §5's numerical
   quotient pairing.
6. $\sum_pC_p$'s value, exactly as open as 108_21 left it.

None of these are minimized above; each is stated at the point in
108_22–108_24 where it arises, and repeated here so this synthesis is not
read as resolving more than it does.

## 6. Verifier

`108_25_stage_1_reformulation.py` re-runs, as subprocesses, the verifiers of
108_05, 108_21, 108_22, 108_23, and 108_24 (five scripts spanning the
diagnosis, the terminal Stage-1 verdict, and this note's three new results),
confirms each exits $0$, and prints a consolidated pass/fail table. It adds
one independent, standalone final check not internal to any single note:
that the exact-cancellation identity of 108_24 Theorem 2.1 holds for a
*third*, freshly chosen model pair $(D(T),L_g)$ not used in 108_23 or
108_24's own verifiers, as a last cross-check that the mechanism is not an
artifact of one specific numerical model.
