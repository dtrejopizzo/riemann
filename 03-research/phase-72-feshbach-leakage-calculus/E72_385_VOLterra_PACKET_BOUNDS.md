# E72.385 - Volterra packet bounds

## 1. Purpose

E72.384 reduces `BV-K` to Volterra packet estimates:

```text
int_0^L |A_z(r)|(K_c|X|)(r)dr,
int_0^L |D_M(r)|(K_c|X|)(r)dr,
```

where

```text
(K_c h)(r)=int_0^r e^(c(r-t))h(t)dt.
```

This note proves a general finite bound for these terms using only Parseval for the source packet
`X`.

## 2. Source packet norm

The source packet is

```text
X(t)=sum_{|n|<=M} xi_n e^(id_nt),
d_n=2pi n/L.
```

With `||xi||_2=1`, Parseval on `[0,L]` gives

```text
int_0^L |X(t)|^2dt = L.                                (1)
```

## 3. Volterra bound

For every `r`,

```text
(K_c|X|)(r)
<= [int_0^r e^(2c(r-t))dt]^(1/2) [int_0^r |X(t)|^2dt]^(1/2)
<= sqrt((e^(2cr)-1)/(2c)) sqrt(L).                    (2)
```

Thus

```text
(K_c|X|)(r) <= C_c sqrt(L)e^(cr).                     (3)
```

Therefore

```text
int_0^L |P(r)|(K_c|X|)(r)dr
<= C_c sqrt(L) int_0^L e^(cr)|P(r)|dr.                (4)
```

For `P=A_z` or `P=D_M`, Cauchy-Schwarz gives

```text
int_0^L e^(cr)|P(r)|dr
<= [int_0^L e^(2cr)dr]^(1/2)||P||_2
<= C_c e^(cL)||P||_2.                                (5)
```

Combining,

```text
int_0^L |P(r)|(K_c|X|)(r)dr
<= C_c sqrt(L)e^(cL)||P||_2.                          (6)
```

## 4. Norms of the packets

For the finite Dirichlet kernel

```text
D_M(r)=sum_{|m|<=M}e^(id_mr),
```

Parseval gives

```text
||D_M||_2 = sqrt(L(2M+1)).                             (7)
```

For

```text
A_z(r)=sum_m a_m(z)e^(id_mr),
a_m(z)=(1-e^(zL))/(iz-d_m),
```

Parseval gives

```text
||A_z||_2 = sqrt(L) |1-e^(zL)| [sum_m |iz-d_m|^(-2)]^(1/2).      (8)
```

For `z` in a fixed compact strip with `sigma=Re z>0`, the finite sum is bounded by

```text
sum_m |iz-d_m|^(-2) <= C_K L,
```

because the mesh spacing is `2pi/L` and the line is a fixed positive distance from the poles.
Therefore

```text
||A_z||_2 <= C_K L e^(sigma L).                        (9)
```

## 5. Consequences

The `A-X` term is bounded by

```text
A-X <= C_K L^(3/2) e^((c+sigma_K)L).                  (10)
```

The `D-X` term before multiplying by `|E_z|` is bounded by

```text
int_0^L |D_M(r)|(K_c|X|)(r)dr
<= C sqrt(L)e^(cL) sqrt(L(2M+1))
<= C L sqrt(M)e^(cL).                                  (11)
```

Multiplying by

```text
|E_z|=|1-e^(zL)| <= C_K e^(sigma_K L),
```

gives

```text
D-X <= C_K L sqrt(M)e^((c+sigma_K)L).                 (12)
```

In the tested Phase 72 windows, `M=O(L)` or at worst polynomial in `L`, so `D-X` is polynomial times
`e^((c+sigma_K)L)`.

## 6. Boundary term

The boundary term is

```text
Boundary_z(y)=1/L[A_z(L)conjugate(X(L-y))+A_z^#(L)X(L-y)].
```

Since `|A_z(L)|, |A_z^#(L)| <= sum_m |a_m(z)|`, Cauchy-Schwarz and the same sum as (8) give

```text
|A_z(L)|+|A_z^#(L)| <= C_K L^(1/2)e^(sigma_K L).
```

Then by Cauchy-Schwarz and Parseval for `X`,

```text
int_0^L e^(cy)|Boundary_z(y)|dy
<= C_K L^(1/2)e^(sigma_K L) L^(-1)
   [int_0^L e^(2cy)dy]^(1/2) ||X||_2
<= C_K L^(1/2)e^((c+sigma_K)L).                       (13)
```

## 7. Theorem

### Theorem 72.385

For every fixed compact shifted strip `K` and `c>0`, the packet gates `A-X`, `D-X`, and `BDRY` of
E72.384 satisfy

```text
A-X + D-X + BDRY <= C_K e^((c+sigma_K)L)L^B
```

provided the active bandwidth `M` grows at most polynomially in `L`.

Consequently `BV-K` holds under the same bandwidth condition.

### Proof

Equations (1)--(13) prove the three bounds.  Substitute them into E72.384. `QED`

## 8. Status

```text
proved: A-X/D-X/BDRY by finite Parseval and Cauchy-Schwarz;
proved: BV-K under polynomial active bandwidth;
feeds: NHW horizontal control from E72.383;
open: signed FarWall and finite-mesh tail remain.
```
