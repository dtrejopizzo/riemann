# E71.9 -- relative arch/free background results

**Date:** 2026-07-07.
**Script:** `E71_9_relative_arch_background_probe.py`.

## Output

The test compared the all-root determinant and the relative determinant

```text
D_zeta^{all}(t) / D_arch^{all}(t)
```

on `[0,12]`, below the first zeta zero.

```text
grid: [0,12.0] below first zero, hmax=55
   N  #zeta #arch      all_relL2     rel_relL2    rel_relSup
  18     11     16   9.062859e+00  3.074798e+04  2.254756e+05
  40     20     21   1.318981e+00  2.313240e+01  1.681254e+02
```

The arch/free roots do not align with the zeta background roots. For example:

```text
N=40 zeta roots[:10] = 2.1756, 4.5757, 10.4222, 12.8360, 14.1347, ...
N=40 arch  roots[:10] = 3.7041, 15.8110, 18.3297, 20.7171, ...
```

Dividing by the arch/free product introduces poles or near-poles in the comparison window and makes
the approximation worse.

## Verdict

The finite-section background is **not** removed by the archimedean/free determinant alone.

Therefore:

```text
B_N != D_arch^{all}
```

for the desired relative determinant.

## Consequence

The correct normalization, if it exists, must be closer to a Fredholm/scattering determinant:

```text
det(I + trace-class perturbation of the CCM background),
```

not a quotient of two unrelated finite spectral products.

This is consistent with Phase 53:

- a boundary/scattering phase fitted from zeta would be circular;
- but a Fredholm determinant built directly from the finite Euler perturbation may still be a live
  CAND-1 object.

## Next target

Try the perturbation determinant at the matrix level:

```text
Delta_N(z) = det(I - (QW_zeta - QW_arch)(QW_arch - z)^{-1})
```

or the equivalent finite-dimensional relative determinant. This uses the finite operator pair rather
than independently dividing their spectral products.

The audit question will be whether its zeros are still real-rooted / Hurwitz-usable, or whether the
relative determinant becomes a complex scattering object whose phase reintroduces the Phase 53
boundary-condition wall.
