# 107.149 -- Dimensional correction for the Hodge target

## 1. Verdict

The direct realization of Weil's square is not an arithmetic surface in
the relative-dimension-one sense.  Its generic fibre is a projective
surface \(Y_T/\mathbb Q\), so a regular proper model

\[
 \mathcal Y_T\longrightarrow\operatorname{Spec}\mathbb Z
\]

has relative dimension two and total Krull dimension three.  Therefore
the direct Hodge expression required by Phase 107 is

\[
 -\overline M_f^{\,2}\cdot\overline H_T,
\]

where \(\overline H_T\) is a fixed nef and big polarization.  The
unpolarized expression
\(-\widehat{\deg}(\overline M_f^{\,2})\) belongs to the curve route and
cannot be used directly on the square.

## 2. The dimension check

Yuan--Zhang's arithmetic Hodge index theorem for a projective variety
of dimension \(n\) over a number field has the form

\[
 \overline M^{\,2}\cdot\overline L_1\cdots\overline L_{n-1}\le 0
\]

under the primitive condition

\[
 M\cdot L_1\cdots L_{n-1}=0.
\]

For the square target, \(n=2\).  Consequently there is exactly one
polarization factor:

\[
 M_f\cdot H_T=0,
 \qquad
 \overline M_f^{\,2}\cdot\overline H_T\le0.
\]

This is also the dimension already implicit in `107_24`, where the
primitive projection is defined using \(\deg_H(D)=D\cdot H\).

## 3. Corrected direct target

The direct Route A target must contain all of the following data:

1. a normal geometrically connected projective surface
   \(Y_T/\mathbb Q\);
2. a regular proper model \(\mathcal Y_T/\operatorname{Spec}\mathbb Z\)
   of relative dimension two;
3. an integrable metrized line bundle \(\overline M_f\);
4. a fixed nef and big metrized polarization \(\overline H_T\);
5. the exact primitive condition \(M_f\cdot H_T=0\);
6. the comparison identity

\[
 -\overline M_f^{\,2}\cdot\overline H_T=\mathcal Q_W(f).
\]

The equality case in the arithmetic Hodge theorem additionally requires
the hypotheses that make numerical triviality detectable; it must not
be inferred from the inequality alone.

## 4. Status of the curve route

Faltings--Hriljac remains an admissible theorem only after constructing
an independent pairing-preserving pushforward from the square target to
a curve or its Jacobian.  Such a map is not currently present in Phase
107.  It is therefore a separate route, not a substitute for the
polarization factor in the direct route.

## 5. Consequence

All previous unpolarized terminal formulas in the direct square route
are superseded by the polarized formula above.  This correction proves
no existence theorem for \(\mathcal Y_T\), no realization theorem for
\(\overline M_f\), and no terminal identity.  It removes a dimensional
type error before those open problems are attacked.

The companion program is a regression certificate over the governing
Phase 107 specifications.  It can return `NO` if any core document
reintroduces the dimension-one formula into the direct route.
