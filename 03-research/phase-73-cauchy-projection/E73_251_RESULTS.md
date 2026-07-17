# E73.251 results - coordinate functional probe

Command:

```text
python3 E73_251_coordinate_functional_probe.py
```

## 1. Summary

For the maximal-minor pivot set `J_*`, define:

```text
M = D_Q[:,J_*]^{-1}D_Q,
z = M xi_L.
```

The probe reports:

```text
zMaxB      = max_j log_L |z_j|;
absCeilB  = max_j log_L sum_n |m_j(n)xi_n|;
gainB     = log_L(absCeil/|z|);
relDistB  = relative distance of m_j to Row(E);
moment0B  = log_L max_j |sum_n m_j(n)|;
moment1B  = log_L max_j |sum_n n m_j(n)|.
```

## 2. Key rows

```text
 lam      L pow pivIdx              row rankE zMaxB absCeilB gainB mNormB relDistB rowDistB moment0B moment1B
   8    4.159   0     [-5, -2, 2, 5] all     7  -4.31     0.08   4.39   0.42    -0.11     0.31    -6.89    -2.18
  10    4.605   0     [-7, -6, 6, 7] all     8  -4.24     0.29   4.53   0.50    -0.34     0.16    -4.58    -0.64
  12    4.970   0     [-9, -4, 4, 9] all     8  -7.69     0.22   7.92   0.55    -0.31     0.25    -3.44     0.35
  16    5.545   0 [-20, -13, 18, 20] all    13 -11.94     0.57  12.51   0.77    -7.66    -6.93     0.86     2.97
```

## 3. Interpretation

The absolute ceiling is much larger than the actual coordinate value:

```text
gainB ≈ 4.4, 4.5, 7.9, 12.5
```

for the `pow=0` windows above.  Thus `MAXMIN-PIV-DIV` cannot be closed by an
absolute estimate on the coordinate functional.

The low moments do not explain the cancellation:

```text
moment0B and moment1B are not uniformly small.
```

The right certificate is rowspace-divisibility for the coordinate functionals:

```text
COORD-ROW-DIV:
m_j = Y_j^*E + O_M(L^-M).
```

Equivalently:

```text
m_j xi_L = O_M(L^-M).
```

This must be proved from the quotient formula for `D_Q`; using full rowspace
projection as a proof would be circular.

## 4. Status

```text
new endpoint: COORD-ROW-DIV for the maximal-minor coordinate rows;
rejected: absolute ceiling and endpoint moment explanations;
open: derive the coordinate rows as structured E-coborders.
```
