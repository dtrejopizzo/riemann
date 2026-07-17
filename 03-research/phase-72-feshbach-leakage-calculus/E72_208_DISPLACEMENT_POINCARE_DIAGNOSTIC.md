# E72.208 - Displacement Poincare diagnostic

## Purpose

E72.207 converts the second character derivative into a displacement-square weighted trace sum. The
next possible bridge back to the augmentation certificate is a Poincare-type relation between:

```text
M_0 = sum_words Tr(word),
M_2 = sum_words Delta(word)^2 Tr(word).
```

If the non-resonant part had a stable effective displacement gap, one could hope to control `M_0` by
`M_2`.

## Diagnostic

Script:

```text
E72_208_displacement_poincare_probe.py
```

It reports:

```text
res0     resonant part Delta=0,
non0     non-resonant q=0 sum,
non2     non-resonant q=1 sum,
minD     smallest nonzero displacement,
effGap   sqrt(non2/non0) when the ratio is positive,
absRatio sum |non-resonant word traces| / |non0|.
```

Output:

```text
E72.208 displacement Poincare diagnostic
m0=sum Tr(word), m2=sum Delta^2 Tr(word)
lam block r m0 m2 res0 non0 non2 minD effGap absRatio
  6     0 2 +1.894812e+00 +8.511697e+00 +9.616206e-01 +9.331912e-01 +8.511697e+00 0.134 3.020 1.46
  6     0 3 +7.412135e-01 +5.486214e+00 -2.481187e-02 +7.660254e-01 +5.486214e+00 0.118 2.676 1.24
  6     1 2 +7.233123e-01 +1.048778e+01 +5.139401e-01 +2.093722e-01 +1.048778e+01 0.032 7.078 5.11
  6     1 3 -1.902974e-01 -4.796595e+00 +0.000000e+00 -1.902974e-01 -4.796595e+00 0.929 5.021 3.22
  8     0 2 +1.461278e+00 +8.518666e+00 +8.907457e-01 +5.705327e-01 +8.518666e+00 0.118 3.864 2.43
  8     0 3 +2.083292e-01 +2.127323e+00 -2.367368e-02 +2.320029e-01 +2.127323e+00 0.087 3.028 2.16
  8     1 2 +5.957448e-01 +1.045802e+01 +5.236131e-01 +7.213167e-02 +1.045802e+01 0.032 12.041 20.55
  8     1 3 -3.593871e-02 -1.555043e+00 +0.000000e+00 -3.593871e-02 -1.555043e+00 0.971 6.578 20.45
 10     0 2 +1.381335e+00 +9.639026e+00 +7.762291e-01 +6.051054e-01 +9.639026e+00 0.118 3.991 1.83
 10     0 3 +3.086448e-01 +3.579223e+00 -1.396165e-02 +3.226064e-01 +3.579223e+00 0.074 3.331 1.53
 10     1 2 +6.282831e-01 +1.402470e+01 +4.846905e-01 +1.435926e-01 +1.402470e+01 0.024 9.883 10.98
 10     1 3 -1.300025e-01 -5.611541e+00 +0.000000e+00 -1.300025e-01 -5.611541e+00 0.970 6.570 5.35
 12     0 2 +1.282124e+00 +1.076726e+01 +7.506459e-01 +5.314786e-01 +1.076726e+01 0.061 4.501 2.29
 12     0 3 +1.439786e-01 +1.978562e+00 -1.079366e-02 +1.547723e-01 +1.978562e+00 0.051 3.575 2.48
 12     1 2 +4.679419e-01 +1.319644e+01 +3.723544e-01 +9.558749e-02 +1.319644e+01 0.008 11.750 15.80
 12     1 3 -7.561881e-02 -4.224922e+00 +0.000000e+00 -7.561881e-02 -4.224922e+00 1.337 7.475 9.14
```

## Reading

The high-block cubic channel is clean:

```text
res0 = 0,
non0 < 0,
non2 < 0,
effGap ~= 5--7.5.
```

This is a strong candidate for a non-resonant displacement Poincare inequality.

The even high-block moment is not clean in the same way:

```text
res0 is large,
minD can be tiny,
absRatio can be large.
```

Therefore a naive minimum-gap Poincare inequality cannot prove the whole fixed certificate. The proof
must separate:

```text
resonant even energy,
non-resonant even leakage,
non-resonant odd sign.
```

## Updated theorem shape

The fixed group-algebra certificate should be attacked by three sub-lemmas:

```text
1. Resonant even energy bound:
   control Delta=0 contributions in NTC/LM8.

2. Non-resonant displacement Poincare:
   control q=0 non-resonant sums by q=1 displacement-square sums where the effective gap is stable.

3. High-block odd sign:
   prove the non-resonant cubic sign that feeds XNEG and the signed residual polynomial.
```

This is more structured than the previous single displacement-moment problem.
