# E72.132 -- Mass gain from complement coercivity

**Date:** 2026-07-09.
**Role:** close the remaining scalar mass gate modulo one explicit coercivity estimate.

## 0. Objects

Let:

```text
b_{x,H}=B_x^*W_H^T1_H,
c_{x,H}^{pm}(tau_j)=B_x^*P_HZ_x^{pm}(tau_j).
```

Then:

```text
Mass_x(H,tau_j)=b_{x,H}^*C_E^(-1)c_{x,H}^{pm}(tau_j).
```

## 1. Coercive mass theorem

Assume the following finite estimates for every fixed `H` and finite root-height window `T`:

```text
Complement coercivity:
C_E >= c_H L I                                                     (COER)

Post-main source bound:
sup_{tau_j<=T} ||b_{x,H}||||c_{x,H}^{pm}(tau_j)|| <= C_H.          (MSB)
```

Then:

```text
sup_{tau_j<=T}|Mass_x(H,tau_j)| <= (C_H/c_H)L^(-1) -> 0.          (MG)
```

### Proof

By `(COER)`:

```text
||C_E^(-1)b_{x,H}|| <= (c_HL)^(-1)||b_{x,H}||.
```

Therefore:

```text
|b^*C_E^(-1)c|
 <= ||C_E^(-1)b||||c||
 <= (c_HL)^(-1)||b||||c||
 <= (C_H/c_H)L^(-1).
```

This is `(MG)`. `QED`

## 2. Consequence for scalar WRL

Combining E72.127 and the theorem above:

```text
CGE-K + ROP + COER + MSB
=> scalar WRL resonance annihilation.
```

This is the current sharpest finite endpoint.

## 3. Diagnostic

The companion script:

```text
E72_132_mass_source_bound_probe.py
```

reports the source product `||b||||cpm||`, the Cauchy-Schwarz mass bound, and the actual mass.

Representative output:

```text
E72.132 mass source bound probe
 lam   L roots  ||b||  max||cpm||  ||b||||cpm||  massBound  actualMass
   6  3.58     3 2.45e+00  1.741e-01     4.269e-01 1.089e-01  9.332e-02
   8  4.16     4 3.18e+00  1.098e-01     3.498e-01 6.348e-02  4.973e-02
  10  4.61     3 2.86e+00  1.167e-01     3.340e-01 4.597e-02  4.051e-02
  12  4.97     4 3.60e+00  6.535e-02     2.353e-01 2.633e-02  2.100e-02
  14  5.28     4 3.41e+00  6.020e-02     2.053e-01 1.916e-02  1.601e-02
  16  5.55     5 3.74e+00  6.922e-02     2.585e-01 2.059e-02  1.688e-02
```

The source product `||b||||cpm||` is bounded in the tested windows, so the observed mass decay is
explained by the shorting coercivity factor.

## 4. Status

```text
proved: COER + MSB imply MG;
proved: CGE-K + ROP + COER + MSB imply scalar WRL;
observed: MSB is bounded in the finite harness;
open:   prove COER and MSB uniformly from the finite CCM construction.
```
