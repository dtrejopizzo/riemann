# Theta translation tails and a quantitative PF3 criterion

## Result and scope

For the theta kernel of `103_34`, the higher theta modes are not merely
``small terms''.  They are exact positive translates of the first mode:

\[
 f_m(u)=m^{-1/2}f_1(u+\log m).                                  \tag{1}
\]

This gives an exact, strictly decreasing sequence of relative tail errors
for the factorial-normalized moments.  Combining it with the discriminant
of `103_36` yields the following non-circular sufficient condition for the
cubic gate.  It uses information not contained in log-concavity or a
pointwise curvature bound.

It does **not** prove the condition for every shift.  In particular, no
claim of PF3, A1, or RH is made in this note.

## 1. Exact translate structure

Write
\[
 x=\pi e^{2u},\qquad
 f_m(u)=\pi m^2e^{5u/2}(2\pi m^2e^{2u}-3)e^{-\pi m^2e^{2u}}.
                                                                    \tag{2}
\]
Putting \(v=u+\log m\) in the formula for \(f_1\) gives the exact
identity
\[
 \boxed{\quad f_m(u)=m^{-1/2}f_1(u+\log m).\quad}              \tag{3}
\]
Thus the full kernel is a very particular one-sided mixture of translates,
not an arbitrary sum of log-concave functions.

Put
\[
 A_p=\int_0^\infty u^p f_1(u)\,du,
 \qquad
 R(u)={\Phi(u)-f_1(u)\over f_1(u)}=\sum_{m\ge2}r_m(u),
 \qquad r_m={f_m\over f_1}.                                    \tag{4}
\]
All terms are positive and the series and its first derivative converge
locally uniformly.  The moment tail is therefore exactly
\[
 \epsilon_p:={1\over A_p}\sum_{m\ge2}\int_0^\infty u^pf_m(u)\,du
 =\mathbb E_{\nu_p}R(U),
 \qquad
 d\nu_p(u)={u^pf_1(u)\,du\over A_p},                            \tag{5}
\]
so that
\[
 M_p=2A_p(1+\epsilon_p).                                       \tag{6}
\]
The change of variables in (3) also gives the useful fully explicit form
\[
 \int_0^\infty u^pf_m(u)\,du
 =m^{-1/2}\int_{\log m}^{\infty}(v-\log m)^pf_1(v)\,dv.       \tag{7}
\]
There is no asymptotic approximation in (3)--(7).

## 2. The tail error is strictly decreasing under moment tilting

The logarithmic derivative calculation already used in `103_34` gives,
with \(a=m^2-1\),
\[
 {d\over du}\log r_m(u)
 =-2ax+{4m^2x\over2m^2x-3}-{4x\over2x-3}<0.                   \tag{8}
\]
Indeed \(t\mapsto4t/(2t-3)\) is decreasing for \(t>3/2\).  Hence
every \(r_m\), and consequently \(R\), is strictly decreasing.

Since \(d\nu_{p+1}=u\,d\nu_p/\mathbb E_{\nu_p}U\), (5) gives the
exact update
\[
 \boxed{\quad
 \epsilon_{p+1}-\epsilon_p
 ={\mathrm{Cov}_{\nu_p}(U,R(U))\over\mathbb E_{\nu_p}U}<0.
 \quad}                                                        \tag{9}
\]
The strict sign follows from the elementary two-copy covariance identity,
because \(U\) is increasing and \(R(U)\) is strictly decreasing.  This
is a theta-mode statement: generic log-concavity does not produce the
function \(R\), let alone its monotonicity.

There is also a uniform rational bound.  The estimate from `103_34`,
\(r_m\le2m^4e^{-(m^2-1)x}\), together with \(x\ge\pi\),
\(e^\pi>23\), and \(m^4=(a+1)^2\le16a^2/9\), yields
\[
\begin{aligned}
 R(u)&\le {32\over9}\sum_{a=3}^{\infty}{a^2\over23^a}\\
 &\le {32\over23^3}{1\over1-1/12}
 ={384\over133837}<{1\over300}.                              \tag{10}
\end{aligned}
\]
Here the ratio of successive summands is at most
\((4/3)^2/23=16/207<1/12\).  Consequently
\[
 \boxed{\qquad 0<\epsilon_{p+1}<\epsilon_p<{1\over300}
 \qquad(p\ge0).\qquad}                                       \tag{11}
\]
The coarse constant in (11) is not intended to resolve the cubic
cancellation; its role is to make the tail separation rigorous.

## 3. A robust first-mode-plus-tail sufficient condition

Set
\[
 b_N={A_{2N}\over(2N)!},\qquad
 \widehat c_N={c_N\over2}=b_N(1+\epsilon_{2N}).                \tag{12}
\]
The factor two is immaterial for the sign of a cubic discriminant.  For
four positive entries \(v_0,\ldots,v_3\), write the quartic form of
`103_36` as
\[
\begin{aligned}
 \mathscr D(v):={\Delta(v)\over27}
 ={}&3v_1^2v_2^2+6v_0v_1v_2v_3\\
 &-4v_1^3v_3-4v_0v_2^3-v_0^2v_3^2.                             \tag{13}
\end{aligned}
\]
Define its negative mass at the first mode by
\[
 Q_N=4b_{N+1}^3b_{N+3}+4b_Nb_{N+2}^3+b_N^2b_{N+3}^2>0.          \tag{14}
\]

> **Proposition (theta tail robustness).**  If, at a given \(N\),
> \[
> \boxed{\qquad
> \mathscr D(b_N,b_{N+1},b_{N+2},b_{N+3})
> >\bigl((1+\epsilon_{2N})^4-1\bigr)Q_N,
> \qquad}                                                       \tag{15}
> \]
> then the actual theta cubic \(J^{3,N}\) has positive discriminant,
> hence three distinct negative roots.

*Proof.*  By (9), each of the four multipliers in (12) lies in
\([1,1+\epsilon_{2N}]\).  The two positive monomials in (13) can only
increase, while each of its three negative monomials increases by at most
the factor \((1+\epsilon_{2N})^4\).  Therefore
\[
 \mathscr D(\widehat c_N,\ldots,\widehat c_{N+3})
 \ge \mathscr D(b_N,\ldots,b_{N+3})
 -\bigl((1+\epsilon_{2N})^4-1\bigr)Q_N.                       \tag{16}
\]
Condition (15) makes the right side positive.  Homogeneity gives
\(\mathscr D(c_N,\ldots,c_{N+3})=16\mathscr D(\widehat c_N,\ldots,
\widehat c_{N+3})\), completing the proof. \(\square\)

Equivalently, with the first-mode relative margin
\[
 \Gamma_N={\mathscr D(b_N,b_{N+1},b_{N+2},b_{N+3})\over Q_N}, \tag{17}
\]
the concrete next criterion is
\[
 \Gamma_N>(1+\epsilon_{2N})^4-1.                              \tag{18}
\]
This retains the *correlated* four-moment information that is discarded by
the independent Gaussian enclosures ruled out in `103_40`.  It is also
compatible with the exact ratio-drop criterion of `103_36`; it is merely a
different sufficient certificate for its discriminant.

## 4. A tempting translation-mixture lemma is false

Identity (3) must not be replaced by the false assertion that positive
mixtures of translates preserve cubic Jensen hyperbolicity.  Here is an
exact counterexample at shift zero.

For the point mass \(\delta_a\) on \((0,\infty)\), its central
normalized coefficients are
\[
 c_N(a)={a^{2N}\over(2N)!}.
\]
The associated cubic has discriminant
\[
 \Delta_a={127\over9600}a^{12}>0,                              \tag{19}
\]
so each individual translated point mass has three distinct negative
cubic Jensen roots.  But the positive mixture of two translates
\[
 \mu={18\over19}\delta_{1/2}+{1\over19}\delta_{3/2}            \tag{20}
\]
has
\[
 (c_0,c_1,c_2,c_3)=
 \left(1,{27\over152},{33\over2432},{83\over97280}\right),   \tag{21}
\]
and direct substitution in the cubic discriminant gives
\[
 \Delta(\mu)=-{3784779\over1708143411200}<0.                  \tag{22}
\]
Thus even a two-point positive mixture of translates of one base measure
can reverse the cubic sign, despite strict PF3 at the two components.
This exactly blocks a shortcut based on (3) alone.  The actual theta
weights and the quantitative monotone errors (5)--(11) must remain in the
argument; they cannot be discarded in favour of an abstract mixture
principle.

## 5. Circularity audit and remaining work

All identities and inequalities above follow from the displayed theta
series, positive-term interchanges, and the elementary estimates already
proved in `103_34`.  They use neither a zero-location hypothesis nor RH.

What remains unproved in (18) is a lower bound for the *first-mode*
relative cubic margin \(\Gamma_N\) at the same scale as the tail error.
The uniform bound (11) is deliberately too blunt for large \(N\), where
`103_40` identifies a third-order cancellation.  A viable continuation
would need correlated estimates for \(\Gamma_N\) and the decreasing
quantity \(\epsilon_{2N}\), not four independent moment intervals.

Finally, a claim that the full theta translation mixture is PF\(_\infty\),
or that all its Jensen polynomials are hyperbolic, would be RH-strength by
the central-function equivalence in `103_31`; it cannot be inserted here
as an auxiliary theorem.  The present proposition is only a one-way,
explicit sufficient test for a fixed cubic shift and makes no such
assumption.
