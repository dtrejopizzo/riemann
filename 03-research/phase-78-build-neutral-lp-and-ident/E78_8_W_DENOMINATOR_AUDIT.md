# E78.8 - Denominator audit for the coupled-generator package

**Run:** 2026-07-18.
**Target:** the zero-free denominator clause in the Phase-78 reduction

```text
W-QUOTIENT-DELTA + |1+W| >= c_K > 0
=> fixed-L convergence of the cell-smoothed symbol.
```

## 1. Purpose

E78.6 and E78.7 reduced the fixed-L arithmetic front to the quotient

```text
W'_{L,N}(i sigma) / (1+W_{L,N}(i sigma)).
```

This note audits the denominator

```text
F_{L,N}(i sigma)=1+W_{L,N}(i sigma)
```

on the safe axis for both the zeta and planted builds.  The goal is to decide
whether denominator collapse is itself a live obstruction or merely a side
condition that stays healthy in practice.

## 2. Probe

Companion:

```text
E78_8_w_denominator_probe.py
E78_8_w_denominator_results.json
```

Using the exact two-generator package from E77.3c / P76.041, the probe computes
for each finite section and each safe sample point:

```text
F_{L,N}(i sigma)=1+W_{L,N}(i sigma).
```

It records

```text
min_{sigma in grid} |F_{L,N}(i sigma)|
```

for both builds.

## 3. Status

## 3. Results

With `lambda=6`, safe grid

```text
sigma in {0.55,0.6,0.75,1.0,1.5,2.0,3.0},
```

and sections `N=8,10,12,14`, the minimum safe-axis denominator size is:

### Zeta

```text
N= 8   min |1+W| = 7.10e5
N=10   min |1+W| = 1.68e6
N=12   min |1+W| = 1.09e10
N=14   min |1+W| = 2.18e10.
```

### Planted build

```text
N= 8   min |1+W| = 20.54
N=10   min |1+W| = 6.64
N=12   min |1+W| = 54.92
N=14   min |1+W| = 213.40.
```

So in the tested safe window the denominator is not merely nonzero; it stays
macroscopically separated from zero in both builds.

## 4. Reading

This is strong evidence that denominator collapse is **not** the active
arithmetic obstruction.

More precisely:

```text
1. zeta does not approach the target through a near-pole regime;
2. the planted build also does not fail by making 1+W vanish;
3. therefore the build separation inside IDENT is not carried by the
   denominator, but by the quotient dynamics
      W'/(1+W)
   itself.
```

This is exactly the desired outcome for the Phase-78 reduction: the side
condition needed in E78.6/E78.7 is healthy, so the live front stays on the
invariant quotient-delta rather than spawning a second denominator front.

## 5. Consequence

The honest live arithmetic object is now:

```text
W-QUOTIENT-DELTA,
```

with denominator separation archived as a non-active side condition on the
tested safe ladder.

No evidence remains that `|1+W|` itself is where IDENT breaks.

## 6. Status

```text
observed:
  |1+W| stays far from zero on the tested safe axis for both zeta and planted
  builds;

clarified:
  denominator collapse is not the active obstruction in IDENT;

reduced:
  the live fixed-L arithmetic object remains W-QUOTIENT-DELTA, not a separate
  denominator-separation theorem;

next:
  derive a shell law or summable envelope for
  Delta[W'/(1+W)]
  on safe compacta.
```
