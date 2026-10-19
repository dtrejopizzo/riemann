# Phase 28 — Four simultaneous fronts

**Prerequisite:** Results of Phases 26–27 accepted; bridge conjecture 26-C.2 as a working hypothesis.

---

## The diagnosis of Phase 27

Phase 27 identified that all the obstacles of the program reduce to the same object:
constructing the arithmetic cohomology $H^1(\mathrm{Spec}\,\mathbb{Z})$ with positive
intersection form (Wall A = Connes–Consani arithmetic site). But it also
identified that this wall has gone unsolved for decades.

Phase 28 abandons the reformulation strategy and opens four fronts that attack
**causal mechanisms**, not equivalences. The distinction is precise:

> An equivalent reformulation of RH answers: *what does RH mean?*
> A causal mechanism answers: *why can the zeros not leave the critical line?*

Phase 28 seeks causal mechanisms.

---

## The four fronts

| Front | Central question | New tool |
|---|---|---|
| **A** | Is the de Bruijn–Newman flow the gradient flow of the logarithmic energy? | Zero dynamics, Csordas–Norfolk–Varga ODE |
| **B** | Is the APS $\eta$-invariant of the Weil operator identically zero? | Atiyah–Patodi–Singer index theory |
| **C** | Is the negative spectral projection $[P_-]$ the trivial class in $K_0(C^*(C_\mathbb{Q}))$? | K-theory of C*-algebras, Baum–Connes |
| **D** | Is the critical line the unique minimum of a canonical arithmetic energy? | Variational problem, transversal energy |

---

## The central result: A and D are the same front

Before beginning: the most important observation of Phase 28 is that Fronts A and D
are the **same program in two languages**.

The de Bruijn–Newman flow on the zeros of $H_t$ is exactly the gradient flow
of the logarithmic energy:
$$E_{\log}(Z) = -\sum_{j \ne k} \log|z_j - z_k|.$$

This was established by Csordas–Norfolk–Varga (1988): the evolution equation of the
zeros is:
$$\frac{dz_n}{dt} = \sum_{k \ne n} \frac{2}{z_k - z_n}.$$

Then the question of Front A (does the flow monotonically decrease the Kreĭn index?)
and the question of Front D (does the arithmetic energy have a unique minimum on the
critical line?) are the same question: does the gradient flow of $E_{\log}$, subject to the
arithmetic constraints of $\zeta$, converge to the configuration with $b_j = 0$?

We will document the two fronts separately for clarity, but the unification is the
most important structural result of Phase 28.

---

## Success criterion per front

| Front | Full success | Partial success (publishable) |
|---|---|---|
| A | $\kappa_t$ strictly non-increasing under the DBN flow → RH | Exact formula $\Lambda = b_{\max}^2/2$ |
| B | $\eta(T_0) = 0$ by arithmetic symmetry → $\kappa = 0$ | Explicit computation of $\eta(T_0)$ |
| C | $[P_-] = 0$ in $K_0$ by Baum–Connes → RH | Precise identification of the image of $[P_-]$ |
| D | Arithmetic energy with unique minimum at $b_j = 0$ → RH | Necessary and sufficient condition in terms of $b_j$ |

---

## Documents of Phase 28

- `phase-28-four-fronts/01-front-A.md` — Front A: DBN flow and Kreĭn monotonicity
- `phase-28-four-fronts/02-front-B.md` — Front B: spectral flow and the $\eta$-invariant
- `phase-28-four-fronts/03-front-C.md` — Front C: K-theory and the obstruction class
- `phase-28-four-fronts/04-front-D.md` — Front D: transversal energy and the critical line as an attractor
