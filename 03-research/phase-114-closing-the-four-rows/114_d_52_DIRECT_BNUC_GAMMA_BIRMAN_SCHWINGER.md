# D.52 — Direct `B_nuc` route: Gamma Birman--Schwinger and hyperbolic Green matrix

## 1. Sign audit: D.47 versus D.49

There are three operators on the same compact window and confusing them
reverses the index problem.  With

\[
 L_T\geq0,qquad
 m_T=2\sum_{(p,k)\in\mathcal P_T}{\log p\over p^{k/2}}+m_0,
 \qquad R_2=M_T^*CM_T,                                      \tag{1.1}
\]

the exact identities are

\[
 \boxed{
 B_T:=B_{{\rm nuc},T}=m_TI-L_T,qquad
 H_{0,T}=L_T-m_TI=-B_T,qquad
 QW_T=R_2-B_T.}                                              \tag{1.2}
\]

On the primitive space `ker M_T`,

\[
 QW_T=-B_T.                                                   \tag{1.3}
\]

Therefore row D asks for

\[
 B_T|_{\ker M_T}\leq0.                                      \tag{1.4}
\]

The direct Hodge certificate of D.47 is

\[
 n_+(B_T)=1,qquad
 \operatorname{In}(M_TB_T^{-1}M_T^*)=(1,1,0),               \tag{1.5}
\]

with the usual range conditions at singular parameters.  By contrast,
D.49 studies the lowest eigenvalue of the lower-bounded operator `QW_T` and
the positivity-improving base `H_(0,T)=-B_T`.  Simplicity of the first
eigenvalue of `H_(0,T)` does not count how many eigenvalues of `H_(0,T)` lie
below zero, hence does not prove `n_+(B_T)=1`.

Equation (1.2) proves that D.47 and D.49 are sign-consistent.  They address
different spectral questions.

## 2. Gamma reference plus the complete finite-place operator

Write

\[
 \Gamma_T=m_0I-L_{\infty,T},                                 \tag{2.1}
\]

where

\[
 \langle F,L_{\infty,T}F\rangle
 =\int_0^\infty {e^{-r/2}\over1-e^{-2r}}
       \|F-S_rF\|_2^2\,dr.                                  \tag{2.2}
\]

Expanding each prime graph energy in (1.2) gives the bounded self-adjoint
finite-place operator

\[
 V_T=\sum_{(p,k)\in\mathcal P_T}{\log p\over p^{k/2}}
       \bigl(S_{k\log p}+S_{-k\log p}\bigr).                 \tag{2.3}
\]

Thus

\[
 \boxed{B_T=\Gamma_T+V_T.}                                   \tag{2.4}
\]

All shifts are compressed by zero extension to `[-T,T]`; (2.3) includes
every `p^k` with `k log p<=2T`.

The Gamma multiplier on the full Fourier line is

\[
 m_\infty(\tau)=\log\pi-
 \operatorname{Re}\psi\left({1\over4}+{i\tau\over2}\right).
                                                                    \tag{2.5}
\]

It is positive near zero and negative for large `|tau|`; its positive zero
is approximately `tau_*=6.2898359888`.  Consequently `Gamma_T` is not an
index-one reference uniformly in `T`.  Time-frequency concentration in any
closed subband of `(-tau_*,tau_*)` produces a number of positive directions
growing linearly with `T`.  Hence the prime operator in (2.3) must remove a
growing Gamma-positive sector.  It cannot be treated as a small perturbation
for the index question.

## 3. Self-adjoint Birman--Schwinger congruence

Assume first that `Gamma_T` is invertible; exceptional windows can be
handled by a small real shift or a Moore--Penrose range formulation.  Put

\[
 J_{\Gamma,T}=\operatorname{sgn}(\Gamma_T),\qquad
 K_T=|\Gamma_T|^{-1/2}V_T|\Gamma_T|^{-1/2}.                  \tag{3.1}
\]

The compactness of `|Gamma_T|^(-1/2)` and boundedness of `V_T` make `K_T`
compact and self-adjoint.  There is an exact congruence

\[
 \boxed{
 B_T=|\Gamma_T|^{1/2}
       (J_{\Gamma,T}+K_T)|\Gamma_T|^{1/2}.}                  \tag{3.2}
\]

Therefore

\[
 \boxed{n_+(B_T)=n_+(J_{\Gamma,T}+K_T).}                    \tag{3.3}
\]

This is the direct Birman--Schwinger index problem.  It is not the scalar
ground-state equation of D.49.  Along the path

\[
 \mathcal B_T(s)=J_{\Gamma,T}+sK_T,qquad0\leq s\leq1,       \tag{3.4}
\]

the desired theorem says that all but one of the initially positive Gamma
directions cross zero, with no reverse crossing and no terminal kernel.
The crossing form at a simple zero `x` is

\[
 {d\over ds}\langle x,\mathcal B_T(s)x\rangle
 =\langle x,K_Tx\rangle.                                    \tag{3.5}
\]

Neither its sign nor the number of crossings follows from compactness.

The equivalent analytic Fredholm condition for an eigenvalue `z` is

\[
 -1\in\operatorname{spec}
 \bigl((\Gamma_T-z)^{-1}V_T\bigr),                           \tag{3.6}
\]

with persistent Gamma eigenvalues treated separately.  Compactness is
enough for this Fredholm alternative; an ordinary Fredholm determinant
would additionally require a trace-ideal estimate which is not asserted.
Formula (3.2) is preferable at `z=0` because it is self-adjoint and records
inertia.

## 4. The two-by-two boundary Green matrix

Assume now that `B_T` and `Gamma_T` are invertible.  The resolvent identity
gives

\[
 \begin{aligned}
 B_T^{-1}
  ={}&\Gamma_T^{-1}
 -\Gamma_T^{-1}V_T
   (I+\Gamma_T^{-1}V_T)^{-1}\Gamma_T^{-1}.                  \tag{4.1}
 \end{aligned}
\]

Hence the D.47 boundary matrix is explicitly

\[
 \boxed{
 \begin{aligned}
 G_T:=M_TB_T^{-1}M_T^*
 ={}&M_T\Gamma_T^{-1}M_T^*\\
 &-M_T\Gamma_T^{-1}V_T
 (I+\Gamma_T^{-1}V_T)^{-1}\Gamma_T^{-1}M_T^*.
 \end{aligned}}                                             \tag{4.2}
\]

Reflection diagonalizes this matrix in the normalized even/odd boundary
vectors `u_e,u_o`:

\[
 G_T\sim
 \begin{pmatrix}
 g_e(T)&0\\0&g_o(T)
 \end{pmatrix},\qquad
 g_\epsilon(T)=
 \langle u_\epsilon,B_{T,\epsilon}^{-1}u_\epsilon\rangle.   \tag{4.3}
\]

Thus the hyperbolic ruling condition is the scalar sign statement

\[
 \boxed{g_e(T)g_o(T)<0.}                                    \tag{4.4}
\]

At a singular window one must replace (4.2) by the reduced inverse and
verify

\[
 M_T^*(\mathbb C^2)\subseteq\operatorname{Ran}B_T,qquad
 \ker B_T\cap\ker M_T=0,                                    \tag{4.5}
\]

exactly as in D.47.

## 5. The direct row-D acceptance theorem

The constrained Haynsworth identity now yields the following source-side
criterion:

> If, on every Galerkin cutoff and uniformly in its exhaustion,
> 
> \[
> n_+(J_{\Gamma,T}+K_T)=1,qquad g_e(T)g_o(T)<0,              \tag{5.1}
> \]
> 
> and (4.5) holds through singular limits, then
> `B_T|_(ker M_T)<0`.

Indeed (3.3) gives `In(B_T)=(1,infinity,0)`, (4.4) gives
`In(G_T)=(1,1,0)`, and D.47 subtracts the boundary inertia to leave a
negative primitive complement.

The two requirements in (5.1) are independent:

1. the first is a global Morse-index/spectral-flow theorem for the complete
   prime--Gamma operator;
2. the second is a two-channel boundary-resolvent calculation.

Neither follows from the other by dimension counting.

## 6. What elementary estimates do and do not show

The operator norm bound

\[
 \|V_T\|\leq2\sum_{(p,k)\in\mathcal P_T}{\log p\over p^{k/2}} 
                                                                    \tag{6.1}
\]

grows on the scale `e^T`.  It does not give `||K_T||<1`, and even such a
bound would preserve the many positive directions of `J_(Gamma,T)` rather
than reduce them to one.

Likewise, positivity improving of `L_T` concerns the lowest eigenvalue of
`H_(0,T)=-B_T`; it proves simplicity of the most negative direction of
`B_T`, not uniqueness of its positive direction.  It has no implication
for (5.1).

A useful sufficient crossing theorem would instead construct a filtration
of the Gamma-positive spectral subspace on which the matrix of `K_T` is
strictly negative, leaving exactly one hyperbolic ruling direction, and
control the negative Gamma complement against reverse crossings.  No such
arithmetic oscillation estimate is presently available.

## 7. Circularity boundary

The direct target

\[
 n_+(B_T)=1,qquad \operatorname{In}(G_T)=(1,1,0)             \tag{7.1}
\]

implies the primitive sign and, after exhaustion, row D.  By the already
proved row-C comparison, the all-test primitive sign is Weil's criterion
and hence equivalent to RH.  Therefore proving (7.1) by invoking positivity
of `QW`, the location of zeta zeros, or a preselected positive spectral
subspace is circular.

By contrast, (3.1)--(4.4) are unconditional identities assembled from the
Gamma multiplier, every prime-power shift and the two boundary jets.  A
proof of their signs by an independent oscillation or total-positivity
theorem would be a valid closure.

## 8. Verdict

The corrected direct route is:

\[
 \boxed{
 B_T=\Gamma_T+V_T
 \longrightarrow
 J_{\Gamma,T}+K_T
 \longrightarrow
 \bigl(n_+=1,\ \det G_T<0\bigr)
 \longrightarrow
 B_T|_{\ker M_T}<0.}                                        \tag{8.1}
\]

The signs agree exactly with D.47 and D.49.  The remaining new theorem is
not a ground-state theorem: it is an index-reduction theorem showing that
the complete prime-power perturbation removes all but one of the growing
Gamma-positive directions while the boundary Green matrix remains
hyperbolic.
