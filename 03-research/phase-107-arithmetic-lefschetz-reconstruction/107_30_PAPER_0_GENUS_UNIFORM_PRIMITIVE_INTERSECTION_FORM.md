# 107.30 -- Paper 0 supplement: genus-uniform primitive intersection form on \(C\times C\)

## 1. Purpose

`107_29` isolates the real remaining gap in Paper 0:

\[
 \text{elliptic positive control}
 \neq
 \text{genus-uniform source derivation of the primitive diagonal package.}
 \tag{1.1}
\]

The present note fills that gap at the exact point where the genus
factor lives, but in a specific sense that must be read carefully.  It
proves, for an arbitrary smooth projective curve \(C/\mathbf F_q\) of
genus \(g\), the classical surface-intersection formulas on \(C\times
C\)

\[
 (\Delta^0)^2=-2g,
 \qquad
 (\Gamma_n^0)^2=-2g\,q^n,
 \qquad
 \Gamma_n^0\cdot\Delta^0=-a_n.
 \tag{1.2}
\]

This is not yet a full rewrite of `107_02`; the fixed elliptic paper is
kept as the positive control.  More importantly, this note uses
adjunction and the classical intersection theory of \(C\times C\).  It
therefore proves that the classical curve-surface route produces the
genus factor.  It does not, by itself, prove that the Phase 107
arithmetic source route over \(\operatorname{Spec}\mathbf Z\) derives
that same factor without importing classical surface input.

## 2. Setup

Let \(C/\mathbf F_q\) be a smooth projective geometrically connected
curve of genus \(g\), and fix a rational base point \(x_0\in C\).

Set

\[
 S:=C\times C,
 \qquad
 F_{\rm v}:=\{x_0\}\times C,
 \qquad
 F_{\rm h}:=C\times\{x_0\},
 \qquad
 \Delta:=\{(P,P):P\in C\}.
 \tag{2.1}
\]

For geometric Frobenius \(F\), let

\[
 \Gamma_n:=\Gamma_{F^n}=\{(P,F^n(P)):P\in C\}\subset S.
 \tag{2.2}
\]

As usual,

\[
 a_n:=q^n+1-\#C(\mathbf F_{q^n}).
 \tag{2.3}
\]

## 3. Ruling intersections and bidegrees

The graph geometry is the same as in the elliptic paper.

### Proposition 3.1: ruling intersections

For every \(n\ge0\),

\[
 \Gamma_n\cdot F_{\rm v}=1,
 \qquad
 \Gamma_n\cdot F_{\rm h}=q^n.
 \tag{3.1}
\]

Also,

\[
 F_{\rm v}^2=F_{\rm h}^2=0,
 \qquad
 F_{\rm v}\cdot F_{\rm h}=1,
 \qquad
 \Delta\cdot F_{\rm v}=\Delta\cdot F_{\rm h}=1.
 \tag{3.2}
\]

Proof.  The ruling identities are the same fiber-degree calculations as
in `107_02`: the first projection of \(\Gamma_n\) is an isomorphism,
while the second has degree \(q^n\).  The ruling self-intersections
vanish because each ruling is a fiber of a projection.  The mixed ruling
intersection and diagonal/ruling intersections are tautological.
\(\square\)

## 4. The genus enters through adjunction

Unlike the elliptic case, one cannot set \(\Delta^2=\Gamma_n^2=0\) when
\(g\neq1\).  The correct formulas come from adjunction on the surface
\(S=C\times C\).

### Proposition 4.1: canonical class of the square

\[
 K_S=p_1^*K_C+p_2^*K_C.
 \tag{4.1}
\]

Proof.  This is the standard canonical divisor formula for a product of
smooth curves.  \(\square\)

### Proposition 4.2: diagonal self-intersection

\[
 \Delta^2=2-2g.
 \tag{4.2}
\]

Proof.  Since \(\Delta\simeq C\), adjunction on the smooth surface \(S\)
gives

\[
 2g-2=\Delta^2+K_S\cdot\Delta.
 \tag{4.3}
\]

Now

\[
 K_S\cdot\Delta
 =(p_1^*K_C+p_2^*K_C)\cdot\Delta
 =(2g-2)+(2g-2)=4g-4.
 \tag{4.4}
\]

Substituting into (4.3) yields

\[
 \Delta^2=(2g-2)-(4g-4)=2-2g.
 \tag{4.5}
\]

\(\square\)

### Proposition 4.3: Frobenius-graph self-intersection

For every \(n\ge0\),

\[
 \Gamma_n^2=q^n(2-2g).
 \tag{4.6}
\]

Proof.  The graph \(\Gamma_n\) is isomorphic to \(C\), so adjunction
again gives

\[
 2g-2=\Gamma_n^2+K_S\cdot\Gamma_n.
 \tag{4.7}
\]

The first projection of \(\Gamma_n\) has degree \(1\) and the second has
degree \(q^n\), hence

\[
 K_S\cdot\Gamma_n
 =(p_1^*K_C+p_2^*K_C)\cdot\Gamma_n
 =(2g-2)+q^n(2g-2)
 =(1+q^n)(2g-2).
 \tag{4.8}
\]

Therefore

\[
 \Gamma_n^2
 =(2g-2)-(1+q^n)(2g-2)
 =-q^n(2g-2)
 =q^n(2-2g).
 \tag{4.9}
\]

\(\square\)

These two formulas are exactly the missing genus-sensitive classical
input.

## 5. Primitive projection

Define the primitive classes by subtracting the ruling components:

\[
 \Delta^0:=\Delta-F_{\rm v}-F_{\rm h},
 \qquad
 \Gamma_n^0:=\Gamma_n-q^nF_{\rm v}-F_{\rm h}.
 \tag{5.1}
\]

### Theorem 5.1: genus-uniform primitive self-intersections

For every \(n\ge1\),

\[
 (\Delta^0)^2=-2g,
 \qquad
 (\Gamma_n^0)^2=-2g\,q^n.
 \tag{5.2}
\]

Proof.  Expand:

\[
 (\Delta^0)^2
 =\Delta^2-2(\Delta\cdot F_{\rm v})-2(\Delta\cdot F_{\rm h})
 +2(F_{\rm v}\cdot F_{\rm h}),
 \tag{5.3}
\]

so by Propositions 3.1 and 4.2,

\[
 (\Delta^0)^2=(2-2g)-2-2+2=-2g.
 \tag{5.4}
\]

Similarly,

\[
 (\Gamma_n^0)^2
 =\Gamma_n^2
 -2q^n(\Gamma_n\cdot F_{\rm v})
 -2(\Gamma_n\cdot F_{\rm h})
 +2q^n(F_{\rm v}\cdot F_{\rm h}),
 \tag{5.5}
\]

which becomes, using Propositions 3.1 and 4.3,

\[
 (\Gamma_n^0)^2
 =q^n(2-2g)-2q^n-2q^n+2q^n
 =-2g\,q^n.
 \tag{5.6}
\]

\(\square\)

This is the exact formula whose absence was exposed by `107_28`.

## 6. Primitive cross term

### Proposition 6.1: genus-uniform primitive cross term

For every \(n\ge1\),

\[
 \Gamma_n^0\cdot\Delta^0=-a_n.
 \tag{6.1}
\]

Proof.  Expand as in the elliptic case:

\[
 \Gamma_n^0\cdot\Delta^0
 =\Gamma_n\cdot\Delta
 -\Gamma_n\cdot F_{\rm v}
 -\Gamma_n\cdot F_{\rm h}
 -q^n(F_{\rm v}\cdot\Delta)
 +q^n(F_{\rm v}\cdot F_{\rm h})
 -F_{\rm h}\cdot\Delta
 +F_{\rm h}\cdot F_{\rm v}.
 \tag{6.2}
\]

Now
\(\Gamma_n\cdot\Delta=\#C(\mathbf F_{q^n})\),
\(\Gamma_n\cdot F_{\rm v}=1\),
\(\Gamma_n\cdot F_{\rm h}=q^n\),
and
\(F_{\rm v}\cdot\Delta=F_{\rm h}\cdot\Delta=F_{\rm v}\cdot F_{\rm h}=1\),
so

\[
 \Gamma_n^0\cdot\Delta^0
 =\#C(\mathbf F_{q^n})-q^n-1
 =-a_n.
 \tag{6.3}
\]

\(\square\)

So the whole \(2\times2\) primitive Gram package is now genus-uniform.

## 7. Consequence for the Gram determinant

### Corollary 7.1: genus-uniform Gram matrix

For every \(n\ge1\),

\[
 G_n^0=
 \begin{pmatrix}
 -2g & -a_n\\
 -a_n & -2g\,q^n
 \end{pmatrix}.
 \tag{7.1}
\]

Hence

\[
 \det G_n^0=4g^2q^n-a_n^2.
 \tag{7.2}
\]

If the Hodge-index theorem is then applied on \(C\times C\), one gets

\[
 |a_n|\le 2g\,q^{n/2}.
 \tag{7.3}
\]

This is exactly the genus-sensitive version of the Paper 0 terminal
bound.

## 8. What this closes and what it does not

What is now closed:

1. the two primitive diagonal entries are no longer tied only to the
   elliptic case;
2. the genus factor \(g\) is derived directly from classical geometry by
   adjunction on \(C\times C\);
3. the genus-2 falsifier of `107_28` now has a matching classical
   \(C\times C\) derivation rather than standing only as an external
   check.

What is not yet closed:

1. `107_02` itself is still written around the fixed elliptic control;
2. this note does not rewrite the full Frobenius--Lefschetz--Euler chain
   for arbitrary genus in the same level of detail;
3. it does not validate any arithmetic surface over
   \(\operatorname{Spec}\mathbf Z\).

## 9. Status consequence

After this note, the Paper 0 situation is sharper:

1. the fixed elliptic control of `107_02` remains proved;
2. genus-sensitive portability of the primitive Gram package is now
   proved at the classical source-intersection level on \(C\times C\);
3. what remains open is a full genus-uniform rewrite of the whole Paper
   0 chain and, separately, the question of deriving the genus factor by
   the genuinely arithmetic Phase 107 route rather than classical
   adjunction alone.
