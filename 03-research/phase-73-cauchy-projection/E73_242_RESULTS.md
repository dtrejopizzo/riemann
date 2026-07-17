# E73.242 results - structured left-coborder audit

Command:

```text
python3 E73_242_structured_left_coborder_audit.py
```

## 1. Summary of output

The script tests, for `deg=0,...,4`,

```text
rho_a approx Y^*E,      Y in span{D^k q_j^*: j=1,2, 0<=k<=deg}.
```

Representative behavior:

```text
centerB    = L^-15 ... L^-21
resPairB   = same scale as centerB
resNormB   improves with deg, but stays far larger than center scale
fullPairB  = same scalar scale, by construction
fullNormB  = forbidden ambient rowspace residual baseline
```

## 2. Interpretation

The polynomial Cauchy primitive module reduces the row norm somewhat, but it
does not reduce the scalar pairing:

```text
<rho_a - Y^*E, xi_L>
```

below the original center scale.  Therefore it does not prove `CURV-COB`.

The full ambient rowspace baseline is included only as a guard.  It shows the
tautological fact that arbitrary rowspace fitting leaves precisely the scalar
obstruction.  It is not a proof object.

## 3. Consequence

The primitive module

```text
span{D^k q_j^*}
```

is too small.  The next non-circular module must include the rational
Loewner/divided-difference structure of the CCM cell:

```text
span{D^k q_j^*/(D^2+beta^2)^m, D^k q_j^*}
```

with beta parameters fixed by the local Cauchy/endpoint geometry, not fitted
from the final residual.

## 4. Status

```text
rejected: polynomial Cauchy primitive module as CURV-COB closure;
guarded:  full pseudoinverse/rowspace baseline is tautological;
next:     rational Loewner primitive module audit.
```

