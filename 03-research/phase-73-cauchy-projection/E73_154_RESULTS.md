# E73.154 Results - Cauchy-plane action

Date: 2026-07-12.

Script:

```text
E73_154_cauchy_plane_action_probe.py
```

Purpose:

Project the rows

```text
q_w H_L,   q_-w H_L
```

onto the Cauchy plane

```text
span{q_w,q_-w}
```

and measure the residual both in row norm and after evaluation on the ground
eigenvector `xi_L`.

## Representative output

```text
 lam     L gamma row   resB  evalB     hB    invB    |a|B    |b|B  eigRel
  16   5.545   14.13   0 -2.310 -19.242 -19.921  -0.983   0.991  -1.517  1.0e+00
  16   5.545   25.01   0 -0.052 -14.252 -13.443   0.654  -0.649  -3.409  1.0e+00
  20   5.991   21.02   0 -1.516 -17.663 -18.303  -1.002   1.004  -2.107  1.0e+00
  24   6.356   25.01   0 -1.888 -18.857 -19.540  -0.981   0.990  -1.237  1.0e+00
  28   6.664   14.13   0 -1.570 -16.306 -16.815  -1.001   1.002  -2.438  1.0e+00
  32   6.931   14.13   0 -1.499 -17.170 -18.074  -0.998   0.999  -2.204  1.0e+00
```

Here:

```text
resB  = log_L(||rho||/||qH||),
evalB = log_L(|rho xi|),
hB    = log_L(|H_0(w)|+|H_0(-w)|).
invB  = log_L(||(mu I-A(w))^-1||).
```

## Reading

The Cauchy plane is not almost invariant in norm.  The relative residual is
only around

```text
L^-1 to L^-2,
```

with a low-scale failure near `lambda=16,gamma=25.01`.

But the residual evaluated on the ground eigenvector is much smaller and
tracks the desired Cauchy-divisor scale.  This gives the finite identity:

```text
(mu I-A(w)) h = rho(w)xi_L.
```

Thus the next possible proof target is:

```text
CPINV + RCE_17,
```

not norm-invariance of the Cauchy plane.

The inverse exponent is favorable in the stable rows:

```text
invB ~= -1.
```

Thus the Cauchy-plane system does not appear to amplify the residual; it
usually gains one power of `L`.  The low-scale outlier
`lambda=16,gamma=25.01` has `invB=0.654`, matching the known finite/base
failure rather than a new asymptotic obstruction.

## Caveat

The displayed `eigRel` is not the diagnostic quantity; both sides of
`qH xi=mu qxi` are tiny, so relative error is ill-conditioned.  The useful
quantities are `evalB`, `hB`, and the condition of `mu I-A(w)` in the next
probe.
