# The cubic Jensen discriminant gate

## Verdict

For the central theta coefficients
\[
 c_N={M_{2N}\over(2N)!}>0,
\]
consider
\[
 J^{3,N}(X)=c_N+3c_{N+1}X+3c_{N+2}X^2+c_{N+3}X^3.                \tag{1}
\]
This note derives and factors its discriminant exactly.  The PF\(_2\)
theorem in `103_34` is not sufficient: the cubic sign contains a new term
measuring the *variation of the descents* of consecutive coefficient
ratios.  Neither the covariance identity used in `103_34` nor the standard
Andreief/Vandermonde square controls that term.

No proof or disproof of cubic hyperbolicity for every shift of the actual
theta kernel is claimed here.  What is closed is the algebraic reduction
and the no-go for extrapolating the degree-two proof.

## 1. Exact discriminant

For a cubic \(AX^3+BX^2+CX+D\), direct elimination of a common root with
its derivative gives
\[
 \mathrm{disc}=B^2C^2-4AC^3-4B^3D-27A^2D^2+18ABCD.
\]
Substituting
\[
 A=c_{N+3},\quad B=3c_{N+2},\quad C=3c_{N+1},\quad D=c_N
\]
gives
\[
\boxed{\begin{aligned}
 {\Delta_N\over27}={}&
 3c_{N+1}^2c_{N+2}^2-4c_{N+1}^3c_{N+3}
 -4c_Nc_{N+2}^3\\
 &-c_N^2c_{N+3}^2
 +6c_Nc_{N+1}c_{N+2}c_{N+3}.
\end{aligned}}                                                   \tag{2}
\]
Because all coefficients of (1) are positive, \(\Delta_N>0\) is
equivalent to three distinct real negative roots: there is no positive
root, and a real cubic with positive discriminant has three distinct real
roots.

## 2. Ratio factorization and the exact new inequality

Put
\[
 x={c_{N+1}\over c_N},\qquad
 y={c_{N+2}\over c_{N+1}},\qquad
 z={c_{N+3}\over c_{N+2}},                                      \tag{3}
\]
and
\[
 a=x-y,\qquad b=y-z.                                             \tag{4}
\]
Dividing (2) by \(c_N^4\), substituting
\[
 c_{N+1}/c_N=x,\quad c_{N+2}/c_N=xy,
 \quad c_{N+3}/c_N=xyz,
\]
and expanding gives first
\[
 {\Delta_N\over27c_N^4}
 =x^2y\,[3x^2y-4x^2z-4xy^2-yz^2+6xyz].                          \tag{5}
\]
Substitution of \(y=x-a\) and \(z=x-a-b\), followed by cancellation,
gives the sharper factorization
\[
 \boxed{\quad
 {\Delta_N\over27c_N^4}
 =x^2y\left[a(a+b)^2-x(a-b)^2\right].\quad}                     \tag{6}
\]
This identity can also be checked by expanding its two sides; it uses no
inequality or asymptotic approximation.

The strict PF\(_2\) result of `103_34` says exactly
\[
 x>y>z>0,\qquad a>0,\qquad b>0.                                \tag{7}
\]
The remaining cubic condition is therefore precisely
\[
 \boxed{\qquad a(a+b)^2>x(a-b)^2.\qquad}                         \tag{8}
\]
It is a third-order regularity condition on the ratio sequence, not another
instance of log-concavity.

## 3. Exact counterexample to the PF2-to-PF3 inference

Strict decrease of the ratios does not imply (8).  Take the exact positive
sequence
\[
 c_0=1,\qquad c_1=1,\qquad c_2={9\over10},\qquad
 c_3={9\over100}.                                                \tag{9}
\]
Its ratios are
\[
 x=1,qquad y={9\over10},\qquad z={1\over10},
\]
so both adjacent PF\(_2\) inequalities are strict.  But
\[
 a={1\over10},\qquad b={4\over5},
\]
and the bracket in (6) is
\[
 {1\over10}\left({9\over10}\right)^2
 -\left(-{7\over10}\right)^2
 ={81\over1000}-{49\over100}
 =-{409\over1000}<0.                                            \tag{10}
\]
Thus the corresponding cubic has negative discriminant.  This is an exact
counterexample to any proof rule using only positivity and the two adjacent
log-concavity minors.

It is not a counterexample to the actual theta sequence.  Its role is to
prove that the theorem in `103_34` cannot be iterated without a new estimate
for \(a-b\).

## 4. Why the Vandermonde-square proposal does not match

For any positive measure \(d\mu(t)\), the Andreief expansion gives the
positive Hankel determinant
\[
 \det(\mu_{r+i+j})_{i,j=0}^2
 ={1\over3!}\int_{(0,\infty)^3}
 (t_1t_2t_3)^r
 \prod_{i<j}(t_i-t_j)^2\prod_{j=1}^3d\mu(t_j)\ge0.              \tag{11}
\]
The determinant in (11) necessarily contains moments through
\(\mu_{r+4}\).  In contrast, the cubic discriminant (2) is quartic in the
four coefficients \(c_N,\ldots,c_{N+3}\) and contains no \(c_{N+4}\).
Consequently it is not the Hankel determinant (11), before or after the
factorial normalization.

One can place the five terms in (2) over a fourfold product of the theta
measure, but its direct symmetrization retains the alternating coefficients
\(3,-4,-4,-1,6\); it does not algebraically reduce to a Vandermonde square.
The exact sequence (9) shows, at minimum, that no identity based only on
coefficient positivity and the adjacent PF\(_2\) minors can turn that
quartic form into a square.  It does not rule out a further identity special
to the actual theta measure.  The factorial factors change the coefficients
of the alternating terms but do not by themselves supply such an identity.

The same mismatch occurs for the natural Wronskian.  A three-by-three
Wronskian/Hankel determinant of consecutive derivatives uses one further
coefficient, whereas the resultant defining \(\Delta_N\) stops at
\(c_{N+3}\).  A Wronskian proof would therefore require an additional
identity eliminating the \(c_{N+4}\) term.  No such identity follows from
the theta moment representation or from integration by parts alone.

## 5. What a theta-specific cubic proof must establish

Let
\[
 r_N={c_{N+1}\over c_N},\qquad d_N=r_N-r_{N+1}>0.                \tag{12}
\]
Then (8) becomes the exact target
\[
 \boxed{\quad
 d_N(d_N+d_{N+1})^2
 >r_N(d_N-d_{N+1})^2\qquad(N\ge0).\quad}                         \tag{13}
\]
The covariance proof in `103_34` establishes only \(d_N>0\).  Proving
(13) requires quantitative control of the change
\(d_N-d_{N+1}\), equivalently a third finite difference of
\(\log c_N\).

For the explicit theta density, differentiating the log-sum identity used
in `103_34` one more time introduces the third centered moment
\[
 \sum_mw_m(\ell_m'-\overline{\ell'})^3,                          \tag{14}
\]
together with covariance terms involving \(\ell_m''\).  Unlike the
variance in the second derivative, (14) has no fixed sign.  The elementary
tail dominance estimates prove that it is small, but smallness by itself
does not imply the scale-sensitive inequality (13), whose two sides tend
to zero with \(N\).

Thus the next valid theorem must be one of the following, with explicit
constants uniform in \(N\):

1. a direct bound for the third finite difference of the normalized
   log-moments strong enough to imply (13); or
2. a theta-specific fourfold integral identity whose signed kernel can be
   controlled using more than positivity/log-concavity; or
3. an effective saddle estimate for the four consecutive moments, plus a
   rigorous finite certificate for the remaining shifts.

Until one of these is supplied, degree three remains open.  The precise
unproved term is the right side of (13), measuring unequal consecutive
ratio descents; neither PF\(_2\) nor a generic Vandermonde square controls
it.
