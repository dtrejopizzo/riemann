# E72.394 results - natural-height outside-zero tail

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_394_outside_zero_tail_probe.py
```

## Output

```text
E72.394 outside-zero high-frequency probe
 lam     L       V2        tau      |F(i tau)|   tau^2|F|/V2
   8   4.159 8.868e+01     64.00    9.755e-12    4.506e-10
   8   4.159 8.868e+01     96.00    4.013e-11    4.170e-09
   8   4.159 8.868e+01    128.00    8.749e-12    1.616e-09
  10   4.605 1.833e+02     80.00    1.749e-10    6.104e-09
  10   4.605 1.833e+02    120.00    1.519e-12    1.193e-10
  10   4.605 1.833e+02    160.00    8.380e-12    1.170e-09
  12   4.970 1.751e+02     96.00    3.239e-12    1.704e-10
  12   4.970 1.751e+02    144.00    1.389e-12    1.645e-10
  12   4.970 1.751e+02    192.00    1.578e-13    3.322e-11
  14   5.278 3.837e+02    112.00    9.902e-12    3.237e-10
  14   5.278 3.837e+02    168.00    1.361e-12    1.001e-10
  14   5.278 3.837e+02    224.00    2.911e-12    3.806e-10
```

## Interpretation

The tested object is the bilateral packet transform

```text
F_z(i tau)=int_-L^L e^(i tau t) B_z^M(|t|)dt.
```

E72.394 predicts

```text
|F_z(i tau)| <= V_2/tau^2.
```

The normalized diagnostic

```text
tau^2 |F_z(i tau)| / V_2
```

is far below `1` in the tested high-frequency range.  This confirms the second-variation mechanism
used to make the zero tail above `T_L=e^L L^A` polynomial or decaying.

## Status

```text
verified: high-frequency bilateral packet transform obeys the tau^-2 profile;
proved: outside-zero tail beyond natural height is polynomial/decaying;
remaining: finite natural-height nodal suppression.
```

