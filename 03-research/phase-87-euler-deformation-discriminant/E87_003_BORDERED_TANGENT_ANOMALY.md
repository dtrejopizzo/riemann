# E87.003 - Exact bordered tangent anomaly

## 1. Tangent of the coupled solve

On an interval of `t` where the selected finite spectral branch is simple,
write

```text
M_t x_t=b_t.                                          (1.1)
```

Then

```text
dot x_t=M_t^(-1)y_t,
y_t=dot b_t-dot M_t x_t.                              (1.2)
```

### Proof

Differentiate (1.1):

```text
dot M_t x_t+M_t dot x_t=dot b_t.                      (1.3)
```

Rearrangement gives (1.2). `QED`

For `H_t=H_A-tH_P` and

```text
M_t=H_t^in-mu_t I,
b_t=b_A-tb_P,                                         (1.4)
```

the tangent source is

```text
y_t=-b_P+H_P^in x_t+dot mu_t x_t.                     (1.5)
```

If the full eigenvalue is simple with normalized eigenvector `xi_t`, the
Hellmann--Feynman formula gives

```text
dot mu_t=-xi_t^T H_P xi_t.                            (1.6)
```

## 2. Tangent of the bordered determinant

Let

```text
G_t(z)=c_t-q^T(zI-D)^(-1)x_t,
c_t=1-1^T x_t.                                        (2.1)
```

Define

```text
h_z^T=1^T+q^T(zI-D)^(-1.                              (2.2)
```

Then

```text
G_t(z)=1-h_z^T x_t,                                   (2.3)

partial_t log G_t(z)
 =-[h_z^T M_t^(-1)y_t]/G_t(z).                        (2.4)
```

Equation (2.4) is also

```text
Tr(B_t(z)^(-1)dot B_t(z)),                             (2.5)
```

where `B_t(z)` is the bordered matrix in E81.002.  It is a bordered trace,
not the spectral resolvent trace of `H_t`.

## 3. Bilateral anomaly

Put `u=s-1/2` and define

```text
Phi_{L,N,t}(s)
 =partial_t log[G_t(iu)G_t(-iu)],                     (3.1)

K_{L,N,t}(s)=Phi_{L,N,t}(s)-J_L(s).                   (3.2)
```

Let

```text
R_{L,N,t}(s)=C_{L,N,t}(s)/E_{L,t}(s).                 (3.3)
```

All explicit factors in `C` are independent of `t`, so

```text
partial_t log R_{L,N,t}(s)=K_{L,N,t}(s).              (3.4)
```

### Theorem 3.1 - deformation identity

On every simply connected safe domain on which the branches remain zero-free,

```text
log[R_{L,N,1}(s)/R_{L,N,0}(s)]
 =integral_0^1 K_{L,N,t}(s)dt.                        (3.5)
```

### Proof

Integrate (3.4) in `t`. `QED`

Piecewise-simple branches satisfy the same identity after subdivision.  A
global proof through a multiple branch must use the full cluster determinant,
not choose an eigenline through a crossing.

## 4. Formal split and its correction

After fixed-`L` convergence, the two separate statements

```text
ARCH-BASE:
partial_s log R_{L,0}(s)->0,                           (4.1)

TANGENT-ANOMALY:
integral_0^1 partial_s K_{L,t}(s)dt->0                (4.2)
```

would be sufficient locally uniformly on `Re s>1`.  However E87.005 shows
that this is an over-strong proof split: the two terms have to cancel and are
not estimated separately.  The corrected target is

```text
D_{L,0}(s)+integral_0^1 partial_s K_{L,t}(s)dt->0.     (4.3)
```

The force-bearing arithmetic term is now the scalar tangent response

```text
h_z^T M_t^(-1)
 ( -b_P+H_P^in x_t+dot mu_t x_t )                     (4.4)
```

inside the bilateral normalized quotient.

## 5. Status

```text
proved:
  exact tangent source;
  exact derivative of the bordered determinant;
  exact deformation identity;

reduced:
  the arithmetic discriminant to the combined deformation identity (4.3);

open:
  fixed-L cluster-safe passage in t;
  the outer signed cancellation in (4.3).
```
