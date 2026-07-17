# E72.370 - ENERGY-CFIR tautology audit

## 1. Purpose

E72.368 gave the positive certificate

```text
ENERGY-CFIR:
||(Lambda_L I-KWin)k+t||^2 <= C_TL^{2B}.
```

E72.369 showed that norm/coercivity estimates do not prove it.  This note identifies the exact
meaning of the residual: it is the finite-window remainder at the nodes.

## 2. Nodal identity

E72.341 gives, for a simple zero window,

```text
Rem_T^M(z)=Lambda_LG_x(z)-(I_TG_x)(z)+Tail_T^M(z).
```

Evaluating at the window nodes gives

```text
J_T Rem_T^M
=(Lambda_L I-KWin)k+t.                              (1)
```

Therefore:

```text
ENERGY-CFIR
<=> ||J_T Rem_T^M||^2 <= C_TL^{2B}.                  (2)
```

## 3. Consequence

The master energy certificate is not a new source theorem.  It is a positive norm form of the nodal
remainder bound.  It is useful for verification, but proving it requires proving that the finite
window remainder is polynomial without using the outside-zero definition.

Thus the true non-circular statement remains:

```text
BFW-coupled / FINITE-CFIR:
derive J_T Rem_T^M=O_T(L^B)
from the finite coupled Feshbach-Weil expression
before expanding Rem_T^M as an outside zero sum.
```

## 4. No-go

The following implications are tautological and do not advance the proof:

```text
outside zero tail small => Rem_T^M small;
Rem_T^M small => ENERGY-CFIR;
ENERGY-CFIR => Rem_T^M small.
```

The admissible direction is:

```text
finite coupled archimedean-prime-Feshbach identity
=> J_T Rem_T^M=O_T(L^B)
=> Cauchy block suppression.
```

## 5. Updated load-bearing target

The exact finite expression to prove is:

```text
J_T[
   T_W02(z)[xi]-T_WR(z)[xi]-T_Prime(z)[xi]
   -2kappa_*G_x(z)
   -I_T^HG_x(z)
   +Tail_T^M(z)
]
=O_T(L^B).                                           (3)
```

This is the same expression as E72.342 `FINITE-CFIR`, but E72.370 clarifies why all later energy,
divisor, and projective certificates are equivalent diagnostics, not replacements for the coupled
identity proof.

## 6. Status

```text
proved: ENERGY-CFIR is exactly the squared norm of J_T Rem_T^M;
clarified: energy/projective/divisor certificates are diagnostics equivalent to nodal CFIR;
open: prove FINITE-CFIR from the finite coupled Feshbach-Weil expression.
```
