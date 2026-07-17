# E73.239 results - moment annihilator audit

Command:

```text
python3 E73_239_moment_annihilator_audit.py
```

## 1. Output

```text
E73.239 moment annihilator audit
Projects weights onto endpoint/derivative moment rows and measures residual pairing.
 lam      L gamma row centerB res2B res3B mom2B mom3B resNorm2B resNorm3B
  12    4.970  14.13   0   -21.26  -21.27  -12.03  -24.35  -12.03       2.02       2.01
  12    4.970  14.13   1   -21.16  -21.14  -12.03  -25.87  -12.03       2.02       2.01
  12    4.970  21.02   0   -20.43  -20.43  -12.21  -24.59  -12.21       2.02       2.01
  12    4.970  21.02   1   -19.87  -19.87  -12.21  -27.36  -12.21       2.02       2.01
  16    5.545  14.13   0   -18.92  -18.90  -12.08  -22.17  -12.08       2.11       2.11
  16    5.545  14.13   1   -20.08  -20.08  -12.08  -22.68  -12.08       2.11       2.11
  16    5.545  21.02   0   -18.21  -18.21  -11.85  -23.62  -11.85       2.11       2.11
  16    5.545  21.02   1   -19.12  -19.12  -11.85  -24.41  -11.85       2.11       2.11
  20    5.991  14.13   0   -18.47  -18.44  -13.38  -21.22  -13.38       2.19       2.19
  20    5.991  14.13   1   -18.33  -18.36  -13.38  -20.29  -13.38       2.19       2.19
  20    5.991  21.02   0   -18.21  -18.22  -11.81  -20.94  -11.81       2.19       2.19
  20    5.991  21.02   1   -18.77  -18.77  -11.81  -21.39  -11.81       2.19       2.19
```

## 2. Interpretation

`res2B` is the pairing after removing from the weight vector the two endpoint
moment directions:

```text
sum c_omega,      sum l_omega.
```

It is essentially the same size as `centerB`.  Thus endpoint moments alone do
not explain the rapid cancellation.

`res3B` includes the derivative row

```text
sum iomega c_omega + sum l_omega.
```

This is not an annihilating constraint for the original packet.  Treating it
as one creates a large artificial contribution of size about `L^-12`, exactly
as expected from the nonzero rank-one source `B'(0)`.

The residual weight norm remains large (`L^2` scale), so no norm argument is
available.

## 3. Consequence

The next relation must come from the finite eigen-equation for `eta`, not from
endpoint data alone:

```text
EIG-COEFF:
derive additional finite coefficient relations satisfied by
eta_w=(I-P_w)xi_L
```

such that the curvature quotient weights lie in their annihilator up to
`O_M(L^-M)`.

This is now the genuine load-bearing algebraic target after all quotient
normalizations.

