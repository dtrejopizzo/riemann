# Phase 8 / Rodgers–Tao statistics-coupled — the heat-flow path lands on the upper pair-correlation

**Author: David Alejandro Trejo Pizzo · 2026-06-04.** `experiments/rt_statistics_coupled.py`.

## The engagement (concrete, with real zeros)

N5 forced arithmetic into the **initial data**; Rodgers–Tao do this by coupling the flow to $\zeta$'s actual
zero statistics. Their **proved** result $\Lambda\ge0$ uses the **lower tail**: the zeros *fluctuate* (they
are not a rigid lattice). RH $=\Lambda\le0$ needs the **upper tail**: no pair clusters so tightly that it
collides and births a complex pair for $t>0$ — *uniformly in height*.

By Gate B an isolated pair heals with $d(y^2)/dt=-2$; reversing, a tight real pair of normalized gap $g$
reaches a backward collision on a $t$-scale $\sim g^2$. So $\Lambda$ is governed by the **closest pairs**.
Measuring real $\zeta$ zeros:

| height $T$ | min normalized gap $g_{\min}$ | backward-collision scale $\sim g_{\min}^2$ |
|---:|---:|---:|
| $\sim 310$ | 0.291 | 0.085 |
| $\sim 1591$ | 0.221 | 0.049 |
| $\sim 10005$ | 0.194 | 0.038 |

**The minimum gap shrinks with height** (and the count of tight gaps grows). This is the Lehmer phenomenon:
there is **no positive uniform lower bound on the gaps**. The zeros never actually collide *on the line* (they
stay simple real — RH), but they come arbitrarily close. *The uniformity problem is now visible in data.*

## The precise verdict

> **The de Bruijn–Newman / heat-flow path, fully engaged, reduces to the UPPER tail of the pair correlation,
> uniformly in $T$.** The lower tail ($\Lambda\ge0$, Rodgers–Tao) is done. The upper tail ($\Lambda\le0=$ RH)
> — a uniform bound forbidding anomalously tight clustering of the zeros — is **open and RH-conditional**
> (Montgomery's pair correlation is proven only in a limited range; the uniform upper control is unknown).
> This is **exactly the B1 wall** (the sine-kernel / pair correlation), upper tail. The flow did not bypass
> the arithmetic; it delivered us, precisely, to the one irreducible statistical statement.

So the heat-flow program closes with the map sharpened, not crossed:
- **N5:** flow-only (Lyapunov) is arithmetic-blind — cannot cross.
- **RT-coupled:** using the statistics, the target is the **uniform upper pair-correlation** — the open core.

## What is durable from Phase 8

1. **The Lyapunov theorem** $\dot{\mathcal L}=-2\sum_{j\ne k}(y_j-y_k)^2/|z_j-z_k|^2\le0$ — clean,
   unconditional, new; rigorously establishes the critical line as the flow's attractor.
2. **The height bound** $|\mathrm{Im}|\le\sqrt{2\Lambda}\le0.63$ for any violator (de Bruijn type).
3. **N5** — the dynamical no-go (flow-only ⇒ arithmetic-blind), subsuming the PT-symmetry/dissipative class.
4. **The precise localization:** RH (via this route) $=$ uniform upper pair-correlation $=$ no-uniform-tight-Lehmer.

These join the P11 five-language map. Phase 8 added a *dynamical* sixth view and, importantly, the first
**proved no-go for a whole class of methods** (N5).

## The irreducible target, named

Every route — static positivity (5 languages), flow-only (N5), statistics-coupled (here) — terminates at the
**same arithmetic statement**: a control of the *upper-tail clustering of the zeros, uniform in height*. This
is the genuine open core; we have no special key to it, and inventing one is the "new mathematics" the problem
demands. The honest odds of cracking it from here are $<2\%$.

## Status
- RT statistics-coupling engaged with real zeros — ✅ lands on the uniform upper pair correlation (B1 wall).
- Lehmer/uniformity problem illustrated (gaps shrink with $T$) — ✅.
- A crossing — ✗. Phase 8 closes: dynamical view + N5 + the named irreducible target.
