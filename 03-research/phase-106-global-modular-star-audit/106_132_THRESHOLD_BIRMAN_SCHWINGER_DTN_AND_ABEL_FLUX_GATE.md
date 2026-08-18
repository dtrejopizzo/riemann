# 106.132 — Threshold Birman--Schwinger/DtN expansion and the Abel-flux gate

## 1. Purpose and verdict

Put

\[
 \mathscr C=(\mathbf1\oplus\mathcal R)^\perp,
 \qquad
 B=A-\frac12
 \quad\hbox{on }\mathscr C.
 \tag{1}
\]

A subthreshold state of \(A\) with eigenvalue
\(\frac12-\kappa^2\) is exactly a negative state

\[
 (B+\kappa^2)q=0.
 \tag{2}
\]

This note develops three equivalent threshold coordinates for (2):
localized Birman--Schwinger, central/tail Feshbach, and boundary
Dirichlet-to-Neumann admittance.  It then compares their
\(\kappa\downarrow0\) expansion with the signed Abel flux of 106.127.

The conclusions are exact.

1. Before anti-shorting, the resolvent has the pole
   \(\kappa^{-2}P_{\mathcal R}\).  Complete radical anti-shorting removes
   that pole exactly.  Centering removes the constant state and, more
   importantly, makes the PNT-continuum plus the first Gamma component
   cancel to \(\frac12I\).  It does not remove a possible essential
   threshold singularity on \(\mathscr C\).
2. Every exact Feshbach self-energy is an operator-valued Herglotz
   function.  Below the tail spectrum it is monotone in the spectral
   parameter.  The localized Birman--Schwinger eigenvalues are likewise
   monotone as \(\kappa^2\) increases.
3. On every fixed finite-dimensional smooth boundary block, and in the
   two-scale regime in which the boundary correction is
   \(o(\kappa^2)\), the first renormalized resolvent coefficient is exactly

   \[
    Q_R\mathcal B_{\sigma,R}Q_R,
    \tag{3}
   \]

   whose incoming prime component is the Abel flux
   \(\mathcal P_D\) of 106.127.  It is not the Abel term alone: outgoing
   PNT, Gamma and theta endpoints remain coupled.
4. That Born expansion is unavailable on a hypothetical bound-state
   profile, where the signed correction is naturally of order
   \(\kappa^2\).  On the moving complete-radical complement it is only
   strongly small, not norm-small.
5. Herglotz monotonicity fixes the imaginary part and the direction of
   spectral motion.  It does not fix the real threshold subtraction
   constant.  Positivity of that finite part is exactly signed boundary
   passivity, hence equivalent to the physical surplus.

Thus the threshold resolvent does identify the 106.127 Abel observable as
the first renormalized coefficient, but it does not assign its sign.

## 2. Semantic audit

The following earlier constructions were checked.

* Phase 64 introduces a Schrödinger Birman--Schwinger model and already
  notes that the sharp top-eigenvalue bound is the missing sign.
* 106.44 separates the exact PNT continuum \(\frac12I\) from the signed
  arithmetic resonance.
* 106.47 proves the essential floor and local compactness.
* 106.58 constructs the exact graph-Fredholm Evans determinant and the
  compatible nonlocal Cauchy pair.
* 106.59 constructs the faithful localized Birman--Schwinger operator for
  every fixed energy below \(1/2\).  Its norm bound is term-for-term the
  original floor.
* 106.70 separates weighted form synthesis from compact-open synthesis.
* 106.100 shows that the relative heat exponent detects the same bottom.
* 106.123 and 106.126 isolate threshold spatial escape and show that local
  second-log regularity plus mean periodicity do not give central
  observability.
* 106.127 computes the theta boundary scale, the ambient Mosco limit and
  the exact incoming Abel flux.

The new calculation is the threshold Laurent/Feshbach expansion after
complete anti-shorting and the identification of its first finite
coefficient with the full signed operator containing the 106.127 flux.
It is not another Birman--Schwinger norm criterion.  The genuinely new
input is the exact theta-boundary scale of 106.127 and the fact that, at
that scale, the first resolvent subtraction coefficient is the literal
joint Abel--Gamma--outgoing-PNT--theta form.  The calculation also proves
that the spatial limit and the threshold-energy limit do not commute on a
putative bound-state profile.

## 3. The exact pole removed by anti-shorting

Work first in the even space before removing constants and the radical.
Let

\[
 P_0=P_{\mathbf1},
 \qquad
 P_{\mathcal R}=P_{\mathcal R},
 \qquad
 Q=I-P_0-P_{\mathcal R}.
 \tag{4}
\]

The strong identities are

\[
 A\mathbf1=0,
 \qquad
 Ar=\frac12r\quad(r\in\mathcal R).
 \tag{5}
\]

Hence \(P_0,P_{\mathcal R},Q\) reduce \(B=A-\frac12\).  For
\(\kappa>0\) away from a pole of the reduced resolvent,

\[
 \boxed{
 (B+\kappa^2)^{-1}
 =
 \frac1{\kappa^2-\frac12}P_0
 +\frac1{\kappa^2}P_{\mathcal R}
 +Q(B_Q+\kappa^2)^{-1}Q.}
 \tag{6}
\]

where \(B_Q=QBQ|_{\operatorname {Ran}Q}\).

Equation (6) separates two different operations.

* Centering removes the constant block.  Its coefficient is regular at
  \(\kappa=0\); the constant is not the threshold pole.
* Radical anti-shorting removes exactly
  \(\kappa^{-2}P_{\mathcal R}\).

No argument in (6) removes a possible threshold singularity of the last
term.  Such a singularity may be continuous rather than a pole and is
precisely what a spatially escaping Weyl sequence would create.

On the centered even sector, 106.127 proves the exact operator
cancellation

\[
 L_0+L_{\Gamma,0}=\frac12I.
 \tag{7}
\]

Therefore, after anti-shorting,

\[
 \boxed{
 B_Q=Q\mathcal B_\sigma Q,
 \qquad
 d\sigma(u)
 =e^{-u/2}d\{\psi(e^u)-e^u\}
 +\frac{e^{-5u/2}}{1-e^{-2u}}\,du.}
 \tag{8}
\]

This is the second cancellation: the order-one continuum threshold is
subtracted before any resolvent estimate.  The operator left in (8) is
signed and still has a threshold at zero.

## 4. Localized Birman--Schwinger at energy \(-\kappa^2\)

Let \(V\ge0\) be a compactly supported boost on \(\mathscr C\), as in
106.59, chosen so that

\[
 H_\kappa:=B_Q+V+\kappa^2>0.
 \tag{9}
\]

For every fixed \(\kappa>0\), such a boost exists after choosing its
support and size using the tail floor at
\(\frac12-\kappa^2\).  Define

\[
 \mathcal K_\kappa
 =H_\kappa^{-1/2}VH_\kappa^{-1/2}.
 \tag{10}
\]

Then

\[
 \boxed{
 B_Q+\kappa^2
 =H_\kappa^{1/2}(I-\mathcal K_\kappa)H_\kappa^{1/2}.}
 \tag{11}
\]

Consequently,

\[
 -\kappa^2\in\sigma_{\rm p}(B_Q)
 \quad\Longleftrightarrow\quad
 1\in\sigma_{\rm p}(\mathcal K_\kappa),
 \tag{12}
\]

with multiplicities.

The nonzero spectrum of (10) is the same as that of

\[
 \widetilde{\mathcal K}_\kappa
 =V^{1/2}(B_Q+V+\kappa^2)^{-1}V^{1/2}.
 \tag{13}
\]

Whenever one fixed \(V\) makes \(B_Q+V\ge0\), functional calculus gives

\[
 \boxed{
 \frac{d}{d(\kappa^2)}
 \widetilde{\mathcal K}_\kappa
 =
 -V^{1/2}(B_Q+V+\kappa^2)^{-2}V^{1/2}
 \le0.}
 \tag{14}
\]

This monotonicity is automatic.  It says that a Birman--Schwinger level
can cross \(1\) only in one direction as the energy is lowered.

It does not give

\[
 \widetilde{\mathcal K}_{0+}\le I.
 \tag{15}
\]

By (11), (15) is equivalent to \(B_Q\ge0\), provided the threshold limit
is defined.  Moreover, the boost supplied by the fixed-energy theorem can
depend on \(\kappa\).  Producing one threshold-admissible \(V\) is itself a
uniform spatial-observability statement; it cannot be inferred from the
fixed-gap construction.

## 5. Feshbach and the operator-valued Herglotz function

Let \(P\) be any finite-rank central heat-core projection in
\(\mathscr C\), put \(\bar P=I-P\), and set

\[
 T=\bar P B_Q\bar P,
 \qquad
 C=\bar P B_QP.
 \tag{16}
\]

For \(z\notin\sigma(T)\), define the self-energy

\[
 \Sigma_P(z)
 =C^*(T-z)^{-1}C
 \tag{17}
\]

and the Feshbach operator

\[
 \mathcal F_P(z)
 =P(B_Q-z)P-\Sigma_P(z).
 \tag{18}
\]

The usual Schur identity gives

\[
 z\in\sigma_{\rm p}(B_Q)
 \quad\Longleftrightarrow\quad
 0\in\sigma_{\rm p}(\mathcal F_P(z)),
 \tag{19}
\]

whenever \(T-z\) is invertible.

### Theorem 1 — Automatic Herglotz monotonicity

The self-energy \(\Sigma_P\) is operator Herglotz:

\[
 \boxed{
 \operatorname {Im}\Sigma_P(z)
 =(\operatorname {Im}z)\,
 C^*(T-\overline z)^{-1}(T-z)^{-1}C
 \ge0
 \quad(\operatorname {Im}z>0).}
 \tag{20}
\]

On a real interval below \(\sigma(T)\),

\[
 \boxed{
 \Sigma_P'(z)=C^*(T-z)^{-2}C\ge0,
 \qquad
 \mathcal F_P'(z)=-P-\Sigma_P'(z)<0.}
 \tag{21}
\]

Equivalently,

\[
 \frac{d}{d(\kappa^2)}
 \mathcal F_P(-\kappa^2)
 =P+\Sigma_P'(-\kappa^2)>0.
 \tag{22}
\]

#### Proof

The resolvent identity gives

\[
 (T-z)^{-1}-(T-\overline z)^{-1}
 =(z-\overline z)
 (T-\overline z)^{-1}(T-z)^{-1}.
 \tag{23}
\]

Sandwich by \(C^*,C\) to obtain (20).  Differentiation of the resolvent
on a real resolvent interval gives (21), and the chain rule gives
(22). \(\square\)

Theorem 1 is independent of the von Mangoldt signs because it is a
general consequence of self-adjointness.  It controls spectral motion,
not the value of \(\mathcal F_P(0)\).

## 6. The threshold spectral measure and what anti-shorting does not remove

If \(T\ge0\), the self-energy has the Stieltjes representation

\[
 \Sigma_P(-\kappa^2)
 =\int_{[0,\infty)}
 \frac{d\Omega_P(t)}{t+\kappa^2},
 \qquad
 d\Omega_P(t)=C^*\,dE_T(t)\,C\ge0.
 \tag{24}
\]

Its atomic threshold singularity is

\[
 \frac1{\kappa^2}C^*E_T(\{0\})C.
 \tag{25}
\]

Complete radical anti-shorting removes the atom generated by the exact
global threshold eigenspace.  It does not imply

\[
 E_T(\{0\})=0
 \tag{26}
\]

for a spatially cut tail block: cutoff and radical projection do not
commute.  Nor does it control a non-atomic divergence of (24) caused by
spectral mass accumulating at zero.

Thus there are three threshold phenomena which must not be conflated:

1. the exact global radical pole, removed in (6);
2. a cutoff-induced tail zero mode, measured by (25);
3. continuous threshold spectral mass, which can diverge without a
   pole.

Only the first is canceled algebraically.

## 7. Boundary admittance and its exact two-scale expansion

Use the theta boundary realization of 106.127.  Before compression, put

\[
 C_R=L_R^D-\frac12I.
 \tag{27}
\]

The Mosco theorem gives \(C_R\to0\) in strong resolvent sense, but not in
operator norm.  On every fixed finite-dimensional block of smooth
boundary profiles, polarization of the explicit calculation in 106.127
gives convergence of the compressed matrix elements
\(\langle f,C_Rg\rangle\to0\).  It does not by itself give
\(\|C_Rg\|\to0\).  After transporting the radical complement,

\[
 C_R^{\rm phys}
 =Q_R\mathcal B_{\sigma,R}Q_R
 \quad\hbox{on }\operatorname {Ran}Q_R.
 \tag{28}
\]

For a parameter satisfying
\(\kappa^2>-\inf\sigma(C_R)\), first define the ambient boundary
admittance

\[
 \mathcal Y_R^{\rm amb}(\kappa)
 =(C_R+\kappa^2)^{-1}.
 \tag{29}
\]

The following algebraic identity is exact on the operator domain:

\[
 \boxed{
 \mathcal Y_R^{\rm amb}(\kappa)
 =\frac1{\kappa^2}I
 -\frac1{\kappa^4}C_R
 +\frac1{\kappa^4}
 C_R\mathcal Y_R^{\rm amb}(\kappa)C_R.}
 \tag{30}
\]

Let \(E\) be a fixed finite-dimensional smooth ambient boundary block.
Assume

\[
 \inf\sigma(C_R)\ge-\varepsilon_R,
 \qquad
 \kappa_R^2\ge2\varepsilon_R,
 \qquad
 \eta_R:=\|C_RE\|=o(\kappa_R^2).
 \tag{31}
\]

Then \(\|\mathcal Y_R^{\rm amb}(\kappa_R)\|\le2\kappa_R^{-2}\), and
(30) gives,
uniformly for \(g\in E\),

\[
 \boxed{
 \begin{aligned}
 \langle g,\mathcal Y_R^{\rm amb}(\kappa_R)g\rangle
 ={}&\kappa_R^{-2}\|g\|^2
 -\kappa_R^{-4}
   \langle g,C_Rg\rangle\\
 &+O\!\left(
   \kappa_R^{-6}\|C_Rg\|^2
 \right).
 \end{aligned}}
 \tag{32}
\]

This is the rigorous ambient two-parameter threshold expansion.  The
condition \(\eta_R=o(\kappa_R^2)\) is a graph-norm hypothesis, stronger
than the fixed-profile form convergence proved by 106.127.  If a direct
graph estimate gives \(\eta_R\to0\), a cofinal
\(\kappa_R\downarrow0\) satisfying (31) can then be selected.  Mosco
convergence alone supplies no such choice, even before passing to the
moving spaces \(\operatorname {Ran}Q_R\).

For the physical admittance

\[
 \mathcal Y_R^{\rm phys}(\kappa)
 =(C_R^{\rm phys}+\kappa^2)^{-1}
 \tag{32a}
\]

the same algebra and remainder bound hold on a family
\(E_R\subset\operatorname {Ran}Q_R\) only under the additional quantitative
hypothesis

\[
 \|C_R^{\rm phys}E_R\|=o(\kappa_R^2).
 \tag{32b}
\]

Condition (32b) is not a consequence of ambient Mosco convergence,
because \(Q_R\) moves with \(R\).  It is exactly where weighted
boundary synthesis/observability enters.

## 8. Identification of the renormalized term with the Abel flux

For an ambient fixed smooth profile, 106.127 gives the same formula below
without the exterior \(Q_R\)'s.  For a physical boundary profile
\(g\in\operatorname {Ran}Q_R\), it gives

\[
 \boxed{
 \begin{aligned}
 \langle g,C_R^{\rm phys}g\rangle
 ={}&
 \mathcal P_D(g)
 +\mathfrak b_{\Gamma,*}(g)\\
 &+\mathcal P_{\rm out}(g)
 +\mathcal T_{\theta}(g),
 \end{aligned}}
 \tag{33}
\]

where

\[
 \begin{aligned}
 \mathcal P_D(g)
 =-2\operatorname {Re}\int_{x>y}
 &D(e^{x-y})e^{(x-y)/2}
 \overline{K(x)g(x)}\\
 &\times\{(Kg)'(y)+\tfrac12K(y)g(y)\}\,dy\,dx,
 \end{aligned}
 \tag{34}
\]

and

\[
 D(T)=\frac{\psi(T)-T+1}{T}.
 \tag{35}
\]

Thus the first nontrivial coefficient in (32) is exactly the complete
signed boundary form whose incoming component is the normalized Abel
flux.  In particular,

\[
 \boxed{
 -\kappa_R^4
 \left[
 \langle g,\mathcal Y_R^{\rm phys}(\kappa_R)g\rangle
 -\kappa_R^{-2}\|g\|^2
 \right]
 =
 \langle g,C_R^{\rm phys}g\rangle+o_E(1)}
 \tag{36}
\]

whenever (32b) holds.  Indeed, after multiplication by \(\kappa_R^4\),
the remainder is at most
\(2\kappa_R^{-2}\|C_R^{\rm phys}g\|^2=o(1)\).

Equation (36) answers the identification question precisely:
the renormalized term is not a new scalar.  It is the already isolated
joint Abel--Gamma--outgoing-PNT flux.

## 9. Why the expansion does not cover a bound-state scale

If (2) holds on a boundary profile, then

\[
 C_R^{\rm phys}g_R
 \simeq-\kappa_R^2g_R.
 \tag{37}
\]

Hence

\[
 \|C_R^{\rm phys}g_R\|\asymp\kappa_R^2\|g_R\|,
 \tag{38}
\]

which is exactly the scale excluded by the perturbative hypothesis
\(\eta_R=o(\kappa_R^2)\).  The geometric series is not merely
technically inconvenient there; its denominator is approaching a pole.

An exact renormalized admittance is

\[
 \mathcal Z_R(\kappa)
 :=\kappa^4
 \left\{\kappa^{-2}I-\mathcal Y_R^{\rm phys}(\kappa)\right\}.
 \tag{39}
\]

Resolvent algebra gives

\[
 \boxed{
 \mathcal Z_R(\kappa)
 =C_R^{\rm phys}
 -C_R^{\rm phys}\mathcal Y_R^{\rm phys}(\kappa)C_R^{\rm phys}
 =\kappa^2 C_R^{\rm phys}
  (C_R^{\rm phys}+\kappa^2)^{-1}.}
 \tag{40}
\]

For fixed positive spectral value \(t\), the multiplier
\(\kappa^2t/(t+\kappa^2)\) tends to zero, not to \(t\).  It approximates
\(t\) only when \(|t|=o(\kappa^2)\).  Therefore one cannot take
\(\kappa\downarrow0\) first and declare the finite part to be (33).
The order of the spatial and spectral limits is force-bearing.

## 10. Automatic Herglotz structure versus physical passivity

The following properties are automatic:

* \(\Sigma_P(z)\) and every compressed resolvent sandwich are Herglotz;
* the imaginary part in the upper half-plane is nonnegative;
* on a real resolvent interval, the self-energy increases with \(z\);
* the positive Birman--Schwinger levels decrease with \(\kappa^2\).

None of them fixes the real threshold finite part.  The scalar family

\[
 m_a(z)=a+\frac1{t-z},
 \qquad t>0,\quad a\in\mathbb R,
 \tag{41}
\]

is Herglotz for every real \(a\).  Its subtraction constant can have
either sign.  Equation (41) is the minimal falsifier for an argument which
tries to infer boundary passivity from Herglotz monotonicity alone.

In the physical problem, the free real constant is replaced by the
joint form (33).  The missing statement is

\[
 \boxed{
 \langle g,C_R^{\rm phys}g\rangle\ge0
 \quad\hbox{on the transported physical boundary range,}}
 \tag{42}
\]

uniformly in the threshold limit, or the corresponding no-pole statement
for \(\mathcal F_P(-\kappa^2)\).

But (42), expanded by (33), is precisely signed Abel passivity with Gamma,
outgoing PNT and theta endpoints kept together.  Globally it is

\[
 B_Q\ge0,
 \tag{43}
\]

the physical surplus.  Herglotz theory supplies its analytic direction
but not its real sign.

## 11. Result

The threshold operator has one algebraically removable singularity:

\[
 \boxed{\kappa^{-2}P_{\mathcal R}.}
 \tag{44}
\]

Complete anti-shorting removes it.  Centering and the exact continuum
cancellation then expose the signed source \(\mathcal B_\sigma\).  On
fixed smooth boundary blocks, the first two-scale resolvent correction is
exactly the 106.127 Abel--Gamma--PNT flux.  On actual moving physical
profiles, that correction is of the same scale as the spectral parameter,
so no perturbative Laurent truncation is valid.

The automatic Herglotz structure proves monotonicity and gives a faithful
Evans/Birman--Schwinger coordinate for any subthreshold pole.  The sole
nonautomatic input is the sign of the renormalized real boundary form.
That sign is the physical-surplus theorem itself.
