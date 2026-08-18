# D.262 — Exact Gamma insertion into the centered Green gate

## Verdict

The paired Blaschke-delay expansion of D.249 can be inserted into the
archimedean old--born cross of D.261 without separating a divergent
constant.  The result is an exact support-commutator expansion.  It does
not, however, produce the missing Hilbert contraction: the completed
archimedean score is a signed multiplier, and its sign changes on the
real frequency axis.

Consequently the local Blaschke colligations do not pay the sharp Douglas
budget one by one.  The only admissible remaining object is the *joint*
support-compressed Green column consisting of the centered Chebyshev
measure and the paired archimedean delay measure.  Any proof which takes
absolute values or assigns a separate positive budget to these two pieces
loses the exact cross required by D.214.

## 1. The exact archimedean score

In the Fourier normalization of D.137 and D.240 put

\[
 R_\Gamma(\tau)
 =\mathrm{Re}\,\psi(5/4+i\tau/2)-\psi(5/4),
 \qquad D_a(\tau)={2a\over \tau^2+a^2}.
\]

D.249 proves, locally uniformly in \(\tau\),

\[
 R_\Gamma(\tau)
 =\sum_{j\ge0}\bigl(D_{a_j}(0)-D_{a_j}(\tau)\bigr),
 \qquad a_j=2j+5/2.                                  \tag{1.1}
\]

With

\[
 \beta=\log\pi-\psi(5/4),
\]

the archimedean part of \(Q_T=-B_{{\rm nuc},T}\) has multiplier

\[
 \boxed{
 q_\infty(\tau)
 =R_\Gamma(\tau)-\beta-D_{1/2}(\tau)
 =-m_\infty(\tau).
 }                                                     \tag{1.2}
\]

Equation (1.2) is the sign convention of D.137(2.6)--(2.10) and
D.240(3.2)--(3.4): Gamma differences belong to the positive reference
column, whereas the scalar and resolvent channels belong to the load
column.

## 2. Support-compressed insertion

Let \(\mathcal F\) be the Fourier transform on the zero-extended line and
write

\[
 \mathscr Q_\infty
 :=\mathcal F^{-1}M_{q_\infty}\mathcal F .           \tag{2.1}
\]

On the common compact smooth primitive core, the archimedean remainder in
D.261 is therefore

\[
 \boxed{
 q_{N,\infty}
 =R_0^{\dagger/2}P_O\Pi_T\mathscr Q_\infty
   \Pi_TP_ES_E^{\dagger/2}.
 }                                                     \tag{2.2}
\]

Here the symbols \(R_0,S_E,P_O,P_E,\Pi_T\) have exactly the normalized
old/born meaning of D.170--D.175.  Formula (2.2) includes the finite-rank
cross created by Tate shorting; in particular one must not discard the
scalar \(-\beta I\) before applying \(\Pi_T\).

For \(J<\infty\), define the paired partial multiplier

\[
 q_{\infty,J}(\tau)
 :=-\beta-D_{1/2}(\tau)
   +\sum_{j=0}^{J}\bigl(D_{a_j}(0)-D_{a_j}(\tau)\bigr). \tag{2.3}
\]

Local uniform convergence in (1.1), followed by convergence on the closed
Gamma form core, gives

\[
 q_{N,\infty}
 =\lim_{J\to\infty}
 R_0^{\dagger/2}P_O\Pi_T
 \mathcal F^{-1}M_{q_{\infty,J}}\mathcal F
 \Pi_TP_ES_E^{\dagger/2}.                            \tag{2.4}
\]

Only the *paired differences* in (2.3) have a limit.  The two series
formed from \(D_{a_j}(0)\) and \(D_{a_j}(\tau)\) separately diverge and
are not operators available to a Douglas factorization.

## 3. The local network cannot be the missing Hilbert contraction

The obstruction is a sign theorem, not numerical evidence.  At the
origin,

\[
 m_\infty(0)=\log\pi-\psi(1/4)
 =\log\pi+\gamma+{\pi\over2}+3\log2>0.              \tag{3.1}
\]

On the other hand the classical digamma asymptotic, uniformly in every
closed angular sector avoiding the negative real axis, gives

\[
 \mathrm{Re}\,\psi(1/4+i\tau/2)
 =\log(|\tau|/2)+O(\tau^{-2}).                       \tag{3.2}
\]

Hence

\[
 m_\infty(\tau)
 =\log(2\pi/|\tau|)+O(\tau^{-2})\longrightarrow-\infty. \tag{3.3}
\]

Thus both \(m_\infty\) and \(q_\infty=-m_\infty\) change sign.  A
boundary multiplier of the form \(V^*V\), or the defect of a Hilbert
contraction with a fixed orientation, is positive semidefinite.  It cannot
equal either signed multiplier on the uncut Fourier core.  Orthogonal
support compression and a finite-rank Tate short do not convert the
signed local identity into a source-defined positive defect identity;
asserting that they do is precisely the global inequality under study.

This proves that the conservative interpretation of each individual
Blaschke delay in D.249 is a *Pontryagin/Krein bookkeeping identity* after
the renormalized signed sum.  It is not the missing Douglas contraction.

## 4. Exact joint Green column

Combine (2.2) with D.261(1.4).  Define, as a closed-form integral,

\[
 \mathfrak q_N
 :=q_{N,\infty}
   -\int_{[1,N]}\mathcal K_N(x)\,dA(x).              \tag{4.1}
\]

Then \(\mathfrak q_N=q_N\), and the complete unresolved residual is

\[
 \boxed{
 \mathscr R_N
 :=\mathcal M_N-mathfrak q_N^*D_N^\dagger\mathfrak q_N.
 }                                                     \tag{4.2}
\]

Equivalently, for \(\varepsilon>0\),

\[
 \mathscr R_{N,\varepsilon}
 :=\mathcal M_N-mathfrak q_N^*(D_N+\varepsilon I)^{-1}
   \mathfrak q_N,                                    \tag{4.3}
\]

and monotone convergence gives

\[
 \mathscr R_N=\inf_{\varepsilon>0}
 \mathscr R_{N,\varepsilon}                         \tag{4.4}
\]

in the extended quadratic-form order.  Therefore a uniform proof of
\(\mathscr R_{N,\varepsilon}\ge0\) for every \(\varepsilon>0\) gives
both the range condition and the sharp constant-one inequality in the
limit.

The reduction is strict in the sense of strategy: D.249 has now been
fully inserted and the possibility of paying its channels independently
has been eliminated.  What remains is to construct a joint source map
\(\mathscr Z_{N,\varepsilon}\), before taking a pseudoinverse, such that

\[
 \mathscr R_{N,\varepsilon}
 =\mathscr Z_{N,\varepsilon}^*
  \mathscr Z_{N,\varepsilon}.                        \tag{4.5}
\]

The source of \(\mathscr Z_{N,\varepsilon}\) must see simultaneously
the paired oscillator measure in (2.3), the centered measure
\(d\Psi-dx\), support compression, and the two Tate jets.

## 5. Classification

* Gamma score identity (1.2): **PROVED**.
* Support-compressed formula (2.2)--(2.4): **PROVED FROM D.137,
  D.170, D.175 AND D.249**.
* Sign change (3.1)--(3.3): **PROVED**.
* Separate local Hilbert-defect route: **IMPOSSIBLE FOR THE PRECISE SIGN
  REASON IN SECTION 3**.
* Joint regularized residual (4.2)--(4.4): **PROVED IDENTITY**.
* Joint source square (4.5): **OPEN; EQUIVALENT TO THE SHARP CELL GATE**.
* Row D: **OPEN**.

## Result C

The paired Gamma network cannot control the D.190 commutator by a
projection/defect mechanism after its renormalized signed assembly: its
exact multiplier changes sign.  The next structurally distinct candidate
is a joint adelic Fourier--Poisson factorization of the regularized
residual (4.3), retaining the arithmetic--Gamma cross.
