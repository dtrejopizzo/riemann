# 107.241 -- Hodge index for the corner pairing on the numerical quotient

## 0. What this closes, and what it does not

107_240 §5 established that the corner pairing descends unconditionally to
the numerical quotient

\[
 V:=\{\text{DC divisors}\}/\mathrm{rad}\,I_\partial ,
 \qquad
 \overline I_\partial \text{ nondegenerate on } V .
 \tag{0.1}
\]

This note computes the **signature** of \(\overline I_\partial\) on \(V\),
unconditionally, and identifies the resulting statement with the classical
Hodge index theorem.

It does **not** prove RH.  It proves that, for the pairing actually
constructed in 107_237--107_239, the Hodge-index statement is exactly
equivalent to RH, and that the classical form of that statement --
*the intersection form has exactly one positive direction* -- is the correct
one.  Row (d) is thereby reduced to a proved equivalence rather than a
missing ingredient.

**Attribution.**  That an inertia count of a Weil-type form tracks off-line
zeros is due to Connes--van Suijlekom.  What is new here is the geometric
packaging: the form is an intersection pairing on a numerical quotient of a
divisor group on a square, its interior density vanishes identically
(107_238), and its polar block is *exactly the intersection matrix of the two
rulings*, matching the independent computation of 107_233.

## 1. Test class and evaluation coordinates

Let \(\mathcal A=C_c^\infty(\mathbb R_+^\times)\), embedded in the idele
class group through the module as in 107_239 §3.  For \(f\in\mathcal A\) write

\[
 \widehat f(s)=\int_0^\infty f(u)\,u^{s}\,d^\times u ,
\]

an entire function of \(s\).  Let \(\widetilde f\) be the involution of
107_239 (4.1), so that

\[
 \widehat{\widetilde f}(s)=\overline{\widehat f(1-\bar s)} .
 \tag{1.1}
\]

Let \(Z\) be the multiset of nontrivial zeros of \(\xi\), \(m_\rho\) the
multiplicity of \(\rho\), and set

\[
 \rho' := 1-\bar\rho .
 \tag{1.2}
\]

### Lemma 1.1 (the mirror involution)

\(\rho\mapsto\rho'\) is an involution of \(Z\) preserving multiplicities, and

\[
 \rho'=\rho \iff \mathrm{Re}\,\rho=\tfrac12 .
\]

**Proof.**  \(\xi(s)=\xi(1-s)\) and \(\xi\) has real coefficients, so
\(\xi(\bar s)=\overline{\xi(s)}\); composing, \(\rho\in Z\Rightarrow
1-\bar\rho\in Z\) with the same multiplicity.  It is an involution since
\(1-\overline{(1-\bar\rho)}=\rho\).  Finally \(\rho=1-\bar\rho\) iff
\(\rho+\bar\rho=1\) iff \(\mathrm{Re}\,\rho=\frac12\). \(\square\)

> The zeros on the critical line are exactly the **fixed points** of the
> mirror involution; the off-line zeros are exactly its **2-cycles**.

This is the structural fact that drives everything below.

## 2. The pairing in evaluation coordinates

By the explicit formula, \(N(h)=\widehat h(0)+\widehat h(1)
-\sum_{\rho}m_\rho\widehat h(\rho)\).  With \(h=f\star\widetilde g\) and
(1.1), \(\widehat h(s)=\widehat f(s)\overline{\widehat g(1-\bar s)}\), hence

\[
 \boxed{
 I_\partial(D_f,D_g)=
 \widehat f(0)\overline{\widehat g(1)}
 +\widehat f(1)\overline{\widehat g(0)}
 -\sum_{\rho\in Z}m_\rho\,
 \widehat f(\rho)\overline{\widehat g(\rho')} . }
 \tag{2.1}
\]

### Lemma 2.1 (Hermitian)

\(I_\partial(D_f,D_g)=\overline{I_\partial(D_g,D_f)}\).

**Proof.**  The polar terms swap into each other.  For the zero sum,
\(\overline{I_\partial(D_g,D_f)}\) contributes
\(\sum_\rho m_\rho\widehat f(\rho')\overline{\widehat g(\rho)}\); reindexing
by the involution \(\rho\mapsto\rho'\), which preserves \(m\) by Lemma 1.1,
returns \(\sum_\rho m_\rho\widehat f(\rho)\overline{\widehat g(\rho')}\).
\(\square\)

### Lemma 2.2 (evaluation coordinates)

By 107_240 Theorem D,
\(\mathrm{rad}\,I_\partial=\{f:\widehat f(0)=\widehat f(1)=0,\
\widehat f(\rho)=0\ \forall\rho\}\).  Hence

\[
 V\hookrightarrow \mathbb C^{\{0,1\}}\oplus\mathbb C^{Z},
 \qquad
 f\longmapsto\bigl(\widehat f(0),\widehat f(1),(\widehat f(\rho))_\rho\bigr)
 \tag{2.2}
\]

is injective, and (2.1) is the pullback of an explicit form on the target.
The image meets every finite block in full: for pairwise distinct
\(s_1,\dots,s_k\) the functionals \(f\mapsto\widehat f(s_j)\) are linearly
independent on \(\mathcal A\), since the characters \(u\mapsto u^{s_j}\) are.

## 3. The Hodge index theorem

Write \(L\) for the set of distinct zeros with \(\mathrm{Re}\,\rho=1/2\)
and \(P\) for the set of mirror 2-cycles \(\{\rho,\rho'\}\),
\(\mathrm{Re}\,\rho\ne1/2\).  Every finite-block truncation of \(V\) is
understood below; the signature statement is blockwise and hence exact on
each finite-dimensional subquotient.

> ### Theorem 3.1
>
> \(\overline I_\partial\) decomposes \(\overline I_\partial\)-orthogonally as
> \[
>  V \;=\; H_{\mathrm{ruling}}
>  \;\oplus\;\bigoplus_{\rho\in L}\ell_\rho
>  \;\oplus\;\bigoplus_{\{\rho,\rho'\}\in P}H_\rho ,
> \]
> where
>
> 1. \(H_{\mathrm{ruling}}\) is spanned by the two polar coordinates and
>    carries the matrix \(\begin{pmatrix}0&1\\1&0\end{pmatrix}\), of
>    signature \((1,1)\);
> 2. \(\ell_\rho\) is the line of an on-line zero, with form
>    \(-m_\rho|v_\rho|^2\), of signature \((0,1)\);
> 3. \(H_\rho\) is the plane of an off-line mirror pair, with matrix
>    \(-m_\rho\begin{pmatrix}0&1\\1&0\end{pmatrix}\), of signature
>    \((1,1)\).
>
> Consequently
> \[
>  \boxed{\;n_+(\overline I_\partial)=1+\#P,
>  \qquad
>  n_-(\overline I_\partial)=1+\#L+\#P.\;}
> \]

**Proof.**  Orthogonality of the three families is immediate from (2.1):
the polar coordinates pair only with each other, and \(v_\rho\) pairs only
with \(v_{\rho'}\).

(1) The polar block of (2.1) is
\(v_0\overline{w_1}+v_1\overline{w_0}\), i.e. the stated matrix, whose
eigenvalues are \(\pm1\).

(2) If \(\rho\in L\) then \(\rho'=\rho\) by Lemma 1.1, so the corresponding
term of (2.1) is \(-m_\rho v_\rho\overline{w_\rho}\), negative definite of
rank one.

(3) If \(\{\rho,\rho'\}\in P\) then \(\rho\ne\rho'\), and the two terms
combine to \(-m_\rho(v_\rho\overline{w_{\rho'}}+v_{\rho'}\overline{w_\rho})\),
with matrix \(-m_\rho\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\)
and eigenvalues \(\mp m_\rho\): one positive, one negative.

Summing the inertias gives the boxed formula.  Multiplicities scale the
blocks by positive numbers and therefore do not affect inertia. \(\square\)

### Corollary 3.2 (counting form)

\[
 n_+(\overline I_\partial)-1
 \;=\;\#P
 \;=\;\tfrac12\,\#\{\text{distinct off-line zeros of }\xi\}.
\]

### Corollary 3.3 (Hodge index \(\Longleftrightarrow\) RH)

\[
 \boxed{\;
 \mathrm{RH}
 \iff
 n_+(\overline I_\partial)=1
 \iff
 \mathrm{sign}(\overline I_\partial)=(1,\ \cdot\ ). \;}
\]

This is verbatim the classical Hodge index theorem for a surface, whose
content is that the intersection form on \(NS\otimes\mathbb R\) has exactly
one positive eigenvalue.

### Corollary 3.4 (primitive form, Faltings--Hriljac shape)

On the primitive subspace \(\widehat f(0)=\widehat f(1)=0\) -- the
degree-zero reduction of 107_24 -- the form is

\[
 Q(f)=-\sum_{\rho}m_\rho\,\widehat f(\rho)\overline{\widehat f(\rho')} ,
\]

and \(Q\le0\) holds for all \(f\) if and only if RH holds.  Under RH,
\(Q(f)=-\sum_\rho m_\rho|\widehat f(\rho)|^2\), the exact analogue of
\(\overline M^2=-2h_{\mathrm{NT}}(M)\le0\).

## 4. Why the polar block is the two rulings

On a product of two curves the two rulings satisfy
\(F_v^2=F_h^2=0\), \(F_v\cdot F_h=1\), i.e. the intersection matrix
\(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\).  Theorem 3.1(1)
produces exactly this matrix from the two poles of \(\zeta\) at \(s=0\) and
\(s=1\).

This is a consistency check across two independently constructed parts of
the phase.  107_233 computes, from the tropical tensor construction and
without any reference to the explicit formula,

\[
 \mathrm{cdim}^{(2)}H^0(D\boxtimes E)=\deg^+(D)\deg^+(E),
\]

which is the bidegree coefficient \(F_v\cdot F_h\).  Theorem 3.1(1) recovers
the same matrix from the polar terms of \(N\).  The two computations agree.

## 5. Status of row (d)

Proved unconditionally here:

* Lemma 1.1: on-line zeros = fixed points of the mirror involution;
* Lemma 2.1: \(I_\partial\) is Hermitian;
* Theorem 3.1: the complete blockwise signature of \(\overline I_\partial\);
* Corollary 3.2: \(n_+-1\) counts off-line mirror pairs;
* Corollary 3.3: the Hodge index statement is equivalent to RH;
* Corollary 3.4: the primitive form has the Faltings--Hriljac sign shape.

Consequently:

\[
 \boxed{\texttt{ROW\_D\_STATUS: HODGE\_INDEX\_STATEMENT\_ESTABLISHED}}
\]

Row (d) is no longer a missing ingredient.  It is a proved equivalence: for
the constructed pairing, *Hodge index* and *RH* are the same statement, in
the same classical form Weil's proof uses.

**Not proved, and not promoted.**  This does not prove RH; it does not
supply global rational functions on the DC quotient topos (107_240 Thm C);
it does not establish \(H^0\), \(H^1\) or Riemann--Roch, which need linear
rather than numerical equivalence (107_240 §5); and it does not change
`ROW_A_STATUS`, which remains `partial`.  Paper status is unchanged.

The whole remaining burden now sits in row (a): making the divisor group and
its pairing geometric.  Rows (b), (c) and (d) no longer contribute
independent unknowns to the scissors.

## 6. Verifier

`107_241_hodge_index_for_the_corner_pairing.py` builds the form (2.1) in
evaluation coordinates on six synthetic zero configurations (no zeta zero is
used as an input), and checks: hermiticity; nondegeneracy; the inertia
identity \((n_+,n_-)=(1+\#P,\ 1+\#L+\#P)\); that the polar block is exactly
\(\left(\begin{smallmatrix}0&1\\1&0\end{smallmatrix}\right)\); invariance of
the inertia under multiplicities; the equivalence \(n_+=1\iff\) no off-line
zeros; negative definiteness of the primitive part exactly in that case; and
linear independence of the evaluation functionals on real bump functions.
