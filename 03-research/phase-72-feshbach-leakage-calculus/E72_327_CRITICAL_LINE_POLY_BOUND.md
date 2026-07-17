# E72.327 -- Critical-line polynomial bound for the cancelled Cauchy transform

**Purpose.** Close the `CRIT-POLY` input from E72.326. On the critical line of the shifted variable,
the cancelled Cauchy kernel is a bounded divided difference of the Fourier exponential. This gives a
polynomial bound without using RH.

## 1. Critical-line kernel

Let

```text
z=i gamma,        gamma real.
```

Then

```text
G_x(i gamma)
= (1-e^(i gamma L))sum_m xi_m/(i(i gamma)-d_m)
= (1-e^(i gamma L))sum_m xi_m/(-gamma-d_m).          (1)
```

Set

```text
u=-gamma.
```

Since `d_m=2pi m/L`,

```text
e^(iuL)=e^(-i gamma L).
```

The scalar multiplier is

```text
R_L(u,d_m):=(1-e^(-iuL))/(u-d_m).
```

At `u=d_m`, this is interpreted by the removable value:

```text
R_L(d_m,d_m)=iL.
```

## 2. Divided-difference bound

Because `e^(-id_mL)=1`,

```text
1-e^(-iuL)=e^(-id_mL)-e^(-iuL).
```

Thus

```text
R_L(u,d_m)
= [e^(-id_mL)-e^(-iuL)]/(u-d_m).
```

By the mean value theorem applied to `v -> e^(-ivL)`,

```text
|R_L(u,d_m)| <= L.                                      (2)
```

uniformly for all real `u` and all mesh points `d_m`.

## 3. Polynomial bound

Using (2),

```text
|G_x(i gamma)|
<= L sum_m |xi_m|.
```

If the active pole-even dimension is `N_L` and `||xi||_2=1`, then

```text
sum_m |xi_m| <= N_L^(1/2).
```

Therefore

```text
|G_x(i gamma)| <= L N_L^(1/2).                         (3)
```

In fixed compact height windows of the Phase 72 finite section, `N_L` is polynomial in `L`; hence

```text
|G_x(i gamma)| <= C_H L^B.
```

The same argument applies to finitely many Hermite derivatives in `gamma`: differentiating the divided
difference raises the bound by powers of `L`, still polynomial for fixed derivative order.

## 4. Status

```text
proved: CRIT-POLY for fixed critical-line zero windows, assuming polynomial active dimension N_L;
no zeta zero location input is used.
```

Combined with E72.326, the transformed route no longer needs a separate critical-line estimate.
