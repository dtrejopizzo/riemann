# E78.4c - Source/subspace audit for neutral-ground-Cauchy

**Run:** 2026-07-18.
**Target:** the remaining source/subspace side in

```text
NEUTRAL-GROUND-CAUCHY
  = anchor-neutrality + source/subspace-side work.
```

## 1. Purpose

E78.4b showed that the safe Cauchy anchor

```text
r(z0) v0
```

stays macroscopic in both builds, so anchor blindness is not the live
build-neutral obstruction.  This note audits the complementary factor:

```text
source overlap: v0^* g_right,
full boundary data: xi(left), xi(right)
```

for the same sectionwise lowest inner mode `v0` and the full section ground
state `xi`.

The point is not to smuggle in simplicity or a `mu_L`-pinned detector, but to
check whether the source-side remnant is itself build-neutral or whether it is
the first genuinely active obstruction.

## 2. Probe

Companion:

```text
E78_4c_source_subspace_probe.py
E78_4c_source_subspace_results.json
```

For each finite section the probe computes:

```text
1. the smallest inner eigenvalue by absolute value, |lambda0(A)|,
   for A = H_inner - mu I with mu the section spectral point;
2. the source overlap |v0^* g_right|;
3. the absolute boundary coordinates of the full ground state xi.
```

The two builds are the zeta build and the standard planted falsifier

```text
("14.134725141734693790", "0.30", "5.0").
```

## 3. Reading template

The reductions from Phase 77 imply:

```text
v0^* g_right = 0
=> full boundary-zero ground state                        (E77.7af),
```

so a robust source overlap and robust boundary coordinates would mean that the
source half is behaving as neutrally as the anchor half.  In that case the
live remnant would shrink further from a scalar nonvanishing problem to a
subspace/existence assembly problem.

Conversely, if one build drove `|v0^* g_right|` or the boundary coordinates to
zero while the other stayed macroscopic, that would have to be audited against
the Phase-78 attribution gate before being admitted as forcing.

## 4. Results

The bilateral probe gives a sharp dichotomy.

### 4.1 Zeta

For the zeta build the source overlap collapses very rapidly:

```text
N= 6  |lam0| = 7.38e-21   |v0^* g| = 2.37e-17   |xiL| = 1.56e-4
N=10  |lam0| = 1.84e-30   |v0^* g| = 1.30e-23   |xiL| = 7.09e-8
N=12  |lam0| = 4.28e-35   |v0^* g| = 1.74e-24   |xiL| = 1.23e-11
N=14  |lam0| = 2.25e-39   |v0^* g| = 1.66e-28   |xiL| = 6.78e-12.
```

So on the zeta ladder:

```text
1. the lowest inner mode becomes almost source-blind in this coordinate;
2. the full ground-state boundary entries remain nonzero, but are tiny.
```

### 4.2 Planted build

For the planted build the same source overlap stays macroscopic:

```text
N= 6  |lam0| = 8.19e-2    |v0^* g| = 3.37e-2    |xiL| = 5.78e-1
N= 8  |lam0| = 3.09e-1    |v0^* g| = 1.92       |xiL| = 8.00e-2
N=10  |lam0| = 1.47e-1    |v0^* g| = 3.40e-1    |xiL| = 2.07e-1
N=12  |lam0| = 9.62e-3    |v0^* g| = 1.60e-1    |xiL| = 2.99e-2
N=14  |lam0| = 7.08e-4    |v0^* g| = 3.88e-2    |xiL| = 9.11e-3.
```

So the planted build emphatically does **not** show source blindness in the
same coordinate.

## 5. Reading

This is not an admissible LP forcing mechanism.  Under the Phase-78 binding
rule, any step that separates zeta from the planted falsifier by order one is a
detector unless it is already proved to imply a live predecessor without
smuggling the zero-location content.

That is exactly what happens here:

```text
lowest-inner-mode source overlap  |v0^* g|
```

is strongly build-discriminating, while the LP front was already attributed
build-neutrally in E77.1b / E77.7az.  Therefore:

```text
SOURCE-MODE-OVERLAP on the distinguished lowest inner mode is a DETECTOR,
not an admissible forcing object for LP.
```

The same warning applies to the tiny zeta boundary entries of the full ground
state: they separate the builds, so they cannot be used directly as a
build-neutral LP mechanism either.

## 6. Consequence for the live remnant

E78.4b already killed the anchor coordinate as the active obstruction.
Section 5 now kills the naive source coordinate as well.

So the corrected conclusion is:

```text
NEUTRAL-GROUND-CAUCHY cannot be pursued through either scalar factor
  r(z0) v0
or
  v0^* g
attached to a distinguished lowest inner mode.
```

Any admissible LP-interface remnant must now be formulated:

```text
1. without singling out a gap-sensitive lowest mode;
2. without pinning to mu_L;
3. at the level of a normalized l2 class / disk assembly, as in
   SAFE-DISK-IDENT and E77.7aj.
```

This is a genuine autopsy, not a regression: it removes another false scalar
target before it can spawn a second detector spiral.

## 7. Status

```text
observed:
  the source overlap |v0^* g| is tiny on the zeta ladder but macroscopic on the
  planted build through N=14;

observed:
  full ground-state boundary coordinates are nonzero in both builds, but also
  strongly build-separated in size;

refuted:
  the distinguished-mode source scalar as a build-neutral LP-interface object;

clarified:
  NEUTRAL-GROUND-CAUCHY cannot be closed through modewise source/anchor
  coordinates; the live remnant must be reformulated at the subspace/class
  assembly level;

next:
  return to the genuinely admissible LP-interface front
  SAFE-DISK-IDENT / normalized l2 class existence, and keep IDENT as the
  home of the arithmetic discriminant.
```
