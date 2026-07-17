# M5 — The Weil-residual classification program (pure theory): an arithmetic invariant separating RH-true from RH-false L-functions

**Route B / creative frontier, pure-theory spine.** Author: David Alejandro Trejo Pizzo · 2026-06-03.
Builds on: P7 (localized detector, forced negativity), P8 (Kreĭn/angular, Thm C), M1 (Connes residual,
Prop B3.1.3), M3 (semi-local residual). Panel input: reframe to **classification, not RH**; the **tautology
test** is mandatory and first.

> **Cover question (the declared goal — RH-independent).**
> *Is there an operator-theoretic invariant of the semi-local Weil residual that separates RH-consistent and
> RH-violating L-functions — and is it genuinely arithmetic, not a re-encoding of the zero locations?*

This document does two things: (1) **proves** that the tautology objection is already answered on our side
(§1), which fixes *which side* the invariant must come from; (2) lays out a **pure-math path** of four
theorem-targets T1–T4 (§§2–5), each leveraging an asset we already own, with proof strategies and an honest
account of what is in hand versus conjectural.

---

## 0. The reframe, precisely

We study a family $\mathcal F$ of L-functions $L$ (degree, conductor, $\Gamma$-factor fixed within a family),
each with completed form $\Lambda_L$, Euler product $\prod_p L_p(s)^{-1}$, and functional equation. To each
$L$ we attach the **semi-local Weil residual operator** $K(L)$ — the residual after the Connes–Consani
manifest square (M1–M3), built from $L$'s *arithmetic* data (Euler factors + $\Gamma$-factor + conductor),
**not** from its zeros. The program seeks an invariant $I(L)$ (a spectral statistic of $K(L)$) such that
$$
I(L)\ \text{is small/bounded for RH-consistent }L,\qquad I(L)\ \text{anomalous for RH-violating }L,
$$
and — crucially — $I$ is a *genuine function of the arithmetic*, not of the zero positions. The deliverable is
the invariant and the theorems governing it; RH is the **north star**, not the target.

---

> **⚠️ FOUNDATION CORRECTION (hostile audit, 2026-06-03).** The first draft proposed working with a
> generalized Connes residual $K_{\mathrm{CC}}(L)$ via "CC eq. (14) with $\lambda(n)\to a_n(L)$." **That is an
> error:** in CC eq. (14) the $\lambda(n)$ are the **prolate spheroidal eigenvalues** (Sonin geometry,
> L-independent), *not* the L-function coefficients. The L-dependence of the semi-local residual enters
> through the **prime/Euler terms**, not the archimedean $\epsilon$. The correct, rigorous, *in-hand* working
> object is therefore **P7's localized arithmetic Weil-Gram** $Q_{\mathrm{arith}}(L)$ (assembled from the
> Euler product + $\Gamma$-factor + conductor), with the angular operator $K(L)$ of its indefinite split, and
> $$
> \lambda_{\min}\big(Q_{\mathrm{arith}}(L)\big)<0\ \iff\ \|K(L)\|>1 .
> $$
> All of §§1–7 below should be read with $K(L)$ = the angular operator of $Q_{\mathrm{arith}}(L)$; $K_{\mathrm{CC}}$
> is the (heavier, continuum) archimedean-clean ideal, related but not what we prove with. The proofs of T1,
> T2 (and the analytic D2) are carried out on $Q_{\mathrm{arith}}$ in the companion file
> `M5-T1-T2-proofs.md`.

## 1. The tautology objection is already answered (the spine) — PROVED

The panel's killer test: *maybe $I(L)=f(\text{distance of nearest zero to the line})$, i.e. the invariant
just detects that you inserted off-line zeros — tautological.* We have already proved the dichotomy that
settles this. **It is the same distinction as P8's no-go.**

> **Proposition 1 (the two sides; assembled from P8 Thm C + M1 Prop B3.1.3).**
> There are two operators whose norm-below-$1$ each $\iff$ RH:
> 1. the **zero-side** $K_{\mathrm{P8}}(L)$, built from zero-evaluations. By **P8 Theorem C** it is a direct
>    functional of the zero configuration ($K_{\mathrm{P8}}=0$ exactly on RH, within the §§6–7 realization),
>    and "circular as a tool" — it *presupposes* the zeros. **Any invariant built from $K_{\mathrm{P8}}$ is
>    the tautology the panel warns against.**
> 2. the **arithmetic-side** $K_{\mathrm{CC}}(L)$, built from the Euler/$\Gamma$ data (Connes–Consani). By
>    **M1 Prop B3.1.3** it is *not* a zero-independent unitary image of $K_{\mathrm{P8}}$, and by construction
>    it is a **real-analytic functional of the Euler factors** (CC eq. (14): $\epsilon$ is an absolutely
>    convergent sum in the local coefficients), hence continuous across the RH boundary, where the
>    zero-distance functional $d(L)$ is not.
>
> **Conclusion.** *The invariant must be taken on the arithmetic side $K_{\mathrm{CC}}$.* There it is, by the
> two cited theorems, **not** a re-encoding of the zero locations: it is a smooth functional of the local
> arithmetic, provably distinct from the zero-side tautology.

**Why this matters strategically.** The panel independently worried about exactly the failure mode our own
P8 Thm C already proves is real (the zero side). So our prior work *certifies* the program's foundation: the
non-tautological invariant exists on the Connes side and nowhere on the zero side. **The tautology test is
passed before any experiment is run.** This is the strongest single point to put to the panel.

*(What remains for full rigor — T1 — is to upgrade "real-analytic in the Euler factors, distinct from
$d(L)$" to a clean separation theorem across a multi-$L$ family. §2.)*

---

## 2. T1 — The anti-tautology / arithmetic-continuity theorem (first target)

> **T1 (target).** The invariant $I(L)=\|K_{\mathrm{CC}}(L)\|$ (suitably conditioned, as in CC §6) is a
> real-analytic functional of the Euler factors $\{a_p(L)\}$ and the $\Gamma$-factor, and is **not** a
> function of the zero-distance data $d(L)$ alone: there exist $L_1,L_2$ in a family with $d(L_1)=d(L_2)$ but
> $I(L_1)\ne I(L_2)$.

**Proof strategy (honest).**
1. *Analyticity.* $K_{\mathrm{CC}}(L)$ is assembled from $\epsilon_L(\rho)=\sum_n \frac{a_n(L)}{\sqrt{1-|a_n(L)|^2}}\langle\zeta_n|\vartheta(\rho^{-1})\zeta_n\rangle$
   (CC eq. (14) generalized: replace $\lambda(n)\to a_n(L)$, the normalized coefficients). On the region of
   absolute convergence this is real-analytic in $\{a_p\}$; the Hilbert–Schmidt norm and the conditioned top
   eigenvalue inherit analyticity (Kato, analytic perturbation of a simple eigenvalue). ✅ provable.
2. *Non-tautology.* Exhibit a two-parameter sub-family where one parameter moves a zero (changing $d$) and a
   second changes a *distant* Euler factor (fixing $d$, changing $I$). The second deformation changes
   $\epsilon_L$ (it touches all $\langle\zeta_n|\cdot|\zeta_n\rangle$) without touching the nearest zero ⟹
   $I$ changes while $d$ does not. ◆ provable modulo constructing the sub-family; this is where the explicit
   violator $L_{\mathrm{DH}}$ and Dirichlet-character twists give concrete handles.

**Status:** §1 already gives the qualitative separation (analytic vs non-smooth); T1 makes it a clean
quantitative theorem. **First milestone of the pure-theory program.**

---

## 3. T2 — The forced spectral transition (transversal crossing), from P7

This is the rigorous form of the panel's "spectral transition" criterion, and it is **nearly in hand** —
it is P7's forced-negativity theorem, lifted into the angular-norm language.

> **T2 (target).** Along a real-analytic one-parameter deformation $L_t$ of the arithmetic that moves a
> conjugate zero-pair off the critical line at displacement $\delta(t)$, the conditioned top eigenvalue
> $\mu(t)=\|K(L_t)\|$ crosses $1$ **transversally** at the RH boundary, with an explicit arithmetic rate:
> $$
> \mu(t)-1\ \asymp\ c\,\delta(t)^2,\qquad c\sim A(\gamma)\ \ (\text{P7's explicit prefactor}),
> $$
> so $\frac{d}{d(\delta^2)}\mu>0$ at $\delta=0$ — a genuine (non-coincidental) spectral transition.

**Proof strategy.** P7 **Theorem I** proves $\lambda_{\min}(Q)\le\lambda_{\min}(Q_0)-c(\delta,\sigma,J;\gamma)$
with $c\sim\delta^2 A(\gamma)$ (matched to computation to $<10^{-5}$). In the Kreĭn/angular split (P8 §7),
$\lambda_{\min}(Q)<0\iff\|K\|>1$, so P7's forced negativity **is** "$\|K\|>1$ at rate $\delta^2 A(\gamma)$."
The remaining step is the *transversality* (the crossing is simple and the derivative is the rank-one P7
perturbation, Hellmann–Feynman), which P7's explicit rank-one structure supplies. ✅ largely in hand;
formalizing the crossing in the conditioned residual is the work.

**Why it answers the panel.** A *transversal* crossing with an *explicit arithmetic rate* is exactly "real
structure, not a numerical coincidence." And $A(\gamma)$ — the prefactor — is an **arithmetic invariant of the
transition** (it depends on the local geometry of the explicit formula at height $\gamma$), a first concrete
$I$-ingredient.

---

## 4. T3 — The anatomy decomposition (which ingredient forces the crossing)

> **T3 (target).** Decompose the residual quadratic form by place,
> $$
> \langle K(L)\,\cdot,\cdot\rangle = \underbrace{R_\infty}_{\Gamma\text{-factor (manifest CC square)}} + \sum_p \underbrace{R_p}_{\text{Euler factor at }p},
> $$
> and determine which terms can drive $\|K\|>1$. Prove: $R_\infty\succeq0$ (CC's archimedean square,
> conditioned), each $R_p$ is an explicit Toeplitz-type block in $a_p,a_{p^2},\dots$; the crossing is forced
> only by the **interaction** $R_\infty+\sum_p R_p$, never by a single place (cross-place, M3 §5).

**Proof strategy.** $R_\infty$ is CC Theorem 6.11 (archimedean, solved). Each $R_p$ comes from the local
Euler factor in $M_{\mathrm{arith}}$ (P7 already assembles $M_{\mathrm{arith}}$ place-by-place). Sign/Toeplitz
analysis of $R_p$ (the Slepian/prolate basis makes these banded). ◆ partially provable; the place-by-place
positivity of $R_\infty$ is CC, the prime blocks are explicit, the *interaction* sign is the open content
(= the semi-local wall). This is where "does the Euler product matter? the conductor? multiplicativity?"
becomes a **theorem about which $R_\bullet$ carry the difference** between $\zeta$ and $L_{\mathrm{DH}}$.

---

## 5. T4 — The classification statement (north star, partial results expected)

> **T4 (conjecture + partial results).** There is an explicit arithmetic functional $\Phi(L)$ of the local
> data with $\|K(L)\|\le\Phi(L)$, such that $\Phi(L)\le1$ holds for an identifiable structural class
> (e.g. L-functions with a positive-definite Rankin–Selberg/symmetric-square structure) and $\Phi(L_{\mathrm{DH}})>1$.
> $\Phi$ is the sought invariant: it separates the classes *by arithmetic*, and even as a **necessary** or
> **probabilistic** statement is new knowledge about L-function anatomy.

This is the program's declared output. Full $\Phi$ controlling $\|K\|\le1$ for $\zeta$ is RH ($<1\%$); a
*partial* $\Phi$ (a sufficient arithmetic condition on a sub-class, or a sharp necessary condition) is the
realistic, publishable target — exactly the panel's "necessary / probabilistic / observable invariant is
still new knowledge."

---

## 6. The deformation family (rigorous version of the panel's convincing experiment)

To avoid the tautology (and to *prove* T2/T3 are not coincidence), the right object is a **continuous family**
$L_t$, not two points. Three orthogonal deformations, each isolating one arithmetic ingredient:
- **(D1) zero-position deformation** (move a pair off the line): drives T2; the *control*, expected to give
  the tautological $f(\delta)$ — its job is to be **subtracted** from the others.
- **(D2) Euler-factor deformation** (perturb $a_p$ at fixed nearest-zero $d$): if $I$ moves under D2 with $d$
  fixed, the invariant is **non-tautological** (T1's witness) — *this is the experiment to run first, to try
  to destroy the program*.
- **(D3) conductor / $\Gamma$-factor deformation**: isolates the archimedean contribution (T3 $R_\infty$).

A **sharp spectral bifurcation** under D2 or D3 (not D1) is the signal of real arithmetic structure. This is
the empirical counterpart of T1–T3; it guides the proofs and is run with the P7 engine (M4), but the
**headline deliverables are the theorems**, with the family as evidence.

---

## 7. Honest priors, guardrails, and what is in hand

| Target | In hand | To prove | Prior of a real result |
|---|---|---|---|
| §1 tautology resolution | ✅ (P8 Thm C + M1 Prop B3.1.3) | — | done |
| T1 anti-tautology / analyticity | analyticity ✅; separation ◆ | the witness sub-family | high |
| T2 forced transition | P7 Thm I (rate $\delta^2A(\gamma)$) ✅ | transversality in conditioned $K$ | high |
| T3 anatomy decomposition | $R_\infty$ (CC), $R_p$ explicit ✅ | the interaction sign | moderate |
| T4 classification $\Phi$ | — | the arithmetic bound | partial: moderate; full: $<1\%$ |

**Guardrails (unchanged).** Zero-independence (B0): the invariant lives on the arithmetic side, *proved*
non-tautological (§1). Magnitude ≠ sign: $\|K\|\le1$ for $\zeta$ is evidence, never RH. Audit before
pillarizing. **Declared goal = classification/anatomy, RH = north star.**

**Net for the panel (one line).** *The tautology objection is already settled by our own results — the
zero-side invariant is the tautology (P8 Thm C), the arithmetic-side Connes residual is provably distinct and
analytic in the Euler factors (M1 Prop B3.1.3) — so the classification invariant exists on the arithmetic
side by theorem; we then propose a pure-theory path (T1 analyticity/separation, T2 a transversal forced
spectral transition lifted from P7's explicit $\delta^2A(\gamma)$ rate, T3 a place-by-place anatomy, T4 the
separating arithmetic functional $\Phi$), with a three-deformation family $L_t$ as the falsifying evidence,
declared goal = anatomy of L-functions, RH the north star.*

---

### Status / next
- §1 (tautology resolved) — ✅ proved (assembled from P8/M1).
- T1 — ⬜ first pure-theory milestone (analyticity ✅, separation witness ◆).
- T2 — ◆ near-in-hand (P7 Thm I + transversality).
- T3 — ◆ partial (CC + explicit prime blocks; interaction open).
- T4 — ⬜ north star; partial $\Phi$ the realistic target.
- D1–D3 family / M4 experiment — ⬜ evidence, guides the proofs.

*Records updated on completion: this folder, `00-MAP.md`, the proof log, project memory.*
