# E72.392 - Tail absorbed into the zero-node system

## 1. Purpose

E72.391 proves that the finite Fourier tail is an explicit linear operator on the same nodal vector
`G_x(w)` that appears in the zero-node system.  This note inserts that operator into E72.322 and proves
that, at a polynomial active cutoff above the mesh scale, the tail is a lower-order perturbation of the
maximal-real-part Cauchy block.

This closes the earlier split:

```text
PAIR-Z plus TAIL-POLY
```

into one finite nodal system.

## 2. Tail kernel

From E72.391,

```text
Lcal(B_z^tail)
= -2i/L sum_w wG_x(w) R_M(z,w),                       (1)
```

where

```text
R_M(z,w)
:= sum_{|m|>M} (1-e^(zL))/[(iz-d_m)(w^2+d_m^2)].      (2)
```

The sum is symmetric in the Fourier tail indices.

## 3. Polynomial bound for the rational tail kernel

Fix compact shifted windows for `z,w`, away from kinematic coincidences with the Fourier mesh.  For
`|m|>M`,

```text
|d_m|asymp |m|/L,
```

and hence

```text
|iz-d_m| >= c_K |m|/L,
|w^2+d_m^2| >= c_K m^2/L^2
```

after increasing `M` by a fixed compact-dependent constant.  Therefore

```text
|1/[(iz-d_m)(w^2+d_m^2)]|
<= C_K L^3/|m|^3.
```

Summing the tail gives

```text
|R_M(z,w)| <= C_K e^(Re z L) L^3/M^2.                 (3)
```

Consequently the coefficient in (1) obeys

```text
|(-2i/L)wR_M(z,w)|
<= C_K e^(Re z L) L^2/M^2.                            (4)
```

## 4. Insert into the zero-node system

At a shifted zero node `z=a`, E72.322 gives

```text
D_aG(a)-sum_{w != a}K_{a,w}G(w)
= -Lcal(B_a^tail)+outside-window terms.
```

Using (1), the finite-window part becomes

```text
D_aG(a)
- sum_{w != a}K_{a,w}G(w)
- sum_w T^M_{a,w}G(w)
= outside-window terms,                              (5)
```

with

```text
T^M_{a,w}:=2i w R_M(a,w)/L.                           (6)
```

Thus the tail is not an error term.  It is an explicit matrix perturbation of the same nodal system.

## 5. Perturbative size on a maximal off-line cluster

Let `A={a_1,...,a_N}` be a maximal-real-part cluster in a fixed height window:

```text
Re a_j=alpha>0.
```

E72.324 proves that the leading block of `D-K` on `A` is

```text
-diag(e^(a_jL)) C_A,
C_A(j,k)=1/(a_j+a_k),
```

with `C_A` invertible.

By (4), the tail block on the same cluster satisfies

```text
|T^M_{a_j,a_k}| <= C_K e^(alpha L)L^2/M^2.            (7)
```

Therefore, relative to the leading block, the tail perturbation has size

```text
O_K(L^2/M^2).                                         (8)
```

Choose a polynomial active cutoff

```text
M >= L^(1+epsilon).
```

Then

```text
L^2/M^2 <= L^(-2epsilon) -> 0.                        (9)
```

Thus the finite Fourier tail is absorbed into the invertible maximal Cauchy block by a Neumann
perturbation argument.

## 6. Theorem

### Theorem 72.392

Fix a shifted zero height window and a compact shifted `z`-strip.  Assume the active Fourier cutoff
satisfies

```text
M >= L^(1+epsilon)
```

for some `epsilon>0`.  Then the finite Fourier tail contribution to the zero-node system is a
lower-order perturbation of the maximal-real-part off-line Cauchy block:

```text
|| C_A^(-1) diag(e^(-a_jL)) T^M_A || <= C_K L^(-2epsilon).
```

In particular, for all sufficiently large `L`, the tail cannot destroy the Cauchy-block forcing of
E72.324.

### Proof

The identity (1) is E72.391.  The rational kernel estimate is (3).  On a maximal cluster
`Re a_j=alpha`, (4) gives the same exponential scale `e^(alpha L)` as the leading Cauchy block, but
with the extra factor `L^2/M^2`.  Since `C_A` is a fixed invertible matrix in the chosen finite height
window, multiplying by `C_A^(-1)diag(e^(-a_jL))` gives (8).  The cutoff condition gives (9), and the
Neumann perturbation conclusion follows. `QED`

## 7. Status

```text
proved: finite Fourier tail is absorbed by maximal Cauchy-block nodal forcing;
requires: polynomial cutoff M >= L^(1+epsilon);
compatible with E72.389: D2BV/SFREQ allows any polynomial active bandwidth;
remaining: outside-window zero contribution and nodal-to-strip propagation.
```
