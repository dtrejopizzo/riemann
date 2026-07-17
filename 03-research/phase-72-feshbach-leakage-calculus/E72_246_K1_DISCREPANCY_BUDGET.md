# E72.246 - K1 discrepancy budget

## Purpose

E72.245 shows that `K1` has positive high-window average. This note measures how much discrepancy the
prime-power measure uses when sampling `K1`.

Let:

```text
contAvg  = average_{u in (0.6,1)} K1(u),
primeAvg = (sum beta_n K1(u_n))/(sum beta_n),
disc     = primeAvg-contAvg.
```

The total-variation budget is:

```text
TV(K1)=sum_grid |Delta K1|.
```

## Diagnostic

Script:

```text
E72_246_k1_discrepancy_budget_probe.py
```

Output:

```text
E72.246 K1 discrepancy budget probe
TV is total variation on grid; disc=primeAvg-contAvg.
lam contAvg primeAvg disc relDisc TV disc/TV margin/TV supSlope
 12 +1.139410e-02 +1.366502e-02 +2.270925e-03 +0.199 2.726376e-01 0.008 0.050 1.802694e+00
 16 +8.798376e-03 +8.900117e-03 +1.017411e-04 +0.012 6.203957e-02 0.002 0.143 7.315794e-01
 20 +8.334867e-03 +7.504729e-03 -8.301377e-04 -0.100 5.336304e-02 0.016 0.141 5.684401e-01
 24 +6.859984e-03 +6.933629e-03 +7.364443e-05 +0.011 4.795390e-02 0.002 0.145 4.218481e-01
 28 +5.111877e-03 +5.271645e-03 +1.597677e-04 +0.031 1.517207e-01 0.001 0.035 1.268660e+00
 32 +3.210690e-03 +2.400028e-03 -8.106615e-04 -0.252 2.808378e-01 0.003 0.009 2.405439e+00
 36 +4.216730e-03 +4.388385e-03 +1.716545e-04 +0.041 1.831238e-02 0.009 0.240 9.831670e-02
```

## Reading

The actual prime-power discrepancy is small compared with total variation:

```text
|disc|/TV <= 0.016
```

in the tested windows.

However, the total-variation margin is tight at `lambda=32`:

```text
primeAvg/TV ~= 0.009.
```

Thus a crude Koksma-style estimate can support the stable windows, but `lambda=32` should remain in
the finite exceptional set together with the sharp HOC3 certificate.

At `lambda=36`, the kernel becomes smooth and the TV margin is large:

```text
primeAvg/TV ~= 0.240.
```

This supports the stable/asymptotic split.

## LOW1 Proof Template

Prove:

```text
contAvg(K1) >= c_0/L,
TV(K1) <= C_1/L,
Disc(mu_L) <= d_L,
```

and:

```text
c_0/L - d_L C_1/L > 0.
```

Then:

```text
sum beta_n K1(u_n)>0,
t_B<0.
```

Finite delicate windows are verified separately.
