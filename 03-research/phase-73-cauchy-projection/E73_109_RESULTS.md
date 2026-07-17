# E73.109 results - HERM-BOX enclosure probe

## 1. Purpose

E73.108 identified `HERM-BOX` as the missing technical lemma for turning the box FAR-SLOPE probe
into a certificate.  E73.109 implements a first conservative enclosure:

```text
sup_B G <= max_grid G + 4 Lip_grid radius_cell.
```

This is not yet formal interval arithmetic, but it is stronger than corner sampling and tests whether
the budget survives inflated Hermite weights.

## 2. Output

```text
E73.109 HERM-BOX enclosure probe
Grid+inflated-Lipschitz upper enclosure for G_theta,m over cluster boxes.
 lam     L box                         selected        CmainUp  maxInfl status
  16   5.545 [0.18,0.22]x[13.93,14.33] 37.6,30.4,32.9    1.693e-01    1.006 PASS
  16   5.545 [0.15,0.25]x[13.63,14.63] 37.6,30.4,32.9    2.043e-01    1.016 PASS
  20   5.991 [0.15,0.25]x[20.52,21.52] 37.6,32.9,30.4    1.342e-01    1.030 PASS
  24   6.356 [0.15,0.25]x[20.52,21.52] 32.9,30.4,37.6    2.519e-01    1.030 PASS
  28   6.664 [0.15,0.25]x[20.52,21.52] 37.6,30.4,32.9    2.031e-01    1.030 PASS
```

## 3. Diagnosis

The inflated enclosure barely changes the budget:

```text
maxInfl <= 1.030
```

on the tested boxes.  The certified upper budget remains:

```text
CmainUp <= 0.252
```

well below the target:

```text
C_main=1.
```

Thus the box certificate has enough slack to absorb a rigorous interval enclosure for the Hermite
weight.

## 4. Caveat

The current Lipschitz constant is estimated by finite differences and inflated by `4`.  This is
computational evidence, not a formal proof.  The formal version must use either:

```text
1. direct interval arithmetic for the explicit formula; or
2. analytic derivative bounds for G_theta,m on each box.
```

## 5. Consequence

The `HERM-BOX` technical lemma looks tractable:

```text
HERM-BOX + E73.106 => interval proof of FAR3-MAIN-RAT on tested boxes.
```

The remaining gap is rigor of the enclosure method, not loss of budget.

## 6. Status

```text
verified: inflated box enclosure passes with slack;
open: replace finite-difference Lipschitz by rigorous interval/analytic derivative bounds.
```
