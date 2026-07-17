# E73.248 - Maximal-minor pivot rule for the quotient defect

## 1. Question

E73.247 used column-pivoted QR to select physical coordinates `J` for

```text
D_Q xi_L = D_Q[:,J] z_J,
z_J = xi_J + D_Q[:,J]^{-1}D_Q[:,R]xi_R.
```

QR is a numerical selection rule.  To turn `PIV-QUOT-DIV` into an explicit
finite identity, the pivot set must be specified without a black-box numerical
algorithm.

## 2. Tested physical rules

For `rank D_Q=4`, the audit compared:

```text
QR       : column-pivoted QR;
NORM4    : four columns of largest column norm;
SYMPAIR  : two strongest symmetric +/- frequency pairs;
EDGECORE : edge pair plus strongest remaining columns;
MAXMINOR : columns J maximizing |det D_Q[:,J]|.
```

## 3. Verdict

`NORM4`, `SYMPAIR`, and `EDGECORE` are not uniformly reliable.  They can be
close in later windows, but in the small trusted windows they may produce much
worse transfer norms and much larger pivot coordinates.

The robust rule is:

```text
J_*(L,w) in argmax_{|J|=4} |det D_Q[:,J]|.
```

In the tested windows, `MAXMINOR` matches the QR-quality pivots up to ordering
or harmless nearby choices:

```text
condB, zMaxB, transB
```

stay at the QR scale.

## 4. New finite theorem

The endpoint can now be written without QR:

```text
MAXMIN-PIV-DIV:
Let J_*(L,w) maximize |det D_Q[:,J]|.  Then

z_{J_*}
 = xi_{J_*} + D_Q[:,J_*]^{-1}D_Q[:,R_*]xi_{R_*}
 = O_M(L^-M).
```

The supporting nondegeneracy theorem is:

```text
MAXMIN-NONDEG:
|det D_Q[:,J_*]| >= L^{-B}
```

for some fixed `B`, uniformly in the allowed windows.

If `MAXMIN-NONDEG` and `MAXMIN-PIV-DIV` hold, then `CURV-QUOT-DIV` follows.

## 5. Relation to Phase 72 minor gates

This resembles the bordered-minor and compatibility-minor language from Phase
72, but it is not the same old rowspace route:

```text
Phase 72 rowspace minors: decide whether a residual row lies in Row(E).
E73.248 maximal minors: choose coordinates inside the already-formed DD-local quotient.
```

The quotient defect `D_Q` has already removed the fixed DD-local image.  The
maximal minor is only a coordinate denominator for the remaining obstruction.

## 6. Status

```text
rejected: NORM4/SYMPAIR/EDGECORE as universal symbolic pivot laws;
selected: maximal-volume quotient minor J_*;
open:     prove MAXMIN-NONDEG and MAXMIN-PIV-DIV analytically.
```
