# E79.52 - A single fixed curvature mode closes the residual template on the zeta side

**Scope:** `GAP-Z` only, first minimal template beyond affine.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** adding one
fixed quadratic mode in `sigma` to the affine residual template sharply closes
the remaining zeta-side fitting error, and its coefficient is small enough to
be a plausible next transport variable.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the audited multisigma residual data from E79.44.
E72.16/E77.7az: respected. This is a finite template audit, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this is the right next ansatz

E79.48-E79.51 left a very specific picture:

```text
- affine in sigma is already good;
- the slope transports;
- the level burden survives all obvious normalizations.               (52-1)
```

So the first honest richer template is the minimal one:

```text
residual(sigma; N) ~ a_N sigma + b_N + g_N q(sigma),                  (52-2)
```

with a **fixed** curvature shape `q`, not an arbitrary extra profile.

## 2. Probe

Companion files:

```text
E79_52_TWO_MODE_SIGMA_TEMPLATE_PROBE.py
E79_52_two_mode_sigma_template_results.json
```

We keep the affine part and add the single curvature mode

```text
q(sigma) = (sigma - sigma_c)^2,   sigma_c = (0.75 + 2.0)/2 = 1.375.  (52-3)
```

So the fit is

```text
a_N sigma + b_N + g_N (sigma-1.375)^2.                               (52-4)
```

The outputs are:

```text
- normalized max/RMS fitting error;
- the curvature coefficient g_N;
- the scaled coefficient N^2 |g_N|.                                  (52-5)
```

## 3. Result

On the zeta side, the extra mode sharply closes what remained after E79.48: the
two-mode fit errors are uniformly much smaller than the affine ones.

Numerically:

```text
zeta normalized max error:
N= 8   2.54e-5
N=10   1.64e-5
N=12   2.51e-6
N=14   1.03e-5
N=16   1.31e-6                                                   (52-6a)
```

The curvature coefficient is also already on a coherent scale:

```text
zeta N^2 |g_N|:
N= 8   0.0957
N=10   0.1409
N=12   0.1209
N=14   0.1796
N=16   0.1854                                                   (52-6b)
```

So the level burden is not arbitrary; it is already largely captured by one
fixed curvature mode.

By contrast, the planted hard rows remain far from closed:

```text
plant normalized max error:
N= 8   0.232
N=10   0.381
N=12   0.00259
N=14   0.159
N=16   0.0110                                                   (52-6c)

plant N^2 |g_N|:
N= 8   143.4
N=10   62.3
N=12   4.07
N=14   249.7
N=16   5.98                                                    (52-6d)
```

So the two-mode template does not just improve every build equally; it exposes
another strong zeta/plant separation on the hard rows.

## 4. Reading

This is the first residual ansatz that survives all the autopsies:

```text
primitive packet
  + transported slope
  + one fixed curvature mode.                                         (52-7)
```
That is a real structural gain. It says the unresolved burden is no longer a
free function of sigma; it already lives in a 1-dimensional correction slot.

## 5. Consequence

The next honest transport question is now extremely concrete:

```text
does g_N itself transport simply with N on the zeta side, and does the plant
fail that transport on the hard rows?                                 (52-8)
```

If yes, the residual side has essentially been reduced to a tiny finite law.

## 6. Status

```text
proved by probe:
  one fixed quadratic mode sharply improves the residual template beyond the
  affine law on the audited zeta ladder, driving the zeta fitting error down to
  about 1e-6-1e-5 on the audited grid;

reduced:
  the residual burden past the affine slope/level split now lives in a single
  curvature coefficient g_N;

open:
  identify the N-transport law for g_N and test whether the plant violates it
  on the hard rows;

next:
  audit the transport band for N^2|g_N| (or the right nearby scaling) across
  the audited ladder.
```
