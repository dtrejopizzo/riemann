# E78.93 - `U-RADIAL-GAP` is the rigid half of the weighted-gap split

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.92 reduced the endpoint weighted modulus quotient to

```text
W_N(sigma) = PREF_N(sigma) / U-RADIAL-GAP_N(sigma).     (GVP-1)
```

The next candid question is:

```text
which side of this quotient is structurally rigid enough to pursue first? (GVP-2)
```

This note answers that directly.

## 2. Audit criteria

The comparison is simple:

```text
1. internal organization on the certified zeta ladder;
2. behavior under the standard planted falsifier.       (GVP-3)
```

The side that is both orderly on zeta and unstable on the falsifier is the
correct next theorem-grade object.

## 3. Probe audit

Companion:

```text
E78_93_gap_vs_prefactor_probe.py
E78_93_gap_vs_prefactor_results.json
```

### Zeta

For `U-RADIAL-GAP_N`, the organization is very clean.

At each audited sigma slice:

```text
sigma=1.0:
  0.921090, 0.637392, 0.472324, 0.369516,
  0.312124, 0.244040, 0.152534                    (strictly decreasing)

sigma=3.0:
  0.877520, 0.616667, 0.471362, 0.373403,
  0.305329, 0.260538, 0.212595                    (strictly decreasing). (GVP-4)
```

So on the full certified zeta ladder:

```text
U-RADIAL-GAP_N is sigma-slice monotone and strictly positive. (GVP-5)
```

By contrast, `PREF_N` is only partially organized:

```text
sigma=1.0:
  2.358724, 1.399994, 1.221541, 0.795455,
  0.803383, 0.576331, 0.342817                    (not monotone)

sigma=3.0:
  2.152594, 1.310792, 1.187573, 0.782239,
  0.780989, 0.592388, 0.411475                    (monotone).         (GVP-6)
```

So `PREF_N` still oscillates even on the healthy branch.

### Planted falsifier

The falsifier location is even more decisive.

`U-RADIAL-GAP_N` already fails coherently:

```text
plant gap min = -0.908427,                                  (GVP-7)
```

so the planted branch can cross below zero at the exact source of the `u`
growth law.

Meanwhile `PREF_N` is far less rigid: it changes sign, ranges wildly, and is
strongly contaminated by the unstable factors `-SAFEDELTA_N` and `s_N+2`.

Representative planted rows:

```text
sigma=1.0, N=12:  gap = -0.908427,   pref = +164.412
sigma=1.0, N=18:  gap = 75.979715,   pref = -2638.601
sigma=3.0, N=10:  gap = 11.333212,   pref = -1763.151.   (GVP-8)
```

So the prefactor is not the stable half of the split. It is the noisy half.

## 4. Consequence

This yields the admissible refinement

```text
U-RADIAL-GAP-LOWER-BOUND
is the primary modulus-growth target,

PREF-CONTROL
is secondary bookkeeping.                               (GVP-9)
```

In particular, the endpoint branch from E78.92 should now be read as

```text
PRIMARY:   U-RADIAL-GAP-LOWER-BOUND,
SECONDARY: PREF-CONTROL.                                (GVP-10)
```

That is a genuine narrowing of the burden, not a mere rephrasing:
`U-RADIAL-GAP_N` is the part that is both internally organized on zeta and
structurally broken by the falsifier.

## 5. Candid reading

This note does **not** prove the lower bound cofinally.

What it proves is that, among the two exact pieces from E78.92, the correct one
to chase first is not ambiguous anymore.

The rigid side is the radial gap itself.

## 6. Status

```text
observed:
  U-RADIAL-GAP_N is strictly positive and sigma-slice monotone on the certified
  zeta ladder;

observed:
  PREF_N still oscillates on the healthy sigma=1.0 branch;

observed:
  the planted falsifier already breaks U-RADIAL-GAP_N by sign loss, while
  PREF_N is merely noisy and sign-unstable;

clarified:
  the primary live modulus-growth target is U-RADIAL-GAP-LOWER-BOUND, with
  PREF-CONTROL demoted to secondary bookkeeping;

next:
  search for a theorem-grade lower mechanism for U-RADIAL-GAP_N from the shell
  quotient laws of theta' and 1-theta.
```
