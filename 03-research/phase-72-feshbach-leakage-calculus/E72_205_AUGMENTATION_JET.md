# E72.205 - Augmentation character jet

## Purpose

E72.203 rejected a global character-torus norm proof with the fixed constants. This does not explain
whether the augmentation character `chi=1` is structurally special or merely accidental.

Here we compute the local character jet at the augmentation.

For one block, define

```text
A(t)=sum_n exp(it log n)A_n^+ + exp(-it log n)A_n^-.
```

Then

```text
A(0)=K,
A'(0)=i sum_n (log n)(A_n^+ - A_n^-),
A''(0)=-sum_n (log n)^2(A_n^+ + A_n^-).
```

These are exact finite matrices.

## Diagnostic

Script:

```text
E72_205_augmentation_jet_probe.py
```

It computes the first and second perturbative derivatives of the extreme eigenvalues of `A(t)` at
`t=0`, and checks them against finite differences.

Output:

```text
E72.205 augmentation character jet probe
eig=min/max at t=0; lambda1, lambda2 are perturbative derivatives
lam block eig lambda0 lambda1 lambda2 fd1 fd2 diag2 mix2
 12     0 min -0.393222 -5.69e-17 +1.453e+00 -1.67e-13 +1.453e+00 +1.453e+00 -2.585e-31
 12     0 max +0.438740 +5.58e-17 -2.327e+00 -2.78e-14 -2.327e+00 -2.327e+00 +1.905e-31
 12     1 min -0.445263 -1.52e-16 +7.636e+00 -2.22e-13 +7.636e+00 +7.636e+00 -6.955e-31
 12     1 max +0.239318 +2.07e-16 -1.941e+00 -8.33e-14 -1.941e+00 -1.941e+00 +1.975e-30
 16     0 min -0.353059 -1.15e-16 +1.557e+00 -8.33e-14 +1.557e+00 +1.557e+00 -3.378e-29
 16     0 max +0.399474 -8.20e-16 -2.612e+00 -8.33e-14 -2.612e+00 -2.612e+00 +2.034e-29
 16     1 min -0.437356 +1.23e-15 +8.924e+00 +1.39e-13 +8.924e+00 +8.924e+00 -1.151e-28
 16     1 max +0.218518 +2.30e-17 -1.991e+00 -2.78e-14 -1.991e+00 -1.991e+00 +6.705e-29
 20     0 min -0.339139 -3.04e-17 +1.768e+00 +2.22e-13 +1.768e+00 +1.768e+00 -3.577e-31
 20     0 max +0.356348 +2.58e-17 -2.598e+00 -2.78e-14 -2.598e+00 -2.598e+00 +2.422e-31
 20     1 min -0.448625 +1.86e-16 +1.020e+01 -2.78e-14 +1.020e+01 +1.020e+01 -2.237e-30
 20     1 max +0.182363 +7.40e-17 -2.086e+00 +5.55e-14 -2.086e+00 -2.086e+00 +8.016e-31
 24     0 min -0.318900 +2.95e-17 +1.986e+00 +5.55e-14 +1.986e+00 +1.986e+00 -1.211e-31
 24     0 max +0.348993 +4.51e-17 -3.178e+00 +2.78e-14 -3.178e+00 -3.178e+00 +2.083e-31
 24     1 min -0.508479 -7.75e-17 +1.402e+01 +0.00e+00 +1.402e+01 +1.402e+01 -6.331e-31
 24     1 max +0.192462 -7.54e-17 -2.309e+00 +0.00e+00 -2.309e+00 -2.309e+00 +7.162e-31
```

## Reading

At `t=0`:

```text
lambda'_extreme(0) = 0
```

to numerical precision. Moreover:

```text
lambda_min''(0) > 0,
lambda_max''(0) < 0.
```

Thus the augmentation is locally favorable: the negative extreme moves upward and the positive extreme
moves downward under infinitesimal character twists.

The global torus failure from E72.203 is therefore not an infinitesimal instability. It comes from
larger character twists that eventually create a deeper negative eigenvalue in the high block.

## Exact local identity

The vanishing of the first derivative has an exact reason. Since

```text
A_n^-=(A_n^+)^*,
A'(0)=i sum_n (log n)(A_n^+-(A_n^+)^*),
```

`A'(0)` is Hermitian but odd under the adjoint-pair symmetry. For the observed extreme eigenvectors,
the Rayleigh pairing with this odd channel vanishes:

```text
<v_ext,A'(0)v_ext>=0.
```

The second derivative is dominated here by the direct term

```text
<v_ext,A''(0)v_ext>,
```

with essentially zero mixing correction in the tested windows.

## Consequence

The proof should exploit an augmentation-local evenness principle:

```text
the augmentation character is a local norm well for the fixed blocks.
```

This is weaker than a global torus norm bound and compatible with E72.203.

The remaining theorem can now be sharpened:

```text
prove the fixed group-algebra trace inequalities at chi=1
using adjoint-pair evenness and path-sensitive Green-word sums,
not by controlling all chi_t.
```
