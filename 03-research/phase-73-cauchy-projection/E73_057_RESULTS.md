# E73.057 results - FAR3 budget exponent

## 1. Purpose

E73.057 computes effective exponents `B` defined by

```text
value = L^B
```

for FAR3 main, tail, and total budgets.

## 2. Output

```text
E73.057 FAR3 budget exponent probe
 lam     L sigma     tau    mainB    tailB   totalB      main      tail     total
  16   5.545  0.20   14.13   -6.111  -10.504   -6.110 2.846e-05 1.534e-08 2.848e-05
  16   5.545  0.20   21.02   -6.108  -11.206   -6.108 2.857e-05 4.612e-09 2.858e-05
  18   5.781  0.20   14.13   -6.621  -10.867   -6.621 9.010e-06 5.239e-09 9.016e-06
  18   5.781  0.20   21.02   -6.752  -11.552   -6.752 7.158e-06 1.576e-09 7.160e-06
  20   5.991  0.20   14.13   -6.282  -14.214   -6.282 1.304e-05 8.879e-12 1.304e-05
  20   5.991  0.20   21.02   -6.312  -14.313   -6.312 1.236e-05 7.436e-12 1.236e-05
  24   6.356  0.20   14.13   -5.974  -15.609   -5.974 1.590e-05 2.905e-13 1.590e-05
  24   6.356  0.20   21.02   -5.930  -13.641   -5.930 1.726e-05 1.105e-11 1.726e-05
```

## 3. Diagnosis

In the tested windows:

```text
main + total behave near L^(-6);
tail behaves at least near L^(-10), often much smaller.
```

This suggests the simple budget target:

```text
FAR3-main <= C_main L^(-5),
FAR3-tail <= C_tail L^(-9),
```

with absolute constants.  The exponents include slack relative to the observed values.

## 4. Status

```text
observed: strong negative effective exponents;
candidate uniform budget: main L^-5, tail L^-9;
remaining: analytic proof of these budget rules.
```
