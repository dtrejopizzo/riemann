# E72.392 results - tail absorbed into zero-node system

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_392_tail_kernel_probe.py
```

## Output

```text
E72.392 tail kernel scale probe
   L      M       |T|/e^(aL)    scaled=M^2/L^2
  8.0     23      1.990e-04      1.645e-03
  8.0     34      6.215e-05      1.123e-03
  8.0     46      2.527e-05      8.354e-04
 10.0     32      1.526e-04      1.562e-03
 10.0     48      4.544e-05      1.047e-03
 10.0     64      1.925e-05      7.886e-04
 12.0     42      1.196e-04      1.465e-03
 12.0     63      3.554e-05      9.796e-04
 12.0     84      1.504e-05      7.368e-04
 16.0     64      8.114e-05      1.298e-03
 16.0     96      2.407e-05      8.664e-04
 16.0    128      1.017e-05      6.508e-04
 20.0     90      5.693e-05      1.153e-03
 20.0    135      1.687e-05      7.687e-04
 20.0    179      7.244e-06      5.802e-04
```

## Interpretation

The tested quantity is the tail matrix coefficient

```text
T^M_{z,w}=2iwR_M(z,w)/L.
```

After removing the leading exponential `e^(Re z L)`, E72.392 predicts

```text
|T^M_{z,w}|/e^(Re z L) <= C_K L^2/M^2.
```

The column

```text
(|T|/e^(Re z L)) M^2/L^2
```

stays around `10^-3` and decreases mildly across the tested range.  This supports the perturbative
tail estimate used in the theorem.

## Status

```text
verified: rational tail kernel has the predicted L^2/M^2 relative scale;
proved: tail is perturbative for M >= L^(1+epsilon);
remaining: outside-window zero contribution and nodal-to-strip propagation.
```

