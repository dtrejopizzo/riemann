# 107.13 -- Paper D, Part II: the terminal identity and the RH closure logic

## 1. Purpose

This note executes Work Package IV-B of `107_00`.  Its job is to state
the exact final identity that Phase 107 must prove before any positivity
argument is invoked:

\[
 \boxed{
 -\overline M_f^{\,2}\cdot\overline H_T=\mathcal Q_W(f).
 }
 \tag{1.1}
\]

The logical rule is strict:

\[
 \text{new work} = \text{prove (1.1), not prove positivity by construction.}
 \tag{1.2}
\]

If the sign \(\mathcal Q_W(f)\ge0\) is used in defining
\(\overline M_f\), then the argument is circular and Phase 107 fails.

## 2. Inputs required before the terminal step

The terminal identity sits at the end of the whole chain already
assembled in the earlier papers.

1. `107_06` gives the finite-support source intersection package.
2. `107_09` gives the source arithmetic Lefschetz formula.
3. `107_10` gives the target proper-model framework \(\mathcal Y_T\).
4. `107_11` gives the target divisor-to-line-bundle realization
   \(D_f\mapsto\overline M_f\) and the exact-kernel requirement
   \(\ker=\mathfrak R_W\).
5. `107_12` gives the applicability checklist for invoking an existing
   arithmetic Hodge theorem.

Only after these pieces are proved may IV-B begin.

## 3. What the terminal identity must compare

The two sides of (1.1) come from different constructions and must be
shown equal without presupposing either one from the other.

### Source side

The source side is the explicit Weil quadratic form
\(\mathcal Q_W(f)\), represented in Phase 107 by the finite-support
prime--Gamma--polar divisor package and its self-intersection on the
primitive degree-zero sector.

### Target side

The target side is the polarized arithmetic self-intersection of the
realized metrized line bundle \(\overline M_f\) on the
relative-dimension-two model \(\mathcal Y_T\), or in the precise adelic
replacement category, with a fixed nef and big polarization
\(\overline H_T\).

The theorem of IV-B is exactly the statement that these two independently
defined quantities coincide.

## 4. Sign convention

The sign convention must be fixed before the proof starts.

### Convention 4.1

Phase 107 adopts the arithmetic-geometry normalization

\[
 \overline M_f^{\,2}\cdot\overline H_T\le0
 \tag{4.1}
\]

on the degree-zero sector of the target category whenever the relevant
Hodge theorem applies.

Therefore the Phase 107 matching identity must read

\[
 \mathcal Q_W(f)=-\overline M_f^{\,2}\cdot\overline H_T,
 \tag{4.2}
\]

not with the opposite sign.

The whole content is then transported to the source side.

## 5. Terminal identity target

### Theorem 5.1: terminal identity

For every compactly supported test \(f\), choose \(T\) large enough that
\(D_f\) is realized on \(\mathcal Y_T\), and require the primitive
condition \(M_f\cdot H_T=0\).  Assume:

1. the finite-support realization theorem of `107_10`;
2. the faithful Picard/Jacobian realization of `107_11`;
3. the applicability audit of `107_12`.

Then the realized metrized line bundle \(\overline M_f\) satisfies

\[
 \boxed{
 -\overline M_f^{\,2}\cdot\overline H_T
 =\mathcal Q_W(f).
 }
 \tag{5.1}
\]

This is the exact endpoint of IV-B.

The direct theorem used after this identity is Yuan--Zhang in generic
dimension two.  Faltings--Hriljac supplies an alternative only after a
separate pairing-preserving reduction to a curve or Jacobian; no such
reduction is currently proved in Phase 107.

The present note does not prove Theorem 5.1; it fixes its content and
its logical consequences.

## 6. How Theorem 5.1 must be proved

The proof of (5.1) has four required comparison layers.

### 6.1. Generator comparison

One must compare the target self-intersections of the realized generator
classes

\[
 F_{\mathrm v},\quad F_{\mathrm h},\quad \Delta,\quad Z_\infty,\quad
 \Gamma_{p,k}
 \tag{6.1}
\]

with their source intersection numbers.

### 6.2. Bilinear extension

Using additivity of the realization map, extend the generator
comparisons to arbitrary finite-support source divisors.

### 6.3. Diagonal/Lefschetz compatibility

Show that the target diagonal intersection reproduces the same
prime--Gamma--polar Lefschetz numbers already computed on the source side
in `107_09`.

### 6.4. Primitive degree-zero reduction

Verify that the comparison descends to the primitive degree-zero sector,
with kernel exactly \(\mathfrak R_W\), so that equality cases on the
target side match equality cases on the source side.

Without item 6.4, the identity could still hold only modulo a larger
null space, which is forbidden by the Phase 107 stop rules.

## 7. Equality-case audit

The terminal identity is not fully proved until its equality case is
transported correctly.

### Proposition 7.1: equality requires exact radical agreement

If (5.1) holds but the null space of the target self-intersection is
larger than \(\mathfrak R_W\), then Phase 107 still fails.

Proof.  The goal of Phase 107 is not merely to prove a nonnegative
quadratic form; it is to identify the Weil form itself inside arithmetic
intersection theory.  A larger null space would change the equality case
and therefore define a different quadratic object.  This contradicts the
explicit audit condition (18a) of `107_00`.  \(\square\)

### Corollary 7.1: radical jets

The known radical jets

\[
 r_j=\frac{K^{(2j)}}K-4^{-j}
 \tag{7.1}
\]

must map to zero after realification in the target category, and no
non-radical test may do so.

This is the equality-case version of Theorem 5.1.

## 8. Logical closure to RH

Once Theorem 5.1 and the audit of `107_12` are both proved, the closure
to RH is formal.

### Theorem 8.1: conditional RH closure

Assume:

1. Theorem 5.1 holds for every admissible \(f\);
2. the chosen target category satisfies the hypotheses of a proven
   arithmetic Hodge-index theorem;
3. the equality case agrees exactly with \(\mathfrak R_W\).

Then

\[
 \mathcal Q_W(f)\ge0
 \tag{8.1}
\]

for every admissible \(f\), with equality exactly on the Weil radical.
By Weil's criterion, RH follows.

Proof.  By the arithmetic Hodge theorem on the target category,
\(\overline M_f^{\,2}\cdot\overline H_T\le0\) on the
\(H_T\)-primitive sector.
The terminal identity (5.1) therefore gives \(\mathcal Q_W(f)\ge0\).
The equality-case audit transfers the null space exactly to
\(\mathfrak R_W\).  Weil's criterion then yields RH.  \(\square\)

Theorem 8.1 is the final logical closure of the program, not an
independent source of new geometry.

## 9. Circularity tests

The terminal step fails if any of the following occurs.

1. \(\overline M_f\) is defined using the positivity of
   \(\mathcal Q_W\).
2. The metric on \(\overline M_f\) is reverse-engineered from the
   desired equality (5.1) rather than from the source Gamma--polar
   geometry.
3. The source pairing is compared only after quotienting by an
   uncontrolled larger kernel.
4. The positivity theorem is applied before proving the exact identity
   (5.1).

These are the final anti-circularity gates of Phase 107.

## 10. Status

Part IV is now fully specified at the theorem level.

1. `107_12` states the applicability audit for existing arithmetic Hodge
   theorems.
2. The present note states the exact terminal identity and the logical
   closure from that identity to RH.

What remains open is still the hard part:
prove III-A, III-B, IV-A, and IV-B in full, not just at the blueprint
level.  Until then, Phase 107 has a complete formal roadmap but not yet
the final arithmetic surface theorem.
