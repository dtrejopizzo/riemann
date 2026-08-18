# E77.7s - Adaptive resonant window autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7r refuted fixed low-dimensional resonant blocks and left the next
smaller target:

```text
ADAPTIVE-RESONANT-WINDOW:
choose the resonant block by a spectral window tied to eta, not by a fixed
mode count.
```

This note audits the first natural implementation:

```text
|lambda_j| <= alpha * eta
```

with `alpha=100`.

## 2. Probe

Companion:

```text
E77_7s_adaptive_window_probe.py
E77_7s_adaptive_window_results.json
```

Command:

```bash
python3 E77_7s_adaptive_window_probe.py \
  --lambda 6 --max-modes 18 --dps 60 --alpha 100
```

For each `eta`, the probe subtracts the full spectral block

```text
E_N^res(eta) = span{u_j : |lambda_j| <= 100 eta}
```

before forming the projective quotient.

## 3. Result

### Zeta

At the finest regularization `eta=1e-8`, the adaptive windows are large:

```text
N=6:  7 modes
N=12: 14 modes
N=18: 21 modes.
```

Yet the projective profile does **not** stabilize better.  In fact it is
typically much worse than the raw regularization:

```text
N=6:  raw 0.0832   -> reg 0.2656
N=10: raw 0.0766   -> reg 0.1361
N=12: raw 0.0665   -> reg 0.2887
N=18: raw 0.0527   -> reg 0.0838.
```

Only sporadically is the adaptive window slightly better, and never by the
orders needed for closure.

### Planted build

For the planted build, the same adaptive rule selects no modes at the finest
regularization:

```text
window size = 0 for every N=6..18.
```

So the adaptive-window profile equals the raw profile exactly in the tested
window.

## 4. Reading

This is a strong autopsy.

```text
1. a purely spectral eta-window is too blunt;
2. for zeta it removes too much and worsens the projective profile;
3. for the planted build it removes nothing at all in the tested regime.
```

So the right object is not a window defined only by `|lambda_j| <= C eta`.
The resonant package must depend on the **boundary coupling** as well as on
the eigenvalue scale.

## 5. What is refuted

The following target is refuted:

```text
PURE-ETA-SPECTRAL-WINDOW:
define the resonant block by |lambda_j| <= alpha eta alone.
```

It is neither selective enough for zeta nor active enough for the planted
build.

## 6. Smaller live object

The next admissible reduction is:

```text
BOUNDARY-COUPLED-SELF-ENERGY-WINDOW:
define the resonant package through the paired boundary self-energy,
not by eigenvalue size alone.
```

Equivalently, the relevant low-dimensional object should be built from the
matrix-valued quantity

```text
P_res A_N(mu_ref)^(-1) b_N
```

after the safe Cauchy pairing, or from a Schur/Feshbach reduction in which
the boundary source participates in the block selection.

This is strictly smaller than the full singular-section theorem and strictly
more accurate than:

```text
one mode,
fixed 3-mode block,
pure eta spectral window.
```

## 7. Status

```text
observed:  the adaptive eta-window worsens the zeta regularized profile in
           most tested sections;
observed:  the same rule is inactive on the planted build in the tested
           regime;
refuted:   PURE-ETA-SPECTRAL-WINDOW;
open:      BOUNDARY-COUPLED-SELF-ENERGY-WINDOW;
next:      define the resonant package through the paired boundary
           self-energy / Feshbach block rather than through |lambda| alone.
```
