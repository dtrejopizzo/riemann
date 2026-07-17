# E72.380 Results - Actual packet WWR

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_380_actual_packet_wwr_probe.py
```

## Output

```text
E72.380 actual packet WWR probe
 lam  dim     z                  T    cells    errPrime    nearWeighted  crudeVar   mass
   6   21 (0.25+1j)             50     18   4.161e-12     7.961e+00  2.757e+01 1.116e+01
   8   25 (0.25+1j)             70     26   1.359e-11     1.176e+01  6.882e+01 1.170e+01
  10   29 (0.25+1j)             90     35   1.216e-10     1.443e+01  1.070e+02 7.222e+00
  12   33 (0.25+1j)            110     47   5.860e-11     2.086e+01  1.659e+02 1.314e+01
```

## Reading

This is the first WWR stress on the actual finite Feshbach packet

```text
B_z^M(y)=sum_{m,n}a_m(z)xi_nQ_y(m,n),
```

using the pole-even ground vector from the current Phase 71/72 build.

The finite-height prime-wall error is extremely small in this range.  The weighted local scale is
moderate, while the crude right-wall variation is already much larger.  This is the expected
signature of E72.379:

```text
sum first with Lambda(n)n^(-1/2-c),
then estimate;
do not estimate Var(e^(ct)B) directly.
```

## Status

```text
validated: WWR quantities are computable for the actual packet;
validated: actual-packet finite-height prime-wall error is tiny in tested windows;
validated: weighted local scale is much smaller than crude wall variation;
open: prove the WWR bounds analytically and uniformly.
```
