# E72.21 -- Blaschke defect obstruction to boundary-modulus identification

**Date:** 2026-07-08.
**Role:** prevent the false proof of E72.20 by real-axis modulus convergence alone.

## 0. The tempting false move

E72.20 reduces RH to relative potential convergence:

```text
log|F_x/G_x| -> log|Xi/G|  in L^1_loc(S).
```

One might try to prove this from convergence on the real axis. This cannot work. Off-real zeros are
invisible to boundary modulus.

## 1. Blaschke factor

In the upper half-plane, for `rho` with `Im rho>0`, define

```text
B_rho(z) := (z-rho)/(z-conj rho).
```

Then:

```text
|B_rho(t)|=1     for t in R,
```

but `B_rho` has a zero at `rho` and a pole at `conj rho`.

Thus multiplying an analytic function by `B_rho` changes the interior divisor while leaving the
boundary modulus on `R` unchanged.

## 2. The obstruction theorem

### Theorem 72.21

No theorem using only real-axis modulus convergence

```text
log|F_x(t)/G_x(t)| -> log|Xi(t)/G(t)|
```

can imply the relative potential convergence of E72.20.

More precisely, for any candidate limit `H(z)` and any off-real point `rho`, the functions

```text
H(z)
```

and

```text
H(z)B_rho(z)
```

have identical boundary modulus on the real line but different divisor currents in the strip.

### Proof

For real `t`,

```text
|B_rho(t)| = |t-rho|/|t-conj rho| = 1.
```

Therefore

```text
log|H(t)B_rho(t)| = log|H(t)|.
```

But by Poincare-Lelong,

```text
(1/(2pi))Delta log|B_rho|
```

contains a positive point mass at `rho` and a negative point mass at `conj rho` when viewed as a
relative meromorphic current. Hence the interior divisor data differ. `QED`

## 3. Consequence for the CCM route

The relative potential convergence `(RPC)` cannot be proved from:

```text
real-axis modulus matching,
real-axis L2 convergence,
or Cartwright type alone.
```

It must use one of:

```text
1. phase/current convergence of log(F_x/G_x), not just modulus;
2. a de Branges/Hermite-Biehler structure excluding nontrivial inner factors;
3. a finite residue-current identity strong enough to rule out Blaschke defects.
```

This is the same obstruction as the Phase 70 Abel boundary loss, but now expressed exactly as an inner
factor defect.

## 4. The correct new target

The target from E72.20 must be strengthened to:

### Relative Schur-free Cartwright convergence

The relative functions

```text
H_x := F_x/G_x
```

converge in the Cartwright class with no residual inner/Blaschke factor:

```text
H_x -> Xi/G
```

in local `L^1` potential topology and in argument/current topology.

Equivalently, the relative logarithmic derivatives converge as distributions:

```text
d log H_x -> d log(Xi/G)
```

on the strip, not only on the real boundary.

## 5. Status

```text
proved: boundary modulus cannot identify the Xi divisor;
proved: any proof of RPC must control inner/Blaschke defects;
open:   prove Schur-free relative current convergence from finite CCM data.
```

This is now the sharp analytic form of the missing theorem.
