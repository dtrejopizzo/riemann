# E72.238 - Tail operator bound

## Purpose

E72.237 closes the block identity numerically with strong slack. This note tests a simple proof bound
for the tail:

```text
tailPlus = Tr(D^3)+3Tr(D C^* C).
```

Since only the positive part of `D` can increase the tail:

```text
Tr(D^3) <= Tr(D_+^3),
Tr(D C^*C) <= ||D_+|| op Tr(C^*C).
```

Thus:

```text
tailPlus <= Tr(D_+^3) + 3 ||D_+|| op ||C||_HS^2.       (TOB)
```

## Diagnostic

Script:

```text
E72_238_tail_operator_bound_probe.py
```

Output:

```text
E72.238 tail operator bound probe
tailPlus = Tr(D^3)+3Tr(D C*C); bound uses D_+ operator and HS coupling.
lam tailPlus DposCube DposOp Dpos2 C_HS2 bound ratio lowMargin/bound
 12 +1.491131e-03 2.716847e-03 1.033014e-01 3.581161e-02 3.690603e-03 3.860581e-03 2.589 2.835
 16 +9.182290e-04 2.098215e-03 8.165702e-02 3.379358e-02 3.465703e-03 2.947212e-03 3.210 3.469
 20 +4.777648e-04 1.609803e-03 7.637509e-02 2.938329e-02 2.346193e-03 2.147375e-03 4.495 5.235
 24 +6.784812e-04 1.334669e-03 7.628012e-02 2.563010e-02 2.731883e-03 1.959834e-03 2.889 8.351
 28 +5.473822e-04 1.193644e-03 7.424244e-02 2.478068e-02 2.183268e-03 1.679917e-03 3.069 8.253
 32 +5.122781e-04 8.728945e-04 6.253627e-02 2.169438e-02 3.199860e-03 1.473216e-03 2.876 1.780
```

Here:

```text
lowMargin = -[Tr(B^3)+3Tr(BCC^*)].
```

## Reading

The elementary tail bound loses a factor `2.6--4.5` against the signed tail, but the low margin still
dominates:

```text
lowMargin / TOB >= 1.78
```

on the tested stable windows.

## HOC3 Sufficient Package

The high-block odd cubic sign follows from:

```text
LOW:
  -[Tr(B^3)+3Tr(BCC^*)] >= M_L,

TAIL:
  Tr(D_+^3)+3||D_+||op||C||_HS^2 <= M_L.
```

Using the `2x2` identity for `B`, the low side can be written as:

```text
-[(3t_Bs_B-t_B^3)/2 + 3Tr(BCC^*)] >= M_L.
```

This reduces HOC3 to four scalar finite estimates:

```text
t_B, s_B, Tr(BCC^*), ||D_+||op, Tr(D_+^3), ||C||_HS^2.
```

All are defined from the exact model-whitened high plus-current and use no zero information.
