# E86.001 - Exact finite spectral Abel identity

## 1. Ordered complementary data

Fix one parity channel.  Write the complementary eigenvalues as

```text
eta_P<lambda_1<=lambda_2<=...<=lambda_m,               (1.1)
```

and put

```text
d_j=-Delta_P(lambda_j),
b_j(z)=L_z(q_j)X_{q_j},
B_j(z)=sum_{k=1}^j b_k(z).                             (1.2)
```

Here `X_q=S_q` in the even-cluster-to-odd-complement channel and `X_q=A_q`
in the odd-cluster-to-even-complement channel.

By E85.004,

```text
d_1>=d_2>=...>=d_m>0.                                 (1.3)
```

### Proof of monotonicity

For every cluster eigenvalue `lambda`, the function

```text
lambda/[x(x-lambda)]                                  (1.4)
```

is positive and strictly decreasing for `x>lambda`.  Averaging against the
positive cluster measure proves (1.3).

## 2. Abel identity

### Theorem 2.1

One has the exact identity

```text
sum_{j=1}^m b_j(z)d_j
 =B_m(z)d_m
  +sum_{j=1}^{m-1}B_j(z)(d_j-d_{j+1}).                (2.1)
```

### Proof

Write `b_j=B_j-B_{j-1}` with `B_0=0`, expand the sum and shift the second
index.  All interior terms telescope and both endpoints remain. `QED`

Since the Weyl defect is `Delta_P=-d`, the corresponding parity response is
the negative of the right side of (2.1), multiplied by `alpha` or `beta`.

## 3. Crude ceiling consequence

Equation (2.1) gives

```text
|sum_j b_jd_j|
 <=d_1 max_{1<=j<=m}|B_j|.                            (3.1)
```

This bound preserves cancellation inside each cumulative sum, but it replaces
the location of the cumulative peaks by their global maximum.  It is only a
sufficient condition and must be checked numerically before being adopted as
a theorem target.

The same identity holds after one safe `z` derivative because the `d_j` do
not depend on `z`.

## 4. Status

```text
proved:
  monotonicity of the spectral Weyl weights;
  exact endpoint-retaining Abel identity;
  crude cumulative ceiling bound;

open:
  whether the crude ceiling has the correct scale.
```

