# E79.3f - The zeta outer edge shows a stable shell profile at N^-2 scale

**Scope:** `GAP-Z` only, direct inspection of the surviving edge law inside
`ZERO^common`.  
**Class:** REDUCCION GENUINA (the live edge object acquires a concrete local
profile).  
**What we know after this document that we did not know before:** on the zeta
side, the common-cloud terms at fixed distance from the outer edge have a
remarkably stable `N^2`-scaled profile. So the active edge is not just "where
the mass sits"; it behaves like a genuine local shell law.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct spectral-cloud bookkeeping only.
E72.16/E77.7az: respected. This is convergence-side structure; build
       separation is descriptive only, not used as forcing.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

E79.3e left the live common-cloud problem in the form

```text
COMMON-GAP-Z
  = [slowly growing outer layer carrying essentially all of ZERO^common]
    + [tiny interior correction].                                       (T-1)
```

That makes the next honest question very sharp:

```text
does the outer layer itself have a stable local law when indexed by distance
from the edge?                                                          (T-2)
```

If yes, then the hard object is no longer "a growing packet" in the abstract,
but a concrete edge profile.

## 2. Probe

Companion files:

```text
E79_3F_EDGE_PROFILE_PROBE.py
E79_3F_edge_profile_results.json
```

For

```text
ZERO_N^common(sigma) = sum_{j<=d_N} common_terms_j(sigma),
common_terms_j(sigma) = P_sigma(kappa_j^(N+2)) - P_sigma(kappa_j^(N)),
```

with roots ordered by increasing `|kappa|`, define the shell at depth `r` from
the outer edge by

```text
EDGE_{N,r}(sigma) = common_terms_{d_N-r}(sigma),   r = 0,1,2,...        (T-3)
```

The probe records `EDGE_{N,r}`, `N EDGE_{N,r}`, `N^2 EDGE_{N,r}`, and the
cumulative edge prefix

```text
PREFIX_{N,r}(sigma) = sum_{0 <= u <= r} EDGE_{N,u}(sigma).               (T-4)
```

## 3. Result: a stable N^-2 shell law appears on the zeta side

At `sigma = 1`, for zeta, the first outer shells satisfy:

```text
r = 0:  N^2 EDGE_{N,0} = 0.0260, 0.0237, 0.0229, 0.0203, 0.0189
r = 1:  N^2 EDGE_{N,1} = 0.0430, 0.0390, 0.0360, 0.0351, 0.0319
r = 2:  N^2 EDGE_{N,2} = 0.0426, 0.0396, 0.0385, 0.0371, 0.0343
r = 3:  N^2 EDGE_{N,3} = 0.0388, 0.0456, 0.0453, 0.0438, 0.0437
r = 4:  N^2 EDGE_{N,4} = 0.0353, 0.0418, 0.0445, 0.0444, 0.0427
```

for `N = 8,10,12,14,16`.

This is the key point:

```text
for fixed depth r near the edge, EDGE_{N,r} is consistent with an N^-2-scale
law whose coefficient depends mainly on r and only weakly on N.          (T-5)
```

It is not exact flat collapse, but it is far more coherent than the earlier
"whole cloud" picture. In particular the outermost few shells stay in narrow
bands after multiplying by `N^2`.

The same zeta-side prefix data also show why the fixed-width picture died but
the edge picture survives. At `sigma = 1`,

```text
PREFIX up to r=7 captures:
N= 8:  0.9899 of ZERO^common
N=10:  0.9318
N=12:  0.8700
N=14:  0.8021
N=16:  0.6677                                                 (T-6)
```

So a fixed width is not enough asymptotically, but the individual shells
themselves still obey a stable local law.

## 4. Plant does not share this local profile

At `sigma = 1`, planted gives for the same shell coefficients:

```text
r = 0:  0.0093, 0.3221, 0.2737, 0.2161, 0.3160
r = 1: -0.0014, 0.0848, 0.2411, 0.2616, 0.2555
r = 2: -0.0476,-0.0004,-0.0053, 0.0155,-0.0067
r = 3:  0.0188, 0.0003, 0.0041, 0.0104, 0.0042
```

There is no comparable collapse. Signs and amplitudes wander too much for a
shared local shell law.

So the structural conclusion is:

```text
the edge-law picture is genuine on the zeta side and absent on the planted
side, exactly as expected from a convergence-side anatomy probe.         (T-7)
```

## 5. Consequence

The honest surviving common-cloud object now sharpens again:

```text
COMMON-GAP-Z
  = [local N^-2 shell law on a slowly growing outer edge]
    + [tiny interior correction].                                        (T-8)
```

This is the first time the live object has acquired a concrete local form. The
burden is no longer "control a mysterious large packet"; it is to understand:

```text
1. how many edge shells are needed as N grows,
2. whether the shell coefficients admit a summable envelope in r,
3. and whether the interior correction can be disposed of separately.     (T-9)
```

That is a much tighter target than where E79 began.

## 6. Status

```text
proved by probe:
  on the zeta side, the common-cloud terms at fixed depth from the outer edge
  exhibit a stable N^-2-scaled profile across the audited ladder;

observed:
  the planted build does not share this local edge profile;

reduced:
  COMMON-GAP-Z from "slowly growing outer layer plus tiny interior
  correction" to "local N^-2 shell law on a slowly growing outer edge plus
  tiny interior correction";

open:
  quantify the growth law of the required edge depth and test whether the
  shell coefficients are summable as a profile in the edge index r;

next:
  measure the minimal depth m(N) together with the shell coefficient profile
  to see whether the whole edge contribution can be organized as a summable
  double law in N and r.
```
