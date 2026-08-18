# 107.75 -- Paper A unified finite-support synthesis audit

## 1. Purpose

`107_34`, `107_35`, and `107_64` exact-audit three different load-
bearing layers of Paper A, but `107_06` still lacked one audit artifact
for the synthesis claim itself:
that one finite-support source package really assembles into one
coherent arithmetic pairing, rather than into independent local rules
checked only one by one.

This note exact-audits that synthesis shadow.

## 2. Exact shadow audited here

The verifier `107_75_paper_a_unified_synthesis_audit.py` exact-audits a
single finite symbolic model of `107_06` in which:

1. disconnected Euler unions are killed by connected extraction before
   entering the pairing;
2. off-diagonal finite contributions survive only on visible
   prime-power support pairs;
3. the same Green functional governs both cross-pairings and
   self-pairings;
4. the resulting bilinear package satisfies exact polarization and
   cutoff independence once the visible support is contained in the
   cutoff window;
5. inserting either decomposable source mass or a diagonal-only shift
   changes the result in exactly detectable ways.

So the milestone theorem of `107_06` is pressure-tested as one package,
not merely as a list of previously separate ingredients.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact Paper A unified-synthesis checks passed.
```

So the workspace now contains a reproducible finite audit that the
visible Milestone I package behaves like one coherent source-defined
pairing in a shared exact model.

## 4. What this proves and what it does not

This audit proves a narrow but useful point:

1. the connected extractor, finite prime-power support law, and common
   Green closure can be realized together in one exact symbolic model;
2. decomposable Euler data do not survive into the primitive pairing;
3. diagonal-only renormalization is still visible as a genuine defect of
   the unified package.

It does **not** prove:

1. the full analytic archimedean metric theorem of `107_05`;
2. a published arithmetic-surface realization over
   \(\mathrm{Spec}\,\mathbf Z\);
3. the later Lefschetz, Picard/Jacobian, or Hodge steps of Phase 107.

So the correct reading is:

\[
 \text{finite unified Milestone I synthesis shadow exact-audited},
 \qquad
 \text{full target-side metric theorem still open}.
 \]
