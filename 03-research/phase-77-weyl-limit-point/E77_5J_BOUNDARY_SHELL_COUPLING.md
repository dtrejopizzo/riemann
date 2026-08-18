# E77.5j - Boundary/Shell Coupling Audit

## Objective

E77.5i proved that the zeta Schur cocycle is genuinely ternary:

```text
Delta theta = A+B+C
```

cannot be reduced to a factor bound or a two-term pair cancellation.  The
next possible simplification is geometric: is `N -> N+2` a pure shell
update?

E77.5j checks the actual section geometry.

## Geometry

For central sections,

```text
N=8:  inner = {-7,...,7},   boundary = 8
N=10: inner = {-9,...,9},   boundary = 10
```

Thus `N -> N+2` does not merely add an exterior pair.  It performs the
coupled move:

```text
boundary N moves to boundary N+2;
old boundary N enters the interior;
old left boundary -N enters the interior;
two new shell nodes -N-1 and N+1 also enter.
```

Equivalently, the new interior nodes are:

```text
[-N-1, -N, N, N+1].
```

Therefore the next cell identity must couple boundary migration with shell
insertion.

## Probe

Artifacts:

```text
E77_5j_boundary_shell_coupling_probe.py
E77_5j_boundary_shell_coupling_results.json
E77_5j_smoke_results.json
```

Main command:

```bash
python3 E77_5j_boundary_shell_coupling_probe.py --lambda 6 --max-modes 22 --dps 100 --output E77_5j_boundary_shell_coupling_results.json
```

The probe measures:

```text
|theta_N-theta_{N+2}|,
|1/(z-d_N)-1/(z-d_{N+2})|,
boundary-pole-shift / |Delta theta|.
```

This is not used as a proof estimate; it audits whether boundary migration
is negligible or an active part of the signed cocycle.

## Certification Table

Max over `sigma in {0.55,0.6,0.75,1,1.5,2,3}` for `Delta theta`; range over
the same sigmas for `pole/delta`.

| build | step | entered inner nodes | max abs Delta theta | pole/delta range |
|---|---:|---|---:|---:|
| zeta | 8 -> 10 | [-9,-8,8,9] | 0.068445728 | 0.208054-0.231356 |
| zeta | 10 -> 12 | [-11,-10,10,11] | 0.053619596 | 0.177130-0.185577 |
| zeta | 12 -> 14 | [-13,-12,12,13] | 0.023515542 | 0.288561-0.306070 |
| zeta | 14 -> 16 | [-15,-14,14,15] | 0.022835206 | 0.222902-0.228960 |
| zeta | 16 -> 18 | [-17,-16,16,17] | 0.017264103 | 0.229337-0.235073 |
| zeta | 18 -> 20 | [-19,-18,18,19] | 0.015438585 | 0.205178-0.208286 |
| zeta | 20 -> 22 | [-21,-20,20,21] | 0.0067492443 | 0.384021-0.389467 |
| planted | 8 -> 10 | [-9,-8,8,9] | 2.8023251 | 0.00508164-0.00520675 |
| planted | 10 -> 12 | [-11,-10,10,11] | 1.8421061 | 0.00512496-0.00521561 |
| planted | 12 -> 14 | [-13,-12,12,13] | 3.6679515 | 0.00183107-0.00184999 |
| planted | 14 -> 16 | [-15,-14,14,15] | 7.2624973 | 0.000692828-0.000700863 |
| planted | 16 -> 18 | [-17,-16,16,17] | 1.8386094 | 0.00213346-0.00215343 |
| planted | 18 -> 20 | [-19,-18,18,19] | 1.9241482 | 0.00163422-0.00164626 |
| planted | 20 -> 22 | [-21,-20,20,21] | 1.9757430 | 0.00130403-0.00131183 |

## Reading

For zeta, the raw boundary pole shift is a visible fraction of
`Delta theta`:

```text
0.177 <= pole-shift / |Delta theta| <= 0.389.
```

It is not the whole cocycle, but it is too large to discard before
cancellation.

For the planted falsifier, the same boundary migration is tiny relative to
the O(1) Schur instability:

```text
0.00069 <= pole-shift / |Delta theta| <= 0.00522.
```

Thus the zeta mechanism is a coupled boundary/shell cancellation, while
the planted build is dominated by an off-line instability not explained by
the mesh boundary migration.

## Reduced Target

`TERNARY-CELL-CANCEL` is sharpened to:

```text
BOUNDARY-SHELL-CELL:
  derive theta_N-theta_{N+2} from the one-step move

    interior gains {-N-1,-N,N,N+1},
    boundary moves N -> N+2,

  as a single finite Loewner/cell residual with signed leading
  cancellation.
```

The proof must couple:

```text
old boundary entering the interior,
new boundary pole,
left/right shell insertion,
the three Schur cocycle terms A+B+C.
```

Any update formula that treats `N -> N+2` as a pure external-shell pair is
now ruled out.

## Status

```text
proved:    exact section-geometry audit for consecutive even steps;
refuted:   pure-shell update as the correct next identity;
observed:  zeta boundary migration is an active-size component of the
           small cocycle;
observed:  planted boundary migration is negligible relative to its O(1)
           Delta theta;
reduced:   TERNARY-CELL-CANCEL -> BOUNDARY-SHELL-CELL;
next:      E77.5k should derive the coupled four-node plus moving-boundary
           Loewner identity before applying Cauchy evaluation.
```
