# E72.309 -- Root-reduced rank-one form of normalized MSD

**Purpose.** Use the finite Weyl root equation to collapse the rank-two normal form of E72.308 to a
rank-one scalar product. This is a genuine algebraic cancellation, not an estimate.

## 1. Weyl root relation in even form

Let `tau` be a finite Weyl root for the even ground vector `xi`:

```text
sum_m xi_m/(tau-d_m)=0.
```

Since `xi_m=xi_-m` and the mesh is symmetric, this is equivalent to

```text
A_tau:=sum_m xi_m/(tau^2-d_m^2)=0.                  (1)
```

Indeed, pairing `d` and `-d` gives

```text
1/(tau-d)+1/(tau+d)=2tau/(tau^2-d^2).
```

For `tau != 0`, the root equation is exactly `tau A_tau=0`.

## 2. Moment definitions

E72.308 defines

```text
U_j(z)=sum_m s_m^j xi_m/(z^2+d_m^2),
V_j(z)=sum_m s_m^j d_m xi_m/(z^2+d_m^2),
```

with

```text
s_m=2d_m/(tau^2-d_m^2).
```

Set also

```text
R_tau:=sum_m xi_m/(tau^2-d_m^2)^2.                  (2)
```

## 3. First partial fraction: `V_1`

Since

```text
V_1(z)=sum_m 2d_m^2 xi_m/((tau^2-d_m^2)(z^2+d_m^2)),
```

and

```text
d^2/((tau^2-d^2)(z^2+d^2))
= tau^2/((tau^2+z^2)(tau^2-d^2))
  - z^2/((tau^2+z^2)(z^2+d^2)),
```

the root relation (1) gives

```text
V_1(z)= - 2z^2/(tau^2+z^2) U_0(z).                 (3)
```

## 4. Second partial fraction: `U_2`

Similarly,

```text
U_2(z)=sum_m 4d_m^2 xi_m/((tau^2-d_m^2)^2(z^2+d_m^2)).
```

The identity

```text
d^2/((tau^2-d^2)^2(z^2+d^2))
= tau^2/((tau^2+z^2)(tau^2-d^2)^2)
 - z^2/((tau^2+z^2)^2(tau^2-d^2))
 - z^2/((tau^2+z^2)^2(z^2+d^2))
```

together with (1) gives

```text
U_2(z)
= 4tau^2/(tau^2+z^2) R_tau
   - 4z^2/(tau^2+z^2)^2 U_0(z).                    (4)
```

## 5. Exact rank-one cancellation

E72.308 gives

```text
N_tau(z)=-(4/L)(z^2U_0(z)U_2(z)+V_1(z)^2).
```

Substitute (3) and (4). The `U_0(z)^2` terms cancel:

```text
z^2U_0U_2+V_1^2
= 4z^2tau^2/(tau^2+z^2) U_0(z)R_tau.
```

Therefore

```text
N_tau(z)
= -16 z^2 tau^2/(L(tau^2+z^2)) U_0(z)R_tau.        (5)
```

This is the normalized MSD transform at a finite root.

## 6. Consequence for NZ-MSD

The compact nontrivial-zero target becomes

```text
NZ-MSD:
R_tau * sum_rho
 (1-e^((rho-1/2)L))
 ((rho-1/2)^2 tau^2)/(tau^2+(rho-1/2)^2)
 U_0(rho-1/2)
= O_H(L^5).                                         (6)
```

The harmless constant factor `-16/L` has been absorbed into the `L^5` budget.

Equivalently, the root-level finite divisibility pressure is carried by a single scalar Stieltjes
moment:

```text
U_0(z)=sum_m xi_m/(z^2+d_m^2).
```

## 7. Reading

E72.308 reduced the problem to three moments `U_0,U_2,V_1`. E72.309 uses the finite Weyl root equation
to eliminate `U_2` and `V_1`. The remaining compact-root Mellin obstruction is a one-moment transform,
multiplied by the root energy `R_tau`.

This is the sharpest algebraic reduction so far:

```text
matrix double commutator
=> Loewner quadratic form
=> rank-two moments
=> root-reduced rank-one moment.
```

E72.310 rewrites the remaining moment as the finite Cauchy transform

```text
U_0(z)=iC_x(iz)/z,
```

so the compact target becomes a Mellin-Cauchy criterion.
