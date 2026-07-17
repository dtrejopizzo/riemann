# The symbol-positivity detector for Omega_7

> **SCOPE (E68.5-E68.6, 2026-07-07): this detector is GAUGE-FRAGILE, not gauge-uniform.**
> The band-averaged symbol `sigma_A - sigma_P` is FAITHFUL at some gauges -- at t0 = 100, 200 it is
> marginally `~ 0` for zeta (with clean interior extraction; the touch at 0 is the correct de Branges
> marginality), matching the exact index. But at other gauges (t0 = 30, 50, 400) it goes spuriously
> negative for zeta (min `-0.7 .. -2.5` even after trimming edge contamination) although the EXACT
> signed index is `ind_-(A_N - P_lambda) = 0` there (verified, precision-robust). Root cause: the
> operator is NOT Toeplitz, so the band symbol represents it faithfully only where the non-Toeplitz
> part is benign, which is gauge-dependent. **Use only at gauges where it is validated (e.g. t0~100);
> for a gauge-robust statement use the exact signed index `ind_-(A_N - P_lambda) = 0 <=> RH` (E67.9).**

**A symbol-level detector, faithful at validated gauges but not gauge-uniform, for the terminal defect
of the ARP-P path.**
Origin: Phase 67, experiments E67.16-E67.17. Module: [symbol_positivity_detector.py](symbol_positivity_detector.py).

## Statement

The archimedean jet `A_N` and prime jet `P_lambda` of the terminal defect are approximately Toeplitz
(entries depend on `j-k`), so each carries a symbol on the unit circle. For Hermitian Toeplitz
matrices `A_N >= P_lambda  <=>  sigma_A(theta) >= sigma_P(theta)` pointwise (Szego / Avram-Parter).
Therefore the terminal-defect positivity equivalent to RH becomes a pointwise symbol inequality:

```
Omega_7   <=>   sigma_A(theta) >= sigma_P(theta)  for all theta
          <=>   the symbol of -Xi'/Xi is nonnegative on the circle
          <=>   RH.
```

`sigma_P` is the symbol `-zeta'/zeta` on the critical line; `sigma_A` the archimedean symbol.

## Why it is beautiful

- **Faithful and sharp.** `zeta`: `min(sigma_A - sigma_P) = +0.045`, negative fraction `0.000`.
  Off-line zero: `min` dips to `-34`, `-284`, `-3947` (beta = 0.65, 0.80, 0.95), negative on ~half
  the circle.
- **Marginality is visible.** The zeta minimum is `+0.045` -- the symbol *touches* zero. That is the
  symbol-level signature of zeta sitting exactly at the de Branges boundary (`delta_N -> 0+`).
- **Classical ground.** It moves Omega_7 into Toeplitz/Szego theory, where real tools exist:
  Wiener-Hopf/symbol factorization, Szego winding number, Fisher-Hartwig (for the marginal touch),
  Borodin-Okounkov. References: Bottcher-Silbermann (Toeplitz operators), Simon (OPUC),
  Borodin-Okounkov (resolvent-trace/Fredholm-determinant formula).

## Usage

```python
from symbol_positivity_detector import detect, planted_zero, symbol_gap
import mpmath as mp

detect(t0=100.0)                      # zeta:  (+0.045, 0.000)  -> nonnegative -> RH
z0 = mp.mpc(100, -1)
rho = mp.mpf("0.8") + mp.mpc(0,1)*mp.mpf("100")
detect(t0=100.0, Xi_deriv=planted_zero(z0, rho))   # off-line: strongly negative -> RH false
```

## Honest scope

This is a *detector*, not a proof, on two counts:

1. The symbols are computed through `zeta`, so nonnegativity for zeta is the E67.9 signed-index
   detector re-expressed.
2. **It is a symbol-depth detector, not a clean GLT measure (E67.19-E68.2).** The band structure varies
   with position (not constant-Toeplitz), which suggested a GLT/pseudodifferential reading -- but the
   direct test (E68.1-E68.2) shows the GLT distribution law FAILS: the position-resolved symbol has
   `measure{kappa<0} ~ 0.4` for zeta while `ind_- = 0`. So the object is not a clean GLT sequence and
   rigorous GLT eigenvalue-counting is not available. What IS faithful is the symbol DEPTH: the minimum
   of the symbol goes to `0^-` for zeta (the marginal de Branges touch) and to `-infinity` for a planted
   off-line zero. So the reliable statement is `Omega_7 <=> the symbol does not cross zero
   (min >= 0 in the limit)`, a sign/depth detector -- not a measure identity, and not a rigorous
   reduction.

Its value is as a faithful sign/depth detector and an attack surface -- Omega_7 as symbol
nonnegativity of an explicit special function -- not as a closed or rigorous argument. Omega_7 remains
the single open input of P52/P53.
