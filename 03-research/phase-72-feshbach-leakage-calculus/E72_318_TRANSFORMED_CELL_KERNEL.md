# E72.318 -- Closed form for the transformed cell kernel

**Purpose.** Compute the transformed cell kernel which appears in `TPW`:

```text
KQ_z(y;n):=sum_m (1-e^(zL))/(iz-d_m) Q_y(m,n).
```

This is the first analytic gain after E72.317. The Cauchy multiplier is not arbitrary: it is the
periodic Green kernel for the Fourier mesh.

## 1. Fourier Green identity

Let

```text
d_m=2pi m/L.
```

For the complete Fourier mesh and `0<r<L`,

```text
sum_{m in Z} e^(i d_m r)/(z+i d_m)
= L e^(-zr)/(1-e^(-zL)).
```

Since

```text
iz-d_m = i(z+i d_m),
```

we get

```text
(1-e^(zL))sum_{m in Z} e^(i d_m r)/(iz-d_m)
= iL e^(z(L-r)).                                      (1)
```

Similarly,

```text
(1-e^(zL))sum_{m in Z} e^(-i d_m r)/(iz-d_m)
= iL e^(zr),                                          (2)
```

again for `0<r<L`.

These are exact Fourier identities. The factor `1-e^(zL)` has converted the Cauchy pole lattice into
an exponential transport kernel.

## 2. Integral representation of `Q_y`

With the normalization used in Phase 72,

```text
Q_y(m,n)
= (1/L) int_0^(L-y)
   [ e^(i d_m(t+y))e^(-i d_n t)
     + e^(-i d_m(t+y))e^(i d_n t) ] dt.                 (3)
```

For `m != n`, (3) gives

```text
Q_y(m,n)= [sin(d_m y)-sin(d_n y)]/[pi(n-m)],
```

and for `m=n`,

```text
Q_y(m,m)=2(1-y/L)cos(d_m y).
```

So (3) is exactly the earlier closed kernel.

## 3. Complete-mesh transformed cell

Insert (1)--(2) into (3). For `0<y<L`,

```text
KQ_z^infty(y;n)
= i int_0^(L-y)
   [ e^(z(L-t-y))e^(-i d_n t)
     + e^(z(t+y))e^(i d_n t) ] dt.                     (4)
```

Evaluating the integrals gives

```text
KQ_z^infty(y;n)
= i/(z+i d_n)
   [ e^(z(L-y)) - e^(i d_n y)
     + e^(zL)e^(-i d_n y) - e^(zy) ].                  (5)
```

This is the closed analytic form of the transformed cell.

## 4. Finite-mesh correction

In the finite CCM matrix the mesh is truncated to `|m|<=M_x`. Therefore

```text
KQ_z^M(y;n)=KQ_z^infty(y;n)-TailQ_z^M(y;n),
```

where

```text
TailQ_z^M(y;n)
= sum_{|m|>M_x} (1-e^(zL))/(iz-d_m) Q_y(m,n).          (6)
```

The exact finite theorem must keep (6). The complete-mesh formula is the main analytic identity; the
finite cutoff contributes a separate tail gate:

```text
TQ-tail:
sum_n xi_n TailQ_z^M(y;n)
```

is polynomially bounded after the same model-prime-archimedean combination.

## 5. Transformed prime current

Using (5), the prime part of E72.317 becomes

```text
T_Prime^infty(z)[xi]
= sum_{r<=e^L} Lambda(r)r^(-1/2)
   sum_n xi_n KQ_z^infty(log r;n).
```

Equivalently, putting `y=log r`,

```text
T_Prime^infty(z)[xi]
= i sum_{r<=e^L} Lambda(r)r^(-1/2)
   sum_n xi_n
   [ e^(z(L-y)) - e^(i d_n y)
     + e^(zL)e^(-i d_n y) - e^(zy) ]/(z+i d_n).        (7)
```

This should not be estimated termwise. It is the prime component of the combined transform

```text
T_W02 - T_WR - T_Prime.
```

## 6. Shifted Cauchy packets

Define the shifted Cauchy-Fourier packets

```text
H_+(z;y):=sum_n xi_n e^(i d_n y)/(z+i d_n),
H_-(z;y):=sum_n xi_n e^(-i d_n y)/(z+i d_n),
H_0(z):=sum_n xi_n/(z+i d_n).
```

Then (5) gives

```text
sum_n xi_n KQ_z^infty(y;n)
= i[ (e^(z(L-y))-e^(zy))H_0(z)
     - H_+(z;y)
     + e^(zL)H_-(z;y) ].                                (8)
```

Since

```text
C_x(iz)=-iH_0(z),
```

the transformed eigenvector equation is now an equation among shifted Cauchy packets.

## 7. Consequence for TPW

The remaining theorem `TPW` can be sharpened:

```text
TPW-packet:
after replacing every occurrence of Q_y by (8), the combined model-archimedean-prime functional
has polynomial strip growth, and the finite tail (6) is polynomially bounded.
```

This is strictly more explicit than E72.317. The exponential terms are visible:

```text
e^(zL)H_-(z;y),
e^(z(L-y))H_0(z).
```

They must cancel only in the combined Abel functional. Estimating them separately would recreate the
incoherent ceiling.

## 8. Status

```text
proved: complete-mesh Green identity (1)--(2);
proved: closed transformed cell formula (5);
proved: TPW reduces to a shifted Cauchy-packet Abel identity plus finite tail control;
open:   prove the combined packet Abel cancellation and TQ-tail.
```

The next lemma should apply the same Abel subtraction as E72.300--E72.305 to the packet formula (8).
