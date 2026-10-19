# Phase 7 — The band-limited Carleson constant, the sine-kernel bridge, and the Connes core

The phase builds a rigorous, finite, computable reformulation of Weil positivity for band-limited test
functions (so the prime sum truncates automatically, avoiding the distributional pathology that
sank phase-6's pointwise attempt): the band-limited Carleson constant $C(d,T_0)$, with
$\mathrm{RH} \iff C(d,T_0) \le 1$ for all $d, T_0$. It then measures this constant numerically to test
whether prime incoherence (unique factorization) buys any positivity slack, identifies the second-order
structure of the form as the sine-kernel/GUE pair-correlation process, and compares the whole setup to
Connes–Consani's multiplicative (adelic) organization of Weil positivity.

## Results
- Band-limited Carleson reformulation of Weil positivity, with intrinsic threshold 1 and no free
  normalization: CONSTRUCTED/PROVED (exact identity $A_\Phi - P_F = \sum_\rho |f(\gamma_\rho)|^2$ for
  the zero-side Gram).
- Numerical measurement of $C(d,T_0)$ across heights $T_0 \in \{100,1000,5000,10^4\}$: $C \le 1$
  always, and $C \to 1$ exactly (margin $\to 0$) once primes up to $e^{2d} \gtrsim T_0^{0.85}$ are
  included: NUMERICAL. The only sub-unit margin occurs in a prime-deficient regime and is shown to be
  purely archimedean (zero-density vs. basis-dimension balance), not arithmetic.
- Clean negative verdict: prime incoherence (ℚ-linear independence of {log p}) contributes no
  exploitable positivity margin — adding primes pushes $C$ up toward saturation, never creates a
  buffer below 1; the positivity of $A_\Phi - P_F$ for true zeros is literally the realness of the
  zeros, i.e. RH itself: ARGUED/NUMERICAL (refutes the "prime incoherence as independent lever" hope
  with explicit numbers), consistent with the earlier no-gos (phase-6's $G_p$ indefiniteness, P8's
  Theorem C).
- Second-order (sine-kernel) bridge: the subdominant spectrum of $A_\Phi - P_F$ below the saturated
  top eigenvalue is identified with the reproducing-kernel Gram of the band-limited space, which is the
  sine kernel — i.e. the Montgomery–Dyson pair-correlation/GUE determinantal process: NUMERICAL/ARGUED
  (verified identity between the Gram and the sinc kernel to within $7 \times 10^{-2}$); interpreted as
  first order (Carleson constant = 1) being RH and second order being pair correlation, read at two
  scales of the same operator.
- Connes core comparison (phase-7c): the band-limited form is shown to be a prolate-spheroidal
  compression of Connes–Consani's archimedean operator $Q_c$ (bridge verified numerically via matching
  eigenvalue counts and transition widths); their proved archimedean positivity is confirmed to be the
  easy piece, and the obstruction is found to sit at the same place as in the band-limited approach:
  ARGUED/NUMERICAL, CITED for the Connes–Consani archimedean positivity theorem itself.

## Documents
- `P7-OPEN-CORE-carleson-saturation.md` — construction and measurement of the band-limited Carleson constant; the clean negative on prime incoherence.
- `P7b-second-order-sinekernel-bridge.md` — identification of the second-order structure with the sine kernel.
- `connes/P7c-connes-core-same-wall.md` — the prolate bridge to Connes–Consani's archimedean operator; `connes/prolate_bridge.py` computes it.
- `experiments/` — numerical engines (`carleson_band_engine.py`, `second_order_offline.py`, `second_order_sinekernel.py`) backing the measurements above.

## Relation to other phases
Follows directly from the refutation in `phase-6-osterwalder-schrader-reflection` (avoids its
distributional pitfall by band-limiting); its finding that the obstruction is the same wall as
Connes–Consani's and as P8's Theorem C (from `phase-4-handoff`) cross-confirms the cross-place nature
of the obstruction across independent frameworks.
