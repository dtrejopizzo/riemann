# E73.252 results - structured coordinate coborder probe

Command:

```text
python3 E73_252_structured_coord_coborder_probe.py
```

## 1. Output excerpt

```text
E73.252 structured coordinate coborder probe
Project coordinate rows m_j against combined DD-local generated image.
 lam      L srcPow fitPow rankS zMaxB resPairMaxB resNormMaxB relResMaxB fullRowPairB
   8    4.159      0      0     5  -4.31       -4.31        0.42       -0.00        -4.31
   8    4.159      0      4     5  -4.31       -4.31        0.42       -0.00        -4.31
  10    4.605      0      0     6  -4.24       -4.24        0.41       -0.07        -4.24
  10    4.605      0      4     6  -4.24       -4.24        0.41       -0.07        -4.24
  12    4.970      0      0     6  -7.69       -7.69        0.48       -0.05        -7.69
  12    4.970      0      4     6  -7.69       -7.69        0.48       -0.05        -7.69
  16    5.545      0      0     7 -11.94      -11.94        0.68       -0.04       -11.95
  16    5.545      0      4     9 -11.94      -11.66        0.32       -0.41       -11.95
```

## 2. Interpretation

The relevant comparison is:

```text
zMaxB versus resPairMaxB.
```

They remain essentially equal.  Increasing the DD-local fit power does not
produce a structural coborder for the coordinate rows.

The norm residual can change, especially in conditioning-sensitive
`lambda=16` rows, but the scalar pairing does not collapse.  Therefore this is
not the missing mechanism.

## 3. Status

```text
rejected: combined DD-local first-layer image for COORD-ROW-DIV;
open:     construct a second-layer quotient-coordinate coborder COORD-COB2.
```
