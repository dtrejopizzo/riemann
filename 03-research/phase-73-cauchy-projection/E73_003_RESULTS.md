# E73.003 results - critical divided-difference source

## Command

```text
python3 03-research/phase-73-cauchy-projection/E73_003_critical_source_probe.py
```

## Output

```text
E73.003 critical source probe
 lam     L    nO nK    |rat|       |src|       absErr     expWeighted
   8   4.159    3  5  4.004e-09  4.004e-09  1.382e-16    9.194e-09
  10   4.605    3  5  3.724e-09  3.724e-09  9.700e-17    9.349e-09
  12   4.970    3  5  4.735e-11  4.735e-11  2.133e-16    1.276e-10
  14   5.278    3  5  2.480e-09  2.480e-09  1.763e-15    7.123e-09
```

## Interpretation

The probe compares:

```text
rat = C_OO^(-1)C_OKG_K,
src = sum_m xi_m S_b(d_m),
```

where `S_b` is the composed rational-projection/divided-difference kernel of E73.003.

The norms match.  The absolute error is the expected floating cancellation cost from evaluating the
critical divided differences and rational interpolation kernel separately.

## Status

```text
verified: NAT-PROJ equals NAT-SRC in the tested finite windows;
current endpoint: prove exponential smallness of sum_m xi_m S_b(d_m) from the pole-even CCM equation.
```

