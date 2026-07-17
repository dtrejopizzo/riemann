# E72.345 -- Explicit CFIR row multiplier

**Purpose.** Identify the first, canonical candidate for the row multiplier `A_T` in E72.344.  The
multiplier is not arbitrary: it is the Hermite jet of the same Cauchy row used to derive the
transformed eigenvector equation.

## 1. Cauchy row

For shifted `z`, define the row vector on the active pole-even mesh

```text
k_z(m):=(1-e^(zL))/(iz-d_m).
```

Then

```text
G_x(z)=k_z xi.
```

The eigenvector equation is

```text
(C_E-mu I)xi=0.
```

Multiplying by `k_z` gives the exact row identity

```text
k_z(C_E-mu I)xi=0.                                  (1)
```

Expanding `C_E=W02-WR-Prime-e_pole I`, (1) is precisely

```text
T_W02(z)[xi]-T_WR(z)[xi]-T_Prime(z)[xi]
-(mu+e_pole)G_x(z)=0.                                (2)
```

Thus the transformed Feshbach equation has a canonical row multiplier: `k_z`.

## 2. Hermite jet multiplier

For the fixed window `W_T`, define

```text
A_T^0(L):=J_T k_z,
```

meaning the row matrix whose `(a_j,p)` row is

```text
(1/p!) partial_z^p k_z |_{z=a_j}.
```

Then

```text
A_T^0(L)(C_E-mu I)xi=0                               (3)
```

and, by (2),

```text
J_T[
T_W02-T_WR-T_Prime-(mu+e_pole)G_x
]=0.                                                  (4)
```

This identity is exact and finite.

## 3. Difference between `A_T^0` and CFIR

The CFIR defect from E72.342 is

```text
Def_CFIR,T
= J_T[
T_W02-T_WR-T_Prime
-2kappa_*G_x
-I_T^HG_x
+Tail_T^M
].
```

Using (4), this becomes

```text
Def_CFIR,T
= J_T[
Lambda_LG_x - I_T^HG_x + Tail_T^M
],                                                    (5)
```

where

```text
Lambda_L=mu+e_pole-2kappa_*.
```

This is E72.342(6).  Therefore the canonical multiplier `A_T^0` already accounts for the coupled
archimedean-prime-Feshbach part.  The only remaining algebra is the finite interpolation correction

```text
J_T[Lambda_LG_x-I_T^HG_x+Tail_T^M].                   (6)
```

## 4. Corrected row-ideal target

Let `R_T` be the row matrix for (6).  E72.344 asked for

```text
R_T=A_T(C_E-mu I)+S_T.
```

The canonical decomposition is now

```text
Full_CFIR_Row
= A_T^0(C_E-mu I) + R_T,                              (7)
```

where `Full_CFIR_Row xi=Def_CFIR,T`.

Thus all nontrivial content is concentrated in the interpolation row `R_T`, not in the original
transformed equation.

The sharpened endpoint is:

```text
INTERP-ROW:
R_T = A_T^1(C_E-mu I)+S_T,       ||S_T||<=C_TL^B.     (8)
```

Exact closure is `S_T=0`.

## 5. Why this matters

This separates the two algebraic layers:

```text
Layer 1: transformed Feshbach equation
         closed exactly by A_T^0=J_Tk_z.

Layer 2: finite zero-window interpolation residual
         open, encoded by INTERP-ROW.
```

So the remaining proof is not a re-proof of the transformed eigenvector equation.  It is the finite
Hermite interpolation row identity (8), with the signed tail collapsed by E72.343.

## 6. Status

```text
proved: A_T^0=J_Tk_z exactly kills the coupled transformed Feshbach equation;
reduced: CFIR-ROW to the interpolation row certificate INTERP-ROW;
open: construct A_T^1 or prove the determinant identities for R_T.
```
