# E101.013 - Intermediate two-hypothesis package

E101.018--E101.019 supersede the minimality claim in this document.  The
two-hypothesis theorem below remains valid, but `MASS-BOUND` follows from two
values of `LOCAL-COVARIANT-IDENT` and is not an independent input.

## 1. Two hypotheses

For the normalized bilateral bordered characteristic, fix one safe reference
point and one nonempty open safe interval `I`.  Consider

```text
MASS-BOUND:
  sup_alpha sum_j 1/[r_(alpha,j)^2+sigma_0^2]
  <infinity;                                         (1.1)

LOCAL-COVARIANT-IDENT:
  DEF_alpha(s;s_*)->0
  locally uniformly for s in I.                     (1.2)
```

Here `DEF_alpha` is the complete integrated covariant residual of E101.011.

## 2. Closure theorem

### Theorem 2.1

`MASS-BOUND` and `LOCAL-COVARIANT-IDENT` imply `Omega7`.

### Proof

E101.012 turns (1.1) into local boundedness, hence normality, of the normalized
finite real-rooted family on the whole plane.  Equation (1.2) identifies every
sublimit with the normalized square of `Xi` on the open interval `I`.  The
identity theorem identifies the sublimit globally.  Hurwitz transfers finite
real-rootedness to the limit and excludes every off-real zero of `Xi`.
Therefore `Omega7` holds. `QED`

## 3. Logical roles of the split

The two hypotheses perform disjoint tasks:

```text
MASS-BOUND               compactness only;
LOCAL-COVARIANT-IDENT    arithmetic identification only.           (3.1)
```

Neither contains a zero-location premise.  The first is a one-sided bound on
one positive scalar.  The second is a signed determinant identity on one safe
interval.

Because their conjunction implies `Omega7`, difficulty conservation forces
the RH-strength content to occur in at least one of them.  Their logical form
supports the working allocation that the signed identification is the
discriminant while the mass bound is compactness infrastructure, but this
allocation remains to be proved by a build-neutral derivation of (1.1).

## 4. Superseding reduction

The direct route appeared at this stage to need

```text
1. MASS-BOUND at one safe point;
2. LOCAL-COVARIANT-IDENT on one safe interval.       (4.1)
```

All deformation, characteristic, adjugate, Euler and shell formulas feeding
these two statements are exact finite identities.

E101.019 proves the sharper statement

```text
LOCAL-COVARIANT-IDENT alone =>Omega7.                (4.2)
```

## 5. Status

```text
proved:
  valid two-hypothesis safe closure theorem;

superseded:
  claim that MASS-BOUND is an independent minimal input;

open:
  LOCAL-COVARIANT-IDENT;
  Omega7.
```
