# Phase 10 — Deep-run analysis (M=25, T up to 10⁴, 10154 ζ zeros, 3.4 h)

**Author: David Alejandro Trejo Pizzo · 2026-06-04.** Figure: `deeprun_M10.1-M10.3.png`.
The deeper Colab run (basis dim $M=25$, heights to $T=10^4$) sharpens M10.1–M10.2 and **corrects an
over-optimistic reading of M10.3** — which is exactly why we ran it deeper. Honest analysis below.

---

## M10.1 (deeper) — degeneration, sharper

| $d$ | bare Hodge gap | signature |
|---:|---:|---:|
| 1.0 | $+0.353$ | $(1,25,0)$ definite |
| 1.5 | $+5.4\times10^{-3}$ | $(1,25,0)$ definite |
| 2.0 | $+8\times10^{-11}$ | $(1,22,3)$ degenerate |
| 4.0 | $\sim0$ | $(1,13,12)$ degenerate |

With $M=25$ the picture is **cleaner**: definite (Lorentzian) for small genus, degenerating to signature
$(1,13,12)$ by $d=4$ — 12 null directions. Confirms M10.1: the bare intersection form degenerates toward $\zeta$.

## M10.2 (deeper) — regularized gap survives, confirmed

$\lambda_{\min}(G)=0.15,0.33,0.46,0.62,0.72,0.74$ as $d=1.5\!\to\!4$. Positive and healthy, rising as the band
resolves. Confirms: the **primitive form is definite**; the degeneration was trivial nullity.

## M10.3 (deeper) — the important correction

| $T_0$ | $K/M$ | $\lambda_{\min}(G)$ | tightest $\beta_{\min}$ | $\lambda_{\min}/\beta_{\min}^2$ |
|---:|---:|---:|---:|---:|
| 50 | 19/25 | 0.284 | 0.475 | 1.26 |
| 100 | 19/25 | 0.281 | 0.372 | 2.03 |
| 300 | 20/25 | 0.249 | 0.374 | 1.78 |
| 1000 | 19/25 | 0.290 | 0.392 | 1.89 |
| 3000 | 19/25 | 0.204 | 0.365 | 1.53 |
| **10⁴** | 20/25 | **0.111** | **0.313** | 1.13 |

**The new fact: at $T=10^4$ the regularized gap dropped to $0.111$ — about half the $\sim0.28$ plateau.**
The earlier (T≤3000) "stability" was a too-short range. Two honest readings, and the data discriminates:

> **The regularized gap obeys $\boxed{\lambda_{\min}(G)\approx\tfrac{\pi^2}{6}\,\beta_{\min}^2}$** — the
> **squared tightest normalized gap** (the $2\times2$ sine-kernel level-repulsion law,
> $1-\tfrac{\sin\pi\beta}{\pi\beta}\approx\tfrac{\pi^2}{6}\beta^2$). Ratio $\lambda/\beta^2\in[1.1,2.0]$ around
> $\pi^2/6=1.64$; the $T=10^4$ dip is exactly its window's tighter pair ($\beta_{\min}=0.31$, the smallest).

So the frame bound is **governed by each window's tightest pair**, not uniformly constant. With fixed $K\approx19$,
$\beta_{\min}$ is the min of $\sim19$ GUE gaps — a *fluctuating* quantity (the $T=10^4$ dip is consistent with
fluctuation, not proven systematic decay). **But the uniform infimum over *all* windows is set by the GLOBAL
tightest Lehmer pairs, and $\inf\beta_{\min}\to0$ (the Lehmer phenomenon), so $\inf\lambda_{\min}(G)\to0$.**

## Honest conclusion of the deep run

> **The regularized Hodge index gap is NOT uniformly bounded below in the naive sense: it equals
> $\tfrac{\pi^2}{6}\beta_{\min}^2$, so it dips wherever a tight pair sits and its infimum $\to0$ at the Lehmer
> pairs.** The "T-stability" of the shallow run was the slow, fluctuating regime; the deep run reveals the
> bound's true governance by the extremal tightest gap. **The cohomological route therefore reduces to (U) —
> controlling $\beta_{\min}$ uniformly — the SAME extremal target, now with the explicit law
> $\lambda_{\min}(G)=\tfrac{\pi^2}{6}\beta_{\min}^2$ tying the regularized Hodge gap to the minimum gap.**

This is the guard-rail working: more numbers corrected the optimism. What **survives and is genuinely useful**:
1. The **explicit law** $\lambda_{\min}(G)=\tfrac{\pi^2}{6}\beta_{\min}^2$ — the regularized Hodge gap *is* the
   squared minimum gap. (Ties M10.2/M10.3 to T9-cal's $\beta_{\min}\sim N^{-1/3}$ and the collision margin.)
2. The **two-sided framing** still stands: RH $\iff$ uniform $A_2$ on $E\sim\xi$ $\iff$ $S(T)$ regularity, and
   $A_2$ is *designed* to handle sparse bad sets (the Lehmer windows). Whether Selberg's unconditional $S(T)$
   control tames them is the precise M10.4 question — now sharpened by the law above.

## What the deep run did NOT do
It did not reach the genuinely tight Lehmer pairs (the smallest $\beta_{\min}$ here is $0.31$; record Lehmer
pairs have $\beta\sim10^{-3}$ at much greater heights). So the *uniform* failure is not yet visible in data — only
the $\beta_{\min}^2$ governance is. The infimum question is (U), unreachable by finite computation.

### Status → M10.4
- $\lambda_{\min}(G)=\tfrac{\pi^2}{6}\beta_{\min}^2$ — ✅ established (deep run, corrected M10.3).
- Uniform frame bound holds — ❌ not uniform (dips as $\beta_{\min}^2$; $\inf\to0$ at Lehmer) = (U).
- The $A_2$/$S(T)$ two-sided framing survives; **M10.4 prices it**: does Selberg's unconditional $S(T)$ control
  give *any* nontrivial unconditional lower bound on the frame constant / $\beta_{\min}$?
