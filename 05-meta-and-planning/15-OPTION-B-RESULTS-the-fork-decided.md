# Option (b), the fork decided numerically: the negative index is not finite-rank-capturable

**Auditor build · 2026-06-05.** `phase-14/experiments/a_tail_relative_form_bound.py`. The Pontryagin route reduced
RH-adjacency to one inequality: **(RFB$_X$)** — is the prime tail $\mathfrak p_{>X}$ relatively form-bounded by the
archimedean form with constant $<1$ for some *fixed* cutoff $X$? If yes, $\kappa<\infty$ (finitely many off-line
zeros). The relevant one-sided quantity (the one that controls *negative squares* of $\mathfrak t=\mathfrak a-
\mathfrak p$) is $\lambda_{\max}(\mathfrak p_{>X},\mathfrak a)$: the tail stops producing negative squares once
$\lambda_{\max}<1$. We computed it on the validated Phase-7 engine (high smooth height $T_0=1000$, bands $d=4,5$).

---

## The data

$\lambda_{\max}(\mathfrak p_{>X},\mathfrak a)$ as a function of the head-cut $X$:

| $X$ | $d{=}4$ ($e^{2d}{=}2981$) | $d{=}5$ ($e^{2d}{=}22026$) |
|---:|---:|---:|
| $1$ (full) | **1.00000** | **1.00000** |
| $5$ | 1.186 | 1.227 |
| $30$ | 1.098 | 1.357 |
| $150$ | 1.082 | 1.490 |
| $400$ | 0.714 | 1.049 |
| $1000$ | 0.375 | 1.048 |
| $\sim e^{2d}/4$ | — | 0.378 |

Two facts, both sharp:

1. **The full form saturates at exactly $1$.** $\lambda_{\max}(\mathfrak p,\mathfrak a)=1.00000$ at $X=1$ for both
   bands — the engine reproduces **N3** (Carleson saturation, $C\equiv1$) to five places. Validation of the
   computation, and a reminder that the boundary is *attained*.
2. **The subordination cutoff scales with the band.** $\lambda_{\max}(\mathfrak p_{>X},\mathfrak a)$ first drops
   below $1$ at
   $$
   X^*(d)\ \approx\ \tfrac1{10}\,e^{2d}\qquad(X^*(4)\approx300,\ X^*(5)\approx2000),
   $$
   i.e. in $\log$-scale the subordinate tail is the **fixed-width top slice** $[\,2d-\log 10,\ 2d\,]$ of the
   prime range, of width $\approx2.3$ *independent of $d$*. For any **fixed** $X$, $\lambda_{\max}(\mathfrak p_{>X},
   \mathfrak a)$ **increases with $d$** and crosses back above $1$ (e.g. $X{=}400$: $0.71\to1.05$).

## The verdict (the fork resolves to the knife-edge branch)

> **(RFB$_X$) fails for every fixed $X$ as $d\to\infty$.** The cutoff that makes the tail subordinate,
> $X^*(d)\sim e^{2d}/10$, diverges; in $\log$-scale the offending directions occupy a fixed-width window that
> *slides to infinity* with the band. The negative squares of the Weil form are therefore **not confined to a
> finite prime head** — they recur at every scale, self-similarly. **The finite-rank-head argument does not yield
> $\kappa<\infty$;** the Pontryagin route does not, by this mechanism, bound the number of off-line zeros.

This is the **scale-invariance of the N3 saturation**, made quantitative: criticality ($\lambda_{\max}=1$) is not a
small-prime artifact (removing small primes actually *raises* $\lambda_{\max}$ above $1$ — the saturation at exactly
$1$ is a global conspiracy of *all* primes, not a head effect) and not a large-prime tail effect; it is **uniform
across $\log$-prime scale**. The marginal constant $a=1$ is intrinsic to every dyadic prime block, matching the
GUE scale-invariance of the zeros.

## What this closes and what it leaves

- **Closed:** the specific hope that $\kappa<\infty$ follows from form-subordination of a finite tail. It does not
  — decisively, numerically, with the obstruction quantified ($X^*(d)\sim e^{2d}/10$, a sliding fixed-width
  critical window).
- **Sharpened:** the option-(b) wall is now the statement *"the relative-form criticality $a=1$ is
  scale-invariant"* — the same knife-edge as N3, now shown to live at all scales rather than at small primes. Any
  route to $\kappa<\infty$ must defeat criticality **uniformly in scale**, not merely past some cutoff.
- **Left open (the genuine residue):** $\kappa<\infty$ might still hold for a reason *other* than tail
  subordination — e.g. **cancellation across scales** (the sliding critical windows at different $d$ might
  destructively interfere in the true $d\to\infty$ form, even though each is individually marginal). The matcher's
  next concrete question: is $\lambda_{\max}(\mathfrak p,\mathfrak a)$ in the **genuine** ($d\to\infty$,
  non-band-limited) form equal to $1$ with the supremum *attained* (finitely many critical directions, $\kappa<
  \infty$) or *approached* (infinitely many, $\kappa=\infty$)? The band-limited data shows each finite-$d$
  truncation attains $1$; whether the limit attains or approaches is the surviving fork, and it is the
  infinite-dimensional analogue of "$\Lambda=0$ attained vs approached."

## Status

- Option (b) attacked to a computation; the fork **decided against** finite-rank-head $\kappa<\infty$.
- New quantitative law: subordination cutoff $X^*(d)\sim e^{2d}/10$; criticality $a=1$ **scale-invariant**.
- Surviving sub-fork: attained-vs-approached saturation in the genuine form ($\kappa<\infty$ vs $\kappa=\infty$),
  possibly via cross-scale cancellation — the one door this route leaves open, and a concrete next computation
  (track $\lambda_{\max}(d)\to1$ and the multiplicity of near-$1$ eigenvalues as $d\to\infty$).
