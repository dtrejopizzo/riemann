# Phase 4 — Pure-Mathematics Work Program: The Faithfulness of the Localized Weil Form

**For:** the pure-mathematics team.
**Prepared by:** D. A. Trejo Pizzo (with the program's computational record).
**Date:** 2026-06.

This document states, self-contained and precisely, the one mathematical question to which the
entire computational program has reduced, and decomposes it into a dependency-ordered list of
problems a pure-math team can attack. It is deliberately honest about logical strength: it
distinguishes what is *proven*, what is *empirically supported*, and what is *open theory*.

> **The single instruction that governs everything.** Do **not** attempt to prove
> $\inf\operatorname{spec}(\mathcal T)\ge0$ directly — that is the Riemann Hypothesis. The target of
> this program is **faithfulness**, which is logically *weaker* than RH and is RH-independent.
> If faithfulness is established, RH is reduced to the **sign of the limit of a rigorously
> convergent finite-dimensional approximation scheme**. That is the achievable goal; the sign
> itself is not.
>
> **A caution we keep in front of us:** $\text{faithfulness}\ne\text{effective decidability}$.
> Even with A$\wedge$B$\wedge$C, the convergence $\lambda_{\min}(Q_J)\to\inf\operatorname{spec}(\mathcal T)$
> carries **no a-priori rate**: the sequence could approach $0$ so slowly that deciding its sign is
> exactly as hard as RH. We therefore sell the outcome as a *new faithful approximation scheme*,
> **not** as "RH becomes computable." Attaching the word *computable* to the limit without an
> effective error bound is the one overclaim this document forbids.

---

## 1. Setup (self-contained)

### 1.1 The Weil functional and the criterion
For an even Schwartz test function $g$ with transform $h=\hat g$, the Riemann–Weil explicit formula
reads
$$
\sum_{\rho} h(\gamma_\rho)
= h(\tfrac i2)+h(-\tfrac i2)
+ \frac1{2\pi}\!\int_{\mathbb R} h(r)\,\Omega(r)\,dr
- 2\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,g(\log n),
\qquad \Omega(r)=\re\psi(\tfrac14+\tfrac{ir}2)-\log\pi,
$$
the sum over non-trivial zeros $\rho=\tfrac12+i\gamma_\rho$. The **Weil functional** is the
Hermitian form $B(f_1,f_2)$ obtained by applying either side to $f_1\star\tilde f_2$
($\tilde f(x)=\overline{f(-x)}$). **Weil's criterion:** $\mathrm{RH}\iff B\succeq0$ on the admissible
class.

### 1.2 The localized form
On a Hermite–Gauss basis $\{\varphi_j\}_{j<J}$ centered at height $T_0$, width $\sigma$, define the
finite Gram matrix of $B$:
$$
\boxed{\,Q(T_0,\sigma,J)=M_{\mathrm{zeros}}-M_{\mathrm{arith}}\,},\qquad
(M_{\mathrm{zeros}})_{jk}=\sum_\rho\varphi_j(\gamma_\rho)\overline{\varphi_k(\gamma_\rho)},
$$
$M_{\mathrm{arith}}$ assembling the prime-power sum (cutoff $X$), the archimedean term, and the
polar term. The closed-form Fourier transform of the basis products is
$g(u)=e^{-iT_0u}e^{-\sigma^2u^2/4}L_{J-1}^{(1)}(\sigma^2u^2/2)/2\pi$ (associated Laguerre).

### 1.3 The Connes operator
Connes (1999) realizes $B$ as a trace: there is a regularized Hilbert space $\mathcal H=L^2_\delta(X)$
on the adèle class space $X=\mathbb A_{\mathbb Q}/\mathbb Q^\times$, and a densely defined
(formally self-adjoint) operator $\mathcal T$ whose quadratic form is $B$, with
$$
\mathrm{RH}\iff \mathcal T\succeq0\iff \inf\operatorname{spec}(\mathcal T)\ge0.
$$

---

## 2. What is already PROVEN (P7) — the rigorous foundation

These are unconditional theorems (computational record + rigorous proof). The team may treat them
as established.

**(P7-A) Forced negativity, explicit constants.** Writing $Q=Q_0+P$ with $Q_0$ the on-line (PSD)
form and $P$ the perturbation from an off-line quartet at displacement $\delta$ near $T_0$, a
Taylor expansion gives a rank-$\le2$ contribution $A(\gamma)$ and Courant–Fischer yields
$$
\lambda_{\min}(Q)\le\lambda_{\min}(Q_0)-c(\delta,\sigma,J;\gamma),\qquad c=a(\gamma)\delta^2+O(\delta^3),\ \ a(\gamma)=-\lambda_{\min}(A(\gamma))>0,
$$
with the $\delta^2$ law and prefactor matched numerically to $<10^{-5}$.

**(P7-B) Unconditional truncation bound.** With $\|g(u)\|_{\mathrm{op}}\le P_{2J}(u)e^{-\sigma^2u^2/4}$,
$$
\eta(X)\le\frac2\pi\int_{\log X}^\infty e^{u/2}\|g(u)\|_{\mathrm{op}}\,du\le A\,e^{-\alpha(\log X)^2},\quad \alpha=\tfrac{\sigma^2}8+o(1),
$$
**from the Prime Number Theorem alone** — no zero-density or GRH input.

**(P7-C) The dichotomy.** Detecting a *fixed* off-critical zero is technical/unconditional; the
*uniform* passage $\lambda_{\min}(Q_X)\to\lambda_{\min}(Q_\infty)$ over all $f$ is equivalent to RH.

---

## 3. The reduction and the empirical state

### 3.1 The named inequality
Modulo P7, $\mathrm{RH}\iff$ **(LB)** $\inf\operatorname{spec}(\mathcal T)\ge0$ — *provided* $Q$ is a
faithful compression of $\mathcal T$ (Section 4). The faithfulness is the prior question.

### 3.2 What the numerics established (and did not)
A stability probe (Lise Science run 9) returned, on the GRH-respecting controls $\zeta$, $L(\chi_4\bmod5)$,
$L(\Delta,s)$:
- the explicit-formula trace identity $\tr(M_{\mathrm{zeros}})=\tr(M_{\mathrm{arith}})$ to
  $10^{-27}$–$10^{-43}$ (the engine computes the **form** $B$ faithfully);
- **uniform-in-$T_0$ stability** of $\lambda_{\min}(Q)$ as $J\to\infty$ (the sharpest empirical
  falsifier of faithfulness **did not fire**);
- **monotonicity** in $\sigma$ and under nested windows, with **no Conrey–Li obstruction** present;
- small-$\sigma$ negativity is a **truncation** artifact, not spectral structure (it grows with the
  cutoff $X$), so the localization injects no spurious geometry.

**Honest ceiling.** These are GRH controls, where $\lambda_{\min}\approx0$ trivially; the numerics
are a *weak confirmer* of faithfulness, not a proof. The implication is **one-way**: faithfulness
$\Rightarrow$ the observed stability, but the observed stability $\not\Rightarrow$ faithfulness
(spectral pollution can produce clean finite numerics). The theoretical core is untouched and is
this document's subject.

### 3.3 Logical status of Problem B — *and why P7-A supports its independence from RH*
The external referee's first hard question is: **is B genuinely independent of RH, or does it secretly
require it?** B splits into two claims of very different status.

- **B-1 (self-adjoint realization exists).** The operator underlying $B$ is symmetric and commutes
  with the natural conjugation $f\mapsto\tilde f$ (time reversal; the explicit formula is real). By von
  Neumann's theorem, a commuting conjugation forces **equal deficiency indices** $n_+=n_-$, so
  self-adjoint extensions exist **unconditionally**. This matches Connes: the Hilbert space and action
  are built without assuming RH; only positivity is withheld. B-1 lives on the easy side.

- **B-2 (the realization is bounded below by a finite constant).** Via Friedrichs, this is equivalent
  to **semiboundedness of the form** $B$. The logical ladder is
  $$
  \underbrace{\mathrm{RH}}_{B\succeq0,\ \inf=0}\ \Longrightarrow\
  \underbrace{B\ \text{semibounded by }C<0}_{\inf\operatorname{spec}=C\in(-\infty,0)}\ \Longrightarrow\
  \underbrace{B\ \text{not semibounded}}_{\inf\operatorname{spec}=-\infty},
  $$
  each implication strict. There is an **entire interval** $C\in(-\infty,0)$ of worlds where *"B holds,
  RH fails."* For B to collapse into RH one would need a **spectral dichotomy** — "bounded below
  $\Rightarrow$ bounded below by $0$" — i.e. the spectrum cannot dip into $(C,0)$ without diving to
  $-\infty$.

**P7-A is internal evidence against that dichotomy.** The forced-negativity theorem shows an off-line
quartet at displacement $\delta$ produces a **finite** dip $\sim -a(\gamma)\delta^2$, not a collapse:
the negativity mechanism is *finite per zero*. That is exactly the behavior expected if "bounded below"
is **strictly weaker** than "$\succeq0$" — our own proven asset suggests the separation B $\not\Rightarrow$
RH is real.

**Where the resistance is predicted to appear (the honest caveat).** P7-A controls *one* quartet; the
full form sums over *all* off-line zeros. If RH failed with positive proportion off the line, the finite
dips could **accumulate** to $-\infty$, and whether they do is governed by the **density** of off-line
zeros. Hence the realistic outcome is not collapse but conditionality:
$$
\boxed{\text{B-2 is conjectured provable \emph{modulo a zero-density hypothesis} — weaker than RH, but not unconditional.}}
$$
This is the same "PNT / zero-density level" already seen in P7-B. If confirmed, Phase 4's deliverable
on this flank is sharper than "B is unconditional": it would **locate B in the zero-density tier** of
the hierarchy, strictly between the unconditional and RH — a *quantitative* form of the logical
separation. The worst case ("every bounded-below realization forces positivity") would itself be a
first-order theorem: it would pin the obstacle of RH inside the operator's extension/semiboundedness
theory. Either way, B is the right place to dig.

**Refinement (proof Day 1) — the entanglement is in the *norm*, and it fuses B with D.** Working the
form explicitly shows the prime functional is **not** a pointwise multiplier (the prime measure is
non-tempered) and, more decisively, that an off-line zero's contribution involves **point-evaluations
of $\widehat g$ off the real axis**, which are **unbounded on $L^2(\mathbb R,du)$**. Hence semiboundedness
is *ill-posed in the naive norm* — with $L^2$ it plausibly collapses back to RH. The genuine-weakening
branch exists only in a **weighted reproducing-kernel (de Branges) space $H(E)$** where strip
evaluations are bounded. So the regularization is innocent for the algebraic identity (A) but **the
norm/weight is a genuine, decisive choice for B** — and constructing that weight *is* Problem D step (i).
**Operational consequence: merge the B and D sub-teams; they are one problem.**

**Consolidation (proof Day 2).** Pursuing the de Branges norm produced three rigorous facts and one
reduction. (i) The free part is the Gamma-factor geometry: $\Omega(r)=2\,\mathrm{Re}(\gamma'/\gamma)(\tfrac12+ir)$.
(ii) A **width-$\tfrac12$ triple coincidence**: the admissible strip (from the pole), the off-line
displacement range $|\beta-\tfrac12|<\tfrac12$, and the first pole of $\gamma(\tfrac12+iz)$ at $z=i/2$ are
the *same* strip. (iii) In a de Branges space $H(E)$ point-evaluations are bounded everywhere, so the
$L^2$ pathology dissolves. The reduction: semiboundedness is **norm-dependent**, no single $E$ both bounds
evaluations and reproduces the Weil energy, so the right object is the de Branges **chain**, and
$$
\boxed{\ \text{B-2}\ \rightsquigarrow\ \text{a natural problem in a de Branges chain for }E_{T_0,\sigma}\ }
$$
— a **suggestive reduction, not an equivalence** (downgraded Day 3 from `≡`; upgrading needs canonicity of
$H(E)$, preservation of the Weil spectral bottom, and semiboundedness$\iff$ordering, none yet proven). The
logically prior question is **closability** of the Weil form in $H(E)$, which reduces to one
distribution-free inequality (an $H(E)$-relative KLMN bound on the prime form), *gated by* the archimedean
de Branges weight asymptotic (logarithmic vs exponential — currently unverified). A guard-rail holds
throughout: **sign/value invariance** — "$\inf\operatorname{spec}\ge0$" $=$ RH is norm-independent, so no
choice of norm can hide or fabricate RH; only the *finiteness* of the bottom (B-2) is norm-dependent, and
closability is exactly what makes the sign survive completion. *(Derivations:
`proofs/B2.4a-de-branges-norm.md`, `proofs/B2.4a-closability.md`.)*

**Break attempt + retraction (proof Days 4–5) — the de Branges space survives; a self-caught error.**
Day 4 *claimed* to break the de Branges reduction (a width-driven $\sqrt N$ prime "blow-up" making
$\mathfrak t$ non-semibounded in $H(E_\gamma)$, redirecting to a Fock/Bargmann norm). **Day 5 retracts
that claim as false.** Making the argument rigorous exposed an illegitimate **hard cutoff** of a
conditionally-convergent prime series — the same error already latent in the Day-0 KLMN reasoning. The
**explicit-formula identity** $\mathfrak t(g,g)=\sum_\rho|\widehat g(\gamma_\rho)|^2$ shows the form is
*finite and bounded* for smooth test functions at generic $T_0$ (the prime series resums to the finite
$2\,\mathrm{Re}(-\zeta'/\zeta(\tfrac12+iT_0))$); there is no prime blow-up. **Consequence:** the
Fock/chain detours were chasing an artifact; the archimedean de Branges space $H(E_\gamma)$ is back in
play. The *only* rigorous unboundedness mechanism is the Day-1 one (off-axis evaluation from off-line
zeros), which $H(E_\gamma)$ **bounds** (DB.3). So B-2 reduces, cleanly, to: *is the off-line-zero sum
bounded below in $H(E_\gamma)$?* — a **zero-density question, i.e. exactly §3.3's original conjecture**,
now reached without phantoms. **Permanent guard-rail adopted:** any blow-up claim must be checked against
the explicit-formula identity before being believed. *(Derivation + retraction: `proofs/B2.4a-break-attempt.md` §5.)*

**Audit of the new pillar (proof Day 6).** Because the retraction put all weight on the explicit-formula
identity $\mathfrak t(g,g)=\sum_\rho h(\gamma_\rho)$ ($h=\widehat g\,\widehat g^*$), it was audited hard.
It **survives — unconditionally on the dense core** ($C_c^\infty$ and $\mathcal D$) — but two statements
were corrected: (i) the RHS is **indefinite, not a sum of squares** — on-line zeros give
$|\widehat g(\gamma)|^2\ge0$, off-line quartets give $4\,\mathrm{Re}[\widehat g(t-ib)^2]$, and positivity
$\iff$ RH (so "$\sum|\widehat g(\gamma_\rho)|^2$" is RH-only shorthand); (ii) validity is **core-level** —
whether the identity and the sign survive **closure in $H(E_\gamma)$ is open** (a dense-core identity need
not control the closure). This is the **first formulation in the Day 0–6 sequence to survive a deliberate
hard audit without retraction**; the single open analytic crux is now stable: *does EF-id survive closure
in $H(E_\gamma)$, and is the off-line-zero sum bounded below there?* *(Audit: `proofs/EF-identity-audit.md`.)*

---

## 4. The faithfulness question, decomposed into problems

"$Q$ is a faithful compression of $\mathcal T$" is **two** claims of different difficulty. Attack in
dependency order.

### Problem A — the algebraic compression identity (Part I) ⚑
$$
Q(T_0,\sigma,J)=P_J\,\mathcal T\,P_J,\qquad P_J=\text{orth. projection onto }\operatorname{span}\{U(\varphi_j)\}.
$$
**Task.** Verify, at the level of matrix entries and domains, that
$B(\varphi_j,\varphi_k)=\langle\varphi_j,\mathcal T\varphi_k\rangle_{\mathcal H}$: the $\varphi_j$
lie in the form domain of $\mathcal T$; the regularization $\delta$ is the one making the explicit
formula the trace; the sign convention of $M_{\mathrm{zeros}}-M_{\mathrm{arith}}$ matches $\mathcal T$.
**Status.** Laborious but, in principle, decidable. The form-level computation is supported by the
trace-identity closure (§3.2). **Nearest tools:** Connes (1999) §§ on the trace formula; Bombieri,
*Remarks on Weil's quadratic functional*; Connes–Consani, *Riemann–Roch for $\mathbb Z$* (2024).
**Caveat.** Part A validates the *form*; the existence of the *operator* $\mathcal T$ as a genuine
self-adjoint operator is Problem B.

### Problem B — the entanglement (Part II-a): a realization without positivity ⚑⚑ (THE CRUX)
**Task.** Establish a **self-adjoint, bounded-below** realization of $\mathcal T$ on $\mathcal H$ —
bounded below by *any* constant, possibly negative — **without assuming positivity (RH).**
**Why this is the crux.** By the min-max principle, *if* $\mathcal T$ is self-adjoint, bounded below,
and the localized family is form-complete (Problem C), then
$\lambda_{\min}(P_J\mathcal T P_J)\downarrow\inf\operatorname{spec}(\mathcal T)$ — faithfulness for the
bottom eigenvalue. The danger is **entanglement**: the regularization that yields a good realization
might itself require positivity. The yes/no question is:
$$
\boxed{\text{Can a self-adjoint, bounded-below realization of }\mathcal T\text{ be built without assuming }\mathcal T\succeq0\,?}
$$
- **Yes** $\Rightarrow$ (with Problem C) a *faithful spectral reformulation*:
  $\mathrm{RH}\iff\operatorname{sign}\big(\inf_{T_0,\sigma}\lim_J\lambda_{\min}(Q)\big)\ge0$ — RH as the
  sign of the limit of a **rigorously convergent finite-dimensional ladder**. **This is the program's
  dream outcome, and it is RH-independent.** (Recall the preamble caution: faithful convergence is not
  an *effective* sign test unless a rate is also proven.)
- **No** (the realization needs positivity) $\Rightarrow$ RH's difficulty lives exactly here, in its
  strongest form, and we have located it precisely.
**Nearest tools:** Connes' regularized $L^2_\delta(X)$; Burnol's Hilbert-space completions; Suzuki's
work on the Weil/Connes operator; the self-adjoint extension theory of symmetric operators
(von Neumann deficiency indices).

### Problem C — form-completeness and no spectral pollution (Part II-b) ⚑⚑
**Task.** Prove the Hermite–Gauss family $\{U(\varphi_j)\}$ is **form-complete** for $\mathcal T$ and
that the bottom-eigenvalue convergence is **pollution-free** (norm-resolvent, not merely strong).
**Status.** The numerics (§3.2: uniform-in-$T_0$ stability, monotone saturation) are *evidence* for
pollution-free behavior on GRH controls, but not a proof — pollution can hide in the limit.
**Nearest tools:** spectral approximation theory — Lewin–Séré, *Spectral pollution and how to avoid
it* (2010); A. C. Hansen, *On the approximation of spectra of linear operators* (2008); Davies–Plum,
*Spectral pollution* (2004); the min-max / Rayleigh–Ritz principle.

### Problem D — the de Branges flank (alternative route) ⚑
v9 found **no Conrey–Li obstruction** empirically; this re-opens the de Branges route, which was
otherwise blocked. **Task.** (i) Identify the structure function $E=E_{T_0,\sigma}(z)$ for which the
localized Hermite–Gauss kernels are the reproducing kernels (Hermite–Biehler class). (ii) Express
(LB) as the **chain (ordering) condition** on $E$. (iii) **Confirm theoretically** that the
localized chain avoids the Conrey–Li counterexample class (the empirical absence in §3.2 is
suggestive, not decisive). **Nearest tools:** de Branges, *Hilbert Spaces of Entire Functions*
(1968); Lagarias, Hilbert-space/$L$-function work; Conrey–Li (2000) for the obstruction.

---

## 5. The dependency graph and the payoff

```
   Problem A (compression identity)  ──┐
                                       ├──►  if A ∧ B ∧ C :  Q faithfully tracks inf spec(𝒯)
   Problem B (realization, no posit.) ─┤        ⇒  RH ⟺ sign of a rigorously convergent ladder
   Problem C (form-complete, no poll.)─┘            (a genuine new reformulation, RH-independent)

   Problem D (de Branges chain)  ──────►  independent route: (LB) ⟺ chain condition on E(z)
```

- **Realistic strong outcome (the achievable target):** establish A ∧ B ∧ C $\Rightarrow$ a faithful
  spectral reformulation. RH still open, but reduced to the sign of the limit of a convergent
  *explicit finite-dimensional ladder* — a reformulation in the lineage of Li, Nyman–Beurling, Weil,
  de Branges. The distinguishing feature is the explicit ladder; the honest claim is **faithful
  convergence**, not effective decidability (preamble caution).
- **Either flank's structural positivity** (Problem B's realization made positive, or Problem D's
  chain proved) would touch RH itself — very low probability, but this is where it would come from.

---

## 6. The outcome ladder — what counts as success *without* RH

The point of Phase 4 is not binary (RH / not-RH). There is a graded scale of genuinely valuable
outcomes, **all of which leave RH open**. The team should know which rung it is aiming at.

| Rung | What is established | External reading | Impact |
|---|---|---|---|
| **A only** | the algebraic compression identity $Q=P_J\mathcal T P_J$ | "the detector provably computes the Weil form" | moderate |
| **A ∧ B** | + a self-adjoint bounded-below realization of $\mathcal T$, no positivity assumed | "the Weil/Connes operator exists as a genuine bounded-below self-adjoint operator" | strong |
| **A ∧ B ∧ C** | + form-completeness, pollution-free | "**the localized ladder converges, rigorously, to the Weil/Connes spectral criterion**" | very strong |
| **A ∧ B ∧ C ∧ D** | + the de Branges chain appears naturally | "two independent structures — Weil/Connes and de Branges — point at the same object" | exceptional |
| **+ structural positivity** | the realization or chain *forces* $\succeq0$ | RH itself | historic |

**The category shift at rung A∧B∧C.** This is the realistic target. It moves the project from
> *"an interesting numerical experiment"*

to
> *"a rigorous spectral reformulation + a computable approximation + proven convergence."*

That is a different *kind* of object, and it is publishable on its own terms — exactly the lineage of
Nyman–Beurling, Li, Connes, de Branges, Montgomery: **none resolved RH, all are permanent
references**, valued for the tools they built, not for settling the conjecture.

**Where the difficulty goes after A∧B∧C.** Paradoxically, once the ladder is faithful the central
problem stops being computational and becomes a single, classical, clearly-isolated question of
spectral theory:
$$
\inf\operatorname{spec}(\mathcal T)\ge0\,?
$$
That isolation — the difficulty of RH concentrated in *one* identified operator-theoretic statement
rather than dispersed across truncations, localizations, numerical controls and faithfulness doubts —
is itself the conceptual prize of Phase 4, independent of whether the sign is ever decided.

> **D is a status change, not a probability change.** v9 did not make the de Branges route *likely*;
> it removed a strong reason to *discard* it (no Conrey–Li obstruction in the localized regime). Read
> D as "now a legitimate line of inquiry," not as "now expected to work."

---

## 7. Suggested first moves and resource allocation

A defensible split of pure-math effort, given that B is where a *new* conceptual result can appear
even with RH fully open, and A is the most decidable (and most credibility-building) target:

| Effort | Problem | Rationale |
|---|---|---|
| **50%** | **B + D fused** (realization in the right norm) | the crux; Day-1 showed B-2 is well-posed *only* in a de Branges space $H(E)$, so D step (i) = constructing that norm is now **on B's critical path**, not an alternative route |
| **30%** | **A** (compression identity) | most decidable; a rigorous proof of A sharply raises external credibility |
| **15%** | **C** (no pollution) | apply standard pollution criteria *before* attempting a completeness proof |
| **5%**  | **D** (chain condition, the *positivity* half) | the de Branges chain/Conrey–Li question proper; lower priority than the norm-construction half folded into B |

> **Update (Day 1):** the original "split A vs D across sub-teams" is superseded for the *norm-construction*
> part of D, which now belongs with B. What remains separable in D is the chain/ordering (positivity)
> question — keep that at low priority.

Concrete first steps:

1. **Pin the regularization in A first.** The entire faithfulness chain hinges on *which* $\mathcal H$
   and $\delta$ make $Q=P_J\mathcal T P_J$ hold. Settle this before anything else; B and C inherit it.
2. **State Problem B as a deficiency-index question.** Recast "self-adjoint bounded-below realization
   without positivity" as a concrete self-adjoint-extension / lower-bound problem for the symmetric
   operator underlying $B$, and ask whether the lower bound is obtainable from the archimedean + prime
   structure alone (PNT-level), echoing P7-B.
3. **For C, run the pollution checklist** (Lewin–Séré criteria) against the localized family before
   investing in a completeness proof. C is where specialists will attack first — a non-compact,
   form-defined, regularized operator approximated by finite compressions is a textbook pollution
   risk, so the separation of B (existence) from C (spectral fidelity) must stay clean.
4. **Split A vs D across sub-teams** — they are largely independent.

## 8. What the team should ask the computational side for
The instrument can be re-pointed cheaply. Useful next experiments (a "v10"), to *inform* B and C:
- the **off-line amplification** as a faithfulness probe: for $\zeta_\delta$, does
  $\lambda_{\min}(Q(\cdot,\cdot,J))$ track a genuine spectral feature of the perturbed operator, or
  is the $J$-amplification pollution? (The sharp Part-II test v9 did not run.)
- norm-resolvent vs strong convergence diagnostics for the compression (Problem C).
- explicit numerical $E_{T_0,\sigma}(z)$ for small $J$ (Problem D, step i).

---

*Companion documents: `00-MAP.md`
(diagram), `phase-0-foundations/0A2-connes-compression.md` (the faithfulness analysis),
`06-papers/P7-localized-weil-detector/main.tex` (the proven theorems).*
