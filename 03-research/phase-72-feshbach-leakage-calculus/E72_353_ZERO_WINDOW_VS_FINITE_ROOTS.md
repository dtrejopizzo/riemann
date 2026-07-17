# E72.353 - Zero windows are not finite Weyl-root windows

## 1. Purpose

E72.349--E72.352 use finite Cauchy roots as a numerical stress test for candidate rows.  This note
separates that diagnostic use from the load-bearing theorem needed for scalar WRL.

There are two different kinds of windows:

```text
finite Weyl-root windows:     G_x(a)=k_a xi=0 by construction;
Xi-zero contradiction windows: a is a shifted zero of the limiting Xi divisor.
```

Only the second kind is load-bearing for RH.

## 2. Finite Weyl-root windows

Let `a` be a finite root of the finite Cauchy transform

```text
G_x(z)=k_z xi.
```

Then

```text
G_x(a)=0.
```

If the window is made of simple finite roots, the interpolation part satisfies, at the nodal level,

```text
(Lambda_L G_x)(a)=0,
K_L(a,b)G_x(b)=0       for every root b in W_T.
```

For Hermite finite roots, the same statement holds for the included vanishing jets.  Therefore the
candidate residual at such a window collapses to the tail/normalization sector:

```text
J_T[Lambda_LG_x-I_T^HG_x+Tail_T^M]
= J_T Tail_T^M
```

modulo the included jet multiplicities.

This explains the numerical behavior:

```text
root rows pass mainly because the Cauchy root relation kills the visible interpolation terms.
```

That is useful as a formula check, but it is not the RH theorem.

## 3. Xi-zero contradiction windows

For the compact-root contradiction argument, fix a finite window of shifted zeros of the limiting
completed function:

```text
W_T={(a_j,m_j): Xi(1/2+a_j)=0, Re a_j>0}.
```

At finite `x`, these are not roots of `G_x` a priori.  The quantities

```text
J_TG_x = {G_x^(p)(a_j)/p!}
```

are unknown.  They are precisely the values that must be forced small.

The Hermite identity is

```text
J_T Rem_T^M
= H_T(L)J_TG_x + J_TTail_T^M.                         (1)
```

On a maximal-real-part off-line cluster,

```text
H_T(L) =
-diag(e^(a_jL)) C_conf + lower exponential blocks,
```

with `C_conf` invertible.  Therefore a polynomial bound for the left side of (1) forces
exponential suppression of the unknown finite values `J_TG_x`.

This is the actual forcing mechanism.

## 4. Non-circular target

The load-bearing target must therefore be stated for fixed Xi-zero contradiction windows:

```text
For every fixed W_T of shifted Xi zeros,
R_T^{Xi}(L)xi = O_{W_T}(L^B),
```

where

```text
R_T^{Xi}(L)xi
= J_T[Lambda_LG_x-I_T^HG_x+Tail_T^M],
```

and the nodes in `J_T` and `I_T^H` are the fixed `Xi`-zero representatives.

This may be proved by the stronger row-ideal statement

```text
R_T^{Xi}(L) in Row(C_E-mu I) + O(L^B),
```

but E72.352 shows it cannot be repaired by adding rowspace rows after the fact.

## 5. Meaning of shifted controls

The shifted controls in E72.349--E72.352 are not intended as the theorem itself.  They serve a
specific falsification purpose:

```text
If a proposed formula only passes at finite roots but fails at nearby shifted points,
then it is using the finite-root identity G_x(a)=0 rather than proving a structural row identity.
```

This is why the shifted defects matter.  They show that the partial rows are not yet structural.

## 6. Correct endpoint after E72.353

The endpoint is not:

```text
show candidate rows vanish at finite Weyl roots.
```

That is too weak and mostly kinematic.

The endpoint is:

```text
derive the exact residual row for an arbitrary fixed Xi-zero window
and prove its polynomial row-ideal defect without using G_x(a_j)=0.
```

Equivalently:

```text
R_T^{Xi}(L) adj(C_E-mu I) = O(L^B)
```

for every fixed contradiction window.  This is the finite algebraic form of scalar WRL resonance
annihilation.

## 7. Status

```text
clarified: finite Weyl-root tests are diagnostics, not the RH endpoint;
clarified: Xi-zero windows carry the actual off-line forcing;
corrected: shifted controls test structurality of candidate rows;
open: prove the Xi-window residual row-ideal bound.
```
