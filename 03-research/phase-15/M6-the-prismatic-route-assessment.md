# Phase 15 · M6 — The prismatic route (Advisor 4-2): where the integer grading actually lives

**Author: David Alejandro Trejo Pizzo · 2026-06-06.**
M5 closed the archimedean–modular direction with the **Lefschetz dichotomy**: Hodge–Riemann positivity needs a
lowest-weight/integer grading, and LI forbids one on the zeros (discrete horn) while the continuum only offers
principal series (continuum horn). Advisor 4-2 proposed escaping this by **changing the underlying topology** rather
than the grading: use **prismatic cohomology** (Bhatt–Scholze) over the absolute base, whose Frobenius and
**Sen/monodromy operators** supply a *canonical integer grading* (Hodge–Tate weights). This document assesses that
route with the program's filter. Verdict: prismatic cohomology **does** supply the integer-graded Lefschetz the
dichotomy lacked — but **locally**, on the weight grading of the anatomy, where for $\zeta$ it is trivial; the
**global** zero-carrying cohomology it would need is exactly SURF, unchanged. No escape, but a real sharpening:
the dichotomy's "missing integer grading" exists locally, confirming the obstruction is purely global gluing.

---

## 1. The proposal and why it is genuinely different

The Lefschetz dichotomy (M5) is a statement about gradings on a **fixed** space ($L^2$ of the spectral parameter).
Advisor 4-2's move is orthogonal: keep the requirement (an integer-graded hard Lefschetz) but **change the geometry
that produces it**.

- **Prismatic cohomology** $R\Gamma_{\mathbbΔ}(X/A)$ unifies de Rham, étale, crystalline, Hodge–Tate; it carries a
  Frobenius $\varphi$ built into the $\delta$-ring structure of the prism.
- The **Sen operator** $\Theta$ on Hodge–Tate cohomology has eigenvalues equal to the **Hodge–Tate weights**
  (integers); the **monodromy operator** $N$ (semistable case) is nilpotent and, by Jacobson–Morozov, generates an
  $\mathfrak{sl}_2$ — the **monodromy–weight filtration**, a genuine hard-Lefschetz-type structure with **integer
  grading**.

So the prismatic world *does* contain integer-graded $\mathfrak{sl}_2$-actions of exactly the type M5 found absent
on the continuum. The question the filter must answer: **what do the prismatic Frobenius and its monodromy grading
compute for $\zeta$ — the zeros, or something else?**

## 2. The filter: prismatic Frobenius $=$ local Satake $=$ the anatomy (not the zeros)

**Fact (Bhatt–Scholze; crystalline comparison).** For good reduction at $p$, the prismatic/crystalline Frobenius
eigenvalues on cohomology are the **local Satake parameters** $\{\alpha_{i,p}\}$ of the $L$-factor at $p$.

For $\zeta_{\mathbb Q}$ the local factor is $(1-p^{-s})^{-1}$ — a **single** Satake parameter $\alpha_p=1$. Hence the
prismatic Frobenius content is the anatomy power sums
$$
s_k(p)=\sum_i\alpha_{i,p}^{\,k}=1\qquad\text{for all }p,k,
$$
the **trivial anatomy of $\zeta$** (P19). The Hodge–Tate weights are integers and the monodromy is
$N=0$ (everywhere good reduction; $\zeta$ is the zeta of $\operatorname{Spec}\mathbb Z$ itself, a Tate motive).
*(Grounding computation: `experiments/m6_prismatic_frobenius.py`.)*

**The decisive separation.** The prismatic Frobenius eigenvalues are the **local** data $\{\alpha_{i,p}\}$, living on
the **local $p$-adic Hodge structure** (weights). The **global zeros** $\{\gamma_\rho\}$ are a **different object** —
the spectral side of the explicit formula, dual to the primes/Satake, **not** equal to local Frobenius eigenvalues:
$$
\underbrace{\{\alpha_{i,p}\}\ \text{(prismatic Frobenius, local)}}_{\text{prime side of the explicit formula}}
\qquad\xleftrightarrow{\ \text{explicit formula (duality)}\ }\qquad
\underbrace{\{\gamma_\rho\}\ \text{(zeros, global)}}_{\text{spectral side}} .
$$
Prismatic cohomology computes the **left** side. The integer monodromy grading it carries grades the **weights** of
the local Hodge structure, not the ordinates $\gamma_\rho$ — and for $\zeta$ that grading is trivial.

## 3. Why this does not escape — and what it sharpens

\begin{proposition}[M6 — the prismatic integer grading is local; the global obstruction is unchanged]
The integer-graded hard-Lefschetz $\mathfrak{sl}_2$ supplied by the prismatic Sen/monodromy operators acts on the
**local** weight structure (Hodge–Tate weights, monodromy filtration), reproducing the P19 anatomy
($s_k(p)=1$ for $\zeta$). It does **not** act on the global zero-spectrum: the $\gamma_\rho$ are not prismatic
Frobenius eigenvalues. Producing a cohomology over $\operatorname{Spec}\mathbb Z$ whose Frobenius eigenvalues are the
$\gamma_\rho$ — and gluing the local prismatic data into it — is the **SURF/Deninger–Connes–Consani** target, which
prismatic cohomology (a $p$-adic/local theory, per prism) does not currently supply.
\end{proposition}

So the prismatic route **relocates** to the program's standing wall (SURF: the missing global arithmetic surface for
$\operatorname{Spec}\mathbb Z$), not to a new one. The dichotomy's **discrete horn** — LI on the global zeros — is
untouched: to grade the $\gamma_\rho$ by an integer Lefschetz you still need them in an integer/weight structure,
which LI forbids.

**The sharpening (genuine).** The Lefschetz dichotomy (M5) said an integer-graded HR Lefschetz "exists in no current
geometry" for our setup. M6 corrects that: it **does** exist — *locally*, as the prismatic monodromy–weight
$\mathfrak{sl}_2$ on the anatomy. The obstruction is therefore **purely the global assembly** (gluing local
integer-graded Lefschetz data across all $p$ into a single zero-carrying cohomology), not a local impossibility.
This is consistent with, and refines, the program's standing diagnosis: the wall is SURF (the global surface), and
$\zeta$'s triviality ($N=0$, Tate motive, dimension $1$) is exactly why no surface is present to glue onto.

## 4. The one concrete sub-target the prismatic view leaves

The prismatic perspective does name a precise, non-vacuous question (the honest continuation, not a crossing):

> **Does absolute prismatic cohomology over $\operatorname{Spec}\mathbb Z$ (or over the sphere spectrum $\mathbb S$,
> à la Connes–Consani $\mathbb F_1$) admit a global Frobenius whose eigenvalues are the $\zeta$-zeros?**

This is the Deninger "$\Phi$ on leafwise cohomology" / Connes–Consani target stated in prismatic language. It is the
same object Attempt 6 isolated (the zero-carrying cohomology, distinct from the Arakelov height theory), now with a
candidate machine (absolute prismatic / $\delta$-rings) to build it. The program cannot manufacture it; flagging it
as the precise locus — and confirming (M6) that the *local* integer Lefschetz already exists, so only the *global*
gluing is missing — is the honest output.

## 5. Status

- **Assessed:** the prismatic route changes the topology and supplies an integer-graded monodromy–weight
  $\mathfrak{sl}_2$ — but on the **local** anatomy (Satake/Hodge–Tate weights), trivial for $\zeta$ ($N=0$). It does
  **not** supply the global zero-carrying cohomology.
- **Verdict:** **no escape from the dichotomy.** The prismatic integer grading is local (weights), not on the global
  zeros; the global obstruction is SURF, unchanged. The discrete horn (LI on the zeros) stands.
- **Sharpening (the gain):** the integer-graded HR Lefschetz the dichotomy lacked **exists locally** — so the
  obstruction is precisely the **global gluing** into a $\operatorname{Spec}\mathbb Z$-cohomology with the zeros as
  Frobenius eigenvalues, the Deninger/Connes–Consani/SURF target, now stated prismatically.
- **No crossing.** Consistent with the CAP/SURF map of the whole program: $\zeta$-routes terminate at the wrong-sign
  capstone (analysis) or the missing surface (geometry); the prismatic route is the latter, sharpened.

> M6 closes the four advisor routes against the filter: A1 restates M3 (in $W^*(\T)$); the archimedean–modular route
> (A2/A3/A4-i) reaches the Lefschetz dichotomy (M4–M5); the prismatic route (A4-2) relocates to SURF with the gain
> that the missing integer Lefschetz is local, not impossible. The standing wall — a global zero-carrying cohomology
> with a hard-Lefschetz class over $\operatorname{Spec}\mathbb Z$ — is unchanged, and now characterized from every
> side the advisors proposed.
