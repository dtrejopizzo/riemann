# E72.362 results - skew window-tail decomposition

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_362_skew_window_tail_probe.py
```

The probe verifies the exact decomposition

```text
Delta = Delta_win + Delta_tail
```

where

```text
Delta_win  = S_win(z)K(w)-S_win(w)K(z),
Delta_tail = S_tail(z)K(w)-S_tail(w)K(z).
```

## Table

```text
lam   N roots node    totalNorm     winNorm      tailNorm     reconErr
 6.0  10     2 root   7.65436e-32  1.38760e-33  7.62129e-32  1.02406e-47
 6.0  10     2 shift  8.31815e-01  8.24730e-01  9.18001e-03  3.48676e-16

 8.0  12     3 root   8.10567e-24  8.09753e-24  8.65845e-27  2.96392e-40
 8.0  12     3 shift  3.39512e+01  3.39326e+01  1.57889e-01  1.66997e-14

10.0  14     3 root   6.64504e-24  6.64345e-24  3.33762e-26  7.06068e-40
10.0  14     3 shift  3.98551e+01  3.95880e+01  3.06822e-01  6.41226e-15

12.0  16     3 root   2.73555e-28  2.95842e-28  3.33396e-29  1.07811e-43
12.0  16     3 shift  5.57415e+01  5.57426e+01  2.44647e-01  6.69758e-15
```

## Reading

The reconstruction error is roundoff:

```text
reconErr ~ 1e-14 or smaller.
```

So the skew decomposition is implemented correctly.

For shifted controls, the window skew dominates:

```text
winNorm >> tailNorm.
```

Thus the current signed finite tail is not the mechanism that cancels generic shifted-window skew.
The cancellation required by `CFIR-DIV` must be specific to Xi-zero windows and must act already on
the interpolation window kernel `K_L`, not merely on the finite Fourier tail.

## Consequence

The next target is the window-skew divisor identity:

```text
Delta_win(z,w) in (Z(z),Z(w)) + controlled signed-tail correction.
```

Equivalently, the completed explicit formula must imply an antisymmetric relation among

```text
K_L(a_i,b)K(a_j)-K_L(a_j,b)K(a_i)
```

on Xi-zero windows.
