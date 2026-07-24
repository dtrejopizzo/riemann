# E79.3e - After removing the active outer layer, the zeta interior remainder is tiny

**Scope:** `GAP-Z` only, refinement of the common-cloud front.  
**Class:** REDUCCION GENUINA (the live cloud problem shrinks again).  
**What we know after this document that we did not know before:** on the zeta
side, once the minimal outer layer capturing `90%` or `99%` of `ZERO^common` is
removed, the leftover interior remainder is already very small. So the honest
live object is no longer the whole common cloud, and not even "outer layer plus
interior remainder" on equal footing: it is primarily a **thin growing edge law**
plus a **tiny interior correction**.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct spectral-cloud bookkeeping only.
E72.16/E77.7az: respected. This is still convergence-side structure; build
       separation is descriptive only, not used as forcing.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

E79.3d sharpened the common-cloud picture to

```text
COMMON-GAP-Z = [slowly growing outer layer] + [interior remainder].      (T-1)
```

That was still honest, but incomplete. The next real question is:

```text
after removing the minimal outer layer that already captures a fixed fraction
theta of |ZERO_N^common|, how large is the leftover interior piece?       (T-2)
```

If that interior piece is already tiny, then the hard content of `ZERO^common`
really does localize near the outer edge.

## 2. Probe

Companion files:

```text
E79_3E_INTERIOR_REMAINDER_PROBE.py
E79_3E_interior_remainder_results.json
```

For the common-cloud term

```text
ZERO_N^common(sigma) = sum_{j<=d_N} common_terms_j(sigma),
common_terms_j(sigma) = P_sigma(kappa_j^(N+2)) - P_sigma(kappa_j^(N)),
```

with roots ordered by increasing `|kappa|`, let `m_theta(N,sigma)` be the
minimal thickness from E79.3d such that

```text
|OUTER_{N,m_theta}(sigma)| >= theta |ZERO_N^common(sigma)|,               (T-3)
OUTER_{N,m}(sigma) = sum_{d_N-m < j <= d_N} common_terms_j(sigma).
```

Then define the leftover interior remainder

```text
REM_{N,theta}(sigma) = ZERO_N^common(sigma) - OUTER_{N,m_theta}(sigma).   (T-4)
```

The probe records `REM_{N,theta}`, its size relative to `ZERO_N^common`, and the
scaled quantities `N |REM|`, `N^2 |REM|`.

## 3. Result: on the zeta side the interior remainder is already tiny

At `sigma = 1`, zeta gives:

```text
N= 8:  m90 = 7,  |REM_90| / |common| = 2.22e-2
       m99 = 9,  |REM_99| / |common| = 8.28e-4

N=10:  m90 = 8,  |REM_90| / |common| = 6.82e-2
       m99 = 11, |REM_99| / |common| = 1.32e-3

N=12:  m90 = 9,  |REM_90| / |common| = 4.67e-2
       m99 = 11, |REM_99| / |common| = 4.55e-3

N=14:  m90 = 10, |REM_90| / |common| = 7.40e-2
       m99 = 13, |REM_99| / |common| = 7.46e-3

N=16:  m90 = 11, |REM_90| / |common| = 9.73e-2
       m99 = 14, |REM_99| / |common| = 8.19e-3
```

This is the key new reduction:

```text
after removing the minimal layer that captures 99% of the common-cloud total,
the leftover interior contribution is already below 1% of ZERO_N^common on the
entire audited zeta ladder.                                              (T-5)
```

In absolute terms, still at `sigma = 1`,

```text
|REM_99| = 3.2e-6, 3.7e-6, 1.1e-5, 1.5e-5, 1.5e-5   for N=8,10,12,14,16,
N |REM_99| = 2.6e-5, 3.7e-5, 1.3e-4, 2.0e-4, 2.4e-4.
```

The same pattern repeats at `sigma = 2`, with nearly identical relative
fractions.

So the interior correction is not just smaller than the whole common cloud. It
is already **tiny** once the active outer layer is removed.

## 4. Plant does not produce the same cofinal geometry

On the planted side the same remainder statistics are erratic. For example at
`sigma = 1`,

```text
N= 8:  |REM_90| / |common| = 2.20
N=10:  |REM_90| / |common| = 1.92
N=12:  |REM_90| / |common| = 3.45
N=14:  |REM_90| / |common| = 1.93
N=16:  |REM_90| / |common| = 1.36e-1
```

This is not a stable shared packet law. It reflects the same sign instability
already seen in E79.3a-E79.3d.

That does **not** invalidate the reduction here, because this is still only
cloud anatomy, not a forcing theorem. But it does mean the useful geometric
picture is zeta-side only:

```text
thin growing edge + tiny interior correction.                            (T-6)
```

## 5. Consequence

The honest surviving common-cloud object is now:

```text
COMMON-GAP-Z
  = [slowly growing outer layer carrying essentially all of ZERO^common]
    + [tiny interior correction].                                        (T-7)
```

This is stronger than E79.3d. The interior is no longer a comparably-sized
partner in the decomposition; it is a small correction after the minimal active
edge is removed.

So the next honest target is no longer "understand the whole cloud":

```text
it is to control the slowly growing edge law itself, and then show the tiny
interior correction is summable with room to spare.                       (T-8)
```

That is a materially smaller object than the phase started with.

## 6. Status

```text
proved by probe:
  on the zeta side, once the minimal outer layer capturing 99% of
  ZERO_N^common is removed, the leftover interior remainder stays below 1% of
  the total common-cloud contribution on the whole audited ladder;

observed:
  the same geometry is not shared by the planted build, which remains cloud-
  unstable and sign-sensitive;

reduced:
  COMMON-GAP-Z from "slowly growing outer layer plus interior remainder" to
  "slowly growing outer layer plus tiny interior correction";

open:
  quantify the edge law itself and prove a summable bound for the interior
  correction;

next:
  isolate the outer-layer term directly and test whether its thickness/growth
  law is compatible with a summable displacement estimate.
```
