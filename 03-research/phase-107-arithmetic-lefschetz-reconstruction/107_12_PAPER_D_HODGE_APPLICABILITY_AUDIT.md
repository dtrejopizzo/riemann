# 107.12 -- Paper D, Part I: applicability audit for arithmetic Hodge theory

## 1. Purpose

This note executes Work Package IV-A of `107_00`.  Its role is to state,
line by line, what must be verified before any existing arithmetic
Hodge-index theorem may be invoked in Phase 107.

The basic methodological rule is:

\[
 \text{``a Hodge theorem exists''}
 \neq
 \text{``it applies to the Phase 107 objects.''}
 \tag{1.1}
\]

Phase 15 already isolated this distinction sharply: Faltings--Hriljac
and Yuan--Zhang are real theorems, but they control height-type
arithmetic Picard data, not automatically the zero-carrying objects
desired for RH.  The present note turns that warning into a formal audit.

## 2. Inputs from earlier papers

The audit starts from the current Phase 107 outputs.

1. `107_06` constructs the source arithmetic intersection pairing on
   finite-support divisors.
2. `107_09` constructs the arithmetic Lefschetz identity on the source
   side.
3. `107_10` states the finite proper-model target \(\mathcal X_T\).
4. `107_11` states the desired Picard/Jacobian realization
   \(D_f\mapsto\overline M_f\) and the exact kernel condition
   \(\ker=\mathfrak R_W\).

The question of IV-A is simple to state:
once III-A and III-B are built, do the resulting objects lie inside a
category where a proven arithmetic Hodge theorem actually applies?

## 3. The two admissible routes

The program allows exactly two routes.

### Route A: existing theorem on a classical/adelic target

For every compactly supported test, the realized class \(\overline M_f\)
 lies either in

\[
 \widehat{\mathrm{Pic}}_{\rm int}(\mathcal Y_T),
 \qquad M_f\cdot H_T=0
 \tag{3.1}
\]

for a regular proper arithmetic surface, or in the precise integrable
adelic category

\[
 \widehat{\mathrm{Pic}}_{\rm int}(\mathcal Y_T),
 \qquad M_f\cdot H_T=0
 \tag{3.2}
\]

to which Yuan--Zhang applies.

For the direct square route, the generic fibre is a surface and the
relevant instance is Yuan--Zhang in dimension two.  Thus the model has
relative dimension two over \(\mathrm{Spec}\,\mathbb Z\), and the
Hodge expression contains one fixed nef and big polarization
\(\overline H_T\).  The relative-dimension-one
Faltings--Hriljac route is admissible only after an independently proved
pairing-preserving pushforward to a curve or Jacobian.

### Route B: new theorem in a new category

If the Phase 107 target remains an absolute/dynamical category not
covered by the classical theorems, then one must prove a new
Hodge--Rosati index theorem there.

No hybrid argument is allowed.  In particular, one may not construct a
new category and then import Faltings--Hriljac only by analogy.

## 4. Checklist for Route A

Assume the realization target is classical or adelic in the precise
sense of Route A.  Then the following items must be checked for every
admissible \(f\).

### A1. Regularity and properness

There must exist a model \(\mathcal Y_T\to\mathrm{Spec}\,\mathbb Z\)
of relative dimension two that is regular and proper, or an exact
adelic substitute with a proved comparison to such models.

This is the direct output expected from `107_10`.

### A2. Integrability of the metric

The metric on \(\overline M_f\) must belong to the domain allowed by the
chosen theorem:

1. smooth/admissible Arakelov metric in the surface case, or
2. integrable adelic metric in the Yuan--Zhang case.

The source Gamma--polar Green metric of `107_05` must therefore be shown
to descend into that class, not merely to define a formal determinant.

### A3. Arithmetic degree zero

The realized class must satisfy the exact degree-zero hypothesis
required by the theorem:

\[
 M_f\cdot H_T=0
 \tag{4.1}
\]

relative to the fixed ample polarization.

This is stronger than saying that the source divisor was "primitive" or
"balanced" before realization.

### A4. Admissibility / semipositivity

When the chosen theorem requires admissibility or semipositivity of the
metric or auxiliary polarization, those hypotheses must be checked
directly on the realized objects.

The source construction may not use the desired sign to prove these
properties, or the argument becomes circular.

### A5. Finiteness of intersections

The polarized self-intersection in the direct square route

\[
 \overline M_f^{\,2}\cdot\overline H_T
 \tag{4.2}
\]

and the mixed pairings
\(\overline M_f\cdot\overline M_g\cdot\overline H_T\) must be finite in the
target category.

Paper A proves finiteness on the source determinant package.  IV-A must
still verify that the target intersection theory computes the same
numbers without introducing new divergences.

### A6. Pullback and pushforward compatibility

The realization and comparison maps must preserve the functorial
operations used in the theorem:

1. pullback along the structural projections and correspondence maps;
2. pushforward where the theorem requires it;
3. compatibility of these operations with the source determinant pairing.

This item is essential because the Phase 107 objects are not isolated
divisors; they come from a correspondence calculus.

## 5. Checklist for Route B

If Route A fails and one keeps a genuinely new absolute category, then
the following must be proved inside that category.

### B1. A precise degree-one object

The new category must contain a well-defined degree-one or primitive
sector carrying the Phase 107 divisor classes.

### B2. A Rosati/Hodge form

There must be a bilinear or Hermitian intersection form intrinsically
defined in the new category, not imported from the target sign.

### B3. A Hodge-index theorem

One must prove directly that the form is negative semidefinite on the
degree-zero sector and identify its equality case.

### B4. Equality-case compatibility

The radical of that form must agree exactly with the explicit Weil
radical \(\mathfrak R_W\).  Any larger radical fails the audit.

Because no such theorem has yet been proved in the current absolute
category, Route B remains only a placeholder.

## 6. The height-versus-zeros warning

Phase 15 gave two sharp warnings that remain decisive here.

### Proposition 6.1: existing theorems control the right category only after realization

Faltings--Hriljac and Yuan--Zhang do not by themselves prove RH for
Phase 107.

Proof.  As emphasized in Phase 15 Attempts 5 and 6, those theorems
control Arakelov/adelic Picard data and therefore height-type
cohomology.  RH would follow only after III-A and III-B identify the
Phase 107 zero-carrying source package with precisely that target
category and transport the source pairing to the arithmetic
self-intersection pairing.  \(\square\)

### Proposition 6.2: wrong-cohomology realizations fail the audit

A realization that lands only on a height theory unrelated to the
source Lefschetz/divisor package does not pass IV-A.

Proof.  The elliptic control of Phase 15 shows that a genuine arithmetic
surface can exist while the proven Hodge theorem still governs heights
and special values rather than the required zero-carrying data.  Hence
the mere existence of an arithmetic surface is insufficient; the
realization must land on the correct realized divisor package of
Phase 107.  \(\square\)

## 7. Applicability theorem target

### Theorem 7.1: applicability audit target

Assume that for every compactly supported test \(f\):

1. `107_10` is proved, giving a regular proper model \(\mathcal Y_T\) or
   an exact adelic substitute;
2. `107_11` is proved, giving a faithful realization
   \(D_f\mapsto\overline M_f\);
3. items A1--A6 above hold.

Then the existing arithmetic Hodge-index theorem applies to the
realized classes \(\overline M_f\).

This is the precise endpoint of IV-A.  It is an audit theorem, not yet a
proof in the present note.

## 8. Failure conditions

The applicability audit fails immediately if any of the following
occurs.

1. The model is nonproper or obtained by deleting places outside the
   cutoff.
2. The metric is formal but not admissible/integrable in the target
   theorem.
3. Degree zero holds only on the source side, not on the realized target.
4. The realization loses point-spectrum/divisor visibility in an
   absolutely continuous completion.
5. The theorem is invoked on a category for which no published or
   independently proved Hodge theorem exists.
6. Equality cases in the target are not matched against
   \(\mathfrak R_W\).

Any such failure stops the program before the terminal identity.

## 9. Status

Part IV now has its first formal deliverable:
the issue is no longer "is there an arithmetic Hodge theorem?" but
"have the Phase 107 objects been realized in the exact domain of that
theorem, with all hypotheses and equality cases verified?"  That is the
only admissible interpretation of IV-A.

The remaining work of Part IV is IV-B: prove the terminal identity

\[
 -\overline M_f^{\,2}\cdot\overline H_T=\mathcal Q_W(f)
\]

with the sign convention fixed before positivity is applied.
