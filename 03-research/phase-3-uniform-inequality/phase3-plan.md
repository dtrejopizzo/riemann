# Phase 3 — The Structural Assault on the Uniform Inequality

**Status:** research frontier. This is the only phase that could, in principle, touch RH; it is
also where every prior program has stopped. The honest deliverable is a *sharp reduction* and a
verdict on whether a structural positivity makes the target inequality manifest — **not** a
proof. Everything below marked ⚑ needs verification by a working analytic number theorist /
operator theorist before it is trusted.

---

## 0. What the RHx programs handed us, stated exactly

They reduced the program to a single inequality. Recall the localized Weil quadratic form
$Q=Q(T_0,\sigma,J)=M_{\text{zeros}}-M_{\text{arith}}$ on the Hermite–Gauss basis, with prime
cutoff $X$ giving $Q_X$ and the complete arithmetic side giving $Q_\infty$. v8 proved:

- **(A) Forced negativity** — an off-critical zero forces $\lambda_{\min}(Q)<0$ with explicit
  $\delta^2$ constants. *(Unconditional.)*
- **(B) Truncation** — $\eta(X)=\|Q_X-Q_\infty\|$-type residual $\le A e^{-\alpha(\log X)^2}$,
  from Hermite–Gauss decay + PNT. *(Unconditional.)*
- **(C) Verdict** — the lemma needed to **detect a fixed zero** is technical; the lemma needed
  to **prove RH** is:

> **(LB) The uniform positivity limit.** For every admissible test function $f$ (every
> localization $(T_0,\sigma)$ and the basis completion $J\to\infty$),
> $\lambda_{\min}\big(Q_\infty(f)\big)\ge 0$ — equivalently the Weil functional $B\succeq0$ on
> the whole admissible class. This is **RH**.

**The precise gap.** For a *fixed* $f$, $\lambda_{\min}(Q_X)\to\lambda_{\min}(Q_\infty)$ as
$X\to\infty$ by (B) + eigenvalue continuity — that is controlled. What is **not** controlled is
the passage to positivity **uniformly over all $f$ and as $J\to\infty$**: the limit
$\lambda_{\min}(Q_\infty(f))$ could dip below $0$ for some $f$ exactly when an off-critical zero
exists (by (A)). So (LB) is the statement that *no admissible $f$ ever sees negativity in the
limit* — and that is RH. Phase 3 asks: **is there a structural reason (LB) must hold?**

---

## 1. Why finite computation cannot reach (LB) (and what can)

By (A), negativity is *real* in the limit when a zero is off the line; no amount of finite-$X$
or finite-$J$ control removes it. So (LB) cannot be reduced to a truncation estimate — it must
come from a property of the **arithmetic side** that forces $\lambda_{\min}(Q_\infty)\ge0$
independently of the (unknown) zero locations. There are exactly two known places such a
property could live, and both are positivity statements in disguise:

- a **trace / reflection positivity** (Connes): $B(f,f)=\mathrm{Tr}\,\pi(f)\pi(f)^*\ge0$ for a
  unitary representation $\pi$ — manifestly $\ge0$ if the right Hilbert space exists;
- a **monotonicity of a canonical system** (de Branges): $B\succeq0$ iff a structure function
  $E$ has its zeros in one half-plane, controlled by a chain (ordering) condition.

Phase 3 is the attempt to realize one of these for our *localized* $Q$.

---

## 2. Flank I — Connes (the trace / basis-restriction route) ⚑

**Goal:** write $Q_\infty(f)$ as a compression of the Weil trace operator and ask whether its
positivity survives the restriction to the Hermite–Gauss span.

**2.1 The dictionary.** In Connes' spectral realization \[Connes 1999\], the Weil explicit
formula is a trace over the adèle class space $\mathbb{A}_\mathbb{Q}/\mathbb{Q}^\times$; the
zeros appear as an *absorption* spectrum and $B(f,f)$ is (formally) $\ge0$ *because* it is a
trace of $\pi(f)\pi(f)^*$. The obstruction Connes identified is that the relevant operator is
**not** manifestly positive without the correct Sobolev/weighted space — the positivity is
exactly the hard point, equivalent to RH.

**2.2 The new, sharp sub-question.** Our $Q$ is the compression of this trace to
$\mathrm{span}\{\varphi_j\}$. v8's empirical finding (Front C) — that the *truncation* is
controlled by basis Fourier decay alone — suggests the conjecture:

> ⚑ **(Connes–stability conjecture).** The compression $P_J\,\mathcal{T}\,P_J$ of the Weil
> trace operator $\mathcal{T}$ to the Hermite–Gauss projection $P_J$ converges to $\mathcal{T}$
> in a sense strong enough that $\lambda_{\min}(P_J\mathcal{T}P_J)\to\inf\mathrm{spec}\,\mathcal{T}$
> **uniformly in the localization**.

If true, (LB) reduces to $\inf\mathrm{spec}\,\mathcal{T}\ge0$ — i.e. to the *spectral
positivity of one operator*, which is Connes' formulation of RH. This does **not** prove RH,
but it would convert (LB) into a single operator-positivity question with an explicit
finite-dimensional approximation (our $Q$) — a genuinely new, testable bridge.

**2.3 What to do / what an expert must check.**
- ⚑ Verify the compression identity $Q=P_J\mathcal{T}P_J$ rigorously (sign conventions,
  domains). This is the crux of Phase 0.A.2 and must be done by someone fluent in \[Connes 1999\].
- Test the stability conjecture *numerically* with our instrument: does
  $\lambda_{\min}(Q(T_0,\sigma,J))$ stabilize in $J$ uniformly across $T_0$ for the GRH controls?
  (This is a clean, cheap experiment our engine can run.)
- If stability holds empirically, the open lemma is named even more sharply; if it fails,
  Connes' route does not give *uniform* control and we learn that too.

---

## 3. Flank II — de Branges (the canonical-system / chain route) ⚑

**Goal:** identify the de Branges space generated by our localized kernels and read (LB) as a
chain (monotonicity) condition.

**3.1 The dictionary.** A Hermite–Gauss localized family is a family of **reproducing kernels**.
By the de Branges theory \[de Branges 1968\], such kernels generate a space $H(E)$ of entire
functions with a structure function $E=E(z)$; positivity of the associated quadratic form is
equivalent to $E$ being **Hermite–Biehler** (all zeros in the closed lower half-plane) and to a
*monotone chain* of nested subspaces $H(E_t)$, $t$ increasing.

**3.2 The new, sharp sub-question.**

> ⚑ **(de Branges–chain conjecture).** The structure function $E$ attached to the
> $\zeta$-localized kernels satisfies the de Branges chain (ordering) condition; equivalently,
> the family $\{H(E_t)\}$ is totally ordered by inclusion.

The chain condition is *exactly* the de Branges reformulation of RH for $\zeta$ \[de Branges'
program; Conrey–Li caveats below\]. The value of routing through *our localized $Q$* is that the
chain condition becomes a **monotonicity of $\lambda_{\min}(Q(T_0,\sigma,J))$ in the
localization parameters** — a quantity our engine computes directly.

**3.3 Caveat (mandatory honesty).** de Branges' own attempted proof has known gaps; **Conrey–Li
(2000)** exhibited a structural obstruction (a positivity that the proposed spaces do not have).
Any de Branges-flank work must be checked against that obstruction first — ⚑ an expert must
confirm our localized chain does not fall into the Conrey–Li counterexample class before any
effort is invested.

**3.4 What to do.**
- ⚑ Identify $E(z)$ for the Hermite–Gauss localized kernels explicitly (Phase 0.A.3).
- Test the chain monotonicity numerically: is $\lambda_{\min}(Q)$ monotone in $\sigma$ / in the
  nesting of windows for the GRH controls? (Cheap experiment.)
- Compare against the Conrey–Li obstruction.

---

## 4. Flank III — the function-field template (orientation only)

RH is *proven* for curves over $\mathbb{F}_q$ via **positivity of the intersection form**
(Hodge index / Castelnuovo–Severi). The dictionary entry we want is:

> ⚑ what is the arithmetic analogue of "the intersection form is negative-definite on the
> primitive cohomology" that would correspond to (LB)?

This is the Connes–Consani $\mathbb{F}_1$ program's target. We use it only for *orientation*:
it tells us (LB) should be the shadow of a **definite intersection pairing**, which is more
naturally a Connes (trace) object than a de Branges (chain) object — a weak reason to weight
Flank I over Flank II.

---

## 5. The realistic plan and its honest ceiling

**Sequence.**
1. **0.A.2 / 0.A.3 (now):** rigorously establish the two dictionaries — $Q$ as a Connes
   compression, and $E(z)$ as a de Branges structure function. ⚑ expert-verified. *These are
   publishable expository contributions on their own, independent of RH.*
2. **Cheap experiments (now):** use our engine to test the two stability/monotonicity
   conjectures (§2.3, §3.4) on the GRH controls. A clean positive signal sharpens the open
   lemma; a negative signal kills a flank. Either is valuable.
3. **The frontal attempt (open-ended):** whichever flank survives, attempt (LB) as the
   corresponding structural positivity. This is genuine open research and may not close.

**Tiered outcomes (honest).**
- **Realistic:** a sharp, expert-verified reduction of (LB) to *one* operator-positivity
  (Connes) or *one* chain condition (de Branges), with our instrument as the finite-dimensional
  probe — a real contribution to how RH is approached, publishable, RH still open.
- **Strong (low probability):** prove the stability/monotonicity that reduces (LB) to a *known*
  positivity, narrowing the gap to a single classical statement.
- **Dream (very low probability, honestly pursued):** establish the structural positivity → a
  proof, or the last step before one.

**The ceiling, stated plainly.** (LB) **is** RH. No reduction below removes that; the best
Phase 3 can do is convert RH into the single most structurally natural positivity and hand a
working specialist an explicit finite-dimensional ladder ($Q(T_0,\sigma,J)$) climbing toward
it. That is the maximal honest aim — and it requires the community step of PLAN §Phase 4: this
will not be finished by a closed AI+cloud loop.

---

## 6. Immediate, dependency-free actions

1. ⚑ Draft `0A2-connes-compression.md` — $Q=P_J\mathcal{T}P_J$ with the explicit Weil-trace
   operator and the compression, flagged for expert review.
2. ⚑ Draft `0A3-debranges-structure-function.md` — identify $E(z)$ for the localized kernels;
   check against Conrey–Li.
3. Spec a small Lise Science run ("v9 stability probe"): does $\lambda_{\min}(Q)$ stabilize in $J$
   uniformly in $T_0$ (Connes-stability) and behave monotonically in $\sigma$/window nesting
   (de Branges-chain) for ζ, L(χ), L(Δ)? Self-contained, reuses the v8 engine.

**References to pin:** Connes (1999); de Branges, *Hilbert Spaces of Entire Functions* (1968);
Conrey–Li, *A note on the de Branges spaces and the Riemann hypothesis* (2000); Bombieri,
*Remarks on Weil's quadratic functional*; Connes–Consani, Riemann–Roch for $\mathbb{Z}$ (2024).
