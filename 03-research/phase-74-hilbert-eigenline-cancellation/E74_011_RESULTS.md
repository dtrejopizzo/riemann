# E74.11 results - algebraic quotient bridge

Command:

```text
python3 E74_011_algebraic_quotient_bridge_probe.py
```

## Summary

The direct bridge requested by E73.277 does not close:

```text
APR rho modulo left-coborders is not represented by rho's raw cauchy0
coefficients.
```

Representative trusted rows:

```text
 lam      L gamma row fitRel imageRel resB cauchyRel bridgeRel quotMiss
   8  4.159 14.13   0 4.9e-06 4.0e-06 -1.37 2.00e-01 8.00e-01 7.44e-03
   8  4.159 21.02   0 7.7e-06 4.0e-06  1.55 2.12e-03 9.98e-01 8.15e-03
  10  4.605 14.13   0 4.6e-07 1.9e-07  0.30 3.60e-02 9.65e-01 1.74e-01
  12  4.970 14.13   1 1.8e-06 1.8e-06  0.07 8.96e-02 9.11e-01 3.14e-02
  16  5.545 21.02   0 8.9e-05 1.8e-04  0.15 2.44e-03 1.00e+00 1.79e-01
```

## Reading

The large `bridgeRel` means the raw cauchy0 coefficients of the APR row do not
explain the APR principal residual modulo the generated image `M_L`.

The smaller `quotMiss` means the residual still lives close to the abstract
quotient span `(C_L+M_L)/M_L` in the better-conditioned windows.

## Verdict

```text
rejected: direct raw-cauchy0 bridge;
survives: quotient-lift bridge;
next:     construct an explicit partial-fraction basis for C_L cap M_L and
          define the quotient-lift residual without numerical projectors.
```

