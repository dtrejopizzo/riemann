# E79.3h - The edge budget survives the extended ladder through N=24

**Scope:** `GAP-Z` only, extended audit of the E79.3g mechanism.  
**Class:** REDUCCION GENUINA (the edge-budget mechanism survives beyond the
short ladder).  
**What we know after this document that we did not know before:** the zeta-side
edge budget is not a short-range artifact of `N <= 16`. It remains coherent
through `N = 24`, with `N |ZERO^common|` staying in a narrow band and the edge
proxy continuing to track it closely.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct cloud bookkeeping only.
E72.16/E77.7az: respected. This is convergence-side anatomy, not a forcing step.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

E79.3g gave the first mechanical explanation of the borderline common-cloud law:

```text
[active edge width ~ cN] x [one shell ~ const/N^2]  =>  total ~ const/N.  (T-1)
```

But that audit only lived on the short ladder `N = 8,10,12,14,16`. The obvious
question was:

```text
does the same mechanism survive when the ladder is extended to N=24?      (T-2)
```

If not, the whole budget picture could still have been a short-range mirage.

## 2. Probe

Companion file:

```text
E79_3H_extended_edge_budget_results.json
```

This is an extended run of the E79.3g budget probe with

```text
max_n = 26, dps = 60,
rows N = 8,10,12,14,16,18,20,22,24,
both builds.                                                             (T-3)
```

The quantities audited are the same as in E79.3g:

```text
N |ZERO_N^common|,
m_theta(N) / N,
proxy_theta(N) = (m_theta(N)/N) * avg_N2_shell.                          (T-4)
```

## 3. Result: the zeta-side budget is stable through N=24

At `sigma = 1`, zeta gives:

```text
N    N|ZERO^common|      m90/N          proxy_0.9
8    0.0310854807        0.8750000000   0.0303958771
10   0.0281226360        0.8000000000   0.0262048374
12   0.0296360707        0.7500000000   0.0282522432
14   0.0273997960        0.7142857143   0.0253730883
16   0.0291004611        0.6875000000   0.0262682001
18   0.0279074761        0.7222222222   0.0261309902
20   0.0247075789        0.6500000000   0.0227441151
22   0.0291479649        0.7272727273   0.0269222759
24   0.0265871019        0.6250000000   0.0240402060
```

This is the key extended-ladder fact:

```text
N |ZERO_N^common| stays in the narrow band 0.0247 - 0.0311 all the way from
N=8 to N=24.                                                            (T-5)
```

Its mean over the whole audited ladder is

```text
mean_N [N |ZERO_N^common|] = 0.02819...                                 (T-6)
```

and the `0.9`-budget proxy continues to track it closely throughout.

## 4. No sign yet of superlinear width pressure

The second useful fact is that the effective relative width does **not** drift
upward on the extended ladder. For zeta:

```text
m90/N = 0.875, 0.8, 0.75, 0.714..., 0.6875, 0.722..., 0.65, 0.727..., 0.625.
```

So the data do **not** suggest that the active width is getting worse than
linear as `N` grows. If anything, the relative width slightly relaxes along the
extended run.

That matters because it narrows the honest options for beating the borderline
budget:

```text
the extra gain is unlikely to come from some hidden superlinear collapse in the
active width already visible on this ladder.                             (T-7)
```

## 5. Plant remains incoherent under the same extension

The planted build shows no analogous clean regime on the same extended ladder.
Its width ratios and budget proxies continue to wander without the zeta-side
stability.

So the extended run reinforces, rather than weakens, the structural split:

```text
zeta has a coherent borderline edge budget;
plant does not exhibit the same stable mechanism.                        (T-8)
```

## 6. Consequence

This extended audit tightens the live object one more time:

```text
COMMON-GAP-Z
  = [extended-ladder-stable linear edge width]
    x [extended-ladder-stable local N^-2 shell profile]
    + [tiny interior correction].                                        (T-9)
```

That is stronger than E79.3g because the mechanism is now seen to persist well
beyond the original short ladder. So the program can stop treating the
borderline exponent as a fragile small-N phenomenon.

The honest remaining question is now sharper:

```text
where does the extra gain come from that beats this stable linear-width times
N^-2-shell budget?                                                      (T-10)
```

At this point there are really only two plausible places left:

```text
1. decay of shell coefficients deeper into the active edge,
2. a more refined effective width notion than the crude m_theta count.   (T-11)
```

## 7. Status

```text
proved by probe:
  the zeta-side edge budget of E79.3g survives the extended ladder through
  N=24, with N |ZERO_N^common| staying in a narrow band and the edge proxy
  continuing to track it closely;

observed:
  the active width ratio m90/N does not drift upward on the extended ladder;

reduced:
  COMMON-GAP-Z from a short-ladder edge-budget picture to an extended-ladder-
  stable edge-budget law;

open:
  identify the extra gain that beats the stable borderline budget;

next:
  test decay of shell coefficients as the edge depth approaches the active
  thickness, to see whether the effective edge mass is smaller than the raw
  width count suggests.
```
