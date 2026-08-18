# E78.21 - Sign-coherent balance reduces the denominator defect to a ratio defect

**Run:** 2026-07-18.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.20 identified the denominator side condition as

```text
BALANCED-DENOMINATOR:
  control |Q_logT| / |Q_ext| on a cofinal envelope.       (SB-1)
```

This note observes that on the audited zeta rows there is an additional exact
feature:

```text
Q_ext and Q_logT have the same sign.                      (SB-2)
```

Under `(SB-2)`, the defect is not merely bounded by the ratio imbalance; it is
**exactly equal** to it after normalization by `|Q_ext|`.

## 2. Exact identity under sign coherence

Assume

```text
Q_ext,N Q_logT,N >= 0.                                    (SB-3)
```

Then

```text
|Q_ext,N - Q_logT,N|
 = ||Q_ext,N| - |Q_logT,N||.                              (SB-4)
```

Divide by `|Q_ext,N|` (when nonzero):

```text
|Q_ext,N - Q_logT,N| / |Q_ext,N|
 = |1 - |Q_logT,N|/|Q_ext,N||.                            (SB-5)
```

Using E78.20 notation,

```text
DEFECT-OVER-EXT_N := |Q_N|/|Q_ext,N|                      (SB-6)
RATIO_N := |Q_logT,N|/|Q_ext,N|,                          (SB-7)
```

so `(SB-5)` becomes

```text
DEFECT-OVER-EXT_N = |1 - RATIO_N|                         (SB-8)
```

whenever sign coherence holds.

This is stronger than E78.20's comparability statement: it says the defect is
literally the distance of the balanced ratio from `1`.

## 3. Probe audit

Companion:

```text
E78_21_sign_coherent_balance_probe.py
E78_21_sign_coherent_balance_results.json
```

The probe reads the certified E77.5y rows and checks:

```text
- whether Q_ext and Q_logT have the same sign;
- whether (SB-8) reconstructs the defect on same-sign rows.
```

### Zeta

On the audited zeta rows:

```text
same-sign count      = 12
opposite-sign count  = 0
max reconstruction error in (SB-8) = 0.
```

Representative rows:

```text
sigma=1.0, N=10:
  |Q_logT|/|Q_ext| = 1.018784
  |Q_N|/|Q_ext|    = 0.018784
  exact via |1-r|  = 0.018784

sigma=3.0, N=14:
  |Q_logT|/|Q_ext| = 1.038876
  |Q_N|/|Q_ext|    = 0.038876
  exact via |1-r|  = 0.038876
```

So on the current zeta ladder the denominator defect is exactly a ratio-to-one
defect.

### Planted build

The planted build does not preserve sign coherence:

```text
same-sign count      = 8
opposite-sign count  = 4.
```

The failures occur precisely where `Q_logT` changes sign relative to `Q_ext`.
On those rows `(SB-8)` is not available, which is why E78.20's weaker balance
form is the right unconditional formulation.

## 4. Consequence

Together with E78.20:

```text
SIGN-COHERENT-BALANCE:
  sign coherence of (Q_ext,Q_logT)
  + cofinal ratio control RATIO_N -> 1

=> DEFECT-OVER-EXT_N -> 0                                  (SB-9)
=> LOGT-CANCEL-COFINAL, via E78.20/E78.19.               (SB-10)
```

This is a genuine simplification of the live target. The denominator side
condition is no longer just "bounded away from collapse"; under sign coherence
it becomes:

```text
show that |Q_logT|/|Q_ext| tends to 1.
```

That is a much sharper and more interpretable object.

## 5. Candid reading

This note does **not** prove sign coherence on a cofinal envelope, and it does
not yet prove `RATIO_N -> 1`.  What it proves is that if those two facts hold,
then the normalized defect is exactly the distance of that ratio from `1`.

So the front contracts one more time:

```text
from generic denominator balance
to sign-coherent ratio-to-one control.
```

This is particularly aligned with the ledger discipline because it distinguishes
the zeta rows from the plant in an exact way:

```text
zeta keeps sign coherence on the audited ladder;
the plant loses it on a nontrivial subset of rows.
```

## 6. Status

```text
proved:
  under sign coherence, the normalized defect is exactly |1-r| with
  r=|Q_logT|/|Q_ext|;

proved:
  all audited zeta rows satisfy sign coherence, with exact reconstruction
  error zero;

observed:
  the planted build fails sign coherence on part of the ladder;

reduced:
  BALANCED-DENOMINATOR to the sharper target
    SIGN-COHERENT-BALANCE = sign coherence + ratio-to-one control;

next:
  derive sign coherence and ratio-to-one from the exact shell/Schur formulas,
  rather than from the certified rows alone.
```
