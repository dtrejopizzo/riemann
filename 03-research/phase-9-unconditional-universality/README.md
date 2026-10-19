# Phase 9 — Unconditional gap universality: the Montgomery support barrier and its exchange rate

Phase 8 reduced the heat-flow attack to one irreducible target: unconditional, uniform-in-height control
of the tightest zero-pair gaps (extremal gap universality). This phase turns that target into a
structured program, tests one new "spearhead" functional meant to escape the earlier arithmetic-blindness
no-go, attacks Montgomery's pair-correlation support barrier head-on, and ends with a precise,
quantified exchange rate between partial unconditional progress on the support problem and certified
RH-verification up to an explicit height.

## Results
- Spearhead functional test (N6): every functional of the de Bruijn–Newman flow monotone under it falls
  into one of three classes — generic (universal, arithmetic-blind), archimedean (controls the zero
  count, not reality), or prime-aware via the explicit formula (its sign content is exactly Weil
  positivity, i.e. RH): PROVED (no-go), verified numerically on each case; closes the "arithmetic-aware
  monotone functional" escape route from the earlier N5 no-go.
- Program design (U): formalizes the needed target as unconditional, one-sided (lower-gap-only),
  extremal (not averaged) gap universality for ζ zeros, and surveys known partial results (Montgomery
  pair correlation, Rudnick–Sarnak n-level correlations, Katz–Sarnak function-field universality),
  identifying the common "support barrier" (Fourier support restricted to (−1,1)) as the shared
  obstruction: CITED survey, ARGUED reduction.
- T9-A (support barrier head-on): identifies the region beyond support 1 as governed by prime pair
  correlations / short-interval prime variance; shows the available unconditional tool
  ($F(\alpha) \ge 0$) gives lower bounds on clustering (small gaps exist) but not the needed upper
  bound (clustering is bounded) — a wrong-signed tool, the third occurrence of this directionality
  obstruction in the program: NO-GO (ARGUED, with indicative numerical computation of $F(\alpha,T)$).
- T9-cal (exchange-rate deliverable): derives a precise, rigorous-up-to-O(1) exchange rate
  $\alpha_{\mathrm{req}}(T) \asymp (T \log T)^{1/3}$ between unconditionally proven Montgomery support $A$
  and the height $T \sim A^3$ up to which the extremal collision margin (hence RH) would be certified:
  PROVED (derivation) / CALIBRATION (a concrete, named target for the field rather than a proof).

## Documents
- `PLAN-RH-PHASE9-unconditional-universality.md` — states target (U) and surveys the known landscape.
- `M9.1-N6-spearhead-verdict.md` — the spearhead functional no-go (N6).
- `T9A-verdict-wrong-sign.md` — the support-barrier/wrong-sign obstruction.
- `T9cal-DELIVERABLE-exchange-rate.md` — the quantified support-to-height exchange rate.
- `experiments/` — numerical scripts backing each verdict (`M9_1_spearhead.py`, `T9A_montgomery_F.py`, `T9cal_support_requirement.py`).

## Relation to other phases
Continues directly from `phase-8-heat-flow-monotonicity`'s upper-tail reduction; its final exchange-rate
calibration is the program's candid closing deliverable for the heat-flow/pair-correlation line of
attack.
