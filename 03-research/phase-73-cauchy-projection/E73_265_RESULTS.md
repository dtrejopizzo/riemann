# E73.265 results - commutator transport probe

Command:

```text
python3 E73_265_commutator_transport_probe.py
```

## Output

```text
E73.265 commutator transport probe
Compares right-projected Schur pairing q H R xi with left-projected eigenline pairing q R H xi.
 lam      L gamma row centerB rightAB rightPB leftAB leftPB leftMatchB commAB commPB commMatchB
   8    4.159  14.13   0   -21.68    -1.52    -1.52  -27.63  -27.63     -53.01   -1.52   -1.52    -484.67
   8    4.159  14.13   1   -21.46    -1.50    -1.50  -28.32  -28.32     -52.73   -1.50   -1.50    -484.67
   8    4.159  21.02   0   -15.76    -2.18    -2.18  -26.79  -26.79     -52.52   -2.18   -2.18    -484.67
   8    4.159  21.02   1   -15.79    -2.15    -2.15  -26.75  -26.75     -52.04   -2.15   -2.15    -484.67
  10    4.605  14.13   0   -18.50    -0.14    -0.14  -24.47  -24.47     -48.11   -0.14   -0.14    -452.32
  10    4.605  14.13   1   -18.51    -0.14    -0.14  -24.10  -24.10    -452.32   -0.14   -0.14    -452.32
  10    4.605  21.02   0   -14.98    -0.42    -0.42  -24.34  -24.34     -47.66   -0.42   -0.42    -452.32
  10    4.605  21.02   1   -14.98    -0.42    -0.42  -24.09  -24.09     -47.66   -0.42   -0.42    -452.32
  12    4.970  14.13   0   -20.64    -1.32    -1.32  -27.33  -27.33     -46.23   -1.32   -1.32    -430.82
  12    4.970  14.13   1   -20.34    -1.33    -1.33  -24.31  -24.31     -45.09   -1.33   -1.33    -430.82
  12    4.970  21.02   0   -16.61    -2.09    -2.09  -24.40  -24.40     -45.39   -2.09   -2.09    -430.82
  12    4.970  21.02   1   -16.84    -2.10    -2.10  -25.91  -25.91     -45.68   -2.10   -2.10    -430.82
  16    5.545  14.13   0   -19.22    -4.02    -4.02  -21.58  -21.58     -40.13   -4.02   -4.02    -403.27
  16    5.545  14.13   1   -19.90    -0.88    -0.88  -22.00  -22.00     -41.40   -0.88   -0.88    -403.27
  16    5.545  21.02   0   -18.18    -1.91    -1.91  -22.75  -22.75     -41.95   -1.91   -1.91    -403.27
  16    5.545  21.02   1   -19.05    -0.97    -0.97  -22.28  -22.28     -42.12   -0.97   -0.97    -403.27
  20    5.991  14.13   0   -19.21    -1.52    -1.52  -22.12  -22.12     -39.70   -1.52   -1.52    -385.84
  20    5.991  14.13   1   -18.38    -2.05    -2.05  -20.72  -20.72     -37.98   -2.05   -2.05    -385.84
  20    5.991  21.02   0   -17.67    -0.74    -0.74  -20.85  -20.85     -40.14   -0.74   -0.74    -385.84
  20    5.991  21.02   1   -17.76    -0.92    -0.92  -21.22  -21.22     -39.00   -0.92   -0.92    -385.84
```

## Reading

The left-projected arch/prime matching is already exact:

```text
qR H_L^A xi_L - qR H_L^P xi_L = qR H_L xi_L = mu_L qR xi_L = 0.
```

This is visible in `leftMatchB`, which is at numerical zero.

But the right-projected terms `qH_L^X Rxi_L` are ordinary size.  The center is
therefore not the left matching itself; it is the difference between the two
transport defects:

```text
T_X=qH_L^X Rxi_L-qR H_L^X xi_L=q[H_L^X,R]xi_L.
```

Thus:

```text
center = T_A-T_P.
```

The remaining theorem is:

```text
T_A-T_P=O_M(L^-M).
```

## Status

```text
validated: left-projected matching follows exactly from the eigenline equation;
validated: UNIF-ETA is the arch-prime matching of commutator transport defects;
open: prove the commutator transport matching theorem analytically.
```

