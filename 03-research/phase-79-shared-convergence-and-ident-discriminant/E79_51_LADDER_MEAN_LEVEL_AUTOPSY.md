# E79.51 - Subtracting the ladder mean does not remove the residual level burden

**Scope:** `GAP-Z` only, first direct test of the "subtract the ladder mean"
idea after E79.50.  
**Class:** AUTOPSIA HONESTA.  
**What we know after this document that we did not know before:** subtracting
the ladder mean from the residual level does not reveal a new clean transport
law on the zeta side. It just recenters the same uneven burden, with the hard
rows still dominating.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the affine coefficients from E79.48.
E72.16/E77.7az: respected. This is a finite normalization autopsy, not a
                forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. The remaining easy hope

After E79.50, the level burden was still alive, but one simple normalization
had not yet been killed:

```text
maybe the level becomes simple after subtracting its ladder mean.      (51-1)
```

This is the mildest possible improvement beyond recentering sigma.

## 2. Probe

Companion files:

```text
E79_51_LADDER_MEAN_LEVEL_AUTOPSY_PROBE.py
E79_51_ladder_mean_level_autopsy_results.json
```

The probe uses the best zeta-side centered level at the best available center
from E79.50, namely

```text
c_N = a_N * 0.75 + b_N,                                               (51-2)
```

and also the raw affine intercept `b_N`. For both, it computes:

```text
dc_N = c_N - mean(c_N),
db_N = b_N - mean(b_N),                                               (51-3)
```

and audits whether `dc_N` or `db_N` now show a simpler transport scale.

## 3. Result

They do not.

On the zeta side, the hard rows remain the same hard rows after mean
subtraction:

```text
N|dc_N|  = 0.00326, 0.128, 0.0133, 0.0203, 0.217
N|db_N|  = 0.0300, 0.102, 0.0314, 0.0501, 0.238.                    (51-4)
```

So subtracting the ladder mean does not uncover a hidden narrow transport band.
It mainly re-expresses the fact that `N=10` and `N=16` remain the dominant
level outliers.

## 4. Reading

This is another useful autopsy:

```text
the level burden is not cured by recentering sigma,
and it is not cured by subtracting the ladder mean either.            (51-5)
```

That means the burden is genuinely shaped, not just shifted.

## 5. Consequence

After E79.50-E79.51, the easy normalization routes are exhausted:

```text
- coordinate recentering: dead;
- ladder-mean subtraction: dead.                                     (51-6)
```

So the next honest front is no longer "better centering". It is:

```text
either a true transport law for the shaped level term,
or a richer residual template with more than one mode.               (51-7)
```

## 6. Status

```text
proved by probe:
  subtracting the ladder mean from the residual level does not reveal a clean
  zeta-side transport law;

reduced:
  the level burden is real, shaped, and survives both obvious
  normalizations tried so far;

open:
  decide whether the next object is a shaped level transport law or a 2-mode
  residual template;

next:
  test a minimal 2-mode residual template against the audited sigma grid.
```
