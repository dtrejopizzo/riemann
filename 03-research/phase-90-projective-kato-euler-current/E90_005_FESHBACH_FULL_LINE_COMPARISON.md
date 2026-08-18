# E90.005 - Feshbach and full-line comparison

## 1. Energy-dependent Schur equation

Write

```text
M_t=[A_t B_t;
     B_t^* C_t].                                      (1.1)
```

If `(kappa_t,v_t)` is a full eigenpair and `v_t=(p_t,r_t)`, then, whenever
`C_t-kappa_t I` is invertible,

```text
r_t=-(C_t-kappa_t I)^(-1)B_t^*p_t,                   (1.2)

[A_t-B_t(C_t-kappa_t I)^(-1)B_t^*]p_t
 =kappa_t p_t.                                       (1.3)
```

Thus the exact full spectral line is represented by an energy-dependent
Schur complement.  The static complement in E88.001 is the value at zero.

## 2. Static-lift error

The resolvent identity gives

```text
(C_t-kappa_t I)^(-1)-C_t^(-1)
 =kappa_t(C_t-kappa_t I)^(-1)C_t^(-1).               (2.1)
```

Hence

```text
norm[r_t+C_t^(-1)B_t^*p_t]
 <=|kappa_t|
   norm[(C_t-kappa_t I)^(-1)]
   norm[C_t^(-1)B_t^*p_t].                           (2.2)
```

For the bordered profile,

```text
|h_zv_t-h_(t,z)^eff p_t|
 <=norm[h_(Q,z)] |kappa_t|
   norm[(C_t-kappa_t I)^(-1)]
   norm[C_t^(-1)B_t^*p_t].                           (2.3)
```

Therefore the static Feshbach profile and the full spectral profile agree
projectively provided the right side of (2.3) is uniformly small relative to
one nonvanishing base profile.

## 3. Consequence

The Schur-row transport term in E89.003 is not an additional arithmetic
source.  It is the coordinate expression of the motion of the full spectral
line.  The full-space formula E90.002 absorbs it automatically and shows that
the only operator rotating that line is the prime matrix.

The comparison still requires a complementary resolvent bound.  It cannot be
deduced from `kappa_t->0` alone.

## 4. Status

```text
proved:
  exact energy-dependent Schur equation;
  exact static-lift error identity and bound;
  equivalence of the two profile coordinates under an explicit relative
  error hypothesis;

open:
  the uniform complementary resolvent and nonvanishing estimates needed in
  the matched layer.
```

