# E72.222 - Even-leading bound for Rraw

## Purpose

E72.220--E72.221 show:

```text
||B_x^*U_yB_x||_HS^2
<= ||E U_y E||_HS^2
~= (dim_even/2)(1-y/L).
```

This note tests the resulting simple bound for the near-sharp raw-profiled sum:

```text
Rraw_j
= sum_{n in S_j} (Lambda(n)^2/n)||B_x^*U_{log n}B_x||_HS^2.
```

The candidate upper bound is:

```text
Rraw_j
<= (dim_even/2)
   sum_{n in S_j} (Lambda(n)^2/n)(1-log n/L).       (ELR)
```

## Diagnostic

Script:

```text
E72_222_even_leading_sum_probe.py
```

Output:

```text
E72.222 even-leading Rraw bound probe
lead=0.5*dim_even*sum beta2*(1-u)
lam block qdim Rraw lead ratio leadL4 sum1-u
 12     0   33 3.622832e+01 3.817292e+01 1.054 6.257418e-02 2.313511e+00
 12     1   33 1.806069e+01 2.061765e+01 1.142 3.379706e-02 1.249555e+00
 16     0   41 5.351819e+01 5.609154e+01 1.048 5.932471e-02 2.736173e+00
 16     1   41 3.351179e+01 3.621242e+01 1.081 3.829974e-02 1.766460e+00
 20     0   49 7.547344e+01 7.872782e+01 1.043 6.109368e-02 3.213381e+00
 20     1   49 4.765757e+01 5.141492e+01 1.079 3.989855e-02 2.098568e+00
 24     0   57 1.034607e+02 1.072507e+02 1.037 6.571059e-02 3.763184e+00
 24     1   57 5.853232e+01 6.445024e+01 1.101 3.948749e-02 2.261412e+00
 28     0   65 1.307571e+02 1.355233e+02 1.036 6.870171e-02 4.169949e+00
 28     1   65 7.705970e+01 8.106002e+01 1.052 4.109227e-02 2.494155e+00
```

## Reading

The even-leading bound is near-sharp:

```text
lead/Rraw ~= 1.04--1.14.
```

This is substantially better than the soft `sqrt(1-u)` profile and almost as good as the exact raw
profile.

## Consequence

The resonant pair theorem can now be stated using only:

```text
dim_even,
sum (Lambda(n)^2/n)(1-log n/L),
lambda_min(C_x).
```

Namely:

```text
Res_2(S_j)
<= [dim_even / lambda_min(C_x)^2]
   sum_{n in S_j} (Lambda(n)^2/n)(1-log n/L).       (R2-ELR)
```

This is a clean finite inequality. It uses no character torus, no zeros, and no delicate ground-vector
alignment.

## Status

Strong positive. The resonant degree-2 sublemma is reduced to:

```text
1. full-even overlap estimate;
2. quadratic model coercivity;
3. elementary prime-square weighted sum.
```
