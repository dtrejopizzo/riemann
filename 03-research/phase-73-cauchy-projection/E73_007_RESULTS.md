# E73.007 results - structured primitive probe

## Command

```text
python3 03-research/phase-73-cauchy-projection/E73_007_structured_primitive_probe.py
```

## Output

```text
E73.007 structured primitive probe
 lam     L   dim  pwr  basis  relDef    eigDef     expEig    |Y|      |DY|
   8   4.159    25    1     15 1.42e-07  1.18e-10  2.71e-10 5.90e+01 9.07e+02
   8   4.159    25    2     30 2.51e-08  1.20e-10  2.75e-10 6.10e+02 8.76e+03
   8   4.159    25    3     45 2.51e-08  1.19e-10  2.73e-10 6.10e+02 8.76e+03
  10   4.605    29    1     15 5.63e-07  1.16e-10  2.90e-10 5.58e+01 8.22e+02
  10   4.605    29    2     30 1.22e-08  1.08e-10  2.71e-10 1.87e+03 2.54e+04
  10   4.605    29    3     45 1.22e-08  1.20e-10  3.02e-10 1.84e+03 2.49e+04
  12   4.970    33    1     15 7.40e-07  3.18e-12  8.59e-12 3.48e+01 5.42e+02
  12   4.970    33    2     30 4.30e-08  2.01e-11  5.44e-11 3.76e+03 5.14e+04
  12   4.970    33    3     45 4.30e-08  4.95e-11  1.34e-10 3.70e+03 5.04e+04
  14   5.278    37    1     15 1.15e-06  9.05e-11  2.60e-10 1.98e+01 3.30e+02
  14   5.278    37    2     30 5.71e-09  8.18e-11  2.35e-10 2.37e+03 3.60e+04
  14   5.278    37    3     45 5.72e-09  8.73e-11  2.51e-10 2.37e+03 3.61e+04
```

## Interpretation

The structured `RAT-DD` image captures almost all of the source:

```text
pwr=1: relDef about 10^-7 to 10^-6;
pwr=2: relDef about 10^-8 to 10^-9.
```

The eigenline defect remains the target quantity, as it must:

```text
eigDef = |<xi,S_b>|.
```

The primitive norms grow substantially for `pwr=2`, so the analytic proof must not rely on an
uncontrolled inverse.  Still, the result supports the key structural claim:

```text
S_b lies very close to the image of C_E-mu on a small rational/divided-difference class.
```

## Status

```text
observed: structured primitive class captures the non-eigenline source to high precision;
not closed: eigenline defect is still NAT-SRC;
next: derive the image identity symbolically, replacing least squares by an explicit primitive.
```

