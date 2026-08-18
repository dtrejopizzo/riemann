# E94.001 - Exact global cofactor current

## 1. Data

Let `M` be the real symmetric inner CCM block shifted by the selected finite
level, let `b` be the raw right boundary column and let

```text
h_z^T=1^T+q^T(zI-D)^(-1).                             (1.1)
```

Define

```text
Delta=det M,
y=adj(M)b.                                           (1.2)
```

The global bordered numerator is

```text
N(z)
 =det[[M,b],[h_z^T,1]]
 =Delta-h_z^T y.                                     (1.3)
```

Equation (1.3) is a polynomial identity in the entries of `M` and `b`; it
does not require `M` to be invertible.

## 2. Safe derivative

Since

```text
partial_z h_z^T=-q^T(zI-D)^(-2),                     (2.1)
```

one has

```text
N'(z)=q^T(zI-D)^(-2)y.                               (2.2)
```

Where `N(z)` is nonzero,

```text
N'(z)/N(z)
 =[q^T(zI-D)^(-2)adj(M)b]
  /[det M-h_z^Tadj(M)b].                             (2.3)
```

No spectral gap, pseudoinverse or eigenline occurs in (2.3).

## 3. Bilateral current

Put `u=s-1/2`.  The exact bordered contribution to the logarithmic derivative
is

```text
i N'(iu)/N(iu)-i N'(-iu)/N(-iu).                     (3.1)
```

Multiplication of `N` by any nonzero scalar independent of `z` leaves (3.1)
unchanged.  Thus common determinant scales may be cleared before estimating.

## 4. Status

```text
proved:
  exact global adjugate numerator;
  exact inverse-free safe derivative;
  exact bilateral cofactor current.
```

