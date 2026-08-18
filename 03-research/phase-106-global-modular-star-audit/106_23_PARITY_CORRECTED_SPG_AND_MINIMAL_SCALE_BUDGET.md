# 106.23 — Parity-corrected SPG and the minimal scale budget

## Purpose

The moving co-Poisson vector of 106.12 is not automatically invariant under
multiplicative inversion.  Consequently, the even rank-one polar formula of
106.17 cannot be applied directly to that vector.  This note repairs the
parity issue before any further estimate is attempted.

There are four results.

1. The full completed operator has an exact rank-two polar decomposition.
2. Canonical inversion symmetrization preserves the complete co-Poisson
   radical and the exterior (L^2) leakage form.
3. Gate SPG is restated for the resulting even moving vector.
4. The scale assumptions in 106.12 and 106.15 are reduced to the weakest
   polynomial-loss package actually required by the weighted curvature gate.

The parity repair and the scale reduction are unconditional.  The remaining
form-dual estimate and complementary inertia estimate are not proved here.

## 1. The missing odd polar channel

Use additive logarithmic coordinates on

\[
 I_L=[-L/2,L/2],\qquad N=e^L=\lambda^2,
\]

and define

\[
 c_L(x)={\bf1}_{I_L}(x)\cosh(x/2),\qquad
 s_L(x)={\bf1}_{I_L}(x)\sinh(x/2).
\]

Let \(\mathcal D_N\) and \(\kappa_N\) be the positive jump form and the
centering constant of 106.17.  The polar quadratic term is

\[
 2\operatorname {Re}\left(
 \widehat F(i/2)\overline{\widehat F(-i/2)}\right).
\]

Since

\[
 \widehat F(i/2)=\langle c_L,F\rangle+\langle s_L,F\rangle,
 \qquad
 \widehat F(-i/2)=\langle c_L,F\rangle-\langle s_L,F\rangle,
\]

polarization gives the following correction.

### Theorem 1 — Full parity decomposition

On the common closed-form domain,

\[
\boxed{
 A_L=
 \mathcal D_N-\kappa_N I
 +2|c_L\rangle\langle c_L|
 -2|s_L\rangle\langle s_L|.}
\tag{1}
\]

Therefore, for a normalized \(q\) and a unit vector \(g\perp q\),

\[
\boxed{
 \langle A_Lq,g\rangle
 =\mathcal D_N(q,g)
 +2\overline{\langle c_L,q\rangle}\langle c_L,g\rangle
 -2\overline{\langle s_L,q\rangle}\langle s_L,g\rangle.}
\tag{2}
\]

The last term vanishes only after restricting both entries to the
inversion-even sector.  Thus 106.17(21)--(25) is correct for an even vector,
but not for the unsymmetrized moving vector of 106.12.

#### Proof

Put \(C=\langle c_L,F\rangle\) and
\(S=\langle s_L,F\rangle\).  Then

\[
 2\operatorname {Re}\bigl((C+S)\overline{(C-S)}\bigr)
 =2|C|^2-2|S|^2.
\]

Combine this identity with the centered jump-square formula 106.17(8),
and polarize.  This proves (1)--(2). \(\square\)

## 2. Canonical even symmetrization

On \(L^2(\mathbb R_+^*,d^*u)\), let

\[
 (JF)(u)=F(u^{-1}).
\tag{3}
\]

The involution \(J\) is unitary.  Let

\[
 P=P_{[\lambda^{-1},\lambda]},\qquad
 F=\mathcal E(f),\qquad
 V=PF,\qquad R=(1-P)F.
\tag{4}
\]

For the codimension-two prolate vector of 106.12,

\[
 f(0)=0,\qquad \int f=0.
\tag{5}
\]

Poisson summation then gives

\[
 J\mathcal E(f)=\mathcal E(\widehat f).
\tag{6}
\]

The compressed Fourier relation is

\[
 P_\lambda\widehat f
 =\sum_j c_j\chi_j\psi_{j,\lambda},
\]

whereas \(f=\sum_jc_j\psi_{j,\lambda}\).  The eigenvalues \(\chi_j\)
are different.  Hence the moving vector is generically not inversion-even;
the two moment conditions in (5) do not change that fact.

Define

\[
 F^+=\frac{F+JF}{\sqrt2},\qquad
 V^+=PF^+,\qquad R^+=(1-P)F^+.
\tag{7}
\]

### Theorem 2 — Symmetric radical and exact leakage conservation

The vector \(F^+\) belongs to the complete polarized Weil radical,
\(JV^+=V^+\), and

\[
\boxed{
 QW_\lambda(V^+,G)=-QW(R^+,G)}
\tag{8}
\]

for every even semilocal core vector \(G\).  Moreover,

\[
\boxed{R^+=\frac{R+JR}{\sqrt2}.}
\tag{9}
\]

For two source vectors \(f,g\),

\[
\boxed{
 \langle R_f^+,R_g^+\rangle
 =\langle R_f,R_g\rangle.}
\tag{10}
\]

Thus symmetrization preserves exactly the exterior \(L^2\) leakage Gram
form and does not alter the source prolate angle levels \(d_4,d_8\).

#### Proof

In the zero parameter of 106.12,
\(\widehat{JF}(s)=\widehat F(-s)\).  The complete zeta divisor is invariant
under \(s\mapsto-s\), so \(J\) preserves the polarized radical.  Hence
\(F^+\) is radical.  The interval in (4) is inversion invariant, so \(P\)
commutes with \(J\), proving (8)--(9) by Theorem 2 of 106.12.

Because \(f\) is supported in \([-\lambda,\lambda]\), the original
co-Poisson vector vanishes for \(u>\lambda\).  Therefore \(R\) is supported
below \(\lambda^{-1}\), while \(JR\) is supported above \(\lambda\).
The cross inner products vanish, \(J\) is unitary, and (10) follows. \(\square\)

The same calculation for
\(F^-=(F-JF)/\sqrt2\) gives

\[
 \|R^+\|^2=\|R^-\|^2=\|R\|^2,\qquad
 \|V^+\|^2+\|V^-\|^2=2\|V\|^2.
\tag{10a}
\]

Consequently at least one definite-parity projection has norm at least
\(\|V\|\), so parity projection need not amplify normalized \(L^2\)
leakage.  The odd sector is governed by

\[
 A_L^-=\mathcal D_N-\kappa_NI-2|s_L\rangle\langle s_L|.
\tag{10b}
\]

The bilateral negative-test theorem 106.11 permits a two-parity closure,
but the positive rank-one coordinate of 106.17 is specifically the plus
sector.

### Warning

Equation (10) is an \(L^2\) statement.  It does not assert

\[
 QW(R_f^+,R_g^+)=QW(R_f,R_g),
\]

because the Weil form is nonlocal.  The transfer from the angle form to the
Weil form remains the arithmetic part of Gate CWA/SPG.

## 3. The corrected exact residual

The positive-parity component is nonzero for the nonzero prolate source.
Indeed, if \(F^+=0\), then \(F=-JF\).  Since \(F\) vanishes above
\(\lambda\), it would then also vanish below \(\lambda^{-1}\).  Its
logarithmic Fourier transform would be an entire function of finite
exponential type vanishing on the complete zeta divisor.  The divisor has
counting function \(\asymp T\log T\), whereas a nonzero entire function of
finite exponential type has only \(O(T)\) zeros in that strip.  Hence
\(F=0\).  The Mellin identity
\(\mathcal MF=\zeta(s+1/2)\mathcal Mf(s+1/2)\) then gives \(f=0\), a
contradiction.

Put

\[
 q_L^+=\frac{V^+}{\|V^+\|},\qquad
 e_L^+=\frac{R^+}{\|V^+\|}.
\tag{11}
\]

For even \(g\perp q_L^+\), Theorems 1--2 give

\[
\boxed{
 \mathcal D_N(q_L^+,g)
 +2\overline{\langle c_L,q_L^+\rangle}\langle c_L,g\rangle
 =-QW(e_L^+,g).}
\tag{12}
\]

There is also an exact literal-prime expression.  On the smooth core define

\[
 \delta_u^2=\tau_u+\tau_{-u}-2I,
 \qquad
 k_*(u)=\frac{e^{-5u/2}}{1-e^{-2u}},
\]

and

\[
\boxed{
 T_L=
 \sum_{n\le e^L}\frac{\Lambda(n)}{\sqrt n}\,
       \delta_{\log n}^2
 +\int_0^L\bigl(k_*(u)-e^{u/2}\bigr)\delta_u^2\,du.}
\tag{13}
\]

The compensated identity of 106.18--106.19 yields

\[
\boxed{
 b_L^+:=(I-|q_L^+\rangle\langle q_L^+|)A_L^+q_L^+
 =-(I-|q_L^+\rangle\langle q_L^+|)T_Lq_L^+.}
\tag{14}
\]

Formula (14) retains every ordinary prime power, Gamma, both polar branches,
and the zero-extension boundary before taking a norm.  It is the exact
quantity to estimate.  It is not a new positivity identity: its semantic
predecessors are E72.294, E73.294, E74.004 and E101.056, while the specific
moving vector and the scales below are new.

## 4. Minimal polynomial-loss budget

Let

\[
 \mathscr R_L^+=\langle A_L^+q_L^+,q_L^+\rangle,
\qquad
 \beta_L^+=
 \inf_{\substack{g\perp q_L^+\\g\ {\rm even}\\\|g\|=1}}
 \langle A_L^+g,g\rangle.
\tag{15}
\]

Retain the proved prolate scales

\[
 d_4\asymp\lambda^9e^{-4\pi\lambda^2},\qquad
 d_8\asymp\lambda^{17}e^{-4\pi\lambda^2},\qquad
 \frac{d_4}{d_8}\asymp\lambda^{-8}.
\tag{16}
\]

The earlier sufficient package \(R_L^+=O(d_4)\) is stronger than the Schur
argument requires.

### Theorem 3 — Minimal SPG scale package

Suppose, for fixed exponents \(p_R,p_b\), that

\[
\boxed{
 |\mathscr R_L^+|=O(\lambda^{p_R}d_4),\quad p_R<8,}
\tag{17}
\]

\[
\boxed{
 \beta_L^+\ge c d_8,}
\tag{18}
\]

and

\[
\boxed{
 \|b_L^+\|=O(\lambda^{p_b}d_4),\quad p_b\le\frac{15}{2}.}
\tag{19}
\]

Then

\[
 \beta_L^+-\mathscr R_L^+\asymp d_8
\tag{20}
\]

and, for every fixed \(B<1/2\),

\[
\boxed{
 \lambda^B\frac{\|b_L^+\|}{\beta_L^+-\mathscr R_L^+}\longrightarrow0.}
\tag{21}
\]

If \(\epsilon_{0,L}^+\) is the even ground eigenvalue and
\(g_L^+\) its next-even gap, then

\[
 0\le \mathscr R_L^+-\epsilon_{0,L}^+
 \le\frac{\|b_L^+\|^2}{\beta_L^+-\mathscr R_L^+}
 =O\bigl(\lambda^{2p_b-8}d_4\bigr),
\tag{22}
\]

and

\[
\boxed{
 \lambda^{2B}
 \frac{\mathscr R_L^+-\epsilon_{0,L}^+}{g_L^+}
 \longrightarrow0.}
\tag{23}
\]

#### Proof

Equation (17) and (16) give \(\mathscr R_L^+=o(d_8)\), proving (20).  Then

\[
 \lambda^B\frac{\|b_L^+\|}{\beta_L^+-\mathscr R_L^+}
 =O\left(\lambda^{B+p_b-8}\right).
\]

At the endpoint \(p_b=15/2\), the exponent is \(B-1/2<0\), proving
(21).  The scalar Schur complement gives (22).  Min--max gives
\(g_L^+\ge\beta_L^+-R_L^+\), so

\[
 \lambda^{2B}
 \frac{\mathscr R_L^+-\epsilon_{0,L}^+}{g_L^+}
 =O\left(\lambda^{2B+2p_b-16}\right)\to0,
\]

again including \(p_b=15/2\). \(\square\)

### Interpretation

The Rayleigh value needs only an \(o(\lambda^8)\) loss relative to
\(d_4\).  The cross residual may lose as much as \(\lambda^{15/2}\)
relative to \(d_4\).  Equivalently, a direct bound on the Rayleigh excess
may lose \(\lambda^7\).  Logarithmic and moderate polynomial graph-norm
losses are therefore harmless.

This relaxation does not remove the essential exponential cancellation.
An absolute estimate at the linear leakage scale \(\sqrt{d_4}\) is still
too large by \(e^{2\pi\lambda^2}\).  What is required is a quadratic
leakage estimate with an allowed polynomial loss.

## 5. Nonduplication verdict and next theorem

The repository-wide semantic audit gives the following binding exclusions.

- Paley--Wiener propagation, coarse gaps and Davis--Kahan are already
  closed by Phases 71, 80, 101 and 106.07--106.10.
- Feshbach, Picone, Hardy, positive-jump, nested-cutoff and generic frame
  arguments merely restate or fail the denominator in (18).
- PNT smoothing, large-sieve magnitude estimates, quantile transport and
  translation-metric geometry erase the literal atom-sensitive mechanism.
- Adding finitely many radical/prolate modes does not improve the
  residual-to-overlap quotient, by 106.14.

The divisor identity

\[
 \sum_{m\ge2}\frac{\Lambda(m)}{\sqrt m}
 \tau_{-\log m}\mathcal E(f)(x)
 =\mathcal E((\log\!\cdot)f)(e^x)-x\mathcal E(f)(e^x)
\tag{24}
\]

follows from \(\sum_{m\mid k}\Lambda(m)=\log k\).  It is the
Mecke/divisor generator already developed in E70.11--E70.12 and Phase 104.
After the opposite orientation and the boundary tail are restored, (24)
returns exactly (12)--(14); it does not square the leakage.  It is therefore
not reopened as a closure mechanism.

The next nonduplicated obligations are now exactly:

\[
\boxed{
 \frac{|QW(R^+,R^+)|}{\|V^+\|^2}
 \le C\lambda^{p_R}d_4,
 \qquad p_R<8,}
\tag{25}
\]

\[
\boxed{
 \|(I-|q_L^+\rangle\langle q_L^+|)T_Lq_L^+\|
 \le C\lambda^{p_b}d_4,
 \qquad p_b\le15/2,}
\tag{26}
\]

and the literal-prime inertia estimate (18).  Equations (25)--(26) concern
only the canonical parity-corrected moving vector.  They are strictly
narrower than positivity of the Weil form on all tests.

No statement in this note proves (18), (25), (26), Gate SPG, or RH.
