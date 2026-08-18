# E101.045 - Directional IDENT attribution

## 1. Finite normalized boundary problem

Let

```text
D_N=diag(d_(-N),...,d_N)
```

be a real simple mesh and let `V_N` be its coordinate space.  Write

```text
ell_N(v)=1^T v,
X_N=ker ell_N.                                      (1.1)
```

Let `M_N:V_N->W_N` be the finite rectangular CCM block.  Assume that the
normalized boundary problem has a unique solution:

```text
M_N y_N=0,
ell_N(y_N)=1.                                       (1.2)
```

Let `k_N` be any normalized comparison vector,

```text
ell_N(k_N)=1,
e_N=M_N k_N.                                        (1.3)
```

The relevant observation is not the ambient vector difference.  For
`z` outside the mesh define the normalized Cauchy row

```text
C_(N,z)(v)=z sum_j v_j/(z-d_j).                     (1.4)
```

Because of the normalization in (1.2)--(1.3), this is exactly the bilateral
factor of E101.043:

```text
B_(y_N)(z)=C_(N,z)(y_N),
B_(k_N)(z)=C_(N,z)(k_N).                            (1.5)
```

## 2. Directional Green functional

The uniqueness in (1.2) is equivalent to

```text
ker M_N intersect X_N={0}.                          (2.1)
```

Indeed, a nonzero vector in the intersection can be added to `y_N` without
changing either equation in (1.2), and the difference of two normalized
solutions belongs to that intersection.

Consequently the restricted map

```text
T_N=M_N|_(X_N):X_N->ran T_N                         (2.2)
```

is injective.  On its range define the directional Green functional

```text
Psi_(N,z)=C_(N,z) T_N^(-1).                         (2.3)
```

No inverse on all of `W_N` is used.  The inverse in (2.3) is only the
algebraic inverse from `ran T_N` to `X_N`, followed immediately by the
selected Cauchy row.

### Theorem 2.1 - Exact directional error identity

For every `z` outside the mesh,

```text
C_(N,z)(y_N)-C_(N,z)(k_N)=-Psi_(N,z)(e_N).          (2.4)
```

If `B_(k_N)(z)!=0`, then

```text
B_(y_N)(z)/B_(k_N)(z)-1
=-Psi_(N,z)(e_N)/B_(k_N)(z).                       (2.5)
```

### Proof

By (1.2)--(1.3),

```text
y_N-k_N in X_N,
T_N(y_N-k_N)=-e_N.                                  (2.6)
```

Thus `e_N` belongs to `ran T_N` and

```text
y_N-k_N=-T_N^(-1)e_N.                               (2.7)
```

Applying `C_(N,z)` proves (2.4).  Division by (1.5) proves (2.5). `QED`

## 3. Exact form of SAFE-PROLATE-BRIDGE

Let `K` be a compact safe set disjoint from the mesh, and suppose

```text
inf_(z in K)|B_(k_N)(z)|>0.                         (3.1)
```

Then (2.5) gives the equivalence

```text
sup_(z in K)|B_(y_N)(z)/B_(k_N)(z)-1| ->0

iff

sup_(z in K)|Psi_(N,z)(e_N)|/|B_(k_N)(z)| ->0.     (3.2)
```

The left side is the projective boundary-to-model bridge.  The right side
is its exact residual formulation.  Define it as

```text
DIRECTIONAL-IDENT(K).                               (3.3)
```

Thus no additional compactness theorem lies between directional
identification and `SAFE-PROLATE-BRIDGE`: they are the two sides of the
finite identity (2.5).

## 4. Optimal directional stability constant

On `X_N` define

```text
||v||_(K,k_N)
=sup_(z in K)|C_(N,z)(v)|/|B_(k_N)(z)|.            (4.1)
```

If `K` has an accumulation point in the resolvent set, (4.1) is a norm.
Indeed, vanishing of the rational Cauchy transform on such a set implies
that it vanishes identically; its residues then give `v_j=0` for every `j`.

For any norm `||.||_(Y_N)` on `W_N`, put

```text
beta_N(K;k_N)
=inf{||T_N v||_(Y_N):
      v in X_N, ||v||_(K,k_N)=1}.                  (4.2)
```

Finite-dimensional injectivity gives `beta_N>0`.  Moreover,

```text
sup_(z in K)|Psi_(N,z)(q)|/|B_(k_N)(z)|
<=||q||_(Y_N)/beta_N(K;k_N)                        (4.3)
```

for `q in ran T_N`, and `1/beta_N` is the best possible constant in
(4.3).

### Proof

Write `q=T_Nv`.  The left side of (4.3) equals `||v||_(K,k_N)` by (2.3).
The definition (4.2) gives

```text
beta_N||v||_(K,k_N)<=||T_Nv||_(Y_N).               (4.4)
```

This proves (4.3).  Taking an infimizing sequence in (4.2) proves
optimality. `QED`

In particular,

```text
||e_N||_(Y_N)/beta_N(K;k_N)->0                     (4.5)
```

is sufficient for the bridge.  Bare injectivity, or bare limit-point
uniqueness, asserts only `beta_N>0` section by section.  It gives no lower
bound of the scale required in (4.5).  This is the exact reason an ambient
small-residual proof can fail even after uniqueness has been established.

## 5. Coupled radical decomposition

For the normalized prolate comparison vector, P76.063 gives

```text
e_N=E_(PROLATE,N)+E_(WEIL,N)+E_(FOURIER,N).         (5.1)
```

The three terms denote, respectively, physical prolate error, omitted Weil
support, and the Fourier shell.  Substitution into (2.5) gives

```text
B_(y_N)(z)/B_(k_N)(z)-1
=-{Psi_(N,z)(E_(PROLATE,N)+E_(WEIL,N)
                       +E_(FOURIER,N))}
  /B_(k_N)(z).                                      (5.2)
```

Equation (5.2) fixes the order of operations.  The three terms are summed
before an absolute value is taken.  Separate ambient bounds on them are not
required and, in the ill-conditioned regime, can be much stronger than the
actual theorem.

The remaining prolate route is therefore the single estimate

```text
sup_(z in K)
|Psi_(N,z)(E_(PROLATE,N)+E_(WEIL,N)+E_(FOURIER,N))|
/|B_(k_N)(z)| ->0.                                  (5.3)
```

This is the normalized bordered Cauchy pairing requested in P76.063, now
written as a precise functional identity.

## 6. LP and IDENT attribution

The operational LP statements of the earlier route concern contraction of
finite Weyl disks and uniqueness of their normalized limit.  In the finite
language above, their role is to justify (2.1) and to prevent two different
safe limit transforms.

They do not evaluate the right side of (2.5).  In particular,

```text
LP:
  uniqueness of the admissible normalized direction;

IDENT:
  vanishing of the arithmetic residual in that direction.     (6.1)
```

Under the Outcome-A attribution established in the preceding work, the
operational LP mechanism is shared by the zeta and planted constructions.
Therefore a consequence using only LP hypotheses is build-neutral.  The
falsifier can be rejected only when the model residual is paired as in
(5.3), or in an equivalent Gamma-prime, Stieltjes, or heat formulation.

This proves the attribution statement:

```text
the force-RH step of the LP+IDENT chain is IDENT,
represented exactly by DIRECTIONAL-IDENT(K).        (6.2)
```

The statement does not prove (5.3).  It proves that a further attempt to
extract the discriminant from qualitative LP contraction cannot close the
chain under Outcome A.

## 7. Transfer to the squared determinant and heat current

Taking `k_N` as the comparison vector `w` in E101.044 gives

```text
mathcal R_(y_N,k_N)(zeta)
=B_(y_N)(sqrt(zeta))B_(y_N)(-sqrt(zeta))
 /[B_(k_N)(sqrt(zeta))B_(k_N)(-sqrt(zeta))].        (7.1)
```

Hence DIRECTIONAL-IDENT on the two square-root sector rays implies weighted
convergence of `log mathcal R_(y_N,k_N)`.  The sector formula of E101.044
then gives convergence of the corresponding finite heat traces.

After the explicit prime and mesh heat tails of E101.041 are removed, this
is the same coupled core comparison appearing in `HEAT-COFACTOR-IDENT` and
`GAUSSIAN-WEIL-QUADRATURE`.  The following diagram records implications,
not additional assumptions:

```text
DIRECTIONAL-IDENT on sector rays
        |
        v
projective squared-determinant convergence
        |
        v
coupled finite heat convergence
        |
        v
LOCAL-COVARIANT-IDENT
        |
        v
Omega7.                                             (7.2)
```

The load-bearing estimate is the first arrow's hypothesis, namely (5.3).
Sector stability, Gaussian tail bounds, and LP uniqueness are the closed
infrastructure surrounding it.

## 8. Status

```text
proved:
  exact directional Green identity;
  equivalence of SAFE-PROLATE-BRIDGE and paired residual convergence;
  optimal directional inf-sup constant;
  exact insertion of the coupled radical decomposition;
  attribution of the force-RH step to IDENT under Outcome A;

closed as insufficient:
  qualitative LP uniqueness without a paired-residual estimate;
  ambient residual smallness without control relative to beta_N;
  sectorial stability before boundary-to-model identification;

open:
  DIRECTIONAL-IDENT, the estimate (5.3).
```
