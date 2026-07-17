# E71.11 -- log-derivative background probe results

**Date:** 2026-07-07.
**Script:** `E71_11_logder_background_probe.py`.

## Output

The script compared `Xi'/Xi` on `[0.4,12]` with three finite CCM log derivatives:

```text
all      = log derivative of product over CCM roots
poleRel  = m_N'/m_N = P_N'/P_N - Q_N'/Q_N
sineDep  = d/ds log(sin(sL/2)m_N(s))
```

Result:

```text
grid: [0.4,12.0], 180 points; target max=9.194236e-01
   N  #roots   all_L2     poleRel_L2  sineDep_L2   all_sup    poleRel_sup sineDep_sup
  18      11  2.474e+01    7.497e+01   2.473e+01  8.644e+01    3.256e+02   8.667e+01
  40      20  1.589e+01    7.289e+01   1.593e+01  4.855e+01    3.322e+02   4.906e+01
```

## Verdict

The simple canonical backgrounds fail:

```text
background_N != pole mesh Q_N,
background_N != sine comb,
background_N != all-root product correction.
```

The finite `m_N` object has the right local roots, but its raw logarithmic derivative is dominated by
finite-section background/pole structure.

## Consequence

The next candidate cannot be a static background depending only on the pole mesh. It must use the
finite-section dynamics itself.

A natural zero-independent discriminator is **persistence in N**:

```text
zeta roots:      stable under finite-section refinement;
background roots: drift with N.
```

This does not prove RH, but it may identify the relative determinant's physical divisor without
centering contours at known zeros.
