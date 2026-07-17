# E73.036 results - factor budget audit

## 1. Purpose

E73.035 splits the final critical data as

```text
g_cancelled(i gamma) = (1-exp(i gamma L)) C_raw(gamma).
```

E73.036 asks whether the projected Hermite gate needs hidden cancellation between critical nodes, or
whether the positive factor budget

```text
e^(alpha L) sum_k ||h_A(k)||_Herm |1-exp(i gamma_k L)| |C_raw(gamma_k)|
```

is already close to the actual projected output.

## 2. Computed table

```text
E73.036 factor budget probe
Audits whether CRIT-DIV-FACT survives absolute factor budgets after Hermite projection.
 lam     L sigma  gamma0  m nK    projected    absBudget   ratio    rawOnly    meshOnly    hermCeil  bestGamma  bestMesh    bestRaw
   8   4.159  0.05   14.13  2  6    5.466e-08    6.238e-08 8.76e-01  6.504e-08  1.481e-07  1.411e-07     32.935  1.176e+00  2.715e-09
   8   4.159  0.20   14.13  3  6    6.815e-07    7.739e-07 8.81e-01  8.079e-07  1.563e-06  1.538e-06     32.935  1.176e+00  2.715e-09
  12   4.970  0.10   14.13  2  6    2.656e-08    6.165e-08 4.31e-01  1.138e-07  2.658e-07  1.281e-07     37.586  1.502e+00  1.443e-09
  16   5.545  0.20   21.02  3  6    1.532e-06    3.890e-06 3.94e-01  5.560e-06  1.437e-05  8.303e-06     37.586  1.026e+00  1.312e-08
  18   5.781  0.20   14.13  3  6    9.308e-07    1.225e-06 7.60e-01  1.773e-05  8.993e-05  4.041e-06     30.425  5.078e-02  1.194e-07
  24   6.356  0.05   14.13  2  6    1.055e-07    1.086e-07 9.71e-01  7.594e-07  4.263e-06  4.909e-07     37.586  1.406e-01  7.074e-08
  24   6.356  0.20   21.02  3  6    2.287e-06    2.334e-06 9.80e-01  1.641e-05  5.661e-05  7.218e-06     37.586  1.406e-01  7.074e-08
```

Full output is reproduced by:

```text
python3 03-research/phase-73-cauchy-projection/E73_036_factor_budget_probe.py
```

## 3. Diagnosis

The ratio

```text
actual projected output / absolute factor budget
```

is often close to one.  Therefore the final gate is not relying on a large hidden cancellation among
the Hermite-projected critical nodes.

This is good news.  It means the final analytic target can be made positive:

```text
FBUD:
e^(alpha L) sum_k ||h_A(k)||_Herm |1-exp(i gamma_k L)| |C_raw(gamma_k)| <= L^B.
```

By the triangle inequality,

```text
FBUD => CRIT-DIV-FACT => DATA-HERM => NAT-PROJ.
```

Unlike earlier absolute ceilings, this one is not visibly destroyed in the tested windows.

## 4. What this changes

The remaining proof no longer needs a universal signed cancellation identity at the Hermite
projection level.  It can target the positive product budget:

```text
Hermite kernel size
times mesh-resonance defect
times finite Cauchy divisor defect.
```

This is the first positive inequality in the Phase 73 endpoint that survived the incoherent-ceiling
audit.

## 5. Next analytic target

Prove a finite product divisibility theorem:

```text
For every natural-height off-line Hermite cluster A with alpha=Re A>0,

e^(alpha L) sum_{gamma_k in K_L}
||h_A(i gamma_k)||_Herm
|1-exp(i gamma_k L)|
|C_x(i gamma_k)|
<= L^B.
```

This is stronger than the required signed gate but is now experimentally plausible.
