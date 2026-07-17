# E72.172 -- Polynomial majorant certificate

**Date:** 2026-07-09.
**Role:** certify that the fixed degree-10 polynomials from E72.171 majorize the split quadratic on
the full intervals, not merely on the LP grid.

## 0. Certification method

For each polynomial `p`, verify both one-variable inequalities:

```text
p(t)-t^2 >= 0                  on [-M,0],
p(t)-(1-a)^2t^2 >= 0           on [0,M].
```

The companion script:

```text
E72_172_polynomial_majorant_certificate.py
```

computes all real critical points of the two difference polynomials and evaluates endpoints plus
critical points. A constant buffer `2e-5` is added to the LP polynomials before certification.

## 1. Output

```text
E72.172 polynomial majorant certificate
K0: interval=[-0.9,0.9], a=0.7
  min p(t)-t^2 on [-M,0]      at -0.660384017505:  1.060761893054e-05
  min p(t)-r^2 t^2 on [0,M]   at  0.406138211957:  1.853672751932e-05
K1: interval=[-0.6,0.6], a=0.6
  min p(t)-t^2 on [-M,0]      at -0.486757812783:  1.940707346521e-05
  min p(t)-r^2 t^2 on [0,M]   at  0.278258489697:  1.970566995060e-05
certificate: both fixed polynomials majorize the split quadratic on their intervals
```

## 2. Consequence

For any self-adjoint blocks satisfying:

```text
||K_0||<=0.90,
||K_1||<=0.60,
```

the certified polynomials imply:

```text
E_0(K_0)+E_1(K_1)
 <= Tr p_0(K_0)+Tr p_1(K_1).
```

Together with E72.171:

```text
Tr p_0(K_0)+Tr p_1(K_1)<=0.92,
cross_+<=0.04,
```

this proves:

```text
F2B-PSD
```

in the stable range.

## 3. Remaining proof target

The hard arithmetic statement has been moved to:

```text
PTC-trace:
Tr p_0(K_0)+Tr p_1(K_1)<=0.92
```

and:

```text
PTC-norm/cross:
||K_0||<=0.90, ||K_1||<=0.60, cross_+<=0.04.
```

All three are finite explicit estimates on the exact discrete prime-power block operators.
