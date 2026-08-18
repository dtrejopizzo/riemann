# 106.96 — Signed amplitude transfer and the Krylov gate

## Purpose and verdict

The remaining bordered-minor inequality is

\[
 \tau_{d+1}(Y)>\delta_J\tau_d(Y).                 \tag{1}
\]

This note constructs an exact signed amplitude-transfer row after the
complete radical anti-short.  The construction retains one common old-mode
regression and produces the requested determinant-amplitude identity before
the final Cauchy--Schwarz estimate.

The construction does **not** by itself prove contractivity.  The simplest
trial row is exactly the two-moment matched filter already derived in
106.83--106.85, and it can fail even when (1) holds.  The correct flexible
successor is a nested Krylov hierarchy.  Its first level is the matched
filter, it increases monotonically, and it recovers the exact adaptive gain
after finitely many levels on every fixed finite row.  The remaining
arithmetic theorem is to prove that one explicitly controlled level exceeds
\(\delta_J\) using the literal theta translations and von Mangoldt weights.

## 1. The finite observation row

Put \(m=M-1\), \(d=m+J\), and let

\[
 \mathcal Y_Y=
 \bigoplus_{\substack{X<n=p^k\leq Y}}L^2(\mathbb R,dx).
\]

For a multiplier \(q\), define

\[
 (D_Yq)_n(x)=
 \left({\Lambda(n)\over\sqrt n}K(x)K(x-\log n)\right)^{1/2}
 \{q(x)-q(x-\log n)\}.                           \tag{2}
\]

Use the notation

\[
 A=\widehat A\succ0,\qquad
 U=D_Y|_{V_{M-1}},\qquad
 W=D_Y|_{\mathcal R_J},\qquad
 v=D_Yq_J^*.                                      \tag{3}
\]

In

\[
 \mathcal H_Y=\mathbb C^m\oplus\mathcal Y_Y
\]

the nuisance and new columns are

\[
 \begin{aligned}
 f_i&=(A^{1/2}e_i,Ue_i),&&1\leq i\leq m,\\
 f_{m+a}&=(0,Wr_a),&&1\leq a\leq J,\\
 f_*&=(0,v).
 \end{aligned}                                    \tag{4}
\]

Their Gram determinants are \(\tau_d(Y)\) and \(\tau_{d+1}(Y)\).

## 2. Exact one-particle amplitude transfer

The inner product is conjugate-linear in the first argument.  For raw
determinants \(\Delta_r\), equip the alternating coordinate space with

\[
 \|\Phi\|_{[r]}^2={1\over r!}
 \int_{\Omega_Y^r}|\Phi|^2\,d\nu_Y^r.             \tag{5}
\]

Then Andreief gives

\[
 \|\Delta_d\|_{[d]}^2=\tau_d(Y),\qquad
 \|\Delta_{d+1}\|_{[d+1]}^2=\tau_{d+1}(Y).       \tag{6}
\]

### Theorem 1 — Trial signed transfer row

Let \(\psi\in\ker W^*\) and put

\[
 \beta_\psi=\langle\psi,v\rangle\ne0,
 \qquad
 g_\psi=(-A^{-1/2}U^*\psi,\psi).                 \tag{7}
\]

Define

\[
 h_\psi={(-1)^d\sqrt{\delta_J}\over
                 \overline{\beta_\psi}}g_\psi,
 \qquad H_\psi=\overline{h_\psi}.               \tag{8}
\]

Then

\[
 \boxed{
 \int H_\psi(\omega)
 \Delta_{d+1}(\omega,\boldsymbol\omega)\,d\nu_Y(\omega)
 =\sqrt{\delta_J}\Delta_d(\boldsymbol\omega).} \tag{9}
\]

Moreover the corresponding exterior contraction has norm

\[
 \boxed{
 \|T_{H_\psi}\|_{\rm op}^2
 =\delta_J\,{\displaystyle
 \|\psi\|^2+\|A^{-1/2}U^*\psi\|^2
 \over\displaystyle |\langle\psi,v\rangle|^2}.} \tag{10}
\]

Consequently the strict inequality

\[
 |\langle\psi,v\rangle|^2>
 \delta_J\{\|\psi\|^2+\|A^{-1/2}U^*\psi\|^2\} \tag{11}
\]

implies (1).

#### Proof

For every old column,

\[
 \langle g_\psi,f_i\rangle
 =-\langle U^*\psi,e_i\rangle+\langle\psi,Ue_i\rangle=0.
\]

For a radical column,

\[
 \langle g_\psi,f_{m+a}\rangle
 =\langle W^*\psi,r_a\rangle=0.
\]

Finally \(\langle g_\psi,f_*\rangle=\beta_\psi\), so (8) gives
\(\langle h_\psi,f_*\rangle=(-1)^d\sqrt{\delta_J}\).  Laplace
expansion of \(\Delta_{d+1}\) in its first row proves (9): all nuisance
cofactors vanish after integration, and the last cofactor has sign
\((-1)^d\).

The integral operator in (9) is contraction by the one-particle vector
\(h_\psi\) on the exterior power.  With normalization (5), its operator
norm is \(\|h_\psi\|\).  Formula (10) follows from (7)--(8).  Taking norms
in (9), using (6), and then (11), gives

\[
 \delta_J\tau_d(Y)
 \leq\|T_{H_\psi}\|_{\rm op}^2\tau_{d+1}(Y)
 <\tau_{d+1}(Y).
\]

This proves the theorem. \(\square\)

The vector in (7) is the required single common regression.  No
prime-by-prime regression is performed.  Mean periodicity may be used on
the zero-mode columns entering \(U\) and \(v\), but the radical condition
is imposed separately by \(W^*\psi=0\), in agreement with 106.94.

## 3. Exact gain and the matched-filter loss

Let

\[
 \Pi=I-W(W^*W)^{-1}W^*,\qquad
 z=\Pi v,\qquad
 B=\Pi UA^{-1}U^*\Pi.                            \tag{12}
\]

On \(\operatorname {ran}\Pi\), the exact finite adaptive gain is

\[
 \boxed{G_Y=\langle z,(I+B)^{-1}z\rangle.}       \tag{13}
\]

The choice \(\psi=z\) in Theorem 1 gives

\[
 Q_1={R^2\over R+L},\qquad
 R=\|z\|^2,qquad L=\langle z,Bz\rangle,         \tag{14}
\]

which is precisely the matched-filter bound of 106.83 and the sharp
two-moment Stieltjes bound of 106.85.  Thus

\[
 Q_1>\delta_J                                      \tag{15}
\]

is sufficient, but it is not equivalent to (1).

Let \(d\nu_z(t)=d\langle z,E_B(t)z\rangle/R\) and
\(\bar t=\int t\,d\nu_z=L/R\).  Direct algebra gives the exact loss

\[
 \boxed{
 G_Y-Q_1
 =R\int { (t-\bar t)^2
          \over(1+\bar t)^2(1+t)}\,d\nu_z(t).}   \tag{16}
\]

Hence equality holds exactly when the spectral measure seen by \(z\) is
supported at one point.

### Counterexample 2 — MF may fail after the true crossing

Take no radical, \(A=1\), \(U=(0,3)^{\mathsf T}\),
\(z=v=(1,1)^{\mathsf T}\), and \(\delta=1\).  Then

\[
 B=\operatorname {diag}(0,9),\qquad R=2,\qquad L=9,
\]

so

\[
 Q_1={4\over11}<1.
\]

But

\[
 G_Y=1+{1\over10}={11\over10}>1.
\]

Equivalently, the augmented Gram matrix is

\[
 \begin{pmatrix}10&3\\3&2\end{pmatrix},
\]

whose Schur gain is \(11/10\); after subtracting the unit border, the
resulting determinant is \(1>0\).  Thus failure of MF cannot close the
route negatively.

## 4. The noncircular Krylov hierarchy

Put

\[
 m_j=\langle z,B^jz\rangle\qquad(j\geq0).         \tag{17}
\]

For \(k\geq1\), let

\[
 \mathcal K_k=\operatorname {span}
 \{z,Bz,\ldots,B^{k-1}z\}.                       \tag{18}
\]

Define

\[
 H_k=[m_{i+j}+m_{i+j+1}]_{i,j=0}^{k-1},
 \qquad b_k=(m_0,\ldots,m_{k-1})^{\mathsf T},     \tag{19}
\]

and, using the Moore--Penrose inverse if the Krylov family is dependent,

\[
 \boxed{Q_k=b_k^*H_k^\dagger b_k.}               \tag{20}
\]

### Theorem 3 — Monotone finite exactness

For every \(k\),

\[
 \boxed{
 Q_k=sup_{0\ne\psi\in\mathcal K_k}
 { |\langle\psi,z\rangle|^2
  \over\langle\psi,(I+B)\psi\rangle}.}          \tag{21}
\]

Consequently

\[
 Q_1\leq Q_2\leq\cdots\leq G_Y.                 \tag{22}
\]

If the spectral measure of \(B\) seen by \(z\) has \(r\) distinct
support points, then

\[
 \boxed{Q_r=G_Y.}                                 \tag{23}
\]

In particular, \(r\leq\operatorname {rank}B+1\leq M\).

#### Proof

For \(\psi=\sum_{i<k}c_iB^iz\), its response to \(z\) is
\(c^*b_k\), while its \((I+B)\)-norm is \(c^*H_kc\).  The finite
Riesz formula proves (20)--(21).  Nestedness of the Krylov spaces gives
(22).  On the finite spectral support, interpolate the function
\((1+t)^{-1}\) by a polynomial of degree at most \(r-1\).  Hence
\((I+B)^{-1}z\in\mathcal K_r\), and equality in the global Riesz formula
gives (23). \(\square\)

For \(k=1\), (20) is exactly (14).  For \(k=2\), put

\[
 a=m_0+m_1,\qquad b=m_1+m_2,\qquad c=m_2+m_3.
\]

Then

\[
 \boxed{
 Q_2={c m_0^2-2b m_0m_1+a m_1^2\over ac-b^2}.}  \tag{24}
\]

When \(ac>b^2\), its improvement over MF is

\[
 \boxed{
 Q_2-Q_1=
 { (m_0m_2-m_1^2)^2
  \over
  (m_0+m_1)^2
  \left[m_2+m_3-{(m_1+m_2)^2\over m_0+m_1}\right]}.}          \tag{25}
\]

Thus the second signed filter captures exactly the spectral-variance
piece which MF discards.  In Counterexample 2, \(Q_2=G_Y=11/10\).

## 5. Relation with theta packet cofactors

An orthonormal packet dictionary in \(\mathcal Y_Y\) gives a coordinate
realization of Theorem 1.  The square response matrix must include the old
positive feature block \(A^{1/2}\); otherwise it forces the tail packets to
annihilate the old modes and loses the common-regression assistance.

For a finite packet subspace \(S\subset\ker W^*\), let

\[
 K_{ij}=\langle\psi_i,(I+B)\psi_j\rangle,
 \qquad a_i=\langle\psi_i,z\rangle.               \tag{26}
\]

The best packet certificate is

\[
 \Gamma_S=a^*K^{-1}a.                            \tag{27}
\]

In a square orthonormal response matrix this is equivalently the usual
determinant/cofactor ratio.  If the packet family is not orthonormal, its
Gram matrix must remain in (26); a raw sum of squared cofactors is then
incorrect.

Midpoint theta packets expose the phases

\[
 A_n(z)=2z\sin\!\left({z\log n\over2}\right)
 +\tanh\!\left({\log n\over4}\right)
  \cos\!\left({z\log n\over2}\right),            \tag{28}
\]

and the physical strength

\[
 \beta_n\asymp\Lambda(n)n^2e^{-2\pi n}.          \tag{29}
\]

Their nonvanishing proves observability, but not contractivity: the
cofactor ratio retains the absolute scale (29).  The required estimate
must compare that scale with \(\delta_J\), not merely prove a nonzero
phase determinant.  This is the same quantitative warning established in
106.73--106.74 and 106.84.

## 6. Status of the remaining sign

The amplitude-transfer kernel is now explicit.  Its contractivity on a
fixed trial space is the finite inequality

\[
 \boxed{Q_k>\delta_J.}                            \tag{30}
\]

Every fixed \(k\) gives a genuinely noncircular sufficient certificate,
and the associated filter \(\psi=P_{k-1}(B)z\) keeps all cross-prime
phases until the final Hilbert norm.  However, using finite exactness
(23) without an independent lower estimate merely returns
\(G_Y>\delta_J\).

The new arithmetic obligation is therefore not construction of \(H_Y\),
nor MF alone, nor qualitative packet invertibility.  It is a literal
theta--Gamma--von-Mangoldt bound on the moments

\[
 m_0,m_1,m_2,m_3,\ldots                            \tag{31}
\]

which proves (30) at a controlled level before the theta envelope falls
below the deficit.  The first strictly stronger target than the already
audited MF condition is the four-moment inequality

\[
 \boxed{Q_2>\delta_J,}                            \tag{32}
\]

with \(Q_2\) given explicitly by (24).
