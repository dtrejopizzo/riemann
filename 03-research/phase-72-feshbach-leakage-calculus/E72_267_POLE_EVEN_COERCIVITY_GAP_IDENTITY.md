# E72.267 -- Pole-even coercivity gap identity

**Purpose.** Turn the corrected model coercivity estimate into an exact spectral identity.

In the pole-relative even geometry of E72.262,

```text
e_pole  = lambda_0(H_model),
B_even  = orthonormal even Fourier basis,
C_model = B_even^T(H_model-e_pole I)B_even.
```

The global model pole is odd, while the physical RFBD complement is the full even sector.

## Lemma

Let

```text
lambda_0^odd  = lambda_0(H_model),
lambda_0^even = lambda_min(B_even^T H_model B_even).
```

Then

```text
lambda_min(C_model) = lambda_0^even - lambda_0^odd.
```

Consequently the pole-even quadratic coercivity estimate

```text
C_model >= c_C L^2 I
```

is equivalent to the odd/even gap estimate

```text
lambda_0^even - lambda_0^odd >= c_C L^2.
```

## Proof

By construction,

```text
C_model = B_even^T H_model B_even - e_pole I_even.
```

Since `B_even` is an orthonormal basis of the even sector, the eigenvalues of
`B_even^T H_model B_even` are exactly the even-sector eigenvalues of `H_model`. Subtracting
`e_pole I_even` shifts every eigenvalue by `-e_pole`. Therefore its smallest eigenvalue is

```text
lambda_min(C_model)
= lambda_min(B_even^T H_model B_even) - e_pole
= lambda_0^even - lambda_0^odd.
```

This proves the identity.

## Numerical check

The companion script checks the identity in the corrected harness:

```text
E72.267 pole-even coercivity gap identity
Checks min eig(C_model)=lambda_0(H_model|even)-lambda_0(H_model).
lam L dim e_pole even0 gap minC relErr gap/L2 cond oddNorm evenLeak
  6 3.583519  19 -3.755535523e+00 -1.251543828e+00 2.503991695e+00 2.503991695e+00 1.60e-15 1.949905104e-01 4.009e+00 1.000e+00 2.209e-16
  8 4.158883  25 -5.375111257e+00 -1.462295379e+00 3.912815878e+00 3.912815878e+00 1.70e-15 2.262225999e-01 3.610e+00 1.000e+00 4.500e-16
 12 4.969813  33 -8.777747852e+00 -1.753611155e+00 7.024136698e+00 7.024136698e+00 3.79e-16 2.843890084e-01 3.167e+00 1.000e+00 3.664e-16
 16 5.545177  41 -1.232544481e+01 -1.959856512e+00 1.036558829e+01 1.036558829e+01 5.14e-16 3.371033429e-01 2.927e+00 1.000e+00 4.587e-16
 20 5.991465  49 -1.596102409e+01 -2.119849783e+00 1.384117431e+01 1.384117431e+01 7.70e-16 3.855732981e-01 2.775e+00 1.000e+00 3.791e-16
 24 6.356108  57 -1.965548698e+01 -2.250241580e+00 1.740524540e+01 1.740524540e+01 8.16e-16 4.308217907e-01 2.670e+00 1.000e+00 5.903e-16
```

The pole is odd to numerical precision (`oddNorm=1`, `evenLeak~1e-16`), and the identity holds to
roundoff.

## Consequence

The corrected MCOER2 theorem is no longer a hidden matrix statement. It is the explicit model gap
theorem:

```text
MCOER2-pole-even:
lambda_0(H_model|even)-lambda_0(H_model|odd) >= c_C L^2.
```

This is purely archimedean/model-theoretic. It contains no primes, no zeros, and no RH-strength
arithmetic input.

The remaining analytic task is to prove this odd/even gap lower bound from the explicit
archimedean/prolate kernel defining `H_model`.
