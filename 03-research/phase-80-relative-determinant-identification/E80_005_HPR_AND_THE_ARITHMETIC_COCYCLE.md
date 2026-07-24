# E80.005 - HPR compression and the arithmetic cocycle

## 1. Exact Hilbert compression

Let `r,eta in C^m`, let `U,F in C^m`, and define the skew mesh matrix

```text
A_jb = 1/(2 i pi(n_b-n_j)),  j != b,
A_jj = 0.                                               (1.1)
```

For a vector `X`, write `M_X=diag(X)`.  The scalar in `HPR-DIV` is

```text
HPR(r,eta;U,F)
 = sum_j r_j eta_j U_j
   + sum_j F_j r_j(A eta)_j
   + sum_j F_j eta_j(A r)_j.                            (1.2)
```

### Proposition 1.1

One has the exact identity

```text
HPR(r,eta;U,F)
 = r^T(M_U+[M_F,A])eta.                                 (1.3)
```

### Proof

The first off-diagonal term in (1.2) is `r^T M_F A eta`.  Since
`A^T=-A`, the second one is

```text
eta^T M_F A r = -r^T A M_F eta.
```

Their sum is `r^T[M_F,A]eta`.  Adding the diagonal term proves (1.3).
`QED`

## 2. Reconstruction of the finite cell operator

Put

```text
d_j=2 pi n_j/L,
F_j=W^odd(d_j),
U_j=U^even(d_j).
```

Let `Lambda_F^full` be the full Loewner matrix of `F`, including `F'(d_j)`
on its diagonal.  The off-diagonal entries satisfy

```text
[M_F,A]_jb
 = (F_j-F_b)/(2 i pi(n_b-n_j))
 = -(1/(iL))(Lambda_F^full)_jb.                         (2.1)
```

The closed-weight differential identity gives

```text
U_j=W^even(d_j)-(1/(iL))F'(d_j).                        (2.2)
```

Consequently

```text
M_U+[M_F,A]
 = M_{W^even}-(1/(iL))Lambda_F^full
 = H_L^CCM + G_L,                                       (2.3)
```

where the last equality is the pointwise cell reconstruction followed by the
Gamma-prime functional.  The possible constant closed-weight gauge `G_L` has
rows in the Cauchy constraint space.  For the admissible vector
`eta=R_w xi_L`, one has `Q_w eta=0`, and hence `r^T G_L eta=0`.  Thus, in the
paired quotient,

```text
HPR(r,eta;U,F)=r^T H_L^CCM eta.                          (2.4)
```

This closes the coordinate question: HPR-DIV, the two-symbol Loewner scalar,
the cell scalar and the Schur-commutator scalar are the same finite bilinear
functional.

## 3. Why this is not yet relative determinant identification

The relative determinant defect of E80.003 is

```text
D_{L,N}(s)
 = L coth(L(s-1/2)/2)
   + i T'_{L,N}(i(s-1/2))/T_{L,N}(i(s-1/2))
   - i T'_{L,N}(-i(s-1/2))/T_{L,N}(-i(s-1/2))
   - B^ext_{L,N}(s)
   - H_L^Euler(s).                                      (3.1)
```

Here `H_L^Euler=E_L'/E_L`.  By the finite determinant identity,
`T'/T` is a difference of resolvent traces.  In contrast, (2.4) is one
directional pairing of the finite CCM matrix in the Cauchy-gauge quotient.
The archive contains exact
identities for both objects, but no exact identity equating (2.4) with (3.1).

This distinction cannot be removed by generic linear algebra.  For example,
with `r=eta=e_1` and

```text
X_t=diag(0,t),
```

one has `r^T X_t eta=0` for every `t`, while

```text
Tr(zI-X_t)^(-1)=1/z+1/(z-t)                             (3.2)
```

varies with `t`.  Therefore one directional scalar does not determine a
resolvent trace.  This example does not refute a special CCM identity; it proves
that such an identity, if true, needs additional CCM arithmetic and cannot be
deduced from HPR compression alone.

## 4. The correct section cocycle

Define the exact holomorphic defect

```text
D_{L,N}(s)=d/ds log C_{L,N}(s)-H_L^Euler(s).             (4.1)
```

For consecutive sections the Euler term cancels, giving the cocycle identity

```text
D_{L,N+2}(s)-D_{L,N}(s)
 = d/ds log(C_{L,N+2}(s)/C_{L,N}(s)).                   (4.2)
```

The mixed Schur update of P76.049 computes the transfer part of the right-hand
side before absolute values are taken, while the external-mesh increment is
explicit.  Formula (4.2), not HPR-DIV by itself, is the exact cocycle attached
to RDI.

### Proposition 4.1 - convergence does not identify the cocycle limit

Let `V` be a domain compactly contained in `Re s>1`.  If

```text
sum_N sup_V |D_{L,N+2}-D_{L,N}| < infinity,              (4.3)
```

then `D_{L,N}` converges uniformly on `V` to a holomorphic function `D_L`.
Condition (4.3) alone does not imply `D_L=0`.

### Proof

The first assertion is the uniform Cauchy criterion.  For the second, adding
any fixed holomorphic function `h` to every `D_{L,N}` preserves all increments
in (4.3) and changes the limit to `D_L+h`. `QED`

Thus the remaining theorem has two logically separate clauses:

```text
COCYCLE-CONV:
  for each fixed L, the signed mixed-shell increments converge locally
  uniformly to an intrinsic holomorphic defect D_L;

COCYCLE-ANCHOR:
  D_L -> 0 locally uniformly as L->infinity.                            (4.4)
```

The second clause is `SAFE-GAMMA-IDENT` in relative-determinant coordinates.
It is the arithmetic normalization that a fixed-`L` convergence theorem cannot
supply.  No identity `D_L=0` at finite `L` is required.

## 5. Smallest valid proof-facing expression

P76.041 gives, exactly,

```text
T_b(z)=F_b(z)/(z-d_b),
F_b(z)=1+H_b(z)+H_b^bd,
H_b=a_b U+b_b V.                                      (5.1)
```

P76.042 reconstructs `H_b` from the inhomogeneous cell equation while retaining
the source term.  Substitution of (5.1) into (3.1), followed by the iterated
limits `N->infinity` and `L->infinity`, is therefore the smallest currently
justified arithmetic expression for `COCYCLE-ANCHOR`.  Any proposed proof must
control the logarithmic derivative of the coupled numerator `F_b`;
estimating its Gamma and prime pieces separately before forming `F_b'/F_b`
repeats the hard-Euler-trace error.

## 6. Status

```text
proved:
  exact HPR commutator compression (1.3);
  exact reconstruction HPR = two-symbol = cell = directional CCM scalar;
  the exact relative section cocycle (4.2);
  cocycle convergence does not determine its holomorphic limit;

closed:
  HPR-DIV as a possible missing algebraic reformulation;

corrected:
  HPR-DIV is not an established bridge to RDI;
  the RDI cocycle requires both convergence and an arithmetic anchor;

open:
  COCYCLE-CONV;
  COCYCLE-ANCHOR, equivalently outer SAFE-GAMMA-IDENT after fixed-L
  convergence;

next:
  determine the weakest convergence theorem actually needed in place of the
  absolute GAP-Z formulation.
```
