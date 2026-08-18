# D.57 — A rigorous interval engine and the first-hinge startup obstruction

## 1. Purpose

D.55--D.56 reduce row D on every bounded support range to a uniformly
finite parity--Feshbach problem.  This note constructs the rigorous interval
mechanism needed to verify that problem between consecutive prime-power
thresholds.  It also audits the first requested interval immediately after

\[
 T_2={\log2\over2}.                                       \tag{1.1}
\]

The audit identifies an exact startup obstruction.  The available
Connes--Consani theorem gives nonnegativity, but not a coercive gap, on the
full primitive space at `T_2`; its strict Sonin square requires an additional
central vanishing condition.  The entering `p=2` hinge has an indefinite
crossing form.  Therefore no perturbative interval, however short, follows
from the presently proved boundary statement.

This is not evidence that positivity fails after `T_2`.  It proves that the
proposed interval induction needs one additional certified datum: a
positive finite-core margin or a sign theorem on the boundary nullspace.

No floating-point sample is used as a proof, and no RH or screw positivity
is assumed.

## 2. Exact threshold partition

Let `q_1<q_2<...` be the increasing sequence of distinct prime powers and
put

\[
 \tau_j={1\over2}\log q_j.                                \tag{2.1}
\]

On every open cell

\[
 I_j=(\tau_j,\tau_{j+1})                                  \tag{2.2}
\]

the set of finite-place terms is constant.  Only their compression to the
moving window changes.  The first nontrivial cell is

\[
 I_2=\left({\log2\over2},{\log3\over2}\right),            \tag{2.3}
\]

and contains exactly the hinge

\[
 g_2(t)={\log2\over\sqrt2}(|t|-\log2)_+.                  \tag{2.4}
\]

For exact interval arithmetic, logarithms need not be treated as floating
constants.  For an integer `n>1`, put `z=(n-1)/(n+1)`.  Then

\[
 \log n=2\sum_{r=0}^{N}{z^{2r+1}\over2r+1}+R_N,
 \qquad
 0<R_N<{2z^{2N+3}\over(2N+3)(1-z^2)}.                    \tag{2.5}
\]

Thus every threshold has nested rational enclosures.  The same construction
handles `log p` in all hinge coefficients.

## 3. Source-defined interval entries

Fix a compact rational interval `J subset I_j` and the common D.55 cutoff
constructed with its right endpoint.  Transport all windows to `[-1,1]`
and use parity-adapted prolate or finite-element coordinates.  Every matrix
entry is enclosed from the following source pieces.

### 3.1 Prime-power hinges

On a threshold cell, each function

\[
 (T|x-y|-\log q)_+                                       \tag{3.1}
\]

has a fixed active/inactive subdivision after refining the spatial cells by
the rational enclosures (2.5).  It is affine in `T` on each active piece.
Integration of polynomial finite elements is then exact over rational
endpoints, with the logarithm enclosure supplying directed rational bounds.

### 3.2 Gamma--Lerch part

Use the positive digamma expansion

\[
 \ell(\tau)=\sum_{r=0}^{R}{1\over a_r}
 {\tau^2\over4a_r^2+\tau^2}+\mathcal R_R(\tau),
 \qquad a_r=r+1/4.                                        \tag{3.2}
\]

For `|tau|<=Omega`, the omitted tail obeys

\[
 0\leq\mathcal R_R(\tau)
 \leq{\tau^2\over4}\sum_{r>R}{1\over a_r^3}
 \leq{\tau^2\over8(R+1/4)^2}.                            \tag{3.3}
\]

Outside the finite band, D.55 supplies the strict negative margin.  Hence
the Gamma tail is bounded analytically rather than truncated numerically.

### 3.3 Universal constants

The identity

\[
 \psi(1/4)=-\gamma-\pi/2-3\log2                           \tag{3.4}
\]

reduces `m_0` to rational enclosures for `pi`, `log 2` and Euler's constant.
Classical rational bounds for the harmonic remainder

\[
 {1\over2(n+1)}<H_n-\log n-\gamma<{1\over2n}              \tag{3.5}
\]

give a convergent directed enclosure for `gamma`.  Thus no special-function
floating value is required.

## 4. Uniform Schur derivative bound

Use the common high/core splitting of D.55 on `J`.  In either parity channel
write

\[
 B(T)=\begin{pmatrix}A(T)&C(T)\\C(T)^*&D(T)\end{pmatrix},
 \qquad D(T)\leq-\eta/2,                                  \tag{4.1}
\]

and

\[
 S(T)=A(T)-C(T)D(T)^{-1}C(T)^*.                           \tag{4.2}
\]

Between thresholds the interval construction above gives finite constants
`L_A,L_C,L_D,K_C` such that

\[
 \|A'\|\leq L_A,\quad \|C'\|\leq L_C,
 \quad\|D'\|\leq L_D,\quad\|C\|\leq K_C.                 \tag{4.3}
\]

Differentiating (4.2) and using `||D^(-1)||<=2/eta` yields

\[
 \boxed{
 \|S'(T)\|\leq
 L_S:=L_A+{4K_CL_C\over\eta}
          +{4K_C^2L_D\over\eta^2}.}                      \tag{4.4}
\]

All quantities on the right have directed rational enclosures.  The
effective jets of D.56 have an analogous derivative bound obtained from

\[
 \widetilde p=p-CD^{-1}q.                                 \tag{4.5}
\]

## 5. The interval propagation lemma

Suppose a rigorous interval `LDL^*` certificate at `T_c in J` proves the
D.56 inequalities with a common spectral/sign margin `mu>0`, including the
even Green inequality.  If `L_tot` bounds the derivatives of all three
certified scalar/matrix inequalities, then they retain their signs on

\[
 |T-T_c|<{\mu\over L_{tot}}.                              \tag{5.1}
\]

This follows from the min--max inequality

\[
 |\lambda_k(S(T))-\lambda_k(S(T_c))|
 \leq\|S(T)-S(T_c)\|\leq L_S|T-T_c|                       \tag{5.2}
\]

and its scalar analogue for the jet Schur quantities.  Repeating (5.1),
with overlap and outward-rounded endpoints, is a rigorous induction across
one threshold cell.  At the next threshold the new hinge is added with its
one-sided interval formula (3.1).

Thus the estimate which permits iteration is not mere positivity at a
point: it is a **strict finite-core margin divided by a certified derivative
bound**.

## 6. Audit of the first post-`2` interval

Consider, for definiteness, the exact rational interval

\[
 J_0=[347/1000,87/250].                                   \tag{6.1}
\]

Formula (2.5) proves using rational arithmetic that

\[
 {\log2\over2}<347/1000<87/250<{\log3\over2};             \tag{6.2}
\]

hence `J_0` lies strictly inside the one-hinge cell.

To start the induction from `T_2`, one would need a margin `mu_2>0` in
(5.1).  The currently available full-primitive theorem supplies only

\[
 QW_{T_2}\geq0.                                           \tag{6.3}
\]

The stronger Sonin lower bound is strictly positive only on the subclass
with an additional central Mellin zero.  It does not furnish `mu_2>0` on
the full two-ruling primitive space.

Meanwhile the entering perturbation is not nonnegative.  D.53 proves

\[
 \dot Q_2(F,F)=-2{\log2\over\sqrt2}
 \mathrm{Re}\,\langle F,S_{\log2}F\rangle,            \tag{6.4}
\]

and exhibits compactly supported smooth vectors for both signs of the
correlation.  The abstract obstruction is already exact in dimension two:

\[
 A_0=\begin{pmatrix}0&0\\0&1\end{pmatrix}\geq0,
 \qquad
 A_0+\varepsilon
 \begin{pmatrix}-1&0\\0&0\end{pmatrix}
 =\begin{pmatrix}-\varepsilon&0\\0&1\end{pmatrix}.       \tag{6.5}
\]

For every `epsilon>0` a negative mode is created from the unprotected null
direction.  Therefore (6.3) plus any norm-small estimate for the first hinge
cannot prove positivity on even the shortest right-hand interval.

### Verdict for `J_0`

The interval certificate does **not** close `J_0` from the currently proved
boundary data.  This is a rigorous failure of the startup argument, not a
floating-point failure and not a counterexample to the desired inequality.
The missing datum is one of:

1. a certified positive lower eigenvalue for the full primitive form at one
   point of `J_0`;
2. a proof that the nullspace in (6.3) is zero with a coercive bound in the
   D.55 graph norm;
3. a proof that the first-hinge crossing form is nonnegative on that
   nullspace.

Any of these would provide the initial `mu` for (5.1), after which the
source-defined interval engine can iterate.

## 7. Why a floating Galerkin matrix is insufficient

Published computations report positive truncated matrices throughout
`log2<L<log3`, with very small lowest eigenvalues near the right endpoint.
They are valuable diagnostics but do not supply the required proof because

1. the bottom margin approaches the truncation error scale;
2. a floating eigenvalue has no directed enclosure;
3. without D.55's high Schur residual, an omitted mode can change inertia;
4. point samples do not control the continuum in `T`.

The scheme in Sections 2--5 addresses all four issues, but it still needs a
single rigorously positive seed margin in the full primitive class.

## 8. Circularity audit

Declaring the continuous `g` to be a screw function would give precisely
the missing nonnegative form on all windows.  Using that declaration to
choose `mu`, or to rule out the nullspace in (6.3), would import Weil
positivity and RH.  It is not an admissible startup certificate.

Likewise, the Meyer zero representation cannot provide the interval margin:
its spectral sign is the row-D conclusion transported through row C.

## 9. Result

D.57 supplies a rigorous, source-defined interval architecture:

* exact rational threshold enclosures;
* complete prime-power hinge entries;
* analytic Gamma-tail bounds;
* a uniform high Schur margin;
* parity splitting;
* derivative-controlled interval propagation.

It also proves that the architecture cannot be started immediately to the
right of `log2/2` using only the currently established semidefinite boundary
theorem.  A coercive seed or a boundary-nullspace crossing theorem is the
specific next mathematical target.  No post-`2` interval is claimed closed.

