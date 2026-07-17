# E73.236 results - endpoint moment divisibility

Command:

```text
python3 E73_236_endpoint_moment_probe.py
```

## 1. Output

```text
E73.236 endpoint moment divisibility
Checks sum c=0, sum l=0 and invariance under W,V constant gauges.
 lam      L gamma row sumCB sumLB centerB gaugedB diffB
   8    4.159  14.13   0  -26.51  -27.59   -21.68   -21.68  -29.72
   8    4.159  14.13   1  -26.92  -27.75   -21.46   -21.46  -30.79
   8    4.159  21.02   0  -27.10  -28.44   -15.76   -15.76  -31.11
   8    4.159  21.02   1  -27.10  -28.19   -15.79   -15.79  -29.87
  10    4.605  14.13   0  -25.42  -25.87   -18.50   -18.50  -25.46
  10    4.605  14.13   1 -452.32  -26.32   -18.51   -18.51  -25.42
  10    4.605  21.02   0  -24.96  -26.32   -14.98   -14.98  -26.97
  10    4.605  21.02   1  -24.96  -26.32   -14.98   -14.98  -25.96
  12    4.970  14.13   0  -23.57  -24.63   -20.62   -20.62  -26.10
  12    4.970  14.13   1  -23.19  -24.33   -20.34   -20.34  -24.93
  12    4.970  21.02   0  -24.48  -24.83   -16.61   -16.61  -25.98
  12    4.970  21.02   1  -24.87  -25.60   -16.84   -16.84  -26.02
```

## 2. Interpretation

The endpoint moment relations

```text
sum_omega c_omega = 0,
sum_omega l_omega = 0
```

hold at the numerical floor expected from the Cauchy projection and finite
assembly.  The center is invariant under constant gauges of both weight
families:

```text
W_omega -> W_omega-alpha,
V_omega -> V_omega-beta.
```

The `diffB` column is below the center by roughly 5--15 powers of `L`, limited
by floating construction of `eta` and complex weights.

## 3. Consequence

ETA-DIV should be attacked in the quotient weight space:

```text
C = sum c_omega (W_omega-alpha)
  + sum l_omega (V_omega-beta).
```

The first finite divisibility layer is now explicit.  The next required layer
is a higher-order moment or balanced-ramp identity that annihilates more than
constant weight components.

