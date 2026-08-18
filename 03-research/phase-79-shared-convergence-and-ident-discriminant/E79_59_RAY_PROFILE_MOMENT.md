# E79.59 - The modal-ray amplitude is better seen as a profile-moment effect than as a local cancellation effect

**Scope:** `GAP-Z` only, first signed/weighted profile-moment audit for the
scalar modal-ray amplitude.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** `rho_N` tracks
global moments of the normalized active-edge profile more clearly than it tracks
local sign cancellation. In particular, the best audited signals come from the
front-vs-back mass imbalance and the slope of the normalized edge profile.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only normalized edge-profile data and the signed-block
       audit already certified earlier in the phase.
E72.16/E77.7az: respected. This is a transport reduction, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this is the next candid test

E79.58 localized `rho_N` to edge intensity rather than edge width. The next
question is whether that dependence is merely local intensity, or whether it is
actually a **moment of the whole normalized edge profile**.

There are two obvious candidates:

```text
1. a global tilt / slope of the normalized edge profile;
2. a signed front-vs-back imbalance across the active edge.                (59-1)
```

E79.3k already showed that short-range alternating cancellation is tiny, so if
`rho_N` has a signed source it should be global rather than pairwise local.

## 2. Probe

Companion files:

```text
E79_59_RAY_PROFILE_MOMENT_probe.py
E79_59_ray_profile_moment_results.json
```

On the audited zeta ladder, using the sigma=`1.0`, `90%` active-edge profile
from E79.3j, the probe forms:

```text
- profile_avg:     mean normalized shell intensity;
- profile_centroid: intensity-weighted barycenter in normalized depth u;
- profile_slope:   least-squares slope of intensity versus (u-1/2);
- front_back_gap:  mass on u<=0.4 minus mass on u>=0.6.                   (59-2)
```

It compares these with `|rho_N|` from E79.56, and also includes the local
alternating ratio from E79.3k as a control.

## 3. Result

The strongest audited correlations are:

```text
corr(|rho_N|, front_back_gap)   ~  0.74
corr(|rho_N|, profile_slope)    ~ -0.73
corr(|rho_N|, profile_centroid) ~ -0.69.                                 (59-3)
```

By contrast, the short-range alternating control is weaker:

```text
corr(|rho_N|, alt_ratio)        ~ -0.59.                                 (59-4)
```

So the scalar amplitude is better explained by a **global shape moment** of the
edge profile than by the tiny local sign oscillation measured in E79.3k.

The picture is consistent across the audited rows:

```text
- large |rho_N| comes with profiles that are more front-loaded;
- small |rho_N| comes with flatter or back-heavier profiles.              (59-5)
```

In that language, `rho_N` is responding to where the active-edge intensity sits,
not merely to how much total intensity there is.

## 4. Reading

This is a real refinement of E79.58.

The previous step said "intensity matters more than width."  
This step says more:

```text
the relevant scalar is not raw intensity alone,
but a low-order moment of the normalized intensity profile.               (59-6)
```

That is a much smaller search space. It suggests that `rho_N` may be controlled
by a single profile moment or a very short linear combination of such moments.

## 5. Consequence

After E79.59, the next admissible target is quite concrete:

```text
fit rho_N against one or two primitive profile moments
and test whether the resulting law is build-neutral on the convergence side but
breaks on the planted build only at the amplitude level.                  (59-7)
```

The specific candidates now are:

```text
- front_back_gap,
- profile_slope,
- profile_centroid,
possibly normalized by the average active-edge intensity from E79.58.      (59-8)
```

## 6. Status

```text
proved by probe:
  the modal-ray amplitude rho_N tracks global moments of the normalized
  active-edge profile more clearly than it tracks local alternating
  cancellation;

reduced:
  the scalar-law search from generic intensity observables to a tiny family of
  profile moments (front/back imbalance, slope, centroid);

open:
  identify the minimal moment law for rho_N and test whether it remains stable
  beyond the audited zeta ladder;

next:
  build the first explicit one- or two-moment predictor for rho_N and compare
  it against the planted build as a non-forcing diagnostic.
```
