# E93.005 - Proof-effort allocation

## 1. Primary front

All primary effort should target the finite identity

```text
partial_s log
 det[[M_(L,N),b_(L,N)],
     [h_(L,N,iu),1]]

 plus its bilateral partner and explicit mesh factors

 minus H_L(s).                                       (1.1)
```

The task is to show that the base-point-subtracted form of (1.1) tends to
zero along a resolved directed family.

## 2. Admissible methods

The two methods that act directly on the force-bearing object are

```text
A. BORDERED CELL IDENTITY
   derive a finite Gamma--Euler product rule for the bordered determinant,
   retaining every boundary and Fourier-compression term;

B. BORDERED STIELTJES IDENTITY
   construct an independent even arithmetic shift from the Gamma--prime
   functional and prove convergence of the bordered spectral shift to it. (2.1)
```

The two methods are equivalent at the target level but expose different
error terms.

## 3. Secondary front

Fixed-`L` convergence should be pursued only if it yields an estimate that
enters method A or B.  A stand-alone proof of GAP-Z would close optional
infrastructure but would leave (1.1) untouched.

The endpoint-layer calculations remain useful only when they produce an
exact cofactor or boundary term in (1.1).  Estimates of collapsing eigenvalues
or matched widths are retired.

## 4. Next theorem

The next phase should compute the derivative of the global bordered
determinant directly from the entrywise Gamma--prime cell formula and split it
into

```text
independent Euler current
+ explicit boundary/compression defect.              (4.1)
```

The defect must remain one coupled scalar.  Absolute cellwise estimates are
inadmissible because finite truncation is not positive.

