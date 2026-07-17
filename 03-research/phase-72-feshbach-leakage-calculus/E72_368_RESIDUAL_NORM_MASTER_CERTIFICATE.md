# E72.368 - Residual norm master certificate

## 1. Purpose

E72.365--E72.367 split simple-window CFIR into projective and scalar gates.  This note recombines them
as one positive finite certificate: the squared norm of the Hermite residual.

This is not a new theorem.  It is the cleanest proof-facing scalar functional for the next analytic
attack.

## 2. Master residual

For a simple Xi-zero window, define

```text
R_CFIR := (Lambda_L I-KWin)k+t.
```

The finite Hermite CFIR target is:

```text
||R_CFIR|| <= C_T L^B.                               (1)
```

Squaring gives the master energy certificate:

```text
E_CFIR
:= ||(Lambda_L I-KWin)k+t||^2
<= C_T L^{2B}.                                      (2)
```

## 3. Exact decomposition

Let

```text
v:=KWin k-t,
lambda_win:=<k,v>/<k,k>.
```

Then

```text
E_CFIR
= ||P_k^perp v||^2
 + |lambda_win-Lambda_L|^2 ||k||^2.                  (3)
```

Thus:

```text
E_CFIR = projective energy + scalar-consistency energy.
```

## 4. Why this matters

The previous determinant and wedge certificates are exact but sign-indefinite.  The master residual
energy is positive and finite.  It is the right object for an analytic proof if one can express its
pieces through the coupled Feshbach/explicit-formula identity without expanding into incoherent
absolute prime sums.

The wrong proof would bound:

```text
||KWin k|| + ||t|| + |Lambda_L| ||k||.
```

That loses the cancellation.  The correct proof must keep:

```text
(Lambda_L I-KWin)k+t
```

as one coupled object.

## 5. Equivalent statements

For simple windows, the following are equivalent up to the stated polynomial error:

```text
1. CFIR-H.
2. R_T^{Xi}(Lambda_L)xi=O_T(L^B).
3. PCFIR + SCALAR-CONS.
4. E_CFIR <= C_TL^{2B}.
```

For multiple windows, replace vectors by Hermite blocks and use the principal-part projectors of
E72.359.

## 6. Next analytic target

The remaining proof should target:

```text
ENERGY-CFIR:
|| (Lambda_L I-KWin)J_TG_x + J_TTail_T^M ||^2
<= C_T L^{2B}
```

directly from the coupled transformed Feshbach equation.

This target is finite, explicit, and falsifiable.  It contains the exact scalar and projective
requirements and does not allow after-the-fact fitting.

## 7. Status

```text
proved: residual norm energy is equivalent to PCFIR + SCALAR-CONS;
specified: positive finite master certificate ENERGY-CFIR;
open: prove ENERGY-CFIR analytically without incoherent termwise bounds.
```
