# E72.381 Results - Local WWR derivative reduction

## Command

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_381_local_wwr_derivative_probe.py
```

## Output

```text
E72.381 local WWR derivative probe
 lam  dim    T     delta    Omega      derivInt    ratio    mass
   6   21   50.0 1.414e-01  2.350e+00   4.462e+00    0.527 1.116e+01
   8   25   70.0 1.195e-01  3.927e+00   6.609e+00    0.594 1.170e+01
  10   29   90.0 1.054e-01  5.321e+00   8.380e+00    0.635 7.222e+00
  12   33  110.0 9.535e-02  7.322e+00   1.256e+01    0.583 1.314e+01
```

## Reading

The table checks the finite inequality

```text
Omega_delta(z)
<= int_0^L |(B_z^M)'(r)|W_{L,delta}(r)dr
```

for the actual Phase 72 packet.  The ratio `Omega/derivInt` is safely below `1` in the tested
windows, as predicted by E72.381.

This confirms that the local part of WWR can be audited through a prime-windowed derivative integral
rather than a pointwise supremum over every prime cell.

## Status

```text
validated: local WWR derivative domination for the actual packet;
validated: the finite prime-window weight W_{L,delta} is computable and stable;
proved in E72.381: Omega_delta <= weighted derivative integral;
open: prove the weighted derivative integral is polynomial uniformly.
```
