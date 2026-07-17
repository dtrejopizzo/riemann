# E73.155 Results - RCE component split

Date: 2026-07-12.

Script:

```text
E73_155_rce_component_probe.py
```

Purpose:

Split the evaluated Cauchy-plane residual into model and prime parts:

```text
rho_actual xi = rho_model xi - rho_prime xi.
```

Here:

```text
H_actual = H_model - Prime,
H_model = W02 - WR.
```

## Output

```text
 lam     L gamma   modelB  primeB signedB cancelB   hB  invB status
  16   5.545   14.13   -0.874  -0.874 -19.076  -18.606 -19.921 -0.983 PASS
  16   5.545   21.02   -0.867  -0.867 -18.058  -17.595 -19.024 -0.961 PASS
  16   5.545   25.01   -0.796  -0.796 -14.097  -13.705 -13.443  0.654 FAIL
  20   5.991   14.13   -1.339  -1.339 -18.452  -17.499 -19.303 -0.990 PASS
  20   5.991   21.02   -0.433  -0.433 -17.330  -17.285 -18.303 -1.002 PASS
  20   5.991   25.01   -1.676  -1.676 -17.100  -15.810 -18.092 -0.985 PASS
  24   6.356   14.13   -0.690  -0.690 -16.569  -16.254 -17.576 -0.989 PASS
  24   6.356   21.02   -0.714  -0.714 -17.556  -17.217 -18.720 -0.989 PASS
  24   6.356   25.01   -0.772  -0.772 -18.309  -17.912 -19.540 -0.981 PASS
  28   6.664   14.13   -0.298  -0.298 -15.864  -15.931 -16.815 -1.001 FAIL
  28   6.664   21.02   -0.424  -0.424 -15.925  -15.866 -16.915 -0.991 FAIL
  28   6.664   25.01   -0.527  -0.527 -16.636  -16.475 -17.687 -0.992 PASS
  32   6.931   14.13   -1.061  -1.061 -17.047  -16.344 -18.074 -0.998 PASS
  32   6.931   21.02   -0.822  -0.822 -16.604  -16.141 -17.588 -0.997 PASS
  32   6.931   25.01   -1.353  -1.353 -16.324  -15.329 -17.313 -0.997 PASS
```

## Reading

The model and prime evaluated residuals have the same ordinary size:

```text
modelB ~= primeB ~= L^0 to L^-1.
```

The signed difference is much smaller:

```text
signedB ~= -16 to -19.
```

So the observed mechanism is not smallness of either component.  It is a
high-order signed cancellation:

```text
rho_model xi ~= rho_prime xi.
```

This is exactly the strong critical-node version of the transformed packet
identity from E72.317--E72.318.

## Consequence

The active theorem is:

```text
SCRCE_17:
sum_j |rho_model,j xi_L-rho_prime,j xi_L|
<= C L^(-17-a),
```

with `a` supplied by the inverse of the 2x2 Cauchy-plane system.

Together with `CPINV`, this implies:

```text
H0-DIV_17
=> LDIV_17
=> CSV_17
=> Uniform GATE-73.
```

The failures are the already known base/transition rows.  They should be
handled either by finite manifest absorption or by a sharper standard-box
schedule; they do not create a new mechanism.
