# E77.7h - Shell-transfer defect localization

**Run:** 2026-07-18.

## 1. Purpose

E77.7h reduced the fixed-mu block-growth front to the exact shell residual

```text
r_{R,M}=g_{R,M}-C_{R,M}^*A_{R,M}^{-1}h_{R,M}.
```

The previous note identified zeta-specific componentwise decay of this
residual and named:

```text
SHELL-TRANSFER-DEFECT:
prove that the old shorted response transports to the new shell source
with geometric componentwise defect.
```

This note localizes which package is responsible for that cancellation.

## 2. Probe

Companion:

```text
E77_7h_shell_transfer_defect_probe.py
E77_7h_shell_transfer_defect_results.json
E77_7h_shell_transfer_defect_R12_results.json
```

Commands:

```bash
python3 E77_7h_shell_transfer_defect_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 10 \
  --pairs 12:14,14:16,16:18,18:20 --dps 60

python3 E77_7h_shell_transfer_defect_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 12 \
  --pairs 14:16,16:18,18:20 --dps 60 \
  --output E77_7h_shell_transfer_defect_R12_results.json
```

The three builds are:

```text
zeta:      full Gamma-prime/cell arithmetic package;
arch_only: include_arith=False;
plant:     zeta package plus the standard planted off-line falsifier.
```

For each shell, the probe records:

```text
log10 <r,S^{-1}r>/eta_R,
log10 ||r||/||g||,
outer shell component |r_j/g_j|.
```

## 3. Result

At `R=10`, zeta shows geometric componentwise shell transport:

| shell | log10 energy/eta | log10 ||r|| ratio | outer |r_j/g_j| |
|---:|---:|---:|---:|
| 12 -> 14 | -4.5695  | -5.0017  | 9.9691e-6 |
| 14 -> 16 | -8.7163  | -9.0623  | 8.9705e-10 |
| 16 -> 18 | -12.7598 | -12.6225 | 2.4819e-13 |
| 18 -> 20 | -16.5436 | -15.9385 | 2.7340e-16 |

At `R=12`, the same pattern persists:

| shell | log10 energy/eta | log10 ||r|| ratio | outer |r_j/g_j| |
|---:|---:|---:|---:|
| 14 -> 16 | -4.1478  | -4.7202  | 1.9210e-5 |
| 16 -> 18 | -8.1919  | -8.7743  | 1.7044e-9 |
| 18 -> 20 | -11.9763 | -12.3874 | 6.6520e-13 |

The archimedean-only build does not show the cancellation:

| R | shell range | outer |r_j/g_j| scale |
|---:|---:|---:|
| 10 | 12 -> 20 | 1.0154 to 1.0488 |
| 12 | 14 -> 20 | 1.0120 to 1.0313 |

The planted build also does not show the cancellation:

| R | shell range | outer |r_j/g_j| scale |
|---:|---:|---:|
| 10 | 12 -> 20 | 0.6340 to 1.3839 |
| 12 | 14 -> 20 | 0.9799 to 1.2741 |

Thus the mechanism is not Hilbert/archimedean alone.  It is a coupled
Gamma-prime/cell transfer phenomenon.

## 4. Admissible Implication

The next target must be an identity or convergence statement, not a sign,
margin, or positivity claim.  The admissible reduced object is:

```text
GAMMA-CELL-SHELL-TRANSFER:
for fixed L and R, the full zeta Gamma-prime/cell package satisfies

g_{R,M}=C_{R,M}^*A_{R,M}^{-1}h_{R,M}+e_{R,M}

with componentwise reflected-shell defect

|e_{R,M,j}/g_{R,M,j}| <= A_R q_R^(M-R)

in the shell coordinates relevant to the shorted Stieltjes increment.
```

Then, by the exact shell Schur identity already recorded in E77.7h,

```text
GAMMA-CELL-SHELL-TRANSFER
=> SHELL-TRANSFER-DEFECT
=> GEOMETRIC-SHELL-RESIDUAL
=> SHELL-RESIDUAL-CANCELLATION
=> SHORTED-SHELL-ENERGY
=> SHELL-STIELTJES-INCREMENT
=> COFINAL-CYCLIC-TAIL
=> CYCLIC-POLE-CAPTURE
=> KRYLOV-WINDOW-RESOLUTION
=> CYCLIC-WINDOW-MASS
=> WFE-CYCLIC-TAIL
=> FESHBACH-RITZ-ENVELOPE
=> RITZ-BRACKET + BRACKETED-LOW-MODE-BTG
=> BTG-DIV-L
=> fixed-mu block growth
=> operational Weyl contraction.                         (T-1)
```

The implication is P76.061-safe: it uses the actual shorted residual
appearing in the Schur complement, never an ambient inverse norm.

## 5. Autopsy

`SHELL-TRANSFER-DEFECT` is not closed here.  The probe refutes the
archimedean-only explanation and names the exact missing mechanism:

```text
the full Gamma-prime/cell algebra transports the old shorted response
to the new shell source with exponentially small defect.
```

This is a theorem-grade reduction because proving the named transfer
statement implies the previous live target by (T-1).  It is also smaller
than the spectral bracket problem: it is a direct finite shell identity
problem for the residual vector.

## 6. Status

```text
proved:    GAMMA-CELL-SHELL-TRANSFER would imply the full current chain
           up to BTG-DIV-L by (T-1);
observed:  zeta shell transfer defect decays geometrically for R=10 and
           R=12 through max_modes=20;
observed:  arch_only lacks the cancellation, with outer defect O(1);
observed:  planted lacks the cancellation, with outer defect O(1);
refuted:   Hilbert/archimedean-only shell transfer as the mechanism;
open:      theorem-grade Gamma-prime/cell shell transfer;
open:      SHELL-TRANSFER-DEFECT and every upstream target in (T-1);
live:      GAMMA-CELL-SHELL-TRANSFER.
```
