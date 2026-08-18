# E85.001 - Exact spectral-ratio formula

## 1. Parity eigenbasis

Let `M` be real symmetric and commute with the mesh reversal `J`.  Choose real
orthonormal eigenvectors

```text
Mp=lambda_p p,
Mq=lambda_q q,                                        (1.1)
```

with `p` in the cluster `P` and `q` in its complement `Q`.  Write

```text
A_p=1^T p,
S_p=s^T p.                                            (1.2)
```

For even vectors `S_p=0`; for odd vectors `A_p=0`.

## 2. Cross-parity matrix elements of D

### Lemma 2.1

If `lambda_p!=lambda_q`, then

```text
q^T Dp=[q^T[D,M]p]/(lambda_p-lambda_q).                (2.1)
```

Consequently,

```text
q^T Dp
 =-(2/L)A_p S_q/(lambda_p-lambda_q),
                  p even, q odd,                      (2.2)

q^T Dp
 = (2/L)S_p A_q/(lambda_p-lambda_q),
                  p odd, q even.                      (2.3)
```

The matrix element is zero when `p` and `q` have the same parity.

### Proof

Taking the `(q,p)` matrix element of

```text
[D,M]=-(2/L)(s1^T-1s^T)                               (2.4)
```

gives (2.1)--(2.3).  Since `D` reverses parity on the symmetric mesh, the
same-parity matrix elements vanish. `QED`

## 3. Exact reduced response

Put

```text
a_P=sum_{p in P_even}A_p^2,
c_P=sum_{p in P_odd}S_p^2,                             (3.1)
```

and use the minimal moment vector

```text
g_P
 =-(L alpha/(2a_P))sum_{p in P_even}A_p p
  +(L beta/(2c_P))sum_{p in P_odd}S_p p.               (3.2)
```

Let

```text
r_P=C^(-1)QD Mg_P.                                    (3.3)
```

### Theorem 3.1

The odd and even eigencomponents of `r_P` are

```text
q^T r_P
 =alpha S_q/a_P
  sum_{p in P_even}A_p^2
   lambda_p/[lambda_q(lambda_p-lambda_q)],
                         q in Q_odd,                  (3.4)

q^T r_P
 =beta A_q/c_P
  sum_{p in P_odd}S_p^2
   lambda_p/[lambda_q(lambda_p-lambda_q)],
                         q in Q_even.                 (3.5)
```

### Proof

Because `Mg_P` lies in `ran P`,

```text
q^T r_P
 =lambda_q^(-1)sum_{p in P}
   lambda_p(q^T Dp)(p^Tg_P).                          (3.6)
```

Insert (2.2)--(2.3) and the coefficients in (3.2).  The factors `2/L` and
`L/2` cancel, yielding (3.4)--(3.5). `QED`

All unknown eigenvector couplings have disappeared.  Only eigenvalues and the
two scalar spectral measures of `1` and `s` remain.

## 4. Status

```text
proved:
  exact cross-parity D matrix elements;
  exact spectral-ratio expansion of the reduced response;

open:
  safe annihilation of the two ratio sums along a cofinal cluster schedule.
```

