# E79.56 - The scalar amplitude along the zeta modal ray is the live burden; no short law is visible yet

**Scope:** `GAP-Z` only, first audit after the ray reduction of E79.55.  
**Class:** AUTOPSIA HONESTA.  
**What we know after this document that we did not know before:** E79.55 really
does reduce the transported pair to one scalar amplitude along a fixed ray, but
that scalar does not itself collapse to a simple constant-scale or short sign
law on the audited ladder. So the amplitude, not the direction, is the next
honest object.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Uses only the already-audited ray reduction from E79.55.
E72.16/E77.7az: respected. This is a transport autopsy, not a forcing step.
Circularity: respected. No new endpoint identity enters.
```

## 1. Why this audit is necessary

E79.55 reduced the two-mode pair to

```text
(N a_N, N g_N) = rho_N * (1, 0.362905...) + tiny transverse defect.         (56-1)
```

Once the direction is fixed, there are only two remaining questions:

```text
1. does |rho_N| itself collapse to a short amplitude law?
2. does sign(rho_N) follow a tiny finite-state pattern?                      (56-2)
```

If both answers were yes, the whole two-mode transport burden would nearly
close. So this is the first honest post-ray audit.

## 2. Probe

Companion files:

```text
E79_56_RAY_AMPLITUDE_AUTOPSY_probe.py
E79_56_ray_amplitude_autopsy_results.json
```

Using the fixed zeta-side ray slope `k` from E79.55, we project each point
onto the ray:

```text
rho_N := (N a_N + k N g_N)/(1+k^2),   k = 0.362905...                      (56-3)
```

The probe records:

```text
- rho_N, |rho_N|, N|rho_N|;
- the resulting amplitude bands;
- mismatch counts against the smallest obvious sign patterns
  (constant or alternating).                                                (56-4)
```

## 3. Result

On the zeta side,

```text
rho_N =  0.03318, -0.03868, -0.02768, 0.03546, -0.03184                    (56-5)
```

so

```text
|rho_N| = 0.02768 ... 0.03868,   band ratio 1.40,                          (56-6)
```

while the scaled quantity

```text
N |rho_N| = 0.265, 0.387, 0.332, 0.497, 0.509,                             (56-7)
```

has noticeably worse spread:

```text
band ratio 1.92.                                                            (56-8)
```

So the amplitude does stay on an order-one zeta ladder, but it does **not**
show the same sharp collapse that the ray direction showed.

The sign side is also still unresolved. On the audited zeta ladder the pattern
is

```text
+  -  -  +  -                                                               (56-9)
```

and every obvious tiny model already misses at least two rows:

```text
constant sign          -> 2 or 3 misses
simple alternating     -> 2 or 3 misses.                                   (56-10)
```

So the sign pattern is coherent in the weak sense that the two coordinates
share one common sign, but it is not yet a trivial parity law.

By contrast, on the planted build the same projected amplitude is completely
disorganized (`N|rho_N|` band ratio about `7.9e2`), so the ray reduction
remains strongly zeta-specific.

## 4. Reading

This is the right kind of failure.

E79.55 was not a fake simplification: the transport direction really did
collapse. But the scalar amplitude along that direction still carries the live
ladder geometry. More honestly:

```text
the zeta two-mode burden is now:
  fixed ray direction
  + nontrivial scalar amplitude
  + nontrivial but small sign law
  + tiny transverse defect.                                                 (56-11)
```

So the residual burden has been localized, but not yet solved.

## 5. Consequence

After E79.56, the next admissible target is very specific:

```text
find the transport law for rho_N itself,
or reparameterize rho_N by a more intrinsic scalar attached to the packet/edge
geometry that phase 79 has already isolated.                               (56-12)
```

The important point is that we should **not** spend more time re-fitting the
ray direction: that part is already done.

## 6. Status

```text
proved by probe:
  the E79.55 ray reduction is genuine, but the resulting zeta-side amplitude
  rho_N does not yet collapse to a short constant-scale or trivial sign law on
  the audited ladder;

observed:
  |rho_N| stays in a moderate zeta-side band, while N|rho_N| is less stable
  and the sign pattern is not captured by the smallest obvious templates;

reduced:
  the live two-mode transport burden to the scalar amplitude/sign structure
  along a fixed ray, rather than to the full coefficient pair;

open:
  identify the intrinsic scalar law behind rho_N, if one exists;

next:
  compare rho_N directly against packet strength / edge-tail observables
  already isolated in E79.43-E79.46 and E79.3u-3u to test whether the amplitude
  is controlled by the same terminal geometry as the first packet.
```
