# E72.197 - Signed Green-word expansion

## Purpose

E72.196 identified the exact fixed certificate as a set of Green-cycle inequalities. This note opens
each overlap cell using the one-sided translation identity

```text
Q_x(y)=U_y+U_y^*.
```

The result is an exact signed-word expansion of every Green-cycle.

## Identity

For each prime power `n`, define the two signed relative cells

```text
A_n^+ = - beta_n C_x^(-1/2)B_x^*U_{y_n}B_xC_x^(-1/2),
A_n^- = - beta_n C_x^(-1/2)B_x^*U_{y_n}^*B_xC_x^(-1/2).
```

Then

```text
A_n = A_n^+ + A_n^-.
```

Therefore, for any Green-cycle word `w=(n_1,...,n_r)`,

```text
Tr(A_{n_1}...A_{n_r})
 =
sum_{eps_1,...,eps_r in {+,-}}
Tr(A_{n_1}^{eps_1}...A_{n_r}^{eps_r}).          (SGW)
```

This is just multilinearity, but it matters because the signed words retain the translation phases
that absolute-value and Haar-style arguments destroy.

## Verification

Script:

```text
E72_197_signed_green_word_probe.py
```

It checks `(SGW)` after the exact relative whitening/compression:

```text
E72.197 signed Green-word expansion probe
checks Q_y=U_y+U_y* after exact relative whitening
lam block r direct signed relErr imag
  6     0 2 -2.245942529477e-02 -2.245942529477e-02 3.398e-15 0.000e+00
  6     0 3 -6.730681517029e-03 -6.730681517029e-03 6.443e-16 6.019e-36
  6     1 2 +3.710557803745e-05 +3.710557803744e-05 6.447e-14 0.000e+00
  6     1 3 -2.515356863783e-08 -2.515356863787e-08 1.650e-12 1.881e-37
  8     0 2 -4.550369167584e-03 -4.550369167584e-03 8.578e-15 0.000e+00
  8     0 3 -4.237773648823e-03 -4.237773648823e-03 0.000e+00 0.000e+00
  8     1 2 -3.874596320045e-04 -3.874596320045e-04 1.119e-14 0.000e+00
  8     1 3 -5.639868665379e-21 -5.639868665380e-21 4.002e-14 0.000e+00
 12     0 2 -8.854239478081e-04 -8.854239478080e-04 7.935e-14 0.000e+00
 12     0 3 -1.585076396926e-03 -1.585076396926e-03 4.104e-16 1.881e-37
 12     1 2 -3.454962703296e-05 -3.454962703296e-05 2.216e-14 0.000e+00
 12     1 3 +4.690067806540e-08 +4.690067806540e-08 4.374e-15 3.673e-40
```

## Consequence

The final fixed inequalities can be attacked at the signed Green-word level:

```text
GC-NTC, GC-LM8, GC-XNEG32
```

become finite sums of signed one-sided translation words with model Green insertions.

This is narrower than the previous cycle form. Any successful proof must exploit cancellation between
these signed words, or a structural domination of their signed sum. Bounding the absolute values of the
signed words would reintroduce the incoherent ceiling.
