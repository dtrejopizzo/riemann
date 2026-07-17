# E73.233 results - canonical commutator defect identity

Command:

```text
python3 E73_233_commutator_defect_probe.py
```

## 1. Output

```text
E73.233 canonical commutator defect identity
Checks C=qH(I-P)xi = <D,xi>, D=[I-P,H]q*+mu(I-P)q*.
 lam      L gamma row centerB pairB errB ||D||B ||comm||B ||muterm||B
   8    4.159  14.13   0   -21.68  -21.68  -28.65   -3.18     -3.18     -51.01
   8    4.159  14.13   1   -21.46  -21.46  -28.97   -3.18     -3.18     -50.93
   8    4.159  21.02   0   -15.76  -15.76  -29.27   -4.54     -4.54     -51.04
   8    4.159  21.02   1   -15.79  -15.79  -30.04   -4.54     -4.54     -51.10
  10    4.605  14.13   0   -18.50  -18.50  -25.38   -2.13     -2.13     -46.06
  10    4.605  14.13   1   -18.51  -18.51  -25.80   -2.13     -2.13     -46.30
  10    4.605  21.02   0   -14.98  -14.98  -26.88   -3.16     -3.16     -45.93
  10    4.605  21.02   1   -14.98  -14.98  -27.81   -3.16     -3.16     -45.70
  12    4.970  14.13   0   -20.64  -20.64  -24.69   -1.47     -1.47     -43.68
  12    4.970  14.13   1   -20.34  -20.34  -25.76   -1.47     -1.47     -43.67
  12    4.970  21.02   0   -16.61  -16.61  -25.61   -2.56     -2.56     -43.76
  12    4.970  21.02   1   -16.84  -16.84  -26.29   -2.56     -2.56     -43.97
```

Here `centerB` means `log_L |C_q|`, `pairB` means
`log_L |<D_q,xi>|`, and `errB` is the identity error exponent.

## 2. Interpretation

The exact identity is numerically certified:

```text
qH(I-P)xi = <[I-P,H]q* + mu(I-P)q*, xi>
```

to roughly `L^-24`--`L^-30` in the tested windows.

The easy norm theorem is false in these coordinates.  The defect norm is only
around:

```text
||D_q|| = L^-1.47 ... L^-4.54,
```

while the center is:

```text
|C_q| = L^-14.98 ... L^-21.68.
```

Thus U4 cannot be proved by the strong estimate:

```text
||[I-P,H]q*|| + |mu| ||(I-P)q*|| rapidly small.
```

The smallness is a paired cancellation:

```text
<D_q,xi_L> rapidly small
```

inside a defect vector that is much larger in norm.

The `mu` term is negligible in the tested windows (`L^-43` or smaller), so the
dominant object is the paired commutator:

```text
<[I-P_w,H_L]q_a^*,xi_L>.
```

## 3. Consequence for the proof route

E73.233 is progress because it removes one false theorem before we invest in
it:

```text
not enough: norm-small Cauchy commutator;
correct:    paired commutator cancellation against the CCM ground vector.
```

The next analytic target is therefore:

```text
PCC-U4:
|<[I-P_w,H_L]q_a^*,xi_L>| <= A_M L^-M
```

proved from the explicit Gamma/prime cell formula and the finite eigenline
equation, without using `Q_w xi_L` small.

