# E73.159 Results - Endpoint symmetric image probe

Date: 2026-07-12.

Script:

```text
E73_159_endpoint_symmetric_image_probe.py
```

Purpose:

Test whether endpoint-critical divided differences with symmetric off-node
denominators generate the structured image seen in E73.010--E73.011.

## Output

```text
 lam     L mode   cols rank  condB   relB scalarB expScalarB
  16   5.545 poly       6    4   5.08  -2.80   -12.86     -12.22
  16   5.545 sym1       6    6  12.91  -5.26   -12.86     -12.22
  16   5.545 sym2      12    6  11.91  -5.28   -12.86     -12.22
  20   5.991 poly       6    4   4.80  -1.93   -13.06     -12.39
  20   5.991 sym2      12    7  11.24  -4.33   -13.06     -12.39
  24   6.356 poly       6    4   4.74  -2.17   -14.58     -13.89
  24   6.356 sym2      12    7  10.32  -3.77   -14.58     -13.89
  28   6.664 poly       6    4   5.66  -2.01   -13.92     -13.22
  28   6.664 sym2      12    7  11.05  -3.77   -13.92     -13.22
  32   6.931 poly       6    4   4.90  -1.67   -17.17     -16.46
  32   6.931 sym2      12    7  10.05  -2.04   -17.19     -16.48
```

## Reading

The symmetric basis improves the norm residual `relB` in several rows, but
the scalar residual is invariant:

```text
scalarB and expScalarB are unchanged up to numerical noise.
```

This is forced by `E_L xi_L=0`.  The image part is invisible to `xi_L`.

## Status

validated:

```text
endpoint-symmetric image is a useful low-rank structural model;
image-basis refinement cannot by itself reduce the scalar obstruction.
```

remaining:

```text
derive the scalar residual formula after the endpoint-critical image part is removed.
```
