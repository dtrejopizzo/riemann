# E78.78 - `TAIL/A` is governed by a radial average of `(-SAFEDELTA)/A`

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.77 named the next honest radial target:

```text
SAFEU-TAIL-COUPLING:
  TAIL_N(sigma_0,sigma) <= kappa(sigma) A_N.           (RAC-1)
```

This note identifies the exact quantity that governs that coupling.

## 2. Exact identity

From E78.71,

```text
TAIL_N(sigma_0,sigma)
 = -(1/2) ∫_{sigma_0}^{sigma} SAFEDELTA_N(t) dt.       (RAC-2)
```

Divide by the safe-u amplitude `A_N = N Delta safe_u_N` to get

```text
TAIL_N(sigma_0,sigma) / A_N
 = (sigma-sigma_0)
   * Avg_{[sigma_0,sigma]} [ (-SAFEDELTA_N(t)) / (2 A_N) ]. (RAC-3)
```

Equivalently,

```text
TAIL_N(sigma_0,sigma) / (A_N (sigma-sigma_0))
 = Avg_{[sigma_0,sigma]} [ (-SAFEDELTA_N(t)) / (2 A_N) ].   (RAC-4)
```

So the scale-coupled tail law from E78.77 is not arbitrary: it is exactly a
radial-average control problem for the normalized shell derivative

```text
(-SAFEDELTA_N) / A_N.                                   (RAC-5)
```

## 3. Probe audit on the common ladder

Companion:

```text
E78_78_radial_average_coupling_probe.py
E78_78_radial_average_coupling_results.json
```

Using the common zeta rows `sigma in {1.0,3.0}`, the probe compares

```text
TAIL_N / (A_N (sigma-sigma_0))                         (RAC-6)
```

against the pointwise proxy

```text
(-SAFEDELTA_N(i sigma)) / A_N.                         (RAC-7)
```

The observed alignment is strong:

```text
corr( TAIL/[A_N (sigma-sigma_0)], (-SAFEDELTA)/A_N )
  ≈ 0.976.                                             (RAC-8)
```

Representative rows:

```text
sigma=1.0, N= 8:
  TAIL/[A(σ-σ0)] ≈ 0.01557,
  (-SAFEDELTA)/A ≈ 0.04004

sigma=3.0, N= 8:
  TAIL/[A(σ-σ0)] ≈ 0.01187,
  (-SAFEDELTA)/A ≈ 0.03833

sigma=1.0, N=18:
  TAIL/[A(σ-σ0)] ≈ 0.00273,
  (-SAFEDELTA)/A ≈ 0.00705

sigma=3.0, N=18:
  TAIL/[A(σ-σ0)] ≈ 0.00209,
  (-SAFEDELTA)/A ≈ 0.00699.                            (RAC-9)
```

So the common ladder is consistent with a theorem-grade bound of the form

```text
(-SAFEDELTA_N(t)) / A_N <= M(t)                        (RAC-10)
```

which would imply

```text
TAIL_N(sigma_0,sigma) / A_N
 <= (1/2) ∫_{sigma_0}^{sigma} M(t) dt.                 (RAC-11)
```

## 4. Consequence

This sharpens E78.77 substantially:

```text
SAFEU-TAIL-COUPLING
<=
NORMALIZED-SAFEDELTA-AVERAGE:
  control (-SAFEDELTA_N)/A_N on the safe axis.         (RAC-12)
```

That is a better object because it is:

```text
- exact by integration,
- radial rather than shell-static,
- already native to E77.5g.                            (RAC-13)
```

So the next live target is no longer a generic `kappa(sigma)`, but an explicit
average of a certified shell derivative.

## 5. Honest reading

This note does not prove a cofinal bound for `(-SAFEDELTA_N)/A_N`.

What it proves is that this is the correct normalized integrand, and that the
common zeta rows support that identification much better than any raw relation
to the safe-u geometric ratio.

## 6. Status

```text
proved:
  TAIL/A is exactly a radial-average problem for (-SAFEDELTA)/A;

observed:
  on the common zeta ladder the normalized average
  TAIL/[A(σ-σ0)] correlates strongly (≈ 0.976) with the pointwise proxy
  (-SAFEDELTA)/A;

reduced:
  SAFEU-TAIL-COUPLING to the normalized derivative target
  NORMALIZED-SAFEDELTA-AVERAGE.
```
