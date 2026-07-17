# Phase 69 -- the forcer on the gauge-robust exact signed index

**Opened:** 2026-07-07. Successor to Phase 68.

## Why this phase

Phase 67-68 built a rich picture but its central heuristic (the band-averaged Toeplitz symbol) turned
out **gauge-fragile** (E68.5-E68.6): faithful at some gauges (t0~100, marginal 0), false-negative at
others (t0=30,50,400), because the operator is not Toeplitz. So the forcer must be pursued on the
**exact, gauge-robust** object, not its symbol shadow.

## What survives from Phase 67-68 (do not rebuild)

- **The robust object:** `ind_-(A_N - P_lambda) = 0 <=> RH`, verified gauge-uniform and
  precision-robust: for zeta, `ind_- = 0` at every gauge t0 with min eigenvalue ~1e-16..1e-21
  (E68.5 cross-check). The marginality (`delta_N -> 0+`) is UNIFORM in the gauge -- a solid fact.
- **The signed certificate type:** Jantzen / negative-index, the right kind of object (E67.9-E67.11).
- **On-line zero = 0 negative squares**, exact (E67.11).
- **Localization:** the terminal difficulty concentrates near one frequency (theta ~ pi/2), the touch
  point where zeta is marginal (E67.19, E68.4) -- a genuine local picture, even if the symbol that
  revealed it is not gauge-uniform.
- **Arch sector Gamma_q**, zeta-free (E67.1b/c).

## The task

Prove `ind_-(A_N - P_lambda) = 0` for all N, by structure, **uniformly in the gauge** -- from the
Gamma_q archimedean carrier and the Euler/von Mangoldt data, without computing the zeros, without
`-zeta'/zeta` as a partition function, without fitting. This is the forcer, on the exact object.

The gauge-uniformity is now an asset, not just a demand: E68.5 shows the exact marginal index is
stable across gauges, so a proof can target the uniform structure directly rather than a single gauge.

## Plan

1. **Gauge-uniform marginality.** Characterize why `delta_N -> 0+` uniformly in t0 (E68.5). Is there a
   gauge-invariant quantity behind it (the Cayley/Moebius invariance `w_{1-rho}=1/w_rho`, the de Branges
   boundary)? A gauge-invariant reformulation would remove the fragile gauge dependence entirely.
2. **Exact signed certificate.** Work the Jantzen/negative-index on the exact whitened defect (not the
   symbol), using the Gamma_q structure, targeting a structural reason `ind_- = 0` for zeta and `> 0`
   for off-line.
3. **Falsifier throughout:** Davenport-Heilbronn and planted off-line zeros must break every mechanism.

## Honesty contract

Carried from Phase 67-68. No fabricated closure; every lemma passes a numerical gate; audit the audits.
If the forcer lands on the Weil wall, characterize it precisely -- that is itself a result.
