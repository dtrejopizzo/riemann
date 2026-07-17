# E73.206 - High-precision closed matrix entries

Date: 2026-07-14.

## 1. Purpose

E73.205 shows that the bordered eigenline certificate cannot be built from the
legacy double/quadrature matrix.  This note starts the replacement: construct
the finite matrix entries from the same closed finite-frequency + digamma tail
functional used in E73.199.

## 2. Entry modes

For the finite basis index pair `(m,n)`, the kernel entry is:

```text
Q_mn(y)=2(1-y/L)cos(d_n y)                         if m=n,
Q_mn(y)=(sin(d_m y)-sin(d_n y))/(pi(n-m))          if m!=n,
d_j=2pi j/L.
```

Thus every entry is already a finite-frequency packet:

```text
Q_mn(y)=sum c_omega e^(iomega y)+y sum l_omega e^(iomega y).
```

The high-precision entry is:

```text
H_mn=A_L^digamma[Q_mn]-P_L[Q_mn],
```

or just `A_L^digamma[Q_mn]` for the model matrix.

## 3. Status

```text
implemented: high-precision closed matrix entry centers;
verified: comparison against legacy quadrature matrix on small windows;
not yet: outward-rounded interval entries.
```
