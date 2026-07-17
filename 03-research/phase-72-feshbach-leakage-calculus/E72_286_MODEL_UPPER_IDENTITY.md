# E72.286 -- Model upper identity

**Purpose.** Reduce `MUCB` to a pure archimedean model spectral endpoint estimate.

In the corrected pole-even geometry,

```text
C_model = H_model|even - e_pole I,
e_pole  = lambda_0(H_model).
```

The global model ground is odd, so

```text
e_pole = lambda_0(H_model|odd).
```

Therefore:

```text
lambda_min(C_model)
= lambda_0(H_model|even)-lambda_0(H_model|odd),
```

as in E72.267, and also:

```text
||C_model||
= lambda_max(H_model|even)-lambda_0(H_model|odd).             (MU-ID)
```

Thus `MUCB` is the pure model endpoint theorem:

```text
lambda_max(H_model|even)-lambda_0(H_model|odd) = O(L^2).
```

No prime terms or zeta zeros enter this statement.

## Probe

Run:

```text
python3 E72_286_model_upper_identity_probe.py
```

Output:

```text
E72.286 model upper identity probe
For C_model=H_model|even-lambda_0(H_model|odd)I:
lambda_min(C_model)=lambda_0^even-lambda_0^odd, ||C_model||=lambda_max^even-lambda_0^odd.
lam L dimE dimO odd0 even0 evenMax minC/L2 opC/L2
 16 5.545177   41   40 -1.232544e+01 -1.959857e+00 1.800959e+01 3.371033e-01 9.865376e-01
 20 5.991465   49   48 -1.596102e+01 -2.119850e+00 2.244504e+01 3.855733e-01 1.069877e+00
 24 6.356108   57   56 -1.965549e+01 -2.250242e+00 2.680908e+01 4.308218e-01 1.150110e+00
 28 6.664409   65   64 -2.339219e+01 -2.359929e+00 3.112176e+01 4.735465e-01 1.227395e+00
 32 6.931472   73   72 -2.716069e+01 -2.454289e+00 3.539571e+01 5.142315e-01 1.302030e+00
```

## Reading

`MUCB` is not an arithmetic estimate.  It is the upper endpoint partner of the lower parity-gap theorem.

The proof-facing model package is now:

```text
lower endpoint: lambda_0^even-lambda_0^odd >= cL^2,
upper endpoint: lambda_max^even-lambda_0^odd <= CL^2.
```

Together these give the model size interval needed for compact-root HPAC estimates.
