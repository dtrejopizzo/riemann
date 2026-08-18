# 106.18 — Exact PNT-discrepancy compensation and the remaining signed measure

## Purpose

Document 106.17 rewrites the finite ordinary-prime--Gamma multiplier as a
positive centered jump form.  This note gives a complementary physical-side
identity.  It performs the prime, pole and Gamma cancellation before any
absolute value and shows exactly what remains:

\[
\boxed{\text{one explicit locally singular kernel}
+\text{ one Stieltjes integral against }d(\psi(x)-x).}
\]

The continuous PNT main term cancels the growing polar branch exactly, and
the remaining polar branch cancels jointly with Gamma.  The only unresolved
signed arithmetic input not eliminated by algebra is the actual prime
discrepancy measure; the remaining explicit kernel must still be controlled
jointly with it.

## 1. Correlation coordinate

Let \(f,g\) be smooth functions supported in the additive interval \(I_L\),
extended by zero.  Put

\[
 H(u)=\langle f,\tau_ug\rangle,
 \qquad
 F(u)=H(u)+H(-u),
 \qquad 0\le u\le L.
\tag{1}
\]

For a Gate-SPG cross term, \(g\perp f\), and therefore

\[
 H(0)=0,\qquad F(0)=0.
\tag{2}
\]

Write

\[
 \Psi(u)=\psi(e^u).
\tag{3}
\]

The Stieltjes measure \(d\Psi\) has an atom of mass \(\Lambda(n)\) at
\(u=\log n\).

## 2. Joint prime--pole cancellation

In the CCM normalization, the polar and Euler cross terms are

\[
\begin{aligned}
 P(f,g)
 &=\int_0^L F(u)\bigl(e^{u/2}+e^{-u/2}\bigr)\,du,\\
 E(f,g)
 &=-\int_{(0,L]}F(u)e^{-u/2}\,d\Psi(u).
\end{aligned}
\tag{4}
\]

### Theorem 1 — Exact PNT compensation

One has

\[
\boxed{
 P(f,g)+E(f,g)
 =
 \int_0^L F(u)e^{-u/2}\,du
 -\int_{(0,L]}F(u)e^{-u/2}\,
   d\bigl(\Psi(u)-e^u\bigr).}
\tag{5}
\]

#### Proof

Since \(d(e^u)=e^u\,du\),

\[
\begin{aligned}
 -\int F(u)e^{-u/2}\,d(\Psi(u)-e^u)
 &=
 -\int F(u)e^{-u/2}\,d\Psi(u)
 +\int F(u)e^{u/2}\,du.
\end{aligned}
\tag{6}
\]

Adding the remaining \(e^{-u/2}\) polar branch gives (5). \(\square\)

Thus no asymptotic PNT estimate is used in (5): the main measure \(d(e^u)\)
has been inserted and cancelled exactly.

## 3. Joint Gamma compensation

The off-diagonal Gamma kernel is

\[
 c_\infty(u)=\frac{e^{-u/2}}{1-e^{-2u}},
\tag{7}
\]

and its cross term is

\[
 G(f,g)=-\int_0^L F(u)c_\infty(u)\,du.
\tag{8}
\]

### Theorem 2 — Complete signed prime--Gamma--pole identity

For every cross term satisfying (2),

\[
\boxed{
\begin{aligned}
 P(f,g)+G(f,g)+E(f,g)
 &=
 -\int_0^L
 F(u)\frac{e^{-5u/2}}{1-e^{-2u}}\,du\\
 &\quad
 -\int_{(0,L]}F(u)e^{-u/2}\,
 d\bigl(\psi(e^u)-e^u\bigr).
\end{aligned}}
\tag{9}
\]

#### Proof

Subtract (8) from the first integral on the right of (5).  The elementary
identity

\[
 e^{-u/2}-\frac{e^{-u/2}}{1-e^{-2u}}
 =
 -\frac{e^{-5u/2}}{1-e^{-2u}}
\tag{10}
\]

gives (9). \(\square\)

Near zero the first kernel in (9) is \(1/(2u)+O(1)\).  Condition (2) and
smoothness give \(F(u)=O(u)\), so the integral is finite.  This is why the
cross-term orthogonality must be retained when using (9).

Equation (9) is the requested global signed cancellation identity.  It
uses the actual atoms \(\Lambda(n)\), the Gamma factor and both polar
branches jointly.  It does not take an absolute value of any of the three
source terms.  The identity is proved on the smooth form core.  Extending
the two separated integrals in (9) to arbitrary Gate-SPG form-domain pairs
requires a separate joint-continuity argument and is not asserted here.

## 4. Rectangular wave packets

The remaining sign can be exposed on the normalized packet

\[
 f_{L,U}(x)
 =
 L^{-1/2}e^{iUx}\mathbf1_{[-L/2,L/2]}(x).
\tag{11}
\]

This is a diagonal calculation: \(F(0)=2\), so it is not an application of
the cross identity (9).  The Gamma term below is the unsplit full
archimedean packet value.

Define

\[
\begin{aligned}
 S_L(U)
 &:=
 \sum_{n\le e^L}
 \frac{\Lambda(n)}{\sqrt n}
 \left(1-\frac{\log n}{L}\right)
 \cos(U\log n),\\
 M_\pm(L,U)
 &:=
 \int_0^L e^{\pm u/2}
 \left(1-\frac uL\right)\cos(Uu)\,du,\\
 \Delta_L(U)&:=S_L(U)-M_+(L,U).
\end{aligned}
\tag{12}
\]

The packet correlation is

\[
 F(u)=2(1-u/L)\cos(Uu),\qquad 0\le u\le L.
\tag{13}
\]

### Proposition 3 — Exact packet compensation

Put

\[
 A_+(L,U)=
 \frac{2\sinh((1/2+iU)L/2)}
 {\sqrt L\,(1/2+iU)}.
\tag{14a}
\]

The polar term is

\[
\boxed{
 P_L(U)
 =
 2\operatorname {Re}A_+(L,U)^2
 =
 2\bigl(M_+(L,U)+M_-(L,U)\bigr).}
\tag{14}
\]

It is not sign-definite.  Its exact real form is

\[
\boxed{
\begin{aligned}
 P_L(U)
 =\frac{4}{L(U^2+1/4)^2}\Big[
 &(1/4-U^2)\bigl(\cosh(L/2)\cos(UL)-1\bigr)\\
 &+U\sinh(L/2)\sin(UL)
 \Big].
\end{aligned}}
\tag{14b}
\]

and

\[
\boxed{P_L(U)+E_L(U)=2M_-(L,U)-2\Delta_L(U).}
\tag{15}
\]

Consequently, if \(A_{\Gamma,L}(U)\) denotes the Gamma value of this
packet, then

\[
\boxed{
 Q_L(f_{L,U},f_{L,U})
 =
 A_{\Gamma,L}(U)+2M_-(L,U)-2\Delta_L(U).}
\tag{16}
\]

#### Proof

Substitute (13) in (4).  The elementary integral of
\((1-u/L)e^{(\pm1/2+iU)u}\) gives (14).  Expanding \(A_+^2\) gives
(14b).  The Euler atom sum is \(-2S_L(U)\), and (15)--(16) follow.
\(\square\)

Thus a sufficient scalar theorem for all rectangular packets is

\[
\boxed{
 \Delta_L(U)
 \le M_-(L,U)+\frac12A_{\Gamma,L}(U)
 \qquad(L>0,\ U\in\mathbb R).}
\tag{17}
\]

The inequality (17) is not proved here.  Perron inversion shows why it is
force-bearing: an off-line zero contributes an exponentially growing term
to \(\Delta_L(U)\) after a resonant choice of \(U\); if several extremal
zeros occur, a Turán power-sum selection is required.  Hence (17) is a
packet version of the signed branch theorem, not a consequence of PNT
alone.

## 5. A rigorous far-center exclusion

Although (17) remains open globally, the exact packet coordinate improves
the crude center range.

Let \(a_\infty(t)=2\theta'(t)\), and set

\[
 c_\Gamma=\frac1{4\pi},
 \qquad
 C_\Gamma=
 \sup_{t\in\mathbb R}
 \left[
 c_\Gamma\log(2+|t|)-a_\infty(t)
 \right]<\infty.
\tag{18a}
\]

Then

\[
 a_\infty(t)\ge
 c_\Gamma\log(2+|t|)-C_\Gamma.
\tag{18}
\]

Assume the elementary Chebyshev bound

\[
 \psi(x)\le C_\psi x\qquad(x\ge1).
\tag{19}
\]

Put

\[
 m_0=\frac2\pi\int_0^1\left(\frac{\sin y}{y}\right)^2dy
 \ge\frac{2\sin^2(1)}{\pi}.
\tag{20}
\]

### Proposition 4 — Packet centers beyond the exponential strip

For \(L\ge2\) and \(|U|\ge4\),

\[
\boxed{
 Q_L(f_{L,U},f_{L,U})
 \ge
 m_0c_\Gamma\log(2+|U|/2)-C_\Gamma
 -\frac{8C_\psi e^{L/2}}{L}
 -\frac{5e^{L/2}}{LU^2}.}
\tag{21}
\]

In particular, the packet form is nonnegative whenever

\[
 \log(2+|U|/2)
 \ge
 \frac{C_\Gamma+(8C_\psi+5/16)\lambda/L}
 {m_0c_\Gamma}.
\tag{22}
\]

#### Proof

The Fourier density of (11) has mass \(m_0\) in
\(|t-U|\le2/L\).  Applying (18) on this interval gives the first two terms
in (21), after increasing \(C_\Gamma\) to cover bounded \(U\).

The exact formula (14b) gives, for \(L\ge2\) and \(|U|\ge4\),

\[
\begin{aligned}
 P_L(U)
 &\ge-\frac4L\left[
 \frac{\cosh(L/2)+1}{U^2+1/4}
 +\frac{|U|\sinh(L/2)}{(U^2+1/4)^2}
 \right]\\
 &\ge-\frac{5e^{L/2}}{LU^2}.
\end{aligned}
\tag{22a}
\]

Moreover,

\[
 |S_L(U)|\le S_L(0).
\tag{23}
\]

Stieltjes integration by parts, (19), and
\[
 \frac{d}{dx}\left[
 x^{-1/2}\left(1-\frac{\log x}{L}\right)\right]
 =
 -x^{-3/2}
 \left[
 \frac12\left(1-\frac{\log x}{L}\right)+\frac1L
 \right]
\tag{24}
\]
give

\[
 S_L(0)\le\frac{4C_\psi e^{L/2}}{L}.
\tag{25}
\]

The Euler contribution is \(-2S_L(U)\).  Combining these estimates proves
(21), and (22) follows. \(\square\)

The old absolute estimate confined possible negative wells to
\(|U|\le\exp(C\lambda)\).  Equation (22) improves this to

\[
 |U|\le\exp(C\lambda/L).
\tag{26}
\]

It is a genuine center-dependent gain, but it still leaves every fixed
height as \(L\to\infty\) and therefore cannot imply RH.

## 6. The tapered second moment still loses the center

The exact polar weight does not repair the center loss at the level of
second moments.  Define

\[
 \mathcal P_L^\triangle(t)
 =
 \sum_{n\le e^L}\frac{\Lambda(n)}{\sqrt n}
 \left(1-\frac{\log n}{L}\right)n^{-it}.
\tag{27}
\]

The classical zero-free-region PNT and partial summation give

\[
\begin{aligned}
 A_2(L)
 &:=
 \sum_{n\le e^L}\frac{\Lambda(n)^2}{n}
 \left(1-\frac{\log n}{L}\right)^2
 =\frac{L^2}{12}+O(1),\\
 B_2(L)
 &:=
 \sum_{n\le e^L}\Lambda(n)^2
 \left(1-\frac{\log n}{L}\right)^2
 \sim\frac{2e^L}{L}.
\end{aligned}
\tag{28}
\]

The two-sided Montgomery--Vaughan mean-value theorem, uniformly in the
center \(U\), therefore gives for \(Y=e^L/L\)

\[
\boxed{
 \frac1{2Y}\int_{U-Y}^{U+Y}
 |\mathcal P_L^\triangle(t)|^2dt
 =
 \frac{L^2}{12}+O(1).}
\tag{29}
\]

The main term is independent of \(U\).  Even after the exact polar taper,
an \(L^2\) argument contains no center decay.  The remaining estimate must
be one-sided and signed.

## 7. Remaining theorem

The exact cancellation has now been completed algebraically:

\[
\boxed{
 \text{prime main term}+\text{growing pole}=0,\qquad
 \text{remaining pole}+\text{Gamma}
 =-\frac{e^{-5u/2}}{1-e^{-2u}}.}
\tag{30}
\]

The only unknown arithmetic distribution is

\[
 d\bigl(\psi(e^u)-e^u\bigr)
\tag{31}
\]

against the correlations generated by the moving co-Poisson vector and its
orthogonal complement, at the \(d_8\) scale of Gate SPG.  The explicit
locally singular integral in (9) must be controlled at the same scale; it
has no sign for a general cross correlation.  Equation (9) prevents any
future proof from estimating the original prime, Gamma and pole channels
separately; (17) is its simplest packet-level falsifier.

No such uniform one-sided estimate is proved in this note, so Gate SPG and
RH remain open.
