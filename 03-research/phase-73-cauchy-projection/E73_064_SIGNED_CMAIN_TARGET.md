# E73.064 - SIGNED-CMAIN target

## 1. Purpose

E73.063 shows that `DEN-GAP` is not a positive estimate.  It is a signed cancellation statement
for the finite CCM pole-even vector.

This document states the next target.

## 2. Definitions

For a FAR3 node `t=-gamma_k`, define:

```text
C_signed(t) := sum_n xi_n/(t-d_n),
C_abs(t)    := sum_n |xi_n|/|t-d_n|.
```

Then:

```text
|C_signed(t)| <= C_abs(t)
```

is true but far too weak.

## 3. SIGNED-CMAIN

The signed cancellation target is:

```text
SIGNED-CMAIN-8:
|C_signed(t)| <= C_sign L^-8 C_abs(t)
```

for every FAR3 node `t=-gamma_k`.

## 4. Why this implies CMAIN-10

E73.063 observes:

```text
C_abs(t) is about L^-1
```

on FAR3 nodes.  The uniform positive companion needed is:

```text
ABS-2:
C_abs(t) <= C_abs0 L^-2
```

or, with the observed weaker scale,

```text
ABS-1:
C_abs(t) <= C_abs0 L^-1.
```

Then:

```text
SIGNED-CMAIN-8 + ABS-2 => CMAIN-10,
```

and

```text
SIGNED-CMAIN-9 + ABS-1 => CMAIN-10.
```

The data support cancellation around `L^-8` to `L^-12`, so either split may be viable.

## 5. Load-bearing source

`SIGNED-CMAIN` must come from the finite eigenvector equation defining `xi`, not from Cauchy kernel
positivity.

The required identity should use:

```text
1. pole-even symmetry of xi;
2. the finite CCM spectral equation;
3. evaluation at the FAR3 critical heights.
```

## 6. Current endpoint

The route now reduces the main term to:

```text
finite eigenvector cancellation
for C_signed(t)=sum_n xi_n/(t-d_n)
at the FAR3 nodes.
```

This is the sharpest form of the arithmetic core reached so far in Phase 73.
