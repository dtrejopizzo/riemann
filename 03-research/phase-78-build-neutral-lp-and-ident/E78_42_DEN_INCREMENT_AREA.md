# E78.42 - The denominator shell numerator is an increment area

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.41 reduced the denominator side to the symplectic shell numerator

```text
det(d_N+2, d_N),  where d_N := 1-theta_N.                (DIA-1)
```

This note removes one more layer of redundancy: the same numerator depends only
on the shell increment `Delta d_N := d_N+2 - d_N` against the old vector `d_N`.

## 2. Exact increment-area identity

Define

```text
Delta d_N := d_N+2 - d_N.                                 (DIA-2)
```

By bilinearity and antisymmetry of the planar determinant,

```text
det(d_N+2, d_N)
 = det(d_N + Delta d_N, d_N)
 = det(d_N, d_N) + det(Delta d_N, d_N)
 = det(Delta d_N, d_N).                                   (DIA-3)
```

So the denominator live numerator is exactly the oriented area of the shell
increment against the old denominator vector.

Combining with E78.41 gives

```text
Im((1-theta_N+2)/(1-theta_N))
 = det(Delta d_N, d_N) / |d_N|^2.                         (DIA-4)
```

This is the cleanest increment form so far.

## 3. Probe audit

Companion:

```text
E78_42_den_increment_area_probe.py
E78_42_den_increment_area_results.json
```

The probe reconstructs `(DIA-3)` directly from the certified `E77.5ac` points.

### Exactness

For both builds:

```text
max reconstruction error < 1e-13.                         (DIA-5)
```

So the increment-area identity is exact to roundoff.

### Zeta

Representative rows:

```text
sigma=1.0:
  N=10->12  det(Delta d_N, d_N) =  5.5077714030365475e-05
  N=20->22  det(Delta d_N, d_N) = -3.719533327334706e-07

sigma=3.0:
  N=10->12  det(Delta d_N, d_N) =  1.3868502617626975e-04
  N=20->22  det(Delta d_N, d_N) = -1.0772061934513116e-06. (DIA-6)
```

So on the audited zeta ladder the live denominator numerator is already visible
as a tiny shell increment area.

### Planted build

Representative rows:

```text
sigma=1.0:
  N=10->12  det(Delta d_N, d_N) = 102.62259880005914
  N=12->14  det(Delta d_N, d_N) = 580.6428674678534

sigma=3.0:
  N=10->12  det(Delta d_N, d_N) = 108.13070351260096
  N=12->14  det(Delta d_N, d_N) = 710.7946495420936.      (DIA-7)
```

So the falsifier fails directly through a huge shell increment area.

## 4. Consequence

This yields a smaller finite target:

```text
control the oriented area between the shell increment Delta d_N and the old
denominator vector d_N.                                   (DIA-8)
```

Equivalently,

```text
small increment area
+ denominator scale
=> small Im(q_b,N)
=> denominator rigidity chain.                            (DIA-9)
```

This is a real reduction because the new numerator depends on one increment and
one base vector, rather than on two full shell vectors symmetrically.

## 5. Honest reading

This note does not yet prove the increment area is small cofinally. What it does
is identify the exact increment object that carries the denominator obstruction.

That is a better theorem-grade target than the two-shell determinant itself.

## 6. Status

```text
proved:
  det(1-theta_N+2,1-theta_N) is exactly det(Delta d_N,d_N) with
  Delta d_N = d_N+2-d_N;

proved:
  the reconstruction holds to roundoff for both builds;

observed:
  zeta keeps the increment area tiny on the audited ladder;

observed:
  the planted build fails through huge increment areas at the early steps;

reduced:
  the denominator bilinear numerator to an increment-area target;

next:
  normalize the increment area by |Delta d_N| |d_N| or autopsy it into an even
  smaller directional increment law.
```
