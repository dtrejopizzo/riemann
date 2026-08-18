# 106.127 — Theta boundary Mosco limit and the signed PNT flux gate

## 1. Purpose and verdict

Let

\[
 \mathscr C=(\mathbf 1\oplus\mathcal R)^\perp,
 \qquad A=L|_{\mathscr C},
 \tag{1}
\]

where \(L\) is the complete ordinary-prime--Gamma Doob generator.  The
essential-floor theorem allows a hypothetical sequence of normalized
eigenstates

\[
 Aq_j=\alpha_jq_j,
 \qquad \alpha_j\uparrow\frac12,
 \qquad q_j\rightharpoonup0\ \hbox{locally}.
 \tag{2}
\]

This note computes the operator seen by such a sequence at a positive
spatial end.  The conclusions are precise.

1.  Translation by a fixed \(y\) is not the theta boundary scale.  If
    \(w=hK/c_K\) is the Doob density, the unique nondegenerate scale at
    \(R\) is

    \[
      \varepsilon_R={-\partial_x\log w(R)\}^{-1}
      \sim {e^{-2R}\over2\pi}.
      \tag{3}
    \]

    On \(x=R+\varepsilon_Ry\), the conditional tail law tends to
    \(e^{-y}dy\) on \(\mathbb R_+\).
2.  Before radical compression, the Dirichlet boundary forms converge in
    the Mosco sense to \(\frac12 I\).  Hence their resolvents converge
    strongly.  Norm-resolvent convergence is impossible because the Gamma
    small-jump operator remains unbounded for every finite \(R\).
3.  The value \(1/2\) is not merely a PNT asymptotic.  The PNT continuum
    and the \(e^{-u/2}\) piece of Gamma give exactly \(\frac12 I\) on the
    even centered sector.  The first correction is the compensated signed
    measure

    \[
      d\sigma(u)=e^{-u/2}d\{\psi(e^u)-e^u\}
      +{e^{-5u/2}\over1-e^{-2u}}du.
      \tag{4}
    \]

4.  For a fixed smooth boundary profile, the positive long-jump Gamma
    correction is

    \[
      e^{-3R}\int_{\mathbb R}e^{5z/2}K(z)dz
      =e^{-3R}\Xi(5i/2)
      =e^{-3R}\xi(3)>0.
      \tag{5}
    \]

    It is preceded by the literal signed PNT quadrature, whose sign and
    true scale are not fixed by PNT.
5.  Keeping the complete radical projection exposes the remaining issue.
    The ambient Mosco recovery vectors need not survive projection onto
    \(\mathscr C\).  The exact next operator is the compressed signed flux
    \(Q_R\mathcal B_RQ_R\), not the scalar \(1/2\).  Its PNT part has a
    convention-free Abel representation in terms of
    \(D(T)=\{\psi(T)-T+1\}/T\), but the paired flux is not positive.

Thus the ultraviolet and ambient spatial limits are now determined.  The
remaining physical-surplus theorem is a signed passivity estimate for the
literal Abel flux on boundary profiles which actually lie in the transported
complete radical complement.

## 2. Semantic audit

The following earlier calculations were checked before taking the limit.

* 106.24 concerns the prolate endpoint and exterior \(H^1\) leakage.  Its
  scale is the semilocal aperture scale, not the double-exponential theta
  scale (3).
* 106.43 identifies the complete complement by \((hq)*K=0\).  It does not
  provide weighted boundary observability.
* 106.44 proves that the continuum prime operator tends to \(1/2\) and
  writes the arithmetic resonance through the signed PNT discrepancy.
* 106.47 proves the moving-PNT tail floor, local compactness and the exact
  nonlocal IMS identity.  It gives the Mosco liminf used below, but not a
  recovery sequence after complete radical projection.
* 106.66 gives the exact ideal-cosh displacement density
  \(2\cosh(u/2)\) and the compensated measure (4).  The exact cancellation
  in Section 4 below is its operator version.
* 106.69--106.70 show that mean periodicity does not imply weighted form
  synthesis and that real translations are unbounded in the physical
  weighted topology.
* 106.87 and 106.90 give finite local Christoffel detection only after a
  finite mode block has been fixed.  They provide no complete-radical
  boundary recovery theorem.
* 106.113 closes the bounded Hodge boundary-flux escape.  The Abel flux
  below is not divergence-free Hodge flux; it is the signed arithmetic
  part of the physical generator itself.
* 106.120--106.123 isolate threshold spatial escape and remove its local
  ultraviolet component for actual eigenstates.

No Phase-106 document computes the theta-scale Mosco limit, the coefficient
in (5), or the exact normalized Abel flux below.  Earlier uses of Mosco in
the prolate/CCM programme concern a different family of finite semilocal
operators.

## 3. The natural theta boundary scale

Put

\[
 h(x)=\cosh(x/2),\qquad c_K=\frac12,qquad
 w(x)={h(x)K(x)\over c_K}.
 \tag{6}
\]

The first theta summand gives, as \(x\to+\infty\),

\[
 K(x)=2\pi^2C_\Xi e^{9x/2}e^{-\pi e^{2x}}
 \left(1-{3\over2\pi}e^{-2x}
       +O(e^{-3\pi e^{2x}})\right).
 \tag{7}
\]

Consequently

\[
 w(x)=2\pi^2C_\Xi e^{5x}e^{-\pi e^{2x}}
 \{1+e^{-x}+O(e^{-2x})\},
 \tag{8}
\]

and

\[
 b_R:=-\partial_x\log w(R)
 =2\pi e^{2R}-5+e^{-R}+O(e^{-2R}),
 \qquad \varepsilon_R=b_R^{-1}.
 \tag{9}
\]

For every fixed compact set of \(y\)'s,

\[
 {w(R+\varepsilon_Ry)\over w(R)}
 =e^{-y}\{1+O_R(e^{-2R})(1+y^2)\}.
 \tag{10}
\]

Laplace's endpoint method also gives

\[
 M_R:=\int_R^\infty w(x)dx
 =\varepsilon_Rw(R)\{1+O(e^{-2R})\}.
 \tag{11}
\]

Equations (10)--(11) prove that the conditional positive-tail law,
pulled back by \(x=R+\varepsilon_Ry\), converges in total variation on
compact sets to \(e^{-y}dy\).  A fixed translation \(x=R+y\) would instead
collapse all its mass at the left endpoint; it is therefore a singular
coordinate for the tail problem.

For \(g\in C_c^\infty(0,\infty)\), define its exact even two-tail lift by

\[
 (V_Rg)(\pm(R+\varepsilon_Ry))
 ={e^{-y/2}g(y)\over
   \sqrt{2\varepsilon_Rw(R+\varepsilon_Ry)}}
 \quad(y>0),
 \tag{12}
\]

and set it equal to zero on \((-R,R)\).  Then

\[
 \|V_Rg\|_{L^2(\mu_K)}^2
 =\int_0^\infty|g(y)|^2e^{-y}dy.
 \tag{13}
\]

Its mean is \(O(\sqrt{M_R})\), so subtracting the constant mode changes
neither the boundary profile nor any estimate below.

## 4. The threshold is an exact operator cancellation

Split the prime measure and the Gamma density as

\[
 d\nu_p=e^{u/2}du+e^{-u/2}d\{\psi(e^u)-e^u\},
 \qquad
 g(u)du=e^{-u/2}du+{e^{-5u/2}\over1-e^{-2u}}du.
 \tag{14}
\]

Let \(L_0\) be the jump operator with density \(e^{u/2}du\), and let
\(L_{\Gamma,0}\) have density \(e^{-u/2}du\).  Directly changing
variables in both orientations gives

\[
 (L_0+L_{\Gamma,0})q(x)
 ={2c_K\over h(x)}\int_{\mathbb R}K(z)
 \cosh\!\left({x-z\over2}\right){q(x)-q(z)\}dz.
 \tag{15}
\]

If \(q\) is even, then the sinh term in the addition formula integrates
to zero.  If it is also centered, then

\[
 \int K(z)h(z)q(z)dz=0,
 \qquad
 \int K(z)h(z)dz=c_K.
 \tag{16}
\]

Using \(2c_K^2=1/2\) in (15) yields the exact identity

\[
 \boxed{(L_0+L_{\Gamma,0})q=\frac12q.}
 \tag{17}
\]

Equivalently, if \(\mathfrak b_\sigma\) denotes the form generated by
(4), then on \(\mathscr C\)

\[
 \boxed{
 \langle q,(A-\tfrac12)q\rangle
 =\mathfrak b_\sigma(q)
 =\int_0^\infty J_u(q)d\sigma(u).}
 \tag{18}
\]

This calculation must precede every tail estimate.  Estimating the PNT
continuum and Gamma separately loses the exact cancellation of their
order-\(e^{-R}\) terms.

## 5. Ambient Mosco limit and failure of norm resolvent convergence

Let \(L_R^D\) be the Friedrichs operator of the complete form restricted
to even functions which vanish on \((-R,R)\), transported by (12) to

\[
 \mathscr H_\partial=L^2(\mathbb R_+,e^{-y}dy).
 \tag{19}
\]

### Theorem 1 — Ambient boundary Mosco limit

The transported forms converge in the Mosco sense:

\[
 \boxed{
 \mathfrak l_R^D\ \xrightarrow[\ R\to\infty\ ]{\rm Mosco}\
 \frac12\|\cdot\|_{\mathscr H_\partial}^2.}
 \tag{20}
\]

Consequently

\[
 (L_R^D+z)^{-1}\longrightarrow(\tfrac12+z)^{-1}I
 \quad\hbox{strongly}\qquad(z>0).
 \tag{21}
\]

#### Proof

For the liminf, pull a weakly convergent sequence back by (12).  Every
pullback vanishes on \((-R,R)\), so the uniform moving-PNT tail floor of
106.47 applies directly and gives

\[
 \liminf_R\mathfrak l_R^D(g_R)
 \ge\frac12\liminf_R\|g_R\|^2.
 \tag{22}
\]

Weak lower semicontinuity of the Hilbert norm proves the Mosco liminf.  No
shrinking-width IMS estimate is needed here; the nonlocal IMS calculation
enters only when a physical eigenstate is first separated into its central
and tail pieces.

For recovery, take first \(g\in C_c^\infty(0,\infty)\).  In the lift
\(V_Rg\), every fixed prime displacement is much larger than the boundary
width, while displacements comparable with \(\varepsilon_R\) contain no
prime atom.  Moving PNT gives the prime killing rate \(1/2+o(1)\).  The
Gamma small-jump form is

\[
 O_g\!\left({K(R)\over h(R)}\log\varepsilon_R^{-1}\right)=o(1),
 \tag{23}
\]

and its long-jump part is \(O(e^{-R})\) before the exact cancellation in
(17).  Thus (17), or equivalently (18) and PNT, gives

\[
 \mathfrak l_R^D(V_Rg)=\frac12\|g\|^2+o(1).
 \tag{24}
\]

Density and the liminf extend recovery to every \(g\in\mathscr H_\partial\).
This proves Mosco convergence and hence (21).  \(\square\)

Norm-resolvent convergence does not hold.  For every finite \(R\), the
Gamma \(u^{-1}\) singularity makes \(L_R^D\) unbounded above.  Since the
limit is the scalar \(1/2\), functional calculus gives

\[
 \left\|(L_R^D+1)^{-1}-{2\over3}I\right\|
 =\sup_{\lambda\in\sigma(L_R^D)}
 \left|{1\over1+\lambda}-{2\over3}\right|
 ={2\over3}.
 \tag{25}
\]

The correct topology is therefore strong resolvent/Mosco, not norm
resolvent.

## 6. The first boundary correction

Write

\[
 E_1(T)=\psi(T)-T+1,
 \qquad D(T)={E_1(T)\over T}.
 \tag{26}
\]

The \(+1\) is the endpoint convention which makes \(E_1(1)=0\); it does
not change \(dE_1=d\{\psi(T)-T\}\).

For the outgoing diagonal quadrature define

\[
 \Delta_\psi(x)
 ={c_K\over h(x)}\int_{(0,\infty)}
 \{K(x-u)+K(x+u)\}e^{-u/2}\,dE_1(e^u).
 \tag{27}
\]

The PNT gives \(\Delta_\psi^{(j)}(x)=o(1)\), for every fixed \(j\), and
an effective Vinogradov--Korobov input gives the corresponding usual
subexponential envelope.  No sign follows.

Choose \(\ell_R\downarrow0\) with
\(\ell_R/\varepsilon_R\to\infty\), for example
\(\ell_R=e^{-R}\).  The range \(0<u<\ell_R\) contributes

\[
 O_g\!\left(e^{-B R}\right)\quad\hbox{for every fixed }B>0
 \tag{28}
\]

to a fixed smooth profile: the small-jump singularity is cancelled by the
difference and the remaining coefficient is \(K(R-\ell_R)/h(R)\).
For the positive Gamma remainder, put \(z=x-u\).  Uniformly for
\(x=R+O(\varepsilon_R)\),

\[
\begin{aligned}
 {c_K\over h(x)}\int_{\ell_R}^\infty
 K(x-u){e^{-5u/2}\over1-e^{-2u}}du
 &=e^{-3x}\int_{\mathbb R}e^{5z/2}K(z)dz
   +o(e^{-3R})\\
 &=e^{-3R}\xi(3)+o(e^{-3R}).
\end{aligned}
 \tag{29}
\]

The forward theta translate is smaller than every exponential.  It follows
that, for every fixed smooth boundary profile,

\[
\boxed{
\begin{aligned}
 \mathfrak b_\sigma(V_Rg)
={}&\int_0^\infty e^{-y}|g(y)|^2
       \Delta_\psi(R+\varepsilon_Ry)dy\\
 &+e^{-3R}\xi(3)\|g\|_{\mathscr H_\partial}^2
 +o(e^{-3R})+O_g(e^{-BR}).
\end{aligned}}
 \tag{30}
\]

Here the last term denotes only theta-local errors; it does not absorb the
PNT term.  Expanding the first line, when desired, gives

\[
 \Delta_\psi(R)\|g\|^2
 +\varepsilon_R\Delta_\psi'(R)
   \int_0^\infty y|g(y)|^2e^{-y}dy
 +O_g(\varepsilon_R^2\eta_2(R)),
 \tag{31}
\]

where \(\eta_2(R)=\sup_{x\ge R}|\Delta_\psi''(x)|\to0\).
Thus the first correction is not universally the positive term (5).  It is
the signed arithmetic multiplication operator in the first line of (30).
Even its first profile-dependent variation,
\(\varepsilon_R\Delta_\psi'(R)y\), can be larger than \(e^{-3R}\xi(3)\).

## 7. Exact Abel form of the incoming PNT channel

The diagonal correction (27) is sufficient for a Dirichlet boundary
profile, but an actual eigenstate is not cut off: its values one prime jump
inward must be retained.  There is an exact signed representation.

For a smooth rapidly decreasing \(\phi\), set

\[
 S_x(\phi)=\sum_{n\ge2}{\Lambda(n)\over\sqrt n}
 \phi(x-\log n).
 \tag{32}
\]

### Lemma 2 — Normalized moving-Abel identity

With the endpoint convention (26),

\[
\boxed{
\begin{aligned}
 e^{-x/2}S_x(\phi)
={}&\int_{-\infty}^x\phi(y)e^{-y/2}dy\\
 &+\int_{-\infty}^xD(e^{x-y})e^{-y/2}
       \{\phi'(y)+\tfrac12\phi(y)\}dy.
\end{aligned}}
 \tag{33}
\]

#### Proof

Write (32) as the Stieltjes integral of
\(f_x(T)=T^{-1/2}\phi(x-\log T)\) against \(d\psi(T)\), beginning at
\(T=1\).  The \(dT\) part is

\[
 e^{x/2}\int_{-\infty}^x\phi(y)e^{-y/2}dy.
 \tag{34}
\]

Since \(E_1(1)=0\), integration by parts has no lower endpoint term, and

\[
 f_x'(T)=-T^{-3/2}
 \{\phi'(x-\log T)+\tfrac12\phi(x-\log T)\}.
 \tag{35}
\]

The upper endpoint vanishes by PNT and the decay of \(\phi\).  Substitute
\(T=e^{x-y}\), divide by \(e^{x/2}\), and obtain (33). \(\square\)

Take \(\phi=Kq\).  If \(q\) is even and centered, then

\[
 \int_{\mathbb R}K(y)q(y)e^{-y/2}dy=0.
 \tag{36}
\]

Therefore the first line of (33) is only the theta tail

\[
 -\int_x^\infty K(y)q(y)e^{-y/2}dy,
 \tag{37}
\]

and the nontrivial incoming prime channel is the signed flux

\[
\boxed{
 \mathcal F_D[q](x)
 :=\int_{-\infty}^xD(e^{x-y})e^{-y/2}
 \{(Kq)'(y)+\tfrac12K(y)q(y)\}dy.}
 \tag{38}
\]

Pairing the eigen-equation with \(q\) does not make (38) positive.  Its
Hermitian quadratic contribution is, up to the theta endpoint (37),

\[
\boxed{
\begin{aligned}
 \mathcal P_D(q)
 =-2\operatorname {Re}\int_{x>y}
 D(e^{x-y})e^{(x-y)/2}\,
 \overline{K(x)q(x)}
 \{(Kq)'(y)+\tfrac12K(y)q(y)\}\,dy\,dx.
\end{aligned}}
 \tag{39}
\]

The derivative and the undifferentiated term in (39) must remain together.
An integration by parts which replaces them by total variation of \(D\),
or an estimate using \(|D|\), returns to the loss quantified in 106.118.
Equation (39) is the exact signed passivity observable left by the physical
eigen-equation.

## 8. Keeping the complete radical projection

Let \(Q=P_{\mathscr C}\).  Since the radical is an exact threshold
eigenspace, \(Q\) reduces \(L\).  Under any unitary realization \(U_R\) of
the boundary scaling, put

\[
 Q_R=U_RQU_R^{-1}.
 \tag{40}
\]

The exact compressed form is

\[
\boxed{
 A_R-\frac12I
 =Q_R\mathcal B_{\sigma,R}Q_R
 \quad\hbox{on }\operatorname {Ran}Q_R.}
 \tag{41}
\]

No projection has been discarded in (41).  The ambient recovery sequence
\(V_Rg\) used in Theorem 1 need not satisfy

\[
 \|Q_RV_Rg-V_Rg\|\longrightarrow0.
 \tag{42}
\]

Indeed, (42) is a theta-boundary form-synthesis statement for the complete
mean-periodic complement.  It is not implied by \((hq)*K=0\), and it is
exactly the spatial observability issue isolated in 106.70 and 106.123.

Consequently Theorem 1 proves the ambient strong-resolvent limit, while for
\(A_R\) it proves only the Mosco liminf.  Any limit profile of actual
subthreshold eigenstates already belongs to \(\operatorname {Ran}Q_R\),
and its first correction is not (30) with an arbitrary \(g\), but

\[
 \boxed{
 Q_R\left[
 M_{\Delta_\psi(R+\varepsilon_R\cdot)}
 +e^{-3R}\xi(3)I+\mathcal T_R
 \right]Q_R,}
 \tag{43}
\]

where \(\mathcal T_R\) contains the exact incoming flux (38), the
small-jump remainder and theta-superexponential terms.  It tends to zero
strongly on every fixed smooth ambient profile, but not in norm and not
uniformly on the moving ranges \(\operatorname {Ran}Q_R\).

## 9. The signed passivity theorem now required

The boundary calculation rules out a purely asymptotic proof based only on
the statement that the tail operator tends to \(1/2I\).  That convergence
has zero margin and is already exhausted by (20).

The exact successor is the following one-sided statement.  For every
normalized sequence \(g_R\in\operatorname {Ran}Q_R\) which can arise from
an actual subthreshold eigenstate and is tight in the theta boundary
coordinate,

\[
\boxed{
 \liminf_{R\to\infty}
 \left{
  \mathcal P_D(g_R)
  +\mathfrak b_{\Gamma,*}(g_R)
  +\text{the coupled outgoing PNT term}
 \right}\ge0.}
 \tag{44}
\]

Here \(\mathfrak b_{\Gamma,*}\) is generated by the positive density
\(e^{-5u/2}(1-e^{-2u})^{-1}\), and the outgoing and incoming PNT terms are
the two parts of the same signed form; they may not be estimated
separately.  On a fixed Dirichlet profile, (44) reduces at first order to

\[
 \int e^{-y}|g(y)|^2\Delta_\psi(R+\varepsilon_Ry)dy
 +e^{-3R}\xi(3)\|g\|^2\ge-o(e^{-3R}).
 \tag{45}
\]

For actual mean-periodic profiles the nonlocal flux (39) is also leading.
Proving (44), or proving instead that no nonzero tight profile can belong
to the moving ranges \(\operatorname {Ran}Q_R\), excludes the threshold
escape of 106.123.  The present calculation proves neither alternative;
it identifies their exact operators, scales and signs without replacing
the literal von Mangoldt discrepancy by an absolute envelope.

## 10. Result

The spatial end has a universal ambient limit, but that limit is only the
threshold scalar:

\[
 \boxed{L_R^D\xrightarrow{\rm strong\ resolvent}\frac12I.}
 \tag{46}
\]

The cancellation producing \(1/2\) is exact, and the first deterministic
positive correction is \(e^{-3R}\xi(3)\).  The correction which can decide
the sign appears earlier: it is the signed PNT multiplication/flux operator
(27), (38)--(39), compressed by the complete transported radical projection.
The remaining theorem is therefore not another tail floor or another
compactness statement.  It is signed boundary passivity on the moving
mean-periodic range, with all ordinary prime phases and the positive Gamma
remainder retained jointly.
