# E77.7h - Mesh numerator profile

**Run:** 2026-07-18.

## 1. Purpose

The live target after the barycentric audit is the nodal match

```text
N_{R,M}(a)=B_{R,M}(d_a)-S_L(d_a)A_{R,M}(d_a)
```

on the newly added shell mesh nodes.  This note compares the numerator on
old external mesh nodes and new shell nodes.

## 2. Exact Row Identity

Let `u_{R,M}` be the old Feshbach vector in physical coordinates.  On old
external coordinate rows,

```text
(H_L-lambda_M)u_{R,M}=0.
```

Writing `H_L` with the Loewner/cell identity gives the finite-part relation

```text
N_{R,M}(i)
= (L/2)(2C_L(d_i)-lambda_M) u_i,
        R < |i| <= M_old.                         (P-1)
```

On new shell nodes, `u_a=0`, so

```text
H_{a,old}u_{R,M}=-(2/L)N_{R,M}(a).                (P-2)
```

Thus the shell target is a boundary vanishing statement for the same mesh
numerator whose old-node finite parts are fixed by `(P-1)`.

## 3. Probe

Companion:

```text
E77_7h_mesh_numerator_profile_probe.py
E77_7h_mesh_numerator_profile_results.json
E77_7h_mesh_numerator_profile_R12_results.json
```

Commands:

```bash
python3 E77_7h_mesh_numerator_profile_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 10 \
  --pairs 16:18,18:20 --dps 50

python3 E77_7h_mesh_numerator_profile_probe.py \
  --lambda 6 --max-modes 20 --ref-modes 12 \
  --pairs 16:18,18:20 --dps 50 \
  --output E77_7h_mesh_numerator_profile_R12_results.json
```

The probe records:

```text
max old-node log10 |N|,
max shell-node log10 |N|,
max_shell |N| / max_old |N|.
```

## 4. Results

For `R=10`:

| build | shell | old max log10 | shell max log10 | shell/old |
|---|---:|---:|---:|---:|
| zeta | 16 -> 18 | -7.0669 | -29.7787 | 1.94e-23 |
| zeta | 18 -> 20 | -6.7110 | -32.4050 | 2.02e-26 |
| arch_only | 16 -> 18 | -0.4979 | -0.6750 | 0.6651 |
| arch_only | 18 -> 20 | -0.4949 | -0.7173 | 0.5993 |
| plant | 16 -> 18 | -0.4312 | -0.8859 | 0.3510 |
| plant | 18 -> 20 | -0.4339 | -0.7737 | 0.4573 |

For `R=12`:

| build | shell | old max log10 | shell max log10 | shell/old |
|---|---:|---:|---:|---:|
| zeta | 16 -> 18 | -8.7356 | -29.7797 | 9.03e-22 |
| zeta | 18 -> 20 | -8.1508 | -32.4063 | 5.55e-25 |
| arch_only | 16 -> 18 | -0.5666 | -0.6760 | 0.7773 |
| arch_only | 18 -> 20 | -0.5635 | -0.7184 | 0.7001 |
| plant | 16 -> 18 | -0.7134 | -0.8925 | 0.6621 |
| plant | 18 -> 20 | -0.7178 | -0.7802 | 0.8661 |

Zeta has a new-shell boundary numerator many orders of magnitude smaller
than its old-node finite-part scale.  The controls do not.

## 5. Reduced Target

The live object is now:

```text
MESH-BOUNDARY-NUMERATOR-VANISHING:
for fixed L and cofinal shell distance,

max_{new shell a}|N_{R,M}(a)|
 <= E_R q_R^(M-R) max_{old external i}|N_{R,M}(i)|.
```

Together with `(P-2)`, this gives the nodal weighted Cauchy match:

```text
MESH-BOUNDARY-NUMERATOR-VANISHING
=> MESH-S-WEIGHTED-CAUCHY-MATCH
=> GAMMA-CELL-SHELL-TRANSFER
=> SHELL-TRANSFER-DEFECT
=> ... => BTG-DIV-L
=> fixed-mu block growth
=> operational Weyl contraction.                  (P-3)
```

## 6. Autopsy

The old external equations alone do not explain the shell cancellation.
They determine the old finite parts through `(P-1)`, but zeta imposes an
additional boundary vanishing at newly added mesh nodes.  This is absent in
the archimedean-only and planted builds.

Therefore the next proof should not seek a smooth extrapolation of old
finite parts.  It should seek a discrete boundary law for the mesh
numerator, likely through finite cell aliasing or a recurrence for
`N_{R,M}` at the insertion boundary.

## 7. Status

```text
proved:    old-node finite-part identity (P-1) and shell identity (P-2);
proved:    MESH-BOUNDARY-NUMERATOR-VANISHING implies the current chain to
           BTG-DIV-L by (P-3);
observed:  zeta shell numerator is 1e-21--1e-26 of old-node scale in tested
           R=10 and R=12 windows;
observed:  arch_only and planted shell numerator remains comparable to
           old-node scale;
refuted:   smooth extrapolation from old-node finite parts as the mechanism;
open:      theorem-grade MESH-BOUNDARY-NUMERATOR-VANISHING;
open:      all upstream targets in (P-3);
live:      MESH-BOUNDARY-NUMERATOR-VANISHING.
```
