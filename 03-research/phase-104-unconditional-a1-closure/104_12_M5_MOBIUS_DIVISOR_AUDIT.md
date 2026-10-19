# 104_12 — M5: Möbius–divisor convolution and the positive-adjoint obstruction

**Status:** the exact signed convolution that M5 called for is obtained, but the
resulting inequality is exactly the first-difference gate, not a new bound. The
additional attempt to turn the Möbius inversion into a positive Gram factorization is
ruled out on the minimal divisor poset \(\{1,p\}\). The structural reason is that
Dirichlet inversion is holomorphic, while a Hilbert square introduces the adjoint and,
with it, ratios \(n/m\).

This document deepens Section 7 of `104_11`; it does not repeat the `max`-kernel
stop-gate. Neither A1 nor RH is proved.

## 1. Preregistration and falsifiers

M5 may use:

1. \(\Lambda=\mu*\log\) in the Dirichlet convolution algebra;
2. absolute convergence for \(a=1+\varepsilon>1\);
3. the exact Laguerre addition and generating formulas;
4. pairing of the pole with the prime term before
   \(\varepsilon\downarrow0\).

It may not infer a sign from:

* the Möbius coefficients taken separately;
* a norm of each factor taken separately;
* functional symmetry without the real von Mangoldt weights;
* a metric constructed after assuming the sought positivity.

The falsifiers are:

* **relaxed convolution level:** a single factor or a mass move produces a
  Laguerre response with both signs;
* **relaxed spectral level:** the quartet
  \(8-8\cosh(n\alpha)\cos(n\theta)\);
* **positive factorization level:** the divisor poset \(\{1,p\}\), treated in
  Section 5.

## 2. Degree convolution theorem

Let \(a=1+\varepsilon>1\). Define

\[
 M_j(a)=\sum_{d\ge1}{\mu(d)\over d^a}L_j(\log d),
 \qquad
 B_k(a)=\sum_{m\ge1}{\log m\over m^a}L_k^{(-1)}(\log m).
\tag{1}
\]

Both series converge absolutely. The addition formula

\[
 L_n(x+y)=\sum_{j=0}^nL_j(x)L_{n-j}^{(-1)}(y)
\tag{2}
\]

and the identity \(\Lambda=\mu*\log\) give

\[
 \boxed{
 P_n(a):=\sum_{r\ge2}{\Lambda(r)\over r^a}L_n(\log r)
 =\sum_{j=0}^nM_j(a)B_{n-j}(a).}
\tag{3}
\]

The proof is an absolutely convergent regrouping:

\[
 \begin{aligned}
 P_n(a)
 &=\sum_{dm\ge1}{\mu(d)\log m\over (dm)^a}
                   L_n(\log d+\log m)\\
 &=\sum_{j=0}^n
   \left(\sum_d{\mu(d)\over d^a}L_j(\log d)\right)
   \left(\sum_m{\log m\over m^a}L_{n-j}^{(-1)}(\log m)\right).
 \end{aligned}
\]

With \(t=z/(1-z)\), the generating functions are as follows. They are initially
understood in a neighborhood of \(z=0\) where \(\Re(a+t)>1\), and therefore as
equalities of analytic germs at \(z=0\). Neither convergence nor absence of
singularities is claimed over all of \(|z|<1\): upon continuation,
\(1/\zeta(a+t)\) may encounter zeros of \(\zeta\).

\[
 \boxed{
 \sum_{j\ge0}M_j(a)z^j={1\over1-z}{1\over\zeta(a+t)},
 \qquad
 \sum_{k\ge0}B_k(a)z^k=-\zeta'(a+t).}
\tag{4}
\]

Hence

\[
 \sum_{n\ge0}P_n(a)z^n
 ={1\over1-z}\left(-{\zeta'\over\zeta}(a+t)\right).
\tag{5}
\]

The importance of (3) is not a nonexistent positivity: it is that it keeps the
cancellation across all degrees \(j+(n-j)=n\) before any estimate is made.

## 3. Exact pairing with the pole

The corresponding continuous term is

\[
 J_{n,\varepsilon}
 =\int_1^\infty x^{-1-\varepsilon}L_n(\log x)\,dx
 ={(\varepsilon-1)^n\over\varepsilon^{n+1}}.
\tag{6}
\]

Its generating function is

\[
 \sum_{n\ge0}J_{n,\varepsilon}z^n
 ={1\over1-z}{1\over\varepsilon+t}.
\tag{7}
\]

Thus, the regulated cost of `103_67` is

\[
 \boxed{
 C_{n,\varepsilon}
 =\sum_{j=0}^nM_j(1+\varepsilon)B_{n-j}(1+\varepsilon)
 -J_{n,\varepsilon}.}
\tag{8}
\]

The two terms of (8) have no separate limit as
\(\varepsilon\downarrow0\). The form that automatically preserves this collision is

\[
 F_\varepsilon(z)
 =(\varepsilon+t)\zeta(1+\varepsilon+t).
\tag{9}
\]

From (9) through (12), all series and derivatives are likewise interpreted as
analytic germs at \(z=0\), within a neighborhood where
\(\Re(1+\varepsilon+t)>1\). None of these formulas presupposes a zero-free
continuation up to \(|z|=1\).

Since

\[
 -{d\over dt}\log\{(\varepsilon+t)\zeta(1+\varepsilon+t)\}
 =- {1\over\varepsilon+t}
   -{\zeta'\over\zeta}(1+\varepsilon+t),
\]

and \(dt/dz=(1-z)^{-2}\), one obtains

\[
 \boxed{
 \sum_{n\ge0}C_{n,\varepsilon}z^n
 =-(1-z)F_\varepsilon(z)^{-1}F_\varepsilon'(z).}
\tag{10}
\]

If

\[
 F_\varepsilon(z)=\sum_{k\ge0}f_kz^k,
 \qquad F_\varepsilon(z)^{-1}=\sum_{j\ge0}g_jz^j,
\]

and

\[
 h_n=\sum_{j=0}^ng_j(n-j+1)f_{n-j+1},
\tag{11}
\]

then

\[
 C_{0,\varepsilon}=-h_0,
 \qquad
 \boxed{C_{n,\varepsilon}=h_{n-1}-h_n\quad(n\ge1).}
\tag{12}
\]

This is the normalized version, finite at the pole, of the signed degree
convolution.

## 4. Exact comparison with the internal antecedents

### 4.1 E70.11

E70.11 establishes, in the multiplicative semigroup algebra,

\[
 Z^{-1}\delta Z=\sum_{r\ge2}\Lambda(r)e_r.
\tag{13}
\]

Equations (3)–(5) are exactly the pullback of (13) under the Laguerre
transform and the map \(s=a+z/(1-z)\):

| E70.11 | 104_12 |
|---|---|
| inverse \(Z^{-1}\) | coefficients \(M_j(a)\) |
| derivative \(\delta Z\) | coefficients \(B_k(a)\) |
| Dirichlet product | degree convolution (3) |
| connection \(Z^{-1}\delta Z\) | logarithmic derivative (10) |

Hence (3) is a useful and more concrete identity for A1, but it is not an
independent source of sign relative to E70.11.

### 4.2 E70.12

If \({\cal A}=F^{-1}F'\), then

\[
 {\cal A}'+{\cal A}^2=F^{-1}F''.
\tag{14}
\]

After undoing the substitution \(s=1+\varepsilon+t\), (14) is the Riccati
identity

\[
 \Lambda\log+\Lambda*\Lambda=\mu*\log^2
\tag{15}
\]

of E70.12. Composing with Cayley adds chain-rule factors, not a Gamma term nor a
sign. Using (14) as an inequality with no additional input would amount to citing
as a lemma the Euler–Gamma target that E70.12 left open.

### 4.3 103_71

The Cauchy inequality

\[
 \left|\sum_{j=0}^nM_jB_{n-j}\right|
 \le
 \left(\sum_{j=0}^n|M_j|^2\right)^{1/2}
 \left(\sum_{j=0}^n|B_{n-j}|^2\right)^{1/2}
\tag{16}
\]

is exactly the norm separation ruled out in 103_71. The positive factor
already has exponential size in a central lobe; (16) would require an exponential
compensation in the Möbius norm and eliminates the relative signs that (3)
preserves.

Conclusion: M5 can only advance by estimating (3), (8), or (10) **as a single
signed convolution**.

## 5. New feasibility test: can Möbius be the adjoint?

The holomorphic factorization

\[
 Z^{-1}\delta Z
 =Z^{-1/2}(\delta Z)Z^{-1/2}
\tag{17}
\]

looks like a congruence. To turn it into a square or a positive Gram form, the
holomorphic inverse would have to behave like the adjoint under some positive
metric. This fails algebraically.

Let \({\cal D}\) be a divisor-finite set, ordered by divisibility, and let

\[
 (Z_{\cal D})_{d,n}=\mathbf1_{d\mid n}
\tag{18}
\]

be its zeta matrix. Its inverse is the Möbius matrix \(M_{\cal D}=Z_{\cal D}^{-1}\).

**Theorem 1 (unipotent obstruction).** If \({\cal D}\) contains a nontrivial
divisibility relation, there is no positive-definite Hermitian matrix \(G\)
such that

\[
 M_{\cal D}=Z_{\cal D}^{\dagger_G}
 :=G^{-1}Z_{\cal D}^*G.
\tag{19}
\]

**Proof.** Equality (19) would imply

\[
 Z_{\cal D}^{\dagger_G}Z_{\cal D}=I,
\]

that is, \(Z_{\cal D}\) would be unitary for the positive inner product given by
\(G\). Then \(G^{1/2}Z_{\cal D}G^{-1/2}\) would be an ordinary unitary matrix,
and in particular diagonalizable. But \(Z_{\cal D}\) is unipotent triangular and,
if divisibility is nontrivial, has a nonzero Jordan part. It is not
diagonalizable. Contradiction. \(\square\)

The minimal falsifier is \({\cal D}=\{1,p\}\):

\[
 Z=\begin{pmatrix}1&1\\0&1\end{pmatrix},
 \qquad
 M=\begin{pmatrix}1&-1\\0&1\end{pmatrix}.
\tag{20}
\]

If \(G=\begin{pmatrix}a&b\\\bar b&c\end{pmatrix}>0\) and \(Z^*GZ=G\), entry
\((1,2)\) gives \(a+b=b\), so \(a=0\), impossible for \(G>0\).

This theorem separates two multiplications that must not be confused:

* \(MZ=I\) uses Dirichlet convolution and products \(mn\);
* a Hilbert square uses \(Z^*Z\) and generates ratios \(n/m\).

Möbius inversion cancels the first geometry, not the second. If the inverse is
replaced by the real adjoint, the ratio comb and the diagonal mass of E70.10
reappear. If (19) is forced through an indefinite metric, precisely the sought
positivity is lost.

Hence the most natural additional factorization for M5 is ruled out before an
extensive search.

## 6. Second tested variable: filtration by Euler factors

Another possibility is introducing a prime cutoff \(Y\) and activating the Euler
factors one by one. The increment corresponding to a prime \(p\) is

\[
 P_{n,p}(a)=\log p\sum_{k\ge1}p^{-ak}L_n(k\log p).
\tag{21}
\]

Response (21) changes sign as the degree and the factor's position relative to
the Laguerre zeros vary. Hence the \(Y\)-filtration is not monotone in the
sought functional. This is exactly the prime-cutoff falsifier of
`103_19` and the mass move of `103_59`; adding the variable \(Y\) creates no new
inequality.

## 7. The remaining inequality is not yet a mechanism

The condition required by the M1/M5 attack would be

\[
 \limsup_{\varepsilon\downarrow0}C_{n,\varepsilon}
 \le {1\over2}\Delta A_n.
\tag{22}
\]

By the exact identity of `103_59`,

\[
 \Delta D_n
 =\Delta A_n-2\lim_{\varepsilon\downarrow0}C_{n,\varepsilon},
\tag{23}
\]

(22) is exactly \(\Delta D_n\ge0\). It is a sufficient target stronger than
A1, not a consequence of (3) or of (10). Stating

\[
 \text{"the complete convolution (8) satisfies (22)"}
\]

with no additional lemma would just rename the target.

In the extension to all Hardy vectors, the Euler–Gamma connection inequality is
AHM, as already recorded by E70.11. In the present Laguerre family, (22) is its
first-difference diagonal. Neither version follows from the connection identity.

The off-line quartet shows the exact strength level: any derivation using only
the functional equation and conjugation violates (22) along subsequences. A valid
theorem must again quantitatively use the real weights
\(\Lambda(p^k)=\log p\).

## 8. The only M5 factorization not refuted

After Theorems 1 and (21), a continuation of M5 cannot be:

* an ordinary congruence with \(Z^{-1/2}\);
* a Hilbert square of the Möbius inverse;
* a monotone sum over Euler factors;
* Cauchy–Schwarz between the two degree sequences;
* the Riccati identity with no independent Gamma term.

The only unrefuted architecture within this family would be a **graded
Euler–Gamma complex** with three properties proved before invoking positivity:

1. its Euler differential produces the cross term (3);
2. its ratio correlations \(n/m\) are exact boundaries or algebraically
   canceling supersymmetric pairs;
3. the physical quotient preserves a positive metric and its remaining diagonal
   is exactly the Gamma budget \(\Delta A_n/2\).

The word "supersymmetric" is not the mechanism. Without a construction proving
1–3 simultaneously, this option is only a specification. A cancellation via
supertrace or a Krein metric does not help: it cancels the diagonals using
negative signs and produces no Hilbert inequality.

No such complex was found in this attack. The unipotent obstruction shows that it
would need to contain information beyond ordinary Möbius inversion.

## 9. Decision

```text
proved:
  exact Möbius–divisor convolution in the Laguerre degree;
  pole–prime normalization as -(1-z)F^{-1}F';
  formula-by-formula identification with E70.11 and E70.12;
  equivalence of the missing bound with the first-difference gate;
  impossibility of realizing Möbius = adjoint under a positive metric;
  return of the ratio comb when using the true adjoint.

ruled out:
  M5 as an ordinary Gram matrix or a Z^{-1/2} congruence;
  monotone filtration by Euler factors;
  separate norms in the degree convolution;
  Riccati as an autonomous source of sign.

not proved:
  a new inequality for the real signed convolution;
  a positive graded Euler–Gamma complex;
  (22), A1, or RH.

decision:
  M5 supplies an exact coordinate, but not a present closure mechanism.
  Following the Phase 104 order, the non-local M3 is activated; M5 should
  only be reopened if a concrete construction of complex 1–3 appears.
```
</content>
