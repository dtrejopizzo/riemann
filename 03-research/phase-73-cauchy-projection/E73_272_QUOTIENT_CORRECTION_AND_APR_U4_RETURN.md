# E73.272 - Quotient correction and return to APR-U4

Date: 2026-07-14.

## 1. Purpose

E73.271 stated the curvature quotient theorem in a proof-facing form.  The
prior audit E73.256 contains a crucial correction that must be made explicit:
quotienting by any exact left-coborder rowspace cannot itself create scalar
cancellation after pairing with the exact eigenline.

This note corrects the endpoint and prevents the program from pursuing a
false quotient-cancellation mechanism.

## 2. Exact quotient invariance

Let

```text
E_L=H_L-mu_LI,          E_Lxi_L=0,
M={Y^*E_L : Y in P},
rho_a=q_aH_LR_w.
```

For every row `m in M`,

```text
mxi_L=Y^*E_Lxi_L=0.
```

Therefore for any exact projection `Pi_M` onto `M`,

```text
(rho_a-Pi_Mrho_a)xi_L = rho_axi_L.              (1)
```

This is E73.256.  It applies equally to the DD-local module, to any enlarged
symbolic primitive module, and to the `M_L^{sym}` notation of E73.271.

Thus the quotient defect `Delta_a=rho_a-Pi_Mrho_a` is useful for row geometry,
conditioning, pivot choice, and nondegeneracy, but it is not a new scalar
annihilation source.

## 3. Correct role of E73.271

The identity

```text
q_aH_LR_wxi_L=Delta_axi_L
```

is true but not a reduction in scalar difficulty, because by (1)

```text
Delta_axi_L=rho_axi_L=q_aH_LR_wxi_L.
```

So `CURV-QUOT-DIV` is not a theorem beyond the principal residual.  It is a
coordinate presentation of the same theorem.

The valid split is:

```text
Nondegeneracy / coordinate side:
  QROW-INDEP
  => GRAM-NONDEG
  => MAXMIN-NONDEG

Scalar side:
  APR-U4 / PRINCIPAL-RESIDUAL
  rho_axi_L=q_aH_LR_wxi_L=O_M(L^-M).
```

Together, these imply the finite Cramer numerator and pivot statements, but
the scalar smallness must come from APR-U4, not from quotienting.

## 4. Current scalar theorem

The surviving load-bearing theorem is:

### APR-U4 / Principal Residual

For every admissible Cauchy row/window and every `M`,

```text
rho_axi_L=q_aH_LR_wxi_L=O_M(L^-M).              (APR-U4)
```

Equivalently, by E73.269--E73.270,

```text
F_L[B_a]
=mathcal A_L[q_aQ_yR_wxi_L]
 -sum_{p^k<=e^L}(log p)p^(-k/2)q_aQ_{klog p}R_wxi_L
=O_M(L^-M),
```

where

```text
B_a(y)=q_aQ_yR_wxi_L.
```

Equivalently, after balanced ramp subtraction,

```text
int_0^L K_L(t)(B_a^bal)''(t)dt=O_M(L^-M).
```

Equivalently, in coupled Loewner form,

```text
F_L[
  2q_acos(yD)R_wxi_L
  -(2/L)q_aD(sin(yD))[J]R_wxi_L
]=O_M(L^-M).
```

## 5. What still helps from the quotient branch

The quotient branch remains useful only for these tasks:

```text
1. selecting stable finite rows/pivots;
2. proving QROW-INDEP / MAXMIN-NONDEG;
3. giving determinant coordinates for finite certification;
4. separating conditioning artifacts from exact scalar statements.
```

It must not be presented as:

```text
1. a new source of scalar cancellation;
2. a proof of APR-U4;
3. a way to make Delta_axi_L smaller than rho_axi_L.
```

## 6. Next analytic target

The next proof attempt must attack APR-U4 directly in one of its exact forms:

```text
CELL-APR:
  A_L[q_aQ_yR_wxi_L]-P_L[q_aQ_yR_wxi_L];

SECOND-ABEL-APR:
  int_0^L K_L(t)(B_a^bal)''(t)dt;

COMM-APR:
  q_a[H_L^A,R_w]xi_L-q_a[H_L^P,R_w]xi_L;

LOEWNER-APR:
  F_L[2q_acos(yD)R_wxi_L-(2/L)q_aD(sin(yD))[J]R_wxi_L].
```

Among these, the proof-facing form is still the balanced second-Abel /
coupled Loewner form, because:

```text
1. endpoint moments alone were rejected by E73.239;
2. separated Loewner estimates were rejected by E72.55;
3. quotient projection cancellation was rejected by E73.256;
4. rank-two transport through Q_wxi_L was rejected by E73.266.
```

## 7. Status

```text
corrected: quotient projection cannot supply scalar cancellation;
kept:      quotient geometry for nondegeneracy and finite coordinate
           certification;
survives:  APR-U4 / principal residual as the scalar theorem;
next:      prove APR-U4 in balanced second-Abel / coupled Loewner form.
```

