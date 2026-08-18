# E78.52 - The radial contraction law is exactly an Euclidean increment inequality

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.50 reduced the modulus side to the local quadratic increment law

```text
2 Re(w_N) + |w_N|^2 < 0,                                  (DEI-1)
```

with

```text
w_N := Delta d_N / d_N,
d_N := 1-theta_N,
Delta d_N := d_N+2 - d_N.                                 (DEI-2)
```

This note removes the remaining quotient normalization and rewrites the same
burden directly in the Euclidean geometry of the shell increment `Delta d_N`
relative to the old denominator vector `d_N`.

## 2. Exact Euclidean identity

Because

```text
Re(w_N)
 = Re(Delta d_N * conj(d_N)) / |d_N|^2
 = <Delta d_N, d_N> / |d_N|^2,                           (DEI-3)
```

and

```text
|w_N|^2 = |Delta d_N|^2 / |d_N|^2,                       (DEI-4)
```

the E78.50 residual becomes

```text
2 Re(w_N) + |w_N|^2
 = ( 2<Delta d_N,d_N> + |Delta d_N|^2 ) / |d_N|^2.       (DEI-5)
```

Since `|d_N|^2 > 0`, we obtain the exact equivalence

```text
DEN-QUADRATIC-RADIAL-INCREMENT
<=> 2<Delta d_N,d_N> + |Delta d_N|^2 < 0.                (DEI-6)
```

Equivalently,

```text
EUCLIDEAN-INCREMENT-LOCK:
  -2<Delta d_N,d_N> > |Delta d_N|^2.                     (DEI-7)
```

So the modulus burden is now a direct inwardness law for the shell increment:
the inward projection of `Delta d_N` onto `d_N` must dominate its full squared
size.

## 3. Why this is the most local form so far

E78.47 phrased the burden as a ratio of radii.
E78.50 moved it to a normalized increment `w_N`.
This note removes that normalization entirely.

The live content is now a single finite inequality in the original shell
vectors:

```text
old denominator vector    d_N,
next increment            Delta d_N.                      (DEI-8)
```

No quotient, argument, or modulus normalization remains.

## 4. Probe audit

Companion data already available:

```text
E78_50_den_quadratic_radial_increment_results.json
E77_5ac_theta_logderiv_coupling_{zeta,plant}.json
```

The equivalence `(DEI-5)` was checked directly from the certified Phase-77
`one_minus_theta` rows.

### Exactness

For both builds:

```text
max reconstruction error < 1e-13.                         (DEI-9)
```

### Zeta

Representative rows:

```text
sigma=1.0, N=10->12:
  <Delta d_N,d_N> = -0.02859934747
  |Delta d_N|^2   =  0.01446494911
  -2<Delta d_N,d_N> - |Delta d_N|^2 = 0.04273374584

sigma=3.0, N=12->14:
  <Delta d_N,d_N> = -0.00460526019
  |Delta d_N|^2   =  0.00175912297
  margin          =  0.00745139741.                      (DEI-10)
```

Across the audited zeta ladder:

```text
median Euclidean margin = 0.0018075796498932093
min    Euclidean margin = 0.000268379781308588
max    Euclidean margin = 0.04273374583597611.           (DEI-11)
```

So on the audited zeta ladder the shell increment points sufficiently inward in
Euclidean projection to beat its own squared size.

### Planted build

Representative rows:

```text
sigma=1.0, N=10->12:
  <Delta d_N,d_N> =  288.09395133
  |Delta d_N|^2   = 2095.11731220
  margin          = -2671.30521486

sigma=3.0, N=12->14:
  <Delta d_N,d_N> = -1313.81356207
  |Delta d_N|^2   =   817.38992102
  margin          =  1810.23720312.                      (DEI-12)
```

So the plant fails exactly where the increment points violently outward in
projection, and can later re-enter the inward regime.

## 5. Consequence

This yields the most local denominator modulus endpoint named so far:

```text
DEN-EUCLIDEAN-INCREMENT-LOCK:
  prove cofinally that -2<Delta d_N,d_N> > |Delta d_N|^2. (DEI-13)
```

Then the earlier chain recovers automatically:

```text
Euclidean increment lock
=> quadratic radial increment negativity
=> radial contraction of |d_N|
=> modulus subunit law
=> denominator direction chain.                           (DEI-14)
```

## 6. Candid reading

This note does not yet prove the inequality cofinally. What it does prove is
that the modulus burden has now been pushed all the way down to a direct shell
comparison in the original denominator vectors.

That is strictly more primitive than the ratio law and more primitive than the
centered quotient language.

## 7. Status

```text
proved:
  2 Re(w_N)+|w_N|^2 = (2<Delta d_N,d_N>+|Delta d_N|^2)/|d_N|^2 exactly;

proved:
  DEN-QUADRATIC-RADIAL-INCREMENT is exactly equivalent to the Euclidean
  increment inequality -2<Delta d_N,d_N> > |Delta d_N|^2;

observed:
  zeta satisfies this audited Euclidean inwardness law with positive margin on
  every tested row;

observed:
  the planted build fails exactly where the increment projection turns strongly
  outward;

reduced:
  DEN-QUADRATIC-RADIAL-INCREMENT to DEN-EUCLIDEAN-INCREMENT-LOCK;

next:
  isolate a finite shell law for the signed projection <Delta d_N,d_N>, or
  split that projection into an even smaller radial-plus-angular scalar pair.
```
