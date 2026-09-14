# P121 -- the common parabolic lift of the global Green phase

## Status

This note proves an exact `U(1,1)` lift of the scalar finite-window Green
multiplier.  All local relative Euler phases and the quarter-Gamma phase act
through one square-zero generator.  Their product is therefore additive,
not multiplicative, in the singular coordinate, and its Krein
Wigner--Smith connection recovers the complete multiplier `A_T` exactly.

The construction removes the artificial accumulation of the common
`k=0` Tate pole in the scalar Euler product.  It does not prove F2: the
nonzero periodic pole lattices become nontrivial unipotent monodromies.  F2
is precisely the assertion that the equality-state section has zero
coefficient against those monodromies.

## 1. A universal parabolic generator

Put

\[
 J=\begin{pmatrix}1&0\\0&-1\end{pmatrix},\qquad
 N=\begin{pmatrix}i&1\\1&-i\end{pmatrix}.          \tag{1.1}
\]

Direct multiplication gives

\[
 N^2=0,\qquad N^*J+JN=0.                           \tag{1.2}
\]

Consequently, for every real scalar `theta`,

\[
 U(\theta)=I+\theta N                              \tag{1.3}
\]

is `J`-unitary.  Indeed the linear term in
`U(theta)^* J U(theta)` vanishes by (1.2), and
`N^*JN=-JN^2=0` kills the quadratic term.

The Hermitian matrix

\[
 \Pi:=-iJN=\begin{pmatrix}1&-i\\ i&1\end{pmatrix} \tag{1.4}
\]

is positive semidefinite of rank one, with eigenvalues `0` and `2`.

### Lemma 1.1 -- additive parabolic product

For arbitrary real numbers `theta_1,...,theta_m`,

\[
 \prod_{j=1}^m U(\theta_j)
 =U\left(\sum_{j=1}^m\theta_j\right).              \tag{1.5}
\]

#### Proof

Every mixed term contains `N^2` and vanishes.  QED.

## 2. Exact Euler--Gamma phase lift

For a prime `p`, put `a_p=log p`, `r_p=p^(-1/2)`,
`z_p(tau)=exp(i a_p tau)` and

\[
 c_p(z)={z-r_p\over z(1-r_pz)}.                    \tag{2.1}
\]

On the real axis `c_p(z_p(tau))` is unimodular.  Choose a continuous local
real phase `theta_p` by

\[
 c_p(z_p(\tau))^{-1}=e^{i\theta_p(\tau)}.          \tag{2.2}
\]

The already proved relative Poisson identity is

\[
 \theta_p'(\tau)=a_p(1-P_p(\tau)).                 \tag{2.3}
\]

Similarly write the quarter-Gamma boundary multiplier as

\[
 b_\infty(\tau)=e^{i\theta_\infty(\tau)},\qquad
 \theta_\infty'(\tau)=g_\Gamma(\tau)-m_0.         \tag{2.4}
\]

For the finite active prime set `S_T`, define

\[
 \mathbb U_T(\tau)
 :=U(\theta_\infty(\tau))
   \prod_{p\in S_T}U(\theta_p(\tau)).              \tag{2.5}
\]

Lemma 1.1 gives

\[
 \mathbb U_T(\tau)=I+\Theta_T^{\rm par}(\tau)N,
 \qquad
 \Theta_T^{\rm par}
 =\theta_\infty+\sum_{p\in S_T}\theta_p.          \tag{2.6}
\]

This equality is local in the phase chart; changes of logarithm add the
corresponding unipotent monodromy and do not affect the connection below.

### Theorem 2.1 -- exact parabolic Green connection

Let `Q=-i d/dtau`.  On the common smooth core,

\[
 \boxed{
 \mathbb U_T^*JQ\mathbb U_T-JQ
   =A_T(\tau)\Pi,}                                  \tag{2.7}
\]

where

\[
 A_T(\tau)=g_\Gamma(\tau)-m_0
 +\sum_{p\in S_T}a_p(1-P_p(\tau))                 \tag{2.8}
\]

is exactly the finite-window multiplier in the zero-residual Green
identity.

#### Proof

Since `mathbb U_T` is `J`-unitary,

\[
 \mathbb U_T^*JQ\mathbb U_T-JQ
 =-iJ\mathbb U_T^{-1}\mathbb U_T'.                \tag{2.9}
\]

Equations (1.2) and (2.6) give

\[
 \mathbb U_T^{-1}\mathbb U_T'
 =(\Theta_T^{\rm par})'N.                         \tag{2.10}
\]

By (2.3)--(2.4), `(Theta_T^par)'=A_T`.  Substitution
in (2.9) and definition (1.4) prove (2.7).  QED.

If `v=(1,i)^t/sqrt(2)`, then `Pi v=2v`.  Hence compression of (2.7) to
the fixed line `C v`, with the harmless factor `1/2`, recovers the scalar
Green identity exactly.  No `B_nuc`, zero location, square root or fitted
parameter enters the construction.

## 3. What happens to the Tate poles

Each scalar factor `c_p^{-1}` has upper critical poles at

\[
 \tau_{p,k}={2\pi k\over\log p}+{i\over2},
 \qquad k\in\mathbb Z.                             \tag{3.1}
\]

At `k=0` all primes meet at the same Tate point.  A scalar product of the
factors accumulates pole order with `|S_T|`.  In the parabolic lift their
logarithms multiply the same `N`, and (1.5) makes the singularity additive;
there is only one nilpotent direction.  Thus a single Tate zero cancels the
common *linear conormal direction* rather than one scalar pole per prime.

For `k != 0`, the lattices (3.1) are prime-dependent.  Analytic continuation
of `theta_p` around such a point changes it by `2 pi` times an integer, so
the parabolic lift acquires monodromy

\[
 \operatorname{Mon}_{p,k}(\mathbb U_T)
 =I+2\pi m_{p,k}N.                                 \tag{3.2}
\]

The two Tate evaluations do not annihilate these modes.  They are the same
full periodic boundary modules isolated in D.196, now compressed into a
single unipotent conjugacy class rather than represented by an indefinite
diagonal residue form.

## 4. Relation to F2

Put `E(z)=xi(1/2+z)` and, on the complement of its divisor, define the
source-coupled nilpotent connection

\[
 \nabla_F=d- {E'(z)\over E(z)}K_F(z)N\,dz.          \tag{4.1}
\]

All values of its connection form are scalar multiples of the same
square-zero matrix `N`, so path ordering is unnecessary.  At a simple
critical zero `lambda=i gamma`, its residue is `K_F(lambda)N`, and its local
monodromy is

\[
 \operatorname{Mon}_\lambda(\nabla_F)
 =I+2\pi i K_F(\lambda)N.                           \tag{4.2}
\]

Indeed the exponential truncates after its linear term because `N^2=0`.
Since `N != 0`, this proves

\[
 K_F(i\gamma)=0
 \quad\Longleftrightarrow\quad
 \operatorname{Mon}_{i\gamma}(\nabla_F)=I.          \tag{4.3}
\]

Consequently F2 is equivalently the following concrete statement:

> the source-coupled parabolic connection of every first-contact state has
> trivial local monodromy at every simple critical zero.

Theorem 2.1 constructs the finite Euler--Gamma parabolic carrier and its
exact Green connection; (4.1)--(4.3) construct the critical source-coupled
monodromy coordinate.  They do not prove its triviality.  Finite energy of a
single-valued flat frame
cannot be assumed: its logarithmic divergence is exactly the critical
conormal square already computed in phase 121.

## 5. Corpus audit and exact gain

### 5.1 Two-semimetric rigidity

There is a sharp algebraic closure criterion inside the same two-dimensional
carrier.  Put

\[
 N_-:=\overline N
 =\begin{pmatrix}-i&1\\1&i\end{pmatrix},\qquad
 \Pi_-:=iJN_-
 =\begin{pmatrix}1&i\\-i&1\end{pmatrix}.           \tag{5.1}
\]

Both `Pi` and `Pi_-` are positive semidefinite of rank one, and

\[
 \Pi+\Pi_-=2I.                                     \tag{5.2}
\]

### Proposition 5.1 -- simultaneous semimetric preservation kills the parabolic coefficient

For `c in C`, let `M_c=I+cN`.  Then

\[
 M_c^*\Pi M_c=\Pi                                  \tag{5.3}
\]

for every `c`, whereas

\[
 M_c^*\Pi_-M_c=\Pi_-
 \quad\Longleftrightarrow\quad c=0.                \tag{5.4}
\]

Consequently a monodromy in the parabolic subgroup generated by `N` which
preserves both oriented semimetrics is the identity.

#### Proof

Since `Pi N=-iJN^2=0` and, by adjunction, `N^*Pi=0`, expansion proves
(5.3), for arbitrary complex `c`.  If (5.4) also holds, (5.2) implies
`M_c^*M_c=I`.  But `(M_c-I)^2=c^2N^2=0`, so `M_c` is unipotent.  A unitary
matrix is normal and therefore diagonalizable, while a unipotent matrix has
only the eigenvalue one.  Hence `M_c=I`.  Since `N != 0`, this gives `c=0`.
The converse is immediate.  QED.

Proposition 5.1 would close F2 immediately if first contact supplied the
same physical monodromy with both compatibilities (5.3)--(5.4).

### 5.2 Why ordinary Real covariance supplies only one compatibility

Let

\[
 S=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 \mathcal C(v)=S\overline v.                       \tag{5.6}
\]

Then

\[
 S\overline NS=N,\qquad S\overline\Pi S=\Pi.       \tag{5.7}
\]

Thus the physical Real involution transports the plus parabolic system to a
distinct reflected fibre and, after the canonical Real identification,
returns the *same* pair `(N,Pi)`.  It does not put `Pi_-` on the original
fibre.  Consequently (5.4) is not a consequence of ordinary Real covariance.
As in the two-port audit, asserting that the reflected and unreflected
semimetrics act simultaneously on one physical fibre is the missing
cross-port matching, not a formal symmetry.

### 5.3 Why self-adjointness also supplies the wrong-sided compatibility

The first-contact operator is self-adjoint, so it is tempting to use its
adjoint equation as the missing second law.  In the parabolic carrier this
produces the conjugate monodromy

\[
 M_c^*=I+\overline c,N_- .                         \tag{5.8}
\]

Its preservation of its natural semimetric is

\[
 (M_c^*)^*\Pi_-M_c^*=\Pi_-,
 \quad\text{equivalently}\quad
 M_c\Pi_-M_c^*=\Pi_-.                              \tag{5.9}
\]

But (5.9) holds for every complex `c`.  Indeed
`N\Pi_-=0` and `\Pi_-N^*=0`, so all linear and quadratic terms in the
left side vanish.  It is a **co-preservation** law for `M_c`, whereas
Proposition 5.1 requires the opposite-sided isometry

\[
 M_c^*\Pi_-M_c=\Pi_-.                              \tag{5.10}
\]

Thus taking the adjoint of the first-contact equation does not produce the
missing compatibility.  It gives a second identity, but one which the
universal nonzero parabolic model already satisfies.

### 5.4 The critical square is exactly the opposite-metric trace defect

Full matrix preservation is stronger than necessary.  For arbitrary
`c in C`, direct expansion gives the scalar identity

\[
 \boxed{
 \operatorname {tr}(M_c^*\Pi_-M_c-\Pi_-)=8|c|^2.} \tag{5.11}
\]

#### Proof

Write `c=x+iy`.  The two diagonal entries of the defect are

\[
 4(x^2+y^2-y),\qquad 4(x^2+y^2+y),                 \tag{5.12}
\]

and their sum is `8(x^2+y^2)`.  QED.

At a critical zero `rho=1/2+i gamma` of multiplicity `m_rho`, normalize the
source monodromy as

\[
 M_{F,\rho}=I+2\pi i\,m_\rho K_F(i\gamma)N.       \tag{5.13}
\]

Then (5.11) yields

\[
 {1\over4\pi}
 \operatorname {tr}
 (M_{F,\rho}^*\Pi_-M_{F,\rho}-\Pi_-)
 =8\pi m_\rho^2|K_F(i\gamma)|^2.                  \tag{5.14}
\]

The right side is exactly the local summand of the antisymmetric critical
square in the negative-half residue theorem.  Consequently, on every finite
critical ordinate window `J`,

\[
 \boxed{
 \mathfrak D_{T,J}^{\rm crit}(F)
 ={1\over4\pi}
 \sum_{\substack{\rho=1/2+i\gamma\\\gamma\in J}}
 \operatorname {tr}
 (M_{F,\rho}^*\Pi_-M_{F,\rho}-\Pi_-).}             \tag{5.15}
\]

Thus F2 no longer requires a matrix-valued matching theorem.  It is enough
to prove the single scalar conservation law

\[
 P_T\mathscr A_TF=0
 \quad\Longrightarrow\quad
 \operatorname {tr}(M_{F,\rho}^*\Pi_-M_{F,\rho})
 =\operatorname {tr}(\Pi_-)
 \quad\text{for every simple critical }\rho.       \tag{5.16}
\]

By (5.11), (5.16) forces every critical conormal coefficient to vanish.
The law (5.16) is not yet derived from first contact; writing it is not a
proof.  Its gain is that the already existing positive defect is now an
exact monodromy trace, with no unspecified norm or matching operator.

The exact terminal form of F2 can therefore be sharpened once more:

> prove from the first-contact equation, before scalar supertrace, that its
> critical monodromy preserves the opposite oriented semimetric `Pi_-`.

Proposition 5.1 then gives trivial monodromy, (4.3) gives
`K_F(i gamma)=0`, and the already proved faithfulness theorem gives `F=0`.

### 5.5 The complex radical line reduces F2 to one linear Krein flux

The quadratic trace law (5.16) is canonical, but it is not the smallest
possible terminal datum.  Put `c=x+iy` and retain `M_c=I+cN`.  A direct
expansion gives

\[
 \operatorname {tr}(M_c^*JM_c-J)=-4\,\operatorname {Im}c,       \tag{5.17}
\]

and, equivalently after quarter rotation of the source,

\[
 \operatorname {tr}\big((I+icN)^*J(I+icN)-J\big)
 =-4\,\operatorname {Re}c.                                    \tag{5.18}
\]

These identities have no quadratic remainder because `N^*JN=0`.

The stronger observation is that the first-contact space is complex linear.
If `F` is a first-contact vector, then so is `iF`, and

\[
 c_{iF,\rho}=i c_{F,\rho},\qquad
 c_{F,\rho}:=2\pi i m_\rho K_F(i\gamma).                     \tag{5.19}
\]

Consequently, if the same unrotated scalar flux law is valid on the whole
complex radical line, equations (5.17)--(5.19) give

\[
\left.\begin{aligned}
 \operatorname {tr}(M_{c_{F,\rho}}^*JM_{c_{F,\rho}}-J)&=0,\\
 \operatorname {tr}(M_{c_{iF,\rho}}^*JM_{c_{iF,\rho}}-J)&=0
\end{aligned}\right\}
\quad\Longrightarrow\quad c_{F,\rho}=0.                       \tag{5.20}
\]

Indeed the first line kills `Im(c_{F,rho})`; the second kills
`Im(i c_{F,rho})=Re(c_{F,rho})`.  Thus F2 needs only one real scalar flux
law, functorial under multiplication of the witness by `i`, at each critical
point.  Neither full preservation of `Pi_-` nor the quadratic trace identity
(5.16) is logically necessary.  This is a reduction in the target, not its
proof.  Physical `J`-unitarity of the finite Green product does not by itself
imply this source-coupled law.  Deriving (5.20) from first contact remains the
force-bearing statement.

### 5.6 Relation to the earlier non-abelian audit

Phase 120 considered nilpotent residues in a Higgs/Bogomolny star.  Its
type audit correctly observed that a nilpotent residue has zero eigenvalues
and cannot encode `(log p)p^(-j/2)` as a parabolic weight.  The construction
above does not do that.  The arithmetic coefficient is the derivative of
the fixed boundary phase in (2.3), and the nilpotent generator only prevents
multiplicative accumulation of the common singular direction.

D.196 already proves that two scalar Tate jets do not exhaust the periodic
boundary modules.  The present theorem does not contradict it: the
nontrivial monodromies (3.2) are precisely those surviving modules.

The exact new gain is (2.7): a source-defined common square-zero parabolic
lift whose Krein Green connection is the full `A_T`.  The remaining
extension theorem is F2 itself and remains open.

## 6. Status

```text
common square-zero generator                         PROVED
J-unitary parabolic Euler--Gamma product              PROVED
exact connection = A_T times one positive rank-one   PROVED
collapse of the common k=0 Tate conormal direction   PROVED
critical conormal = unipotent monodromy coefficient  PROVED
two-semimetric rigidity of that monodromy             PROVED
Real alone does not supply the second semimetric      PROVED
adjoint equation gives only automatic co-preservation PROVED
critical square = opposite-metric trace defect       PROVED
complex-line reduction to one linear Krein flux       PROVED
triviality of critical monodromy on equality          OPEN (F2)
global square and row (d)                             OPEN
```

No paper-42 change is authorized by this theorem alone.
