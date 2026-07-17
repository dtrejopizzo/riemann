# E73.250 - Incremental Gram nondegeneracy

## 1. Purpose

E73.249 reduced maximal-minor nondegeneracy to the quotient Gram volume:

```text
GRAM-NONDEG:
Vol_Q = det(D_QD_Q^*)^{1/2} >= L^{-B}.
```

This note factors that volume into successive distances.  The goal is to decide
whether the lower bound should be proved through row norms, through angle
control, or through a hidden determinant identity.

## 2. Incremental factorization

Let the four quotient rows be ordered as

```text
d_1,d_2,d_3,d_4.
```

Define

```text
s_1 = ||d_1||,
s_j = dist(d_j, span(d_1,...,d_{j-1})),  j=2,3,4.
```

Then:

```text
Vol_Q = prod_{j=1}^4 s_j.
```

Equivalently, writing

```text
sin theta_j = s_j / ||d_j||,
```

one has

```text
Vol_Q = prod_j ||d_j|| prod_{j>=2} sin theta_j.
```

Thus `GRAM-NONDEG` follows from the finite packet of estimates:

```text
INC-GRAM-NONDEG:
dist(d_j, span(d_1,...,d_{j-1})) >= L^{-B_j},  j=1,2,3,4.
```

## 3. What the audit shows

The tested windows show no super-polynomial angular collapse.  The smallest
angle sine has exponent between roughly:

```text
L^{-1.67} and L^{-3.89}
```

depending on ordering and window.  The row norms are also polynomial-scale.

Therefore the nondegeneracy part of the endpoint is not the apparent hard
arithmetical cancellation.  It should be a finite divided-difference
independence theorem for the four quotient rows.

## 4. New theorem target

The preferred analytic target is:

```text
QROW-INDEP:
For the canonical four quotient rows D_Q, there is an ordering d_1,...,d_4
such that

dist(d_j, span(d_1,...,d_{j-1})) >= L^{-B}

uniformly in the allowed windows.
```

Then:

```text
QROW-INDEP => GRAM-NONDEG => MAXMIN-NONDEG.
```

This leaves the true RH-strength statement isolated as:

```text
MAXMIN-PIV-DIV:
z_{J_*}=O_M(L^-M).
```

## 5. Status

```text
proved: Vol_Q factors as product of four Gram-Schmidt increments;
observed: increments and angle sines are polynomial-scale;
open: prove QROW-INDEP from the DD-local divided-difference structure.
```
