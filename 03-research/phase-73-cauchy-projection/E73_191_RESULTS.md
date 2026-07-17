# E73.191 results - endpoint rank-one source

Command:

```text
python3 E73_191_endpoint_rank_one_source_probe.py
```

Output:

```text
E73.191 endpoint rank-one source
Measures S_eta, S_q, and B_a'(0)=-(2/L)S_qS_eta.
 lam     L gamma row SetaB SqB prodB xiSumB parSumB etaNorm
  12   4.970   14.13   0 -10.87   1.03 -10.41  -10.87   -22.31  1.0000
  12   4.970   14.13   1 -10.87   1.03 -10.41  -10.87   -22.31  1.0000
  12   4.970   21.02   0 -10.87   0.85 -10.59  -10.87   -20.23  1.0000
  12   4.970   21.02   1 -10.87   0.85 -10.59  -10.87   -20.23  1.0000
  16   5.545   14.13   0  -9.41   0.22  -9.78   -9.41   -20.83  1.0000
  16   5.545   14.13   1  -9.41   0.22  -9.78   -9.41   -20.83  1.0000
  16   5.545   21.02   0  -9.41   0.45  -9.55   -9.41   -20.02  1.0000
  16   5.545   21.02   1  -9.41   0.45  -9.55   -9.41   -20.02  1.0000
  20   5.991   14.13   0 -10.67   0.18 -11.10  -10.67   -20.47  1.0000
  20   5.991   14.13   1 -10.67   0.18 -11.10  -10.67   -20.47  1.0000
  20   5.991   21.02   0 -10.67   1.75  -9.54  -10.67   -21.67  1.0000
  20   5.991   21.02   1 -10.67   1.75  -9.54  -10.67   -21.67  1.0000
  24   6.356   14.13   0  -8.56   0.67  -8.52   -8.56   -18.40  1.0000
  24   6.356   14.13   1  -8.56   0.67  -8.52   -8.56   -18.40  1.0000
  24   6.356   21.02   0  -8.56   0.85  -8.34   -8.56   -20.65  1.0000
  24   6.356   21.02   1  -8.56   0.85  -8.34   -8.56   -20.65  1.0000
  32   6.931   14.13   0  -7.98  -1.71 -10.32   -7.98   -20.09  1.0000
  32   6.931   14.13   1  -7.98  -1.71 -10.32   -7.98   -20.09  1.0000
  32   6.931   21.02   0  -7.98   0.98  -7.63   -7.98   -19.38  1.0000
  32   6.931   21.02   1  -7.98   0.98  -7.63   -19.38  1.0000
```

Reading:

```text
S_eta has the same scale as sum xi_L.
The Cauchy-plane component has negligible mass: sum P_w xi_L is about L^-18 to L^-22.
The endpoint derivative is governed by the global source mass sum xi_L times S_q(a).
```

Conclusion:

```text
B_a'(0)=-(2/L)S_q(a)S_eta
       =-(2/L)S_q(a)sum xi_L + negligible.
```

Thus the next structural sublemma is:

```text
MASS-ZERO:
sum_n xi_L(n) = O_R(L^-R)
```

or, if that is too strong globally, subtract the explicit rank-one ramp and
prove `TRANS-CELL` for the double-zero remainder.
