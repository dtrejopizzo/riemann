# E73.158 Results - Current source-image scalar residual

Date: 2026-07-12.

Script:

```text
E73_158_current_source_image_probe.py
```

Purpose:

Rerun the structured image test in the current larger scale range, using the
exact ground eigenvector.  The test measures:

```text
R_b=(I-P_Image(E_L P_L))S_b,
<xi_L,S_b>=<xi_L,R_b>.
```

## Output

```text
E73.158 current source-image scalar residual probe
 lam     L   dim rank  condB   relB xiShareB  srcB  scalarB expScalarB status
  16   5.545    41    9  12.50  -7.11    -7.15   1.40   -12.86     -12.22 PASS
  16   5.545    41    9  12.50  -4.83    -7.08  -3.39   -15.31     -14.66 PASS
  16   5.545    41    9  12.50  -4.83    -7.25   1.26   -10.83     -10.18 PASS
  20   5.991    49   10  12.37  -7.09    -7.36   1.38   -13.07     -12.40 PASS
  20   5.991    49   10  12.37  -4.86    -7.42  -3.17   -15.45     -14.78 PASS
  20   5.991    49   10  12.37  -5.06    -7.33   1.33   -11.07     -10.40 PASS
  24   6.356    57   11  11.52  -6.26    -9.68   1.37   -14.57     -13.88 PASS
  24   6.356    57   11  11.52  -4.11    -9.69  -3.03   -16.84     -16.15 PASS
  24   6.356    57   11  11.52  -4.33    -9.68   1.33   -12.68     -12.00 PASS
  28   6.664    65   11  11.32  -5.61    -9.66   1.37   -13.90     -13.20 PASS
  28   6.664    65   11  11.32  -3.69    -9.55  -2.88   -16.13     -15.42 PASS
  28   6.664    65   11  11.32  -3.88    -9.55   1.34   -12.09     -11.39 PASS
  32   6.931    73   13  11.60  -7.62    -7.82   1.36   -14.08     -13.37 PASS
  32   6.931    73   13  11.60  -5.72    -8.51  -2.76   -16.99     -16.28 PASS
  32   6.931    73   13  11.60  -5.95    -8.56   1.38   -13.13     -12.41 PASS
```

## Reading

The structured image has small rank:

```text
rank ~= 9 to 13
```

and captures most of the source, but the decisive fact is scalar:

```text
xiShareB ~= -7 to -10.
```

That means the remaining cokernel component is mostly orthogonal to `xi_L`.
This matches E73.020/E73.021 and remains true in the larger current scales.

The weighted scalar residual is polynomially small in this synthetic
off-line test:

```text
expScalarB ~= -10 to -16.
```

## Status

validated:

```text
structured image scalar criterion remains numerically stable at current scales;
generic norm-image membership is not the right target;
the source-image residual must be controlled only in the xi_L scalar channel.
```

open:

```text
derive the low-rank structured image symbolically and prove the scalar residual bound through
natural-height windows.
```
