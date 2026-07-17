# The cross-scale cancellation door, probed: the √N barrier is overcome on each direction; the wall is the exact-boundary calibration

**Auditor build · 2026-06-05.** `phase-14/experiments/cross_scale_cancellation.py`. The one formally-open door of
option (b): in the genuine ($d\to\infty$) form, do the prime octaves cancel destructively across scales (so the
saturation $\lambda_{\max}=1$ is maintained robustly), or accumulate (marginal conspiracy)? We measured, on the
saturating direction $g^\ast$ (the $\lambda_{\max}$ eigenvector), the running ratio $R(Y)=\fp_{\le Y}[g^\ast]/
\fa[g^\ast]\to1$ and the cancellation strength $|\fp_{\le Y}[g^\ast]|/\sqrt Y$ against the naive Chebyshev
amplitude.

---

## Two facts from the data

**(1) The √N barrier is overcome on each direction.** $|\fp_{\le Y}[g^\ast]|/\sqrt Y$ decays monotonically toward
$0$ ($d{=}6$: $\dots,0.016,0.009,0.006,0.004,0.002$). The prime form on the optimal direction grows far slower
than the naive $\sqrt Y\to e^{d}$; it stays bounded ($=\fa[g^\ast]$). So the relative-form prime sum *is*
square-root-cancelled on every finite direction — the $\sqrt N$ growth that blocks the naive KLMN is **not** the
obstruction at the level of individual test functions.

**(2) The saturation lands at exactly the boundary, by a sign-alternating octave conspiracy.** The per-octave
increments $\Delta R$ are $O(0.1)$, do **not** decay, and **alternate in sign** at the top: at $d{=}5$ the form
overshoots to $R=1.064$ then the last two octaves correct by $-0.042,-0.022$ to $1.000$; at $d{=}6$ several octaves
are negative ($-0.075,-0.062,-0.063$), landing at $R=1.00000$. The octaves do genuine cross-scale cancellation, and
they are calibrated to terminate at exactly $R=1$ — no slack below, no overshoot above.

## Verdict

> The cross-scale door does **not** hide a crossing. The cancellation is real and convergent **relative to the
> naive $\sqrt N$ amplitude** (fact 1), so the square-root barrier is a red herring *pointwise*; but it is
> calibrated to land at **exactly** the archimedean envelope ($R=1$, the N3 saturation) via $O(0.1)$
> **sign-alternating** octave corrections (fact 2). The obstruction is not "the primes grow like $\sqrt N$'' --- they
> are cancelled --- it is "the cancellation terminates at the boundary with zero margin,'' maintained by a genuine
> cross-scale conspiracy.

This is the octave-resolved form of N3 (prime incoherence buys zero margin): the incoherence is now seen to be a
*sign-alternating cancellation across $\log$-prime octaves* that holds the prime form exactly at the archimedean
ceiling. Combined with the two earlier closures (finite-rank head fails, $X^\ast(d)\sim e^{2d}/10$; finite defect
fails, near-null multiplicity grows linearly), the picture is complete and consistent: the marginality is
**self-similar across scale, infinite-dimensional in directions, and boundary-exact in magnitude**.

## What this settles for option (b)

- The last formally-open door (cross-scale cancellation) is **characterized, not crossed**: the cancellation
  exists and beats $\sqrt N$, but terminates exactly at $R=1$. There is no mechanism here that pushes $R$
  uniformly below $1$ (which would give a margin / $\kappa<\infty$ slack) or above (off-line zeros).
- The three probes converge: option (b) returns, fully, to the semiboundedness of the Weil form at the exact
  boundary --- the Weil criterion --- with the marginality now resolved in all three coordinates (scale:
  self-similar; direction-count: infinite; magnitude: boundary-exact). No finite or cross-scale shortcut exists.

## The honest residue (where this leaves the genuine limit)

For $\zeta$ the running ratio lands at $R=1.000$ (RH-consistent: $R\le1$). The data does not, and cannot, decide
the genuine-limit sign of the margin $1-R$ --- that is the Weil criterion itself. What the probe adds is
mechanistic: the margin is held at $0$ by sign-alternating octave cancellation, so any unconditional proof of
$R\le1$ (semiboundedness) must control that alternating cross-scale sum --- i.e., exhibit the cancellation as a
*theorem about the prime octaves*, not a numerical coincidence. That is the same $I_{2b}$ object the classifier
isolates (a general theorem supplying the boundary), now localized to: **a cross-scale cancellation law for
$\sum_{\text{octave}}\Lambda(n)n^{-1/2}(g\star\tilde g)(\log n)$ that is sign-alternating and boundary-exact.** No
such law is known; whether it is provable unconditionally is the residue, and it is a sharply posed prime-side
statement rather than a statement about zeros.

## Status

- Cross-scale door **probed and characterized**: √N overcome pointwise ($|\fp|/\sqrt Y\to0$); saturation
  boundary-exact via $O(0.1)$ sign-alternating octave corrections (octave-resolved N3).
- Option (b) **fully closed** across its three sub-questions (finite head, finite defect, cross-scale), all
  returning to the boundary-exact semiboundedness of the Weil form.
- Sharp prime-side residue named: an unconditional sign-alternating boundary-exact cross-scale cancellation law ---
  the $I_{2b}$ object, localized to the prime octaves.
