# 107.92 -- Assembled equality-case gate audit

## 1. Purpose

`107_48` exact-audits the kernel shadow of `107_11`, `107_56`
exact-audits the primitive-quotient terminal shadow of `107_13`, and
`107_68` exact-audits the sharp exactness requirement
\(\ker=\mathfrak R_W\).  But F10 still lacked one assembled artifact:
there was no single exact witness that these three conditions really act
as one equality-case gate rather than as separate local checks.

This note exact-audits that assembled equality-case shadow.

## 2. Exact shadow audited here

The verifier `107_92_assembled_equality_case_gate_audit.py`
exact-audits one finite symbolic equality-case state in which:

1. radical directions vanish only through the explicit radical shadow;
2. non-radical directions survive in the realified target shadow;
3. the primitive-quotient quadratic identity holds with the correct
   nullspace on that same state;
4. any enlargement of the kernel beyond the explicit radical breaks the
   equality-case gate immediately, even if the remaining package stays
   internally self-consistent;
5. the current equality-case layer is therefore pressure-tested as one
   exact minimality-and-identity gate.

So the audit tests the whole equality-case discipline as one assembled
rule rather than as independent compatibility checks.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact assembled equality-case gate checks passed.
```

So the workspace now contains a reproducible exact audit that the
current equality-case layer behaves as one assembled gate with sharp
minimality.

## 4. What this proves and what it does not

This audit proves a narrow but useful point:

1. F10 is no longer supported only by separate kernel and quotient
   shadows; those conditions are now exact-audited as one assembled
   gate;
2. extra-kernel realizations are rejected not only algebraically but at
   the level of the full current equality-case discipline;
3. the remaining gap is the actual geometric realization theorem, not
   uncertainty about the exact logical shape of the equality case.

It does **not** prove:

1. the actual geometric realization of `107_11`;
2. the full target-side arithmetic self-intersection theorem of
   `107_13`;
3. RH closure.

So the correct reading is:

\[
 \text{assembled equality-case gate exact-audited},
 \qquad
 \text{geometric kernel equality still open}.
 \]
