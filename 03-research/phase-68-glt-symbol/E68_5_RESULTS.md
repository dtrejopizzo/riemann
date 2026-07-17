# E68.5 -- the symbol detector is gauge-fragile (false negatives); the exact signed index is the robust object

**Date:** 2026-07-07.
**Script:** [E68_5_touch_local.py](E68_5_touch_local.py) + direct ind_- cross-check.

## Finding

Characterizing the touch-point margin `sigma_min` of the band-averaged symbol vs the height gauge `t0`
(zeta, y=1, N=14):

```
t0    theta*    sigma_min    curvature
30   -1.506    -1.461       147.5
50   -1.460    -3.975       350.2
100  +1.619    +0.040         0.117
200  +1.559    +0.050         0.064
400  -1.919    -5.806       506.4
```

`sigma_min` is strongly NEGATIVE for zeta at t0 = 30, 50, 400 -- a false indication that RH is violated.
Cross-check of the EXACT defect (the ground truth):

```
zeta ind_-(A_N - P_lambda) = 0 at t0 = 30, 50, 100, 400   (min eigenvalue ~1e-16..1e-21,
identical at dps 40 and 70 -- precision-robust).
```

So RH/Omega_7 holds at the operator level at every gauge, and the band-averaged **symbol detector
produces false negatives**. The huge local curvature (150-500) at the failing gauges vs ~0.06 at
t0=100,200 shows these are spurious non-Toeplitz spikes, not real negativity.

## Consequence -- honest correction

- **Robust object:** the exact signed index `ind_-(A_N - P_lambda) = 0 <=> RH` (E67.9). Gauge-robust,
  precision-robust. This is the real detector.
- **Not robust:** the band-averaged Toeplitz symbol `sigma_A - sigma_P >= 0`. It is gauge-FRAGILE and
  gives false negatives; it only looked clean at t0=100 by luck. The Szego law (E67.18) and the whole
  Toeplitz/symbol reformulation (E67.16-18, Phase 68 E68.1-4) rest on this fragile representation and
  are therefore NOT reliable as stated.

The 02-foundations detector doc has been marked with a warning; it is kept as a cautionary result, not
a working tool.

## Where this leaves us

- Omega_7 is unchanged and open; the exact signed-index characterization (E67.9-E67.11) stands and is
  gauge-robust.
- The Toeplitz-symbol direction (E67.16 onward) is undermined: the band-averaged symbol is not a
  faithful, gauge-stable representation of the operator. Phase 68's premise (analyze the symbol) does
  not have a reliable object under it.
- The next honest move is to return to the gauge-robust exact object (the whitened defect / its signed
  index) and seek structure there, or a genuinely gauge-stable reduction -- not the band symbol.
```
solid   : ind_-(A_N-P_lambda)=0 <=> RH, gauge- and precision-robust
retracted: band-averaged symbol as a faithful detector (gauge-fragile, false negatives)
open    : the forcer, on the exact object
```
