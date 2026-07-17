# E72.26 -- Bordered pencil formula for the finite CCM divisor current

**Date:** 2026-07-08.
**Role:** replace root tracking and false vector transport by an exact finite determinant/current
identity for the Weyl numerator.

## 0. Finite data

Let

```text
D_x = diag(d_{x,k}),
1_x = (1,1,...,1)^T,
xi_x = finite CCM ground vector,
m_x(s)=xi_x^T (sI-D_x)^(-1)1_x.
```

Write

```text
m_x(s)=P_x(s)/Q_x(s),
Q_x(s)=det(sI-D_x).
```

The finite CCM divisor is the zero set of `P_x`.

## 1. Bordered pencil

Define the bordered linear pencil

```text
B_x(s) :=
  [ 0        xi_x^T ]
  [ 1_x      sI-D_x ].
```

This is a finite `(n_x+1) x (n_x+1)` matrix depending linearly on `s`.

## 2. Determinant identity

### Lemma 72.26

For every `s` off the pole mesh,

```text
det B_x(s) = - P_x(s).                            (BD)
```

Consequently,

```text
P_x'(s)/P_x(s)
 = Tr( B_x(s)^(-1) B_x'(s) ).                     (BC)
```

### Proof

Take the Schur complement of the lower-right block `sI-D_x`:

```text
det B_x(s)
 = det(sI-D_x) det( 0 - xi_x^T(sI-D_x)^(-1)1_x )
 = - Q_x(s)m_x(s)
 = - P_x(s).
```

Differentiating `log det B_x(s)=log(-P_x(s))` gives

```text
d/ds log P_x(s)
 = Tr(B_x(s)^(-1)B_x'(s)).
```

`QED`

## 3. Explicit inverse check

Solving the bordered system gives another expression:

```text
B_x(s)^(-1)B_x'(s)
```

has trace

```text
m_x'(s)/m_x(s)+Q_x'(s)/Q_x(s),
```

which matches E72.23. Thus the bordered pencil is not a new approximation; it is the exact same
finite current in determinant form.

## 4. Why the bordered pencil matters

The false E72.24 ansatz tried to transport the vector

```text
r_x(s)=(sI-D_x)^(-1)1_x.
```

The correct object transports the finite pencil

```text
B_x(s).
```

Current convergence becomes a resolvent-trace convergence problem:

```text
Tr(B_x(s)^(-1)B_x'(s)) -> Xi'(s)/Xi(s).           (BTC)
```

This is exactly the two-height current convergence needed by E72.22.

## 5. Fredholm limit target

The new proof target is:

### Bordered Fredholm Convergence

There exists a limiting trace-class/Fredholm pencil `B(s)` such that:

```text
B_x(s) -> B(s)
```

in trace-resolvent sense on two interior horizontal lines, and

```text
det B(s) = c Xi(s)
```

with `c != 0`.

Then:

```text
Tr(B_x^(-1)B_x') -> Tr(B^(-1)B') = Xi'/Xi,
```

so E72.22 and E72.19 imply RH.

## 6. Non-circularity gate

This target is admissible if `B(s)` is constructed as the operator limit of:

```text
D_x,
1_x,
xi_x
```

from finite CCM data.

It is circular if `B(s)` is defined by declaring

```text
det B(s)=Xi(s).
```

The determinant identity must be a theorem of the finite CCM/Fredholm limit.

## 7. Status

```text
proved: finite CCM divisor current equals bordered pencil trace current;
open:   prove bordered Fredholm convergence and identify the determinant with Xi.
```

This is now the cleanest algebraic form of the Schur-free convergence problem.
