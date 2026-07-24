# E77.7e - Paired Interlacing-Gap Audit

**Run:** 2026-07-18.

## 1. Exact Implication

For the inner block

```text
A_N(mu)=H_{L,N}^{inner}-mu I,
A_N(mu)x_N(mu)=b_N,
```

the resolvent identity gives

```text
x_N(mu_N)-x_N(mu_L)
=(mu_N-mu_L)A_N(mu_N)^(-1)A_N(mu_L)^(-1)b_N.   (DG-1)
```

Therefore the target

```text
DIR-GAP-PAIR:
sup_{z in K}
 |(mu_N-mu_L)r_z A_N(mu_N)^(-1)A_N(mu_L)^(-1)b_N|
 /max(1,|r_z x_N(mu_N)|) -> 0                 (DG-2)
```

implies `DIR-MU-FREEZE` immediately by `(DG-1)`.  This records the required
admissibility implication from E77.6.

## 2. Interlacing Decomposition

Let

```text
nu_N=lambda_min(H_{L,N}^{inner}),
g_N=nu_N-mu_N>0,
v_N=normalized ground vector of the inner block.
```

The dangerous component of the first resolvent is

```text
<v_N,b_N>/g_N.
```

E77.7d suggests that `v_N` should concentrate in low Fourier indices because
the diagonal grows logarithmically.  E77.7e tests whether this localization
suppresses `<v_N,b_N>` faster than interlacing collapses `g_N`.

## 3. Probe

Companion:

```text
E77_7e_dir_gap_pair_probe.py
```

Command:

```bash
python3 E77_7e_dir_gap_pair_probe.py \
  --lambda 6 --max-modes 20 --dps 60
```

The largest measured `mu_20` is used only as a numerical reference for
`mu_L`.  E77.7d proves existence of the true limit but this finite run does
not identify its exact value.

The double-resolvent identity reconstructs the direct moving/frozen
difference to the available precision.  Late zeta relative defects rise to
`8.8e-14` because the matrices reach gaps near `1e-49`; planted defects remain
near `1e-59`.

## 4. Zeta Anatomy

| N | `|mu_N-mu_ref|` | gap `g_N` | normalized overlap | center-five mass | paired ratio |
|---:|---:|---:|---:|---:|---:|
| 12 | 2.40e-37 | 4.28e-35 | 1.36e-23 | 0.9345 | 0.00570 |
| 14 | 1.71e-41 | 2.25e-39 | 1.77e-28 | 0.9212 | 0.00767 |
| 16 | 1.54e-45 | 1.56e-43 | 2.38e-31 | 0.9099 | 0.00992 |
| 17 | 2.36e-47 | 1.52e-45 | 2.29e-32 | 0.9050 | 0.01545 |
| 18 | 2.53e-49 | 2.33e-47 | 1.95e-33 | 0.9005 | 0.01082 |
| 19 | 4.57e-51 | 2.48e-49 | 2.39e-34 | 0.8963 | 0.01825 |

The localization premise is real: about `90%` of the inner ground vector
lies in the five central indices.  The normalized boundary overlap becomes
extraordinarily small.  But the interlacing gap collapses still faster, so

```text
|<v_N,b_N>|/g_N
```

grows rather than decays.  The final paired ratio stays in the range
`0.2%--1.8%` and has no observed decay through `N=19`.

Thus ground-mode localization alone does not prove `(DG-2)`.

## 5. Planted Anatomy

The plant displays the expected resonance subsequences:

| N | `|mu_N-mu_ref|` | gap `g_N` | normalized overlap | paired ratio |
|---:|---:|---:|---:|---:|
| 12 | 3.99e-2 | 9.62e-3 | 0.3610 | 0.800 |
| 14 | 2.52e-2 | 7.08e-4 | 0.0423 | 0.967 |
| 16 | 9.36e-3 | 4.49e-3 | 0.1286 | 0.670 |
| 17 | 9.24e-3 | 1.21e-4 | 0.0151 | 0.985 |
| 18 | 4.69e-3 | 4.55e-3 | 0.0637 | 0.504 |
| 19 | 1.06e-3 | 3.63e-3 | 0.0845 | 0.226 |

Avoiding `N=14,17` improves the finite values, but no theorem licenses a
plant-only resonance-avoiding subsequence.  Such a distinction would require
the E72.16 zero-filter audit before entering the proof chain.

## 6. Autopsy and Pivot

The proposed sufficient mechanism

```text
small ground overlap beats the interlacing gap
```

is refuted by the zeta data: the overlap is small, but not relative to the
gap.  `DIR-GAP-PAIR` itself is not refuted asymptotically, because the true
`mu_L` is replaced by a finite reference and the window is short.  It remains
unproved and sits directly beside the inverse-gap wall of P76.061.

Crucially, directional freezing is not logically necessary for LP.  It was
introduced only to transfer the old moving-point diagnostics to the fixed
operator.  E77.7d already constructs `H_L` and its real point `mu_L`; one may
prove LP directly there:

```text
FIXED-MU-BLOCK-GROWTH:
min_{0<=j<q} ||x_{N+j}(mu_L)||^2 -> infinity
=> Weyl-disk contraction at mu_L
=> LP.                                          (DG-3)
```

This bypasses the double inverse and preserves the admissibility rule because
`(DG-3)` explicitly implies the predecessor LP target.  The moving `S_N`
tables remain diagnostics only.

## 7. Status

```text
proved:    DIR-GAP-PAIR => DIR-MU-FREEZE by (DG-1);
proved:    exact finite double-resolvent reconstruction;
observed:  zeta ground localization and tiny boundary overlap;
refuted:   overlap smallness alone as control relative to the gap;
observed:  planted resonances at N=14 and N=17;
open:      DIR-GAP-PAIR, but no longer required for the direct LP route;
live:      FIXED-MU-BLOCK-GROWTH at the intrinsic mu_L;
next:      E77.7f fixed-mu block-growth setup using MR-1 and the logarithmic
           diagonal, without transferring moving-point energies.
```

