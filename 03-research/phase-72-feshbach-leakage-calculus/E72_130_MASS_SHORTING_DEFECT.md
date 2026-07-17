# E72.130 -- Mass shorting defect

**Date:** 2026-07-09.
**Role:** decide where the remaining mass leakage is created.

## 0. Three masses

For the post-main source:

```text
Z_x^{pm}(tau_j)=(2/(L sqrt(x)))K_x^E(tau_j)k_x,
```

there are three natural mass measurements on the physical band:

```text
preMass:
  1_H^TW_H P_HZ_x^{pm},

qMass:
  1_H^TW_H B_xB_x^*P_HZ_x^{pm},

postMass:
  1_H^TW_H B_xC_E^(-1)B_x^*P_HZ_x^{pm}.
```

The final mass gain `(MG)` is `postMass -> 0`.

## 1. Interpretation

If `preMass` is already small, then the integrated Loewner commutator creates an almost centered
source.

If `preMass` is not small but `qMass` is small, then the Feshbach complement projection kills the
mass.

If only `postMass` is small, then the cancellation is a genuine shorting effect and the proof must
use `C_E^(-1)`.

## 2. Diagnostic

The companion script:

```text
E72_130_mass_shorting_defect_probe.py
```

reports all three masses and the ratios `post/pre`, `post/q`.

Representative output:

```text
E72.130 mass shorting defect probe
 lam   L roots  max preMass  max qMass  max postMass  post/pre  post/q
   6  3.58     3   3.625e-01  3.573e-01    9.332e-02 2.574e-01 2.612e-01
   8  4.16     4   3.620e-01  2.733e-01    4.973e-02 1.374e-01 1.819e-01
  10  4.61     3   3.054e-01  2.901e-01    4.051e-02 1.326e-01 1.397e-01
  12  4.97     4   1.900e-01  1.883e-01    2.100e-02 1.105e-01 1.115e-01
  14  5.28     4   2.107e-01  1.725e-01    1.601e-02 7.600e-02 9.283e-02
  16  5.55     5   2.307e-01  2.124e-01    1.688e-02 7.316e-02 7.948e-02
```

The mass is not created small by the raw commutator or by complement projection.  It is damped by the
shorted inverse `C_E^(-1)`.

## 3. Status

```text
observed: preMass and qMass are O(1), while postMass/preMass decreases;
identified: MG is a shorting damping theorem for the mass functional;
open: prove the shorting damping uniformly from the spectrum/structure of C_E.
```
