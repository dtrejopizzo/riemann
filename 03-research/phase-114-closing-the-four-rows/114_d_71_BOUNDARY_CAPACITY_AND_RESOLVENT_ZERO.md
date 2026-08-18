# D.71 — Boundary capacity and the first resolvent zero

## Status

D.70 reduces the cyclic Sturm route in each parity channel to exclusion of
a positive zero of

\[
 m_\epsilon(z)=
 \langle u_\epsilon,(B_\epsilon-z)^{-1}u_\epsilon\rangle. \tag{0.1}
\]

This note gives an exact source-side variational interpretation of that
zero.  It is the blow-up threshold of a boundary capacity with the Tate jet
fixed.  The interpretation compares the first zero directly with `z=0` and
includes the complete prime--Gamma operator.

It also proves a precise Poisson no-go: solving the boundary Euler--Lagrange
equation and evaluating its stationary action does not establish the sign.
The stationary action can be finite while the true boundary capacity is
infinite.  A negative-square Poisson identity is equivalent to the missing
primitive inequality unless its extremality is obtained independently from
the source geometry.

No RH, zeta zero, Weil positivity or screw positivity is used.  The paper is
not modified.

## 1. One parity channel

Fix a support window and one parity `epsilon in {e,o}`.  Let
`B=B_epsilon` be the self-adjoint prime--Gamma block and normalize its jet
`u=u_epsilon` to have norm one.  Decompose

\[
 H=\mathbb C u\oplus u^\perp,qquad
 B=\begin{pmatrix}a&b^*\\b&D\end{pmatrix}.                 \tag{1.1}
\]

The one-jet primitive operator is exactly

\[
 D=P_{u^\perp}BP_{u^\perp}.                               \tag{1.2}
\]

For a real parameter `z`, put

\[
 q_z(f)=\langle f,(B-z)f\rangle,qquad
 \ell(f)=\langle u,f\rangle.                              \tag{1.3}
\]

Define the upper boundary capacity

\[
 \boxed{
 \mathcal C_u(z)=
 \sup\{q_z(f): f\in\operatorname {Dom}(q_B),\ \ell(f)=1\}.}
                                                                    \tag{1.4}
\]

The value `+infinity` is allowed.  All prime powers and Gamma enter through
the single source form `q_z`; no spectral zero is used in the definition.

## 2. Exact boundary-capacity theorem

Write `f=u+x`, with `x in u^perp`.  Then

\[
 q_z(u+x)=a-z+2\operatorname {Re}\langle b,x\rangle
                 +\langle x,(D-z)x\rangle.                \tag{2.1}
\]

The standard completion theorem for a semidefinite quadratic form gives:

> **Theorem 2.1 (boundary capacity).**  The capacity `C_u(z)` is finite if
> and only if
> \[
> D-z\le0,qquad
> b\in\operatorname {Ran}(z-D)^{1/2}.                      \tag{2.2}
> \]
> In that case
> \[
> \boxed{
> \mathcal C_u(z)=a-z+|(z-D)^{\dagger/2}b\|^2
> =a-z-\langle b,(D-z)^\dagger b\rangle.}                 \tag{2.3}
> \]
> If `D-z<0`, the maximizing vector is unique and equals
> \[
> f_z=u+(z-D)^{-1}b.                                      \tag{2.4}
> \]

### Proof

If `D-z` has a positive direction `v`, then

\[
 q_z(u+tv)=t^2\langle v,(D-z)v\rangle+O(t)\to+\infty.     \tag{2.5}
\]

Thus finiteness forces the first condition in (2.2).  Put `A=z-D>=0`.
The remaining quadratic expression is

\[
 2\operatorname {Re}\langle b,x\rangle-|A^{1/2}x\|^2.   \tag{2.6}
\]

It is bounded above precisely when the functional defined by `b` is
continuous in the seminorm `||A^(1/2)x||`, which is the range condition in
(2.2).  Riesz representation and completion of the square give

\[
 2\operatorname {Re}\langle b,x\rangle-|A^{1/2}x\|^2
 =\|A^{\dagger/2}b\|^2
  -\|A^{1/2}x-A^{\dagger/2}b\|^2.                         \tag{2.7}
\]

This proves (2.3); if `A` is invertible it also proves (2.4).

## 3. The first zero is the capacity threshold

Let

\[
 \mu_u=\sup\operatorname {spec}(D).                       \tag{3.1}
\]

For every `z>mu_u`, the operator `z-D` is strictly positive and Theorem 2.1
applies.  For every `z<mu_u`, (2.5) gives infinite capacity.  Therefore

\[
 \boxed{
 \mu_u=\inf\{z\in\mathbb R:\mathcal C_u(z)<\infty\}.}    \tag{3.2}
\]

At an endpoint the range condition decides whether the infimum is attained;
it does not change (3.2).

Whenever both `B-z` and `D-z` are invertible, block inversion gives

\[
 \langle u,(B-z)^{-1}u\rangle
 ={1\over a-z-\langle b,(D-z)^{-1}b\rangle}
 ={1\over\mathcal C_u(z)}.                                \tag{3.3}
\]

If `u` is cyclic, no compression eigenvalue is persistent.  As `z` decreases
to the largest eigenvalue `mu_u` from above,

\[
 \mathcal C_u(z)\to+\infty,qquad m_u(z)\to0.              \tag{3.4}
\]

Thus (3.2) is exactly the first resolvent zero of D.70 in variational
coordinates.

The desired comparison with the origin is now exact:

\[
 \boxed{
 D\le0
 \quad\Longleftrightarrow\quad
 \mathcal C_u(z)<\infty\text{ for every }z>0.}            \tag{3.5}
\]

Under strictness and the range condition,

\[
 D<0\quad\Longleftrightarrow\quad\mathcal C_u(0)<\infty.  \tag{3.6}
\]

Equations (3.5)--(3.6) are a source-side variational inequality for both
`m_e` and `m_o`.  They do not yet prove either capacity finite.

## 4. Rank-one boundary majorant

The capacity has an equivalent operator meaning.  For a real constant `C`,

\[
 q_z(f)\le C|\ell(f)|^2\quad(f\in\operatorname {Dom}(q_B)) \tag{4.1}
\]

holds if and only if `C_u(z)` is finite and

\[
 C\ge\mathcal C_u(z).                                     \tag{4.2}
\]

Indeed, (4.1) on `ell(f)=1` gives (4.2), while homogeneity handles nonzero
boundary value and Theorem 2.1 handles `ell(f)=0`.

Consequently the primitive Hodge inequality is equivalent, channel by
channel, to existence for every `z>0` of a finite rank-one majorant

\[
 \boxed{B-zI\le \mathcal C_u(z)|u\rangle\langle u|.}       \tag{4.3}
\]

This is the exact analytic analogue of a boundary intersection term: every
positive direction must factor through the corresponding Tate ruling.

## 5. Poisson completion and its circularity boundary

When `D-z<0`, (2.7) gives the exact negative-square identity

\[
 \boxed{
 q_z(\alpha u+x)
 =\mathcal C_u(z)|\alpha|^2
 -\|(z-D)^{1/2}x-(z-D)^{-1/2}b\alpha\|^2.}                \tag{5.1}
\]

The vector

\[
 x_z(\alpha)=(z-D)^{-1}b\alpha                            \tag{5.2}
\]

is the harmonic or Poisson extension of boundary value `alpha`; the second
term in (5.1) is its Dirichlet defect.

Formula (5.1) would prove the required sign immediately if its Poisson
operator were constructed independently and the squared norm were compared
source-by-source with all prime powers and Gamma.  But deriving (5.1) from
the square root of `z-D` presupposes `z-D>=0`, which by (3.5) is exactly the
primitive inequality.

> **Corollary 5.1 (Poisson-factorization audit).**  A trace-exact boundary
> identity obtained by algebraically completing the actual form `B-zI` is
> equivalent to the row-D sign on the zero-boundary space.  It becomes an
> independent proof only if the Poisson extension and its positive Dirichlet
> norm are constructed before identifying their trace with `B_nuc`.

This is the one-jet parity version of the support-lift contract of D.35.

## 6. A stationary Poisson solution is not enough

There is a sharper failure which is easy to overlook.  The Euler--Lagrange
equation for the constrained action can have a unique solution even when
the capacity is infinite.

Take the cyclic example from D.70:

\[
 B=\operatorname {diag}(4,3,2,-1),\qquad u=(1,1,1,1)^T.   \tag{6.1}
\]

Use the unnormalized boundary functional `ell(f)=u^T f`.  Since

\[
 u^TB^{-1}u={1\over4}+{1\over3}+{1\over2}-1={1\over12},   \tag{6.2}
\]

the constrained stationary vector is

\[
 f_{\rm stat}={B^{-1}u\over u^TB^{-1}u},qquad
 \ell(f_{\rm stat})=1,                                   \tag{6.3}
\]

and its stationary action is the finite positive number

\[
 \langle f_{\rm stat},Bf_{\rm stat}\rangle=12.            \tag{6.4}
\]

However

\[
 v=(1,-1,0,0)^T\in\ker\ell,qquad
 \langle v,Bv\rangle=7>0.                                \tag{6.5}
\]

Therefore

\[
 \langle f_{\rm stat}+tv,B(f_{\rm stat}+tv)\rangle
 =7t^2+O(t)\to+\infty,                                   \tag{6.6}
\]

so the true capacity is infinite.

> **Theorem 6.1 (stationary-action no-go).**  Cyclicity, invertibility of
> the bulk operator, solvability of the boundary Poisson equation, and a
> finite exact boundary action do not imply the primitive sign.  One must
> prove that the stationary solution is a maximum, equivalently that the
> zero-boundary Hessian is nonpositive.

This counterexample prevents replacing the D.56 inequality by a formal
Dirichlet-to-Neumann calculation.

## 7. Two parity channels and the remaining gate

Apply Theorem 2.1 separately to

\[
 (B_e,u_e),\qquad(B_o,u_o).                               \tag{7.1}
\]

The two-jet primitive inequality is equivalent to

\[
 \mathcal C_{u_e}(z)<\infty,qquad
 \mathcal C_{u_o}(z)<\infty
 \quad\text{for every }z>0.                              \tag{7.2}
\]

Once (7.2) is independently proved, the signs of the finite values at
`z=0` give the even/odd boundary Green signature required in D.56.

The advance of this note is the exact identification of the first positive
resolvent zero with a source-defined capacity threshold and the minimal
rank-one boundary majorant (4.3).  The obstruction is equally exact:
finiteness of that capacity, or extremality of the Poisson solution, is the
primitive Hodge inequality itself.  No new source estimate proving (7.2)
is obtained here; row D remains open.

