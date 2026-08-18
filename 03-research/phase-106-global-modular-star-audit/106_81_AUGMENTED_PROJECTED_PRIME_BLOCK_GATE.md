# 106.81 — The augmented projected prime-block gate

## Purpose and verdict

The pure conditional-distance determinant of 106.80 is a correct lower
certificate, but it is not the force-bearing quantity.  Numerically it can
miss a successful block-Kalman crossing by several orders of magnitude.
The reason is structural: regression against the old observation range is
not free.  It is priced by the positive preceding prime--Gamma block
\(A\).

This note retains that price and combines it with the exact theta midpoint
channel.  For a finite block \(\mathcal P\) of primes, the full gain is

\[
 \Delta_{\mathcal P}
 =\min_y\{\langle y,Ay\rangle+\|r+Uy\|^2\}.      \tag{1}
\]

Projecting every literal displacement feature onto its normalized odd
midpoint aperture gives matrices \(S_0\) and \(r_S\) and the rigorous
lower bound

\[
 \boxed{
 \Delta_{\mathcal P}\ge
 \Delta_{\mathcal P}^{\rm mid}
 :=r_S^*(I+S_0A^{-1}S_0^*)^{-1}r_S.}             \tag{2}
\]

The right side has the exact augmented determinant representation

\[
 \boxed{
 \Delta_{\mathcal P}^{\rm mid}
 =\frac{\det\begin{pmatrix}
 A+S_0^*S_0&S_0^*r_S\\
 r_S^*S_0&\|r_S\|^2
 \end{pmatrix}}
 {\det(A+S_0^*S_0)}.}                            \tag{3}
\]

This is the correct regularized Cauchy--Binet object.  It does not require
the raw prime sampling matrix to have a large smallest singular value.
The old coercivity \(A\) controls the directions parallel to the old
samples; only the scalar midpoint response of the new signed regression
residual must remain large.

On a fixed elementary mode block that response is

\[
 (r_S)_p=-\sqrt{\beta_p}\{A_p(q^*)+\rho_p(q^*)\},
 \qquad
 \beta_p\asymp(\log p)p^2e^{-2\pi p},            \tag{4}
\]

with a controlled additive error.  Consequently the finite sufficient
crossing test becomes a weighted scalar phase-energy inequality, not a
raw \(M\)-column determinant inequality.

The conclusion is two-sided.

* This removes the unnecessarily strong high-dimensional frame demand.
  Baker separation is not needed to control all old columns
  simultaneously.
* Baker/rational independence still does not prove the remaining scalar
  estimate: the residual frequencies are Riemann spectral parameters, and
  every lower estimate remains multiplied by the summable theta strength
  \(\beta_p\).  A quantitative match with the signed deficit is still
  required.

## 1. The exact augmented gain

Let

\[
 V_{M-1}=\operatorname{span}\{\phi_1,\ldots,\phi_{M-1}\}
 \subset V_M
\]

and suppose that the current signed finite head has block matrix

\[
 H_0=\begin{pmatrix}A&c\\c^*&h\end{pmatrix},
 \qquad A\succ0.                                  \tag{5}
\]

Set

\[
 a=A^{-1}c,
 \qquad
 q^*=\phi_M-\sum_{j<M}a_j\phi_j,
 \qquad
 \sigma_0=h-c^*A^{-1}c.                          \tag{6}
\]

For a finite prime block \(\mathcal P\), let

\[
 \mathcal D_{\mathcal P}
 =\bigoplus_{p\in\mathcal P}
 \sqrt{\frac{\log p}{\sqrt p}}\,D_p              \tag{7}
\]

be the direct sum of the exact literal first-power features.  Prime powers
can be inserted without changing any argument.  Write

\[
 U=\mathcal D_{\mathcal P}|_{V_{M-1}},
 \qquad
 v=\mathcal D_{\mathcal P}\phi_M,
 \qquad
 r=v-Ua=\mathcal D_{\mathcal P}q^*.              \tag{8}
\]

The block-Kalman identity of 106.79 is

\[
 \Delta_{\mathcal P}
 =\min_y\{\langle y,Ay\rangle+\|r+Uy\|^2\}
 =r^*(I+UA^{-1}U^*)^{-1}r.                       \tag{9}
\]

Taking the Schur complement gives the exact full-feature determinant

\[
 \Delta_{\mathcal P}
 =\frac{\det\begin{pmatrix}
 A+U^*U&U^*r\\
 r^*U&\|r\|^2
 \end{pmatrix}}
 {\det(A+U^*U)}.                                 \tag{10}
\]

Formula (10), rather than the pure observation Gram, is the target to be
estimated.

### Proposition 1 — Exact singular channels and a directional bound

Let

\[
 C=UA^{-1/2},
 \qquad B=CC^*=UA^{-1}U^*.
\]

If \(s_j\) are the nonzero singular values of \(C\), \(e_j\) are the
corresponding left singular vectors, and

\[
 r=r_\perp+\sum_jr_je_j,
 \qquad r_\perp\in\ker U^*,
\]

then

\[
 \boxed{
 \Delta_{\mathcal P}
 =\|r_\perp\|^2+\sum_j\frac{|r_j|^2}{1+s_j^2}.}   \tag{10a}
\]

In particular,

\[
 \boxed{
 \Delta_{\mathcal P}
 \ge
 \frac{\|r\|^4}
 {\|r\|^2+\|A^{-1/2}U^*r\|^2}.}                 \tag{10b}
\]

#### Proof

The spectral resolution of \((I+CC^*)^{-1}\) gives (10a).  For (10b),
Cauchy--Schwarz applied to

\[
 (I+B)^{-1/2}r,
 \qquad (I+B)^{1/2}r
\]

gives

\[
 \|r\|^4
 \le
 \langle r,(I+B)^{-1}r\rangle
 \langle r,(I+B)r\rangle.                       \tag{10c}
\]

The first factor on the right is \(\Delta_{\mathcal P}\), while

\[
 \langle r,(I+B)r\rangle
 =\|r\|^2+\langle U^*r,A^{-1}U^*r\rangle.
\]

This proves (10b).  \(\square\)

Bound (10b) is strictly more directional than replacing \(B\) by its
operator norm.  Large singular channels are harmless when the new residual
has little projection onto their left singular vectors.

There is also an exact mixed-minor interpretation of (10).  Choose
\(L\) with \(A=L^*L\).  For any finite-row realization of the literal
feature, set

\[
 \mathsf X_{\rm full}=
 \begin{pmatrix}L&0\\U&r\end{pmatrix},
 \qquad
 \mathsf Y_{\rm full}=\begin{pmatrix}L\\U\end{pmatrix}.
                                                                  \tag{10d}
\]

Then

\[
 \boxed{
 \Delta_{\mathcal P}
 =\frac{
   \displaystyle\sum_{|I|=M}|\det(\mathsf X_{\rm full})_I|^2}
  {\displaystyle\sum_{|J|=M-1}|\det(\mathsf Y_{\rm full})_J|^2}.} \tag{10e}
\]

For the continuum displacement feature, the row sums in (10e) become the
mixed Gram--Andreief integrals of 106.80.  The terms use arbitrary mixtures
of rows from \(L\) and literal theta observations.  This is exactly the
energy omitted by the pure prime determinant.

## 2. Exact midpoint projection

For \(p\in\mathcal P\), put

\[
 t_p=\frac12\log p,
 \qquad
 a_p(y)=K(t_p+y)K(t_p-y),
 \qquad
 \mu_{2,p}=\int_{\mathbb R}y^2a_p(y)\,dy,        \tag{11}
\]

and define the normalized odd aperture vector

\[
 e_p(y)=\frac{y\sqrt{a_p(y)}}{\sqrt{\mu_{2,p}}}.
                                                                  \tag{12}
\]

Let \(\Pi_p=e_p\otimes e_p\), and let
\(\Pi_{\mathcal P}=\bigoplus_{p\in\mathcal P}\Pi_p\).  Define

\[
 S_0=\Pi_{\mathcal P}U,
 \qquad
 r_S=\Pi_{\mathcal P}r,                         \tag{13}
\]

identifying each one-dimensional range of \(\Pi_p\) with \(\mathbb C\).

### Theorem 2 — Augmented projection lower bound

One has (2), and its right side equals the determinant ratio (3).

#### Proof

For every \(y\), orthogonal projection decreases the feature norm:

\[
 \|r+Uy\|^2
 \ge\|\Pi_{\mathcal P}(r+Uy)\|^2
 =\|r_S+S_0y\|^2.                                \tag{14}
\]

Adding \(\langle y,Ay\rangle\) and taking the minimum gives

\[
 \Delta_{\mathcal P}
 \ge\min_y\{\langle y,Ay\rangle+|r_S+S_0y\|^2\}.
                                                                  \tag{15}
\]

The normal equation in (15) is

\[
 (A+S_0^*S_0)y=-S_0^*r_S.                       \tag{16}
\]

Substitution, followed by Woodbury, gives

\[
\begin{aligned}
 \Delta_{\mathcal P}^{\rm mid}
 &=\|r_S\|^2-r_S^*S_0(A+S_0^*S_0)^{-1}S_0^*r_S\\
 &=r_S^*(I+S_0A^{-1}S_0^*)^{-1}r_S.
\end{aligned}                                    \tag{17}
\]

The Schur determinant formula applied to the matrix in (3) proves the
ratio identity.  \(\square\)

The immediate scalar estimate is

\[
 \boxed{
 \Delta_{\mathcal P}
 \ge
 \frac{\|r_S\|^2}
 {1+\|S_0\|^2/\lambda_{\min}(A)}.}               \tag{18}
\]

Unlike a pure Gram-distance bound, (18) does not vanish when \(r_S\) lies
in the range of \(S_0\).  That component can be removed only by paying the
positive energy \(A\).

## 3. Cauchy--Binet with accumulated coercivity

Choose a square factor \(L\) with \(A=L^*L\), and define

\[
 \mathsf X=
 \begin{pmatrix}
 L&0\\
 S_0&r_S
 \end{pmatrix},
 \qquad
 \mathsf Y=
 \begin{pmatrix}
 L\\S_0
 \end{pmatrix}.                                 \tag{19}
\]

Then the numerator and denominator of (3) are

\[
 \det(\mathsf X^*\mathsf X),
 \qquad
 \det(\mathsf Y^*\mathsf Y),                    \tag{20}
\]

respectively.  Ordinary Cauchy--Binet therefore gives

\[
\boxed{
 \Delta_{\mathcal P}^{\rm mid}
 =\frac{
 \displaystyle\sum_{|I|=M}|\det\mathsf X_I|^2}
 {
 \displaystyle\sum_{|J|=M-1}|\det\mathsf Y_J|^2}.}            \tag{21}
\]

All minors in (21) are nonnegative squares.  The terms using all
\(M-1\) rows of \(L\) and one prime row contribute exactly

\[
 \det(A)\|r_S\|^2                               \tag{22}
\]

to the numerator.  The remaining terms are additional nonnegative mixed
old-coercivity/prime minors.  Thus (21) preserves both sources of
conditioning rather than requiring the prime rows alone to span every old
direction.

This explains the finite diagnostics attached to 106.80: the pure Gram
minor discards the terms in (21) containing rows of \(L\), precisely the
terms responsible for the observed extra gain.

## 4. Literal midpoint response of the signed residual

For an elementary mode \(\chi_z\), define

\[
 A_p(z)
 =2z\sin(zt_p)+\tanh(t_p/2)\cos(zt_p)            \tag{23}
\]

and

\[
 \beta_p=C_\Xi^2\pi^3(\log p)p^2e^{-2\pi p}
 (1+p^{-1/2})^{-2}.                              \tag{24}
\]

The projected-row calculation uses the Gaussian moments already proved
in 106.73.  Uniformly on every fixed compact strip block,

\[
 \left\langle e_p,
 \sqrt{\frac{\log p}{\sqrt p}}D_p\chi_z
 \right\rangle
 =-\sqrt{\beta_p}\{A_p(z)+\rho_p(z)\},          \tag{25}
\]

where

\[
 |\rho_p(z)|\le C_{\mathcal Z}p^{b/2-1}.         \tag{26}
\]

For jets of order at most \(J\), multiply the right side of (26) by
\((1+\log p)^J\).  For completeness, (25) follows by inserting

\[
 \chi_z(t_p+y)-\chi_z(t_p-y)
 =2\chi_z'(t_p)y+\frac13\chi_z'''(t_p)y^3+cdots
\]

in the projection integral, using
\(\mu_{4,p}/\mu_{2,p}=O(p^{-1})\), and the exact identity

\[
 2\chi_z'(t_p)=-\operatorname {sech}(t_p/2)A_p(z).
\]

The normalization is exactly (24), up to the additive error (26).

Extend \(A_p\) and \(\rho_p\) linearly to \(V_M\).  In particular, for
the signed regression residual (6),

\[
 \eta_p:=A_p(q^*)
 =A_p(\phi_M)-\sum_{j<M}a_jA_p(\phi_j),          \tag{27}
\]

and

\[
 \boxed{
 (r_S)_p=-\sqrt{\beta_p}\{\eta_p+\rho_p(q^*)\}.}                \tag{28}
\]

If \(V_p\) denotes the row of old samples
\(A_p(\phi_1),\ldots,A_p(\phi_{M-1})\), and \(R_p\) its error row, then

\[
 (S_0)_{p,*}=-\sqrt{\beta_p}(V_p+R_p).           \tag{29}
\]

## 5. The regularized scalar crossing certificate

Equations (18), (28), and (29) prove the following result.

### Theorem 3 — Finite regularized phase-energy test

If \(\sigma_0<0\), the staircase row crosses after \(\mathcal P\) whenever

\[
\boxed{
 \frac{
 \displaystyle\sum_{p\in\mathcal P}
 \beta_p|\eta_p+\rho_p(q^*)|^2}
 {\displaystyle
 1+\lambda_{\min}(A)^{-1}
 \sum_{p\in\mathcal P}\beta_p\|V_p+R_p\|^2}
 >-\sigma_0.}                                    \tag{30}
\]

The sharper finite certificate replaces the left side of (30) by the
augmented minor ratio (21).  Both are built from the actual ordinary-prime
weights and can be checked by outward interval arithmetic.

The mathematical improvement over the pure determinant target is exact:
instead of proving that all \(M\) prime-sampling columns are uniformly
independent, it is enough to prove that the **one new residual response**
\(\eta_p\) has enough weighted energy after the old directions have been
regularized by \(A\).

## 6. Diagnostic test of the directional bound

The script

```text
python3 tools/joint_block_innovation_diagnostic.py --dx 0.001 --span 20
```

now evaluates (10b) directly from the exact full atom matrices.  The
following rows are stable negative-pivot transitions in a
weighted-orthonormal basis of the first twenty real zero modes, recomputed
with meshes \(dx=10^{-3}\) and \(dx=5\cdot10^{-4}\).  The table reports
the finer mesh.  They are floating-point diagnostics, not interval
certificates.

\[
\begin{array}{c|c|c|c|c|c|c}
M&X_0\to X_1&-\sigma_0&d_M(\mathcal B)^2&
\Delta_{\mathcal B}&\text{bound (10b)}&
\text{bound}/\Delta\\ \hline
4&1\to2&2.105\,10^{-1}&1.058\,10^{-2}&
3.944\,10^{-1}&3.219\,10^{-1}&0.816\\
7&2\to3&1.343\,10^{-2}&3.565\,10^{-6}&
8.648\,10^{-2}&8.016\,10^{-2}&0.927\\
12&3\to4&2.290\,10^{-2}&1.479\,10^{-8}&
5.014\,10^{-2}&4.833\,10^{-2}&0.964\\
16&4\to5&1.316\,10^{-2}&2.346\,10^{-12}&
2.551\,10^{-2}&2.492\,10^{-2}&0.977
\end{array}                                                    \tag{30a}
\]

Thus (10b) certifies all four displayed crossings, whereas the pure
conditional distance fails by factors ranging from about \(20\) to more
than \(10^9\).  This confirms that the relevant quantity is not global
prime-frame conditioning but directional overlap with the singular
channels priced by \(A\).

At \(M=18\), the coarser mesh produces a negative pivot whereas the finer
mesh makes the same pivot positive.  That row is therefore excluded rather
than promoted as evidence in either direction.  The ratios in (30a) remain
stable under mesh refinement, but interval arithmetic is required before
any finite row is called a certificate.  The directional theorem itself is
exact; only this numerical table is diagnostic.

## 7. Attenuation and the role of Baker separation

The simplification in Section 5 does not remove the physical attenuation.
For a block of primes \(p\ge P\), 106.73 gives

\[
 \sum_{p\ge P}\beta_p
 \bigl(|\eta_p|^2+\|V_p\|^2+O(p^{b-2})\bigr)
 \le C_{M,X_0}(\log P)P^{2+b}e^{-2\pi P}.        \tag{31}
\]

The exact full-feature gain obeys the same upper scale because
\((I+UA^{-1}U^*)^{-1}\preceq I\).  Therefore any crossing based only on
the tail \(p\ge P\) necessarily requires

\[
 \boxed{
 -\sigma_0
 <C_{M,X_0}(\log P)P^{2+b}e^{-2\pi P}.}           \tag{32}
\]

Baker/rational-independence input has a smaller role than in the raw
determinant proposal, but it still does not prove (30):

1.  The scalar \(\eta_p\) is a finite trigonometric-exponential sum whose
    frequencies are the spectral parameters of the selected zero modes.
    Those parameters are not logarithms of algebraic numbers.  Smallness
    of \(\eta_p\) is therefore not controlled by a Baker lower bound for a
    nonzero integer linear form in \(\log p\).

2.  Rational independence can exclude some exact common periods, but it
    gives no lower bound for the weighted sum in (30).  Exact
    observability already proves that the full displacement feature of
    \(q^*\) is nonzero; the missing issue is its size at the physical
    midpoint projection.

3.  Even a hypothetical polynomial estimate

    \[
     \max_{p\in\mathcal P}|\eta_p|\ge P^{-C_M}
    \]

    remains multiplied by \(\beta_p\).  It can pay (30) only when the
    deficit is already at the matching superexponential theta-tail scale.

Thus the correct next theorem is not a high-dimensional Vandermonde bound.
It is the tail-matched scalar innovation estimate

\[
 \boxed{
 \sum_{p\in\mathcal P}\beta_p
 |A_p(q^*)+\rho_p(q^*)|^2
 >(-\sigma_0)
 \left(1+\frac{\|S_0\|^2}{\lambda_{\min}(A)}\right)}           \tag{33}
\]

for a suitable finite block before the available theta weight becomes too
small.

## 8. Status

Established here:

* the exact augmented determinant is retained;
* the exact singular-channel expansion and directional lower bound (10b)
  are proved;
* orthogonal midpoint projection gives a rigorous lower bound, not a
  signed asymptotic approximation;
* accumulated old coercivity and new prime sampling are combined by the
  Cauchy--Binet ratio (21);
* finite diagnostics show that (10b), unlike the pure observation
  determinant, retains most of the exact gain and certifies the observed
  negative-pivot crossings through dimension (16);
* the force-bearing matrix problem reduces to a directional scalar
  residual response;
* the unavoidable attenuation condition is (32).

Still required:

* a quantitative lower bound for the literal weighted residual response
  in (33), matched to the signed deficit.

The correction is substantial: raw prime-frame conditioning is not the
remaining obstruction.  The only phase quantity that must be controlled
is the innovation response of the new signed residual, with the old
directions regularized by their already proved positive block.
