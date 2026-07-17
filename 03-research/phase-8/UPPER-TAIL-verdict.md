# Phase 8 / Attacking the upper tail — the sharpest form of the target, and where it lands

**Author: David Alejandro Trejo Pizzo · 2026-06-04.** `experiments/upper_tail_backward.py`.

## What "attack the upper tail" became, precisely

Self-correction first (guard-rail on my own RT-coupled note): the target is **not** an *average* pair
correlation — it is **extremal**. Even **one** complex pair forces $\Lambda>0$; $\Lambda$ is the **sup** of
backward-collision times. So RH needs control of the **worst** pair, uniformly — which no averaged statistic
gives.

**The mechanism (verified).** Under the flow a pair of gap $g$ obeys $g^2(t)=g_0^2+8t$ (2-body, verified to
$2\%$). Going **backward** ($t<0$) gaps shrink; a pair collides (births a complex pair) at $t_c=-g_0^2/8<0$.
The first backward collision time over all pairs **is** $\Lambda$ (the largest $t$ with a multiple zero).
RH $\iff t_c<0$ for the worst pair, **uniformly in $T$**.

## The measurement, and a genuinely new quantitative observation

Backward-flowing real $\zeta$ zeros until the tightest pair collides:

| $T$ | min gap$(t{=}0)$ | mean spacing $s$ | $t_c$ (collision) | $t_c/s^2$ |
|---:|---:|---:|---:|---:|
| 99 | 0.845 | 2.281 | $-0.105$ | $-0.020$ |
| 850 | 0.484 | 1.280 | $-0.032$ | $-0.0195$ |
| 2547 | 0.425 | 1.046 | $-0.025$ | $-0.023$ |

- In **absolute** units the margin $|t_c|$ **shrinks** with height ($0.105\to0.032\to0.025$) — because the
  mean spacing shrinks ($s\sim2\pi/\log T\to0$). This is the uniformity danger made visible.
- But in **normalized** units $t_c/s^2$ **clusters around a universal negative constant $\approx-0.02$**, not
  $0$. *(Suggestive: 3 points, a crude windowed flow without mean field — not a clean law.)* This is exactly
  the **GUE / sine-kernel prediction**: the closest-pair collision time, in mean-spacing units, is a universal
  negative constant. The marginal $\Lambda=0$ picture is consistent: $t_c\to0^-$ in absolute units (sup $=0$),
  while the *normalized* margin stays bounded below $0$.

## The sharpest statement of the target — and where it lands

> **RH $\Longleftarrow$ the normalized backward-collision margin $t_c/s^2$ stays a (universal) negative
> constant, uniformly in $T$** — i.e. the closest-pair gap statistics of the zeros are **GUE-universal,
> unconditionally**. This is the maximally quantitative form of the upper-tail target.

And it lands exactly on the **B1 wall**: GUE gap universality for $\zeta$ zeros is **open and RH-conditional**
(Montgomery's pair correlation is proven only in a restricted range; full universality / the unconditional
upper-tail control is unknown). The flow has not bypassed it — it has compressed the whole question into a
single sharp, quantitative, *extremal* statistic, and that statistic's uniform control is the open core.

## Honest verdict

Attacking the upper tail gave: (i) a **verified mechanism** ($g^2=g_0^2+8t$; $\Lambda=$ first backward
collision), (ii) a **new quantitative observation** (the normalized collision margin looks like a universal
negative constant $\approx-0.02$, GUE-consistent), and (iii) the **sharpest target statement**: RH $\Longleftarrow$
unconditional GUE gap universality of $\zeta$ zeros. **No crossing.** The irreducible barrier is now named in
its strongest form, and it is a famous open problem (unconditional universality), with no special key. $<2\%$.

This closes the upper-tail attack and, with it, the heat-flow program: every route — static (5 languages),
flow-only (N5), statistics-coupled, upper-tail extremal — terminates at the **unconditional gap/pair-correlation
universality of the zeros**, the one irreducible arithmetic statement.

## Status
- 2-body collision law $g^2=g_0^2+8t$, $\Lambda=$ first backward collision — ✅ verified.
- Normalized margin $t_c/s^2\approx-0.02$ universal (GUE) — ◆ suggestive (crude probe), RH-consistent.
- Sharpest target: RH ⟸ unconditional GUE gap universality — ✅ named; ❌ open, no key, $<2\%$.
- A crossing — ✗. Heat-flow program fully mapped and closed.
