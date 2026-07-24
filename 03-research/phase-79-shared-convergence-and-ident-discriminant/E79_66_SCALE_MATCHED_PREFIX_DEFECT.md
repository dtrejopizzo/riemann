# E79.66 - The usable prefix-defect coordinate is the scale-matched one, not the raw prefix fractions

**Scope:** `GAP-Z` only, closure of the scalar-law side branch opened in
E79.64-E79.65.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the prefix
reading from E79.65 is real, but the predictor-stable coordinate is not any raw
prefix fraction from the common-cloud bookkeeping. The coordinate that preserves
the best audited stability is the scale-matched first-prefix defect
`edge0 / intensity` (equivalently `1 - edge0 / intensity`).

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only already-audited shell/profile observables.
E72.16/E77.7az: respected. This is scalar-law bookkeeping, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this audit was necessary

E79.64 isolated the best local correction as the scale-free first-shell defect

```text
relDef = 1 - edge0 / intensity,                                          (66-1)
```

and E79.65 showed that `relDef` is almost the same geometric information as the
shortest prefix bookkeeping already present in E79.3f. But "almost the same
information" leaves an honest ambiguity:

```text
can the raw prefix coordinates replace relDef directly in the predictor,
or is the scale matching to intensity essential?                          (66-2)
```

This note resolves that point explicitly.

## 2. Coordinates compared

The baseline model remains

```text
|rho_N| ~ affine(profile_slope, intensity).                              (66-3)
```

To that baseline we add, one at a time:

```text
ratio0avg   = edge0 / intensity,
relDef      = 1 - edge0 / intensity,
edge0frac, edge1frac, edge2frac,
prefix_gap_10 = edge1frac - edge0frac,
prefix_gap_21 = edge2frac - edge1frac.                                  (66-4)
```

Here `edgekfrac` are the absolute shortest-prefix fractions read directly from
the zeta-side common-cloud edge profile in E79.3f.

## 3. Result

The best audited third coordinate is unchanged:

```text
slope + intensity + ratio0avg
or equivalently
slope + intensity + relDef.                                              (66-5)
```

Numerically, the leave-one-out maxima are:

```text
slope + intensity + ratio0avg      -> ~0.261
slope + intensity + relDef         -> ~0.261
slope + intensity + edge0frac      -> ~0.381
slope + intensity + edge1frac      -> ~0.413
slope + intensity + edge2frac      -> ~0.414
slope + intensity + prefix_gap_21  -> ~0.416
slope + intensity + prefix_gap_10  -> ~0.432.                           (66-6)
```

So the raw prefix fractions and raw prefix-gap increments do **not** preserve
the stability of E79.64, even though they are highly correlated with `relDef`.

The correlation side confirms the geometric reading without changing that
predictive verdict:

```text
corr(relDef, edge0frac)     ~ -0.977
corr(relDef, edge1frac)     ~ -0.976
corr(relDef, edge2frac)     ~ -0.977
corr(relDef, prefix_gap_10) ~ -0.974
corr(relDef, prefix_gap_21) ~ -0.979.                                   (66-7)
```

## 4. Reading

This is the clean resolution of the E79.65 ambiguity.

The boundary correction is genuinely a prefix-defect phenomenon, but the usable
coordinate is not

```text
"how much common-cloud mass has arrived by shell 0,1,2" in raw prefix units. (66-8)
```

It is

```text
"how small the very first prefix is, after matching it to the active-edge
 intensity scale."                                                        (66-9)
```

So the prefix reading survives, but only in a **scale-matched** form.

## 5. Consequence

After E79.66, the scalar-law side branch is as reduced as it honestly can be on
the audited ladder:

```text
|rho_N| ~ affine(
    profile_slope,
    active-edge intensity,
    scale-matched first-prefix defect
).                                                                        (66-10)
```

That is narrower than E79.64 and cleaner than E79.65:

```text
not a raw shell value,
not a raw prefix fraction,
but a scale-matched first-prefix defect.                                 (66-11)
```

This is small enough that the next sensible move is no longer to keep mining
variants of the same scalar coordinate family, but to decide whether this branch
is now mature enough to be treated as descriptive support and return to the
main `GAP-Z` objects.

## 6. Status

```text
proved by probe:
  the predictor-stable coordinate is the scale-matched first-prefix defect
  `edge0/intensity` (equivalently `1-edge0/intensity`), not any raw prefix
  fraction or raw prefix-gap increment from the common-cloud bookkeeping;

reduced:
  the boundary-correction front from "prefix-like" to the exact usable
  coordinate family: scale-matched first-prefix defect;

clarified:
  E79.65's prefix reading is geometrically correct but should not be overstated
  as literal coordinate interchangeability;

open:
  decide whether the scalar-law branch is now sufficiently closed to archive as
  descriptive support and return to the load-bearing `GAP-Z` chain;

next:
  update the phase-79 README to record this branch as reduced and re-center the
  live work on the main `ZERO` / common-cloud convergence objects.
```
