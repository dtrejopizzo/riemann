# E73.266 results - rank-two transport collapse

Command:

```text
python3 E73_266_rank_two_transport_collapse.py
```

## Output

```text
E73.266 rank-two transport collapse audit
Checks qHRxi = (mu e_a - qHQ*G) h, h=Qxi.
 lam      L gamma row centerB r2B errB hB muB BHopB archR2B primeR2B archErrB primeErrB
   8    4.159  14.13   0   -21.68  -21.68  -27.79  -19.03  -24.84   -0.73    -1.52     -1.52    -26.75     -27.23
   8    4.159  14.13   1   -21.46  -21.46  -29.21  -19.03  -24.84   -0.73    -1.50     -1.50    -27.23     -26.75
   8    4.159  21.02   0   -15.76  -15.76  -29.32  -13.24  -24.84   -0.73    -2.18     -2.18    -27.23     -27.72
   8    4.159  21.02   1   -15.79  -15.79  -28.89  -13.24  -24.84   -0.73    -2.15     -2.15   -484.67     -27.23
  10    4.605  14.13   0   -18.50  -18.50  -25.04  -17.91  -21.82   -0.36    -0.14     -0.14    -23.60     -24.06
  10    4.605  14.13   1   -18.51  -18.51  -25.09  -17.91  -21.82   -0.36    -0.14     -0.14    -23.00     -23.00
  10    4.605  21.02   0   -14.98  -14.98  -25.44  -14.40  -21.82   -0.35    -0.42     -0.42   -452.32     -24.06
  10    4.605  21.02   1   -14.98  -14.98  -25.16  -14.40  -21.82   -0.35    -0.42     -0.42    -23.60    -452.32
  12    4.970  14.13   0   -20.64  -20.64  -25.28  -19.10  -20.55   -0.48    -1.32     -1.32    -23.21     -22.91
  12    4.970  14.13   1   -20.34  -20.35  -24.13  -19.10  -20.55   -0.48    -1.33     -1.33   -430.82    -430.82
  12    4.970  21.02   0   -16.61  -16.61  -24.75  -15.28  -20.55   -0.43    -2.09     -2.09    -23.78     -24.64
  12    4.970  21.02   1   -16.84  -16.84  -28.10  -15.28  -20.55   -0.43    -2.10     -2.10    -23.78     -23.96
  16    5.545  14.13   0   -19.32  -19.10  -19.78  -20.04  -18.67    1.00    -4.02     -4.02    -21.70     -21.93
  16    5.545  14.13   1   -19.96  -19.57  -19.99  -20.04  -18.67    1.00    -0.88     -0.88    -21.61     -21.61
  16    5.545  21.02   0   -18.18  -18.17  -20.60  -19.12  -18.67    0.98    -1.91     -1.91    -22.42     -21.01
  16    5.545  21.02   1   -19.03  -19.07  -20.65  -19.12  -18.67    0.98    -0.97     -0.97    -21.45    -403.27
  20    5.991  14.13   0   -18.89  -20.23  -18.94  -19.29  -17.46    1.00    -1.52     -1.52    -21.68     -19.58
  20    5.991  14.13   1   -18.33  -18.29  -19.81  -19.29  -17.46    1.00    -2.05     -2.05    -21.02     -20.33
  20    5.991  21.02   0   -17.68  -17.67  -19.89  -18.50  -17.46    1.01    -0.74     -0.74    -20.29     -20.29
  20    5.991  21.02   1   -17.79  -17.72  -18.85  -18.50  -17.46    1.01    -0.92     -0.92    -20.91     -19.82
```

## Reading

In the stable windows the rank-two expression

```text
qH_LRxi_L=(mu_L e_a-qH_LQ^*(QQ^*)^(-1))Qxi_L
```

matches the center.  At larger `lambda` the direct double comparison loses
digits because both sides are obtained by subtracting ordinary-sized
archimedean/prime/Cauchy-plane terms; this is the same conditioning issue
already recorded for row determinants in E73.260.

The mathematical conclusion is independent of that numerical conditioning:
the identity is exact, but it is not an admissible proof source.  It expresses
the target through

```text
h=Qxi_L,
```

which is exactly the Cauchy divisor data whose smallness the scalar WRL route
is trying to prove.

## Consequence

The rank-two expansion is a detector only:

```text
qH_LRxi_L=(mu_LI-B(w))Qxi_L.
```

It collapses to E73.240 and should not be used as the non-circular proof of
`UNIF-ETA`.

The surviving target remains E73.265:

```text
q_a[H_L^A,R_w]xi_L-q_a[H_L^P,R_w]xi_L=O_M(L^-M),
```

proved directly from the explicit Gamma-prime commutator transport, not by
assuming control of `Q_wxi_L`.

## Status

```text
validated: rank-two expansion is exact where numerically stable;
rejected: rank-two expansion as non-circular proof mechanism;
kept: commutator transport matching theorem.
```

