# E79.88 - A finite conjunctive gate excludes the cloud-only planted resonance

**Scope:** `DISCRIMINANT`, finite gate extracted from E79.83-E79.87.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the
structural correction of E79.87 can already be written as an explicit audited
conjunction of finite predicates. On the audited ladder, that conjunction is
passed by zeta and by neither planted control, including the cloud-only
resonant row.

## 0. Why this is the right next object

E79.87 clarified that the exceptional planted row was not a zeta-like event.
It was a cloud-only resonance:

```text
internal near-symmetry without small |c|,
without residual balance,
without a sharply detached outlier.                                     (88-1)
```

So the candid next step is to stop talking about this only conceptually and
write a finite gate that expresses exactly that correction.

## 1. Gate definition

Using the exact finite quantities already named in E79.83-E79.87, define three
predicates on a section row:

```text
CLOSE  := |c_N| < 1e-5,                                                 (88-2)
BAL    := R_net < 1e-6  and  |log(R_pm)| < 0.1,                         (88-3)
GEOM   := outlier_fraction > 5  and  D_N < 5e-3,                        (88-4)
```

where:

```text
c_N              = 1 - sum_j x_j,
R_net            = |sum_j r_j| / sum_j |r_j|,
R_pm             = (sum_{r_j>0}|r_j|) / (sum_{r_j<0}|r_j|),
outlier_fraction = |kappa_max|/|kappa_second|,
D_N              = mean_pair_defect / outlier_fraction.                 (88-5)
```

The conjunction

```text
ALL3 := CLOSE and BAL and GEOM                                          (88-6)
```

is the smallest finite gate that matches the corrected chain from E79.87.

## 2. Probe

Companion files:

```text
E79_88_conjunctive_gate_probe.py
E79_88_conjunctive_gate_results.json
```

The probe recomputes these quantities directly from the finite sections on the
audited `lambda=6`, `N=8,10,12`, `dps=60` ladder for:

```text
zeta,
plant gamma1, beta=0.30,
plant gamma2, beta=0.30.                                                (88-7)
```

## 3. Result

The conjunction separates exactly as intended on the audited rows.

### Zeta

All audited zeta rows pass all three predicates:

```text
N=8,10,12:  CLOSE=TRUE, BAL=TRUE, GEOM=TRUE, ALL3=TRUE.                 (88-8)
```

Numerically this is the familiar regime:

```text
|c_N| ~ 1e-7..1e-9,
R_net ~ 1e-12..1e-16,
R_pm ~ 1,
outlier_fraction ~ 11..14,
D_N ~ 1e-3.                                                             (88-9)
```

### Plant gamma1

No audited `gamma1` row passes the conjunction:

```text
ALL3_count = 0.                                                         (88-10)
```

In fact `CLOSE` and `BAL` fail on every audited row, while `GEOM` also fails on
every audited row because the outlier never enters the zeta-scale separation.

### Plant gamma2

No audited `gamma2` row passes the conjunction either:

```text
ALL3_count = 0.                                                         (88-11)
```

And this includes the resonant row isolated in E79.87:

```text
plant gamma2, N=12:
  CLOSE = FALSE  (|c| ~ 1.46e2),
  BAL   = FALSE  (R_net = 1, R_pm = 0),
  GEOM  = FALSE  (outlier_fraction ~ 1.16 even though the inner cloud is
                  very symmetric),
  ALL3  = FALSE.                                                        (88-12)
```

So the cloud-only resonance is excluded exactly where it should be.

## 4. Reading

This is not yet the theorem-grade discriminant, and the thresholds are only an
audited finite normalization. But it is already a useful structural reduction.

The important point is not the specific constants `1e-5`, `1e-6`, `0.1`, `5`,
`5e-3` by themselves. The important point is that the corrected chain from
E79.87 can already be expressed as:

```text
zeta mechanism = closure + balance + geometry,
resonant plant = geometry-like feature without closure/balance.         (88-13)
```

That is exactly the distinction the previous scalar proxies were missing.

## 5. Consequence

After E79.88, the live discriminant burden sharpens again:

```text
the next theorem-grade target is not D_N alone, nor cloud symmetry alone,
but a structural implication toward the conjunction CLOSE + BAL + GEOM.  (88-14)
```

Equivalently, the next candid reduction is:

```text
small |c_N| + residual balance
  => the zeta cloud enters the sharp-outlier / tiny-D_N regime,         (88-15)
```

or else an autopsy that names which part of that implication is false.

## 6. Status

```text
proved by audit:
  the corrected E79.87 picture can be encoded as a finite conjunction
  of closure, residual balance, and cloud geometry predicates;

proved by audit:
  all audited zeta rows pass that conjunction, while neither planted control
  does, including the cloud-only resonant row;

clarified:
  the exceptional planted row is excluded for the right reason:
  it lacks closure and balance, not because the inner cloud fails to mimic
  symmetry locally;

reduced:
  the next live discriminant object to a structural route toward
  CLOSE + BAL + GEOM, rather than toward D_N alone;

open:
  prove the bridge from closure/balance to the geometric regime, or name
  the next finite obstruction if that bridge breaks.
```
