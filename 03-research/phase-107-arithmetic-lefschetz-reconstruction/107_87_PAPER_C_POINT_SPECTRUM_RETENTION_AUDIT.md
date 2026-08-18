# 107.87 -- Paper C point-spectrum retention audit

## 1. Purpose

`107_63` exact-audits the exclusion of absolutely continuous
completions, and `107_48`, `107_73`, and `107_86` exact-audit kernel,
intrinsicity, and finite-support realization shadows.  But F7 still
lacked one direct assembled artifact:
there was no single exact witness that the current candidate
realization shadow actually retains discrete point/resonance classes as
distinguishable target-side data rather than only excluding one wrong
completion model in isolation.

This note exact-audits that retention shadow.

## 2. Exact shadow audited here

The verifier `107_87_paper_c_point_spectrum_retention_audit.py`
exact-audits one finite symbolic realization state in which:

1. visible point/resonance generators survive as discrete target-side
   classes on one intrinsic single-receiver package;
2. non-radical point/resonance witnesses remain distinguishable after
   quotienting by the explicit radical shadow;
3. collapsing the realization to an absolutely continuous completion
   erases those discrete witnesses exactly;
4. collapsing the Green separation channels or splitting the receiver
   away from the intrinsic package also destroys retention;
5. the current candidate target and finite-support realization shadows
   therefore preserve point-spectrum visibility at the finite audit
   level.

So the audit pressure-tests one exact retention shadow rather than only
an exclusion of bad ambient models.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact Paper C point-spectrum retention checks passed.
```

So the workspace now contains a reproducible exact audit that the
current candidate realization shadow retains discrete point/resonance
data as visible target-side classes, while standard collapsing
completions fail cleanly.

## 4. What this proves and what it does not

This audit proves a narrow but useful point:

1. F7 is no longer supported only by a negative exclusion test; the
   current candidate realization shadow now has a positive exact
   retention witness;
2. non-radical point/resonance classes are exact-audited as surviving in
   the current intrinsic single-receiver package;
3. the remaining gap is the actual realized target theorem, not whether
   the present finite shadows can even retain point-spectrum data.

It does **not** prove:

1. existence of a genuine arithmetic surface or adelic target carrying
   those classes;
2. the full faithful Picard/Jacobian realization theorem of `107_11`;
3. theorem-level Route A applicability or RH.

So the correct reading is:

\[
 \text{finite point-spectrum retention shadow exact-audited},
 \qquad
 \text{actual realized retention theorem still open}.
 \]
