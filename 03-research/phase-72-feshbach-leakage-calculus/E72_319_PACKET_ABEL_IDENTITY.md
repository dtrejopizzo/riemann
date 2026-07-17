# E72.319 -- Packet Abel identity for the transformed PW equation

**Purpose.** Apply the explicit-formula/Abel subtraction to the transformed packet from E72.318.
This is the packet analogue of E72.300--E72.305, but without assuming endpoint vanishing.

The important new feature is that the endpoint term is not lost: it is proportional to the cancelled
Cauchy transform `G_x(z)` and can be moved back to the left side of the transformed eigenvector
equation.

## 1. Packet attached to the transformed kernel

For fixed `z`, define the transformed packet

```text
B_z(y):=sum_n xi_n KQ_z(y;n),
```

where `KQ_z` is the finite transformed cell. In the complete-mesh main term, E72.318 gives

```text
B_z^infty(y)
= i[ (e^(z(L-y))-e^(zy))H_0(z)
     - H_+(z;y)
     + e^(zL)H_-(z;y) ].
```

The finite packet is

```text
B_z^M(y)=B_z^infty(y)-B_z^tail(y).
```

This note treats an abstract packet `B`; the finite tail is carried separately.

## 2. Combined model-prime-archimedean functional

Define

```text
Lcal(B)
:= int_0^L (e^(y/2)+e^(-y/2))B(y)dy
   - WR(B)
   - sum_{r<=e^L} Lambda(r)r^(-1/2)B(log r).          (1)
```

Then the complete-mesh part of `TPW` is exactly

```text
T_W02^infty[z][xi]-T_WR^infty[z][xi]-T_Prime^infty[z][xi]
= Lcal(B_z^infty).                                    (2)
```

The finite CCM transform adds `-Lcal(B_z^tail)` with the inherited sign.

## 3. Abel identity with endpoints retained

Let

```text
A(y):=e^(-y/2)B(y),
E(e^y):=psi(e^y)-e^y.
```

Stieltjes integration gives

```text
sum_{r<=e^L} Lambda(r)r^(-1/2)B(log r)
= int_0^L e^(y/2)B(y)dy
   + [E(e^y)A(y)]_0^L
   - int_0^L E(e^y)A'(y)dy.                            (3)
```

Substitute into (1):

```text
Lcal(B)
= int_0^L e^(-y/2)B(y)dy
   - WR(B)
   - [E(e^y)A(y)]_0^L
   + int_0^L E(e^y)A'(y)dy.                            (4)
```

This is the correct endpoint-sensitive form.

## 4. Explicit formula contribution

Use

```text
E(e^y)
= -sum_rho e^(rho y)/rho
   - log(2pi)
   - (1/2)log(1-e^(-2y)).
```

For every term `E_*(y)` in this formula, the combination

```text
int_0^L E_*(y)A'(y)dy - [E_*(y)A(y)]_0^L
```

equals

```text
-int_0^L E_*'(y)A(y)dy
```

whenever the endpoint is interpreted with the same renormalization as `WR`.

Therefore the nontrivial-zero contribution is

```text
sum_rho int_0^L e^((rho-1/2)y)B(y)dy.                  (5)
```

The constant `-log(2pi)` contributes zero.

The trivial lattice contributes

```text
int_0^L e^(-5y/2)/(1-e^(-2y))B(y)dy.                  (6)
```

Combining (6) with the explicit low exponential in (4),

```text
int_0^L e^(-y/2)B(y)dy
+ int_0^L e^(-5y/2)/(1-e^(-2y))B(y)dy
= int_0^L e^(y/2)B(y)/(2sinh y)dy.                    (7)
```

Thus

```text
Lcal(B)
= sum_rho M_B(rho-1/2) + Arch_0(B),                   (8)
```

where

```text
M_B(w):=int_0^L e^(wy)B(y)dy,
```

and `Arch_0(B)` is the renormalized difference

```text
Arch_0(B)
:= Ren int_0^L e^(y/2)B(y)/(2sinh y)dy - WR(B).        (9)
```

When `B(0)=0`, `Arch_0(B)=0`, recovering E72.305.

## 5. Endpoint reduction for the transformed packet

For the transformed cell,

```text
Q_0(m,n)=2 delta_mn.
```

Therefore

```text
B_z(0)
= sum_n xi_n sum_m (1-e^(zL))/(iz-d_m)Q_0(m,n)
= 2(1-e^(zL))sum_n xi_n/(iz-d_n)
= 2G_x(z).                                             (10)
```

Since the renormalized archimedean defect `Arch_0(B)` depends only on the endpoint value `B(0)` in
the WR normalization, there is an explicit scalar `kappa_L` such that

```text
Arch_0(B_z)=2 kappa_L G_x(z).                          (11)
```

The constant is completely explicit from the chosen WR finite-part normalization:

```text
kappa_L
= Arch_0(1)
```

with the same cutoff `L`.

## 6. Renormalized transformed PW equation

Insert (8)--(11) into E72.317. The complete-mesh main gives

```text
(mu+e_pole)G_x(z)
= sum_rho M_{B_z^infty}(rho-1/2)
   + 2kappa_L G_x(z)
   - Lcal(B_z^tail).                                  (12)
```

Equivalently,

```text
(mu+e_pole-2kappa_L)G_x(z)
= sum_rho M_{B_z^infty}(rho-1/2)
   - Lcal(B_z^tail).                                  (13)
```

This is the endpoint-corrected packet form of `TPW`.

## 7. New proof target

Since the pole-even gap gives the left coefficient its coercive scale, `PW-Cauchy` follows from:

```text
Packet-zero bound:
|sum_rho M_{B_z^infty}(rho-1/2)| <= C L^B(1+|z|)^B,
```

and

```text
Packet-tail bound:
|Lcal(B_z^tail)| <= C L^B(1+|z|)^B.
```

The first is now an explicit transform of the closed packet (E72.318), and the second is a finite
Fourier cutoff estimate.

## 8. Status

```text
proved: endpoint-sensitive Abel identity (4);
proved: nontrivial-zero/trivial-lattice decomposition (8);
proved: Arch_0(B_z)=2kappa_L G_x(z);
reduced: TPW to packet-zero bound plus packet-tail bound in (13).
```

The next analytic task is to compute `M_{B_z^infty}(w)` from the closed packet formula and look for
factorization in `(1-e^((z+w)L))`, `(1-e^(zL))`, or the finite Weyl numerator.
