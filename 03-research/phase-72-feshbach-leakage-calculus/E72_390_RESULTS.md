# E72.390 results - parity tail gain

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_390_parity_tail_probe.py
```

## Output

```text
E72.390 parity tail probe
 lam    L     M    max|S1|       m      |Lc|        m|Lc|      m^2|Lc|
   8  4.159    12   1.681e-18     24   5.940e-11   1.426e-09   3.421e-08
   8  4.159    12   1.681e-18     36   2.371e-11   8.534e-10   3.072e-08
   8  4.159    12   1.681e-18     48   9.988e-12   4.794e-10   2.301e-08
  10  4.605    14   1.247e-18     28   2.086e-09   5.840e-08   1.635e-06
  10  4.605    14   1.247e-18     42   6.412e-11   2.693e-09   1.131e-07
  10  4.605    14   1.247e-18     56   2.733e-11   1.531e-09   8.571e-08
  12  4.970    16   1.182e-18     32   2.213e-10   7.083e-09   2.267e-07
  12  4.970    16   1.182e-18     48   2.160e-11   1.037e-09   4.977e-08
  12  4.970    16   1.182e-18     64   9.514e-12   6.089e-10   3.897e-08
  14  5.278    18   2.460e-18     36   3.100e-10   1.116e-08   4.018e-07
  14  5.278    18   2.460e-18     54   5.680e-11   3.067e-09   1.656e-07
  14  5.278    18   2.460e-18     72   2.655e-11   1.912e-09   1.376e-07
```

## Interpretation

The tested parity moment is

```text
S1(w)=sum_n xi_n d_n/(w^2+d_n^2).
```

It vanishes to machine precision (`10^-18`) for the actual pole-even vector.  This verifies the exact
parity cancellation used in E72.390.

The coefficient `Lc=Lcal(b_m)` does not show harmonic behavior: `m|Lc|` decreases as `m` grows.  This
is the numerical signature that the apparent `1/m` term is absent and the tail begins at the next
order.

## Status

```text
verified: leading tail moment S1(w) vanishes by pole-even parity;
verified: Lcal(b_m) has no visible m^-1 profile in the tested windows;
remaining: control the next coefficient spectrally, not by absolute zero sums.
```

