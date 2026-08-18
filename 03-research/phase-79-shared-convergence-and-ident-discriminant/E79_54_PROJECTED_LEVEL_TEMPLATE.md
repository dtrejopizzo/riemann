# E79.54 - Freezing the transported N^-1 modes globally does NOT compress the zeta residual to a single level

**Scope:** `GAP-Z` only, first compression audit after E79.53.  
**Class:** AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** the slope and
curvature modes do transport on an `N^-1` scale, but freezing them at global
zeta-side means is too coarse. The remaining zeta residual is NOT yet almost a
single scalar level per section, so the `N`-dependence of those coefficients is
still load-bearing.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the two-mode coefficients from E79.52.
E72.16/E77.7az: respected. This is a finite compression audit, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this is the next candid compression

E79.53 showed that both nontrivial coefficients already transport on the same
`N^-1` scale:

```text
a_N ~ alpha / N,
g_N ~ gamma / N.                                                      (54-1)
```

So the sharp next question is:

```text
if alpha and gamma are frozen at their zeta-side transported values, is the
rest already just one scalar level per section?                       (54-2)
```

## 2. Probe

Companion files:

```text
E79_54_PROJECTED_LEVEL_TEMPLATE_PROBE.py
E79_54_projected_level_template_results.json
```

The probe computes the zeta-side transported means

```text
alpha = average_N (N a_N),
gamma = average_N (N g_N),                                            (54-3)
```

and then, for each section in each build, freezes

```text
(alpha/N) sigma + (gamma/N) (sigma-1.375)^2,                          (54-4)
```

leaving only one free scalar level `ell_N`. It audits the fit

```text
residual(sigma; N) ~ ell_N + (alpha/N) sigma + (gamma/N)(sigma-1.375)^2.
                                                                    (54-5)
```

## 3. Result

It does NOT collapse as hoped.

With the zeta-anchored transported means

```text
alpha = -0.005895...,
gamma = -0.002191...,                                                 (54-6)
```

the projected-level template leaves zeta-side normalized max errors

```text
N= 8   0.133
N=10   0.262
N=12   0.0578
N=14   0.0907
N=16   0.0336.                                                       (54-6a)
```

These are much larger than the sectionwise two-mode errors of E79.52, so the
global freeze is too crude.

The planted hard rows are worse again:

```text
N= 8   0.579
N=10   0.489
N=14   0.377,                                                        (54-6b)
```

but the key point is that even zeta does not collapse to a single-level law.

## 4. Reading

This is still useful, because it pinpoints the remaining freedom more sharply:

```text
the two transported modes are real,
but their sectionwise amplitudes cannot yet be replaced by one global pair
(alpha, gamma).                                                       (54-7)
```

So the obstruction is not "there is no modal structure"; it is "the modal
coefficients still carry nontrivial N-dependence".

## 5. Consequence

After E79.52-E79.54, the correct statement is weaker but sharper:

```text
primitive packet
  + two modes that transport on N^-1 scale
  + still-nontrivial sectionwise amplitudes.                          (54-8)
```

So the next candid burden is the `N`-dependence of those amplitudes, not an
arbitrary sigma-shape.

## 6. Status

```text
proved by probe:
  freezing the zeta-side transported means alpha,gamma does NOT reduce the
  residual to a single scalar level per section;

reduced:
  the live burden is now correctly localized in the sectionwise N-dependence of
  the two modal amplitudes, rather than in an unconstrained residual profile;

open:
  identify the transport law for the pair (N a_N, N g_N), beyond simple global
  averaging;

next:
  test whether the pair (N a_N, N g_N) lies near a short one-parameter curve or
  a tiny finite-state pattern on the zeta ladder.
```
