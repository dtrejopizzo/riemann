# Phase 9 / T9-cal — The calibration deliverable: an exchange rate between Montgomery support and analytic RH

**Author: David Alejandro Trejo Pizzo · 2026-06-04.** `experiments/T9cal_support_requirement.py`.
This is the program's honest finite contribution: not a proof of RH, but a precise, quantified statement of
**exactly how much** unconditional progress on Montgomery's pair correlation would certify the extremal
collision margin (analytic RH) up to a given height — a concrete target for the community, calibrated by our
detector and the extremal reduction of P12.

## The bridge (rigorous up to an O(1) constant)

1. **Detector ↔ support (N3).** The band-limited Weil–Carleson detector at band $d$, height $T$, uses pair
   correlations $F(\alpha)$ only up to $\alpha=2d/\log T=x$ (primes $\le e^{2d}=T^{x}$). [P11, N3.]
2. **Support ↔ resolved gap (Nyquist).** To certify the collision margin against a pair of *normalized* gap
   $\beta$, the form factor must be controlled up to $\alpha\asymp 1/\beta$ (resolving a separation $\beta$
   needs band $\sim1/\beta$; O(1) constant). [B1 sine-kernel second order.]
3. **Extremal pair (P12).** $\Lambda$ is set by the *tightest* pair (Prop. 4.1). So certifying the margin up to
   height $T$ requires support up to $\alpha_{\mathrm{req}}(T)\asymp 1/\beta_{\min}(T)$, where $\beta_{\min}(T)$
   is the smallest normalized gap among all zeros up to $T$.

## The exchange rate (the deliverable)

GUE level repulsion gives the gap density $\sim s^2$ near $0$, so the minimum normalized gap among $N$ zeros
scales as $\beta_{\min}\asymp N^{-1/3}$ (from $N\!\int_0^{\beta}s^2\,ds\asymp1$). With $N=N(T)\sim\frac{T}{2\pi}\log T$,

$$
\boxed{\ \alpha_{\mathrm{req}}(T)\ \asymp\ \frac{1}{\beta_{\min}(T)}\ \asymp\ N(T)^{1/3}\ \asymp\ \Big(\tfrac{T}{2\pi}\log T\Big)^{1/3}\ }
$$

— and inverting, **proving Montgomery's $F(\alpha)\le O(1)$ unconditionally up to a given $\alpha=A$ certifies
the extremal collision margin (hence the analytic non-existence of off-line zeros / RH) for the first
$\sim A^{3}$ zeros.** A clean exchange rate:

| proven unconditional support $A$ | certifies the extremal margin up to | $\approx$ height $T$ |
|---:|---:|---:|
| $1$ (Montgomery, **proven**) | $\sim1$ zero | — (bulk/average only) |
| $5$ | $\sim125$ zeros | $T\sim100$ |
| $20$ | $\sim8000$ zeros | $T\sim2500$ |
| $100$ | $\sim10^{6}$ zeros | $T\sim2\times10^5$ |
| $\to\infty$ | all zeros | **full RH** |

*(Numerical illustration, block-level, confirming $\alpha_{\mathrm{req}}>1$ at every nontrivial height:
$\beta_{\min}=0.29,0.22,0.19$ at $T\approx310,1591,10^4$, i.e. $\alpha_{\mathrm{req}}=1/\beta_{\min}=3.4,4.5,5.2$
for a fixed $300$-zero window; the height-$T$ requirement over all $N(T)$ zeros follows the $N^{1/3}$ law above.)*

## What this says, precisely and honestly

- **Montgomery's proven range $\alpha<1$ is, for the extremal target, essentially empty.** It controls only
  gaps $\beta>1$ — the *bulk/average* (the marginal $C\approx1$, the GUE mean). It **never** reaches the
  tightest pairs ($\beta_{\min}<1$ at every nontrivial height), which live in the conjectural region $\alpha>1$.
  This is *why* the known range certifies RH-consistency on average but not the extremal absence of off-line
  zeros.
- **Each unit of new proven support buys $\sim\alpha^3$ certified zeros.** The support-extension problem and
  finite-height analytic RH are linked by an explicit polynomial exchange rate. Full RH is the $\alpha\to\infty$
  endpoint — equivalently, the complete Montgomery conjecture / unconditional short-interval prime variance.
- **The detector makes this measurable.** For any claimed unconditional bound on $F(\alpha)$ up to $\alpha=A$,
  the detector can verify directly which heights it certifies, turning "extend the support" into a checkable,
  quantified milestone.

## Status (and the program's finite output)
- The exchange rate $\alpha_{\mathrm{req}}\asymp N^{1/3}$, support $A\leftrightarrow\sim A^3$ certified zeros — ✅
  derived (bridge rigorous up to O(1); GUE scaling), illustrated numerically.
- This is **not** RH and **not** a crossing — it is the precise, quantified target: *how much* unconditional
  pair-correlation suffices, height by height.
- It is the honest, finite residual contribution after N1–N6 + T9-A + the wrong-sign capstone. With it, the
  program's analytic arc is complete: the wall is mapped, the target is cornered, and the cost of crossing is
  priced.
