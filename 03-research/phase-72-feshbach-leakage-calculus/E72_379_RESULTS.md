# E72.379 Results - Weighted wall quadrature

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_379_weighted_wall_quadrature_probe.py
```

## Output

```text
E72.379 weighted wall quadrature probe
 L    c     T       errPrime      nearWeighted    crudeVar      mass
4.0  0.8    40.0    9.574e-05     1.183e+00   3.433e+00 1.741e+00
4.0  1.2    40.0    6.219e-05     1.416e+00   7.124e+00 1.741e+00
5.0  0.8    60.0    1.225e-05     1.493e+00   5.020e+00 2.862e+00
5.0  1.2    60.0    9.293e-06     1.830e+00   1.326e+01 2.862e+00
```

## Reading

The probe compares:

```text
errPrime:
actual finite-height prime wall quadrature error;

nearWeighted:
the local weighted modulus scale from E72.379;

crudeVar:
the global variation of e^(ct)B(t).
```

As `c` grows, `crudeVar` grows much faster than the weighted local scale.  This is the numerical
signature of the cancellation

```text
n^(-1/2-c)e^(c log n)=n^(-1/2).
```

The test is a toy-packet certification, not a proof for the actual Feshbach packet.  It validates the
architecture of E72.379: sum with the prime weights first, then estimate.

## Status

```text
validated: weighted wall quadrature avoids the crude right-wall variation ceiling;
validated: the local wall gauge cancellation is visible numerically;
proved in E72.379: exact finite quadrature defect identity;
open: prove WWR for the actual Feshbach packet B_z^M.
```
