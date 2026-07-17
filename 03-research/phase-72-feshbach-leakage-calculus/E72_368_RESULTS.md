# E72.368 results - residual norm master energy

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_368_master_energy_probe.py
```

The probe checks:

```text
E_CFIR
= ||Lambda k-(KWin k-tail)||^2
= projective energy + scalar energy.
```

It uses `mu` as scalar proxy.  The theorem uses the exact

```text
Lambda_L=mu+e_pole-2kappa_*.
```

## Table

```text
lam   N roots node      fullE        projE       scalarE      splitErr
 6.0  10     2 root          nan         nan         nan         nan
 6.0  10     2 shift  1.2257e+01  2.1909e-01  1.2038e+01  0.0000e+00

 8.0  12     3 root   1.8844e-22  3.4239e-24  1.8502e-22  2.3510e-38
 8.0  12     3 shift  5.3475e+02  2.2840e+01  5.1191e+02  4.5475e-13

10.0  14     3 root   1.7969e-22  2.4889e-24  1.7720e-22  4.7020e-38
10.0  14     3 shift  5.6518e+02  3.2722e+01  5.3246e+02  2.2737e-13

12.0  16     3 root   7.7318e-27  1.1152e-28  7.6202e-27  2.8699e-42
12.0  16     3 shift  4.3922e+02  8.2154e+01  3.5707e+02  0.0000e+00
```

## Reading

The split error is roundoff:

```text
splitErr ~= 0 to 1e-13.
```

Thus the master energy certificate is exactly the sum of:

```text
PCFIR energy + SCALAR-CONS energy.
```

In shifted controls, scalar energy is the dominant part.  So the scalar gate is not optional.

## Consequence

The next analytic target should be the single positive finite statement:

```text
ENERGY-CFIR:
|| (Lambda_L I-KWin)J_TG_x + J_TTail_T^M ||^2
<= C_T L^{2B}.
```

It keeps both projective and scalar requirements and forbids after-the-fact scalar fitting.
