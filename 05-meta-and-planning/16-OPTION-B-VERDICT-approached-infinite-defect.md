# Option (b), sub-fork decided: APPROACHED — the critical structure is infinite-dimensional

**Auditor build · 2026-06-05.** `phase-14/experiments/near_critical_multiplicity.py`. The surviving sub-fork of
the Pontryagin route was: in the genuine ($d\to\infty$) Weil form, is the saturation $\lambda_{\max}=1$ **attained**
(finite critical structure $\Rightarrow$ finite defect $\kappa<\infty$ possible) or **approached** (growing number
of near-critical directions $\Rightarrow$ infinite-dimensional marginality)? Computed.

---

## The data (full pencil $(P_F,A_\Phi)$, $T_0=1000$, basis scaled with band)

| $d$ | #primes | dim | $\lambda_{\max}$ | gap $\lambda_{\max}-\lambda_2$ | $\#\{\lambda>0.9\}$ | $\#\{\lambda>0.99\}$ |
|---:|---:|---:|---:|---:|---:|---:|
| 3 | 98 | 31 | 1.00000 | $10^{-5}$ | 4 | 3 |
| 4 | 465 | 37 | 1.00000 | $10^{-6}$ | 13 | 11 |
| 5 | 2532 | 43 | 1.00013 | $10^{-4}$ | 20 | 19 |
| 6 | 15040 | 49 | 1.00000 | $10^{-6}$ | 28 | 27 |

## Verdict: APPROACHED, decisively

- The near-critical multiplicity **grows linearly**: $\#\{\lambda>0.99\}=3,11,19,27$ for $d=3,4,5,6$ (constant
  increment $8$, i.e. $\approx 8d-21$).
- The **spectral gap $\lambda_{\max}-\lambda_2\approx0$**: the top eigenvalues are degenerate at $1$, not isolated.
- The **critical fraction grows**: $3/31,\,11/37,\,19/43,\,27/49$ — from $10\%$ to $55\%$ of the spectrum near $1$.

> The saturation $\lambda_{\max}=1$ is **not carried by a bounded number of directions.** A growing-dimensional
> (in fact positive-fraction, growing) subspace has $\mathfrak p\approx\mathfrak a$, i.e. $\mathfrak t=\mathfrak a-
> \mathfrak p\approx0$. The Weil form has a **near-null space of growing dimension** — the infinite-dimensional
> analogue of "$\Lambda=0$ approached, not attained."

## Consequence for option (b)

- **The finite-defect picture fails.** $\kappa<\infty$ via a finite critical structure is **not** available: the
  near-critical (near-null) space is infinite-dimensional and grows linearly with the band. Combined with the
  earlier result that the finite-rank-head reduction also fails (subordination cutoff $X^*(d)\sim e^{2d}/10$
  slides to $\infty$), **both mechanisms for $\kappa<\infty$ are closed by computation.**
- **The criticality is self-similar.** Linear growth of the near-null dimension with $d$ (band $=$ $\log$-prime
  range $=$ height-scale) matches the $\log T$ growth of the zero density and the scale-invariance found in the
  $a_{\text{tail}}$ experiment: criticality at every scale, not a localized defect.

## Where this returns the program

Option (b), pushed to computation, returns to the program's central wall, now with a sharp datum:

> The Weil form for $\zeta$ is **critically marginal with an infinite-dimensional near-null space.** Semiboundedness
> in the limit ($\inf\mathfrak t/\|\cdot\|^2 = 0$ attained, $\kappa=0$, vs. escaping to $-\infty$) is decided on
> this growing subspace — which is exactly the original $(LB)$/closability question (proof log Days 0–23), now
> equipped with the structural fact that the critical subspace is **not finite.** A finite-defect ($\Pi_\kappa$)
> shortcut does not exist; any resolution must control the form on an infinite-dimensional near-null space, i.e.
> face the over-sampling/coercivity problem (Days 12–16) head-on.

## Status

- Sub-fork **decided: APPROACHED** (near-critical multiplicity grows linearly; gap $\to0$; critical fraction
  $\to$ majority).
- Option (b) **closed** at the computed level: neither finite-rank head ($X^*(d)\to\infty$) nor finite defect
  (growing near-null space) yields $\kappa<\infty$.
- Net: the Pontryagin route does not cross the wall, but the wall is now characterized precisely — *infinite-
  dimensional, self-similar criticality* — returning to the semiboundedness/coercivity core with no finite
  shortcut. The honest residue is that the program's central inequality (semiboundedness of the localized Weil
  form) is the irreducible object, and the off-line-zero count is not finite-rank-detectable.
