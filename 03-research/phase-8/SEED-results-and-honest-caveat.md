# Phase 8 — Seed results (Gate A) and the honest caveat

**Author: David Alejandro Trejo Pizzo · 2026-06-04.** `experiments/heatflow_seed.py`.

## What the seed established (real, measured)

Coupling the local Coulomb-gas zero dynamics ($\dot z_j=2\sum_{k\ne j}(z_j-z_k)^{-1}$, the de Bruijn–Newman
forward flow) to our band-limited Carleson constant $C=1-\lambda_{\min}(Z,A_\Phi)$ (with $Z$ the Weil
zero-side form — the **indefinite** quartet for complex zeros, the PSD $vv^*$ for real ones):

1. **Real zeros:** $C(t{=}0)=0.998033\le1$ — **marginal**, just under $1$. This is the local shadow of
   $\Lambda=0$: RH true with essentially zero margin (consistent with N3 saturation). $dC/dt\approx+10^{-3}$.
2. **The attractor (the rigorous mechanism):** an injected off-line pair at $\delta_0=0.30$ gives $C=1.0023>1$
   (violation correctly detected). Under the **forward** flow the pair **heals**: $\max|\mathrm{Im}\,z|$ drops
   $0.30\to0.269$ and $C\to1.0014$ toward $1$. Same healing at $\delta_0=0.05,0.15$ ($|\mathrm{Im}|$ shrinks).
   **The critical line is the attractor of the heat flow, and our detector tracks it.**

This is the rigorous realization of the "stable attractor / PT-symmetry" instinct (suggestion 1) — as actual
mathematics (a Coulomb gas), not a metaphor. The path is concrete, computable, and our assets couple to it.

**A guard-rail catch (logged):** the first seed used the PSD Gram $\sum vv^*$ for complex zeros — **always
PSD**, so it could never show $C>1$ and falsely reported "no healing." Corrected to the Weil quartet
$\sum\mathrm{outer}(S(z),\overline{S(\bar z)})$ (indefinite for complex $z$; matches B1). Only then did the
violation ($C>1$) and the healing appear. *Every sign claim checked against ground truth before belief.*

## The honest caveat (what the seed does NOT show)

The seed ran the flow **forward** (increasing $t$) — the **well-posed, smoothing** direction, where healing
is *expected and somewhat trivial* (heat smooths). **The actual RH content is in the backward/marginal
direction:** RH $\iff\Lambda\le0\iff$ no complex pair exists already at $t=0$, i.e. flowing **backward** from
$t=\Lambda>0$ down to $0$ never **births** a pair. The backward heat flow is ill-posed; the seed does not test
it. So the seed **confirms the mechanism and the measurability**, and **identifies the Lyapunov candidate**,
but does **not** resolve the hard direction.

## The refined Lyapunov candidate (for Gate B)

$C$ itself is not the clean Lyapunov ($dC/dt$ small, $+$ on real zeros — creeps toward saturation). The seed
shows the right functional is the **off-line-ness**
$$\mathcal L(t)=\sum_j\big(\mathrm{Im}\,z_j(t)\big)^2,$$
which the flow contracts (the conjugate-partner term $\dot z\ni -i/\mathrm{Im}\,z$ pulls each complex zero
toward the real axis at rate $\sim1/\mathrm{Im}$). $\mathcal L\ge0$, $\mathcal L=0\iff$ all real, and
$\mathcal L(t)=0$ for $t\ge\Lambda$. 

> **Gate B (the crux, restated honestly).** Prove from the Coulomb ODE that $\mathcal L$ cannot become
> positive as $t$ decreases to $0$ — i.e. the partner-attraction (always healing, rate $1/\mathrm{Im}$)
> dominates the shear from the other zeros, **uniformly in height**. This is genuinely different from a
> static positivity (it is a differential inequality for a flow), but it is **essentially $\Lambda\le0$** and
> may be RH-equivalent. The make-or-break: is the domination provable from the ODE structure (Coulomb
> repulsion + kernel positivity) alone, or does it need an input equivalent to "no complex zeros"?

## Status / next
- Gate A — ✅ mechanism real, measured; attractor confirmed; Lyapunov candidate $\mathcal L=\sum(\mathrm{Im}\,z)^2$ identified.
- Honest caveat — the forward seed does not test the hard (backward) direction; that is Gate B.
- NEXT (Gate B): the differential inequality $\dot{\mathcal L}\le 0$ near $t=0$ from the ODE — attempt the
  proof; if it needs RH as input, log the sixth language honestly. Then Gate C (uniformity in $T_0$).
