# 107.197 -- The standard Fock exact sequence has zero Bott--Chern anomaly

## 1. Finite geometric approximants

For \(N\ge2\), truncate the exact sequence of 107_196 to

\[
 0\longrightarrow F_{2,N}
 \longrightarrow F_{1,N}
 \longrightarrow\mathbb C e_1
 \longrightarrow0,
 \tag{1.1}
\]

where

\[
 F_{1,N}=\operatorname{span}(e_1,\ldots,e_N),
 \qquad
 F_{2,N}=\operatorname{span}(e_2,\ldots,e_N).
\]

Equip every space with the standard number-basis Hermitian metric.  Then

\[
 F_{1,N}=\mathbb C e_1\mathbin{\widehat\oplus}F_{2,N}
 \tag{1.2}
\]

is an isometric orthogonal splitting, compatible with \(N\) and
\(q^N\).

## 2. Bott--Chern normalization

For an exact sequence of Hermitian vector bundles

\[
 0\to\overline E'\to\overline E\to\overline E''\to0,
\]

the Bott--Chern secondary Chern character is normalized to vanish when
the sequence is orthogonally split:

\[
 \widetilde{\operatorname{ch}}
 (\overline E',\overline E,\overline E'')=0.
 \tag{2.1}
\]

Applying (2.1) to (1.1) gives zero at every cutoff \(N\).

## 3. No-go theorem

**Theorem.**  The standard Hermitian realization of the relative Fock
determinant in 107_196 produces no Bott--Chern secondary current.  Any
extension of Bott--Chern theory to the filtered limit that is compatible
with finite orthogonally split truncations and continuous in \(N\)
also assigns zero to this sequence.

**Proof.**  Equation (1.2) proves that every finite sequence is
isometrically split, so (2.1) gives zero.  A compatible continuous limit
of the constant zero system is zero. \(\square\)

This conclusion coexists with the nontrivial determinant ratio

\[
 {D_1(q)\over D_2(q)}=1-q.
\]

The ratio belongs to the determinant functor of the quotient
\(\mathbb C e_1\); it is not a metric anomaly of the exact sequence.
Consequently it cannot be relabeled as the missing secondary current.

## 4. Required refinement

A nonzero secondary class now requires additional geometry, for example:

1. a non-orthogonally split metric derived from transverse dynamics;
2. a superconnection whose off-diagonal term couples \(e_1\) to the
   tail;
3. a boundary condition producing an eta/analytic-torsion anomaly;
4. a genuinely equivariant normal bundle with nontrivial curvature.

Choosing such a coupling arbitrarily would merely install the target.
It must be derived from Deninger's ambient system or the
Connes--Consani square and must still fail for Davenport--Heilbronn.

## 5. Exact scope

This closes only the **standard orthogonal Fock metric** route.  It does
not disprove all secondary realizations of the virtual class.  It proves
that the canonical determinant cancellation of 107_196, by itself,
contains no Bott--Chern curvature information.

## 6. Falsifier

The verifier checks the real prime/spectral atlas and cutoffs
\(N=2,4,8,16,32\).  It constructs the Gram matrices, verifies exactness,
orthogonal splitting, equivariance under \(q^N\), and determinant
multiplicativity.  A metric with a nonzero off-diagonal coupling must be
detected as non-orthogonal, preventing the gate from confusing a
potential anomaly with the standard sequence.
