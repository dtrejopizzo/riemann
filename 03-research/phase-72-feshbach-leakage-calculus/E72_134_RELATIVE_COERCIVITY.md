# E72.134 -- Relative complement coercivity

**Date:** 2026-07-09.
**Role:** replace crude Weyl dominance by a form-relative coercivity theorem.

## 0. Relative criterion

E72.133 shows that:

```text
||C_actual-C_model||
```

is too large for a crude Weyl proof, even though `C_actual` is strongly coercive.  The right sufficient
criterion is:

```text
C_actual >= theta_H C_model,        theta_H>0,               (RCOER)
```

as quadratic forms on the even Feshbach complement.

If also:

```text
C_model >= a_H L I,                                           (MCOER)
```

then:

```text
C_actual >= theta_H a_H L I,
```

which is exactly `(COER)` from E72.132.

## 1. Diagnostic

The companion script:

```text
E72_134_relative_coercivity_probe.py
```

computes the generalized eigenvalues of:

```text
C_actual v = lambda C_model v.
```

The minimum generalized eigenvalue is the largest admissible `theta_H`.

Representative output:

```text
E72.134 relative coercivity probe
 lam   L  minGen(act/model)  maxGen  minModel/L  theta*minModel/L
   6  3.58          5.747e-01 1.607e+00   7.296e-01         4.193e-01
   8  4.16          5.109e-01 1.569e+00   9.918e-01         5.067e-01
  10  4.61          6.226e-01 1.495e+00   1.221e+00         7.601e-01
  12  4.97          4.259e-01 1.463e+00   1.514e+00         6.450e-01
  14  5.28          4.347e-01 1.398e+00   1.711e+00         7.438e-01
  16  5.55          4.576e-01 1.371e+00   1.913e+00         8.752e-01
```

The relative lower bound is stable and separated from zero in the tested windows.  Thus actual
coercivity can be proved by:

```text
MCOER: C_model >= a_H L I,
RCOER: C_actual >= theta_H C_model.
```

## 2. Status

```text
observed: min generalized eigenvalue is bounded below in the finite harness;
reduced: COER to MCOER + RCOER;
open:   prove MCOER and RCOER analytically.
```
