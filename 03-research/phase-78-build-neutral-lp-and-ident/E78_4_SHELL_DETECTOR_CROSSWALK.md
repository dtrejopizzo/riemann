# E78.4 - Crosswalk: the E77 shell cascade after the Phase-78 correction

**Run:** 2026-07-18.
**Purpose:** record, once and cleanly, how the late E77 shell-reduction chain
should be used after the Phase-78 build-neutral LP correction, so that its
exact identities remain available without reintroducing it as an LP forcing
mechanism.

## 1. What Phase 78 changes

Phase 78 does **not** refute the measurements or exact identities discovered in
the E77 shell line. It changes their **role**.

From `phase-78-build-neutral-lp-and-ident/README.md` and
`E77_7AZ_ATTRIBUTION_GATE.md`:

```text
- Outcome A stands: operational LP / BTG-DIV-L is build-neutral.
- Any LP-side scalar whose smallness separates zeta from the plant by order one
  is a DETECTOR under the E72.16 gate, not an admissible forcing mechanism.
- The arithmetic discriminant is quarantined to IDENT.
```

Therefore the late shell chain

```text
PROJECTED-SOURCE-TO-SHORTED-ENERGY
=> PROJECTED-QUADRATIC-BRIDGE
=> EVEN-CHANNEL-QUADRATIC-BRIDGE
=> EVEN-BLOCK-LOCK
=> SMALL-MODE-ALIGNMENT-LAW
=> WEIGHTED-INNER-OUTER-MISMATCH
=> RELATIVE-MISMATCH-LAW
=> ACTIVE-BRANCH-TO-SHELL-BRIDGE
=> ACTIVE-VECTOR-CANCELLATION-DEFECT
```

cannot be used as an LP forcing chain.

## 2. What remains valid and reusable

The following discoveries remain part of the toolkit:

```text
E77.7an  shell residual = Schur source under common-core identification;
E77.7ao  shell collapse is seen after resolvent/projection, not on ||k||;
E77.7aq  odd shell channel is inert; the live shell energy sits in the even 2x2 block;
E77.7ar  zeta even block is nearly rank-one while the plant is not;
E77.7as  zeta residual avoids the small eigendirection of that block;
E77.7au  the alignment defect is an explicit weighted inner/outer mismatch;
E77.7av  the natural scale-free quantity is the relative mismatch.
```

These are **exact identities or detector-grade decompositions**.  They stay
useful as:

1. diagnostics for falsifier location,
2. harness targets for future probes,
3. sources of finite CCM identities that may reappear inside IDENT or a
   build-neutral BTG proof in a different role.

What is archived is only the interpretation

```text
smallness of these shell scalars => LP forcing.
```

## 3. Correct use from here on

The late E77 shell cascade should now be read as:

```text
detector layer:
  RELATIVE-MISMATCH, ACTIVE-VECTOR-CANCELLATION-DEFECT, etc.

reusable exact algebra:
  even/odd block reduction,
  explicit weighted inner/outer mismatch identity,
  Schur-source / shell-residual identification.
```

Admissible reuse rule:

```text
You may reuse the exact finite identities from E77.7an-7au.
You may not reuse the zeta-vs-plant smallness of the shell scalars as an LP
forcing premise unless a separate build-neutral symmetry theorem is proved.
```

## 4. Consequence for current work

The current active strategy does **not** need to be thrown away. It needs to be
retagged:

```text
- as a detector/autopsy program on the shell side;
- as a source of exact finite identities;
- not as the LP proof route.
```

So the honest live fronts after this crosswalk are exactly the Phase-78 fronts:

```text
LP-BTG:     BTG-DIV-L build-neutrally;
LP-interface: SAFE-DISK-IDENT / NEUTRAL-GROUND-CAUCHY, mu-free remnant only;
IDENT:      FIXED-L-WEYL, SAFE-GAMMA-IDENT, OUTER-LIMIT;
closure:    RDP-SHELL, PROLATE, WEIL-TAIL, E77.8/E77.9, final assembly.
```

Meanwhile the shell detector line remains archived but searchable.

## 5. Status

```text
clarified:
  Phase 78 changes the role of the E77 shell cascade, not the truth of its
  exact algebraic identities;

archived as forcing:
  the shell smallness chain E77.7ao-7az;

retained as reusable toolkit:
  exact Schur/shell identities, even-channel reduction, weighted mismatch
  identity, and the associated probe harnesses.
```
