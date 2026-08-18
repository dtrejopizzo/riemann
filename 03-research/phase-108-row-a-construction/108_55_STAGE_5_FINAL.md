# 108.55 — Stage 5: final verdict

## 0. Result

**Stage 5 closes negatively.** Neither the naive comparison (108_50) nor the regularized
comparison (108_51–108_54) exhibits Stage 3's assembly $L_g(s)=c_g(s)\Phi(s)$ as an
intersection number $I_{\mathrm{partial}}$ in Stage 0's sense. The regularized route's own
three-condition test (108_51 §2) is now fully resolved:

| Condition | Verdict | Where |
|---|---|---|
| I (cutoff family exists) | **Holds** (proved, not just architectural) | 108_54 §1 |
| II (regularized pairing $\to c_g(s)\Phi(s)$) | **Fails** for the natural/naive renormalization of the toy model; genuinely open for the real, unread operator $T$ | 108_54 §2 |
| III (the radicals correspond) | **Fails** (proved, independent of I and II) | 108_53 |

Condition III's failure is sufficient by itself: the "Statement" of 108_51 §2 needs **all
three** conditions to hold for the regularized route to succeed, and III is now a proved
negative, resting only on the closed form for $\Phi$ (task-supplied, re-derived here) and on
facts about Stage 0's radical quoted directly from source. This is not a gap in the
programme's knowledge; it is a structural fact about two already-fully-specified objects.

## 1. What is now settled, end to end

**Naive route (108_50, unchanged, permanent).** No map of generators exists in either
direction: $f_s$ cannot be compactly supported (Theorem 1.2), and the reverse Mellin-zero-set
map does not land in the graded quotient's finite mass-zero generators (Theorem 2.2).

**Regularized route, Condition I (108_54 §1).** An explicit smooth compactly-supported family
$f_{s,T}(x)=x^{s-1}\chi(\log x/\log T)$ exists, has support in $[T^{-2},T^2]$ for every finite
$T$, and converges to $f_s$ exactly (not just approximately) on every compact subset of
$(0,\infty)$ once $T$ is large enough — a genuine, proved construction, under the one named
assumption that Stage 0's category is at least $C^\infty_c((0,\infty))$.

**Regularized route, Condition II (108_54 §2).** The flat-cutoff toy pairing diverges on a
mass-zero pair (108_51 Proposition 3.1, reconfirmed). Subtracting the divergent part
(minimal subtraction) drives the toy remainder to exactly $0$ for *every* mass-zero pair
tested — a constant, independent of $s$ — which cannot equal the non-constant, generically
nonzero $c_g(s)\Phi(s)$ (108_38 Theorems 3.1, 3.2) except at accidental coincidences.
Non-minimal counter-terms make the limit an arbitrary, unmotivated constant (Proposition 2.3).
So the toy model's version of Condition II **fails** under the only two schemes examined —
one because it's ambiguous, the other because it's wrong. Whether Stage 0's real, unread
operator $T$ carries a *different*, canonical regularization (as the genuine explicit-formula
literature does, via contour shifts rather than sharp truncation) that would make Condition II
hold anyway is **not decided here** — it is the one place in this closure where source access
Stage 0's own definitions would be needed and was deliberately withheld from this pass.

**Regularized route, Condition III (108_53, the decisive result).** Using the supplied closed
form $\Phi(s)=2\psi(1-s)-\tfrac12\psi(s/2)-\tfrac12\psi((1-s)/2)-\log(4\pi)$ (re-derived here
from 108_38 Lemma 2.1 plus standard digamma identities, not merely assumed), three independent,
proved facts show the two radicals cannot correspond under any map respecting the natural
$s$-indexing:

1. $\Phi$ is holomorphic — finite, not singular — at *every* zero of $\xi$ (Theorem 1.2 of
   108_53), because the individual poles of $-\zeta'/\zeta(s)$ and $-\zeta'/\zeta(1-s)$ at a
   zero of $\xi$ cancel exactly. $\operatorname{rad}\Lambda^0$'s generators (zeros of $\Phi$)
   are therefore chosen by an equation with **zero sensitivity** to the arithmetic data
   (zeros of $\xi$) that generates $\operatorname{rad}I_{\mathrm{partial}}$.
2. The mirror involution $s\mapsto1-s$ that structures $\operatorname{rad}
   I_{\mathrm{partial}}$'s off-line planes and its $\{0,1\}$ polar block holds for $\Phi$
   *only* at $s\in\tfrac12+\mathbb Z$ (Theorem 2.1, exact closed-form classification) — and
   $\Phi(\tfrac12)\ne0$, so it holds nowhere $\Phi$ actually vanishes. $\Phi$'s zero set is
   not mirror-symmetric.

   This is now airtight rather than merely observed at one point. 108_53 Theorem 6.1 proves
   $\Phi'(s)=-\psi_1(1-s)-\tfrac14\psi_1(\tfrac s2)-\tfrac14\psi_1(1-\tfrac s2)<0$ throughout
   $(0,1)$ — three manifestly negative terms, after collapsing the raw derivative with the
   once-differentiated duplication formula — so $\Phi$ is **strictly decreasing** on the
   strip and has **exactly one** zero there, simple, at
   $s^\ast=0.30169238816042209152\ldots$ Hence $\operatorname{rad}\Lambda^0$ restricted to
   the open strip is **one-dimensional**, spanned by $\delta_{s^\ast}$ alone. There is
   therefore no second zero anywhere in $(0,1)$ available to pair with $s^\ast$ under
   $s\mapsto1-s$: the mirror-pair generator shape that $\operatorname{rad}
   I_{\mathrm{partial}}$'s off-line planes require is not merely absent at $1-s^\ast$, it is
   **impossible**.
3. $\Phi$ has poles, not candid finite values, exactly at $s=0,1$ (Theorem 3.1), with simple
   poles of residue exactly $+1$ at **both** — the two points
   $\operatorname{rad}I_{\mathrm{partial}}$ treats as its nondegenerate, non-radical
   generators.

## 2. Why this is a complete closure, not an unresolved question

The task's own framework (108_51 §2, "Statement") makes Conditions I–III jointly necessary and
sufficient for the regularized route to exhibit $L_g=c_g\Phi$ as an intersection number. A
proof that any *one* of them fails — proved outright, not merely unestablished — closes the
route. Condition III's failure (§1 above, full proofs in 108_53) is exactly such a proof, and
it is logically independent of Conditions I and II: it compares two sets of $s$-values fixed by
already-established theorems (108_38 Theorem 3.3 for one side, the task-quoted Stage 0 radical
description for the other) and needs no further input from how the cutoff is built or whether
its pairing limit converges. So even setting aside Condition II's remaining uncertainty about
the real operator $T$, the regularized route is closed: **whatever $T$ turns out to be, the
target coordinates it would need to vanish at (zeros of $\xi$, and the points $0,1$) are not
where $\Phi$ vanishes, is singular, or is symmetric, respectively.**

This mirrors, and now supersedes, 108_50's already-proved naive-route impossibility: both
routes fail, for related but distinct reasons (108_50: the *objects* cannot be identified;
108_53: even after regularizing the objects, the *radicals* — the coarsest, most
structural invariant of each pairing — cannot be identified either).

## 3. Is there a residual open question?

One item is not settled: whether Stage 0's actual pairing operator $T$ (never read in this
pass, per the task's explicit scope restriction) supplies a canonical regularization making
Condition II hold for the *real* $I_{\mathrm{partial}}$, as opposed to the toy model of 108_54
§2. This is stated precisely so it could, in principle, be checked by a future pass with
access to 107_240's internal construction of $T$:

> **The one remaining question, precisely stated.** Does Stage 0's operator $T$, applied to
> the cutoff family $D_{f_{s,T}}$ of 108_54 Construction 1.1 paired against a corresponding
> $D_{g_T}$, converge as $T\to\infty$ (without any further, hand-added counter-term) to a
> finite limit, for every $s$ and every admissible $g$?

But — and this is the point of §2 — **resolving this question one way or the other no longer
closes Stage 5**, because Condition III is independently and permanently false. A "yes" answer
would only mean the *pairing values* converge; it would not repair the fact that the
*vanishing loci* of the two radicals are governed by structurally unrelated equations (Theorems
1.2, 2.1, 3.1 of 108_53). Consequently this residual question is flagged for completeness (it
is the one fact this note could not check, for want of source access) but is **not** what
Stage 5 is conditional on: Stage 5's verdict is unconditional, negative, and does not change
whichever way that question resolves.

## 4. Final verdict

> ### Stage 5 (final)
> Stage 3's assembly $L_g(s)=c_g(s)\Phi(s)$ is **not** an intersection number in Stage 0's
> sense, neither via the naive comparison (108_50, permanent) nor via the regularized
> comparison of 108_51–108_54: Condition III of the regularized route is **proved false**
> (108_53 Theorem 4), independently of Conditions I (proved true, 108_54 §1) and II (fails for
> the naive/toy renormalization, 108_54 §2, with one named, out-of-scope question remaining
> about the real operator $T$ that would not change this verdict either way, per §3 above).
> This is a complete, negative closure of Stage 5, not an open problem deferred to a later
> stage.

**What this does and does not say about the wider programme.** It does **not** say Stage 1–4's
individual results are wrong — 108_38's closed form for $\Phi$, its radical
(Theorem 3.3), and 108_38 Theorems 3.1/3.2 are all used here exactly as proved, and this note's
new results (108_53 Theorem 1.2 in particular) are additional, independently interesting facts
about $\Phi$ discovered in service of this comparison. It says specifically that the
*comparison* Stage 5 was asked to make — identifying the graded pairing's descent with Stage
0's corner intersection pairing — does not hold, by an explicit, named, structural obstruction:
$\Phi$'s zero set is generated by an elementary, prime-free combination of digamma functions
that is provably blind to the zeros of $\xi$, has the wrong symmetry, and is singular exactly
where Stage 0's radical needs it finite.

## 5. Nothing here bears on $\mathrm{RH}$

Every theorem in 108_53/108_54 either (a) is an algebraic identity in $\Phi$ and its closed
form, (b) uses only the unconditional zero-free strip $0<\operatorname{Re}(\rho)<1$ for zeros
of $\xi$ (Hadamard–de la Vallée Poussin, far short of $\mathrm{RH}$), or (c) is an elementary
calculus statement about the toy integral $P(T;a)$. No statement about the location of zeros
of $\xi$ *within* the critical strip is made or needed anywhere in this closure.
`ROW_A_STATUS` is not promoted by this note.

## 6. Scope

**Proved here (synthesis of 108_53, 108_54).** The table in §0; the independence argument of
§2; the precise statement of the one residual, non-blocking question in §3; the final verdict
of §4.

**Read from source, not re-derived.** All of 108_38, 108_50, 108_51's already-established
results, used as cited throughout; the task-supplied Stage 0 pairing formula, radical
description, and quotient/signature decomposition (attributed to 107_240, 107_241).

**Verified numerically.** Nothing new beyond what 108_53's and 108_54's own verifiers already
check; this note's verifier (§7) re-runs the two headline claims from each as an integration
check, not a new independent computation.

**Not established, and explicitly not claimed.** The precise behavior of Stage 0's real
operator $T$ under the cutoff of 108_54 (named as the one open, non-blocking question in §3);
that $\Phi$ has only real zeros (108_53 §6: numerical search only); any statement bearing on
$\mathrm{RH}$ (none made, per §5).

## 7. Verifier

`108_55_stage_5_final.py` does not introduce new mathematics; it is an integration check that
(1) re-imports and re-derives the two headline numerical facts of 108_53 (finiteness of $\Phi$
at a nontrivial zeta zero vs. blow-up of $\zeta'/\zeta$ there; exact locus of mirror symmetry)
and of 108_54 (existence of the minimal-subtraction ambiguity; disagreement of the toy
remainder with the $\Phi$-based target) independently in a single self-contained script, so
that this closing note's verdict table is checked against fresh computation rather than merely
asserted; (2) confirms the logical independence claim of §2 is at least *not contradicted*
numerically, by checking that Condition III's failure (mismatch at a zero of $\xi$, asymmetry
at $s^\ast$, pole at $s=0,1$) holds using none of the toy-model machinery of 108_54 (a separate
code path, to guard against the two files' checks silently depending on each other).
