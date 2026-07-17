# E72.103 -- Relative root-current audit

**Date:** 2026-07-09.
**Role:** test whether the persistent model defect in `D2` is removed by passing from pointwise
root-vanishing to a relative root-current subtraction.

## 0. Motivation

E72.101--E72.102 show that the absolute finite-band defect:

```text
D2_x(H,s;tau_j)
```

is already present in the model/prolate background. This is not surprising in light of E72.31 and
E72.68: the scalar WRL problem is post-main, while the HPAC finite-band certificate is still absolute.

The natural correction is not:

```text
D2(tau_j)->0 root by root,
```

but a relative current:

```text
sum_{actual roots} D2_actual - sum_{model roots} D2_model.
```

## 1. Probe

The companion script:

```text
E72_103_relative_root_current_probe.py
```

computes, for a fixed root-height window:

```text
RelD2 := |sum_A D2_actual(tau_A)-sum_M D2_model(tau_M)|,
```

and compares it to:

```text
sum_A |D2_actual| + sum_M |D2_model|.
```

## 2. Result

Representative relative ratios:

```text
lambda=12:
  s=5   relRatio=1.90e-01
  s=10  relRatio=1.83e-01
  s=15  relRatio=8.16e-01

lambda=20:
  s=5   relRatio=3.25e-01
  s=10  relRatio=5.68e-01
  s=15  relRatio=6.21e-01

lambda=24:
  s=5   relRatio=5.22e-01
  s=10  relRatio=4.61e-02
  s=15  relRatio=6.61e-01
```

There is occasional strong cancellation, but it is not robust across the tested `s`-windows.

## 3. Conclusion

The passage from pointwise roots to an unweighted relative root-current is conceptually better than
absolute pointwise `D2`, but it does not by itself close the defect.

The surviving lesson is:

```text
absolute D2 is too strong because it contains background,
unweighted relative D2 is too weak/coarse to expose a stable cancellation.
```

## 4. Status

```text
tested: unweighted relative root-current subtraction;
observed: sporadic but non-robust cancellation;
open: find the correct relative current weights or a different background gauge.
```
