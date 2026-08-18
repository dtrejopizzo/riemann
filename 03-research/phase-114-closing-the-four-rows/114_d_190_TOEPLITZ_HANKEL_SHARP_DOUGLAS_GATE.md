# D.190 — Toeplitz--Hankel boundary block and the sharp Douglas gate

## Verdict

The old/shell coupling of the complete A--B--C multiplier can be written
exactly as a support commutator.  On the two-Tate primitive source it is

\[
 X_{OE}^{\rm prim}=P_O\Pi_TQ_T\Pi_TP_E,
 \qquad Q_T=-B_{{\rm nuc},T},                         \tag{0.1}
\]

where \(P_O,P_E\) are the old-cell and newly born shell projections and
\(\Pi_T\) is the orthogonal projection onto the common kernel of the two
Tate jets.  Before the finite-rank Tate compression,

\[
 P_OQ_TP_E=[P_O,Q_T]P_E.                              \tag{0.2}
\]

Formula (0.2) is a genuine Toeplitz--Hankel boundary operator.  It includes
the full Gamma kernel, the centred resolvent, and every prime power
\(p^k\).  The Tate compression changes it by rank at most four, whereas
the uncompressed boundary block has infinite rank already in the Gamma
channel.

There is an exact sharp Douglas theorem:

\[
 X_{OE}^{\rm prim}=A_O^{1/2}C_{OE},\qquad
 C_{OE}^*C_{OE}\le B_E                               \tag{0.3}
\]

with constant one if and only if the enlarged old-plus-shell block of
\(Q_T\) is positive.  Thus the desired carré-du-champ factorization is not
a formal consequence of the commutator: for an exhausting family of
cells, (0.3) is equivalent to global row-D positivity.  This identifies
precisely what a noncircular construction must add.  It must produce an
independent, source-defined contraction transporting the infinite-rank
Poisson boundary block into the old defect channel.  The two Tate jets
alone cannot do this.

No zero or RH input is used.  The paper is not modified.

## 1. Complete centred multiplier

Let \(I_T=[-T,T]\), extend functions by zero, and write

\[
 a_{p^k}=k\log p,\qquad w_{p^k}={\log p\over p^{k/2}}. \tag{1.1}
\]

D.134 gives on the two-Tate primitive form domain

\[
 Q_T=-B_{{\rm nuc},T}
 =H_{5/4,T}-\beta I-R_{1/2,T}
  -\sum_{p^k\le e^{2T}}w_{p^k}
       (S_{a_{p^k}}+S_{-a_{p^k}}),                    \tag{1.2}
\]

where

\[
 \begin{aligned}
 H_{5/4,T}(f,f)
 &=\frac12\iint_{\mathbb R^2}
   \gamma_{5/4}(|t-s|)|\widetilde f(t)-\widetilde f(s)|^2\,dt\,ds,\\
 \gamma_{5/4}(r)&={e^{-5r/2}\over1-e^{-2r}},\\
 (R_{1/2,T}f)(t)&=\int_{I_T}e^{-|t-s|/2}f(s)\,ds .
 \end{aligned}                                       \tag{1.3}
\]

The sum in (1.2) is literally over all prime powers, not merely primes.
It is finite on every bounded support interval and contains the complete
local finite-place term of the explicit formula.  The Gamma term in
(1.3) is the complete shifted archimedean multiplier.

Take an orthogonal support decomposition

\[
 L^2(I_T)=H_O\oplus H_E\oplus H_R,                   \tag{1.4}
\]

where \(H_O=L^2(O)\), \(H_E=L^2(E)\), and \(O,E\) are disjoint, with
\(E\) the newly attached shell.  Since \(P_OP_E=0\), every multiplier
or translation \(M\) satisfies

\[
 P_OMP_E=(P_OM-MP_O)P_E=[P_O,M]P_E.                  \tag{1.5}
\]

Therefore the raw old/shell block is the exact sum

\[
\boxed{
\begin{aligned}
 X_{OE}:=P_OQ_TP_E
 ={}&-P_OK_{\Gamma}P_E-P_OR_{1/2,T}P_E\\
 &-\sum_{p^k\le e^{2T}}w_{p^k}
       P_O(S_{a_{p^k}}+S_{-a_{p^k}})P_E ,
\end{aligned}}                                       \tag{1.6}
\]

where, in polarized form,

\[
 \langle f,P_OK_\Gamma P_Ee\rangle
 =\int_{O\times E}\gamma_{5/4}(|t-s|)
       \overline{f(t)}e(s)\,dt\,ds.                  \tag{1.7}
\]

The sign in (1.6) follows by polarizing the difference form (1.3): for
disjointly supported \(f,e\),

\[
 H_{5/4,T}(f,e)
 =-\int_{O\times E}\gamma_{5/4}(|t-s|)
       \overline{f(t)}e(s)\,dt\,ds.                  \tag{1.8}
\]

The scalar channel \(-\beta I\) has no old/shell cross block.  The second
line of (1.6) retains separately every translation by \(k\log p\), with
its exact weight \((\log p)p^{-k/2}\).  Equations (1.6)--(1.8) are the
requested Gamma-plus-all-\(p^k\) Toeplitz--Hankel formula.

The formulas are first read on smooth functions supported a positive
distance from the common boundary.  They extend to the common form domain
by closing (1.3).  This avoids assigning an ordinary bounded kernel to the
\(r^{-1}\) singularity of \(\gamma_{5/4}\) at zero.

## 2. The two Tate jets are a finite-rank correction

Let

\[
 M_Tf=\left(\int_{I_T}e^{t/2}f(t)\,dt,
             \int_{I_T}e^{-t/2}f(t)\,dt\right),       \tag{2.1}
\]

and let \(\Pi_T\) be the orthogonal projection onto \(\ker M_T\).  These
are exactly the two primitive moments identified with the two Tate jets in
D.137.  Put \(F_T=I-\Pi_T\).  Then \(\mathrm{rank}\,F_T\le2\), and

\[
 \Pi_TQ_T\Pi_T-Q_T=-F_TQ_T-Q_TF_T+F_TQ_TF_T.         \tag{2.2}
\]

On any finite-energy spectral regularization, (2.2) implies

\[
 \mathrm{rank}\,\bigl(
 P_O(\Pi_TQ_T\Pi_T-Q_T)P_E\bigr)\le4.                \tag{2.3}
\]

The same statement holds as a finite-rank form perturbation on the closed
form domain.  In contrast, the integral operator (1.7) has infinite rank
for any two nonempty intervals \(O,E\).  Indeed, if it had rank \(r\), the
functions

\[
 t\longmapsto\gamma_{5/4}(|t-s_j|),\qquad s_j\in E,  \tag{2.4}
\]

would span a space of dimension at most \(r\).  On separated intervals
the kernel is real analytic.  A finite linear relation in (2.4), continued
to a common analytic component, would give a finite linear relation among
distinct translates of \(\gamma_{5/4}\).  Taking the Laplace transform
gives a nonzero exponential polynomial times the nonzero transform of
\(\gamma_{5/4}\), hence all coefficients vanish.  Arbitrarily many
distinct \(s_j\) are therefore independent.

Consequently the two jets remove the two-dimensional polar quotient but
cannot transport or annihilate the full boundary Hankel block.

## 3. Sharp Douglas factorization of one shell

Let a self-adjoint closed form \(q\) on \(H_O\oplus H_E\) have block

\[
 \mathcal Q_{OE}=
 \begin{pmatrix}A_O&X_{OE}\\X_{OE}^*&B_E\end{pmatrix},             \tag{3.1}
\]

where \(A_O\ge0\).  The generalized Schur--Douglas theorem gives the
following equivalent assertions:

1. \(\mathcal Q_{OE}\ge0\);
2. \(\mathrm{Ran}\,X_{OE}\subseteq
   \mathrm{Ran}\,A_O^{1/2}\) and
   \(B_E-X_{OE}^*A_O^\dagger X_{OE}\ge0\);
3. there is an operator \(C_{OE}:H_E\to\overline{\mathrm{Ran}\,A_O})
   such that

   \[
    X_{OE}=A_O^{1/2}C_{OE},\qquad C_{OE}^*C_{OE}\le B_E .          \tag{3.2}
   \]

For bounded blocks this is the ordinary Douglas lemma followed by the
Schur complement.  For closed forms it follows by applying that statement
to \((A_O+\varepsilon)^{-1/2}X_{OE}\) and taking the monotone
\(\varepsilon\downarrow0\) limit; the limit exists precisely under the
range condition in item 2.

Thus the sharp constant one in (3.2) is **equivalent** to positivity of
the enlarged old-plus-shell form.  The commutator identity (1.5) specifies
\(X_{OE}\) exactly, but supplies neither the range inclusion nor the last
Schur inequality.

Apply this to the primitive compression

\[
 q(f,e)=\langle f+e,\Pi_TQ_T\Pi_T(f+e)\rangle.        \tag{3.3}
\]

If \(O_1\subset O_2\subset\cdots\) is an exhaustion by integer cells and
every newly born shell admits (3.2) with constant one, induction gives
positivity on every finite union.  Closedness gives \(Q_T\ge0\) on the
full primitive form domain.  Conversely, global positivity implies every
compression and hence every factorization (3.2).  Therefore

\[
 \boxed{\text{sharp boundary Douglas factorization on all cells}
 \ \Longleftrightarrow\ Q_T=-B_{\rm nuc}^{\rm prim}\ge0.}          \tag{3.4}
\]

By the Weil criterion, (3.4) is row D.  It cannot be invoked as an
auxiliary positive lemma without proving the same theorem by independent
means.

## 4. What a carré-du-champ does prove

For the positive reference operator

\[
 \mathcal R_T=H_{5/4,T}
 +\sum_{p^k\le e^{2T}}w_{p^k}J_{p^k,-}^*J_{p^k,-}\ge0,             \tag{4.1}
\]

the boundary factorization with constant one is automatic: write
\(\mathcal R_T=D_T^*D_T\), split \(D_TP_O\) and \(D_TP_E\), and use their
common target.  This is the genuine carré-du-champ supplied by the Gamma
jump differences and the antisymmetric Witt channels.

But

\[
 Q_T=\mathcal R_T-\mathcal W_T^*\mathcal W_T,         \tag{4.2}
\]

where \(\mathcal W_T\) contains the \(\beta\)-channel, the centred
resolvent, and every symmetric \(p^k\)-channel.  Subtracting the load in
(4.2) changes the old/shell block by exactly the centred Poisson anomaly
of D.77 and D.169.  The reference carré-du-champ therefore yields an
ambient factorization, not the defect factorization of the already
shorted old core.

This explains why the Hadamard map \(J_{p^k,+}\leftrightarrow
J_{p^k,-}\) is isometric before shorting yet leaves the residual
\(\mathfrak r_N\) afterwards.  The missing statement is not a norm
estimate for the raw Witt word; it is the range identity

\[
 \mathfrak r_N=D_N^{1/2}\widetilde w_N                 \tag{4.3}
\]

with the remaining unit budget.

## 5. Exact extra structure required

The preceding equivalence narrows the admissible next theorem.  A
noncircular closure must construct, from A--B--C before knowing the sign,
one of the following equivalent data:

* a trace-exact supported Poisson correction carrying the entire operator
  \(P_OQ_TP_E\), not only its two Tate moments;
* a nonlocal prime--Gamma martingale transform \(U_{OE}\) satisfying an
  independently proved isometry/contractivity law and
  \(X_{OE}^{\rm prim}=A_O^{1/2}U_{OE}B_E^{1/2}\);
* an exact source-defined solution of (4.3), with the norm budget proved
  from an identity other than positivity of \(Q_T\).

The extra datum must be infinite-dimensional.  A rank-two Tate correction,
or any fixed finite-rank modification, cannot cancel the infinite-rank
Gamma boundary block and all translated \(p^k\)-blocks simultaneously.

This is a no-go only for deriving the sharp factorization from the bare
Toeplitz--Hankel commutator and the two jets.  It does not assert that row D
is impossible.  It locates the precise new construction needed for the
next step: a source-side Poisson transport retaining the cross-window
block while enforcing support.

## 6. Reproducible finite-section audit

The companion script
`114_d_190_toeplitz_hankel_douglas_verify.py` checks:

1. \(P_OQP_E=[P_O,Q]P_E\) for a dense Toeplitz convolution plus several
   shift channels;
2. an old principal block can be positive while the enlarged Toeplitz
   block is indefinite;
3. in that case the sharp Schur/Douglas budget fails;
4. the cross block has full finite-section rank;
5. compression by two moment vectors changes the cross block by rank at
   most four and does not remove it;
6. for a positive comparison block, the sharp Douglas factorization and
   Schur complement hold with constant one.

The finite matrices are not evidence for or against RH.  They certify the
operator-typing and logical equivalence used above.
