# 106.176 — Local Green identity and exact Tate translation energy

## 1. Purpose

The metric comparison left after 106.175 must be an equality involving
the actual CCM Rosati form, not another abstract positive completion.
This note derives its local Green identity directly from the local terms
in the CCM trace formula.

Every local principal-value correlation equals a scalar renormalized mass
minus a positive translation-difference energy.  On the radial
\(p\)-adic sector, the latter has exactly the coefficients
\((\log p)p^{-|k|/2}\) of the Tate/Cauchy modules constructed in
106.153--106.154.  Thus the local positive metric is now identified
bilinearly with the local CCM term.  The remaining discrepancy is a
single global boundary form containing degree, codegree, the polar plane,
and the jointly regularized scalar masses.

The difference-square mechanism itself is not new inside this project:
106.17, 106.19, and 106.22 already derived the real translation metric
and proved that its abstract positivity does not close the global Weil
inequality.  The new content here is narrower and tied to the present
construction: the place-by-place bilinear CCM identity, the literal
\(p\)-adic shell identification with the Tate/Cauchy module, the exact
archimedean identification with the Gamma spin page, and the resulting
boundary form (16).  No sign is inferred from the local squares alone.

## 2. The normalized scaling representation

Let

\[
 \mathscr H_C=L^2(C_{\mathbb Q},|x|\,d^*x).                  \tag{1}
\]

For \(a\in C_{\mathbb Q}\), define

\[
 (U_af)(x)=|a|^{-1/2}f(a^{-1}x).                             \tag{2}
\]

Then \(U_a\) is unitary on \(\mathscr H_C\).  For
\(f,g\in\mathbf S(C_{\mathbb Q})\), put

\[
 F=f*g^\sharp,
 \qquad
 g^\sharp(x)=|x|^{-1}\overline{g(x^{-1})}.                  \tag{3}
\]

### Lemma 2.1 — Correlation identity

For every \(a\in C_{\mathbb Q}\),

\[
 \boxed{
 F(a)=|a|^{-1/2}\langle f,U_ag\rangle_{\mathscr H_C}.}       \tag{4}
\]

In particular,

\[
 F(1)=\langle f,g\rangle_{\mathscr H_C}.                    \tag{5}
\]

#### Proof

Using multiplicative Haar measure,

\[
 \begin{aligned}
 F(a)
 &=\int_{C_{\mathbb Q}}f(x)g^\sharp(x^{-1}a)\,d^*x\\
 &=|a|^{-1}\int f(x)|x|\overline{g(a^{-1}x)}\,d^*x\\
 &=|a|^{-1}\langle f,L_ag\rangle_{\mathscr H_C},
 \end{aligned}                                               \tag{6}
\]

where \(L_ag(x)=g(a^{-1}x)=|a|^{1/2}U_ag(x)\).  Substitution
gives (4). \(\square\)

## 3. The local Dirichlet energy

For a place \(v\), embed \(u\in\mathbb Q_v^\times\) as the idele equal
to \(u\) at \(v\) and to one elsewhere, and write \(U_{v,u}\) for the
corresponding operator (2).  Define the positive symmetric measure away
from \(u=1\) by

\[
 d\nu_v(u)={|u|_v^{1/2}\over|1-u|_v}\,d^*u.                 \tag{7}
\]

It is invariant under \(u\mapsto u^{-1}\).  For Schwartz vectors define

\[
 \boxed{
 \mathcal E_v(f,g)
 ={1\over2}\int_{\mathbb Q_v^\times}
 \langle(I-U_{v,u})f,(I-U_{v,u})g\rangle_{\mathscr H_C}
 \,d\nu_v(u).}                                             \tag{8}
\]

The integral is ordinary, not principal value: the difference removes
the singularity at \(u=1\), and the half-density in (7) is integrable at
zero and infinity after the two differences are expanded jointly.

### Theorem 3.1 — Local Green identity

Let

\[
 I_v(F)=\int_{(\mathbb Q_v^\times,e_v)}'
        {F(u^{-1})\over|1-u|_v}\,d^*u                       \tag{9}
\]

be the CCM normalized principal value, and denote by
\(c_v=I_v(1)\) its scalar finite part.  Then

\[
 \boxed{
 I_v(f*g^\sharp)
 =c_v\langle f,g\rangle_{\mathscr H_C}-\mathcal E_v(f,g).}  \tag{10}
\]

Moreover \(\mathcal E_v(f,f)\ge0\).

#### Proof

Expanding (8), using unitarity, and changing \(u\) to \(u^{-1}\) in one
cross term gives

\[
 \mathcal E_v(f,g)
 =\int\left(langle f,g\rangle
       -\langle f,U_{v,u^{-1}}g\rangle\right)d\nu_v(u).      \tag{11}
\]

By (4), with \(a=u^{-1}\),

\[
 F(u^{-1})=|u|_v^{1/2}
             \langle f,U_{v,u^{-1}}g\rangle.                \tag{12}
\]

The difference between the two terms in (11) is integrable at \(u=1\).
Reintroducing their common principal-value normalization gives exactly
(10).  Positivity follows directly from (8). \(\square\)

Equation (10) is independent of any location of a zeta zero.  It is the
local integration-by-parts identity whose absence kept the Tate metric
and CCM trace pairing disconnected.

## 4. Exact finite-prime radial energy

Normalize \(d^*u\) so that a valuation shell has mass \(\log p\), as in
the local explicit formula.  On vectors invariant under
\(\mathbb Z_p^\times\), the unit part of (8) vanishes.  Write \(U_p\) for
translation by the idele with component \(p\) at \(p\).  On the shell
\(p^k\mathbb Z_p^\times\),

\[
 {|u|_p^{1/2}\over|1-u|_p}=p^{-|k|/2},
 \qquad k\ne0.                                              \tag{13}
\]

### Theorem 4.1 — Tate energy equals local CCM energy

On the radial sector,

\[
 \boxed{
 \mathcal E_p(f,g)
 ={\log p\over2}\sum_{k\in\mathbb Z\setminus\{0\}}
 p^{-|k|/2}
 \langle(I-U_p^k)f,(I-U_p^k)g\rangle.}                      \tag{14}
\]

The series converges absolutely on smooth vectors.  Its coefficients are
exactly the Fourier moments of the Poisson measure
\(\mu_{p^{-1/2}}\) used in 106.153 and the common Cauchy process of
106.154.

#### Proof

Decompose \(\mathbb Q_p^\times\) into valuation shells.  Radiality makes
the integrand constant on each shell and kills the \(k=0\) unit energy.
For \(k>0\), \(|p^k|_p=p^{-k}<1\) and \(|1-p^ku|_p=1\).  For
\(k<0\), \(|1-p^ku|_p=|p^k|_p\).  Both cases give (13).  Substitution in
(8) proves (14).  Geometric decay gives absolute convergence. \(\square\)

Thus the local Cauchy/Poisson module is not merely a model with the right
trace.  Its Dirichlet metric is the local Green energy of the actual CCM
principal-value distribution.

## 4.1 Exact archimedean spin decomposition

Write \(u=\sigma e^t\), with \(\sigma\in\{+1,-1\}\) and
\(t=\log|u|\).  The two positive kernels in (7) are

\[
 K_+(t)={1\over2|\sinh(t/2)|},
 \qquad
 K_-(t)={1\over2\cosh(t/2)}.                                \tag{14a}
\]

For \(t>0\),

\[
 \boxed{
 K_+(t)+K_-(t)
 ={2e^{-t/2}\over1-e^{-2t}}
 =2g_\Gamma(t),}                                            \tag{14b}
\]

where \(g_\Gamma\) is the Gamma density in (1) of 106.160.  Let

\[
 \chi_{\epsilon,\gamma}(u)
 =\mathrm{sgn}(u)^\epsilon|u|^{i\gamma},
 \qquad \epsilon\in\{0,1\}.                               \tag{14c}
\]

These characters diagonalize normalized real scaling.

### Theorem 4.2 — Gamma spin equals the even real Green energy

In the even sector \(\epsilon=0\), which contains the Riemann zeta
factor, the Mellin multiplier of (8) is

\[
 \boxed{
 m_{\Gamma,0}(\gamma)
 =4\int_0^\infty g_\Gamma(t)
       \bigl(1-\cos(\gamma t)\bigr)\,dt\ge0.}                \tag{14d}
\]

Thus the Lévy density of the archimedean Green energy is four times the
positive spin trace

\[
 \mathrm{Tr}(e^{-tN_\Gamma})
 ={e^{-t/2}\over1-e^{-2t}}
\]

of 106.160.  The factor four is forced by the two sign components and the
two halves \(t\gtrless0\).

#### Proof

For a character (14c), the integrand of (8), divided by its squared
amplitude, is

\[
 {1\over2}|1-\sigma^\epsilon e^{i\gamma t}|^2
 =1-\sigma^\epsilon\cos(\gamma t).                          \tag{14e}
\]

For \(\epsilon=0\), sum (14e) against \(K_+\) and \(K_-\), use
(14b), and then use evenness in \(t\).  This gives (14d).
Mellin--Plancherel diagonalizes the whole quadratic form. \(\square\)

## 5. The compensated global Green formula

Let \(S\) be a finite set of places containing \(\infty\).  Define the
partial CCM pairing

\[
 \begin{aligned}
 \mathfrak h_S(f,g)
 &=\widehat F(0)+\widehat F(1)
   -(\log|a|)F(1)-\sum_{v\in S}I_v(F),                       \tag{15}
 \end{aligned}
\]

where \(a\) is the differental idele.  Theorem 3.1 yields the exact
identity

\[
 \boxed{
 \begin{aligned}
 \mathfrak h_S(f,g)
 &=\sum_{v\in S}\mathcal E_v(f,g)
   +\mathcal B_S(f,g),\\
 \mathcal B_S(f,g)
 &=\widehat F(0)+\widehat F(1)
   -\left(\log|a|+\sum_{v\in S}c_v\right)
      \langle f,g\rangle_{\mathscr H_C}.
 \end{aligned}}                                             \tag{16}
\]

Neither \(\sum_v\mathcal E_v\) nor \(\sum_vc_v\) is asserted to
converge separately.  The CCM/Meyer nuclear trace theorem states that the
compensated combination (15), hence (16), has a limit on the strong
Schwartz space.  Therefore

\[
 \boxed{
 \mathfrak h_{\rm Ros}(f,g)
 =\mathrm{FP}_{S\nearrow\Sigma_{\mathbb Q}}
  \left[\sum_{v\in S}\mathcal E_v(f,g)+\mathcal B_S(f,g)\right].}
                                                                    \tag{17}
\]

This is the requested Green identity before the final boundary
identification.  Its first term is positive when \(f=g\); every possible
negative direction is confined to the finite-rank/global boundary form
\(\mathcal B_S\) and its joint finite part.

## 6. Comparison with the constructed pages

The terms in (17) now have source-defined realizations:

* finite radial \(\mathcal E_p\): the Tate/Cauchy translation metric,
  by Theorem 4.1;
* nonradial finite modes: the same local difference energy before radial
  compression;
* \(v=\infty\): the Gamma spin page, by Theorem 4.2;
* \(\widehat F(0)+\widehat F(1)\): the \(H^0/H^2\) polar plane;
* the scalar finite part of the first primitive Hardy layer: the map
  \(B_\infty\) of 106.172.

The two Tate balance equations in 106.169 are the coefficient form of
removing the common constant and its Hodge conjugate.  They must be
applied to the **joint** expression in (17).  The scalar masses in
\(\mathcal B_S\) are not the scalar in 106.172: on the unramified radial
sector one has

\[
 c_p=\log p\sum_{k\ne0}p^{-|k|/2}
 ={2\log p\over\sqrt p-1},                                  \tag{17a}
\]

whereas 106.172 regularizes \(\sum_p(\log p)/p\).  Thus
\(\mathcal B_S\) cannot be assigned a finite part independently of
\(\sum_{v\in S}\mathcal E_v\).  Their leading pieces cancel inside each
local Green identity (10).

## 7. Joint projection statement and its correction

Let \(\mathscr D_{\rm mp}\) be the nuclear Poisson/mean-periodic chain
domain.  Let \(\Phi_S\) denote the joint local Green feature map supplied
by (8), with its two generic endpoints retained, and let
\(P_S^{\rm mid}\) denote the Hodge-stable removal of those endpoints,
the analogue of \(\ker R\cap\ker RJ\).  At the first-primitive level the
natural candidate was

\[
 \boxed{
 \mathfrak h_{\rm Ros}(f,g)
 =\lim_{S\nearrow\Sigma_{\mathbb Q}}
 \left\langle
 P_S^{\rm mid}\Phi_Sf,
 P_S^{\rm mid}\Phi_Sg
 \right\rangle.}                                            \tag{18}
\]

The polar and 106.172 counterspaces are components of the joint
construction, not post-hoc finite parts of \(\mathcal B_S\).  Documents
106.177--106.178 sharpen and correct (18).  After all return shells are
included, the operator-valued middle projector exists explicitly, but its
positive norm and the generic/polar residual have opposite full-rank
white-light divergences.  Therefore the two terms are not separately
Cauchy and (18), interpreted as an ordinary Hilbert-norm limit, is too
strong.

The corrected object is the graded finite pairing

\[
 [\Phi_Sf,\Phi_Sg]_S
 =\langle P_S^{\rm mid}\Psi_Sf,
          P_S^{\rm mid}\Psi_Sg\rangle+\mathcal R_S(f,g),    \tag{18a}
\]

whose equality with (16) is exact at every finite cutoff.  Its canonical
off-diagonal Julia Hodge star is constructed in 106.178.  The remaining
theorem is that the Fourier-odd invariant graph descends
torsion-sensitively through the complete CCM cyclic restriction cone and
that the induced residue pairing is the finite part of (18a).  The two
summands in (18a) must remain joined until after this descent.

## 8. Falsification controls

1. Positivity of each \(\mathcal E_v\) does not by itself prove positivity
   of (17); the jointly regularized boundary form is retained.
2. Separating the two divergent terms in (17), or assigning a finite part
   to \(\mathcal B_S\) alone, is not permitted.
3. Replacing the literal shell weights in (14) by an absolute estimate
   would destroy the exact local Green identity.
4. The theorem proves a bilinear identification with the CCM local terms,
   not the torsion-sensitive global descent of (18a).

## 9. Status

Proved without RH or zero input:

* the exact correlation formula (4);
* a positive local Dirichlet form at every place;
* the exact local principal-value Green identity (10);
* exact equality of the radial \(p\)-adic energy with the Tate/Cauchy
  coefficients;
* exact equality of the even archimedean energy with the Gamma spin
  density;
* the compensated global Green identity (17);
* confinement of the remaining metric discrepancy to the global boundary
  form \(\mathcal B_S\).

Still required after 106.177--106.178:

* torsion-sensitive descent of the Fourier-odd Julia graph through the
  complete CCM nuclear restriction cone;
* identification of its residue metric with the joined finite part
  (18a);
* passage from (17)--(18a) to the positive Rosati polarization.

## 10. Primary input

The local principal values and global trace formula used in (9), (15),
and (17) are those of Connes--Consani--Marcolli, *The Weil proof and the
geometry of the adeles class space*, in the Meyer nuclear formulation.
All translation-energy identities are derived above.
