# E72.232 - Low-edge subspace

## Purpose

E72.231 identified the low Fourier modes `m=0,1` as the dominant carrier of the high-block negative
eigenvalue. This probe tests the Rayleigh minimum restricted to explicit subspaces:

```text
P01    = span_Q{0,1},
P01E   = span_Q{0,1,N},
P01EE  = span_Q{0,1,N-1,N}.
```

Here `span_Q` means even Fourier modes projected off the model ground state and represented in the
compressed `bq` coordinates.

## Diagnostic

Script:

```text
E72_232_low_edge_subspace_probe.py
```

Output:

```text
E72.232 low-edge subspace Rayleigh probe
High block A_1; subspaces are Q-projected even Fourier modes.
lam fullMin min01 ratio01 min01E ratio01E min01EE ratio01EE
 12 -2.226316e-01 -2.166748e-01 0.973 -2.180901e-01 0.980 -2.193710e-01 0.985
 16 -2.186781e-01 -2.163538e-01 0.989 -2.167684e-01 0.991 -2.170493e-01 0.993
 20 -2.243125e-01 -2.215981e-01 0.988 -2.216522e-01 0.988 -2.216621e-01 0.988
 24 -2.542393e-01 -2.519621e-01 0.991 -2.519626e-01 0.991 -2.519627e-01 0.991
 28 -2.409324e-01 -2.391790e-01 0.993 -2.391795e-01 0.993 -2.391933e-01 0.993
 32 -1.368453e-01 -1.270259e-01 0.928 -1.286056e-01 0.940 -1.286363e-01 0.940
```

## Reading

The two-dimensional explicit subspace `P01` captures most of the negative edge:

```text
min(P01 A_1 P01) / min(A_1) = 0.928 to 0.993.
```

Adding the endpoint mode improves only slightly. The correct min-max input is therefore the explicit
`2x2` low block, not a hidden eigenvector.

## New sublemma

Define `P_L=span_Q{0,1}`. Prove a uniform low-block negative edge:

```text
lambda_min(P_L A_1 P_L) <= -alpha_L,
```

with `alpha_L` large enough to dominate the positive cubic tail.
