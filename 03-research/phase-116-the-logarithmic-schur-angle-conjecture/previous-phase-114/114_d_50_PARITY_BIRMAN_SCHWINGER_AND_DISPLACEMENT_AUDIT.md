# D.50 — Parity Birman--Schwinger comparison and displacement-rank audit

## 1. The two channels with exact normalization

Let `J F(t)=F(-t)`.  Write `H_e,H_o` for the restrictions of the D.49
Levy operator `H_0` to the even and odd subspaces.  Put

\[
 \phi_e=\phi_++\phi_-=2\cosh(t/2),\qquad
 \phi_o=\phi_+-\phi_-=2\sinh(t/2),                            \tag{1.1}
\]

and normalize

\[
 u_e=2^{-1/2}\phi_e,\qquad u_o=2^{-1/2}\phi_o.                \tag{1.2}
\]

The crossed polar block of D.49 is exactly

\[
 R_2=|u_e\rangle\langle u_e|-|u_o\rangle\langle u_o|.         \tag{1.3}
\]

Thus the full CCM operator splits as

\[
 A_e=H_e+|u_e\rangle\langle u_e|,qquad
 A_o=H_o-|u_o\rangle\langle u_o|.                            \tag{1.4}
\]

This sign pattern is important: the polar block pushes the even channel
up and the odd channel down.

## 2. Secular functions and interlacing

For `z` outside the corresponding unperturbed spectrum define

\[
 m_e(z)=\langle u_e,(H_e-z)^{-1}u_e\rangle,qquad
 m_o(z)=\langle u_o,(H_o-z)^{-1}u_o\rangle.                  \tag{2.1}
\]

Away from the unperturbed spectrum, the matrix determinant lemma gives the
secular equations

\[
 1+m_e(z)=0\quad\hbox{(even)},qquad
 1-m_o(z)=0\quad\hbox{(odd)}.                                \tag{2.2}
\]

If `alpha_(e,k),alpha_(o,k)` are the eigenvalues of `H_e,H_o`, then

\[
 m_\epsilon(z)=\sum_k
 { |\langle u_\epsilon,v_{\epsilon,k}\rangle|^2
   \over \alpha_{\epsilon,k}-z},\qquad
 m_\epsilon'(z)>0                                             \tag{2.3}
\]

away from poles after omitting zero weights.  Consequently rank-one
interlacing gives, with weak inequalities in the noncyclic case,

\[
 \alpha_{e,0}\leq\mu_{e,0}\leq\alpha_{e,1}\leq\mu_{e,1}\leq\cdots,
                                                                    \tag{2.4}
\]

and

\[
 \mu_{o,0}\leq\alpha_{o,0}\leq\mu_{o,1}\leq\alpha_{o,1}\leq\cdots.
                                                                    \tag{2.5}
\]

The inequalities adjacent to a pole are strict when the corresponding
spectral weight in (2.3) is nonzero.

There is one indispensable qualification.  If `v` is an eigenvector of
`H_e` orthogonal to `u_e`, or an eigenvector of `H_o` orthogonal to `u_o`,
then it persists as an eigenvector of the perturbed operator at the same
eigenvalue.  Such persistent eigenvalues are not zeros of (2.2), because
the determinant quotient has a removable zero/pole cancellation there.
Thus (2.2) describes all eigenvalues only after cyclicity is proved.  For
the first odd state the required strictness condition is

\[
 \langle u_o,v_{o,0}\rangle\ne0.                             \tag{2.6}
\]

## 3. What positivity improving actually proves

D.49 proves that `exp(-sH_0)` is positivity improving.  Compact resolvent
then implies that the global ground state of `H_0` is simple, strictly
positive and even.  Hence

\[
 \alpha_{e,0}<\alpha_{o,0}.                                  \tag{3.1}
\]

Moreover `u_e>0`, so its overlap with the even ground state is nonzero.
There is no analogous consequence for (2.6): both factors are odd and
positivity improving on the full interval does not determine the sign of
their restrictions to a half interval.
For `z<alpha_(e,0)`, the full resolvent is positivity improving and
`|u_o|<u_e` away from the origin, whence

\[
 0\leq m_o(z)\leq
 \langle |u_o|,(H_0-z)^{-1}|u_o|\rangle<m_e(z).               \tag{3.2}
\]

This is the full resolvent comparison supplied by positivity.  It does not
compare the perturbed ground states: (2.4) places `mu_(e,0)` above the pole
`alpha_(e,0)`, precisely where `(H_0-z)^(-1)` is no longer positive.  Nor
does positivity improving alone control the sign of the odd half-space
kernel

\[
 R_o(z;t,s)={1\over2}\bigl(R_0(z;t,s)-R_0(z;t,-s)\bigr),
 \qquad t,s>0.                                                \tag{3.3}
\]

Thus (3.1)--(3.2) are genuine but insufficient consequences.

## 4. Exact boundary-triplet ordering gate

For every real `E<alpha_(o,0)`, rank-one Schur complementation gives

\[
 A_o-E>0
 \quad\Longleftrightarrow\quad
 m_o(E)<1.                                                    \tag{4.1}
\]

Let `mu_e=inf spec(A_e)` and `mu_o=inf spec(A_o)`.  It follows immediately
that, provided `mu_e<alpha_(o,0)`,

\[
 \boxed{\mu_e<\mu_o\quad\Longleftrightarrow\quad m_o(\mu_e)<1.}
                                                                    \tag{4.2}
\]

There is also a directly usable sufficient version.  If an explicitly
constructed even unit vector `v` has

\[
 E=\langle v,A_ev\rangle<\alpha_{o,0},
 \qquad
 \langle u_o,(H_o-E)^{-1}u_o\rangle<1,                       \tag{4.3}
\]

then `mu_e<=E<mu_o`, so the full ground state lies in the even sector.
Simplicity is a separate intra-even assertion.  It follows, for example,
if `mu_e` is a nonpersistent secular root: then `m_e'(mu_e)>0` makes that
root simple.  Formula (4.3), with a prolate or other source-defined even
trial vector, is a noncircular arithmetic target: every object in it is
built from the prime-power and Gamma operator before any zeta zero is used.

A cruder sufficient estimate is

\[
 \alpha_{e,0}+\|u_e\|^2<\alpha_{o,0}-\|u_o\|^2,              \tag{4.4}
\]

but the jet norms grow with the window, so (4.3) is the sharper gate.

## 5. Audit of the CCM displacement-rank identity

At Galerkin level CCM prove

\[
 [D,A]=|\beta\rangle\langle\eta|-|\eta\rangle\langle\beta|,
 \qquad JD=-DJ,\quad J\eta=\eta,\quad J\beta=-\beta.         \tag{5.1}
\]

For an even eigenvector `x` of eigenvalue `mu` and an odd eigenvector `y`
of eigenvalue `nu`, (5.1) yields

\[
 (\nu-\mu)\langle x,Dy\rangle
   =-\langle x,\eta\rangle\langle\beta,y\rangle.             \tag{5.2}
\]

This is a useful Cauchy-type relation between the parity sectors, but its
right-hand side has no fixed sign.  It is a skew commutator identity, not a
positive factorization.  In particular it supplies neither

\[
 A_o-c=QQ^*,\qquad A_e-c=Q^*Q,                               \tag{5.3}
\]

nor an intertwining relation ordering the two ground energies.  Likewise,
reflection diagonalizes the boundary Weyl matrix into `m_e,m_o`, but (5.1)
does not impose an inequality between those two Herglotz functions.  The
counterexample below shows that no such SUSY or ordering conclusion follows
from the stated hypotheses.

## 6. A three-dimensional counterexample with all abstract properties

Take the grid `t=(-1,0,1)` and

\[
 J(x_-,x_0,x_+)=(x_+,x_0,x_-),\quad
 D=\operatorname{diag}(-1,0,1),\quad
 \eta=(1,1,1)^T,\quad\beta=(-1,0,1)^T.                       \tag{6.1}
\]

Let

\[
 A=\begin{pmatrix}0&1&1\\1&10&1\\1&1&0\end{pmatrix}.       \tag{6.2}
\]

Then `AJ=JA` and a direct entrywise calculation gives

\[
 [D,A]=|\beta\rangle\langle\eta|-|\eta\rangle\langle\beta|. \tag{6.3}
\]

Define the exact Tate vectors on this grid by

\[
 (\phi_\pm)_j=e^{\pm t_j/2},\qquad
 R_2=|\phi_-\rangle\langle\phi_+|
     +|\phi_+\rangle\langle\phi_-|,qquad H_0=A-R_2.         \tag{6.4}
\]

For `i!=j`,

\[
 (H_0)_{ij}=1-2\cosh((t_i-t_j)/2)<0.                         \tag{6.5}
\]

Hence `-H_0` is an irreducible Metzler matrix and `exp(-sH_0)` is strictly
positive for every `s>0`.  After adding a sufficiently large scalar to
`H_0`, it is a symmetric Dirichlet generator with killing; equivalently
`H_0=L-mI` exactly as in D.49.  Thus its ground state is simple, positive
and even.

Nevertheless the odd vector `(1,0,-1)^T` is an eigenvector of `A` with
eigenvalue `-1`, whereas the two even eigenvalues are

\[
 {11\pm\sqrt{89}\over2}.                                    \tag{6.6}
\]

Since `(11-sqrt(89))/2>-1`, the full ground state is simple and odd.  This
example simultaneously has reflection, the exact cosh/sinh polar jets, a
positivity-improving Levy/Dirichlet base and the CCM displacement-rank
identity.  Therefore those properties cannot prove `mu_e<mu_o`.

## 7. The exact additional arithmetic estimate

The surviving comparison problem is not an unspecified parity argument.
It is the scalar inequality

\[
 \boxed{
 \exists E_T<\alpha_{o,0}(T):\quad
 \mu_e(T)\leq E_T,qquad
 \sum_k { |\langle u_o,v_{o,k}\rangle|^2
          \over\alpha_{o,k}(T)-E_T}<1.}                      \tag{7.1}
\]

An explicit even trial vector proves the first inequality.  The second is
an odd-channel Green-function bound.  Equivalently,

\[
 \int_0^\infty e^{sE_T}
   \langle u_o,e^{-sH_o}u_o\rangle\,ds<1.                    \tag{7.2}
\]

Unlike bare positivity improving, (7.1) measures the prime-power and Gamma
weights quantitatively after removal of the even ground pole.  Proving it
uniformly in the Galerkin cutoff gives the fixed-window parity ordering
needed in D.48.  Together with simplicity of the resulting even secular
root it gives the fixed-window simple-even theorem.  Obtaining these facts
with the expanding-window residual rate of D.48 is the subsequent
convergence gate.

If one wants strict odd interlacing itself, rather than the cyclicity-free
Schur test (7.1), one must additionally prove (2.6).  The Schur test is
preferable because it automatically includes any persistent odd state:
`A_o-E>0` rules all of them out below `E` without assuming cyclicity.

## 8. Verdict

The parity reduction is exact and useful, but it does not close row D by
formal operator theory:

1. positivity improving proves only the unperturbed ordering (3.1) and the
   below-spectrum comparison (3.2);
2. rank-one interlacing, including possible persistent eigenvalues, moves
   the two channels toward each other and can reverse their order;
3. the CCM displacement identity gives (5.2), not a positive SUSY square;
4. the exact noncircular target is the odd resolvent bound (7.1), preferably
   evaluated at a source-defined even trial energy.

The counterexample proves that an arithmetic estimate beyond the structural
hypotheses is logically necessary.
