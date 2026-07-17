# E72.302 -- Mellin spectral form of PNTERR-FORM

**Purpose.** Convert the remaining arithmetic error `PNTERR-FORM` into an explicit Mellin spectral
divisibility target. This is the finite identity sitting closest to scalar WRL.

## 1. PNTERR as a derivative pairing

From E72.301,

```text
PNTERR_tau
= int_0^L E(e^y)e^(-y/2)(F_tau'(y)-F_tau(y)/2)dy.
```

Set

```text
A_tau(y)=e^(-y/2)F_tau(y).
```

Since E72.299 proves

```text
F_tau(0)=F_tau(L)=0,
```

one has

```text
A_tau(0)=A_tau(L)=0,
```

and

```text
A_tau'(y)=e^(-y/2)(F_tau'(y)-F_tau(y)/2).
```

Thus

```text
PNTERR_tau=int_0^L E(e^y) A_tau'(y)dy.                (1)
```

## 2. Zero expansion

Write the Chebyshev error schematically as

```text
E(e^y)=psi(e^y)-e^y.
```

On a truncated height window, the explicit formula gives

```text
E(e^y)= - sum_{rho} e^(rho y)/rho + trivial/polar terms + tail.
```

Substituting into (1), each zero contributes

```text
- rho^(-1) int_0^L e^(rho y)A_tau'(y)dy.
```

By integration by parts and the endpoint cancellation of `A_tau`,

```text
int_0^L e^(rho y)A_tau'(y)dy
= -rho int_0^L e^(rho y)A_tau(y)dy.
```

Therefore the zero contribution is exactly

```text
int_0^L e^((rho-1/2)y)F_tau(y)dy.                    (2)
```

The factor `rho^(-1)` cancels. This is the Mellin spectral object.

## 3. Closed finite transform

Define

```text
M_tau(z):=int_0^L e^(z y)F_tau(y)dy.
```

Using

```text
F_tau(y)
= sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [sin(d_m y)-sin(d_n y)]/[pi(n-m)],
```

and `d_m L=2pi m`, one has for every complex `z`

```text
int_0^L e^(z y)sin(d_m y)dy
= d_m(1-e^(zL))/(z^2+d_m^2).                         (3)
```

Hence

```text
M_tau(z)
= (1-e^(zL))
   sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [ Phi_z(d_m)-Phi_z(d_n) ]/[pi(n-m)],               (4)
```

where

```text
Phi_z(d)=d/(z^2+d^2).
```

Equivalently, since `d_m-d_n=2pi(m-n)/L`,

```text
M_tau(z)
= -2(1-e^(zL))/L
   sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [ Phi_z(d_m)-Phi_z(d_n) ]/(d_m-d_n).               (5)
```

This is a completely finite divided-difference formula.

## 4. Spectral PNTERR identity

Combining (2) with the explicit formula gives the finite-height schematic identity

```text
PNTERR_tau
= sum_rho M_tau(rho-1/2)
   + trivial/polar contribution
   + explicit tail.                                  (6)
```

The exact version uses the usual symmetric height truncation and the corresponding explicit-formula
tail. No zero is inserted into the construction of `M_tau`; zeros only appear when the Chebyshev error
is spectrally expanded.

## 5. Divisibility target

If `rho=beta+i gamma` is off the critical line, then

```text
M_tau(rho-1/2)
```

contains the factor `1-e^((rho-1/2)L)`. For `beta>1/2`, this grows like

```text
e^((beta-1/2)L)
```

unless the divided-difference sum in (5) annihilates it.

Thus the precise Mellin spectral divisibility target is:

```text
MSD-FORM:
For every compact root-height window H and every zero rho in the explicit-formula window,
the finite divided-difference sum

S_tau(z)
:= sum_{m != n} xi_m xi_n (s_m-s_n)^2
   [ Phi_z(d_m)-Phi_z(d_n) ]/(d_m-d_n)

has the cancellation needed at z=rho-1/2 to make
sum_rho M_tau(rho-1/2)=O_H(L^4).
```

Equivalently, the finite transform `M_tau(z)` must be divisible, in the scalar WRL sense, by the
finite spectral obstruction carried by the off-line zero factors.

## 6. Current route

After E72.301 and E72.302, the compact-root FORM route is:

```text
ARCH-FORM
+ explicit-formula tail/trivial bounds
+ MSD-FORM
=> PNTERR-FORM
=> FORM-DCB
=> DCB
=> fixed-height compact-root HPAC decay.
```

This is no longer a matrix stress test. The remaining arithmetic content is the finite Mellin
divisibility identity (5) evaluated at the spectral parameters `z=rho-1/2`.
