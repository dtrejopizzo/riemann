# 106.24 — Exact PSWF endpoint identities and the exterior \(H^1\) budget

## Purpose and prior-art audit

This note isolates what the fixed-order prolate asymptotic actually gives at
the moving endpoint.  It also computes an exact first-Sobolev leakage
identity.  The calculation is performed in the Fourier normalization used in
106.12,

\[
 \widehat f(\xi)=\int_{\mathbb R}f(x)e^{-2\pi i x\xi}\,dx.
 \tag{1}
\]

A semantic search through Phases 1--106, Papers 36 and 39, and the local CCM
sources found the following earlier ingredients:

1. the compressed-Fourier eigenvalue equation and the scalar
   Slepian--Fuchs defect asymptotic in 106.12(24), (37);
2. the open BV/moment-transfer obligation in E101.053;
3. rank-two commutators for the CCM periodic derivative.

It did **not** find the endpoint Hadamard identity below, the
concentration--position commutator below, or the resulting exterior
\(H^1\) identity.  The CCM rank-two commutator is a different operator and
does not duplicate this calculation.

There is one important source boundary.  The scalar equivalence

\[
 d_j(\lambda)\asymp
 \lambda^{2j+1}e^{-4\pi\lambda^2}
 \tag{2}
\]

cannot by itself be differentiated.  The needed endpoint estimate is instead
imported directly from the primary fixed-order calculation of Slepian,
*Prolate Spheroidal Wave Functions, Fourier Analysis and Uncertainty---IV*,
Bell System Technical Journal **43** (1964),
[doi:10.1002/j.1538-7305.1964.tb01037.x](https://doi.org/10.1002/j.1538-7305.1964.tb01037.x),
equations (89), the displayed
endpoint asymptotic immediately before (91), (93), and the one-dimensional
reduction in Section VII.  Thus no derivative of (2) is used below.

## 1. Normalization

Let

\[
 I_\lambda=[-\lambda,\lambda],\qquad
 P_\lambda={\bf1}_{I_\lambda},
 \tag{3}
\]

and let \(\psi_{j,\lambda}\) be a real, \(L^2(I_\lambda)\)-normalized,
even prolate mode in the Fourier (+1) sector.  Extend it by zero outside
\(I_\lambda\).  Thus

\[
 P_\lambda\mathcal F P_\lambda\psi_{j,\lambda}
   =\chi_j(\lambda)\psi_{j,\lambda},
 \qquad 0<\chi_j(\lambda)<1,
 \tag{4}
\]

and put

\[
 \alpha_j(\lambda)=\chi_j(\lambda)^2,
 \qquad d_j(\lambda)=1-\alpha_j(\lambda).
 \tag{5}
\]

The concentration operator

\[
 K_\lambda
 =P_\lambda\mathcal F^*P_\lambda\mathcal F P_\lambda
 \tag{6}
\]

has kernel

\[
 K_\lambda(x,y)
 =\frac{\sin(2\pi\lambda(x-y))}{\pi(x-y)}
 \tag{7}
\]

and \(K_\lambda\psi_{j,\lambda}=\alpha_j\psi_{j,\lambda}\).
The additive Fourier leakage is

\[
 r_{j,\lambda}=(1-P_\lambda)\widehat\psi_{j,\lambda},
 \qquad \|r_{j,\lambda}\|_2^2=d_j(\lambda).
 \tag{8}
\]

Every derivative norm of \(r_{j,\lambda}\) below is the componentwise
Sobolev norm on the open exterior
\((-\infty,-\lambda)\cup(\lambda,\infty)\); it does not include the boundary
delta created by differentiating the sharp indicator.

Under the unitary scaling

\[
 c=2\pi\lambda^2,
 \qquad
 \varphi_{j,c}(t)=\lambda^{1/2}\psi_{j,\lambda}(\lambda t),
 \quad -1\le t\le1,
 \tag{9}
\]

\(\varphi_{j,c}\) has unit norm on \([-1,1]\), and \(\alpha_j\) is the
standard eigenvalue of the sinc concentration operator \(\mathcal Q_c\).

## 2. Exact endpoint and boundary-slope identities

### Theorem 1 — Hadamard endpoint identity in the physical scale

For every simple prolate branch,

\[
 \boxed{
 \frac{d}{d\lambda}\log\alpha_j(\lambda)
 =4|\psi_{j,\lambda}(\lambda)|^2.}
 \tag{10}
\]

Equivalently,

\[
 \boxed{
 |\psi_{j,\lambda}(\lambda)|^2
 =-\frac{d_j'(\lambda)}{4(1-d_j(\lambda))}.}
 \tag{11}
\]

#### Proof

For the standard normalization (9), the Hadamard--Fuchs identity is

\[
 \partial_c\log\alpha_j(c)
 =\frac{2|\varphi_{j,c}(1)|^2}{c}.
 \tag{12}
\]

It also follows directly by differentiating the simple eigenvalue of the
sinc kernel.  Since

\[
 \frac{dc}{d\lambda}=4\pi\lambda,
 \qquad
 |\varphi_{j,c}(1)|^2
 =\lambda|\psi_{j,\lambda}(\lambda)|^2,
\]

(12) becomes (10).  Equation (11) follows from
\(\alpha_j=1-d_j\).  Notice that the moving-domain normalization is already
included in (12); counting four boundary faces without differentiating the
normalization would give an erroneous factor two. \(\square\)

Let \(\mu_j(\lambda)\) denote the eigenvalue of the physical prolate wave
operator

\[
 PW_\lambda
 =-\partial_x\bigl((\lambda^2-x^2)\partial_x\bigr)
   +(2\pi\lambda x)^2.
 \tag{13}
\]

### Theorem 2 — Exact endpoint slope

At the right endpoint,

\[
 \boxed{
 \psi_{j,\lambda}'(\lambda)
 =\frac{\mu_j(\lambda)-4\pi^2\lambda^4}{2\lambda}
   \psi_{j,\lambda}(\lambda).}
 \tag{14}
\]

For every fixed \(j\),

\[
 0\le \mu_j(\lambda)\le C_j\lambda^2
 \qquad(\lambda\ge\lambda_j).
 \tag{15}
\]

#### Proof

The differential equation is

\[
 (\lambda^2-x^2)\psi''-2x\psi'
 +\bigl(\mu_j-4\pi^2\lambda^2x^2\bigr)\psi=0.
 \tag{16}
\]

Set \(x=\lambda\) to obtain (14).  Nonnegativity of \(PW_\lambda\) on
the regular interval realization gives the lower bound in (15).  For the
upper bound, choose a fixed \((j+1)\)-dimensional subspace of smooth
functions supported in \((-1,1)\).  For \(\lambda\ge1\), its Rayleigh
quotients for (13) are bounded by \(C_j\lambda^2\).  Min--max gives (15).
\(\square\)

## 3. Fixed-order endpoint asymptotics from a primary source

The exact consequence of (10) is a logarithmic derivative, but the argument
does not need to differentiate (2).  Write \(\Phi_{j,c}\) for the standard
unit-normalized PSWF on \([-1,1]\).  In Slepian's notation, the ordinary
one-dimensional even sector is obtained from the generalized radial problem
by taking \(D=1\), \(p=-1\), angular degree \(N=0\), and hence replacing the
parameter called \(N\) in the two-dimensional formulas by
\(N+p/2=-1/2\).  The ordinary mode number and the radial number are related
by \(j=2n\).  Finally, Slepian normalizes the radial function on \([0,1]\),
so the unit-normalized even extension on \([-1,1]\) is smaller by
\(2^{-1/2}\).

With these substitutions, the endpoint asymptotic displayed immediately
before Slepian's equation (91) and the concentration-defect asymptotic (93)
have the same leading constant after the factor \(2^{-1}\) from even
extension is applied.  Their ratio is therefore

\[
 \boxed{
 |\Phi_{j,c}(1)|^2
 =c\bigl(1-\alpha_j(c)\bigr)\bigl(1+o_j(1)\bigr),
 \qquad j\ \hbox{fixed and even}.}
 \tag{17}
\]

For completeness, before the one-dimensional substitution the two source
asymptotics are

\[
 \varphi_{N,n}(1)^2\sim
 \frac{\pi 2^{2N+4n+4}}
      {\Gamma(n+1)\Gamma(n+N+1)}
 c^{N+2n+2}e^{-2c},
 \tag{18}
\]

and

\[
 1-\lambda_{N,n}(c)=
 \frac{\pi 2^{2N+4n+3}}
      {\Gamma(n+1)\Gamma(n+N+1)}
 c^{N+2n+1}e^{-2c}\bigl(1+O_{N,n}(c^{-1})\bigr).
 \tag{19}
\]

The paper derives (18) from its fixed-order endpoint analysis and (19) by
integrating the exact differential identity (89).  In particular, (17) is
an endpoint theorem in the source, not a formal derivative of an
asymptotic equivalence.

The normalization factor can be checked without suppressing constants.  At
\(N=-1/2\), \(n=j/2\), the coefficient in (18), after dividing by two for
the even extension, and the coefficient in (19) are both

\[
 \frac{\pi\,2^{2j+2}}
 {\Gamma(j/2+1)\Gamma(j/2+1/2)}.
\]

Their powers of \(c\) are respectively \(j+3/2\) and \(j+1/2\), so their
ratio is exactly \(c\).

Since (9) gives
\(|\Phi_{j,c}(1)|^2=\lambda|\psi_{j,\lambda}(\lambda)|^2\) and
\(c=2\pi\lambda^2\), (17) yields, for each fixed
\(j\in\{0,4,8,12\}\),

\[
 \boxed{
 |\psi_{j,\lambda}(\lambda)|^2
 =2\pi\lambda d_j(\lambda)\bigl(1+o_j(1)\bigr).}
 \tag{20}
\]

Combining this with (14)--(15) gives

\[
 \boxed{
 |\psi_{j,\lambda}'(\lambda)|^2
 =8\pi^5\lambda^7d_j(\lambda)\bigl(1+o_j(1)\bigr).}
 \tag{21}
\]

In particular, the rigorous bounds needed below are

\[
 |\psi_{j,\lambda}(\lambda)|^2\ll_j\lambda d_j,
 \qquad
 |\psi_{j,\lambda}'(\lambda)|^2\ll_j\lambda^7d_j.
 \tag{22}
\]

Equations (10) and (20) also give the derivative bound requested by the
Hadamard route,

\[
 -d_j'(\lambda)\ll_j\lambda d_j(\lambda),
 \tag{23}
\]

but (23) is a consequence of the independently sourced endpoint asymptotic,
not of differentiating (2).

## 4. Exact exterior first-Sobolev identity

Let \(M\) denote multiplication by \(x\).  From (7),

\[
 [K_\lambda,M](x,y)
 =-\frac{\sin(2\pi\lambda(x-y))}{\pi}.
 \tag{24}
\]

For an even prolate mode, parity and (4) imply the rank-one formula

\[
 \boxed{
 [K_\lambda,M]\psi_{j,\lambda}(x)
 =-\frac{\chi_j\psi_{j,\lambda}(\lambda)}{\pi}
   \sin(2\pi\lambda x).}
 \tag{25}
\]

Indeed, the sine moment of \(\psi_j\) vanishes and its cosine moment at
frequency \(\lambda\) is
\(\widehat\psi_j(\lambda)=\chi_j\psi_j(\lambda)\).

### Theorem 3 — Exact \(H^1\) leakage formula

Put

\[
 m_{2,j}(\lambda)=\int_{-\lambda}^{\lambda}
 x^2|\psi_{j,\lambda}(x)|^2\,dx.
 \tag{26}
\]

Then

\[
 \boxed{
 \|r_{j,\lambda}'\|_2^2
 =4\pi^2d_jm_{2,j}
   -2\alpha_j\psi_{j,\lambda}(\lambda)
                   \psi_{j,\lambda}'(\lambda).}
 \tag{27}
\]

Equivalently,

\[
 \boxed{
 \|r_{j,\lambda}'\|_2^2
 =4\pi^2d_jm_{2,j}
 +\alpha_j\frac{4\pi^2\lambda^4-\mu_j}{\lambda}
       |\psi_{j,\lambda}(\lambda)|^2.}
 \tag{28}
\]

#### Proof

Plancherel and (6) give

\[
 \|r_j'\|_2^2
 =4\pi^2\langle M\psi_j,(I-K_\lambda)M\psi_j\rangle.
 \tag{29}
\]

Since \(K_\lambda\psi_j=\alpha_j\psi_j\),

\[
 (I-K_\lambda)M\psi_j
 =d_jM\psi_j-[K_\lambda,M]\psi_j.
 \tag{30}
\]

Moreover,

\[
 \int_{-\lambda}^{\lambda}x\psi_j(x)\sin(2\pi\lambda x)\,dx
 =-\frac{\widehat\psi_j'(\lambda)}{2\pi}
 =-\frac{\chi_j\psi_j'(\lambda)}{2\pi}.
 \tag{31}
\]

Substitute (25) and (31) into (29).  This gives (27), while (14)
gives (28). \(\square\)

Since \(m_{2,j}\le\lambda^2\), (15), (22), and (28) imply

\[
 \boxed{
 \|r_{j,\lambda}\|_{H^1(\mathbb R\setminus I_\lambda)}^2
 \ll_j \lambda^4d_j(\lambda).}
 \tag{32}
\]

Thus the first graph norm costs only the polynomial exponent

\[
 \boxed{p=4<8.}
 \tag{33}
\]

For a fixed finite linear combination
\(f=\sum_{j\in J}c_j\psi_{j,\lambda}\), Cauchy--Schwarz gives

\[
 \|(1-P_\lambda)\widehat f\|_{H^1}^2
 \ll_J \lambda^4\sum_{j\in J}|c_j|^2d_j.
 \tag{34}
\]

Applied to the first constrained vector of 106.12, the coefficients are
\(c_0,c_4=O(1)\), \(c_8=O(\lambda^{-8})\), and hence

\[
 \|(1-P_\lambda)\widehat f_\lambda^{(0)}\|_{H^1}^2
 \ll \lambda^4d_4.
 \tag{35}
\]

The analogous second constrained vector on modes \(0,4,8,12\) satisfies

\[
 \|(1-P_\lambda)\widehat f_\lambda^{(1)}\|_{H^1}^2
 \ll \lambda^4d_8.
 \tag{36}
\]

These losses fit strictly inside the relaxed \(p<8\) budget of 106.23.

## 5. What this does and does not close

The result is a genuine improvement over the \(L^2\)-only angle identity:
the raw additive Fourier leakage has one full derivative at polynomial cost
\(\lambda^4\), not at the forbidden square-root leakage scale.

It does **not** yet prove

\[
 |QW(R^+,R^+)|\ll\lambda^p d_4.
 \tag{37}
\]

The reason is the same one isolated in 106.12(49)--(54): \(R^+\) is obtained
after the co-Poisson map and multiplicative inversion.  The co-Poisson map
contains Mellin multiplication by \(\zeta\), and no previously proved
bounded map sends the constrained additive exterior \(H^1\) norm in (35) to the complete
Weil sampling norm.  Establishing that transfer would be the arithmetic
diagonal theorem, not a consequence of prolate endpoint analysis alone.

The exact outcome is therefore:

\[
\begin{array}{c|c}
\text{statement}&\text{status}\\ \hline
\partial_\lambda\log\chi_j^2=4|\psi_j(\lambda)|^2
  &\text{proved exactly}\\
\psi_j'(\lambda)=\frac{\mu_j-4\pi^2\lambda^4}{2\lambda}\psi_j(\lambda)
  &\text{proved exactly}\\
\text{exterior }H^1\text{ identity (27)}
  &\text{proved exactly}\\
\|r_j\|_{H^1}^2\ll\lambda^4d_j
  &\text{proved from Slepian IV's independent endpoint asymptotic}\\
H^1\text{ additive leakage}\to QW\text{ co-Poisson leakage}
  &\text{open arithmetic transfer}.
\end{array}
\tag{38}
\]

## 6. Dilation/Mellin audit: an exact endpoint obstruction

The first additive derivative in (32) must not be confused with a graph norm
for the multiplicative dilation generator.  Let \(f\) be even and smooth on
\([-\lambda,\lambda]\), and extend it sharply by zero.  Repeated integration
by parts gives, as \(t\to+\infty\),

\[
 \widehat f(t)
 =\frac{f(\lambda)\sin(2\pi\lambda t)}{\pi t}
  +\frac{f'(\lambda)\cos(2\pi\lambda t)}{2\pi^2t^2}
  +O_{f,\lambda}(t^{-3}),
 \tag{39}
\]

and a direct integration by parts applied to
\(\widehat f'(t)=-2\pi i\widehat{xf}(t)\) gives

\[
 \boxed{
 t\partial_t\widehat f(t)
 =2\lambda f(\lambda)\cos(2\pi\lambda t)
  +O_{f,\lambda}(t^{-1}).}
 \tag{40}
\]

Consequently, if \(f(\lambda)\ne0\), then

\[
 t\partial_t\widehat f
 \notin L^2((\lambda,\infty),dt),
 \qquad
 t\partial_t\widehat f
 \notin L^2((\lambda,\infty),d^*t).
 \tag{41}
\]

The second assertion follows from
\(\int_R^T\cos^2(2\pi\lambda t)\,d^*t
=\tfrac12\log(T/R)+O_\lambda(1)\).

This obstruction applies to every individual fixed prolate mode by (20).
It also applies to the first constrained vector of 106.12.  Indeed, the
coefficient asymptotics recorded in 106.26(25) give
\(c_4\to c_4^\infty\ne0\), \(c_8=O(\lambda^{-8})\), and the endpoint
hierarchy from (20) and the fixed-order defects is

\[
 \left|\frac{\psi_0(\lambda)}{\psi_4(\lambda)}\right|
 =O(\lambda^{-4}),\qquad
 \left|\frac{\psi_8(\lambda)}{\psi_4(\lambda)}\right|
 =O(\lambda^4).
 \tag{42}
\]

Hence
\[
 f_\lambda^{(0)}(\lambda)
 =c_4^\infty\psi_{4,\lambda}(\lambda)
   \bigl(1+O(\lambda^{-4})+o(1)\bigr)\ne0
\]
for all sufficiently large \(\lambda\).  There can therefore be no estimate
of the form

\[
 \|t\partial_t(1-P_\lambda)\widehat
 f_\lambda^{(0)}\|_{L^2(d^*t)}
 \le \lambda^A\sqrt{d_4}
\]
for any finite \(A\): the norm on the left is infinite.

For an individual prolate mode, the exterior Fourier continuation also
satisfies

\[
 \bigl((t^2-\lambda^2)\widehat f'(t)\bigr)'
 +(4\pi^2\lambda^2t^2-\mu)\widehat f(t)=0,
 \qquad t>\lambda,
\]
whose outgoing oscillatory branch has precisely the \(t^{-1}\) carrier in
(39).  The prolate ODE thus identifies, rather than removes, the dilation
obstruction.

This does not refute the two-orientation Fuchs--Mellin carrier estimate of
106.26.  The boundary carriers in (39) are small enough for that estimate
after oscillatory Mellin evaluation.  What remains uncontrolled there is
the co-Poisson image of the interior remainder

\[
 -\frac1{2\pi^2t^2}
 \int_0^\lambda f_\lambda''(x)\cos(2\pi tx)\,dx,
\]

with the two Mellin orientations and their zeta-zero cancellations kept
together.  A standard dilation Sobolev norm cannot supply that cancellation.
