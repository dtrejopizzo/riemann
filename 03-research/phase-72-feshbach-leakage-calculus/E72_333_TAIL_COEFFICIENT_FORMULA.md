# E72.333 -- Closed coefficient formula for the finite Fourier tail

**Purpose.** Compute the coefficients `Lcal(b_m)` from E72.331. This turns `TAIL-COEFF` into an
explicit spectral divided-difference identity.

## 1. Tail coefficient

For a tail index `m` outside the active finite mesh and active indices `n` inside the mesh, define

```text
b_m(y):=sum_n xi_n Q_y(m,n).
```

Since `m` is outside and `n` is inside, `m != n`. Therefore

```text
Q_0(m,n)=0,
Q_L(m,n)=0,
```

and hence

```text
b_m(0)=b_m(L)=0.
```

Thus the endpoint defect `Arch_0` from E72.319 vanishes:

```text
Lcal(b_m)=sum_rho M_{b_m}(rho-1/2).                  (1)
```

No `kappa` term appears in the finite tail coefficients.

## 2. Mellin transform of one off-diagonal cell

For `m != n`,

```text
Q_y(m,n)= [sin(d_m y)-sin(d_n y)]/[pi(n-m)].
```

For any complex `w`,

```text
int_0^L e^(wy)sin(d_j y)dy
= d_j(1-e^(wL))/(w^2+d_j^2),
```

because `d_jL=2pi j`. Define

```text
Phi_w(d):=d/(w^2+d^2).
```

Then

```text
M_{m,n}(w)
:=int_0^L e^(wy)Q_y(m,n)dy
= (1-e^(wL))[Phi_w(d_m)-Phi_w(d_n)]/[pi(n-m)].       (2)
```

## 3. Coefficient formula

Combining (1)--(2):

```text
Lcal(b_m)
= sum_rho (1-e^((rho-1/2)L))
   sum_n xi_n
   [Phi_{rho-1/2}(d_m)-Phi_{rho-1/2}(d_n)]/[pi(n-m)].
                                                                  (3)
```

The zero sum is taken in the symmetric explicit-formula sense.

This is the exact tail coefficient.

## 4. TAIL-COEFF in closed form

E72.331 asks to prove

```text
sum_{|m|>M} (1-e^(zL))/(iz-d_m) Lcal(b_m)=O_K(L^B).
```

Using (3), this becomes

```text
TAIL-SPEC:
sum_{|m|>M} (1-e^(zL))/(iz-d_m)
sum_rho (1-e^(w_rho L))
   sum_n xi_n
   [Phi_{w_rho}(d_m)-Phi_{w_rho}(d_n)]/[pi(n-m)]
= O_K(L^B),                                           (4)
```

where

```text
w_rho=rho-1/2.
```

This is a finite/spectral identity with no hidden matrix language.

## 5. High-m expansion

For fixed `w` and active `n`, as `|m| -> infinity`,

```text
[Phi_w(d_m)-Phi_w(d_n)]/(n-m)
= Phi_w(d_n)/m + O_w(1/m^2)
```

because `Phi_w(d_m)=O(1/d_m)=O(L/m)`.

Thus the leading tail coefficient is

```text
Lcal(b_m)
= (1/m) sum_rho (1-e^(w_rho L))
     sum_n xi_n Phi_{w_rho}(d_n)/pi
   + O(1/m^2 * spectral factors).                     (5)
```

The leading spectral factor is the Stieltjes moment

```text
U_0(w_rho)=sum_n xi_n/(w_rho^2+d_n^2),
```

with an additional `d_n` in `Phi`. This is the same family of moments that appeared in E72.309--E72.310.

## 6. Meaning

The finite tail is not an unrelated estimate. Its leading coefficient is governed by the same
Mellin-Cauchy moments as the main compact obstruction. Therefore `TAIL-SPEC` must be proved together
with `MC-NZ`; separating it by absolute values would lose the cancellation.

## 7. Status

```text
proved: exact formula (3) for Lcal(b_m);
reduced: TAIL-COEFF to the explicit spectral tail identity TAIL-SPEC;
open:   prove TAIL-SPEC by pairing with the main MC-NZ/Cauchy moment cancellation.
```
