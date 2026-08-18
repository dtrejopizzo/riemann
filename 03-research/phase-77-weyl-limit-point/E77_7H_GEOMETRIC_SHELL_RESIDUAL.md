# E77.7h - Geometric shell-residual shape

**Run:** 2026-07-18.

## 1. Purpose

E77.7h reduced the shell estimate to:

```text
GEOMETRIC-SHELL-RESIDUAL:
<r_{R,M},S_{R,M}^{-1}r_{R,M}>/eta_R
 <= A_R q^(M-R),  q<1.
```

This note inspects the vector shape of

```text
r_{R,M}=g_{R,M}-C_{R,M}^*A_{R,M}^{-1}h_{R,M}
```

to determine whether the geometric law is merely energetic or already
visible component by component.

## 2. Probe

Companion:

```text
E77_7h_geometric_shell_residual_probe.py
E77_7h_geometric_shell_residual_results.json
E77_7h_geometric_shell_residual_R12_results.json
```

Commands:

```bash
python3 E77_7h_geometric_shell_residual_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 10 \
  --pairs 12:14,14:16,16:18,18:20 --dps 60

python3 E77_7h_geometric_shell_residual_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 12 \
  --pairs 14:16,16:18,18:20 --dps 60 \
  --output E77_7h_geometric_shell_residual_R12_results.json
```

The probe records the direct shell source `g`, the mediated source
`C^*A^{-1}h`, the residual `r`, componentwise residual/direct ratios, and
left/right parity.

## 3. Zeta Pattern

For `R=10`, the energy and vector cancellation ratios are:

| shell | log10 energy/eta | log10 ||r|| ratio | cancellation ratio to previous |
|---:|---:|---:|---:|
| 12 -> 14 | -4.5695  | -5.0017  | NA |
| 14 -> 16 | -8.7163  | -9.0623  | 8.70e-5 |
| 16 -> 18 | -12.7598 | -12.6225 | 2.75e-4 |
| 18 -> 20 | -16.5436 | -15.9385 | 4.83e-4 |

For `R=12`:

| shell | log10 energy/eta | log10 ||r|| ratio | cancellation ratio to previous |
|---:|---:|---:|---:|
| 14 -> 16 | -4.1478  | -4.7202  | NA |
| 16 -> 18 | -8.1919  | -8.7743  | 8.83e-5 |
| 18 -> 20 | -11.9763 | -12.3874 | 2.44e-4 |

The residual is even under left/right reflection in the measured shells.
This parity is not the discriminant: the planted build is even as well.
The zeta-specific feature is the componentwise scale.  At `R=10`:

```text
outer component |r_j/g_j|:
12->14: ~9.97e-6
14->16: ~8.97e-10
16->18: ~2.48e-13
18->20: ~2.73e-16
```

Thus the mediated response predicts the new direct shell source to
componentwise geometric accuracy.

## 4. Planted Contrast

The planted build remains even, but the componentwise residual ratios are
order one and oscillatory.  At `R=10`, representative outer-component
ratios are:

```text
12->14: ~0.63;
14->16: ~0.97;
16->18: ~1.38;
18->20: ~0.94.
```

For `R=12`, cancellation ratios between shells are about `0.70` and `2.08`,
not geometric decay.

This is a useful falsifier diagnostic, but not a proof by sign or by
off-line-zero filtering.

## 5. Reduced Target

The next admissible object is:

```text
SHELL-TRANSFER-DEFECT:
Prove, from the exact Hilbert/cell shell update, that

g_{R,M} - C_{R,M}^*A_{R,M}^{-1}h_{R,M}

has componentwise geometric decay in shell distance, in the reflected-even
shell coordinates.
```

Then

```text
SHELL-TRANSFER-DEFECT
=> GEOMETRIC-SHELL-RESIDUAL
=> SHELL-RESIDUAL-CANCELLATION
=> SHORTED-SHELL-ENERGY
=> SHELL-STIELTJES-INCREMENT
=> COFINAL-CYCLIC-TAIL
=> ... => BTG-DIV-L => corrected LP.          (G-1)
```

This remains P76.061-safe because the target is the actual shell residual,
not a separate ambient inverse norm.

## 6. Autopsy

`GEOMETRIC-SHELL-RESIDUAL` is not closed here.  The probe identifies the
load-bearing phenomenon:

```text
the old shorted response transports almost exactly to the new zeta shell.
```

The proof must now explain this as an algebraic shell transfer identity or
as a controlled defect of such an identity.  A generic spectral or norm
argument will not see the componentwise cancellation.

## 7. Status

```text
proved:    SHELL-TRANSFER-DEFECT would imply the chain to BTG-DIV-L (G-1);
observed:  zeta componentwise shell residual decays geometrically for
           R=10 and R=12;
observed:  planted does not show componentwise shell transfer;
refuted:   shell parity alone as the mechanism, since both builds are even;
open:      theorem-grade Hilbert/cell shell transfer defect;
open:      GEOMETRIC-SHELL-RESIDUAL, SHELL-RESIDUAL-CANCELLATION,
           SHORTED-SHELL-ENERGY, SHELL-STIELTJES-INCREMENT,
           COFINAL-CYCLIC-TAIL, CYCLIC-POLE-CAPTURE,
           KRYLOV-WINDOW-RESOLUTION, CYCLIC-WINDOW-MASS,
           WFE-CYCLIC-TAIL, RITZ-BRACKET, BRACKETED-LOW-MODE-BTG,
           BTG-DIV-L, corrected LP;
live:      SHELL-TRANSFER-DEFECT.
```

