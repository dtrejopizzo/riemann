# D.163 — Tate-deflated weighted prolate depth and the Suzuki gate

## Verdict

The centred Tate--Chebyshev form has an exact **weighted prolate**
realization which retains the depth of every negative well, every
prime-power coefficient, and the complete Gamma multiplier.  It also gives
the unique minimum-norm support-local comparison map requested after
D.137.  In particular, this formulation does not replace the negative set
by its thickness.

The finite Frobenius tower at a prime is grouped by the exact finite
Poisson polynomial

\[
 P_{p,K}(\tau)=1+2\sum_{k=1}^{K}p^{-k/2}
                    \cos(k\tau\log p),                 \tag{0.1}
\]

where \(K=\lfloor2T/\log p\rfloor\).  Thus the complete primitive
multiplier is

\[
\boxed{
 r_T(\tau)=h_{5/4}(\tau)-\beta-{1\over\tau^2+1/4}
 -\sum_{p\le e^{2T}}\log p\,[P_{p,K_p(T)}(\tau)-1].}  \tag{0.2}
\]

The digamma recurrence makes (0.2) exactly the A--B--C multiplier with all
\(p^k\) and Gamma; it is not an approximation.

Let \(r_T^\pm=\max(\pm r_T,0)\), and let \(PW_T^0\) be the
Paley--Wiener space with the two Tate evaluations at \(\pm i/2\) removed.
The weighted prolate depth is the generalized Rayleigh quotient

\[
 \kappa_T=sup_{0\ne G\in PW_T^0}
 {\int r_T^-(\tau)|G(\tau)|^2d\tau
  \over
  \int r_T^+(\tau)|G(\tau)|^2d\tau}.                  \tag{0.3}
\]

With the standard kernel-range convention when the denominator vanishes,

\[
 \boxed{-B_{\rm nuc}^{\rm prim}\ge0
 \Longleftrightarrow \kappa_T\le1.}                   \tag{0.4}
\]

Equation (0.3) is the precise weighted prolate/depth theorem still to be
proved.  It sees the *amplitude* of every arithmetic well.  Ordinary
Logvinenko--Sereda estimates see only thickness and cannot imply it.

Suzuki's 2026 continuous screw-function realization does not supply the
missing inequality.  It proves continuity of the localized lowest
eigenvalue and positivity for sufficiently small windows, and constructs
self-adjoint first-order realizations after choosing
\(\lambda<\lambda_T\).  Choosing \(\lambda=0\) requires
\(\lambda_T>0\), which is already the localized Weil inequality.  The
screw kernel itself is positive in the Krein--Langer sense if and only if
RH.  Therefore no sign or monotonicity from that work may be imported into
(0.3).

## 1. Exact finite-depth Poisson grouping

Put \(\rho_p=p^{-1/2}\), \(z=\rho_pe^{i\tau\log p}\), and
\(K=K_p(T)=\lfloor2T/\log p\rfloor\).  The elementary geometric identity

\[
 P_{p,K}(\tau)-1
 =2\mathrm{Re}{z(1-z^K)\over1-z}               \tag{1.1}
\]

gives

\[
 \log p\,[P_{p,K}(\tau)-1]
 =2\sum_{k\log p\le2T}{\log p\over p^{k/2}}
       \cos(k\tau\log p).                             \tag{1.2}
\]

The right side is precisely the sum of the derived contacts
\(\mathbb L_{p^k}\) with the central metric depth \(p^{-k/2}\).  Hence
(1.1) is compatible with the Witt raising law and the Poisson/Szego
realization of D.109--D.110.  No prime powers are filled in analytically.

At infinite depth,

\[
 P_{p,\infty}(\tau)
 ={1-p^{-1}\over
   1-2p^{-1/2}\cos(\tau\log p)+p^{-1}},               \tag{1.3}
\]

the usual Poisson kernel.  For a finite support window, (1.1), not (1.3),
is the exact object.

## 2. Gamma and Tate centering

Write

\[
\begin{aligned}
 h_{5/4}(\tau)
 &=\mathrm{Re}\,\psi(5/4+i\tau/2)-\psi(5/4),\\
 \beta&=\log\pi-\psi(5/4).
\end{aligned}                                         \tag{2.1}
\]

The recurrence \(\psi(z+1)=\psi(z)+1/z\) gives

\[
 h_{5/4}(\tau)-\beta-{1\over\tau^2+1/4}
 =\mathrm{Re}\,\psi(1/4+i\tau/2)-\log\pi.      \tag{2.2}
\]

Combining (1.2) and (2.2) proves (0.2).  Plancherel then gives

\[
 -B_{\rm nuc}^{\rm prim}(F,F)
 ={1\over2\pi}\int_{\mathbb R}r_T(\tau)
                       |\widehat F(\tau)|^2d\tau.     \tag{2.3}
\]

The primitive conditions are exactly

\[
 \widehat F(i/2)=\widehat F(-i/2)=0.                  \tag{2.4}
\]

Thus (2.3) lives on \(PW_T^0\), not on an unconstrained bandlimited
space.

## 3. The exact Tate-deflated prolate kernel

In the Fourier normalization of D.121 the Paley--Wiener reproducing kernel
is

\[
 K_T(z,w)={\sin T(z-\overline w)\over
                  \pi(z-\overline w)}.                \tag{3.1}
\]

Let \(a_1=i/2,a_2=-i/2\),
\(\mathsf G_T=(K_T(a_i,a_j))_{i,j}\), and

\[
 k_T(z)=(K_T(z,a_1),K_T(z,a_2)).                      \tag{3.2}
\]

The reproducing kernel of \(PW_T^0\) is the exact rank-two deflation

\[
 \boxed{
 K_T^0(z,w)=K_T(z,w)-k_T(z)\mathsf G_T^{-1}k_T(w)^*.} \tag{3.3}
\]

Let \(P_T^0\) denote the corresponding orthogonal projection.  Define
the positive weighted compressions

\[
 A_T^\pm=P_T^0M_{r_T^\pm}P_T^0.                       \tag{3.4}
\]

On \(\overline{\mathrm{Ran}(A_T^+)^{1/2}}\), put

\[
 \mathcal K_T^{\rm wpr}
 =(A_T^+)^{\dagger/2}A_T^-(A_T^+)^{\dagger/2}.        \tag{3.5}
\]

Equivalently, (3.5) is the integral-operator pencil obtained by inserting
the kernel (3.3) on both sides of the weights \(r_T^\pm\).  Its top
spectral value is (0.3):

\[
 \|\mathcal K_T^{\rm wpr}\|=\kappa_T.                \tag{3.6}
\]

This is a genuine weighted prolate operator.  The time limitation is
encoded by (3.1), the two Tate jets by (3.3), and the arithmetic well depth
by \(r_T^-\).  Replacing \(r_T^-\) by an indicator of its support destroys
the information which (0.3) needs.

## 4. The canonical support-local comparison

Define closed feature maps on their natural form domains by

\[
 X_TG=\sqrt{r_T^+}\,G,
 \qquad
 Y_TG=\sqrt{r_T^-}\,G,
 \qquad G\in PW_T^0.                                  \tag{4.1}
\]

Then

\[
 2\pi(-B_{\rm nuc}^{\rm prim})(G,G)
 =\|X_TG\|^2-\|Y_TG\|^2.                             \tag{4.2}
\]

If \(\ker X_T\subseteq\ker Y_T\), the algebraic rule

\[
 C_T^0(X_TG)=Y_TG                                     \tag{4.3}
\]

is well defined.  Its unique minimum-norm closed extension is the
Moore--Penrose comparison

\[
 \boxed{C_T^{\rm can}=Y_TX_T^\dagger,\qquad
        \|C_T^{\rm can}\|^2=\kappa_T.}                \tag{4.4}
\]

Thus (4.4) produces the exact support-local candidate demanded by D.137,
and

\[
 \|C_T^{\rm can}\|\le1
 \Longleftrightarrow -B_{\rm nuc}^{\rm prim}\ge0.    \tag{4.5}
\]

The formula is constructive; its norm-one estimate is the substantive
remaining theorem.

## 5. Exact prime-power threshold cocycle

Let \(N=p^k\), \(a_N=\log N\), \(w_N=(\log p)/\sqrt N\), and
\(a_N/2<T<a_N\).  On
\(A_{N,T}=[-T,T-a_N]\), set

\[
 J_{N,\pm}F(t)={F(t+a_N)\pm F(t)\over\sqrt2}.          \tag{5.1}
\]

The new finite-depth term in (1.2) has the exact balanced decomposition

\[
 -2w_N\mathrm{Re}\,C_F(a_N)
 =w_N\|J_{N,-}F\|^2-w_N\|J_{N,+}F\|^2.               \tag{5.2}
\]

Assume the preceding cell form \(Q_{N-1,T}\) is nonnegative and put

\[
 R_{N,T}=Q_{N-1,T}+w_NJ_{N,-}^*J_{N,-}.               \tag{5.3}
\]

The exact support-local weighted capacity is

\[
 \boxed{
 \mathcal K_{N,T}^{\rm ann}
 =w_NJ_{N,+}R_{N,T}^\dagger J_{N,+}^*.}               \tag{5.4}
\]

With the usual range condition,

\[
 Q_{N,T}\ge0
 \Longleftrightarrow
 \|\mathcal K_{N,T}^{\rm ann}\|\le1.                \tag{5.5}
\]

At birth \(|A_{N,T}|=0\), so the cocycle (5.1) vanishes exactly.  Formula
(5.4) is the nonperturbative boundary cocycle which survives the Hadamard
no-go of D.133.  Iterating (5.5) is equivalent to (0.4); it does not spend
an independent Gamma reserve at every prime.

## 6. What Suzuki's continuous screw realization supplies

Suzuki constructs the continuous kernel \(g(x-y)\), the localized
self-adjoint Friedrichs operator \(A_T\), and its lowest eigenvalue
\(\lambda_T\).  The following conclusions are unconditional:

1. \(\lambda_T\) is continuous in \(T\);
2. \(\lambda_T>0\) for sufficiently small \(T\);
3. after choosing any \(\lambda<\lambda_T\), the positive form
   \(A_T-\lambda I\) gives a Hilbert space in which the first derivative
   has self-adjoint extensions; and
4. the associated characteristic functions have real zeros.

These facts do not imply \(\lambda_T\ge0\) for all \(T\).  The construction
of the positive Hilbert metric explicitly begins with
\(\lambda<\lambda_T\).  Choosing \(\lambda=0\), which would identify the
unshifted Weil form with that metric, is permitted exactly when
\(\lambda_T>0\).  Moreover the continuous kernel is a screw function in
the positive Krein--Langer sense if and only if RH.  The paper's global
limit formula with the unshifted metric is presented conjecturally (and
its heuristic discussion assumes RH).

Consequently Suzuki supplies a valuable continuous realization and a
continuity theorem, but no support-window monotonicity or boundary
capacity stronger than (5.5).  Using its positive screw property or taking
\(\lambda=0\) for every window would import the desired sign.

## 7. Exact remaining estimate

The route has therefore been sharpened to a single non-thickness target:

\[
\boxed{
 \sup_{0\ne G\in PW_T^0}
 {\displaystyle\int r_T^-(\tau)|G(\tau)|^2d\tau
  \over
  \displaystyle\int r_T^+(\tau)|G(\tau)|^2d\tau}
 \le1\quad(T>0),}                                     \tag{7.1}
\]

where \(r_T\) is the exact finite-depth Poisson--Gamma function (0.2).
Unlike the discarded thickness route, (7.1) couples Paley--Wiener
concentration to the full arithmetic depth of each well.  Unlike a global
label intertwiner, it is support-local and changes by the explicit annular
cocycle (5.4).  Establishing (7.1), or equivalently all the threshold
bounds (5.5), completes row D.

