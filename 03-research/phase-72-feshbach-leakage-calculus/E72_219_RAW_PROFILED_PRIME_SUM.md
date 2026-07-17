# E72.219 - Near-sharp raw-profiled prime sum

## Purpose

E72.218 showed that the soft `sqrt(1-u)` profile is too loose. The near-sharp route is to keep the
actual raw HS profile:

```text
Rraw_j(x)
 =
sum_{n in S_j(x)}
  (Lambda(n)^2/n)||B_x^*U_{log n}B_x||_HS^2.
```

Then coercivity gives:

```text
Res_2(S_j) <= 2 Rraw_j(x) / lambda_min(C_x)^2.       (RRAW)
```

## Diagnostic

Script:

```text
E72_219_raw_profiled_prime_sum_probe.py
```

Output:

```text
E72.219 raw-profiled prime sum probe
Rraw=sum beta2 ||B*U_logn B||_HS^2; bound=2Rraw/minC^2
lam block actual Rraw Rraw/L4 bound ratio c_obs
 12     0 7.506459e-01 3.622832e+01 5.938653e-02 1.279065e+00 1.70 0.305
 12     1 3.723544e-01 1.806069e+01 2.960561e-02 6.376446e-01 1.71 0.305
 16     0 5.903247e-01 5.351819e+01 5.660302e-02 9.516911e-01 1.61 0.345
 16     1 3.676131e-01 3.351179e+01 3.544344e-02 5.959258e-01 1.62 0.345
 20     0 5.066864e-01 7.547344e+01 5.856824e-02 7.486171e-01 1.48 0.396
 20     1 3.181675e-01 4.765757e+01 3.698281e-02 4.727129e-01 1.49 0.396
 24     0 4.667205e-01 1.034607e+02 6.338848e-02 6.566820e-01 1.41 0.439
 24     1 2.615648e-01 5.853232e+01 3.586169e-02 3.715143e-01 1.42 0.439
 28     0 4.259593e-01 1.307571e+02 6.628553e-02 5.783996e-01 1.36 0.479
 28     1 2.487475e-01 7.705970e+01 3.906436e-02 3.408709e-01 1.37 0.479
```

## Reading

The near-sharp raw-profiled sum has stable scale:

```text
Rraw_0(x) / L^4 ~= 0.056--0.067,
Rraw_1(x) / L^4 ~= 0.030--0.040.
```

The resulting coercive bound loses only:

```text
1.36--1.71
```

against the actual resonant pair energy. This is the same good ratio observed in E72.215.

## Candidate theorem

A sharp resonant-pair theorem can be stated as:

```text
Rraw_0(x) <= C_0 L^4,       C_0 ~= 0.07,
Rraw_1(x) <= C_1 L^4,       C_1 ~= 0.04,
lambda_min(C_x) >= c_C L^2.
```

Then:

```text
Res_2(S_j) <= 2C_j/c_C^2.
```

This is a precise finite theorem with two model/Fourier constants and no zeros.

## Status

Positive. The resonant pair sublemma should be pursued through the near-sharp raw-profiled sum, not
through a soft universal profile.
