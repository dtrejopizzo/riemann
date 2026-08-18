# E77.7ai - Boundary-zero clause decision

**Run:** 2026-07-18.

## 1. Purpose

After E77.7ah, the remaining question was organizational but important:

```text
Should NO-FULL-BOUNDARY-ZERO-GROUNDSTATE be proved as a standalone theorem,
or should it be recorded as an explicit subclause of
BORDERED-WEYL-COMPLETENESS?
```

This note answers that question from the current evidence.

## 2. Boundary equations do not give a short standalone proof

For a finite ground-state eigenvector `xi` of the full section,

```text
(H-mu I) xi = 0,
```

the boundary row equation is

```text
(H_00-mu) xi_0 + sum_{j=1}^{n-2} H_{0j} xi_j = 0.     (AI-1)
```

So if `xi_0 = 0`, one gets only

```text
sum_{j=1}^{n-2} H_{0j} xi_j = 0.                      (AI-2)
```

There is no immediate contradiction from positivity or sign, because the
interior weighted sum may in principle cancel.

The finite audit confirms this.  On the zeta ladder the actual boundary
entries are nonzero, but the naive predictor

```text
|xi_0| ?~ |sum_{j=1}^{n-2} H_{0j} xi_j| / |H_00-mu|
```

is only comparable, not an exact rigid lower bound:

```text
N= 6: |xi_0| = 1.56e-4, predictor = 2.82e-4
N= 8: |xi_0| = 1.49e-7, predictor = 1.51e-7
N=10: |xi_0| = 7.09e-8, predictor = 1.10e-7.
```

So the raw boundary equation is informative but does not by itself produce a
clean theorem-grade exclusion.

## 3. Interlacing also stops short

The principal-submatrix eigenvalues satisfy strict finite gaps on the tested
zeta ladder:

```text
N= 6: mu_inner - mu_full = 7.38e-21
N=10: mu_inner - mu_full = 1.84e-30.
```

This is consistent with Cauchy interlacing and with the simple zero mode of
the shifted inner block.  But interlacing alone does not exclude a full
eigenvector whose boundary coordinates vanish, because in that case the full
eigenvector simply restricts to an inner eigenvector at the same eigenvalue.

Therefore strict inequality must come from extra structure, not from generic
interlacing alone.

## 4. Candid conclusion

At the current state of the ledger, there is **not yet** a short standalone
proof of

```text
NO-FULL-BOUNDARY-ZERO-GROUNDSTATE
```

from elementary boundary equations or generic interlacing.

But E77.7af and E77.7ag already show why the clause matters:

```text
NO-FULL-BOUNDARY-ZERO-GROUNDSTATE
=> source nonvanishing v0^* g != 0,
anchor nonvanishing is healthy on the critical ladder,
=> singular fixed-section clause for PROJECTIVE-MU-TRANSFER.
```

So the most candid and useful organization is:

```text
record NO-FULL-BOUNDARY-ZERO-GROUNDSTATE as an explicit subclause inside
BORDERED-WEYL-COMPLETENESS,
not as a silently assumed corollary.
```

## 5. Consequence for the chain

The LP-side theorem target should therefore be stated as:

```text
BORDERED-WEYL-COMPLETENESS
includes:
  separation of safe Cauchy rows,
  singular-section regularization,
  pencil compatibility,
  existence of normalized class,
  simplicity/nonvanishing at mu_L,
  exclusion of full boundary-zero ground states where needed for the
  singular projective bridge.
```

This avoids two opposite mistakes:

```text
1. pretending the boundary-zero exclusion is already automatic;
2. splitting off a fake standalone theorem with no current exact proof.
```

## 6. Status

```text
audited:   boundary equations and generic interlacing do not yet give a
           clean standalone proof of boundary-zero exclusion;
decided:   NO-FULL-BOUNDARY-ZERO-GROUNDSTATE should presently be carried as
           an explicit subclause of BORDERED-WEYL-COMPLETENESS;
refined:   the singular LP bridge has been reduced as far as current exact
           evidence justifies without overclaiming;
next:      resume the main LP endpoint at the level of
           BORDERED-WEYL-COMPLETENESS / BTG-DIV-L, with the singular clause
           now properly localized inside it.
```
