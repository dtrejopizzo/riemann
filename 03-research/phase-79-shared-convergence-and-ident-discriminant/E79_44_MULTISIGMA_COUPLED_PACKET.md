# E79.44 - Raw coupled matching survives the multisigma coherence test

**Scope:** `GAP-Z` only, stronger follow-up to E79.43.  
**Class:** REDUCCION GENUINA + AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** the
degenerate raw coupled rule from E79.43 is not a one-sigma accident. On the
audited zeta ladder, the same support already minimizes the coupled mismatch
simultaneously across several safe sigma slices, and nonzero geometry penalties
still never win.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct finite packet bookkeeping only.
E72.16/E77.7az: respected. This remains an anatomy probe, not an admissible
                build-neutral forcing step.
Circularity: respected. Uses only terminal common-cloud shells and ZERO^extra.
```

## 1. Why this probe was necessary

E79.43 showed:

```text
the zeta-side sparse packet is almost reconstructed by the raw coupled rule
|packet - ZERO^extra|,
but every winning parameter choice is lambda = mu = 0.                 (44-1)
```

That still left one loophole:

```text
maybe the degeneracy is only a one-sigma artifact, and once one asks for one
support to work across several safe sigma slices, a nontrivial geometric
penalty becomes necessary.                                             (44-2)
```

E79.44 tests exactly that loophole.

## 2. Probe

Companion files:

```text
E79_44_MULTISIGMA_COUPLED_PACKET_PROBE.py
E79_44_multisigma_coupled_packet_results.json
```

For each audited section `N`, the probe uses the same terminal window as
E79.43 but now demands a **single support** that works simultaneously for

```text
sigma in {0.75, 1.0, 1.5, 2.0}.                                       (44-3)
```

For every subset `S` in the last `4` active shells it scores

```text
J_mean(S) = average_sigma mismatch_sigma(S)
          + lambda * (#blocks(S)-1)
          + mu * |S|,                                                 (44-4)

J_max(S)  = max_sigma mismatch_sigma(S)
          + lambda * (#blocks(S)-1)
          + mu * |S|,                                                 (44-5)
```

with the same penalty grid as E79.43:

```text
lambda, mu in {0, 0.01, 0.05, 0.10}.                                 (44-6)
```

So the support must now be coherent across several safe sigma slices, not just
one.

## 3. Result: zeta keeps the same supports, and penalties still die

At `sigma=1` and `sigma=2`, E79.43 had already hinted at exact agreement of the
best raw-coupled supports on the zeta side. E79.44 strengthens this:

```text
zeta, mean-aggregated optimum:
N= 8   support {6,7,8}
N=10   support {7,8,9,10}
N=12   support {7}
N=14   support {10,11,12}
N=16   support {11,13}                                               (44-7)
```

and these are exactly the same supports selected by the one-sigma optimum in
E79.43.

Moreover, the winning parameter choice is still always

```text
lambda = 0, mu = 0,                                                   (44-8)
```

for both the mean and max aggregators on the audited zeta ladder.

So the zeta-side packet is not merely a lucky `sigma=1` fit:

```text
the same raw-coupled support already matches ZERO^extra coherently across a
whole safe sigma family.                                               (44-9)
```

The actual zeta-side mismatch levels stay small across the full family:

```text
N= 8   mean 0.0243   max 0.0274
N=10   mean 0.00736  max 0.00932
N=12   mean 0.0222   max 0.0234
N=14   mean 0.0224   max 0.0242
N=16   mean 0.0349   max 0.0359                                        (44-9a)
```

## 4. Plant side

The plant side behaves differently in exactly the way one would want from an
anatomy probe:

```text
- the multisigma mean optimum becomes unstable and can jump to supports
  {14}, {17}, {0}, {25}, {0};
- the mismatch level is then huge (mean about 0.68-1.07, max about 0.85-1.71);
- yet even there, nonzero penalties still do not rescue a universal geometry.
                                                                    (44-10)
```

So the multisigma strengthening increases the contrast in support stability,
not through a new penalty law, but through whether the raw-coupled packet is
already coherent across sigma.

## 5. Reading

This closes one plausible escape hatch from E79.43.

Before E79.44, one could still hope:

```text
single-sigma raw matching works, but a multisigma requirement will force the
first nontrivial geometric refinement.                                 (44-11)
```

After E79.44, the sharper statement is:

```text
even the multisigma coherence test does not force any nonzero universal
penalty; the zeta-side packet is already stable under raw coupled matching
alone.                                                                 (44-12)
```

That means the live question has narrowed further:

```text
either the candid next finite object really is the raw coupled packet itself,
or any surviving refinement has to involve something richer than block-count,
support-size, or multisigma consistency of a fixed terminal support.    (44-13)
```

## 6. Consequence

This is not a closure, but it is a real reduction:

```text
the degeneracy of E79.43 is structurally stable under safe-sigma coupling. (44-14)
```

So the next admissible move is no longer to try another tiny geometric penalty
of the same flavor. The next object has to be richer, for example:

```text
- a signed residual after subtracting the raw coupled packet,
- a cross-section transport rule for that packet,
- or an explicit theorem-grade claim that raw coupled matching is itself the
  next primitive object.                                               (44-15)
```

## 7. Status

```text
proved by probe:
  the zeta-side raw coupled support from E79.43 already minimizes the coupled
  mismatch simultaneously across sigma in {0.75,1.0,1.5,2.0};

observed:
  nonzero block-count and support-size penalties still never win on the audited
  zeta ladder, even under multisigma coherence demands;

reduced:
  the E79.43 degeneracy is structurally stable, not a one-sigma accident;

open:
  identify the first refinement beyond raw coupled matching that is genuinely
  richer than these small geometric penalties, or promote the raw coupled
  packet itself to the next primitive finite object;

next:
  test residual-based refinements of the raw coupled packet, rather than more
  support-only or penalty-only selectors.
```
