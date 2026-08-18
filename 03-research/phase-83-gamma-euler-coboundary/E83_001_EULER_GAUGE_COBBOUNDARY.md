# E83.001 - Exact Euler gauge coboundary

## 1. Semigroup algebra

Let `e_n` be the multiplicative shift basis,

```text
e_m e_n=e_{mn},
delta(e_n)=(log n)e_n.                                 (1.1)
```

With Abel regularization, define

```text
Z_epsilon=sum_{n>=1}n^(-epsilon)e_n,
M_epsilon=sum_{n>=1}mu(n)n^(-epsilon)e_n.              (1.2)
```

Dirichlet convolution gives

```text
M_epsilon Z_epsilon=Z_epsilon M_epsilon=e_1.           (1.3)
```

The Euler connection is

```text
A_epsilon
 = Z_epsilon^(-1)delta Z_epsilon
 = M_epsilon delta Z_epsilon
 = sum_{n>=2}Lambda(n)n^(-epsilon)e_n.                 (1.4)
```

## 2. Gauge identity

Let the algebra act on a module on which `delta` obeys the Leibniz rule.

### Proposition 2.1

For every vector `v` in the common domain,

```text
(delta+A_epsilon)v
 = Z_epsilon^(-1)delta(Z_epsilon v).                   (2.1)
```

Equivalently,

```text
A_epsilon v
 = Z_epsilon^(-1)delta(Z_epsilon v)-delta v.           (2.2)
```

If `delta k=0`, then

```text
A_epsilon k
 = Z_epsilon^(-1)delta((Z_epsilon-I)k).                (2.3)
```

### Proof

The Leibniz rule gives

```text
delta(Zv)=(delta Z)v+Z delta v.
```

Multiplication by `Z^{-1}` proves (2.1)--(2.2).  If `delta k=0`, subtract
`delta k` inside the right side to obtain (2.3). `QED`

Thus the prime current is an exact gauge coboundary in the Euler module.  No
sign or zero-location input is used.

## 3. Riccati identity

Differentiating `Z^{-1}Z=I` gives

```text
delta(A_epsilon)+A_epsilon^2
 = Z_epsilon^(-1)delta^2 Z_epsilon.                    (3.1)
```

This identity is internal to the Euler algebra.  It supplies no map from the
Euler module to the Gamma/CCM complement.

## 4. Status

```text
proved:
  the exact Euler gauge identities (2.1)--(2.3);
  the Riccati identity (3.1);

closed:
  algebraic origin of the candidate coboundary;

open:
  transport of (2.3) into the actual CCM complement;

next:
  state an exact intertwiner criterion that produces the correction u_N
  without applying the complement inverse.
```

