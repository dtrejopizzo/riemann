# D.189 — The exact return is not the raw Witt Gram

## Verdict

There is no exact identity

\[
 q_N^*T^kq_N= \text{a scalar multiple of }V_{N,k+1}
 \quad\text{or }V_{N,k+1}+H_{N,k+1}                 \tag{0.1}
\]

derived only from Witt composition and integer-cell orthogonality.
Those Grams occur before the reference inverse is inserted.  The exact
return contains matrix elements of the compressed Green operator between
distinct translated strips.

More precisely, after expanding the arithmetic channels, every return has
the form

\[
 \boxed{
 q_N^*T^kq_N
 =\sum_{\boldsymbol n,\boldsymbol m}
 c_{\boldsymbol n}\overline{c_{\boldsymbol m}}\,
 \mathcal G_{k,N}(\boldsymbol n,\boldsymbol m)
 +\mathcal A_{k,N},}                                 \tag{0.2}
\]

where

* \(c_{\boldsymbol n}\) is the exact product of
  \(\Lambda(n_i)/\sqrt{n_i}\);
* \(\mathcal G_{k,N}\) contains the intervening complete Green kernels,
  boundary projections and Tate shorting;
* \(\mathcal A_{k,N}\) contains the \(\beta,Q_{1/2}\), Gamma and endpoint
  channels.

The raw Witt Gram is recovered only when

\[
 \mathcal G_{k,N}(\boldsymbol n,\boldsymbol m)
 =\mathbf1_{\prod n_i=\prod m_i}
 \quad\text{(plus the one reflected collision).}    \tag{0.3}
\]

The actual Green kernel does not satisfy (0.3).  It is positive and
convolution-dominated after the D.182 split, which proves the majorant
D.183, but it has nonzero off-diagonal matrix elements.

Consequently D.187 proves uniform summability of the correct arithmetic
majorant; it cannot by itself provide the sharp unit Schur constant.
The remaining task is genuinely a defect/Douglas factorization of the
centered cross, not an omitted convolution calculation.

## 1. Exact feature expansion

Let

\[
 R=X^*X,\qquad L=Y^*Y,\qquad
 A=YR^{-1/2},\qquad T=A^*A.                          \tag{1.1}
\]

For a centered cross \(q\),

\[
 q^*T^kq
 =\langle Aq,(AA^*)^{k-1}Aq\rangle,\qquad k\ge1.    \tag{1.2}
\]

The arithmetic part of \(Y\) is the direct sum of
\(\sqrt{w_n}J_{n,+}\), while \(R^{-1}\) is the Green operator of Gamma
plus all \(\sqrt{w_n}J_{n,-}\), compressed to support and to the two Tate
conditions.  Expanding (1.2) therefore alternates

\[
 J_{n,+},\quad R^{-1},\quad J_{m,+}^*.              \tag{1.3}
\]

After applying the Hadamard rotations, a typical coefficient is a matrix
element

\[
 \langle U_{\boldsymbol m}f,\,
 R^{-1}U_{\boldsymbol n}g\rangle                     \tag{1.4}
\]

or an iterated version of it.  Integer-cell separation proves
orthogonality when \(R^{-1}\) is absent.  It does not diagonalize (1.4).

## 2. Finite killed-shift counterexample

Let \(e_0,e_1,e_2,e_3\) be the standard basis of \(\mathbb R^4\).  Two
directed placements send a one-dimensional boundary source to

\[
 U_1e_0=e_1,\qquad U_2e_0=e_2.                      \tag{2.1}
\]

They are exactly orthogonal.  For weights \(a,b>0\), the raw synthesis is

\[
 B e_0=ae_1+be_2,\qquad
 \|Be_0\|^2=a^2+b^2.                                \tag{2.2}
\]

Let \(\mathcal R\) be a strictly positive killed graph Laplacian on the
four-point interval and \(G=\mathcal R^{-1}\).  Positivity improvement of
the Green kernel gives

\[
 \langle e_1,Ge_2\rangle>0.                         \tag{2.3}
\]

Therefore

\[
\begin{aligned}
 \langle Be_0,GBe_0\rangle
 &=a^2G_{11}+b^2G_{22}+2abG_{12}\\
 &\ne c(a^2+b^2)                                    \tag{2.4}
\end{aligned}
\]

for any scalar \(c\) determined solely by the raw Gram.  Varying one
interior killing coefficient changes \(G_{12}\) while preserving (2.1)
and (2.2), so no universal raw-Witt identity can restore (2.4).

The example has exactly the structural features relevant here:

* orthogonal untranslated placements;
* a positive Dirichlet/killed reference;
* a positive Green kernel;
* nonzero realignment after inversion.

A rank-two compression, modelling Tate, changes \(G\) by finite rank but
does not force every off-diagonal element to vanish.

## 3. What survives exactly

Three statements remain valid.

1. **Before inverses:** ordered Witt words group exactly to
   \(\Lambda_k(m)/\sqrt m\), and their integer-cell Gram is
   \(V_{N,k}\pm H_{N,k}\).
2. **Localized Markov inverses:** D.183 gives a positive convolution
   majorant preserving those same Grams.
3. **All depths:** D.187 proves that the majorant is summable uniformly in
   \(k\).

None of these statements identifies the exact signed return with its
majorant.  The difference is the Green-weighted centered discrepancy and
the endpoint/Gamma channel in (0.2).

## 4. Sharp remaining statement

Let \(D=I-T\) on the already proved old cell.  The exact acceptance
condition remains

\[
 q_N=D^{1/2}a_N,\qquad
 \|a_N\|^2\le\text{the remaining born margin}.       \tag{4.1}
\]

Equivalently,

\[
 q_N^*D^\dagger q_N
 =\sum_{k\ge0}q_N^*T^kq_N
 \le\text{the remaining born margin}.               \tag{4.2}
\]

Equation (0.2) is the correct expansion to use in proving (4.2).  Replacing
its Green matrix by (0.3) proves only the arithmetic majorant and can lose
the unit constant in either direction.

