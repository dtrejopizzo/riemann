# E101.061 - Abel-polynomial no-go and diagonal obstruction

## 1. Decision

E101.060 proves an exact bilateral Abel identity and proposes the sufficient
uniform bounds

```text
||A_z^+-A_z^-||_(Linf(0,1))=O(1),
||B_z^++B_z^-||_(Linf(0,1))=O(1).                  (1.1)
```

The bounds (1.1) are false as a consequence of the dual equation and the
rank-two displacement law.  They can fail even when

```text
the rectangular block has full row rank;
the normalized kernel converges;
the comparison residual tends to zero;
the desired scalar dual pairing tends to zero.       (1.2)
```

Thus the Abel identity survives, but a source-independent uniform dual norm
is rejected as the proof mechanism.

## 2. Exact dual Bezout equation

Let `d_i` be the shared row and column nodes and let `e` be an additional
column node.  Suppose

```text
(d_i-d_j)M_(i,j)=-a[s(d_i)-s(d_j)]                 (2.1)
```

off the diagonal.  Let `pM=q` and define

```text
eta_i=M_(i,i)+a s'(d_i),                            (2.2)

F_p(lambda)
=sum_i p_i [s(d_i)-s(lambda)]/(d_i-lambda).         (2.3)
```

The singularities in (2.3) are removable.

### Theorem 2.1

At every shared node,

```text
eta_i p_i-aF_p(d_i)=q_i.                            (2.4)
```

At an additional column node,

```text
-aF_p(e)=q_e.                                       (2.5)
```

If

```text
Delta(lambda)=prod_i(lambda-d_i),

P_1(lambda)=Delta(lambda)sum_i p_i/(lambda-d_i),
P_s(lambda)=Delta(lambda)sum_i p_i s(d_i)/(lambda-d_i),  (2.6)
```

then

```text
F_p(lambda)
=[s(lambda)P_1(lambda)-P_s(lambda)]/Delta(lambda).  (2.7)
```

### Proof

At a shared node,

```text
F_p(d_i)
=p_i s'(d_i)
 +sum_(j!=i)p_j[s(d_j)-s(d_i)]/(d_j-d_i).           (2.8)
```

Use (2.1) in the `i`-th column of `pM=q` and separate the diagonal term.
This gives (2.4).  At the external node, every entry is fixed by (2.1),
which gives (2.5).  Finally, put the two sums in (2.3) over the common
denominator `Delta`; the result is (2.7). `QED`

The obstruction is visible in (2.4): displacement does not determine the
diagonal numbers `eta_i`.  For an actual CCM block,

```text
eta_i=2C_L(d_i)-mu.                                 (2.9)
```

Therefore any proof of (1.1) must use quantitative information about the
full Gamma--Euler cosine symbol and the chosen level.  Rank-two displacement
alone cannot supply it.

## 3. Symmetric exact counterexample

Take

```text
L=2pi,
h=1,
a=1/pi,

d=(-1,0,1),
e=(-1,0,1,2),

s(x)=pi(7x-x^3)/6.                                  (3.1)
```

Thus

```text
(s(-1),s(0),s(1),s(2))=(-pi,0,pi,pi).              (3.2)
```

For `delta!=0`, define

```text
M_delta=
[ -1/3+delta   -1       -1       -2/3 ]
[ -1           -3/2     -1       -1/2 ]
[ -1           -1       -1/3+delta  0  ].           (3.3)
```

### Proposition 3.1

The family (3.3) satisfies the exact rectangular displacement law

```text
D_rM_delta-M_deltaD_c
=-1/pi(s_r1^T-1s_c^T).                              (3.4)
```

Its shared three-by-three block `H_delta` is symmetric and centrosymmetric,

```text
det H_delta=-delta(1+3delta/2),                     (3.5)

H_delta u=delta(1,0,1)^T,
u=(1,-4/3,1)^T.                                     (3.6)
```

Hence `M_delta` has full row rank for all sufficiently small nonzero
`delta`.

### Proof

Every off-diagonal entry in (3.3) satisfies (3.4) by direct substitution of
(3.1)--(3.2); diagonal entries are unconstrained by a commutator with `D`.
Direct expansion gives (3.5), and matrix multiplication gives (3.6). `QED`

## 4. Convergent kernel and small comparison residual

The normalized kernel is

```text
y_delta=
( 3/[2(2+3delta)],
 -1/2,
 -3/[2(2+3delta)],
  3/2 )^T,                                          (4.1)

M_delta y_delta=0,
1^T y_delta=1.                                      (4.2)
```

It converges to the fixed comparison vector

```text
k=(3/4,-1/2,-3/4,3/2)^T,                            (4.3)
```

which satisfies

```text
M_delta k
=delta(3/4,0,-3/4)^T.                               (4.4)
```

Thus the ambient comparison residual is `O(delta)` and the normalized
boundary line itself converges.

## 5. Divergent Abel polynomials

Choose `z=i`, let

```text
c_j=z/(z-e_j),
B_(y_delta)=c y_delta,
q=c-B_(y_delta)1^T,                                 (5.1)
```

and let `pM_delta=q`.  Normalize by the fixed model value

```text
b=B_k=ck=-1/5+3i/20!=0.                             (5.2)
```

Since `pH_delta=q_shared`, equation (3.6) gives

```text
delta(p_(-1)+p_1)=q_shared u.                       (5.3)
```

As `delta->0`,

```text
q_shared u->-1/5-i/10!=0.                           (5.4)
```

Consequently the even Abel polynomials of E101.060 are

```text
P_A(t)=A^+(t)-A^-(t)
=pi[p_(-1)+p_1](1-t^2)/b,                          (5.5)

P_B(t)=B^+(t)+B^-(t)
=1/b {
 [q_shared u/delta](1-4t/3+t^2)
 -(4/3)q_0t
 }.                                                 (5.6)
```

Both norms in (1.1) diverge like `1/|delta|`.

The BMOA replacement diverges as well.  The first Taylor coefficient of the
Abel transform `Kcal P_A` is

```text
1/pi integral_0^1P_A(t)dt
=2[p_(-1)+p_1]/(3b),                                (5.7)
```

and the corresponding coefficient of the leading polynomial in (5.6) is
also nonzero.  Since a BMOA norm controls every fixed Taylor coefficient, no
uniform BMOA bound is possible in this family.

## 6. The scalar pairing still closes

The singular dual mode in (5.3) is even, whereas the residual (4.4) is odd.
Indeed, the vector `(1,0,-1)` is an eigenvector of `H_delta` with eigenvalue
`2/3+delta`, so `p_(-1)-p_1` remains bounded.  Therefore

```text
pM_delta k
=3delta[p_(-1)-p_1]/4
->0.                                                (6.1)
```

Equations (5.5)--(5.7) and (6.1) prove the decisive separation:

```text
the source-adapted scalar tends to zero;
every proposed uniform Abel dual norm diverges.      (6.2)
```

Thus a uniform dual bound is not merely unproved.  It is strictly stronger
than the scalar theorem and can fail while that theorem holds.

## 7. Canonical CCM diagnostic

The companion computation

```text
E101_061_abel_polynomial_probe.py                    (7.1)
```

rebuilds the multiprecision CCM entries, constructs the canonical
right-bordered block, solves the bordered dual equation and reconstructs the
odd symbol from the same build.  With `lambda=6`, `z=i` and normalization
`b=B_(k_N)(i)`, it gives

```text
             arithmetic build          inserted-quartet build
N        ||P_A||inf   ||P_B||inf      ||P_A||inf   ||P_B||inf
3        3.682e12     1.954e13        9.689e9      2.504e11
4        8.707e14     3.416e15        8.455e11     2.969e13
5        1.480e16     4.550e16        4.564e12     1.359e14
6        2.837e17     7.045e17        1.261e13     8.642e13.       (7.2)
```

The adjoint residuals are below `10^(-49)` in the arithmetic run and the
displacement defects are below `10^(-70)`.  Repeating the largest sections at
higher precision preserves the displayed digits.  The experiment is not an
asymptotic proof, but it agrees with the exact no-go mechanism.

The size depends strongly on normalization.  Normalization by `||p||_2`
makes the two polynomials small, but that is not the projective normalization
in DIRECTIONAL-IDENT.  The relevant denominator is `B_(k_N)(z)`.

## 8. Consequence for the route

The following statements are rejected as main targets:

```text
uniform ABEL-POLYNOMIAL-EXTERIOR;
uniform BMOA boundedness of the two dual generators;
uniform H2 boundedness obtained by treating the generators separately.
                                                               (8.1)
```

The exact bilateral identity E101.060 remains valid.  What survives is only
a source-adapted estimate of the complete integral

```text
integral_0^1[P_A(t)C_N(t)-P_B(t)D_N(t)]dt/t,         (8.2)
```

with both generator channels retained.  Estimating `P_A` and `P_B`
separately loses the even--odd cancellation exhibited in (6.1).

Using the actual diagonal (2.9) could in principle control a weighted
directional channel.  A coercive bound for the full adjoint Loewner operator,
however, is the old directional inf-sup wall unless it evaluates (8.2)
through a new finite arithmetic identity.

## 9. Status

```text
proved:
  exact dual Bezout equation and diagonal obstruction;
  symmetric full-rank counterexample;
  kernel convergence and O(delta) comparison residual;
  divergence of the polynomial and BMOA dual norms;
  simultaneous convergence of the source-adapted scalar;

verified:
  explosive growth in canonical multiprecision CCM sections;

rejected:
  source-independent Abel, BMOA and separate-generator H2 bounds;

retained:
  the exact coupled Abel integral as a diagnostic coordinate;

open:
  a new finite identity for the source-adapted current;
  DIRECTIONAL-IDENT and Omega7.
```
