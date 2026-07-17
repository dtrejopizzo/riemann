# E72.358 - CFIR divisor block theorem

## 1. Purpose

E72.354 reduced scalar compatibility to 2x2 Lambda-elimination minors.  E72.356 showed that the only
non-node-blind way to close those minors is divisibility by the Xi divisor.  E72.357 converted this
divisibility into finite Hermite principal-part blocks.

This note states the resulting theorem in the exact form needed by the Phase 72 route.

## 2. Data

Fix a finite Xi-zero contradiction window

```text
W_T={(a_j,m_j)}.
```

For each Hermite slot

```text
alpha=(a_j,r),        0<=r<m_j,
```

define the finite rows

```text
K_alpha := (1/r!) partial_z^r k_z |_{z=a_j},
S_alpha := (1/r!) partial_z^r S_z^{Xi} |_{z=a_j},
```

where

```text
S_z^{Xi}
```

is the exact non-scalar part of the Xi-window CFIR residual:

```text
R_z^{Xi}(Lambda)=Lambda k_z + S_z^{Xi}.
```

Let

```text
E=C_E-mu I,
Adj=Adj(E)
```

be the reduced adjugate.

## 3. Divisor block

For two Hermite slots `alpha,beta`, define the adjugate compatibility block

```text
M_{alpha,beta}
:= (S_alpha Adj)(K_beta Adj)^T
 - (S_beta Adj)(K_alpha Adj)^T.                      (1)
```

In the rank-one ground channel this is equivalent, up to a nonzero scalar factor, to

```text
M_{alpha,beta}
= (S_alpha xi)(K_beta xi)-(S_beta xi)(K_alpha xi).   (2)
```

The exact CFIR divisor-block condition is:

```text
M_{alpha,beta}=0
for every alpha,beta in the Hermite window.           (3)
```

The polynomial version is:

```text
|M_{alpha,beta}| <= C_T L^B
```

in the normalization of the transformed row.

## 4. Theorem

### Theorem 72.358

Assume the polynomial CFIR divisor-block condition for every fixed Xi-zero contradiction window:

```text
M_{alpha,beta}=O_T(L^B)
```

for all Hermite slots `alpha,beta`.  Assume also the scalar consistency gate:

```text
SCALAR-CONS:
the scalar recovered from any nondegenerate slot equals
Lambda_L=mu+e_pole-2kappa_*
up to polynomial error.
```

Then the Xi-window interpolation residual is scalar-compatible:

```text
(Lambda_L K_T+S_T^{Xi})Adj(E)=O_T(L^B).
```

Consequently

```text
R_T^{Xi}(Lambda_L)xi=O_T(L^B),
```

and the maximal-real-part Cauchy block of E72.324--E72.325 forces exponential suppression of the
off-line Hermite jets `J_TG_x`.

### Proof

The block condition says that the flattened vectors

```text
vec(S_T^{Xi}Adj),     vec(K_TAdj)
```

have all 2x2 minors polynomially small.  By E72.354, exact vanishing of these minors is equivalent to
the existence of a scalar `Lambda` such that

```text
(Lambda K_T+S_T^{Xi})Adj=0.
```

In the polynomial case, choose the slot with maximal `|K_alpha Adj|` in the fixed window and set

```text
Lambda_*=- (S_alpha Adj)/(K_alpha Adj)
```

in that scalar channel.  The 2x2 minor bounds give, for every `beta`,

```text
S_beta Adj + Lambda_* K_beta Adj = O_T(L^B)
```

after the chosen normalization.  This is the asserted scalar compatibility.

Since the reduced adjugate has range equal to the ground nullspace, scalar compatibility is equivalent
to

```text
R_T^{Xi}(Lambda_*)xi=O_T(L^B).
```

By `SCALAR-CONS`, the recovered scalar is the transformed coefficient `Lambda_L` up to polynomial
error.  E72.342 then gives

```text
H_T(L)J_TG_x + J_TTail_T^M = O_T(L^B).
```

On the maximal positive-real-part off-line cluster, E72.324--E72.325 identify the leading block of
`H_T(L)` as the invertible confluent Cauchy block multiplied by `diag(e^{a_jL})`.  Therefore the
corresponding Hermite jets are exponentially suppressed.  Descending over real parts gives the fixed
window suppression.  `QED`

## 5. What remains

The proof has now isolated the only new mathematical identity needed:

```text
CFIR-DIV:
For the exact Xi-derived non-scalar residual S_z^{Xi},
the blocks M_{alpha,beta} are polynomially small on every finite Xi-zero Hermite window.
```

By E72.357, this is equivalent to saying the two-variable minors

```text
Delta(z,w)
```

belong to the local ideal `(Z(z),Z(w))` up to polynomial error.

The remaining scalar gate is:

```text
SCALAR-CONS:
the scalar forced by the divisor block is the same Lambda_L already supplied by the transformed
Feshbach equation.
```

## 6. Status

```text
proved: divisor-block condition implies scalar-compatible CFIR;
proved: scalar-compatible CFIR feeds the existing maximal Cauchy forcing;
open: prove CFIR-DIV for the exact Xi-derived residual S_z^{Xi};
open: prove SCALAR-CONS without fitting Lambda after the fact.
```
