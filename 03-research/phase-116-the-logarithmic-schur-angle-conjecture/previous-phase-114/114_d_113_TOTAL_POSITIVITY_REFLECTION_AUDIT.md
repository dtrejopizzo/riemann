# D.113 — Total positivity, two-jet compression and Gamma counterminors

## Status

The one-prime cofinal kernel

\[
 K_\rho(r,s)=\rho^{|r-s|},\qquad \rho=p^{-1/2},
\]

is totally nonnegative.  This is a genuine variation-diminishing structure
on each ordered Frobenius-depth chain.

It does not survive the operations required for row D.

1. Ordinary total nonnegativity is already destroyed by the Künneth tensor
   of two depth chains.
2. Orthogonal compression by the two Tate jets produces minors of both
   signs, even after the unique diagonal sign gauge which makes all entries
   positive in the first nontrivial example.
3. The signed local kernel \(K_\rho-I\) has a positive direction satisfying
   both local Tate moment equations for the actual prime \(p=3\).
4. A positive sum of two distinct Gamma heat modes has principal and cross
   minors of opposite signs.  Thus the oscillator is not a sign-regular
   kernel under ordinary one-dimensional ordering.

Consequently neither classical total positivity, sign regularity nor a
variation-diminishing theorem preserved by Künneth can prove the global
primitive inequality.  Any restoration in the completed prime--Gamma form
would have to be a cross-place cancellation theorem.  The exact inequality
which must cancel the local \(p=3\) counterdirection is displayed below;
proving it uniformly is a special case of row D, not a consequence of the
local cones.

No zeta zero or sign of \(B_{\rm nuc}\) is used.  The paper is not modified.

## 1. Total nonnegativity of one prime chain

Let \(S\) be the unilateral shift and put

\[
 A_\rho=(I-\rho S)^{-1}.
\]

Its matrix is

\[
 (A_\rho)_{ij}=\mathbf1_{i\geq j}\rho^{i-j}.            \tag{1.1}
\]

This is the path matrix of a directed weighted line, hence is totally
nonnegative by the Lindström--Gessel--Viennot lemma.  Products and
transposes of totally nonnegative matrices are totally nonnegative by
Cauchy--Binet.  Since

\[
 K_\rho=(1-\rho^2)A_\rho^*A_\rho,                      \tag{1.2}
\]

every ordered minor of \(K_\rho\) is nonnegative.

The vanishing minors have the expected Markov meaning: separated row and
column sets are conditionally independent across a cut.  Thus the kernel
is totally nonnegative, not strictly totally positive.

The neutral-chamber residuation Jacobians of D.110 are consecutive
replication/path matrices.  Their polar parts differ only by positive
column scalings.  They preserve this one-chain cone under composition.

## 2. Künneth does not preserve the ordinary total order

Take \(\rho=1/2\) and the two-depth kernel

\[
 K=\begin{pmatrix}1&1/2\\1/2&1\end{pmatrix}.           \tag{2.1}
\]

Both \(K\) and its second copy are totally positive.  In lexicographic
order their Künneth matrix is

\[
 K\otimes K=
 \begin{pmatrix}
 1&1/2&1/2&1/4\\
 1/2&1&1/4&1/2\\
 1/2&1/4&1&1/2\\
 1/4&1/2&1/2&1
 \end{pmatrix}.                                         \tag{2.2}
\]

The minor with rows \((0,1)\) and columns \((1,2)\) is

\[
 \det\begin{pmatrix}1/2&1/2\\1&1/4\end{pmatrix}
 =-{3\over8}.                                           \tag{2.3}
\]

Hence ordinary one-dimensional total positivity is not a monoidal property
of the row-A Künneth object.  A multivariate MTP notion may survive on the
product partial order, but it has no single oscillation count capable of
removing exactly the two global Tate directions.

## 3. Two-jet compression destroys sign regularity

On four consecutive depths let

\[
 K_{ij}=2^{-|i-j|},\qquad
 h_-=(1,1/2,1/4,1/8)^t,qquad
 h_+=(1/8,1/4,1/2,1)^t.                                \tag{3.1}
\]

Let \(P\) be the orthogonal projection onto
\(\ker h_-^t\cap\ker h_+^t\), and set \(C=PKP\).  The unique diagonal
sign gauge making every entry of \(C\) nonnegative is

\[
 D=\operatorname{diag}(1,-1,-1,1).                     \tag{3.2}
\]

One computes

\[
 DCD={1\over474721}
 \begin{pmatrix}
 57660&100686&51000&43464\\
 100686&200715&26814&51000\\
 51000&26814&200715&100686\\
 43464&51000&100686&57660
 \end{pmatrix}.                                         \tag{3.3}
\]

Its principal minor on \((0,1)\) is positive:

\[
 \det(DCD)_{(0,1),(0,1)}={3024\over474721}>0,           \tag{3.4}
\]

whereas the minor with rows \((0,1)\) and columns \((0,2)\) is

\[
 \det(DCD)_{(0,1),(0,2)}=-{7560\over474721}<0.          \tag{3.5}
\]

Thus the compressed kernel is neither totally nonnegative nor sign-regular
of order two.  Positivity as a Hilbert compression remains true; it is the
variation-diminishing order which is lost.

## 4. Exact local primitive counterdirection at \(p=3\)

Let \(\rho=3^{-1/2}\), take six depths, and define the local second-order
Tate annihilator

\[
 (Zy)_j=y_j-(\rho+\rho^{-1})y_{j-1}+y_{j-2},            \tag{4.1}
\]

with zero coefficients outside the range.  Its characteristic roots are
\(\rho\) and \(\rho^{-1}\), so

\[
 \sum_{j=0}^5(Zy)_j\rho^j=0,qquad
 \sum_{j=0}^5(Zy)_j\rho^{-j}=0.                        \tag{4.2}
\]

For

\[
 y=(-2,-3,-3,-2)^t
\]

one obtains

\[
 x=Zy=left(
 -2,
 -3+{8\sqrt3\over3},
 -5+4\sqrt3,
 -5+4\sqrt3,
 -3+{8\sqrt3\over3},
 -2\right)^t.                                           \tag{4.3}
\]

Equations (4.2) hold exactly, but

\[
 \boxed{
 x^t(K_\rho-I)x={4\over3}(-109+63\sqrt3)>0.}            \tag{4.4}
\]

The final inequality is exact because
\(63^2\cdot3=11907>11881=109^2\).

Therefore even the **local** signed prime form has a positive direction
after its own two Tate modes are removed.  Local variation diminution
cannot imply the required sign.

## 5. Gamma heat modes have an exact counterminor

Consider any heat-regularized sum of two distinct positive oscillator
modes.  On an equally spaced chain its stationary kernel has

\[
 f_k=w_1\rho_1^k+w_2\rho_2^k,qquad
 0<\rho_1\ne\rho_2<1,quad w_1,w_2>0.                  \tag{5.1}
\]

The principal two-by-two minor is

\[
 \det\begin{pmatrix}f_0&f_1\\f_1&f_0\end{pmatrix}
 =f_0^2-f_1^2>0.                                       \tag{5.2}
\]

But the cross minor with rows \((0,1)\) and columns \((1,2)\) is

\[
 \begin{aligned}
 \det\begin{pmatrix}f_1&f_2\\f_0&f_1\end{pmatrix}
 &=f_1^2-f_0f_2\\
 &=-w_1w_2(\rho_1-\rho_2)^2<0.                         \tag{5.3}
 \end{aligned}
\]

For example, \(w_1=w_2=1\), \(\rho_1=1/2\),
\(\rho_2=1/3\) gives \(-1/36\).

The quarter-shift oscillator contains infinitely many distinct positive
rates \(j+1/4\).  After any positive heat regularization, (5.3) becomes

\[
 -\sum_{i<j}w_iw_j(\rho_i-\rho_j)^2<0,                 \tag{5.4}
\]

while (5.2) stays positive.  Hence the Gamma heat-mode kernel is not
sign-regular of order two.  A positive sum of totally nonnegative
exponential Green kernels need not be totally nonnegative; total
nonnegativity is closed under composition, not under arbitrary addition.

## 6. The exact cross-place obligation

The local vector (4.3) contributes

\[
 q_3=\log3\,{4\over3}(-109+63\sqrt3)>0                 \tag{6.1}
\]

to the signed prime sector.  Therefore any completed prime--Gamma Hodge
theorem must prove, on every geometric landing of this depth vector,

\[
 B_{\Gamma+\mathrm{other\ primes}}(x,x)\leq-q_3.        \tag{6.2}
\]

This is a quantitative cross-place cancellation.  Neither the
one-prime TN cone nor the Gamma mode cone implies (6.2), since the required
operations have the explicit counterminors (2.3), (3.5) and (5.3).

At the operator level the completed assertion remains

\[
 \|\partial_XF\|^2\geq(2A_X+m_0)\|F\|^2,qquad
 M_-(F)=M_+(F)=0.                                      \tag{6.3}
\]

Thus a proof that the completion restores the **Hodge sign** is exactly D.
A proof that it restores total positivity or sign regularity would be
strictly stronger and is already incompatible with the natural Künneth
and heat-mode coordinate kernels above.

## 7. Outcome

The variation-diminishing route separates cleanly:

\[
 \begin{array}{c|c}
 \text{one prime depth Green}&\text{totally nonnegative}\\
 \text{residuation composition}&\text{preserves the chain cone}\\
 \text{Künneth product order}&\text{fails TN: (2.3)}\\
 \text{two Tate compression}&\text{fails SR}_2:\ (3.4)-(3.5)\\
 \text{signed local prime form}&\text{positive primitive vector: (4.4)}\\
 \text{Gamma heat sum}&\text{fails SR}_2:\ (5.2)-(5.3).
 \end{array}
\]

Therefore D cannot be obtained from a classical total-positivity theorem
on the completed stratified object.  The remaining viable principle must
be a genuinely adelic cross-place polarization or reflection positivity
which is weaker than total positivity but strong enough to prove (6.3).

