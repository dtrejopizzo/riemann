# E72.244 - Low-margin decomposition

## Purpose

E72.243 shows that the low block is controlled by the `2x2` invariants `t=Tr(B)` and `s=Tr(B^2)`.
This note separates the low margin:

```text
lowMargin = -Tr(B^3)-3Tr(BCC^*).
```

## Diagnostic

Script:

```text
E72_244_low_margin_decomposition_probe.py
```

Output:

```text
E72.244 low-margin decomposition probe
lowMargin=-TrB3-3BCC; auto gap check: 3s-t^2 >= s for 2x2 Hermitian.
lam -TrB3 -3BCC lowMargin s gap gap/s bccHelpFrac
 12 1.016915e-02 +7.743330e-04 1.094348e-02 4.716908e-02 1.007822e-01 2.137 +0.071
 16 1.011079e-02 +1.130253e-04 1.022382e-02 4.745727e-02 1.059321e-01 2.232 +0.011
 20 1.088083e-02 +3.616291e-04 1.124246e-02 4.919967e-02 1.026946e-01 2.087 +0.032
 24 1.599281e-02 +3.741454e-04 1.636695e-02 6.369185e-02 1.346332e-01 2.114 +0.023
 28 1.367062e-02 +1.936095e-04 1.386423e-02 5.773067e-02 1.264122e-01 2.190 +0.014
 32 2.048046e-03 +5.747763e-04 2.622823e-03 1.627185e-02 3.550938e-02 2.182 +0.219
 36 1.607003e-02 +2.980302e-04 1.636806e-02 6.387046e-02 1.345642e-01 2.107 +0.018
```

## Reading

The low margin is mostly the `2x2` cubic:

```text
lowMargin ~= -Tr(B^3).
```

The coupling term `-3Tr(BCC^*)` is usually a small bonus. It becomes useful at the delicate
`lambda=32` window, where it contributes about `22%` of the low margin.

For the `2x2` Hermitian block:

```text
t^2 <= 2s,
3s-t^2 >= s.
```

The data show:

```text
(3s-t^2)/s ~= 2.1.
```

Thus the low-side sign is structurally stable once `t<0` is proved.

## Consequence

The stable low proof can focus on:

```text
t_B <= -a/L,
s_B >= b/L,
```

with `t_B<0` supplied by the `K1` kernel average from E72.243. The `BCC` term can be treated as bonus
or retained only in finite delicate windows.
