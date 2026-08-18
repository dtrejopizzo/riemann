# 107.78 -- Paper C realization degree-zero covariance audit

## 1. Purpose

`107_48` exact-audits the kernel shadow of `107_11`, and `107_49`
exact-audits the pairing-transport shadow, but one visible target-side
requirement of the realization map still lacked its own audit artifact:
the realized classes should actually sit in degree zero after primitive
correction, and the visible critical scaling should preserve that
degree-zero status rather than leaking back into the ample direction.

This note exact-audits that shadow.

## 2. Exact shadow audited here

The verifier
`107_78_paper_c_realization_degree_zero_covariance_audit.py`
exact-audits one finite symbolic model of `107_11` in which:

1. primitive projection produces realized classes of exact target-side
   degree zero;
2. the realization map is additive on a visible finite basis;
3. discrete visible critical scaling preserves realized degree zero;
4. the realized degree-zero classes remain compatible with the
   transported self-pairing and with one explicit radical direction.

So the candidate realization is pressure-tested not only as a kernel or
pairing object, but also as a degree-zero object carrying the expected
visible covariance.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact Paper C realization degree-zero covariance checks passed.
```

So the workspace now contains a reproducible exact audit that the
visible realization shadow lands in degree zero after primitive
correction and keeps that status under the finite critical scaling
shadow.

## 4. What this proves and what it does not

This audit proves a narrow but useful point:

1. the visible realization shadow can be projected exactly into degree
   zero;
2. critical visible scaling need not reintroduce degree leakage in that
   finite model;
3. the degree-zero condition is now pressure-tested together with
   pairing transport and radical compatibility.

It does **not** prove:

1. actual target-side degree zero on a realized arithmetic surface or
   adelic target;
2. full continuous scaling covariance of the true realization map;
3. the geometric Picard/Jacobian realization theorem of `107_11`.

So the correct reading is:

\[
 \text{finite degree-zero/covariance realization shadow exact-audited},
 \qquad
 \text{actual realized target still open}.
 \]
