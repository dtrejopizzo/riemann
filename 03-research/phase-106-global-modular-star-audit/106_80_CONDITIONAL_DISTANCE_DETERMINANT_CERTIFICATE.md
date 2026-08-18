# 106.80 — Conditional-distance determinants for literal prime blocks

## Purpose and conclusion

This note makes the finite-block certificate exact. Let a finite head
\(X_0\) have a positive preceding-mode block \(A\) on \(V_{M-1}\), and
add a finite nonempty block \(\mathcal B\) of previously omitted ordinary
prime powers. If \(U\) is the old-mode observation map and \(r\) is the
new-mode regression residual in that block, define

\[
 \widetilde G_{\mathcal B}^{(M)}
 :=
 \begin{pmatrix}
 A+U^*U&U^*r\\
 r^*U&\|r\|^2
 \end{pmatrix}.                                  \tag{1}
\]

The exact block-Kalman gain is the augmented conditional determinant

\[
 \Delta_{\mathcal B}
 =\left\langle r,(I+UA^{-1}U^*)^{-1}r\right\rangle
 =\frac{\det\widetilde G_{\mathcal B}^{(M)}}
        {\det(A+U^*U)}.                           \tag{2}
\]

Consequently, if the current scalar innovation is
\(\sigma_{M,X_0}<0\), the necessary-and-sufficient finite crossing test is

\[
 \boxed{
 \frac{\det\widetilde G_{\mathcal B}^{(M)}}
      {\det(A+U^*U)}
 >-\sigma_{M,X_0}.}                               \tag{3}
\]

The pure prime observation geometry supplies the secondary lower bound

\[
 \boxed{
 \Delta_{\mathcal B}\ge d_M(\mathcal B)^2
 =\frac{\det G_{\mathcal B}^{(M)}}
        {\det G_{\mathcal B}^{(M-1)}}.}           \tag{4}
\]

No ambient-norm determinant is missing from (4). The identity uses an
adapted ordered basis in which the new mode has coefficient one. A
dimensionless version, with the norm Gram included, is given in Section 5.

The raw determinant condition obtained by replacing the left side of
(3) with the ratio in (4) is sufficient but not necessary. Bound (4) is
optimal among lower bounds that use only the prime observation
geometry of \(\mathcal B\) and are uniform in the positive preceding
signed block. Numerically, however, it can lose several orders of
magnitude because it discards the component of \(r\) parallel to
\(\mathrm{ran}\,U\). The augmented determinant (2) retains that
component through \(A^{1/2}\) and is therefore the force-bearing target.

Each prime-power channel is an infinite-dimensional displacement feature.
It must not be replaced by a scalar midpoint sample. The exact
Gram--Andreief and continuous Cauchy--Binet formulas below retain the full
theta placement, the literal weights, complex zero modes, and confluent
multiplicity jets.

## 1. Literal weighted block and mode flag

Let

\[
 V_{M-1}=\mathrm{span}\,\{\phi_1,\ldots,\phi_{M-1}\}
 \subset
 V_M=\mathrm{span}\,\{\phi_1,\ldots,\phi_M\}. \tag{5}
\]

The basis may be complex. It may contain conjugate nonreal zero-orbit
modes and the jets required by multiple zeros. After removing the
\(z\leftrightarrow-z\) duplication, the vectors in (5) are linearly
independent.

For a prime power \(n=p^k\), put

\[
 u_n=\log n,
 \qquad
 w_n=\frac{\Lambda(n)}{\sqrt n}
     =\frac{\log p}{p^{k/2}}>0.                   \tag{6}
\]

In \(\mathcal Y_n=L^2(\mathbb R,dx;\mathbb C)\), with inner product
conjugate-linear in the first entry, define

\[
 (D_nq)(x)
 =\sqrt{K(x)K(x-u_n)}\{q(x)-q(x-u_n)\}.          \tag{7}
\]

Thus

\[
 \|D_nq\|_{\mathcal Y_n}^2
 =\mathcal J_{u_n}(q).                            \tag{8}
\]

For a finite nonempty block \(\mathcal B\), define the literal weighted
feature

\[
 \boxed{
 \mathcal D_{\mathcal B}q
 =\bigoplus_{n\in\mathcal B}\sqrt{w_n}\,D_nq}
 :V_M\longrightarrow
 \mathcal Y_{\mathcal B}
 :=\bigoplus_{n\in\mathcal B}\mathcal Y_n .      \tag{9}
\]

The square root in (9) is essential:

\[
 \mathcal D_{\mathcal B}^*\mathcal D_{\mathcal B}
 =\sum_{n\in\mathcal B}w_nD_n^*D_n,              \tag{10}
\]

which is exactly the physical prime-power increment. Put

\[
 U=\mathcal D_{\mathcal B}|_{V_{M-1}},
 \qquad
 v=\mathcal D_{\mathcal B}\phi_M.                \tag{11}
\]

In coefficient coordinates, \(U:\mathbb C^{M-1}\to\mathcal Y_{\mathcal B}\)
sends \(a\) to
\(\mathcal D_{\mathcal B}\sum_{j<M}a_j\phi_j\).

### Lemma 1 — Injectivity for complex modes and jets

The restriction of \(\mathcal D_{\mathcal B}\) to \(V_M\) is injective.
Consequently,

\[
 U^*U\succ0,
 \qquad
 \mathcal D_{\mathcal B}^*\mathcal D_{\mathcal B}\succ0
 \quad\text{on }V_M.                              \tag{12}
\]

#### Proof

Choose \(n\in\mathcal B\). If
\(\mathcal D_{\mathcal B}q=0\), then \(D_nq=0\). Strict positivity of
\(K(x)K(x-u_n)\) gives

\[
 q(x)=q(x-u_n)                                    \tag{13}
\]

almost everywhere and hence everywhere by continuity. Every elementary
zero mode and every finite parameter jet is a polynomial times a quotient
of trigonometric exponentials by \(\cosh(x/2)\). Since the finite set of
spectral parameters lies in the open strip, every \(q\in V_M\) obeys

\[
 |q(x)|\le C_q(1+|x|)^d e^{-\eta|x|}              \tag{14}
\]

for some \(\eta>0\). Parameter differentiation only changes the
polynomial factor, so (14) includes confluent jets and conjugate complex
orbits. Iterating (13) gives \(q(x)=q(x+ju_n)\to0\), hence \(q=0\).
The same argument on \(V_{M-1}\) proves injectivity of \(U\). \(\square\)

## 2. Conditional distance and Schur determinant

Let the signed finite-head form before adding \(\mathcal B\) have matrix

\[
 H_0=
 \begin{pmatrix}A&c\\c^*&h\end{pmatrix},
 \qquad A\succ0,                                  \tag{15}
\]

in the ordered basis (5). Set

\[
 a=A^{-1}c,
 \qquad
 q^*=\phi_M-\sum_{j<M}a_j\phi_j,
 \qquad
 \sigma_0=h-c^*A^{-1}c.                          \tag{16}
\]

The vector \(q^*\) has coefficient one on \(\phi_M\). Define

\[
 \boxed{
 d_M(\mathcal B)^2
 :=\mathrm{dist}\,\!\left(
 \mathcal D_{\mathcal B}q^*,
 \mathcal D_{\mathcal B}V_{M-1}
 \right)^2.}                                     \tag{17}
\]

Although \(q^*\) depends on the signed head, (17) does not: adding an
element of \(V_{M-1}\) to \(q^*\) does not change the distance. Equivalently,

\[
 d_M(\mathcal B)^2
 =\min_{b\in\mathbb C^{M-1}}\|v-Ub\|^2.          \tag{18}
\]

Let

\[
 G_{\mathcal B}^{(M)}
 =\left[\left\langle
 \mathcal D_{\mathcal B}\phi_i,
 \mathcal D_{\mathcal B}\phi_j
 \right\rangle\right]_{i,j\le M}
 =\begin{pmatrix}
 U^*U&U^*v\\
 v^*U&\|v\|^2
 \end{pmatrix},                                  \tag{19}
\]

and \(G_{\mathcal B}^{(M-1)}=U^*U\).

### Theorem 2 — Conditional-distance determinant identity

\[
 \boxed{
 \begin{aligned}
 d_M(\mathcal B)^2
 &=\|v\|^2-v^*U(U^*U)^{-1}U^*v\\
 &=\frac{\det G_{\mathcal B}^{(M)}}
         {\det G_{\mathcal B}^{(M-1)}}.
 \end{aligned}}                                  \tag{20}
\]

#### Proof

Lemma 1 gives \(U^*U\succ0\). The normal equation for (18) is

\[
 U^*Ub=U^*v,                                      \tag{21}
\]

so the unique minimizer is
\(b=(U^*U)^{-1}U^*v\). Substitution proves the first line of (20).
Congruence of (19) by

\[
 T=
 \begin{pmatrix}
 I&-(U^*U)^{-1}U^*v\\
 0&1
 \end{pmatrix}                                   \tag{22}
\]

gives

\[
 T^*G_{\mathcal B}^{(M)}T
 =(U^*U)\oplus[d_M(\mathcal B)^2].               \tag{23}
\]

Since \(\det T=1\), taking determinants proves the second line. This is a
Hermitian argument and therefore applies unchanged to complex orbit modes
and confluent jets. \(\square\)

## 3. Exact Kalman gain and the determinant lower certificate

Adding (10) changes (15) into

\[
 H_+=
 \begin{pmatrix}
 A+U^*U&c+U^*v\\
 c^*+v^*U&h+\|v\|^2
 \end{pmatrix}.                                  \tag{24}
\]

Let \(\sigma_+\) be its Schur pivot over the first \(M-1\) coordinates.
Writing

\[
 r=v-Ua=\mathcal D_{\mathcal B}q^*               \tag{25}
\]

gives the exact block-Kalman identity

\[
 \boxed{
 \sigma_+=\sigma_0+\Delta_{\mathcal B},
 \qquad
 \Delta_{\mathcal B}
 =\langle r,(I+UA^{-1}U^*)^{-1}r\rangle.}        \tag{26}
\]

It also gives the signed determinant identities

\[
 \boxed{
 \sigma_+
 =\frac{\det H_+}{\det(A+U^*U)},
 \qquad
 \Delta_{\mathcal B}
 =\frac{\det H_+}{\det(A+U^*U)}
 -\frac{\det H_0}{\det A}.}                     \tag{27}
\]

Define the augmented maps

\[
 \widetilde U y=(A^{1/2}y,Uy),
 \qquad
 \widetilde r=(0,r)
 \quad\text{in}\quad
 \mathbb C^{M-1}\oplus\mathcal Y_{\mathcal B}.   \tag{27a}
\]

### Theorem 3 — Exact augmented conditional determinant

\[
 \boxed{
 \begin{aligned}
 \Delta_{\mathcal B}
 &=\mathrm{dist}(
     \widetilde r,\mathrm{ran}\,\widetilde U)^2\\
 &=\frac{
 \det\begin{pmatrix}
 A+U^*U&U^*r\\
 r^*U&\|r\|^2
 \end{pmatrix}}
 {\det(A+U^*U)}.
 \end{aligned}}                                  \tag{27b}
\]

#### Proof

The Gram matrix of the old augmented columns
\((A^{1/2}e_j,Ue_j)\) is \(A+U^*U\); their cross column with
\((0,r)\) is \(U^*r\), and the new-column norm is \(\|r\|^2\).
Moreover,

\[
 \mathrm{dist}(
 \widetilde r,\mathrm{ran}\,\widetilde U)^2
 =\min_y\{\|A^{1/2}y\|^2+\|r-Uy\|^2\}
 =\Delta_{\mathcal B},                            \tag{27c}
\]

where the final equality is (29) after \(y\mapsto-y\). Applying the
Schur determinant identity of Theorem 2 to these augmented columns proves
(27b). \(\square\)

Thus the exact crossing condition has the finite determinant form

\[
 \boxed{
 \frac{
 \det\begin{pmatrix}
 A+U^*U&U^*r\\
 r^*U&\|r\|^2
 \end{pmatrix}}
 {\det(A+U^*U)}
 >-\sigma_0.}                                    \tag{27d}
\]

### Theorem 4 — Sharp observation-only lower bound

\[
 \boxed{
 \Delta_{\mathcal B}\ge d_M(\mathcal B)^2.}      \tag{28}
\]

The lower bound is optimal among bounds depending only on \((U,v)\) and
valid uniformly for every positive preceding block \(A\).

#### Proof

For \(y\in\mathbb C^{M-1}\), completion of the old signed square gives

\[
 \Delta_{\mathcal B}
 =\min_y\{\langle y,Ay\rangle+\|r+Uy\|^2\}.       \tag{29}
\]

Dropping the nonnegative first term and using \(r=v-Ua\) yields

\[
 \Delta_{\mathcal B}
 \ge\min_y\|v-Ua+Uy\|^2
 =\min_b\|v-Ub\|^2
 =d_M(\mathcal B)^2.                             \tag{30}
\]

For optimality, fix \(U,v\), fix any \(a\), take
\(A_\varepsilon=\varepsilon I\), and set
\(c_\varepsilon=A_\varepsilon a\). Then \(r=v-Ua\) is fixed and

\[
 \Delta_\varepsilon
 =\langle r,(I+\varepsilon^{-1}UU^*)^{-1}r\rangle. \tag{31}
\]

The finite-dimensional range of \(U\) is closed. On
\(\mathrm{ran}\,U\), the operator in (31) tends strongly to zero; on
\(\ker U^*\), it is the identity. Therefore

\[
 \Delta_\varepsilon\longrightarrow
 \|P_{\ker U^*}r\|^2
 =\mathrm{dist}(v,\mathrm{ran}\,U)^2
 =d_M(\mathcal B)^2.                             \tag{32}
\]

No uniformly larger observation-only lower bound is possible. \(\square\)

### Corollary 5 — Finite crossing criteria

Since \(A+U^*U\succ0\), the enlarged \(M\)-mode head is strictly positive
if and only if

\[
 \boxed{\Delta_{\mathcal B}>-\sigma_0.}          \tag{33}
\]

The pure literal-observation condition

\[
 \boxed{
 \frac{\det G_{\mathcal B}^{(M)}}
      {\det G_{\mathcal B}^{(M-1)}}
 >-\sigma_0}                                     \tag{34}
\]

is sufficient by (20) and (28).

For disjoint finite blocks
\(\mathcal B_1,\ldots,\mathcal B_R\), update the signed regression after
each block and denote the exact adaptive gains by \(\Delta_j\).
Telescoping gives

\[
 \sigma_R=\sigma_0+\sum_{j=1}^R\Delta_j.         \tag{35}
\]

Thus

\[
 \boxed{\sum_{j=1}^R\Delta_j>-\sigma_0}          \tag{36}
\]

is necessary and sufficient for crossing at that finite stage, whereas

\[
 \boxed{
 \sum_{j=1}^R
 \frac{\det G_{\mathcal B_j}^{(M)}}
      {\det G_{\mathcal B_j}^{(M-1)}}
 >-\sigma_0}                                     \tag{37}
\]

is sufficient. Each ratio in (37) is independent of the adaptive signed
regression at the start of its block.

The strongest observation-only certificate uses the union
\(\mathcal B=\bigcup_{j\le R}\mathcal B_j\). The direct-sum distance uses
one common regression vector, so

\[
 \begin{aligned}
 d_M(\mathcal B)^2
 &=\min_b\sum_{j=1}^R\|v_j-U_jb\|^2\\
 &\ge\sum_{j=1}^R\min_b\|v_j-U_jb\|^2
 =\sum_{j=1}^Rd_M(\mathcal B_j)^2.               \tag{38}
 \end{aligned}
\]

The union determinant therefore retains at least as much cross-prime
complementarity as separately regressed block determinants.

## 4. Gram--Andreief and Cauchy--Binet formulas

Introduce the disjoint-union observation space

\[
 \Omega_{\mathcal B}
 =\bigsqcup_{n\in\mathcal B}(\{n\}\times\mathbb R)              \tag{39}
\]

with positive measure

\[
 d\nu_{\mathcal B}(n,x)
 =w_nK(x)K(x-u_n)\,dx.                            \tag{40}
\]

Put

\[
 F_j(n,x)=\phi_j(x)-\phi_j(x-u_n).                \tag{41}
\]

Then, for \(d=M-1,M\),

\[
 (G_{\mathcal B}^{(d)})_{ij}
 =\int_{\Omega_{\mathcal B}}
 \overline{F_i(\omega)}F_j(\omega)\,
 d\nu_{\mathcal B}(\omega).                      \tag{42}
\]

All integrals are absolutely convergent by theta decay and (14).

### Theorem 6 — Exact Gram--Andreief formula

For \(d=M-1\) or \(d=M\),

\[
 \boxed{
 \det G_{\mathcal B}^{(d)}
 =\frac1{d!}
 \int_{\Omega_{\mathcal B}^d}
 \left|\det[F_j(\omega_i)]_{i,j=1}^d\right|^2
 \prod_{i=1}^d d\nu_{\mathcal B}(\omega_i).}     \tag{43}
\]

#### Proof

Expand the determinant and its conjugate:

\[
 \sum_{\pi,\tau\in S_d}
 \mathrm{sgn}(\pi)\mathrm{sgn}(\tau)
 \prod_{i=1}^d
 F_{\pi(i)}(\omega_i)\overline{F_{\tau(i)}(\omega_i)}.          \tag{44}
\]

Fubini applies by absolute integrability. Integrating each \(\omega_i\)
produces Gram entries. For each relative permutation
\(\tau\pi^{-1}\), there are \(d!\) choices of \(\pi\); the prefactor
cancels them and leaves the Leibniz expansion of
\(\det G_{\mathcal B}^{(d)}\). \(\square\)

Expanding the disjoint union in (43) gives the continuous Cauchy--Binet
formula

\[
\boxed{
\begin{aligned}
 \det G_{\mathcal B}^{(d)}
 ={}&\frac1{d!}
 \sum_{(n_1,\ldots,n_d)\in\mathcal B^d}
 \left(\prod_{i=1}^dw_{n_i}\right)\\
 &\times\int_{\mathbb R^d}
 \left|\det\!\left[
 \phi_j(x_i)-\phi_j(x_i-u_{n_i})
 \right]_{i,j=1}^d\right|^2\\
 &\hspace{18mm}\times
 \prod_{i=1}^dK(x_i)K(x_i-u_{n_i})\,dx_i .
\end{aligned}}                                   \tag{45}
\]

Repeated prime powers among the \(n_i\) are allowed: one displacement
atom has an infinite-dimensional \(x\)-feature and can contribute more
than one independent row.

Combining (20), (43), and the factorials yields

\[
 \boxed{
 d_M(\mathcal B)^2
 =\frac1M\,
 \frac{\displaystyle
 \int_{\Omega_{\mathcal B}^M}
 |\det[F_j(\omega_i)]_{i,j\le M}|^2\,d\nu_{\mathcal B}^M}
 {\displaystyle
 \int_{\Omega_{\mathcal B}^{M-1}}
 |\det[F_j(\omega_i)]_{i,j<M}|^2\,d\nu_{\mathcal B}^{M-1}}.}   \tag{46}
\]

For a finite quadrature with observation points
\(\omega_1,\ldots,\omega_R\), positive masses
\(\alpha_1,\ldots,\alpha_R\), and sample matrix
\(Z_{\ell j}=F_j(\omega_\ell)\), ordinary Cauchy--Binet gives

\[
 \boxed{
 \det(Z^*\mathrm{diag}(\alpha)Z)
 =\sum_{\substack{I\subset\{1,\ldots,R\}\\|I|=d}}
 \left(\prod_{\ell\in I}\alpha_\ell\right)
 |\det Z_I|^2.}                                  \tag{47}
\]

Indeed, apply Cauchy--Binet to
\((\mathrm{diag}\,\sqrt\alpha\,Z)^*
(\mathrm{diag}\,\sqrt\alpha\,Z)\). Formula (47) is useful for
outward-interval certificates; (43)--(46) are the exact continuum
identities.

## 5. Basis and normalization audit

There is no hidden orthonormality assumption in (20).

* Replacing the old basis by
  \((\phi_1,\ldots,\phi_{M-1})S\), with
  \(S\in GL_{M-1}(\mathbb C)\), multiplies both determinants in (20) by
  \(|\det S|^2\).
* Replacing \(\phi_M\) by \(\phi_M+v_0\), \(v_0\in V_{M-1}\), is a
  determinant-one triangular basis change and leaves both the distance
  and the ratio unchanged.
* Replacing \(\phi_M\) by \(\alpha\phi_M\) multiplies
  \(d_M(\mathcal B)^2\), the determinant ratio, and
  \(\sigma_0\) by \(|\alpha|^2\). Hence (34) is invariant.

If a dimensionless quantity is preferred, let \(N_M\) be the ambient norm
Gram and define

\[
 \nu_M
 =\mathrm{dist}_{\mu_K}(\phi_M,V_{M-1})^2
 =\frac{\det N_M}{\det N_{M-1}}.                 \tag{48}
\]

Then

\[
 \boxed{
 \widehat d_M(\mathcal B)^2
 :=\frac{d_M(\mathcal B)^2}{\nu_M}
 =\frac{
 \det G_{\mathcal B}^{(M)}\det N_{M-1}}
 {\det G_{\mathcal B}^{(M-1)}\det N_M}.}         \tag{49}
\]

The normalized crossing condition is

\[
 \widehat d_M(\mathcal B)^2
 >-\frac{\sigma_{M,X_0}}{\nu_M}.                 \tag{50}
\]

Equations (49)--(50), rather than an extra norm factor inserted into
(20), are the correct normalized formulation.

## 6. Remaining quantitative statement

The algebraic and sampling parts of the proposed mechanism are complete.
The force-bearing finite target is the augmented inequality

\[
 \boxed{
 \frac{
 \det\begin{pmatrix}
 A+U^*U&U^*r\\
 r^*U&\|r\|^2
 \end{pmatrix}}
 {\det(A+U^*U)}
 >-\sigma_{M,X_0}.}                              \tag{51}
\]

Unlike the prime-only ratio, (51) is not a lossy sufficient condition: it
is exactly \(\Delta_{\mathcal B}>-\sigma_{M,X_0}\). The matrix uses the
already-positive preceding prime--Gamma geometry and the new literal
prime block jointly. The remaining task is to prove that, for every row
of the cofinal mode exhaustion, some finite ordinary-prime block satisfies
(51). The positive-measure prime-only determinant remains available as a
secondary certificate, but the diagnostic in Section 7 shows that it is
not quantitatively strong enough to be the universal hypothesis.

## 7. Semantic audit and the augmented-determinant correction

The algebra in this note has identifiable predecessors inside the project,
but its literal joint-prime application is not a duplicate.

* `E72_117_GRAM_DETERMINANT_ORTHOGONALITY.md` already proves the generic
  identity
  \(
  \mathrm{dist}(y,\mathrm{ran}\,U)^2
  =\det G[U,y]/\det G[U]
  \).
  Thus the Schur-to-distance algebra is not new by itself.
* `199_COMPARATIVE_INNOVATION_MARGIN_GATE.md` already formulates a signed
  Schur innovation and warns that proving its sign after inserting the
  target diagonal is circular. It does not contain the physical theta
  displacement bank or the Kalman update.
* Phase 46 proves conditional Gram--Vandermonde lower bounds for finite
  systems of zero exponentials. Those bounds depend on zero gaps and
  degenerate at unresolved clusters; they are not ordinary-prime block
  gains.
* Documents 106.73--106.74 already show that nonvanishing of a
  high-dimensional prime sampling determinant is insufficient: the theta
  envelope and mode-Gram conditioning must be compared on the same scale.
* Documents 106.76 and 106.78--106.79 prove finite literal observability
  and the exact adaptive Kalman gain. What is specific here is the
  observation-only lower bound for a joint literal block and its
  positive-measure determinant representation.

The observation-only certificate (34), although exact as a sufficient
condition, is too strong to be promoted to the main closure target. The
diagnostic

```text
python3 tools/joint_block_innovation_diagnostic.py \
  --dx 0.0005 --span 12 --heads 1,2,3,5,19
```

gives the following representative rows. These are floating-point
diagnostics, not interval certificates.

\[
\begin{array}{c|c|r|r|r}
M&X_0\to X_1&\sigma_{M,X_0}&d_M(\mathcal B)^2&\Delta_{\mathcal B}\\ \hline
4&1\to19&-2.105\cdot10^{-1}&1.628\cdot10^{-2}&4.137\cdot10^{-1}\\
7&2\to19&-1.343\cdot10^{-2}&1.786\cdot10^{-5}&8.765\cdot10^{-2}\\
12&3\to19&-2.290\cdot10^{-2}&1.123\cdot10^{-7}&5.111\cdot10^{-2}
\end{array}                                                    \tag{52}
\]

In all three rows the exact block gain crosses, whereas the pure
observation distance does not pay the initial deficit. The loss has a
precise geometric source. The pure distance retains only the component of
the observation residual perpendicular to \(\mathrm{ran}\,U\). The
exact Kalman gain also retains the parallel component, with its cost
measured by the already-positive preceding signed block \(A\). That
parallel component dominates in (52).

The exact augmented determinant (27b) preserves that parallel component.
It combines the positive preceding prime--Gamma block and the new literal
prime sensors before taking the Schur complement. The remaining target is
therefore (51), or the equivalent adaptive sum over consecutive blocks.
The pure Gram ratio (34) remains a valid optional certificate, but the
diagnostic shows that it is not the right universal hypothesis.
