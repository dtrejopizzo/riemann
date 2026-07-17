# E73.003 - Critical divided-difference kernel for NAT-PROJ

## 1. Purpose

E73.002 proves that the Cauchy projection is a rational interpolation residue:

```text
H_b=sum_{k in K_L} Pi(b,k)G_K(k).
```

This note inserts the exact critical-line formula for `G_K(k)` and obtains a single finite mesh
functional.  This is the first form of `NAT-PROJ` with no Cauchy matrix inverse and no zero-tail
language.

## 2. Critical divided difference

Let

```text
k=i gamma,        gamma real,
d_m=2pi m/L.
```

Then

```text
G_K(k)
=(1-e^(kL))sum_m xi_m/(ik-d_m)
=(1-e^(i gamma L))sum_m xi_m/(-gamma-d_m).           (1)
```

Set

```text
u=-gamma.
```

Since `e^(-id_mL)=1`, the kernel is

```text
(1-e^(i gamma L))/(-gamma-d_m)
=(1-e^(-iuL))/(u-d_m)
=[e^(-id_mL)-e^(-iuL)]/(u-d_m).                      (2)
```

Thus

```text
G_K(i gamma)=sum_m xi_m DD_L(u,d_m),                  (3)
```

where

```text
DD_L(u,d):=[e^(-idL)-e^(-iuL)]/(u-d)
```

with removable value `iL` at `u=d`.

## 3. Compose with rational projection

From E73.002,

```text
H_b=sum_{k=i gamma in K_L} Pi(b,k)G_K(k).
```

Using (3),

```text
H_b=sum_m xi_m S_b(d_m),                              (4)
```

where the finite projection source is

```text
S_b(d_m):=
sum_{k=i gamma in K_L} Pi(b,k) DD_L(-gamma,d_m).      (5)
```

Therefore `NAT-PROJ` is exactly:

```text
max_{b in O_L} e^(Re b L)
 |sum_m xi_m S_b(d_m)| <= L^B.                        (6)
```

This is a finite mesh identity involving only:

```text
off-line zero window O_L;
critical zero window K_L;
finite pole-even vector xi;
Fourier mesh d_m.
```

## 4. Interpretation

The kernel `DD_L(u,d_m)` is a bounded divided difference:

```text
|DD_L(u,d_m)| <= L
```

on the real line.  That gives only a polynomial bound for `G_K(k)`, already known from E72.327.

The new requirement is much stronger: after applying the rational projection weights `Pi(b,k)`, the
mesh source `S_b(d_m)` must be almost orthogonal to the pole-even vector `xi` at the exponential scale
`e^(-Re b L)`.

Thus the next closure mechanism must use the finite pole-even equation for `xi`, not generic
divided-difference bounds.

## 5. The finite source criterion

Define

```text
SRC_b:=sum_m xi_m S_b(d_m).
```

Then:

```text
NAT-SRC:
max_{b in O_L} e^(Re b L)|SRC_b| <= L^B.              (7)
```

E73.002--E73.003 prove:

```text
NAT-SRC <=> NAT-PROJ.
```

This is the current sharpest finite identity.

## 6. Status

```text
proved: NAT-PROJ is equivalent to finite mesh source cancellation NAT-SRC;
open: prove NAT-SRC from the pole-even CCM equation, or identify it as the final finite obstruction.
```

