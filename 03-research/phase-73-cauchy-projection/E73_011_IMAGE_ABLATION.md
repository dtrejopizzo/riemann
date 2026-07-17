# E73.011 - Image ablation

## 1. Purpose

E73.010 identifies a low-rank structured image.  This note tests which parts of the `RAT-DD_2`
dictionary generate that image.

## 2. Result

The ablation results are recorded in `E73_011_RESULTS.md`.  The main findings are:

```text
r=1 and r=2 separately already capture most of the source;
single critical family crit0 is much better than other single critical families;
crit0+crit4 recovers essentially the full all-p2 distance;
individual off-node families are nearly interchangeable.
```

Thus the stable object is not the full raw dictionary.  It appears to be an endpoint-critical image:

```text
critical endpoint divided differences + one representative off-node rational denominator.
```

## 3. Updated ansatz

Replace the large dictionary by the smaller canonical class

```text
EC-RAT-DD:
span{DD_L(-gamma_min,d), DD_L(-gamma_max,d)}
  multiplied by the first two rational denominator powers.
```

The off-node denominator choice seems to change conditioning more than span, so the next proof object
should use a symmetric off-node denominator product rather than separate redundant denominators.

## 4. Status

```text
observed: low-rank image is generated mainly by endpoint critical families;
next: build a symmetric endpoint-critical basis and test IMAGE-RANK again.
```

