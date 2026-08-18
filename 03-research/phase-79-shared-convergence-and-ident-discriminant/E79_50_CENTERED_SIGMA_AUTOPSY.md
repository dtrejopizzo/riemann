# E79.50 - Recentering sigma does not remove the residual intercept burden

**Scope:** `GAP-Z` only, autopsy of the obvious coordinate change after E79.49.  
**Class:** AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** the residual
intercept is not an artifact of having written the affine template in the raw
coordinate `sigma`. Sweeping the center `sigma0` in
`a_N (sigma-sigma0) + c_N(sigma0)` does not stabilize the zeta-side level; the
best band already occurs at the left edge of the audited grid, and moving the
center inward only worsens it.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the affine coefficients from E79.48.
E72.16/E77.7az: respected. This is a coordinate-change autopsy, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. The tempting shortcut

After E79.49, the obvious hope was:

```text
maybe the intercept is only large because the affine template is written in the
wrong sigma coordinate.                                                (50-1)
```

So one tries

```text
residual(sigma; N) ~ a_N (sigma-sigma0) + c_N(sigma0),               (50-2)
```

and asks whether some center `sigma0` makes the zeta-side level `c_N(sigma0)`
transport much more cleanly.

## 2. Probe

Companion files:

```text
E79_50_CENTERED_SIGMA_AUTOPSY_PROBE.py
E79_50_centered_sigma_autopsy_results.json
```

The probe sweeps

```text
sigma0 in {0.75, 1.0, 1.25, 1.5, 1.75, 2.0},                         (50-3)
```

and for each center measures, across the audited ladder:

```text
- band(c_N(sigma0)),
- band(N c_N(sigma0)),
- mean(c_N(sigma0)).                                                  (50-4)
```

If recentering were the fix, one of these centers would sharply collapse the
zeta-side band.

## 3. Result

It does not.

On the zeta side, the best raw band already occurs at the left edge:

```text
sigma0 = 0.75   gives   band(c_N) = 3.77,                            (50-5)
```

and then the band worsens monotonically as the center moves right:

```text
sigma0 = 1.00   band(c_N) = 4.14
sigma0 = 1.25   band(c_N) = 4.60
sigma0 = 1.50   band(c_N) = 5.20
sigma0 = 1.75   band(c_N) = 6.00
sigma0 = 2.00   band(c_N) = 7.13.                                    (50-6)
```

The same is true for the scaled level `N c_N(sigma0)`: the best band is again
at the left edge, and every more central choice is worse.

So there is no hidden center that makes the zeta intercept suddenly transport
cleanly.

## 4. Reading

This is exactly the kind of autopsy we needed:

```text
the unresolved level term is real,
not a coordinate artifact.                                            (50-7)
```

That matters because it rules out an easy reparametrization escape. The slope
transport from E79.49 is genuine, but the level burden survives every simple
recentering on the audited grid.

## 5. Consequence

After E79.49-E79.50, the residual side splits cleanly:

```text
- slope: already transports as N^-1;
- level: remains unresolved and is not removed by centered sigma.     (50-8)
```

So the next candid target is no longer a coordinate change. It must be either:

```text
- a true transport law for the level term itself,
- or a different residual template that is richer than affine level+tilt. (50-9)
```

## 6. Status

```text
proved by probe:
  sweeping the affine center sigma0 does not produce a sharply more stable
  zeta-side level term; the best band is already at sigma0=0.75 and all more
  central choices are worse;

reduced:
  the intercept burden is real and survives the obvious centered-sigma
  reparametrization;

open:
  identify a genuine transport law for the level term, or replace the affine
  template by a richer residual ansatz;

next:
  test whether the level becomes simpler after subtracting its ladder mean, or
  whether a 2-mode residual template is required.
```
