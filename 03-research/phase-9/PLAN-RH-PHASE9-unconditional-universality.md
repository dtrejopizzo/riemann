# Phase 9 — The new-mathematics program: unconditional gap universality of the ζ zeros

**Author: David Alejandro Trejo Pizzo · 2026-06-04.**
Every route in this program (P11's five static languages; P12's dynamical N5 and extremal reduction) terminates
at one irreducible arithmetic statement. This document turns that statement into a structured attack — the
"new mathematics" the problem demands — with a genuinely new spearhead that escapes the N5 no-go, an honest
landscape of what is known, concrete sub-targets and milestones, and the role of our own assets. Odds are
small and the horizon is long; this is written as a real multi-stage program, not a promise.

---

## 0. The target, stated exactly

From P12 (Prop. 4.1, Obs. 4.2): $\mathrm{RH}=\{\Lambda\le0\}$ follows from

> **(U) — Unconditional extremal gap universality.** *The normalized backward-collision margin $t_c/s^2$ of the
> $\zeta$ zeros stays a negative constant, uniformly in height $T$* — equivalently, the **closest-pair gaps**
> of the zeros obey a universal one-sided (GUE) bound, unconditionally and with **no exceptions**, uniform in
> $T$.

Two features make (U) hard and shape the attack:
- **Extremal, not average.** A single anomalously tight pair would decide $\Lambda$; averaged statistics
  (mean spacing, integrated pair correlation) are blind to a sparse exceptional set. (U) is a *sup*/no-exceptions
  statement.
- **One-sided.** We need only the *lower* control of gaps (no pair too tight). This is weaker than the full
  two-sided gap distribution and is the lever we exploit.

---

## 1. The honest landscape (what is known, where the barriers are)

| Result | Status | Barrier to (U) |
|---|---|---|
| Montgomery pair correlation $R_2(\alpha)\to1-(\frac{\sin\pi\alpha}{\pi\alpha})^2$ | proven for test fns with Fourier support in $(-1,1)$ | the **support barrier**: $|\mathrm{supp}|<1$; full support is open and prime-deep |
| Rudnick–Sarnak $n$-level correlations $=$ GUE | **unconditional**, restricted support | same support barrier; restricted range only |
| Katz–Sarnak universality (function fields) | **proven** (Deligne equidistribution, monodromy) | no transport to number fields known |
| Simplicity of zeros (all simple) | $>41\%$ simple (Levinson/Conrey mollifier) | $100\%$ open; tight-pair = near-double |
| Smallest gaps / level repulsion tail | conjectural ($\sim s^2$ near $0$) | the extremal tail is exactly (U) |

**Reading.** The GUE statistics are *known unconditionally in a restricted Fourier-support range* (Montgomery,
Rudnick–Sarnak). (U) needs (a) the **extremal/no-exceptions** strengthening and (b) enough **support** to reach
the closest-pair regime. Both are central open problems; (U) sits at their intersection.

---

## 2. The spearhead: escape N5 with an *arithmetic-aware* monotone functional

P12/N5 proved a **position-only** Lyapunov functional cannot work: the flow is arithmetic-blind, so any
$F(\{z_j\})$ has an arithmetic-blind derivative. **The escape is to use a functional of $H_t$ itself**, not of
its zeros — one that sees the *kernel* $\Phi$ (hence the primes) through the explicit-formula structure, and is
*also* monotone under the flow. This is the one move N5 does not forbid.

> **Spearhead idea (S9).** Seek a functional $\mathcal F[H_t]$ — e.g. a weighted Dirichlet energy
> $\int w(x)\,|\partial_x\log H_t(x)|^2\,dx$, or a relative entropy of the empirical zero measure against the
> arithmetic density $\frac1{2\pi}\log\frac{T}{2\pi}$, or an explicit-formula pairing $\sum_p c_p(t)$ — that
> **(a)** is monotone along the flow (Lyapunov), **(b)** depends on the **arithmetic** of $H_t$ (its primes /
> kernel), and **(c)** controls the extremal collision margin. Then monotonicity + the arithmetic of the
> initial data could force $t_c/s^2<0$ uniformly. N5 is evaded precisely because $\mathcal F$ is not a function
> of zero positions alone.

**Concrete first computation (M9.1).** The flow has a free energy: $\dot z_j=2\partial_{z_j}W$,
$W=\sum_{k<l}\log(z_k-z_l)$ (Coulomb). Compute $\frac{d}{dt}$ of the candidate $\mathcal F$'s along the flow,
coupled to the $t$-deformed explicit formula (the zeros of $H_t$ satisfy a $t$-deformed Weil formula relating
them to a Gaussian-smoothed prime sum). Identify whether any $\mathcal F$ is simultaneously (a) monotone and
(b) arithmetic-aware. *This is the genuinely new object; M9.1 is the make-or-break of the whole spearhead.*

---

## 3. Sub-targets (independently valuable; some incremental)

- **T9-A — Extend the support range.** Push Montgomery/Rudnick–Sarnak past the current Fourier-support limit,
  even slightly, in the *one-sided closest-pair* direction. Tools: the explicit formula + sieve/large-sieve,
  Goldston-type variance bounds, the recent unconditional pair-correlation extensions. *Incremental, real,
  publishable even partially.*
- **T9-B — Bound the tight-pair tail unconditionally.** Show $\#\{$pairs with normalized gap $<\delta\}\ll
  \delta^{3}\,N(T)$ (the GUE level-repulsion exponent) unconditionally, or any nontrivial power. Tools:
  mollified second/fourth moments (Conrey–Ghosh–Gonek), the resolvent/Montgomery–Vaughan large sieve. Connects
  to simplicity of zeros. *A power-law tail bound, even weak, directly feeds (U).*
- **T9-C — The arithmetic-aware Lyapunov (S9).** §2. The spearhead; highest novelty, highest risk.
- **T9-D — Function-field transport.** Study what in the Katz–Sarnak/Deligne proof of universality is
  *structural* (monodromy, equidistribution) vs. *geometric* (Frobenius), and whether the structural part has a
  number-field shadow via the Connes–Consani arithmetic site. *Deep, long-horizon, but the only place
  universality is actually proven.*

---

## 4. Our assets (what we bring that the standard programs do not)

- **The validated detector (P7/P11):** computes the extremal Carleson/collision margin directly; a *measuring
  instrument* for (U) and for testing whether a given support-range or moment bound suffices. Use it to
  **calibrate** T9-A/T9-B (how much support / how strong a tail bound is *exactly* enough for $t_c/s^2<0$).
- **The extremal reduction (P12):** reframes universality as a **one-sided extremal** statement (collision
  margin), possibly attackable by a maximum principle on the flow rather than the full correlation — a softer
  target than the complete gap distribution.
- **The Lyapunov theorem (P12):** the monotone structure S9 builds on.
- **The five-language map (P11):** tells us every equivalent of the *static* obstruction, so we can recognize
  immediately if a sub-target secretly reduces to one (the guard against circular "progress").

---

## 5. Methodology (OpenAI-autonomous-proof style) and gates

- **Precise lemmas, stated to prove or break.** First: **L9.1** — *does there exist $\mathcal F[H_t]$ monotone
  under the flow and dependent on the kernel $\Phi$?* (the S9 make-or-break).
- **Verify-first.** Every monotonicity/bound checked numerically (real zeros, the detector) before belief.
- **Self-refute.** Break each candidate $\mathcal F$ before building on it; a false monotonicity must die at the
  computer. (Guard-rail: every sign/blow-up claim checked vs. ground truth.)
- **Anti-circularity gate.** After any sub-result, check it against the P11 five-language map and N5: if it
  reduces to "reality of the zeros" or to a position-only functional, it is the wall again — log and reassess.
- **Decision gates.** (A) Does S9 produce an arithmetic-aware monotone $\mathcal F$? If no after a bounded
  effort, S9 is dead — pivot to the incremental T9-A/B. (B) Do T9-A/B reach the *closest-pair* regime, or stall
  at the support barrier? (C) Is any sub-target unconditional, or does it import RH/GRH?

---

## 6. Honest expectations and horizon

- **(U) is a central open problem** (the unconditional, extremal, full-support GUE universality of ζ zeros).
  Cracking it outright is a multi-year, likely community-scale effort; from here, $<1\%$ for the full target.
- **But the program is well-posed and partly incremental:** T9-A (support) and T9-B (tight-pair tail) are
  genuine, publishable sub-problems where partial progress is real and our detector can calibrate *exactly how
  much* is needed. The spearhead S9 is high-risk/high-novelty and is the one move that escapes our own N5.
- **What would constitute a crossing:** either S9 yields an arithmetic-aware Lyapunov forcing $t_c/s^2<0$, or
  T9-A/B reach the closest-pair regime unconditionally. Both are new mathematics; both are honestly named.
- **What is already banked (so the program rests on solid ground):** P1–P12, the validated detector, the
  no-gos N1–N5, the Lyapunov theorem, and the precise target. Phase 9 is the attack on the named target, not a
  re-derivation of the wall.

---

## 7. Immediate next step

**M9.1 / L9.1 — the spearhead's make-or-break:** set up the $t$-deformed explicit formula for $H_t$ and test
whether a kernel-dependent functional $\mathcal F[H_t]$ (weighted Dirichlet energy or relative entropy) is
monotone under the flow. If yes, we have the first object in the program's history that is *both* monotone and
arithmetic-aware — the genuine escape from N5. If no, pivot to T9-A (extend support), the most incremental
real sub-problem, with the detector calibrating the needed range.

### Status
- Target (U) stated exactly; landscape mapped; barriers named — ✅.
- Spearhead S9 (arithmetic-aware monotone functional) — ⬜ the make-or-break, M9.1 next.
- Sub-targets T9-A/B/C/D + asset roles + gates + honest horizon — ✅ designed.
- This is the program for the new mathematics; execution begins at M9.1.
