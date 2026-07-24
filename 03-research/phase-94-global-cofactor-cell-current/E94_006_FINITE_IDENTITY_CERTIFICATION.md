# E94.006 - Finite identity certification

## 1. Reconstructed section

A multiprecision CCM section was rebuilt from the Gamma integral and the
finite prime-power sum with

```text
lambda=6,
outer modes=7,
working precision=70 decimal digits.                 (1.1)
```

The inner block, raw right boundary column, mesh diagonal and symbol vector
were reconstructed independently from the entry formula.

## 2. Residuals

The relative residuals were

```text
M A+(2/L)[C s+(S-Delta S_b)1]
  6.91e-97,

Delta A+(2/L)[C U+(S-Delta S_b)V]
  2.35e-206,

P(z)-Delta N(z),  z=0.4+1.2i
  6.21e-207.                                         (2.1)
```

The first residual is limited by the independently integrated CCM entries.
The latter two are algebraic consequences evaluated at much smaller relative
scale.

## 3. Conclusion

The certification confirms the sign in the displacement commutator, the
boundary convention `q=D1-d_b1`, and the polynomial numerator formula.  It is
not evidence for the cofinal Gamma--Euler limit; it validates only the finite
identities proved in E94.001--E94.003.

