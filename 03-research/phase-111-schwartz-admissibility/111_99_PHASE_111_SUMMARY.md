# 111.99 — Phase 111 summary

## Verdict

> **d1 is alive.** Every piece of the corner pairing converges on
> Schwartz-class data. Phase 110 closed the *compactly supported* route only,
> and its obstruction lies in a direction orthogonal to every convergence
> question here.

| item | verdict |
|---|---|
| polar terms $\widehat f(0),\widehat f(1)$ | exist, under explicit decay conditions (111_01) |
| zero sum $\sum_\rho\widehat f(\rho)\overline{\widehat g(\rho)}$ | converges absolutely, by an enormous margin |
| prime sum $\sum_n\Lambda(n)h(n)n^{-1/2}$ | converges (111_03 §2) |
| identity-value constraint of phase 108 | does **not** carry over — the trace is renormalized (111_02 §1) |
| $\xi$-divisible class $\cap$ convergent class | **nonempty**, modulo two linear conditions (111_03 §1) |
| $\mathfrak T$ as currently constructed | **construction unavailable** on Schwartz data (111_03 §3) |

## The structural finding

$\xi$ behaves oppositely in the two directions that matter, and both rates
are carried by $\Gamma$, not by $\zeta$:

| direction | rate | consequence |
|---|---|---|
| real axis, $\sigma\to\infty$ | $\log|\xi(\sigma)|/\sigma\to+\infty$ | kills compact support (phase 110) |
| critical line, $t\to\infty$ | $\log|\xi(\tfrac12+it)|/t\to-\pi/4$ | makes the zero sum converge |

Verified: the real-axis rate runs $0.126,\ 0.958,\ 2.046,\ 3.188$; the
critical-line rate runs $-0.327,\ -0.668,\ -0.730,\ -0.773,\ -0.782$ against
$-\pi/4=-0.785398$. Control: $\Gamma$'s own contribution to the critical-line
rate is $0.734,\ 0.783,\ 0.787,\ 0.786,\ 0.786$ — it *is* the whole rate,
while $\log|\zeta|=O(\log t)$ contributes nothing.

**So phase 110's impossibility and phase 111's convergence are not in
tension. They are different features of the same function.**

## The one open item

107_239 §3 builds $\mathfrak T(h):=\mathfrak T_{S(h)}(h)$ on a **finite** set
of places $S(h)$ fixed by $h$'s support. For Schwartz $h$ every prime power
contributes, so no finite $S(h)$ exists. By 111_03 §2 the sums nonetheless
converge, so this is a **construction** task — replace finite-place
stabilization by a convergence argument — not a divergence obstruction. We
have not built it and do not claim it is routine.

## Independent confirmation of the backward map

107_239's own "Still open" list names, in its own words, exactly the
requirements the backward map labels d1, d3, d4, d5: that $I_\partial$ be the
intersection product entering a Riemann–Roch theorem; the class whose local
equations are the DC potentials, with principal invariance; $H^1$ or an
existence theorem for positive self-intersection; and a
Hodge-index/effectivity statement.

## Verifiers

`111_01_convergence_of_the_three_pieces.py`, `111_02_the_two_directions.py`,
`111_03_verdict.py` — all exit 0.

Nothing in this phase bears on RH. No status promoted.
