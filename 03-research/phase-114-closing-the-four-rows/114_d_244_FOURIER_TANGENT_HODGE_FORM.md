# D.244 — A source-defined Lorentzian form on the prime tangent channels

## Verdict

The isolated self-dual local vector of D.242 has an exact first variation
whose Fourier-even and Fourier-odd parts have equal norm.  After tensoring
over a finite set of primes, the odd tangent channels remain mutually
orthogonal, whereas the even channels acquire coherent cross-prime
couplings.  Their signed Gram has inertia

\[
 (1,|S|-1,0)
\]

for \(|S|\ge2\).

This is a genuine source-defined Hodge-signature theorem using only local
additive Fourier self-duality.  It is not yet row D: the signed tangent Gram
is second order in the local logarithmic velocities, whereas the
A--B--C score is first order.  The remaining comparison is to show that the
canonical Fisher normalization and old-core shorting of this tangent form
is exactly the D.190 capacity residual.

## 1. Local tangent splitting

For one prime put

\[
 \sigma_p=\epsilon_0-p^{-1}\epsilon_1,\qquad
 d_p=\left.\partial_\sigma
   (\epsilon_0-p^{-\sigma-1/2}\epsilon_1)
 \right|_{\sigma=1/2}
 ={\log p\over p}\epsilon_1.                       \tag{1.1}
\]

Let

\[
 d_{p,+}={d_p+\mathcal F_pd_p\over2},\qquad
 d_{p,-}={d_p-\mathcal F_pd_p\over2}.              \tag{1.2}
\]

D.242 gives

\[
 d_{p,-}={\log p\over2p}w_p,\qquad
 \mathcal F_pd_{p,\pm}=\pm d_{p,\pm}.              \tag{1.3}
\]

Since \(\mathcal F_p\epsilon_1\) has no \(\epsilon_1\)-coefficient,

\[
 \langle d_p,\mathcal F_pd_p\rangle=0.             \tag{1.4}
\]

Therefore

\[
 \boxed{
 \|d_{p,+}\|^2=\|d_{p,-}\|^2
 ={(\log p)^2(p-1)\over2p^2}.
 }                                                   \tag{1.5}
\]

The central vector has norm

\[
 a_p:=\|\sigma_p\|^2=1-p^{-2},                     \tag{1.6}
\]

and, because \(d_{p,-}\) is Fourier odd,

\[
 \langle d_{p,-},\sigma_p\rangle=0,\qquad
 b_p:=\langle d_{p,+},\sigma_p\rangle
      =\langle d_p,\sigma_p\rangle
      =-{(\log p)(p-1)\over p^2}.                  \tag{1.7}
\]

All formulas are exact with the self-dual Haar normalization.

## 2. Tensor tangent channels

For a finite set \(S\) of primes let

\[
 \Sigma_S=\bigotimes_{p\in S}\sigma_p,
\]

and for \(p\in S\) define

\[
 e_{p,\pm}
 =d_{p,\pm}\otimes
   \bigotimes_{\substack{q\in S\\q\ne p}}\sigma_q.
                                                               \tag{2.1}
\]

Put \(A_S=\prod_{q\in S}a_q\).  Tensor-product orthogonality gives

\[
 \langle e_{p,-},e_{q,-}\rangle
 =0\qquad(p\ne q),                                  \tag{2.2}
\]

and (1.5) gives equal diagonal Grams

\[
 \|e_{p,+}\|^2=\|e_{p,-}\|^2
 =A_S\,{(\log p)^2\over2(p+1)}.                    \tag{2.3}
\]

For distinct primes, (1.7) gives

\[
 \langle e_{p,+},e_{q,+}\rangle
 =A_S\,x_px_q,\qquad
 x_p={b_p\over a_p}=-{\log p\over p+1}.             \tag{2.4}
\]

The signed tangent form

\[
 \mathfrak h_S(c,c)
 =\left\|\sum_{p\in S}c_pe_{p,+}\right\|^2
  -\left\|\sum_{p\in S}c_pe_{p,-}\right\|^2         \tag{2.5}
\]

therefore has matrix

\[
 \boxed{
 [\mathfrak h_S]_{pq}
 =\begin{cases}
 0,&p=q,\\
 A_Sx_px_q,&p\ne q.
 \end{cases}
 }                                                   \tag{2.6}
\]

Equivalently,

\[
 [\mathfrak h_S]
 =A_S\left(xx^*-\mathrm{diag}(|x_p|^2)\right). \tag{2.7}
\]

## 3. Exact inertia

\[
 \boxed{
 \mathrm{Inertia}(\mathfrak h_S)
 =\begin{cases}
 (0,0,1),&|S|=1,\\
 (1,|S|-1,0),&|S|\ge2.
 \end{cases}
 }                                                   \tag{3.1}
\]

Indeed, on the codimension-one hyperplane

\[
 x^*c=0,
\]

equation (2.7) becomes

\[
 \mathfrak h_S(c,c)
 =-A_S\sum_p|x_p|^2|c_p|^2<0
\]

for \(c\ne0\).  Thus the positive index is at most one.  For
\(r=|S|\ge2\), the matrix is nonsingular because the determinant lemma
gives

\[
 \det(xx^*-\mathrm{diag}(|x_p|^2))
 =(-1)^r(1-r)\prod_p|x_p|^2\ne0.                  \tag{3.2}
\]

Its trace is zero, so it cannot be negative definite; hence it has exactly
one positive eigenvalue and \(r-1\) negative eigenvalues.

This proof is finite-dimensional but uniform in \(S\) and uses no
information about zeta zeros.

## 4. Degree coordinates

There is a distinguished rescaling which exposes the arithmetic degree.
Write

\[
 c_p=(p+1)m_p.                                      \tag{4.1}
\]

Since \(x_pc_p=-(\log p)m_p\), formula (2.7) becomes

\[
 \boxed{
 \mathfrak h_S(c,c)
 =A_S\left[
   \left(\sum_{p\in S}(\log p)m_p\right)^2
   -\sum_{p\in S}(\log p)^2|m_p|^2
 \right].
 }                                                   \tag{4.2}
\]

Thus, with

\[
 \deg_S(m)=\sum_{p\in S}(\log p)m_p,                \tag{4.3}
\]

one has the strict primitive inequality

\[
 \boxed{
 \deg_S(m)=0,\ m\ne0
 \quad\Longrightarrow\quad
 \mathfrak h_S(c,c)
 =-A_S\sum_p(\log p)^2|m_p|^2<0.
 }                                                   \tag{4.4}
\]

The rescaling (4.1) is the unique diagonal rescaling, up to a common
scalar, which changes the source functional
\(-\log p/(p+1)\) into the arithmetic mass \(\log p\).  It is therefore
canonical once compatibility with the A--B contact normalization is
required.  What remains unproved is that this degree coordinate is the
coordinate induced by the completed mixed correspondence comparison.

Equation (4.4) is an exact finite-prime Castelnuovo--Severi inequality for
the tangent form.  It is not obtained from the zeta explicit formula.

It also constructs the sharp contraction.  Let

\[
 \mathcal E_\pm c=\sum_{p\in S}c_pe_{p,\pm},
 \qquad
 \mathcal K_S=\{c:x^*c=0\}.
\]

Since the odd channels are nonzero and mutually orthogonal,
\(\mathcal E_-\) is injective.  Define

\[
 \Theta_S(\mathcal E_-c)=\mathcal E_+c,
 \qquad c\in\mathcal K_S.                           \tag{4.4a}
\]

Then (4.4), in the original coordinates, proves

\[
 \boxed{
 \|\Theta_S\mathcal E_-c\|^2
 \leq\|\mathcal E_-c\|^2,\qquad c\in\mathcal K_S.
 }                                                   \tag{4.4b}
\]

Thus \(\|\Theta_S\|\leq1\), and equality for a nonzero finite vector is
impossible.  This contraction is defined by additive-Fourier parity before
any pseudoinverse or explicit-formula sign is introduced.

The same formula gives an exact rank-one completion.  Define the positive
local Fisher contact

\[
 \mathfrak c_S(c,c)
 :=A_S\sum_p|x_p|^2|c_p|^2
 =A_S\sum_p(\log p)^2|m_p|^2.                      \tag{4.5}
\]

Then

\[
 \boxed{
 \mathfrak h_S+\mathfrak c_S
 =A_S\,|\deg_S|^2
 }                                                   \tag{4.6}
\]

has rank one.  Thus the coherent even tangent couples the independent
local odd contacts into a single global degree direction.  Algebraically,
this is exactly the mechanism missing from the finite-contact obstruction:
one positive local channel per prime is replaced by one global positive
channel and a negative primitive complement.

The word “contact” in (4.5) refers to the Fisher tangent contact.  Its
comparison with the torsion determinant contact \(\log p\) of row B
requires the inverse Fisher normalization in the next section and is not
being assumed here.

### Torsion-normalized contact coordinates

The inverse Fisher normalization is an explicit congruence.  Put

\[
 m_p={z_p\over\sqrt{\log p}}.                       \tag{4.7}
\]

Then (4.2) becomes

\[
 \boxed{
 A_S^{-1}\mathfrak h_S(z,z)
 =\left|\sum_{p\in S}\sqrt{\log p}\,z_p\right|^2
  -\sum_{p\in S}(\log p)|z_p|^2.
 }                                                   \tag{4.8}
\]

The negative diagonal in (4.8) is exactly the reduced torsion-contact Gram
\(\bigoplus_p(\log p)\) of row B, with one idempotent channel for all
powers of the same prime.  Hence

\[
 A_S^{-1}\mathfrak h_S+
 \bigoplus_{p\in S}(\log p)
 =
 \left(\sqrt{\log p}\sqrt{\log q}\right)_{p,q}       \tag{4.9}
\]

is positive of rank one.  This proves, at the finite prime-tangent level,
an exact source-defined completion of the multi-positive contact blocks
into one positive global line.

The normalization in (4.7) is forced if the diagonal tangent energy
\((\log p)^2\) is required to equal the determinant contact \(\log p\).
It does not yet prove that the support-localized Gamma--Poisson shorting
implements this congruence on the completed mixed correspondence module.

## 5. Cofinal prime limit and equality

Remove the harmless scalar \(A_S\) and use the torsion-normalized
coordinates.  For \(S\subset S'\), zero-extension gives

\[
 A_S^{-1}\mathfrak h_S
 =\left.(A_{S'}^{-1}\mathfrak h_{S'})\right|_{\mathbb C^S}. \tag{5.1}
\]

Hence there is a well-defined Hermitian form on the algebraic direct limit
\(\mathbb C^{(\mathbb P)}\):

\[
 \boxed{
 \mathfrak h_{\mathbb P}(z,z)
 =|d_{\mathbb P}(z)|^2
  -\sum_p(\log p)|z_p|^2,\qquad
 d_{\mathbb P}(z)=\sum_p\sqrt{\log p}\,z_p .
 }                                                   \tag{5.2}
\]

Every finite-dimensional restriction has positive index one.  On the
primitive kernel,

\[
 \boxed{
 d_{\mathbb P}(z)=0
 \quad\Longrightarrow\quad
 \mathfrak h_{\mathbb P}(z,z)
 =-\sum_p(\log p)|z_p|^2\leq0,
 }                                                   \tag{5.3}
\]

and equality holds only for \(z=0\).

The degree functional is not bounded on the bare Hilbert completion
\(\ell^2(\log p)\); this is the same finiteness obstruction that forbids a
finite-rank Néron--Severi replacement.  It is continuous on the rapidly
decreasing prime-coordinate subspace inherited from the nuclear Dirichlet
algebra, where
\(\sum_p\sqrt{\log p}|z_p|<\infty\).  Thus (5.2) has a natural nuclear
form domain, but no Hilbert completion is silently asserted.

The equality case of the source Hodge form is therefore completely
classified before comparison with row C.

### Lift of all prime powers

The one-coordinate-per-prime formulation does not discard Frobenius depth.
For a finitely supported balanced correspondence coefficient
\(a=(a_n)\), put

\[
 z_p(a)=\sum_{k\geq1}p^{-k/2}a_{p^k}.              \tag{5.4}
\]

Then

\[
 \begin{aligned}
 \sum_p(\log p)z_p(a)\overline{z_p(b)}
 &=
 \sum_p\sum_{k,\ell\ge1}
 {\,\log p\over p^{(k+\ell)/2}}\,
 a_{p^k}\overline{b_{p^\ell}}.                    \tag{5.5}
 \end{aligned}
\]

The coefficient is exactly

\[
 {\Lambda(p^{k+\ell})\over\sqrt{p^{k+\ell}}},
\]

and terms supported at two different primes vanish.  Thus (5.5) is the
complete centrally normalized reduced-contact Gram, including every prime
power.  Formula (5.2) therefore lifts canonically along (5.4) to the
prime-power correspondence algebra.

This lift is compatible with the one-state resolvent compression of D.237:
the geometric series in (5.4) is the scalar orbit coordinate of
\((I-p^{-1/2}U_p)^{-1}\).

## 6. The forced-Green mismatch

The prime tangent theorem does not by itself identify the completed
A--B--C form.  On the balanced correspondence coefficients it supplies

\[
 |\sum_p\sqrt{\log p}\,z_p|^2
 -\sum_p(\log p)|z_p|^2,                            \tag{6.1}
\]

whereas row C fixes

\[
 B_{\rm nuc}=K_{\rm fin}+G_\infty.                 \tag{6.2}
\]

The archimedean operator \(G_\infty\) has infinite rank on every nontrivial
support interval.  The degree term in (6.1) has rank one on every finite
prime set.  Therefore (6.1) cannot equal (6.2) without an additional
infinite-dimensional Gamma tangent channel and a nontrivial comparison.
This is a rank obstruction, not a normalization issue.

Consequently D.244 solves the local-prime Hodge completion and its equality
case, but not the forced Green comparison.  The Gamma--support curvature
remains essential.

## 7. Relation to the row-D gate

The form (2.5) has three features required of a Hodge input:

1. it is constructed before any explicit-formula sign;
2. it has one positive direction for every finite prime set;
3. its negative hyperplane is given explicitly by \(x^*c=0\).

But it is not yet identified with \(Q_T\) or its threshold residual.
Specifically:

* its entries are quadratic in the tangent velocities \(\log p\);
* the A--B--C logarithmic score is first order in those velocities;
* support compression and old-core Green shorting are absent from (2.5);
* the archimedean Gamma tangent and the two Tate equations have not yet
  been inserted.

The correctly typed comparison target is not
\(\mathfrak h_S=Q_T\).  It is:

> **Fisher-shorted comparison.**  Equip the tangent channels with the
> inverse local Fisher metric, transport them through the adelic quotient,
> compress by support and the two Tate equations, and short the transported
> old channel.  Prove that the resulting born form is
> \[
> B_E-X_{OE}^*A_O^\dagger X_{OE}.
> \]

If this theorem holds, (3.1) supplies the source-side one-positive-direction
input and the primitive Tate hyperplane must be compared with
\(x^*c=0\).  If it fails, the exact discrepancy identifies which Gamma or
support curvature is still missing.

## 8. Classification

* Local Fourier tangent splitting (1.1)--(1.7): **PROVED**.
* Tensor Gram formulas (2.2)--(2.7): **PROVED IDENTITIES**.
* Lorentzian inertia theorem (3.1): **PROVED**.
* Identification of its negative hyperplane: **PROVED**.
* Degree-coordinate primitive inequality (4.2)--(4.4): **PROVED**.
* Source-defined sharp prime-tangent contraction (4.4a)--(4.4b):
  **PROVED**.
* Rank-one local-to-global completion (4.5)--(4.6): **PROVED**.
* Torsion-normalized completion of the row-B prime contact Gram
  (4.7)--(4.9): **PROVED AT THE FINITE TANGENT LEVEL**.
* Cofinal nuclear prime form and primitive equality case (5.1)--(5.3):
  **PROVED**.
* All-prime-power lift (5.4)--(5.5): **PROVED**.
* Equality with the completed row-C form without a Gamma tangent:
  **IMPOSSIBLE BY RANK**.
* Fisher-shorted comparison with D.190: **OPEN**.
* Agreement of the Hodge hyperplane with the two Tate primitive equations:
  **OPEN**.
* Row D: **OPEN**.
