# E72.385 Results - Volterra packet bounds

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_385_volterra_packet_probe.py
```

## Output

```text
E72.385 Volterra packet bounds probe
 lam    L    M     AXscaled   DXscaled   Bscaled   boundScale
   6  3.584   10  1.861e+00  4.294e+00 5.971e-01  6.784e+00
   8  4.159   12  2.338e+00  4.655e+00 8.233e-01  8.481e+00
  10  4.605   14  2.479e+00  4.590e+00 9.700e-01  9.883e+00
  12  4.970   16  2.567e+00  4.615e+00 1.100e+00  1.108e+01
  14  5.278   18  2.500e+00  4.313e+00 1.102e+00  1.213e+01
```

## Reading

The columns report A-X, D-X, and BDRY after division by

```text
e^((c+sigma)L),
```

for `z=0.25+i`, `c=0.65`.  The scaled quantities remain moderate and are below the coarse polynomial
scale reported as `boundScale`.

This supports E72.385: the Volterra packet estimates are not hiding exponential growth beyond the
necessary factor `e^((c+sigma)L)`.

## Status

```text
validated: A-X/D-X/BDRY have the predicted finite packet scale;
proved in E72.385: BV-K follows from finite Parseval/Cauchy-Schwarz under polynomial bandwidth;
closed for NHW: horizontal BV-K gate, modulo finite bandwidth bookkeeping;
open: signed FarWall and finite-mesh tail.
```
