# 109.99 — Phase 109 summary: the one-sided pairing exists, and its radical
# refutes the hypothesis

## 0. The hypothesis, restated

Phase 108 showed the two-sided Tate pairing is unconditionally wrecked by
the identity shell ($k=0$): 108_17 Theorem 2.2/3.1 prove the finiteness
criterion $\varphi_0=0$ is violated by every member of the graded family,
always. The one object that survived cleanly was the one-sided sum
(108_36), built from shells $k\ge1$ only, equal to $-\zeta'/\zeta(s)$.
Phase 109 asked: if that one-sided sum is bilinearized, does the identity-
shell obstruction simply not arise, and does the resulting pairing's
radical come out **zero-determined** (Stage-0 shape, 107_240 Theorem D),
opening a route toward unifying rows (a)–(d)?

## 1. Verdict table

| Step | Question | Outcome | File |
|---|---|---|---|
| 1 | Does a genuine bilinear one-sided pairing exist? | **Yes.** $B(f,g)=\sum_n\Lambda(n)f(n)g(n)$, absolutely convergent on $\mathcal G_B$, bilinear, symmetric, not Hermitian, recovers 108_36 exactly at $B(f_s,f_0)$. | `109_01_THE_ONE_SIDED_PAIRING.md` |
| 2 | Is $\mathrm{rad}\,B$ zero-determined or $\Gamma$-determined? | **Neither.** $\mathrm{rad}\,B=\{f:f(p^k)=0\ \forall p,k\ge1\}$ — prime-power-determined. Explicit witness $F=\sin(\pi x)$: in the radical, transform zero-free on **all** of $\xi$'s zero set. **Hypothesis refuted.** | `109_02_THE_RADICAL.md` |
| 3 | Signature | **Skipped** (Step 2 not zero-determined, per the mission's own gate); the only computable inertia ($n_+=\infty,n_-=0$, from $\Lambda(n)>0$) is unconditionally true and carries no information about zeros of $\xi$. | `109_03_THE_SIGNATURE.md` |

## 2. What actually happened, in one paragraph

Excluding the identity shell does exactly what 108_17 said it would for the
finiteness question: the resulting one-sided sum has no leftover constant,
and it does support a genuine, non-circular bilinear structure — the
"canonical bilinear square" of the shell point-evaluation functional
$\Gamma_{p,k}$, forced (not chosen) by $\Gamma_{p,k}$ already being a point
evaluation. But the reason the two-sided construction was zero-blind
(108_91's $\Phi$) and the reason *this* one-sided pairing is *also*
zero-blind are different mechanisms, and it matters that they are: $\Phi$
came from a designed symmetrization that cancels every pole at a zero of
$\xi$; here, no such cancellation happens — $-\zeta'/\zeta$ genuinely has
poles at every zero of $\xi$ (108_36 Proposition 2.1, unchanged). What is
zero-blind instead is the *pairing's degeneracy structure*: $B$ is diagonal
in the basis of point evaluations at prime powers, a discrete arithmetic set
with no established relation to $\xi$'s zero set, so its radical is
governed by that discrete set, not by $\xi$. The zeros of $\xi$ show up only
as poles of the meromorphically continued *number* $B(f_s,f_t)=
-\zeta'/\zeta(s+t)$ along the lines $s+t=\rho$ in the $(s,t)$-plane — a
different phenomenon from the radical, as 109_01 Remark 4.1 makes explicit.
The explicit witness $F(x)=\sin(\pi x)$ (109_02 Theorem 3.3) turns this from
a plausibility argument into a proof: it is a genuine radical element whose
transform, in closed form $\pi^{-s}\Gamma(s)\sin(\pi s/2)$, is zero-free at
every single zero of $\xi$, trivial or nontrivial. That is a complete,
non-numerical refutation (the numerics in the verifier check the standard
Mellin-pair formula and $\Gamma$'s zero-freeness, not the logic).

## 3. Anti-circularity audit

* The bilinearization $B(f,g)=\Gamma_{p,k}(f)\Gamma_{p,k}(g)$ summed was
  argued to be *forced* (109_01 Definition 1.1: the unique rank-one
  symmetric bilinear square of an already-existing linear functional, and
  point evaluation is multiplicative so this coincides with the equally
  natural $\Gamma_{p,k}(fg)$) — not chosen after the fact to make an
  identity come out. It was checked against 108_36's number as a
  consequence (Corollary 3.2), not built to match it.
* The pre-registration (109_00 §3, restated at the top of 109_02) fixed,
  before any computation, what would count as confirmation and what would
  count as refutation of the zero-determined hypothesis, including the
  specific bar that the confirmation must not smuggle in the un-built
  Stage-4 archimedean term (109_02 Remark 3.2).
* The witness $F=\sin(\pi x)$ was not reverse-engineered from the target
  conclusion in the circular sense the mission warns about: it is the
  simplest possible function vanishing at all integers, chosen because its
  Mellin transform happens to have an elementary, textbook closed form —
  the *fact* that this transform is zero-free on $\xi$'s zero set is a
  consequence of $\Gamma$ having no zeros and $\sin(\pi s/2)$ vanishing only
  at even integers, both independent, checkable, standard facts, not
  something imposed on the construction.
* Step 3 was not attempted merely to have something to report; 109_03
  explains explicitly why the one number that *is* computable there
  ($n_+=\infty,n_-=0$) is content-free, rather than silently omitting the
  step or dressing up a vacuous computation as a result.

## 4. Scope (programme-wide)

**Proved in this phase:** 109_01 Theorems 2.1, 2.2, 3.1 and Corollary 3.2;
109_02 Theorems 2.1, 3.3 and Corollary 4.1; 109_03's one-line positive-
definiteness remark.

**Read from source, not re-derived:** 108_34 (shell functionals,
$k\ge1$ branch = point evaluation); 108_36 Theorem 1.1 (the one-sided
assembly equals $-\zeta'/\zeta$, its convergence domain and poles); 108_17
(quoted only for context/motivation in 109_00, not used in any proof here).

**Verified numerically:** all claims in 109_01 and 109_02 with shrinking-
error / exact-finite-sum / control-clause checks, per file; see §5.

**Not established, and explicitly not claimed:** that no bilinearization of
the one-sided shells has a zero-determined radical (only the canonical,
forced one was tested); any intersection-theoretic reading; anything about
RH. Nothing in this phase bears on RH, and no status is promoted.

## 5. Verifier results (this run)

* `109_01_the_one_sided_pairing.py` — 9/9 checks, exit 0.
* `109_02_the_radical.py` — 8/8 checks, exit 0.
* `109_03` — no verifier attached; see 109_03 §1–2 for why one would be
  content-free.
* `109_99_phase_109_summary_verifier.py` (below) — re-runs the load-bearing
  claims standalone: the closed-form/pairing identity, the radical
  membership + non-membership control, and the refutation witness's
  zero-freeness at a zero of $\xi$, contrasted with its exact vanishing at
  $s=2$.

## Supervisor addendum (109_04)

Two corrections were made to this phase on review.

**1. "Forced" was overstated.** 109_01 Definition 1.1 describes its pairing as
"canonical … literally forced … no free parameter is chosen here." What is
forced is only that a *single* linear functional has one rank-one square. The
actual choice is to assemble the squares **diagonally**, i.e. $K(n,m)=
\Lambda(n)\delta_{nm}$; a general kernel $K(n,m)$ on the same functionals is
equally admissible. 109_02's verdict is therefore, as written, a fact about
one kernel.

**2. The result is stronger than reported, and does not need "forced".**
109_04 Theorem 1.1 proves the conclusion for **every** kernel supported on
the prime powers: $Z:=\{f:f(p^k)=0\ \forall p,k\}\subseteq
\mathrm{rad}\,B_K$, by a one-line argument using nothing about $K$. With
the witness $F(x)=\sin(\pi x)$ — which lies in $Z$ and whose Mellin transform
has **constant** modulus $1/\sqrt2$ on the critical line (109_04 Lemma 1.2$'$,
exact, not asymptotic) — no such pairing has a zero-determined radical.

**What this makes of the phase.** The hypothesis had two halves. The first
held: a genuine bilinear one-sided pairing exists and the identity-shell
obstruction of 108_17 does not arise. The second could not have held: the
hypothesis conflated "the assembled Dirichlet series has poles at the zeros"
with "the pairing detects the zeros", and those are statements about opposite
sides of the Mellin transform. The zeros are not in the coefficients
$\Lambda(n)$; they are in the continuation.

**Corrected target for row (a)** (109_04 §3): a pairing that is
*continuation-side* (reading $\widehat f$ at points, not $f$ at prime powers)
**and** *non-symmetrized* (pairing across the mirror, not summing over it)
**and** zero-free in its definition. One-sidedness was not the operative
variable.
