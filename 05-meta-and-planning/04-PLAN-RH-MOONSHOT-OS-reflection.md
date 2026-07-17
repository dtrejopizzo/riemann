# PLAN — RH MOONSHOT: Osterwalder–Schrader reflection positivity via the Euler-product lattice

**The path past the wall.** Author: David Alejandro Trejo Pizzo · 2026-06-03.
A genuinely novel synthesis — not another reformulation, a *mechanism to force the sign*. High-risk,
principled, and it unifies the entire program (the Kreĭn $J$, the anatomy $R_p$, Conjecture B2, the validated
engine) into one attack. Honest odds for full RH: $<1\%$; but every sub-step is a real result, and the route
is one no one has assembled.

---

## 0. The wall, stated exactly (so we know what we must cross)

Everything we proved is equivalent to RH and stuck at the **sign**:
$$
\mathrm{RH}\iff \mathfrak t\succeq0\iff \inf\operatorname{spec}(\mathcal T)\ge0\iff\|K\|\le1\iff \nu\ \text{Carleson}\le1\iff \mathrm{Id}-K_{\mathrm{CC}}\succeq0.
$$
The **magnitude** (finiteness, $\|K\|<\infty$, the Carleson bound is finite) is unconditional from Ramanujan.
The **sign** ($\le1$, $\succeq0$) is RH. P8 Theorem C: the zero side cannot supply it (circular). Connes'
archimedean route can, and is stuck at "lower the top eigenvalue below 1." **No bound forces the sign; only a
*structure* that makes positivity manifest can.** A square $\mathcal T=A^*A$ is one such structure. **OS
reflection positivity is another — and it comes with a construction machine.**

## 1. The new insight: $J$ is the functional-equation reflection, so positivity is *reflection* positivity

Our Kreĭn fundamental symmetry $J:\rho\mapsto 1-\bar\rho$ is the **functional-equation reflection**
$s\leftrightarrow1-s$, i.e. reflection of $\Re(s)$ about the critical line. In the spectral variable
$s=\tfrac12+ir$, $J$ is reflection $r\leftrightarrow\bar r$ across the real axis $\Im r=0$; **the off-line
displacement $\delta=\Im r$ is a "Euclidean time", and the critical line is the time-zero slice.** Then:
$$
\boxed{\ \mathrm{RH}\iff \text{the Weil form is Osterwalder–Schrader reflection-positive for }\Theta=J.\ }
$$
This is not analogy: "$E^*JE\succeq0$ on $R(E)$" *is* the statement "$\langle\Theta F,F\rangle\ge0$", the OS
reflection-positivity axiom, with $\Theta=J$ the time-reflection.

**Why this is leverage and the angular/Carleson forms were not.** The angular operator and the Carleson
measure are *reformulations* of "is it positive?". OS reflection positivity is a reformulation **with a
theorem attached**: the **OS reconstruction theorem** says a reflection-positive form yields, by GNS on the
time-zero slice, a Hilbert space and a *self-adjoint* generator $H\succeq0$ with the time-translations acting
as $e^{-H\tau}$. **Applied here, OS reconstruction produces the Hilbert–Pólya operator for free** — the
zeros become the spectrum of a self-adjoint $H$, hence real, hence RH. So:
$$
\text{(OS reflection positivity of the Weil form)}\ \xrightarrow{\ \text{OS reconstruction}\ }\ \text{Hilbert–Pólya }H=H^*\ \Rightarrow\ \text{real spectrum}\ \Rightarrow\ \mathrm{RH}.
$$
The task moves from "bound a norm" to "**prove a reflection positivity**" — and reflection positivity has a
*standard route*: factorization over a lattice.

## 2. The mechanism: the Euler product is a reflection-positive lattice factorization

In statistical mechanics/QFT, reflection positivity of a system that **factorizes over sites** follows from
(i) each local factor being reflection-positive and (ii) the product/Markov structure (a tensor/transfer
argument). **The Euler product is exactly a factorization over sites** (the primes $p$, plus the archimedean
place $\infty$): $\Lambda_L(s)=\prod_v L_v(s)$. So the strategy:
$$
\boxed{\ \Big(\text{each local factor }L_v\text{ is reflection-positive}\Big)\ +\ \Big(\text{the product over }v\text{ preserves it}\Big)\ \Longrightarrow\ \text{global OS positivity}\ \Longrightarrow\ \mathrm{RH}.\ }
$$

**The consistency check that this is the right idea.** $L_{\mathrm{DH}}$ violates RH and **has no Euler
product** (no site factorization). The mechanism *predicts* exactly this: no factorization $\Rightarrow$ no
reflection-positive tensor structure $\Rightarrow$ positivity may fail $\Rightarrow$ off-line zeros. $\zeta$
(Euler product) $\Rightarrow$ factorization $\Rightarrow$ reflection positivity $\Rightarrow$ RH. **This is
the structural mechanism behind our Conjecture B2** ("factorizing profile $\iff$ Euler product"): B2 is the
*shadow* of "Euler product $\Rightarrow$ reflection-positive lattice $\Rightarrow$ OS positivity $\Rightarrow$
RH." The whole program's discriminant lands here.

## 3. The proof skeleton (four steps; each is a result on its own)

> **S1 — Set up the OS form rigorously.** Identify the triple (field configurations, Euclidean time $\tau=\delta$,
> measure $d\mu$) such that the Weil quadratic form $\mathfrak t$ equals the OS form
> $\langle\Theta F,F\rangle_\mu$ with $\Theta=J$. *Deliverable:* a precise OS-axiom statement of Weil
> positivity. *Anchor:* our validated engine already computes $\mathfrak t$ on $\Theta$-paired configurations
> (the $\delta$ vs $-\delta$ structure is built into $M_{\mathrm{zeros}}$); it can **test S1 numerically**.

> **S2 — Local reflection positivity at each place.** Prove each local factor is reflection-positive.
> - *Archimedean $\infty$:* this is (essentially) Connes–Consani's solved case — the Sonin/prolate manifest
>   square. Re-read it as local OS positivity for the $\Gamma$-factor. *Likely provable.*
> - *Finite primes $p$:* **new.** The local Euler factor $L_p(s)^{-1}=\prod_j(1-\alpha_{p,j}p^{-s})$ must give
>   a reflection-positive local form. With Ramanujan ($|\alpha_{p,j}|=1$), the local factor is a finite,
>   explicit, unitary object — a *finite-dimensional* reflection-positivity check per prime. *This is the
>   concrete, attackable heart.*

> **S3 — The gluing (the hard core).** Prove the product over places **preserves** reflection positivity: a
> Markov / Cotlar–Stein / transfer-matrix argument on the adelic structure. This is where the prime conspiracy
> becomes a *tensor* structure rather than a cancellation. *Anchor:* our anatomy decomposition
> $\lambda_{\min}=R_\infty-\sum_p R_p$ is the additive shadow of the multiplicative gluing; the engine
> measures the cross-place terms.

> **S4 — OS reconstruction $\Rightarrow$ Hilbert–Pólya.** Apply OS reconstruction to the (now proven)
> reflection-positive form: obtain $H=H^*\succeq0$ on the time-zero (critical-line) slice, with the zeros as
> its spectrum. Real spectrum $\Rightarrow$ RH. *This step is standard once S1–S3 hold* — it is the payoff of
> doing positivity the OS way rather than the bound way.

## 4. Why this is genuinely new (and honest about it)

- **New synthesis, not new pieces.** Reflection positivity, OS reconstruction, the Euler product, Hilbert–Pólya,
  Connes' archimedean positivity — all exist. **What no one has assembled** is: *use the functional-equation
  reflection as the OS time-reflection, the Euler product as the reflection-positive lattice, and OS
  reconstruction to build Hilbert–Pólya* — with the $\zeta$-vs-$L_{\mathrm{DH}}$ discriminant as the built-in
  consistency check. Our program is uniquely positioned because we already proved $J$ is the reflection (Kreĭn
  structure), isolated the per-place anatomy ($R_p$), and built a validated engine that computes the form on
  $\Theta$-paired data.
- **The hard step is S3 (gluing).** Reflection positivity for number-theoretic "lattices" is delicate: the
  primes are not a literal nearest-neighbour lattice, and the adelic "time" is not obviously OS-compatible.
  S3 is where the moonshot lives or dies. **We do not assume it; we attack it, and a clean no-go for S3 is
  itself a major structural theorem** (it would say *why* the prime conspiracy resists factorization).

## 5. The validated engine as the guide (our unfair advantage)

Every step is **numerically testable** with the Phase-3 engine, which already computes $\mathfrak t$ on
$\delta$-displaced (i.e. $\Theta$-paired) configurations:
- **S1 test:** verify the OS form identity numerically (the engine's $\delta\leftrightarrow-\delta$ structure).
- **S2 test:** isolate a single prime's contribution and check local reflection positivity.
- **S3 test:** measure the cross-place (off-diagonal) terms; do they preserve or break positivity as primes
  are added? (Our anatomy already saw $\lambda_{\min}$ stay at the floor for $\zeta$ — consistent with S3
  holding; the engine can stress-test it.)
This converts an abstract program into a **falsifiable, instrument-guided** one — the way physics actually
finds new structure.

## 6. Tiered outcomes (honest)

| Outcome | Prob. | Value |
|---|---|---|
| Full S1–S4 $\Rightarrow$ **RH** | $<1\%$ | the theorem |
| S1+S2 (OS setup + per-place reflection positivity) | $\sim15\%$ | a new positivity framework for $\mathfrak t$ |
| S3 no-go (why factorization fails to glue) | $\sim25\%$ | a major structural theorem; explains the wall |
| OS reconstruction of a Hilbert–Pólya $H$ modulo S3 | $\sim10\%$ | the long-sought operator, conditional |
| The $\zeta$-vs-$L_{\mathrm{DH}}$ mechanism made rigorous (B2 via reflection positivity) | $\sim30\%$ | the discriminant, explained |

**The realistic prize is S3-or-its-no-go** — either way a first-of-its-kind result on *why* the Euler product
controls the sign.

## 7. Hedge angles (if OS stalls)

- **(H1) Rigidity / over-determination.** Use P7's quantitative forced-negativity ($\lambda_{\min}\le-c\delta^2 A(\gamma)$)
  as a constraint that an off-line zero imposes at *every* height (through the global prime side). Show the
  system of constraints (functional equation + Euler product + local forced-negativity at all heights) has
  **no consistent off-line solution** (a rigidity theorem). Our engine measures $A(\gamma)$; the question is
  whether the constraints over-determine.
- **(H2) Function-field interpolation.** Weil *proved* RH for curves over $\mathbb F_q$ via positivity
  (intersection theory on $C\times C$). Construct a deformation from the function-field object (positive,
  provable) to $\zeta$, with a Lyapunov function (the angular norm $\|K\|$, T2's transversality) that prevents
  the crossing $\|K\|=1$. Connes' Scaling Site is the target geometry; our quantitative local rate is the new
  control.

## 8. Guardrails (the discipline that got us here)

- **Zero-independence (B0):** the OS form and the local factors must be built from the arithmetic, not the
  zeros (else circular, P8 Thm C). The Euler product is zero-independent — good.
- **Magnitude $\ne$ sign:** OS positivity is a *structure*, not a bound; do not slip back into bounding $\|K\|$.
- **Audit before pillarizing; the engine falsifies.** Every step gets the numerical stress-test before it
  becomes a foundation. A failed gate kills a step early.
- **Honest priors up front.** $<1\%$ for RH; high for durable structural results. We mine the moonshot for
  structure, with RH as the target we genuinely attack, not assume.

---

## First concrete move (M-OS-1)

**Set up S1 precisely and test it on the engine.** Write the Weil form as an OS form
$\mathfrak t(F)=\langle\Theta F,F\rangle_\mu$ with $\Theta=J$ and identify $(\mu,\tau)$; then use the
validated Phase-3 engine to verify the OS reflection-positivity statement numerically on $\zeta$ (should hold,
$\delta=0$ slice) and watch it *fail* as $\delta$ grows (the forced-negativity curve we already have IS the OS
reflection-positivity test). If the identification is clean, S2 (per-place) is the next attack.

**Net.** *We stop trying to bound the sign and instead try to build the structure that makes it manifest:
Osterwalder–Schrader reflection positivity for the functional-equation reflection, with the Euler product as
the reflection-positive lattice and OS reconstruction delivering Hilbert–Pólya. It is the one path that turns
"the Euler product controls RH" from a slogan into a mechanism, it explains $\zeta$ vs $L_{\mathrm{DH}}$, and
it is instrument-guided by our validated engine. Odds are long; the route is new; and it is the honest place
to point a serious, ambitious effort.*
