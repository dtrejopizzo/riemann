# E72.371 - Full finite CFIR row build protocol

## 1. Purpose

E72.370 shows that the remaining proof is not the energy certificate itself, but the finite coupled
identity:

```text
FINITE-CFIR:
J_T[
   T_W02-T_WR-T_Prime
   -2kappa_*G_x
   -I_T^HG_x
   +Tail_T^M
]=O_T(L^B).
```

Previous numerical probes used partial rows:

```text
Lambda k_z - I_Tk_z + TailBasis.
```

This protocol specifies how to build the full finite row before applying any rowspace, energy, or
divisor test.

## 2. Required finite rows

For every active mesh column `n` and spectral variable `z`, construct:

```text
R_W02(z;n):
  transformed row of the model W02 term;

R_WR(z;n):
  transformed row of the archimedean WR term;

R_Prime(z;n):
  transformed row of the finite prime term;

R_G(z;n):
  k_z(n);

R_I(z;n):
  interpolation row (I_T^H k_.)(z;n);

R_Tail(z;n):
  collapsed finite TailBasis row.
```

The full row is:

```text
R_full(z;n)
= R_W02(z;n)-R_WR(z;n)-R_Prime(z;n)
 -2kappa_* R_G(z;n)
 -R_I(z;n)
 +R_Tail(z;n).                                      (1)
```

Then:

```text
Def_CFIR,T = J_T R_full · xi.
```

## 3. Relation to the transformed eigen-equation

The transformed eigen-equation gives:

```text
R_W02-R_WR-R_Prime = (mu+e_pole)R_G
```

when applied to `xi`.  Substituting this after evaluation gives the reduced row:

```text
R_reduced(z;n)
= Lambda_L R_G(z;n)-R_I(z;n)+R_Tail(z;n),
Lambda_L=mu+e_pole-2kappa_*.
```

But E72.352 warns:

```text
adding rows of (C_E-mu I) cannot repair the row-ideal defect.
```

Therefore a valid build must distinguish:

```text
full coupled row before using E xi=0;
reduced interpolation row after using E xi=0.
```

The two are equal only after applying to the actual eigenvector `xi`, not as raw rows.

## 4. Verification ladder

The build should report:

```text
1. fullDef      = ||J_T R_full xi||;
2. reducedDef   = ||J_T R_reduced xi||;
3. couplingErr  = ||J_T(R_full-R_reduced)xi||;
4. rowspaceDef  = distance of R_reduced to Row(C_E-mu I);
5. energyCFIR   = ||J_T R_reduced xi||^2.
```

Expected identities:

```text
couplingErr = roundoff
```

if all terms and constants are normalized consistently.

If `couplingErr` is not roundoff, the implementation has a normalization/sign error in
`W02/WR/Prime/kappa/e_pole`.

## 5. Why this is the next necessary computation

E72.349--E72.368 tested partial rows and equivalent certificates.  They did not build the full coupled
row from the primitive finite operator terms.  The next falsifiable step is to compute (1) directly.

Only after this build passes the coupling check can the analytic proof attack the actual finite
identity.

## 6. Status

```text
specified: exact full finite CFIR row construction;
specified: reduced row and coupling consistency check;
open: implement R_W02, R_WR, R_Prime from the primitive finite kernels and run the ladder.
```
