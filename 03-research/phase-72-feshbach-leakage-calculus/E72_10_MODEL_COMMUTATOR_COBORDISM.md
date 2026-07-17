# E72.10 -- Model commutator cobordism for PSC

**Date:** 2026-07-08.
**Role:** replace the abstract PSC primitive by an explicit commutator mechanism against the model
prolate complement.

## 0. Purpose

E72.9 isolates PSC:

```text
<v,b_x> = <C_x^0 v,w_x> + eps_x(v),
||w_x|| -> 0,
||eps_x||_{(C_x^0)^*} -> 0,
||C_x^{-1}(C_x-C_x^0)w_x|| -> 0.
```

This document gives a structural way to produce `w_x` without solving an inverse equation.

The idea is:

```text
residual force = model commutator + small error.
```

If the actual/model perturbation satisfies, on the model ground vector,

```text
Q_x R_x k_x = Q_x [C_x^0,A_x] k_x + e_x,
```

then, because

```text
C_x^0 k_x = 0
```

after model recentering,

```text
Q_x [C_x^0,A_x] k_x = C_x^0 Q_x A_x k_x.
```

Thus the primitive is

```text
w_x = Q_x A_x k_x,
```

constructed from a model transport operator `A_x`, not from `C_x^{-1}b_x`.

## 1. Setup

Use the notation of E72.9:

```text
b_x = Q_xR_xk_x,
C_x^0 = Q_x(H_x^0-mu_x^0)Q_x,
C_x = C_x^0 + V_x.
```

Extend `C_x^0` to the one-dimensional ground line by setting

```text
C_x^0 k_x = 0.
```

Let `A_x` be an operator defined on the model core, preserving the finite/restricted space up to a
controlled boundary remainder. No self-adjointness of `A_x` is needed.

## 2. The model commutator hypothesis

### Hypothesis MCC

There exist operators `A_x` and remainders `e_x` such that:

```text
(MCC1)  b_x = Q_x[C_x^0,A_x]k_x + e_x;
(MCC2)  ||Q_xA_xk_x|| -> 0;
(MCC3)  ||(C_x^0)^{-1}e_x|| -> 0;
(MCC4)  ||C_x^{-1}V_xQ_xA_xk_x|| -> 0;
(MCC5)  ||C_x^{-1}V_x(C_x^0)^{-1}e_x|| -> 0.
```

All inverses in `(MCC3)` are model inverses; the actual inverse appears only in the one-vector
replacement terms `(MCC4)-(MCC5)`.

## 3. Theorem 72.10 -- MCC implies PSC

Assume MCC. Then PSC holds with

```text
w_x = Q_xA_xk_x,
eps_x(v) = <v,e_x>.
```

Consequently,

```text
||C_x^{-1}b_x|| -> 0.
```

### Proof

Since `C_x^0k_x=0`,

```text
[C_x^0,A_x]k_x = C_x^0A_xk_x - A_xC_x^0k_x = C_x^0A_xk_x.
```

Projecting to the complement gives

```text
Q_x[C_x^0,A_x]k_x = C_x^0Q_xA_xk_x,
```

because `C_x^0` acts on the complement and kills the ground line. Therefore `(MCC1)` becomes

```text
b_x = C_x^0w_x + e_x,
w_x = Q_xA_xk_x.
```

Pairing against a test vector `v` gives

```text
<v,b_x> = <C_x^0v,w_x> + <v,e_x>,
```

so `(PSC1)` holds. `(PSC2)` is `(MCC2)`, and `(PSC3)` follows from `(MCC3)` by the model dual identity:

```text
sup_v |<v,e_x>|/||C_x^0v|| = ||(C_x^0)^{-1}e_x|| -> 0.
```

Finally, `(PSC4)` and the same estimate for the error primitive are exactly `(MCC4)-(MCC5)`. Hence PSC
holds, and E72.9 gives reduced leakage. `QED`

## 4. Why this is non-circular

The primitive is:

```text
w_x = Q_xA_xk_x.
```

It is valid only if `A_x` is constructed independently from:

```text
C_x^{-1},
the endpoint Xi resolvent,
zero-local kernels,
and additive local inverses.
```

Thus the mathematical burden has moved to constructing a **model transport** `A_x` such that the actual
arithmetic residual on `k_x` is a model commutator.

This is a narrower and cleaner object than PSC:

```text
PSC asks for a model primitive.
MCC asks for a model transport whose commutator produces that primitive.
```

## 5. The intended `A_x`

The natural candidate is a pole-relative prolate boundary transport.

In the prolate boundary coordinate `theta`, write the model complement schematically as

```text
C_x^0 ~ -partial_theta (p_x(theta) partial_theta) + q_x(theta)
```

on the complement of the ground line. A first-order transport has the form

```text
A_x = alpha_x(theta) partial_theta + beta_x(theta),
```

with boundary/pole counterterms chosen so that `Q_xA_xk_x` lies in the primitive complement.

Then

```text
[C_x^0,A_x]k_x
```

is a second-order expression whose leading terms are derivatives of the model ground profile. The
coefficients `alpha_x,beta_x` should be chosen so that those leading terms match the actual arithmetic
force:

```text
Q_xR_xk_x.
```

This is the prolate/Sonin analogue of a homological equation.

## 6. The homological equation

The formal equation for the transport is:

```text
Q_xR_xk_x = Q_x[C_x^0,A_x]k_x + e_x.             (HE)
```

In boundary coordinates this is a first-order equation for `alpha_x,beta_x`, because `k_x` solves the
model ground equation

```text
C_x^0k_x = 0.
```

The dangerous second derivatives cancel against the model equation; what remains is a transport equation
for the boundary mismatch.

This cancellation is the reason a commutator route is better than solving `C_x^0w=b_x` directly.

## 7. Finite-channel version

For the low/high split of E72.6, it is enough to solve `(HE)` modulo high model modes.

Let `Pi_x^0(M)` be the first `M` complement modes of `C_x^0`. The finite-channel MCC condition is:

```text
Pi_x^0(M)b_x
  = Pi_x^0(M)[C_x^0,A_x]k_x + e_{x,M},
```

with

```text
||Pi_x^0(M)Q_xA_xk_x|| -> 0,
||(C_x^0)^{-1}e_{x,M}|| -> 0
```

for every fixed `M`, plus a uniform reduced model tail. This is the smallest practical proving target.

It avoids the old prolate failure: it does not ask the entire complement to be Dirichlet-like; only the
finite slow channels of the one source `b_x` are matched by a model commutator.

## 8. Kill tests

MCC fails as a new route if:

```text
K1. A_x is constructed from C_x^{-1} or the endpoint resolvent.
K2. A_x is chosen by diagonalizing the actual complement C_x.
K3. HE is solved for all complement sources, not just k_x.
K4. The proof uses additive Green/resolvent assembly over primes.
K5. The proof estimates e_x by absolute prime-cell sums.
K6. The proof turns the model boundary coordinate into a Christoffel evaluator at zeta zeros.
K7. The proof needs uniform lower coercivity equivalent to the old Phase 60 sign wall.
```

## 9. Status

```text
proved:   MCC => PSC => reduced leakage => stable divisor convergence;
open:     construct the pole-relative prolate boundary transport A_x satisfying MCC.
```

This is a genuine sharpening of the missing mathematics. The next object is not an inverse and not a
kernel: it is a transport operator `A_x` whose model commutator reproduces the one residual force
`Q_xR_xk_x`.

