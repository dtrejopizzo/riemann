# E73.192 results - ramp-normalized packet

Command:

```text
python3 E73_192_ramp_normalized_packet_probe.py
```

Output:

```text
E73.192 ramp-normalized packet
Splits B=Bp0*r0+Brem and measures ramp vs double-zero remainder.
 lam     L gamma row totalB rampB remB checkB rem0B remp0B remLB
  12   4.970   14.13   0  -20.85 -12.23 -12.23  -35.70 -22.98  -20.46 -21.48
  12   4.970   14.13   1  -21.09 -12.23 -12.23  -35.95 -24.09  -20.46 -22.05
  12   4.970   21.02   0  -20.40 -12.41 -12.41  -37.04 -23.77  -20.64 -22.91
  12   4.970   21.02   1  -19.87 -12.41 -12.41  -36.71 -24.43  -20.64 -23.19
  16   5.545   14.13   0  -19.19 -11.68 -11.68  -33.88 -21.11  -19.19 -19.72
  16   5.545   14.13   1  -19.98 -11.68 -11.68  -34.45 -21.68  -19.19 -20.08
  16   5.545   21.02   0  -18.18 -11.45 -11.45  -33.26 -21.47  -18.96 -20.75
  16   5.545   21.02   1  -19.03 -11.45 -11.45  -33.39 -22.27  -18.96 -20.37
  20   5.991   14.13   0  -19.09 -12.95 -12.95  -35.10 -19.96  -20.20 -19.76
  20   5.991   14.13   1  -18.56 -12.64 -12.64  -33.50 -19.91  -19.89 -19.27
  20   5.991   21.02   0  -17.65 -11.29 -11.29  -33.17 -21.48  -18.54 -18.91
  20   5.991   21.02   1  -17.76 -11.29 -11.29  -32.45 -23.10  -18.54 -19.50
```

Reading:

```text
The simple ramp split is algebraically correct.
The remainder has zero value at 0 and L, and its derivative is reduced to
floating/finite-difference scale.
But ramp and remainder contributions are both much larger than the final
signed residual and cancel each other.
```

Conclusion:

```text
The naive ramp r_0(y)=y(1-y/L) is not proof-facing.
It creates an artificial cancellation:

ramp contribution ~ remainder contribution >> total residual.
```

The correct normalization should choose a ramp `r_*` with

```text
r_*(0)=0,      r_*'(0)=1,      r_*(L)=0,
A_L[r_*]-P_L[r_*]=0.
```

Then the endpoint derivative is removed without adding a separate matching
term.  The next target is a balanced ramp.
