# E70.1 -- de Bruijn-Newman connection: Omega_7 = (Lambda <= 0), and the direction problem

**Date:** 2026-07-07.
**Scripts:** E70_1_heatflow.py, E70_1b_heatflow.py, dbg.py.

## Numerics (self-corrected)

The heat-flow kernel `H_lambda(z) = int e^{lambda u^2} Phi(u) cos(zu) du` was computed correctly. My
initial "bug" diagnosis was wrong: the standard dBN normalization gives `H_0(z)` zeros at `z = 2 gamma_n`,
so the first zero is at `z = 2 * 14.1347 = 28.27` -- exactly what the code found. Validating `MyXi(t)`
against `xi(1/2+it)` failed only because I compared in the wrong (un-doubled) variable. The zero at
28.27 shifts with lambda (28.04 at lambda=0.4, 28.62 at lambda=-0.6): it stays real and moves.

## The connection

```
H_0 = xi (up to normalization);  H_lambda has all real zeros  <=>  lambda >= Lambda (dBN constant).
de Bruijn: Lambda <= 1/2.   Rodgers-Tao 2018: Lambda >= 0.   RH <=> Lambda <= 0  =>  RH <=> Lambda = 0.
Our gauge-free Omega_7 (E69.1): xi in Laguerre-Polya = all zeros real = Lambda <= 0.
So  Omega_7  <=>  Lambda <= 0.
```

## The direction problem (honest, decisive)

The heat-flow forcing pushes zeros to the real axis as `lambda` INCREASES -- the de Bruijn direction
(`Lambda <= 1/2`, and the flow makes things real). This is the PROVEN half. But RH needs `Lambda <= 0`:
that the zeros are ALREADY real at `lambda = 0`. The flow does not give this. Rodgers-Tao's `Lambda >= 0`
makes RH "barely true" -- it does NOT help prove it.

So the Lee-Yang / dBN heat-flow forcing forces the WRONG direction for a proof. If a heat-flow
monotonicity gave `Lambda <= 0`, RH would be proved via dBN -- it is not, precisely because the
monotonicity yields `Lambda >= 0`. The direct Lee-Yang theorem route lands identically: "xi has the
Lee-Yang positivity" = "xi in Laguerre-Polya" = RH -- the same wall.

## What is genuinely gained

Not a dead end -- a precise placement in the deepest active framework:

```
Omega_7 <=> Lambda <= 0,   Lambda >= 0 proven (Rodgers-Tao)   =>   Omega_7 <=> Lambda = 0.
```

This localizes exactly what is missing: the `Lambda <= 0` direction is where the ARITHMETIC enters.
Rodgers-Tao proved `Lambda >= 0` with a GENERAL argument (zero pair-correlation, little arithmetic).
Our terminal defect `A_N - P_lambda` carries the Euler product explicitly -- the only route by which
Phase 70 could add something the general framework lacks: a `Lambda <= 0` handle from Euler structure.

## Status

```
gained    : Omega_7 <=> Lambda = 0 (placed in the dBN / Rodgers-Tao framework)
honest    : the heat-flow / Lee-Yang forcing gives Lambda >= 0 (the proven, wrong-direction half)
open      : a Lambda <= 0 handle from the Euler product -- the arithmetic direction, Weil-hard
not useful: heat-flow monotonicity alone (it forces the wrong way)
```
