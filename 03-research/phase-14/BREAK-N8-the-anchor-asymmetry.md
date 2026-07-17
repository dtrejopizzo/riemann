# Breaking N8: absence WITHOUT square-root cancellation — the anchor asymmetry (N8 was a symptom)

**Author: David Alejandro Trejo Pizzo · 2026-06-04.**
The audit's sharpest objection: N8's claim *"the square-root cancellation barrier is RH-equivalent, hence there is
no more elementary ingredient behind it"* is the strongest step in the whole chain, and the one to attack. Not to
prove RH — **to break N8.** The precise binary question: *does there exist an exact mechanism that forces ABSENCE
of zeros WITHOUT passing through a square-root-type cancellation estimate?* This document answers it: **yes.** N8's
universal form is therefore **false**; N8 is a *symptom* of one family of routes, not the universal cause. The real
structure behind it is an **anchor asymmetry**, and it reframes the RH-directed question.

---

## 1. The counterexample (N8's universal form is false)

**Theorem (de la Vallée Poussin, 1896).** $\zeta(1+it)\ne0$ for all real $t\ne0$. *This is an exact ABSENCE result.*

**Its proof uses no cancellation estimate.** For $\sigma>1$, with $c_n=\Lambda(n)/\log n\ge0$,
$$
3\,\Re\log\zeta(\sigma)+4\,\Re\log\zeta(\sigma+it)+\Re\log\zeta(\sigma+2it)
=\sum_n c_n n^{-\sigma}\bigl(3+4\cos(t\log n)+\cos(2t\log n)\bigr)\ge0,
$$
because $3+4\cos\theta+\cos2\theta=2(1+\cos\theta)^2\ge0$. Hence $\zeta(\sigma)^3|\zeta(\sigma+it)|^4|\zeta(\sigma+2it)|\ge1$.
If $\zeta(1+it_0)=0$ ($t_0\ne0$), then as $\sigma\to1^+$: $\zeta(\sigma)\sim(\sigma-1)^{-1}$ (**the pole**),
$\zeta(\sigma+it_0)=O(\sigma-1)$ (the zero), $\zeta(\sigma+2it_0)\to\zeta(1+2it_0)$ **finite** (no pole, since
$t_0\ne0$). The product is $O(\sigma-1)\to0<1$ — contradiction. $\square$

The only ingredients are **(i)** an algebraic positivity ($2(1+\cos\theta)^2\ge0$), **(ii)** the **pole** of $\zeta$
at $s=1$, **(iii)** the *location* of that pole (none at $1+2it_0$). **No Dirichlet-polynomial mean value, no large
values estimate, no square-root cancellation.** So:

> **An exact absence-of-zeros theorem is proved with zero cancellation input.** N8's universal claim — *any* absence
> must pass through square-root cancellation — is **refuted**. *(The auditor's Scenario B is at least partly correct:
> N8 is a symptom, not the universal cause.)*

## 2. What N8 actually captured (and what it conflated)

N8 is **true of the density / exact-aggregate routes** (Littlewood, Motohashi, zero-density estimates): those reach
$\sigma=\tfrac12$ by controlling an oscillating sum, and there the square-root barrier is real and RH-equivalent.
But N8 **silently universalized** to all routes. The positivity route above is a route it does not describe. So the
program has **two distinct walls**, which N8 (and my earlier "capstone $=$ N8" unification) wrongly merged:

| route | mechanism | wall it hits |
|---|---|---|
| Littlewood, Motohashi, zero-density | control an oscillating prime sum | **square-root cancellation (N8)** |
| de la Vallée Poussin, Hilbert–Pólya, Weil positivity | positivity $+$ an **anchor** | **absence of an unconditional anchor at $\sigma=\tfrac12$** |

My earlier statement "positivity tools give only existence/density" was **wrong**: de la Vallée Poussin is a
positivity tool that gives **absence**. The difference between it and RH is **not cancellation** — it is the
**anchor**.

## 3. The real structure: the anchor asymmetry

Absence-via-positivity has the form **(positivity identity) + (an anchor = a place where $\zeta$ is unconditionally
large/forced)**:
- **de la Vallée Poussin:** anchor $=$ the **pole at $\sigma=1$**. Unconditional, free — gives absence on the line
  $\sigma=1$ with no cancellation, and a zero-free region a shrinking distance inward (the width $c/\log t$ uses only
  a *convexity* growth bound $|\zeta|\ll\log t$, far below square-root).
- **Hilbert–Pólya:** anchor $=$ **self-adjointness** of a putative operator with spectrum $=\{\gamma_\rho\}$. Would
  force *all* zeros real (absence at $\sigma=\tfrac12$) with no cancellation — but no such operator is known.
- **Weil positivity:** anchor $=$ **positivity at the center** $\sigma=\tfrac12$ via the functional equation. Would
  give RH — but its sign is undetermined unconditionally (the capstone).

**The asymmetry:** the pole anchors $\sigma=1$ **unconditionally and for free**. The critical line $\sigma=\tfrac12$
has **no unconditional anchor** — no pole there, no lower bound on $|\zeta(\tfrac12+it)|$, and the functional equation
supplies *symmetry* ($\xi(s)=\xi(1-s)$) but not an anchor. The density routes, lacking an anchor at $\tfrac12$,
*substitute* cancellation — and hit N8. The positivity routes that *could* reach $\tfrac12$ are exactly the ones whose
anchor (self-adjointness / center-positivity) is unproven.

> **The deeper object — behind the symptom N8.** The wall is not "square-root cancellation." It is: **there is no
> known unconditional positivity anchor at $\sigma=\tfrac12$ analogous to the pole at $\sigma=1$.** N8 is what the
> *anchorless* (cancellation) routes encounter; the capstone/Hilbert–Pólya is the *missing anchor* itself.

## 4. The reframed RH-directed question (different from N8, not yet collapsed)

Not *"prove square-root cancellation"* (N8 — a symptom of anchorless routes). Instead, the de la Vallée Poussin
template, moved to the center:

> **Q(anchor).** Is there an **unconditional positivity anchor at $\sigma=\tfrac12$** — a function/structure that is
> provably "large/positive" at the center, the way the pole forces $\zeta$ large at $\sigma=1$ — that a positivity
> identity could leverage into a zero-free statement reaching the critical line?

Candidates this exposes as one family: a hypothetical **auxiliary object with a pole (or forced lower bound) at
$\sigma=\tfrac12$**; the **self-adjoint operator** of Hilbert–Pólya; the **center-positivity** of Weil. They are the
*same missing ingredient* — an anchor at the center — now named as such.

## 5. Honest status — what is and isn't established (no repeat of N8's over-reach)

- **Established:** N8's *universal* form is **false** — de la Vallée Poussin forces exact absence with no
  cancellation. N8 correctly describes only the **density/anchorless** routes. The program has **two** walls, not
  one; the earlier "capstone $=$ N8" unification **over-reached** and is hereby corrected.
- **Established:** a coherent **anchor** structure organizes the positivity routes: the pole anchors $\sigma=1$
  (free); $\sigma=\tfrac12$ has no unconditional anchor; Hilbert–Pólya and Weil are the two candidate center-anchors,
  both unproven.
- **NOT claimed (and explicitly flagged, lest it repeat N8's error):** I do **not** assert Q(anchor) is more
  elementary than RH, nor that it is RH-equivalent. It is a **different** formulation — about a lower-bound/anchor
  structure, not about cancellation — and it has **not** been audited to collapse. That is its value: it is the one
  reframing that the program's collapse-to-N8 did **not** dispose of, because N8 only ruled out the *anchorless*
  routes.
- **Consequence for the program:** the honest frontier is **not** "the square-root barrier is the inevitable point
  of passage." It is: *anchorless routes hit square-root cancellation (N8); an anchored route at $\sigma=\tfrac12$
  would bypass it entirely, and whether such an anchor exists is open.* The auditor's Scenario B stands: **N8 is a
  symptom; the cause is the anchor asymmetry.**
