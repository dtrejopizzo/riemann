# E67.11 Results — the Krein-Langer / Jantzen atom

**Date:** 2026-07-06.
**Script:** [E67_11_krein_langer_atom.py](E67_11_krein_langer_atom.py).

## Identity used

The terminal defect `A_N - P_lambda` is the confluent Pick/Loewner jet of `h = h_A + h_P`
(the log-derivative of Xi) at `z0`. A zero of Xi at `rho` is a simple pole of `-Xi'/Xi`, contributing
`g_rho(z) = -1/(z-rho)`. So the signed index decomposes into per-zero atoms.

## Results (z0 = 100 - i, N=8)

**(1) On-line atom is exact.** For `rho` at `beta=0.5` (on-line), the Pick jet has `ind_-=0` with
`min-eig = -1.6e-15` (numerical zero). A real pole of `-Xi'/Xi` gives a (semi)definite form: **no
negative square**. This is the load-bearing fact: RH (all zeros on-line) => `ind_- = 0`.

**(2) Additivity for nearby paired off-line zeros.** Each off-line zero taken with its
functional-equation reflection (beta=0.8 and beta=0.2): `K=0->0, K=1->1, K=2->2`. kappa counts off-line
pairs.

**(3) zeta robust.** `ind_-=0` up to N=20 (the `-1e-16` entries are numerical noise below tolerance).

## Self-caught nuance (do NOT overclaim ind_- = kappa at finite N)

- A single **unpaired** complex pole gives `ind_-=7` at N=8, not 1 (confluent-jet truncation artifact).
- `K=3` nearby pairs gave `ind_-=2`, not 3 (far zeros fall outside the effective window at small N).

So: the **dichotomy `0 vs >0` is a faithful detector** and **`on-line -> 0` is exact**, but the exact
equality `ind_- = (number of off-line zeros)` is a **stabilized/regularized** statement, not the raw
finite-N count. Any earlier reading that `ind_- = kappa` exactly at finite N is corrected here.

## How it advances the construction

Module-theoretic target, now pinned by the atom:

```
reducibility at a REAL point  (on-line zero)    -> Jantzen radical = UNITARY subquotient = 0 negative
reducibility at a COMPLEX point (off-line zero) -> NEGATIVE Jantzen layer (negative square)
```

This is exactly `U_q(su(1,1))` at a root of unity: `det H_q(mu)=0` on the real axis -> unitary layer;
off the axis -> negative layer. The Krein-Langer atom built here **is** the Jantzen atom.

Moreover, because the raw finite-N/window count is unstable, the root-of-unity regime -- intrinsically
**finite** (finite-dimensional modules, finite Jantzen filtration) -- is the natural candidate to supply
the **canonical regularization** of kappa that the bare confluent jet does not give cleanly.

## State

```
load-bearing fact : on-line zero = 0 negative squares (EXACT)          [E67.11(1)]
signed detector    : ind_- = 0  <=>  RH (faithful)                      [E67.9, E67.11]
count subtlety     : exact kappa is regularized, not raw finite-N       [E67.11 self-caught]
tool               : root-of-unity Shapovalov = finite Jantzen index    [E67.10]
open construction  : canonical von Mangoldt twist placing reducibility
                     of the q-module at the zeros of Xi                 [THE remaining heart]
```
