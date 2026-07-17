# E72.354 - Affine Lambda elimination for the Xi-window CFIR row

## 1. Purpose

E72.351 showed numerically that a fitted scalar left coefficient does not close the shifted partial
rows.  E72.352 then proved that additive rowspace corrections cannot repair the defect.  The next
analytic step is to remove the scalar ambiguity exactly.

This note splits the exact Xi-window residual row into its affine `Lambda_L` part and eliminates
`Lambda_L` by finite determinant identities.  The result is a proof-facing certificate which is
stronger than fitting a scalar and weaker than guessing the value of `Lambda_L`.

## 2. Exact affine split

Fix an Xi-zero contradiction window

```text
W_T={(a_j,m_j)}
```

and the Hermite jet map `J_T`.  The exact interpolation residual row is

```text
R_T^{Xi}(Lambda)
= J_T[ Lambda G_x - I_T^H G_x + Tail_T^M ].
```

Since `G_x(z)=k_z xi`, this is a finite row matrix of the form

```text
R_T^{Xi}(Lambda) = Lambda K_T + S_T,                  (1)
```

where

```text
K_T := J_T k_z,
S_T := J_T[-I_T^H k_z + TailBasis_T^M].
```

All entries of `K_T` and `S_T` are explicit finite functions of:

```text
L, active mesh d_n, window nodes a_j, multiplicities m_j.
```

No outside zero sum appears.

## 3. Row-ideal condition with the reduced adjugate

Let

```text
E=C_E-mu I
```

and assume the pole-even ground eigenspace is simple.  Let `Adj(E)` denote the reduced adjugate.  Then

```text
Row membership of R_T^{Xi}(Lambda)
<=> (Lambda K_T + S_T) Adj(E)=0.                     (2)
```

Define the finite matrices

```text
Y_T := K_T Adj(E),
X_T := S_T Adj(E).                                   (3)
```

Then the exact scalar-compatible CFIR certificate is:

```text
there exists Lambda such that X_T + Lambda Y_T = 0.  (4)
```

This is already finite and root-window explicit.

## 4. Lambda-eliminated minors

Let the combined index `u=(alpha,c)` run over Hermite rows `alpha` and columns `c` of `Adj(E)`.
Write

```text
y_u := (Y_T)_{alpha,c},
x_u := (X_T)_{alpha,c}.
```

There exists a scalar `Lambda` satisfying (4) if and only if:

```text
x_u y_v - x_v y_u = 0                                (5)
```

for every pair `u,v`, and every slot with `y_u=0` also has `x_u=0`.

Equivalently, the two flattened vectors

```text
vec(X_T), vec(Y_T)
```

are linearly dependent, with `vec(X_T)=-Lambda vec(Y_T)`.

### Proof

If (4) holds, then `x_u=-Lambda y_u`, so (5) follows immediately.

Conversely, suppose all minors (5) vanish.  If every `y_u=0`, then the extra condition gives every
`x_u=0`, so any `Lambda` works.  Otherwise choose `u_0` with `y_{u_0} != 0` and set

```text
Lambda := -x_{u_0}/y_{u_0}.
```

For every `v`, (5) gives

```text
x_v y_{u_0} - x_{u_0} y_v = 0,
```

hence `x_v=-Lambda y_v`.  Thus (4) holds.  `QED`

## 5. Rank-one simplification

Because the ground eigenspace is simple,

```text
Adj(E)=gamma xi xi^*
```

for a nonzero scalar `gamma`.  Therefore (3) reduces to the scalar null components:

```text
Y_T = gamma (K_T xi) xi^*,
X_T = gamma (S_T xi) xi^*.
```

Consequently the minors (5) are equivalent to

```text
(S_alpha xi)(K_beta xi) - (S_beta xi)(K_alpha xi)=0   (6)
```

for every pair of Hermite slots `alpha,beta`, with the same zero-denominator condition.

This recovers E72.351 as the simple-node special case, but now it is written as an exact finite
certificate for arbitrary Xi-zero Hermite windows.

## 6. Why this is not a rowspace repair

E72.352 says that adding `A E` to `R_T` cannot change `R_T xi`.  E72.354 does something different:
it does not add a rowspace correction.  It identifies the necessary and sufficient compatibility
condition for the only legitimate scalar degree of freedom already present in the exact equation.

Thus failure of (5) is a genuine obstruction to scalar CFIR closure for the chosen row construction.
Success of (5), plus the value

```text
Lambda = -x_u/y_u,
```

returns the scalar left coefficient demanded by the transformed Feshbach equation.

## 7. Polynomial version

For the asymptotic certificate, exact vanishing can be replaced by polynomial smallness relative to
the leading Cauchy scale.  Define

```text
Delta_{u,v}:=x_u y_v-x_v y_u.
```

The polynomial Lambda-eliminated certificate is:

```text
|Delta_{u,v}| <= C_T L^B |Adj(E)|_scale^{-2}
```

in the normalization used for `X_T,Y_T`, together with polynomial control on the residual after using
the least-squares scalar

```text
Lambda_* = - <Y_T,X_T> / ||Y_T||^2.
```

For a maximal off-line cluster, the allowed residual is polynomial before applying the inverse
exponential Cauchy block of E72.324--E72.325.

## 8. Updated finite endpoint

The current exact endpoint can now be stated as two nested finite identities:

```text
LAMBDA-ELIM:
  vec(S_T Adj(E)) and vec(K_T Adj(E)) are linearly dependent.

ROW-CFIR:
  for the resulting Lambda_L,
  (Lambda_L K_T+S_T)Adj(E)=0.
```

If `LAMBDA-ELIM` fails, no scalar left coefficient can close the exact residual row.  If it passes,
`ROW-CFIR` is reduced to checking the one recovered scalar value against the independently defined

```text
Lambda_L=mu+e_pole-2kappa_*.
```

## 9. Status

```text
proved: exact affine split R_T^{Xi}(Lambda)=Lambda K_T+S_T;
proved: finite Lambda-elimination criterion by 2x2 minors;
proved: rank-one adjugate reduction to scalar null-component wedges;
open: build K_T,S_T for actual Xi-window nodes and test LAMBDA-ELIM / ROW-CFIR.
```
