# P75.004-P75.006 - Euler/Gamma expansion and signed remainder audit

## Starting point

By P75.003,

```text
|P_L(z)|^2
= |D_L(z)|^2 r_z^* adj(H_L-mu_L I) r_z / tr adj(H_L-mu_L I).
```

Insert the finite CCM decomposition

```text
H_L = W02_L - WR_L - Prime_L.
```

Any determinant expansion of the adjugate is therefore a finite signed sum of
minors whose entries are multilinear expressions in the three sectors.

## Candidate expansion

The strongest available form is:

```text
P_L(gamma)
= Main_L(gamma)
 + ArchTail_L(gamma)
 + PrimeTail_L(gamma)
 + MeshTail_L(gamma),
```

where each term is obtained by replacing entries in the bordered/adjugate
minor with the corresponding finite sector kernel before the determinant or
cofactor expansion is evaluated.

This is exact but not useful unless

```text
Main_L(gamma)=A_L(gamma) Xi(1/2+i gamma)
```

and

```text
ArchTail_L(gamma)+PrimeTail_L(gamma)+MeshTail_L(gamma)=O_M(L^-M)D_L(gamma).
```

## Recombination test

The cell transform identity from Phase 74 is

```text
KQ_z(y;n)
= i/(z+i d_n)
  [e^{z(L-y)}-e^{i d_n y}
   +e^{zL}e^{-i d_n y}-e^{zy}].
```

The allowed recombination is:

```text
T_W02(i gamma)[xi_L]
-T_WR(i gamma)[xi_L]
-T_Prime(i gamma)[xi_L]
```

before estimating any sector.  Performing this recombination gives exactly
the Phase 74 remainder:

```text
EG_LOCK_L(gamma)
= T_W02(i gamma)[xi_L]
- T_WR(i gamma)[xi_L]
- T_Prime(i gamma)[xi_L].
```

Thus the candidate

```text
REM_L(gamma)=P_L(gamma)-A_L(gamma)Xi(1/2+i gamma)
```

is theorem-grade only if one proves a new signed arithmetic estimate for
`EG_LOCK_L(gamma)`.  The determinant/adjugate normalization does not by
itself reduce the endpoint.

## No-go for termwise tails

Termwise bounds on `ArchTail`, `PrimeTail`, or `MeshTail` lose the signed
coupling that distinguishes zeta from planted/DH.  They either:

```text
1. are too weak, typically algebraic or exponential in the wrong scale;
2. require a zero-free/positivity input equivalent to scalar WRL;
3. cancel equally for planted controls, which violates P75.012.
```

## P75.006 conclusion

The signed explicit-formula remainder exists as a finite identity, but the
available formula is not a new object:

```text
ARITH-REM == EG_LOCK == TPW/scalar-WRL endpoint.
```

This triggers P75.015 outcome C unless a later cutoff or Schur argument
produces an independent all-orders estimate.  P75.007-P75.009 audit those
escape routes.

