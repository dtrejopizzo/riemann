# 106.49 — The joint star current and the alignment defect

## Purpose

The local Riesz reduction of 106.48 asks for the sign of

\[
 \mathfrak T(P)=\mathrm{Tr}(PL^2)
 -\frac12\mathrm{Tr}(PL)                       \tag{1}
\]

on a finite spectral cluster. This note expands (1) directly in the
ordinary-prime--Gamma source, before splitting or estimating any cross
term. The result is an exact star-current identity.

The calculation also fixes the role of

\[
 j_2=\delta\Lambda+\Lambda*\Lambda.
\]

The convolution part comes from two prime moves. The
\(\delta\Lambda\) part is a logarithmic rate-variation term and cannot be
inserted into the prime--prime square by itself. The nonnegative Riccati jet
appears only after the oriented, mixed, Gamma and centering terms have been
reassembled.

## 1. The vector feature of a finite cluster

Let \(P=P_J\) be a finite-rank spectral projection as in 106.48 and choose
an orthonormal eigenbasis \(q_1,\ldots,q_m\). Define

\[
 \mathbf Q(x)=(q_1(x),\ldots,q_m(x))\in\mathbb C^m.   \tag{2}
\]

For \(u>0\), write

\[
\begin{aligned}
 \Delta_u^-\mathbf Q(x)&=\mathbf Q(x)-\mathbf Q(x-u),\\
 \Delta_u^+\mathbf Q(x)&=\mathbf Q(x)-\mathbf Q(x+u). \tag{3}
\end{aligned}
\]

Retain the complete positive displacement measure

\[
 d\nu_\zeta(u)=
 \sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}\,
 \delta_{\log n}(du)
g(u)\,du,\qquad
g(u)=\frac{e^{-u/2}}{1-e^{-2u}}.                     \tag{4}
\]

Define the joint star current

\[
\boxed{
\begin{aligned}
 \mathbf B_P(x)=\int_0^\infty\{&
 K(x-u)\Delta_u^-\mathbf Q(x)\\
 &+K(x+u)\Delta_u^+\mathbf Q(x)\}\,d\nu_\zeta(u).
\end{aligned}}                                       \tag{5}
\]

The prime and Gamma currents in (5) are never estimated separately.

## 2. Exact current formula

### Theorem 1 — Joint star-current trace identity

On every finite subthreshold spectral cluster,

\[
\boxed{
 \mathrm{Tr}(PL^2)
 =c_K\int_{\mathbb R}\frac{K(x)}{h(x)}
 \|\mathbf B_P(x)\|_{\mathbb C^m}^2\,dx}              \tag{6}
\]

and

\[
\boxed{
\begin{aligned}
 \mathrm{Tr}(PL)
 =\int_0^\infty\int_{\mathbb R}
 K(x)K(x-u)
 \|\mathbf Q(x)-\mathbf Q(x-u)\|^2\,dx\,d\nu_\zeta(u).
\end{aligned}}                                       \tag{7}
\]

Consequently the cluster-current inequality of 106.48 is exactly

\[
\boxed{
\begin{aligned}
 c_K\int\frac{K}{h}\|\mathbf B_P\|^2
 \ge \frac12\int_0^\infty\int_{\mathbb R}
 K(x)K(x-u)\|\Delta_u^-\mathbf Q(x)\|^2
 \,dx\,d\nu_\zeta(u).                                \tag{8}
\end{aligned}} 
\]

#### Proof

The generator formula 106.41(7), applied componentwise, gives

\[
 L\mathbf Q(x)=\frac{c_K}{h(x)}\mathbf B_P(x).        \tag{9}
\]

Since \(d\mu_K=hK\,dx/c_K\),

\[
\begin{aligned}
 \sum_{j=1}^m\|Lq_j\|_{L^2(\mu_K)}^2
 &=\int\frac{hK}{c_K}
 \left\|\frac{c_K}{h}\mathbf B_P\right\|^2dx\\
 &=c_K\int\frac Kh\|\mathbf B_P\|^2dx,
\end{aligned}
\]

which is (6). Formula (7) is the sum over \(j\) of the exact form
identity 106.31(7). Substitution into (1) proves (8). All statements first
hold with a common Gamma and prime cutoff. Graph-norm convergence removes
the cutoffs. \(\square\)

No zero or spectral coordinate occurs on the right side of (8). The only
cluster information is carried by the vector feature \(\mathbf Q\), whose
kernel is the projection kernel \(\Pi(x,y)=\langle\mathbf Q(x),\mathbf
Q(y)\rangle\).

## 3. A finite-rate alignment identity

The Gamma measure has infinite total mass at zero, so first introduce a
common cutoff

\[
 d\nu_{\varepsilon,N}
 =\mathbf1_{[\varepsilon,\varepsilon^{-1}]}g(u)\,du
 +\sum_{2\le n\le N}\frac{\Lambda(n)}{\sqrt n}
 \delta_{\log n}.                                    \tag{10}
\]

At each \(x\), let

\[
\begin{aligned}
 W_{\varepsilon,N}(x)
 &=\int\{K(x-u)+K(x+u)\}\,d\nu_{\varepsilon,N}(u),\\
 d\pi_x(u,\sigma)
 &=\frac{K(x+\sigma u)}
 {W_{\varepsilon,N}(x)}\,d\nu_{\varepsilon,N}(u),
 \qquad \sigma\in\{-1,+1\}.                          \tag{11}
\end{aligned}
\]

Thus \(\pi_x\) is a probability measure on oriented displacements. Put

\[
 V_x(u,\sigma)=\mathbf Q(x)-\mathbf Q(x+\sigma u),    \tag{12}
\]

and denote its conditional mean and variance by

\[
\begin{aligned}
 \overline V_x&=\int V_x\,d\pi_x,\\
 \mathcal V_x&=\int\|V_x-\overline V_x\|^2\,d\pi_x.
                                                               \tag{13}
\end{aligned}
\]

The cutoff current is

\[
 \mathbf B_{\varepsilon,N}(x)
 =W_{\varepsilon,N}(x)\overline V_x.                 \tag{14}
\]

After writing (7) with both orientations, the cutoff version of (1) is

\[
\boxed{
\begin{aligned}
 \mathfrak T_{\varepsilon,N}(P)
 =\int_{\mathbb R}K(x)\Bigg[
 &\left\{\frac{c_KW_{\varepsilon,N}(x)^2}{h(x)}
 -\frac14W_{\varepsilon,N}(x)\right\}
 \|\overline V_x\|^2\\
 &-\frac14W_{\varepsilon,N}(x)\mathcal V_x
 \Bigg]dx.                                           \tag{15}
\end{aligned}} 
\]

#### Proof

The symmetrized form of (7) is

\[
 \mathrm{Tr}(PL)
 =\frac12\int K(x)W_{\varepsilon,N}(x)
 \int\|V_x\|^2d\pi_x\,dx.                            \tag{16}
\]

Use

\[
 \int\|V_x\|^2d\pi_x
 =\|\overline V_x\|^2+\mathcal V_x                   \tag{17}
\]

and (6), (14). This gives (15). \(\square\)

Formula (15) must be read before taking the Gamma cutoff away. Its two
displayed terms need not converge separately as \(\varepsilon\downarrow0\);
their sum does, by Theorem 1. It nevertheless identifies the exact sign
mechanism: the desired lower bound is a *coherence estimate*. The squared
joint current must dominate the conditional dispersion of the complete
prime--Gamma increments.

## 4. The precise role and direction of the Riccati jet

Write the one-sided prime connection formally as

\[
 A=\sum_{n\ge2}\frac{\Lambda(n)}{\sqrt n}S_{\log n},
 \qquad \delta S_{\log n}=(\log n)S_{\log n}.         \tag{18}
\]

Then

\[
 \delta A+A^2
 =\sum_{n\ge2}\frac{j_2(n)}{\sqrt n}S_{\log n},
 \qquad
 j_2(n)=\delta\Lambda(n)+(\Lambda*\Lambda)(n)\ge0.    \tag{19}
\]

Equation (19) controls a second-order *dispersion* of the oriented prime
connection. The primitive theta estimate 106.40(11),

\[
 A_\theta(x)^2\le K(x)B_\theta(x),                   \tag{20}
\]

has the same direction: it is an upper bound for a squared mean by a
nonnegative second moment.

The sign required in (15) is the reverse type of statement: a lower bound
for the complete mean current in terms of its increment variance. Therefore
\(j_2\ge0\) cannot simply be applied to the prime square and declared to
prove (8). Such an application has the wrong inequality direction and also
omits the Gamma cross term.

This is not a rejection of the Riccati jet. It determines how it must be
used: the \(\delta\Lambda\) and \(\Lambda*\Lambda\) pieces must cancel the
negative variance in (15) *after* the projection identities

\[
 \Pi^2=\Pi,\qquad L_x\Pi=L_y\Pi,\qquad
 \Pi\mathcal R=0                                      \tag{21}
\]

have been inserted. The unrestricted coefficient lift fails because it has
none of (21).

## 5. Falsifier and surviving theorem

A proof using only nonnegativity of \(j_2\), positive jump weights and a
polar rank-one term would also apply to the one-atom model of 106.19. That
model has arbitrarily many subthreshold levels. Hence those three abstract
properties cannot prove (8).

The literal-prime statement left by (15) is strictly narrower:

> **Projection alignment theorem.** For the ordinary von Mangoldt weights,
> every finite-rank reducing feature \(\mathbf Q\) satisfying (21) obeys
> the cutoff-stable joint coherence bound obtained by moving the negative
> variance term of (15) to the other side.

Equivalently,

\[
\boxed{
\begin{aligned}
 \frac14\int K W_{\varepsilon,N}\mathcal V_x\,dx
 \le\int K\left(
 \frac{c_KW_{\varepsilon,N}^2}{h}-\frac14W_{\varepsilon,N}
 \right)\|\overline V_x\|^2dx+o_{\varepsilon,N}(1),
                                                               \tag{22}
\end{aligned}}
\]

with the joint limit taken in the graph norm and with no separation of
prime and Gamma currents.

The next step is to use \(L_x\Pi=L_y\Pi\) to replace the conditional
variance in (22) by a rate-variation expression. The same-orientation part
then produces \(\Lambda*\Lambda\), while the logarithmic commutator produces
\(\delta\Lambda\). Any remaining term after that substitution is the exact
signed obstruction to the \(j_2\) closure.
