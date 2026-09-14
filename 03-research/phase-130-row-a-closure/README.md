# Phase 130 — row A closure: A.8, A.5, A.7, A.1 (builder/auditor loop, round 2)

Opened 2026-09-12, after the owner accepted the A.6 amendment and ordered A.8
attempted with new mathematics and nothing left open.

| file | content |
|---|---|
| R130_000 | lead blueprint (Fable): three insights — rulings as limits of spread Tate characters in `N_A^dist`; Mittag–Leffler form of the symbol over the periodic Tate lattice with universal residue `∓i`; the determinant Banach algebra `𝓐_tr` |
| R130_001 | builder round 1 (Opus): 43 passages; rejected 5 blueprint claims with reasons |
| R130_002 | hostile audit round 1 (Opus): 20 findings, 1 FATAL (`M` unbounded for the round-1 norm) |
| R130_003 | lead audit round 1: F1–F6, incl. the Mertens theorem (global scalar pairing of the rulings is 1) |
| R130_004 | builder round 2: every finding disposed; two verdicts moved down, none up |
| R130_005 | lead final audit and closure-rule decision |
| scripts/ | `ml_check.py`, `contour_check2.py`, `R130_ml_check.py`, `mertens_check.py` |

**[phase 133, PANEL_1 finding A8.]**  `scripts/ml_check.py` crashed through
phase 132 (a numpy/mpmath type mix: `np.exp` applied to an `mpf` inside
`mp.quad`).  The crash is repaired and the script runs, but it is **superseded**
and is not the script of record: its blocks 1–2 agree with the closed forms,
while its block 3 (the contour identity) is a draft that does not reproduce the
direct shell sum.  The script of record for Theorem 9.7b — Mittag-Leffler form
and the universal Tate residues `∓i` at `±i/2` at every place — is
**`scripts/R130_ml_check.py`**, which passes.  Nothing in the phase-130 record
depends on `ml_check.py` block 3.

## Outcome

`ROW A: WEIL-STRENGTH-COMPLETE` on the declared carrier (fixed finite chart,
chart system + colimit as additional structure, invertible sector), A.6 under
the 2026-09-12 amendment, A.8 with target `Pic_b(B_T)` (forced by Paper 43
Thm 10.8).  Dissent of the round-1 hostile audit on A.8 recorded verbatim in
Paper 43 §10.3.3.  Not claimed: `𝓝_∞^W = 0`, `c_cut`, non-invertible objects,
continuous extension of `I_A` to the completion squared, stack descent.
Handed to row C: Thm 10.8b (Mertens, CLASSICAL) — the finite-chart
vector-valuedness of `λ_RR` is the shadow of a global scalar hyperbolic
ruling pairing whose value `1` is the prime number theorem in Mertens' form.
