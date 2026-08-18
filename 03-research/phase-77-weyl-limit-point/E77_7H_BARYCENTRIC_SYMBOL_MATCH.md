# E77.7h - Barycentric symbol-match audit

**Run:** 2026-07-18.

## 1. Purpose

E77.7h reduced the shell-transfer defect to the exact weighted Cauchy
identity

```text
r_a=(2/L)(S_L(d_a)A_{R,M}(d_a)-B_{R,M}(d_a)).
```

This note tests whether the match

```text
B_{R,M}(z) ~= S_L(z) A_{R,M}(z)
```

is a local interpolation phenomenon or only a nodal shell phenomenon.

## 2. Probe

Companion:

```text
E77_7h_barycentric_symbol_match_probe.py
E77_7h_barycentric_symbol_match_results.json
E77_7h_barycentric_symbol_match_R12_results.json
```

Commands:

```bash
python3 E77_7h_barycentric_symbol_match_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 10 \
  --pairs 16:18,18:20 --dps 50

python3 E77_7h_barycentric_symbol_match_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 12 \
  --pairs 16:18,18:20 --dps 50 \
  --output E77_7h_barycentric_symbol_match_R12_results.json
```

For each pair, the probe evaluates

```text
E(z)=B_{R,M}(z)-S_L(z)A_{R,M}(z)
```

at the new shell mesh nodes and at off-mesh midpoints.  It records

```text
|E(z)| / max(|B(z)|, |S(z)A(z)|).
```

## 3. Results

For `R=10`:

| build | shell | max log10 relative defect at nodes | max log10 relative defect at midpoints |
|---|---:|---:|---:|
| zeta | 16 -> 18 | -12.9706 | -0.0741 |
| zeta | 18 -> 20 | -15.1181 | 0.2988 |
| arch_only | 16 -> 18 | -0.0741 | -0.0393 |
| arch_only | 18 -> 20 | -0.0738 | -0.0417 |
| plant | 16 -> 18 | -0.0273 | 0.1193 |
| plant | 18 -> 20 | 0.0999 | 0.1000 |

For `R=12`:

| build | shell | max log10 relative defect at nodes | max log10 relative defect at midpoints |
|---|---:|---:|---:|
| zeta | 16 -> 18 | -12.9705 | -0.0741 |
| zeta | 18 -> 20 | -15.1180 | 0.2988 |
| arch_only | 16 -> 18 | -0.0741 | -0.0393 |
| arch_only | 18 -> 20 | -0.0738 | -0.0417 |
| plant | 16 -> 18 | -0.0274 | 0.1194 |
| plant | 18 -> 20 | 0.1000 | 0.1001 |

The zeta match is strong at the new mesh nodes and absent at nearby
off-mesh midpoints.

## 4. Consequence

The following stronger target is refuted by the zeta build itself at this
scale:

```text
LOCAL-SYMBOL-INTERPOLATION:
B_{R,M}(z)/A_{R,M}(z) -> S_L(z) locally between mesh nodes.
```

The admissible target is strictly nodal:

```text
MESH-S-WEIGHTED-CAUCHY-MATCH:
on new shell mesh nodes d_a only,

|B_{R,M}(d_a)-S_L(d_a)A_{R,M}(d_a)|
 <= E_R q_R^(M-R) max(|B_{R,M}(d_a)|,|S_L(d_a)A_{R,M}(d_a)|).
```

Then, because of the exact Gamma/cell identity from the previous note,

```text
MESH-S-WEIGHTED-CAUCHY-MATCH
=> S-WEIGHTED-CAUCHY-MATCH on shell nodes
=> GAMMA-CELL-SHELL-TRANSFER
=> SHELL-TRANSFER-DEFECT
=> ... => BTG-DIV-L
=> fixed-mu block growth
=> operational Weyl contraction.                       (B-1)
```

This is not a zero filter: the target speaks only about the CCM mesh nodes
and the finite Gamma-prime symbol attached to the same section.

## 5. Autopsy

The next proof cannot use ordinary local rational approximation.  The
observed zeta cancellation is mesh-locked.  Any theorem that asks for
control on intervals between shell nodes is too strong and false in the
measured regime.

The live mechanism should therefore be sought in discrete cell algebra:
aliasing, finite-difference identities, or a mesh recurrence for the
barycentric numerator

```text
N_{R,M}(a)=B_{R,M}(d_a)-S_L(d_a)A_{R,M}(d_a).
```

## 6. Status

```text
proved:    MESH-S-WEIGHTED-CAUCHY-MATCH implies the current chain to
           BTG-DIV-L by (B-1);
observed:  zeta has strong nodal match at R=10 and R=12;
observed:  arch_only and planted do not have nodal match;
refuted:   LOCAL-SYMBOL-INTERPOLATION as a reduced target;
open:      theorem-grade MESH-S-WEIGHTED-CAUCHY-MATCH;
open:      all upstream targets in (B-1);
live:      MESH-S-WEIGHTED-CAUCHY-MATCH.
```
