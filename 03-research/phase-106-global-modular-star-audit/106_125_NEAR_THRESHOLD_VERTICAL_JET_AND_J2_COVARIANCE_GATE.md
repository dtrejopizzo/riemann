# 106.125 — Near-threshold vertical jets and the covariant \(j_2\) gate

## 1. Purpose and verdict

Document 106.120 identifies the weakest possible off-line obstruction.  If
an off-line orbit is written in the normalized zero coordinate as

\[
 s=\gamma+ib,
 \qquad b\ne0,
 \tag{1}
\]

and a real even Weil transform vanishes at the real trace \(\gamma\), then
the negative Krein channel is only quadratic in \(b\).  The proposed
successor was to charge this quadratic term to the literal positive second
Euler jet

\[
 j_2=\delta\Lambda+\Lambda*\Lambda=\mu*\log^2\ge0,
 \tag{2}
\]

while retaining Gamma, the pole and the complete radical anti-short.

This note performs that test.  It gives an exact obstruction, rather than
a physical-surplus theorem.

1.  The quadratic expansion is exact:

    \[
    4m_s\{(\mathrm{Re}\,F(s))^2
          -(\mathrm{Im}\,F(s))^2\}
    =-4m_sb^2F'(\gamma)^2+O(b^4).
    \tag{3}
    \]

2.  The fixed vertical jet \(F\mapsto F'(\gamma)\) does **not** descend
    through the complete \(\Xi\)-radical.  At a simple real zero,

    \[
    (P\Xi)'(\gamma)=P(\gamma)\Xi'(\gamma),
    \tag{4}
    \]

    although \(P\Xi\) represents the zero class in the physical quotient.
3.  Consequently no postshort \(j_2\) seminorm can control the fixed jet.
    Before shorting, the opposite obstruction occurs: the raw positive
    \(j_2\) energy is strictly positive on an exact threshold radical on
    which the complete curvature is zero.
4.  The Toeplitz--Hankel vertical Cauchy estimate controls an analytic
    circle norm, not the radically shorted physical \(j_2\) energy.  The
    half-shift equation is inhomogeneous at the derivative level, with
    forcing \(2\Xi'(\gamma)\).

Thus the literal second jet still overcounts if it is kept positive before
the anti-short, and it cannot control the proposed fixed vertical jet after
the anti-short.  A valid second-order attack has to differentiate the
radical projection as well.  Equivalently, it needs a **covariant vertical
jet on the moving radical quotient**, coupled to the complete signed
prime--Gamma--polar Hessian.  Positivity of (2) does not supply that
connection term.

No assertion about the truth or falsity of the physical surplus is made.

## 2. Semantic audit

The calculation below uses, and does not repeat, the following earlier
results.

* Phase 70, E70.11--E70.12 proves the Möbius connection and its Riccati
  identity

  \[
  \delta A+A^2=Z^{-1}\delta^2Z,
  \qquad A=Z^{-1}\delta Z,
  \tag{5}
  \]

  but also records that this Euler identity contains no Gamma--polar sign.
* Phase 70, E70.10 proves that an ordinary Euler square produces the
  unwanted ratio comb \(\log(n/m)\).
* 106.40 proves (2), its pointwise theta realization and the indefinite
  literal polarization on \(\{p,p^2\}\).
* 106.49 proves that the desired cluster curvature is a lower coherence
  estimate, whereas \(j_2\) is a second-moment upper estimate.
* 106.54--106.60 prove that the primitive \(j_2\) walk overcounts the
  physical two-step walk and that the missing intermediate-position,
  Gamma and polar terms must remain coupled.
* 106.64 proves the exact Toeplitz--Hankel kernel

  \[
  B(s,z)=\frac12\{\Phi(s-z)+\Phi(s+z)\},
  \qquad \Phi=\widehat{K/h},
  \tag{6}
  \]

  on the mean-periodic quotient.
* 106.69 proves the vertical relation

  \[
  \Phi(u+i/2)+\Phi(u-i/2)=2\Xi(u),
  \tag{7}
  \]

  but shows that it does not close the horizontal Toeplitz--Hankel Gram.
* 106.99 proves that the second ordered primitive has a positive
  intermediate-position defect, while the order-three defect is already
  indefinite.
* 106.112 proves that the unshorted Bochner probability itself does not
  descend through the complete radical.  The present note specializes
  that quotient issue to the first vertical evaluation jet and identifies
  its exact near-threshold scale.
* 106.120 proves the quadratic near-line expansion at the level of the
  signed orbit form.
* 106.124 computes the transverse mean-periodic leakage
  (t\Xi'(t)\widehat F(t)) of geometric dilation.  Here the derivative is
  instead the vertical motion of an evaluation point; both calculations
  expose the same need to differentiate the radical projection, but their
  operators and quadratic forms are different.

The new point is the compatibility of that vertical expansion with the
**complete radical quotient**.  It is a quotient-covariance issue, not a
new use of coefficient positivity.

## 3. Exact quadratic escape of an off-line orbit

Let \(F\) be entire, real on the real axis and even.  Fix
\(\gamma\in\mathbb R\), and suppose

\[
 F(\gamma)=0.
 \tag{8}
\]

Taylor expansion and reality of the real-axis derivatives give

\[
\begin{aligned}
 \mathrm{Re}\,F(\gamma+ib)
  &=-\frac{b^2}{2}F''(\gamma)+O(b^4),\\
 \mathrm{Im}\,F(\gamma+ib)
  &=bF'(\gamma)-\frac{b^3}{6}F'''(\gamma)+O(b^5).
\end{aligned}
\tag{9}
\]

Hence

\[
 (\mathrm{Re}\,F(\gamma+ib))^2
 -(\mathrm{Im}\,F(\gamma+ib))^2
 =-b^2F'(\gamma)^2+O(b^4).
 \tag{10}
\]

Multiplication by the exact orbit factor \(4m_s\) in 106.37 proves (3).
No estimate and no zero-location assumption enters (9)--(10).

If \(F'(\gamma)\ne0\), the first nonzero signed contribution is therefore
strictly negative and of order \(b^2\).  This is the scale which a
second-order physical surplus would have to absorb.

## 4. The fixed vertical jet does not live on the radical quotient

Let \(\mathscr A_{\rm ev}\) be any of the physical even analytic transform
classes used in 106.37 and 106.64, enlarged to include the exact Riemann
kernel and its even derivatives.  Its complete radical contains

\[
 \mathscr I_\Xi
 =\{P\Xi:P\text{ is an even real polynomial}\}.
 \tag{11}
\]

Let \(\gamma\) be a simple real zero of \(\Xi\), and define the first
vertical jet

\[
 J_\gamma(F)=F'(\gamma).
 \tag{12}
\]

### Theorem 1 — Non-descent of the vertical jet

The functional \(J_\gamma\) does not descend to
\(\mathscr A_{\rm ev}/\mathscr I_\Xi\).  More precisely, for every even
real polynomial \(P\),

\[
 \boxed{J_\gamma(P\Xi)=P(\gamma)\Xi'(\gamma).}
 \tag{13}
\]

In particular, choosing \(P(\gamma)\ne0\) gives a vector representing zero
in the quotient on which \(J_\gamma\ne0\).

#### Proof

The product rule gives

\[
 (P\Xi)'(\gamma)
 =P'(\gamma)\Xi(\gamma)+P(\gamma)\Xi'(\gamma).
 \tag{14}
\]

The first term vanishes because \(\Xi(\gamma)=0\), and the second is
nonzero when \(P(\gamma)\ne0\) because the zero is simple.  This proves
(13). \(\square\)

The same statement holds at a zero of multiplicity \(m\): the first jet
which sees the divisor is the \(m\)-th jet, and

\[
 (P\Xi)^{(m)}(\gamma)=P(\gamma)\Xi^{(m)}(\gamma).
 \tag{15}
\]

Thus the obstruction is not tied to simplicity; simplicity merely makes
it occur at the quadratic scale (3).

### Corollary 2 — No quotient estimate for the fixed jet

Let \(C\) be any linear feature map and let \(\mathcal R\) be the complete
radical in its source space.  Put

\[
 \overline C=P_{(C\mathcal R)^\perp}C,
 \qquad
 \|[f]\|_C^2=\|\overline Cf\|^2
 =\mathrm{dist}(Cf,C\mathcal R)^2.
 \tag{16}
\]

Then no finite constant \(M\) can satisfy

\[
 |J_\gamma(F_f)|^2
 \le M\|[f]\|_C^2
 \tag{17}
\]

for all physical tests \(f\), where \(F_f\) is their Weil transform.

#### Proof

For \(r\in\mathcal R\), equation (16) gives \(\overline Cr=0\).  Choose
an exact radical test whose transform is \(P\Xi\) with
\(P(\gamma)\ne0\).  The right side of (17) is zero, while Theorem 1 makes
the left side strictly positive. \(\square\)

This corollary applies in particular to the completely shorted \(j_2\)
feature map.  It is independent of the size of its coefficients and of
the heat regularization used to generate a form core.

## 5. Why the value channel descends but its fixed linearization does not

There is no contradiction between Corollary 2 and the exact Krein
factorization.  Evaluation at an **actual** zero \(s\) does descend:

\[
 (P\Xi)(s)=0.
 \tag{18}
\]

What fails is the operation in which the evaluation point is moved
vertically while the representative and the radical ideal are held fixed.
Indeed, let \(b\mapsto\Xi_b\) be a differentiable hypothetical family and
let

\[
 s_b=\gamma+ib,
 \qquad \Xi_b(s_b)=0.
 \tag{19}
\]

For every moving radical representative \(R_b=P_b\Xi_b\),

\[
 0={d\over db}R_b(s_b)
 =\partial_bR_b(s_b)+i\partial_sR_b(s_b).
 \tag{20}
\]

The term \(i\partial_sR_b\), which by itself produces (13), is cancelled
exactly by the derivative of the moving radical.  Thus the quotient
derivative is a covariant derivative

\[
 \nabla_bR_b
 :=\partial_bR_b(s_b)+i\partial_sR_b(s_b),
 \tag{21}
\]

not the fixed vertical jet \(i\partial_sR_0(\gamma)\).  Equation (20) is
the precise connection term omitted by a fixed-test Cauchy argument.

For the literal zeta function there is no independent deformation
parameter \(b\): the prime, Gamma and polar data determine \(\Xi\).
Consequently (21) cannot be manufactured from the Euler coefficient
identity (2).  It has to arise from differentiating the complete signed
prime--Gamma--polar quotient, including the radical projector.

## 6. The Toeplitz--Hankel Cauchy estimate has the wrong target norm

The exact mean-periodic kernel is (6).  Its first vertical derivative is

\[
 \boxed{
 \partial_sB(s,z)
 =\frac12\{\Phi'(s-z)+\Phi'(s+z)\}.}
 \tag{22}
\]

For every \(r>0\), the elementary Hardy--Cauchy estimate gives

\[
 r^2|\partial_sB(\gamma,z)|^2
 \le {1\over2\pi}\int_0^{2\pi}
 |B(\gamma+re^{i\theta},z)|^2\,d\theta.
 \tag{23}
\]

This is a correct positive estimate, but its right side is an analytic
circle norm.  It is neither the discrete zero-evaluation norm in the Krein
factorization nor the physical \(j_2\) translation energy.

Differentiating the exact half-shift equation (7) gives

\[
 \boxed{
 \Phi'(u+i/2)+\Phi'(u-i/2)=2\Xi'(u).}
 \tag{24}
\]

At a simple real zero \(\gamma\), the right side is nonzero.  Therefore
the vertical derivative is not a homogeneous mean-periodic direction and
cannot be removed by (7).  Equations (22)--(24) are the transform-side
version of Theorem 1.

The arithmetic meaning is equally direct.  The operator \(\delta\) in
(2) differentiates multiplicative displacements \(\log n\), while
\(\partial_s\) in (22) inserts the spatial coordinate in the Fourier
transform.  Their conversion requires the intermediate theta placement
and its commutators.  Documents 106.54 and 106.99 prove that those terms
are signed; they are not a positive remainder.

## 7. Exact literal-prime overcount before anti-shorting

The failure after anti-shorting has a complementary failure before
anti-shorting.

For an ordinary prime \(p\),

\[
 \Lambda(p^a)=\log p,
 \qquad
 j_2(p^a)=(2a-1)(\log p)^2.
 \tag{25}
\]

The natural two-index polarization

\[
 \mathcal H(m,n)=j_2(mn)-\Lambda(m)\Lambda(n)
 \tag{26}
\]

has, on \(\{p,p^2\}\), the exact matrix

\[
 {1\over(\log p)^2}\mathcal H
 =\begin{pmatrix}2&4\\4&6\end{pmatrix}.
 \tag{27}
\]

For \(v=(2,-1)^T\),

\[
 \boxed{v^*\mathcal Hv=-2(\log p)^2<0.}
 \tag{28}
\]

This already rules out an unrestricted Gram lift of \(j_2\).

There is also a complete-system saturation test.  Let

\[
 r_1^\circ={K''\over K}
 -\mu_K\!\left({K''\over K}\right),
 \qquad Lr_1^\circ=\frac12r_1^\circ.
 \tag{29}
\]

For its rank-one projection,

\[
 \mathrm{Tr}\,P_{r_1}
 (L^2-\tfrac12L)=0.
 \tag{30}
\]

After the exact ground-state unitary, write \(f=\mathcal Ur_1^\circ\).
For every \(N\ge2\), the raw positive second-jet energy is

\[
 \mathcal J_{2,N}(f)
 ={1\over2}\sum_{2\le n\le N}{j_2(n)\over\sqrt n}
 \|f-S_{\log n}f\|_2^2>0.
 \tag{31}
\]

The \(n=2\) term is positive because \(j_2(2)=(\log2)^2\) and a nonzero
\(L^2(\mathbb R)\) function cannot be \(\log2\)-periodic.  Comparing
(30) and (31) proves that every identity of the form

\[
 L(L-\tfrac12)
 =\text{positive raw }j_2\text{ square}
  +\text{nonnegative remainder}
 \tag{32}
\]

is false in the literal Riemann system.  The complete Gamma--polar and
intermediate-theta terms have to cancel (31) on the radical.

Equations (17) and (32) give the exact dichotomy:

* before anti-shorting, positive \(j_2\) overcounts;
* after anti-shorting, the fixed vertical jet is not a quotient
  functional and therefore cannot be charged to the shorted \(j_2\) norm.

## 8. The correct second-order target

Let \(P_{\mathcal R}\) denote the complete radical projection in one fixed
physical Hilbert coordinate.  A quotient-compatible jet may be defined by

\[
 J_\gamma^{\rm cov}(f)
 =J_\gamma\bigl(F_{(I-P_{\mathcal R})f}\bigr).
 \tag{33}
\]

Unlike (12), this functional annihilates the radical.  Let

\[
 C_{2,N}^{\rm sh}
 =P_{(C_{2,N}\mathcal R)^\perp}C_{2,N}
 \tag{34}
\]

be the shorted literal second-jet feature.  On a fixed heat or hybrid row,
the sharp possible estimate is

\[
 \boxed{
 |J_\gamma^{\rm cov}(f)|^2
 \le M_{\gamma,N}
 \|C_{2,N}^{\rm sh}f\|^2,}
 \tag{35}
\]

where the optimal constant is the quotient Riesz norm

\[
 M_{\gamma,N}
 =\bigl\|
   (C_{2,N}^{\rm sh})^{\dagger *}
   J_\gamma^{\rm cov}
  \bigr\|^2,
 \tag{36}
\]

whenever the functional belongs to the range of
\((C_{2,N}^{\rm sh})^*\); otherwise it is infinite.  This is the standard
Moore--Penrose characterization and follows by minimizing the feature norm
under the scalar constraint \(J_\gamma^{\rm cov}(f)=1\).

However, (35) is not yet the physical Hessian.  Differentiating the
anti-short also differentiates \(P_{\mathcal R}\).  On every fixed finite
heat/hybrid block this correction has an exact formula.

Let \(b\mapsto\mathcal A_b\) be a twice differentiable family of the
complete signed finite-block operators and let
\(b\mapsto\mathcal R_b\) be its radical bundle.  Choose a differentiable
unitary trivialization

\[
 U_b\mathcal R_0=\mathcal R_b,
 \qquad U_0=I,
 \qquad X_b=U_b^*U_b',
 \tag{37}
\]

so \(X_b^*=-X_b\).  Put

\[
 \widetilde{\mathcal A}_b=U_b^*\mathcal A_bU_b,
 \qquad Q_0=I-P_{\mathcal R_0}.
 \tag{38}
\]

### Theorem 3 — Exact covariant Hessian of the finite short

At \(b=0\), with all unlabelled quantities evaluated there,

\[
\boxed{
\begin{aligned}
 {d\over db}\widetilde{\mathcal A}_b
 &=\mathcal A'+[\mathcal A,X],\\
 {d^2\over db^2}\widetilde{\mathcal A}_b
 &=\mathcal A''+2[\mathcal A',X]
   +[[\mathcal A,X],X]+[\mathcal A,X'].
\end{aligned}}
\tag{39}
\]

Consequently the Hessian of the compressed form in the fixed quotient
coordinate is

\[
 \boxed{
 \nabla^2\mathcal A
 =Q_0\{\mathcal A''+2[\mathcal A',X]
   +[[\mathcal A,X],X]+[\mathcal A,X']\}Q_0.}
 \tag{40}
\]

If \(\mathcal A_b\mathcal R_b=0\) for all \(b\), then the entire operator
inside braces in (40) annihilates \(\mathcal R_0\).  Its first term
\(\mathcal A''\) need not do so.

#### Proof

Differentiate \(U_b^*U_b=I\) to obtain
\((U_b^*)'=-X_bU_b^*\) in the trivialized coordinate.  The product rule
then gives

\[
 \widetilde{\mathcal A}_b'
 =U_b^*\mathcal A_b'U_b
  +[\widetilde{\mathcal A}_b,X_b].
 \tag{41}
\]

Differentiate (41) once more and set \(b=0\).  The derivative of its first
term is \(\mathcal A''+[\mathcal A',X]\), while the derivative of its
second term is

\[
 [\mathcal A'+[\mathcal A,X],X]+[\mathcal A,X'].
 \tag{42}
\]

Their sum is (39), and compression by the fixed \(Q_0\) gives (40).
Finally, \(\mathcal A_bU_br=0\) for \(r\in\mathcal R_0\) is equivalent to
\(\widetilde{\mathcal A}_br=0\).  Two differentiations prove the last
assertion. \(\square\)

The Euler component of \(\mathcal A''\) contains \(j_2\).  Equations
(20), (30) and (31) prove that the projector-derivative and
Gamma--polar terms are of the same order and cannot be discarded or
assigned a favorable sign separately.

Therefore the admissible successor is not another positive \(j_2\)
estimate.  It is the following joint theorem.

### Covariant second-variation target

Construct the connection of the complete radical bundle under the
physical prime--Gamma deformation, calculate the full signed Hessian of
the corresponding short, and prove that its restriction to the heat/hybrid
complement absorbs

\[
 4m_sb^2|J_\gamma^{\rm cov}(f)|^2
 \tag{43}
\]

uniformly as \(b\to0\).  The calculation must use the common finite cutoff
before passing to the limit, because 106.55 proves that the primitive
\(j_2\) term and the intermediate-position defect have no separate
cutoff-free limits.

## 9. Result

The near-threshold quadratic escape is real, but the proposed
vertical-Cauchy/positive-\(j_2\) closure is not quotient compatible.
The decisive identities are

\[
 \boxed{
 \begin{aligned}
 &\text{off-line loss}=-4m_sb^2F'(\gamma)^2+O(b^4),\\
 &J_\gamma(P\Xi)=P(\gamma)\Xi'(\gamma)\ne0,\\
 &\mathcal J_{2,N}(\mathcal Ur_1^\circ)>0
   \quad\text{while}\quad
   \langle r_1^\circ,L(L-\tfrac12)r_1^\circ\rangle=0.
 \end{aligned}}
 \tag{44}
\]

Thus neither ordering works:

\[
 \boxed{
 \text{positive }j_2\text{ then short}
 \quad\text{overcounts},
 \qquad
 \text{short then fixed vertical jet}
 \quad\text{is not well defined}.}
 \tag{45}
\]

The only surviving second-order object is the covariant Hessian of the
complete signed short.  Proving its uniform nonnegativity on the heat and
hybrid exhaustion would prove the physical surplus; it is not proved by
the Riccati identity or by vertical Cauchy estimates alone.
