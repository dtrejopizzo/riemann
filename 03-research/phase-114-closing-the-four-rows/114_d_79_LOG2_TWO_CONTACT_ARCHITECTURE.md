# D.79 — The `T=log(2)` two-contact endpoint: exact mesh and diagnostic gate

This note records a rigorous architectural reduction and a deliberately
non-rigorous spectral selection diagnostic.  It is **not** an endpoint
positivity certificate.

Put `a=log(2)`, `b=log(3)`, `d=2a-b`, and `e=2b-3a`.  At `T=a` the active
positive-measure contacts are precisely the translations by `a` and `b`;
the translation by `log(4)=2T` has null overlap.  Partition `[-a,a]` at

```
-a, a-b, b-2a, 0, 2a-b, b-a, a.
```

The macro lengths are `d,e,d,d,e,d`.  Translation by `a` maps macros
`1->4`, `2->5`, and `3->6`, while translation by `b` maps `1->6`, including
both endpoints.  Consequently, subdividing the four `d`-macros into the
same number of cells and the two `e`-macros into the same number makes the
piecewise-polynomial projector commute *exactly* with both contact shifts.
There is no almost-alignment estimate and no sampled assertion here.  The
free-vector-space verification is executable in
`114_d_79_log2_shift_mesh_check.py`.

For selection we used 20 cells in every `d`-macro, 8 in every `e`-macro,
and Legendre degrees 0 through 9.  Thus the complete lower space has
dimension 960 and each parity block dimension 480.  The local diagonal
resolvents were evaluated with the same polynomial ODE formula as D.77;
only the final eigenvalue selection was floating point.

With moment penalty `rho=1000`, the observed lowest projected eigenvalues
and the rigorous D.76 scalar-tail lower bounds were:

| Gamma depth | projected even | D.76 even tail | sum | projected odd | D.76 odd tail | sum |
|---:|---:|---:|---:|---:|---:|---:|
| 40 | -9.94082e-3 | 2.573943e-3 | -7.36688e-3 | -6.50400e-3 | 1.525061e-3 | -4.97894e-3 |
| 80 | -1.659494e-3 | 6.871597e-4 | -9.72335e-4 | -1.60784e-3 | 3.913435e-4 | -1.21650e-3 |
| 160 | -2.964055e-4 | 1.780429e-4 | -1.18363e-4 | -3.766127e-4 | 9.907769e-5 | -2.77535e-4 |
| 320 | -7.058276e-5 | 4.534586e-5 | -2.52369e-5 | -8.578955e-5 | 2.492325e-5 | -6.08663e-5 |

Increasing the diagnostic penalty from `10^3` to `10^6` at depth 160
changed neither lowest eigenvalue at the displayed precision.  Hence the
remaining deficit is not the finite-penalty moment direction.  In
particular, no large Arb run at depth 320 is justified by these data.

The next proof obligation is a **coupled Gamma-tail/Feshbach bound** which
retains the action of the tail on the lower eigenspace.  The universal
scalar Robin lower bound of D.76 discards too much directional information
at this endpoint.  Any future certificate must also keep the full-space
moment cancellation: restricting only the projected lower block to its
moment kernel would be insufficient because lower and high moment
components may cancel.

## Operator-valued tail lower bound

This obligation has an elementary global resolution at the architectural
level.  If

```
E_b = (2/b) I - K_b,
```

then on the Fourier side its multiplier is

```
2 xi^2 / (b (b^2+xi^2)).
```

Consequently, for `b>=B`,

```
E_b >= (B/b)^3 E_B.
```

Indeed, the ratio of the two multipliers is
`B(B^2+x)/(b(b^2+x))`, with `x=xi^2`, and its derivative has the
nonnegative sign of `b^2-B^2`; its minimum is therefore the value
`B^3/b^3` at zero.  For every finite consecutive block `J` beginning at
`B`, this proves the full-space operator inequality

```
sum_{b in J} E_b >= (sum_{b in J} (B/b)^3) E_B.
```

It is important that this is an inequality on the complete Hilbert space,
not an insertion into the projected block.  Hence it has no omitted
`P--Q` cross term and is compatible with the exact moment penalty.

At depth 160, partitioning each of the first eight dyadic octaves of the
tail into four consecutive equal subblocks initially produced the floating
numbers

```
even  > 3.04909271e-4,
odd   > 2.92209247e-4
```

for the projected lower matrices.  **This diagnostic is rejected.**  Its
largest anchors have `b` of order `10^5`; taking midpoints after the local
ODE formula has cancelled exponentially large terms is numerically
unstable.  Moderate-frequency recomputations do not reproduce the even
margin: one subdivided octave plus an operator tail anchor gives about
`7.14e-8`, two subdivided octaves give about `7.69e-8`, and a two-anchor
Loewner interpolation gives about `6.52e-8`.  Thus `3.05e-4` must not be
used as selection evidence, much less as a directed claim.

The valid conclusion is only the operator inequality itself.  The even
channel is near-tangent and requires a capacity/factorisation argument
with cancellation handled before numerical evaluation.

## Capacity diagnostics

For the odd low mode of the depth-160 projected block, a zero-padded FFT
evaluation of the exact tail multiplier

```
r_N(tau) = Re(psi(N+1/4+i tau/2)-psi(N+1/4))
```

gave `1/<v,R_tail^{-1}v> = 2.83130e-4`, against a base deficit
`3.76613e-4`; a single rank-one capacity is insufficient.  After splitting
`R_tail=(B/4)E_B+R_B`, the odd projected base is already positive by
`8.13856e-6`.

For the even low mode of that split, write
`v=alpha cosh(x/2)+w`, with integral of `w` zero.  The full-space moment
regularisation gives the variational denominator

```
<w,R_B^{-1}w> + alpha^2/(2 rho).
```

The stable floating values were `alpha=-0.00663635`,
`<w,R_B^{-1}w>=880673.104`, and capacity `1.13550e-6`.  The projected base
deficit is `1.74647e-6`, leaving `-6.11e-7`; this rank-one regularisation is
also insufficient by itself.  These figures are diagnostics, not interval
certificates.

The reproducible directed audit
`114_d_79_stable_projected_tangency_verify.py` uses the elementary
coefficient `B/4+1/2=80.625` and proves only
`lambda_min(projected)>-1e-7`.  It stops before the high-space/Feshbach
step by design.  A floating profile using the nearly optimal coefficient
gave lowest even value `-8.06e-9`, moment against `cosh(x/2)` below
`3e-10`, and ordinary mean about `-9.39e-3`.  Thus the near-null vector is
already primitive to numerical precision; increasing the moment penalty
cannot remove the tangency.
