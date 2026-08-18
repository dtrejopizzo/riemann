# E79.55 - The transported two-mode coefficient pair collapses to one signed ray on the zeta ladder

**Scope:** `GAP-Z` only, transport geometry of the two-mode coefficients from
E79.52-E79.54.  
**Class:** REDUCCION GENUINA.  
**What we know after this document that we did not know before:** the remaining
sectionwise freedom in the zeta-side pair `(N a_N, N g_N)` is not genuinely
two-dimensional on the audited ladder. It collapses almost completely to one
ray through the origin, up to a sign flip and a small amplitude drift.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the already-audited two-mode coefficients.
E72.16/E77.7az: respected. This is a finite transport audit, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this is the right next reduction

E79.54 killed the crude freeze

```text
a_N ~ alpha/N,   g_N ~ gamma/N
```

with global constants `alpha,gamma`: the sectionwise `N`-dependence is still
load-bearing. But E79.52-E79.53 left open a sharper possibility:

```text
the pair (N a_N, N g_N) might still live near a one-parameter ray,
rather than filling a genuine 2-dimensional region.                         (55-1)
```

That is the smallest candid geometric question left before inventing richer
templates.

## 2. Probe

Companion files:

```text
E79_55_MODAL_RAY_REDUCTION_probe.py
E79_55_modal_ray_reduction_results.json
```

For each audited row we form

```text
x_N := N a_N,
y_N := N g_N.                                                             (55-2)
```

Then we test the simplest origin-pinned model:

```text
y_N ~ k x_N,                                                              (55-3)
```

both with sign and in absolute value. The output records:

```text
- the points (x_N,y_N);
- the signed and absolute best-fit ray slopes k;
- the max relative fit error;
- the sign pattern along the ladder.                                      (55-4)
```

## 3. Result

On the zeta side, the collapse is extremely strong.

The audited points are:

```text
N= 8   ( 0.03321,  0.01196)
N=10   (-0.03867, -0.01409)
N=12   (-0.02767, -0.01008)
N=14   ( 0.03548,  0.01283)
N=16   (-0.03183, -0.01159).                                             (55-5)
```

So the two coordinates always have the same sign, and the ratio is already in a
very narrow band:

```text
|N a_N| / |N g_N| = 2.744, 2.746, 2.746, 2.765, 2.776.                   (55-6)
```

The best signed origin-pinned fit is

```text
N g_N ~ 0.362905 * (N a_N),                                              (55-7)
```

equivalently

```text
N a_N ~ 2.75554 * (N g_N),                                               (55-8)
```

with max relative error only

```text
0.73%.                                                                    (55-9)
```

So, on the audited zeta ladder, the residual two-mode coefficient pair is
already one-dimensional to very high accuracy.

By contrast, the planted build does not show any comparable collapse:

```text
- corr(Na,Ng) is not even positive/coherent;
- the angle spread is large;
- the best ray fit has order-one relative error.                         (55-10)
```

## 4. Reading

This sharpens E79.54 in the right way.

The obstruction was not that the coefficient pair needed two free transport
coordinates. It was that the pair still carried one residual ladder amplitude
and one sign choice. More candidly:

```text
(N a_N, N g_N) = rho_N * (1, 0.362905...) up to a common sign and tiny error. (55-11)
```

So the zeta-side two-mode burden reduces from "an arbitrary pair of amplitudes"
to

```text
one scalar amplitude rho_N
+ one coherent sign flip pattern
+ a sub-percent transverse defect.                                        (55-12)
```

That is a real reduction, not just a prettier fit.

## 5. Consequence

After E79.55, the candid next object is no longer the full pair
`(N a_N, N g_N)`. It is the scalar ladder amplitude multiplying the common ray:

```text
primitive packet
  + modal ray direction (now essentially fixed)
  + scalar amplitude rho_N along that ray
  + tiny transverse defect.                                               (55-13)
```

So the next transport audit should ask whether `rho_N` itself follows a short
law on the zeta ladder, and whether the plant fails that law on the hard rows.

## 6. Status

```text
proved by probe:
  on the audited zeta ladder the transported coefficient pair (N a_N, N g_N)
  lies on a single signed ray through the origin to sub-percent relative error;

observed:
  the planted build has no comparable one-ray collapse;

reduced:
  the live residual transport burden from a 2-parameter coefficient pair to a
  single scalar ladder amplitude along a fixed ray, plus a tiny transverse error;

open:
  identify the transport law for that scalar amplitude rho_N and its sign
  pattern on the zeta ladder;

next:
  parameterize the zeta-side pair by rho_N and audit whether rho_N itself lies
  in a narrow band, a short recurrence, or a tiny finite-state ladder.
```
