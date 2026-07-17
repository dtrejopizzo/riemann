# E72.217 - Prime-square profile sum

## Purpose

E72.216 gives the explicit profiled resonant bound:

```text
Res_2(S_j)
<= (1.5/c_C^2) L^(-2)
   sum_{n in S_j(x)} (Lambda(n)^2/n) sqrt(1-log n/L).
```

This note measures the remaining arithmetic sum.

## Diagnostic

Script:

```text
E72_217_prime_square_profile_sum_probe.py
```

Output:

```text
E72.217 prime-square profile sum probe
S0=sum beta2, Sphi=sum beta2 sqrt(1-logn/L)
lam L block S0 Sphi Sphi/L Sphi/L2 boundCoef
boundCoef = 1.5*Sphi/L^2, so Res2 <= boundCoef/c_C^2
 12  4.970     0 4.003118e+00 3.022758e+00 6.082236e-01 1.223836e-01 1.835754e-01
 12  4.970     1 7.155516e+00 2.804849e+00 5.643770e-01 1.135610e-01 1.703415e-01
 16  5.545     0 4.578881e+00 3.519044e+00 6.346135e-01 1.144442e-01 1.716663e-01
 16  5.545     1 9.487625e+00 3.836440e+00 6.918515e-01 1.247663e-01 1.871495e-01
 20  5.991     0 5.365280e+00 4.127954e+00 6.889725e-01 1.149923e-01 1.724885e-01
 20  5.991     1 1.125603e+01 4.545135e+00 7.586016e-01 1.266137e-01 1.899206e-01
 24  6.356     0 6.383026e+00 4.869519e+00 7.661166e-01 1.205323e-01 1.807985e-01
 24  6.356     1 1.240436e+01 4.959377e+00 7.802538e-01 1.227565e-01 1.841348e-01
 28  6.664     0 7.073118e+00 5.395902e+00 8.096595e-01 1.214901e-01 1.822351e-01
 28  6.664     1 1.374394e+01 5.479666e+00 8.222283e-01 1.233760e-01 1.850640e-01
 32  6.931     0 7.639465e+00 5.834456e+00 8.417340e-01 1.214366e-01 1.821548e-01
 32  6.931     1 1.500190e+01 5.978687e+00 8.625423e-01 1.244385e-01 1.866578e-01
 36  7.167     0 8.411423e+00 6.396826e+00 8.925341e-01 1.245332e-01 1.867998e-01
 36  7.167     1 1.586733e+01 6.283597e+00 8.767356e-01 1.223289e-01 1.834933e-01
 48  7.742     0 9.764819e+00 7.446826e+00 9.618237e-01 1.242281e-01 1.863421e-01
 48  7.742     1 1.875451e+01 7.472782e+00 9.651762e-01 1.246611e-01 1.869916e-01
 64  8.318     0 1.115863e+01 8.540714e+00 1.026804e+00 1.234471e-01 1.851706e-01
 64  8.318     1 2.198408e+01 8.803748e+00 1.058427e+00 1.272489e-01 1.908734e-01
 96  9.129     0 1.381320e+01 1.054544e+01 1.155196e+00 1.265456e-01 1.898184e-01
 96  9.129     1 2.634661e+01 1.051959e+01 1.152365e+00 1.262354e-01 1.893531e-01
```

## Reading

The profiled prime-square sum is stable:

```text
Sphi/L^2 ~= 0.12--0.127
```

for both blocks through `lambda=96`.

Thus the arithmetic half of the resonant bound is harmless:

```text
1.5 Sphi/L^2 ~= 0.18--0.19.
```

The quality of the final resonant bound is therefore controlled almost entirely by the coercivity
constant `c_C`.

## Consequence

With `c_C=0.45`, the coefficient is about:

```text
0.19 / 0.45^2 ~= 0.94.
```

With `c_C=0.50`, it is about:

```text
0.19 / 0.50^2 ~= 0.76.
```

So the square-root profile and prime-square sum are close to the observed budget, but a proof using
only the weakest `c_C=0.20` pre-stable bound would be far too loose.

## Status

Reduced:

```text
arithmetic sum -> stable elementary constant about 0.19.
```

Open:

```text
prove a strong enough stable-window coercivity constant,
or sharpen the raw HS profile below 0.75 sqrt(1-u).
```
