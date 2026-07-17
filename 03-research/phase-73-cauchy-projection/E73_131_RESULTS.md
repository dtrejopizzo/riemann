# E73.131 Results - First-Order Eigenvector Perturbation Fails

Date: 2026-07-12.

Script:

```text
E73_131_eigenvector_perturbation_csv.py
```

Purpose:

Test whether the CSV cancellation from E73.130 is explained by first-order
perturbation of the arch/free ground vector under the prime perturbation:

```text
delta xi
 ?=
 - (A_arch-mu_arch I)^{-1}_{perp} (A_zeta-A_arch) xi_arch.
```

If true, CSV would be a response-linear identity.

Output:

```text
E73.131 eigenvector perturbation CSV probe
Tests first-order arch resolvent prediction for delta xi and C_delta.
 lam     L gamma     archB trueDelB predDelB  errDelB zetaPredB
  16   5.545   14.13   -1.372   -4.191   -2.825   -2.772     -1.326
  16   5.545   21.02   -0.326   -3.145   -0.933   -0.946     -0.581
  20   5.991   14.13   -1.838   -3.840   -2.013   -1.993     -1.532
  20   5.991   21.02   -0.195   -2.197   -0.953   -1.017     -0.362
  24   6.356   14.13   -1.116   -2.555   -2.868   -2.314     -1.095
  24   6.356   21.02   -0.475   -1.914   -1.367   -1.612     -0.591
  28   6.664   14.13    1.215   -0.170    0.473    0.288      1.067
  28   6.664   21.02   -0.546   -1.930   -1.437   -1.699     -0.653
```

## Reading

The first-order arch response does not predict the CSV cancellation.

The predicted zeta channel

```text
C_arch + C_pred_delta
```

remains around arch scale, not CSV scale:

```text
zetaPredB ~ L^-1 or worse,
```

where the true zeta value is around

```text
L^-17.
```

Therefore the prime perturbation is not a small linear correction of the
arch/free ground vector in the scalar CSV channel.  It reorients the ground
vector non-perturbatively relative to the critical evaluation rows.

## Consequence

Do not base CSV on first-order perturbation around the arch/free model.

The correct finite theorem must use the full zeta-coupled eigenvector,
probably as a constrained minimizer:

```text
xi_zeta = argmin <v,C_E v>,
```

and prove that this minimizer lies almost in the intersection of the
critical evaluation kernels:

```text
<xi_zeta,k_gamma> ~= 0
```

for the Phase 73 critical rows.

This suggests the next target:

```text
Critical Evaluation Kernel Theorem:
the zeta-coupled ground vector is asymptotically contained in
ker Ev_gamma for all natural-height critical rows.
```

Unlike the failed arch perturbation, this uses the full coupled matrix and
does not linearize away the arithmetic effect.

