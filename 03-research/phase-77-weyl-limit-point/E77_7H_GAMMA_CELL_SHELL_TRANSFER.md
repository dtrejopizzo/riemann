# E77.7h - Gamma/cell shell-transfer reduction

**Run:** 2026-07-18.

## 1. Purpose

The previous E77.7h note localized the shell-transfer defect to the full
Gamma-prime/cell package:

```text
g_{R,M}-C_{R,M}^*A_{R,M}^{-1}h_{R,M}.
```

This note rewrites that vector by the exact Loewner cell identity and names
the next smaller target.

## 2. Exact Cell Identity

For the package symbol `S_L(t)` attached to the same build as `H_L`,
P76.011 gives

```text
H_{ij}=2 C_L(d_i) delta_ij
      -(2/L) (S_L(d_i)-S_L(d_j))/(d_i-d_j),     i != j,
```

with `d_j=2 pi j/L`.

Let `u_{R,M}` be the old Feshbach vector reconstructed in physical
coordinates:

```text
u_{R,M}=-v_R + W_{R,M}^{old} x_{R,M}^{old},
```

where

```text
(K_oo-(mu_R-eta_M)I)x_{R,M}^{old}=h_o.
```

For a new shell coordinate `a`, `u_{R,M}(a)=0`, so the diagonal term is
absent and

```text
H_{a,old} u_{R,M}
=-(2/L) [
   S_L(d_a) sum_j u_j/(d_a-d_j)
   - sum_j S_L(d_j)u_j/(d_a-d_j)
 ].                                                   (GC-1)
```

But the Schur residual from E77.7h satisfies

```text
r_a=h_a-K_{oa}^*x_{R,M}^{old}=-H_{a,old}u_{R,M}.       (GC-2)
```

Combining `(GC-1)` and `(GC-2)`, the shell-transfer defect is exactly the
failure of a weighted Cauchy interpolation:

```text
S_L(d_a) A_{R,M}(d_a)-B_{R,M}(d_a),

A_{R,M}(z)=sum_j u_j/(z-d_j),
B_{R,M}(z)=sum_j S_L(d_j)u_j/(z-d_j).                 (GC-3)
```

No positivity, inverse norm, or zero filter is used.

## 3. Probe

Companion:

```text
E77_7h_gamma_cell_shell_transfer_probe.py
E77_7h_gamma_cell_shell_transfer_results.json
E77_7h_gamma_cell_shell_transfer_R12_results.json
```

Commands:

```bash
python3 E77_7h_gamma_cell_shell_transfer_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 10 \
  --pairs 16:18,18:20 --dps 50

python3 E77_7h_gamma_cell_shell_transfer_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 12 \
  --pairs 16:18,18:20 --dps 50 \
  --output E77_7h_gamma_cell_shell_transfer_R12_results.json
```

The probe verifies both identities:

```text
H_shell u = -r,
H_shell u = -(2/L)(S(d_a)A(d_a)-B(d_a)).
```

## 4. Numerical Audit

For `R=10`:

| build | shell | log10 Loewner id defect | log10 residual id defect | log10 ||H_shell u|| | log10 term cancel |
|---|---:|---:|---:|---:|---:|
| zeta | 16 -> 18 | -51.8834 | -51.4206 | -29.8813 | -16.0559 |
| zeta | 18 -> 20 | -51.6602 | -52.6289 | -32.5049 | -16.3703 |
| arch_only | 16 -> 18 | -50.9816 | -51.7772 | -0.6387 | -0.3385 |
| arch_only | 18 -> 20 | -51.1891 | -51.3546 | -0.6799 | -0.3377 |
| plant | 16 -> 18 | -50.3256 | -51.5996 | -0.9789 | -0.4881 |
| plant | 18 -> 20 | -50.1970 | -51.5212 | -0.8252 | -0.2120 |

For `R=12`:

| build | shell | log10 Loewner id defect | log10 residual id defect | log10 ||H_shell u|| | log10 term cancel |
|---|---:|---:|---:|---:|---:|
| zeta | 16 -> 18 | -51.9792 | -52.0475 | -29.8823 | -16.0558 |
| zeta | 18 -> 20 | -51.6937 | -52.5121 | -32.5062 | -16.3702 |
| arch_only | 16 -> 18 | -51.0386 | -51.5386 | -0.6397 | -0.3385 |
| arch_only | 18 -> 20 | -51.5386 | -inf | -0.6809 | -0.3377 |
| plant | 16 -> 18 | -50.3310 | -51.5865 | -0.9855 | -0.4881 |
| plant | 18 -> 20 | -50.1827 | -51.6011 | -0.8317 | -0.2120 |

Thus the exact algebra is neutral across builds, while the weighted Cauchy
match is zeta-specific in these windows.

## 5. Reduced Target

The live object is now:

```text
S-WEIGHTED-CAUCHY-MATCH:
for fixed L and cofinal shell distance, the old Feshbach vector u_{R,M}
satisfies, on reflected shell coordinates,

|S_L(d_a)A_{R,M}(d_a)-B_{R,M}(d_a)|
 <= E_R q_R^(M-R) |g_a|,

where A and B are the two Cauchy transforms in (GC-3).
```

Then the exact identities above give

```text
S-WEIGHTED-CAUCHY-MATCH
=> GAMMA-CELL-SHELL-TRANSFER
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
=> operational Weyl contraction.                         (GC-4)
```

## 6. Autopsy

`GAMMA-CELL-SHELL-TRANSFER` is not closed here.  It has been reduced to the
weighted Cauchy match `(GC-3)`.

The refuted approaches are now sharper:

```text
refuted: Hilbert/archimedean-only transfer;
refuted: generic Loewner identity as sufficient;
refuted: shell parity alone.
```

The load-bearing phenomenon is the zeta-specific interpolation relation

```text
B_{R,M}(d_a) ~= S_L(d_a) A_{R,M}(d_a)
```

for the old Feshbach vector.  This is a convergence/identity target, not a
sign target, so it remains MW-1-safe and P76.061-safe.

## 7. Status

```text
proved:    exact shell residual identity (GC-1)--(GC-3);
proved:    S-WEIGHTED-CAUCHY-MATCH implies the current chain to BTG-DIV-L
           by (GC-4);
observed:  zeta weighted Cauchy cancellation is about 1e-16 in both R=10
           and R=12 windows tested;
observed:  arch_only and planted builds satisfy the identities but fail the
           weighted Cauchy match at O(1) scale;
refuted:   archimedean-only or generic Loewner explanations;
open:      theorem-grade S-WEIGHTED-CAUCHY-MATCH;
open:      GAMMA-CELL-SHELL-TRANSFER and every upstream target in (GC-4);
live:      S-WEIGHTED-CAUCHY-MATCH.
```
