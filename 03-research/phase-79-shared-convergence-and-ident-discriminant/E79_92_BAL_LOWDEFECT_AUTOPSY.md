# E79.92 - `BAL => LOW_DEFECT` is too strong: low internal defect can occur without strong residual balance

**Scope:** `DISCRIMINANT`, autopsy of the second half of E79.90.  
**Class:** AUTOPSIA HONESTA.  
**What we know after this document that we did not know before:** the candidate
mechanism-level implication

```text
BAL => LOW_DEFECT                                                       (92-1)
```

is too strong as a theorem target. On the audited planted ladders, low internal
pair defect can already occur without the near-perfect residual balance that
zeta exhibits.

## 0. Why this autopsy is necessary

E79.90 split the geometry mechanism into:

```text
CLOSE => STRONG_ESCAPE,
BAL   => LOW_DEFECT.                                                    (92-2)
```

The first half survived E79.91 and became more precise. The second half needed
its own direct audit before being promoted.

That audit was done by reading the already-certified section data from
E79.90. The conclusion is not ambiguous: `LOW_DEFECT` is not exclusive to the
strong zeta-side balance regime.

## 1. The decisive rows

On the audited zeta ladder:

```text
R_net ~ 1e-12 down to 1e-22,
|log(R_pm)| ~ 0,
mean_pair_defect ~ 0.018 down to 0.014.                                (92-3)
```

So zeta certainly satisfies both `BAL` and `LOW_DEFECT`.

But the planted ladders already show the failure of the proposed implication as
a useful sharp mechanism:

### Plant gamma1

```text
N=10: R_net ~ 0.541, |log(R_pm)| ~ 1.21, mean_pair_defect ~ 0.0227,
N=12: R_net ~ 0.211, |log(R_pm)| ~ 0.429, mean_pair_defect ~ 0.0119,
N=18: R_net ~ 0.133, |log(R_pm)| ~ 0.267, mean_pair_defect ~ 0.00678.  (92-4)
```

These rows are **not** balanced in the zeta sense, yet they already lie in the
low-defect regime.

### Plant gamma2

```text
N=12: R_net = 1,   |log(R_pm)| = inf,   mean_pair_defect ~ 0.0158,
N=14: R_net ~ 0.562, |log(R_pm)| ~ 1.27, mean_pair_defect ~ 0.0220,
N=18: R_net ~ 0.348, |log(R_pm)| ~ 0.726, mean_pair_defect ~ 0.00608.  (92-5)
```

Again the same phenomenon: very weak or nonexistent balance can coexist with a
small internal pair defect.

So the resonance pattern from E79.87 was not isolated to one row. The planted
ladders can repeatedly imitate the **low-defect half** of the geometry without
entering anything like zeta-side balance.

## 2. What survives

The failed implication does not destroy the whole phase-79 reduction. What
survives is more nuanced and still useful:

```text
- strong zeta-side BAL travels with LOW_DEFECT;
- LOW_DEFECT by itself does not identify zeta;
- the genuinely discriminating geometry lives in
    STRONG_ESCAPE + LOW_DEFECT,
  not in LOW_DEFECT alone.                                              (92-6)
```

This is exactly consistent with E79.87-E79.91:

```text
the planted side can imitate the symmetric-remainder half,
but not the denominator-driven escape half.                             (92-7)
```

## 3. Structural correction to E79.90

The mechanism-level picture must therefore be revised from

```text
CLOSE => STRONG_ESCAPE,
BAL   => LOW_DEFECT.                                                    (92-8)
```

to the weaker but honest statement

```text
CLOSE => STRONG_ESCAPE      survives as the main live reduction,
LOW_DEFECT is only a permissive geometric subfeature,
not a balance-forced discriminant by itself.                            (92-9)
```

So the live front does **not** compress all the way to two symmetric elementary
implications. It compresses asymmetrically:

```text
one side (escape) is genuinely constrained by closure,
the other side (low defect) is too permissive to carry arithmetic content
without the escape half attached.                                       (92-10)
```

## 4. Consequence

After this autopsy, the honest next target is not

```text
BAL => LOW_DEFECT.                                                      (92-11)
```

That target should be retired.

The right replacement is:

```text
identify what extra ingredient, beyond low internal defect, distinguishes
the zeta-side geometry from the planted mimics.                         (92-12)
```

Given E79.91, the obvious surviving candidate is that the true discriminating
content lives on the **escape side**, with low defect acting only as a
background compatibility condition.

## 5. Status

```text
refuted by audit:
  the mechanism-level target BAL => LOW_DEFECT is too strong;

proved by audit:
  planted rows can exhibit LOW_DEFECT with only weak balance or no balance at
  all, so LOW_DEFECT alone is not arithmetic content;

clarified:
  the discriminating geometry remains the conjunction
  STRONG_ESCAPE + LOW_DEFECT, with the escape half carrying the real rigidity;

reduced:
  the live front to the denominator-driven escape mechanism on one side, and a
  search for the right non-permissive companion to low defect on the other;

next:
  stop pursuing BAL => LOW_DEFECT as a proof target and instead test whether
  the zeta-only content on the geometry side is already exhausted by the
  escape mechanism.
```
