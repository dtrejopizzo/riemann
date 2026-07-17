# E73.005 - Coborder non-tautology audit

## 1. Purpose

E73.004 proposes proving the source identity

```text
SRC_b=<xi,S_b>
```

by writing `S_b` as a coborder for the finite eigen-equation:

```text
S_b=(C_E-mu I)Y_b+R_b.
```

This note separates the tautological part from the useful part.

## 2. Free coborder is tautological

Let

```text
A:=C_E-mu I,
C_E xi=mu xi,
||xi||=1.
```

Since `C_E` is self-adjoint,

```text
Range(A)=xi^perp.
```

For every source `S_b`,

```text
S_b=A Y_b + <xi,S_b>xi.                              (1)
```

Thus an unrestricted coborder always exists, and its residual is exactly the desired quantity.  It
does not prove `NAT-SRC`.

## 3. Non-tautological coborder criterion

The coborder route has content only if the primitive is controlled in a class where the known Phase 72
operator identities apply.  The finite measurable criterion is:

```text
COB-CTRL:
Y_b^min:=A^dagger(S_b-<xi,S_b>xi)
has polynomial size in a proof-facing norm N_L,
```

and the residual obeys

```text
e^(Re b L)|<xi,S_b>| <= L^B.                         (2)
```

The first condition is evidence that `S_b` really lies in a stable operator coborder class.  The
second is still the target, but now it can be attacked by applying the explicit finite operator
identity to `Y_b^min`.

## 4. Useful norms

For a source vector on the Fourier mesh, the first norms to monitor are:

```text
||Y_b^min||_2,
||(D Y_b^min)||_2,
||(D^2 Y_b^min)||_2,
```

where `D=diag(d_m)`.  Polynomial growth in these norms is compatible with the rational/divided
difference class of E73.004.

Exponential growth would falsify the coborder route.

## 5. Status

```text
proved: unrestricted coborder is tautological;
defined: non-tautological finite criterion COB-CTRL;
next: compute Y_b^min and the weighted eigenline residual for actual Phase 73 sources.
```

