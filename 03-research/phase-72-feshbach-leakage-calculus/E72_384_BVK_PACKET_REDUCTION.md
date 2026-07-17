# E72.384 - BV-K packet reduction

## 1. Purpose

E72.383 identifies the horizontal contour gate:

```text
BV-K:
int_{-L}^{L}e^(ct)|df_z(t)| <= C_K e^((c+sigma_K)L)L^B,
f_z(t)=B_z^M(|t|)1_{|t|<=L}.
```

This note reduces `BV-K` to explicit finite packet estimates for `B_z^M` and `B'_z`.

## 2. Even packet variation

Since `f_z(t)=B_z^M(|t|)` and `B_z^M(L)=0`,

```text
int_{-L}^{L}e^(ct)|df_z(t)|
<= |B_z^M(0)|(1+1)
 + int_0^L (e^(ct)+e^(-ct)) |(B_z^M)'(t)|dt.          (1)
```

The jump contribution at `t=0` is absent if the even packet is interpreted continuously; the displayed
endpoint term is a safe bound for the two one-sided variations.  Since `e^(-ct)<=e^(ct)`,

```text
int_{-L}^{L}e^(ct)|df_z(t)|
<=2|B_z^M(0)|+2int_0^L e^(ct)|(B_z^M)'(t)|dt.          (2)
```

Using `B_z^M(0)=2G_x(z)`, the endpoint part is already part of the transformed left coefficient.

Thus `BV-K` follows from:

```text
DBV-K:
int_0^L e^(ct)|(B_z^M)'(t)|dt
<= C_K e^((c+sigma_K)L)L^B.                           (3)
```

## 3. Derivative packet form

E72.337 gives

```text
(B_z^M)'(y)
=1/L int_0^(L-y)
 [ (-zA_z(t+y)-iE_zD_M(t+y))conjugate(X(t))
   +( zA_z^#(t+y)+iE_zD_M(t+y))X(t) ]dt
 -Boundary_z(y),                                      (4)
```

where

```text
E_z=1-e^(zL),
Boundary_z(y)=1/L[A_z(L)conjugate(X(L-y))+A_z^#(L)X(L-y)].
```

Therefore `DBV-K` follows from the finite estimates:

```text
A-X:
int_0^L e^(cy) int_0^(L-y)|A_z(t+y)||X(t)|dt dy
<= C_K e^((c+sigma_K)L)L^B,
```

```text
D-X:
|E_z| int_0^L e^(cy) int_0^(L-y)|D_M(t+y)||X(t)|dt dy
<= C_K e^((c+sigma_K)L)L^B,
```

and

```text
BDRY:
int_0^L e^(cy)|Boundary_z(y)|dy
<= C_K e^((c+sigma_K)L)L^B.
```

These are finite harmonic-analysis estimates on the active mesh.

## 4. A useful change of variables

In `A-X`, set `r=t+y`.  Then `0<=t<=r<=L`, so

```text
int_0^L e^(cy) int_0^(L-y)|A_z(t+y)||X(t)|dt dy
=int_0^L |A_z(r)| int_0^r e^(c(r-t))|X(t)|dt dr.       (5)
```

The same formula holds with `D_M` in place of `A_z`.  Thus the packet estimates are one-sided
Volterra convolutions:

```text
int_0^L |A_z(r)| (K_c|X|)(r)dr,
int_0^L |D_M(r)| (K_c|X|)(r)dr,
```

where

```text
(K_c h)(r)=int_0^r e^(c(r-t))h(t)dt.
```

## 5. Status

```text
proved: BV-K follows from DBV-K plus endpoint control;
proved: DBV-K reduces to A-X, D-X, and BDRY finite packet estimates;
reduced: natural-height horizontal control to explicit Volterra packet inequalities;
open: prove A-X/D-X/BDRY uniformly for the actual pole-even source packet X.
```
