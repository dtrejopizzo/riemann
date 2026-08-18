# 111.03 — Verdict on requirement d1

## 0. Verdict

> **d1 is alive.**  Every piece of the corner pairing converges on
> Schwartz-class data.  What phase 110 closed was the *compactly supported*
> route, and its obstruction lives in a direction orthogonal to every
> convergence question raised here.
>
> One item is **not** closed, and it is a construction task rather than a
> convergence obstacle: the renormalized corner trace is currently built on a
> mechanism that is unavailable for Schwartz data.  §3 names it exactly.

| piece | on Schwartz data | where |
|---|---|---|
| polar terms $\widehat f(0),\widehat f(1)$ | **exist**, under explicit decay conditions | 111_01 §1 |
| zero sum $\sum_\rho\widehat f(\rho)\overline{\widehat g(\rho)}$ | **converges absolutely**, by an enormous margin | 111_01 §2, 111_02 §3 |
| prime sum $\sum_n\Lambda(n)h(n)/\sqrt n$ | **converges** | §2 below |
| the trace $\mathfrak T$ as *currently constructed* | **construction unavailable** — see §3 | §3 |
| $\xi$-divisible class $\cap$ convergent class | **nonempty**, modulo two linear conditions | §1 |

## 1. Compatibility (Task 3)

The question that would have made everything vacuous: does the class where
the pairing converges actually **contain** nonzero $\xi$-divisible elements?

> ### Proposition 1.1
> It does.  With $g(r)=e^{-(\log r)^2}$, $\widehat g(w)=\sqrt\pi e^{w^2/4}$,
> and $\widehat f=\xi\widehat g$, the transform $\widehat f$ decays on the
> critical line faster than $e^{-t^2/4}$, so every convergence requirement of
> 111_01 §§1–2 is met with room to spare.

Verified: $|\widehat f(\tfrac12+it)|=7.1\times10^{-1},\ 9.9\times10^{-13},\
2.2\times10^{-286},\ 8.6\times10^{-4407}$ at $t=1,10,50,200$.

> ### Proposition 1.2 (the extra conditions, and they are harmless)
> $\xi(0)=\xi(1)=\tfrac12\ne0$, so $\xi$-divisibility gives
> $\widehat f(\rho)=0$ at every zero but **not** $\widehat f(0)=
> \widehat f(1)=0$.  Membership in $\operatorname{rad}I_\partial$ needs the
> additional $\widehat g(0)=\widehat g(1)=0$: two linear conditions, cutting
> a codimension-2 subspace of an infinite-dimensional space.

This was worth checking rather than assuming — a convergence class disjoint
from the $\xi$-divisible one would have settled nothing.  It is not disjoint.

## 2. The prime sum converges

For compactly supported $h$ only finitely many prime powers lie in the
support, so the prime side of the explicit formula is a finite sum.  For
Schwartz $h$ **every** prime power contributes.  The sum nonetheless
converges.

> ### Proposition 2.1
> For $h$ Schwartz on $(0,\infty)$ — in particular decaying faster than any
> power at $\infty$ — $\sum_{n\ge2}\Lambda(n)h(n)n^{-1/2}$ converges
> absolutely.

**Proof.**  $\Lambda(n)\le\log n$, and $h(n)=O(n^{-3})$ by rapid decay, so
the terms are $O(n^{-3}\log n\cdot n^{-1/2})$, summable. $\square$

Verified with $h(r)=e^{-(\log r)^2}$: the partial sums are
$0.62419273130875$ at $N=10^2$ and $0.62419273227271$ from $N=10^3$ through
$N=2\times10^5$, the increments collapsing to exactly $0$ in working
precision.  Control: with the non-Schwartz $h\equiv1$ the same sum diverges
($16.9,\ 60.5,\ 197.5,\ 891.8$), so the test discriminates.

## 3. The one thing that is not closed

107_239 §3 defines the renormalized corner trace as $\mathfrak T(h):=
\mathfrak T_{S(h)}(h)$, where $S(h)$ is a **finite** set of places
determined by $h$'s support, and states that enlarging $S$ adds zero local
terms — "the same finite-place support mechanism that makes the prime sum in
the explicit formula finite for compact support."

> ### The gap, stated exactly
> That mechanism is **unavailable** for Schwartz data: $h(p^k)\ne0$ for every
> prime power, so no finite $S(h)$ exists and $\mathfrak T_{S(h)}$ is not
> defined.  By §2 the relevant sums converge, so this is a **construction**
> task — replace the finite-place stabilization by a convergence argument —
> and **not** a divergence obstruction.

This is the candid boundary of phase 111.  We have not built that
construction, and we do not claim it is routine; we claim only that the
obstacle is not convergence, since §2 settles convergence directly.

## 4. What this means for the programme

Phase 110 proved $\xi$-divisibility impossible on compactly supported data,
by a growth argument on the **real axis**.  111_02 Corollary 2.3 shows that
argument is silent about the **critical line**, where $\xi$ decays at rate
$-\pi/4$; and every convergence question in the pairing is a critical-line
question.  So the two results do not conflict, and d1 was never closed by
phase 110 — only its compactly supported route was.

Note also that 107_239's own "Still open" list names, in its own words,
exactly the requirements the programme's backward map labels d1, d3, d4 and
d5: proving $I_\partial$ is the intersection product entering a
Riemann–Roch theorem; constructing the class whose local equations are the
DC potentials and proving principal invariance; constructing $H^1$ or an
existence theorem for positive self-intersection; and proving a
Hodge-index/effectivity statement.  That is independent confirmation that
the map's edge list is the right one.

## 5. Scope

**Proved here.** Proposition 1.1 (via 111_02 §3), Proposition 1.2,
Proposition 2.1.

**Read from source, not re-derived.** 107_239 §3 (the definition of
$\mathfrak T$ and its finite-place mechanism) and its "Still open" list;
107_240 Theorem D; 110_02's growth theorem and its example; 111_01's
convergence results for the polar terms and the zero sum; 111_02's two rate
theorems.

**Verified numerically.** The probe's decay at four heights; the prime sum's
convergence with a control that diverges; $\xi(0)=\xi(1)=\tfrac12$.

**Not established, and explicitly not claimed.**  That $\mathfrak T$ can be
constructed on Schwartz data (§3) — only that convergence is not what stands
in the way.  That a $g$ meeting $\widehat g(0)=\widehat g(1)=0$ *and* every
other admissibility requirement simultaneously exists.  Anything about
$\RH$: no zero of $\xi$ enters any definition here.

`ROW_A_STATUS` unchanged.  Nothing here bears on $\RH$.

## 6. Verifier

`111_03_verdict.py` checks Proposition 2.1's convergence by refinement
against a control that must diverge; the probe's decay; and
$\xi(0)=\xi(1)=\tfrac12$ with a clause rejecting the plausible wrong value
$0$.
