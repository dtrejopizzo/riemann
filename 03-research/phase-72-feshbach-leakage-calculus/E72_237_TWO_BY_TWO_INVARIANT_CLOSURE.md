# E72.237 - Two-by-two invariant closure

## Purpose

This note turns the low-block sign into a basis-free `2x2` invariant.

For any `2x2` matrix `B`, Cayley-Hamilton gives:

```text
B^2 - (Tr B)B + (det B)I = 0.
```

Multiplying by `B` and taking trace gives:

```text
Tr(B^3) = (3 t s - t^3)/2,      t=Tr(B), s=Tr(B^2).       (2x2C)
```

Thus:

```text
t<0 and 3s-t^2>0  =>  Tr(B^3)<0.
```

## Diagnostic

Script:

```text
E72_237_two_by_two_invariant_closure_probe.py
```

Output:

```text
E72.237 two-by-two invariant closure probe
For 2x2 B: TrB3 = (3 t s - t^3)/2, t=TrB, s=TrB2.
lam tB sB gap3s-t2 TrB3 formulaErr tailPlus lhsLow lhsLow/tail
 12 -2.018045e-01 4.716908e-02 +1.007822e-01 -1.016915e-02 0.0e+00 +1.491131e-03 -1.094348e-02 7.339
 16 -1.908920e-01 4.745727e-02 +1.059321e-01 -1.011079e-02 1.7e-18 +9.182290e-04 -1.022382e-02 11.134
 20 -2.119065e-01 4.919967e-02 +1.026946e-01 -1.088083e-02 1.7e-18 +4.777648e-04 -1.124246e-02 23.531
 24 -2.375759e-01 6.369185e-02 +1.346332e-01 -1.599281e-02 0.0e+00 +6.784812e-04 -1.636695e-02 24.123
 28 -2.162864e-01 5.773067e-02 +1.264122e-01 -1.367062e-02 1.7e-18 +5.473822e-04 -1.386423e-02 25.328
 32 -1.153524e-01 1.627185e-02 +3.550938e-02 -2.048046e-03 4.3e-19 +5.122781e-04 -2.622823e-03 5.120
```

Here:

```text
tailPlus = Tr(D^3)+3Tr(D C^* C),
lhsLow   = Tr(B^3)+3Tr(B C C^*).
```

## Reading

The block inequality is already closed numerically by a large invariant margin:

```text
-lhsLow / tailPlus >= 5.12
```

on the tested stable windows.

The proof target becomes:

```text
Low invariant:
  t_B <= -a_L,
  3s_B-t_B^2 >= b_L,

Tail bound:
  Tr(D^3)+3Tr(D C^* C) <= T_L,

Coupled low bound:
  Tr(B^3)+3Tr(B C C^*) <= -M_L,

with M_L >= T_L.
```

The key simplification is that `Tr(B^3)` is now controlled by two scalar invariants `t_B` and `s_B`.

## Current Finite Closure Form

HOC3 follows from the following explicitly checkable finite inequalities:

```text
(I)   t_B < 0,
(II)  3s_B-t_B^2 > 0,
(III) -[ (3t_Bs_B-t_B^3)/2 + 3Tr(BCC^*) ]
      >= Tr(D^3)+3Tr(DC^*C).
```

This is the sharp current endpoint of the high-block cubic lemma.
