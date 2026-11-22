# CCM spectral triple engine

Python implementation of the Connes–Consani–Moscovici (CCM) spectral triple ("Zeta Spectral
Triples", arXiv:2511.22755). It was validated in Phase 60 and reused as the standard engine in
later phases (including Phase 64).

## What it computes

The engine builds the Weil quadratic form QW on a Hermite-style basis {U_k}, |k| ≤ N, extracts the
eigenvector of its lowest eigenvalue, and recovers the spectrum of the CCM operator as the real
roots of f(s) = Σ_k ξ_k/(s − 2πk/L).

**Observed (NUMERICAL).** With primes p ≤ 13 the float64 version reproduces the first ~6 nontrivial
zeros of ζ to machine precision.

**Interpretation (heuristic).** The operator is self-adjoint by construction, so its spectrum is
real at each finite level (λ, N); the question is moved to whether the limit N, λ → ∞ preserves the
reality of the roots (a Hurwitz-type approximation question rather than a positivity question).
This does not prove anything about RH; it is an instrument for studying that convergence.

## Contents

- [`ccm_operator.py`](ccm_operator.py) — the validated implementation (float64).
- [`ccm_operator_highprecision.py`](ccm_operator_highprecision.py) — the same construction in
  mpmath (dps = 40), used to measure convergence rates in N and λ; gives the ζ baseline against
  which functions violating RH (e.g. L_DH) are compared.
- [`ccm_operator_v1.py`](ccm_operator_v1.py) — an earlier, incorrect version kept for provenance:
  it computed the von Mangoldt term but discarded it (`QW=Q_arch*0.5`), producing a log-spacing
  ladder rather than the zeros.
- [`symbol_positivity_detector.py`](symbol_positivity_detector.py) and
  [`SYMBOL_POSITIVITY_DETECTOR.md`](SYMBOL_POSITIVITY_DETECTOR.md) — a Toeplitz-symbol detector
  for the terminal defect of the ARP-P path (Phase 67). Its scope note applies: it is faithful
  only at validated gauges (e.g. t0 ≈ 100), not gauge-uniform.

## Related folders

- [`../../03-research/phase-60-discriminant/`](../../03-research/phase-60-discriminant/) — the
  validation write-up (`CCM_VALIDATED.md`) and numerical gates.
- [`../../03-research/phase-67-quantum-q-index/`](../../03-research/phase-67-quantum-q-index/) —
  origin of the symbol detector.
- [`../validation/`](../validation/), [`../zeros-data/`](../zeros-data/), [`../README.md`](../README.md).
