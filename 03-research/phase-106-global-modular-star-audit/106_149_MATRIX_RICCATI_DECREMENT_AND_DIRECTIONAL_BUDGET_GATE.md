# 106.149 — Matrix Riccati decrement and directional-budget gate

## 1. Purpose and result

Document 106.148 proves that the scalar multi-atom Riccati one-form is exact:
changing the order, grouping, or continuous schedule of the literal
prime-power increments cannot create a scalar holonomy beyond the endpoint

\[
 -\delta_J+G_J.
 \tag{1}
\]

There is nevertheless a stronger question which the scalar pivot does not
display.  Before the last one-dimensional Schur complement is taken, can the
literal atoms deliver enough energy in **every polar direction**?  This note
computes that matrix flow exactly.

On a finite completely anti-shorted heat/hybrid row let \(A_0\succ0\) be the
complete retained positive source matrix, let \(B\succeq0\) be the polar
information matrix, and insert literal prime powers \(n_j=p_j^{k_j}\) through

\[
 a_j={\Lambda(n_j)\over\sqrt{n_j}},
 \qquad
 H_j=a_jD_j^*D_j,
 \qquad
 A_j=A_{j-1}+H_j.
 \tag{2}
\]

Define the relative polar matrix

\[
 R_j=B^{1/2}A_j^{-1}B^{1/2}.
 \tag{3}
\]

The exact Woodbury decrement is

\[
 \boxed{R_{j-1}-R_j=W_j^*W_j,}
 \tag{4}
\]

where

\[
 \boxed{
 W_j=\sqrt{a_j}\,
 \bigl(I+a_jD_jA_{j-1}^{-1}D_j^*\bigr)^{-1/2}
 D_jA_{j-1}^{-1}B^{1/2}.}
 \tag{5}
\]

Consequently

\[
 \boxed{R_N=R_0-\sum_{j=1}^NW_j^*W_j.}
 \tag{6}
\]

The physical contraction on that row is equivalent to the **directional
budget**

\[
 \boxed{
 A_N-B\succeq0
 \quad\Longleftrightarrow\quad
 \sum_{j=1}^NW_j^*W_j\succeq R_0-I.}
 \tag{7}
\]

Formula (7) retains every direction and all common readaptation.  By
contrast, trace, determinant, and divisor-mass identities retain only global
or scalar information.  A minimal exact rational two-dimensional example,
realized with the literal weights
\(\Lambda(2)/\sqrt2\) and \(\Lambda(3)/\sqrt3\), satisfies the natural trace
and determinant tests while violating (7) in one direction.

Thus scalar/global budgets cannot prove the needed contraction.  The note
does **not** exclude a full directional inequality using the actual theta
translation geometry of all \(D_{p^k}\).  That source-specific inequality
remains open.

## 2. Nonduplication audit

| Document | Existing result | Additional issue settled here |
|---|---|---|
| 106.78 | Exact one-atom scalar Kalman innovation | Does not retain a matrix of polar directions |
| 106.89 and 106.91 | Exact radical-conditioned scalar endpoint and cofinal determinant crossing | Do not give the pre-pivot directional flow |
| 106.95 | Positive minor charging does not create the missing bordered-minor inequality | Does not compute the matrix Woodbury budget |
| 106.104 and 106.114 | Exact divisor current/ANOVA identity and its unitary character | Do not imply a Loewner lower bound in a selected direction |
| 106.144 | Complete chord-fibre decompositions are isometric | Does not classify the adaptive matrix decrement |
| 106.148 | The multi-parameter scalar Riccati connection is flat | Does not test trace/determinant replacements for matrix contraction |

The new content is (4)--(7), the exact trace and determinant consequences,
and the smallest rational falsifier showing why those scalar consequences do
not recover the Loewner inequality.

## 3. Finite completely anti-shorted row

Let \(E\) be a finite-dimensional real or complex Hilbert space obtained
after the complete finite radical anti-short on one heat/hybrid row.  All
Gamma, retained ordinary-prime, and positive seed contributions are included
in

\[
 A_0:E\to E,
 \qquad A_0\succ0.
 \tag{8}
\]

Let

\[
 B:E\to E,
 \qquad B\succeq0,
 \tag{9}
\]

be the complete polar information block on that same row.  No commutation of
\(A_0\) and \(B\) is assumed.

For each additional literal prime power \(n_j=p_j^{k_j}\), retain its exact
ordinary von Mangoldt weight

\[
 a_j={\Lambda(n_j)\over\sqrt{n_j}}
 ={\log p_j\over p_j^{k_j/2}}>0.
 \tag{10}
\]

The complete theta displacement observation at the chord
\(u_j=\log n_j\) is denoted by

\[
 D_j:E\longrightarrow F_j,
 \tag{11}
\]

where \(F_j\) may retain the same-side, central-crossing, residue, and divisor
components before their final orthogonal recombination.  Its positive source
increment is exactly

\[
 H_j=a_jD_j^*D_j\succeq0.
 \tag{12}
\]

Set

\[
 A_j=A_0+\sum_{i=1}^jH_i.
 \tag{13}
\]

Because \(A_0\succ0\), every \(A_j\) is invertible.  The relative matrix
\(R_j\) in (3) measures the polar block through the current fully adapted
positive metric.

## 4. Exact Woodbury decrement

### Theorem 1 — Positive matrix innovation

For every \(j\ge1\), define \(W_j\) by (5).  Then (4) holds.  In particular,

\[
 R_0\succeq R_1\succeq\cdots\succeq R_N\succeq0.
 \tag{14}
\]

#### Proof

Apply the operator Woodbury identity with

\[
 U_j=\sqrt{a_j}\,D_j:
 \tag{15}
\]

\[
 (A_{j-1}+U_j^*U_j)^{-1}
 =A_{j-1}^{-1}
 -A_{j-1}^{-1}U_j^*
 (I+U_jA_{j-1}^{-1}U_j^*)^{-1}
 U_jA_{j-1}^{-1}.
 \tag{16}
\]

Surrounding (16) by \(B^{1/2}\) gives

\[
\begin{aligned}
 R_{j-1}-R_j
 &=B^{1/2}A_{j-1}^{-1}U_j^*
 (I+U_jA_{j-1}^{-1}U_j^*)^{-1}
 U_jA_{j-1}^{-1}B^{1/2}\\
 &=W_j^*W_j.
\end{aligned}
 \tag{17}
\]

This proves (4) and the Loewner monotonicity (14).  Summing (4) proves
(6). \(\square\)

The factor \(W_j\) is not the raw chord \(D_j\).  It is the chord after the
single common metric \(A_{j-1}^{-1}\) has readapted to every preceding
prime-power atom.  Hence (4) preserves the cross-prime adaptation that is
lost by independent termwise estimates.

## 5. Exact physical directional budget

### Theorem 2 — Contraction is a matrix budget

For every finite \(N\), the following are equivalent:

\[
 A_N-B\succeq0,
 \tag{18}
\]

\[
 R_N\preceq I,
 \tag{19}
\]

and

\[
 \sum_{j=1}^NW_j^*W_j\succeq R_0-I.
 \tag{20}
\]

#### Proof

Consider the Hermitian block matrix

\[
 \mathbb M_N=
 \begin{pmatrix}
 A_N&B^{1/2}\\
 B^{1/2}&I
 \end{pmatrix}.
 \tag{21}
\]

Taking its Schur complement first with respect to \(I\) gives

\[
 \mathbb M_N\succeq0
 \quad\Longleftrightarrow\quad
 A_N-B\succeq0.
 \tag{22}
\]

Taking its Schur complement instead with respect to \(A_N\succ0\) gives

\[
 \mathbb M_N\succeq0
 \quad\Longleftrightarrow\quad
 I-B^{1/2}A_N^{-1}B^{1/2}\succeq0,
 \tag{23}
\]

which is (19).  Finally, substitute (6) into (19).  The result is exactly
(20). \(\square\)

If a cofinal family satisfies \(A_N\uparrow A_\infty\) in a topology for
which the compressed inverses converge, the same identity gives

\[
 A_\infty-B\succeq0
 \quad\Longleftrightarrow\quad
 \sum_{j\ge1}W_j^*W_j\succeq R_0-I.
 \tag{24}
\]

Equation (24) is only an exact coordinate for the surviving theorem.  Its
right-hand side must still be proved from the literal Riemann theta feature
geometry; Woodbury algebra does not supply that lower bound.

## 6. Trace and determinant identities

### Corollary 3 — Total Hilbert--Schmidt decrement

For every finite \(N\),

\[
 \boxed{
 \sum_{j=1}^N\|W_j\|_{\mathrm{HS}}^2
 =\mathrm{Tr}(R_0-R_N).}
 \tag{25}
\]

#### Proof

Take the trace in (6), using
\(\mathrm{Tr}(W_j^*W_j)=\|W_j\|_{\mathrm{HS}}^2\). \(\square\)

Thus the trace necessary condition for (20) is

\[
 \sum_{j=1}^N\|W_j\|_{\mathrm{HS}}^2
 \ge \mathrm{Tr}(R_0-I).
 \tag{26}
\]

It is not sufficient, because it does not specify where the decrement is
deposited.

### Corollary 4 — Multiplicative decrement

Assume \(B\succ0\).  Then

\[
 \boxed{
 \log\det R_{j-1}-\log\det R_j
 =\log\det
 \bigl(I+a_jD_jA_{j-1}^{-1}D_j^*\bigr),}
 \tag{27}
\]

and hence

\[
 \boxed{
 \log\det R_0-\log\det R_N
 =\sum_{j=1}^N
 \log\det
 \bigl(I+a_jD_jA_{j-1}^{-1}D_j^*\bigr).}
 \tag{28}
\]

#### Proof

Since \(B\succ0\),

\[
 \det R_j={\det B\over\det A_j}.
 \tag{29}
\]

The matrix determinant lemma gives

\[
 {\det A_j\over\det A_{j-1}}
 =\det\bigl(I+a_jD_jA_{j-1}^{-1}D_j^*\bigr).
 \tag{30}
\]

If the observation target \(F_j\) has not itself been finitely compressed,
the determinant on the right of (30) is its finite-rank Fredholm determinant;
equivalently one may use the ordinary determinant of
\(I+a_jA_{j-1}^{-1/2}D_j^*D_jA_{j-1}^{-1/2}\) on \(E\).

Combining (29) and (30) proves (27), and summation proves (28). \(\square\)

The determinant records total volume contraction.  It does not exclude one
expanding direction compensated by stronger contraction in another.

## 7. Directional top-mode flow

The matrix inequality can also be read as an observability budget along the
moving worst polar direction.  Let

\[
 A(t)=A+tD^*D,
 \qquad
 \lambda(t)=\lambda_{\max}(B,A(t))
 =\sup_{v\ne0}{\langle v,Bv\rangle\over\langle v,A(t)v\rangle}.
 \tag{31}
\]

At every point where the top generalized eigenvalue is simple, choose
\(v(t)\) with

\[
 Bv=\lambda Av,
 \qquad
 \langle v,Av\rangle=1.
 \tag{32}
\]

The generalized Feynman--Hellmann identity gives

\[
 \boxed{
 {d\over dt}\log\lambda(t)=-\|Dv(t)\|^2.}
 \tag{33}
\]

At a multiple top eigenvalue, the right derivative is

\[
 {d^+\over dt}\log\lambda(t)
 =-\min_{\substack{v\in E_{\max}(t)\\
                    \langle v,A(t)v\rangle=1}}
 \|Dv\|^2.
 \tag{34}
\]

Therefore a source-specific proof of (20) must observe the moving top
generalized eigenspace strongly enough.  A trace or determinant lower bound
can be large while that particular direction remains almost invisible.

## 8. Minimal exact rational falsifier

The directional loss already occurs in dimension two with two injective
atoms and literal ordinary-prime weights.

Let

\[
 E=\mathbb R^2,
 \qquad
 A_0=I,
 \qquad
 B=\begin{pmatrix}6/5&0\\0&1\end{pmatrix}.
 \tag{35}
\]

Use the literal prime powers \(n_1=2\) and \(n_2=3\), so

\[
 a_2={\log2\over\sqrt2},
 \qquad
 a_3={\log3\over\sqrt3}.
 \tag{36}
\]

Put

\[
 H=\begin{pmatrix}1/20&0\\0&2\end{pmatrix}
 \tag{37}
\]

and define the injective observation maps

\[
 D_n=
 \begin{pmatrix}
 (20a_n)^{-1/2}&0\\
 0&(2/a_n)^{1/2}
 \end{pmatrix},
 \qquad n\in\{2,3\}.
 \tag{38}
\]

Then, with the actual weights in (36),

\[
 a_nD_n^*D_n=H
 \qquad(n=2,3).
 \tag{39}
\]

Thus

\[
 A_1=I+H=
 \begin{pmatrix}21/20&0\\0&3\end{pmatrix},
 \qquad
 A_2=I+2H=
 \begin{pmatrix}11/10&0\\0&5\end{pmatrix}.
 \tag{40}
\]

The relative matrices are

\[
 R_0=
 \begin{pmatrix}6/5&0\\0&1\end{pmatrix},
 \qquad
 R_1=
 \begin{pmatrix}8/7&0\\0&1/3\end{pmatrix},
 \qquad
 R_2=
 \begin{pmatrix}12/11&0\\0&1/5\end{pmatrix}.
 \tag{41}
\]

Hence the exact innovations are

\[
 W_1^*W_1=R_0-R_1
 =\begin{pmatrix}2/35&0\\0&2/3\end{pmatrix},
 \tag{42}
\]

\[
 W_2^*W_2=R_1-R_2
 =\begin{pmatrix}4/77&0\\0&2/15\end{pmatrix},
 \tag{43}
\]

and

\[
 \sum_{j=1}^2W_j^*W_j
 =\begin{pmatrix}6/55&0\\0&4/5\end{pmatrix}.
 \tag{44}
\]

The required directional budget is

\[
 R_0-I=
 \begin{pmatrix}1/5&0\\0&0\end{pmatrix}.
 \tag{45}
\]

It fails in the first coordinate, since

\[
 {6\over55}<{1\over5}
 \qquad\text{and}\qquad
 \sum_{j=1}^2W_j^*W_j-(R_0-I)
 =\begin{pmatrix}-1/11&0\\0&4/5\end{pmatrix}.
 \tag{46}
\]

Equivalently,

\[
 \lambda_{\max}(R_2)={12\over11}>1.
 \tag{47}
\]

Nevertheless the trace budget passes by a wide margin:

\[
 \mathrm{Tr}(R_0-R_2)
 ={10\over11}
 >{1\over5}
 =\mathrm{Tr}(R_0-I).
 \tag{48}
\]

The natural endpoint scalar tests also pass:

\[
 \mathrm{Tr}\,R_2={71\over55}<2,
 \qquad
 \det R_2={12\over55}<1.
 \tag{49}
\]

Thus the total decrement and the volume decrement are both ample, but most
of the energy is deposited in the second coordinate while the first remains
subcritical.  Dimension two is minimal: in dimension one, trace, determinant,
and Loewner order all reduce to the same scalar comparison.

The example uses the literal arithmetic weights attached to \(2\) and \(3\),
and the scalar divisor identity at the endpoint \(6\),

\[
 \Lambda(2)+\Lambda(3)=\log6,
 \tag{50}
\]

is of course exact.  What is abstract is the choice (38) of observation
directions.  Therefore (35)--(49) is **not** a counterexample to the actual
Riemann theta chord geometry.  It proves only that literal weights and the
scalar divisor identity do not, by themselves, force the required
directional allocation.

## 9. Consequence for the theta/divisor programme

The divisor ANOVA and finite theta-residue transforms of 106.104, 106.114,
and 106.144 are isometries.  At the matrix level they may replace a feature
factorization \(D\) by another factorization of the same positive increment

\[
 H=D^*D.
 \tag{51}
\]

But the total matrix decrement is fixed by the endpoints:

\[
 \sum_jW_j^*W_j
 =B^{1/2}(A_0^{-1}-A_N^{-1})B^{1/2}.
 \tag{52}
\]

Consequently an isometric divisor or theta reorganization cannot turn an
insufficient directional decrement into a sufficient one.  Nor can a
different order of the same atoms do so: (52) is independent of ordering,
in agreement with the Riccati flatness theorem of 106.148.

This leaves one precise source-specific possibility.  The **actual** theta
translation maps \(D_{p^k}\), with Gamma and the pole retained in the common
metric and with the complete radical anti-short already performed, may obey
a directional inequality unavailable to abstract positive atoms:

\[
 \boxed{
 \sum_{p^k}W_{p^k}^*W_{p^k}
 \succeq R_0-I.}
 \tag{53}
\]

Equivalently, the moving worst generalized eigenspace must receive the
observability budget dictated by (33)--(34).  Proving (53) requires a new
arithmetic statement about the joint orientation of the literal theta
chords.  It cannot be replaced by:

1. total Hilbert--Schmidt energy;
2. determinant or volume contraction;
3. the scalar divisor mass identity;
4. a unitary ANOVA/DFT change of feature coordinates; or
5. a different Riccati schedule for the same increments.

## 10. Status

The exact matrix decrement, its trace and determinant laws, and the
two-dimensional falsifier are proved unconditionally on every finite seeded
row.

The surviving full-theta statement (53) is open.  This note narrows the
remaining mechanism from a scalar/global source budget to a genuinely
directional arithmetic observability theorem.  It does not prove the
physical surplus, \(G_J>\delta_J\), A1, or RH.
