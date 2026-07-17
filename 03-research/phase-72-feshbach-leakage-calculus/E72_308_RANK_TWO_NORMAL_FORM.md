# E72.308 -- Rank-two normal form for the normalized MSD transform

**Purpose.** Factor the Loewner matrix of E72.307. The normalized transform `N_tau(z)` is not a
generic double sum: by parity it collapses to a rank-two scalar expression.

## 1. Loewner kernel factorization

Recall

```text
Phi_z(d)=d/(z^2+d^2).
```

For `a != b`,

```text
[Phi_z(a)-Phi_z(b)]/(a-b)
= (z^2-ab)/((z^2+a^2)(z^2+b^2)).                    (1)
```

Indeed,

```text
a(z^2+b^2)-b(z^2+a^2)
=(a-b)(z^2-ab).
```

Thus the Loewner matrix is the rank-two kernel

```text
L_z(m,n)
= (z^2-d_m d_n)/((z^2+d_m^2)(z^2+d_n^2)).
```

The diagonal value is the same formula with `m=n`:

```text
Phi_z'(d_m)=(z^2-d_m^2)/(z^2+d_m^2)^2.
```

## 2. Moment notation

Let

```text
s_m=s_m(tau)=2d_m/(tau^2-d_m^2),
```

and define

```text
U_j(z):=sum_m s_m^j xi_m/(z^2+d_m^2),
V_j(z):=sum_m s_m^j d_m xi_m/(z^2+d_m^2).
```

Because the mesh is symmetric, `xi_m=xi_-m`, `d_m` is odd, and `s_m` is odd. Hence

```text
U_1(z)=0,      V_0(z)=0,      V_2(z)=0.
```

## 3. Rank-two formula

E72.307 gives

```text
N_tau(z)
= -2/L sum_{m,n} xi_m xi_n (s_m-s_n)^2 L_z(m,n).
```

Using (1), split `L_z` as

```text
L_z(m,n)
= z^2/((z^2+d_m^2)(z^2+d_n^2))
 - d_m d_n/((z^2+d_m^2)(z^2+d_n^2)).
```

For any weights `a_m`,

```text
sum_{m,n} (s_m-s_n)^2 a_m a_n
=2( (sum_m s_m^2 a_m)(sum_m a_m) - (sum_m s_m a_m)^2 ).
```

Applying this to the two rank-one pieces and using the parity cancellations gives

```text
N_tau(z)
= -4/L [ z^2 U_0(z)U_2(z) + V_1(z)^2 ].              (2)
```

This is the normalized MSD transform in scalar normal form.

## 4. NZ-MSD in rank-two form

The compact nontrivial-zero target becomes

```text
NZ-MSD:
sum_rho (1-e^((rho-1/2)L))
  [ (rho-1/2)^2 U_0(rho-1/2)U_2(rho-1/2)
    + V_1(rho-1/2)^2 ]
= O_H(L^5).                                          (3)
```

The factor `L^5` instead of `L^4` absorbs the prefactor `-4/L` in (2).

For a single off-line packet with `z=rho-1/2`, `Re z>0`, the pointwise pressure is

```text
z^2 U_0(z)U_2(z)+V_1(z)^2
= O_H(L^5 e^(-Re(z)L))
```

after packet symmetrization.

## 5. Why this matters

The Loewner double commutator has now collapsed to three scalar resolvent moments:

```text
U_0(z),   U_2(z),   V_1(z).
```

Thus the remaining compact divisibility theorem is no longer a matrix identity. It is a rank-two
resolvent moment identity for the actual even ground vector `xi`.

This is the sharpest finite form reached so far in the compact-root branch.

E72.309 uses the Weyl root equation

```text
sum_m xi_m/(tau^2-d_m^2)=0
```

to reduce the rank-two expression further to

```text
N_tau(z)= -16 z^2 tau^2/(L(tau^2+z^2)) U_0(z)R_tau.
```
