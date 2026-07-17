# E73.194 results - second Abel kernel

Command:

```text
python3 E73_194_second_abel_kernel_probe.py
```

Output:

```text
E73.194 second Abel kernel
Checks F[Bbal]=int K_L(t) Bbal''(t) dt.
 lam     L gamma row totalB abelB relErr cAbsB
  12   4.970   14.13   0  -20.85 -17.09  4.2e+02   0.25
  12   4.970   14.13   1  -21.09 -17.94  1.6e+02   0.25
  12   4.970   21.02   0  -20.40 -17.25  1.5e+02   0.25
  12   4.970   21.02   1  -19.87 -17.55  4.2e+01   0.25
  16   5.545   14.13   0  -19.19 -14.36  3.9e+03  -0.07
  16   5.545   14.13   1  -19.98 -14.86  6.4e+03  -0.07
  16   5.545   21.02   0  -18.18 -14.57  4.9e+02  -0.07
  16   5.545   21.02   1  -19.03 -15.43  4.7e+02  -0.07
```

Sanity check on polynomial double-zero packets:

```text
r1       relative error 4.8e-11
y2L2     relative error 1.2e-09
y3       relative error 1.2e-11
```

Reading:

```text
The second-Abel identity is algebraically correct and passes on explicit
double-zero polynomial packets.

For the oscillatory balanced Cauchy packet, the direct nested quadrature of
int K_L B'' is not accurate enough to reach the true residual scale.  It
lands around L^-14--L^-17 while the matrix residual is L^-18--L^-21.
```

Conclusion:

```text
E73.194 is a proof-facing analytic identity, but the current numerical probe
is only a conditioning diagnostic for the actual B_bal packets.
```

The new theorem target is still valid:

```text
SECOND-ABEL:
int_0^L K_L(t)(B_a^bal)''(t)dt = O_R(L^-R),
```

but it should be verified in future by exact finite-frequency summation or
interval arithmetic, not by nested adaptive quadrature.
