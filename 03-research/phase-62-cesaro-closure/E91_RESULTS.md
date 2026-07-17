# E91 — Cesàro Convergence Curve of `b_bulk(λ)` (Phase 62, C1 numerical frame)

**Date:** 2026-06-26 · dps=40 · dense grid λ = 7,8,…,22 (integers) · ζ and DH falsador.

## Question

C0 showed ζ's intrinsic-Jacobi band width is bounded and DH's grows. C1 needs the sharper
statement to be analytically attackable: `b_bulk(λ) = b_smooth(λ) + b_osc(λ)` with `b_smooth`
bounded (PNT) and the **Cesàro average** of `b_osc` → 0 (unconditional zero-density). This run
checks the convergence curve that such a decomposition predicts.

## Result — ζ Cesàro-converges, DH diverges (dense grid)

| metric | ζ | DH |
|--------|-----|-----|
| slope of `b_bulk` vs λ (linear fit) | **−0.0024** (bounded) | **+0.0560** (linear growth) |
| Cesàro mean `Bbar(22)` | **0.1325** | 1.8770 |
| last Cesàro step `|dBbar|` | 2.0e-3 (settling) | 2.3e-2 (still climbing) |
| 2nd-half std of `b_bulk` | 0.028 | 0.082 |

- **ζ:** `b_bulk` oscillates around ≈0.13 with a clear dip at λ=14–16 (0.08–0.09) then recovers —
  a bounded **oscillation**, no trend. The running Cesàro mean stabilizes to 0.1325 and its
  steps shrink. This is precisely "bounded smooth part + zero-mean oscillatory part".
- **DH:** `b_bulk` rises monotonically 1.38 → 2.22; the Cesàro mean never settles. The
  decomposition's averaging hypothesis **fails** for DH — exactly the falsador behaviour.

## Reading

The numerical frame for C1 is confirmed: for ζ the band width is a bounded constant plus an
oscillation whose running average converges; for DH there is a genuine secular growth that no
Cesàro average can remove. This says the **analytic target is correct**: prove
`(1/Λ) Σ_{λ≤Λ} b_osc(λ) → 0` for ζ, where `b_osc` is the zero-sum part of the explicit formula
and the bound uses only the unconditional count `N(T) ~ (T/2π)log T`.

**Honesty:** this is evidence, not proof. The oscillation is consistent with the prime/zero echo
in the band `L = 2 log λ`, but E91 does not yet *identify* `b_osc` with the zero-sum term — that
identification (applying the explicit formula to the Doob-conjugated kernel) is the open analytic
step, written up in [C1-ANALYSIS.md](C1-ANALYSIS.md). DH refutes any shortcut.

## Reproduce

```
venv/bin/python E91_cesaro_convergence.py "[7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]"
```
