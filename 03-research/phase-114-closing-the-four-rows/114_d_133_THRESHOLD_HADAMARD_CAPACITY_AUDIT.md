# D.133 — Hadamard variation at a prime-power threshold

## Verdict

There is an exact right-Hadamard formula for opening the threshold

\[
 T=T_N+\delta,\qquad T_N={1\over2}\log N,
\]

on a common smooth core after unitary dilation to \((-1,1)\).  It contains

1. the derivative of the complete Gamma multiplier;
2. one explicit transport derivative for every earlier prime-power
   contact;
3. a rank-two endpoint form for the contact born at \(N\); and
4. a finite-rank derivative of the two-Tate projection.

The formula is rigorous as a quadratic-form derivative on smooth vectors.
It is **not** a bounded-operator derivative on the natural logarithmic
Gamma form domain.  The new contact has the endpoint Hadamard form

\[
 -{2w_N\over T_N}
 \bigl(\overline{f(-1)}g(1)+\overline{f(1)}g(-1)\bigr),
 \qquad w_N={\Lambda(N)\over\sqrt N},                  \tag{0.1}
\]

and point evaluation is unbounded in that domain.  Primitive smooth
endpoint spikes show that (0.1) has arbitrarily large positive and
negative values while the Gamma shape derivative and all earlier-contact
derivatives stay bounded along a suitable sequence.  Hence the initial
crossing form has no uniform sign, even after imposing both Tate moments.

The same issue prevents a classical operator-norm derivative of the shorted
annular capacity \(\operatorname {Cap}_N\) at birth.  On fixed coercive
blocks its derivative is the usual Schur--Hadamard expression, derived
below.  At an actual threshold the annular Hilbert space is born with the
cell and the entering translation has norm one for every \(\delta>0\),
although it is zero at \(\delta=0\).  Thus the fixed-space differentiability
hypotheses fail.  Any finite right derivative obtained after a mesh or
boundary regularization depends on that regularization.

This does not contradict the positive logarithmic-capacity interval of
D.60.  The Gamma *energy* of a boundary layer grows like
\(\log(1/\delta)\), whereas its shape derivative is singular.  Positivity
for a short cell must therefore be proved by a non-perturbative capacity
estimate, not by a nonnegative first variation.  No uniform signed
Hadamard induction follows from A--B--C alone.

No RH statement is assumed and the paper is not modified.

## 1. Fixed-window realization

Let

\[
 (U_TF)(x)=T^{1/2}F(Tx),\qquad -1<x<1,                 \tag{1.1}
\]

so \(U_T:L^2(-T,T)\to L^2(-1,1)\) is unitary.  Write

\[
 a_n=\log n,\qquad \alpha_n(T)={a_n\over T},\qquad
 w_n={\Lambda(n)\over\sqrt n}.                         \tag{1.2}
\]

Only prime powers have \(w_n\ne0\); the notation \(\Lambda(n)\) denotes
the reduced A--B contact degree, not an independently inserted analytic
weight.

Extend functions by zero outside \((-1,1)\).  For \(0<\alpha<2\), define
the symmetric truncated translation form

\[
\begin{aligned}
 C_\alpha(f,g)={}&J_\alpha(f,g)+\overline{J_\alpha(g,f)},\\
 J_\alpha(f,g)={}&\int_{-1}^{1-\alpha}
       \overline{f(x)}g(x+\alpha)\,dx.                 \tag{1.3}
\end{aligned}
\]

The uncompressed renormalized operator on the fixed window is

\[
 K_{N,T}=G_T-m_0I-\sum_{2\le n\le N}w_nC_{\alpha_n(T)}, \tag{1.4}
\]

where \(G_T\) is the Gamma multiplier

\[
 \langle f,G_Tg\rangle
 ={1\over2\pi}\int_{\mathbb R}
 \ell_\infty(\sigma/T)
 \overline{\widehat f(\sigma)}\widehat g(\sigma)\,d\sigma, \tag{1.5}
\]

and

\[
 \ell_\infty(u)=\operatorname {Re}\psi(1/4+iu/2)-\psi(1/4). \tag{1.6}
\]

The two moment vectors may be taken as

\[
 v_{T,+}(x)=e^{Tx/2},\qquad v_{T,-}(x)=e^{-Tx/2}.       \tag{1.7}
\]

The irrelevant common factor \(T^{1/2}\) from (1.1) does not change their
span.  If \(V_T:\mathbb C^2\to L^2(-1,1)\) has these columns and
\(\mathsf G_T=V_T^*V_T\), then

\[
 P_T=I-V_T\mathsf G_T^{-1}V_T^*                        \tag{1.8}
\]

is the primitive projection.  The operator in D.121 is

\[
 \widetilde H_{N,T}=P_TK_{N,T}P_T.                     \tag{1.9}
\]

## 2. Gamma shape derivative

On \(C_c^\infty(-1,1)\), differentiation of (1.5) gives

\[
 \boxed{
 \langle f,\dot G_Tg\rangle
 =-{1\over2\pi T^2}\int_{\mathbb R}
 \sigma\ell_\infty'(\sigma/T)
 \overline{\widehat f(\sigma)}\widehat g(\sigma)\,d\sigma.} \tag{2.1}
\]

This contains the full quarter-shift Gamma factor.  It is not a finite
oscillator truncation.

The multiplier in (2.1) is bounded.  Near zero,
\(u\ell_\infty'(u)=O(u^2)\), while Stirling's formula gives

\[
 u\ell_\infty'(u)=1+O(u^{-2})\qquad(|u|\to\infty).     \tag{2.2}
\]

Thus \(\dot G_T\) extends to a bounded operator on \(L^2(-1,1)\), locally
uniformly for \(T>0\).  Notice the contrast: \(G_T\) has logarithmic order,
but its dilation derivative has order zero.

## 3. Every earlier contact

For smooth \(f,g\), put

\[
 A_\alpha(f,g)
 =-\overline{f(1-\alpha)}g(1)
   +\int_{-1}^{1-\alpha}
       \overline{f(x)}g'(x+\alpha)\,dx.                \tag{3.1}
\]

Leibniz' rule says \(dJ_\alpha(f,g)/d\alpha=A_\alpha(f,g)\).

Since \(\dot\alpha_n=-a_n/T^2\), the complete derivative of an earlier
contact is

\[
\boxed{
 \dot C_{n,T}(f,g)
 =-{a_n\over T^2}
 \left(A_{\alpha_n}(f,g)
       +\overline{A_{\alpha_n}(g,f)}\right).           \tag{3.2}
}
\]

This form of (3.2) makes the conjugation convention explicit.  It includes
every \(n<N\) with \(w_n\ne0\).

Although (3.2) is a valid smooth-core Hadamard form, its endpoint traces
are not bounded on the logarithmic Gamma form domain.  Earlier contacts
are form-norm continuous in \(T\), but in general not differentiable there
in bounded form norm.

## 4. The contact born at the threshold

Assume \(N\) is a prime power and put \(T_0=T_N=a_N/2\).  Then
\(\alpha_N(T_0)=2\), and (1.3) is zero because the integration interval has
zero length.  Taking the right derivative in \(T\), (3.1) yields

\[
 \left.{d\over dT}J_{\alpha_N(T)}(f,g)\right|_{T_0+}
 ={2\over T_0}\overline{f(-1)}g(1).                   \tag{4.1}
\]

Consequently

\[
 \boxed{
 \dot C_{N,T_0+}(f,g)
 ={2\over T_0}
 \bigl(\overline{f(-1)}g(1)+\overline{f(1)}g(-1)\bigr).} \tag{4.2}
\]

Since the contact occurs with coefficient \(-w_N\) in (1.4), its
Hadamard contribution is exactly (0.1).  It has rank two on any function
space with continuous endpoint trace, with eigenvectors given by equal and
opposite endpoint values.  One sign is negative and the other positive.

The rank-two description must not be mistaken for a bounded rank-two
operator on the natural form domain

\[
 \mathcal Q_\Gamma=\left\{f:
 \int(1+\log(2+|\sigma|))|\widehat f(\sigma)|^2d\sigma<\infty
 \right\}.                                             \tag{4.3}
\]

Point evaluation at \(\pm1\) is unbounded on (4.3), because logarithmic
Fourier control is below every positive Sobolev trace exponent.

## 5. Derivative of the primitive projection

The columns in (1.7) satisfy

\[
 \dot v_{T,\pm}=\pm{x\over2}v_{T,\pm}.                 \tag{5.1}
\]

Differentiating (1.8) gives the finite-rank identity

\[
\boxed{
\begin{aligned}
 \dot P_T={}&-\dot V_T\mathsf G_T^{-1}V_T^*
             -V_T\mathsf G_T^{-1}\dot V_T^*\\
 &+V_T\mathsf G_T^{-1}\dot{\mathsf G}_T
        \mathsf G_T^{-1}V_T^*,\\
 \dot{\mathsf G}_T={}&\dot V_T^*V_T+V_T^*\dot V_T.
                                                               \tag{5.2}
\end{aligned}}
\]

Its rank is at most four.  Combining (2.1), (3.2), (4.2) and (5.2) gives
the complete smooth-core derivative

\[
\boxed{
 \dot{\widetilde H}_{N,T_0+}
 =\dot P_{T_0}K_{N-1,T_0}P_{T_0}
  +P_{T_0}\dot K_{N,T_0+}P_{T_0}
  +P_{T_0}K_{N-1,T_0}\dot P_{T_0},}                   \tag{5.3}
\]

where

\[
 \dot K_{N,T_0+}
 =\dot G_{T_0}
  -\sum_{2\le n<N}w_n\dot C_{n,T_0}
  -w_N\dot C_{N,T_0+}.                                \tag{5.4}
\]

Equations (5.3)--(5.4) include Gamma, every earlier contact, the entering
contact and both moving Tate constraints.  They are the requested
Hadamard formula.

## 6. Exact primitive countersequence to a signed crossing theorem

Choose \(\phi\in C^\infty([0,1])\), supported in \([0,1/2)\) relative to
the half-line and with \(\phi(0)\ne0\).  For small
\(\varepsilon>0\), set

\[
 b_\varepsilon(x)=\varepsilon^{-1/2}
 \left[\phi\left({1-x\over\varepsilon}\right)
       +\phi\left({1+x\over\varepsilon}\right)\right]. \tag{6.1}
\]

Both endpoint values have the same sign and size
\(\varepsilon^{-1/2}\phi(0)\), whereas
\(\|b_\varepsilon\|_2=O(1)\).  Its two Tate moments are
\(O(\sqrt\varepsilon)\).  Select two fixed smooth interior correctors
\(\chi_\pm\), supported away from

\[
 \{\pm1\}\cup
 \{1-\alpha_n(T_0),-1+\alpha_n(T_0):n<N,\ w_n\ne0\},  \tag{6.2}
\]

whose two-by-two moment matrix is invertible.  Such a pair exists because
the forbidden set is finite and the functions \(e^{\pm T_0x/2}\) are
linearly independent on every open interval.  There are coefficients
\(c_{\varepsilon,\pm}=O(\sqrt\varepsilon)\) such that

\[
 f_\varepsilon=b_\varepsilon
   -c_{\varepsilon,+}\chi_+
   -c_{\varepsilon,-}\chi_-\in\operatorname {Ran}P_{T_0}. \tag{6.3}
\]

The endpoint values are unchanged.  Therefore the entering term in
(5.3) satisfies

\[
 -w_N\dot C_{N,T_0+}(f_\varepsilon,f_\varepsilon)
 =-{4w_N|\phi(0)|^2\over T_0\varepsilon}.              \tag{6.4}
\]

The remaining terms are \(o(\varepsilon^{-1})\):

* the Gamma derivative is bounded on \(L^2\) by Section 2;
* the correctors in (6.3) are \(O(\sqrt\varepsilon)\);
* their supports can be chosen to avoid all the finitely many trace points
  in (3.2), so earlier-contact endpoint products have no
  \(\varepsilon^{-1}\) contribution;
* the integral parts of (3.2) have disjoint translated boundary layers for
  sufficiently small \(\varepsilon\); and
* \(\dot P_{T_0}f_\varepsilon=O(\sqrt\varepsilon)\), while its pairing with
  the fixed smooth range of \(\dot P_{T_0}\) is subleading.

It follows that

\[
 \langle f_\varepsilon,
   \dot{\widetilde H}_{N,T_0+}f_\varepsilon\rangle
 \longrightarrow-\infty.                              \tag{6.5}
\]

Changing the sign of one endpoint layer reverses (6.4), and the same
moment-correction argument gives values tending to \(+\infty\).  Hence the
primitive crossing form is indefinite and unbounded in both directions.
In particular, there is no uniform theorem
\(\dot{\widetilde H}_{N,T_0+}\ge0\) or
\(\dot{\widetilde H}_{N,T_0+}\le0\).

This is a counterexample to a *signed first-variation method*, not to row
D.  For (6.1), the undifferentiated Gamma energy grows like
\(\log(1/\varepsilon)\); it cannot be discarded when \(\delta\) and
\(\varepsilon\) tend to zero together.

## 7. Shorted capacity and why its classical derivative fails at birth

On fixed Hilbert spaces, let

\[
 \mathcal H(\delta)=
 \begin{pmatrix}A(\delta)&B(\delta)\\
                 B(\delta)^*&D(\delta)\end{pmatrix},
 \qquad A(0)>0,                                        \tag{7.1}
\]

be differentiable in operator norm.  The shorted capacity is

\[
 \operatorname {Cap}(\delta)
 =D(\delta)-B(\delta)^*A(\delta)^{-1}B(\delta).        \tag{7.2}
\]

Direct differentiation gives the exact Schur--Hadamard formula

\[
\boxed{
\begin{aligned}
 \dot{\operatorname {Cap}}={}&\dot D
 -\dot B^*A^{-1}B-B^*A^{-1}\dot B\\
 &+B^*A^{-1}\dot A A^{-1}B.                           \tag{7.3}
\end{aligned}}
\]

For a scalar inverse capacity

\[
 \operatorname {cap}=\langle b,A^{-1}b\rangle^{-1},   \tag{7.4}
\]

one likewise obtains

\[
\boxed{
 \dot{\operatorname {cap}}
 =-\operatorname {cap}^2
 \left(2\operatorname {Re}\langle\dot b,A^{-1}b\rangle
 -\langle b,A^{-1}\dot A A^{-1}b\rangle\right).}      \tag{7.5}
\]

These are the desired capacity variation formulas whenever their
hypotheses hold.

They do not apply directly to the threshold capacity of D.121.  Let

\[
 \ell=2-\alpha_N(T)>0.                                 \tag{7.6}
\]

The entering translation identifies the left layer \((-1,-1+\ell)\) with
the right layer \((1-\ell,1)\).  If \(u_\ell\) has equal normalized
profiles on these layers, then

\[
 \|u_\ell\|_2=1,
 \qquad \langle u_\ell,C_{\alpha_N(T)}u_\ell\rangle=1. \tag{7.7}
\]

For the threshold regime \(0<\ell<1\), the two layers are disjoint and
the restriction of the contact to their sum is the off-diagonal unitary
identification.  Thus

\[
 \|C_{\alpha_N(T)}\|=1\quad(0<\ell<1),
 \qquad C_2=0.                                         \tag{7.8}
\]

The contact is strongly/form-norm continuous on suitable domains but not
operator-norm continuous at birth.  Simultaneously, the annular summand in
the decomposition defining \(\operatorname {Cap}_N\) has zero dimension at
\(\delta=0\) and positive infinite dimension for every \(\delta>0\).
There is no canonical fixed annular Hilbert space on which (7.3) can be
differentiated.

After blowing the layer up to a fixed interval, (7.7) becomes an order-one
off-diagonal boundary block, while the Gamma form acquires the singular
scale \(\log(1/\delta)\).  It is therefore false that
\(\operatorname {Cap}_N(\delta)\) has an intrinsic finite bounded-operator
right derivative determined by (0.1).  A Galerkin or mollified trace may
have a derivative, but it is a derivative of that regularization.

## 8. Consequence for threshold induction

The exact conclusions are:

1. the new renormalized contact vanishes at the threshold itself;
2. its smooth-core right derivative is the rank-two form (0.1);
3. the complete primitive derivative is (5.3)--(5.4);
4. the derivative is indefinite and unbounded on primitive smooth vectors;
5. the shorted capacity has the formal derivative (7.3) only after a fixed
   differentiable regularization; and
6. the true cell opening is governed by logarithmic boundary capacity, not
   by a signed first derivative.

Therefore no uniform sign of the initial variation can be used to propagate
row D through all prime-power cells.  A successful multiscale proof must
establish the non-perturbative Schur capacity itself, with the joint Gamma
and earlier-contact cancellation retained.  The Hadamard calculation makes
that requirement sharper but does not close D.
