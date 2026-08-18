# E77.5k - Moving-Boundary Four-Node Identity Audit

## Objective

E77.5j reduced the live endpoint to:

```text
BOUNDARY-SHELL-CELL:
  couple the insertion {-N-1,-N,N,N+1} with the boundary move N -> N+2.
```

E77.5k tests the natural common-core representation.  For the step
`N -> N+2`, set

```text
common core = {-N+2,...,N-2}.
```

Then the old section has active block

```text
{-N+1,N-1},
```

while the new section has active block

```text
{-N-1,-N,-N+1,N-1,N,N+1}.
```

Eliminating the common core gives the exact finite identity

```text
T(z)=t0(z)-tau(z) S^{-1}k.
```

The question is whether the associated common-core coordinate

```text
theta_common = tau S^{-1}k/t0
```

is the right object for the next cancellation theorem.

## Probe

Artifacts:

```text
E77_5k_moving_boundary_four_node_probe.py
E77_5k_moving_boundary_four_node_results.json
E77_5k_smoke_results.json
```

Main command:

```bash
python3 E77_5k_moving_boundary_four_node_probe.py --lambda 6 --max-modes 22 --dps 100 --output E77_5k_moving_boundary_four_node_results.json
```

The probe verifies the common-core Schur identity against the direct
transfer and compares

```text
Delta theta_common
```

with the shell-coordinate

```text
Delta theta_shell
```

from E77.5g.

## Certification Table

Max over `sigma in {0.55,0.6,0.75,1,1.5,2,3}`.

| build | step | old active | new active | max abs Delta common | max abs Delta shell | common/shell range | max identity error |
|---|---:|---|---|---:|---:|---:|---:|
| zeta | 8 -> 10 | [-7,7] | [-9,-8,-7,7,8,9] | 0.11350687 | 0.068445728 | 1.51448-1.91078 | 1.35e-77 |
| zeta | 10 -> 12 | [-9,9] | [-11,-10,-9,9,10,11] | 0.15749518 | 0.053619596 | 2.93007-3.15101 | 3.00e-72 |
| zeta | 12 -> 14 | [-11,11] | [-13,-12,-11,11,12,13] | 0.15034587 | 0.023515542 | 6.39347-6.85562 | 3.01e-68 |
| zeta | 14 -> 16 | [-13,13] | [-15,-14,-13,13,14,15] | 0.15184209 | 0.022835206 | 6.64947-6.86943 | 7.68e-64 |
| zeta | 16 -> 18 | [-15,15] | [-17,-16,-15,15,16,17] | 0.14171004 | 0.017264103 | 8.20836-8.44282 | 4.65e-60 |
| zeta | 18 -> 20 | [-17,17] | [-19,-18,-17,17,18,19] | 0.13341131 | 0.015438585 | 8.64142-8.79557 | 2.06e-56 |
| zeta | 20 -> 22 | [-19,19] | [-21,-20,-19,19,20,21] | 0.12456914 | 0.0067492443 | 18.4568-18.7561 | 4.26e-53 |
| planted | 8 -> 10 | [-7,7] | [-9,-8,-7,7,8,9] | 5.1570562 | 2.8023251 | 1.75756-1.92079 | 2.15e-101 |
| planted | 10 -> 12 | [-9,9] | [-11,-10,-9,9,10,11] | 47.824494 | 1.8421061 | 25.7192-26.2627 | 2.01e-100 |
| planted | 12 -> 14 | [-11,11] | [-13,-12,-11,11,12,13] | 23.835904 | 3.6679515 | 6.49842-6.52799 | 6.23e-101 |
| planted | 14 -> 16 | [-13,13] | [-15,-14,-13,13,14,15] | 4.3415027 | 7.2624973 | 0.597671-0.597993 | 2.08e-101 |
| planted | 16 -> 18 | [-15,15] | [-17,-16,-15,15,16,17] | 2.6426634 | 1.8386094 | 1.43557-1.43807 | 1.74e-101 |
| planted | 18 -> 20 | [-17,17] | [-19,-18,-17,17,18,19] | 4.7502038 | 1.9241482 | 2.46873-2.46883 | 5.55e-101 |
| planted | 20 -> 22 | [-19,19] | [-21,-20,-19,19,20,21] | 0.89917940 | 1.9757430 | 0.454544-0.455323 | 2.23e-101 |

## Reading

The common-core Schur identity is exact.  The max identity error is
`4.26e-53` for zeta and `2.23e-101` for planted.

But `theta_common` is not the invariant endpoint.  It depends strongly on
the chosen core/active split.  For zeta:

```text
|Delta theta_common| / |Delta theta_shell|
  grows from about 1.5--1.9 to about 18.5--18.8.
```

For planted it is also unstable, ranging from `0.45` to `26.3`.

Thus the moving-boundary/four-node identity is useful, but only at the
transfer or logarithmic-derivative level.  A proof phrased in
`theta_common` would be coordinate-dependent and would not match the
certified shell-coordinate Cauchy behavior from E77.5g.

## Autopsy

The attempted reduction

```text
BOUNDARY-SHELL-CELL via theta_common
```

fails.  The failure is not numerical instability: the transfer identities
hold to roundoff.  The failure is mathematical/coordinatization:
`theta = correction/t0` changes when the same transfer is represented with
a different eliminated core.

Therefore the next object must be partition-invariant:

```text
LOGT-CELL:
  derive the moving-boundary/four-node update for

    log T_N(i sigma) - log T_{N+2}(i sigma)

  or its safe derivative, before choosing a theta coordinate.
```

This preserves the actual SR-LOG endpoint and avoids a fake dependency on
Schur coordinates.

## Status

```text
proved:    exact common-core 2-node/6-node Schur identities;
refuted:   theta_common as the next closure coordinate;
observed:  the correct identity must be transfer/log-derivative invariant;
reduced:   BOUNDARY-SHELL-CELL -> LOGT-CELL;
next:      E77.5l should express the N -> N+2 safe log-derivative update
           directly from the common-core transfer identity.
```
