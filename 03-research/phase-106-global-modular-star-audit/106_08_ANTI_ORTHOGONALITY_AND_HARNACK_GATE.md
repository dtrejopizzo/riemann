# 106.08 — Anti-orthogonality and the sharp Harnack gate

## Purpose

Document 106.07 leaves an exact alternative:

\[
 |\epsilon_{0,L}|\,|\langle \phi_L,k_L\rangle|
 \quad\hbox{is small},
 \tag{1}
\]

but this does not decide whether the least eigenvalue is small or the
ground state is becoming orthogonal to the prolate model.  This note tests
the three natural ways of selecting the first branch:

1. normalization at an endpoint or at the origin;
2. positivity improvement and Harnack estimates;
3. a direct lower bound for the ground/model overlap.

The outcome is sharp.  There is an exact anti-orthogonality criterion which,
for the full ordinary-prime Weil operator, would already imply RH.  The
bilateral Paley--Wiener theorem of 106.11 subsequently proves that the same
is true for either parity block separately.  Positivity
improvement reduces that criterion to a quantitative Harnack--tightness
estimate, but qualitative positivity supplies no uniform constant.  A
two-dimensional positivity-improving countermodel has a fixed negative
ground energy, a strictly positive near-radical model, and overlap tending
to zero.  It is also the finite-dimensional normal form of the hypothetical
off-line evaluation mode from 106.07.

No assertion below assumes RH.

## 1. The exact anti-orthogonality identity

Let \(A_L\) be self-adjoint on a Hilbert space \(\mathcal H_L\), with
normalized simple ground state \(\phi_L\) and ground eigenvalue
\(\epsilon_L\).  Let \(q_L\in\operatorname{Dom}(A_L)\) be a normalized
model vector and let \(\mu_L\in\mathbb R\).  Put

\[
 \alpha_L:=|\langle\phi_L,q_L\rangle|,
 \qquad
 r_L:=\|(A_L-\mu_L)q_L\|.
 \tag{2}
\]

### Theorem 1 — Sharp residual/overlap criterion

For every \(L\),

\[
 \boxed{
 |\epsilon_L-\mu_L|\,\alpha_L\le r_L.
 }
 \tag{3}
\]

Consequently, if

\[
 \mu_L\longrightarrow0,
 \qquad
 \frac{r_L}{\alpha_L}\longrightarrow0,
 \tag{4}
\]

then \(\epsilon_L\to0\).

#### Proof

Self-adjointness and \(A_L\phi_L=\epsilon_L\phi_L\) give

\[
 (\epsilon_L-\mu_L)\langle\phi_L,q_L\rangle
 =\langle\phi_L,(A_L-\mu_L)q_L\rangle.
 \tag{5}
\]

Cauchy--Schwarz proves (3), and (4) proves the conclusion. \(\square\)

The estimate is sharp: equality holds when the residual is a scalar
multiple of \(\phi_L\).  Thus no argument using only the norm of the model
residual can remove the divisor \(\alpha_L\).

### Proposition 2 — What failure of RH gives before choosing parity

Let

\[
 QW_L=QW_L^+\oplus QW_L^-
 \tag{6a}
\]

be the decomposition under the reflection
\(Jf(u)=f(u^{-1})\), and let \(\epsilon_L^\pm\) be the bottoms of the
two restricted forms.  If RH is false, then there are a sign
\(\sigma\in\{+,-\}\), a constant \(c>0\), and \(L_0\) such that

\[
 \epsilon_L^\sigma\le -c
 \qquad (L\ge L_0).
 \tag{6b}
\]

In particular the bottom \(\epsilon_L^{\rm full}\) of the full semilocal
Weil operator satisfies the same bound.

#### Proof

If RH is false, the Weil criterion provides a smooth compactly supported
test \(f\), with no parity assertion, such that

\[
 QW(f,f)<0.
 \tag{6c}
\]

Write \(f=f_++f_-\), where \(Jf_\pm=\pm f_\pm\).  Reflection invariance of
the Weil distribution gives

\[
 QW(f,f)=QW(f_+,f_+)+QW(f_-,f_-).
 \tag{6d}
\]

Consequently one of these two compactly supported tests, denoted
\(f_\sigma\), has negative Weil value.  Put

\[
 c:=-\frac{QW(f_\sigma,f_\sigma)}
          {\|f_\sigma\|_2^2}>0.
 \tag{6e}
\]

For every support window containing the fixed support of \(f_\sigma\), the
Rayleigh principle gives

\[
 \epsilon_L^\sigma\le-c.
 \tag{6f}
\]

The full bottom is at most either parity bottom. \(\square\)

Proposition 2 by itself does **not** say that the negative test is even.
This limitation is removed in 106.11: an off-line quartet produces fixed
compactly supported negative tests in **both** parity sectors.  Proposition
2 is retained here as the elementary decomposition argument; the bilateral
result is the theorem used below.

### Corollary 3 — Full-sector or single-parity Weil closure gate

Assume the semilocal operators \(A_L\) represent the restriction of the
ordinary-prime Weil form and that their selected eigenvalue satisfies the
detection property

\[
 \neg{\rm RH}\quad\Longrightarrow\quad
 \epsilon_L\le-c\quad\hbox{for every sufficiently large \(L\)}
 \tag{D}
\]

for some \(c>0\).  If normalized vectors \(q_L\) and real numbers
\(\mu_L\to0\) satisfy (4), then RH holds.

The detection property is automatic when \(\epsilon_L\) is the bottom of
the **full** semilocal operator.  By Theorem 1 and Corollary 2 of 106.11,
it is also automatic when \(\epsilon_L\) is the bottom of either the even
or the odd ordinary-prime semilocal block.  No comparison between the two
parity bottoms is required.

#### Proof

Theorem 1 and (4) give \(\epsilon_L\to0\), contradicting (D) under failure
of RH. \(\square\)

Corollary 3 is a genuine bypass of the curvature comparison: it is enough
to prevent the ground state from escaping the near-radical branch.  It does
not, by itself, prove
\(\widehat\phi_L/\widehat k_L\to1\); that stronger identification still
requires the weighted angle/gap estimate of 106.07.

For the CCM model one naturally takes \(q_L=k_L/\|k_L\|_2\) and
\(\mu_L=0\).  The missing quantitative statement is therefore

\[
 \boxed{
 \frac{\|A_Lq_L\|}
 {|\langle\phi_L,q_L\rangle|}\longrightarrow0.
 }
 \tag{9}
\]

The numerator is the model-radical error.  The denominator is the precise
branch-selection factor.  For the ordinary-prime even sector, 106.11 proves
the detection condition (D), so (9) alone is sufficient for RH.

## 2. Endpoint normalization does not select a Hilbert direction

### Proposition 4 — Scalar normalization is angle-blind

Let \(u,v\ne0\) be vectors in a Hilbert space and let \(\ell\) be a linear
functional with \(\ell(u)\ell(v)\ne0\).  Rescale \(u\) and \(v\) so that
\(\ell(u)=\ell(v)=1\).  Their normalized overlap is unchanged:

\[
 \frac{|\langle \ell(u)^{-1}u,\ell(v)^{-1}v\rangle|}
 {\|\ell(u)^{-1}u\|\,\|\ell(v)^{-1}v\|}
 =\frac{|\langle u,v\rangle|}{\|u\|\,\|v\|}.
 \tag{10}
\]

#### Proof

Both numerator and denominator acquire the same factor
\(|\ell(u)\ell(v)|^{-1}\). \(\square\)

Thus normalizing
\(\widehat\phi_L(0)=\widehat k_L(0)\), fixing an endpoint value, or fixing
one Cauchy datum removes a scalar ambiguity but cannot prove a lower bound
for \(\alpha_L\).  This agrees with Theorem 1 of 106.07: curvature is
insensitive to affine exponential normalization, whereas branch selection
is an angular statement in the source Hilbert space.

## 3. What positivity improvement would have to prove

Even granting that both vectors can be represented in the same positive
cone, strict positivity alone is insufficient on an expanding domain.  The
following elementary bound isolates the exact additional input.

### Theorem 5 — Harnack--tightness overlap bound

Let \((X_L,\mu_L)\) be a measure space.  Let \(q_L,\phi_L\ge0\) satisfy
\(\|q_L\|_2=\|\phi_L\|_2=1\).  Suppose that on a measurable set
\(E_L\subset X_L\),

\[
 q_L\ge m_L>0,
 \qquad
 \int_{E_L}\phi_L^2\,d\mu_L\ge\tau_L>0,
 \qquad
 \|\phi_L\|_{L^\infty(E_L)}\le M_L.
 \tag{11}
\]

Then

\[
 \boxed{
 \langle\phi_L,q_L\rangle
 \ge \frac{m_L\tau_L}{M_L}.
 }
 \tag{12}
\]

Consequently, the concrete sufficient condition

\[
 \|A_Lq_L\|\,
 \frac{M_L}{m_L\tau_L}\longrightarrow0
 \tag{13}
\]

implies RH under the sector-detection hypothesis of Corollary 3.

#### Proof

On \(E_L\), nonnegativity and the \(L^\infty\) bound give

\[
 \tau_L
 \le\int_{E_L}\phi_L^2\,d\mu_L
 \le M_L\int_{E_L}\phi_L\,d\mu_L.
 \tag{14}
\]

Therefore

\[
 \langle\phi_L,q_L\rangle
 \ge m_L\int_{E_L}\phi_L\,d\mu_L
 \ge m_L\tau_L/M_L.
 \tag{15}
\]

Combine this with (9). \(\square\)

The three factors have distinct roles:

- \(m_L\) prevents the model from disappearing on the comparison region;
- \(\tau_L\) is a tightness estimate preventing ground-state mass from
  escaping that region;
- \(M_L\) is the quantitative Harnack/delocalization constant.

A positivity-improving semigroup proves \(\phi_L>0\) at each fixed \(L\).
It does not make any of \(m_L,\tau_L,M_L^{-1}\) uniform in \(L\).  In
particular, a fixed-\(L\) Harnack inequality is useful here only if its
constant is tracked and (13) is verified against the actual CCM residual.

There is a second structural caution.  For the pole-free semilocal operator,
the Gamma convolution has a conditionally negative symbol and the Euler
translations enter with positivity-preserving signs, so a Trotter argument
can produce a positivity-improving heat semigroup.  The zeta operator in the
even sector also contains the pole rank-one term.  Positivity improvement
for the pole-free part does not automatically prove that the completed
ground vector and the prolate model lie in the same positive cone.  The
estimate (12) must be established in the actual representation in which
the overlap in (9) is taken.

## 4. A sharp positivity-improving countermodel

Qualitative Perron--Frobenius information cannot prove (9), even if the
model is strictly positive and its residual tends to zero.

For \(0<\eta<1\), on \(\mathbb R^2\) with its standard positive cone, set

\[
 A_\eta=
 \begin{pmatrix}
 -1&-\eta\\
 -\eta&0
 \end{pmatrix},
 \qquad
 \widetilde q_\eta=
 \begin{pmatrix}\eta^2\\1\end{pmatrix},
 \qquad
 q_\eta=\frac{\widetilde q_\eta}{\|\widetilde q_\eta\|}.
 \tag{16}
\]

### Theorem 6 — Positive near-radical/negative-ground separation

The family (16) has all of the following properties.

1. \(A_\eta\) is self-adjoint and \(e^{-tA_\eta}\) is positivity improving
   for every \(t>0\).
2. The ground eigenvalue is simple and

   \[
    \epsilon_\eta
    =\frac{-1-\sqrt{1+4\eta^2}}2
    \longrightarrow-1.
    \tag{17}
   \]

3. A normalized ground vector is strictly positive and proportional to

   \[
    \phi_\eta=
    \begin{pmatrix}1\\t_\eta\end{pmatrix},
    \qquad
    t_\eta=
    \frac{2\eta}{\sqrt{1+4\eta^2}+1}\sim\eta.
    \tag{18}
   \]

4. The model \(q_\eta\) is strictly positive and near-radical:

   \[
    \|A_\eta q_\eta\|\sim\eta,
    \qquad
    \langle A_\eta q_\eta,q_\eta\rangle
       =-2\eta^3+O(\eta^4)\longrightarrow0.
    \tag{19}
   \]

5. Nevertheless,

   \[
    \alpha_\eta
      :=\langle\phi_\eta/\|\phi_\eta\|,q_\eta\rangle
      \sim\eta,
    \qquad
    \frac{\|A_\eta q_\eta\|}{\alpha_\eta}\longrightarrow1.
    \tag{20}
   \]

#### Proof

The matrix \(-A_\eta\) has strictly positive off-diagonal entries and is
irreducible.  Its exponential is therefore entrywise strictly positive for
every positive time, proving item 1.  The characteristic polynomial is

\[
 \lambda^2+\lambda-\eta^2,
 \tag{21}
\]

which proves (17).  Substitution proves that (18) is its positive ground
eigenvector.  Direct multiplication gives

\[
 A_\eta\widetilde q_\eta
 =\begin{pmatrix}-\eta-\eta^2\\-\eta^3\end{pmatrix}.
 \tag{22}
\]

Equations (19) follow.  Finally,

\[
 \langle(1,t_\eta),(\eta^2,1)\rangle
 =\eta^2+t_\eta\sim\eta,
 \tag{23}
\]

and the normalizing factors tend to one.  This proves (20). \(\square\)

This model passes the strongest qualitative version of the proposed
positivity argument: the semigroup is positivity improving, the ground and
model are strictly positive, the ground is simple, and the model residual
and Rayleigh value tend to zero.  Yet the ground remains at energy \(-1\).
The vanishing overlap cancels the vanishing residual exactly in (3).

It also explains what a nonuniform Harnack constant would look like.  The
ground-coordinate ratio is \(1/t_\eta\asymp\eta^{-1}\), while the model
coordinate ratio is \(\eta^{-2}\).  Fixed-parameter positivity survives,
but every uniform comparison constant diverges.

## 5. Test against a hypothetical off-line mode

The countermodel is not merely a generic matrix obstruction.  Its two
coordinates have the geometry forced by a hypothetical zero off the
critical line:

- the first coordinate is a negative evaluation mode whose energy stays
  bounded away from zero;
- the second coordinate is the prolate/radical branch;
- \(\eta\) is the coupling between them;
- the prolate residual and its overlap with the negative ground state both
  vanish at the same rate.

For the actual Weil form, 106.07 records that a hypothetical non-real zero
\(z_0=x_0+ia\) has normalized Paley--Wiener evaluation vector

\[
 \frac{K_{L,z_0}}{\|K_{L,z_0}\|_2},
 \qquad
 \|K_{L,z_0}\|_2^2=\frac{\sinh(|a|L)}{|a|},
 \tag{24}
\]

and that its overlap with the truncated full kernel tends to zero.  Thus
an off-line mode creates exactly the separation realized by (16).  Any
purported proof of a uniform lower bound for \(\alpha_L\) that uses only
positivity improvement, model radicality, or endpoint normalization would
also apply to Theorem 6 and is therefore false.

This is the required off-line falsifier.  A successful estimate must use an
ordinary-prime property which prevents the evaluation mode from becoming
the ground state.  By Corollary 3 and the bilateral detection theorem of
106.11, such an estimate is already an RH-strength exclusion theorem; it
cannot be supplied by abstract
Perron--Frobenius theory.

## 6. Relation to the curvature theorem

There are now two distinct sufficient gates.

### Gate A — RH without ground-transform identification

\[
 \boxed{
 \|A_Lq_L\|/|\langle\phi_L,q_L\rangle|\to0.
 }
 \tag{25}
\]

This forces \(\epsilon_L\to0\).  It proves RH for the full ground state and,
by 106.11, for either ordinary-prime parity ground state separately.

### Gate B — The requested curvature identification

\[
 \boxed{
 \frac{\|k_L\|_2W_{L,B}}{\inf_K|\widehat k_L|}
 \left(
  \frac{R_L-\epsilon_{0,L}}
       {\epsilon_{1,L}-\epsilon_{0,L}}
 \right)^{1/2}\to0,
 }
 \tag{26}
\]

with the projection-tail term included.  This is (25) of 106.07 and gives
\(\partial_z^2\log(\widehat\phi_L/\widehat k_L)\to0\).

Gate A is sufficient for RH but does not force the model to span the entire
ground line.  Gate B does.  Neither follows from an unscaled residual
estimate.

## 7. Binding conclusion

The branch-selection problem is not an unspecified compactness issue.  It
has the exact scalar form (25).  Endpoint normalization cannot change it.
Positivity improvement can address it only through a quantitative,
support-uniform Harnack--tightness estimate of the form (13).  Theorem 6
shows that qualitative positivity, simplicity, and a vanishing model
residual leave the off-line alternative completely open.

For the actual ordinary-prime operator, the smallest new theorem capable of
closing this branch is therefore one of the following equivalent-strength
inputs:

1. a direct anti-orthogonality estimate with
   \(|\langle\phi_L,q_L\rangle|\gg\|A_Lq_L\|\);
2. a quantitative Harnack--tightness bound satisfying (13);
3. a signed arithmetic estimate excluding every fixed negative evaluation
   mode from the least spectral branch.

Any of the three proves RH by Corollary 3.  The bilateral theorem of 106.11
has removed parity dominance from the list of required inputs.  The three
remaining quantitative inputs are not supplied by CCM compact-resolvent
theory, Suzuki real-rootedness, or the prolate near-radical estimate alone.

## Status

Proved here:

- the sharp residual/overlap identity;
- the elementary parity consequence of failure of RH: a fixed negative
  test in at least one parity block;
- its direct implication to RH for the full ordinary-prime Weil
  restrictions;
- invariance of the overlap angle under endpoint normalization;
- the exact Harnack--tightness sufficient condition;
- a positivity-improving countermodel with fixed negative ground energy,
  strictly positive near-radical model, and vanishing overlap;
- compatibility of that countermodel with the hypothetical off-line
  evaluation geometry.

Not proved here:

- the arithmetic anti-orthogonality estimate (25), or the stronger
  curvature gate (26), for the actual ordinary-prime CCM ground states.

Subsequently proved in 106.11:

- failure of RH supplies fixed negative tests in both parity blocks;
- hence the even CCM anti-orthogonality gate needs no additional parity
  hypothesis.
