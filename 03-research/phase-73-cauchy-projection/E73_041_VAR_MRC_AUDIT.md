# E73.041 - VAR-MRC audit

## 1. Purpose

E73.040 showed that the incoherent derivative envelope is useless.  E73.041 tests a sharper finite
variant:

```text
VAR:
|C_x(gamma)| <= |gamma-rho| sup_{t in [rho,gamma]} |C_x'(t)|,
```

where the supremum is taken over the signed rational derivative, not over `sum |xi_n|`.

This is still non-circular.  In principle, the exact supremum is a finite algebraic certificate:
critical points of `|C_x'|^2` are roots of a polynomial obtained from `P_x/D_x`.

## 2. Result

Numerically, `VAR` again does not improve the final budget.  The optimized bound almost always
falls back to the trivial value.

Representative output:

```text
E73.041 VAR-MRC probe
Compares trivial, incoherent derivative, and signed-variation derivative budgets.
 lam     L sigma     tau  m roots varWins      actual      absDeriv      varDeriv   var/act
   8   4.159  0.05   14.13  2    12       1   2.395e-07     2.395e-07     2.395e-07  1.00e+00
  12   4.970  0.20   21.02  3    14       0   4.907e-06     4.907e-06     4.907e-06  1.00e+00
  18   5.781  0.20   14.13  3    30       1   9.016e-06     9.016e-06     9.016e-06  1.00e+00
  24   6.356  0.20   21.02  3    34       2   1.726e-05     1.726e-05     1.726e-05  1.00e+00
```

## 3. Interpretation

The finite roots explain the smallness of some individual raw Cauchy values, but the inequality
needed for the Phase 73 gate is not made easier by replacing `|C_x(gamma)|` with a derivative
distance-to-root certificate.

The final useful positive statement is therefore not:

```text
root distance alone controls the gate.
```

It is the direct weighted Cauchy smallness:

```text
WCS:
e^(alpha L) sum_k
G_theta,m(a,i gamma_k)
|1-exp(i gamma_k L)|
|C_x(i gamma_k)|
<= L^B.
```

This is exactly `PFD` with the Hermite inverse removed.

## 4. Minimal endpoint

After E73.041 the clean chain is:

```text
WCS
=> PFD
=> DATA-HERM
=> CC-PROJ
=> NAT-PROJ
=> scalar WRL.
```

The remaining theorem is `WCS`, not a separate root-covering theorem.

## 5. What remains mathematically

To close the route, prove `WCS` uniformly for natural-height off-line clusters.  This is a finite
weighted L1 estimate for the cancelled Mellin-Cauchy data:

```text
G_theta,m(a,i gamma_k)       geometric Hermite coupling;
|1-exp(i gamma_k L)|         scalar Weyl mesh cancellation;
|C_x(i gamma_k)|             finite CCM Cauchy spectral defect.
```

No hidden Cauchy matrix inverse remains.
