# E79.115 - dps=70 breaks down at N>=28; the E79.114 tail was arithmetic noise

**Scope:** `DISCRIMINANT`, precision control on E79.114.
**Class:** AUTOPSIA HONESTA (voids a prior result, including one of my own leads).

## 1. Question

E79.114 extended the proxy ladder to `N=36` at `dps=70` and produced an
erratic zeta tail:

```text
alpha: N=32 -> 0.663,  N=34 -> 0.825,  N=36 -> 0.390.                  (115-1)
```

A factor-of-two swing between adjacent rows is not the behaviour of the
smooth sequence seen at `N<=26`. Before that could be called a breakdown of
the regime it had to be excluded as arithmetic noise.

Critically, the E79.113 dps control was run **only at N<=18**. It was never
evidence about `N=28..36`, though it had been cited as if the precision
question were settled.

## 2. Method

Recompute rows `N=26..36` at `dps = 70, 110, 150`. Declare a row STABLE only
if `alpha` agrees to `1e-12` relative across all three. Also record:

```text
sep_2_3     = |kappa_2| / |kappa_3|   (conditioning of second_abs),
max_abs_imag = max_j |Im kappa_j|     (E78.152 asserts kappa_j REAL).      (115-2)
```

## 3. Result - dps=70 is invalid from N=28 onward

```text
N     dps=70        dps=110       dps=150       rel spread   STABLE
26    0.333710179   0.333710179   0.333710179   8.9e-13      True
28    0.398655980   0.398655949   0.398655949   7.8e-08      False
30    0.380018474   0.379804859   0.379804859   5.6e-04      False
32    0.662676947   0.371718697   0.371718697   0.783        False
34    0.825093512   0.347447192   0.347447192   1.37         False
36    0.389899525   0.596604850   0.596604850   0.346        False      (115-3)
```

`dps=110` and `dps=150` agree exactly at every row. So the sequence is
converged by `dps=110`, and `dps=70` is simply wrong for `N>=28`.

```text
VERDICT: the E79.114 rows N=28..36 are VOID.
The honest ceiling of the dps=70 ladder is N=26.                       (115-4)
```

The E79.114 "erratic tail" does not exist. At converged precision the same
rows are smooth:

```text
N        26        28        30        32        34        36
alpha   0.33371   0.39866   0.37980   0.37172   0.34745   0.59660
gap     0.02892   0.05111   0.04248   0.03516   0.02536   0.09449
|g/a|   0.0867    0.1282    0.1119    0.0946    0.0730    0.1584       (115-5)
```

## 4. A lead of mine that this kills

While E79.115 was running I floated, from the `dps=70` partial output, the
suggestion that `sep_2_3` rising to `1.89` at `N=32` and `2.15` at `N=34`
indicated a **second eigenvalue beginning to escape**, and that this was a
more promising object than the proxy branch because it touches the E79.93
escape mechanism.

That is false. At converged precision:

```text
sep_2_3 @ dps=150:
  N=26: 1.317,  N=28: 1.392,  N=30: 1.371,
  N=32: 1.365,  N=34: 1.333,  N=36: 1.695.                             (115-6)
```

Flat. The apparent rise was `dps=70` garbage. **There is no second-escape
signal.** The lead is withdrawn; no work should be started on it.

The eigenvalues are also cleanly real at all audited rows
(`max_j |Im kappa_j| <= 6.2e-112` at `dps=150`), so E78.152's reality
assertion is not in question here and `mp.re(ev)` is not discarding anything.

## 5. What this does and does not do to E79.113

E79.113 ran at `dps=70` with rows `N=8..26`. Its top row `N=26` is STABLE
(`8.9e-13`), and instability grows with `N`, so its rows are inside the valid
range and **its numbers stand**. The margin at `N=26` is thin, however, and
rows `N=20,22,24` were not directly precision-tested.

The E79.113 conclusion that needs revisiting is the *interpretation*:

```text
E79.113 reported |gap/alpha| rising monotonically over N=20..26
  (0.0303, 0.0717, 0.0787, 0.0867)
and called the proxy "slowly degrading, not converging".               (115-7)
```

At converged precision the continuation does **not** keep rising:

```text
N=28: 0.1282 -> 30: 0.1119 -> 32: 0.0946 -> 34: 0.0730,               (115-8)
```

a monotone *decrease* over four rows, before `N=36` jumps to `0.1584`.

So the honest statement is neither E79.113's "degrading" nor a clean
convergence:

```text
|gap/alpha| rises to a local maximum near N=28, falls back through N=34,
then rises again at N=36. It oscillates in a band of roughly 0.03-0.16
with no established trend.                                             (115-9)
```

## 6. Status

```text
proved     : nothing (numerical control).
observed   : dps=70 invalid for N>=28; dps=110 sufficient through N=36;
             kappa_j real to 1e-112; sep_2_3 flat (~1.3-1.7), no second escape.
refuted    : E79.114 rows N=28..36 (VOID, computed at insufficient precision);
             the "second escape" lead (my own, withdrawn);
             E79.113's "monotone upward drift" as a trend claim -- the
             continuation falls for four rows.
open       : whether N=36's rise to 0.1584 is real or needs dps>150;
             whether |gap/alpha| has any trend at all, or just oscillates.
next       : if this branch is continued at all, recompute the WHOLE ladder
             N=8..38 at dps=150 in one internally consistent table, and
             verify N=36,38 at dps=200. Nothing else on this branch is
             worth doing on a mixed-precision basis.
```

## 7. Wall checklist

```text
K1-K5      : OK. Pure precision control, no new object.
E72.16     : N/A. DISCRIMINANT branch; no convergence claim made.
zero loc.  : OK. No zero LOCATION enters.
MW-1..6    : OK.
probe      : PRESENT (E79_115_large_row_precision_control_probe.py +
             _results.json).
```

## 8. Consequence

Two process lessons, both costly:

```text
1. A dps control is only evidence for the rows it was run on. The E79.113
   control covered N<=18 and was cited loosely for a ladder reaching N=36.
2. A verdict rule fixed in advance is worthless if its categories do not
   cover the outcome space. E79.114's rule mapped any non-monotonicity to
   "turns over", and so returned D-turns on data that was pure noise.   (115-10)
```

The residual-coherence branch has now consumed E79.106-E79.115 and has not
produced an object that bears on E79.5 or E79.6. That should weigh in any
decision to continue it.
