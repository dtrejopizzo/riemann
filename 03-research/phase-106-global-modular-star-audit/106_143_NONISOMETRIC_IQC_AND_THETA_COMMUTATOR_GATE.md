# 106.143 — Non-isometric IQC and theta-commutator gate

## 1. Purpose and verdict

This note tests a mechanism not covered by the metric-preserving rigidity
theorems 106.105 and 106.141: a bounded, frequency-dependent, matrix IQC
multiplier which is not an isometry in the ambient Hilbert metric.

The audit is exact.

1.  The literal ordinary-prime--Gamma--pole form is the pullback of one
    Krein signature through the complete theta-weighted delay observation.
2.  The exact frequency object is a two-frequency integral kernel.  The
    bare delay phase \(1-e^{-i\omega u}\) is not the physical symbol,
    because multiplication by
    \(\sqrt{K(x)K(x-u)}\) couples frequencies.
3.  An exact IQC multiplier differs from the original signature only by a
    null IQC on the completely anti-shorted physical range.  It changes the
    realization, not the sign.
4.  A nonexact multiplier gives a sufficient theorem only after one proves
    both its transformed positivity and the compressed dominance of the
    discarded remainder.  A source-independent dominance condition
    necessarily attenuates the positive prime/Gamma ports and amplifies the
    negative polar port; it therefore produces a strictly harder gate.
5.  A nonconstant scalar dynamic multiplier cannot be commuted through the
    theta-weighted delay ports.  The exact omitted commutator is nonzero.
6.  Any bounded matrix IQC using only finitely many delay ports is defeated
    by simultaneous phase recurrence, even before any triangle estimate is
    taken.  This does not by itself falsify a multiplier constructed after
    the complete Riemann anti-short; it proves that such a multiplier must be
    cofinal and source-specific.

Thus non-isometry in the ambient Hilbert metric supplies no intermediate
sign theorem.  The only surviving IQC is a cofinal compressed multiplier
whose remainder dominance is proved from the literal placements
\(\log p^k\), weights \(\Lambda(p^k)\), Gamma channel, pole, and complete
mean-periodic anti-short.  That dominance is a new form of the physical
surplus, not a consequence of IQC calculus alone.

## 2. The exact post-short observation

Put

\[
 \mathscr C=(\mathbf 1\oplus\mathcal R)^\perp
\tag{1}
\]

and, for \(u>0\), define

\[
 m_u(x)=\{K(x)K(x-u)\}^{1/2},\qquad
 (C_uq)(x)=m_u(x)\{q(x)-q(x-u)\}.
\tag{2}
\]

Then \(\|C_uq\|_2^2=J_u(q)\).  With

\[
 a_n={\Lambda(n)\over\sqrt n},\qquad u_n=\log n,
 \qquad r_\Gamma(u)={e^{-5u/2}\over1-e^{-2u}},
\tag{3}
\]

introduce the three closed observation channels

\[
\begin{aligned}
 Z_pq&=(\sqrt{a_n}\,C_{u_n}q)_{n\ge2},\\
 Z_\Gamma q&=(\sqrt{r_\Gamma(u)}\,C_uq)_{u>0},\\
 Z_0q&=(e^{u/4}C_uq)_{u>0}.
\end{aligned}
\tag{4}
\]

Write

\[
 Zq=(Z_pq,Z_\Gamma q,Z_0q),\qquad
 \mathcal J=\mathrm{diag}(I,I,-I).
\tag{5}
\]

The common-cutoff Stieltjes reconstruction of 106.138 and the convention
audit of 106.139 give the exact identity

\[
 \boxed{
 \mathfrak Q_{\rm phys}(q)
 =\langle Zq,\mathcal JZq\rangle,
 \qquad q\in\mathscr C.}
\tag{6}
\]

Every prime power occurs in (4) with its literal ordinary von Mangoldt
weight.  The complete Gamma remainder and polar continuum occur with their
exact coefficients.  No zero-location statement is used in (6).

## 3. The exact frequency kernel

Use

\[
 \widehat f(\omega)=\int_{\mathbb R}f(x)e^{-i\omega x}\,dx,
 \qquad
 f(x)={1\over2\pi}\int_{\mathbb R}\widehat f(\omega)e^{i\omega x}\,d\omega.
\tag{7}
\]

### Theorem 1 — Theta-modulated delay symbol

For every smooth core multiplier,

\[
 \boxed{
 \widehat{C_uq}(\omega)
 ={1\over2\pi}\int_{\mathbb R}
 \widehat m_u(\omega-\eta)
 (1-e^{-i\eta u})\widehat q(\eta)\,d\eta.}
\tag{8}
\]

Equivalently, if \(w_u(x)=K(x)K(x-u)=m_u(x)^2\), then

\[
\boxed{
\begin{aligned}
 J_u(q)={1\over(2\pi)^2}\iint
 &(1-e^{-i\xi u})(1-e^{i\eta u})
 \widehat w_u(\eta-\xi)\\
 &\times\widehat q(\xi)\overline{\widehat q(\eta)}
 \,d\xi\,d\eta .
\end{aligned}}
\tag{9}
\]

At a common displacement cutoff \(Y\), the exact physical kernel is

\[
\boxed{
 \mathbb A_Y(\xi,\eta)
 =\int_{[0,Y]}
 (1-e^{-i\xi u})(1-e^{i\eta u})
 \widehat w_u(\eta-\xi)\,d\sigma_Y(u),}
\tag{10}
\]

where

\[
 d\sigma_Y
 =\sum_{\log n\le Y}a_n\delta_{\log n}
  +r_\Gamma(u)\mathbf1_{[0,Y]}du
  -e^{u/2}\mathbf1_{[0,Y]}du
\tag{11}
\]

uses one endpoint convention.  Hence

\[
 \mathfrak Q_{\rm phys,Y}(q)
 ={1\over(2\pi)^2}\iint
 \mathbb A_Y(\xi,\eta)
 \widehat q(\xi)\overline{\widehat q(\eta)}\,d\xi d\eta.
\tag{12}
\]

#### Proof

The translation difference has Fourier transform

\[
 \widehat{q-q(\cdot-u)}(\eta)
 =(1-e^{-i\eta u})\widehat q(\eta).
\]

The product formula gives (8).  Expanding
\(\int w_u|q-q(\cdot-u)|^2\) using (7) gives (9).  Integrating (9) against
the common signed measure (11) gives (10)--(12). \(\square\)

Formula (8) is the exact scalar/matrix-symbol audit.  Replacing it by the
diagonal phase \(1-e^{-i\omega u}\) deletes the convolution by
\(\widehat m_u\), hence deletes the theta envelope.  Such a replacement
is not an identity for the Riemann form.

## 4. Exact dynamic IQCs on the physical range

Let

\[
 \mathscr Z=\overline{Z\mathscr C}
\tag{13}
\]

in the graph norm of the three channels.  Let \(\Pi=\Pi^*\) be any bounded
operator on the observation space.  It may be a measurable
operator-valued frequency multiplier \(\Pi(\omega)\), including a full
matrix mixing the prime, Gamma, and polar fibers.  Put

\[
 \mathfrak Q_\Pi(q)=\langle Zq,\Pi Zq\rangle.
\tag{14}
\]

### Theorem 2 — Null-IQC rigidity and the exact sufficient pair

One has

\[
 \boxed{
 \mathfrak Q_\Pi=\mathfrak Q_{\rm phys}
 \text{ on }\mathscr C
 \quad\Longleftrightarrow\quad
 Z_{\mathscr C}^*(\Pi-\mathcal J)Z_{\mathscr C}=0.}
\tag{15}
\]

Moreover the pair

\[
 \boxed{
 Z_{\mathscr C}^*\Pi Z_{\mathscr C}\succeq0,
 \qquad
 Z_{\mathscr C}^*(\mathcal J-\Pi)Z_{\mathscr C}\succeq0}
\tag{16}
\]

implies the physical surplus.  Conversely, any proof which obtains the
physical sign by adding these two IQCs must prove both members of (16);
the second is the exact price of changing the multiplier.

#### Proof

Equation (15) is obtained by subtracting (14) from (6) and polarizing on
the form core.  Adding the two operator inequalities in (16) gives

\[
 Z_{\mathscr C}^*\mathcal JZ_{\mathscr C}\succeq0,
\]

which is (6). \(\square\)

Thus an exact non-isometric multiplier is a null IQC on the physical
range.  It can simplify coordinates, but it cannot alter the quadratic
form evaluated on any physical row.

## 5. What a source-independent non-isometric multiplier does

Let \(\Psi(\omega)\) be a bounded dynamic multiplier and set

\[
 \Pi_\Psi(\omega)=\Psi(\omega)^*\mathcal J\Psi(\omega).
\tag{17}
\]

A source-independent sufficient remainder condition is

\[
 \mathcal J-\Pi_\Psi(\omega)\succeq0
 \quad\text{for almost every }\omega.
\tag{18}
\]

Write, relative to positive and negative ports,

\[
 \Psi=\begin{pmatrix}A&B\\ C&D\end{pmatrix}.
\]

Then (18) is exactly

\[
\boxed{
\begin{pmatrix}
 I-A^*A+C^*C&-A^*B+C^*D\\
 -B^*A+D^*C&-I-B^*B+D^*D
\end{pmatrix}\succeq0.}
\tag{19}
\]

For a diagonal scaling \(\Psi=\mathrm{diag}(D_+,D_-)\), this
reduces to

\[
 \boxed{D_+^*D_+\preceq I,\qquad D_-^*D_-\succeq I.}
\tag{20}
\]

Thus every universal diagonal remainder attenuates the positive
prime/Gamma ports and amplifies the negative polar port.  For example,

\[
 \Psi_\varepsilon
 =\mathrm{diag}(\sqrt{1-\varepsilon}\,I_+,
                       \sqrt{1+\varepsilon}\,I_-)
\tag{21}
\]

gives

\[
 \boxed{
 \mathfrak Q_{\Pi_{\Psi_\varepsilon}}(q)
 =\mathfrak Q_{\rm phys}(q)-\varepsilon\|Zq\|^2.}
\tag{22}
\]

Consequently transformed positivity in (22) is a strictly stronger
condition.  Every negative physical direction remains negative, with a
larger deficit.

Hilbert non-isometry itself is irrelevant.  The constant matrix

\[
 \Psi_r=\begin{pmatrix}\cosh r&\sinh r\\
                        \sinh r&\cosh r\end{pmatrix}
\tag{23}
\]

has arbitrarily large Hilbert norm but satisfies

\[
 \Psi_r^*\mathcal J\Psi_r=\mathcal J.
\tag{24}
\]

It is \(\mathcal J\)-isometric and leaves (6) unchanged.

## 6. A nonconstant scalar multiplier creates an exact theta commutator

Let \(D=d(-i\partial_x)\) be a bounded scalar Fourier multiplier.  Since
\(D\) commutes with translation,

\[
 [D,C_u]=[D,M_{m_u}](I-U_u).
\tag{25}
\]

### Theorem 3 — Commutation rigidity

On the smooth core,

\[
\boxed{
\begin{aligned}
 \widehat{[D,C_u]q}(\omega)
 ={1\over2\pi}\int
 &[d(\omega)-d(\eta)]\widehat m_u(\omega-\eta)\\
 &\times(1-e^{-i\eta u})\widehat q(\eta)\,d\eta .
\end{aligned}}
\tag{26}
\]

For any fixed \(u>0\),

\[
 [D,C_u]=0\quad\Longrightarrow\quad
 d\text{ is constant almost everywhere}.
\tag{27}
\]

#### Proof

Equation (26) follows from (8).  Since \(m_u>0\),

\[
 \widehat m_u(0)=\int_{\mathbb R}m_u(x)\,dx>0.
\]

Continuity makes \(\widehat m_u\) nonzero on a neighborhood of zero.  If
the kernel in (26) vanishes, then
\(d(\omega)=d(\eta)\) for almost every sufficiently close pair, outside
the discrete null set of \(1-e^{-i\eta u}\).  Chaining overlapping
neighborhoods along \(\mathbb R\) proves that \(d\) is almost everywhere
constant. \(\square\)

Therefore a nonconstant dynamic scaling cannot be pushed through the
literal theta-weighted delay bank.  Discarding (26) omits another
connection term.  Retaining it returns to the matrix kernel (10).

## 7. Finite-bank matrix IQCs fail by recurrence

Let \(a_1,\ldots,a_M>0\), and define

\[
 E_Aq=(C_{a_1}q,\ldots,C_{a_M}q).
\tag{28}
\]

### Theorem 4 — Bounded finite-IQC observability fails

Let \(\mathcal M\) be any bounded self-adjoint operator on the finite
output space of (28).  Let \(I\Subset(0,\infty)\) have positive length and
let \(g>0\) almost everywhere on \(I\).  There is a sequence
\(\xi_k\to\infty\) such that, for
\(q_k(x)=\cos(\xi_kx)\),

\[
 \boxed{
 \langle E_Aq_k,\mathcal M E_Aq_k\rangle\longrightarrow0,}
\tag{29}
\]

whereas

\[
 \boxed{
 \int_Ig(u)J_u(q_k)\,du
 \longrightarrow
 \int_Ig(u)(K*K)(u)\,du>0.}
\tag{30}
\]

Hence no bounded finite-delay matrix or dynamic IQC can dominate the
continuum channel on the full smooth multiplier core.

#### Proof

Simultaneous Dirichlet recurrence supplies \(\xi_k\to\infty\) such that

\[
 e^{i\xi_ka_j}\longrightarrow1\qquad(1\le j\le M).
\]

Equation 106.137(14) then gives
\(J_{a_j}(q_k)\to0\) for every \(j\), so
\(\|E_Aq_k\|^2\to0\).  Boundedness of \(\mathcal M\) proves (29).
Uniform Riemann--Lebesgue on the compact displacement interval gives
(30), exactly as in 106.137(15). \(\square\)

Theorem 4 is stronger than the passive-path falsifier in one direction:
it covers every bounded matrix multiplier on a finite delay bank, not only
a positive graph Schur complement.  Its scope is also exact.  The witness
has not been projected through the complete Riemann radical, so the theorem
does not falsify a genuinely post-short, cofinal, source-specific IQC.

## 8. Off-line stress test and the surviving class

Suppose counterfactually that an off-line zero orbit exists.  Theorem 4 of
106.141, inherited from 106.93, supplies a vector \(q\in\mathscr C\) with

\[
 \mathfrak Q_{\rm phys}(q)<0.
\tag{31}
\]

For every multiplier satisfying the compressed remainder inequality

\[
 Z_{\mathscr C}^*(\mathcal J-\Pi)Z_{\mathscr C}\succeq0,
\tag{32}
\]

one has

\[
 \mathfrak Q_\Pi(q)\le\mathfrak Q_{\rm phys}(q)<0.
\tag{33}
\]

Thus no universally valid remainder multiplier can repair the off-line
direction.  If \(\Pi\) is instead selected so that
\(\mathfrak Q_\Pi(q)\ge0\), then (32) fails on that same vector, and the
implication back to the physical form is lost.

On a finite completely anti-shorted heat or hybrid row
\(E=\mathrm{span}\,\{q_1,\ldots,q_m\}\), the exact audit is the pair
of matrices

\[
 H_\Pi(E)_{ij}=\langle Zq_i,\Pi Zq_j\rangle,
 \qquad
 H_\mathcal J(E)_{ij}=\langle Zq_i,\mathcal JZq_j\rangle,
\tag{34}
\]

with the two required inequalities

\[
 \boxed{
 H_\Pi(E)\succeq0,
 \qquad
 H_\mathcal J(E)-H_\Pi(E)\succeq0.}
\tag{35}
\]

This is a legitimate new finite-row optimization coordinate.  It does not
alter the logical target: the sum of the two matrices in (35) is the
physical matrix itself.

## 9. Result

The non-metric-preserving IQC route has now been classified.

* Exact dynamic multipliers are null-IQC reparametrizations on the physical
  range.
* Source-independent sufficient remainders harden the polar channel and
  cannot manufacture the missing sign.
* Nonconstant scalar frequency multipliers create the exact theta
  commutator (26), so the bare delay symbol is incomplete.
* Every bounded finite-delay matrix IQC fails continuum observability by
  recurrence.
* A cofinal post-short IQC remains possible only if one proves the
  source-specific compressed dominance (32) together with transformed
  positivity.

That last possibility is mathematically distinct in representation but not
in force: adding its two inequalities gives

\[
 \mathfrak Q_{\rm phys}\ge0\quad\text{on }\mathscr C.
\]

Therefore the IQC calculus supplies an exact audit and a broad finite-bank
falsifier, but no new automatic reserve.  The surviving mechanism is still
a genuinely cofinal signed ordinary-prime--Gamma--pole comparison after the
complete anti-short; its proof must use arithmetic structure beyond bounded
frequency-multiplier algebra.
