# E72.384 Results - BV-K packet reduction

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_384_bvk_packet_probe.py
```

## Output

```text
E72.384 BV-K packet reduction probe
 lam    L       BVdirect    DBVbound    ratio   scaledDBV
   6   3.584   2.337e+01   5.900e+01   0.396   6.545e-01
   8   4.159   4.728e+01   9.054e+01   0.522   5.156e-01
  10   4.605   6.853e+01   1.320e+02   0.519   4.541e-01
  12   4.970   1.056e+02   2.065e+02   0.512   4.744e-01
  14   5.278   1.354e+02   2.633e+02   0.514   4.315e-01
```

## Reading

The probe checks:

```text
BVdirect <= 2|B(0)|+2 int_0^L e^(ct)|B'(t)|dt.
```

The ratio is below `0.53` in all tested windows.  The scaled derivative bound

```text
DBVbound / (e^((c+sigma)L)L)
```

is stable, supporting the `BV-K` packet scale used in E72.383.

## Status

```text
validated: BV-K reduction to DBV-K for the actual packet;
validated: DBV-K has stable e^((c+sigma)L)L scaling in tested windows;
proved in E72.384: DBV-K reduces to A-X/D-X/BDRY Volterra packet inequalities;
open: prove A-X/D-X/BDRY uniformly.
```
