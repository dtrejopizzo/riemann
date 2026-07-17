# E73.268 - Equivalence of cell, coefficient, and second-Abel forms

Date: 2026-07-14.

## 1. Purpose

E73.267 states the remaining theorem in cell form:

```text
mathcal A_L[y -> q_aQ_yR_wxi_L]
-sum_{p^k<=e^L}(log p)p^(-k/2)q_aQ_{klog p}R_wxi_L
=O_M(L^-M).                                      (CELL-CTM)
```

This note ties that form back to the coefficient and second-Abel normal forms.
The goal is to make clear that these are not three different gates.  They are
three exact representations of the same scalar center.

## 2. Packet identity

Define the transverse packet

```text
B_{a,w,L}(y)=q_aQ_yR_wxi_L.
```

The finite trigonometric-cell expansion is:

```text
B_{a,w,L}(y)
=sum_omega c_omega e^(iomega y)
 +y sum_omega l_omega e^(iomega y).              (1)
```

This is the coefficient packet used in E73.222--E73.237.

## 3. Prime equivalence

Using (1),

```text
sum_{p^k<=e^L}(log p)p^(-k/2)B_{a,w,L}(klog p)
=sum_omega c_omega W_omega^P
 +sum_omega l_omega V_omega^P.                  (2)
```

The companion script verifies (2) directly against the cell sum.

## 4. Archimedean equivalence

The archimedean cell functional is exactly the closed digamma functional:

```text
mathcal A_L[B_{a,w,L}]
=sum_omega c_omega W_omega^A
 +sum_omega l_omega V_omega^A.                  (3)
```

Thus:

```text
CELL-CTM
<=>
sum_omega c_omega(W_omega^A-W_omega^P)
 +sum_omega l_omega(V_omega^A-V_omega^P)
=O_M(L^-M).                                     (COEFF-ETA)
```

This is the E73.222/E73.235 closed center.

## 5. Second-Abel equivalence

After subtracting the neutral ramp from E73.237,

```text
B^bal=B-B'(0)r_*,
F_L[r_*]=0,
```

one has:

```text
F_L[B]=F_L[B^bal]
=int_0^L K_L(t)(B^bal)''(t)dt.                  (4)
```

Therefore:

```text
CELL-CTM <=> COEFF-ETA <=> SECOND-ABEL.
```

The analytic theorem can be attacked in whichever language exposes the useful
structure, but proving one proves all.

## 6. Numerical audit

The companion script checks:

```text
1. B(y) from cells equals B(y) from modes at sample points;
2. prime cell sum equals prime mode sum;
3. cell center equals coefficient center;
4. coefficient center equals matrix qH_LR_wxi_L.
```

The expected errors are at floating/mp assembly scale.

## 7. Status

```text
proved formally: CELL-CTM <=> COEFF-ETA <=> SECOND-ABEL;
verified numerically: cell/mode/center assemblies agree in tested windows;
open: prove the common scalar is O_M(L^-M).
```

