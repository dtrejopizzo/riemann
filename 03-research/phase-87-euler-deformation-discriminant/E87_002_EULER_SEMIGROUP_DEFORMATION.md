# E87.002 - Exact Euler semigroup deformation

## 1. Fractional Euler gauge

In the finite truncated-shift algebra, `Z` is invertible and every positive
shift is nilpotent.  Hence `log Z` is a finite algebraic sum and one may define

```text
Z_t=exp(t log Z),  0<=t<=1.                            (1.1)
```

The shift algebra is commutative.  Therefore `log Z` commutes with its scale
derivative and

```text
Z_t^(-1)delta Z_t=t delta(log Z).                      (1.2)
```

At `t=1`,

```text
delta(log Z)=Z^(-1)delta Z=A.                          (1.3)
```

Thus

```text
A_t=Z_t^(-1)delta Z_t=tA.                              (1.4)
```

### Proof

Differentiate the exponential in the commutative algebra:

```text
delta exp(t log Z)
 =exp(t log Z)t delta(log Z).                          (1.5)
```

Multiplication by `Z_t^{-1}` gives (1.2).  The usual logarithmic derivative
identity in a commutative algebra gives (1.3), and hence (1.4). `QED`

## 2. Linear CCM deformation

After Hermitian symmetrization, let

```text
H_P=A+A^*.                                            (2.1)
```

Then the deformation induced by (1.4) is exactly

```text
H_t=H_A-tH_P.                                         (2.2)
```

This is the arithmetic deformation already available at the finite CCM
level, now derived from the fractional Euler gauge.

## 3. Independent product deformation

Define

```text
E_{L,t}(s)
 =s^2(s-1)^2 pi^(-s)Gamma(s/2)^2
  exp(2t sum_{2<=n<=exp(L)}Lambda(n)n^(-s)/log n).     (3.1)
```

Then

```text
partial_t log E_{L,t}(s)
 =J_L(s),                                             (3.2)

J_L(s)=2 sum_{2<=n<=exp(L)}Lambda(n)n^(-s)/log n.     (3.3)
```

The endpoints are the archimedean primitive and the finite Euler--Gamma
primitive of E80.002.

## 4. Status

```text
proved:
  exact fractional Euler gauge in the finite shift algebra;
  exact linear prime deformation of the CCM operator;
  exact matching deformation of the independent product;

open:
  comparison of their bordered determinant currents along t.
```

