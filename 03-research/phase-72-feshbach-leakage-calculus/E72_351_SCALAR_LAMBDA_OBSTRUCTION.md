# E72.351 -- Scalar Lambda obstruction

**Purpose.** Prove and test the finite criterion for whether a single scalar left coefficient
`Lambda_L` can close the interpolation row.  The answer from the shifted-node stress is no: a fitted
scalar helps, but the nodewise consistency ratios are not constant.

## 1. Finite row form

For a finite window node `a`, write the partial CFIR row as

```text
R_a(Lambda)=Lambda k_a + S_a,
```

where

```text
k_a(m)=(1-e^(aL))/(ia-d_m)
```

and `S_a` contains the interpolation row and collapsed `TailBasis` terms.

The row belongs to `Row(E)` if and only if it annihilates the ground vector:

```text
R_a(Lambda) xi = 0.
```

Thus, whenever `k_a xi != 0`, the unique scalar that closes node `a` is

```text
Lambda_a = - (S_a xi)/(k_a xi).                      (1)
```

## 2. Consistency theorem

### Lemma 72.351

A single scalar `Lambda` closes all rows in a finite window if and only if the values `Lambda_a` in
(1) are equal for every node with `k_a xi != 0`, and for every node with `k_a xi=0` one has
`S_a xi=0`.

### Proof

The equations are

```text
Lambda(k_a xi)=-(S_a xi)
```

for each node.  If `k_a xi != 0`, this forces `Lambda=Lambda_a`.  Therefore all such nodes must give
the same value.  If `k_a xi=0`, the equation is solvable only when `S_a xi=0`.  These conditions are
also sufficient by substitution. `QED`

## 3. Numerical stress

The probe computes:

```text
mean Lambda_a,
max_a |Lambda_a-mean|,
relative spread = max_a |Lambda_a-mean|/|mean|.
```

At finite root nodes the ratio is ill-conditioned because `k_a xi=0` by construction; those values are
diagnostic only.  Shifted nodes are the real test.

Representative shifted-node output:

```text
lam N  node   |mean Lambda|  spread      rel spread
6   10 shift  3.79588e+00   1.10382e+00 2.90795e-01
8   12 shift  4.39937e+00   1.83878e+00 4.17963e-01
10  14 shift  6.26502e+00   2.85451e+00 4.55628e-01
12  16 shift  4.65512e+00   4.68953e+00 1.00739e+00
```

The relative spread is not small.  Hence the partial CFIR row cannot be closed by a single scalar
`Lambda_L`.

## 4. Meaning

This does not contradict the transformed theorem.  It says only that the scalar left coefficient is
not enough.  E72.352 adds a further restriction: the missing correction cannot be an additive
rowspace row.  The full coupled row

```text
T_W02 - T_WR - T_Prime - 2kappa_*G
```

must contribute through the derivation of the exact residual row itself, not by being added after
the rowspace test.  If the correction is of the form `A(C_E-mu I)`, then it annihilates `xi` and
leaves the defect unchanged.

## 5. Status

```text
proved: exact scalar consistency criterion;
observed: shifted finite windows violate scalar consistency;
corrected: rowspace/operator additions cannot repair the defect after R_T is formed;
concluded: the remaining correction must be in the exact residual construction or in a non-rowspace compatibility identity.
```
