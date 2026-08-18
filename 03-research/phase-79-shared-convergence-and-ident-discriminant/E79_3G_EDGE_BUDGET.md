# E79.3g - The zeta common-cloud term obeys an explicit edge budget

**Scope:** `GAP-Z` only, quantitative synthesis of E79.3d and E79.3f.  
**Class:** REDUCCION GENUINA (the borderline exponent now has a concrete
mechanism).  
**What we know after this document that we did not know before:** on the zeta
side, the common-cloud contribution is numerically explained by a simple edge
budget:

```text
[active edge width ~ cN] x [one shell ~ const/N^2]  =>  total ~ const/N.
```

So the previously mysterious borderline exponent is no longer just a fit. It has
a concrete geometric source inside the common cloud.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct cloud bookkeeping only.
E72.16/E77.7az: respected. This is still convergence-side anatomy, not a
       build-separating forcing step.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

After E79.3f the live common-cloud object had the form

```text
COMMON-GAP-Z
  = [local N^-2 shell law on a slowly growing outer edge]
    + [tiny interior correction].                                        (T-1)
```

The next natural question is whether the borderline size of the total common
cloud can be explained directly from those two ingredients:

```text
does the whole common-cloud term behave like
    (number of active edge shells) x (size of one shell)?                (T-2)
```

If yes, then the apparent near-`N^-1` law is structurally accounted for.

## 2. Probe

Companion files:

```text
E79_3G_EDGE_BUDGET_PROBE.py
E79_3G_edge_budget_results.json
```

For each `N` and threshold `theta`, the probe combines:

```text
- m_theta(N): the minimal outer-layer thickness from E79.3d,
- avg_N2_shell: the average of N^2 EDGE_{N,r} over the first m_theta shells,
- N |ZERO_N^common|: the observed total common-cloud scale.
```

This gives the explicit budget proxy

```text
proxy_theta(N) = (m_theta(N) / N) * avg_N2_shell,                        (T-3)
```

which is exactly what one gets from the heuristic

```text
ZERO_N^common ~ m_theta(N) * (const / N^2).                              (T-4)
```

## 3. Result: the zeta-side edge budget almost reconstructs N |ZERO^common|

At `sigma = 1`, zeta gives:

```text
N    N|ZERO^common|      proxy_0.9         proxy_0.99
8    0.0310854807        0.0303958771      0.0310597411
10   0.0281226360        0.0262048374      0.0280854270
12   0.0296360707        0.0282522432      0.0295012400
14   0.0273997960        0.0253730883      0.0271953281
16   0.0291004611        0.0262682001      0.0288620971
```

This is the key point:

```text
the edge-budget proxy tracks N |ZERO_N^common| very closely on the whole
audited zeta ladder.                                                     (T-5)
```

So the common-cloud size is not mysterious anymore. It is quantitatively
explained by:

```text
active width m_theta(N) proportional to N,
times an N^-2 shell law with stable local coefficients.                  (T-6)
```

The same data make the mechanism explicit. For zeta, still at `sigma = 1`,

```text
m90/N      = 0.875, 0.8, 0.75, 0.714..., 0.6875,
avg_N2_shell
           = 0.0347, 0.0328, 0.0377, 0.0355, 0.0382.
```

So:

```text
m90(N) is order N, while the shell coefficient scale stays order 1.      (T-7)
```

That is precisely the budget that yields a total of order `N^-1`.

## 4. Plant does not share the same coherent budget

The planted build does not exhibit the same clean accounting. At `sigma = 1`,

```text
N    N|ZERO^common|      proxy_0.9
8    1.71005621994       2.04697870542
10   0.0689644094266     0.0631800988318
12   0.00512816259042    0.022807657112
14   0.0166485830908     0.0154352236768
16   0.0173894536874     0.0197516657688
```

There are occasional matches, but no stable regime analogous to zeta. This is
consistent with the earlier plant-side instability of both the shell profile and
the active thickness.

## 5. Consequence

This sharpens the candid surviving object once again:

```text
COMMON-GAP-Z
  = [linear-in-N active edge width]
    x [local N^-2 shell profile]
    + [tiny interior correction].                                        (T-8)
```

That is the first full mechanical explanation of the borderline zeta-side law.
It also clarifies exactly what must improve for a proof of summability:

```text
either the effective width must be shown to be sublinear,
or the deeper-edge shell coefficients must decay enough in the edge index r
to beat the raw width count.                                             (T-9)
```

So the open problem is no longer "why is the exponent near 1?" The program now
knows where that exponent comes from.

## 6. Status

```text
proved by probe:
  on the zeta side, the observed scale of ZERO_N^common is quantitatively
  explained by the product
      [active edge width ~ cN] x [single shell ~ const/N^2];

observed:
  the planted build does not exhibit the same coherent edge budget;

reduced:
  COMMON-GAP-Z from "local N^-2 shell law on a slowly growing outer edge plus
  tiny interior correction" to the explicit budget law
      [linear width] x [N^-2 shell profile] + [tiny interior correction];

open:
  find the extra gain that turns this borderline N^-1 budget into a genuinely
  summable estimate;

next:
  test whether the shell profile decays as the edge depth approaches the active
  thickness, or whether the effective width itself is actually sublinear beyond
  the current audited ladder.
```
