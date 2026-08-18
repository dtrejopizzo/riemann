# E101.050 - Periodic Cauchy endpoint localization

## 1. Fourier and Cauchy conventions

Let `f in W^(1,1)(0,L)` and define

```text
a_n=(1/L)integral_0^L f(x)exp(-i d_n x)dx,
d_n=2pi n/L.                                         (1.1)
```

For `z` outside the real mesh, put

```text
R_L(f;z)=sum_(n in Z) a_n/(z-d_n),
C_L(f;z)=z R_L(f;z).                                 (1.2)
```

One integration by parts gives `a_n=O_L(1/|n|)`.  Since
`(z-d_n)^(-1)=O_L(1/|n|)`, the series in (1.2) converges absolutely and
locally uniformly away from the mesh.

## 2. Exact periodic resolvent kernel

### Theorem 2.1

For `z` off the real mesh,

```text
R_L(f;z)
=-i e^(izL)/(1-e^(izL))
  integral_0^L f(x)e^(-izx)dx,                       (2.1)

C_L(f;z)
=-i z e^(izL)/(1-e^(izL))
  integral_0^L f(x)e^(-izx)dx.                       (2.2)
```

### Proof

The periodic resolvent kernel of `-i partial_x` is

```text
K_z(x)=(1/L)sum_(n in Z)e^(i d_nx)/(z-d_n).          (2.3)
```

On `0<x<L`, the equation

```text
(z+i partial_x)K_z=0                                 (2.4)
```

gives `K_z(x)=c e^(izx)`.  The unit jump of the periodic delta distribution
at zero gives

```text
i[K_z(0+)-K_z(L-)]=1,                                (2.5)
```

so

```text
c=-i/(1-e^(izL)).                                    (2.6)
```

Substituting (1.1) into (1.2), interchanging the absolutely convergent
resolvent series with the integral, and using

```text
K_z(L-x)=-i e^(iz(L-x))/(1-e^(izL))                 (2.7)
```

proves (2.1).  Multiplication by `z` proves (2.2). `QED`

The constant-function check is exact: if `f=1`, then only `a_0=1` and both
sides of (2.2) equal one.

## 3. Bilateral endpoint localization

Set `z=plus or minus i sigma`, `sigma>0`.  Formula (2.2) gives

```text
|C_L(f;i sigma)|
<=sigma/[1-e^(-sigma L)]
  integral_0^L |f(x)|e^(-sigma(L-x))dx,              (3.1)

|C_L(f;-i sigma)|
<=sigma/[1-e^(-sigma L)]
  integral_0^L |f(x)|e^(-sigma x)dx.                 (3.2)
```

Thus the upper safe half-axis sees only the right boundary layer, and the
lower safe half-axis sees only the left boundary layer.

Let `0<sigma_0<=sigma<=sigma_1`.  Then

```text
sup_sigma |C_L(f;i sigma)|
<=sigma_1/[1-e^(-sigma_0 L)] E_L^+(f),

sup_sigma |C_L(f;-i sigma)|
<=sigma_1/[1-e^(-sigma_0 L)] E_L^-(f),               (3.3)
```

where

```text
E_L^+(f)=integral_0^L |f(x)|e^(-sigma_0(L-x))dx,
E_L^-(f)=integral_0^L |f(x)|e^(-sigma_0x)dx.          (3.4)
```

No bulk norm of `f` appears.

## 4. One safe derivative

Differentiating (2.2) is legitimate locally uniformly away from the mesh.
On a compact safe interval, its derivative is bounded by a constant times

```text
integral_0^L (1+x)|f(x)|e^(-sigma(L-x))dx            (4.1)
```

on the upper axis, and by

```text
integral_0^L (1+x)|f(x)|e^(-sigma x)dx               (4.2)
```

on the lower axis.  Recenter the upper integral with `u=L-x`; the derivative
of the prefactor cancels the apparent factor `L` from differentiating
`e^(-izx)`.  Directly rewriting (2.2) as

```text
C_L(f;z)
=-i z/[1-e^(izL)]
  integral_0^L f(L-u)e^(izu)du                       (4.3)
```

for `Im z>0` shows that the correct upper weight is actually `(1+u)`, not
`(1+x)`.  The derivative of the denominator contributes an additional
factor `L e^(-sigma L)`, which is uniformly bounded and tends to zero on a
safe compact.  Likewise, the lower formula obtained by dividing numerator
and denominator by `e^(izL)` uses distance `x` from the left endpoint.
Hence the sufficient derivative conditions are

```text
E_(L,1)^+(f)
=integral_0^L(1+L-x)|f(x)|e^(-sigma_0(L-x))dx ->0,

E_(L,1)^-(f)
=integral_0^L(1+x)|f(x)|e^(-sigma_0x)dx ->0.         (4.4)
```

Under (4.4), `C_L(f;plus or minus i sigma)` and their first safe derivatives
tend to zero locally uniformly.

## 5. Finite Fourier sections

Let

```text
C_(L,N)(f;z)=z sum_(|n|<=N)a_n/(z-d_n).              (5.1)
```

For every fixed `L`,

```text
C_(L,N)(f;z)->C_L(f;z)                               (5.2)
```

locally uniformly with one `z` derivative.  Indeed, one integration by parts
gives

```text
|a_n|
<=[|f(L)-f(0)|+||f'||_1]/(2pi|n|),                  (5.3)
```

while the Cauchy denominator and its derivative contribute one and two more
powers of `1/|n|`, respectively.

The scalar normalization row satisfies

```text
sum_(n in Z)^sym a_n=[f(0)+f(L)]/2.                  (5.4)
```

For `f in W^(2,1)`, E101.049 gives the quantitative finite-section error.
For the directed argument, ordinary fixed-`L` convergence in (5.2)--(5.4)
is enough: after choosing `L`, take `N` large enough, also enforcing
`N/L->infinity` on the final diagonal.

## 6. Endpoint theorem for PROLATE-INBAND

Let

```text
f_L=k_lambda-k.                                      (6.1)
```

Assume

```text
PROLATE-ENDPOINT:
  E_(L,1)^+(f_L)+E_(L,1)^-(f_L)->0,
  f_L(0)+f_L(L)->0.                                  (6.2)
```

Assume also that the normalized boundary transforms `B_(y_N)` and their
first safe derivatives are locally bounded, as supplied by the LP/normality
infrastructure.  Then there is a cofinal diagonal `N(L)` such that

```text
q_(N,z)P_Nf_L->0                                     (6.3)
```

bilaterally and locally uniformly with one derivative.

### Proof

For the full Fourier series, (3.3)--(4.4) make the Cauchy term tend to zero,
while (5.4) and the last condition in (6.2) make the normalization term tend
to zero.  The local bounds on `B_(y_N)` preserve this product.  For each
fixed `L`, choose `N(L)` so large that the two finite-section errors in
(5.2)--(5.4), including their derivatives, are below a prescribed number
tending to zero.  Increase `N(L)` further if necessary so that
`N(L)/L->infinity`.  This proves (6.3). `QED`

## 7. Relation to the prolate estimates

The endpoint quantities in (6.2) are precisely the weighted form of the
physical and derivative endpoint errors recorded in P76.065.  They are
strictly weaker than the global `PROLATE-W21` condition of E101.049.

Therefore the direct in-band prolate observation does not require bulk
`W^(2,1)` convergence.  It requires only theorem-grade verification that the
recorded double-exponential endpoint bounds hold uniformly in the weighted
layers (4.4).

## 8. Revised RT-0

```text
RT-0a  periodic Cauchy endpoint theorem;                       proved;
RT-0b  fixed-L Fourier diagonal and N/L compatibility;         proved;
RT-0c  PROLATE-ENDPOINT for the precise prolate localization;  open.  (8.1)
```

`RT-0c` is zero-independent source analysis.  It is not the arithmetic
discriminant.

## 9. Status

```text
proved:
  exact periodic Cauchy kernel;
  bilateral localization to opposite endpoint layers;
  first-derivative weighted criterion;
  fixed-L Fourier passage and cofinal diagonal;
  PROLATE-ENDPOINT implication to the complete in-band observation;

superseded as a necessary hypothesis:
  global PROLATE-W21 from E101.049;

open:
  theorem-grade PROLATE-ENDPOINT for k_lambda-k;
  RT-2, recombined RDP-SHELL;
  RT-3, shifted safe leakage and DIRECTIONAL-IDENT.
```
