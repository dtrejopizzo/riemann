# E73.002 results - rational Cauchy projection

## Command

```text
python3 03-research/phase-73-cauchy-projection/E73_002_rational_projection_probe.py
```

## Output

```text
E73.002 rational Cauchy projection probe
 lam     L    nO nK    |mat|       |rat|       absErr     relErr
   8   4.159    3  5  4.004e-09  4.004e-09  1.735e-24  4.334e-16
  10   4.605    3  5  3.724e-09  3.724e-09  1.268e-24  3.404e-16
  12   4.970    3  5  4.735e-11  4.735e-11  1.740e-25  3.675e-15
  14   5.278    3  5  2.480e-09  2.480e-09  4.642e-25  1.871e-16
```

## Interpretation

The matrix projection

```text
C_OO^(-1)C_OKG_K
```

matches the rational residue formula of E73.002 to roundoff.  This validates the replacement of the
Cauchy inverse by the explicit rational interpolation formula.

## Status

```text
verified: rational projection formula equals matrix projection;
next: compose Pi(b,k) with the critical divided-difference formula for G_K(k).
```

