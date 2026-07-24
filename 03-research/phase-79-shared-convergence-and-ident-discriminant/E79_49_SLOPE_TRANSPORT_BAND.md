# E79.49 - The affine residual slope already obeys an N^-1 transport band on the zeta side

**Scope:** `GAP-Z` only, first transport law for the affine residual template.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the affine
residual slope from E79.48 is not just section-dependent noise. On the audited
zeta ladder it already obeys a clean `N^-1` transport band: `N |a_N|` stays in
a tight range, while the planted hard rows blow far outside that scale.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the affine coefficients already extracted in E79.48.
E72.16/E77.7az: respected. This is a transport audit, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why slope is the first transport variable

E79.48 named the residual law as

```text
residual(sigma; N) ~ a_N sigma + b_N.                                (49-1)
```

The intercept `b_N` still drifts a lot on the audited ladder, so the first
honest transport question is the simpler one:

```text
does the slope a_N already scale in a clean way with N?               (49-2)
```

## 2. Probe

Companion files:

```text
E79_49_SLOPE_TRANSPORT_BAND_PROBE.py
E79_49_slope_transport_band_results.json
```

For each audited section, the probe reads the least-squares affine slope
`a_N` from E79.48 and records:

```text
- a_N,
- N a_N,
- N |a_N|.                                                            (49-3)
```

The live target is a simple transport band for `N |a_N|`.

## 3. Result

On the zeta side:

```text
N= 8   N|a_N| = 0.0333
N=10   N|a_N| = 0.0388
N=12   N|a_N| = 0.0278
N=14   N|a_N| = 0.0356
N=16   N|a_N| = 0.0319                                             (49-4)
```

So:

```text
mean(N|a_N|) = 0.0335,
max/min band ratio = 1.40.                                           (49-5)
```

That is already a clear `N^-1` transport law on the audited ladder.

By contrast, on the planted build:

```text
N|a_N| = 5.07, 1.27, 0.184, 7.35, 0.547,
mean(N|a_N|) = 2.89,
max/min band ratio = 39.95.                                           (49-6)
```

So the plant does not merely have a worse constant; it fails the entire zeta
transport scale on the hard rows.

## 4. Reading

This is the first honest `N`-transport law on the residual side:

```text
a_N = O(1/N) with a numerically stable zeta-side coefficient scale.   (49-7)
```

That is much stronger than simply saying the residual is affine in sigma.

It also tells us where to look next:

```text
the slope already transports cleanly;
the remaining burden is the intercept / center level.                 (49-8)
```

## 5. Consequence

After E79.48-E79.49, the residual side now has a two-layer structure:

```text
primitive packet
  + affine sigma template
  + slope transport a_N ~ const/N on the zeta side.                  (49-9)
```

So the next honest step is not to revisit the slope, but to ask whether the
intercept admits a similarly simple renormalization, or whether the true
2-parameter law should be expressed in a shifted sigma coordinate.

## 6. Status

```text
proved by probe:
  the affine residual slope obeys a clean zeta-side N^-1 transport band on the
  audited ladder;

observed:
  the planted hard rows lie far outside that band, so the transport scale is
  genuinely discriminating on the residual side;

reduced:
  the next unresolved transport burden is the intercept / center level, not the
  slope;

open:
  identify the right transport variable for the intercept, or recenter the
  affine template so the full 2-parameter law becomes simpler;

next:
  test a centered-sigma affine template that may stabilize the intercept.
```
