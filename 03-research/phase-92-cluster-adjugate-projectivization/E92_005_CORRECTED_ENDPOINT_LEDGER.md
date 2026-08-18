# E92.005 - Corrected endpoint ledger

## 1. Removed obligations

The following estimates were introduced only to replace the complete cluster
by one resonant line:

```text
DOM-E;
DOM-M;
rho_E<<epsilon_N<<rho_O;
uniform one-line dominance across that window.        (1.1)
```

E92.001--E92.004 prove that none of (1.1) is necessary for the projective
endpoint quotient.  They remain optional sufficient conditions for a rank-one
asymptotic formula, but they are removed from the minimal route to RDI.

## 2. Remaining analytic clauses

The cluster-adjugate route has one independent analytic requirement:

```text
CA-1  fixed-L projective convergence of the global bordered numerator. (2.1)
```

`CA-1` does not identify the limit arithmetically.  Cofinal compatibility is
closed by the diagonal theorem E92.007 once `CA-1` and the outer arithmetic
limit are available.

Complementary invertibility is not on this list.  E92.006 replaces every
local Feshbach chart by the global bordered determinant if necessary.

Base-point nonvanishing is also not a separate theorem obligation.  Each
finite numerator is a nonzero safe meromorphic function by E92.006, and its
projective class can be covered by evaluation charts.  If one safe evaluation
vanishes, another chart is used.  A fixed base point is imposed only after a
nonzero limiting chart has been selected.

## 3. Remaining force-bearing clause

Let

```text
B_(L,N)(s;s_*)
 =[N_(L,N,1)(iu)N_(L,N,1)(-iu)]
  /[N_(L,N,1)(iu_*)N_(L,N,1)(-iu_*)].                (3.1)
```

The arithmetic statement is

```text
CLUSTER-RDI-ANCHOR:
B_(L,N)(s;s_*)
 ->E_L(s)/E_L(s_*)                                   (3.2)
```

through the prescribed finite-section and outer limits, with the explicit
noncluster factors included according to E80.003.

Equation (3.2) is exactly RDI-ANCHOR in denominator-free cluster coordinates.
It remains the force-bearing clause.

## 4. Strategic consequence

The endpoint eigenvalue cascade, parity scale separation and matching-window
problem are not the mathematical core.  They arise from using singular
inverse coordinates before projectivization.  The canonical finite object is
the bordered determinant (E92.001(3.1)).

Future work should therefore act directly on that determinant by one of two
methods:

```text
1. prove a finite Gamma--Euler identity for the bordered determinant;
2. prove its normalized logarithmic derivative converges to H_L.       (4.1)
```

## 5. Status

```text
closed and removed from the minimal route:
  one-line dominance and matched parity widths;

open analytic infrastructure:
  CA-1;

open arithmetic core:
  CLUSTER-RDI-ANCHOR, equivalently RDI-ANCHOR and IDENT.
```
