# E73.135 Results - Constrained Evaluation Gap

Date: 2026-07-12.

Script:

```text
E73_135_constrained_eval_gap.py
```

Purpose:

Test whether `ROW-KER` can be certified variationally by comparing the
ground energy with the ground energy restricted to one critical-evaluation
kernel:

```text
min_{v perp e_gamma, ||v||=1} <v,Hv> - lambda_0(H).
```

If this constrained gap were well-conditioned, it could give a spectral
route to

```text
|<xi,e_gamma>| small.
```

Output:

```text
E73.135 constrained critical-evaluation gap
For row e, compares min_{v perp e}<Hv>-mu with leak^2*gap.
 lam     L gamma      pRow     qNorm     gapB  cGapB predCostB ratio
  16   5.545   14.13    0.593    20.602  -20.295 -21.094   -61.499 huge
  20   5.991   14.13    0.611    19.580  -19.427 -19.864   -58.588 huge
  24   6.356   14.13    0.740    18.578  -18.293 -19.046   -55.450 huge
  28   6.664   14.13    2.599    22.443  -17.220 -18.374   -62.107 huge
```

## Reading

The constrained gap is not resolving the rowwise leak.  The predicted cost

```text
|<xi,e_gamma>|^2 * spectral_gap
```

is many powers smaller than the numerically resolved constrained energy.
This is because the low spectrum is extremely compressed; the variational
gap lives at a scale where finite precision and near-degeneracy dominate.

Thus the constrained-minimization route is not a useful certificate for
`ROW-KER` in the current finite harness.

## Consequence

Do not use

```text
min_{v perp e_gamma}<v,Hv> - lambda_0(H)
```

as the primary proof route for CSV.  It is too ill-conditioned.

The correct target remains the direct rowwise orthogonality:

```text
ROW-KER_17:
|<xi_L,e_gamma>| <= C L^{-17-p_gamma}.
```

This may still have a variational proof, but it must use the explicit
Euler/Gamma cell equation or a stable Feshbach quotient, not the raw
constrained gap of the full finite matrix.

