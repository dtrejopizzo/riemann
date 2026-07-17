# E72.199 - Displacement resonance decomposition

## Purpose

E72.198 suggested grouping signed Green-words by their exact signed displacement

```text
Delta = sum_i eps_i log n_i,
```

or equivalently by the rational product

```text
R = prod_i n_i^(eps_i).
```

The resonant class is `R=1`. Non-resonant classes have `R!=1` and carry a net translation phase.

## Diagnostic

Script:

```text
E72_199_displacement_resonance_probe.py
```

Output:

```text
E72.199 signed displacement resonance probe
groups signed Green-words by exact product prod n^eps
lam block r groups total resonant nonres absTotal absNonres
  6     0 2     67 +1.894812e+00 +9.616206e-01 +9.331912e-01 2.320108e+00 1.358487e+00
  6     0 3    243 +7.412135e-01 -2.481187e-02 +7.660254e-01 9.731124e-01 9.483006e-01
  6     1 2    289 +7.233123e-01 +5.139401e-01 +2.093722e-01 1.584702e+00 1.070762e+00
  6     1 3   2336 -1.902974e-01 +0.000000e+00 -1.902974e-01 6.120327e-01 6.120327e-01
  8     0 2    123 +1.461278e+00 +8.907457e-01 +5.705327e-01 2.275711e+00 1.384965e+00
  8     0 3    591 +2.083292e-01 -2.367368e-02 +2.320029e-01 5.257407e-01 5.020670e-01
  8     1 2    719 +5.957448e-01 +5.236131e-01 +7.213167e-02 2.005691e+00 1.482078e+00
  8     1 3   9052 -3.593871e-02 +0.000000e+00 -3.593871e-02 7.348706e-01 7.348706e-01
 10     0 2    157 +1.381335e+00 +7.762291e-01 +6.051054e-01 1.883132e+00 1.106903e+00
 10     0 3    871 +3.086448e-01 -1.396165e-02 +3.226064e-01 5.080193e-01 4.940576e-01
 10     1 2   1349 +6.282831e-01 +4.846905e-01 +1.435926e-01 2.061908e+00 1.577218e+00
 10     1 3  23304 -1.300025e-01 +0.000000e+00 -1.300025e-01 6.953147e-01 6.953147e-01
```

## Reading

The even moment `r=2` has a large resonant component. This is expected: words can pair `+log n` with
`-log n`.

The odd moment `r=3` shows the decisive feature:

```text
high block: resonant = 0, total < 0.
```

So the sign in the high block is not a diagonal multiplicative resonance. It is a genuinely
non-resonant signed Green-word effect.

This rules out the simplest proof strategy:

```text
Keep only R=1 and bound R!=1 by absolute values.
```

That would miss the sign and reintroduce the incoherent ceiling.

## New target

The next theorem must estimate non-resonant displacement classes coherently. A plausible form is:

```text
For each fixed degree r and block j, the Green-word class sum

  C_j,r(R) = sum_{prod n_i^eps_i = R}
             Tr(A_{n_1}^{eps_1}...A_{n_r}^{eps_r})

has a sign/decay law as a function of log R.
```

The fixed certificate then becomes a finite combination of class sums `C_j,r(R)`. The proof should aim
for a displacement-kernel estimate, not a termwise prime-power estimate.

## Status

This is progress but not closure. It identifies the next mathematical object that can plausibly carry
the missing cancellation:

```text
signed non-resonant Green-word class sums.
```
