# E82.001 - Exact projective generator endpoint

## 1. Coupled solution

Use the notation of E81.004 and put

```text
h_N=alpha_b u_N+beta_b v_N,
f_N=alpha_b s_N+beta_b 1,
M_N h_N=f_N.                                           (1.1)
```

Define the linear Cauchy functional

```text
L_{N,z}(h)=sum_j h_j/(z-d_j)+sum_j h_j/(d_j-d_b).      (1.2)
```

Then the exact numerator is

```text
G_N(z)=1+L_{N,z}(h_N).                                 (1.3)
```

No determinant, zero list or inverse of the scalar `c_N` occurs.

## 2. Fixed-L endpoint

Choose a safe point `z_*`.  The required convergence statement is

```text
PG-CONV:
G_N(z)/G_N(z_*) -> G_L(z)/G_L(z_*)                    (2.1)
```

locally uniformly on safe complex domains, with a zero-free limit.  This is
exactly the secular part of `RDI-CONV`.

After `PG-CONV`, the arithmetic target is

```text
PG-ANCHOR:
i G_L'(iu)/G_L(iu)-i G_L'(-iu)/G_L(-iu)
 -[H_L(s)-d/ds log A_L(s)] -> 0                        (2.2)
```

locally uniformly as `L->infinity`.

## 3. Spectral expansion

Let `(lambda_{j,N},e_{j,N})` be an orthonormal eigenbasis of the self-adjoint
inner block `M_N`.  Whenever it is invertible,

```text
h_N=sum_j <e_{j,N},f_N>/lambda_{j,N} e_{j,N},          (3.1)

L_{N,z}(h_N)
 =sum_j <e_{j,N},f_N>/lambda_{j,N}
          L_{N,z}(e_{j,N}).                            (3.2)
```

Formula (3.2) shows why a norm estimate is inappropriate: the small
denominators, source overlaps and Cauchy profiles must remain paired.

## 4. Necessary proof data

A proof of `PG-CONV` must control one projective object, not the two generator
vectors separately.  Sufficient data are:

```text
P1  a spectral cluster projection P_N;
P2  a nonzero scale t_N;
P3  local convergence of t_N^(-1)L_{N,z}(P_N h_N);
P4  local negligibility of t_N^(-1)L_{N,z}((I-P_N)h_N);
P5  convergence of t_N^(-1), accounting for the constant 1 in G_N.      (4.1)
```

No simplicity or gap between individual modes is assumed.

## 5. Status

```text
proved:
  exact coupled equation (1.1);
  exact projective numerator (1.3);
  exact paired spectral expansion (3.2);

reduced:
  fixed-L convergence to the projective cluster data P1--P5;

open:
  P1--P5 for the CCM sections;
  PG-ANCHOR;

next:
  prove the abstract cluster-projective theorem, including the zero-free
  condition needed for logarithmic derivatives.
```

