# E73.260 - Row-replacement form of ETA-ADJ

## 1. Purpose

E73.259 states the reduced adjugate detector:

```text
ETA-ADJ:
rho_{a,w}Adj_red(E_L)
=O_M(L^-M)||Adj_red(E_L)||,
E_L=H_L-mu_LI.
```

This note writes and tests the determinant-only version:

```text
det ReplaceRow(E_L;i,rho_{a,w})
```

for every row `i`.

## 2. Algebraic identity

For a rank `n-1` matrix `E_L` with one-dimensional nullspace, the cofactors of
`E_L` form the reduced adjugate. Replacing row `i` by `rho` gives, up to the
standard cofactor sign,

```text
det ReplaceRow(E_L;i,rho)
= (rho Adj_red(E_L))_i.                         (1)
```

Since

```text
Adj_red(E_L)=scale * xi_Lxi_L^*,
```

we get

```text
det ReplaceRow(E_L;i,rho_{a,w})
= scale * (rho_{a,w}xi_L) * conjugate(xi_{L,i}). (2)
```

Therefore the normalized l2 determinant defect satisfies:

```text
(sum_i |det ReplaceRow(E_L;i,rho)|^2)^1/2 / |scale|
= |rho xi_L|.                                    (3)
```

Equation (3) is the zero-free row-replacement certificate equivalent to
`ETA-DIV`.

## 3. Numerical audit

The companion script evaluates row replacements by `slogdet` and normalizes by
the reduced cofactor scale computed from the nonzero eigenvalues.

Representative output:

```text
 lam      L gamma row rhoPairB maxDetB l2DetB predMaxB predL2B detScaleLog gapB
   8    4.159  21.02   0   -15.84  -15.98  -15.70   -16.23  -15.84     -238.98 -25.71
  10    4.605  14.13   0   -18.49  -18.73  -18.49   -18.73  -18.49     -339.41 -22.21
  12    4.970  21.02   0   -16.59  -16.84  -16.63   -16.96  -16.59     -455.12 -21.76
  16    5.545  21.02   0   -18.95  -18.40  -17.90   -19.38  -18.95     -936.09 -19.70
```

For `lambda=8,10,12`, the direct l2 row-replacement defect agrees with
`rhoPairB` at the level expected from double precision and determinant
conditioning. For `lambda=16`, direct determinants become visibly unstable:
the singular gap and cofactor scale are beyond what naive double `slogdet`
can certify.

## 4. Consequence

`ETA-ADJ` has two proof-facing realizations:

```text
1. reduced-adjugate/eigenline certificate:
   use a bordered Krawczyk eigenline certificate, then form Adj_red(E_L)
   as scale*xi_Lxi_L^*;

2. determinant-only certificate:
   interval-evaluate all det ReplaceRow(E_L;i,rho) and compare them with the
   reduced cofactor scale.
```

The second is more zero-free but numerically harder.  The first is more stable
once the eigenline has been certified by the already-developed bordered
Krawczyk machinery.

## 5. Status

```text
proved: row-replacement determinant form of ETA-ADJ;
verified: direct determinant audit matches stable rows;
warning: naive double determinants are not proof-facing at larger L;
open: implement interval determinant or Krawczyk-certified reduced adjugate.
```

