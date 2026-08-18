# E79.3d - The active outer layer grows slowly on the zeta side

**Scope:** `GAP-Z` only, refinement of the outer-layer picture inside
`ZERO^common`.  
**Class:** REDUCCION GENUINA (cofinal geometric refinement).  
**What we know after this document that we did not know before:** the zeta
common-cloud term is not controlled by a fixed shell width, but its active outer
layer does grow much more slowly than the whole common-cloud dimension. So the
right geometric object is no longer "almost the whole cloud" and no longer "a
fixed shell width", but a **cofinal outer layer of slowly growing thickness**.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound mechanism.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct cloud bookkeeping only.
E72.16/E77.7az: respected. Convergence-side structure only; build separation is
       recorded as evidence, not used as forcing.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

E79.3c showed:

```text
ZERO^common is edge-driven on the zeta side, but not by any fixed shell width. (T-1)
```

The natural next question is then quantitative:

```text
how thick must the outer layer be to capture a fixed fraction of
ZERO_N^common(sigma)?                                                  (T-2)
```

## 2. Probe

Companion files:

```text
E79_3D_OUTER_LAYER_THICKNESS_PROBE.py
E79_3D_outer_layer_thickness_results.json
```

For

```text
ZERO_N^common(sigma) = sum_{j<=d_N} common_terms_j(sigma),
common_terms_j(sigma) = P_sigma(kappa_j^(N+2)) - P_sigma(kappa_j^(N)),
```

with roots ordered by increasing `|kappa|`, define the outer-layer partial sums

```text
OUTER_{N,m}(sigma) = sum_{d_N-m < j <= d_N} common_terms_j(sigma).   (T-3)
```

The probe measures the minimal `m` such that

```text
|OUTER_{N,m}(sigma)| >= theta |ZERO_N^common(sigma)|                  (T-4)
```

for `theta in {0.5, 0.9, 0.99}`.

## 3. Result: zeta has a slowly growing active edge thickness

At `sigma = 1`, zeta gives:

```text
N= 8, dim=15: m50 = 4, m90 = 7,  m99 = 9
N=10, dim=19: m50 = 4, m90 = 8,  m99 = 11
N=12, dim=23: m50 = 5, m90 = 9,  m99 = 11
N=14, dim=27: m50 = 6, m90 = 10, m99 = 13
N=16, dim=31: m50 = 7, m90 = 11, m99 = 14
```

This is the key improvement over E79.3c:

```text
although the relevant edge thickness grows with N, it grows much more slowly
than the full common-cloud dimension d_N = 15,19,23,27,31.            (T-5)
```

In particular:

```text
m50 is only 4,4,5,6,7 while d_N is 15,19,23,27,31;
m90 is only 7,8,9,10,11 on the same ladder.                           (T-6)
```

So the zeta common-cloud term is not "almost the whole cloud" in the operative
sense; it is a **thin but growing outer layer**.

## 4. Plant does not share this geometry

At `sigma = 1`, planted gives:

```text
N= 8, dim=15: m50 = 14, m90 = 14, m99 = 14
N=10, dim=19: m50 = 2,  m90 = 14, m99 = 16
N=12, dim=23: m50 = 1,  m90 = 1,  m99 = 1
N=14, dim=27: m50 = 1,  m90 = 1,  m99 = 2
N=16, dim=31: m50 = 1,  m90 = 1,  m99 = 1
```

This is not a coherent scaling law at all. It reflects exactly the instability
already seen in E79.3a/E79.3c: sign changes and cancellations in the common
cloud make the effective outer-layer thickness meaningless as a stable build-
neutral geometric invariant on the planted side.

So:

```text
the "slowly growing outer layer" picture is a zeta-side structural feature,
not a shared packet law.                                                (T-7)
```

That is admissible here because this is still only structural diagnosis, not a
forcing step.

## 5. Consequence

This sharpens the live `COMMON-GAP-Z` object to the most precise version so far:

```text
COMMON-GAP-Z
  = [slowly growing outer layer] + [interior remainder].              (T-8)
```

The point is not that the outer layer is fixed; it is that it stays much thinner
than the whole common cloud on the audited zeta ladder.

So the next candid reduction target is:

```text
control the outer-layer thickness m_theta(N) and show the interior remainder is
small enough to preserve summability.                                  (T-9)
```

That is a real cofinal refinement, not just another descriptive restatement.

## 6. Status

```text
proved by probe:
  on the zeta side, the active outer-layer thickness needed to capture fixed
  fractions of ZERO^common grows slowly compared to the full common-cloud
  dimension;

observed:
  on the planted side, the same thickness parameters are erratic and do not
  define a stable packet geometry;

reduced:
  the live common-cloud problem from "growing outer layer plus interior
  remainder" to the more precise object "slowly growing outer layer plus
  interior remainder";

open:
  quantify the asymptotic law of m_theta(N) and the decay of the interior
  remainder;

next:
  isolate the interior remainder numerically and see whether it is already
  summable after removing the slowly growing outer layer.
```
