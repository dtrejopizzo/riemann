# E101.017 - Renormalized-slope falsifier audit

## 1. Quantity tested

The root-free raw Stieltjes mass

```text
M^raw_(L,N)(sigma)
 ={1/sigma}{
    (L/2)coth(sigma L/2)
    +Re[iT_(L,N)'/T_(L,N)](i sigma)
  }                                                  (1.1)
```

was computed directly from the multiprecision Gamma--prime CCM entries.
The same computation was repeated after inserting the established off-line
plant into the finite Weil matrix.

The safe point was `sigma=1.25`.  No zero finder was used.

## 2. Outer-length sweep

For cutoff `N=6`, the values are

```text
L             zeta M             planted M
2.1972        0.0606006          0.861828
2.7726        0.0834650          1.11593
3.2189        0.106921           1.01116
3.5835        0.126234           1.41709.
```

Two additional, more resolved sections give

```text
L             N       zeta M             planted M
4.1589        8       0.131124           1.49917
4.6052        8       0.155939           1.57687.
```

## 3. Fixed-length resolution check

At `L=3.5835`, increasing the cutoff gives

```text
N             zeta M
6             0.126234
8             0.103291
10            0.0892356.                              (3.1)
```

Thus the outer sweep at a fixed small cutoff must not be read as an
asymptotic trend; the finite-section correction is visible and has the sign
predicted by the spectral-shift analysis.

## 4. Interpretation

The plant does not produce an immediate growth instability in the raw mass
(1.1).  Both
systems remain controlled over the tested range, although they approach
different values and at different rates.  This is the behavior expected of a
compactness input that may be build-neutral.

Since `M_core<=M_raw`, the audit also gives finite-range upper evidence for
the core mass.  It therefore supports the allocation

```text
RENORMALIZED-SLOPE       compactness infrastructure;
LOCAL-COVARIANT-IDENT   arithmetic discriminant.     (4.1)
```

It does not prove either assertion.  In particular, bounded finite data do
not establish a uniform outer-length estimate.

## 5. Status

```text
observed:
  no plant-specific blowup of the renormalized Stieltjes mass;
  visible finite-section convergence on the zeta build;

supported but open:
  build-neutrality of RENORMALIZED-SLOPE;

open:
  analytic uniform bound and local covariant identification.
```
