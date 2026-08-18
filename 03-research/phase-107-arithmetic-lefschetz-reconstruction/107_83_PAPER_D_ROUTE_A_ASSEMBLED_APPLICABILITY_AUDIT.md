# 107.83 -- Paper D Route A assembled applicability audit

## 1. Purpose

`107_50` now records exact finite shadows for every Route A item A1--A6,
but those shadows still lived mostly in separate artifacts.  One
question remained open at the governance level:
can the current candidate target package satisfy the visible A1--A6
discipline simultaneously in one assembled model, or are the separate
shadows only pairwise compatible?

This note exact-audits that assembled applicability shadow.

## 2. Exact shadow audited here

The verifier `107_83_paper_d_route_a_assembled_applicability_audit.py`
exact-audits one finite symbolic target model in which:

1. one candidate envelope supplies the common target-side carrier for
   the visible incidence/boundary package;
2. one intrinsic realized class lands in degree zero and preserves the
   visible critical scaling;
3. one normal-crossings metric profile with one remainder channel
   satisfies the visible A2/A4 discipline;
4. one transported target pairing stays finite on every visible
   non-diagonal channel, with unresolved behavior confined to the true
   diagonal placeholder;
5. one visible functoriality package remains compatible with the same
   target state;
6. deleting any one of A1--A6 makes the assembled Route A state fail
   immediately.

So the audit pressure-tests not merely the pieces of Route A, but one
joint finite target-side applicability shadow.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact Route A assembled applicability checks passed.
```

So the workspace now contains a reproducible exact audit that the
visible Route A shadows can coexist in one assembled candidate target
state, while still failing cleanly when any one required ingredient is
removed.

## 4. What this proves and what it does not

This audit proves a narrow but useful point:

1. the current A1--A6 shadows are no longer only a checklist but one
   assembled finite target-side discipline;
2. the candidate envelope, degree-zero realization, metric discipline,
   target-pairing finiteness, and functoriality can be read in one
   coherent visible package;
3. the current phase can still be certified as not yet genuinely
   Route-A-applicable because the assembled shadow remains only finite
   and symbolic.

It does **not** prove:

1. a genuine regular proper arithmetic surface or published adelic
   comparison theorem;
2. actual target-side integrability, semipositivity, or pairing
   finiteness;
3. the theorem-level Route A applicability claim of `107_12`.

So the correct reading is:

\[
 \text{finite assembled Route A applicability shadow exact-audited},
 \qquad
 \text{actual geometric Route A applicability still open}.
 \]
