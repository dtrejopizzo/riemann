# Phase 71 -- CAND-1: zeta spectral triples, the operator-convergence front

**Opened:** 2026-07-07. Route: **CAND-1** (NO-GO-LIST §VII) -- Connes-Consani-Moscovici
"Zeta Spectral Triples" (arXiv:2511.22755, 2602.04022). Chosen deliberately because it is the
**one live candidate that is NOT on the positivity wall**: the operators `H_x` are self-adjoint
**by construction**, so there is no Weil-positivity inequality to prove; the open obstacle is
**operator convergence** `sp(H_x) → {zeros of ζ}`.

## Why this is not another circle

Phases 67-70 all reformulated `Ω_7` into Weil positivity = **MW-1** (documented master wall);
the archimedean-cushion / heat-flow / prolate levers are **MW-4 / NG-E1** (wrong sign, per-place
positivity refuted). CAND-1 changes the QUESTION from "is a form positive?" (impossible without RH)
to "do explicit self-adjoint operators converge?" -- open, not refuted, with 10^-55 numerical
evidence (6 primes reproduce the first zero).

## Engine (reused, not rebuilt)

The faithful CCM spectral-triple `QW` matrix already exists:
`../phase-60-discriminant/experiments/E4_ccm_faithful.py` (construction Thm 1.1 / eq 3.13-3.16),
and the convergence-horizon framing in `E6_convergence_horizon.py`. Phase 71 isolates the
**mechanism**, not the phase-60 discriminant thesis (which died, NG-F1).

## Results

- **[E71.1](E71_1_RESULTS.md)** -- reality mechanism. `sp(H)` is real because the CCM construction
  produces a self-adjoint finite operator; in the rational model this appears through roots of
  `f(s)=Σ ξ_k/(s−d_k)`. The tested ζ vectors have mixed signs and still all-real roots, so the
  mechanism is not Weil positivity. So:
  (1) CAND-1 is genuinely **off MW-1**; (2) the construction is **blind to off-line zeros as complex
  eigenvalues** -- an off-line zero can only appear as a **convergence failure**. 100% of RH content
  is localized in convergence. Confirmed the NO-GO-LIST CAND-1 characterization from inside.

- **[E71.2](E71_2_RESULTS.md)** -- convergence as detector: **confirmed live.** True ζ converges
  (`error→0`, all 5 zeros exact at N=40); a planted off-line zero makes convergence **stall** at a
  stable nonzero floor (~0.1-0.3, flat in N). So on the front that is off MW-1, convergence
  `sp(H_x)→{γ}` is a genuine RH-detector, not blind. **Next (E71.3):** the convergence rate for ζ
  and whether the finite Euler product (PNT-controlled, zero-independent) bounds it -- the E6 horizon
  on a mechanism now confirmed off the wall.

- **[E71.3](E71_3_RESOLVENT_CONVERGENCE_RATE.md)** -- convergence rate / PNT horizon. Separates the
  problem into finite-section convergence at fixed `lambda`, the `lambda->infinity` CCM horizon, and
  resolvent stability. Conclusion: PNT controls crude finite Euler input but cannot by itself prove
  the zero limit; the exact remaining theorem is zero-independent CCM resolvent convergence.
  Numerical output is recorded in **[E71.3 results](E71_3_RESULTS.md)**.

- **[E71.4](E71_4_RIESZ_WINDOW_STABILITY.md)** -- replaces nearest-root matching by Riesz-window
  stability: each isolating zero window must have rank one and its unique eigenvalue must converge.
  The first wide-window test is too coarse, so the corrected target is micro-contour Riesz stability.
  Results are recorded in **[E71.4 results](E71_4_RESULTS.md)**.

- **[E71.5](E71_5_HURWITZ_REAL_ROOT_CLOSURE.md)** -- removes the need to center contours at known
  zeros: if the normalized CCM characteristic functions have only real zeros and converge locally
  uniformly to `Xi`, Hurwitz/Rouche implies all zeros of `Xi` are real. The remaining theorem is
  exactly local uniform CCM characteristic convergence.

- **[E71.6](E71_6_CHARACTERISTIC_CONVERGENCE.md)** -- builds the natural entire function
  `Phi_N(s)=(2/sqrt(L))sin(sL/2)Σ xi_k/(s-d_k)` and starts testing function-level convergence to
  `Xi`; this is the first smoke test of the Hurwitz closure target. The raw scalar-normalized function
  fails to converge in **[E71.6 results](E71_6_RESULTS.md)**, so the next object must be the canonical
  CCM determinant/de Branges normalization.

- **[E71.7](E71_7_NOGO_WALL_AUDIT.md)** -- audits Phase 71 against the NO-GO list, Phase 53
  inverted-Stone wall, and the Phase 60 tribunal. Verdict: CAND-1 remains live only as a
  normal-family/Hurwitz convergence theorem for finite real-rooted CCM determinants; any appeal to
  global unitarity, positivity, or `epsilon_0>0` falls back into old walls.

- **[E71.8](E71_8_CANONICAL_PRODUCT_DETERMINANT.md)** -- tests the finite canonical product
  `Π(1-t²/r²)` over CCM roots. If the all-roots product is distorted by background finite-section
  roots, the required object is a native CCM relative determinant rather than a raw spectral product.
  Results are recorded in **[E71.8 results](E71_8_RESULTS.md)**.

- **[E71.9](E71_9_RELATIVE_BACKGROUND.md)** -- tests the first background candidate:
  divide the zeta all-root product by the archimedean/free all-root product from the same CCM window.
  This probes whether the spurious finite-section roots are removable by a zero-independent relative
  determinant. The arch/free quotient fails in **[E71.9 results](E71_9_RESULTS.md)**, pointing next
  to finite-dimensional perturbation/Fredholm determinants.

- **[E71.10](E71_10_MFUNCTION_DEBRANGES_TARGET.md)** -- corrects that next step: the relevant finite
  spectral object is not `det(QW-z)` but the Weyl m-function `m_N(s)=Σ xi_k/(s-d_k)` and its
  de Branges numerator. The remaining task is to find the canonical background subtraction for the
  log-derivative of this m-function.

- **[E71.11](E71_11_LOGDER_BACKGROUND.md)** -- tests canonical log-derivative backgrounds for
  `m_N`: all-root product, pole-relative `m_N'/m_N`, and sine-depoled
  `d log(sin(sL/2)m_N)/ds`, compared with `Xi'/Xi` on a zero-free interval. These simple
  backgrounds fail in **[E71.11 results](E71_11_RESULTS.md)**.

- **[E71.12](E71_12_PERSISTENCE_FILTER.md)** -- tests a dynamic, zero-independent background rule:
  roots persistent under finite-section refinement are physical, drifting roots are background.
  This is a detector for the relative determinant's stable divisor, not yet a proof object. Results
  are recorded in **[E71.12 results](E71_12_RESULTS.md)**.

- **[E71.13](E71_13_PERSISTENT_PRODUCT.md)** -- forms a provisional canonical product over the
  persistent clusters from E71.12 and compares it to `Xi/Xi(0)`. This tests whether the stable
  divisor carries the determinant shape before replacing clustering by an intrinsic projection.
  Results are recorded in **[E71.13 results](E71_13_RESULTS.md)**.

- **[E71.14](E71_14_STABLE_RIESZ_PROJECTION_TARGET.md)** -- converts the persistence success into
  the precise theorem target: construct intrinsic finite-section Riesz/Fredholm projections
  `Pi_N^phys` from CCM Weyl data whose determinants have real zeros and converge locally uniformly to
  `Xi/Xi(0)`.

- **[E71.15](E71_15_STABLE_PROJECTION_PROOF_ATTEMPT.md)** -- attempts the proof of E71.14. The
  compactness/Hurwitz half is proved conditionally from local counting and tail bounds; the remaining
  unproved core is the CCM Stable Divisor Identification proposition, which must identify the
  intrinsic stable divisor with the `Xi` divisor without using zeros.

- **[E71.16](E71_16_CONNES_FACT64_BRIDGE.md)** -- audits Connes `arXiv:2602.04022` and imports the
  strongest available bridge: Fact 6.4 proves `hat k_lambda -> Xi` uniformly on closed substrips of
  `|Im z|<1/2` for the prolate model vector. The remaining theorem becomes the precise
  eigenvector-approximation lemma `theta_x -> k_lambda`.

- **[E71.17](E71_17_STABLE_DIVISOR_REDUCTION.md)** -- proves the conditional stable-divisor
  reduction: if `hat theta_x-hat k_lambda -> 0` on compact substrips, then the finite real-rooted CCM
  divisor converges to the divisor of `Xi`, hence RH by Hurwitz. It also proves a standard
  operator-gap criterion reducing the missing estimate to `||H_x-H_x^0||=o(g_x)` for the
  prolate-vs-Weil model.

## Honesty contract

Carried from Phases 64-70. Self-adjointness by construction is real but must not be mistaken for a
proof: the spectrum is real for ANY input, so reality alone proves nothing -- the content is whether
the operators converge to the ACTUAL zeta zeros. DH/planted falsador mandatory. No false victory;
`sp(H_x)→{γ}` with all-real limit = RH is the target, and proving the convergence (not the reality)
is the CCM open frontier.
