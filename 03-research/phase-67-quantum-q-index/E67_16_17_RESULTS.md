# E67.16 / E67.17 -- the Toeplitz-symbol form of Omega_7 (a better surface)

**Date:** 2026-07-06.
**Scripts:** [E67_16_structure_probe.py](E67_16_structure_probe.py),
[E67_17_symbol_positivity.py](E67_17_symbol_positivity.py).

## E67.16 -- classical structure of the jets

The raw jets are approximately Toeplitz (entries depend on `j-k`):

```
A_N (arch)        toeplitz_dev = 0.228   (hankel 1.25)
P_lambda (prime)  toeplitz_dev = 0.149   (hankel 1.21)  -- banded, |P[j,k]| ~ f(|j-k|)
D_N (whitened)    toeplitz_dev = 0.79    -- whitening BREAKS Toeplitz
```

So E113's Toeplitz observation was structurally real (only the scalar-whitening claim was retracted).
`P_lambda` carries the symbol `-zeta'/zeta` on the critical line; `A_N` the archimedean symbol. The
whitening `A_N^{-1/2}` is not a Toeplitz operation, so one should work with the PAIR `(A_N, P_lambda)`
(which is Omega_7 directly: `A_N >= P_lambda`), not the whitened defect.

## E67.17 -- symbol positivity is a faithful detector

For Hermitian Toeplitz `A_N, P_lambda`, `A_N >= P_lambda  <=>  sigma_A(theta) >= sigma_P(theta)`
pointwise (Szego / Avram-Parter, symbol limit). Band-averaged symbols give:

| case | min(sigma_A - sigma_P) | frac negative |
|---|---|---|
| zeta (RH true) | **+0.045** | 0.000 |
| offline beta=0.65 | -34.2 | 0.49 |
| offline beta=0.80 | -283.8 | 0.50 |
| offline beta=0.95 | -3947 | 0.51 |

Clean and faithful: the symbol is nonnegative for zeta and dips strongly negative for off-line zeros.
The zeta minimum `+0.045` is MARGINAL (touches 0): the symbol-level signature of zeta at the
de Branges boundary (delta_N -> 0+).

## Reformulation

```
Omega_7  <=>  sigma_A(theta) >= sigma_P(theta) for all theta
         <=>  the symbol of -Xi'/Xi is nonnegative on the circle
         <=>  RH.
```

This is a Toeplitz/Szego statement, in a domain with rigorous machinery: symbol (Wiener-Hopf)
factorization, Fisher-Hartwig, Borodin-Okounkov, Szego limit theorems. The pivotal q-trace forcing
becomes a SYMBOL INTEGRAL: the pivotal-weighted negative part of `sigma_A - sigma_P` must vanish.

## Honest status

- This is still equivalent to RH (the symbol is computed via zeta; proving positivity = RH). It is a
  reformulation, not yet a reduction to something easier.
- BUT it is a much better ATTACK SURFACE than the abstract index or the whitened root-of-unity
  resolvent: symbol positivity of an explicit special function, with real tools.
- Bibliography to build on (to avoid known errors): Bottcher-Silbermann (Toeplitz operators),
  Simon (OPUC), Widom (asymptotics), Borodin-Okounkov (Fredholm-determinant / resolvent-trace formula).

## Next step

Compute the Wiener-Hopf / Szego factorization of the symbol `sigma = sigma_A - sigma_P` and locate
its zero(s): for zeta the symbol touches 0 (marginal, a double zero on the circle = winding 0);
an off-line zero makes the symbol change sign (nonzero winding / negative index). The forcing theorem
in symbol form: `sigma` has no sign change (winding number 0) <=> the negative-index symbol integral
vanishes. This connects the pivotal q-trace to the Szego winding, a concrete and classical target.

```
new  : Omega_7 = symbol nonnegativity of -Xi'/Xi (Toeplitz/Szego)     [E67.16-17]
solid ground : Bottcher-Silbermann, Simon OPUC, Borodin-Okounkov
open : prove the symbol has no sign change by structure (winding-0),
       equivalently the pivotal-weighted negative symbol integral = 0
```
