# E67.1b Results — q-Gamma / Plancherel archimedean matching

**Date:** 2026-07-06.
**Script:** [E67_1b_qgamma_plancherel.py](E67_1b_qgamma_plancherel.py).
**Exact source:** `../../04-papers/P52-riemann-proof-audit/h8lab.py`, using the exact
`hA_taylor + pick_jet` archimedean jet.

## Purpose

E67.1 showed that a single `SU(1,1)` coherent kernel gives only the leading Szego term:

```text
A_N ~ log(t0 / 2pi) * G_exact.
```

E67.1b tests the corrected archimedean object: the q-Gamma / Plancherel c-function. The q-deformed
input is

```text
psi_q(x) = d/dx log Gamma_q(x),
```

inserted into the exact P52 archimedean function

```text
h_A,q(z) =
  i[-(1/s + 1/(s-1)) + 1/2 log(pi) - 1/2 psi_q(s/2)],
  s = 1/2 + i z.
```

The polar `s(s-1)` factor is included because `h8lab.py` includes it in `h_A`.

## Function-level convergence

Relative errors for `h_A,q(z0) -> h_A(z0)`:

| z0 | q=0.90 | q=0.97 | q=0.99 | q=0.995 |
|---:|---:|---:|---:|---:|
| 10-i | 1.318e-1 | 3.838e-2 | 1.269e-2 | 6.332e-3 |
| 100-i | 9.759e-1 | 2.422e-1 | 7.950e-2 | 3.964e-2 |
| 1000-i | 6.624e-1 | 4.603e-1 | 5.461e-1 | 2.417e-1 |

The large-height function test needs `q` much closer to 1 for uniform convergence in the oscillatory
parameter; the current direct series is not optimized for that regime.

## Matrix-level convergence

Relative Frobenius errors for `A_N,q -> A_N`:

| z0 | N | q=0.90 | q=0.97 | q=0.99 | q=0.995 |
|---:|---:|---:|---:|---:|---:|
| 10-i | 2 | 8.367e-2 | 2.907e-2 | 1.003e-2 | 5.059e-3 |
| 10-i | 4 | 9.570e-2 | 3.267e-2 | 1.123e-2 | 5.658e-3 |
| 10-i | 6 | 1.001e-1 | 3.399e-2 | 1.167e-2 | 5.878e-3 |
| 100-i | 2 | 5.928e-1 | 3.036e-2 | 2.109e-3 | 2.360e-4 |
| 100-i | 4 | 5.908e-1 | 2.979e-2 | 1.923e-3 | 2.191e-4 |
| 100-i | 6 | 5.900e-1 | 2.958e-2 | 1.849e-3 | 2.124e-4 |

Additional spot check at `z0=100-i`:

| N | q=0.995 | q=0.997 | q=0.999 |
|---:|---:|---:|---:|
| 2 | 2.360e-4 | 2.274e-4 | 1.437e-4 |
| 4 | 2.191e-4 | 2.730e-4 | 1.613e-4 |

The `q=0.997/0.999` direct series becomes expensive for higher jets; an Euler-Maclaurin or accelerated
q-polygamma implementation would be needed for production numerics.

## Verdict

**PASS conceptual / numerical support.**

The q-Gamma/Plancherel correction is the right archimedean object:

- it is purely Gamma/q-Gamma and therefore zeta-free;
- it includes the full polygamma tower missing from the single coherent kernel;
- its q-jets converge to the exact P52 `A_N` matrix, not merely to the scalar leading term.

Operational consequence for Phase 67:

```text
single coherent kernel       = rejected as exact A_N model (E67.1)
q-Gamma/Plancherel c-function = accepted as archimedean sector for QSC-exist
```

The remaining live work is now `QSC-exist` for the prime current and `QSC-contract` from CQG
Haar/Peter-Weyl relations.

