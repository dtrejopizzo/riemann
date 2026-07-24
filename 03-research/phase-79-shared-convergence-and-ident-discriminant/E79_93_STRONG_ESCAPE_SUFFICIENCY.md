# E79.93 - Strong escape is a sufficient signature of the zeta-side route, but not a necessary condition for all near-coherence

**Scope:** `DISCRIMINANT`, follow-up to the asymmetric corrections of E79.91-E79.92.  
**Class:** REDUCCION GENUINA + honest asymmetry audit.  
**What we know after this document that we did not know before:** on the
audited ladder, `STRONG_ESCAPE` already behaves as a clean sufficient signature
for the zeta-side route:

```text
STRONG_ESCAPE  =>  GEOM and high coherence on the audited data,         (93-1)
```

but it is **not** a necessary condition for every finite near-coherent row or
step, because the planted side still has cloud-only resonances.

## 0. Why this is the next honest question

After E79.91-E79.92, the phase-79 front became explicitly asymmetric:

```text
- the escape half is rigid and denominator-driven,
- the low-defect half is permissive and can be mimicked by planted rows. (93-2)
```

That naturally suggests one sharper audit:

```text
is STRONG_ESCAPE already enough to identify the honest zeta-side geometry /
coherence route, even if it does not capture every accidental near-coherence? (93-3)
```

This is exactly the kind of statement that can shrink the live front without
claiming a false converse.

## 1. Data used

No new heavy finite build is needed. This note combines:

```text
- sectionwise escape/geometry data from E79.90,
- stepwise coherence data from E79.83.                                 (93-4)
```

On the audited ladder:

```text
sections: N = 8,10,12,14,16,18,
steps:    N -> N+2 from 8->10 through 16->18.                          (93-5)
```

We use the E79.90 predicate

```text
STRONG_ESCAPE := |(q^T x)/c| / mesh_radius > 50,                       (93-6)
```

and the E79.83 high-coherence regime

```text
coherence_fraction > 0.99.                                              (93-7)
```

## 2. Result

### Sectionwise geometry

From E79.90:

```text
- every audited STRONG_ESCAPE row is a zeta row,
- every audited STRONG_ESCAPE row also satisfies GEOM,
- no planted row satisfies STRONG_ESCAPE.                               (93-8)
```

So on the audited section ladder:

```text
STRONG_ESCAPE is already a sufficient signature of the zeta-side geometry
route.                                                                  (93-9)
```

### Stepwise coherence

From E79.83:

```text
- all five audited zeta steps have coherence_fraction > 0.99,
- no plant_gamma1 step does,
- exactly one plant_gamma2 step does: 12->14 with coherence ~ 0.999772. (93-10)
```

That exceptional planted step is exactly the cloud-only resonance already
named in E79.87/E79.92:

```text
near-coherence without STRONG_ESCAPE, without closure, without balance. (93-11)
```

So the honest reading is:

```text
STRONG_ESCAPE is sufficient for the audited zeta-side route,
but not necessary for every isolated finite near-coherence event.       (93-12)
```

## 3. Reading

This is the right asymmetric statement for the current evidence.

The false strong claim would be:

```text
high coherence  <=>  STRONG_ESCAPE.                                     (93-13)
```

The audited data do **not** support that, because of the planted
`gamma2, 12->14` resonance.

But the weaker and useful statement **is** supported:

```text
STRONG_ESCAPE picks out the honest zeta-side route cleanly on the audited
ladder, while the converse fails only through already-understood planted
resonances.                                                             (93-14)
```

That is exactly the kind of asymmetry the phase now needs.

## 4. Consequence

After E79.93, the live burden sharpens again:

```text
the escape side no longer needs to be justified by a biconditional.
It is enough to show that the zeta-side route must enter STRONG_ESCAPE,   (93-15)
```

with any remaining planted near-coherence treated as detector-grade
resonances rather than as counterexamples to the mechanism.

So the next honest target is:

```text
derive why the codimension-one closure regime forces STRONG_ESCAPE
theorem-grade, with only a mild numerator regularity hypothesis.        (93-16)
```

## 5. Status

```text
proved by audit:
  on the audited section ladder, STRONG_ESCAPE is already a sufficient
  signature of the zeta-side geometry regime;

proved by audit:
  the converse fails only through the already-named cloud-only planted
  resonance, so the asymmetry is real rather than accidental;

clarified:
  the escape mechanism should be pursued as a sufficient forcing route,
  not as a biconditional classifier of every finite near-coherence event;

reduced:
  the live front to a theorem-grade derivation of the zeta-side entrance into
  STRONG_ESCAPE from the closure regime.
```
