# 107.68 -- Equality-case exactness audit

## 1. Purpose

`107_48` exact-audits the finite kernel shadow of `107_11`, and
`107_56` exact-audits the primitive-quotient shadow of `107_13`.  The
remaining governance gap is sharper:
Phase 107 must reject realizations that are internally consistent but
still kill one extra non-radical direction, or that verify only an
inclusion

\[
 \mathfrak R_W \subseteq \ker(f\mapsto \overline M_f)
 \]

instead of the exact equality.

This note adds an exact finite audit artifact for that sharpness.

## 2. Exact shadow audited here

The verifier `107_68_equality_case_exactness_audit.py` exact-audits the
following finite shadow.

1. The admissible equality-case target is exact kernel equality, not
   mere radical containment.
2. Quotienting by the explicit radical preserves the correct quadratic
   identity on the primitive sector.
3. Any realization model that kills an additional non-radical direction
   is rejected exactly, even if the remaining quadratic package stays
   self-consistent on the smaller quotient.
4. The visible equality case is therefore audited as a minimality
   statement, not only as a compatibility statement.

## 3. Outcome

Running the verifier on Saturday, August 1, 2026 produced:

```text
All exact equality-case exactness checks passed.
```

So the workspace now contains a reproducible exact audit that the Phase
107 equality case cannot be weakened to a larger kernel without being
detected.

## 4. What this proves and what it does not

This audit proves a narrow but useful point:

1. the equality-case gate is now pressure-tested as exactness, not only
   as radical compatibility;
2. extra-kernel realizations are finitely falsifiable in one visible
   model;
3. the distinction
   \(\ker=\mathfrak R_W\) versus
   \(\ker\supsetneq\mathfrak R_W\) is now audited explicitly.

It does **not** prove:

1. the actual geometric realization of `107_11`;
2. the full target-side arithmetic self-intersection theorem of
   `107_13`;
3. the final RH closure.

So the correct reading is:

\[
 \text{finite equality-case exactness shadow exact-audited},
 \qquad
 \text{geometric kernel equality still open}.
 \]
