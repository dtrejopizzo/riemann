# E72.360 results - log-derivative multiplicity audit

Command:

```text
python3 03-research/phase-72-feshbach-leakage-calculus/E72_360_logder_multiplicity_audit.py
```

The audit checks the correction in E72.360:

```text
Z'/Z with holomorphic tests sees only F(a), not higher Hermite coefficients.
```

For `Z=z^m`,

```text
Res F(z) Z'(z)/Z(z) dz = m F(0).
```

The `1/Z` principal part sees the full block

```text
F_0,...,F_{m-1}.
```

## Table

```text
m  case       logderRes        ppNorm       ppBlock
1  F          1.000000e+00     1.000000e+00 [1.+0.j]
1  G          1.000000e+00     1.000000e+00 [1.+0.j]
1  G-F        0.000000e+00     0.000000e+00 [0.+0.j]

2  F          2.000000e+00     1.000000e+00 [1.+0.j 0.+0.j]
2  G          2.000000e+00     3.201562e+00 [1.+0.j  3.-0.5j]
2  G-F        0.000000e+00     3.041381e+00 [0.+0.j  3.-0.5j]

3  F          3.000000e+00     1.000000e+00 [1.+0.j 0.+0.j 0.+0.j]
3  G          3.000000e+00     3.905125e+00 [ 1.+0.j   3.-0.5j -1.+2.j ]
3  G-F        0.000000e+00     3.774917e+00 [ 0.+0.j   3.-0.5j -1.+2.j ]

4  F          4.000000e+00     1.000000e+00 [1.+0.j 0.+0.j 0.+0.j 0.+0.j]
4  G          4.000000e+00     3.905125e+00 [ 1.+0.j   3.-0.5j -1.+2.j   0.+0.j ]
4  G-F        0.000000e+00     3.774917e+00 [ 0.+0.j   3.-0.5j -1.+2.j   0.+0.j ]
```

## Reading

For `m>1`, `F` and `G` have the same `logderRes` but different principal-part blocks.  Their
difference `G-F` is invisible to holomorphic `Z'/Z` tests while still having nonzero Hermite data.

Therefore:

```text
simple zeros:
  double Z'/Z contour identities are sufficient.

multiple zeros:
  use E72.359 principal-part projectors or meromorphic local dual tests.
```

This prevents a false Hermite proof from entering the Phase 72 chain.
