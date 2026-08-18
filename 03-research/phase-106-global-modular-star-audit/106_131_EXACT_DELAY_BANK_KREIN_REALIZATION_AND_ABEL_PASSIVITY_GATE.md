# 106.131 — Exact delay-bank Krein realization and the Abel passivity gate

## 1. Purpose and verdict

Document 106.127 reduced positive theta-boundary escape to the jointly
signed ordinary-prime--Gamma--pole flux.  This note asks whether that flux
is the boundary dissipation of a passive port-Hamiltonian network.

There is an exact answer.

1. Every prime power \(n=p^k\) is an exact finite delay line of length
   \(u_n=\log n\), with terminal conductance

   \[
     a_n={\Lambda(n)\over\sqrt n}.
     \tag{1}
   \]

   The Gamma factor is the direct integral of the same lines with density

   \[
     g(u)={e^{-u/2}\over1-e^{-2u}}.
     \tag{2}
   \]

2. The polar threshold is another direct integral of delay lines, with
   density \(2\cosh(u/2)\), but with the opposite metric sign.  Eliminating
   the line states gives exactly, and not asymptotically,

   \[
     \mathscr E_K(q)-{1\over2}\mathrm{Var}_{\mu_K}(q)
     =\int_0^\infty J_u(q)\,d\sigma(u).
     \tag{3}
   \]

   Thus the completed network is a Krein port system.  It is not a Hilbert
   passive network for algebraic reasons.
3. Eliminating the prime lines in the moving boundary coordinate gives
   exactly the normalized Abel flux of 106.127.  Its causal impulse response
   is

   \[
     k_D(t)=e^{t/2}D(e^t),
     \qquad D(T)={\psi(T)-T+1\over T},
     \tag{4}
   \]

   and its transfer function is

   \[
     \widehat k_D(s)
     ={1\over s+1/2}
      \left\{-{\zeta'\over\zeta}(s+1/2)-{1\over s-1/2}\right\}.
     \tag{5}
   \]

4. The pole at \(s=1/2\) cancels exactly.  Every nontrivial zero
   \(\rho\) gives a pole at \(s=\rho-1/2\).  Consequently an exact stable
   Hilbert-passive continuation of this transfer to
   \(\mathrm{Re}\,s>0\) is already equivalent to RH at the level of
   pole location.  Passivity is not supplied by the positive local weights
   \(\Lambda(p^k)\).
5. Mean periodicity is compatible with the delay bank but does not make its
   Abel drive mean periodic.  If \(F=hq\), \(F*K=0\), and
   \(a=K/h\), the exact leakage is

   \[
     \boxed{
     \big\{(\partial+\tfrac12)(aF)\big\}*K
     =(aF)*(K'+\tfrac12K).}
     \tag{6}
   \]

   This nonzero radical-connection term is the quantity left after the
   internal delay states are removed.

Hence the delay construction is exact and useful, but it does not create
the missing sign.  The surviving theorem is precisely the dissipativity of
the compressed Krein network, equivalently the signed Abel passivity
statement of 106.127.

## 2. Binding semantic audit: the Phase-64 local-cell erratum

This construction must not be confused with
`phase-64-connes-route/CONSTRUCTION-local-Tate-colligation-p-adic.md`.
That document retains a binding erratum.  Its scalar Euler cell

\[
 \theta_p(z)={1-a p^{iz}\over1-a p^{-iz}}
 \tag{7}
\]

has a pole in the upper half-plane, and the proposed transfer matrix obeys

\[
 \det\{J-T_p(z)^*JT_p(z)\}
 =-{a^2(p^y-p^{-y})^2\over1-a^2}<0
 \qquad(y=\mathrm{Im}\,z>0).
 \tag{8}
\]

It is therefore not \(J\)-contractive.  Euler factors are not local scalar
Schur cells.  The corrected Phase-64 object is the positive von Mangoldt
Hamiltonian measure, not a passive Euler transfer.

The construction below respects that correction.  It uses only the
positive infinitesimal weights \(\Lambda(p^k)/\sqrt{p^k}\) to construct a
positive *source* delay bank.  It never asserts local scalar passivity.
The new calculation is the global on-shell elimination of that bank after
the complete polar subtraction and its identification with the Abel flux of
106.127.

Three later Phase-106 results are also binding.  Document 106.105 proves
that an exact source transfer has norm fixed by the physical spectral
floor; changing its realization cannot improve the gain.  Document 106.113
excludes a bounded divergence-free Hodge boundary-flux closure.  Document
106.129 proves that the complete radical frame has a signed projective
connection.  The delay realization below is consistent with all three: it
does not propose another local Schur factor, and its final term is the same
connection written in the moving Abel coordinate.

## 3. Exact displacement ports

For \(u>0\), let

\[
 (U_uq)(x)=q(x-u)
 \tag{9}
\]

be the real-translation operator on the multiplier core, and define

\[
 (C_uq)(x)
 =\{K(x)K(x-u)\}^{1/2}\{q(x)-q(x-u)\}.
 \tag{10}
\]

Then

\[
 \|C_uq\|_{L^2(dx)}^2
 =J_u(q)
 :=\int_{\mathbb R}K(x)K(x-u)|q(x)-q(x-u)|^2dx.
 \tag{11}
\]

This port has a literal lossless delay-line realization.  Put

\[
 z_u(s,x)=q(x-s),\qquad0\le s\le u.
 \tag{12}
\]

It solves

\[
 \partial_sz_u+\partial_xz_u=0,
 \qquad z_u(0,x)=q(x),
 \qquad z_u(u,x)=q(x-u).
 \tag{13}
\]

The local Hamiltonian \(|z_u|^2/2\) satisfies the exact boundary balance

\[
 \partial_x\int_0^u{|z_u(s,x)|^2\over2}ds
 ={|z_u(0,x)|^2-|z_u(u,x)|^2\over2}.
 \tag{14}
\]

Attaching the endpoint difference port in (10) and eliminating the unique
solution of (13) produces the terminal dissipation (11).  No approximation
of \(q(x-u)\) and no Taylor expansion in \(u\) occurs.

Let

\[
 d\nu_+(u)
 =\sum_{n\ge2}{\Lambda(n)\over\sqrt n}\delta_{\log n}(du)
  +g(u)du,
 \qquad
 d\nu_0(u)=2\cosh(u/2)du.
 \tag{15}
\]

The direct-integral observation maps are

\[
 \begin{aligned}
 C_+q&=(C_uq)_{u>0}
     \in\int_{(0,\infty)}^\oplus L^2(dx)\,d\nu_+(u),\\
 C_0q&=(C_uq)_{u>0}
     \in\int_{(0,\infty)}^\oplus L^2(dx)\,d\nu_0(u).
 \end{aligned}
 \tag{16}
\]

The singularity \(g(u)\sim(2u)^{-1}\) causes no defect on the form core,
because \(J_u(q)=O(u^2)\).  The double-exponential decay of \(K\) controls
the growing reference density in \(C_0\).  Therefore

\[
 \boxed{
 \|C_+q\|^2=\mathscr E_K(q),
 \qquad
 \|C_0q\|^2={1\over2}\mathrm{Var}_{\mu_K}(q).}
 \tag{17}
\]

The second identity is the exact ideal-cosh identity of 106.66.

## 4. The completed channel is exactly Krein

Give the output space of \(C_+\oplus C_0\) the fundamental symmetry

\[
 \mathcal J=I_{\mathscr Y_+}\oplus(-I_{\mathscr Y_0}).
 \tag{18}
\]

Then (17) gives

\[
\boxed{
 \langle(C_+q,C_0q),\mathcal J(C_+q,C_0q)\rangle
 =\mathscr E_K(q)-{1\over2}\mathrm{Var}_{\mu_K}(q).}
\tag{19}
\]

Using

\[
 d\nu_p=e^{u/2}du+e^{-u/2}d\{\psi(e^u)-e^u\},
 \tag{20}
\]

and

\[
 g(u)du=e^{-u/2}du
       +{e^{-5u/2}\over1-e^{-2u}}du,
 \tag{21}
\]

the \(e^{u/2}\) and \(e^{-u/2}\) line banks cancel the two halves of
\(2\cosh(u/2)\) exactly.  Thus (19) becomes

\[
\boxed{
 \langle Cq,\mathcal JCq\rangle
 =\int_0^\infty J_u(q)\,d\sigma(u),
 \qquad
 d\sigma(u)=e^{-u/2}d\{\psi(e^u)-e^u\}
 +{e^{-5u/2}\over1-e^{-2u}}du.}
\tag{22}
\]

This proves that the delay bank reproduces the exact signed measure of
106.66 and 106.127.

If \(q\) is centered, then

\[
 \mathrm{Var}_{\mu_K}(q)=\|q\|_{\mu_K}^2.
 \tag{23}
\]

Consequently, under the heat feedback generated by the completed form,

\[
 \partial_\tau q=-(C_+^*C_+-C_0^*C_0)q,
 \tag{24}
\]

one has the exact supply balance

\[
 {d\over d\tau}{\|q\|_{\mu_K}^2\over2}
 =-\|C_+q\|^2+\|C_0q\|^2
 =-\int_0^\infty J_u(q)d\sigma(u).
 \tag{25}
\]

Thus the sign sought in the physical-surplus theorem is exactly the
dissipativity of this Krein feedback.  It is not a consequence of the
lossless balances (14).

## 5. Why passive internal-state elimination cannot supply the sign

The obstruction can be stated without any spectral model.

### Lemma 1 — Hilbert-passive shorting preserves positivity

Let a closed quadratic form on \(\mathscr H\oplus\mathscr Z\) have block
operator

\[
 \mathbb M=
 \begin{pmatrix}A&B\\B^*&D\end{pmatrix}\ge0.
 \tag{26}
\]

Its shorted form

\[
 \mathfrak s(q)=\inf_{z\in\mathscr Z}
 \left\langle(q,z),\mathbb M(q,z)\right\rangle
 \tag{27}
\]

is nonnegative.  If \(D^{-1}\) exists on the relevant range, then

\[
 \mathfrak s(q)=\langle q,(A-BD^{-1}B^*)q\rangle\ge0.
 \tag{28}
\]

#### Proof

Every member of the family minimized in (27) is nonnegative.  This proves
the first statement.  Completing the square gives (28).  The general
closed-form statement follows by monotone regularization
\(D\mapsto D+\varepsilon I\). \(\square\)

Therefore a network built only from positive storage, positive terminal
resistors and passive feedback cannot *derive* the negative \(C_0\)-square
in (19).  One must either:

* retain \(C_0\) as a negative-energy/polar port, obtaining the exact Krein
  identity (19); or
* prove that the shorted Krein form is nonnegative on the physical range.

The second alternative is exactly the physical surplus.  Internal-state
elimination reorganizes it but cannot make it automatic.

## 6. Exact elimination of the moving prime lines

Let

\[
 E_1(T)=\psi(T)-T+1,
 \qquad D(T)={E_1(T)\over T},
 \qquad \phi=Kq,
 \qquad B=\partial+\frac12.
 \tag{29}
\]

The prime-line output at \(x\) is

\[
 S_x(\phi)
 =\sum_{n\ge2}{\Lambda(n)\over\sqrt n}\phi(x-\log n).
 \tag{30}
\]

Solving the translation lines and applying Stieltjes integration by parts
gives the exact identity

\[
\boxed{
 e^{-x/2}S_x(\phi)
 =\int_{-\infty}^x\phi(y)e^{-y/2}dy
  +\int_{-\infty}^xD(e^{x-y})e^{-y/2}B\phi(y)dy.}
\tag{31}
\]

For completeness, the first term is the continuum-line response.  The
second is the response of the signed discrepancy after the continuum has
been shorted.  If \(q\) is even and centered, the first term equals the
theta endpoint

\[
 -\int_x^\infty K(y)q(y)e^{-y/2}dy.
 \tag{32}
\]

Put

\[
 k_D(t)=e^{t/2}D(e^t).
 \tag{33}
\]

Then the nontrivial incoming channel in (31) is

\[
\boxed{
\mathcal F_D[q](x)
 =e^{-x/2}\int_0^\infty k_D(t)B\phi(x-t)dt.}
\tag{34}
\]

Pairing this output with the physical boundary row gives exactly

\[
\boxed{
\begin{aligned}
 \mathcal P_D(q)
 =-2\mathrm{Re}\,\int_{x>y}
 D(e^{x-y})e^{(x-y)/2}\,
 \overline{K(x)q(x)}\,B(Kq)(y)\,dy\,dx .
\end{aligned}}
\tag{34a}
\]

Thus the delay realization reproduces the signed quadratic Abel flux as
well as its linear input--output map.

This is an exact causal delay-line realization.  Indeed, with input
\(v=B\phi\), define the half-line memory state

\[
 z(x,t)=v(x-t),\qquad t\ge0.
 \tag{35}
\]

It solves

\[
 \partial_xz+\partial_tz=0,
 \qquad z(x,0)=v(x),
 \tag{36}
\]

and the output is the literal observation

\[
 y_D(x)=\int_0^\infty k_D(t)z(x,t)dt,
 \qquad \mathcal F_D[q](x)=e^{-x/2}y_D(x).
 \tag{37}
\]

For a finite memory interval the state has the lossless balance

\[
 \partial_x\int_0^T{|z(x,t)|^2\over2}dt
 ={|v(x)|^2-|v(x-T)|^2\over2}.
 \tag{38}
\]

The observation kernel \(k_D\), rather than the transport equation, carries
the arithmetic sign.

## 7. The exact Abel transfer and its pole test

Initially for \(\mathrm{Re}\,s>1/2\), PNT and (33) give

\[
\begin{aligned}
 \widehat k_D(s)
 &=\int_0^\infty D(e^t)e^{t/2}e^{-st}dt\\
 &=\int_1^\infty E_1(T)T^{-s-3/2}dT.
\end{aligned}
\tag{39}
\]

Set \(z=s+1/2\).  Since \(E_1(1)=0\), Stieltjes integration by parts gives

\[
 z\widehat k_D(s)
 =\int_1^\infty T^{-z}dE_1(T).
 \tag{40}
\]

For \(\mathrm{Re}\,z>1\),

\[
 \int_1^\infty T^{-z}dE_1(T)
 =-{\zeta'\over\zeta}(z)-{1\over z-1}.
 \tag{41}
\]

Equations (40)--(41) prove (5), first in its half-plane of absolute
definition and then meromorphically.

The principal pole at \(z=1\) cancels between the two terms in (41).  If
\(\rho\) is a nontrivial zero of multiplicity \(m_\rho\), then

\[
 \mathrm{Res}_{s=\rho-1/2}\widehat k_D(s)
 =-{m_\rho\over\rho}\ne0.
 \tag{42}
\]

The Gamma and pole/reference line banks have only their fixed
archimedean singularities; they are analytic at every nonreal
\(s=\rho-1/2\).  Hence they cannot cancel (42).

### Corollary 2 — Critical stability is already RH

The following are equivalent:

1. \(\widehat k_D\) has no pole in \(\mathrm{Re}\,s>0\);
2. \(\zeta\) has no zero with \(\mathrm{Re}\,\rho>1/2\);
3. RH holds.

#### Proof

The equivalence of 1 and 2 follows from (42).  The functional equation
maps a zero \(\rho\) to \(1-\rho\).  Thus the absence of zeros to the right
of the critical line also excludes zeros to its left. \(\square\)

In particular, any exact Hilbert-passive realization of (34) whose
transfer is analytic in the open right half-plane proves RH before an
energy inequality is applied.  The algebraic delay realization
(35)--(37) is unconditional, but its critical stable/passive extension is
not.  This is the global version of the pole defect which invalidated the
Phase-64 scalar local cells.

## 8. Compatibility with the complete mean-periodic constraint

Let

\[
 \mathscr C=(\mathbf1\oplus\mathcal R)^\perp,
 \qquad F=hq,
 \qquad a={K\over h}.
 \tag{43}
\]

For \(q\in\mathscr C\),

\[
 F*K=0,
 \qquad \phi=Kq=aF.
 \tag{44}
\]

The Abel drive is

\[
 v=B(aF)=aF'+(a'+\tfrac12a)F.
 \tag{45}
\]

Mean periodicity is invariant under differentiation, but not under the
nonconstant multiplier \(a\).  On the common convolution core,

\[
\begin{aligned}
 v*K
 &=\{(aF)'+\tfrac12aF\}*K\\
 &=(aF)*(K'+\tfrac12K).
\end{aligned}
\tag{46}
\]

This proves the connection identity (6).  Define

\[
 \boxed{
 \mathcal C_{K,h}F:=(aF)*(K'+\tfrac12K).}
 \tag{47}
\]

It is the exact transverse drive generated when a mean-periodic physical
row enters the Abel line.  It vanishes neither from \(F*K=0\) nor from
centering.  This agrees with the local-universality obstruction of 106.126
and the radical projective connection of 106.129: nonconstant local
multiplication is not an endomorphism of the complete mean-periodic
kernel.

The nonvanishing assertion is testable without a zero label.  Fix \(x_0\).
The value of (47) is the linear functional

\[
 F\longmapsto
 \int_{\mathbb R} a(y)F(y)
 \{K'(x_0-y)+\tfrac12K(x_0-y)\}\,dy.
 \tag{47a}
\]

Its analytic coefficient is not identically zero: \(a>0\), whereas
\(K'+K/2\not\equiv0\).  On an interval where it has strict sign, the local
universality theorem 106.126 supplies exact mean-periodic graph rows
approximating a compact profile of the same sign, with the required
weighted tail control.  Functional (47a) is then nonzero on one of those
rows.  Hence (47) cannot be deleted on the physical mean-periodic class.

If \(\Pi_{\mathcal M}\) denotes the projection onto

\[
 \mathcal M=\ker(f\mapsto f*K),
 \tag{48}
\]

then the exact unabsorbed internal port is

\[
 \boxed{
 (I-\Pi_{\mathcal M})B M_{K/h}F,}
 \tag{49}
\]

and its observable convolution is (47).  Dropping (49) is precisely the
invalid step which would make the zero-mode line appear passive.

## 9. Complete anti-short and surviving passivity statement

Let \(Q=P_{\mathscr C}\).  The exact delay bank after complete anti-shorting
is

\[
 \boxed{
 Q(C_+^*C_+-C_0^*C_0)Q.}
 \tag{50}
\]

On a theta boundary scale, the incoming component of (50) is (34), the
outgoing component is the same signed PNT discrepancy before the endpoint
lines are eliminated, and the strictly positive Gamma remainder has
density

\[
 {e^{-5u/2}\over1-e^{-2u}}.
 \tag{51}
\]

They are three coordinates of one Krein network and cannot be estimated
separately.  The exact remaining theorem is

\[
\boxed{
 \langle q,Q(C_+^*C_+-C_0^*C_0)Qq\rangle\ge0
 \qquad(q\in\mathscr C),}
\tag{52}
\]

or, in the boundary realization, joint nonnegativity of

\[
 \boxed{
 \text{outgoing signed PNT port}
 +\mathcal P_D(q)
 +\mathfrak b_{\Gamma,*}(q),}
 \tag{53}
\]

with the connection port (49) retained.  Equation (53) is exactly the
signed passivity gate (44) of 106.127.

The delay-line realization therefore does two useful things: it proves
that no prime, Gamma or polar boundary term is missing, and it identifies
the precise leakage created by the complete mean-periodic constraint.  It
does not convert the Krein supply rate into a positive Hilbert supply rate.
That conversion is the physical surplus itself.

## 10. Result

The ordinary-prime--Gamma--pole channel has a complete exact network
realization:

\[
 \boxed{
 \text{positive prime/Gamma delay bank}
 \ \ominus\ 
 \text{ideal-cosh polar delay bank}.}
 \tag{54}
\]

On-shell elimination gives both the compensated measure \(d\sigma\) and
the moving Abel flux, with transfer (5).  The construction is not the
withdrawn scalar Euler colligation of Phase 64, and it makes no false local
passivity claim.

The exact obstruction is now visible in two equivalent forms:

\[
 \boxed{
 \text{right-half-plane poles of }\widehat k_D
 \quad\Longleftrightarrow\quad
 \text{off-line zeta zeros},}
 \tag{55}
\]

and

\[
 \boxed{
 \mathcal C_{K,h}F=(K/h\,F)*(K'+\tfrac12K),}
 \tag{56}
\]

the radical-connection port which survives exact mean periodicity.  A
successful successor must prove dissipativity of the compressed Krein
network with (56) included; a passive delay-line ansatz without that term
is incomplete.
