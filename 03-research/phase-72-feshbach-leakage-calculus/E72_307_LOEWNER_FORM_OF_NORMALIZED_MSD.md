# E72.307 -- Loewner form of the normalized MSD transform

**Purpose.** Rewrite the normalized transform `N_tau(z)` from E72.306 as a finite double-commutator
quadratic form. This removes the remaining unstructured double sum.

## 1. Divided-difference matrix

Let

```text
Phi_z(d)=d/(z^2+d^2).
```

Define the Loewner matrix

```text
L_z(m,n)= [Phi_z(d_m)-Phi_z(d_n)]/(d_m-d_n),       m != n.
```

The diagonal values may be chosen as `Phi_z'(d_m)`; they do not affect the double-commutator formula
below because they are multiplied by `(s_m-s_m)^2=0`.

Since

```text
d_m-d_n = 2pi(m-n)/L,
```

the normalized transform from E72.306 becomes

```text
N_tau(z)
= -2/L sum_{m != n} xi_m xi_n (s_m-s_n)^2 L_z(m,n).       (1)
```

## 2. Double-commutator form

Let `S=S_tau` be diagonal with entries `s_m`. For any matrix `L`,

```text
([S,[L,S]])_{mn}=-(s_m-s_n)^2 L_{mn}.
```

Therefore (1) is exactly

```text
N_tau(z)
= (2/L) <xi,[S_tau,[L_z,S_tau]]xi>.                  (2)
```

This is the normalized Mellin spectral divisibility transform in operator form.

## 3. Integral representation of the Loewner kernel

Since

```text
Phi_z(d)=1/2( 1/(z-id) - 1/(z+id) ) * (-i)
```

equivalently a rational combination of resolvents, `L_z` is a resolvent Loewner kernel. For
`d_m != d_n`,

```text
L_z(m,n)
= [Phi_z(d_m)-Phi_z(d_n)]/(d_m-d_n).
```

Thus all dependence on a possible off-line zero `z=rho-1/2` is carried by a finite resolvent
divided-difference matrix, not by prime sums.

## 4. Normalized NZ-MSD in Loewner form

Substituting (2) into E72.306 gives:

```text
NZ-MSD:
sum_rho (1-e^((rho-1/2)L))
  (2/L)<xi,[S_tau,[L_{rho-1/2},S_tau]]xi>
= O_H(L^4).                                          (3)
```

Equivalently, for an off-line packet `z,-z,conj z,-conj z`, the packet contribution is

```text
Packet_tau(z)
= (2/L) [
    (1-e^(zL))<xi,[S,[L_z,S]]xi>
  + (1-e^(-zL))<xi,[S,[L_{-z},S]]xi>
  + conjugates
].
```

## 5. Correct next finite identity

The strongest pointwise version is now:

```text
LOEWNER-POINT-MSD:
<xi,[S_tau,[L_z,S_tau]]xi>
= O_H(L^5 e^(-Re(z)L))
```

for every shifted off-line zero packet with `Re z>0`, after packet symmetrization.

The summed version is:

```text
LOEWNER-NZ-MSD:
sum_rho (1-e^((rho-1/2)L))
  <xi,[S_tau,[L_{rho-1/2},S_tau]]xi>
= O_H(L^5).
```

The extra factor `L` relative to `NZ-MSD` comes from the prefactor `2/L` in (2).

## 6. Reading

This is a genuine finite identity. The object to prove is no longer a raw Mellin transform or an
unstructured zero sum. It is a zero-divisor weighted family of Loewner double-commutators evaluated on
the actual ground vector `xi`.

This matches the earlier Phase 72 lesson that the surviving mechanism must be a commutator mechanism,
not an absolute-value prime estimate.

E72.308 factors the Loewner kernel and obtains the scalar normal form

```text
N_tau(z)=-(4/L)(z^2U_0(z)U_2(z)+V_1(z)^2).
```
