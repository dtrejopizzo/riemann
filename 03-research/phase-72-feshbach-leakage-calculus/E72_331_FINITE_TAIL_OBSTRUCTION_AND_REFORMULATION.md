# E72.331 -- Finite tail obstruction and the correct TAIL-POLY target

**Purpose.** Audit the remaining finite Fourier tail `TAIL-POLY`. A pointwise tail bound is false at
polynomial cutoff in right shifted strips. The only viable target is a smoothed `Lcal` tail identity.

## 1. Tail kernel

E72.318 defines

```text
TailQ_z^M(y;n)
= sum_{|m|>M} (1-e^(zL))/(iz-d_m) Q_y(m,n).
```

Using the integral form of `Q_y`, this tail is built from the Fourier remainder

```text
R_M(z;r)
:=(1-e^(zL))sum_{|m|>M} e^(id_m r)/(iz-d_m).
```

The complete series gives the exact Green kernel

```text
(1-e^(zL))sum_{m in Z} e^(id_m r)/(iz-d_m)
= iL e^(z(L-r)).
```

## 2. Pointwise polynomial tail is not available

For `Re z=sigma>0`, the coefficients satisfy

```text
|(1-e^(zL))/(iz-d_m)| ~ e^(sigma L) L/|m|.
```

A Dirichlet estimate can improve the summation from absolute `sum 1/m` to roughly `1/M` away from
endpoints, but it still gives the scale

```text
|R_M(z;r)| ~ e^(sigma L) L/M
```

at polynomial cutoff. Thus a pointwise bound

```text
|R_M(z;r)| <= L^B
```

would require an exponentially large cutoff `M`, unless additional cancellation is supplied by the
functional applied to the tail.

Therefore:

```text
pointwise Fourier-tail control cannot prove TAIL-POLY.
```

## 3. Correct target: smoothed tail after Lcal

The tail enters the transformed route only through

```text
Lcal(B_z^tail),
```

not through `sup_y |B_z^tail(y)|`.

Thus the correct theorem is:

```text
TAIL-POLY-Lcal:
|Lcal(B_z^tail)| <= C_K L^B
```

on fixed shifted compact sets.

This must use the combined functional

```text
Lcal(B)
= int_0^L (e^(y/2)+e^(-y/2))B(y)dy
   - WR(B)
   - sum_{r<=e^L}Lambda(r)r^(-1/2)B(log r),
```

before taking absolute values.

## 4. Exact coefficient form

Write

```text
B_z^tail(y)=sum_{|m|>M} a_m(z) b_m(y),
a_m(z):=(1-e^(zL))/(iz-d_m),
```

where

```text
b_m(y):=sum_n xi_n Q_y(m,n).
```

Then

```text
Lcal(B_z^tail)=sum_{|m|>M} a_m(z) Lcal(b_m).           (1)
```

The tail theorem becomes a coefficient estimate:

```text
TAIL-COEFF:
sum_{|m|>M} (1-e^(zL))/(iz-d_m) Lcal(b_m)
= O_K(L^B).                                           (2)
```

This is a finite explicit identity. It is the only acceptable form of `TAIL-POLY`.

## 5. Required decay of `Lcal(b_m)`

Since `a_m(z)` contains `e^(sigma L)/m`, polynomial boundedness of (2) follows if the combined
functional coefficients satisfy, for some fixed `delta>0`,

```text
Lcal(b_m)=O_K(e^(-sigma L) |m|^(-1-delta)L^B)
```

or if the signed series in (2) has an independent Abel/Dirichlet cancellation.

The first option is too strong unless `Lcal` supplies the same endpoint cancellation as the complete
mesh. The second option is the realistic one:

```text
TAIL-ABEL:
partial sums of Lcal(b_m) have enough cancellation to offset the cancelled Cauchy coefficient.
```

## 6. Status

```text
proved: pointwise finite Fourier tail is not polynomial at polynomial cutoff;
reduced: TAIL-POLY to the explicit signed coefficient identity (2);
closed: coefficient formula for Lcal(b_m) in E72.333;
open:   prove the resulting spectral tail identity TAIL-SPEC.
```

This prevents a false closure of the transformed route by an invalid tail estimate.
