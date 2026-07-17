# CCM Spectral Triple Engine

Implementation of the Connes–Consani–Moscovici (CCM) spectral triple ("Zeta Spectral Triples", arXiv:2511.22755), validated in Phase 60 of the theoretical program and reused as the standard engine in later phases (including Phase 64).

## Files

- **`ccm_operator.py`** — the validated, faithful implementation (float64). Builds the Weil quadratic form QW on a Hermite-style basis {U_k}, |k|≤N, extracts the eigenvector of its lowest eigenvalue, and recovers the spectrum of the CCM operator as the real roots of f(s) = Σ_k ξ_k/(s − 2πk/L). Reproduces the first ~6 nontrivial zeros of ζ to machine precision (float64) for primes p≤13.
- **`ccm_operator_highprecision.py`** — the same construction in mpmath (dps=40), used to measure convergence rates (N→∞ and λ→∞) rather than just hit a single precision target. Establishes the RH-true (ζ) convergence baseline against which RH-violating functions (e.g. L_DH) are compared.
- **`ccm_operator_v1.py`** — the earlier, non-faithful version (kept for reference/provenance). It computed the von Mangoldt term but discarded it (`QW=Q_arch*0.5`), producing a "stripped" log-spacing ladder rather than the actual zeros.

## Key result

The operator is self-adjoint by construction, so its spectrum is real automatically — it sidesteps the sign/positivity obstruction that blocked earlier routes. Each finite level (λ,N) gives real zeros of an approximant; **RH is then equivalent to whether the N,λ→∞ convergence preserves the reality of the roots** (a Hurwitz-type approximation-theory question, not a positivity question). This does not prove RH, but it is the first validated instrument in the program for attacking that specific convergence gap.

Source: `03-research/phase-60-discriminant/` (see `CCM_VALIDATED.md` there for the full validation writeup and numerical gates).
