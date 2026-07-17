# E73.281 - Generated pairing annihilation correction

Date: 2026-07-14.

## 1. Purpose

E73.279 and E73.280 interpreted the canonical coefficient decomposition of
APR rows as evidence that generated and residual sectors interfere.  E73.281
checks the exact algebra behind that interpretation.

The correction is:

```text
in exact mesh space, generated columns pair zero with xi_L;
the nonzero generated pairings in E73.279--E73.280 are coordinate-fit
contamination.
```

## 2. Exact theorem

Let

```text
E_L=H_L-mu_LI,
E_Lxi_L=0.
```

For every primitive vector `p`,

```text
<xi_L,E_Lp>=<E_Lxi_L,p>=0
```

because `H_L` is self-adjoint.  Therefore any exact generated source

```text
S_L A_L y = E_L P_L y
```

must satisfy

```text
ell_L(A_Ly)=0,
ell_L(c)=<xi_L,S_Lc>.
```

So the generated sector cannot carry a genuine nonzero scalar contribution.

## 3. Numerical audit

The probe compares:

```text
genMeshB    = exponent of ||xi_L^* E_L P_L||,
genCoeffB   = exponent of ||xi_L^* S_L A_L||,
imageRel    = relative error of representing E_LP_L columns in S_L,
centerB     = true APR center rho xi_L,
coeffCenterB = coefficient reconstruction center.
```

The output shows:

```text
genMeshB    ~ -16 to -22,
genCoeffB   ~ -4 to -9,
centerB     ~ -19 to -24,
coeffCenterB ~ -7 to -12.
```

Thus a small relative coordinate error in representing generated columns
produces an absolute scalar error much larger than the APR scalar.

## 4. Consequence for E73.279--E73.280

E73.279 and E73.280 are not proof-facing evidence for a coupled generated
versus residual interference identity.  Their large generated pairings are
not mathematical signal; they are caused by using approximate canonical
coordinates in a scalar channel much smaller than the coordinate residual.

The valid exact statement is instead:

```text
ell_L(M_L)=0
```

provided `M_L` is represented exactly as the image of `(H_L-mu_LI)`.

Therefore quotienting by the exact generated module is algebraically allowed:
`ell_L` descends to the quotient.  What failed in E73.279 is the approximate
coordinate implementation, not the exact quotient principle.

## 5. Corrected endpoint

The proof-facing finite object is:

```text
Exact canonical source complex:

P_L --E_L--> S_L --ell_L--> C,
ell_L E_L = 0.
```

The remaining theorem is that the APR row has an exact canonical
representative whose quotient class pairs rapidly small:

```text
EXACT-QUOT-APR:
rho_{j,w}=S_Lc_{j,w}+e_{j,w},
e_{j,w}xi_L=O_M(L^(-M)),
and
ell_L([c_{j,w}])=O_M(L^(-M)).
```

The representation error must itself be controlled below the APR scale.
Equivalently, before using coefficient coordinates again, one must prove an
exact symbolic partial-fraction representation of the relevant rows.  Least
squares fits with `imageRel=1e-6` are far too crude for a scalar of size
`L^-20` or smaller.

## 6. What this fixes

This restores the correct algebraic direction:

```text
1. generated rows are true coborders and pair zero;
2. coefficient approximations can fake nonzero generated pairings;
3. any valid quotient theorem must be exact symbolic, not numerical
   least-squares in an ill-conditioned source basis.
```

Thus the next task is not to prove a coupled-pair interference theorem, but to
construct the exact source complex and exact quotient representative.

## 7. Status

```text
proved algebraically: ell_L E_L = 0;
verified numerically: mesh generated pairing is at floor;
diagnosed: E73.279--E73.280 generated pairings are coordinate contamination;
open: build exact symbolic source coordinates for APR rows and the generated
      image before making quotient claims.
```
