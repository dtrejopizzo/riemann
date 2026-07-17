# E73.258 - Transverse eigen-residual audit

## 1. Purpose

E73.257 shows that `Q_w eta=0` alone is far too weak.  The next possible
non-circular input is the eigenvector origin of

```text
eta=(I-P_w)xi_L.
```

This note tests whether that origin supplies an autonomous equation inside
`ker Q_w`, independent of the small Cauchy trace `h=Q_wxi_L`.

## 2. Exact identity

Let

```text
E=H_L-mu_L I,        P=P_w,        R=I-P,
xi=xi_L,             eta=Rxi.
```

Since `E xi=0`,

```text
R E eta = - R E Pxi.                              (1)
```

Thus `eta` is a transverse approximate eigenvector only to the extent that the
forcing term `R E Pxi` is small.

But `Pxi` is the Cauchy-plane lift of

```text
h=Q_wxi.
```

Therefore a proof of small transverse residual through (1) risks becoming the
same circular Cauchy-divisor argument already isolated in E73.188.

## 3. Numerical audit

The companion script measures:

```text
etaB       = log_L ||eta||,
hB         = log_L ||Qxi||,
PxiB       = log_L ||Pxi||,
transResB  = log_L ||R E eta||,
forceB     = log_L ||-R E Pxi||,
scalarMaxB = log_L max_a |q_aHeta|.
```

Representative output:

```text
 lam      L gamma etaB hB PxiB transResB forceB force/PxiB scalarMaxB scalar/transB
   8    4.159  14.13   0.00 -19.03  -17.93     -23.20  -23.20      -5.27     -21.46          1.74
  10    4.605  21.02   0.00 -14.40  -13.64     -15.83  -15.83      -2.19     -14.98          0.85
  12    4.970  14.13  -0.00 -19.10  -18.94     -21.75  -21.75      -2.81     -20.35          1.40
  16    5.545  21.02   0.00 -19.12  -19.72     -19.31  -20.90      -1.19     -18.18          1.12
  20    5.991  21.02   0.00 -18.50  -20.19     -18.32  -20.66      -0.47     -17.66          0.66
```

For the smaller stable cases, `transResB` and `forceB` agree, confirming (1).
For larger cases the floating eigen-residual `E xi` can dominate the exact
zero balance, so the equality is conditioning-limited.

## 4. Verdict

Rejected as an independent proof mechanism:

```text
TRANS-EIG-AUTO:
eta is intrinsically a small-residual eigenvector in ker Q_w, independently of
the Cauchy trace h=Q_wxi.
```

Kept:

```text
R E eta = -R E Pxi,
```

as an exact identity and diagnostic.

The identity does not evade the divisor variable.  `Pxi` is controlled by
`h=Q_wxi`, and using its smallness to prove `q_aHeta` small is the E73.188
circular branch.

## 5. Current minimal target

After E73.256--E73.258, the scalar theorem cannot be proved by:

```text
1. quotient projection cancellation;
2. Q_weta=0 / endpoint constraints alone;
3. autonomous transverse eigen-residual smallness.
```

The remaining non-circular statement is still the explicit model-prime
coefficient identity:

```text
EIGEN-KER-DIV / ETA-DIV:
sum_omega c_omega(eta_w)W_omega
+sum_omega l_omega(eta_w)V_omega
+E_exp
=O_M(L^-M),
```

where `eta_w=(I-P_w)xi_L` is the finite CCM ground vector component, and the
proof must use the explicit Gamma-prime construction of `H_L` rather than
only the abstract projection identities.

