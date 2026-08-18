# 107.56 -- Paper D terminal-identity primitive-quotient audit

## 1. Purpose

`107_49` exact-audits the bilinear transport shadow behind `107_11`, but
`107_13` still culminates in a sharper statement:
after primitive degree-zero projection and exact radical quotienting,
the source Weil form and the target self-pairing must coincide as one
quadratic object, with the correct equality case.

The present note exact-audits that finite shadow.
It does not prove the full arithmetic-surface theorem.  It proves
something narrower and exact:
in one finite visible model, the terminal identity survives primitive
projection, descends to the quotient by the explicit radical, and has
the right nullspace there.

## 2. Shadow being tested

The verifier uses:

1. a finite source pairing matrix;
2. a finite target height matrix equal to its negative;
3. the polarization vector used for primitive projection;
4. one explicit radical direction already isolated in `107_48`--`107_49`.

The exact finite question is:

\[
 -\widehat{\deg}(\overline M_f^{\,2})=\mathcal Q_W(f)
 \tag{2.1}
\]

does this remain true after:

1. primitive projection to degree zero;
2. passage to the quotient by the explicit radical;
3. inspection of the equality case on a visible finite coefficient box?

## 3. What the verifier checks

The script
`107_56_paper_d_terminal_identity_primitive_quotient_audit.py`
exact-audits four statements.

1. For sample finite-support vectors, primitive projection produces
   degree-zero classes on which the source and target quadratic values
   match exactly with the required minus sign.
2. Adding any multiple of the explicit radical leaves both quadratic
   values unchanged, and the quotient representative is therefore
   well defined.
3. On the finite primitive coefficient box \([-2,2]^6\), vanishing of
   the quadratic form occurs exactly on primitive vectors lying in the
   radical span.
4. The generator images already satisfy the same primitive quotient
   comparison, so the quotient-level identity is compatible with the
   generator basis.

Everything is exact: the verifier works over rational arithmetic, not
floating approximations.

## 4. Result

The verifier passes exactly.

This means `107_13` now has a genuine finite terminal shadow beyond the
earlier bilinear comparison:
the identity is pressure-tested as a quadratic statement on the
primitive quotient itself, and not only before quotienting or only at
the bilinear level.

## 5. Scope boundary

This audit still does **not** prove:

1. the actual geometric self-intersection on a realized arithmetic
   surface or adelic target;
2. the true generator comparison for realized classes;
3. the analytic Gamma--polar metric comparison;
4. the full theorem of `107_13`.

Its force is finite and exact:
the visible primitive-quotient logic of the terminal identity now has an
independent audit, including the equality case.
