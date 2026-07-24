# E79.89 - On the audited long ladder, closure plus residual balance already forces the zeta geometry regime

**Scope:** `DISCRIMINANT`, next reduction after E79.88.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** on the longer
audited ladder `N=8..18`, every row satisfying the zeta-side closure and
residual-balance predicates also satisfies the zeta-side geometry predicate.
So the implication

```text
CLOSE + BAL  =>  GEOM                                                   (89-1)
```

holds on the full audited finite ladder, not just on the short `N<=12` slice.

## 0. Why this is the right next reduction

E79.88 left the discriminant burden in its sharpest finite form so far:

```text
the theorem-grade target is not D_N alone,
but a structural route toward CLOSE + BAL + GEOM.                       (89-2)
```

The next honest question is therefore immediate:

```text
does the left-hand side already force the right-hand geometry regime
on the current audited ladder?                                          (89-3)
```

If yes, the live burden shrinks again. If not, the first counterexample would
name the next missing finite ingredient.

## 1. Predicates

We keep the audited finite predicates from E79.88:

```text
CLOSE := |c_N| < 1e-5,
BAL   := R_net < 1e-6 and |log(R_pm)| < 0.1,
GEOM  := outlier_fraction > 5 and D_N < 5e-3.                          (89-4)
```

The object tested here is only the implication:

```text
(CLOSE and BAL) => GEOM.                                                (89-5)
```

## 2. Probe

Companion files:

```text
E79_89_closure_balance_to_geom_probe.py
E79_89_closure_balance_to_geom_results.json
```

The probe recomputes the full section metrics directly from the finite CCM data
on the longer audited ladder

```text
lambda=6,  N=8,10,12,14,16,18,  dps=60                                 (89-6)
```

for:

```text
zeta,
plant gamma1, beta=0.30,
plant gamma2, beta=0.30.                                               (89-7)
```

For each row it records the three predicates and whether the implication fails.

## 3. Result

On the full audited long ladder, the implication has no counterexample.

### Zeta

Every audited zeta row satisfies the premise:

```text
premise_count = 6.                                                      (89-8)
```

And every such row satisfies `GEOM`:

```text
geom_given_premise_count = 6,
implication_fail_rows = [].                                             (89-9)
```

So on the zeta ladder:

```text
CLOSE + BAL holds everywhere audited,
and GEOM follows everywhere audited.                                    (89-10)
```

### Plant gamma1 and gamma2

For both planted controls:

```text
premise_count = 0,
implication_fail_rows = [].                                             (89-11)
```

So neither planted ladder even enters the closure-plus-balance regime.

This is exactly the separation pattern that E79.87/E79.88 predicted: the
cloud-only resonant row never threatens the implication because it fails the
premise itself.

## 4. Reading

This is still a finite audit, not a theorem. But it is a real reduction.

Before E79.89, the honest target was the conjunction

```text
CLOSE + BAL + GEOM.                                                     (89-12)
```

After E79.89, on the audited ladder the third predicate is no longer
independent data. It is already forced whenever the first two hold:

```text
audited zeta route:
  CLOSE + BAL  =>  GEOM.                                                (89-13)
```

So the burden shrinks again:

```text
if this implication can be understood structurally,
the live front compresses from three ingredients to two:
  closure + residual balance.                                           (89-14)
```

## 5. Consequence

The next honest target is now sharper than in E79.88:

```text
derive GEOM from the closure-plus-balance side,
or identify the first row outside the audited ladder where that implication
fails and name the missing correction.                                  (89-15)
```

So the immediate next move is not another geometry proxy search, but a direct
attack on how the balanced secular package shapes the `K_N` cloud.

## 6. Status

```text
proved by audit:
  on the audited long ladder N=8..18, every row satisfying CLOSE + BAL
  also satisfies GEOM;

proved by audit:
  both planted controls remain outside the premise regime entirely, so the
  cloud-only planted resonance does not threaten the implication;

reduced:
  the live discriminant burden from CLOSE + BAL + GEOM to the sharper
  candidate route CLOSE + BAL => GEOM;

open:
  explain this implication structurally from the secular package, or find
  the first honest finite obstruction beyond the audited ladder.
```
