# E73.253 results - Cramer numerator identity

Command:

```text
python3 E73_253_cramer_numerator_identity.py
```

## 1. Output

```text
E73.253 Cramer numerator identity
For J*=max minor: z_j = N_j/det(D_J), N_j=det(D_J with col j replaced by D_Q xi).
 lam      L pow pivIdx              denB numMaxB zMaxB crRel numAbsCeilB numGainB
   8    4.159   0     [-5, -2, 2, 5] -46.48  -50.79  -4.31 7.7e-15      -41.70     9.09
   8    4.159   1     [-5, -2, 2, 5] -46.48  -50.79  -4.31 3.7e-14      -41.70     9.09
   8    4.159   2     [-5, -2, 2, 5] -46.48  -50.52  -4.04 1.3e-14      -41.70     8.82
  10    4.605   0     [-7, -6, 6, 7] -38.38  -42.61  -4.24 7.9e-15      -36.13     6.49
  10    4.605   1     [-7, -6, 6, 7] -38.38  -42.62  -4.24 5.7e-15      -36.13     6.49
  10    4.605   2     [-7, -6, 6, 7] -38.38  -42.62  -4.24 7.8e-15      -36.13     6.49
  12    4.970   0     [-9, -4, 4, 9] -33.65  -41.34  -7.69 6.5e-15      -34.61     6.73
  12    4.970   1     [-9, -4, 4, 9] -33.69  -40.42  -6.74 8.1e-15      -34.61     5.81
  12    4.970   2     [-9, -4, 4, 9] -33.69  -41.54  -7.86 2.7e-14      -34.61     6.93
  16    5.545   0 [-20, -13, 18, 20] -19.69  -31.63 -11.94 7.2e-15      -28.05     3.59
  16    5.545   1 [-20, -18, 18, 20] -24.31  -32.49  -8.18 4.5e-15      -28.51     3.97
  16    5.545   2 [-20, -18, 18, 20] -31.44  -40.09  -8.65 4.4e-15      -34.85     5.24
```

## 2. Verification

The Cramer identity is verified at roundoff:

```text
crRel <= 3.7e-14.
```

The scale relation is:

```text
zMaxB = numMaxB - denB.
```

up to rounding, as expected from `z_j=N_j/det(D_J)`.

## 3. Endpoint update

The remaining spectral divisibility can now be stated as the finite determinant
identity:

```text
CRAMER-NUM-DIV:
N_j = O_M(L^-M) det(D_J).
```

Together with `MAXMIN-NONDEG`, this is equivalent to `MAXMIN-PIV-DIV`.
