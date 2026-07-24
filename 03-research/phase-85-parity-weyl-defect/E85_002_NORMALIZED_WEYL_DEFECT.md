# E85.002 - Normalized Weyl-defect form

## 1. Cluster spectral measures

Define probability measures on the cluster eigenvalues by

```text
omega_P^E
 =a_P^(-1)sum_{p in P_even}A_p^2 delta_{lambda_p},

omega_P^O
 =c_P^(-1)sum_{p in P_odd}S_p^2 delta_{lambda_p}.       (1.1)
```

Their finite Weyl functions are

```text
m_P^E(z)=integral d omega_P^E(lambda)/(lambda-z),
m_P^O(z)=integral d omega_P^O(lambda)/(lambda-z).      (1.2)
```

## 2. Algebraic collapse

The identity

```text
lambda/[z(lambda-z)]=1/z+1/(lambda-z)                 (2.1)
```

turns E85.001 into the following theorem.

### Theorem 2.1

For every complementary eigenvector,

```text
q^T r_P
 =alpha S_q Delta_P^E(lambda_q),
                         q in Q_odd,                  (2.2)

q^T r_P
 =beta A_q Delta_P^O(lambda_q),
                         q in Q_even,                 (2.3)
```

where

```text
Delta_P^E(z)=1/z+m_P^E(z),
Delta_P^O(z)=1/z+m_P^O(z).                            (2.4)
```

### Proof

Apply (2.1) inside the normalized sums (3.4)--(3.5) of E85.001. `QED`

The function `Delta_P` measures the failure of the cluster spectral measure
to be the point mass at zero, whose Weyl function is `-1/z`.

## 3. Moment expansion and its range

If `|lambda|<|z|` on the support of `omega_P`, then

```text
Delta_P(z)
 =-sum_{k>=1} m_k(P)/z^(k+1),                         (3.1)

m_k(P)=integral lambda^k d omega_P(lambda).           (3.2)
```

### Proof

Expand

```text
1/(lambda-z)=-(1/z)sum_{k>=0}(lambda/z)^k             (3.3)
```

and cancel the `k=0` term with `1/z`. `QED`

The expansion is useful only when the complementary eigenvalue is outside the
cluster radius.  Taking absolute values gives the sufficient bound

```text
|Delta_P(z)|
 <=eta_P/[|z|(|z|-eta_P)],                             (3.4)
```

where `eta_P=max{|lambda|:lambda in supp omega_P}`.  This bound is not the
target theorem: it discards signed spectral moments and can be much too large
near the cluster edge.

## 4. Exact safe scalar

Let `L_z(q)=ell_z(q)`.  Equations (2.2)--(2.3) give

```text
ell_z(r_P)
 =alpha sum_{q in Q_odd}L_z(q)S_q Delta_P^E(lambda_q)
  +beta sum_{q in Q_even}L_z(q)A_q Delta_P^O(lambda_q). (4.1)
```

This is the complete finite scalar `WRL` in parity Weyl coordinates.  The
cofinal theorem must be proved for (4.1) and its `z` derivative without
replacing the signed sums by (3.4) term by term.

## 5. Status

```text
proved:
  exact normalized Weyl-defect representation;
  convergent moment expansion away from the cluster;
  elementary absolute sufficient bound;
  exact safe scalar formula;

localized:
  WRL to two normalized cluster Weyl defects.
```

