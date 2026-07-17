# E72.372 Results - Hyperbolic pair kernel

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_372_hyperbolic_pair_kernel_probe.py
```

## Output

```text
E72.372 hyperbolic pair-kernel probe
 L      z                  w                  relBracket      DnearErr    orientErr
 6.0  (0.25+1.4j)        (0.33+2.1j)           4.423e-16    1.524e-05    1.017e-15
 8.0  (-0.2+1.7j)        (0.41+3.2j)           6.546e-17    1.622e-05    9.798e-16
10.0  (0.15+2.3j)        (-0.37+1.9j)          6.921e-16    1.716e-05    3.030e-15
12.0  (0.3+1.2j)         (0.55+2.7j)           1.991e-15    7.537e-05    1.882e-15
```

## Reading

The direct bracket

```text
w(1+e^(zL))(1-e^(-wL))+z(1-e^(zL))(1+e^(-wL))
```

matches the hyperbolic Wronskian form

```text
4e^((z-w)L/2)
[w cosh(zL/2)sinh(wL/2)-z sinh(zL/2)cosh(wL/2)]
```

to roundoff.

The `DnearErr` column evaluates the entire divided-difference quotient close to the removable diagonal
`w=z` and compares it with the analytic derivative limit.  The errors are proportional to the finite
offset used in the probe, not to a structural singularity.

The `orientErr` column checks the corrected representative invariance:

```text
4e^((z-w)L/2)G(w)D_a(z,w)
=4e^((z+w)L/2)G(-w)D_a(z,-w),
```

for a test function satisfying `G(-w)=e^(-wL)G(w)`.  The error is roundoff-scale.

## Status

```text
validated: pair-kernel hyperbolic factorization;
validated: numerical behavior is consistent with removable diagonal singularities;
proved in E72.372: exact entire divided-difference kernel D_a(z,w);
open: use the entire kernel to prove the paired zero sampling bound HPAIR.
```
