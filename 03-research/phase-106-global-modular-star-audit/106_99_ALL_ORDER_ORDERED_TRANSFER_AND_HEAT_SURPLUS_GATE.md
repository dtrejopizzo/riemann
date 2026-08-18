# 106.99 — All-order ordered transfer and the heat-surplus gate

## 1. Decision

The heat-core theorem removes the form-domain and exhaustion problem, but it
does not supply the physical sign.  This note tests the strongest natural
successor to the second-order identity

\[
 \Lambda_2=\partial\Lambda+\Lambda*\Lambda\geq0:
\]

retain the complete generalized-von-Mangoldt hierarchy, lift it to the
physical theta sandwich before taking a limit, and resum every intermediate
position.

The calculation has a definitive outcome.

1.  The scalar all-order hierarchy is exact and nonnegative, but it was
    already obtained in `104_16_JORDAN_COCYCLE_ATTACK.md`.
2.  The physical lift is an ordered noncommutative Bell hierarchy.  Every
    intermediate step carries the multiplier \(M_{\eta^2}\).
3.  The primitive-minus-physical defect is a positive square at order two,
    but is already indefinite at order three.
4.  The complete resolvent can be resummed.  Operator Jensen gives an exact
    comparison, but it is an upper comparison, whereas the physical surplus
    requires a lower comparison.
5.  Letting the arithmetic order grow does not cross the critical line.  In
    the absolute-convergence half-plane the hierarchy concentrates
    exponentially on the pole term.
6.  Heat regularization, positivity improvement, exact mean periodicity and
    an exact threshold radical can coexist with a subthreshold state.  A
    four-state rational model proves this simultaneously.

Thus this attack does not prove the heat/hybrid physical surplus.  It does
identify the weakest remaining cofinal statement without imposing an
unnecessary strict inequality on every row.

## 2. Exact finite-row target

After the finite radical has been anti-shorted, use the notation of
`106_89_RADICAL_CONDITIONED_ADAPTIVE_GAIN.md`:

\[
 z=\Pi V_Xq^*,\qquad
 B=\bar U\widehat A^{-1}\bar U^*,
\]

and

\[
 G=\langle z,(I+B)^{-1}z\rangle,
 \qquad
 \delta=-\left(\widehat h-\widehat c^*
                    \widehat A^{-1}\widehat c\right)>0.
 \tag{1}
\]

The completed Schur pivot is exactly

\[
 \boxed{\sigma_\infty=G-\delta.}                   \tag{2}
\]

For a finite augmented response block,

\[
 G_Y=\frac{\tau_{d+1}(Y)}{\tau_d(Y)}\uparrow G,
 \tag{3}
\]

and its Krylov lower bounds satisfy

\[
 Q_1(Y)\le Q_2(Y)\le\cdots\uparrow G_Y.             \tag{4}
\]

The rowwise strict target is \(G>\delta\).  The exact global form identity is

\[
 \boxed{G-\delta
 =\mathcal A_\infty(F_\infty,F_\infty),}             \tag{5}
\]

where \(F_\infty\) is the completed regression residual.  Consequently a
proof of (2) on a form core is the completed Weil sign, not a preliminary
matrix estimate.

## 3. The complete arithmetic hierarchy

Let \(\partial f(n)=(\log n)f(n)\), and let \(*\) denote Dirichlet
convolution.  Define

\[
 \Lambda_k=\mu*(\log)^k,
 \qquad \Lambda_0=\varepsilon,
 \qquad \Lambda_1=\Lambda.                           \tag{6}
\]

The convolution derivation gives

\[
 \boxed{\Lambda_{k+1}=\partial\Lambda_k+
                         \Lambda*\Lambda_k.}         \tag{7}
\]

In particular,

\[
 \Lambda_2=\partial\Lambda+\Lambda*\Lambda,
\]

and

\[
 \Lambda_3=\partial^2\Lambda
 +3\Lambda*\partial\Lambda+\Lambda^{*3}.            \tag{8}
\]

For every \(u\ge0\),

\[
 \boxed{
 \sum_{k\ge0}\Lambda_k(n)\frac{u^k}{k!}
 =\sum_{d\mid n}\mu(d)(n/d)^u
 =n^u\prod_{p\mid n}(1-p^{-u})\ge0.}               \tag{9}
\]

Hence every \(\Lambda_k(n)\) is nonnegative.  In the half-plane of absolute
convergence,

\[
 \boxed{
 \sum_{k\ge0}\frac{u^k}{k!}
  \sum_{n\ge1}\frac{\Lambda_k(n)}{n^s}
 =\frac{\zeta(s-u)}{\zeta(s)}.}                    \tag{10}
\]

Equivalently,

\[
 \sum_{k\ge0}\Lambda_k\frac{u^k}{k!}
 =\exp_*
 \left(\sum_{r\ge1}\frac{u^r}{r!}
                         \partial^{r-1}\Lambda\right). \tag{11}
\]

For completeness, positivity of the Taylor coefficients in (9) is not
being inferred merely from positivity of the function for \(u\geq0\).
It has the following direct finite-difference proof.  If

\[
 n=\prod_{i=1}^r p_i^{a_i},qquad
 x=\log n,qquad h_i=\log p_i,
\]

then

\[
 \Lambda_k(n)=
 \sum_{S\subset\{1,\ldots,r\}}(-1)^{|S|}
 \left(x-\sum_{i\in S}h_i\right)^k.                \tag{11a}
\]

Repeated use of

\[
 f(y)-f(y-h)=\int_0^h f'(y-t)\,dt
\]

gives, when \(r\leq k\),

\[
 \boxed{
 \Lambda_k(n)=\frac{k!}{(k-r)!}
 \int_0^{h_1}\!\cdots\!\int_0^{h_r}
 (x-t_1-\cdots-t_r)^{k-r}\,dt_1\cdots dt_r\geq0.}
 \tag{11b}
\]

Here \(x-t_1-\cdots-t_r\geq
\log n-\sum_{p\mid n}\log p\geq0\).  If \(r>k\), the same repeated
difference annihilates the degree-\(k\) polynomial.  Consequently

\[
 0\leq\Lambda_k(n)\leq(\log n)^k,
 \qquad \Lambda_k(n)=0\quad\text{when }\omega(n)>k, \tag{11c}
\]

and on one prime tower

\[
 \Lambda_k(p^a)=(\log p)^k\{a^k-(a-1)^k\}.          \tag{11d}
\]

Equations (6)--(11d) are arithmetic infrastructure.  Their abstract
positivity is not a Riemann-specific sign theorem: Section 6 of `104_16`
constructs a completed symmetric divisor with off-line zeros and two full
positive Jordan cocycles.

## 4. The physical ordered hierarchy

Put

\[
 E=M_\eta,\qquad M=E^2=M_{\eta^2},qquad 0<M<I.
 \tag{12}
\]

A primitive \(k\)-fold translation collapses every factorization to its
endpoint:

\[
 E S_{\ell_1+\cdots+\ell_k}E.
\]

The physical path retains every intermediate theta position:

\[
 \boxed{
 E S_{\ell_1}M S_{\ell_2}M\cdots M S_{\ell_k}E.}    \tag{13}
\]

For arbitrary factors \(A_1,\ldots,A_k\), telescoping gives the exact
identity

\[
\begin{aligned}
 &EA_1\cdots A_kE-EA_1MA_2M\cdots MA_kE\\
 &\quad=\sum_{j=1}^{k-1}
 EA_1M\cdots MA_j(I-M)A_{j+1}\cdots A_kE.
                                                               \tag{14}
\end{aligned}
\]

At order two, with adjoint factors, (14) is the positive square of 106.54:

\[
 EH^2E-(EHE)^2
 =EH(I-M)HE
 =\{(I-M)^{1/2}HE\}^*\{(I-M)^{1/2}HE\}\ge0.        \tag{15}
\]

There is no corresponding sign for the individual terms of (14) at higher
order.

To record the coefficient recurrence, put

\[
 A_r=\sum_n\frac{\partial^{r-1}\Lambda(n)}{\sqrt n}
                    S_{\log n},
 \qquad \mathfrak dA_r=A_{r+1},
 \qquad \mathfrak dM=0.                            \tag{16}
\]

The one-sided physical Bell operators obey

\[
 \boxed{P_1=A_1,\qquad
        P_{k+1}=\mathfrak dP_k+A_1MP_k.}             \tag{17}
\]

Thus

\[
 P_2=A_2+A_1MA_1,
\]

and

\[
 P_3=A_3+A_2MA_1+2A_1MA_2+A_1MA_1MA_1.             \tag{18}
\]

Replacing every \(M\) by \(I\) recovers the primitive Bell hierarchy.
The full physical expression must also retain the opposite orientations,
the prime--Gamma and Gamma--Gamma words, the pole threshold and the radical
projection at a common finite cutoff.

## 5. Order three has no Loewner sign

The loss of sign in (14) is not a domain or convergence issue.  Take

\[
 E=\begin{pmatrix}1/2&0\\0&3/4\end{pmatrix},
 \qquad
 H=\begin{pmatrix}2&3\\3&5\end{pmatrix}>0.          \tag{19}
\]

Direct rational multiplication gives

\[
 D:=EH^3E-(EHE)^3
 =\begin{pmatrix}
 17715/1024&85635/2048\\
 85635/2048&413955/4096
 \end{pmatrix}.                                     \tag{20}
\]

But

\[
 \boxed{\det D=-\frac{8775}{262144}<0.}             \tag{21}
\]

Therefore \(D\) is indefinite even though \(H>0\) and \(0<E<I\).
The second-order square cannot be iterated coefficient by coefficient.

## 6. Exact all-order resolvent comparison

There is a valid all-order comparison, but it has the upper direction.
Let \(A=A^*\), \(C=C^*\), \(0\le C^2\le I\), and assume
\(I-rA>0\).  Define

\[
 D=(I-C^2)^{1/2},
 \qquad Vx=(Cx,Dx),
 \qquad X=\operatorname{diag}(A,0).
\]

Then \(V\) is an isometry and \(V^*XV=CAC\).  Since
\(f(t)=(1-rt)^{-1}\) is operator convex on the resolvent interval,
operator Jensen gives

\[
 \boxed{
 (I-rCAC)^{-1}
 \preceq C(I-rA)^{-1}C+I-C^2.}                     \tag{22}
\]

Expanding at \(r=0\) shows that (22) is the resummed analogue of (15).
It bounds the physical ordered walk from above.  The gain in (1), however,
requires a lower bound for an inverse quadratic form.

The old-mode adaptation itself has the exact bounded resummation

\[
 \boxed{
 \mathcal R_A
 =\mathcal R^{1/2}
 \left(I+\mathcal R^{1/2}\Phi A^{-1}\Phi^*
                      \mathcal R^{1/2}\right)^{-1}
 \mathcal R^{1/2},}                                  \tag{23}
\]

and

\[
 G=\langle q^*,\mathcal R_Aq^*\rangle,
 \qquad 0\preceq\mathcal R_A\preceq\mathcal R.     \tag{24}
\]

Again, (24) is a contraction in the wrong direction.  The scalar data

\[
 A=1,qquad U=\sqrt3,qquad z=1,qquad\delta=\frac12
\]

satisfy every resolvent contraction above, while

\[
 B=3,qquad G=(1+B)^{-1}=\frac14<\frac12=\delta.     \tag{25}
\]

Thus the missing comparison with \(\delta\) is not contained in resolvent
convexity.

## 7. Growing arithmetic order remains in the pole half-plane

For \(\sigma>1\), put

\[
 F_k(\sigma)=\sum_{n\ge1}\frac{\Lambda_k(n)}{n^\sigma}
 =\frac{(-1)^k\zeta^{(k)}(\sigma)}{\zeta(\sigma)}.
 \tag{26}
\]

Multiplication by \(\zeta(\sigma)\) gives the exact positive series

\[
 \zeta(\sigma)F_k(\sigma)
 =\sum_{n\ge1}\frac{(\log n)^k}{n^\sigma}.          \tag{27}
\]

### Proposition 1 — Uniform high-order pole asymptotic

For every integer \(k\ge1\) and every \(\sigma>1\),

\[
 \boxed{
 \left|\zeta(\sigma)F_k(\sigma)
       -\frac{k!}{(\sigma-1)^{k+1}}\right|
 \le2\left(\frac{k}{e\sigma}\right)^k.}           \tag{28}
\]

#### Proof

The function

\[
 f(x)=(\log x)^kx^{-\sigma},\qquad x\ge1,
\]

is nonnegative and unimodal, with maximum at
\(x=e^{k/\sigma}\) and

\[
 \max f=\left(\frac{k}{e\sigma}\right)^k.
\]

For a nonnegative unimodal function, comparison of the increasing and
decreasing pieces with their unit-interval integrals gives

\[
 \left|\sum_{n\ge1}f(n)-\int_1^\infty f(x)\,dx\right|
 \le2\max f.                                        \tag{29}
\]

Finally, the change of variable \(y=\log x\) gives

\[
 \int_1^\infty(\log x)^kx^{-\sigma}\,dx
 =\int_0^\infty y^ke^{-(\sigma-1)y}\,dy
 =\frac{k!}{(\sigma-1)^{k+1}}.
\]

Equations (27)--(29) prove (28). \(\square\)

Stirling's formula shows that the relative error in (28) decays like

\[
 O_\sigma\left(k^{-1/2}
   \left(\frac{\sigma-1}{\sigma}\right)^k\right).  \tag{30}
\]

Thus growing order makes the safe-half-plane hierarchy concentrate on the
pole at \(s=1\).  It does not propagate positivity to \(\Re s=1/2\).  At
the physical cutoff one has only the elementary estimate

\[
 \sum_{n\le X}\frac{\Lambda_k(n)}{\sqrt n}
 \le2\sqrt X(\log X)^k.                             \tag{31}
\]

No threshold sign follows from (31).

## 8. A four-state heat/mean-periodic countermodel

The failure of an abstract heat argument can be made simultaneous with
mean periodicity and an exact threshold radical.

Work on \(\mathbb Z/4\mathbb Z\), and put

\[
 K=(2,1,2,1),
 \qquad \mu=K/6,
 \qquad r=\Delta K/K=(1,-2,1,-2),                  \tag{32}
\]

where \(\Delta f(j)=2f(j)-f(j-1)-f(j+1)\).  The cyclic Fourier transform
is

\[
 \widehat K=(6,0,2,0),
\]

so

\[
 \ker(F\mapsto F*K)
 =\operatorname{span}\{(1,0,-1,0),(0,1,0,-1)\}
 =(1\oplus\mathbb Rr)^\perp_{L^2(\mu)}.             \tag{33}
\]

Define

\[
 L=\begin{pmatrix}
 1/4&-1/12&-1/12&-1/12\\
 -1/6&1/3&-1/6&0\\
 -1/12&-1/12&1/4&-1/12\\
 -1/6&0&-1/6&1/3
 \end{pmatrix}.                                     \tag{34}
\]

The rows sum to zero, the off-diagonal entries are nonpositive, and

\[
 \mu_iL_{ij}=\mu_jL_{ji}.
\]

The graph is connected, so the Markov semigroup is positivity improving.
Direct multiplication gives

\[
 L1=0,
 \qquad Lr=\frac12r,                                \tag{35}
\]

while, for the two basis vectors in (33),

\[
 Lq_i=\frac13q_i.                                   \tag{36}
\]

Consequently

\[
 \boxed{
 (L-\tfrac12I)|_{\ker(*K)}=-\frac16I.}             \tag{37}
\]

This model contains a positive kernel, exact convolution mean periodicity,
a derivative-ratio threshold radical, reversibility, irreducibility and
heat regularization, yet it has a subthreshold state.  It does not model the
literal Riemann weights; its role is to prove that those abstract structures
cannot replace a quantitative ordinary-prime--Gamma estimate.

## 9. The weakest cofinal closure statement

Let \(H_M\) and \(N_M\) be respectively the completed signed Gram matrix and
the Hilbert Gram matrix on a nested heat or hybrid form core.  Define

\[
 \alpha_M=\left\|
   \left(N_M^{-1/2}H_MN_M^{-1/2}\right)_-
             \right\|.                              \tag{38}
\]

By the min--max principle, \(\alpha_M\) is nondecreasing with \(M\).
Therefore \(\alpha_M\to0\) would already force \(\alpha_M=0\) for every
row; heat smoothing cannot gradually erase a fixed negative mode.

Strict surplus on every row is nevertheless stronger than the finite
inertia argument needs.  The exact minimal target is one cofinal schedule
and one tolerance \(\eta_M\downarrow0\) such that

\[
 \boxed{
 \tau_{d+1}(Y_M)
 \ge(\delta_{M,J,X}-\eta_M)\tau_d(Y_M),}            \tag{39}
\]

with the simultaneous LDL/inertia ordering retained.  Equivalently, using
row-dependent Krylov depth,

\[
 \boxed{
 Q_{k(M)}(Y_M)
 \ge\delta_{M,J,X}-\eta_M.}                         \tag{40}
\]

Equality at the threshold is allowed.  If a fixed subthreshold state
exists, heat form-core approximation makes (39) fail by a fixed normalized
margin for all sufficiently large \(M\).  Hence (39) is both the weakest
cofinal formulation produced by the finite determinant machinery and a
faithful detector of the missing sign.

## 10. Status

Proved here:

* the exact physical ordered Bell recurrence;
* the failure of coefficientwise Loewner positivity at order three;
* the all-order operator-Jensen comparison and its direction;
* the uniform growing-order pole asymptotic;
* a rational heat/mean-periodic threshold countermodel;
* the vanishing-tolerance cofinal formulation.

Not proved here:

\[
 G\ge\delta
\]

for the literal ordinary-prime--Gamma heat/hybrid rows, or equivalently
(39) for one cofinal schedule.  The remaining theorem must use the exact
joint placement of the ordinary weights \(\Lambda(p^a)=\log p\), the Gamma
continuum and the pole after radical anti-shorting.  Scalar higher jets,
primitive resolvent convexity and heat regularization do not supply that
comparison.
