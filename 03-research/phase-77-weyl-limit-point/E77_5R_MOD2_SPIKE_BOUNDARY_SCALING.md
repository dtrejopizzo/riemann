# E77.5r - Mod-2 Spike / Physical Boundary Scaling

## Objective

E77.5q reduced the live obstruction to:

```text
MOD2-SPIKE-CELL:
  explain the N=2 mod 4 spike in the second coefficient Q_N(sigma).
```

The first possible explanation is that the wrong scale was used: `N`
instead of the physical boundary coordinate

```text
d_N = 2*pi*N/L.
```

E77.5r tests that explanation.

## Probe

Artifacts:

```text
E77_5r_mod2_spike_boundary_scaling_probe.py
E77_5r_mod2_spike_boundary_scaling_results.json
```

Command:

```bash
python3 E77_5r_mod2_spike_boundary_scaling_probe.py
```

For `lambda=6`, the harness gives:

```text
L = 2 log(lambda) = 3.58351893846,
d_N = 1.75335624426 N.
```

Thus physical-boundary scaling is a constant rescaling at fixed lambda; the
probe records it explicitly rather than assuming it away.

## Results

Selected scaled profiles `Q_d = Q_N/(2*pi/L)^2`:

```text
zeta sigma=1.0
mod0: 0.09551 -> 0.12456, range=0.03964
mod2: -0.01915 -> 0.36253, range=0.44438

zeta sigma=3.0
mod0: 0.51488 -> 0.46094, range=0.07847
mod2: 0.11725 -> 1.15720, range=1.29240
```

For planted:

```text
plant sigma=1.0
mod0 range=35.05
mod2 range=1.599

plant sigma=3.0
mod0 range=6.429
mod2 range=0.603.
```

## Autopsy

Physical boundary scaling does not remove the zeta mod2 spike.  At fixed
lambda, `d_N` is proportional to `N`, so the scaled coefficient has the same
branch anatomy:

```text
zeta mod0 stable,
zeta mod2 spiking.
```

Therefore the obstruction is not a coordinate-scale mistake.  It is a real
mesh-parity effect of the moving-boundary Loewner cell.

## Reduced Target

`MOD2-SPIKE-CELL` is reduced to:

```text
LOEWNER-PARITY-CELL:
  derive the difference between the N=0 mod 4 and N=2 mod 4 branches from
  the finite Loewner displacement/cell identity.
```

The proof should compare the two four-node insertions:

```text
N=0 mod 4 branch,
N=2 mod 4 branch,
```

and locate the sign/phase source of the mod2 spike.

## Status

```text
proved:    physical boundary scaling does not resolve the spike;
refuted:   d_N scaling as the missing normalization;
observed:  zeta mod0 branch remains stable after scaling;
observed:  zeta mod2 branch remains the live obstruction;
reduced:   MOD2-SPIKE-CELL -> LOEWNER-PARITY-CELL;
next:      E77.5s should derive/measure the branch difference directly
           from the Loewner parity data of the four inserted nodes.
```
