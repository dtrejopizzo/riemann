# Zeros data

This folder stores numerical values of the imaginary parts γ of nontrivial zeros of the Riemann
zeta function, in JSON form. The tables serve as fixed input for numerical checks in the research
phases and for the engine in `../engine/`, so that all computations use the same reference values.

## Contents

- `zeros_10000.json` — a flat list of the first 10,000 ordinates γ (starting 14.1347…).
- `zeros_gamma_100.json` — the first 100 ordinates under the key `zeros_gamma`.
- `zeros_cache.json` — a cache with keys `indices`, `gamma_values`, `N`, `K_N`, used to avoid
  recomputing zeros in repeated runs.

## Related folders

- [../engine/](../engine/) — code that reads these tables.
- [../validation/](../validation/) — notebook that checks the engine against these values.
- [../README.md](../README.md) — overview of the foundations folder.
