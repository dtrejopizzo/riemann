# E77.7az - Attribution gate for the shell-mismatch cascade

**Run:** 2026-07-18.
**Role:** decide, before any further BTG-side work on `SIGNED-ACTIVE-BRANCH-DEFECT`,
whether the plant's order-one failure on the shell-mismatch front is (a) a
detector to be archived, or (b) a genuine relocation of the arithmetic
discriminant from IDENT into LP, formally sanctioned by the E72.16 zero-filter
gate.

## 1. The tension

E77.7av states the shell-side target as

```text
RELATIVE-MISMATCH-LAW:
  prove the relative mismatch is small ON THE ZETA SHELL LADDER.
```

with certified measured values (E77.7av section 3, E77.7ay section 2):

```text
zeta   16->18:  RELATIVE-MISMATCH = 6.4559210e-5
zeta   18->20:  RELATIVE-MISMATCH = 3.1402185e-4
plant  16->18:  RELATIVE-MISMATCH = 1.8666915
```

E77.7ay then refuted branch-order magnitude as the carrier and named the next
object `SIGNED-ACTIVE-BRANCH-DEFECT`, sitting atop the already-proved tower

```text
SIGNED-ACTIVE-BRANCH-DEFECT
=> ACTIVE-BRANCH-TO-SHELL-BRIDGE
=> PHASE5-TO-SHELL-RELATIVE-BRIDGE
=> RELATIVE-MISMATCH-LAW
=> ... => SHELL-RESIDUAL-CANCELLATION
=> ... => BTG-DIV-L
=> scalar Weyl-disk contraction  (LP, front A1).
```

The tension is a location conflict. This entire tower is on the **LP** side
(front A1). But the Falsifier Location Rule (E77.6 section 5; Closure Plan V2
section 6) requires the plant to **pass** operational LP and to **break** in
IDENT (front B: SAFE-GAMMA-IDENT / OUTER-LIMIT). If `SIGNED-ACTIVE-BRANCH-DEFECT`
and everything below it were genuinely **required** for LP, then a plant value
of `1.87` (order one, not small) would break the plant inside **LP**, not IDENT
-- contradicting the required falsifier location, and triggering the E72.16
gate obligation recorded in Closure Plan V2 section 6.

This document resolves the conflict.

## 2. The recorded attribution is Outcome A

The attribution question was decided in E77.1b (`E77_1B_ATTRIBUTION_ENVELOPES.md`,
README lines 46-51): the working verdict is **Outcome A**.

```text
Outcome A: operational LP holds for BOTH builds.
           Planted S_N also diverges (slowly); zeta contracts faster.
           LP is arithmetic-free as designed; the discriminant is IDENT;
           the rate separation is a finite-size shadow of the IDENT failure.
```

Under Outcome A the object genuinely required for LP is **falsifier-neutral by
construction**. E77.7f makes this precise and explicit: the corrected LP
endpoint is `BTG-DIV-L`, which is

```text
"equivalent sectionwise to fixed-mu canonical-energy growth"  (E77.7f),
```

i.e. `S_N(mu_L) -> infinity`. That divergence is exactly the LP object E77.1b
found holds -- slowly -- for **both** builds. So:

```text
BTG-DIV-L is falsifier-neutral: it must hold for zeta AND for the plant.
```

This is not an assumption; it is forced by the conjunction of E77.1b (Outcome A)
and E77.7f (BTG-DIV-L = canonical-energy divergence).

## 3. The decisive step: an over-strong sufficient condition is a detector

`RELATIVE-MISMATCH-LAW` is offered as a **sufficient** condition for BTG-DIV-L:

```text
RELATIVE-MISMATCH-LAW => ... => BTG-DIV-L.
```

But a sufficient condition that is **false** for a build on which the
**conclusion is true** cannot be a faithful reduction. Concretely:

```text
plant:  RELATIVE-MISMATCH = 1.87      (RELATIVE-MISMATCH-LAW fails);
plant:  BTG-DIV-L holds               (Outcome A, section 2).
```

So `RELATIVE-MISMATCH-LAW` is strictly stronger than the thing it is meant to
force. Its build-discriminating content (`1e-4` vs `1.87`) is precisely the part
that BTG-DIV-L does **not** need. That surplus is arithmetic information about
the zero locations riding on a quantity that LP itself does not require.

This is exactly the E72.16 zero-filter pattern.

## 4. Applying the E72.16 zero-filter gate

E72.16 (`phase-72-feshbach-leakage-calculus/E72_16_ZERO_FILTER_GATE.md`) governs
any scalar whose smallness discriminates zeta from off-line builds. Its
Theorem 72.16 shows that a family of finite Mellin/CCM scalar projections that
converges to a nonzero analytic limit and vanishes on the off-critical divisor
**is** a zero-filter: its divisor contains the off-critical zeta divisor. Such a
quantity is admissible as a **forcing mechanism** only under one of

```text
option 1: an analytic zero-filter forced by finite CCM/prolate algebra alone
          (dangerous: circular if it is Xi or a quotient containing Xi);
option 2: a finite-CCM SYMMETRY forcing signed cancellation among maximal
          resonances, WITHOUT using the zero locations as input (the only
          plausible non-circular path);
otherwise: it is a DETECTOR, archived, not pursued as forcing (E77.6 sec. 6).
```

Map the shell-mismatch cascade onto this trichotomy:

- The RELATIVE-MISMATCH is a scalar built from the finite Schur/shell active
  vector; it is `~1e-4` on the zeta ladder and `~1.87` on the plant. Its
  smallness tracks the on-line divisor. This is the Theorem-72.16 shape.
- E77.7ay **already tried and failed** to derive that smallness from a
  finite-CCM symmetry: branch ordering (`boundary > outer > inner`) is
  explicitly labeled a "regime classifier," not the carrier. That is the
  option-2 route, and E77.7ay refuted it. `SIGNED-ACTIVE-BRANCH-DEFECT` is the
  proposal to keep searching for that symmetry.
- No option-1 finite CCM zero-filter has been produced (and any that reproduced
  the `1e-4` vs `1.87` split would, by section 3, be encoding more than
  BTG-DIV-L needs -- i.e. the divisor).

Therefore, under the current (Outcome A) attribution, the shell-mismatch scalar
falls in the **detector** branch of E72.16. It cannot be promoted to a forcing
mechanism without first exhibiting the option-2 finite-CCM symmetry -- which is
the very thing E77.7ay refuted at the branch-order level and which
`SIGNED-ACTIVE-BRANCH-DEFECT` merely re-proposes one level finer.

## 5. Verdict

**The gate resolves to (a): archive.** Explicitly:

```text
1. SIGNED-ACTIVE-BRANCH-DEFECT, RELATIVE-MISMATCH-LAW, and the whole
   E77.7av--ay shell-mismatch cascade are DETECTORS, not forcing mechanisms.
   They separate zeta from the plant precisely because they carry surplus
   arithmetic (zero-location) content beyond what BTG-DIV-L requires.
   They are archived under the E77.6 section 6 admissibility rule, exactly as
   the E77.5d--5ah sign/cone chain was archived in E77.6.

2. The relocation option (b) is NOT sanctioned. Relocation would require
   Outcome B -- a theorem-grade demonstration that the plant genuinely FAILS
   limit-point (a real l2 kernel / no canonical-energy divergence). The
   recorded evidence is the opposite: E77.1b found planted S_N diverges
   (slowly), and E77.7f identifies BTG-DIV-L with that divergence. Absent an
   overturn of Outcome A, there is no discriminant in LP to relocate.

3. Consequently BTG-DIV-L must be pursued as a FALSIFIER-NEUTRAL theorem:
   for any lower-semibounded H_L = D_L + B_L with compact resolvent (E77.7d),
   fixed-mu canonical energy diverges and the bordered Weyl disks contract.
   Its proof may not route through any build-discriminating shell scalar; if a
   proposed step separates zeta from the plant by order one, that step is --
   by sections 3--4 -- carrying more than LP needs and is inadmissible as
   forcing.

4. The arithmetic discriminant is quarantined to IDENT (SAFE-GAMMA-IDENT /
   OUTER-LIMIT, front B), exactly where the Falsifier Location Rule places it
   and where E77.6's derivative probe already measures the plant break
   (mismatch 10.98--50.47 at the arithmetic target).
```

This is the internally consistent reading: the shell rate-separation is the
"finite-size shadow of the IDENT failure" that Outcome A predicted from the
start (README lines 63-67). The program has been measuring that shadow with
ever-finer instruments (E77.7aa--ay) and mistaking a detector for a forcing
target.

## 6. Consequence for the frontier

```text
A1 (BTG side):   the SIGNED-ACTIVE-BRANCH-DEFECT / RELATIVE-MISMATCH branch is
                 CLOSED as a detector. The live BTG object reverts to the
                 falsifier-neutral BTG-DIV-L (E77.7f), to be proved abstractly
                 from compact-resolvent + disk-contraction, build-independently.
                 CAUTION: E77.7ak's SHELL-RESIDUAL-CANCELLATION inherits the same
                 scrutiny -- if its proof leans on the measured zeta/plant shell
                 separation, it is a detector too; only a build-neutral form of
                 it is admissible.

A2 (interface):  SAFE-DISK-IDENT / BORDERED-WEYL-COMPLETENESS is build-neutral
                 by nature (separation of Cauchy rows, pencil compatibility,
                 normalized class, simplicity/nonvanishing at mu_L). Unaffected
                 by this gate; remains the cleanest live LP-interface target.

B  (IDENT):      unchanged and confirmed as the true home of the discriminant:
                 FIXED-L-WEYL, SAFE-GAMMA-IDENT, OUTER-LIMIT.
```

## 7. Status

```text
decided:   the shell-mismatch cascade is a DETECTOR (option a of the gate),
           archived under E77.6 section 6; relocation (option b) not sanctioned
           because Outcome A (E77.1b) leaves no LP-side discriminant.
proved:    BTG-DIV-L is falsifier-neutral (E77.1b Outcome A + E77.7f identity of
           BTG-DIV-L with canonical-energy divergence).
refuted:   SIGNED-ACTIVE-BRANCH-DEFECT / RELATIVE-MISMATCH-LAW as forcing
           mechanisms for LP -- they are over-strong (false for the plant while
           BTG-DIV-L is true for the plant), hence E72.16 detectors.
archived:  E77.7av--ay shell-mismatch branch, and any future finer refinement of
           the same build-discriminating shell scalar.
live:      BTG-DIV-L (build-neutral, abstract); SAFE-DISK-IDENT; the IDENT
           triple FIXED-L-WEYL / SAFE-GAMMA-IDENT / OUTER-LIMIT.
gate:      no zero-filter is admitted; any LP step that separates the builds by
           order one is inadmissible as forcing per E72.16.
```
