# E73.255 results - pair-mode audit for `b=D_Q xi_L`

Command:

```bash
python3 03-research/phase-73-cauchy-projection/E73_255_pair_mode_b_vector_probe.py
```

Conclusion:

```text
PAIR-PARITY-B rejected.
BORDER-ROW-DIV retained.
```

The dominant pair mode is not stable. At `lambda=8` the canonical `pow=0`
case is symmetric-dominant, at `lambda=10` it is antisymmetric-dominant, at
`lambda=12` it returns to symmetric-dominant for `pow=0` but not for `pow=1`,
and at `lambda=16` both gamma pairs can select different dominant modes.

Representative table:

```text
Pair modes
 lam      L pow  g dom  row0B  row1B   symB  antiB pairNormB cancelB domLossB
   8    4.159   0  0  sym -21.68  -21.46 -21.32 -22.61    -21.31    1.15    -0.14
   8    4.159   0  1  sym -15.76  -15.79 -15.53 -18.13    -15.53    2.37    -0.23
  10    4.605   0  0 anti -18.50  -18.51 -21.62 -18.27    -18.27    3.12    -0.22
  10    4.605   0  1 anti -14.98  -14.98 -18.22 -14.75    -14.75    3.25    -0.22
  12    4.970   0  0  sym -20.62  -20.36 -20.26 -21.20    -20.25    0.84    -0.10
  12    4.970   1  0 anti -18.32  -18.36 -20.29 -18.12    -18.12    1.97    -0.20
  16    5.545   0  0 anti -19.30  -19.81 -19.80 -19.30    -19.25    0.50     0.00
  16    5.545   0  1  sym -18.20  -19.15 -18.29 -18.52    -18.18    0.33     0.10
```

Four-mode table:

```text
 lam      L pow   bMaxB  bNormB    ssB    saB    asB    aaB  maxMode
   8    4.159   0  -15.76  -15.53 -15.77 -18.37 -15.77 -18.37       ss
   8    4.159   1  -15.76  -15.53 -15.77 -18.37 -15.77 -18.37       ss
   8    4.159   2  -15.75  -15.53 -15.77 -17.67 -15.77 -17.66       ss
  10    4.605   0  -14.98  -14.75 -18.46 -14.98 -18.45 -14.98       sa
  10    4.605   1  -14.98  -14.75 -18.46 -14.98 -18.45 -14.98       sa
  10    4.605   2  -14.98  -14.75 -18.45 -14.98 -18.45 -14.98       sa
  12    4.970   0  -16.61  -16.49 -16.71 -17.76 -16.72 -17.76       ss
  12    4.970   1  -16.64  -16.49 -16.71 -17.74 -16.72 -18.52       ss
  12    4.970   2  -16.61  -16.49 -16.71 -17.80 -16.72 -17.76       ss
  16    5.545   0  -18.20  -18.18 -18.54 -18.91 -18.45 -18.59       as
  16    5.545   1  -15.26  -15.19 -16.10 -15.42 -16.10 -15.42       aa
  16    5.545   2  -17.03  -16.89 -17.10 -17.98 -17.12 -17.90       ss
```

Interpretation:

```text
The bordered vector is not explained by a universal row-pair parity channel.
The next proof-facing statement must be rowwise quotient annihilation, or a
stronger four-row identity that implies it without selecting a fixed parity.
```

