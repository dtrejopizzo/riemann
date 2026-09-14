# P121 -- causal Mobius observability on the divisor orbit

## 1. One-sentence mechanism

Lift a hypothetical first-loss state to its finite one-sided multiplicative
translation orbit, express the complete Gamma--Euler incoming history as a
unitriangular system on the divisor poset, and use Mobius elimination plus
the quarter-shift Gamma moment uniqueness to force the state to vanish.

This is a proposed mechanism, not a proved closure theorem.

## 2. Exact arithmetic algebra fixed before row (d)

Let `I_T=(-T,T)` and extend functions by zero.  For `a>=0` put

\[
 (S_a^+F)(t)=\widetilde F(t+a),\qquad
 (S_a^-F)(t)=\widetilde F(t-a).
\]

Within either orientation,

\[
 S_a^\pm S_b^\pm=S_{a+b}^\pm .                         \tag{2.1}
\]

For an integer `m>=1`, write `U_m^\pm=S_{\log m}^\pm`.  Then

\[
 U_m^\pm U_n^\pm=U_{mn}^\pm,\qquad
 U_m^\pm=0\quad(\log m\ge 2T).                       \tag{2.2}
\]

Thus each oriented translation algebra factors through the finite monoid

\[
 \mathcal M_T=\{m\in\mathbb N:m<e^{2T}\}\cup\{0\},    \tag{2.3}
\]

where products outside the cutoff equal zero.  Ordering the nonzero nodes by
size makes every nontrivial multiplication strictly triangular.  The zeta
incidence operator

\[
 (Z_Tb)(m)=\sum_{d\mid m}b(d)                         \tag{2.4}
\]

is unitriangular, with inverse

\[
 (Z_T^{-1}c)(m)=\sum_{d\mid m}\mu(d)c(m/d).           \tag{2.5}
\]

Equations (2.1)--(2.5) are algebraic and do not use positivity, zeros of
zeta, or row (d).

Define the degree derivation by
`\partial U_n=-(\log n)U_n`.  The logarithmic connection, rather than the
positive graph Gram, carries the physical contact:

\[
 Z_T\,\partial\, Z_T^{-1}
   =\sum_{p^j<e^{2T}}(\log p)U_{p^j}                 \tag{2.6}
\]

in the corresponding finite Dirichlet algebra.  Central metric conjugation
then supplies the fixed coefficient `(log p)p^{-j/2}`.  This is the reason
to use the divisor orbit causally and not as the positive graph norm ruled
out in D.103.

## 3. The Gamma history variables

Put `A_k=k+1/4`.  The already established causal Gamma cells solve

\[
 \frac12 y_k'+A_ky_k=\sqrt{A_k}F.                    \tag{3.1}
\]

For the positive orientation let

\[
 y_k^+(t)=2\sqrt{A_k}\int_{-T}^{t}
        e^{-2A_k(t-s)}F(s)\,ds,                       \tag{3.2}
\]

and define the reflected negative orientation analogously.  The exact
shift commutator is a free boundary response:

\[
 (S_a^+y_k^+-C_k^+S_a^+F)(t)
 =e^{-2A_k(t+T)}y_k^+(-T+a)                           \tag{3.3}
\]

on the common causal cell.  Consequently all failure of Gamma to commute
with the finite divisor orbit is encoded by the samples

\[
 b_{k,m}^+=y_k^+(-T+\log m),\qquad
 b_{k,m}^-=y_k^-(T-\log m),qquad m\in\mathcal M_T.  \tag{3.4}
\]

No norm or sign is assigned to these samples.

## 4. The decisive new theorem

The phase has one theorem to prove.

### Causal Mobius Observability Theorem (CMO)

Let `F` be a parity-fixed first-loss state:

\[
 F\in\mathcal P_T,\qquad
 P_TA_TF=0.                                           \tag{4.1}
\]

Put `h=\mathcal Z_{T,+}F`, with the already proved finite causal zeta
operator and its nilpotent Mobius inverse.  Lift the two unsupertraced
versions of (4.1) to every node of `\mathcal M_T` and retain the two Tate
corrector coordinates.  The history vector `\mathbf H_k(F)` contains the
root amplitude `h`, its oriented divisor translates, and both families of
Gamma boundary samples (3.4).  After the known affine Gamma head has been
removed, the resulting boundary equations have the form

\[
 \mathbb Z_T\,\mathbf H_k(F)=0\qquad(k\ge0),          \tag{4.2}
\]

where `\mathbb Z_T` is independent of `k` and, after ordering by divisor
depth and placing the two Tate coordinates first, it is block
unitriangular with identity diagonal.  In particular its root diagonal is
the identity on the physical local amplitude `h`; it is not a scalar
obtained by evaluating the Weil form.

Therefore

\[
 h=0,\qquad b_{k,m}^+=b_{k,m}^-=0
 \quad(k\ge0,\ m\in\mathcal M_T).                    \tag{4.3}
\]

The phrase "have the form" in (4.2) is the entire mathematical burden.  It
must be obtained by an exact source calculation.  Defining
`\mathbb Z_T` so that (4.2) holds is inadmissible.

## 5. Why CMO would close the first-loss problem

The root conclusion in (4.3) is exactly the annular vanishing of the local
physical co-Poisson observation in v94 (436)--(441).  Its finite nilpotent
inverse gives

\[
 F=\mathcal Z_{T,+}^{-1}h=0,                         \tag{5.1}
\]

contradicting (4.1).  No global exterior-tail estimate is inserted here.
The remaining boundary conclusions in (4.3) are consistency outputs, not a
substitute for the root implication.

The standard first-loss reduction would consequently give

\[
 -B_{\rm nuc,T}\succeq0\quad\hbox{on }\mathcal P_T
 \quad\hbox{for every }T>0.                           \tag{5.2}
\]

The cofinal limit already established for the row-(d) setup would then
yield row (d).  Section 5 is conditional on CMO; it is not recorded as a
proof.

## 6. Kill conditions

CMO dies, without adjustment, if the exact lifted source equations have
any of the following properties:

1. an incoming-history coefficient joins nodes not related by divisibility;
2. a diagonal block vanishes or depends on the unknown state;
3. the two Tate corrections create a nontriangular feedback into deeper
   divisor levels;
4. the negative orientation requires division by a zeta boundary value;
5. the lifted equations determine only the reflected sum of the two
   histories, reproducing the old Wiener--Hopf ambiguity;
6. the root local amplitude is absent from the identity diagonal, so that
   elimination kills only auxiliary histories and leaves equation (445)
   unchanged.

These are symbolic/source-level failures.  No endpoint eigenvalue or
floating-point positivity calculation is relevant.

## 7. Calibration against comparison objects

* **Davenport--Heilbronn.**  The logarithmic contact is not the positive
  rank-one Euler connection in (2.6); its signed local coefficients should
  fail the physical unitriangular source law before CMO is invoked.
* **Shifted rank-two pair.**  A local contact has two independent primitive
  coordinates.  The scalar identity diagonal in (4.2) is replaced by a
  rank-two block and the required observability is not automatic.
* **Curves over finite fields.**  Place-indexed rank one and Frobenius
  composition are present.  The mechanism should reduce to a finite
  divisor-orbit version of the known Weil sign.
* **Dedekind zeta functions.**  Place-indexed rank one is present.  A valid
  CMO theorem in that setting would prove GRH for Dedekind zeta functions;
  this consequence is explicit and is not being hidden.

## 8. Immediate task

Derive the complete two-orientation history equation for the smallest
symbolic divisor orbit containing

\[
 1,\ 2,\ 3,\ 4,\ 6,\ 12,                              \tag{8.1}
\]

without evaluating a Weil Gram and without assigning a sign.  The purpose
of (8.1) is algebraic: it contains a prime-power chain and the first
commuting prime diamond.  The output is the literal coefficient matrix of
the history variables (3.4), including both Tate columns.  Its support and
diagonal decide whether CMO is a theorem candidate or another false lift.
