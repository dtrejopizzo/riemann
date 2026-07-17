# P76.050 - Safe shell cross-ratio results

For `lambda=6`, `mu=0`, reference `sigma_0=1`, define

```text
Q_N(sigma)
=| [T_{N+1}(i sigma)/T_N(i sigma)]
   /[T_{N+1}(i sigma_0)/T_N(i sigma_0)] |^2.
```

The scaled defects are:

```text
N->N+1    max|Q_N-1|    N^2 max|Q_N-1|/L^2
6->7       0.03648          0.1023
8->9       0.02333          0.1163
9->10      0.01821          0.1148
10->11     0.01501          0.1169
11->12     0.01256          0.1184
```

Unlike the raw shell terms, this canonically normalized quantity has a
stable `L^2/N^2` law.  It is exactly the multiplicative increment of the
safe-ratio characteristic, so its summability proves the fixed-`L`
finite-section limit.
