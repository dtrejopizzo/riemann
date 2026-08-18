# E78.84 - The endpoint quotient tracks `u`-sector size more directly than `Q_theta` curvature

**Run:** 2026-07-19.  
**Scope:** IDENT, fixed-`L` finite front, left endpoint slice `sigma=1.0`.

## 1. Purpose

E78.83 reduced the radial weighted front to the exact one-step quotient

```text
Q_N := (-SAFEDELTA_N(i sigma)) / Delta safe_u_N.       (EQA-1)
```

The next question is what existing finite object best explains this quotient.

A tempting guess is the already certified curvature carrier

```text
Q_theta,N = N^2 ( N Delta safe_u_N - (N+2) Delta safe_u_{N+2} ). (EQA-2)
```

from E78.24. This note audits that shortcut against the competing `u`-sector
geometry on the left endpoint slice.

## 2. Competing explanations

At `sigma=1.0`, the natural candidates are:

```text
curvature scale:      Q_theta,N / (N^2 Delta safe_u_N),         (EQA-3)
u-size scale:         |u_N|,                                     (EQA-4)
sector scale:         Im(u_N) - |Re(u_N)|,                       (EQA-5)
cone ratio:           M_N = (Im(u_N)^2 - Re(u_N)^2)/|u_N|^2.     (EQA-6)
```

If the quotient were essentially a curvature law, `(EQA-3)` should explain it
better than the `u`-sector quantities. If not, the radial branch should stay
aligned with the `u`-sector rather than with `Q_theta`.

## 3. Probe audit

Companion:

```text
E78_84_endpoint_quotient_autopsy_probe.py
E78_84_endpoint_quotient_autopsy_results.json
```

The probe compares the endpoint quotient `Q_N` against the four candidates on
the common audited left-endpoint ladder `N=8,...,20`.

## 4. Observed outcome

The quotient correlates only moderately with the curvature scale:

```text
corr( Q_N, Q_theta/(N^2 Delta safe_u) ) ≈ -0.522.      (EQA-7)
```

That is the wrong sign for a clean direct transfer.

By contrast the quotient tracks the `u`-sector quantities strongly:

```text
corr( Q_N, |u_N| )                  ≈ 0.972,
corr( Q_N, Im(u_N)-|Re(u_N)| )      ≈ 0.989,
corr( Q_N, M_N )                    ≈ 0.676.           (EQA-8)
```

So the endpoint quotient is much closer to a `u`-sector size law than to a
second-drift curvature law.

The raw ratio bands tell the same story:

```text
Q_N / |u_N|
  in [11.44, 25.77],                                   (EQA-9)

Q_N / (Im(u_N)-|Re(u_N)|)
  in [12.21, 42.82],                                   (EQA-10)

Q_theta/(N^2 Delta safe_u)
  in [1.53, 2.12].                                     (EQA-11)
```

Curvature is too flat and too misaligned to be the direct carrier of `Q_N`.

## 5. Autopsy

This kills the shortcut

```text
Q_theta  ->  endpoint quotient Q_N                      (EQA-12)
```

as a primary explanation of the radial weighted front.

That does **not** make `Q_theta` irrelevant. It remains the exact carrier of
the shell curvature law from E78.24. But the endpoint quotient is a different
comparison object:

```text
radial derivative / shell drift,                        (EQA-13)
```

and it is governed much more directly by the one-step `u`-sector geometry.

## 6. Consequence

The next candid reduced target is therefore not curvature-first, but

```text
SECTOR-SIZE-QUOTIENT:
  control (-SAFEDELTA_N(i sigma_L)) / Delta safe_u_N
  from finite bounds on the size and verticality of u_N. (EQA-14)
```

This fits the architecture already in the ledger:

```text
U-PHASE-LAW / QUADRATIC-CONE-CERTIFICATE
  feed safe_u geometry,
and the endpoint quotient is now seen to sit on that branch,
not on the Q_theta curvature branch.                    (EQA-15)
```

## 7. Candid reading

This note does not prove the sector-size quotient law.

What it proves is that the quotient branch and the curvature branch should no
longer be conflated. The current endpoint quotient is better explained by
`u`-sector size than by `Q_theta`.

That is a real clarification because it prevents another false reduction and
keeps the radial front attached to the right finite objects.

## 8. Status

```text
refuted:
  the endpoint quotient is not primarily explained by the curvature scale
  Q_theta/(N^2 Delta safe_u);

observed:
  on the audited left endpoint slice the quotient correlates strongly with
  |u_N| and the sector margin, but only moderately and wrong-signed with the
  curvature scale;

clarified:
  the next candid radial endpoint object is SECTOR-SIZE-QUOTIENT;

reduced:
  SAFEDELTA-SAFEU-QUOTIENT away from the curvature branch and onto the
  u-sector size branch.
```
