# E77.7h - Shell residual-cancellation scaling

**Run:** 2026-07-18.

## 1. Purpose

E77.7h reduced the shorted shell estimate to cancellation of

```text
r_{R,M}=g_{R,M}-C_{R,M}^*A_{R,M}^{-1}h_{R,M}.
```

This note asks whether that cancellation has a stable shell law.  The answer
in the finite zeta runs is yes:

```text
<r,S^{-1}r>/eta_R decays geometrically over successive shells.
```

This is still not a proof of the infinite estimate; it is the next precise
theorem target.

## 2. Probe

Companion:

```text
E77_7h_shell_residual_cancellation_probe.py
E77_7h_shell_residual_cancellation_results.json
E77_7h_shell_residual_cancellation_R12_results.json
```

Commands:

```bash
python3 E77_7h_shell_residual_cancellation_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 10 \
  --pairs 12:14,14:16,16:18,18:20 --dps 60

python3 E77_7h_shell_residual_cancellation_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 12 \
  --pairs 14:16,16:18,18:20 --dps 60 \
  --output E77_7h_shell_residual_cancellation_R12_results.json
```

The probe reuses the exact shorted shell identity and reports:

```text
log10(<r,S^{-1}r>/eta);
log10(||r||/max(||g||,||C^*A^{-1}h||));
ratio to previous shell;
cos(g,C^*A^{-1}h).
```

## 3. Zeta Scaling

For `R=10`:

| shell | log10 energy/eta | ratio to previous shell | log10 residual ratio |
|---:|---:|---:|---:|
| 12 -> 14 | -4.5695  | NA       | -5.0017  |
| 14 -> 16 | -8.7163  | 7.13e-5  | -9.0623  |
| 16 -> 18 | -12.7598 | 9.05e-5  | -12.6225 |
| 18 -> 20 | -16.5436 | 1.64e-4  | -15.9385 |

For `R=12`:

| shell | log10 energy/eta | ratio to previous shell | log10 residual ratio |
|---:|---:|---:|---:|
| 14 -> 16 | -4.1478  | NA       | -4.7202  |
| 16 -> 18 | -8.1919  | 9.03e-5  | -8.7743  |
| 18 -> 20 | -11.9763 | 1.64e-4  | -12.3874 |

The ratios are remarkably consistent across `R=10` and `R=12`.  The direct
and mediated shell vectors are aligned:

```text
cos(g,C^*A^{-1}h) = 1 - tiny
```

through the measured zeta shells.

## 4. Planted Contrast

The planted build does not show the same law.

For `R=10`, shell energy ratios are approximately:

```text
0.9065, 0.2829, 0.9591.
```

For `R=12`, they are:

```text
0.2575, 0.8862.
```

The cosines also oscillate in sign.  This is a quantitative falsifier
diagnostic, not a proof by positivity or a zero filter.

## 5. Reduced Target

The next admissible object is:

```text
GEOMETRIC-SHELL-RESIDUAL:
For cofinal R and shell distance d=M-R, prove

<r_{R,M},S_{R,M}^{-1}r_{R,M}>/eta_R
 <= A_R q^d

with q<1 summable in d, and with A_R compatible with
BRACKETED-LOW-MODE-BTG.
```

Then

```text
GEOMETRIC-SHELL-RESIDUAL
=> SHELL-RESIDUAL-CANCELLATION
=> SHORTED-SHELL-ENERGY
=> SHELL-RESIDUAL-SUM
=> SHELL-STIELTJES-INCREMENT
=> COFINAL-STIELTJES-TIGHTNESS
=> COFINAL-CYCLIC-TAIL
=> ... => BTG-DIV-L => corrected LP.          (R-1)
```

This target is stronger than the short finite measurements but now has the
right shape: a shell-distance summability theorem for a scalar shorted
energy.

## 6. Autopsy

`SHELL-RESIDUAL-CANCELLATION` is not closed here.

The new obstruction is proof of the geometric law.  The data rule out
several weaker targets:

```text
1. qualitative cancellation only;
2. finite pole tracking only;
3. norm estimates for g, C^*A^{-1}h, or S^{-1} separately.
```

The proof must explain why the mediated old response matches the new direct
shell source with shell-distance accuracy.  That is likely an exact
Hilbert/cell product-rule phenomenon, not a generic spectral fact.

## 7. Status

```text
proved:    GEOMETRIC-SHELL-RESIDUAL would imply the chain to BTG-DIV-L;
observed:  zeta shell energy/eta decays by ~7e-5--1.6e-4 per shell step;
observed:  the same zeta pattern appears for R=10 and R=12;
observed:  planted does not show the geometric cancellation law;
refuted:   qualitative finite cancellation as a sufficient proof target;
open:      theorem-grade geometric shell residual estimate;
open:      SHELL-RESIDUAL-CANCELLATION, SHORTED-SHELL-ENERGY,
           SHELL-STIELTJES-INCREMENT, COFINAL-CYCLIC-TAIL,
           CYCLIC-POLE-CAPTURE, KRYLOV-WINDOW-RESOLUTION,
           CYCLIC-WINDOW-MASS, WFE-CYCLIC-TAIL, RITZ-BRACKET,
           BRACKETED-LOW-MODE-BTG, BTG-DIV-L, corrected LP;
live:      GEOMETRIC-SHELL-RESIDUAL.
```

