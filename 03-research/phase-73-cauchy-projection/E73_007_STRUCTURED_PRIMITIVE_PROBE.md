# E73.007 - Structured primitive probe

## 1. Purpose

E73.006 asks for an explicit primitive `Y_b` in a rational/divided-difference class such that

```text
(C_E-mu I)Y_b = S_b - R_b.
```

This note tests a finite candidate class:

```text
DD_L(-gamma,d)/(d^2+beta^2)^r,
```

where `gamma` runs through critical nodes, `beta` through off-line projection nodes, and
`1<=r<=p`.

This is not a free fit over the whole mesh.  It is a small explicit `RAT-DD` class tied to the
Cauchy-projection geometry.

## 2. Diagnostic

For each source `S_b`, solve least squares in the image of the structured class:

```text
min_Y ||(C_E-mu I)Y-S_b||.
```

Report:

```text
relDef = ||S_b-(C_E-mu I)Y||/||S_b||,
eigDef = |<xi,S_b-(C_E-mu I)Y>|,
expEig = e^(Re b L)eigDef.
```

Since `<xi,(C_E-mu I)Y>=0`, `eigDef` is exactly `|<xi,S_b>|`; the probe checks whether the
non-eigenline part is genuinely captured by the structured class.

## 3. Status

Results are recorded in `E73_007_RESULTS.md`.

