# E79.3c - The common-cloud displacement is outer-shell heavy, but not a fixed-shell law

**Scope:** `GAP-Z` only, refinement inside `ZERO^common`.  
**Class:** AUTOPSIA theorem-grade of the fixed-shell reduction.  
**What we know after this document that we did not know before:** the hard term
`ZERO^common` is not uniformly spread across the whole common cloud from the
start; on the zeta side, the outer common shells do carry most of it at small
`N`. But that dominance degrades steadily with `N`, so the surviving object is
not a fixed-width outer-shell law either. This leaves a sharper picture:
`ZERO^common` is edge-driven, but the active edge thickness grows with `N`.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound mechanism.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. This is direct bookkeeping inside the independent K_N cloud.
E72.16/E77.7az: respected. Convergence-side structure only; no build-separating
       statement is used as forcing.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

E79.3b reduced the hard content of `GAP-Z` to

```text
ZERO_N^common(sigma)
  = sum_{j<=d_N} P_sigma(kappa_j^(N+2)) - sum_{j<=d_N} P_sigma(kappa_j^(N)),
```

with the extra-root term already numerically benign.

The next natural hope was:

```text
maybe ZERO^common is mostly carried by a fixed number of OUTER common shells.   (S-1)
```

If true, one could replace the whole-cloud displacement problem by a fixed-width
edge law.

## 2. Probe

Companion files:

```text
E79_3C_COMMON_SHELL_PROBE.py
E79_3C_common_shell_results.json
```

For the common cloud, with roots sorted by increasing `|kappa|`, define

```text
common_terms_j(sigma)
  = P_sigma(kappa_j^(N+2)) - P_sigma(kappa_j^(N)),                    (S-2)

ZERO_N^common(sigma)
  = sum_{j<=d_N} common_terms_j(sigma).                               (S-3)
```

Then for a fixed shell width `m`, define the outer-shell contribution

```text
ZERO_N^{common,outer(m)}(sigma)
  = sum_{d_N-m < j <= d_N} common_terms_j(sigma).                     (S-4)
```

The probe measures `|outer(m)| / |common|` for `m in {2,4,6,8,10}`.

## 3. Result: zeta is edge-heavy, but the edge thickens

At `sigma = 1`, zeta gives for the last `m=8` common shells:

```text
N= 8: common = 0.0038856850916, outer8 = 0.00384654702861, share8 = 0.9899
N=10: common = 0.00281226360364, outer8 = 0.00262048374031, share8 = 0.9318
N=12: common = 0.00246967255598, outer8 = 0.00214853235786, share8 = 0.8700
N=14: common = 0.00195712828482, outer8 = 0.0015697246302,  share8 = 0.8021
N=16: common = 0.00181877881651, outer8 = 0.0012144710968,  share8 = 0.6677
```

So the zeta common-cloud term is indeed outer-shell heavy, but not with a
stable fixed shell width:

```text
the last 8 shells explain almost everything at N=8, but only about 2/3 by N=16.
                                                                    (S-5)
```

This rules out the fixed-width version of the edge law.

## 4. Plant confirms that no fixed shell law survives uniformly

At `sigma = 1`, planted gives for the same `m=8`:

```text
N= 8: common = -0.213757027492, outer8 = -4.31967246055e-6, share8 = 2.0e-5
N=10: common = -0.00689644094266, outer8 =  0.00410484845904, share8 = 0.5952
N=12: common =  0.000427346882535, outer8 = 0.00359587220004, share8 = 8.4144
N=14: common = -0.00118918450649, outer8 = 0.00269448242103, share8 = 2.2658
N=16: common =  0.00108684085546, outer8 = 0.00227663418747, share8 = 2.0947
```

So on the planted side the outer common shells can even have the wrong sign
relative to the total common part, or overwhelm it through cancellation.

This means:

```text
there is no fixed-width outer-shell law that is structurally stable across the
two builds.                                                            (S-6)
```

## 5. Consequence

This is more informative than a simple failure.

What survives is:

```text
ZERO^common is not uniformly bulk-distributed; it is edge-driven on the zeta
side, but the effective edge thickness grows with N.                   (S-7)
```

So the honest next object is no longer:

```text
"a fixed shell width at the outer edge"
```

but rather:

```text
"a growing outer layer of the common cloud, plus a residual interior term".    (S-8)
```

That is the right geometric refinement of `COMMON-GAP-Z`.

## 6. Status

```text
proved by probe:
  on the zeta side, ZERO^common is strongly edge-driven at the audited depths;

proved by probe:
  the fixed-width outer-shell law is false, because the share of the last
  8 shells drops from ~0.99 to ~0.67 across N=8..16;

observed:
  on the planted side, the outer common shells are not even sign-stable
  relative to the total common term;

reduced:
  the live common-cloud problem from "arbitrary whole-cloud redistribution" to
  "growing outer-layer displacement plus interior remainder";

open:
  quantify the effective outer-layer thickness and the decay of the residual
  interior contribution;

next:
  replace the fixed-shell question by a cofinal outer-layer law for
  ZERO^common.
```
