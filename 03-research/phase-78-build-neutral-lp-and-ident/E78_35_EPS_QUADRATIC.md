# E78.35 - `eps_N` is an exact quadratic defect

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.34 rewrote the vertical defect as

```text
eps_N = 1 - det_norm_N,                                   (EQ-1)
```

where `det_norm_N` is the normalized determinant of
`(theta'_N, 1-theta_N)`.

This note turns that scalar into an exact quadratic defect.

## 2. Exact quadratic identity

Let

```text
a_hat_N := theta'_N / |theta'_N|,
b_hat_N := (1-theta_N) / |1-theta_N|,                     (EQ-2)
```

and let `J(x,y)=(y,-x)` be the `-pi/2` rotation.

From E78.34,

```text
det_norm_N = a_hat_N . J b_hat_N,                         (EQ-3)
```

because both vectors are unit vectors.

Therefore

```text
||a_hat_N - J b_hat_N||^2
 = ||a_hat_N||^2 + ||J b_hat_N||^2 - 2 a_hat_N . J b_hat_N
 = 2 - 2 det_norm_N.                                      (EQ-4)
```

Hence

```text
EPS-QUADRATIC:
eps_N
 = 1 - det_norm_N
 = (1/2) ||a_hat_N - J b_hat_N||^2.                       (EQ-5)
```

So the angular defect is exactly a quadratic misalignment energy between the
normalized numerator vector and the rotated normalized denominator vector.

Combining E78.33, E78.34, and `(EQ-5)` gives

```text
angular_term_N
 = |u_N| ( ||a_hat_N - J b_hat_N||^2
         - ||a_hat_N+2 - J b_hat_N+2||^2 ).               (EQ-6)
```

Thus the open angular front is the shell drift of a positive quadratic defect.

## 3. Probe audit

Companion:

```text
E78_35_eps_quadratic_probe.py
E78_35_eps_quadratic_results.json
```

The probe reconstructs `(EQ-5)` directly from the certified `E77.5ac` points.

### Exactness

For both builds:

```text
max reconstruction error < 1e-15.                         (EQ-7)
```

So the quadratic formula is exact to roundoff.

### Zeta

Representative rows:

```text
sigma=1.0, N= 8 new:  quadratic_defect = 0.0018550564382456836
sigma=1.0, N=20 new:  quadratic_defect = 0.23271317503611433
sigma=3.0, N=18 new:  quadratic_defect = 0.00791781311610218. (EQ-8)
```

These are exactly the `eps_N` values from E78.34, hence small on the audited
zeta ladder except for the known low-sigma tail weakening.

### Planted build

Representative rows:

```text
sigma=1.0, N= 8 old:  quadratic_defect = 1.9936608761590813
sigma=1.0, N=10 old:  quadratic_defect = 1.4016864148908432
sigma=3.0, N= 8 old:  quadratic_defect = 1.9611188228805345. (EQ-9)
```

So the planted build is far from the rotated alignment already at the level of
this positive quadratic energy.

## 4. Consequence

This is the cleanest reduced target so far for the angular side:

```text
DET-NORM-DRIFT-SMALLNESS
<=>
QUADRATIC-DEFECT-DRIFT-SMALLNESS,                         (EQ-10)
```

where the live object is the positive scalar

```text
Qdef_N := (1/2) || theta'_N/|theta'_N| - J(1-theta_N)/|1-theta_N| ||^2. (EQ-11)
```

Then

```text
MODULUS-GAIN-DOMINANCE
+ QUADRATIC-DEFECT-DRIFT-SMALLNESS
=> DELTA-SAFEU-GEOMETRIC-ENVELOPE.                        (EQ-12)
```

This is a genuine improvement over E78.34 because the target is now manifestly
nonnegative and quadratic.

## 5. Candid reading

This note does not yet prove the shell drift bound for `Qdef_N`. What it does
is identify the angular difficulty with a positive quadratic misalignment
functional on exact finite data.

That is exactly the sort of theorem-grade object the phase has been trying to
name.

## 6. Status

```text
proved:
  eps_N is exactly half the squared distance between normalized theta'_N and
  the -pi/2 rotation of normalized (1-theta_N);

proved:
  the reconstruction holds to roundoff for both builds;

observed:
  zeta keeps this quadratic defect small on the audited ladder;

observed:
  the planted build has order-one quadratic defect, matching the angular
  failure;

reduced:
  DET-NORM-DRIFT-SMALLNESS to QUADRATIC-DEFECT-DRIFT-SMALLNESS;

next:
  derive a shell drift law for the quadratic defect from the exact updates of
  theta'_N and 1-theta_N.
```
