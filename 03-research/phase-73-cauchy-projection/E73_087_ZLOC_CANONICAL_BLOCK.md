# E73.087 - Canonical local zero window

## 1. Problem fixed

E73.084 showed that a small zero window gives a large HWIN margin.  E73.086 shows the needed
qualification:

```text
the good small window is the cluster-local zero window, not the FAR3 evaluation window.
```

This document makes the window canonical.

## 2. Off-line cluster datum

Let `A` be a natural-height off-line cluster:

```text
A = {rho_j = 1/2 + alpha + i tau_j}
```

with common maximal displacement `alpha>0`, counted with its conjugate and functional-equation
partners.  Let `I_A` be the minimal closed height interval containing the positive heights `tau_j`,
enlarged by the fixed Hermite order radius required by the local Cauchy projection block of E72.324.

The enlargement is fixed by the model, not by the value of the final WCS terms.

## 3. Canonical local zero window

For each `L`, let `Gamma_L` be the critical-line zero-node mesh used by the finite Cauchy packet.
Define:

```text
Z_loc(A,L)
:=
{ i gamma in i Gamma_L : gamma is among the r(A) nearest nodes to I_A }
cup
{ -i gamma : i gamma is selected },
```

where `r(A)` is the local Cauchy block size:

```text
r(A)= total Hermite multiplicity of the maximal-real-part cluster A,
      plus the fixed companion nodes needed for confluent stability.
```

In the simple height-one tests of E73.084--E73.086, `r(A)=3`.

## 4. Separation from FAR3

The FAR3 set is:

```text
D_3(A,L) = top three critical evaluation rows for WCS,
```

selected by the FAR score:

```text
F_k(A,L)=W_k(A,L)dist(-gamma_k,Div(P_x)).
```

The local zero window is:

```text
Z_loc(A,L)=zero-node input for the paired packet divisor identity.
```

These are different variables.  The paired identity is evaluated at:

```text
z = sigma + i gamma_k,       gamma_k in D_3(A,L),
w in Z_loc(A,L).
```

Thus `D_3(A,L)` selects rows and `Z_loc(A,L)` selects local divisor nodes.

## 5. Lemma: non-optimizing admissibility

**Lemma 87.1.**  `Z_loc(A,L)` is admissible for LOCAL-HWIN because its construction uses only:

```text
1. the off-line cluster height interval I_A;
2. the Hermite/confluent order of the local Cauchy block;
3. the finite critical zero-node mesh Gamma_L.
```

It does not use:

```text
1. the WCS term T_k;
2. the FAR score F_k;
3. the size of H_0 at any evaluation row;
4. any optimization over possible windows.
```

*Proof.*  The definition of `Z_loc(A,L)` is nearest-node selection to `I_A` with fixed cardinality
`r(A)`.  All inputs are fixed before the WCS rows are ranked.  Therefore the window is independent of
the quantity being bounded.  This proves admissibility.  `□`

## 6. Lemma: two-window factorization

**Lemma 87.2.**  For each FAR3 evaluation row `z_k=sigma+i gamma_k`, the local paired packet main term
has the estimate:

```text
|Pair_{z_k}^{loc}|
<=
sum_{w in Z_loc(A,L)/+-}
(
 |A_L(z_k,w)||H_0(w)|
 + |B_L(z_k,w)||H_0(-w)|
).
```

*Proof.*  E73.075 gives the exact identity:

```text
Pair_z(w)=A_L(z,w)H_0(w)+B_L(z,w)H_0(-w).
```

Restrict this identity to the finite local window and sum the absolute values.  The triangle
inequality gives the displayed bound.  `□`

## 7. The local theorem now needed

The analytic target is:

```text
LOCAL-HWIN-5:
sum_{gamma_k in D_3(A,L)}
W_k(A,L)
sum_{w in Z_loc(A,L)/+-}
(
 |A_L(z_k,w)||H_0(w)|
 + |B_L(z_k,w)||H_0(-w)|
)
<= C L^-5.
```

This is not a statement about the FAR3 zero window.  It is a two-window estimate: local divisor nodes
against dangerous WCS rows.

## 8. Remaining outside-window term

The complementary zero-node set:

```text
Gamma_L \ Z_loc(A,L)
```

must be handled by the outside-window/tail terms from Phase 72, not by enlarging LOCAL-HWIN.  This is
exactly what E73.086 diagnoses: adding evaluation-near nodes into the local budget can consume the
`L^-5` margin.

## 9. Current endpoint

The route is now:

```text
EXACT-PAIR-DIV
+ LOCAL-HWIN-5 on canonical Z_loc(A,L)
+ outside-window/tail absorption
+ FAR3 nodewise WCS certificate
=> scalar WRL.
```

The next mathematical step is to prove LOCAL-HWIN-5 from:

```text
1. local nodal smallness of H_0 on Z_loc(A,L);
2. the lower bound |z_k +- w| >= sigma for FAR rows;
3. the prefactor decay already isolated in FAR3.
```
