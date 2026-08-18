# E79.43 - The sparse packet is the optimizer of the raw coupled matching functional, but no geometric penalty survives

**Scope:** `GAP-Z` only, first directly coupled `common-cloud + ZERO^extra`
functional.  
**Class:** REDUCCION GENUINA + AUTOPSIA FRANCA.  
**What we know after this document that we did not know before:** once
`ZERO^extra` is allowed to enter the objective directly, the zeta-side sparse
packet becomes almost completely reconstructible. But the winning rule is the
degenerate one with **no** geometry penalty at all. So the remaining difficulty
is no longer “find the support somehow”, but “explain why the raw coupled
matching itself picks these supports, and why no universal low-complexity
penalty improves it”.

## 0. Wall checklist

```text
MW-1:  respected. No positivity target appears.
MW-2:  respected. Fixed-L / Re(s)>1 convergence front only.
MW-3:  respected. No local/global prime assembly.
MW-4:  respected. No sign-lower-bound forcing.
MW-5:  respected. No site/cohomology input.
MW-6:  respected. No gap hypothesis.
K1-K5: respected. Direct finite packet bookkeeping only.
E72.16/E77.7az: respected. This is now an explicitly coupled anatomy probe, not
                an admissible build-neutral forcing step.
Circularity: respected. The selector uses only the audited terminal common-cloud
             shells together with ZERO^extra.
```

## 1. Starting point

After E79.42, the support-only route had been exhausted enough to justify the
next move:

```text
let ZERO^extra enter the selector directly, and ask whether the sparse packet is
the optimizer of a universal low-complexity coupled rule.                (43-1)
```

That is the first probe in the phase where the common cloud is not forced to
guess the support alone.

## 2. Probe

Companion files:

```text
E79_43_COUPLED_PACKET_FUNCTIONAL_PROBE.py
E79_43_coupled_packet_functional_results.json
```

Inside the last 4 active shells, every subset `S` is scored by

```text
J(S) = |packet(S) - ZERO^extra|
     + lambda * (#blocks(S)-1)
     + mu * |S|,                                                        (43-2)
```

with

```text
lambda in {0, 0.01, 0.05, 0.10},
mu     in {0, 0.01, 0.05, 0.10}.                                        (43-3)
```

So the selector is coupled to `ZERO^extra`, but still tries to reward simple
geometry through block-count and support-size penalties.

## 3. Result: zeta is reconstructed almost exactly, but only by the unpenalized rule

At `sigma = 1`, zeta gives:

```text
N      sparse packet                  best coupled support
8      {6,7,8}   0.02288             {6,7,8}      0.02288
10     {5}       0.02948             {7,8,9,10}   0.00870
12     {7}       0.02299             {7}          0.02299
14     {10,11,12} 0.02148            {10,11,12}   0.02148
16     {11,13}   0.03554             {11,13}      0.03554              (43-4)
```

Mean mismatch:

```text
sparse packet   0.02648...
best coupled    0.02232...                                              (43-5)
```

So the coupled rule does something genuinely new:

```text
it reconstructs the zeta-side packet almost completely, and even improves the
N=10 fit by preferring the full 4-shell terminal packet.                (43-6)
```

But the equally important fact is:

```text
every winning zeta-side rule is lambda = 0, mu = 0.                     (43-7)
```

The best selector is the raw matching functional

```text
J(S) = |packet(S) - ZERO^extra|                                         (43-8)
```

with **no** surviving complexity correction.

## 4. Reading

This changes the status of the live object in an important way.

Before E79.43, the open question still looked like:

```text
what intrinsic geometry picks the packet?                               (43-9)
```

After E79.43, the sharper statement is:

```text
once the common cloud is allowed to talk directly to ZERO^extra, the packet is
already there; what is missing is not the existence of a packet, but a universal
geometric principle that refines raw matching.                          (43-10)
```

In other words, the coupled packet is easy; the universal penalty is hard.

## 5. Plant side

The plant side shows why this still does not close anything:

```text
N= 8:  best coupled = {10,11},   mismatch = 0.0153
N=10:  best coupled = {13,15},   mismatch = 0.0700
N=12:  best coupled = {0},       mismatch = 0.8368
N=14:  best coupled = {0,1},     mismatch = 0.7150
N=16:  best coupled = {0},       mismatch = 0.8146                    (43-11)
```

and again the winning parameters are always

```text
lambda = 0, mu = 0.                                                     (43-12)
```

So the coupled rule does not supply any discriminating universal geometry. It
just says:

```text
for each build separately, the best terminal packet is whatever best matches
ZERO^extra on that section.                                             (43-13)
```

That is anatomically useful, but not yet theorem-grade.

## 6. Consequence

This is still a real reduction, because it localizes the obstruction more
cleanly than any support-only probe:

```text
the hard problem is not "is there a tiny coupled packet?" -- yes, there is.
the hard problem is "why should a universal low-complexity penalty select the
right packet nontrivially?"                                             (43-14)
```

So the frontier narrows to:

```text
raw coupled matching works;
universal geometric refinement does not.                                (43-15)
```

That is a much more precise diagnosis than we had before.

## 7. Status

```text
proved by probe:
  the zeta-side sparse packet is almost completely reconstructible as the
  optimizer of the raw coupled matching functional |packet-extra|;

observed:
  the winning parameters are always lambda = mu = 0 on both builds, so no
  universal low-complexity penalty survives;

reduced:
  the open problem is no longer to find a packet, but to understand or refine
  the raw coupled matching principle in a way that is nontrivial and stable;

open:
  identify the first non-degenerate refinement of raw coupled matching, or
  prove that no simple refinement exists on the audited ladder;

next:
  test whether any universal penalty can improve raw matching uniformly, or
  whether the candid next object is the raw coupled packet itself.
```
