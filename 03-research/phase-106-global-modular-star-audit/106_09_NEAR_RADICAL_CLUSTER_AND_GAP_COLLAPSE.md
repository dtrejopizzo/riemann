# 106.09 — Near-radical clusters and conditional gap collapse

## Purpose

The variational criterion in 106.07 contains the first even spectral gap

\[
 g_L^+=\mu_{1,L}^+-\mu_{0,L}^+.
\tag{1}
\]

A natural possible closure would be to prove that this gap is bounded below
uniformly, or at least only polynomially small, and then compare the CCM
model with the ground state.  This note shows that this cannot be the correct
mechanism.

There is an unconditional family of near-radical trial spaces obtained by
cutting off Riemann's full kernel and its derivatives.  Direct estimates on
the polar--Gamma--Euler source prove that their Weil matrices are
double-exponentially small in the additive support length.  Min--max then
gives unconditional *upper* bounds for the second even and first odd
eigenvalues.  Under RH, Weil positivity supplies the missing lower bound
zero, and the actual next-even and parity gaps collapse at the same rate.

The conditional label is essential.  Without RH, a negative ground branch
may remain separated from the near-radical cluster.  Nothing below proves a
lower-gap estimate or RH.

## 1. Setting and notation

Put

\[
 a=\frac L2,\qquad \lambda=e^a.
\tag{2}
\]

Let \(QW\) be the polarized completed Riemann--Weil form in the additive
coordinate, and let \(A_L^+\) and \(A_L^-\) be its compact-form operators on
the even and odd parts of \(L^2([-a,a])\).  Write their eigenvalues in
nondecreasing order as

\[
 \mu_{0,L}^+\le \mu_{1,L}^+\le\cdots,
 \qquad
 \mu_{0,L}^-\le \mu_{1,L}^-\le\cdots.
\tag{3}
\]

Let \(K\) denote Riemann's full kernel in the additive coordinate.  Thus

\[
 \widehat K(z)=\Xi(z),
 \qquad K(-x)=K(x).
\tag{4}
\]

Choose smooth even cutoffs \(\chi_a\) satisfying

\[
 0\le\chi_a\le1,
 \qquad
 \chi_a=1\ \text{on }[-a+1,a-1],
 \qquad
 \mathrm{supp}\,\chi_a\subset[-a,a],
\tag{5}
\]

and, for every fixed \(r\ge0\),

\[
 \sup_{a\ge2}\|\chi_a^{(r)}\|_\infty<\infty.
\tag{6}
\]

Such a family is obtained by translating one fixed smooth cutoff at the two
endpoints and joining it by the constant function one in the interior.

## 2. A weighted continuity lemma for the source formula

For \(b>1/2\), define

\[
 \|f\|_{\mathcal X_b}
 :=\sum_{r=0}^2
 \sup_{x\in\mathbb R}
 e^{b|x|}(1+|x|)^3|f^{(r)}(x)|.
\tag{7}
\]

The exponent \(1/2\) in this definition is not arbitrary: the Euler atoms
at \(\log m\) have weights \(\Lambda(m)m^{-1/2}\).

### Lemma 1 — Weighted polar--Gamma--Euler continuity

For every \(b>1/2\), there is a constant \(C_b\) such that

\[
 \boxed{
 |QW(f,g)|\le C_b\|f\|_{\mathcal X_b}\|g\|_{\mathcal X_b}
 }
\tag{8}
\]

for all smooth \(f,g\) for which the right-hand side is finite.

This statement is unconditional.

#### Proof

Put

\[
 \widetilde g(x)=\overline{g(-x)},
 \qquad H=f*\widetilde g.
\tag{9}
\]

Choose \(b'\) with \(1/2<b'<b\).  Splitting the convolution at
\(|y|=|x|/2\), and differentiating under the integral, gives

\[
 \sum_{r=0}^2
 \sup_x e^{b'|x|}(1+|x|)^2|H^{(r)}(x)|
 \le C_{b,b'}\|f\|_{\mathcal X_b}\|g\|_{\mathcal X_b}.
\tag{10}
\]

We bound the three parts of the completed explicit formula.

First, the polar evaluations are controlled by

\[
 |\widehat H(\pm i/2)|
 \le\int_{\mathbb R}|H(x)|e^{|x|/2}\,dx,
\tag{11}
\]

which is finite and bounded by (10).

Second, in the Gamma term the only local singularity multiplies the
symmetric second difference

\[
 H(x)+H(-x)-2H(0)=O(x^2)
\tag{12}
\]

as \(x\to0\).  The two derivatives in (10) therefore control the origin,
while the exponential bound in (10) controls the integral at infinity.

Third, the Euler atoms satisfy

\[
\begin{aligned}
 \sum_{m\ge2}\frac{\Lambda(m)}{\sqrt m}
 \bigl(|H(\log m)|+|H(-\log m)|\bigr)
 &\le C\|H\|_{b'}
 \sum_{m\ge2}\frac{\Lambda(m)}{m^{1/2+b'}}\\
 &=C\|H\|_{b'}
 \left(-\frac{\zeta'}\zeta\right)\left(\frac12+b'\right),
\end{aligned}
\tag{13}
\]

and the last quantity is finite because \(1/2+b'>1\).  Combining
(10)--(13) proves (8).  No zero location has been used. \(\square\)

## 3. The unconditional near-radical matrix

For \(j=0,1,2\), put

\[
 K_j=\partial_x^jK,
 \qquad
 v_{j,a}=\chi_aK_j,
 \qquad
 e_{j,a}=v_{j,a}-K_j=(\chi_a-1)K_j.
\tag{14}
\]

The theta-series formula for Riemann's kernel, together with its modular
symmetry, gives, for every fixed \(r\ge0\), constants \(C_r,M_r,c_r>0\)
such that

\[
 |K^{(r)}(x)|
 \le C_r e^{M_r|x|}e^{-c_re^{2|x|}}
 \qquad (x\in\mathbb R).
\tag{15}
\]

For \(x\to+\infty\), this follows term by term from the polynomial-Gaussian
theta series

\[
 K(x)=e^{x/2}\sum_{n\ge1}P(ne^x)e^{-\pi n^2e^{2x}}
\tag{16}
\]

with a fixed polynomial \(P\); the negative half-line follows from
\(K(-x)=K(x)\).  Derivatives only change the polynomial prefactor.

Equations (5), (6), (15), and Leibniz's rule imply that, for every fixed
\(b>1/2\),

\[
 \|e_{j,a}\|_{\mathcal X_b}
 \le C_j\lambda^{M_j}e^{-c_j\lambda^2},
 \qquad j=0,1,2.
\tag{17}
\]

On the transform side,

\[
 \widehat{K_j}(z)=(iz)^j\Xi(z).
\tag{18}
\]

Thus every \(K_j\) vanishes on the complete nontrivial zero divisor.  The
absolutely convergent polarized explicit formula with one entry \(K_j\)
therefore gives the unconditional radical identity

\[
 QW(K_j,g)=0
\tag{19}
\]

for every admissible \(g\).  Expanding \(v_{j,a}=K_j+e_{j,a}\) and using
(19) twice yields

\[
 \boxed{
 QW(v_{i,a},v_{j,a})=QW(e_{i,a},e_{j,a}).
 }
\tag{20}
\]

Lemma 1 and (17) now prove the following source-side estimate.

### Theorem 2 — Unconditional near-radical matrix bound

There are constants \(C,M,c>0\) such that, for \(i,j\in\{0,1,2\}\) and all
sufficiently large \(L\),

\[
 \boxed{
 |QW(v_{i,a},v_{j,a})|
 \le \varepsilon_L,
 \qquad
 \varepsilon_L:=C\lambda^Me^{-c\lambda^2}
 =C\exp\left(\frac M2L-ce^L\right).
 }
\tag{21}
\]

No form of RH is used in this theorem.

## 4. Min--max consequences

The vectors \(K\) and \(K''\) are linearly independent.  Otherwise their
Fourier transforms would give

\[
 -z^2\Xi(z)=c\Xi(z)
\tag{22}
\]

on an open set, which is impossible.  Also \(K'\ne0\).  Since
\(v_{j,a}\to K_j\) in \(L^2(\mathbb R)\), the Gram matrix of
\(v_{0,a},v_{2,a}\) is uniformly nonsingular for large \(a\), and
\(\|v_{1,a}\|_2\) is uniformly bounded below.

It follows from (21) that, after changing \(C,M,c\) once, every unit vector
in

\[
 V_a^+=\mathrm{span}\,\{v_{0,a},v_{2,a}\}
\tag{23}
\]

has Weil Rayleigh quotient at most \(\varepsilon_L\) in absolute value, and
the same holds on the odd line

\[
 V_a^-=\mathrm{span}\,\{v_{1,a}\}.
\tag{24}
\]

### Theorem 3 — Unconditional eigenvalue upper bounds

For all sufficiently large \(L\),

\[
 \boxed{
 \mu_{1,L}^+\le\varepsilon_L,
 \qquad
 \mu_{0,L}^-\le\varepsilon_L.
 }
\tag{25}
\]

#### Proof

Apply the min--max principle to the two-dimensional even trial space (23)
and the one-dimensional odd trial space (24). \(\square\)

The inequalities in (25) are only upper bounds.  In particular, they are
compatible with \(\mu_{0,L}^+\le-c_0<0\).  This is exactly the negative
ground/near-radical separation exhibited abstractly in 106.07--106.08.

### Corollary 4 — Gap collapse under RH

Assume RH.  Then the Weil criterion gives

\[
 A_L^+\ge0,
 \qquad A_L^-\ge0
\tag{26}
\]

for every \(L\).  Consequently,

\[
 \boxed{
 0\le g_L^+
 :=\mu_{1,L}^+-\mu_{0,L}^+
 \le\varepsilon_L
 }
\tag{27}
\]

and

\[
 \boxed{
 |\mu_{0,L}^--\mu_{0,L}^+|
 \le\varepsilon_L.
 }
\tag{28}
\]

Thus, if the even state is the simple global ground state, its next-even gap
and its parity gap are both at most

\[
 C\lambda^Me^{-c\lambda^2}.
\tag{29}
\]

#### Proof

Under (26), all four eigenvalues appearing in (27)--(28) are nonnegative.
Theorem 3 gives \(0\le\mu_{1,L}^+\le\varepsilon_L\) and
\(0\le\mu_{0,L}^-\le\varepsilon_L\).  The even one-dimensional trial line
spanned by \(v_{0,a}\) also gives
\(0\le\mu_{0,L}^+\le\varepsilon_L\).  Equations (27)--(28) follow. \(\square\)

The same argument, using any fixed finite collection of even derivatives
\(K,K'',\ldots,K^{(2r)}\) and odd derivatives
\(K',K''',\ldots,K^{(2r+1)}\), places every fixed number of eigenvalues in a
near-zero cluster with the same qualitative rate.  The constants may depend
on the number of derivatives kept.

## 5. Consequence for the variational Gate B

The sharp Gate B from 106.07 is

\[
 \frac{\|k_L\|_2W_{L,B}}
 {\inf_{K_r}|\widehat k_L|}
 \left(
 \frac{R_L-\mu_{0,L}^+}{g_L^+}
 \right)^{1/2}
 \longrightarrow0.
\tag{30}
\]

Corollary 4 shows that a constant, polynomial, or ordinary exponential
lower bound for \(g_L^+\) is incompatible with the RH branch of the actual
semilocal Weil operator.  Gate B therefore cannot be closed by combining an
unscaled quasimode estimate with a coarse spectral gap.  It requires a
*relative hierarchy* in which the Rayleigh excess is smaller than the
collapsing gap after inclusion of the Paley--Wiener weight:

\[
 R_L-\mu_{0,L}^+
 =o\!\left(
 g_L^+
 \left(
 \frac{\inf_{K_r}|\widehat k_L|}
 {\|k_L\|_2W_{L,B}}
 \right)^2
 \right).
\tag{31}
\]

Theorem 2 does not provide (31).  It constructs several near-radical
directions and therefore explains why selection of one of them is harder,
not easier.

There is also no direct Davis--Kahan comparison with the unperturbed prolate
operator.  The CCM model is a nontrivial linear combination of two prolate
eigenfunctions with distinct prolate eigenvalues, and the map used to form
the semilocal model is not a unitary intertwiner.  Hence the model is not a
ground eigenvector of a stated reference operator to which a standard
operator-norm perturbation theorem could be applied.

## 6. Binding status

The source estimates settle the following distinction.

- **Unconditional:** the truncated Riemann-kernel derivative spaces have
  Weil matrices \(O(\lambda^Me^{-c\lambda^2})\), and therefore
  \(\mu_{1,L}^+\) and \(\mu_{0,L}^-\) have upper bounds of that size.
- **Conditional on RH:** positivity turns those upper bounds into a
  near-zero spectral cluster and forces the next-even and parity gaps to
  collapse.
- **Not proved:** a lower bound for the ground eigenvalue, identification of
  the CCM model with the least branch, the relative hierarchy (31), or the
  global curvature limit.

The gap route is therefore closed in its coarse form.  The remaining global
problem is still branch selection at a scale finer than the entire
near-radical cluster.  No statement in this document proves RH.
