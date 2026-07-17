# E72.115 -- Mass alignment gate

**Date:** 2026-07-09.
**Role:** isolate the finite projection estimate behind the mass condition `(MOP)`.

## 0. Mass row

From E72.113:

```text
Mass_x(H,tau_j)=m_{x,H}Y_x(tau_j),
```

where:

```text
m_{x,H}
 = 1_H^TW_HB_xC_E^(-1)B_x^*P_H(2/(L sqrt(x)))L_{k_x}.
```

For fixed `x,H`, this is a finite row vector.  The root variable enters through the packet `Y_x(tau_j)`.

## 1. Exact alignment criterion

Let:

```text
e_{x,H}:=m_{x,H}^*/||m_{x,H}||_2
```

when `m_{x,H} != 0`.  Then:

```text
Mass_x(H,tau_j)
 = ||m_{x,H}||_2 <Y_x(tau_j),e_{x,H}>.                    (MALIGN)
```

Thus `(MOP)` is equivalent to:

```text
sup_{tau_j<=T} ||m_{x,H}||_2 |<Y_x(tau_j),e_{x,H}>| -> 0.
```

A useful sufficient split is:

```text
sup_{tau_j<=T}||m_{x,H}||_2||Y_x(tau_j)||_2=O(1),           (MNORM)
```

and:

```text
sup_{tau_j<=T}
 |<Y_x(tau_j),e_{x,H}>|/||Y_x(tau_j)||_2 -> 0.              (MORTH)
```

Then `(MOP)` holds.

### Proof

`(MALIGN)` is the definition of the normalized mass row.  Under `(MNORM)` and `(MORTH)`:

```text
|Mass_x(H,tau_j)|
 <= ||m_{x,H}||||Y_x(tau_j)||
    |<Y_x(tau_j),e_{x,H}>|/||Y_x(tau_j)|| -> 0.
```

`QED`

## 2. Diagnostic

The companion script:

```text
E72_115_mass_alignment_probe.py
```

reports:

```text
||Y||, ||m||, ||m||||Y||, |mY|, |mY|/(||m||||Y||).
```

Representative output:

```text
E72.115 mass alignment probe
 lam   N roots  max||Y||   ||m||    maxProd   max|mass|  maxRatio
   6  18     3 3.830e+01 1.96e-02 7.500e-01  9.332e-02 1.28e-01
   8  24     4 5.914e+01 1.09e-02 6.469e-01  4.973e-02 8.40e-02
  10  28     3 8.708e+01 6.17e-03 5.375e-01  4.051e-02 8.17e-02
  12  32     4 1.227e+02 4.92e-03 6.039e-01  2.100e-02 3.94e-02
  14  36     4 1.378e+02 2.37e-03 3.260e-01  1.601e-02 5.20e-02
```

The product `||m||||Y||` is bounded in these windows, but the actual mass is smaller by an alignment
factor.  Therefore the mass channel should be proved as a projection orthogonality, not by an
absolute norm estimate.

## 3. Updated final gate

E72.113 can be sharpened as:

```text
CCGD,
MNORM + MORTH,
TOP-q + TAIL-q
```

imply scalar WRL resonance annihilation.

This separates the two finite mechanisms:

```text
mass channel        -> one normalized projection e_{x,H},
flux energy channel -> finitely many singular projections v_l plus singular tail.
```

## 4. Status

```text
proved: MOP is equivalent to a finite mass projection condition;
observed: MOP is numerically an alignment effect;
open:   prove MNORM and MORTH uniformly.
```
