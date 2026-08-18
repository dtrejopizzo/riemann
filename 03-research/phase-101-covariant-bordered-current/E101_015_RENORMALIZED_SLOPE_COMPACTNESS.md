# E101.015 - Raw renormalized slope compactness

## 1. Scalar remainder

At the fixed safe normalization point `sigma_0`, define

```text
Q_(L,N)(sigma_0)
 =(L/2)coth(sigma_0 L/2)
  +Re{i T_(L,N)'(i sigma_0)/T_(L,N)(i sigma_0)}.      (1.1)
```

E101.014 gives, for the raw bilateral family,

```text
Q_(L,N)(sigma_0)=sigma_0 M^raw_(L,N)(sigma_0)>=0.    (1.2)
```

## 2. Compactness equivalence

By E101.012, the normalized raw bilateral family is locally bounded if and
only if

```text
RENORMALIZED-SLOPE:
sup_(L,N) Q_(L,N)(sigma_0)<infinity                  (2.1)
```

along the chosen directed family.

Equivalently,

```text
Re{i T_(L,N)'/T_(L,N)}(i sigma_0)
 =-(L/2)coth(sigma_0 L/2)+O(1).                      (2.2)
```

The lower side of the `O(1)` remainder is automatic from (1.2).  Only a
uniform upper bound is required.

## 3. Relation with fixed-length spectral shift

At fixed `L`, E78.153 reduces convergence in `N` of the transfer logarithmic
derivative to summability of consecutive spectral-shift counting functions.
Equation (2.2) isolates the different outer task:

```text
fixed L:  existence of the N-limit of the safe slope;
outer L:  cancellation of its universal slope L/2 up to O(1).       (3.1)
```

These tasks must not be conflated.  The first is a finite-section convergence
problem.  The second is precisely the compactness bound needed for the
real-rooted closure theorem.

## 4. Updated minimal package

For the raw family, the `MASS-BOUND` hypothesis can be replaced exactly by
`RENORMALIZED-SLOPE`.  Thus, if raw identification is used,

```text
RENORMALIZED-SLOPE + LOCAL-COVARIANT-IDENT
 =>Omega7.                                           (4.1)
```

Both statements now use safe determinant data:

```text
RENORMALIZED-SLOPE      one cofactor logarithmic slope;
LOCAL-COVARIANT-IDENT   one signed integrated cofactor current.     (4.2)
```

E101.018--E101.019 sharpen this package: two values supplied by
`LOCAL-COVARIANT-IDENT` imply `RENORMALIZED-SLOPE`.  Hence the slope bound is
a useful compactness coordinate and diagnostic, but it is not a separate
hypothesis in the shortest closure theorem.

For the core family used in the direct anchor, replace (1.1) by

```text
Q^core_(L,N)(sigma_0)
 =sigma_0 sum_(-N+1<=k<=N)1/(d_k^2+sigma_0^2)
  +Re{iT_(L,N)'/T_(L,N)}(i sigma_0).                 (4.3)
```

E101.025 proves `Q_core=sigma_0 M_core`.  This is the relevant core
compactness diagnostic.

## 5. Status

```text
closed:
  exact root-free formulation of the compactness hypothesis;
  separation of the fixed-length and outer-length duties;

open:
  LOCAL-COVARIANT-IDENT;
  Omega7.
```
