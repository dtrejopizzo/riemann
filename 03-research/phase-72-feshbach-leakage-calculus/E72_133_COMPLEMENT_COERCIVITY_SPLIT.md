# E72.133 -- Complement coercivity split

**Date:** 2026-07-09.
**Role:** test whether `COER` follows from archimedean complement dominance.

## 0. Coercivity needed

E72.132 reduces the scalar mass gain to:

```text
C_E >= c_H L I.                                             (COER)
```

Here `C_E` is the actual shorted complement:

```text
C_E=B_Q^*Q(H_actual-e_0)QB_Q.
```

Write:

```text
C_E=C_model+Delta_arith,
```

where `C_model` is the same complement for the archimedean/free background and `Delta_arith` is the
prime perturbation.

## 1. Weyl sufficient criterion

A direct sufficient theorem is:

```text
lambda_min(C_model) >= a_H L,
||Delta_arith|| <= b_H L,
a_H>b_H.                                                     (ADOM)
```

Then:

```text
lambda_min(C_E) >= (a_H-b_H)L.
```

This would prove `(COER)` without using zeros or Ω7 positivity.

## 2. Diagnostic

The companion script:

```text
E72_133_coercivity_split_probe.py
```

reports:

```text
lambda_min(C_actual)/L,
lambda_min(C_model)/L,
||Delta_arith||/L,
(lambda_min(C_model)-||Delta_arith||)/L.
```

Representative output:

```text
E72.133 complement coercivity split probe
 lam   L  minAct/L  minMod/L  ||Delta||/L  WeylLow/L  maxAct/L
   6  3.58 1.048e+00 7.296e-01   8.170e-01 -8.734e-02 2.179e+00
   8  4.16 1.292e+00 9.918e-01   1.241e+00 -2.491e-01 2.465e+00
  10  4.61 1.531e+00 1.221e+00   9.762e-01  2.447e-01 2.627e+00
  12  4.97 1.766e+00 1.514e+00   2.413e+00 -8.985e-01 2.909e+00
  14  5.28 1.997e+00 1.711e+00   2.612e+00 -9.009e-01 3.140e+00
  16  5.55 2.223e+00 1.913e+00   2.648e+00 -7.358e-01 3.374e+00
```

The crude operator-norm Weyl criterion is too strong: `||Delta_arith||` is large, although the actual
minimum eigenvalue is better than the model minimum in these windows.  The right analytic criterion is
a relative form bound, not absolute perturbation dominance.

## 3. Status

```text
rejected: crude Weyl dominance by ||Delta_arith||;
kept:     actual complement coercivity is strong;
next:     test the relative form bound C_E >= theta C_model.
```
