# E77.7t - Boundary self-energy autopsy

**Run:** 2026-07-18.

## 1. Purpose

E77.7s refuted pure spectral windows and left the next smaller target:

```text
BOUNDARY-COUPLED-SELF-ENERGY-WINDOW:
choose the resonant package by its paired boundary weight, not by |lambda|
alone.
```

This note audits the simplest scalar implementation of that idea.

## 2. Probe

Companion:

```text
E77_7t_boundary_self_energy_probe.py
E77_7t_boundary_self_energy_results.json
```

Command:

```bash
python3 E77_7t_boundary_self_energy_probe.py \
  --lambda 6 --max-modes 18 --dps 60 --capture 0.9
```

For each `eta`, the probe assigns every inner mode the scalar score

```text
| <u_j,b_N> r_{z0}(u_j) / (lambda_j-i eta) |,
```

orders the modes by this boundary-coupled self-energy weight, and subtracts
the smallest set capturing `90%` of the total score before forming the
projective quotient.

## 3. Result

### Zeta

The selected block has moderate size, typically `4--6` modes at the finest
regularization.  Nevertheless it does **not** stabilize the projective
profile.  In several rows it makes it much worse:

```text
N=10: raw 0.0766   -> reg 0.648
N=11: raw 0.0831   -> reg 0.620
N=17: raw 0.0804   -> reg 0.404
N=18: raw 0.0527   -> reg 0.176.
```

Only occasionally is the corrected profile slightly better than raw.

### Planted build

The same scalar boundary-weight rule often improves the already stable
planted regime substantially:

```text
N=6:  raw 8.5e-9   -> reg 8.9e-11
N=9:  raw 7.5e-8   -> reg 2.9e-9
N=10: raw 1.8e-7   -> reg 4.0e-8
N=11: raw 3.6e-7   -> reg 4.2e-8.
```

But in other rows it fails badly:

```text
N=12: raw 6.3e-7   -> reg 1.2e-5
N=15: raw 1.1e-6   -> reg 2.3e-5
N=18: raw 1.9e-6   -> reg 3.1e-5.
```

So even for the plant, a scalar self-energy ranking is not uniformly
coherent.

## 4. Reading

This autopsy is the cleanest one so far.

```text
1. spectral size alone is not enough;
2. boundary-coupled scalar weight alone is still not enough;
3. the live singular object is therefore genuinely matrix-valued.
```

The problematic ingredient is not just "which modes matter," but the
interaction among the chosen modes inside the projective quotient.  A scalar
ranking loses the internal cancellation/mixing that survives after the safe
Cauchy pairing.

## 5. What is refuted

The following target is refuted:

```text
SCALAR-BOUNDARY-SELF-ENERGY-WINDOW:
select a resonant block by ranking individual modes with one scalar
boundary-coupled weight.
```

It helps some planted rows but fails decisively for zeta.

## 6. Smaller live object

The next admissible reduction is:

```text
MATRIX-FESHBACH-RESONANT-BLOCK:
choose and treat the resonant package through a matrix-valued Schur/Feshbach
reduction in which the selected modes are kept coupled, rather than ranked
individually by scalar scores.
```

Equivalently, the correct finite object should be a low-rank matrix block

```text
M_res(eta) = P_res (A_N(mu_ref)-i eta I)^(-1) P_res
```

together with its coupled boundary source/row data, not a scalar score on
each eigenmode.

This is strictly smaller than the full LP bridge and strictly more accurate
than every refuted scalar reduction:

```text
one mode,
fixed 3-mode block,
pure eta spectral window,
scalar boundary-coupled ranking.
```

## 7. Status

```text
observed:  scalar boundary-coupled selection sometimes helps the planted
           regime;
observed:  it fails decisively for zeta and is not uniformly coherent even
           for the plant;
refuted:   SCALAR-BOUNDARY-SELF-ENERGY-WINDOW;
open:      MATRIX-FESHBACH-RESONANT-BLOCK;
next:      formulate the resonant package as a genuinely coupled Schur /
           Feshbach block before projectivization.
```
