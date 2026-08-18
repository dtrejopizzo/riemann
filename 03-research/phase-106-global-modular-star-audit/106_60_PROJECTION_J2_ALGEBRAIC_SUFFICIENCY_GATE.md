# 106.60 — Projection--$j_2$ algebraic sufficiency gate

## Purpose and verdict

The local Evans reduction of 106.58 leaves the joint coherence estimate

\[
 c_K\int_{\mathbb R}\frac{K(x)}{h(x)}\|\mathbf B_P(x)\|^2\,dx
 \geq \frac12\mathrm{Tr}(PL).                 \tag{1}
\]

The proposed next move was to combine, without separating them,

* projection idempotence;
* the reducing equation $L_x\Pi=L_y\Pi$;
* annihilation of the constant and Riemann-radical modes; and
* the literal positive arithmetic jet
  $j_2=\delta\Lambda+\Lambda*\Lambda\geq0$.

This note performs the corresponding algebraic audit.  It proves four
facts.

1. Once the reducing equation is inserted, (1) is exactly the spectral
   polynomial trace
   \(\sum_j\lambda_j(\lambda_j-1/2)\).  Idempotence does not leave an
   additional positive term.
2. The most direct polarized lift of the literal $j_2$ coefficients is
   indefinite already on the ordinary tower \(\{p,p^2\}\).
3. There is a normalized three-state reversible generator satisfying all
   the abstract projection, commutation and radical-annihilation identities,
   but having cluster curvature \(-1/18\).
4. In the literal Riemann system, the exact threshold radical forces every
   independent positive $j_2$-translation energy to be cancelled by a
   signed theta--Gamma--polar term.

Thus the listed identities do not prove (1).  This is a gate for an
*algebraic* $j_2$ closure, not a counterexample to (1) for the ordinary
primes.  A surviving proof must establish a genuinely global, radically
shorted theta-placement inequality.  It cannot obtain the sign by adding an
independent positive $j_2$ square.

## 1. Exact collapse on a reducing feature

Let $P$ be a finite-rank spectral projection of the full generator $L$,
and let \(q_1,\ldots,q_m\) be an orthonormal eigenbasis of its range:

\[
 Lq_j=\lambda_jq_j,
 \qquad 0<\lambda_j<\frac12.                         \tag{2}
\]

Put

\[
 \mathbf Q(x)=(q_1(x),\ldots,q_m(x)),
 \qquad
 \boldsymbol\Lambda_P=\mathrm{diag}
   (\lambda_1,\ldots,\lambda_m).                    \tag{3}
\]

The exact current equation 106.49(9) is

\[
 \frac{c_K}{h(x)}\mathbf B_P(x)
 =L\mathbf Q(x)
 =\mathbf Q(x)\boldsymbol\Lambda_P.                 \tag{4}
\]

Since

\[
 d\mu_K(x)=\frac{h(x)K(x)}{c_K}\,dx,                \tag{5}
\]

substitution of (4) gives

\[
\begin{aligned}
 c_K\int\frac K h\|\mathbf B_P\|^2\,dx
 &=\int\|\mathbf Q(x)\boldsymbol\Lambda_P\|^2
       \,d\mu_K(x)\\
 &=\sum_{j=1}^m\lambda_j^2.                         \tag{6}
\end{aligned}
\]

Orthonormality gives, independently,

\[
 \frac12\mathrm{Tr}(PL)
 =\frac12\sum_{j=1}^m\lambda_j.                    \tag{7}
\]

Consequently (1) is exactly

\[
 \boxed{
 \sum_{j=1}^m\lambda_j(\lambda_j-1/2)\geq0.}        \tag{8}
\]

The projection kernel

\[
 \Pi(x,y)=\langle\mathbf Q(x),\mathbf Q(y)\rangle  \tag{9}
\]

satisfies

\[
 \int\Pi(x,z)\Pi(z,y)\,d\mu_K(z)=\Pi(x,y),         \tag{10}
\]

but (10) is precisely the kernel form of the orthonormality already used in
(6).  Likewise,

\[
 L_x\Pi=L_y\Pi                                      \tag{11}
\]

is the kernel form of (2).  Therefore inserting (10)--(11) into a cyclic
triangle expansion can rearrange (8), but cannot create a new numerical
surplus.  Any claimed surplus has to come from an additional arithmetic
inequality, not from projection algebra itself.

## 2. Literal one-tower obstruction to the polarized $j_2$ lift

For every ordinary prime $p$,

\[
 \Lambda(p^a)=\log p,
 \qquad
 j_2(p^a)=(2a-1)(\log p)^2.                          \tag{12}
\]

Consider the natural polarized kernel

\[
 \mathcal H(m,n)=j_2(mn)-\Lambda(m)\Lambda(n).       \tag{13}
\]

On the literal indices $p,p^2$, division by \((\log p)^2\) gives

\[
 \frac1{(\log p)^2}
 \begin{pmatrix}
 \mathcal H(p,p)&\mathcal H(p,p^2)\\
 \mathcal H(p^2,p)&\mathcal H(p^2,p^2)
 \end{pmatrix}
 =
 \begin{pmatrix}2&4\\4&6\end{pmatrix}.             \tag{14}
\]

For $v=(2,-1)^T$,

\[
 \boxed{
 v^*\mathcal Hv=-2(\log p)^2<0.}                    \tag{15}
\]

Thus $j_2(n)\geq0$ is coefficient positivity, not positivity of the
polarized two-index operator required to control arbitrary cluster
increments.  The obstruction in (15) uses a literal ordinary prime and no
Euler countermodel.

## 3. Minimal reducing-projection falsifier

The next model shows that the projection constraints do not repair the
missing sign at an abstract level.

Let

\[
 \mathcal H=\mathbb C^3,
 \qquad
 \langle f,g\rangle_\mu
 =\frac13\sum_{i=1}^3\overline{f_i}g_i,               \tag{16}
\]

and define the reversible path generator

\[
 L=\frac16
 \begin{pmatrix}
 1&-1&0\\
 -1&2&-1\\
 0&-1&1
 \end{pmatrix}.                                     \tag{17}
\]

Its normalized eigenvectors are

\[
 \mathbf1=(1,1,1),
 \qquad
 q=\sqrt{\frac32}(1,0,-1),
 \qquad
 r=\frac1{\sqrt2}(1,-2,1),                           \tag{18}
\]

and direct multiplication gives

\[
 L\mathbf1=0,
 \qquad Lq=\frac16q,
 \qquad Lr=\frac12r.                                \tag{19}
\]

All three vectors have norm one and are mutually orthogonal for (16).  Let
$P=|q\rangle\langle q|$, and write its kernel relative to the measure
$\mu_i=1/3$ as

\[
 \Pi(i,j)=q_i\overline{q_j}.                         \tag{20}
\]

Then

\[
\begin{aligned}
 \sum_{k=1}^3\Pi(i,k)\Pi(k,j)\mu_k&=\Pi(i,j),\\
 L_i\Pi(i,j)=L_j\Pi(i,j)&=\frac16\Pi(i,j),\\
 P\mathbf1=0,\qquad Pr&=0.                          \tag{21}
\end{aligned}
\]

Thus (21) gives exact idempotence, reduction and annihilation of both the
constant and an exact $1/2$-threshold radical.  Nevertheless,

\[
\boxed{
 \mathrm{Tr}\,P(L^2-\tfrac12L)
 =\frac16\left(\frac16-\frac12\right)
 =-\frac1{18}.}                                     \tag{22}
\]

The current calculation is equally explicit.  With jump rates $1/6$ on
the two unoriented path edges,

\[
 B(i)=\sum_jJ_i(j)\{q_i-q_j\}=(Lq)_i=\frac16q_i.    \tag{23}
\]

Hence

\[
 \sum_i\mu_i|B(i)|^2=\frac1{36},
 \qquad
 \frac12\langle q,Lq\rangle_\mu=\frac1{12},        \tag{24}
\]

so the star-current coherence inequality fails by exactly $1/18$.

This model is not asserted to be Riemann's generator.  Its role is precise:
any proof whose only inputs are positivity of jump rates, (10)--(11), and
radical annihilation would apply to (17), and is therefore false.  The
literal theta placement must enter in a way which has no analogue in
(17).

## 4. Literal Riemann saturation of the $j_2$ cells

There is also an internal falsifier to treating the $j_2$ cells as an
independent positive remainder.  Let

\[
 \widetilde r_1=\frac{K''}{K}
 -\mu_K\!\left(\frac{K''}{K}\right).                 \tag{25}
\]

The exact radical identity of 106.41 is

\[
 L\widetilde r_1=\frac12\widetilde r_1.              \tag{26}
\]

Therefore the rank-one threshold projection $P_{r_1}$ satisfies

\[
 \mathrm{Tr}\,P_{r_1}(L^2-\tfrac12L)=0.         \tag{27}
\]

Conjugate to $L^2(\mathbb R,dx)$ by the exact ground-state unitary and
write $f=\mathcal U\widetilde r_1$.  Then $f\neq0$ and
$f\in L^2(\mathbb R)$.  At a finite Euler cutoff define the positive
centered $j_2$ energy

\[
 \mathcal J_{2,N}(f)
 =\frac12\sum_{2\leq n\leq N}
 \frac{j_2(n)}{\sqrt n}
 \|f-S_{\log n}f\|_2^2.                             \tag{28}
\]

For every $N\geq2$, the $n=2$ summand is strictly positive.  Indeed,

\[
 j_2(2)=(\log2)^2>0,                                 \tag{29}
\]

and $f=S_{\log2}f$ would make $f$ a nonzero periodic $L^2(\mathbb R)$
function, which is impossible.  Thus

\[
 \boxed{\mathcal J_{2,N}(f)>0\qquad(N\geq2).}        \tag{30}
\]

Comparison of (27) and (30) proves that no exact identity can have the
form

\[
 L(L-\tfrac12)=\text{independent positive }j_2\text{ cell square}
 +\text{nonnegative remainder}                       \tag{31}
\]

on the literal Riemann domain.  The intermediate-position defect and the
Gamma--polar--threshold terms must contribute a negative quantity which
cancels (28) on every radical vector.  This is not optional bookkeeping;
it is forced by exact threshold saturation.

## 5. Consequence for the proposed closure

Equations (8), (15), (22), and (30) isolate the failure of the proposed
shortcut.

* Projection idempotence and commutation encode the spectral trace but do
  not determine its sign.
* Coefficient positivity of $j_2$ does not polarize to a positive operator.
* Abstract projection plus radical constraints admit a negative cluster.
* In the literal Riemann system, a positive $j_2$ cell energy is strictly
  positive on a vector where the complete curvature is exactly zero.

The only possible repair is to short the *complete signed joint curvature*,
not the $j_2$ piece alone.  Schematically, if $C_N$ denotes a cell map,
the radical-compatible nonnegative object is

\[
 \mathrm{dist}
 \bigl(C_Nf,\overline{C_N\mathcal R}\bigr)^2,        \tag{32}
\]

not \(\|C_Nf\|^2\).  But proving that the common-cutoff limit of (32),
together with the signed theta--Gamma--polar completion, dominates the
negative edge term is exactly the projection-alignment theorem (1).  It is
not a consequence of $j_2\geq0$.

Accordingly, the next admissible theorem must use the full nondivisible
theta indices and the central crossing channel of 106.38 inside the same
shorting operation as Gamma and the pole.  It must also fail for the model
(17) and vanish on every vector (25).  No QED for (1), and hence no RH
closure, is claimed in this note.
