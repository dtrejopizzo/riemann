# Convex hazard is still insufficient for the cubic Jensen gate

## Verdict

The proposed general lemma is false.  There are smooth positive decreasing
rapidly decreasing densities \(f\) on \([0,\infty)\) for which
\[
 h=-{f'\over f},\qquad h'>0,\qquad h''>0,                     \tag{1}
\]
but the degree-three central Jensen polynomial has negative discriminant.
Thus, even strict increase and strict convexity of the hazard \(h\) do not
imply hyperbolicity of the cubic Jensen polynomials of \(m_p/p!\).

This is stronger than the strong-curvature no-go in `103_39`: it eliminates
the natural attempt to repair that no-go by requiring a sign for
\(h''=-(\log f)'''\).  It does not disprove a theta-specific inequality;
it proves that any such inequality must use more than the signs of the
first two derivatives of its hazard.

## 1. Exact connection to the cubic gate

Use the notation of `103_39`:
\[
 a_p={m_p\over p!},\qquad q_p={a_{p+1}\over a_p},\qquad
 \delta_j=q_j-q_{j+1}.                                        \tag{2}
\]
For the central subsequence \(c_N=a_{2N}\), with \(p=2N\),
\[
 r_N=q_pq_{p+1},\qquad
 d_N=q_{p+1}(\delta_p+\delta_{p+1})+
     q_{p+2}(\delta_{p+1}+\delta_{p+2}).                       \tag{3}
\]
The discriminant of the cubic is positive exactly when
\[
 B_N:=d_N(d_N+d_{N+1})^2-r_N(d_N-d_{N+1})^2>0.                 \tag{4}
\]
There is no loss from passing to this formulation: it is precisely
equation (13) of `103_36`.

The integration-by-parts covariance identity remains valid,
\[
 \delta_j={q_j\over j+2}\,
 \mathrm{Cov}_{\nu_{j+1}}(u,h).                         \tag{5}
\]
Convexity of \(h\) does add a genuine three-point sign.  For
\(x<y<z\),
\[
 \det\begin{pmatrix}1&1&1\\x&y&z\\h(x)&h(y)&h(z)\end{pmatrix}
 =(y-x)(z-x)(z-y)[x,y,z]h\ \geq0,                             \tag{6}
\]
where \([x,y,z]h\) is the second divided difference.  In the smooth
strictly convex case the sign in (6) is strict.  The counterexample below
has this strict three-point positivity and (5), yet has \(B_0<0\).
Consequently no positive-kernel triple-covariance identity can identify
the cubic bracket (4) from these hypotheses alone.

## 2. A rationally certified limiting failure

Consider the compactly supported limiting density
\[
 g(u)=e^{-u}\mathbf 1_{[0,8]}(u).                              \tag{7}
\]
It is used only to obtain an exact sign certificate.  Its normalized
moments are
\[
 a_p=1-qS_p,\qquad
 q=e^{-8},\qquad S_p=\sum_{j=0}^p{8^j\over j!}.                \tag{8}
\]
The exponential series gives the entirely rational enclosure
\[
 {1\over2981}<e^{-8}<{1\over2980}.                            \tag{9}
\]
For completeness, summing through degree \(19\) gives
\[
 \sum_{j=0}^{19}{8^j\over j!}>2980,
 \qquad
 \sum_{j=0}^{19}{8^j\over j!}
 +{8^{20}\over20!}{1\over1-8/21}<2981,                        \tag{10}
\]
which proves (9).

Put \(r_j=a_{2j+2}/a_{2j}\) and \(d_j=r_j-r_{j+1}\).  Each
\[
 r_j(q)={1-qS_{2j+2}\over1-qS_{2j}}                            \tag{11}
\]
is decreasing in \(q\).  Substitution of the two rational endpoints in
(9), followed only by rational arithmetic, gives the safe enclosures
\[
 \begin{array}{c|c}
 \text{quantity}&\text{enclosure}\\ \hline
 r_0&[2939/2979,\ 147/149]\\
 d_0&[53752/729855,\ 32266/437911]\\
 d_1&[13336832/88743105,\ 889792/5916015].
 \end{array}                                                    \tag{12}
\]
In particular \(d_1>d_0>0\) throughout these intervals.  Bounding the
positive first term of (4) from above and the subtracted term from below
therefore yields
\[
 \begin{aligned}
 B_0(g)
 &\le {32266\over437911}
 \left({32266\over437911}+{889792\over5916015}\right)^2\\
 &\quad-{2939\over2979}
 \left({13336832\over88743105}-{32266\over437911}\right)^2\\
 &=-{8237226940150242027080423222262827228
 \over3942136335893843369593422516996966669525}<0.             \tag{13}
 \end{aligned}
\]
Thus the central cubic gate fails at \(N=0\), with no floating-point or
unproved asymptotic step.  Its approximate value is \(-0.002104\), but the
rational inequality (13) is the proof.

## 3. Smooth strict-convex-hazard approximation

The discontinuous endpoint in (7) is not part of the claim.  Let
\(\sigma(t)=(1+e^{-t})^{-1}\), and define, for \(A,\varepsilon>0\),
\[
 \begin{aligned}
 h_{A,\varepsilon}(u)
 &=1+A\varepsilon\log\bigl(1+e^{(u-8)/\varepsilon}\bigr),\\
 V_{A,\varepsilon}(u)&=\int_0^u h_{A,\varepsilon}(t)\,dt,\\
 f_{A,\varepsilon}(u)&=e^{-V_{A,\varepsilon}(u)}.             \tag{14}
 \end{aligned}
\]
These are smooth positive densities (normalization is immaterial), and
\[
 h'_{A,\varepsilon}(u)=A\sigma((u-8)/\varepsilon)>0,
 \qquad
 h''_{A,\varepsilon}(u)
 ={A\over\varepsilon}\sigma((u-8)/\varepsilon)
 \bigl(1-\sigma((u-8)/\varepsilon)\bigr)>0.                  \tag{15}
\]
They are decreasing and have Gaussian tails.

For fixed \(A\), as \(\varepsilon\downarrow0\), the potentials converge
pointwise to
\[
 V_A(u)=u+{A\over2}(u-8)_+^2.                                  \tag{16}
\]
Then, as \(A\to\infty\), \(e^{-V_A(u)}\) converges pointwise to \(g(u)\).
All of these densities are dominated by \(e^{-u}\), so dominated
convergence applies to every moment needed in \(B_0\).  Since (13) is a
strict inequality and \(B_0\) is continuous in the finite list of positive
moments \(m_0,m_2,m_4,m_6\), there are finite \(A\) and positive
\(\varepsilon\) for which
\[
 B_0(f_{A,\varepsilon})<0.                                    \tag{17}
\]
Together with (15), this is the promised smooth counterexample satisfying
all three sign conditions in (1).

## 4. Consequence for the theta route

The hypothesis
\[
 f\ \text{decreasing},\qquad h\ \text{increasing and convex}
\]
proves PF\(_2\) through (5), and supplies the positive triple determinant
(6), but it does **not** prove the cubic Jensen inequality (4).  Therefore
the statement proposed in the work-order is false, and cannot yield RH.

For the actual theta density, a viable next theorem would need a
theta-specific quantitative relation among the five successive tilted
covariances entering (3), or an identity using data beyond the sign of the
divided difference (6).  A mere proof that
\(-(\log\Phi)'''=h''\ge0\), even if true, would not close the cubic gate.
