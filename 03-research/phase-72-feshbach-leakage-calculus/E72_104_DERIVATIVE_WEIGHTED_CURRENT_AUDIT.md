# E72.104 -- Derivative-weighted current audit

**Date:** 2026-07-09.
**Role:** test the residue-weighted version of the relative root-current subtraction.

## 0. Motivation

A divisor/current sum should not necessarily weight all roots equally. For a finite Weyl function:

```text
M_f(tau)=sum_n f_n/(tau-d_n),
```

the natural local residue normalization at a root is:

```text
1/M'_f(tau_j).
```

Thus the weighted relative current is:

```text
sum_{tau_A} D2_actual(tau_A)/M'_{xi}(tau_A)
 - sum_{tau_M} D2_model(tau_M)/M'_{k}(tau_M).
```

## 1. Probe

The companion script:

```text
E72_104_weighted_relative_current_probe.py
```

computes this derivative-weighted relative current and normalizes it by the weighted absolute ceiling.

## 2. Result

Representative relative ratios:

```text
lambda=12:
  s=5   relRatio=8.74e-01
  s=10  relRatio=9.25e-01
  s=15  relRatio=4.75e-01

lambda=20:
  s=5   relRatio=4.90e-01
  s=10  relRatio=6.80e-01
  s=15  relRatio=7.74e-01

lambda=24:
  s=5   relRatio=8.91e-01
  s=10  relRatio=8.68e-01
  s=15  relRatio=9.14e-01
```

Derivative weighting does not reveal a stable cancellation. In these tests it is generally worse than
the unweighted current.

## 3. Conclusion

The finite-band defect is not removed by the two most natural relative-current gauges:

```text
unweighted actual-minus-model roots,
derivative-weighted actual-minus-model roots.
```

The correct background gauge, if it exists, is more subtle than local residue normalization.

## 4. Status

```text
rejected: derivative-weighted relative current as the closure mechanism;
kept:     need for a model/background correction remains real;
open:     identify a canonical relative gauge compatible with HPAC.
```
