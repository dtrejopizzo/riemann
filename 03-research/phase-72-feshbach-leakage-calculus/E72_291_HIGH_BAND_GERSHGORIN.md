# E72.291 -- High-band Gershgorin ceiling

**Purpose.** Reduce the high-band part of APCB to an explicit row-sum estimate.

E72.290 leaves the high-band ceiling:

```text
lambda_max(P_high Delta_arith P_high)_+ = O(L^2),
```

with `P_high` the mesh-frequency projection `|d|>=4`.

For the high block `H=P_high Delta_arith P_high`, Gershgorin gives the finite sufficient condition:

```text
lambda_max(H)
<= max_i sum_j |H_ij|.                                      (HG)
```

Therefore the high-band ceiling follows from the explicit row-sum bound:

```text
max_i sum_j |(P_high Delta_arith P_high)_ij| = O(L^2).       (H-GERSH)
```

This is a crude but non-spectral gate.  It avoids the full-line symbol floor and uses the compressed
high-band matrix directly.

## Probe

Run:

```text
python3 E72_291_high_band_gershgorin_probe.py
```

Output:

```text
E72.291 high-band Gershgorin probe
High block is |d|>=4. Gershgorin ceiling: lambda_max <= max_i sum_j |H_ij|.
lam L dim eig/L2 diagMax/L2 offRow/L2 absRow/L2 fro/L2
 16 5.545177   37 1.608840e-01 1.349013e-01 3.190013e-01 3.664654e-01 4.368457e-01
 24 6.356108   52 1.428188e-01 1.155583e-01 3.138475e-01 3.620481e-01 4.543219e-01
 32 6.931472   68 1.327391e-01 1.051874e-01 2.945819e-01 3.374529e-01 4.814414e-01
```

## Reading

The high-band top eigenvalue is about `0.13--0.16 L^2`.  The absolute row-sum ceiling is about
`0.34--0.37 L^2`, stable in the tested windows.

So the high-band APCB theorem can be replaced by the explicit non-spectral estimate:

```text
H-GERSH: max_i sum_j |H_ij| <= C L^2.
```

The next proof step is to bound those high-band rows from the closed formula for `Q_y(m,n)`, exploiting
the denominator `1/(n-m)` and the cutoff `|d|>=4`.
