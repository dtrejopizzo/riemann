# E79.3o - Mass-based tail cuts are worse than length-based mesoscopic tails

**Scope:** `GAP-Z` only, intrinsic tail-cut attempt by cumulative edge mass.  
**Class:** AUTOPSIA UTIL.  
**What we know after this document that we did not know before:** defining the
deep tail by cumulative absolute mass inside the active edge does **not**
stabilize the pairing with `ZERO^extra`. In fact it performs systematically worse
than the simpler length-based mesoscopic tail sweep of E79.3n.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct cloud bookkeeping only.
E72.16/E77.7az: respected. Convergence-side structure only.
Circularity: respected. Everything is computed from spec(K_N).
```

## 1. Starting point

After E79.3n, the best length-based tails were short mesoscopic terminal
segments, around `20%-30%` of the active `99%` edge. But no single fixed length
fraction was universal. The next natural idea was:

```text
perhaps the right cut is intrinsic in MASS rather than in raw length.     (T-1)
```

That is exactly what this probe tests.

## 2. Probe

Companion files:

```text
E79_3O_MASS_TAIL_PROBE.py
E79_3O_mass_tail_results.json
```

Inside the active `99%` edge, define `tail_beta` as the shortest terminal suffix
whose absolute shell mass captures a fraction `beta` of the total absolute mass
of the active edge, with

```text
beta in {0.20, 0.30, 0.40, 0.50, 0.60}.                                 (T-2)
```

Then audit

```text
|tail_beta - ZERO^extra| / max(|tail_beta|, |ZERO^extra|).              (T-3)
```

## 3. Result: the mass-based cut loses badly to the length-based cut

At `sigma = 1`, zeta gives the following best mass-tail ratios:

```text
N= 8:  0.4629
N=10:  0.4825
N=12:  0.6129
N=14:  0.7660
N=16:  0.7789
```

Compare this with the best length-based ratios from E79.3n:

```text
N= 8:  0.0229
N=10:  0.0087
N=12:  0.3588
N=14:  0.0215
N=16:  0.4141
```

This is not a close call:

```text
the mass-based terminal tail is systematically worse than the best
length-based mesoscopic tail.                                            (T-4)
```

So the intrinsic cut by cumulative absolute mass is **not** the missing
normalization.

## 4. Reading

This failure is actually informative. It says the good deep-edge / extra-root
pairing is not controlled by "how much absolute mass" sits in the tail.

Instead, the useful cut must be sensitive to **where** in the profile the tail
starts, not just how much total mass it contains.

That points back toward geometric/profile-based cuts rather than mass-based
ones.

## 5. Consequence

The live object is sharpened by exclusion:

```text
the correct short terminal tail is not selected by cumulative absolute edge
mass.                                                                    (T-5)
```

So the promising next intrinsic selectors are narrower:

```text
1. profile-based cuts at the onset of the plateau-to-decay transition,
2. signed/matched cuts tied directly to the extra-root scale,
3. perhaps a selector based on N^2 shell amplitudes rather than raw absolute
   mass.                                                                 (T-6)
```

## 6. Status

```text
proved by probe:
  mass-based tail cuts pair worse with ZERO^extra than the best
  length-based mesoscopic tails;

reduced:
  the search for an intrinsic deep-tail cut can discard cumulative absolute
  mass as the primary selector;

open:
  test profile-based or scale-matched intrinsic selectors for the deep
  edge / extra-root pairing;

next:
  locate the tail cut from the plateau-to-decay transition in the normalized
  edge profile and compare that selector against the length sweep.
```
