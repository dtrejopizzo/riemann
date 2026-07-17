# E72.377 Results - Wall Paley inversion

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_377_wall_paley_inversion_probe.py
```

## Output

```text
E72.377 wall Paley inversion probe
 L    c     T      u        wallCoeff         target            relErr
4.0  0.8   40.0   0.70 1.70491268e+00-1.08919320e-16j     1.70496074e+00  2.819e-05
4.0  0.8   60.0   2.20 2.49642468e+00-3.63569306e-16j     2.49666915e+00  9.792e-05
5.0  1.1   60.0   1.50 2.02743035e+00+3.60437412e-16j     2.02791512e+00  2.390e-04
5.0  1.1   80.0   4.20 1.37887599e+01+2.05890961e-15j     1.37911205e+01  1.712e-04
```

## Reading

The probe reconstructs

```text
e^(cu)f(u)
```

from the right-wall Fourier coefficient

```text
1/(2pi) int_{-T}^{T} F(c+it)e^(-itu)dt,
F(w)=int_{-L}^{L}e^(wt)f(t)dt.
```

The observed errors are finite-height and quadrature errors.  This certifies the normalization in
E72.377 and the natural cutoff:

```text
PrimeWall_{c,infty}
=sum_{n<=e^L} Lambda(n)n^(-1/2)B_z^M(log n).
```

## Status

```text
validated: right-wall Fourier inversion;
validated: infinite-height wall coefficient recovers the compact packet;
proved in E72.377: the infinite right-wall prime series collapses to n<=e^L;
open: quantitative finite-height wall-tail bound for the actual Phase 72 packet.
```
