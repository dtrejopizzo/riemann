# Phase 8 — A genuinely new path: the de Bruijn–Newman heat flow, RH ⟺ Λ=0, coupled to our detector

**Author: David Alejandro Trejo Pizzo · 2026-06-04.**
Mandate from the principal: *do not give up; RH is computationally certain, so a proof must exist, even if it
needs new mathematics; build a methodology like the OpenAI autonomous-proof effort (precise statement →
autonomous iterated attack → rigorous verification → self-refutation).* This document designs that path.
It is honest about odds (<5%) and about why this surface is **new** and **not** one of our five mapped walls.

---

## 0. Honest triage of the three proposed directions (engaged, not dismissed)

The principal forwarded three "out-of-the-box" suggestions. I engaged each critically:

1. **PT-symmetry / neuromorphic dissipative Hilbert–Pólya.** The rigorous core is Berry–Keating $xp$ and
   Bender–Brody–Müller (2017). This is the **Hilbert–Pólya wall** we already mapped (P8 no-go): the operator
   is not rigorously self-adjoint, and proving its PT-symmetry unbroken (real spectrum) **is** RH. The
   "neuromorphic/dissipative" dressing adds no rigorous content. *Verdict: a known wall in physics clothing.*
   **But** it contains the right instinct — *dynamics with the critical line as the only stable attractor* —
   which the **rigorous** heat-flow below realizes.
2. **Lattices / SVP geometry.** Genuinely untried by us — and it has a **decisive cautionary fact**: Epstein
   zeta functions (lattice zeta functions) **generically violate RH** (off-line zeros are proven for many
   quadratic forms / class number $>1$). So "lattice geometry forces the critical line" is **false** as a
   general principle; what separates $\zeta$ from Epstein zetas is the **Euler product**. *Verdict: a likely
   dead end — and the reason why **confirms our Conjecture B2** (multiplicativity, not geometry, is the
   discriminant). Useful negative.*
3. **NCG / partition-function entropy.** This is Connes, which we **just engaged** (Phase 7c, N4): the
   archimedean place is provably positive (prolate $\lambda<1$), the obstruction is the finite places, same
   wall. The "negative entropy of an off-line zero" intuition is appealing but in Connes' actual framework
   the obstruction does not become a thermodynamic invariant; it stays the finite-place positivity. *Verdict:
   done; same wall.*

**None is the new path.** But (1)'s dynamical instinct, made rigorous, **is** the new path.

---

## 1. The reframing that breaks the self-reference

Every one of our five languages (P11 §5) reduces RH to *positivity at $t{=}0$ $=$ reality of the zeros at
$t{=}0$* — a **tautology**, because both sides are the same object through the explicit formula. To escape we
need an ingredient that is **logically prior to** the reality of the zeros. The **de Bruijn–Newman flow**
supplies exactly one.

**The flow.** Deform $\xi$ by the backward-heat kernel:
$$H_t(z)=\int_0^\infty e^{tu^2}\,\Phi_{\mathrm{dBN}}(u)\,\cos(zu)\,du,\qquad H_0(z)\propto \xi(\tfrac12+\tfrac{iz}{2}),$$
with $\Phi_{\mathrm{dBN}}$ the standard super-exponentially decaying kernel. $H_t$ satisfies $\partial_t H_t=-\partial_{zz}H_t$.

**The facts (all theorems, none is RH):**
- $H_t$ has **only real zeros** for $t\ge\Lambda$ (de Bruijn–Newman). Classically $\Lambda\le\tfrac12$;
  **Polymath15** $\Lambda\le0.2$.
- $\Lambda\ge 0$ (**Rodgers–Tao, 2018**).
- $\mathrm{RH}\iff \Lambda\le 0 \iff \boxed{\Lambda=0}$ (combining with $\Lambda\ge0$).

> **The escape.** Reality at $t\ge\Lambda>0$ is a **theorem**, independent of RH. The remaining content,
> "propagate reality from $t=\Lambda$ back to $t=0$," is governed by the **zero dynamics** (an ODE), **not**
> by the explicit formula. A dynamical/Lyapunov argument that propagates reality therefore does **not** invoke
> the self-referential positivity. *The time parameter $t$ is the new degree of freedom the five-language map
> said we needed.*

**The honest catch (and why it is still worth it).** $\Lambda=0$ is **marginal** — propagation must hold all
the way to $t=0$ with no slack. That marginality is **exactly our measured saturation $C\equiv1$ (N3)**: RH is
true *with zero margin*. So the difficulty does not vanish; it **relocates** from a static positivity to a
**dynamical criticality** — a different question, possibly with a dynamical answer.

---

## 2. The zero dynamics, and the synthesis with our instrument (the novel part)

Under the flow the zeros $z_j(t)$ move as a **1-D Coulomb gas** (Calogero-type repulsion). For simple real
zeros $x_j(t)$,
$$\dot x_j \;=\; -2\sum_{k\ne j}\frac{1}{x_j-x_k}.$$
Increasing $t$ spreads them (smoothing, the "good" direction → all real at $t\ge\Lambda$); the danger is the
appearance of a complex conjugate pair as $t$ decreases. RH $\iff$ no such pair for $t>0$.

**Our band-limited Carleson constant is a local, computable functional of the zeros**, hence a function of
flow-time:
$$C(d,T_0;t)\;=\;\lambda_{\max}\big(P_F,A_\Phi\big)\ \text{evaluated on the zeros }\{z_j(t)\}.$$
- For $t\ge\Lambda$: $C(d,T_0;t)\le1$ is a **theorem** (real zeros ⟹ sine-kernel Gram is a contraction, P11 §3).
- RH $\iff$ $C(d,T_0;0)\le1$ for all $d,T_0$.
- The **new object** is $\dfrac{d}{dt}C(d,T_0;t)$ along the Coulomb flow — a **local Lyapunov candidate**.
  Our detector **measures it**; the $\delta^2$ law (B1) is precisely the transverse (off-line) response of
  $C$, i.e. the flow's unstable direction.

> **The Phase-8 thesis.** *Couple the Coulomb-gas zero dynamics to the Weil–Carleson detector and seek a
> local monotonicity/Lyapunov functional $\mathcal L(t)$ for the flow such that $\mathcal L$ certifies $C\le1$
> at $t=0$ given $C\le1$ at $t=\Lambda$. If $\mathcal L$ exists and its monotonicity is provable from the ODE
> alone, RH follows by backward propagation — without the self-referential positivity. The make-or-break is
> whether that monotonicity is provable or itself RH-equivalent — to be decided by computation and analysis,
> not assumed.*

**Why this is genuinely ours.** Rodgers–Tao proved $\Lambda\ge0$ with a **global** fluctuation lower bound.
The hard direction $\Lambda\le0$ is open. Our novelty is a **local, detector-coupled** attack on the hard
direction: $C(d,T_0;t)$ is local in height and computable, and B1 shows its second order **is** the
pair-correlation that controls the criticality. The heat-flow path and our B1 are the **same criticality**
seen dynamically vs. statically. (Rodgers–Tao used the lower side of fluctuations for $\Lambda\ge0$; RH/$\Lambda\le0$
needs the **upper** control of clustering — the pair-correlation upper side, which our sine-kernel form carries.)

---

## 3. The methodology (OpenAI-autonomous-proof style)

Mirroring the unit-distance effort: a **precise, self-contained statement**, an **autonomous iterated
attack**, **rigorous verification at every step**, and **mandatory self-refutation**.

- **Precise targets, stated as lemmas to prove or break** (no vague "progress"). The first:
  > **L8.1 (local Lyapunov).** *Along the de Bruijn–Newman flow, for $t\in[0,\Lambda]$ and every $(d,T_0)$,
  > $\frac{d}{dt}C(d,T_0;t)\ge 0$ (the Carleson constant is non-decreasing in $t$, i.e. non-increasing as we
  > approach $t=0$ it does not exceed its $t=\Lambda$ value of $\le1$).* — to be **proved from the Coulomb ODE**
  > or **broken** numerically.
- **Verification first.** Every claimed monotonicity/bound is checked numerically against **real zeta zeros**
  (via the engine) *before* being believed. Our permanent guard-rail (every blow-up/sign claim is checked
  against ground truth first) carries over.
- **Self-refutation mandatory.** Try to **break** each lemma before building on it. A false monotonicity must
  be caught at the computer, not in the write-up. ("Una falsa victoria sería peor que un fracaso.")
- **Honest logging.** Map, proof log, memory updated every step (the faithful bitácora).

**Decision gates (so we don't loop forever):**
- **Gate A (is L8.1 even true?):** numerically evolve real zeros under the Coulomb flow and measure
  $\frac{d}{dt}C$. If it has indefinite sign → L8.1 is false as stated; reformulate (a different $\mathcal L$)
  or stop. *(This is the first seed computation, §4.)*
- **Gate B (is the monotonicity provable from the ODE, or RH-equivalent?):** if L8.1 holds numerically,
  attempt the proof from the Coulomb ODE; if the proof needs an input equivalent to "no complex zeros," we
  have hit the wall again (sixth language) — log it honestly and reassess.
- **Gate C (uniformity):** even a local monotonicity must be **uniform in $T_0$** to close (the recurring
  uniform-passage wall). Test whether the detector-coupled bound is uniform or degrades with height.

---

## 4. First actionable computation (seed)

`experiments/heatflow_seed.py`:
1. Take the first $N$ real zeros; evolve them one small step under the Coulomb ODE $\dot x_j=-2\sum_{k\ne j}(x_j-x_k)^{-1}$,
   both directions ($\pm\Delta t$).
2. Recompute $C(d,T_0;t)$ with the band engine at each step → estimate $\frac{d}{dt}C$ (Gate A).
3. Inject a near-collision (Lehmer pair) and watch whether the backward step **births** a complex pair and
   drives $C>1$ — i.e. confirm the detector sees the flow's instability (calibration), and that the marginal
   $C\equiv1$ is the $\Lambda=0$ shadow.

Outcome of the seed decides whether L8.1 is the right Lyapunov candidate or must be replaced (e.g. by the
gas log-energy, or $\sum_j(\operatorname{Im}z_j)^2$, or a relative-entropy functional of the empirical zero
measure vs. the equilibrium GUE density).

---

## 5. Honest expectations

- **Odds:** <5%. $\Lambda=0$'s marginality means any Lyapunov inequality is razor-thin; it may be
  RH-equivalent (Gate B failure). But the **attack surface is new** (dynamical, time-parametrized), has a
  **non-self-referential ingredient** (reality at $t\ge\Lambda$ is a theorem), **uses our validated assets**,
  and aligns with the **deepest modern work** (Rodgers–Tao, Polymath15).
- **Even if it does not cross:** a local, detector-coupled Lyapunov analysis of the de Bruijn–Newman flow is a
  **publishable** contribution (it would quantify the criticality $\Lambda=0$ locally), and a clean Gate-B
  wall would be the **sixth language** — sharpening the map further.
- **What would make it cross:** an $\mathcal L(t)$ whose monotonicity follows from the **ODE structure alone**
  (Coulomb repulsion + the kernel's positivity), independent of where the zeros are. That is the new
  mathematics to invent — a Lyapunov theory for the Weil–Carleson constant under the heat flow.

---

### Status / next
- Phase-8 designed; the escape mechanism (time parameter; $t\ge\Lambda$ reality is a theorem) identified.
- NEXT: the seed computation (Gate A) — measure $\frac{d}{dt}C$ along the Coulomb flow on real zeros.
- Then: if Gate A passes, attempt L8.1 from the ODE (Gate B); always check uniformity (Gate C).
- Bitácora: this file + proof log Day-25 + map + memory.
