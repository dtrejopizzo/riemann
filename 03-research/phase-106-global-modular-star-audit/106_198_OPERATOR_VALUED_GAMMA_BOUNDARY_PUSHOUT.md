# 106.198 — The operator-valued Gamma boundary pushout

## 1. Purpose

The shared-boundary construction of 106.196 uses the scalar finite part
\(B_\infty^*B_\infty=\kappa_\infty I\).  That is the correct zero-mode
normalization, but it does not retain the nonzero Gamma phases.  A scalar
archimedean row is precisely the type of post-collapse coupling shown to
be Euler-blind in 106.189.

This note inserts the complete Gamma translation gradient before
shorting.  The scalar Schur coefficient
\(\kappa_\infty^{-1}I\) is thereby replaced by

\[
 (\kappa_\infty I+\mathcal J_\Gamma)^{-1},                 \tag{1}
\]

where \(\mathcal J_\Gamma\) is the source-defined positive Gamma Green
operator.  This is the operator-valued, phase-preserving pushout required
by 106.192--106.193.

## 2. The complete Gamma gradient

Let \((\mathscr K,V_t)\) be the common real coefficient Hilbert space and
its strongly continuous orthogonal group from 106.154.  Put

\[
 g_\Gamma(u)=\frac{e^{-u/2}}{1-e^{-2u}},
 \qquad u>0.                                                \tag{2}
\]

On the natural form domain define

\[
 \boxed{
 (\mathcal G_\Gamma F)(u)
 =\sqrt{2g_\Gamma(u)}\,(I-V_u)F}                            \tag{3}
\]

as a map into
\(L^2((0,\infty),du;\mathscr K)\).  Its closed quadratic form is

\[
 \begin{aligned}
 \mathfrak j_\Gamma(F,G)
 &=2\int_0^\infty g_\Gamma(u)
   \langle(I-V_u)F,(I-V_u)G\rangle\,du.                    \tag{4}
 \end{aligned}
\]

Near zero, strong differentiability on the generator core gives
\((I-V_u)F=O(u)\), while \(g_\Gamma(u)=1/(2u)+O(1)\); the
integrand is therefore \(O(u)\).  At infinity the density decays
exponentially.  Monotone form closure defines a positive self-adjoint
operator \(\mathcal J_\Gamma\) such that

\[
 \mathcal G_\Gamma^*\mathcal G_\Gamma
 =\mathcal J_\Gamma.                                       \tag{5}
\]

### Theorem 2.1 — Exact Gamma spectral multiplier

If \(A\) is the self-adjoint generator \(V_u=e^{iuA}\), then

\[
 \boxed{
 \mathcal J_\Gamma
 =m_\Gamma(A),
 \qquad
 m_\Gamma(\gamma)
 =4\int_0^\infty g_\Gamma(u)
       (1-\cos(\gamma u))\,du.}                            \tag{6}
\]

This is exactly the even real Gamma Green multiplier of 106.176(14d).

#### Proof

Apply the spectral theorem to (4).  On a spectral vector of frequency
\(\gamma\),

\[
 \|(I-V_u)F\|^2
 =|1-e^{iu\gamma}|^2\|F\|^2
 =2(1-\cos(\gamma u))\|F\|^2.                              \tag{7}
\]

Multiplication by the factor \(2\) in (4) gives (6). \(\square\)

The Lévy density in (2) is the heat trace of the positive spin operator
\(N_\Gamma\) in 106.195.  Thus (3) and the determinant fiber there are
the Green and determinant realizations of the same archimedean page.

## 3. The full archimedean boundary row

Retain \(B_\infty F=v_\infty\otimes F\) from 106.196 and define

\[
 \boxed{
 \mathbb B_\infty F
 =B_\infty F\oplus\mathcal G_\Gamma F.}                    \tag{8}
\]

Its target is

\[
 \mathbb A_\infty
 =\left(\mathscr H_\infty\widehat\otimes\mathscr K\right)
  \oplus L^2((0,\infty),du;\mathscr K).                    \tag{9}
\]

### Theorem 3.1 — Strict positive boundary operator

\[
 \boxed{
 \mathbb B_\infty^*\mathbb B_\infty
 =K_\Gamma:=\kappa_\infty I+\mathcal J_\Gamma
 \succeq\kappa_\infty I.}                                 \tag{10}
\]

Consequently \(K_\Gamma^{-1}\) is bounded,
\(\|K_\Gamma^{-1}\|\le\kappa_\infty^{-1}\), and the
minimum-norm right inverse of \(\mathbb B_\infty^*\) is

\[
 \boxed{
 (\mathbb B_\infty^*)^\dagger
 =\mathbb B_\infty K_\Gamma^{-1}.}                        \tag{11}
\]

#### Proof

The two summands in (8) are orthogonal.  Equations 106.196(5) and (5)
give (10).  Strict positivity makes \(K_\Gamma^{-1}\) bounded, and

\[
 \mathbb B_\infty^*\mathbb B_\infty K_\Gamma^{-1}=I,      \tag{12}
\]

while the range of \(\mathbb B_\infty\) is orthogonal to the kernel of
its adjoint.  This is the Moore--Penrose formula (11). \(\square\)

## 4. The operator-valued shared-boundary cokernel

Double \(\mathbb A_\infty\) and \(K_\Gamma\), and retain the Tate
boundary row

\[
 \partial_{T,S}v=(R_SJ_Sv,R_Sv).                           \tag{13}
\]

The co-diagonal boundary injection is

\[
 \mathbb d_{\rm bd,S}F
 =\left(\Gamma_SF,\mathbb B_\infty^{(1)}F\right),        \tag{14}
\]

and its orthogonal cokernel model is

\[
 \boxed{
 \mathbb P_S
 =\ker\mathbb d_{\rm bd,S}^*.}                            \tag{15}
\]

Shorting the kernel of \((\mathbb B_\infty^{(1)})^*\), the canonical
representative of a Tate vector \(v\) is

\[
 \boxed{
 \left(
 v,
 -\mathbb B_\infty^{(1)}(K_\Gamma^{-1}\oplus
 K_\Gamma^{-1})\partial_{T,S}v
 \right).}                                                 \tag{16}
\]

### Theorem 4.1 — Phase-preserving Schur metric

The metric induced by (16) is

\[
 \boxed{
 \begin{aligned}
 g_{\mathbb P,S}(v,w)
 &=g_S(v,w)\\
 &\quad+\langle K_\Gamma^{-1}R_SJ_Sv,R_SJ_Sw\rangle\\
 &\quad+\langle K_\Gamma^{-1}R_Sv,R_Sw\rangle.
 \end{aligned}}                                            \tag{17}
\]

It is positive definite, Hodge invariant, compatible under adjoining
primes, and invariant under normalized real scaling.

#### Proof

Equation (10) gives, for every boundary value \(b\),

\[
 \|\mathbb B_\infty K_\Gamma^{-1}b\|^2
 =\langle K_\Gamma^{-1}b,b\rangle.                         \tag{18}
\]

This proves (17).  The first term is positive definite and the remaining
terms are nonnegative.  The coefficient complex structure commutes with
every \(V_u\), hence with \(\mathcal J_\Gamma\), \(K_\Gamma\), and its
inverse.  The two boundary components are exchanged by the Hodge
quarter-turn, proving invariance.  Extension by zero preserves the local
metric and both raw boundary sums, so the cofinal embeddings remain
isometric.  The normalized real flow commutes with every entry in (17).
\(\square\)

In the spectral representation of \(A\), the scalar boundary compliance
is

\[
 \boxed{
 \bigl(\kappa_\infty+m_\Gamma(\gamma)\bigr)^{-1}.}         \tag{19}
\]

Thus nonzero Gamma frequencies are no longer assigned the same response
as the zero mode.  This is the exact improvement over 106.196.

## 5. Relation with the charge-dependent requirement

In the total-energy description of 106.192, the coefficient frequency is
shifted by the arithmetic charge.  Functional calculus in (6) therefore
acts on the \(q\)-charge fiber as

\[
 m_\Gamma(E-\log q).                                       \tag{20}
\]

Hence (10) has the forced diagonal dependence

\[
 (K_\Gamma(E))_{q,q}
 =\kappa_\infty+m_\Gamma(E-\log q),                        \tag{21}
\]

while the Tate boundary row \(R_S\) mixes the common-valuation
multiplicities before \(K_\Gamma^{-1}\) is applied.  The resulting Schur
term in (17) is therefore not a scalar multiplier appended after Euler
collapse.  It is operator-valued on the shared boundary and preserves the
real phases.

## 6. Status and remaining theorem

Proved without RH or zero input:

* the closed full Gamma gradient and its exact multiplier;
* the strictly positive boundary operator \(K_\Gamma\);
* its bounded inverse and minimum-norm right inverse;
* the operator-valued shared-boundary cokernel;
* the positive phase-preserving metric (17);
* Hodge, cofinal, and normalized-scale compatibility;
* the charge-dependent Gamma law (21).

This supersedes the scalar compliance in 106.196; the latter is its
zero-frequency truncation.

Still required:

* pull back (17) through the derived CCM localization of 106.197;
* prove that its alternating form equals the CCM residue alternating form;
* prove that the resulting Hilbert completion retains the separated CCM
  quotient.

The last two clauses are now the sole global Hodge-index comparison; no
local coefficient, Gamma phase, boundary normalization, or kernel
faithfulness remains unspecified.
