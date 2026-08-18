# E84.003 - Rank-two source coboundary

## 1. Displacement equation

Let

```text
M=H-mu I,
D=diag(d_j),
s=(S_L(d_j))_j.                                       (1.1)
```

The exact Loewner representation gives

```text
[D,M]=-(2/L)(s 1^T-1 s^T).                            (1.2)
```

Let

```text
f=alpha s+beta 1.                                     (1.3)
```

## 2. Two-moment representation

### Theorem 2.1

If a vector `g` satisfies

```text
1^T g=-(L/2)alpha,
s^T g= (L/2)beta,                                     (2.1)
```

then

```text
f=[D,M]g.                                             (2.2)
```

Conversely, (2.2) holds if and only if the two moment conditions (2.1) hold,
unless `s` and `1` are linearly dependent, in which case (2.1) is replaced by
the corresponding single compatible condition.

### Proof

Applying (1.2) to `g` gives

```text
[D,M]g
 =-(2/L)(1^Tg)s+(2/L)(s^Tg)1.                        (2.3)
```

Substitution of (2.1) proves (2.2).  If `s` and `1` are independent,
comparison of their coefficients gives the converse.  The dependent case is
the same coefficient comparison in their one-dimensional span. `QED`

This is the finite algebraic form of the endpoint-source identity.  The two
boundary distributions become exactly the two moment rows of the displacement
operator.

## 3. Exact complement coboundary

Let `P` be a spectral projection of `M`, put `Q=I-P`, and define

```text
C=QMQ.                                                (3.1)
```

Since `P` and `Q` commute with `M`, Theorem 2.1 yields

```text
Qf=QD Mg-QM Dg
   =QD Mg-CQDg.                                       (3.2)
```

Therefore the explicit vector

```text
u=-QDg                                                (3.3)
```

satisfies the inverse-free coboundary

```text
Qf=Cu+e,
e=QD Mg.                                              (3.4)
```

No inverse of `C` occurs in the construction of `u`.

## 4. Correct remaining estimate

If `C` is invertible on `ran Q`, the exact response error is

```text
C^(-1)e=C^(-1)QD Mg.                                  (4.1)
```

Thus the required safe estimate is

```text
sup_{z in K}|ell_z(C^(-1)QD Mg)| -> 0,                 (4.2)
```

together with one safe derivative.  Ambient bounds on `C^(-1)` are neither
required nor expected.

If `g` is chosen in a small spectral cluster, then `Mg` is small before the
unbounded reduced response is applied.  Formula (4.2), rather than
`norm(Mg)->0`, is the load-bearing assertion.

## 5. Status

```text
proved:
  exact two-moment commutator representation of the coupled source;
  explicit inverse-free corrector u=-QDg;
  exact reduced error e=QD Mg;

closed:
  construction part of TWO-GENERATOR-ARITHMETIC-COBOUNDARY;

open:
  selection of g inside the spectral cluster with the two prescribed moments;
  safe reduced leakage estimate (4.2).
```

