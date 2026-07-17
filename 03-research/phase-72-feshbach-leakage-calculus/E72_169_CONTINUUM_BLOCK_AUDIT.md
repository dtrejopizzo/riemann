# E72.169 -- Continuum block audit

**Date:** 2026-07-09.
**Role:** test whether `BSE` can be proved by replacing the prime block with its PNT continuum
counterpart.

## 0. Continuum candidate

For a prime-position interval `I`, the prime block is:

```text
K_I^prime = relative whitening of -sum_{log n in I} Lambda(n)n^{-1/2}Q(log n).
```

The first continuum approximation suggested by PNT is:

```text
K_I^cont = relative whitening of -int_I exp(y/2)Q(y)dy.
```

If:

```text
K_I^prime-K_I^cont
```

were small in Hilbert-Schmidt norm, the proof of `BSE` could be reduced to an explicit overlap
operator plus a PNT discrepancy estimate.

## 1. Diagnostic output

The companion script:

```text
E72_169_continuum_block_probe.py
```

reports:

```text
E72.169 continuum block comparison
continuum block = -int_I exp(y/2) Q_y dy, cut=0.60
 lam    L block  ||Kp-Kc||  Eprime   Econt  Hcont  Scont/H
   6  3.58    K0      1.083    0.659   0.272  0.561    0.134
   6  3.58    K1      0.533    0.545   0.373  0.441   -0.632
   8  4.16    K0      1.035    0.641   0.240  0.381   -0.185
   8  4.16    K1      0.588    0.384   0.161  0.226   -0.320
  10  4.61    K0      0.998    0.515   0.176  0.377    0.172
  10  4.61    K1      0.474    0.461   0.312  0.376   -0.597
  12  4.97    K0      0.951    0.565   0.267  0.378   -0.357
  12  4.97    K1      0.453    0.333   0.221  0.280   -0.500
  14  5.28    K0      0.914    0.511   0.246  0.362   -0.295
  14  5.28    K1      0.415    0.332   0.232  0.288   -0.539
  16  5.55    K0      0.857    0.457   0.219  0.333   -0.244
  16  5.55    K1      0.423    0.337   0.227  0.279   -0.557
  18  5.78    K0      0.845    0.447   0.202  0.238   -0.667
  18  5.78    K1      0.413    0.213   0.138  0.187   -0.382
  20  5.99    K0      0.812    0.403   0.192  0.286   -0.277
  20  5.99    K1      0.415    0.332   0.227  0.264   -0.665
```

## 2. Reading

The continuum block has the right qualitative scale but not the prime block itself. The discrepancy
`||Kp-Kc||_HS` remains large in the tested windows. Therefore the proof of `BSE` cannot be obtained by
simply replacing the prime-power measure with the continuous PNT density and treating the remainder as
small.

This is consistent with the half-power warning from E72.49/E72.53: the endpoint/relative whitening
amplifies arithmetic discreteness enough that the naive continuum replacement is not a closed proof.

## 3. Consequence

The surviving target is the exact discrete trace-functional estimate:

```text
E_0(K_0^prime)+E_1(K_1^prime)+cross_+ <= 1-epsilon.
```

The continuum operator may still serve as a comparison background, but it is not by itself the proof.
The discrete von Mangoldt block must remain inside the main estimate.
