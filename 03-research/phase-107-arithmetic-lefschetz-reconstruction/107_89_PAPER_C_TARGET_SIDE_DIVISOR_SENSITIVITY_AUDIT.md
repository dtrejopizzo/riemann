# 107.89 -- Paper C target-side divisor sensitivity audit

## 1. Purpose

`107_05` proves divisor sensitivity at the source metric level, and
`107_48`, `107_73`, `107_78`, and `107_87` exact-audit several finite
realization shadows behind `107_11`.  But F5 still lacked one direct
target-side artifact:
there was no single exact witness that moving a visible divisor changes
the current candidate realized object itself, rather than only changing
source-side bookkeeping before the realization map is applied.

This note exact-audits that target-side sensitivity shadow.

## 2. Exact shadow audited here

The verifier `107_89_paper_c_target_side_divisor_sensitivity_audit.py`
exact-audits one finite symbolic realization state in which:

1. visible moved-divisor presentations determine distinct realized
   target-side classes whenever the move is nontrivial modulo the
   explicit radical shadow;
2. the same intrinsic single-receiver package preserves that location
   sensitivity rather than collapsing moved divisors to one scalar
   correction;
3. primitive degree-zero correction does not destroy the distinction
   between genuinely different divisor locations;
4. only designated radical moves are allowed to vanish in the realified
   target shadow;
5. scalarized or location-blind target substitutes fail the audit
   exactly.

So the audit pressure-tests one exact target-side divisor-sensitivity
shadow rather than leaving F5 only at the source-metric level.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact Paper C target-side divisor sensitivity checks passed.
```

So the workspace now contains a reproducible exact audit that the
current candidate realization shadow keeps visible divisor location as
genuine target-side data, while location-blind substitutes fail
cleanly.

## 4. What this proves and what it does not

This audit proves a narrow but useful point:

1. F5 is no longer supported only by source-side metric rigidity; the
   current candidate realization shadow now has a positive exact
   target-side sensitivity witness;
2. primitive correction, intrinsic packaging, and radical quotienting do
   not force genuine moved-divisor classes to collapse together;
3. the remaining gap is the actual realized Picard/Jacobian theorem, not
   whether the present finite shadows can still see divisor movement at
   all.

It does **not** prove:

1. existence of a genuine arithmetic surface or adelic target carrying
   those divisor classes;
2. the full faithful realization theorem of `107_11`;
3. theorem-level Route A applicability or RH.

So the correct reading is:

\[
 \text{finite target-side divisor-sensitivity shadow exact-audited},
 \qquad
 \text{actual realized divisor-sensitivity theorem still open}.
 \]
