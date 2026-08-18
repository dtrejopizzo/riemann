# 106.64 — The mean-periodic quotient operator and the signed determinant gate

## Purpose and verdict

Document 106.41 identifies the remaining operator as the compression of

\[
L-\frac12
\]

to the orthogonal complement of the constant and of the complete Riemann
radical.  Document 106.43 identifies that complement, after multiplication
by \(h(x)=\cosh(x/2)\), with the mean-periodic equation \(F*K=0\).  This note
performs the resulting operator calculation explicitly.

There are three exact conclusions.

1.  In the \(F=hq\) coordinate the compressed operator is a renormalized
    weighted convolution by the complete ordinary-prime--Gamma measure.
    No abstract projection remains in its action, because the mean-periodic
    subspace is reducing.
2.  On exponential mean-periodic modes its matrix is a Toeplitz--Hankel
    evaluation kernel built from \(\widehat{K/h}\).  This is the complete
    all-atom version of the finite-head kernel in 106.62.
3.  The natural determinant factorization is exactly a Birman--Schwinger
    determinant for the negative Krein channel of 106.37.  Its nonvanishing
    is equivalent to the desired quotient floor.  If an off-line orbit
    exists, that channel is accessible after exact radical projection and
    the determinant has a zero.  Thus the determinant supplies no new sign;
    it locates the remaining obstruction without hiding it.

No zero-location statement is assumed in deriving the operator or the
determinant identities.

## 1. The unitary mean-periodic coordinate

Recall

\[
h(x)=\cosh(x/2),\qquad c_K=\frac12,
\qquad d\mu_K(x)=\frac{h(x)K(x)}{c_K}\,dx.          \tag{1}
\]

Define

\[
d\omega_K(x)=\frac{K(x)}{c_Kh(x)}\,dx,
\qquad (Wq)(x)=h(x)q(x).                            \tag{2}
\]

Then \(W:L^2(\mu_K)\to L^2(\omega_K)\) is unitary, since

\[
\|Wq\|_{L^2(\omega_K)}^2
=\frac1{c_K}\int |hq|^2\frac K h\,dx
=\|q\|_{L^2(\mu_K)}^2.                             \tag{3}
\]

Let

\[
d\nu_\zeta(u)=
\frac{e^{-u/2}}{1-e^{-2u}}\,du
+\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}
 \delta_{\log n}(du),\qquad u>0,                   \tag{4}
\]

and denote by \(\widetilde\nu_\zeta\) its even bilateral extension:

\[
\int_{\mathbb R\setminus\{0\}}a(v)\,
d\widetilde\nu_\zeta(v)
=\int_0^\infty\{a(u)+a(-u)\}\,d\nu_\zeta(u).     \tag{5}
\]

Let

\[
\mathcal N_K
=\{F\in L^2(\omega_K):F*K=0\}                   \tag{6}
\]

on the analytic mean-periodic form domain of 106.43.  The convolution
equation includes the zeroth radical moment, so \(W^{-1}F\) is centered.
Consequently

\[
W(\mathbf1\oplus\mathcal R)^\perp=\mathcal N_K.    \tag{7}
\]

The constant must be removed in (7).  Compressing only away from
\(\mathcal R\) would leave the constant eigenvector, on which
\(L-1/2=-1/2\).

## 2. Exact integral action of the quotient operator

Put

\[
\mathcal A=W\left(L-\frac12\right)W^{-1}.           \tag{8}
\]

### Theorem 1 — Renormalized all-atom convolution formula

On the smooth analytic core,

\[
\boxed{
\begin{aligned}
(\mathcal AF)(x)
={}&c_K\int_{\mathbb R\setminus\{0\}}
 K(x-v)
 \left\{
 \frac{F(x)}{h(x)}-
 \frac{F(x-v)}{h(x-v)}
 \right\}
 d\widetilde\nu_\zeta(v)\\
&-\frac12F(x).
\end{aligned}}                                      \tag{9}
\]

The Gamma integral in (9) is a difference integral.  Its two terms may
not be separated: each separated diagonal/off-diagonal Gamma integral has
a logarithmic divergence at \(v=0\).

Moreover, \(\mathcal N_K\) reduces \(\mathcal A\).  Hence the operator
requested after exact shorting is simply

\[
\boxed{T_F=\mathcal A|_{\mathcal N_K};}              \tag{10}
\]

there is no residual projection in (9).

#### Proof

Substitute \(q=F/h\) in 106.41(7) and multiply the result by \(h(x)\).
The two orientations of each displacement combine exactly into (5), which
gives (9).  Near zero the Gamma density is \((2|v|)^{-1}+O(1)\), whereas
the difference of a smooth \(F/h\) is \(O(|v|)\), so the joint integral is
locally finite.

The self-adjoint generator satisfies

\[
L1=0,\qquad
L\{r_j-\mu_K(r_j)\}
=\frac12\{r_j-\mu_K(r_j)\}.                         \tag{11}
\]

Therefore the closed eigenspace \(\mathbf1\oplus\mathcal R\) and its
orthogonal complement are reducing for \(L\).  Conjugating by \(W\) and
using (7) proves (10).  In particular, (9) obeys the nontrivial invariance
identity

\[
F*K=0\quad\Longrightarrow\quad(\mathcal AF)*K=0.   \tag{12}
\]
\(\square\)

The polarized quadratic form of (10) is

\[
\boxed{
\begin{aligned}
\mathfrak a(F,G)
={}&\int_0^\infty\!\int_{\mathbb R}
 K(x)K(x-u)
 \overline{\Delta_u(F/h)(x)}
 \Delta_u(G/h)(x)\,dx\,d\nu_\zeta(u)\\
&-\frac1{2c_K}\int_{\mathbb R}
 \frac{K(x)}{h(x)}\overline{F(x)}G(x)\,dx,
\qquad F,G\in\mathcal N_K.
\end{aligned}}                                      \tag{13}
\]

Formula (13) contains every literal von Mangoldt atom and the complete
Gamma density before any sign is requested.

## 3. Why mean periodicity does not diagonalize (9)

Put

\[
w(x)=\frac{K(x)}{h(x)},\qquad \Phi(z)=\widehat w(z). \tag{14}
\]

The physical Weil test associated with \(F\) is

\[
f=Kq=wF.                                             \tag{15}
\]

The constraint in (6) controls \(\widehat F\), whereas both the explicit
formula and the off-diagonal part of (9) act on \(wF\).  In Fourier
coordinates,

\[
\widehat{wF}=\widehat w*\widehat F.                 \tag{16}
\]

Thus point support of \(\widehat F\) on the zero divisor is spread by the
entire function \(\Phi\).  This is the exact reason that the equation
\(F*K=0\) does not turn (9) into scalar multiplication.

For a zero \(z\) of \(\Xi\), define

\[
F_z(x)=\cos(zx),\qquad q_z=F_z/h,
\qquad f_z=wF_z.                                     \tag{17}
\]

Then

\[
\boxed{
\widehat f_z(s)=B(s,z),\qquad
B(s,z):=\frac12\{\Phi(s-z)+\Phi(s+z)\}.}           \tag{18}
\]

The first term in (18) is of Toeplitz difference type and the second is of
Hankel sum type.

### Theorem 2 — Complete zero-divisor Toeplitz--Hankel kernel

For zeros \(z,w\) of \(\Xi\), with the usual derivative jets at multiple
zeros,

\[
\boxed{
\mathcal H(z,w)
:=\langle F_z,T_FF_w\rangle_{L^2(\omega_K)}
=\sum_{s\in\mathcal Z}
 \overline{B(\overline s,z)}B(s,w).}                \tag{19}
\]

The zero sum is taken with the symmetric convention and multiplicities of
the Weil formula.  Equivalently,

\[
\overline{B(\overline s,z)}
=B(s,\overline z).                                  \tag{20}
\]

#### Proof

The full-kernel identity 106.31 gives, for centered complement vectors,

\[
\mathfrak a(F,G)=QW(wF,wG).                          \tag{21}
\]

Apply the polarized explicit formula

\[
QW(f,g)=\sum_{s\in\mathcal Z}
 \overline{\widehat f(\overline s)}\widehat g(s)   \tag{22}
\]

and substitute (18).  This proves (19).  Differentiating in \(z,w\)
gives the multiplicity jets.  \(\square\)

For a finite exponential polynomial

\[
F=\sum_{j=1}^da_j\cos(z_jx),                        \tag{23}
\]

formula (19) is exactly the complete all-atom Gram matrix in 106.62.  It
is not automatically positive: the conjugation pattern in (22), rather
than an ordinary Hilbert Gram product, is decisive.

## 4. Exact Krein decomposition of the quotient operator

Use the orbit notation of 106.37.  On real even \(F\in\mathcal N_K\), set

\[
\begin{aligned}
(\mathcal B_0F)_\gamma
 &=\sqrt{2m_\gamma}\,\widehat{wF}(\gamma),\\
(\mathcal B_+F)_s
 &=2\sqrt{m_s}\,\operatorname {Re}\widehat{wF}(s),\\
(\mathcal B_-F)_s
 &=2\sqrt{m_s}\,\operatorname {Im}\widehat{wF}(s),
\end{aligned}                                       \tag{24}
\]

where \(\gamma\) runs through critical pairs and \(s\) through chosen
off-line orbit representatives.  Equations (21)--(22) give, as closed
quadratic forms on the mean-periodic complement,

\[
\boxed{
T_F=\mathcal B_0^*\mathcal B_0
   +\mathcal B_+^*\mathcal B_+
   -\mathcal B_-^*\mathcal B_-.}                   \tag{25}
\]

Thus restricting the physical all-prime--Gamma operator to \(F*K=0\)
does not remove the negative evaluation channel.  It transports that
channel through the smoothing map \(F\mapsto wF\).

## 5. The determinant calculation

Let \(E\subset\mathcal N_K\) be a finite-dimensional subspace of the
common form core, and compress all operators below to \(E\).  Write

\[
G_E=(\mathcal B_0|_E)^*\mathcal B_0|_E
    +(\mathcal B_+|_E)^*\mathcal B_+|_E,
\qquad
C_E=(\mathcal B_-|_E)^*\mathcal B_-|_E.             \tag{26}
\]

Then \(T_E=G_E-C_E\).  For every \(\kappa>0\), the matrix determinant
lemma and Sylvester's identity give

\[
\boxed{
\frac{\det_E(T_E+\kappa I)}
     {\det_E(G_E+\kappa I)}
=\det\!\left[
 I-\mathcal B_-|_E(G_E+\kappa I)^{-1}
      (\mathcal B_-|_E)^*
 \right].}                                          \tag{27}
\]

The determinant on the right is a finite-rank Fredholm determinant in the
negative-channel sequence space.  Define

\[
\mathcal K_{E,\kappa}
=\mathcal B_-|_E(G_E+\kappa I)^{-1}
 (\mathcal B_-|_E)^*.                               \tag{28}
\]

Then

\[
\boxed{
-\kappa\in\sigma(T_E)
\quad\Longleftrightarrow\quad
1\in\sigma(\mathcal K_{E,\kappa}).}                \tag{29}
\]

Likewise,

\[
T_E\ge0
\quad\Longleftrightarrow\quad
C_E\le G_E
\quad\Longleftrightarrow\quad
\|\mathcal K_{E,\kappa}\|\le1
\ \text{for every }\kappa>0.                       \tag{30}
\]

Equations (27)--(30) are exact.  They do not prove (30): the requested
contraction is precisely the comparison of the negative Krein channel
with the two positive channels.

The corresponding trace identity is equally transparent.  For every
finite-rank projection \(P\) in the form core,

\[
\boxed{
\operatorname {Tr}(PT_F)
=\|\mathcal B_0P\|_{\mathrm {HS}}^2
 +\|\mathcal B_+P\|_{\mathrm {HS}}^2
 -\|\mathcal B_-P\|_{\mathrm {HS}}^2.}             \tag{31}
\]

Thus neither the determinant nor the trace converts the signed channel
into a positive one.

## 6. Exact reappearance of an off-line orbit

The determinant obstruction is not merely formal.

### Theorem 3 — Off-line channel produces a negative quotient state

If \(\Xi\) has an off-line orbit, then there exists
\(F\in\mathcal N_K\) in the form domain such that

\[
\boxed{\langle F,T_FF\rangle_{\omega_K}<0.}          \tag{32}
\]

Consequently \(T_F\) has a negative isolated eigenvalue, and for a
suitable finite-dimensional compression and \(\kappa>0\), the determinant
in (27) vanishes.

#### Proof

The interpolation theorem in 106.37 produces a real even compactly
supported Weil test \(f\) with \(QW(f,f)<0\), concentrated in the negative
evaluation channel of one selected off-line orbit.  Since \(K>0\), put
\(q=f/K\), which belongs to the compact form core.  Decompose

\[
q=q_\parallel+q_\perp,
\qquad q_\parallel\in\mathbf1\oplus\mathcal R,
\quad q_\perp\in(\mathbf1\oplus\mathcal R)^\perp.   \tag{33}
\]

The constant and threshold-radical components have zero Weil value and
are polarized-orthogonal to every Weil test.  Hence

\[
QW(Kq_\perp,Kq_\perp)=QW(f,f)<0.                    \tag{34}
\]

Set \(F=hq_\perp\).  Equations (7) and (21) give \(F\in\mathcal N_K\)
and (32).  By 106.47, the essential spectrum of \(T_F\) is contained in
\([0,\infty)\); a negative form value therefore produces a negative
isolated eigenvalue.  Galerkin approximation in the form norm gives a
finite-dimensional compression with a negative eigenvalue, and (29)
gives the determinant zero.  \(\square\)

Conversely, if RH holds, there is no off-line orbit, so
\(\mathcal B_-=0\) and (25) is nonnegative.  Therefore

\[
\boxed{
T_F\ge0
\quad\Longleftrightarrow\quad
\mathcal B_-=0
\quad\Longleftrightarrow\quad
\mathrm {RH}.}                                      \tag{35}
\]

## 7. Audit against 106.37

The physical formula (9) is useful: it displays exactly where every
ordinary \(\Lambda(n)\) and the Gamma measure enter the quotient operator.
The Toeplitz--Hankel formula (19) is also useful: it is the explicit matrix
of that operator on the mean-periodic spectral-synthesis space.

However, the sign factorization (25) is not a new factorization beyond
106.37.  It is precisely the 106.37 Krein factorization restricted to the
image

\[
f=wF,\qquad F*K=0.                                  \tag{36}
\]

The determinant in (27) therefore asks whether the negative evaluation
map is contractively absorbed by the positive evaluation maps.  This is
the same unresolved absorption inequality, not an independent consequence
of determinant analyticity or of the positivity of the coefficients in
\(\nu_\zeta\).

The exact equation where the off-line channel reappears is

\[
\boxed{
\mathcal K_{E,\kappa}
=\mathcal B_-|_E
 \left(
 (\mathcal B_0|_E)^*\mathcal B_0|_E
 +(\mathcal B_+|_E)^*\mathcal B_+|_E
 +\kappa I
 \right)^{-1}
 (\mathcal B_-|_E)^*.}                              \tag{37}
\]

Proving \(\|\mathcal K_{E,\kappa}\|<1\) uniformly is exactly the missing
signed prime--Gamma theorem.  The mean-periodic equation and the
determinant do not supply that inequality: an off-line divisor makes the
left side reach the eigenvalue one.

## 8. Status

The quotient operator requested after exact radical shorting has now been
written both in its literal physical form (9) and in its complete
zero-divisor Toeplitz--Hankel form (19).  The only natural determinant
factorization is (27), and its obstruction is the explicit negative-channel
operator (37).

Accordingly, this route does not prove the quotient floor.  It proves that
any successful determinant argument must establish a genuinely new bound
on (37) from the coupled physical formula (9).  Merely constructing the
determinant, invoking its analyticity, or using the equation \(F*K=0\)
reproduces the Krein negative channel and is tautological with respect to
RH.
