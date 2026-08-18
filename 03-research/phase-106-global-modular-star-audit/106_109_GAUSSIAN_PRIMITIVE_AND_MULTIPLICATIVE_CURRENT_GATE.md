# 106.109 — The Gaussian primitive and the multiplicative-current gate

## 1. Purpose and verdict

The theta atom has two elementary factorizations which have not yet been
used simultaneously:

\[
 k_y=\frac12(D^2-\tfrac14)f_y,
 \qquad
 \phi(y)=-\pi\frac d{dy}\{y^3e^{-\pi y^2}\}.
\]

This note pushes the second factorization through the *complete* physical
displacement measure, before separating primes, Gamma or the pole.  It
gives an exact multiplicative normal form.  In that form all three sources
are represented by the single signed measure

\[
 \boxed{
 d\eta(z)=\sum_{n\ge2}\Lambda(n)\delta_n(dz)
 +\left\{-1+\frac1{z(z^2-1)}\right\}dz,
 \qquad z>1.}                                      \tag{1}
\]

After the farther theta endpoint is expanded, summation by parts moves the
Gaussian derivative onto a strictly positive curvature.  The complete
sign is then carried by one weighted cumulative of \(\eta\).  This is a
genuine exact reduction of the primitive calculation.

It is not a positive-square proof.  The required cumulative is already
negative before the first prime atom, even for the quadratic increment
\((\log z)^2\).  More generally a smooth physical increment can be
localized inside \((4/3,2)\), where the completed Gamma--pole density in
(1) is strictly negative and there is no prime atom.  Thus neither the
Gaussian primitive nor summation by parts produces a fiberwise positive
square.  There is no omitted endpoint term which Gamma or the pole can
later cancel: both are already present in (1), and the endpoint terms
vanish.

The surviving statement is a *global alignment inequality* for the signed
cumulatives after summing the same-side and central fibers.  On heat rows
that statement is exactly the physical surplus of 106.102--106.103.

No zero location is used below.

## 2. Gaussian primitive, Sturm factor and self-duality

For \(y\ge0\), put

\[
 f_y(x)=e^{x/2}e^{-\pi y^2e^{2x}},
 \qquad
 P(y)=y^3e^{-\pi y^2},
 \tag{2}
\]

and let \(D=d/dx\).  Direct differentiation gives

\[
 \boxed{
 k_y(x)=\frac12(D^2-\tfrac14)f_y(x)
 =e^{x/2}\phi(ye^x),}                              \tag{3}
\]

where

\[
 \boxed{
 \phi(y)=\pi y^2(2\pi y^2-3)e^{-\pi y^2}
 =-\pi P'(y).}                                     \tag{4}
\]

With the Fourier convention
\(\widehat g(\xi)=\int_{\mathbb R}g(y)e^{-2\pi i y\xi}\,dy\), one also
has

\[
 \boxed{\widehat\phi=\phi.}                       \tag{5}
\]

Indeed,

\[
 \widehat{y^2e^{-\pi y^2}}
 =\left(\frac1{2\pi}-\xi^2\right)e^{-\pi\xi^2},
\]

and

\[
 \widehat{y^4e^{-\pi y^2}}
 =\left(\xi^4-\frac3\pi\xi^2+\frac3{4\pi^2}\right)
 e^{-\pi\xi^2}.
\]

Substitution in (4) proves (5).

Let

\[
 \mathcal F(x)=\sum_{m\in\mathbb Z}f_{|m|}(x).
 \tag{6}
\]

Poisson summation and (5) show that \(\mathcal F\) is even.  Since the
\(m=0\) term is annihilated by \(D^2-1/4\),

\[
 \boxed{K=\frac14(D^2-\tfrac14)\mathcal F.}        \tag{7}
\]

This identity includes the polar primitive, but it is not an \(L^2\)
ground-state factorization: \(\mathcal F(x)\sim e^{|x|/2}\).  In
particular,

\[
 \int_{-R}^{R}\mathcal F(D^2-\tfrac14)\mathcal F
 =[\mathcal F\mathcal F']_{-R}^{R}
 -\int_{-R}^{R}\left\{|\mathcal F'|^2+	frac14|\mathcal F|^2\right\},
 \tag{8}
\]

and the boundary in (8) is of order \(e^R\), not zero.  This is the first
reason why the local Sturm/Hardy sign does not follow from (7).

There is also an exact lattice summation-by-parts formula.  If
\(\widetilde B_1(t)=\{t\}-1/2\), then Euler summation, together with
\(\int_0^\infty\phi=\phi(0)=0\), gives

\[
 \boxed{
 \sum_{m\ge1}\phi(mh)
 =-\int_0^\infty\widetilde B_1(y/h)\phi'(y)\,dy
 =\pi\int_0^\infty\widetilde B_1(y/h)P''(y)\,dy.} \tag{9}
\]

Thus the continuum zero mode contributes no positive main term: the whole
theta sum is the signed Bernoulli remainder.  Formula (5) equivalently
gives

\[
 \sum_{m\ge1}\phi(mh)
 =h^{-1}\sum_{m\ge1}\phi(m/h).                    \tag{10}
\]

Equations (9)--(10) are the mass-level Poisson identity of 106.107 in
primitive form.  The kernel in (9) changes sign on every lattice cell.

## 3. One multiplicative measure for primes, Gamma and the pole

Retain the compensated displacement measure of 106.66,

\[
 d\sigma(u)=
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\delta_{\log n}(du)
 +\left\{\frac{e^{-u/2}}{1-e^{-2u}}-2\cosh(u/2)\right\}du.
 \tag{11}
\]

### Theorem 1 — Exact multiplicative pushforward

For every test \(F\) for which the pairing exists and which is
\(O(u^2)\) at the origin,

\[
 \boxed{
 \int_0^\infty F(u)e^{u/2}\,d\sigma(u)
 =\int_{(1,\infty)}F(\log z)\,d\eta(z),}           \tag{12}
\]

where \(\eta\) is (1).

#### Proof

At \(u=\log n\), multiplication by \(e^{u/2}\) changes
\(\Lambda(n)n^{-1/2}\) into \(\Lambda(n)\).  In the continuous part,
put \(z=e^u\).  Then

\[
 e^{u/2}left\{\frac{e^{-u/2}}{1-e^{-2u}}
 -2\cosh(u/2)\right\}du
 =\left\{-1+\frac1{z(z^2-1)}\right\}dz.
\]

The density is \(1/(2(z-1))+O(1)\) at \(z=1\), and the assumed double
zero of \(F\) makes the integral ordinary and finite.  This proves (12).
\(\square\)

The transformation is scale-free: the same \(\eta\) occurs above every
theta index.  It is also completely literal.  The atoms are precisely the
ordinary von Mangoldt weights, while the two continuous terms are exactly
Gamma and the polar threshold.

## 4. Exact farther-endpoint expansion of the complete form

For an even multiplier \(r\), set

\[
 W_y^+(z)=|r(y+\log z)-r(y)|^2,                    \tag{13}
\]

and

\[
 W_x^-(z)=|r(x)-r(\log z-x)|^2.                   \tag{14}
\]

The continuous theta scaling gives

\[
 K(y+u)=e^{u/2}\sum_{m\ge1}k_{e^um}(y),           \tag{15}
\]

and, when \(0\le x\le u\),

\[
 K(u-x)=e^{u/2}\sum_{m\ge1}k_{e^um}(-x).          \tag{16}
\]

Every atom on the right of (15)--(16) is positive on the displayed
domain.

### Theorem 2 — Complete multiplicative theta normal form

Writing

\[
 Q(r)=\int_0^\infty J_u(r)\,d\sigma(u),            \tag{17}
\]

one has \(Q=Q^++Q^-\), where

\[
 \boxed{
 Q^+(r)=2\int_0^\infty K(y)\sum_{m\ge1}
 \int_{(1,\infty)} k_{mz}(y)W_y^+(z)\,d\eta(z)\,dy} \tag{18}
\]

and

\[
 \boxed{
 Q^-(r)=\int_0^\infty K(x)\sum_{m\ge1}
 \int_{[e^x,\infty)} k_{mz}(-x)W_x^-(z)\,d\eta(z)\,dx.} \tag{19}
\]

The first line is the complete same-side channel, and the second is the
complete central-crossing channel.  No divisible, fractional, Gamma or
polar term has been omitted.

#### Proof

Insert the exact fold

\[
\begin{aligned}
 J_u(r)={}&2\int_0^\infty K(y+u)K(y)
 |r(y+u)-r(y)|^2\,dy\\
 &+\int_0^uK(x)K(u-x)|r(x)-r(u-x)|^2\,dx
\end{aligned}                                      \tag{20}
\]

in (17).  Use (15) in the first line, (16) in the second, and then apply
(12).  At a common finite prime/displacement cutoff the positive and
negative continuous parts are separately absolutely integrable: the
increment has a double zero at \(u=0\), and the theta series is normally
convergent.  Fubini therefore applies.  The stated identities follow by
the common-cutoff dominated limit used in 106.66 and 106.102.  \(\square\)

At a prime atom \(z=n\), (18) has farther index \(b=mn\).  Summing over
all factorizations \(b=mn\) recovers
\(\sum_{n\mid b}\Lambda(n)=\log b\) and hence the complete divisor
current and dispersion of 106.104.  Equations (18)--(19) additionally
retain the continuous Gamma--pole fibers, so they are not a
divisible-channel truncation.

## 5. Exact Gaussian summation by parts

For \(q\in\mathbb R\), define

\[
 P_q(s)=s^3e^{-\pi s^2e^{2q}}.                    \tag{21}
\]

Then

\[
 k_s(q)=-\pi e^{5q/2}P_q'(s)                      \tag{22}
\]

and

\[
 \boxed{
 P_q''(s)=2s\{2v^2-7v+3\}e^{-v},
 \qquad v=\pi s^2e^{2q}.}                         \tag{23}
\]

Since \(2v^2-7v+3=(2v-1)(v-3)\),

\[
 P_y''(mz)>0\quad(y\ge0,m\ge1,z\ge1),            \tag{24}
\]

and

\[
 P_{-x}''(mz)>0\quad(x\ge0,m\ge1,z\ge e^x).     \tag{25}
\]

For a lower endpoint \(c\ge1\), put

\[
 A_{W,c}(Z)=\int_{(c,Z]}W(z)\,d\eta(z),
 \qquad A_{W,c}(c)=0.                              \tag{26}
\]

At \(c=1\), assume \(W(z)=O((z-1)^2)\), as holds in (13).

### Theorem 3 — Primitive-current identity

On the smooth compact multiplier core,

\[
 \boxed{
 \int_{(c,\infty)}k_{mz}(q)W(z)\,d\eta(z)
 =\pi m e^{5q/2}\int_c^\infty
 P_q''(mz)A_{W,c}(z)\,dz.}                        \tag{27}
\]

Consequently, (18)--(19) become

\[
\begin{aligned}
 Q^+(r)
 ={}&2\pi\int_0^\infty K(y)e^{5y/2}
 \sum_{m\ge1}m\int_1^\infty
 P_y''(mz)A^+_y(z)\,dz\,dy,\\
 Q^-(r)
 ={}&\pi\int_0^\infty K(x)e^{-5x/2}
 \sum_{m\ge1}m\int_{e^x}^\infty
 P_{-x}''(mz)A^-_x(z)\,dz\,dx,
\end{aligned}                                      \tag{28}
\]

where

\[
 A_y^+(Z)=\int_{(1,Z]}W_y^+(z)\,d\eta(z),
 \quad
 A_x^-(Z)=\int_{(e^x,Z]}W_x^-(z)\,d\eta(z).       \tag{29}
\]

#### Proof

Let \(A=A_{W,c}\).  The left side of (27) is

\[
 -\pi e^{5q/2}\int_{(c,\infty)}P_q'(mz)\,dA(z).
\]

Stieltjes integration by parts gives (27), because
\(A(c)=0\), \(P_q'(mz)A(z)\to0\) at infinity, and
\(d(P_q'(mz))/dz=mP_q''(mz)\).  The singularity of \(\eta\) at one
produces no boundary: \(W=O((z-1)^2)\).  Insert (27) in (18)--(19) to
obtain (28).  \(\square\)

This is the exact outcome sought from the Gaussian primitive.  The
curvature in (28) is strictly positive; all undecided sign has been moved
to the weighted physical cumulatives (29).

## 6. The cumulative sign is false before the first prime

The density in (1) is

\[
 \omega(z)=-1+\frac1{z(z^2-1)}
 =-\frac{z^3-z-1}{z(z^2-1)}.                      \tag{30}
\]

Since \(z^3-z-1>0\) for \(z\ge4/3\),

\[
 \omega(z)<0\qquad(4/3\le z<2),                  \tag{31}
\]

and there is no prime-power atom in this open interval.

### Theorem 4 — Minimal completed-source counter-witness

The sufficient condition

\[
 A_{W,1}(Z)\ge0\quad\text{for every }W\ge0\text{ and every }Z>1
 \tag{32}
\]

is false for the literal completed Riemann source.  More precisely:

1. every nonzero smooth \(W\ge0\) supported in \((4/3,2)\) satisfies
   \(A_{W,1}(2^-)<0\);
2. for the quadratic increment \(W(z)=(\log z)^2\),

\[
 \boxed{A_{W,1}(2^-)<-\frac{43}{4500}<0.}          \tag{33}
\]

#### Proof

The first statement is immediate from (31).  For the second, the positive
part of the integral can only occur in \((1,4/3)\).  There,
\(\log z\le z-1\) and

\[
 \omega(z)\le\frac1{z(z^2-1)}\le\frac1{2(z-1)}.
\]

Hence its total positive contribution is at most

\[
 \int_1^{4/3}\frac{z-1}{2}\,dz=\frac1{36}.        \tag{34}
\]

On \([3/2,2]\),

\[
 \omega(z)\le-\frac7{15},
 \qquad
 \log z\ge\log(3/2)>\frac25.                     \tag{35}
\]

The logarithmic bound follows, for example, from
\(\log(1+t)\ge2t/(2+t)\) for \(t\ge0\).  Therefore the contribution of
\([3/2,2]\) is at most

\[
 -\frac7{15}\frac4{25}\frac12=-\frac{14}{375}.   \tag{36}
\]

The omitted interval \([4/3,3/2]\) is also negative.  Combining
(34)--(36) gives

\[
 A_{W,1}(2^-)
 <\frac1{36}-\frac{14}{375}
 =-\frac{43}{4500}.
\]

No atom occurs before \(2\), so this is exactly the completed cumulative,
not a truncated-prime approximation.  \(\square\)

The first witness is physically realizable at a fixed same-side fiber.
Choose \(y_0>0\), a smooth bump \(\chi\) supported in
\((\log(4/3),\log2)\), and an even smooth multiplier which satisfies
\(r(y_0)=0\) and \(r(y_0+u)=\chi(u)\) on that interval.  Then
\(W_{y_0}^+(z)=|\chi(\log z)|^2\), and its cumulative is strictly
negative.  Thus (32) cannot be rescued by restricting to spatial
increments.

This is deliberately a **fiberwise** counter-witness.  It does not show
that the complete quantity \(Q(r)\) is negative for any Riemann test.
The integrations over all theta indices and base points, and especially
the coupling of (18) with the central fibers (19), can compensate the
negative fiber.  Theorem 4 refutes the proposed local primitive-square
argument; it does not refute the global surplus.

## 7. Radical, subthreshold and prior-route audit

### 7.1 Exact radical equality

For every radical multiplier \(r_j=K^{(2j)}/K\),

\[
 Q(r_j)=0.                                          \tag{37}
\]

Equations (28)--(29) therefore give an exact cancellation among positive
and negative cumulative regions.  Replacing any \(A_y^+\) or \(A_x^-\)
by its positive part leaves a strict positive defect on a nonconstant
radical multiplier and is incompatible with (37).  The cross-divisor
dispersion at \(b=p^2\) from 106.104 is the smallest literal arithmetic
instance of the same loss.

### 7.2 Hypothetical subthreshold mode

Let \(Aq=\alpha q\) with \(0<\alpha<1/2\), and let a heat state
concentrate spectrally at \(q\).  The source-rate identity of
106.100--106.103 gives

\[
 \frac{Q[\Gamma_t]}{\mathrm{Tr}\,\Gamma_t}
 \longrightarrow\alpha-\frac12<0.                \tag{38}
\]

The trace lift of (28) is an identity, so the same negative limit appears
in its signed cumulatives.  The Gaussian primitive therefore passes the
subthreshold falsifier: it does not assign an automatic false positive
sign.  Proving that the literal Riemann heat rows cannot realize (38) is
still exactly the physical-surplus theorem.

### 7.3 Relation to the earlier Sturm/Hardy gates

The finite-order factorization in (3) does not evade the Picone/Hardy gate
of 106.19.  For a compact multiplier,

\[
 (D^2-\tfrac14)(\mathcal F r)
 =4Kr+2\mathcal F'r'+\mathcal F r''.              \tag{39}
\]

Thus moving the Sturm operator onto \(\mathcal F r\) leaves the exact
commutator \(2\mathcal F'r'+\mathcal F r''\); using \(\mathcal F\) alone
also leaves the nonvanishing boundary (8).  Formula (28) is the
theta-resolved version of that remainder.  Unlike a generic Picone
identity, it uses the exact ordinary-prime, Gamma and polar source, but
Theorem 4 proves that its local cumulative is not positive.

## 8. Result and exact remaining statement

The Gaussian primitive supplies the following new exact normal form:

\[
 \boxed{
 Q(r)=2\pi\int K e^{5y/2}\sum_m m\int P_y''A_y^+
 +\pi\int K e^{-5x/2}\sum_m m\int P_{-x}''A_x^-.} \tag{40}
\]

All Gaussian curvature factors in (40) are positive.  Nevertheless the
physical cumulatives have both signs, already below the first prime.
Accordingly, integration or summation by parts on the full theta lattice
does **not** yield a positive signed square plus a Gamma/pole boundary.
The boundary vanishes, and Gamma/pole are already inside \(A^\pm\).

The only possible successor in this coordinate is a genuinely global
alignment theorem,

\[
 \boxed{
 2\int K e^{5y/2}\sum_m m\int P_y''A_y^+
 +\int K e^{-5x/2}\sum_m m\int P_{-x}''A_x^-
 \ge -o(\mathrm{Tr}\,\Gamma_t)}              \tag{41}
\]

along a cofinal heat or hybrid sequence, after the exact radical
anti-short.  Equation (41) is just the heat/hybrid physical surplus in the
primitive-current coordinate; it is not proved here.

## 9. Addendum: summing every theta fibre before integration by parts

The preceding obstruction is fiberwise.  One can instead sum the complete
theta lattice, including all character groups, before forming any
cumulative.  This produces a shorter exact object, but it does not restore
a local sign.

The scaling identities (15)--(16) give

\[
 \sum_{m\ge1}k_{mz}(y)=z^{-1/2}K(y+\log z),        \tag{42}
\]

and, for \(z\ge e^x\),

\[
 \sum_{m\ge1}k_{mz}(-x)=z^{-1/2}K(\log z-x).      \tag{43}
\]

Therefore the sum of the same-side and central integrands in
(18)--(19) is

\[
 \boxed{
 F_r(z)=z^{-1/2}J_{\log z}(r).}                   \tag{44}
\]

In particular, the fully aggregated multiplicative cumulative is

\[
 \boxed{
 \mathcal A_r(Z)
 :=\int_{(1,Z]}F_r(z)\,d\eta(z)
 =\int_0^{\log Z}J_u(r)\,d\sigma(u).}             \tag{45}
\]

The character covariance of 106.108 is unitary on each theta fibre, so it
leaves (44)--(45) unchanged.

Let \(\zeta_0\) denote the unique real root in \((1,4/3)\) of

\[
 \zeta_0^3-\zeta_0-1=0.                           \tag{46}
\]

Away from prime-power atoms, (30) and (44) give the exact derivative

\[
 \boxed{
 \mathcal A_r'(z)
 =z^{-1/2}J_{\log z}(r)
 \left\{-1+\frac1{z(z^2-1)}\right\}.}             \tag{47}
\]

At a prime power \(n\), the jump is

\[
 \boxed{
 \mathcal A_r(n^+)-\mathcal A_r(n^-)
 =\frac{\Lambda(n)}{\sqrt n}J_{\log n}(r)\ge0.}  \tag{48}
\]

For a nonconstant continuous multiplier, \(J_u(r)=0\) exactly when \(u\)
is a period of \(r\).  The period group of a nonconstant continuous
function is discrete.  Hence, on every open interval, \(J_u(r)>0\) except
possibly at a discrete set.  Equations (46)--(48) prove the following
aggregate staircase law:

* \(\mathcal A_r\) increases on \((1,\zeta_0)\);
* it decreases strictly, apart from isolated periods, between every two
  consecutive prime-power atoms above \(\zeta_0\);
* every prime-power atom gives an upward jump.

Thus summing all theta fibres before integration by parts does not produce
the cumulative of a pointwise nonnegative square.  The obstruction is now
aggregate rather than fiberwise: the literal completed source forces a
downward continuous drift interrupted by upward arithmetic jumps.  Any
successful square must mix distinct values of \(z\) nonlocally, after the
complete radical anti-short; a fibrewise or Volterra factorization cannot
work.

This staircase statement does **not** prove that \(\mathcal A_r(Z)\) itself
takes negative values, and therefore does not refute the possible global
inequality \(\mathcal A_r(\infty)\ge0\).  It is an exact obstruction to a
local aggregate square, not a counterexample to the physical surplus.
