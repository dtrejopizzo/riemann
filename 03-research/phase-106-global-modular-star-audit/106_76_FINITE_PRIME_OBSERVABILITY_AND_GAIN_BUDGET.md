# 106.76 — Finite prime observability and the gain budget

## Purpose and conclusion

The mode--prime staircase has two logically different ingredients:

1. **observability:** the selected prime channels must distinguish every
   vector in the finite mode space;
2. **gain:** their weighted energy must be large enough to lift the Gamma
   deficit through the fixed level \(1/2\).

The first statement can be proved completely for the literal ordinary
prime channels.  In fact, on every finite elementary zero-mode space, one
single displacement atom is already a positive-definite observation
operator.  This remains true for nonreal zero orbits and multiplicity jets.
The proof is elementary: a vector invisible to one displacement would be
periodic, while every elementary quotient mode tends to zero at both ends.

This gives a constructive determinant lower bound and a uniform
observability constant on every compact displacement interval.  It also
gives a purely finite scalar sufficient condition for a staircase row to
close.  What it does **not** give automatically is the required gain.  The
literal prime weights form a convergent, rapidly attenuated bank, so full
rank and finite-dimensional level discretization do not force the total
gain to cross \(1/2\).

The exact force-bearing comparison is

\[
 \boxed{
 \lambda_{\max}\!\left(
 P_{M,\infty}^{-1/2}B_M P_{M,\infty}^{-1/2}
 \right)<1,}
 \tag{1}
\]

where \(P_{M,\infty}\) is the complete normalized ordinary-prime bank and
\(B_M\) is the normalized Gamma deficit.  Equation (1) is equivalent to a
strictly positive completed level on \(V_M\).  The new result below is that
neither rank, Vandermonde nonvanishing, nor lack of aliasing remains an
obstruction: only the quantitative gain comparison remains.

## 1. Elementary mode spaces and one displacement

Let

\[
 h(x)=\cosh(x/2),
 \qquad
 \chi_{z,k}(x)
 =\partial_z^k\!\left({\cos(zx)\over h(x)}\right),
 \qquad |\mathrm{Im}\,z|<\frac12.             \tag{2}
\]

Fix finitely many distinct zero-orbit representatives \(z\), retain the
required multiplicity jets, and let \(V\) be their span after removal of
the \(z\leftrightarrow-z\) duplication.  Write

\[
 \|q\|_K^2
 ={1\over c_K}\int_{\mathbb R}h(x)K(x)|q(x)|^2\,dx
 \tag{3}
\]

and, for \(u>0\),

\[
 \mathcal J_u(q)
 =\int_{\mathbb R}K(x)K(x-u)
       |q(x)-q(x-u)|^2\,dx.                       \tag{4}
\]

The Riemann theta kernel satisfies \(K(x)>0\) on the real line.

### Theorem 1 — One literal displacement observes every finite mode

For every \(u>0\),

\[
 \boxed{
 q\in V\setminus\{0\}
 \quad\Longrightarrow\quad
 \mathcal J_u(q)>0.}                              \tag{5}
\]

Consequently, if \(N_V\) and \(P_V(u)\) are respectively the norm Gram
matrix and the atom Gram matrix in any basis of \(V\), then

\[
 \boxed{
 P_V(u)\succ0,
 \qquad
 m_V(u):=\lambda_{\min}\!\left(
 N_V^{-1/2}P_V(u)N_V^{-1/2}\right)>0.}            \tag{6}
\]

#### Proof

Every function in \(V\) is real-analytic on the real axis.  Moreover, for
some \(b<1/2\) depending only on the finite mode set,

\[
 |q(x)|\le C_q(1+|x|)^d e^{-(1/2-b)|x|},           \tag{7}
\]

so \(q(x)\to0\) as \(x\to\pm\infty\).  If
\(\mathcal J_u(q)=0\), strict positivity of \(K(x)K(x-u)\) gives

\[
 q(x)=q(x-u)                                      \tag{8}
\]

almost everywhere.  Continuity extends (8) to every real \(x\).  Thus
\(q\) is \(u\)-periodic.  For fixed \(x\), iteration and (7) give

\[
 q(x)=q(x+nu)\longrightarrow0,
 \qquad n\to\infty.
\]

Hence \(q=0\), a contradiction.  The quadratic form (4) therefore has
trivial kernel on the finite-dimensional space \(V\), which proves (5)
and (6).  \(\square\)

The argument includes conjugate nonreal orbits and confluent jets.  It
uses only the strict strip margin \(|\mathrm{Im}\,z|<1/2\), not RH.

### Corollary 2 — Uniform finite-window observability

For every compact interval \(0<a\le u\le b<\infty\),

\[
 \boxed{
 m_V[a,b]:=\min_{u\in[a,b]}m_V(u)>0.}             \tag{9}
\]

#### Proof

On a compact \(u\)-interval, the theta decay and (7) give one integrable
majorant for every matrix entry of \(P_V(u)\).  Dominated convergence
makes \(P_V(u)\), and hence \(m_V(u)\), continuous.  Theorem 1 says that
this continuous function is strictly positive at every point of the
compact interval.  \(\square\)

Thus the question is not whether the literal logarithmic displacements
sample a finite mode space.  They do, with a genuine finite lower frame
constant.

## 2. Constructive determinant lower bounds

Let \(d=\dim V\), choose a basis
\(\phi_1,\ldots,\phi_d\), and put

\[
 f_{j,u}(x)=\phi_j(x)-\phi_j(x-u),
 \qquad a_u(x)=K(x)K(x-u).                        \tag{10}
\]

The atom matrix is the Gram matrix

\[
 P_V(u)_{ij}
 =\int_{\mathbb R}a_u(x)
       \overline{f_{i,u}(x)}f_{j,u}(x)\,dx.       \tag{11}
\]

### Theorem 3 — Andreief sampling formula

\[
 \boxed{
 \det P_V(u)
 ={1\over d!}\int_{\mathbb R^d}
 \left|\det[f_{j,u}(x_i)]_{i,j=1}^d\right|^2
 \prod_{i=1}^d a_u(x_i)\,dx_i.}                  \tag{12}
\]

In particular, there exist real sampling points
\(x_1,\ldots,x_d\) for which

\[
 \det[f_{j,u}(x_i)]\ne0.                          \tag{13}
\]

If boxes \(I_i\ni x_i\) are chosen so that the absolute value of this
determinant is at least \(\eta>0\) on
\(I_1\times\cdots\times I_d\), then

\[
 \boxed{
 \det P_V(u)
 \ge {\eta^2\over d!}
      \prod_{i=1}^d\int_{I_i}a_u(x)\,dx.}         \tag{14}
\]

#### Proof

Formula (12) is the Gram--Andreief identity applied to (11).  The
functions \(f_{j,u}\) are linearly independent: a linear relation would
give a nonzero \(q\in V\) with \(q(x)=q(x-u)\), contradicting Theorem 1.
Linear independence of continuous functions implies the existence of
points satisfying (13).  Continuity then supplies the boxes and the
positive number \(\eta\); restricting (12) to their product gives (14).
\(\square\)

Let

\[
 A_V(u)=N_V^{-1/2}P_V(u)N_V^{-1/2}.               \tag{15}
\]

For \(d\ge2\), the arithmetic--geometric mean inequality applied to all
eigenvalues except the least one gives the certified estimate

\[
 \boxed{
 m_V(u)
 \ge
 {(d-1)^{d-1}\det A_V(u)
  \over(\mathrm{tr}\,A_V(u))^{d-1}}.}        \tag{16}
\]

For \(d=1\), \(m_V(u)=\mathrm{tr}\,A_V(u)\).  Equations (14)--(16)
turn finite sampling into an explicit lower-frame certificate.  For the
elementary modes (2), the determinant in (13) is a confluent
trigonometric-exponential sampling determinant; no unproved global
Vandermonde assertion is needed.

## 3. The exact Gamma-versus-prime gain test

Return to \(V_M\), normalize by \(N_M\), and write

\[
 \begin{aligned}
 G_{\Gamma,M}
 &=N_M^{-1/2}\mathbf G_{\Gamma,M}N_M^{-1/2},\\
 B_M&={1\over2}I-G_{\Gamma,M},\\
 P_{M,X}
 &=\sum_{\substack{p^k\le X}}
 {\log p\over p^{k/2}}\,A_M(k\log p).
 \end{aligned}                                    \tag{17}
\]

Here \(A_M(u)\) is (15) on \(V_M\).  The normalized finite-head defect is

\[
 \widetilde H_{M,X}=P_{M,X}-B_M.                  \tag{18}
\]

Theorem 1 implies \(P_{M,X}\succ0\) as soon as \(X\ge2\).  Congruence by
\(P_{M,X}^{-1/2}\) therefore proves the following exact test.

### Theorem 4 — Finite gain criterion

\[
 \boxed{
 \widetilde H_{M,X}\succeq0
 \quad\Longleftrightarrow\quad
 \lambda_{\max}\!\left(
 P_{M,X}^{-1/2}B_M P_{M,X}^{-1/2}
 \right)\le1.}                                    \tag{19}
\]

A scalar sufficient condition is

\[
 \boxed{
 \sum_{p^k\le X}{\log p\over p^{k/2}}
       m_{V_M}(k\log p)
 \ge b_M,
 \qquad
 b_M:=\max\{0,\lambda_{\max}(B_M)\}.}            \tag{20}
\]

#### Proof

Equation (19) follows from

\[
 P_{M,X}-B_M\succeq0
 \quad\Longleftrightarrow\quad
 I-P_{M,X}^{-1/2}B_MP_{M,X}^{-1/2}\succeq0.
\]

By (6),

\[
 P_{M,X}\succeq
 \left(
 \sum_{p^k\le X}{\log p\over p^{k/2}}
 m_{V_M}(k\log p)
 \right)I.
\]

Also \(B_M\preceq b_M I\).  These two inequalities prove (20).  \(\square\)

Condition (20) is deliberately only sufficient.  The exact test (19)
retains the directional alignment between Gamma and the ordinary-prime
channels.

### Corollary 5 — The critical-coupling staircase

Assume that \(B_M\) has a positive direction and define

\[
 \vartheta_{M,X}
 :=\sup_{v\ne0}{\langle v,B_Mv\rangle
                    \over\langle v,P_{M,X}v\rangle}.
 \tag{20a}
\]

Whenever \(Y>X\) contains at least one new prime-power atom,

\[
 \boxed{\vartheta_{M,Y}<\vartheta_{M,X}.}          \tag{20b}
\]

Moreover,

\[
 \vartheta_{M,X}\longrightarrow
 \vartheta_{M,\infty}
 =\lambda_{\max}\!\left(
 P_{M,\infty}^{-1/2}B_MP_{M,\infty}^{-1/2}\right),
 \tag{20c}
\]

and the three possible staircase behaviors are exactly

\[
\boxed{
\begin{array}{c|c}
\vartheta_{M,\infty}<1 & X_*(M)<\infty,\\
\vartheta_{M,\infty}=1 & \vartheta_{M,X}>1
                         \text{ for every finite }X,\\
\vartheta_{M,\infty}>1 & X_*(M)=\infty.
\end{array}}                                       \tag{20d}
\]

If \(B_M\preceq0\), the row is already closed at the first nonempty head.

#### Proof

Theorem 1 makes every new atom positive definite.  Hence
\(\Delta P=P_{M,Y}-P_{M,X}\succ0\), and finite dimensionality gives

\[
 \Delta P\succeq c_{X,Y}P_{M,X}
\]

for some \(c_{X,Y}>0\).  On every vector with positive numerator in
(20a),

\[
 {\langle v,B_Mv\rangle\over\langle v,P_{M,Y}v\rangle}
 \le {1\over1+c_{X,Y}}\,
 {\langle v,B_Mv\rangle\over\langle v,P_{M,X}v\rangle}.
\]

Taking suprema proves (20b).  Norm convergence of \(P_{M,X}\) and
continuity of inversion on the positive-definite cone prove (20c).

If \(\vartheta_{M,\infty}<1\), convergence and (19) give a finite
crossing.  If \(\vartheta_{M,\infty}>1\), monotonicity prevents one.
Finally, when \(\vartheta_{M,\infty}=1\), let \(v_\infty\) be a maximizing
vector.  The omitted tail \(P_{M,\infty}-P_{M,X}\) is positive definite
at every finite head, so

\[
 \langle v_\infty,P_{M,X}v_\infty\rangle
 <\langle v_\infty,P_{M,\infty}v_\infty\rangle
 =\langle v_\infty,B_Mv_\infty\rangle.
\]

Thus \(\vartheta_{M,X}>1\) for every finite \(X\).  This proves (20d).
\(\square\)

The number \(\vartheta_{M,X}\) is the exact critical coupling of the
finite ordinary-prime bank.  Adding a prime lowers it strictly, but
discreteness alone does not determine whether its limiting value lies
below, at, or above one.

## 4. Why full rank does not force the \(1/2\) crossing

The literal theta localization proved in 106.73 gives, on every fixed
mode block,

\[
 \left\|{\log p\over\sqrt p}A_M(\log p)\right\|
 \ll_M(\log p)p^{2+b}e^{-2\pi p}.                 \tag{21}
\]

Thus the complete prime bank

\[
 P_{M,\infty}=\lim_{X\to\infty}P_{M,X}            \tag{22}
\]

exists in norm.  Every summand in it is positive definite by Theorem 1,
but its total gain is finite.

This distinction cannot be removed by level discretization.  Already in
one dimension, take \(B=1\) and positive sensor strengths

\[
 a_j={1\over4}\,2^{-j},\qquad j\ge1.              \tag{23}
\]

Every sensor is full rank, every partial head increases strictly, and the
tail tends to zero exponentially.  Nevertheless

\[
 \sum_{j\le J}a_j<\frac14<1=B                   \tag{24}
\]

for every finite \(J\), so the threshold is never crossed.  Replacing
\(2^{-j}\) by a normalized sequence of the form
\((\log p_j)p_j^2e^{-2\pi p_j}\) gives the same superexponentially
attenuated pattern as the large-prime bank.

The countermodel does not model the complete Riemann coupling.  Its role
is exact and limited: it proves that the implications

\[
 \text{discrete levels}+
 \text{full-rank prime sensors}+
 \text{vanishing tail}
 \quad\Longrightarrow\quad
 \text{finite threshold crossing}                 \tag{25}
\]

are false without a quantitative gain comparison.

## 5. The remaining cofinal inequality

Taking \(X\to\infty\) in (19), the strict completed gain condition is

\[
 \boxed{
 \Theta_M
 :=\lambda_{\max}\!\left(
 P_{M,\infty}^{-1/2}B_M P_{M,\infty}^{-1/2}
 \right)<1.}                                      \tag{26}
\]

It is equivalent to

\[
 P_{M,\infty}-B_M\succ0,                          \tag{27}
\]

which is precisely the strict completed quotient gap on \(V_M\).  If
(26) holds, norm convergence supplies a finite head, and the explicit
tail bound of 106.67 gives

\[
 X_*(M)
 \le {1\over c}\log {C_M\over\delta_M}           \tag{28}
\]

after replacing the right side by the next prime-power cutoff.

The finite lower-frame theorem therefore removes three possible
obstructions:

* no elementary mode is invisible to a literal prime displacement;
* no finite sampling-rank defect survives;
* no qualitative Vandermonde or aliasing hypothesis is missing.

The only remaining issue is quantitative: prove (26), or the stronger
but scalar condition

\[
 \boxed{
 \sum_{p^k}{\log p\over p^{k/2}}
       m_{V_M}(k\log p)>b_M,}                     \tag{29}
\]

for the ordinary von Mangoldt weights along the cofinal mode exhaustion.
Equation (29) is now a fully explicit determinant-and-integral target by
(12)--(16).  It is stronger than necessary because it discards directional
alignment; (26) is the sharp form.  It should not be promoted to the
cofinal target.  A double-precision diagnostic on the first real-zero
modes already shows why:

\[
\begin{array}{c|c|c|c}
\dim V_M&
b_M&
\sum_{p^k\le11}{\log p\over p^{k/2}}m_{V_M}(k\log p)&
\lambda_{\min}(P_{M,11}-B_M)\\ \hline
4&2.93\cdot10^{-2}&8.18\cdot10^{-4}&+6.40\cdot10^{-2}\\
10&2.40\cdot10^{-1}&1.38\cdot10^{-7}&+2.86\cdot10^{-3}
\end{array}
\tag{30}
\]

The numbers in (30) are diagnostics, not interval certificates.  Their
structural message is unambiguous: the joint bank can close a row even
when the sum of the individual least gains is orders of magnitude too
small.  The surviving mechanism is directional complementarity among
the prime channels and Gamma, exactly as retained by (26).

Accordingly, proving that every exact staircase frontier is finite is not
a remaining sampling or convergence problem.  It is exactly the strict
ordinary-prime gain inequality (26).  The compensated frontier replaces
\(<1\) by \(\le1\) plus a vanishing tolerance and is the appropriate form
when a completed threshold level is allowed.
