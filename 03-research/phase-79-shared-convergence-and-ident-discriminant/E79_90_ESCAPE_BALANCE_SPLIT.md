# E79.90 - The candidate mechanism behind `CLOSE + BAL => GEOM` splits into escape and symmetry

**Scope:** `DISCRIMINANT`, structural follow-up to E79.89.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** on the
audited ladder, the candidate implication

```text
CLOSE + BAL => GEOM                                                     (90-1)
```

admits a concrete finite split:

```text
CLOSE  -> strong rank-one escape scale,
BAL    -> low internal pair defect,                                     (90-2)
```

and these two ingredients already cover the audited geometry regime.

## 0. Why this is the next honest move

E79.89 reduced the live front to the candidate implication

```text
CLOSE + BAL => GEOM.                                                    (90-3)
```

The natural next question is whether `GEOM` itself separates into two finite
mechanisms already present in the secular package:

```text
- outlier separation from the rank-one escape scale q^T x / c,
- internal cloud symmetry from residual balance.                        (90-4)
```

That is exactly what the old E78.155 escape calculation suggests, but it had
never been wired back into the new phase-79 discriminant chain.

## 1. Split predicates

Keep the audited predicates:

```text
CLOSE := |c_N| < 1e-5,
BAL   := R_net < 1e-6 and |log(R_pm)| < 0.1,
GEOM  := outlier_fraction > 5 and D_N < 5e-3.                          (90-5)
```

Now define two finite submechanisms:

```text
STRONG_ESCAPE := |(q^T x)/c| / mesh_radius > 50,                       (90-6)
LOW_DEFECT    := mean_pair_defect < 0.03.                              (90-7)
```

The intent is:

```text
STRONG_ESCAPE    captures the sharp-outlier side,
LOW_DEFECT       captures the symmetric-remainder side.                 (90-8)
```

## 2. Probe

Companion files:

```text
E79_90_escape_balance_split_probe.py
E79_90_escape_balance_split_results.json
```

The probe recomputes the full row metrics on the audited long ladder

```text
lambda=6, N=8..18, dps=60,                                             (90-9)
```

for zeta and the two planted controls, and audits:

```text
CLOSE => STRONG_ESCAPE,
BAL   => LOW_DEFECT,
GEOM  => STRONG_ESCAPE + LOW_DEFECT.                                   (90-10)
```

## 3. Result

On the audited ladder, the split behaves cleanly.

### Zeta

There is no audited zeta failure of either sub-implication:

```text
close->esc fails = [],
bal->def fails   = [].                                                  (90-11)
```

And there is no audited zeta row in `GEOM` lacking the split pair:

```text
geom without split = [].                                                (90-12)
```

Numerically, the pattern is sharp:

```text
escape_ratio ~ 135..53 on N=8..18,
mean_pair_defect ~ 0.018 down to ~0.014.                               (90-13)
```

So on the audited zeta ladder:

```text
CLOSE travels with strong escape,
BAL travels with low pair defect,
and together they already account for GEOM.                             (90-14)
```

### Planted controls

Neither planted control gives a contradictory row.

The `gamma1` ladder fails `CLOSE`, fails `BAL`, and never enters `GEOM`.
The `gamma2` ladder shows exactly why the split matters:

```text
its cloud-only resonant row has LOW_DEFECT,
but not STRONG_ESCAPE and not BAL.                                      (90-15)
```

So the resonance is not a counterexample to the split; it is the expected
partial imitation of only one half of `GEOM`.

## 4. Reading

This is still not a theorem, but it is a more structural reduction than E79.89.

Before this note, `GEOM` was still one compound audited predicate. After this
note, on the audited ladder it can be read as:

```text
GEOM ~= STRONG_ESCAPE + LOW_DEFECT,                                     (90-16)
```

with each half tied to one side of the left-hand premise:

```text
CLOSE -> STRONG_ESCAPE,
BAL   -> LOW_DEFECT.                                                    (90-17)
```

That is the first finite mechanism-level explanation of why the implication
from E79.89 should be true.

## 5. Consequence

The live discriminant burden shrinks one step further. The next honest target
is no longer the raw implication

```text
CLOSE + BAL => GEOM,                                                    (90-18)
```

but the more elementary pair:

```text
CLOSE => STRONG_ESCAPE,
BAL   => LOW_DEFECT.                                                    (90-19)
```

If those can be explained directly from the secular equation, then the
geometric gate becomes derivative rather than primitive.

## 6. Status

```text
proved by audit:
  on the audited long ladder, CLOSE has no counterexample to
  STRONG_ESCAPE, BAL has no counterexample to LOW_DEFECT, and the audited
  GEOM rows are all covered by STRONG_ESCAPE + LOW_DEFECT;

clarified:
  the cloud-only planted resonance mimics only the low-defect half and fails
  the escape half, exactly as the corrected discriminant picture predicts;

reduced:
  the live front from CLOSE + BAL => GEOM to the sharper mechanism-level
  pair CLOSE => STRONG_ESCAPE and BAL => LOW_DEFECT;

open:
  derive those two elementary implications from the secular package, or find
  the first audited-range obstruction if one appears under stricter scaling.
```
