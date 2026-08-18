# E78.41 - `Im(q_b,N)` is an exact bilinear quotient

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.40 reduced the denominator side to

```text
DEN-IMAG-SMALLNESS:
  control Im(q_b,N),                                      (DBI-1)
```

for

```text
q_b,N := (1-theta_N+2)/(1-theta_N).                       (DBI-2)
```

This note removes the quotient opacity and rewrites `Im(q_b,N)` as an exact
bilinear shell functional.

## 2. Exact bilinear formula

Write

```text
d_N := 1 - theta_N.                                       (DBI-3)
```

Then

```text
q_b,N = d_N+2 / d_N = d_N+2 * conj(d_N) / |d_N|^2.       (DBI-4)
```

Taking imaginary parts gives

```text
Im(q_b,N)
 = Im( d_N+2 * conj(d_N) ) / |d_N|^2.                     (DBI-5)
```

Equivalently, with the planar determinant

```text
det(z,w) := Im(z) Re(w) - Re(z) Im(w),                    (DBI-6)
```

we obtain the exact identity

```text
DEN-IMAG-BILINEAR:
Im(q_b,N)
 = det(d_N+2, d_N) / |d_N|^2.                             (DBI-7)
```

So the live denominator quantity is an oriented shell area divided by the old
denominator norm square.

## 3. Probe audit

Companion:

```text
E78_41_den_imag_bilinear_probe.py
E78_41_den_imag_bilinear_results.json
```

The probe reconstructs `(DBI-7)` directly from the certified `E77.5ac` points.

### Exactness

For both builds:

```text
max reconstruction error < 1e-15.                         (DBI-8)
```

So the bilinear formula is exact to roundoff.

### Zeta

Representative rows:

```text
sigma=1.0:
  N=10->12  Im(q_b,N) =  9.740448567951879e-04
            det(d_N+2,d_N) =  5.619007438857176e-05
            |d_N|^2        =  5.769927830178377e-02

sigma=3.0:
  N=12->14  Im(q_b,N) = -4.60174785080823e-03
            det(d_N+2,d_N) = -2.179022834265111e-04
            |d_N|^2        =  4.735114973945906e-02.     (DBI-9)
```

So the tiny zeta imaginary part is already visible as a tiny oriented shell area
relative to a moderate denominator scale.

### Planted build

Representative rows:

```text
sigma=1.0:
  N=10->12  Im(q_b,N) = 2.298807664619163

sigma=3.0:
  N=10->12  Im(q_b,N) = 2.2817795781118035.               (DBI-10)
```

So the plant fails through a large oriented shell area, not through any hidden
complex quotient pathology.

## 4. Consequence

This yields the cleanest denominator endpoint so far:

```text
control the symplectic shell numerator
det(1-theta_N+2, 1-theta_N)
relative to |1-theta_N|^2.                                (DBI-11)
```

Equivalently,

```text
small symplectic shell numerator
+ positive denominator scale
=> small Im(q_b,N)
=> denominator rigidity chain.                            (DBI-12)
```

This is a genuine reduction because the live object is now a single bilinear
finite functional on consecutive denominator vectors.

## 5. Candid reading

This note does not yet prove the numerator is small cofinally. What it does is
remove the last quotient mystery from the denominator side: the live quantity is
an explicit oriented area over a known scale.

That is exactly the sort of finite object the phase has been trying to isolate.

## 6. Status

```text
proved:
  Im((1-theta_N+2)/(1-theta_N)) is exactly
  det(1-theta_N+2,1-theta_N)/|1-theta_N|^2;

proved:
  the reconstruction holds to roundoff for both builds;

observed:
  zeta keeps this bilinear shell numerator tiny relative to the denominator
  scale on the audited ladder;

observed:
  the planted build fails through a large bilinear shell numerator;

reduced:
  DEN-IMAG-SMALLNESS to a bilinear shell-area target;

next:
  seek an exact shell law for det(1-theta_N+2,1-theta_N), or autopsy it into a
  still smaller normalized numerator target.
```
