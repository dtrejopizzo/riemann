# E73.264 results - paired alignment audit

Command:

```text
python3 E73_264_paired_alignment_probe.py
```

## Output

```text
E73.264 paired arch-prime alignment probe
Tests whether UNIF-ETA is row alignment or only xi-paired cancellation.
 lam      L gamma row centerB archB primeB pairRel rowDiffRel rowCos etaArchRel etaPrimeRel
   8    4.159  14.13   0   -21.68   -1.52   -1.52  3.3e-13  1.152e-02  0.9999   1.00e+00    1.00e+00
   8    4.159  14.13   1   -21.46   -1.50   -1.50  4.4e-13  1.152e-02  0.9999   1.00e+00    1.00e+00
   8    4.159  21.02   0   -15.76   -2.18   -2.18  3.9e-09  2.609e-03  1.0000   1.00e+00    1.00e+00
   8    4.159  21.02   1   -15.79   -2.15   -2.15  3.6e-09  2.609e-03  1.0000   1.00e+00    1.00e+00
  10    4.605  14.13   0   -18.50   -0.14   -0.14  6.7e-13  2.922e-02  0.9996   1.00e+00    1.00e+00
  10    4.605  14.13   1   -18.51   -0.14   -0.14  6.6e-13  2.922e-02  0.9996   1.00e+00    1.00e+00
  10    4.605  21.02   0   -14.98   -0.42   -0.42  2.2e-10  9.988e-03  1.0000   1.00e+00    1.00e+00
  10    4.605  21.02   1   -14.98   -0.42   -0.42  2.2e-10  9.988e-03  1.0000   1.00e+00    1.00e+00
  12    4.970  14.13   0   -20.64   -1.32   -1.32  3.5e-14  4.979e-02  0.9988   1.00e+00    1.00e+00
  12    4.970  14.13   1   -20.34   -1.33   -1.33  5.7e-14  4.979e-02  0.9988   1.00e+00    1.00e+00
  12    4.970  21.02   0   -16.61   -2.09   -2.09  7.8e-11  1.624e-02  0.9999   1.00e+00    1.00e+00
  12    4.970  21.02   1   -16.84   -2.10   -2.10  5.4e-11  1.624e-02  0.9999   1.00e+00    1.00e+00
  16    5.545  14.13   0   -19.22   -4.02   -4.02  4.9e-12  1.265e-01  0.9920   1.00e+00    1.00e+00
  16    5.545  14.13   1   -19.90   -0.88   -0.88  7.1e-15  1.265e-01  0.9920   1.00e+00    1.00e+00
  16    5.545  21.02   0   -18.18   -1.91   -1.91  7.9e-13  1.869e-01  0.9825   1.00e+00    1.00e+00
  16    5.545  21.02   1   -19.05   -0.97   -0.97  3.6e-14  1.869e-01  0.9825   1.00e+00    1.00e+00
  20    5.991  14.13   0   -19.21   -1.52   -1.52  1.8e-14  3.138e-01  0.9496   1.00e+00    1.00e+00
  20    5.991  14.13   1   -18.38   -2.05   -2.05  2.0e-13  3.138e-01  0.9496   1.00e+00    1.00e+00
  20    5.991  21.02   0   -17.67   -0.74   -0.74  6.9e-14  6.054e-01  0.7962   1.00e+00    1.00e+00
  20    5.991  21.02   1   -17.76   -0.92   -0.92  8.0e-14  6.054e-01  0.7962   1.00e+00    1.00e+00
```

## Reading

The decisive contrast is:

```text
pairRel    = |(rho^A-rho^P)xi|/|rho^Axi|   tiny, often 1e-14--1e-10;
rowDiffRel = ||rho^A-rho^P||/max(||rho^A||,||rho^P||)
             not tiny, and reaches 0.605 in the tested range.
```

So the remaining cancellation is not row-level convergence:

```text
rho^A ~= rho^P
```

is false as a useful theorem target.

The correct theorem is paired:

```text
<rho^A-rho^P,xi_L>=O_M(L^-M),
```

where `xi_L` is the Gamma-prime eigenline.  This confirms that `EIG-COEFF`
cannot be replaced by a generic Schur-row estimate.

## Status

```text
rejected: row approximation rho^A ~= rho^P as closing mechanism;
confirmed: cancellation is eigenline-paired;
next: derive a transport relation for xi_L that forces this paired Schur
      cancellation.
```

