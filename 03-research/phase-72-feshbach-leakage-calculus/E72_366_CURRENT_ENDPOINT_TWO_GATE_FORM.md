# E72.366 - Current endpoint in two-gate form

## 1. Purpose

E72.354--E72.365 refined the CFIR endpoint.  The old single phrase

```text
prove R_T^{Xi} in Row(C_E-mu I)
```

is now split into two finite gates.  This note records the current endpoint so that the next proof
attempt attacks the correct statements.

## 2. Simple zero windows

For a simple Xi-zero window, define:

```text
k := J_TG_x,
KWin_{ij}:=K_L(a_i,a_j),
t:=J_TTail_T^M.
```

The full finite CFIR equation is:

```text
(Lambda_L I-KWin)k+t=O_T(L^B).                       (1)
```

This is equivalent to the conjunction of:

```text
PCFIR:
  P_k^perp(KWin k-t)=O_T(L^B),

SCALAR-CONS:
  lambda_win = Lambda_L + controlled error,
  lambda_win=<k,KWin k-t>/<k,k>.                     (2)
```

## 3. Divisor interpretation

`PCFIR` is equivalent to the simple-window divisor condition:

```text
Delta(z,w)=S(z)K(w)-S(w)K(z)
belongs to (Z(z),Z(w)) up to polynomial error.
```

Equivalently, it is the vanishing of the alternating residue matrix:

```text
A_{pq}=int int phi_p(z)phi_q(w)Delta(z,w)
       Z'/Z(z)Z'/Z(w) dw dz.
```

`SCALAR-CONS` is not seen by this skew form.  It identifies the recovered projective scalar with the
actual Feshbach left coefficient.

## 4. Multiple zero windows

For multiplicities, replace the simple `Z'/Z` residue matrix by the principal-part projectors:

```text
Pi_{a,r;b,s}[Delta]
= Res Res (z-a)^{m-r-1}(w-b)^{n-s-1}
  Delta(z,w)/(Z(z)Z(w)) dz dw.
```

Holomorphic `Z'/Z` tests are insufficient for higher Hermite slots, by E72.360.

## 5. What is already ruled out

The following routes are closed:

```text
1. Add rowspace corrections A(C_E-mu I): inert by E72.352.
2. Fit Lambda after the fact: replaced by exact SCALAR-CONS.
3. Prove a node-blind kernel identity: falsified by E72.355.
4. Prove universal KWin eigenline preservation: blocked by E72.364.
5. Use holomorphic Z'/Z tests for multiplicities: insufficient by E72.360.
```

## 6. What remains

The remaining mathematical work is:

```text
PCFIR proof:
  Prove P_k^perp(KWin k-t)=O_T(L^B)
  for the actual k=J_TG_x on Xi-zero windows,
  using the coupled explicit formula/Feshbach equation.

SCALAR-CONS proof:
  Prove lambda_win=Lambda_L+controlled error
  from the same coupled identity, not by fitting.
```

Together these imply the finite Hermite CFIR equation, and then the existing maximal Cauchy block
forces off-line suppression.

## 7. Status

```text
closed: algebraic decomposition of CFIR into PCFIR + SCALAR-CONS;
closed: local ideal and residue/projector formulations;
open: analytic proof of PCFIR and SCALAR-CONS for Xi-zero windows.
```
