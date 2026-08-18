# Phase 90 closure - Prime-response localization

## 1. Closed mathematics

The full spectral decomposition removes the moving Feshbach row.  For a
simple dominant spectral line `v_t`, its projective safe profile is

```text
phi_t(z)=h_zv_t.                                      (1.1)
```

Its exact Kato current is

```text
partial_t log[phi_t(z)/phi_t(z_*)]
 =sum_n Lambda(n)n^(-1/2)K_t(z,z_*;log n),           (1.2)
```

where

```text
K_t(z,z_*;y)
 =[h_z S_t Q_y^in v_t]/[h_zv_t]
  -[h_(z_*) S_t Q_y^in v_t]/[h_(z_*)v_t]             (1.3)
```

and `S_t=(M_t-kappa_t I)^dagger` is the reduced resolvent.

The scalar motion `dot mu_t I` has no off-diagonal spectral matrix element
and disappears exactly from (1.2).  The line rotation is driven only by the
prime matrix.

## 2. Exact arithmetic defect

The bilateral layer current and the independent Euler current are now two
finite von Mangoldt sums.  Their difference is the explicit kernel defect
E90.004(3.2).  No zero list and no interchange of infinite sums is used.

## 3. Force-bearing clause

The remaining statement is

```text
PROJECTIVE-KATO-EULER:
BASE-BULK+LAYER-DEF+DOM-ERR->0.                       (3.1)
```

This is RDI-ANCHOR expressed through the prime-response kernel.  It is the
current force-bearing clause, not an independent weakening of RDI.

## 4. Closure grade

```text
closed:
  full spectral residue formula;
  cancellation of scalar eigenvalue motion from line rotation;
  exact prime-cell expansion;
  exact bilateral Euler-matching defect;
  comparison of static Feshbach and full spectral coordinates;

open and transferred:
  DOM-M and matched-layer uniformity;
  complementary resolvent and profile nonvanishing;
  PROJECTIVE-KATO-EULER;
  RDI-ANCHOR and Omega7.
```

