# E77.7ah - Boundary-zero exclusion versus Weyl normalization

**Run:** 2026-07-18.

## 1. Purpose

After E77.7af and E77.7ag, the remaining singular finite-section theorem
target is

```text
NO-FULL-BOUNDARY-ZERO-GROUNDSTATE.
```

The natural question is whether this is already subsumed by the Phase-77
Weyl endpoint gate from E77.7k:

```text
dim E_L = 1,
r_{z0} e_L != 0.
```

This note records the exact relation.

## 2. The two conditions are not logically equivalent

Let `xi` be a ground-state eigenvector of one finite or infinite section.

The exclusion

```text
NO-FULL-BOUNDARY-ZERO-GROUNDSTATE
```

means:

```text
xi(left) = xi(right) = 0
```

does **not** occur.

The Weyl normalization gate from E77.7k means:

```text
r_{z0} xi != 0.                                      (AH-1)
```

These are compatible but not equivalent.

Indeed, `r_{z0}` is a full Cauchy row on all coordinates, so in principle a
vector can have zero boundary entries and still satisfy `(AH-1)` through its
interior mass.  Conversely, a vector can have nonzero boundary entries while
the full Cauchy pairing cancels.

Therefore:

```text
NO-FULL-BOUNDARY-ZERO-GROUNDSTATE
```

is not automatically implied by `(AH-1)`, and `(AH-1)` is not automatically
implied by nonzero boundary entries alone.

## 3. What the current finite audits show

Two finite audits are now available:

1. **Anchor normalization** (E77.7ag): for the simple inner zero mode `v0`,

   ```text
   |r(z0)v0| = 0.3976, 0.3832, ..., 0.3332
   ```

   on the critical zeta ladder `N=6..14`, while `|lambda0(A)|` collapses from
   `7.38e-21` to `2.25e-39`.

2. **Full ground state boundary entries** (light audit, zeta, July 18, 2026):

   ```text
   N= 6: |xiL| = |xiR| = 1.56e-4,  |r_{z0}xi| = 0.3832
   N= 8: |xiL| = |xiR| = 1.49e-7,  |r_{z0}xi| = 0.3615
   N=10: |xiL| = |xiR| = 7.09e-8,  |r_{z0}xi| = 0.3473.
   ```

So in the observed zeta ladder:

```text
1. the full ground state does not have zero boundary entries;
2. the Weyl normalizing functional is simultaneously far from zero.
```

This strongly suggests that the two conditions are both true in the regime of
interest, but by different mechanisms.

## 4. Consequence for the LP chain

The honest reading is:

```text
E77.7k normalization gate:
  dim E_L = 1 and r_{z0} e_L != 0
```

and

```text
NO-FULL-BOUNDARY-ZERO-GROUNDSTATE
```

are separate finite/infinite obstructions that point in the same direction.

The source-blindness reduction E77.7af shows:

```text
NO-FULL-BOUNDARY-ZERO-GROUNDSTATE
=> v0^* g != 0.                                      (AH-2)
```

The anchor audit E77.7ag shows independently that the Cauchy normalization
factor is healthy on the critical finite ladder.

So the singular LP bridge is now best organized as:

```text
SOURCE-BLINDNESS-EXCLUSION
 + ANCHOR-NONVANISHING
=> singular fixed-section clause
=> PROJECTIVE-MU-TRANSFER singular sector.            (AH-3)
```

This fits inside `BORDERED-WEYL-COMPLETENESS`, but it should not be silently
identified with the single scalar condition `(AH-1)`.

## 5. Status

```text
proved:    boundary-zero exclusion and Weyl normalization are compatible but
           not logically equivalent in general;
observed:  on the tested zeta ladder both hold simultaneously;
refined:   NO-FULL-BOUNDARY-ZERO-GROUNDSTATE remains a distinct theorem-grade
           source-side target, not just a paraphrase of E77.7k;
next:      decide whether to prove this exclusion directly from the finite
           ground-state geometry or absorb it as an explicit subclause inside
           BORDERED-WEYL-COMPLETENESS.
```
