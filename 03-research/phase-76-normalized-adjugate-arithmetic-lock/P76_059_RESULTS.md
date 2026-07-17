# P76.059 - Fixed-L boundary extrapolation

A quadratic fit in `1/N` using `N=10,...,15` gives fixed-`L` intercept errors
relative to the resolved prolate safe ratio:

```text
sigma=0.60: 0.515%
sigma=0.75: 0.351%
sigma=1.50: 0.963%
sigma=2.00: 2.185%
```

These are about 25% smaller than the `N=8,...,12` extrapolation, consistent
with continued convergence but not sufficient to prove that the intercept
equals the prolate value.  The result motivates a direct boundary-value
comparison rather than further numerical extrapolation.
