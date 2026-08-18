# 108.16 — Stage 1 closure: the constant term resists all three proposed
# routes, and why

## 0. Final status

\[
 \boxed{\text{Stage 1 does not close. The }a\text{-dependent part is closed
 (108_06, 108_07, 108_11); }\sum_pC_p\text{ remains genuinely open.}}
\]

Three concrete routes were tested to resolve 108_12's remaining obstacle,
$\sum_pC_p$. **All three fail**, each by a proof, not by exhaustion of
patience:

| route | verdict | file |
|---|---|---|
| A — 107_239's phase-space counterterm | **fails**: growth rates incommensurate (linear in $T$ vs. $\ge\Theta(e^T/T)$) | 108_13 |
| B — zeta regularization via $-\zeta'/\zeta(0)$ | **fails as an identification**: the classical constant $-\log(2\pi)$ is real and verified, but the natural regulator applied to $\sum_pC_p$ lands on an object with an accumulation of poles at the evaluation point, plus an independent elementary divergence | 108_14 |
| C — restriction to the primitive/degree-zero subspace | **fails except vacuously**: only $g\equiv0$ annihilates the constant for every test function | 108_15 |

No fourth route is introduced. §5 explains why: the three failures are not
independent accidents — they trace to one underlying fact, which is proved
(not merely observed) in §5, and which sharpens rather than merely repeats
108_12's original finding. `ROW_A_STATUS` remains `partial`. No zero of
$\xi$ is used anywhere in this note or in 108_13–108_15. Nothing here, or
anywhere in Phase 108, bears on RH.

## 1. What was already settled (108_06, 108_07, 108_11, 108_12)

* Every single-place local term, finite and archimedean, converges exactly
  on $0<\Re a<1$, in closed form (108_06, 108_07).
* The $a$-dependent part of the global sum, $A(a)+B(a)$, is
  $L^1_{\mathrm{loc}}((0,1))$, hence defines a Radon measure — the
  distributional target Stage 1 asks for (108_11 Theorem 3.1). This part
  **is** closed and is not reopened by anything below.
* The remaining piece, $\sum_pC_p$, diverges as a naive sum (108_12
  Theorem 2.1: $C_p=+\infty$ for every $p$) and its natural
  local-regularized scale is $\propto\log p$, so the sum over $p$ diverges
  by Chebyshev even after that regularization (108_12 Theorem 3.1).

108_12 identified one candidate repair — 107_239's counterterm — as a
"shape match, not a computation," and flagged it as likely incommensurate.
This note and its companions turn that flag into a proof, and test two
further candidates.

## 2. Route A — the counterterm (108_13)

107_239 (1.4)'s counterterm $-2h(1)\log\Lambda$ is $a$-independent and
proportional to a value at $1$, structurally matching $\sum_pC_p$'s shape.
Using 107_239 §3's *own* correspondence between the cutoff $T=\log\Lambda$
and the stabilizing prime set $S(h)=\{p\le e^T\}$, 108_13 proves:

* the counterterm is **exactly linear** in $T$;
* the natural partial sums of $\sum_pC_p$ over the same set, under *any*
  regularization of the individual $C_p$ consistent with 108_12's own
  findings, grow **at least like $\pi(e^T)=\Theta(e^T/T)$** — Chebyshev's
  theorem, cited and independently re-verified;
* hence their ratio diverges (108_13 Theorem 3.1): no fixed constant makes
  one absorb the other.

This is proved, not merely illustrated: the argument only needs a lower
bound on $C_p^{\mathrm{reg}}$ that both readings of 108_12 already supply.
**Route A is discarded.**

## 3. Route B — zeta regularization (108_14)

108_14 verifies, from a self-implemented Euler–Maclaurin continuation of
$\zeta$ (no scipy, no mpmath), that $\zeta(0)=-\tfrac12$,
$\zeta'(0)=-\tfrac12\log(2\pi)$, hence $-\zeta'/\zeta(0)=-\log(2\pi)$ —
matching the classical constant that appears in the explicit formula's
archimedean term. This part is real and now independently checked in this
program, not merely asserted.

It then tests the precise claim — that the zeta-regularized value of
$\sum_pC_p$ equals a multiple of this constant — and proves it does not
hold as stated:

* applying the *same* regulator $\zeta(s)=\sum_nn^{-s}$ itself uses (weight
  the $k$-th $p$-adic shell of $C_p$ by $p^{-ks}$) gives an exact identity
  $\sum_pC_p(s)=B_0+A(s)$, with $A(s)$ literally 108_06/108_11's own
  object and $B_0:=\sum_p\frac{p-2}{p-1}$;
* $B_0=+\infty$ by a one-line comparison test (no $\log p$, no Chebyshev
  needed) — a strictly more elementary obstruction than 108_12's own,
  untouched by any scale-type regulator, since the bulk shell has $p$-adic
  exponent $0$;
* even granting $B_0$ away, $A(s)$ has $s=0$ as an **accumulation point of
  poles** (108_11 Lemma 2.1, cited and numerically illustrated afresh in
  108_14 by direct evaluation of $\zeta$ near its pole along $s=1/N\to0$) —
  a natural-boundary phenomenon, not the isolated regular point $\zeta$
  itself has at $s=0$.

**The classical constant is confirmed; the identification with
$\sum_pC_p$ is refuted**, with the refutation itself built on already-proved
facts (108_11 Lemma 2.1, 108_12 Theorem 2.1) rather than a new conjecture.
The resemblance to $\log(2\pi)$ remains, candidly, an observation about a
constant that recurs elsewhere in the classical theory — not a proof about
this object.

## 4. Route C — the primitive restriction (108_15)

The constant multiplies the smooth, entire coefficient $c_g(a)$
(108_06 Proposition 2.1) in the assembly, integrated in bulk over the whole
open strip. 107_241 Corollary 3.4's primitive condition
$\hat f(0)=\hat f(1)=0$ transports to $\hat g(0)=\hat g(1)=0$ (§2 of
108_15, with the asymmetry from 108_06's own unshifted involution made
explicit). 108_15 proves:

* $c_g$ is entire; any nonzero $g$ gives a $c_g$ that is not identically
  zero **on all of $\mathbb C$** (Mellin/Fourier injectivity, proved from
  scratch in 108_15 Theorem 3.1 Step 1–2);
* an entire function that is not identically $0$ cannot vanish on an open
  real interval either (identity theorem) — so $c_g\not\equiv0$ on
  $(0,1)$ for every nonzero $g$, primitive or not;
* consequently a test function $\varphi$ detecting a nonzero pairing
  always exists (108_15 Theorem 3.1 Step 3–4);
* an explicit nonzero $g$ satisfying the exact primitive condition is
  constructed and verified numerically in 108_15 §6, with $c_g$ confirmed
  nonzero throughout $(0,1)$ and pairing nontrivially against an interior
  bump.

**The only restriction of $g$ that kills the constant for every test
function is $g\equiv0$** — vacuous, not a meaningful closure. Route C is
discarded, and the reason is structural: a two-point boundary condition
cannot control a density that lives in the bulk.

## 5. Why all three fail: one underlying obstruction, proved

The three routes attack the divergence with three different tools —
a phase-space cutoff (single global scale), a Dirichlet-series evaluation
(single regularized value at an isolated point), and a finite-codimension
restriction (control at finitely many points). Each tool is *designed* for
a divergence that is, respectively: linearly-cutoff-commensurate, isolated
in the regulator variable, or concentrated at finitely many points.

> ### Theorem 5.1 (the obstruction is genuine)
> $\sum_pC_p$'s divergence is neither: (i) commensurate with any single
> linear-in-log-cutoff scale (108_13); (ii) isolated at a regular point of
> a Dirichlet-series continuation (108_14, via the proved accumulation of
> poles of $A(s)$ at $s=0$, 108_11 Lemma 2.1); nor (iii) concentrated at
> finitely many points of the coefficient $c_g(a)$ that it multiplies
> (108_15, via entire-function rigidity). It is a *bulk*, *boundary-
> accumulating* divergence, present at every interior point $a\in(0,1)$
> with a singular structure that only resolves at the endpoints
> $a=0,1$ — exactly where 108_11 Lemma 2.1 already showed $A(a)+B(a)$'s own
> singular set accumulates.

**Proof.** Each clause is exactly the corresponding theorem cited: 108_13
Theorem 3.1 for (i); 108_14 Theorem 2.4 (and 108_11 Lemma 2.1, which it
restates in the variable $s=a$) for (ii); 108_15 Theorem 3.1 for (iii).
$\square$

This does not prove that *no* repair of any kind exists — see §6 — but it
proves that the three repairs suggested by the program's own existing
machinery (107_239's counterterm, zeta regularization, primitivity) are not
merely unproven; they are each disprovable by an elementary, checkable
mechanism, and the three mechanisms are the same phenomenon viewed three
ways: accumulation at the strip's boundary, not an isolated singularity.

## 6. Scope — what is proved, what is not, what remains open

**Proved in 108_13–108_16 (new in this note and its companions):**

* Route A's growth-rate incommensurability (108_13 Theorem 3.1).
* The classical constant $-\zeta'/\zeta(0)=-\log(2\pi)$, independently
  verified from a from-scratch continuation (108_14 §1).
* The exact decomposition $\sum_pC_p(s)=B_0+A(s)$ and the elementary
  divergence of $B_0$ (108_14 Theorem 2.2, 2.3).
* $A(s)$'s accumulation of poles at $s=0$, restated in this variable from
  108_11 Lemma 2.1 (108_14 Theorem 2.4).
* Route C's rigidity theorem: no nontrivial finite-codimension restriction
  of $g$ annihilates the constant for every test function (108_15 Theorem
  3.1, Corollary 3.2), with an explicit numerical witness.

**Verified numerically only (clearly labeled as such in each file):** the
Euler–Maclaurin continuation's agreement with closed-form $\zeta$ values and
the von Mangoldt identity (108_14 §1); the growth-rate comparisons of
108_13; the explicit counterexample construction of 108_15 §6.

**Read from source / classical, not proved here:** the Euler–Maclaurin
summation formula itself; Chebyshev's theorem; the classical fact that
$\log(2\pi)$ appears in the archimedean term of the explicit formula for
$\psi(x)$; the semilocal trace theorem and its counterterm (107_239 §2).

**Not established, and explicitly still open:**

1. **The value, or even the well-posedness, of $\sum_pC_p$ under any
   regularization.** All three natural candidates fail; no exhaustive
   classification of regularizations is attempted, so a route not yet
   imagined is not ruled out in general — only the three tested here.
2. **A fourth route was not constructed.** Given Theorem 5.1's proof that
   the obstruction is a genuine accumulation-at-the-boundary phenomenon
   (the same one already responsible for 108_08's pointwise failure at
   $a=\tfrac12$ and for 108_11 Lemma 2.1's singular-set accumulation), and
   given that the task explicitly allows "prove the obstacle is genuine" as
   the alternative to inventing a new route, that is the outcome recorded
   here rather than a speculative fourth mechanism.
3. Complex $a$, throughout Phase 108 (108_06 §1, 108_08 §9.3, 108_11 §4)
   remains untouched.
4. The comparison with the zero side of the explicit formula remains
   untouched, and is forbidden as a *definition* by 108_00 §2 in any case.
5. Whether the distributional object 108_11 Theorem 3.1 constructs (the
   $a$-dependent part alone, *without* the constant) is "the right one" for
   the rest of the program (107_239–107_241) is not established anywhere in
   Phase 108.

## 7. Updated status table

| component | status |
|---|---|
| finite local terms | closed (108_06) |
| archimedean local term | closed, $\pi\cot(\pi a/2)$ (108_07) |
| global, $a$-dependent part, distributional | **closed** (108_11) |
| global, the constant $\sum_pC_p$ | **open** — three specific repairs now disproved (108_13–108_15), and the obstruction shown to be structural (108_16 Theorem 5.1) |
| Stage 1 overall | **not closed** |

`ROW_A_STATUS` remains `partial`. This note promotes no status, resolves no
row, and bears on RH nowhere.

## 8. Verifier

`108_16_stage_1_closure.py` re-runs the verifiers of 108_11, 108_12,
108_13, 108_14, 108_15 as subprocesses and confirms each exits $0$,
printing a consolidated pass/fail table; it also re-checks, standalone, the
three headline numeric facts this closure note leans on most directly
(Chebyshev's $\theta(x)=\Theta(x)$, the classical constant
$-\zeta'/\zeta(0)=-\log(2\pi)$, and non-degeneracy of the explicit 108_15
counterexample) as an independent final consistency pass.
