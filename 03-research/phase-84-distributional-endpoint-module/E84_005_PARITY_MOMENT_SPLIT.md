# E84.005 - Parity split of the moment problem

## 1. Exact parity structure

Let `J` reverse the symmetric mesh.  Since `S_L` is odd and the CCM matrix is
centrosymmetric,

```text
J1=1,
Js=-s,
JM=MJ.                                                (1.1)
```

Every spectral projection `P` of `M` therefore commutes with `J`.  It follows
that

```text
P1 is even,
Ps is odd,
1^T Ps=0.                                             (1.2)
```

### Theorem 1.1

The moment Gram matrix of E84.004 is exactly diagonal:

```text
G_B=diag(a_P,c_P),                                    (1.3)

a_P=1^T P1,
c_P=s^T Ps.                                           (1.4)
```

It is invertible if and only if `P1` and `Ps` are both nonzero.  In that
case the minimal moment vector is

```text
g_P
 =-(L alpha/(2a_P))P1+(L beta/(2c_P))Ps,              (1.5)

norm(g_P)^2
 =L^2 alpha^2/(4a_P)+L^2 beta^2/(4c_P).               (1.6)
```

### Proof

The cross entry in the Gram matrix is the inner product of an even vector and
an odd vector, hence is zero.  Equations (1.3)--(1.4) follow.  Substitution in
E84.004, equation (1.5), gives (1.5), and orthogonality of its two terms gives
(1.6). `QED`

Thus the two-moment determinant is not the arithmetic discriminant of Phase
79.  It is a parity-diagonal nonvanishing condition, and it can hold for both
the arithmetic build and an off-line control.

## 2. What can still degenerate

Although there is no angular conditioning problem, either spectral mass can
collapse:

```text
a_P=sum_{p in P_even}|1^T p|^2,
c_P=sum_{p in P_odd}|s^T p|^2.                         (2.1)
```

The norm (1.6) then grows.  Consequently the correct small parameter is not
only the spectral width

```text
eta_P=norm(MP),                                       (2.2)
```

but the coupled quantities

```text
eta_P |alpha|/sqrt(a_P),
eta_P |beta|/sqrt(c_P).                               (2.3)
```

Even their decay controls only `Mg_P`, not the reduced response.

## 3. Finite diagnostic

For the exact multiprecision CCM section with `L=2 log 6`, take `P` to be the
nearest even and nearest odd eigenline of the inner shifted matrix.  Let `e`
and `C^(-1)e` be the exact vectors in E84.003, and test the Cauchy row at
`z=i`.  The direct calculation gives

```text
outer modes   norm(g_P)    norm(e)       norm(C^(-1)e)   |ell_i(C^(-1)e)|
4             1.58         7.49e-12      2.76e-3         1.28e-3
6             3.64e2       3.37e-16      3.60e-1         1.31e-1
8             1.82e5       7.32e-18      1.88e2          6.07e1.          (3.1)
```

The coboundary identity residual in these calculations is below the working
multiprecision floor.  Table (3.1) is diagnostic rather than asymptotic proof,
but it decisively falsifies the inference

```text
norm(e)->0  implies  ell(C^(-1)e)->0.                  (3.2)
```

## 4. Cluster enlargement

On the same sections, include the nearest `r` even and `r` odd eigenlines.
The absolute safe response behaves as follows:

```text
outer modes   r=1        r=2        r=3        r=4
6             1.31e-1    1.10e-3    2.40e-5    5.74e-6
8             6.07e1     2.34       5.27e-2    6.93e-4.               (4.1)
```

The response decreases when the cluster absorbs more of the collapsing
spectral cascade, but every fixed `r` deteriorates as the section grows in
this diagnostic.  This isolates the next quantitative question:

```text
find a cofinal rank r_N for which
  r_N grows slowly enough to preserve the projective limit,
  P_N captures both parity moment masses,
  ell(C_N^(-1)e_N) tends to zero safely.                (4.2)
```

## 5. Status

```text
proved:
  exact parity diagonalization of the moment Gram matrix;
  explicit two-sector minimal corrector;
  identification of the two separate moment masses;

refuted by exact finite calculation:
  small unreduced error as a substitute for reduced leakage;
  any fixed two-line cluster as the observed asymptotic mechanism;

localized:
  the remaining problem to a cofinal cluster-rank law and safe spectral-ratio
  leakage.
```

