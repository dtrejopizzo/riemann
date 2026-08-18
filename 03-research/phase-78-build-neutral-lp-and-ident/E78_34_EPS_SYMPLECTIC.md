# E78.34 - `eps_N` is a normalized symplectic defect

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.33 reduced the angular mechanism to the real defect sequence

```text
eps_N := 1 - Im(u_N)/|u_N|,                               (ES-1)
```

with

```text
angular_term_N = 2 |u_N| (eps_N - eps_N+2).              (ES-2)
```

This note removes `u_N` from the definition of `eps_N` itself.

## 2. Exact symplectic formula

Write

```text
a_N := theta'_N,
b_N := 1 - theta_N.                                       (ES-3)
```

Since

```text
u_N = -a_N / b_N,                                         (ES-4)
```

the imaginary share of `u_N` is

```text
Im(u_N)/|u_N|
 = det(a_N, b_N) / (|a_N| |b_N|),                         (ES-5)
```

where

```text
det(x+iy, A+iB) := xB - yA.                               (ES-6)
```

Therefore

```text
EPS-SYMPLECTIC:
eps_N
 = 1 - det(theta'_N, 1-theta_N)
       / (|theta'_N| |1-theta_N|).                        (ES-7)
```

So `eps_N` is exactly a normalized symplectic defect of the pair
`(theta'_N, 1-theta_N)`.

Combining `(ES-2)` and `(ES-7)` gives the exact angular law

```text
angular_term_N
 = 2 |u_N| (det_norm_N+2 - det_norm_N),                   (ES-8)
```

with

```text
det_norm_N := det(theta'_N, 1-theta_N)
              / (|theta'_N| |1-theta_N|).                 (ES-9)
```

Thus `EPS-DRIFT-SMALLNESS` is equivalently a drift control for the normalized
symplectic determinant.

## 3. Probe audit

Companion:

```text
E78_34_eps_symplectic_probe.py
E78_34_eps_symplectic_results.json
```

### Exactness

The probe reconstructs `(ES-7)` directly from the certified `E77.5ac` points.

For both builds:

```text
max reconstruction error < 1e-15.                         (ES-10)
```

So the formula is exact to roundoff.

### Zeta

Representative rows:

```text
sigma=1.0, N= 8 new:  det_norm = 0.9981449435617542,  eps = 0.0018550564382456836
sigma=1.0, N=18 new:  det_norm = 0.93557902734401,    eps = 0.06442097265599
sigma=3.0, N=18 new:  det_norm = 0.9920821868838978,  eps = 0.00791781311610218. (ES-11)
```

Across the audited zeta ladder:

```text
det_norm stays positive and close to 1.                   (ES-12)
```

That is the exact algebraic content behind the small angular correction.

### Planted build

Representative rows:

```text
sigma=1.0, N= 8 old:  det_norm = -0.9936608761590816, eps = 1.9936608761590813
sigma=1.0, N= 8 new:  det_norm =  0.0459561956210513, eps = 0.9540438043789486
sigma=3.0, N=10 old:  det_norm = -0.34729198576408543, eps = 1.3472919857640853. (ES-13)
```

So the planted build fails already at the determinant level: the normalized
symplectic alignment can even be negative.

## 4. Consequence

This yields a sharper reduced target:

```text
EPS-DRIFT-SMALLNESS
<=>
DET-NORM-DRIFT-SMALLNESS,                                 (ES-14)
```

where the live object is now the drift of the explicit real scalar

```text
det_norm_N
 = det(theta'_N, 1-theta_N)/(|theta'_N||1-theta_N|).      (ES-15)
```

Thus the sign-side front can be rewritten as

```text
MODULUS-GAIN-DOMINANCE
+ DET-NORM-DRIFT-SMALLNESS
=> DELTA-SAFEU-GEOMETRIC-ENVELOPE.                        (ES-16)
```

This is a genuine reduction: `det_norm_N` is algebraic in the already-certified
finite objects `theta'_N` and `1-theta_N`, with no residual dependence on the
phase of `u_N`.

## 5. Candid reading

This note does not yet prove the needed drift bound for `det_norm_N`. What it
does prove is that the open angular front has been reduced to a normalized
determinant of the exact finite Schur data.

That is a much better target than an opaque angle variable.

## 6. Status

```text
proved:
  eps_N is exactly 1 minus the normalized determinant of (theta'_N, 1-theta_N);

proved:
  the reconstruction holds to roundoff for both builds;

observed:
  on the audited zeta ladder the determinant stays positive and close to 1;

observed:
  on the planted ladder the determinant can be small or negative, explaining
  the large angular defect;

reduced:
  EPS-DRIFT-SMALLNESS to DET-NORM-DRIFT-SMALLNESS;

next:
  seek a theorem-grade shell drift law for det_norm_N from the exact updates of
  theta'_N and 1-theta_N.
```
