# E77.5e - Shell-update decomposition

**Run:** 2026-07-18.

## 1. Statement

E77.5d reduced `SECTION-LAG` to a summable envelope for consecutive
section changes.  E77.5e decomposes each update:

```text
E_N(sigma)-E_{N+2}(sigma)
= 2 Re i[(F_N'/F_N)-(F_{N+2}'/F_{N+2})]
  - [B_ext,N(sigma)-B_ext,N+2(sigma)].
```

The goal is to identify whether the dominant lag is the explicit external
tail, the coupled Schur log update, or a signed cancellation between them.

## 2. Probe

Probe:

```text
E77_5e_shell_update_probe.py
```

Command:

```bash
python3 E77_5e_shell_update_probe.py \
  --lambda 6 \
  --max-modes 22 \
  --dps 60
```

Output:

```text
E77_5e_shell_update_results.json
```

This rebuilds one maximum section and extracts nested sections, so all
updates belong to a single finite family.

## 3. Zeta Table

| step | max rel. delta | max log update | max external update | log/external |
|---|---:|---:|---:|---:|
| 8 -> 10 | 0.06116 | 0.08148 | 0.09820 | 0.830 |
| 10 -> 12 | 0.03988 | 0.05443 | 0.06533 | 0.833 |
| 12 -> 14 | 0.03213 | 0.03782 | 0.04661 | 0.812 |
| 14 -> 16 | 0.02453 | 0.02822 | 0.03493 | 0.808 |
| 16 -> 18 | 0.02195 | 0.02115 | 0.02715 | 0.779 |
| 18 -> 20 | 0.01839 | 0.01669 | 0.02172 | 0.769 |
| 20 -> 22 | 0.01454 | 0.01379 | 0.01776 | 0.776 |

## 4. Planted Table

| step | max rel. delta | max log update | max external update | log/external |
|---|---:|---:|---:|---:|
| 8 -> 10 | 15.21 | 0.7906 | 0.09820 | 8.05 |
| 10 -> 12 | 0.3879 | 0.03169 | 0.06533 | 0.485 |
| 12 -> 14 | 0.1606 | 0.00384 | 0.04661 | 0.082 |
| 14 -> 16 | 0.1152 | 0.00457 | 0.03493 | 0.131 |
| 16 -> 18 | 0.09581 | 0.00142 | 0.02715 | 0.052 |
| 18 -> 20 | 0.07441 | 0.00150 | 0.02172 | 0.069 |
| 20 -> 22 | 0.06351 | 0.00062 | 0.01776 | 0.035 |

## 5. Reading

For zeta, the coupled Schur log update tracks the explicit external update
with a stable ratio around `0.77--0.83`.  The section-lag delta is the
remaining signed difference.  This is not a raw tail problem; it is a
shell cancellation problem.

For the planted build, after the initial large jump the log update is much
smaller than the external update.  The plant does not reproduce the zeta
shell-cancellation anatomy, even though it satisfies the exact finite
two-generator identities.

## 6. Reduced Target

`DELTA-ENVELOPE` is reduced to:

```text
SHELL-CANCEL:
Prove that the coupled Schur shell update satisfies

    2 Re i[(F_N'/F_N)-(F_{N+2}'/F_{N+2})]
      = c_N(sigma) [B_ext,N-B_ext,N+2] + R_N(sigma),

with c_N(sigma) bounded away from 0 and 1 in the observed zeta window and
with R_N summable under the cofinal N(L)/L condition.
```

Equivalently, prove a summable envelope for the signed remainder after
subtracting the explicit external sine-zero update.

## 7. Why This Is Progress

The live object is now a named shell update between consecutive finite
sections, not full IDENT and not a global positivity statement.  It uses
only the selected Cauchy/two-generator response before taking absolute
values, respecting the P76.061 autopsy.

The falsifier break remains located at IDENT: the planted build passes the
exact algebra but fails the zeta target and does not show the same shell
update anatomy.

## 8. Next Step

E77.5f:

```text
derive the Schur complement formula for adding the two outer modes
N+1 and N+2, express the update of F_b'/F_b as a 2x2 shell resolvent,
and test whether its leading term equals the external sine-zero update.
```

If this leading term identity closes, `SHELL-CANCEL` gives
`DELTA-ENVELOPE`.  If not, the 2x2 shell resolvent term is the next finite
object.

## 9. Status

```text
proved:    no IDENT theorem;
observed:  zeta log/external shell-update ratio is stable around 0.8;
observed:  planted shell-update anatomy is different;
open:      SHELL-CANCEL leading-term theorem;
next:      E77.5f 2x2 Schur shell resolvent for F_b'/F_b update.
```
