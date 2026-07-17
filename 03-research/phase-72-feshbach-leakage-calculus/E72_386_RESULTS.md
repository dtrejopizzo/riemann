# E72.386 Results - FarWall signed gate

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_386_farwall_signed_probe.py
```

## Output

```text
E72.386 FarWall signed probe
 lam     L       T       |total|      |near|       |far|       farAbs   abs/far
   6   3.584     36.0   2.237e-02   4.248e-03   2.007e-02   9.419e+00 4.692e+02
   8   4.159     64.0   9.011e-03   3.261e-04   1.563e-03   1.777e+01 1.137e+04
  10   4.605    100.0   2.187e-03   7.888e-04   6.339e-03   1.485e+01 2.342e+03
  12   4.970    144.0   2.934e-03   1.579e-03   2.380e-02   2.712e+01 1.139e+03
```

## Reading

The diagnostic decomposes the natural-height wall quadrature defect into near and far pieces for the
actual Feshbach packet.  The absolute far ceiling is much larger than the signed far value:

```text
farAbs / |far| = 10^2--10^4.
```

This validates the audit in E72.386.  FarWall cannot be closed by taking absolute values after
splitting into prime cells.  The proof must use the signed band-limiting form:

```text
ErrWall(z)=<g_z, D_T*dmu_{L,c}-dmu_{L,c}>.
```

## Status

```text
validated: absolute FarWall loses several orders of magnitude;
validated: signed FarWall is the load-bearing remaining wall estimate;
proved in E72.386: absolute FarWall has exponential scale at natural height;
open: prove SignedFar for the actual Feshbach packet and finite von Mangoldt measure.
```
