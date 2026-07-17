# E73.246 results - quotient coordinate audit

Command:

```text
python3 E73_246_quotient_coordinate_audit.py
```

## 1. Summary table

```text
E73.246 quotient coordinate audit
Stack defects delta_a for two critical gammas and two Cauchy rows.
Coordinate form: delta_a xi = theta_a dot z_Q.
 lam      L pow MDranks qRank s1B sLastB pairMaxB pairNormB zQMaxB zQNormB coeffMaxB coordErrB
   8    4.159   0    [5, 5]     4  -8.17  -14.93   -15.76    -15.53   -4.30    -4.30     -8.25    -34.42
   8    4.159   1    [5, 5]     4  -8.17  -14.93   -15.76    -15.53   -4.30    -4.30     -8.25    -35.19
   8    4.159   2    [5, 5]     4  -8.17  -14.93   -15.75    -15.53   -4.30    -4.23     -8.25    -34.81
  10    4.605   0    [5, 5]     4  -6.50  -12.42   -14.98    -14.75   -4.39    -4.39     -6.63    -31.80
  10    4.605   1    [5, 5]     4  -6.50  -12.42   -14.98    -14.75   -4.40    -4.40     -6.63    -31.20
  10    4.605   2    [5, 5]     4  -6.50  -12.42   -14.98    -14.75   -4.40    -4.40     -6.63    -31.21
  12    4.970   0    [5, 5]     4  -5.43  -10.98   -16.61    -16.49   -8.07    -8.01     -5.61    -30.53
  12    4.970   1    [5, 5]     4  -5.43  -11.01   -16.64    -16.49   -7.07    -7.06     -5.61    -29.25
  12    4.970   2    [5, 5]     4  -5.43  -11.01   -16.61    -16.49   -8.08    -8.06     -5.61    -29.06
  16    5.545   0    [6, 6]     4  -2.78   -6.58   -18.20    -18.18  -12.39   -12.39     -3.10    -25.35
  16    5.545   1    [8, 7]     4  -3.82   -7.34   -15.26    -15.19   -8.64    -8.64     -4.01    -26.59
  16    5.545   2    [8, 8]     4  -5.03   -9.34   -17.03    -16.89   -8.98    -8.88     -5.23    -27.48
```

## 2. Pointwise pairings for the canonical quotient

```text
Per-coordinate pairings for canonical pow=0:
 lam      L qRank label        pairB
   8    4.159     4 g0: 14.1:r0     -21.68
   8    4.159     4 g0: 14.1:r1     -21.46
   8    4.159     4 g1: 21.0:r0     -15.76
   8    4.159     4 g1: 21.0:r1     -15.79
  10    4.605     4 g0: 14.1:r0     -18.50
  10    4.605     4 g0: 14.1:r1     -18.51
  10    4.605     4 g1: 21.0:r0     -14.98
  10    4.605     4 g1: 21.0:r1     -14.98
  12    4.970     4 g0: 14.1:r0     -20.62
  12    4.970     4 g0: 14.1:r1     -20.36
  12    4.970     4 g1: 21.0:r0     -16.61
  12    4.970     4 g1: 21.0:r1     -16.84
  16    5.545     4 g0: 14.1:r0     -19.30
  16    5.545     4 g0: 14.1:r1     -19.81
  16    5.545     4 g1: 21.0:r0     -18.20
  16    5.545     4 g1: 21.0:r1     -19.15
```

## 3. Interpretation

For `lambda=8,10,12`, the generated DD-local image has stable rank:

```text
rank(M_DD)=5
```

for both tested critical nodes and all rational orders `0,1,2`.

After quotienting, the defect packet for two nodes and two Cauchy rows has rank:

```text
rank Row(D_Q)=4.
```

The coordinate reconstruction error is far below the scalar obstruction:

```text
coordErrB <= -29
```

in the trusted windows.  Thus the quotient obstruction is faithfully represented
by the finite coordinate identity:

```text
delta_a xi_L = theta_a · z_Q.
```

For `lambda=16`, the DD-local generated rank is conditioning-sensitive, as in
E73.245.  The quotient rank remains `4`, but these rows are diagnostic until
symbolic or interval rank certification is available.

## 4. Status

```text
proved algebraically: CURV-QUOT-DIV reduces to QUOT-COORD-DIV once a quotient
                    basis is fixed;
observed:           stable quotient rank 4 for the two-node packet;
open:               symbolic coordinates theta_a,z_Q and proof of their
                    super-polynomial orthogonality.
```
