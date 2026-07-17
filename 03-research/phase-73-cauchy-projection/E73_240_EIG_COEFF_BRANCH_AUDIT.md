# E73.240 - Eigen-coefficient branch audit

Date: 2026-07-14.

## 1. Purpose

E73.239 shows that endpoint moments do not explain the U4 cancellation.  The
next possible source is the finite eigen-equation.  This note audits that
route and separates:

```text
1. the exact eigen-branch, which is circular for proving U4;
2. the non-circular EIG-COEFF target, which must be a structured coborder.
```

## 2. Exact branch

Let

```text
E=H_L-mu_L I,
Q=Q_w,
P=Q^*(QQ^*)^(-1)Q,
R=I-P,
eta=Rxi,
h=Qxi.
```

Since `E xi=0`,

```text
E eta = - E P xi.                                  (1)
```

Apply `Q`.  Because `Q eta=0`,

```text
QH eta = QE eta.
```

Also

```text
Pxi=Q^*(QQ^*)^(-1)h,
A(w)=QHQ^*(QQ^*)^(-1).
```

Thus

```text
QH eta
= -QE Pxi
= -Q(H-mu I)Q^*(QQ^*)^(-1)h
= (mu I-A(w))h.                                  (2)
```

This is exactly the branch already isolated in E73.188.

## 3. Why this does not close U4

The U4 center is

```text
C=QH eta.
```

Equation (2) proves:

```text
C=(mu I-A)h.
```

But the scalar WRL route needs to prove `C` small in order to prove the
characteristic divisor smallness of `h`.  Therefore bounding `C` through the
smallness of `h` is circular.

This branch is still useful as a consistency check, but it cannot be the
proof of `ETA-DIV`, `BSA-DIV`, or `CQ-DIV`.

## 4. Non-circular EIG-COEFF target

A valid eigen-coefficient theorem must not use `h=Qxi` as the small input.  It
must instead produce a structured coborder:

```text
G_{curv}
= coefficient action of E on a fixed primitive module
 + endpoint residual,
```

where `G_curv` is the curvature quotient weight vector from E73.238, and the
primitive module is fixed before pairing with `xi`.

In scalar form:

```text
<x_eta,G_curv>
= <xi,R_struct>,
```

with `R_struct` belonging to an explicit endpoint residual class whose pairing
is provably `O_M(L^-M)`.

This is the coefficient-side analogue of E73.162, but now the source is not an
off-line Hermite source.  The source is the curvature quotient functional
itself.

## 5. New theorem target

```text
CURV-COB:
For every admissible Cauchy window and row, the curvature quotient source
G_curv lies, modulo endpoint residual slots, in the image of the finite
coefficient action of E=H_L-mu_L I on a fixed rational primitive module.

Moreover, the endpoint residual pairing with xi_L is O_M(L^-M).
```

Then:

```text
CURV-COB
=> CQ-DIV
=> BSA-DIV
=> ETA-DIV
=> U4
=> TRANS-CELL
=> scalar WRL.
```

## 6. Anti-tautology conditions

`CURV-COB` is invalid if:

```text
1. the primitive is chosen by pseudoinverse against xi;
2. the residual is defined as projection to xi;
3. the proof uses h=Qxi small;
4. the source is reconstructed after seeing the final scalar center.
```

It is valid only if:

```text
1. the primitive module is finite and symbolic;
2. the coefficient action of E is computed by the CCM cell formula;
3. the residual slots are fixed endpoint slots;
4. the scalar residual estimate is proved directly.
```

## 7. Status

```text
proved: exact eigen-branch C=(mu I-A)h;
audited: this branch is circular for U4;
new target: CURV-COB, a structured coefficient coborder for the curvature
            quotient source.
```

