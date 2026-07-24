# E96.001 - Polarized determinant derivative

## 1. Directional derivative

Let `X` be an `m` by `m` matrix and let `Y` be a direction.  Define

```text
delta_Y det X
 =d/d epsilon det(X+epsilon Y)|_(epsilon=0).          (1.1)
```

Then

```text
delta_Y det X
 =sum_(a,b) Cof_(a,b)(X)Y_(a,b).                     (1.2)
```

Equation (1.2) is valid for singular `X`.

### Proof

The determinant is multilinear in its rows.  The coefficient of `epsilon`
in `det(X+epsilon Y)` is obtained by replacing one row of `X` by the
corresponding row of `Y`.  Expansion of each replacement along that row gives
(1.2). `QED`

## 2. Polarized form

If `Det_m` denotes the symmetric polarization normalized by

```text
Det_m(X,...,X)=det X,                                 (2.1)
```

then

```text
delta_Y det X
 =m Det_m(Y,X,...,X).                                 (2.2)
```

Thus every determinant derivative is linear in the direction `Y`, regardless
of the rank or invertibility of `X`.

## 3. Application

Both

```text
P(t,mu,z),
chi(t,mu)                                             (3.1)
```

are determinants of matrices affine in the prime operator.  Their
deformation derivatives can therefore be expanded cell by cell before any
quotient is formed.

## 4. Status

```text
proved:
  singular-safe directional derivative formula;
  polarized determinant representation.
```

