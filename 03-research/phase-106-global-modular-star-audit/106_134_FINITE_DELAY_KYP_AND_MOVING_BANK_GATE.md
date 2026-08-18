# 106.134 — Finite-delay KYP and the moving-bank gate

## 1. Purpose and conclusion

Document 106.133 computed the exact Hermitian part of the Abel connection

\[
 \mathcal C_{K,h}=T_{K'+K/2}M_{K/h}
\]

on the mean-periodic space. The remaining possible shortcut was that the
positive completed Gamma remainder, perhaps supplemented by the first one
or two literal ordinary-prime delays, might dominate that connection by a
KYP Schur complement.

This note gives an exact negative answer to that structural shortcut.

1. The internal connection port has a canonical, storage-independent
   minimal norm. If

   \[
     \mathcal M=\ker T_K,\qquad
     v=(\partial+\tfrac12)M_{K/h}F,\qquad F\in\mathcal M,
   \]

   then its cost is

   \[
     \|P_{\mathcal M^\perp}v\|^2
     =\lim_{\delta\downarrow0}
      \langle \mathcal CF,
      (T_KT_K^\sharp+\delta I)^{-1}\mathcal CF\rangle .
   \]
2. There is a completely explicit positive-kernel periodic family for
   which mean periodicity holds exactly, the Hermitian connection power is
   the fixed number \(\varepsilon^3/16\), and the Gamma remainder plus
   either the literal \(p=2\) delay or the literal \(p=2,3\) delays is
   \(O(L^{-2})\).
3. The same family makes the minimal Schur cost stay bounded away from
   zero. Hence neither the scalar connection power nor the full KYP
   amplitude can be absorbed by Gamma and a fixed prime head.
4. The witness is an exact heat/hybrid-row witness. Heat smoothing does
   not repair the failed inequality.
5. Quantitatively, a growing delay bank can see this family only if its
   weighted second delay moment is of order at least \(L^2\). An
   individual phase-resolving delay has \(\log n\asymp L\). Thus any
   successful physical certificate must use a cofinal ordinary-prime bank
   (or an equivalent collective estimate of that size), never a fixed
   head.

The construction below is **not** a counterexample for Riemann's theta
kernel. Its kernel is an explicit positive trigonometric polynomial. Its
role is narrower and rigorous: it falsifies every implication using only
positive-kernel mean periodicity, heat covariance, the Gamma remainder and
finitely many literal prime delays. A proof for the Riemann system must use
the theta kernel and the full cofinal placement of the ordinary primes.

## 2. The canonical minimal connection cost

Let \(\mathscr H\) be a Hilbert space on which the convolution operator
\(T=T_K\) is bounded, and put

\[
 \mathcal M=\ker T.
 \tag{1}
\]

On a common connection core let

\[
 B=\partial+\frac12,\qquad
 a=\frac Kh,\qquad
 v=BM_aF,\qquad F\in\mathcal M.
 \tag{2}
\]

The connection identity of 106.131 is

\[
 \boxed{Tv=\mathcal C_{K,h}F.}
 \tag{3}
\]

Decompose

\[
 v=P_{\mathcal M}v+\eta,\qquad
 \eta=P_{\mathcal M^\perp}v.
 \tag{4}
\]

Then \(T\eta=\mathcal CF\), and \(\eta\) is the unique minimal-norm
solution of this equation.

### Lemma 1 — Regularized Schur formula

For every \(v\in\mathscr H\),

\[
 \boxed{
 \|P_{(\ker T)^\perp}v\|^2
 =\lim_{\delta\downarrow0}
  \langle Tv,(TT^*+\delta I)^{-1}Tv\rangle .}
 \tag{5}
\]

Consequently, for (2),

\[
 \boxed{
 \|\eta\|^2
 =\lim_{\delta\downarrow0}
  \langle \mathcal CF,
  (TT^*+\delta I)^{-1}\mathcal CF\rangle .}
 \tag{6}
\]

#### Proof

By the spectral calculus for \(T^*T\),

\[
 T^*(TT^*+\delta I)^{-1}T
 =T^*T(T^*T+\delta I)^{-1}
 \xrightarrow[\delta\downarrow0]{\rm strong}
 P_{(\ker T)^\perp}.
 \tag{7}
\]

Taking the quadratic form on \(v\) proves (5). Equation (3) gives (6).
The characterization as the minimal solution is the orthogonal
decomposition of the affine solution space \(\eta+\ker T\). \(\square\)

Let \(R_{\Gamma,*}=D_{\Gamma,*}^*D_{\Gamma,*}\) denote the positive
Gamma-remainder operator. The regularized KYP block

\[
 \mathbb K_\delta=
 \begin{pmatrix}
   R_{\Gamma,*}&\mathcal C^*\\
   \mathcal C&TT^*+\delta I
 \end{pmatrix}
 \tag{8}
\]

is nonnegative if and only if

\[
 R_{\Gamma,*}
 \succeq
 \mathcal C^*(TT^*+\delta I)^{-1}\mathcal C.
 \tag{9}
\]

Thus a limiting positive-storage certificate necessarily implies

\[
 \boxed{
 \mathfrak b_{\Gamma,*}(F/h)
 \geq
 \|P_{\mathcal M^\perp}BM_aF\|^2.}
 \tag{10}
\]

This is stronger than domination of the Hermitian connection power. The
next sections disprove both forms using the same exact family.

## 3. A positive periodic mean-periodic family

Let

\[
 \mathbb T_L=\mathbb R/L\mathbb Z,\qquad
 dm_L(x)=\frac{dx}{L},\qquad
 \xi=\frac{2\pi}{L}.
 \tag{11}
\]

Convolution below is normalized Haar convolution, so Fourier coefficients
multiply. Fix

\[
 0<\varepsilon<\frac12
 \tag{12}
\]

and define

\[
 \boxed{
 K_L(x)=1+\varepsilon\cos(2\xi x)
          +\varepsilon\cos(3\xi x),\qquad
 h_L=1,\qquad a_L=K_L.}
 \tag{13}
\]

Then

\[
 1-2\varepsilon\leq K_L\leq1+2\varepsilon,\qquad
 c_L=\int_{\mathbb T_L}h_LK_L\,dm_L=1.
 \tag{14}
\]

The physical Hilbert measure in this model is therefore

\[
 d\omega_L=K_L\,dm_L.
 \tag{15}
\]

Put

\[
 F_L(x)=\cos(\xi x).
 \tag{16}
\]

The only nonzero Fourier coefficients of \(K_L\) are

\[
 k_0=1,\qquad
 k_{\pm2}=k_{\pm3}=\frac\varepsilon2.
 \tag{17}
\]

Since \((F_L)_{\pm1}=1/2\), equation (17) gives the exact mean-periodic
constraint

\[
 \boxed{F_L*K_L=0.}
 \tag{18}
\]

This is not an approximate low-frequency mode: (18) is an exact
convolution equation for every \(L\).

## 4. Exact nonvanishing of the Hermitian connection

Set

\[
 \phi_L=K_LF_L,\qquad
 \mathcal C_L=T_{K_L'+K_L/2}M_{K_L}.
 \tag{19}
\]

The coefficients of \(\phi_L\) which meet the Fourier support of \(K_L\)
are

\[
 (\phi_L)_{\pm2}=(\phi_L)_{\pm3}=\frac\varepsilon4.
 \tag{20}
\]

All other coefficients make no contribution to
\(\langle K_L*\phi_L,\phi_L\rangle_2\). Hence Parseval gives

\[
\begin{aligned}
 I_L
 &:=\langle K_L*\phi_L,\phi_L\rangle_{L^2(dm_L)}\\
 &=\sum_{n\in\mathbb Z}k_n|(\phi_L)_n|^2\\
 &=4\left(\frac\varepsilon2\right)
       \left(\frac{\varepsilon^2}{16}\right)
 =\frac{\varepsilon^3}{8}.
\end{aligned}
 \tag{21}
\]

The physical-adjoint identity of 106.133, with \(c_L=1\), now yields

\[
 \boxed{
 \operatorname {Re}
 \langle F_L,\mathcal C_LF_L\rangle_{\omega_L}
 =\frac12I_L
 =\frac{\varepsilon^3}{16}.}
 \tag{22}
\]

In particular, the mean-periodic Kirchhoff cancellation leaves a fixed
strictly positive connection power as \(L\to\infty\).

## 5. Gamma and every fixed prime head vanish on the family

For \(u>0\), let

\[
 J_{L,u}=
 \int_{\mathbb T_L}K_L(x)K_L(x-u)
 |F_L(x)-F_L(x-u)|^2\,dm_L(x).
 \tag{23}
\]

The elementary identity

\[
 \int_{\mathbb T_L}
 |\cos(\xi x)-\cos(\xi(x-u))|^2\,dm_L(x)
 =1-\cos(\xi u)
 \leq\frac{\xi^2u^2}{2}
 \tag{24}
\]

and (14) give

\[
 \boxed{
 J_{L,u}\leq
 \frac{(1+2\varepsilon)^2}{2}\,\xi^2u^2.}
 \tag{25}
\]

Use the same completed Gamma-remainder density as in the Riemann
calculation,

\[
 r_\Gamma(u)=\frac{e^{-5u/2}}{1-e^{-2u}}.
 \tag{26}
\]

Its second moment is finite and has the explicit convergent expansion

\[
 M_{\Gamma,2}
 :=\int_0^\infty u^2r_\Gamma(u)\,du
 =2\sum_{m=0}^\infty
   \left(\frac52+2m\right)^{-3}<\infty.
 \tag{27}
\]

Therefore

\[
 \boxed{
 \mathfrak b_{\Gamma,*}(F_L)
 \leq
 \frac{(1+2\varepsilon)^2}{2}\,\xi^2M_{\Gamma,2}.}
 \tag{28}
\]

Let \(\mathcal P\) be any finite set of prime powers, with the literal
ordinary-prime weights and delays

\[
 w_n=\frac{\Lambda(n)}{\sqrt n},\qquad u_n=\log n.
 \tag{29}
\]

Define its weighted second delay moment

\[
 M_2(\mathcal P)
 =\sum_{n\in\mathcal P}
   \frac{\Lambda(n)}{\sqrt n}(\log n)^2.
 \tag{30}
\]

Equation (25) gives

\[
 \boxed{
 \sum_{n\in\mathcal P}
  \frac{\Lambda(n)}{\sqrt n}J_{L,\log n}
 \leq
 \frac{(1+2\varepsilon)^2}{2}\,\xi^2M_2(\mathcal P).}
 \tag{31}
\]

Combining (28) and (31),

\[
 \boxed{
 \mathfrak b_{\Gamma,*}(F_L)
 +\sum_{n\in\mathcal P}
  \frac{\Lambda(n)}{\sqrt n}J_{L,\log n}
 \leq
 \frac{(1+2\varepsilon)^2}{2}
 \left(\frac{2\pi}{L}\right)^2
 \{M_{\Gamma,2}+M_2(\mathcal P)\}.}
 \tag{32}
\]

For every fixed \(\mathcal P\), the right side tends to zero. More
explicitly, (22) is strictly larger than (32) whenever

\[
 \boxed{
 L^2>
 \frac{32\pi^2(1+2\varepsilon)^2}
      {\varepsilon^3}
 \{M_{\Gamma,2}+M_2(\mathcal P)\}.}
 \tag{33}
\]

Taking \(\mathcal P=\{2\}\) or \(\mathcal P=\{2,3\}\) proves the
announced literal one-prime and two-prime failures. In these two cases

\[
 M_2(\{2\})=\frac{(\log2)^3}{\sqrt2},\qquad
 M_2(\{2,3\})=\frac{(\log2)^3}{\sqrt2}
                +\frac{(\log3)^3}{\sqrt3}.
 \tag{34}
\]

## 6. Failure of the full minimal Schur cost

The scalar failure above is weaker than failure of the KYP Schur
complement. The latter also fails.

Rescale \(\theta=\xi x\). The Hilbert space
\(L^2(K_Ldm_L)\), the convolution operator \(T_{K_L}\), and its kernel
\(\mathcal M_L\) then become independent of \(L\). Only

\[
 B_L=\xi\partial_\theta+\frac12
 \tag{35}
\]

depends on \(L\). Hence

\[
 v_L=B_L(K_LF_L)
 \longrightarrow v_\infty=\frac12K_LF_L
 \quad\hbox{in }L^2(K_Ldm_L).
 \tag{36}
\]

Now \(v_\infty\notin\mathcal M_L\). Indeed,

\[
 T_{K_L}v_\infty
 =\frac12K_L*(K_LF_L)\ne0
 \tag{37}
\]

by the nonzero coefficients in (20). Since \(\mathcal M_L\) is closed,

\[
 d_\varepsilon
 :=\operatorname {dist}(v_\infty,\mathcal M_L)>0.
 \tag{38}
\]

Equations (36)--(38) imply that, for all sufficiently large \(L\),

\[
 \boxed{
 \|P_{\mathcal M_L^\perp}B_LM_{K_L}F_L\|^2
 \geq\frac14d_\varepsilon^2>0.}
 \tag{39}
\]

The left side of the necessary KYP condition (10) tends to zero by (28),
whereas its right side is bounded below by (39). Thus the regularized
Schur block (8) cannot remain positive. Adding any fixed finite prime
head to the upper-left block does not help, by (31).

## 7. Why this is also a heat/hybrid-row gate

Compress the positive Gamma-plus-\(\mathcal P\) form to the exact
mean-periodic space \(\mathcal M_L\), and let \(A_L\geq0\) be its
self-adjoint operator. Put

\[
 S_L=A_L+\frac12I.
 \tag{40}
\]

On every finite Galerkin block, \(S_L\) is bounded. For every \(k\geq1\),

\[
 F_L=e^{-S_L/k}g_{L,k},\qquad
 g_{L,k}=e^{S_L/k}F_L.
 \tag{41}
\]

Thus the witness is literally a hybrid heat-core row. The inequalities in
Sections 5--6 are strict for large \(L\), so continuity of the finite
matrix heat flow makes them persist for a nonempty interval of positive
heat times. A faithful positive heat state is obtained by adding an
arbitrarily small positive matrix to \(|F_L\rangle\langle F_L|\); strict
failure again persists by continuity.

All scalar heat constraints remain valid. In particular,

\[
 Z_V(t)=\operatorname {Tr}(Ve^{-tS_L})
 \tag{42}
\]

is completely monotone, and the kernel \(Z_V(s+t)\) is totally positive.
Those properties do not alter (22), (32), or (39).

For clarity, the latter assertion follows directly from the spectral
measure.  If

\[
 Z_V(t)=\int e^{-t\lambda}\,d\nu_V(\lambda),
\]

then Andreief's identity gives, for increasing \(s_i,t_j\),

\[
 \det[Z_V(s_i+t_j)]_{i,j=1}^m
 =\frac1{m!}\int
   \det[e^{-s_i\lambda_k}]_{i,k}
   \det[e^{-t_j\lambda_k}]_{j,k}
   \prod_{k=1}^m d\nu_V(\lambda_k)\geq0.
 \tag{42a}
\]

On every ordered \(\lambda\)-simplex the two determinants have the same
sign.  Thus even the complete temporal total-positivity hierarchy is
present in the countermodel.

## 8. The exact moving-bank scale

The proof extends without change to a bank \(\mathcal P_L\) depending on
\(L\). Equation (32) shows that

\[
 \boxed{
 M_2(\mathcal P_L)=o(L^2)
 \quad\Longrightarrow\quad
 \mathfrak b_{\Gamma,*}(F_L)
 +\sum_{n\in\mathcal P_L}
  \frac{\Lambda(n)}{\sqrt n}J_{L,\log n}
 \longrightarrow0.}
 \tag{43}
\]

Therefore a necessary condition for this positive bank to balance the
fixed connection power is

\[
 \boxed{M_2(\mathcal P_L)\gtrsim L^2.}
 \tag{44}
\]

The phase of one delay is \(\xi\log n\). An individual delay which sees
the mode at order one must consequently satisfy

\[
 \boxed{\log n\asymp\xi^{-1}\asymp L.}
 \tag{45}
\]

Equation (44) is the invariant conclusion. It allows a collective growing
bank to replace one delay of size (45), but it excludes every fixed head
and every growing head whose weighted second delay moment is
\(o(L^2)\). Thus the KYP certificate, if true for the theta kernel, is
necessarily cofinal in the ordinary-prime bank.

## 9. Scope and surviving physical theorem

The periodic kernel (13) is not Riemann's theta kernel. In particular,
its far translations do not have the double-exponential theta overlap
which makes the complete Riemann prime bank summable. No conclusion about
the truth or falsity of the physical surplus follows from this model.

What the theorem proves is a noncircular exclusion of a whole mechanism:

* exact mean periodicity does not cancel the connection;
* Gamma does not dominate it by a universal KYP inequality;
* the first prime, or the first two primes, do not repair the domination;
* heat/hybrid regularization does not add a sign;
* no fixed finite delay head can be the missing certificate.

The surviving Riemann-specific target must keep the moving ordinary-prime
bank, Gamma, theta and the polar/outgoing channel coupled before the Schur
complement. In the notation of 106.133, it remains the joint estimate

\[
 \mathfrak b_{\Gamma,*}(F/h)
 +2\eta_{\rm phys}\operatorname {Re}
   \langle F,\mathcal C_{K,h}F\rangle_{\omega_K}
 +\mathfrak P_{\rm PNT}(F)\geq0,
 \tag{46}
\]

but (43)--(45) show that its proof must be cofinal rather than a finite
local-cell or fixed-head argument.
