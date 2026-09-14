# P124.005 -- arithmetic collar kernel and the residual obstruction

Status: `EXACT REDUCTION / SIMPLE KERNEL IDENTITY REFUTED`.

This note rewrites the first Tate collar current

\[
        J_+(F)=M_+(\mathscr A_TF)
\]

as a pairing with the explicit adjoint kernel

\[
        b^{full}_{+,T}=\mathscr A_T^*e^{t/2},
\]

then removes both Tate moments.  For primitive sources the current is

\[
        J_+(F)=\langle\rho_{+,T},F\rangle,
        \qquad
        \rho_{+,T}=P_T(e^{t/2}\Phi_{+,T}).
\]

The direct kernel identity that would force `J_+(F)=0`, namely
`\rho_(+,T)=0`, fails by an exact arithmetic jump residual.  This is a
calculated obstruction, not another variation statement.

## 1. Full adjoint kernel

Fix `T>log 2`, put `I_T=(-T,T)`, and extend sources by zero outside
`I_T`.  For `a>0`,

\[
        S_aF(t)=F(t-a),\qquad S_{-a}F(t)=F(t+a).
\]

Use the localized operator from P121:

\[
 \mathscr A_T
 =G_{\Gamma,T}-m_0I
  -\sum_{2\le n<e^{2T}}{\Lambda(n)\over\sqrt n}
       (S_{\log n}+S_{-\log n}),                    \tag{1.1}
\]

where

\[
 G_{\Gamma,T}
 =\int_0^\infty c_\Gamma(u)(2I-S_u-S_{-u})\,du,
 \qquad
 c_\Gamma(u)={e^{-u/2}\over1-e^{-2u}}.              \tag{1.2}
\]

Pairing (1.1) against `phi_+(t)=e^{t/2}` gives

\[
        M_+(\mathscr A_TF)=\langle b^{full}_{+,T},F\rangle.
        \tag{1.3}
\]

Up to changes at finitely many seam points,

\[
\boxed{
\begin{aligned}
b^{full}_{+,T}(t)=e^{t/2}\Bigg[
&\int_0^\infty c_\Gamma(u)
 \left(2-e^{u/2}\mathbf1_{t<T-u}
       -e^{-u/2}\mathbf1_{t>-T+u}\right)du\\
&-m_0
-\sum_{2\le n<e^{2T}}
 \left(\Lambda(n)\mathbf1_{t<T-\log n}
       +{\Lambda(n)\over n}\mathbf1_{t>-T+\log n}\right)
\Bigg].
\end{aligned}}                                      \tag{1.4}
\]

This is the literal `\mathscr A_T^*e^{t/2}` kernel.  The Gamma term may be
read in the form anti-dual; the reduced collar kernel below is an `L^2`
function with endpoint logarithms and finite jumps.

## 2. Reduction by the positive Tate moment

P121's resolved collar potential is

\[
        \widetilde b_{+,T}(t):=e^{t/2}\Phi_{+,T}(t), \tag{2.1}
\]

with

\[
\boxed{
\Phi_{+,T}(t)
=A_T(T-t)+B_T(T+t)+\Theta_T(T-t)+H_T(T+t)}
\tag{2.2}
\]

and

\[
\begin{aligned}
A_T(v)&={1\over2}\log {e^{4T}-1\over e^{2v}-1},\\
B_T(v)&={1\over2}\log {\tanh T\over\tanh(v/2)},\\
\Theta_T(x)&=\sum_{\substack{2\le n<e^{2T}\\ \log n\ge x}}\Lambda(n),\\
H_T(x)&=\sum_{\substack{2\le n<e^{2T}\\ \log n\ge x}}{\Lambda(n)\over n}.
\end{aligned}                                      \tag{2.3}
\]

The full adjoint kernel differs from the resolved collar kernel by only a
positive-Tate character:

\[
        b^{full}_{+,T}
        =\widetilde b_{+,T}+\kappa_{+,T}e^{t/2}.
        \tag{2.4}
\]

Here

\[
\boxed{
\begin{aligned}
\kappa_{+,T}={}&
\int_0^{2T}c_\Gamma(u)(2-e^{u/2}-e^{-u/2})du
+2\int_{2T}^{\infty}c_\Gamma(u)du\\
&-m_0-\sum_{2\le n<e^{2T}}
       \left(\Lambda(n)+{\Lambda(n)\over n}\right).
\end{aligned}}                                      \tag{2.5}
\]

Indeed, for each active `n`, the right-shift terms in (1.4) and (2.1)
differ by `-Lambda(n)e^(t/2)`, and the left-shift terms differ by
`-Lambda(n)e^(t/2)/n`.  The Gamma terms differ by the scalar in (2.5).
Thus, if `M_+(F)=0`,

\[
        M_+(\mathscr A_TF)
        =\langle\widetilde b_{+,T},F\rangle.        \tag{2.6}
\]

For primitive sources this recovers the exact `J_+` formula of
P121_RESOLVED_TATE_COLLAR_INTEGRAL.

## 3. Residual after both Tate moments

Let

\[
        \mathcal T_T=\operatorname{span}\{\phi_+,\phi_-\},
        \qquad \phi_\pm(t)=e^{\pm t/2},
\]

and let `P_T` be the `L^2(I_T)` projection onto `\mathcal T_T^\perp`.
Define

\[
\boxed{
        \rho_{+,T}:=P_T\widetilde b_{+,T}.}
        \tag{3.1}
\]

Equivalently,

\[
        \rho_{+,T}
        =\widetilde b_{+,T}-a_+(T)\phi_+-a_-(T)\phi_-,       \tag{3.2}
\]

where, with `S=sinh T`,

\[
\boxed{
\binom{a_+(T)}{a_-(T)}
={1\over2(S^2-T^2)}
\begin{pmatrix}S&-T\\-T&S\end{pmatrix}
\binom{\langle\widetilde b_{+,T},\phi_+\rangle}
      {\langle\widetilde b_{+,T},\phi_-\rangle}.}
\tag{3.3}
\]

The denominator is nonzero for `T>0`.  Hence every primitive source
satisfies

\[
\boxed{
        J_+(F)=M_+(\mathscr A_TF)
        =\langle\rho_{+,T},F\rangle .}
        \tag{3.4}
\]

For a parity `epsilon` state, only the matching parity component matters:

\[
        J_+(F)=\langle E_\epsilon\rho_{+,T},F\rangle,
        \qquad E_\epsilon={1\over2}(I+\epsilon R).  \tag{3.5}
\]

In the parity Tate convention
`r_epsilon(t)=c(e^{t/2}+epsilon e^{-t/2})`, P121's crossed Tate matrix
then gives

\[
        c={J_+(F)\over2(\sinh T+\epsilon T)}.       \tag{3.6}
\]

Thus `J_+(F)=0` is exactly the desired `c=0` conclusion on a parity
first-contact branch.

## 4. Failed kernel/retard identity

The elementary identity that would prove `J_+(F)=0` for every primitive
source is

\[
        \rho_{+,T}=0,
        \quad\text{equivalently}\quad
        \widetilde b_{+,T}\in\mathcal T_T.          \tag{4.1}
\]

This identity is false.  The Tate characters are continuous, while
`\widetilde b_(+,T)` has arithmetic jumps.  Away from seam collisions,

\[
\boxed{
\begin{aligned}
\Delta_{t=T-\log n}\widetilde b_{+,T}
 &=e^{(T-\log n)/2}\Lambda(n),\\
\Delta_{t=-T+\log n}\widetilde b_{+,T}
 &=-e^{(-T+\log n)/2}{\Lambda(n)\over n}.
\end{aligned}}                                      \tag{4.2}
\]

At a collision the jump is the sum of the displayed contributions.  The
projection by `\mathcal T_T` subtracts only continuous functions, so it
cannot remove any nonzero jump.

There is always such a nonzero jump.  At the seam `t=T-log2`, the right
contribution is `e^((T-log2)/2)log2`.  The only possible left collision
would come from an integer `m=e^(2T)/2`; if it occurs and `Lambda(m)` is
nonzero, its opposite contribution is
`e^((T-log2)/2)Lambda(m)/m`.  Since `T>log2` gives `m>2`, one has
`Lambda(m)/m<log2`.  Hence the combined jump at this seam is still
nonzero.  Therefore the primitive residual is not identically zero:

\[
        \rho_{+,T}\ne0.                              \tag{4.3}
\]

This is the exact residual term that breaks the naive retard identity
`\mathscr A_T^*e^{t/2}\in\mathcal T_T` modulo primitive moments.

## 5. What the first-contact equation would need to add

Let `F_*` be an attained first-contact minimizer.  Then

\[
        F_*\in\mathcal P_T,\qquad
        L_TF_*:=P_T\mathscr A_TP_TF_*=0,\qquad
        L_T\ge0.                                    \tag{5.1}
\]

By (3.4),

\[
        J_+(F_*)=\langle\rho_{+,T},F_*\rangle.       \tag{5.2}
\]

The first-contact equation gives only

\[
        \langle L_TG,F_*\rangle=0
        \qquad(G\in\mathcal Q_T\cap\mathcal P_T).   \tag{5.3}
\]

Therefore a kernel proof of `J_+(F_*)=0` must prove the range inclusion

\[
        \rho_{+,T}\in\overline{\operatorname{Ran}L_T}
        \quad\text{at the first-contact parameter}. \tag{5.4}
\]

For any concrete primitive candidate `G`, the exact remaining term is

\[
        \mathcal R_T(G):=\rho_{+,T}-L_TG,            \tag{5.5}
\]

and the first-contact equation gives

\[
\boxed{
        J_+(F_*)=\langle\mathcal R_T(G),F_*\rangle.}
        \tag{5.6}
\]

The zero-order retard identity (4.1) is the candidate `G=0`; its residual
is exactly `rho_(+,T)`, and (4.2) proves it does not vanish.  The next
possible progress would be an explicit arithmetic solve of (5.4), not
another scalar stationarity identity.

## 6. Signed estimate test

A signed estimate sufficient for this collar route is

\[
        |\langle\rho_{+,T},F\rangle|^2
        \le C_T\,q_T(F,F)
        \qquad(F\in\mathcal P_T\cap\mathcal Q_T).   \tag{6.1}
\]

At first contact it would force `J_+(F_*)=0`.  In operator terms, however,
this is exactly the assertion that `rho_(+,T)` has no projection onto
`ker L_T` and belongs to the corresponding form anti-dual range.  The
resolvent identity makes the residual explicit:

\[
        \langle\rho_{+,T},F_*\rangle
        =\lambda\langle(L_T+\lambda)^{-1}\rho_{+,T},F_*\rangle,
        \qquad \lambda>0.                            \tag{6.2}
\]

Letting `lambda downarrow 0` proves the collar cancellation only after an
independent arithmetic bound excluding a nonzero kernel projection of
`\rho_(+,T)`.  The evaluated kernel and the two Tate moments do not provide
that bound.

## 7. Verdict

The requested exact functional is

\[
        J_+(F)=\langle P_T(e^{t/2}\Phi_{+,T}),F\rangle
        \qquad(F\in\mathcal P_T).                   \tag{7.1}
\]

For parity `epsilon`, this is equivalent to the Tate coefficient through
(3.6).  The concrete identity tested here,
`\mathscr A_T^*e^{t/2}\in\mathcal T_T` after retard/collar reduction, is
false.  Its exact residual is `rho_(+,T)`, with the jump profile (4.2).

A proof of `c=0` from the first-contact minimizer must now either construct
the range inclusion (5.4) from arithmetic retard identities or prove the
signed estimate (6.1).  This note supplies the collar kernel and the exact
residual obstruction those attempts must overcome.
