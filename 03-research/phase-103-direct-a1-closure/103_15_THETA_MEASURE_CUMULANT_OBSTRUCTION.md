# Theta measure, low-order positivity, and the cumulant obstruction

## Purpose

`103_14` keeps the Euler prime sum and the Gamma/pole term separate.  This
note combines them before taking the regulator to zero.  The result is a
single positive theta measure and gives candid positivity for the first two
regularised Li coefficients.  It also gives an exact obstruction: positivity
of that measure and the functional equation do not control the higher
cumulants, hence cannot by themselves prove A1/RH.

## 1. One common positive measure

For \(u>0\), put
\[
 \Phi(u)=\sum_{m\ge1}
 \left(2\pi^2m^4e^{9u/2}-3\pi m^2e^{5u/2}\right)
 e^{-\pi m^2e^{2u}}.                                                  \tag{1}
\]
Every summand is positive on \((0,\infty)\), since its first factor is
\(πm^2e^{5u/2}(2\pi m^2e^{2u}-3)>0\).  The theta transformation gives
the standard cosine representation of the completed xi function.  Equivalently
(up to a positive constant, irrelevant after a logarithmic derivative),
\[
 \xi(s)=c\int_{\mathbb R}\Phi(|u|)e^{(s-1/2)u}\,du,\qquad c>0.        \tag{2}
\]
The superexponential decay from (1) makes all exponential moments finite.

Fix \(a=1+\varepsilon>1\).  Let \(\mu_a\) be the probability measure
\[
 d\mu_a(u)=
 {\Phi(|u|)e^{(a-1/2)u}\,du\over
  \int_{\mathbb R}\Phi(|v|)e^{(a-1/2)v}\,dv}.                         \tag{3}
\]
If \(U\) has law \(\mu_a\), then (2) gives the exact common representation
\[
 \boxed{
 \lambda_n(\varepsilon)
 =n[z^n]\log\mathbb E_a
       \exp\!\left({az\over1-z}U\right).}                           \tag{4}
\]
Here \(\lambda_n(\varepsilon)\) is the completed coefficient of `103_14`,
equation (6).  Thus (4) combines, before any limit, the pole, Gamma, and
Euler-prime pieces into one positive density.

## 2. Exact cumulant formula and the cases \(n=1,2\)

Let \(\kappa_j(a)\) be the cumulants of \(U\) under \(\mu_a\).  Expanding
the cumulant generating function in (4) yields
\[
 \boxed{
 \lambda_n(\varepsilon)
 =n\sum_{j=1}^n {a^j\over j!}
       {n-1\choose j-1}\kappa_j(a).}                                 \tag{5}
\]
All exchanges are justified by the exponential moments noted after (2).
In particular,
\[
 \lambda_1(\varepsilon)=a\kappa_1(a),
 \qquad
 \lambda_2(\varepsilon)=2a\kappa_1(a)+a^2\kappa_2(a).                \tag{6}
\]
The base measure \(\Phi(|u|)du\) is even.  Its moment generating function
is even and strictly log-convex, so at the positive tilt \(a-1/2>0\),
\[
 \kappa_1(a)>0,\qquad\kappa_2(a)=\mathrm{Var}_{\mu_a}(U)>0.
\]
Consequently (6) proves \(\lambda_1(\varepsilon)>0\) and
\(\lambda_2(\varepsilon)>0\) without any assertion about zeros.  This is
only a low-order theorem, not an induction mechanism.

For comparison, the contribution of one Euler factor
\(Z_p(s)=(1-p^{-s})^{-1}\) to these same coefficients is, with
\(q=p^{-a}\),
\[
 \mathcal P_{1,p}(a)=-{a\log p\over p^a-1},                           \tag{7}
\]
\[
 \mathcal P_{2,p}(a)=
 {a\log p\,q\over(1-q)^2}
 \left[a\log p-2(1-q)\right].                                        \tag{8}
\]
Thus the common positivity in (6) is genuinely global: even at order two,
individual Euler factors have no fixed sign.  For example, the bracket in
(8) is negative at \(p=2,a=1\) and hence for all \(a>1\) sufficiently
close to one, whereas it is positive for \(p\) sufficiently large.

## 3. Exact obstruction at higher order

Equation (5) involves every higher cumulant.  Positivity and evenness of a
measure do not control their signs and, more importantly, do not force the
zeros of its Fourier transform to be real.  This is not a heuristic
limitation; the following finite positive measure is an algebraic witness.

Let \(0<q<1/2\) and
\[
 \nu_q={\delta_{-1}+\delta_1+q\delta_{-2}+q\delta_2\over2(1+q)}.
\]
It is positive and even.  Its bilateral Laplace transform, up to a positive
constant, is
\[
 X_q(s)=\cosh(s-1/2)+q\cosh(2(s-1/2)),                                \tag{9}
\]
which has the same reality and functional symmetry
\(X_q(s)=X_q(1-s)\) as \(\xi\).  On the critical line it becomes
\[
 X_q(1/2+it)=\cos t+q\cos2t.
\]
Writing \(x=\cos t\), its zeros satisfy
\[
 2qx^2+x-q=0,
 \qquad
 x_-={-1-\sqrt{1+8q^2}\over4q}<-1.                                  \tag{10}
\]
More explicitly, with \(y=s-1/2\), equation (10) also gives
\(\cosh y=x_-\).  Since \(x_-<-1\), it has the solutions
\[
 y=\pm\mathrm{arcosh}(-x_-)+i(2k+1)\pi,\qquad k\in\mathbb Z,
\]
whose real parts are nonzero.  Hence the positive even measure \(\nu_q\),
despite its functional symmetry, has a transform with zeros off the
critical line.

Therefore the positive theta density in (2) cannot by itself supply the
missing A1 sign.  Any continuation of this mechanism must prove an extra
property specific to \(\Phi\), such as an infinite total-positivity or
Laguerre--Pólya theorem.  That extra property is RH-strength; it is not
implied by (1)--(4).

## 4. Orders three and four; first proposed strengthening destroyed

The next two identities from (5) are
\[
 \lambda_3(\varepsilon)
 =3a\kappa_1+3a^2\kappa_2+{a^3\over2}\kappa_3,                      \tag{11}
\]
\[
 \lambda_4(\varepsilon)
 =4a\kappa_1+6a^2\kappa_2+2a^3\kappa_3+{a^4\over6}\kappa_4.          \tag{12}
\]
Here, writing \(\mu=\mathbb E_aU\),
\[
 \kappa_3=\int(u-\mu)^3d\mu_a(u),
 \qquad
 \kappa_4=\int(u-\mu)^4d\mu_a(u)-3\kappa_2^2.                       \tag{13}
\]
Equations (11)--(13) are the requested single-density tests: no prime sum,
Gamma term, or limiting cancellation remains hidden.

A first sufficient proposal would be complete cumulant positivity
\(\kappa_j(a)\ge0\) for all \(j\ge1\), \(a>1\).  It would make every
summand in (5) nonnegative.  It is false for the actual theta measure.
Indeed, direct differentiation of the completed Euler--Gamma product gives
the exact identity
\[
 \kappa_3(a)=(\log\xi)'''(a)
 ={2\over a^3}+{2\over(a-1)^3}+{1\over8}\psi_2(a/2)
   +(\log\zeta)'''(a).                                               \tag{14}
\]
For \(a>1\), the last term is an absolutely convergent series of fixed
negative sign,
\[
 (\log\zeta)'''(a)
 =-\sum_{p}\sum_{k\ge1}k^2(\log p)^3p^{-ka}\le0.                   \tag{15}
\]
Also the exact polygamma series gives
\[
 \psi_2(x)=-2\sum_{m\ge0}{1\over(x+m)^3}
 \le-{1\over x^2}\qquad(x>0),                                      \tag{16}
\]
where the inequality follows by comparison with the integral from zero to
infinity.  For \(a\ge2\), equations (14)--(16) imply
\[
 \kappa_3(a)\le {2\over a^3}+{16\over a^3}-{1\over2a^2}<0
 \qquad(a>36).                                                       \tag{17}
\]
Thus even this natural all-cumulants positivity route is decisively
unavailable.  Notice that (17) does *not* make (11) negative: its positive
\(\kappa_1\) term is larger.  It only eliminates a proposed termwise
proof.

The genuinely minimal cumulant requirements at these orders are instead
\[
 \kappa_3\ge-{6\over a^2}\kappa_1-{6\over a}\kappa_2,              \tag{17a}
\]
\[
 \kappa_4\ge-{24\over a^3}\kappa_1-{36\over a^2}\kappa_2
                 -{12\over a}\kappa_3.                              \tag{17b}
\]
They are simply (11) and (12) rewritten.  The infinite family obtained
from (5), followed by \(a\downarrow1\), is exactly Li positivity, so it
is not a new positivity principle.

Finally, a stronger proposal that the theta kernel be a Pólya-frequency
(totally positive) kernel would force its Fourier transform to belong to
the Laguerre--Pólya class.  Applied to (2), that says precisely that all
zeros of \(\Xi(t)=\xi(1/2+it)\) are real.  It is therefore a valid
RH-proving target but is equivalent in strength to the desired conclusion,
not a consequence of the elementary positivity in (1).

## 5. Positive coefficients and the failed Kaluza route

Put
\[
 H_a(z)={\xi(a/(1-z))\over\xi(a)}=\sum_{n\ge0}b_n(a)z^n.             \tag{18}
\]
The coefficients \(b_n(a)\) are strictly positive.  Indeed, pair the two
halves of the even base measure in (2).  For \(k\ge0\),
\[
 \xi^{(k)}(a)\ \propto\
 \int_0^\infty u^k\Phi(u)
 \begin{cases}
  2\cosh((a-1/2)u),&k\ \hbox{even},\\
  2\sinh((a-1/2)u),&k\ \hbox{odd},
 \end{cases}du>0.                                                    \tag{19}
\]
Both the Taylor coefficients of \(\xi(a+w)/\xi(a)\) and those of
\(w=az/(1-z)\) are therefore positive, proving the claim.

There is an entirely algebraic sufficient criterion for converting this
fact into positivity of the logarithmic coefficients.  Let
\(B(z)=1+\sum_{n\ge1}b_nz^n\), with \(b_n>0\), and assume its ratios
\(b_n/b_{n-1}\) are nondecreasing.  Write
\[
 {1\over B(z)}=1-\sum_{n\ge1}c_nz^n.                                \tag{20}
\]
Then every \(c_n\ge0\).  To prove this without any external theorem,
compare coefficients in \(B(1-\sum c_nz^n)=1\):
\[
 b_n=c_n+\sum_{j=1}^{n-1}c_jb_{n-j}.                                \tag{21}
\]
Inductively assume \(c_1,\ldots,c_{n-1}\ge0\), multiply the equation for
\(b_{n-1}\) by \(b_n/b_{n-1}\), and use monotonicity of the ratios.  Each
term then dominates its counterpart in the sum in (21), including
\(c_{n-1}b_1\); hence \(b_n\ge\sum_{j<n}c_jb_{n-j}\) and \(c_n\ge0\).
Finally,
\[
 \log B(z)=-\log\!\left(1-\sum_{n\ge1}c_nz^n\right)
 =\sum_{r\ge1}{1\over r}\left(\sum_{n\ge1}c_nz^n\right)^r,          \tag{22}
\]
has nonnegative coefficients.  Thus log-convexity of \(b_n\) would be a
genuine non-circular sufficient criterion for
\(\lambda_n(\varepsilon)\ge0\).

It fails for the actual theta coefficients already at the first minor.
Let \(F(a)=\log\xi(a)\).  Direct composition gives
\[
 b_1=aF'(a),\qquad
 b_2=aF'(a)+{a^2\over2}\bigl(F''(a)+F'(a)^2\bigr),                  \tag{23}
\]
and therefore
\[
 b_0b_2-b_1^2
 =aF'(a)+{a^2\over2}\bigl(F''(a)-F'(a)^2\bigr).                    \tag{24}
\]
The Euler--Gamma formula, its absolutely convergent zeta series, and the
elementary polygamma bounds give
\[
 F'(a)={1\over2}\log{a\over2\pi}+O(a^{-1}),
 \qquad F''(a)={1\over2a}+O(a^{-2}).                                \tag{25}
\]
Substitution in (24) gives
\[
 b_0b_2-b_1^2
 =-{a^2\over8}\log^2{a\over2\pi}+O(a\log a)<0                     \tag{26}
\]
for all sufficiently large \(a\).  Hence the required log-convexity is
false, despite (19).

The finite witnesses above also fail it.  For the limiting two-point case
\(q=0\) in (9), put \(t=a-1/2\).  Then
\[
 b_1=a\tanh t,\qquad b_2=a\tanh t+{a^2\over2},
\]
so \(b_2-b_1^2<0\) for all sufficiently large \(a\).  By continuity the
same failure holds for the off-line examples \(0<q<1/2\) for sufficiently
large \(a\).  Thus the proposed Kaluza property excludes both the actual
theta kernel and the algebraic competitors; it is much stronger than Li
positivity and cannot be the missing mechanism.

Multiplying instead by \(n!\), i.e. replacing \(b_n\) with moment-like
coefficients \(n!b_n\), does not repair this argument: the proof
(20)--(22) is a statement about the coefficients of \(H_a\) itself, and
log-convexity of a differently normalized sequence gives no sign control
for \([z^n]\log H_a\).

## Status

The common-measure construction is exact and proves only the low-order
positivity in (6).  The finite measure (9)--(10) is an exact obstruction to
promoting generic positive-measure arguments to a proof of RH.  No
unconditional control of the higher cumulants, and hence no A1 closure, is
claimed.
