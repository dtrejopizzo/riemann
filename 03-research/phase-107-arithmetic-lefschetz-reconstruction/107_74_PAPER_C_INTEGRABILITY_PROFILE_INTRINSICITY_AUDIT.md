# 107.74 -- Paper C integrability-profile intrinsicity audit

## 1. Purpose

`107_45` exact-audits the logarithmic chart template of `107_23`, and
`107_55` exact-audits the order-only remainder channel later reused by
Route A.  But inside Paper C itself one finite question still remained
too implicit:
do the visible chart/root presentations determine one intrinsic
normal-crossings integrability profile, or could a hidden singular
channel be sneaking in through presentation changes?

This note exact-audits that intrinsicity shadow for `107_23`.

## 2. Exact shadow audited here

The verifier `107_74_paper_c_integrability_profile_intrinsicity_audit.py`
exact-audits the following finite shadow of `107_23`.

1. For each visible order pair, every rooted presentation on the same
   chart determines the same local logarithmic data.
2. The chartwise presentations glue to one intrinsic normal-crossings
   profile on the visible divisor slots
   \((B_{\rm v}, B_{\rm h}, \Delta)\) together with one remainder
   class.
3. Restricting the corner profile to the lower, upper, diagonal, and
   interior sectors recovers exactly the visible local presentations.
4. Introducing an extra singular direction beyond the three visible
   divisor slots is rejected as a genuinely different object.

So the candidate metric is pressure-tested one step beyond the bare
chart ansatz: the visible presentations must encode one intrinsic
integrability profile and not merely a family of compatible-looking
local formulas.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact Paper C integrability-profile intrinsicity checks passed.
```

So the workspace now contains a reproducible exact audit that the
visible chart/root data of `107_23` determine one finite
normal-crossings profile with no hidden fourth singular channel.

## 4. What this proves and what it does not

This audit proves a narrow but useful point:

1. the visible singular data of `107_23` are intrinsic at the finite
   chart/root level;
2. the corner chart really controls the lower, upper, diagonal, and
   interior restrictions as one profile;
3. extra singular directions are detected exactly rather than absorbed
   silently.

It does **not** prove:

1. the actual analytic values of the Gamma--polar coefficients;
2. global continuity/integrability on a proved arithmetic surface;
3. theorem-level Yuan--Zhang applicability.

So the correct reading is:

\[
 \text{finite intrinsic integrability-profile shadow exact-audited},
 \qquad
 \text{actual analytic integrability still open}.
 \]
