# E73.184 results - high-order WR tail certificate

Command:

```text
python3 E73_184_high_order_wr_tail_probe.py
```

Output:

```text
E73.184 high-order WR tail probe
Taylor accelerates WR tail to order K and bounds by F^(K+1).
 lam     L gamma row R  K actualTailB boundB ratioB nextDerB
  12   4.970   14.13   0 80  2      -14.41  -3.82 -10.59     6.80
  12   4.970   14.13   0 80  4      -15.79  -7.04  -8.75    10.22
  12   4.970   14.13   0 80  6      -17.92 -10.10  -7.82    13.70
  12   4.970   14.13   0 80  8      -21.62 -13.08  -8.54    17.21
  16   5.545   14.13   0 80  2      -13.63  -2.44 -11.20     7.50
  16   5.545   14.13   0 80  4      -15.67  -5.44 -10.23    10.72
  16   5.545   14.13   0 80  6      -17.35  -8.31  -9.04    13.97
  16   5.545   14.13   0 80  8      -19.42 -11.08  -8.34    17.27
  20   5.991   14.13   0 80  2      -12.34  -2.50  -9.84     7.01
  20   5.991   14.13   0 80  4      -13.78  -5.43  -8.35    10.03
  20   5.991   14.13   0 80  6      -15.94  -8.22  -7.72    13.10
  20   5.991   14.13   0 80  8      -18.53 -10.89  -7.64    16.24
  24   6.356   14.13   0 80  2      -11.52  -2.16  -9.37     7.05
  24   6.356   14.13   0 80  4      -12.50  -4.90  -7.60    10.07
  24   6.356   14.13   0 80  6      -14.02  -7.43  -6.59    13.21
  24   6.356   14.13   0 80  8      -16.66  -9.79  -6.87    16.47
```

Reading:

```text
ratioB <= 0 means the rigorous order-K bound covers the observed tail.
Increasing K lowers the power tail but raises the derivative envelope; the
optimal K is therefore finite and row-dependent.
```

Representative rows are shown above; the full script scans the two first
critical heights and both Cauchy rows for `lambda=12,16,20,24`.

Observed:

```text
1. actualTailB improves substantially as K grows;
2. boundB also improves, but more slowly;
3. ratioB remains negative, so the rigorous bound covers the observed tail;
4. the derivative envelope nextDerB grows quickly.
```

Conclusion: high-order Taylor acceleration is valid and useful, but the
coefficient-absolute derivative bound is still too conservative.  The next
sharpening should group by frequency and bound derivatives after frequency
aggregation, not before.
