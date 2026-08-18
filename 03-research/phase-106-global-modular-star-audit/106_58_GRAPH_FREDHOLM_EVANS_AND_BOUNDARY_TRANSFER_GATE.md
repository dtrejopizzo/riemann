# 106.58 — Graph-Fredholm Evans reduction and the boundary-transfer gate

## Purpose

Document 106.46 proposed a Fredholm pair of left and right Cauchy-data
spaces in the crossing-edge Hilbert space.  The essential-threshold theorem
of 106.47 is already sufficient to prove a precise Fredholm statement, but
first in the graph domain of the full operator.  This note proves that
statement, constructs the resulting finite-dimensional local Evans
determinant, and identifies exactly what is still needed to transport it to
the raw crossing-edge space.

The outcome is twofold.

1.  Below \(1/2\), the global matching problem is an analytic Fredholm
    problem and therefore has a rigorous finite-dimensional local Evans
    determinant.
2.  The raw crossing-edge space of 106.46 is too large: endpoint-compatible
    traces have infinite codimension in it, so the Cauchy pair is not
    Fredholm there. After replacing it by the compatible trace range, one
    still needs a two-sided graph-to-edge estimate. Even after that
    correction, nonvanishing is exactly the ordinary-prime--Gamma cluster
    current inequality of 106.49.

Thus this note closes the abstract Fredholm part without attributing a sign
to the arithmetic determinant.

## 1. The full operator below the threshold

Let

\[
 \mathcal H=L^2(\mu_K),
 \qquad L=L^*\ge0.                                   \tag{1}
\]

### Lemma 0 — The essential floor is parity-free

The conclusion of 106.47,

\[
 \sigma_{\rm ess}(L)\cap(0,1/2)=\varnothing,         \tag{1a}
\]

holds on the full space, not only on its even part.

#### Proof

The local Gamma estimate of 106.47(2)--(7) has no parity input. For the
tail estimate, fix the central interval used in the moving-PNT quadrature.
If \(f\) is supported outside a sufficiently large symmetric interval,
then \(f=0\) on that central interval. On the positive tail retain only
the backward prime edges \(y=x-\log n\) landing in the central interval.
Exactly the calculation of 106.47(12)--(15) gives

\[
 \mathscr E_p(f\mathbf1_{(R,\infty)})
 \ge(1/2-\varepsilon)
 \|f\mathbf1_{(R,\infty)}\|^2.                       \tag{1b}
\]

On the negative tail retain only the forward edges
\(y=x+\log n\) landing in the same interval. Reflection \(x\mapsto-x\)
and evenness of \(K\) give the identical estimate there. The two retained
edge families are disjoint and the omitted prime and Gamma energies are
nonnegative, so their sum proves the full tail floor. The nonlocal IMS
argument of 106.47(18)--(19), which is also parity-free, now proves (1a).
\(\square\)

The constant mode is a finite-dimensional zero eigenspace, and the exact
radical is contained in the \(1/2\)-eigenspace by 106.41(10). Neither
affects Fredholmness at a parameter strictly between \(0\) and \(1/2\).
The essential-threshold theorem therefore gives

\[
 \sigma_{\rm ess}(L)\cap(0,1/2)=\varnothing.         \tag{2}
\]

Fix a compact interval \(J\Subset(0,1/2)\), and write

\[
 A(z)=L-z:\mathcal X\longrightarrow\mathcal H,
 \qquad \mathcal X=D(L)                              \tag{3}
\]

with the graph norm. For every \(z\in J\), \(A(z)\) is a bounded
Fredholm map of index zero.  Its kernel is the finite-dimensional global
bound-state space at \(z\). Every such bound state is automatically
orthogonal to the constant and radical modes, by self-adjointness and the
distinct eigenvalues \(0,z,1/2\). Thus using the full operator here loses
none of the shorted spectral information and, crucially, preserves the
literal spatial decomposition used below.

## 2. A graph-domain Cauchy pair

Let

\[
 \mathcal H=\mathcal H_-\oplus\mathcal H_+,
 \qquad
 \mathcal H_-=L^2(( -\infty,X],\mu_K),\quad
 \mathcal H_+=L^2((X,\infty),\mu_K),                  \tag{4}
\]

and let χ_± be the two spatial projections.  Define

\[
\begin{aligned}
 \mathcal C_X^-(z)&=\{u\in\mathcal X:\chi_-A(z)u=0\},\\
 \mathcal C_X^+(z)&=\{u\in\mathcal X:\chi_+A(z)u=0\}.
                                                               \tag{5}
\end{aligned}
\]

Thus i) \(\mathcal C_X^-(z)\) consists of functions satisfying the
equation on the left half-line, with the whole right half-line retained as
nonlocal exterior data, and ii) \(\mathcal C_X^+(z)\) is the analogous
right solution space.  No local boundary approximation has been made.

### Theorem 1 — The graph Cauchy pair is Fredholm

For every \(z\in J\),

\[
 \boxed{(\mathcal C_X^-(z),\mathcal C_X^+(z))
        \text{ is a Fredholm pair in }\mathcal X.}    \tag{6}
\]

Moreover,

\[
 \boxed{\mathcal C_X^-(z)\cap\mathcal C_X^+(z)
       =\ker(L-z).}                                  \tag{7}
\]

The assertion is locally uniform in \(z\in J\).

#### Proof

We use a general elementary lemma. Let \(T:X\to Y_1\oplus Y_2\) be a
Fredholm operator and put

\[
 C_1=\ker(\pi_1T),\qquad C_2=\ker(\pi_2T).           \tag{8}
\]

Let \(R=\operatorname {ran}T\), which is closed and has finite codimension.
Plainly \(C_1\cap C_2=\ker T\), hence the intersection is finite
dimensional.

Let \(Q:Y_1\oplus Y_2\to(Y_1\oplus Y_2)/R\) be the quotient map and define

\[
 \delta:R\longrightarrow (Y_1\oplus Y_2)/R,
 \qquad \delta(y)=Q\pi_1y.                           \tag{9}
\]

Because \(Qy=0\) for \(y\in R\), one also has
\(Q\pi_2y=-\delta(y)\). Consequently

\[
 \ker\delta=(R\cap Y_1)+(R\cap Y_2).               \tag{10}
\]

Indeed, one inclusion is immediate. Conversely, if
\(Q\pi_1y=0\), then both \(\pi_1y\) and \(\pi_2y\) belong to \(R\), giving
the decomposition in (10). Since the target of \(\delta\) is finite
dimensional, \(\ker\delta\) is closed and finite-codimensional in \(R\).

Taking inverse images under \(T\) gives

\[
 T^{-1}(\ker\delta)=C_1+C_2.                         \tag{11}
\]

To see the reverse inclusion in (11), write
\(Tu=y_1+y_2\) with \(y_i\in R\cap Y_i\), lift each \(y_i\) through \(T\),
and absorb the resulting element of \(\ker T\subset C_1\cap C_2\).
Therefore \(C_1+C_2\) is closed and finite-codimensional in \(X\). This
proves that \((C_1,C_2)\) is a Fredholm pair.

Apply the lemma to \(T=A(z)\), \(Y_1=\mathcal H_-\), and
\(Y_2=\mathcal H_+\). Equation (7) follows directly from (5).
Fredholmness is stable under the norm-continuous perturbation
\(A(z)-A(z_0)=(z_0-z)I:\mathcal X\to\mathcal H\), proving local
uniformity.  \(\square\)

The theorem is genuinely nonlocal: the exterior half-line is part of the
data.  It does not replace the infinitely many crossing prime-power edges
or the Gamma continuum by a finite boundary vector.

## 3. The local Evans determinant

Let \(\Gamma\) be a finite union of positively oriented contours contained
in \(\{0<\Re z<1/2\}\), disjoint from the spectrum, and enclosing a compact
subinterval of \(J\). Put

\[
 P_\Gamma=\frac1{2\pi i}\int_\Gamma(z-L)^{-1}\,dz.  \tag{12}
\]

By (2), \(P_\Gamma\) has finite rank. Let \(R\) denote reflection, put
\(P_+=(I+R)/2\), and set \(P_\Gamma^+=P_+P_\Gamma\). The finite-dimensional
function

\[
 \boxed{
 D_\Gamma^+(z)=
 \det_{P_\Gamma^+\mathcal H}
 \bigl(P_\Gamma^+(L-z)P_\Gamma^+\bigr)}             \tag{13}
\]

is the even local Evans determinant relevant to the Riemann-kernel
problem. If the even eigenvalues inside \(\Gamma\), repeated with
multiplicity, are \(\lambda_1,\ldots,\lambda_m\), then

\[
 D_\Gamma^+(z)=\prod_{j=1}^m(\lambda_j-z).          \tag{14}
\]

Hence its zeros, with their orders, are exactly the even global
subthreshold states. Formula (13) is also the effective Hamiltonian
determinant of a parity-reduced Grushin completion of \(A(z)\); changing the
completion multiplies it by a nonvanishing analytic factor.

This construction needs no Schatten hypothesis on the raw boundary
projections.  It is the canonical finite-dimensional determinant supplied
by Theorem 1 and the essential-threshold theorem.

## 4. Exact arithmetic sign of the determinant

Let \(P=P_\Gamma^+\), and assume \(\Gamma\) encloses only eigenvalues in
\((0,1/2)\). Then

\[
\begin{aligned}
 \mathfrak T(P)
 &:=\operatorname {Tr}\left(P(L^2-\tfrac12L)\right)\\
 &=\sum_{j=1}^m\lambda_j(\lambda_j-\tfrac12).        \tag{15}
\end{aligned}
\]

Therefore

\[
 \boxed{P=0\quad\Longleftrightarrow\quad
        \mathfrak T(P)\ge0.}                        \tag{16}
\]

The right side of (16) has the exact ordinary-prime--Gamma representation
of 106.49.  If

\[
 \mathbf Q(x)=(q_1(x),\ldots,q_m(x))
\]

is an orthonormal eigenfeature for \(P\), and

\[
\begin{aligned}
 \mathbf B_P(x)=\int_0^\infty\{&K(x-u)
 [\mathbf Q(x)-\mathbf Q(x-u)]\\
 &+K(x+u)[\mathbf Q(x)-\mathbf Q(x+u)]\}
 \,d\nu_\zeta(u),                                  \tag{17}
\end{aligned}
\]

where

\[
 d\nu_\zeta(u)=
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(du)
 +\frac{e^{-u/2}}{1-e^{-2u}}\,du,                   \tag{18}
\]

then

\[
\boxed{
\begin{aligned}
 \mathfrak T(P)=&\ c_K\int_{\mathbb R}\frac{K(x)}{h(x)}
                  \|\mathbf B_P(x)\|^2\,dx\\
 &-\frac12\int_0^\infty\int_{\mathbb R}
 K(x)K(x-u)\|\mathbf Q(x)-\mathbf Q(x-u)\|^2
 \,dx\,d\nu_\zeta(u).                             \tag{19}
\end{aligned}}
\]

Thus nonvanishing of every local Evans determinant in the subthreshold
strip is equivalent to the one signed coherence inequality

\[
\boxed{
 c_K\int\frac K h\|\mathbf B_P\|^2
 \ge\frac12\int\!\!\int
 K(x)K(x-u)\|\Delta_u\mathbf Q(x)\|^2
 \,dx\,d\nu_\zeta(u).}                            \tag{20}
\]

Formula (20) keeps every ordinary von Mangoldt atom, the complete Gamma
channel, the theta positions, and the polar normalization in one identity.
It is also exactly the projection-alignment theorem left open in 106.49.

## 5. The raw edge space is too large

The crossing-edge trace of 106.46 is

\[
 \Gamma_Xu=(u(x),u(y))_{x\le X<y}
 \in\mathscr B_X\oplus\mathscr B_X.                 \tag{21}
\]

There is an algebraic obstruction to using the whole space on the right of
(21), independently of any trace estimate.

### Theorem 2 — The raw crossing-edge pair is not Fredholm

The sum of the traces of any two vertex-function spaces has infinite
codimension in
\(\mathscr B_X\oplus\mathscr B_X\). In particular, the Cauchy-data pair of
106.46, interpreted literally in that ambient space, cannot be a Fredholm
pair.

#### Proof

Choose \(\delta>0\) and the two intervals

\[
 A=[X-2\delta,X-\delta],\qquad
 B=[X+\delta,X+2\delta].                              \tag{22}
\]

On \(A\times B\), the Gamma part of the crossing-edge measure has the
strictly positive smooth density

\[
 \frac12K(x)K(y)
 \frac{e^{-(y-x)/2}}{1-e^{-2(y-x)}}\,dx\,dy.          \tag{23}
\]

It is bounded above and below by positive constants there. Hence the
restriction of \(\mathscr B_X\) to this rectangle is isomorphic to
\(L^2(A\times B)\).

For every vertex function \(u\), the first component of \(\Gamma_Xu\)
restricted to the rectangle depends only on \(x\), and the second depends
only on \(y\). The same remains true after adding traces from the left and
right solution spaces. Thus their sum is contained in

\[
 \{a(x):a\in L^2(A)\}\oplus\{b(y):b\in L^2(B)\}.     \tag{24}
\]

The orthogonal complement of (24) is infinite dimensional. For example,
choose orthonormal zero-mean families \((a_j)\) in \(L^2(A)\) and
\((b_k)\) in \(L^2(B)\); the products \(a_j(x)b_k(y)\) give infinitely
many independent directions orthogonal to all endpoint-only data.
Therefore the sum of the two Cauchy-data spaces has infinite codimension
in the raw edge space, which excludes the Fredholm-pair property.
\(\square\)

The correct boundary ambient space is consequently the compatible vertex
trace space

\[
 \mathscr T_X=
 \overline{\{\Gamma_Xu:u\in D(L)\}}
 \subset\mathscr B_X\oplus\mathscr B_X,              \tag{25}
\]

equipped either with its quotient graph norm or with an equivalent
intrinsic trace norm. To identify the graph pair of Theorem 1 with a closed
Fredholm pair in \(\mathscr T_X\), one needs a two-sided estimate of the
following type, separately on the two half-line solution spaces:

\[
\boxed{
 \|u\|_{D(L)}
 \le C_J\bigl(\|\Gamma_Xu\|_{\mathscr B_X\oplus\mathscr B_X}
             +\|\chi_\mp A(z)u\|_{\mathcal H}\bigr),
 \qquad z\in J.}                                    \tag{26}
\]

together with closed range (or an equivalent parametrix modulo compact
operators). Estimate (26) is not a consequence of total crossing mass:
the prime part of the crossing operator contains partial translations on
whole intervals, and exact radical shorting does not commute with spatial
cutoff.

Consequently a scalar determinant formed directly from

\[
 P_{\mathscr S_X^-(z)}-P_{\mathscr S_X^+(z)}        \tag{27}
\]

inside the compatible trace space still requires a Schatten or
determinant-line comparison theorem. The
graph determinant (13) exists without it, and any correctly normalized
boundary determinant must have exactly the same zero divisor as (13).

## 6. Final gate

The abstract half-line Fredholm issue and the arithmetic sign issue are
distinct:

* The graph-domain pair is Fredholm by Theorem 1.
* A finite-dimensional local Evans determinant exists by (13).
* The raw crossing-edge pair is not Fredholm; the ambient space must first
  be replaced by the compatible trace space (25).
* Transport to compatible Calderon projections requires (26).
* Nonvanishing, in either realization, is equivalent to (20).

In particular, boundary regularization cannot by itself supply the missing
sign.  The exact sign still required is the lower coherence of the joint
ordinary-prime--Gamma star current over its full increment dispersion.
No termwise positivity of \(j_2\), no finite crossing-mass estimate, and no
choice of Evans normalization proves (20).
