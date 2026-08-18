# The first Jensen minor for the specific theta kernel

## Result

Let
\[
 \Phi(u)=\sum_{m\ge1}\pi m^2e^{5u/2}
 (2\pi m^2e^{2u}-3)e^{-\pi m^2e^{2u}},\qquad u>0,                 \tag{1}
\]
and
\[
 M_p=2\int_0^\infty u^p\Phi(u)\,du,qquad
 c_N={M_{2N}\over(2N)!}.                                        \tag{2}
\]
The factor 2 is immaterial and matches the even measure in `103_31`.

> **Theorem.** For every integer \(N\ge0\),
> \[
> \boxed{\qquad c_{N+1}^2>c_Nc_{N+2}.\qquad}                    \tag{3}
> \]

Equivalently, the degree-two central Jensen polynomial
\[
 c_N+2c_{N+1}X+c_{N+2}X^2
\]
has two distinct negative real zeros for every shift \(N\).  In the moment
form of `103_31`, (3) is exactly
\[
 {M_{2N}M_{2N+4}\over M_{2N+2}^2}
 <{(2N+4)(2N+3)\over(2N+2)(2N+1)}.                               \tag{4}
\]

The proof has two independent parts.  First we prove strict log-concavity
of the *actual sum* (1), including the cross-summand variance.  Then an
integration-by-parts covariance lemma converts decreasing log-concavity
into factorial-normalized moment log-concavity.

## 1. Strict log-concavity of the full theta kernel

Put
\[
 x=\pi e^{2u}>\pi,qquad
 f_m(u)=\pi m^2e^{5u/2}(2m^2x-3)e^{-m^2x},qquad
 \ell_m=\log f_m.                                                \tag{5}
\]
Termwise differentiation is justified uniformly on every interval
\([0,U]\) by the Gaussian factor \(e^{-\pi m^2}\).  Direct calculation
gives
\[
 \ell_m'={5\over2}+{4m^2x\over2m^2x-3}-2m^2x,                   \tag{6}
\]
\[
 \ell_m''=-4m^2x-{24m^2x\over(2m^2x-3)^2}<-4m^2x\le-4x.        \tag{7}
\]
Each summand is therefore strictly log-concave.  This alone is not enough:
a sum of log-concave functions need not be log-concave.  We now bound the
missing cross term.

Let \(w_m=f_m/\Phi\).  The exact log-sum identity is
\[
 (\log\Phi)''=\sum_{m\ge1}w_m\ell_m''+
 \mathrm{Var}_w(\ell_m').                                \tag{8}
\]
The variance is no larger than its second moment about the fixed value
\(\ell_1'\):
\[
 \mathrm{Var}_w(\ell_m')
 \le\sum_{m\ge2}w_m(\ell_m'-\ell_1')^2.                          \tag{9}
\]
For \(a=m^2-1\ge3\), the function
\(F(t)=4t/(2t-3)=2+6/(2t-3)\) decreases on \(t>3/2\).  Equations
(6) and \(x>\pi>3\) give
\[
 |\ell_m'-\ell_1'|
 =2ax+F(x)-F(m^2x)
 \le2ax+{6\over2x-3}<3ax.                                      \tag{10}
\]
Moreover,
\[
 {f_m\over f_1}
 =m^2{2m^2x-3\over2x-3}e^{-ax}
 \le2m^4e^{-ax};                                                 \tag{11}
\]
indeed \(2m^2x-3\le2m^2(2x-3)\) follows from \(x>3\).
Since \(w_m\le f_m/f_1\), (9)--(11) yield
\[
 \mathrm{Var}_w(\ell_m')
 \le18x^2\sum_{m\ge2}m^4(m^2-1)^2e^{-(m^2-1)x}.                 \tag{12}
\]

Here is a fully elementary uniform bound for the last series.  For
\(a=m^2-1\ge3\),
\[
 m^4=(a+1)^2\le {16\over9}a^2.
\]
Also \(x^2e^{-ax}\) decreases for \(x\ge\pi\), because
\(2/x-a<0\).  Enlarge the set \(\{m^2-1:m\ge2\}\) to all integers
\(a\ge3\).  The elementary bounds
\[
 \pi^2<10,\qquad e^\pi>23
\]
are rationally checkable: \(3.1415<\pi<22/7\), and the first nine positive
terms of the exponential series at \(3.1415\) already sum to more than
\(23\).  They give
\[
\begin{aligned}
 \mathrm{Var}_w(\ell_m')
 &\le32\pi^2\sum_{a=3}^\infty a^4e^{-a\pi}\\
 &<320\sum_{a=3}^\infty{a^4\over23^a}.                            \tag{13}
\end{aligned}
\]
For \(a\ge3\), the ratio of consecutive summands in the last series is at
most
\[
 {1\over23}\left({4\over3}\right)^4={256\over1863}<{1\over7}.
\]
Consequently
\[
 \mathrm{Var}_w(\ell_m')
 <320\,{81\over23^3}\,{7\over6}<2.49.                            \tag{14}
\]
Combining (7), (8), and (14),
\[
 (\log\Phi)''<-4x+2.49<-12+2.49<0.                              \tag{15}
\]
Thus the complete theta kernel, not merely its individual summands, is
strictly log-concave on \((0,\infty)\).

The theta transformation used to obtain (1) gives a smooth even extension
\(\Phi(|u|)\) through zero.  Hence \(\Phi'(0+)=0\).  By (15),
\((\log\Phi)'\) is strictly decreasing, so
\[
 \Phi'(u)<0\qquad(u>0).                                          \tag{16}
\]

## 2. A self-contained normalized-moment lemma

> **Lemma.** Let \(f:(0,\infty)\to(0,\infty)\) be smooth, decreasing,
> log-concave, and rapidly decreasing, with finite moments
> \(m_p=\int_0^\infty u^pf(u)du\).  Then
> \[
> a_p={m_p\over p!}\qquad(p=0,1,2,\ldots)
> \]
> is strictly log-concave if \((\log f)'\) is not constant:
> \[
> a_p^2>a_{p-1}a_{p+1}\qquad(p\ge1).                             \tag{17}
> \]

*Proof.* Put \(h=-f'/f\).  Decrease of \(f\) gives \(h\ge0\), and
log-concavity gives that \(h\) is nondecreasing.  Under the probability
measure
\[
 d\nu_p(u)={u^pf(u)du\over m_p},
\]
the covariance of the two increasing functions \(u\) and \(h(u)\) is
nonnegative.  This follows directly from
\[
 2\mathrm{Cov}_{\nu_p}(u,h)
 =\iint (u-v)(h(u)-h(v))d\nu_p(u)d\nu_p(v)\ge0.                  \tag{18}
\]
Integration by parts, with vanishing boundary terms, gives
\[
 \mathbb E_{\nu_p}h={p\,m_{p-1}\over m_p},\qquad
 \mathbb E_{\nu_p}(uh)={p+1},\qquad
 \mathbb E_{\nu_p}u={m_{p+1}\over m_p}.                         \tag{19}
\]
Therefore (18)--(19) imply
\[
 p+1\ge {p\,m_{p-1}m_{p+1}\over m_p^2},
\]
or
\[
 {m_p^2\over(p!)^2}\ge
 {m_{p-1}\over(p-1)!}{m_{p+1}\over(p+1)!}.                     \tag{20}
\]
Strictness follows because \(h\) is strictly increasing on a set of
positive measure. \(\square\)

Apply the lemma to \(f=2\Phi\), using (15)--(16) and the
superexponential tail in (1).  The sequence
\[
 a_p={M_p\over p!}
\]
is strictly log-concave.  Thus its successive logarithmic slopes decrease.
Adding two consecutive slopes shows that the even subsequence is also
strictly log-concave:
\[
 a_{2N+2}^2>a_{2N}a_{2N+4}.                                     \tag{21}
\]
Since \(c_N=a_{2N}\), this is (3), completing the proof.

## 3. Does the argument scale beyond the first minor?

The proof establishes precisely PF\(_2\)-type information: all adjacent
two-by-two minors of the normalized coefficient sequence have the required
sign.  Its decisive identity is the two-function covariance square (18).
It does not produce signs for three-by-three Toeplitz minors or the
discriminants of degree-three Jensen polynomials.

There are two concrete reasons the proof does not automatically iterate.

1. Higher minors expand into alternating sums of products of moments;
   neither the scalar curvature bound (15) nor pairwise association (18)
   turns those sums into squares.
2. Differentiating (8) again introduces third centered moments of the
   slopes \(\ell_m'\), which have no fixed sign.  Thus the variance estimate
   responsible for PF\(_2\) has no sign-preserving higher-order analogue.

Accordingly, (3) is a complete new theorem for every shift, but not an
induction to PF\(_r\) for \(r\ge3\).  The next legitimate target is the
degree-three Jensen discriminant expressed in \(c_N,c_{N+1},c_{N+2},c_{N+3}\);
it requires a new three-point or determinant identity specific to the theta
kernel, not another application of log-concavity.
