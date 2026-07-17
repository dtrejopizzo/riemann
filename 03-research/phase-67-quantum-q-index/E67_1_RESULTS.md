# E67.1 Results — archimedean coherent-kernel matching

**Date:** 2026-07-06.
**Script:** [E67_1_arch_match.py](E67_1_arch_match.py).
**Exact source:** `../../04-papers/P52-riemann-proof-audit/h8lab.py`, using only
`hA_taylor + pick_jet` to build the exact P52 archimedean Pick jet `A_N`.

## Test

Compare `A_N` against the `q -> 1` positive-discrete-series coherent kernel on the half-plane:

```text
K_alpha[j,k] =
  exp(i*pi*alpha/2) (-1)^k (alpha)_{j+k}/(j! k!)
  (2 i y)^(-alpha-j-k) tau^(j+k).
```

Allowed fit freedoms:

- exponent `alpha > 0`;
- local coordinate scale `tau`;
- one global positive scalar `c`.

No prime data, no `P_lambda`, no entrywise fitting.

## Output

The optimizer always chose:

```text
alpha = 1
tau   = 1
c     = log(t0 / 2pi)
```

Representative residuals:

| t0 | N=2 | N=4 | N=8 | N=12 | N=24 |
|---:|---:|---:|---:|---:|---:|
| 100 | 1.932e-3 | 1.859e-3 | 1.624e-3 | 1.485e-3 | 1.264e-3 |
| 1000 | 1.054e-4 | 1.015e-4 | 8.863e-5 | 8.101e-5 | 6.896e-5 |
| 1e6 | 4.463e-8 | 4.294e-8 | 3.752e-8 | 3.429e-8 | 2.919e-8 |

The fitted scalar satisfies `c / log(t0/2pi) = 1` to the printed precision for `t0=1e6`.

## Verdict

**PARTIAL / LEADING, not exact.**

The naive coherent kernel recovers the Szego leading term

```text
A_N = log(t0 / 2pi) * G_exact(N,y) + lower-order archimedean corrections.
```

This is not the exact matrix whitening required by P52. It is precisely the kind of scalar-leading
match that Phase 66 warned against. Therefore:

- the bare `q -> 1` `SU(1,1)` coherent kernel is **not enough** for E67.1;
- CAND-67 is not dead, but its archimedean sector must include the full Gamma/polygamma correction,
  not only the Bergman/Szego coherent kernel;
- any `QSC-exist` attempt that uses only `log(t0/2pi) * G_exact` is a Phase-66-style scalar
  approximation and must be rejected.

