# Phase 12 — The first non-positivity path: log-correlated fields, multiplicative chaos, and native UPPER bounds

**Author: David Alejandro Trejo Pizzo · 2026-06-04.**
After eight paradigms confirmed the wrong-sign capstone — *every unconditional handle is a positivity giving
lower bounds; RH is an upper constraint* — the capstone itself dictates what a new path must be: **a mechanism
whose native output is an unconditional UPPER bound, not founded on a positivity.** There is exactly one such
machinery in modern mathematics that is *both* powerful *and* directly connected to $\zeta$: the **theory of
log-correlated fields and multiplicative chaos**, whose probabilistic methods (first/second moment, Girsanov,
branching-random-walk barriers) produce **upper bounds on extremes** unconditionally — the right direction,
without a positivity certificate. And it connects *directly* to the target we already cornered.

---

## 1. Why this escapes the capstone (the principled reason)

The capstone obstructs **positivity** (lower-bound oriented). The log-correlated / multiplicative-chaos toolkit
is the modern machinery that **natively produces upper bounds on the maxima and the fine structure of strongly
correlated fields** — e.g. the proof that $\max_{|h|\le1}|\zeta(\tfrac12+i(T+h))|\sim\log\log T$ (Arguin–Belius–
Bourgade–Radziwiłł–Soundararajan; Najnudel; Harper) is an **upper bound** obtained by a **second-moment /
Girsanov** argument, **not** a positivity. This is the first candidate whose mechanism is structurally on the
*upper* side the capstone says we need.

## 2. The direct connection to our cornered target (via Phase 10)

Phase 10 (P13, M10.3) proved: $\mathrm{RH}$ (regularized Hodge index / uniform Riesz) $\iff$ **uniform Muckenhoupt
$A_2$ on $E\sim\xi$** $\iff$ **extremal regularity of $S(T)=\frac1\pi\arg\zeta(\tfrac12+iT)$**. And:

> **$S(T)$ is a log-correlated field.** Its covariance $\mathbb E[S(t)S(t')]\sim-\frac1{2\pi^2}\log|t-t'|$
> (Bourgade; Najnudel; Selberg's CLT is its one-point marginal). So the **extremal $S(T)$ control that RH needs
> is exactly an extreme-value problem for a log-correlated field** — the home turf of multiplicative chaos.

So the two strands meet: the cornered target (U), in its Phase-10 form (extremal $S(T)$ / uniform $A_2$), is a
log-correlated extreme-value statement, and the log-correlated machinery gives **upper** bounds on exactly such
extremes. The new path is the **collision of our Phase-10 reformulation with the FHK/multiplicative-chaos
upper-bound technology.**

## 3. The thesis

> **Phase-12 thesis.** Use the log-correlated structure of $S(T)$ (and of $\log|\zeta|$) and the
> multiplicative-chaos / branching-random-walk **upper-bound** machinery to control the **extremal** $S(T)$
> over short intervals — equivalently, the tightest zero clusters / the uniform $A_2$ constant — *unconditionally
> and from above*. If the extreme tail can be pushed to the threshold the uniform frame bound needs, RH (via the
> Phase-10 equivalence) follows — through an **upper** bound obtained **without a positivity**.

This is the first route whose **direction** (upper) and **mechanism** (probabilistic extremes, not positivity)
are both what the capstone demands. It does not pre-reduce to a positivity the way Hodge and hyperbolicity did.

## 4. The honest open part, and the new mathematics

- **What is known (unconditional):** the leading-order max of $\zeta$ and of $S(T)$ over $[T,T+1]$
  (log-correlated leading term); the moments / multiplicative chaos in the subcritical regime (Saksman–Webb);
  Harper's sharp upper bounds on the low-moments / the "better than square-root cancellation."
- **What RH needs:** control of the **extreme tail** — the analog of the tightest pairs / the freezing
  transition / the second-order ($-\frac34\log\log T$) term and beyond, *uniformly*, down to the scale where a
  cluster would force an off-line zero. This is the **freezing / the extreme-tail** frontier — open, but in a
  field with rapid recent progress and **upper-bound-native methods**.
- **The new mathematics:** a *uniform-in-$T$, extreme-tail* multiplicative-chaos bound for $S(T)$ at the
  resolution of the minimum gap — sharper than the leading-order max, matched to the $A_2$ threshold. This is
  genuinely new (the freezing/extreme tail of $S(T)$ at minimal scale) and uses the right-direction machinery.

## 5. Milestones

- **M12.1 — confirm the log-correlated structure in our data.** From the zero data (and the deep-run windows),
  estimate the covariance of $S(T)$ across scales and verify the $-\frac1{2\pi^2}\log|t-t'|$ law; locate where
  the tightest pairs sit in the field's extreme excursions. *(Grounding; uses our existing machinery.)*
- **M12.2 — the $A_2$↔extreme-$S(T)$ dictionary, quantified.** Express the uniform $A_2$ constant / the
  regularized Hodge gap $\lambda_{\min}(G)=\frac{\pi^2}6\beta_{\min}^2$ explicitly in terms of the extreme of
  $S(T)$ over the window; identify the *exact* extreme-value threshold RH requires.
- **M12.3 — the multiplicative-chaos upper bound, applied.** Apply the second-moment / barrier upper-bound
  method to the windowed extreme of $S(T)$; determine how far the unconditional bound falls short of the M12.2
  threshold (price it, as we priced T9-A) — and whether the gap is the freezing second-order term (attackable)
  or the full extreme tail (the open core).
- **M12.4 — the capstone test (decisive).** Verify that the multiplicative-chaos upper bound is genuinely **not**
  a positivity at its foundation (first/second-moment + Girsanov are not PSD certificates) — i.e. that this route
  truly sits outside the capstone, unlike Phases 10–11. *This is the make-or-break of the whole phase.*

## 6. Honest assessment

- **Genuinely new to the program, recent, and — for the first time — direction-correct and mechanism-correct:**
  native **upper** bounds via **probability** (log-correlated extremes), not positivity. The capstone itself
  points here.
- **Direct, not speculative, connection** to our cornered target: Phase 10 already reduced RH to extremal $S(T)$
  regularity, and $S(T)$ is log-correlated. The two halves were built to meet.
- **Honest risk:** the extreme tail / freezing at minimal scale is open (it is, after all, RH-strength at the
  end), and the route may still hit a wall — but it is the **first** wall that would *not* be the wrong-sign
  capstone (the mechanism is upper-bound-native). Even a sharp pricing (M12.3) would be the first *upper*-side
  quantification the program has produced.
- **Odds:** small (it is RH), but this is the most principled "new path" the eight-paradigm analysis can point
  to — the one place the wrong-sign obstruction does not, on its face, apply.

### Status / next
- Rationale (native upper bounds, not positivity) + the $S(T)$ log-correlated bridge to Phase 10 — ✅.
- **Next: M12.1** — confirm the $-\frac1{2\pi^2}\log|t-t'|$ covariance of $S(T)$ in our zero data and locate the
  tight pairs in the field's extremes. Grounding the first non-positivity path.
