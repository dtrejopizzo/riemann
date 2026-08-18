# E77.5f - 2x2 Shell Resolvent Identity

## Objective

E77.5e reduced `SECTION-LAG` to a coupled shell update.  E77.5f makes the
update finite and algebraic: split the shifted inner system

```text
A = H_inner - mu I
```

into the two extreme inner shell nodes and the remaining core.  For the
right transfer

```text
T_b(z) = 1/(z-d_b) - r(z) A^{-1} g_b
```

the exact Schur formula is

```text
T_b(z) = t0(z) - tau(z) Sigma^{-1} kappa
T_b'(z) = t0'(z) - tau'(z) Sigma^{-1} kappa
```

where

```text
Sigma = C - U^T A0^{-1} U
kappa = g_shell - U^T A0^{-1} g_core
tau(z) = r_shell(z) - r_core(z) A0^{-1} U
t0(z) = 1/(z-d_b) - r_core(z) A0^{-1} g_core.
```

All inversions in the probe are finite linear solves.  No pseudoinverse,
ambient inverse norm, zero location, Weil positivity, or absolute
pre-cancellation bound is used.

## Probe

Artifact:

```text
E77_5f_shell_resolvent_probe.py
E77_5f_results.json
E77_5f_smoke_results.json
```

Main command:

```text
python3 E77_5f_shell_resolvent_probe.py --lambda 6 --max-modes 22 --dps 100 --output E77_5f_results.json
```

The first implementation used an explicit core inverse and had an unstable
derivative sign.  The certified version solves the core columns directly and
uses the derivative convention

```text
d/dz[-r_core A0^{-1}g_core] = -r_core' A0^{-1}g_core,
r_core' = -1/(z-d)^2.
```

## Certification Table

Max over `sigma in {0.55,0.6,0.75,1,1.5,2,3}`.

| build | N | max identity error | max shell-log update | max correction/core |
|---|---:|---:|---:|---:|
| zeta | 8 | 2.006035e-82 | 0.068252524 | 1.3437864 |
| zeta | 10 | 1.6508606e-76 | 0.040113447 | 1.2753408 |
| zeta | 12 | 2.0736981e-73 | 0.027315251 | 1.2217213 |
| zeta | 14 | 4.7497335e-68 | 0.018645243 | 1.1982058 |
| zeta | 16 | 1.0616466e-63 | 0.014080377 | 1.1753709 |
| zeta | 18 | 8.6750026e-61 | 0.010442305 | 1.1581070 |
| zeta | 20 | 3.1886736e-56 | 0.0081971472 | 1.1426685 |
| zeta | 22 | 1.5716224e-52 | 0.0068066353 | 1.1359206 |
| planted | 8 | 1.2878436e-101 | 0.41021980 | 1.3217474 |
| planted | 10 | 1.439853e-101 | 0.057496232 | 4.0009250 |
| planted | 12 | 2.2114386e-101 | 0.0025192588 | 5.5388467 |
| planted | 14 | 1.4549995e-101 | 0.0013894518 | 9.1905982 |
| planted | 16 | 1.2115568e-101 | 0.00063260819 | 1.9281952 |
| planted | 18 | 1.3844126e-101 | 0.00020569320 | 0.089759551 |
| planted | 20 | 2.1466959e-101 | 0.00045194856 | 2.0137199 |
| planted | 22 | 1.3897654e-101 | 0.00011533706 | 0.038081819 |

## Verdict

`SHELL-RES-2x2` is closed as an exact finite identity.  It is not the final
Omega7 closure: small shell-log size alone is falsifier-neutral, because the
planted build can also become small on some windows.  The meaningful
separation is geometric:

```text
zeta:    correction/core decreases smoothly toward about 1.136 at N=22.
planted: correction/core spikes and collapses: 4.00, 5.54, 9.19, 1.93,
         0.0898, 2.01, 0.0381.
```

Thus E77.5f replaces `SHELL-CANCEL` by a smaller finite object:

```text
SHELL-REG
```

Prove a signed regularity theorem for the Schur shell geometry:

```text
tau(z) Sigma^{-1} kappa / t0(z)
```

on sigma-compacts, strong enough to imply a summable envelope for the
section-lag deltas.  The theorem must distinguish zeta from the planted
off-line build by regularity/phase coherence, not by raw smallness.

## Next Move

E77.5g should measure the Schur phase and increment regularity:

```text
Delta_N log(1 - tau_N Sigma_N^{-1}kappa_N/t0_N)
```

and compare it with the explicit external sine-zero tail from E77.5e.  The
candidate proof target is:

```text
SHELL-REG + EXT-TAIL-AC => DELTA-ENVELOPE => SR-LOG-2SCALE.
```
