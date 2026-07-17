# E73.245 results - curvature quotient defect

Command:

```text
python3 E73_245_curv_quotient_defect.py
```

## 1. Summary

The audit constructs:

```text
M_DD={Y^*E : Y in P_DD}
```

for the DD-local module `P_DD`, projects

```text
rho_a=q_aH_L(I-P_w)
```

onto `M_DD`, and records the quotient defect:

```text
delta_a=rho_a-Proj_{M_DD}rho_a.
```

## 2. Observations

For `lambda=8,10,12`, the generated rowspace rank is stable:

```text
rank(M_DD)=5
```

across the tested DD-local rational orders.  The quotient defect norm is much
smaller than the removed row component, but the scalar pairing remains:

```text
delta_a xi_L ~= rho_a xi_L.
```

For `lambda=16`, the rank begins to vary with rational order and the quotient
projection becomes conditioning-sensitive.  Those rows should be treated as
diagnostic only until the DD-local basis is intervalized or symbolically
rank-certified.

## 3. Meaning

This is the finite endpoint we wanted:

```text
CURV-QUOT-DIV:
delta_a xi_L = O_M(L^-M).
```

The generated DD-local image removes non-load-bearing row geometry; the scalar
obstruction lives in the quotient.  This mirrors E73.167 for the cauchy0
critical defect.

## 4. Consequence

The proof should no longer try to enlarge `P_DD` ad hoc.  It should:

```text
1. symbolically certify rank(M_DD) and the quotient projection;
2. derive a closed formula for the quotient coordinates of rho_a;
3. prove the quotient pairing with xi_L is rapidly small.
```

This is a finite explicit divisibility statement.

## 5. Status

```text
defined and audited: CURV-QUOT;
observed: quotient carries scalar obstruction;
open: symbolic rank/coordinate formula and proof of CURV-QUOT-DIV.
```

