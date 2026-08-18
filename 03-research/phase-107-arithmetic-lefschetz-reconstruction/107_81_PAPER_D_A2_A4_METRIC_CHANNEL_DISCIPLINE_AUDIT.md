# 107.81 -- Paper D A2/A4 metric-channel discipline audit

## 1. Purpose

`107_45`, `107_54`, `107_55`, and `107_74` exact-audit important
pieces of the candidate metric story, but one joint Route A question
still remained implicit:
can the visible normal-crossings profile, the single remainder channel,
and the nonnegative local support package coexist in one exact target-
side shadow without creating extra archimedean channels or negative
logarithmic coefficients?

This note exact-audits that discipline shadow.

## 2. Exact shadow audited here

The verifier
`107_81_paper_d_a2_a4_metric_channel_discipline_audit.py`
exact-audits one finite symbolic model in which:

1. every visible chart presentation determines one intrinsic
   normal-crossings profile on the slots
   \((B_{\rm v}, B_{\rm h}, \Delta)\);
2. one and only one regular remainder channel survives under chart
   transport, rooted refinement, and visible packaging;
3. every visible polarization-active blow-up preserves the nonnegative
   coefficient cone of the same profile;
4. introducing either a fourth singular direction or an extra remainder
   receiver is rejected exactly;
5. the visible corner profile still controls the lower, upper,
   diagonal, and interior restrictions after those local effectivity
   checks.

So the audit pressure-tests the candidate metric as one disciplined
visible package rather than as several unrelated local shadows.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact Route A A2/A4 metric-channel discipline checks passed.
```

So the workspace now contains a reproducible exact audit that the
visible candidate metric keeps one singular profile, one remainder
channel, and one nonnegative local support cone in the same finite
model.

## 4. What this proves and what it does not

This audit proves a narrow but useful point:

1. the visible A2 and A4 shadows can now be read as one coherent
   target-side discipline rule;
2. extra singular or remainder channels are finitely falsifiable in the
   same model that preserves local log-effectivity;
3. the current blow-up/effectivity program does not by itself threaten
   the single-channel metric picture.

It does **not** prove:

1. actual analytic integrability or semipositivity on a realized
   arithmetic surface;
2. the published Yuan--Zhang admissibility hypotheses;
3. the global target-side metric theorem.

So the correct reading is:

\[
 \text{finite A2/A4 metric-discipline shadow exact-audited},
 \qquad
 \text{actual geometric admissibility still open}.
 \]
