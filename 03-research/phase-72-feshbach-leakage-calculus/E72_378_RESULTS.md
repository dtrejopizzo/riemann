# E72.378 Results - Finite-height wall tail

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_378_wall_tail_probe.py
```

## Output

```text
E72.378 finite-height wall-tail probe
 L    c     u      T        err          bound        ratio
4.0  0.8  0.70    40.0    1.330e-04    5.557e+00 2.394e-05
4.0  0.8  0.70    80.0    4.770e-05    4.017e+00 1.187e-05
5.0  1.0  1.50    60.0    4.813e-05    1.298e+01 3.709e-06
5.0  1.0  1.50   120.0    1.077e-05    9.595e+00 1.122e-06
```

## Reading

The probe checks the finite-height wall-tail estimate from E72.378 on a compact toy packet.  The
reported bound is intentionally crude: it uses sampled local modulus, sampled variation, and a large
absolute constant.

The observed wall error decreases as `T` increases.  The bound dominates the error, as expected, but
is far too loose to be a Phase 72 closure mechanism.  This supports the analytic reading of E72.378:

```text
ordinary BV/Dirichlet control is a certificate scaffold,
not the final Feshbach-Weil cancellation.
```

## Status

```text
validated: finite-height wall-tail bound has the correct qualitative behavior;
validated: crude BV bound is safe but much too weak;
proved in E72.378: wall-tail reduces to weighted regularity quantities;
open: prove WeightedWallRegularity for the actual Feshbach packet.
```
