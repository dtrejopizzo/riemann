# 106.141 — Metric-preserving representation rigidity and the surviving class

## 1. Purpose

The recent transfer, connection, and Gamma-splitting calculations prove a
rigidity statement, but only after their scopes are kept separate.  This note
collects that statement and records the exact logical boundary.

There are two different fixed maps:

1. the **full threshold observation** of 106.105, whose contractivity is the
   physical floor (A\geq \frac12 I);
2. the **compact Abel connection** of 106.136, whose contractivity is the
   distinct relative-amplitude inequality
   \(\mathcal C^\sharp\mathcal C\preceq\widetilde A\).

Changing an exact realization of either map cannot improve its optimal gain.
This does not identify the two gains and does not prove either unit bound.
Likewise, fixed or adaptive Gamma splitting does not create a third, weaker
sign theorem.  What survives is a source-specific, jointly signed arithmetic
estimate for the original physical form after the complete radical
anti-short.

## 2. Abstract threshold rigidity

Let \(\mathscr C\) be the completely anti-shorted Hilbert space and let
\(A\geq0\) be the injective physical generator on \(\mathscr C\).  No
positive lower spectral bound is assumed.
Let

\[
 \mathcal G=U_AA^{1/2}:\mathcal D(A^{1/2})\longrightarrow\mathscr Y
 \tag{1}
\]

be a closed source gradient, so that

\[
 \mathcal G^*\mathcal G=A.
 \tag{2}
\]

Let \(D=2^{-1/2}U_D:\mathscr C\to\mathscr Z\), where \(U_D\) is an
isometry.  Thus

\[
 D^*D=\frac12 I.
 \tag{3}
\]

The exact coefficient equation is

\[
 H\mathcal Gf=Df.
 \tag{4}
\]

### Theorem 1 — Full-threshold metric rigidity

Define on \(\overline{\operatorname {Ran}\mathcal G}\)

\[
 C_0:=2^{-1/2}U_DA^{-1/2}U_A^*.
 \tag{5}
\]

Then:

1. \(C_0\mathcal G=D\), and (4) fixes the restriction of every exact
   realization \(H\) to \(\operatorname {Ran}\mathcal G\).
2. When it is bounded, the zero extension of \(C_0\) is the minimum-norm
   bounded exact realization.  With the extended value \(+\infty\) when
   \(\inf\sigma(A)=0\),

   \[
    \inf_{\substack{H\in\mathcal B(\mathscr Y,\mathscr Z)\\
                         H\mathcal G=D}}\|H\|=\|C_0\|
    =\frac1{\sqrt{2\inf\sigma(A)}}.
    \tag{6}
   \]

3. The following assertions are equivalent:

   \[
   \boxed{
   A-\frac12I\succeq0
   \quad\Longleftrightarrow\quad
   \|C_0\|\leq1
   \quad\Longleftrightarrow\quad
   \begin{pmatrix}A&D^*\\ D&I\end{pmatrix}\succeq0.}
   \tag{7}
   \]

4. Unitary changes of source or target coordinates, isometric
   enlargements, and alternative signed kernels satisfying the same
   coefficient equation cannot lower the right side of (6).

#### Proof

Equations (1) and (5) give

\[
 C_0\mathcal Gf
 =2^{-1/2}U_DA^{-1/2}U_A^*U_AA^{1/2}f
 =Df.
 \tag{8}
\]

Therefore any \(H\) satisfying (4) agrees with \(C_0\) on the gradient
range.  If \(C_0\) is bounded, its zero extension is exact and has minimum
norm.  If \(\inf\sigma(A)=0\), spectral vectors approaching zero show that
no bounded exact \(H\) exists.  Since the two polar factors are isometries,
spectral calculus gives (6) with the stated extended convention.  The first two
conditions in (7) are equivalent by (6).  The Schur complement of the
lower-right identity in the block of (7) is

\[
 A-D^*D=A-\frac12I,
 \tag{9}
\]

which proves the last equivalence.  Unitary conjugacy preserves norms, and
an isometric enlargement cannot alter the already-fixed restriction on
\(\operatorname {Ran}\mathcal G\).  \(\square\)

Thus a positive block realization of the full threshold map is a useful
coordinate for the desired sign, but it is not positive for free.  Its
Schur complement is exactly the desired sign.

### Proposition 2 — Harmless commutators do not move the threshold

Suppose a normalized eigenvector satisfies \(Aq=\alpha q\), and let \(X\)
be symmetric on a common form domain.  Then

\[
 \langle q,i[A,X]q\rangle=0.
 \tag{10}
\]

Consequently an identity

\[
 A-\frac12I=B^*B+i[A,X]+R,
 \qquad R\succeq0,
 \tag{11}
\]

already excludes \(\alpha<\frac12\); the commutator does not provide an
independent reserve on the state that has to be excluded.

#### Proof

The two terms in the commutator matrix element are both
\(\alpha\langle q,Xq\rangle\), with opposite signs.  Taking the
\(q\)-matrix element of (11) then gives
\(\alpha-\frac12=\|Bq\|^2+\langle q,Rq\rangle\geq0\).  \(\square\)

## 3. Separate rigidity of the compact connection

Let \(B\) be one of the fixed compact connection maps

\[
 B\in\{\mathcal J,\mathcal C\},
 \qquad
 \mathcal C=T_{K'+K/2}M_{K/h},
 \tag{12}
\]

and let \(\widetilde{\mathcal G}=U_A\widetilde A^{1/2}\) be the complete
ordinary-prime--Gamma gradient of 106.136 after exact anti-shorting.

### Theorem 3 — Fixed-connection factorization rigidity

The minimum-norm factor in

\[
 B=H_B\widetilde{\mathcal G}
 \tag{13}
\]

is

\[
 H_B=B\widetilde A^{-1/2}U_A^*,
 \tag{14}
\]

and

\[
 \boxed{
 \inf_{B=H\widetilde{\mathcal G}}\|H\|^2
 =\|B\widetilde A^{-1}B^\sharp\|.}
 \tag{15}
\]

In particular,

\[
 \|H_{\mathcal C}\|\leq1
 \quad\Longleftrightarrow\quad
 \mathcal C^\sharp\mathcal C\preceq\widetilde A.
 \tag{16}
\]

Regularized common-cutoff factorizations converge in operator norm to the
fixed value in (15).  Therefore neither a different realization of the
same connection nor passage to the cofinal limit can improve this gain.

#### Proof

This is the polar-decomposition and Douglas-factorization calculation of
106.136.  Equation (13) fixes every factor on the complete gradient range;
the zero extension (14) is therefore minimal.  Multiplication gives
\(H_BH_B^\sharp=B\widetilde A^{-1}B^\sharp\), proving (15).  The Douglas
criterion gives (16).  Monotone resolvent convergence, sandwiched by the
compact map \(B\), upgrades to operator-norm convergence.  \(\square\)

Theorem 3 is **not** another proof of Theorem 1.  The map \(\mathcal C\)
is the Abel connection, not the full threshold observation \(D\).  The
linear identity controlled in 106.135 concerns

\[
 2\operatorname {Re}\langle F,\mathcal CF\rangle
 \tag{17}
\]

inside a connection-corrected KYP supply.  It does not imply the quadratic
relative-amplitude bound (16), and neither statement is an exact rewriting
of the original physical form.

## 4. Splitting rigidity

On a finite completely anti-shorted heat or hybrid row \(E\), 106.140 has
the exact decomposition

\[
 \mathfrak Q_{\rm phys}|_E=B_E+W_E,
 \qquad W_E>0.
 \tag{18}
\]

Set

\[
 \kappa_E=\max\left\{0,-\lambda_{\min}
 \bigl(W_E^{-1/2}B_EW_E^{-1/2}\bigr)\right\}.
 \tag{19}
\]

Then

\[
 \boxed{
 \kappa_E\leq1
 \quad\Longleftrightarrow\quad
 \mathfrak Q_{\rm phys}|_E\succeq0.}
 \tag{20}
\]

Hence choosing the Gamma fraction adaptively does not weaken the target.
On a form-core exhaustion, \(\sup_E\kappa_E\leq1\) is exactly completed
positivity.  Replacing (19) by separate domination of the negative spectral
part is only a stronger sufficient condition; the rational example of
106.140 disproves its validity as a general equivalence, not specifically
as a literal-Riemann inequality.

Nor does an operator-valued allocation create slack.  If
\(0\preceq X_E\preceq I\), then

\[
 \exists X_E:\ B_E+W_E^{1/2}X_EW_E^{1/2}\succeq0
 \quad\Longleftrightarrow\quad
 B_E+W_E\succeq0.
 \tag{20a}
\]

The forward implication follows by adding
\(W_E^{1/2}(I-X_E)W_E^{1/2}\succeq0\), and the reverse implication uses
\(X_E=I\).  The same pointwise argument applies to a state-dependent scalar
fraction \(\kappa(q)\in[0,1]\).  Thus scalar, state-dependent, and
operator-valued allocations all have the full reserve as their maximal
element, and their maximal gate is the original physical sign.

The fixed split of 106.139 is different.  It gives a valid stronger form
\(\mathfrak Q_{\rm suff}\leq\mathfrak Q_{\rm phys}\), but
\(\mathfrak Q_{\rm suff}\) is strictly negative on every nonconstant exact
radical before complete anti-shorting.  Its apparent failure on a fixed
four-zero vector after complete anti-shorting is presently a floating-point
diagnostic, not an interval-certified theorem.

## 5. Conditional off-line falsifier and its exact scope

### Theorem 4 — What 106.93 proves

Assume counterfactually that \(\Xi\) has an off-line zero orbit.  Then there
exists a real even \(q\) in the Riemann mean-periodic complement and in the
common form domain such that, for every finite ordinary-prime head \(X\),
the scalar source row with no old-mode or finite-radical coordinate obeys

\[
 \boxed{
 G_X-\delta_X=\mathcal A_\infty(q,q)<0,}
 \tag{21}
\]

and every proper finite restoration \(Y>X\) satisfies

\[
 \mathfrak C_X(Y)\leq G_X<\delta_X.
 \tag{22}
\]

#### Proof

The off-line interpolation theorem supplies
\(\mathcal A_\infty(q,q)<0\).  The omitted ordinary-prime tail is a sum of
nonnegative literal displacement energies.  Thus
\(\mathcal A_X=\mathcal A_\infty-\mathcal T_X<0\), while in the scalar row
the complete adaptive gain is exactly \(G_X=\mathcal T_X\).  This gives
(21), and monotonicity of the proper finite tail gives (22).  \(\square\)

The quantifiers in Theorem 4 matter.  It is conditional on an off-line
orbit and constructs one scalar bad row for all cutoffs.  It does not assert
unconditionally that such a row exists, and it does not identify every
multirow adaptive residual with that one vector.  Its valid conclusion is
that a universal strict-surplus theorem excludes the off-line orbit; it is
not a preliminary estimate insensitive to zero location.

## 6. Rigidity corollary

Within the established Hilbert metrics, none of the following operations
can move an unknown sign to a known one:

1. replacing the exact full-threshold transfer by another signed kernel
   satisfying the same coefficient equation;
2. applying unitary coordinates or isometric state-space enlargements;
3. embedding the same form in a positive block and taking its Schur
   complement;
4. adding a commutator whose diagonal matrix element vanishes on an
   eigenstate;
5. changing the exact realization of the fixed compact Abel connection;
6. taking regularized, Galerkin, or cofinal limits of that fixed
   factorization;
7. spending a fixed, state-dependent, or operator-valued fraction of the
   same Gamma reserve.

These operations remain valuable for localization, compactness, and
computation.  The rigidity claim is only that their sharp constants are
already fixed by the operator or form being represented.  It is **not** a
claim that no mathematical proof can exist, nor does it cover a genuinely
new inequality which uses additional arithmetic structure before the
Hilbert norm is closed.

## 7. The mathematically distinct surviving class

The original force-bearing form is

\[
\boxed{
\begin{aligned}
 \mathfrak Q_{\rm phys}(q)
 &:=\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
       J_{\log n}(q)
   +\int_0^\infty r_\Gamma(u)J_u(q)\,du\\
 &\hspace{2.5cm}-\int_0^\infty e^{u/2}J_u(q)\,du,
 \qquad q\in\mathscr C.
\end{aligned}}
\tag{23}
\]

What remains mathematically distinct is a **source-specific nonlocal
arithmetic comparison** proving

\[
 \mathfrak Q_{\rm phys}(q)\geq0
 \qquad(q\in\mathscr C),
 \tag{24}
\]

or a sufficient statement which genuinely implies (24).  Such an argument
must use a property of the literal placements \(\log p^k\), weights
\(\Lambda(p^k)\), Gamma density, pole, and complete mean-periodic
anti-short which is incompatible with the off-line vector in Theorem 4.
Examples of its possible mathematical form are a jointly signed
prime--Gamma correlation estimate, a source-specific projection-alignment
theorem, or a direct exclusion of subthreshold mean-periodic eigenstates.

It may use nonlinear arithmetic reasoning in its proof, but it cannot gain
the sharp constant merely by re-realizing a fixed linear map.  Once (24) is
proved, the already-established tail monotonicity and finite-selection
machinery convert the strict residual surplus into the finite bordered-minor
crossing.  The new content lies entirely in (24), not in another exact
packaging of it.

## 8. Audit status

Proved here, by synthesis of 106.93, 106.105, 106.136, 106.139, and 106.140:

* full-threshold metric-preserving representation rigidity;
* separate fixed-connection factorization rigidity;
* fixed/adaptive splitting rigidity;
* the exact conditional scope of the literal off-line anti-surplus;
* the boundary of the surviving mechanism class.

Not proved here:

\[
 \mathfrak Q_{\rm phys}\geq0\quad\text{on }\mathscr C.
\]

That is the source-specific theorem which the rigidity results localize but
do not supply.
