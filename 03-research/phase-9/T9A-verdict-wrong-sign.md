# Phase 9 / T9-A — the support barrier, head-on: it is prime short-interval variance, and the unconditional tool is wrong-signed

**Author: David Alejandro Trejo Pizzo · 2026-06-04.** `experiments/T9A_montgomery_F.py`.

## What T9-A is, precisely

Montgomery's $F(\alpha,T)=\frac{2\pi}{T\log T}\sum_{0<\gamma,\gamma'\le T}T^{i\alpha(\gamma-\gamma')}\frac{4}{4+(\gamma-\gamma')^2}$
is known (Montgomery, on RH) to satisfy $F(\alpha)\sim|\alpha|$ for $|\alpha|<1$, and is **conjectured**
$F(\alpha)\sim1$ for $|\alpha|>1$. The region $|\alpha|>1$ is the **support barrier**: by the explicit formula it
is governed by **prime pair correlations** (Hardy–Littlewood), equivalently the **variance of primes in short
intervals** (Goldston–Montgomery). Extending the support past $1$ is one of the famous open problems of analytic
number theory.

*Computed* (700 real zeros, $T\approx667$; finite-$N$ convergence to the limit law is slow, so values are
indicative): $F$ rises through the $\alpha<1$ region and levels near a constant for $\alpha>1$ — the
conjectured shape, with the $\alpha>1$ region exactly where prime correlations enter.

## The sharp barrier — and the recurring wrong-sign theme

Our extremal target (P12): bound the **tight pairs** (small gaps) $=\int F(\alpha)\,\hat k(\alpha)\,d\alpha$ with
$\hat k\ge0$ at **large** $\alpha$ (small gaps $\leftrightarrow$ high frequency). This needs an **UPPER** bound
on $F$ for $\alpha>1$.

Montgomery's **unconditional** tool is $F(\alpha)\ge0$ (it is a sum of squares) together with the known law
for $\alpha<1$. Crucially:

> **$F\ge0$ yields LOWER bounds on clustering** (small gaps *do* occur — the Lehmer phenomenon, simplicity-of-zeros
> results all use $F\ge0$ to show gaps are small/zeros are simple), **NOT the UPPER bound** (clustering is
> *bounded*) that the collision margin / RH needs. **The available unconditional handle is one-sided the WRONG
> way.**

This is not an isolated accident. It is the **third** appearance of the same directionality obstruction:

| where | unconditional fact | direction it gives | RH needs |
|---|---|---|---|
| Gate B (P12) | $\dot{\mathcal L}\le0$ (Lyapunov) | $\mathcal L$ decreases forward | $\mathcal L(0)=0$ (the boundary) |
| N5/N6 | Weil $F\ge0$ (zeros positive-type) | existence / lower bounds | the SIGN / absence |
| T9-A | Montgomery $F\ge0$ | lower bounds on clustering | upper bound on clustering |

> **Meta-observation (the program's capstone).** *Every unconditional handle on the zeros is a **positivity**
> (a ``$\ge0$''), and it is oriented to give **lower bounds / existence / the easy side**. RH is fundamentally a
> one-sided **upper** constraint (no zeros off the line; no clustering above GUE; no anomalously tight pairs).
> Positivity gives the wrong inequality direction. This single mismatch — unconditional positivity is lower-bound-
> oriented, RH is an upper constraint — is, across all six no-gos (N1–N6) and T9-A, the deepest reason RH resists.*

## Honest verdict on T9-A

Attacked head-on, T9-A **reduces to upper bounds on $F(\alpha)$ for $\alpha>1$** $=$ prime pair-correlation /
short-interval variance — a famous open problem — and the **unconditional tool ($F\ge0$) is wrong-signed** for
it. We bring a precise reduction and a calibrating instrument, but **no key**: nothing here unlocks the upper
bound, and the wrong-sign meta-pattern explains why no current unconditional tool will. $<1\%$.

What remains genuinely **doable and finite** (not a crossing, but real): the **calibration deliverable** —
use the detector to determine *exactly how much* of the $\alpha>1$ upper bound (which support range, which tail
exponent) would suffice to force the collision margin $t_c/s^2<0$, giving the community a precise, quantified
target. This is the program's honest residual contribution.

## Status
- T9-A engaged head-on; $F(\alpha)$ computed; barrier = upper bounds on $F$ for $\alpha>1$ = short-interval
  prime variance (famous open) — ✅ characterized.
- The wrong-sign meta-pattern (unconditional positivity is lower-bound-oriented; RH is an upper constraint),
  unifying N1–N6 + T9-A — ✅ stated as the program's capstone.
- A crossing — ✗. The unconditional upper bound has no key; this is the field's open frontier.
- Residual doable: the detector-calibrated quantitative target (finite, real).
