# E73.245 - Curvature quotient defect

Date: 2026-07-14.

## 1. Purpose

E73.244 rejects direct closure by the DD-local primitive module.  The correct
next object is the quotient defect:

```text
rho_a modulo Image(Y^*E : Y in P_DD).
```

This is the transverse analogue of E73.163--E73.167.  We no longer ask whether
the whole residual row is generated.  We isolate the canonical obstruction
left after removing the generated DD-local image.

## 2. Definition

Let

```text
E=H_L-mu_L I,
P_DD=P_DD(gamma,L)
```

be the fixed DD-local primitive module from E73.244.  Define the generated row
space

```text
M_DD={Y^*E : Y in P_DD}.
```

For the transverse row

```text
rho_a=q_aH_L(I-P_w),
```

define the canonical quotient defect by orthogonal projection onto the
finite generated rowspace:

```text
delta_a = rho_a - Proj_{M_DD} rho_a.              (1)
```

This projection is not the forbidden full rowspace of `E`; it is the finite
symbolic image of a prescribed module.

## 3. What the audit measures

The audit reports:

```text
rank(M_DD),
||delta_a||,
|delta_a xi_L|,
|rho_a xi_L|,
```

and verifies whether the scalar center is carried by the quotient defect.

## 4. Result

The generated module removes a large part of row norm, but the scalar center
is essentially unchanged:

```text
delta_a xi_L ~= rho_a xi_L.
```

Thus the quotient is the correct localization of the obstruction.  The
remaining problem is not row approximation; it is a finite quotient scalar
theorem:

```text
CURV-QUOT-DIV:
delta_a xi_L = O_M(L^-M).
```

## 5. Consequence

This is now the sharp finite identity:

```text
CURV-QUOT-DIV
=> CURV-COB
=> CQ-DIV
=> BSA-DIV
=> ETA-DIV
=> U4
=> scalar WRL.
```

The object is finite, explicit, and falsifiable:

```text
1. build P_DD from DD_L(±gamma,d) and local denominator d^2-gamma^2;
2. compute M_DD=P_DD^*E;
3. project rho_a to the quotient;
4. prove the quotient pairing with xi_L is rapidly small.
```

## 6. Status

```text
defined: CURV-QUOT quotient defect;
observed: quotient carries the scalar obstruction;
open: prove CURV-QUOT-DIV from the finite CCM/Feshbach structure.
```

