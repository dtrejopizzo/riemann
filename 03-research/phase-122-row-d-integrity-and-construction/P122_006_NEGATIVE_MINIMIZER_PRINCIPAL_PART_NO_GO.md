# P122.006 — negative-minimizer principal-part no-go

## Verdict

A negative minimizer exists at every fixed window where row D fails, but
retaining its negative eigenvalue does not improve any critical-zero
principal-part argument.  The spectral term is holomorphic and disappears
from all negative Laurent orders.  Therefore Track II cannot close D by a
local pole calculation alone.

## 1. Attained negative eigenvector

On the two-Tate primitive space the form has the exact decomposition

\[
 q_T=\mathcal R_T-\mathcal W_T^*\mathcal W_T.
\]

The reference form is closed and has compact form-domain embedding, while
the load is relatively compact.  Hence the associated self-adjoint
operator is lower semibounded with compact resolvent.  If `q_T` has a
negative direction, its lowest eigenvalue is attained: for some
`lambda<0` and nonzero `F in P_T`,

\[
 P_T\mathscr A_TP_TF=\lambda F.                       \tag{1.1}
\]

Equivalently, before projection,

\[
 \mathscr A_TF=\lambda F+\alpha e^{-t/2}+\beta e^{t/2}.\tag{1.2}
\]

Parity may be imposed because reflection commutes with the operator and
the Tate projection.

## 2. Fourier--Laplace consequence

For compactly supported `F`,

\[
 K_F(z)=\int_{-T}^{T}F(t)e^{-zt}\,dt
\]

is entire.  The transforms of the two Tate forcing functions are also
entire.  Thus the additional minimizer term in (1.2) contributes
`lambda K_F(z)`, an entire function.

At a simple zero `z=i gamma` of the completed Euler factor, the oriented
current still has principal part

\[
 -{K_F(i\gamma)\over z-i\gamma};                     \tag{2.1}
\]

neither its residue nor the double-pole coefficient of the frozen Riccati
expression sees `lambda`.

In particular, if

\[
 L_F={E'\over E}K_F,
\]

then the coefficient of `(z-i gamma)^(-2)` in `L_F'+L_F^2` remains

\[
 c(c-1),\qquad c=K_F(i\gamma),                        \tag{2.2}
\]

exactly as at first contact.  Equation (1.2) supplies no local reason for
(2.2) to vanish.

## 3. Local countermodel

Take the local divisor germ `E(x)=x` and an arbitrary source germ
`K(x)=c+O(x)`.  Adding any regular germ, including `lambda K`, changes only
the nonnegative Laurent coefficients of the transformed equation.  The
residue `c` and Riccati double coefficient `c(c-1)` remain arbitrary.

Therefore no argument which uses only:

* the negative sign `lambda<0`;
* equality of principal parts;
* Real/complex-line covariance; and
* the two entire Tate forcing terms

can deduce `c=0` or sparse critical support.  A global source theorem may
still exploit `lambda<0`, but it must involve more than local pole order.

## 4. Track-II decision

`RETIRED-AS-LOCAL-PRINCIPAL-PART-ROUTE`.

The fixed-window negative-minimizer formulation remains a valid fallback
for variational arguments.  It is not a new residue mechanism.  Any future
Track-II proposal must state a global identity in which the sign of
`lambda` survives; otherwise it is rejected by this note.
