# E97.006 - Finite trace certification

## 1. Independent matrix audit

The trace and adjugate identities were evaluated on independent complex
matrices of dimension seven at seventy-decimal precision.  The Euler unit was
chosen invertible and nonnormal, the position operator diagonal, and the test
sensitivity fully noncommuting.

## 2. Residuals

```text
Tr(KA)-Tr([Z,K]Z^(-1)X)
  1.81e-71,

Tr(KA^*)-Tr((Z^*)^(-1)[K,Z^*]X)
  0,

B[Z,adj(B)]B+det(B)[Z,B]
  relative residual 3.05e-71.                        (2.1)
```

## 3. Scope

The audit confirms the order and signs of all noncommuting factors in
E97.002 and E97.004.  It does not test the asymptotic safe boundary pairing.

