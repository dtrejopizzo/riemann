# E78.77 - The next live object is a scale-coupled tail law `TAIL <= kappa(sigma) A_N`

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front.

## 1. Purpose

E78.76 killed the ratio-only shortcut

```text
rho_N = A_{N+2}/A_N  =>  small TAIL/BASE,              (SBC-1)
```

because `TAIL/BASE` needs scale information, not only geometric shape.

This note records the sharper candidate suggested by the common certified rows:

```text
control the radial tail directly by the safe_u amplitude A_N. (SBC-2)
```

## 2. Candidate coupling law

Recall the two relevant scales:

```text
A_N := N Delta safe_u_N,                               (SBC-3)
TAIL_N(sigma_0,sigma) := BASE_N(sigma_0)-Re Delta ell_N(i sigma). (SBC-4)
```

The most natural scale-coupled target is:

```text
SAFEU-BASE-COUPLING:
  TAIL_N(sigma_0,sigma) <= kappa(sigma) A_N            (SBC-5)
```

on the zeta cofinal path.

Combined with any lower comparison

```text
A_N <= C' BASE_N(sigma_0),                             (SBC-6)
```

this would give

```text
TAIL_N(sigma_0,sigma) / BASE_N(sigma_0)
 <= kappa(sigma) C'.                                   (SBC-7)
```

and therefore feed directly into the fractional budget of E78.75.

So `(SBC-5)` is a genuine reduced target with explicit upward implication.

## 3. Probe audit on the common ladder

Companion:

```text
E78_77_safeu_base_coupling_probe.py
E78_77_safeu_base_coupling_results.json
```

The common audited rows are again

```text
sigma in {1.0, 3.0},
N = 8,10,12,14,16,18.                                  (SBC-8)
```

The probe computes

```text
kappa_obs(N,sigma) := TAIL_N(sigma_0,sigma) / A_N.     (SBC-9)
```

### Zeta

At `sigma=1.0`:

```text
kappa_obs in [0.00123, 0.00701].                       (SBC-10)
```

At `sigma=3.0`:

```text
kappa_obs in [0.00511, 0.02908].                       (SBC-11)
```

Across the full common ladder:

```text
kappa_obs
  min    = 0.00123,
  median = 0.00606,
  max    = 0.02908.                                    (SBC-12)
```

Representative rows:

```text
sigma=1.0:
  N= 8   TAIL/A ≈ 0.00701
  N=18   TAIL/A ≈ 0.00123

sigma=3.0:
  N= 8   TAIL/A ≈ 0.02908
  N=18   TAIL/A ≈ 0.00511.                             (SBC-13)
```

So the coupling candidate is numerically far tighter than the raw tail/base
budget, and it decays with `N` on both audited sigma slices.

### Companion scale

The same rows give

```text
A_N / BASE_N(sigma_0)
  min    = 0.95145,
  median = 2.14157,
  max    = 4.42479.                                    (SBC-14)
```

Hence the observed relation

```text
TAIL/BASE = (TAIL/A) * (A/BASE)                        (SBC-15)
```

is numerically consistent with E78.76: the radial budget is controlled only
after both factors are tracked.

## 4. Consequence

The shell front now has a clean two-factor structure:

```text
TAIL/BASE
 = (TAIL/A) * (A/BASE).                                (SBC-16)
```

This suggests the honest split:

```text
(i)  SAFEU-TAIL-COUPLING:   TAIL <= kappa(sigma) A_N,
(ii) SAFEU-BASE-COMPARISON: A_N <= C' BASE.            (SBC-17)
```

If both are proved cofinally with

```text
kappa(sigma) C' < 1,                                   (SBC-18)
```

then E78.75 closes on the radial side.

So the single vague phrase "control the tail" has now been sharpened into two
precise comparison objects.

## 5. Honest reading

This note does not prove `(SBC-5)` or `(SBC-6)`. It only names them and shows
that they fit the audited zeta data much better than the dead ratio shortcut.

That is still a real gain:

```text
the live target is now scale-coupled and factorized.   (SBC-19)
```

## 6. Status

```text
clarified:
  the next honest shell object is a scale-coupled tail law TAIL <= kappa A_N;

observed:
  on the common zeta ladder TAIL/A stays in the small band
  0.00123-0.02908, while A/BASE stays in the band 0.95145-4.42479;

reduced:
  radial budget control to the two-factor target
  SAFEU-TAIL-COUPLING + SAFEU-BASE-COMPARISON.
```
