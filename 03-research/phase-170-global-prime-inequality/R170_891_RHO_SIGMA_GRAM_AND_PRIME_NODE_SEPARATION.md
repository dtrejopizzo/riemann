# R170_891 — Gram matrix of rho/sigma and separation by prime nodes

## 0. Doubly audited theorem

In each real parity sector, the static and moving Tate coordinates
have explicit primitive representatives. For the physical operator
`A_M`, these representatives are linearly independent on the whole
primitive space as soon as the route `d=2` is active.

Let

\[
 b_\epsilon(t)=e^{-t/2}+\epsilon e^{t/2},
 \qquad
 g_\epsilon=4(\sinh T+\epsilon T),                        \tag{0.1}
\]

and, within the sector `epsilon`,

\[
 \Pi_\epsilon u=u-b_\epsilon{(b_\epsilon,u)\over g_\epsilon}.\tag{0.2}
\]

Then

\[
\boxed{
 a_\epsilon={1\over g_\epsilon}\Pi_\epsilon PA_Mb_\epsilon,
 \qquad \rho_F=(a_\epsilon,F),}                          \tag{0.3}
\]

\[
\boxed{
 s_\epsilon=-2\Pi_\epsilon(t b_\epsilon'),
 \qquad \sigma_\epsilon(F)=(s_\epsilon,F).}             \tag{0.4}
\]

For every `T>log(2)/2` and stabilized cutoff,

\[
\boxed{\det G(a_\epsilon,s_\epsilon)>0.}                 \tag{0.5}
\]

The proof of (0.5) uses a node produced by the integer `2`; it does not rely
on an estimate or a spectral margin.

## 1. Representatives

If `F` is primitive and `PA_MF=rho_F b_epsilon`, the symmetry of `A_M` gives

\[
 g_\epsilon\rho_F=(b_\epsilon,PA_MF)=(PA_Mb_\epsilon,F), \tag{1.1}
\]

which proves (0.3). For `M>=e^(2T)`,

\[
 PA_Mb_\epsilon=P\mathcal M b_\epsilon
 -\sum_{2\le d<e^{2T}}{\Lambda(d)\over\sqrt d}
  P(\tau_{\log d}+\tau_{-\log d})b_\epsilon.              \tag{1.2}
\]

Hence `a_epsilon` stabilizes with `M`; the tail `R_M` does not enter
this interior coordinate.

R170_845 gives `dot b_epsilon=t b_epsilon'` and

\[
 \dot\Pi F=-b_\epsilon{(\dot b_\epsilon,F)\over g_\epsilon}.\tag{1.3}
\]

Hence `sigma=2 Re(dotPi F,b)` produces (0.4). In pointwise form,

\[
 s_\epsilon(t)=-2t b_\epsilon'(t)
 +{T\cosh T-\sinh T\over\sinh T+\epsilon T}b_\epsilon(t).\tag{1.4}
\]

## 2. Exact determinant

Set

\[
 u=PA_Mb_\epsilon,\quad d=(b_\epsilon,\dot b_\epsilon),
 \quad E=\|\dot b_\epsilon\|^2,
\]

\[
 u_0=(b_\epsilon,u),\qquad u_1=(u,\dot b_\epsilon).       \tag{2.1}
\]

Then

\[
 \|a_\epsilon\|^2={1\over g_\epsilon^2}
 \left(\|u\|^2-{u_0^2\over g_\epsilon}\right),          \tag{2.2}
\]

\[
 \|s_\epsilon\|^2=4\left(E-{d^2\over g_\epsilon}\right),
 \qquad
 (a_\epsilon,s_\epsilon)=-{2\over g_\epsilon}
 \left(u_1-{u_0d\over g_\epsilon}\right).               \tag{2.3}
\]

Consequently

\[
\boxed{
\begin{aligned}
 \det G(a_\epsilon,s_\epsilon)={4\over g_\epsilon^2}
 \bigg[&\left(\|u\|^2-{u_0^2\over g_\epsilon}\right)
       \left(E-{d^2\over g_\epsilon}\right)\\
 &-\left(u_1-{u_0d\over g_\epsilon}\right)^2\bigg].
\end{aligned}}                                           \tag{2.4}
\]

The geometric scalars are

\[
 d=2(T\cosh T-\sinh T),                                  \tag{2.5}
\]

\[
 E=T^2\sinh T-2T\cosh T+2\sinh T
   -\epsilon{T^3\over3}.                                 \tag{2.6}
\]

In particular `s_epsilon` is not zero.

## 3. Separation via the node of 2

Suppose `T>log(2)/2`. The point

\[
 x_0=T-\log2\in(-T,T)                                    \tag{3.1}
\]

is the interior endpoint of the route
`-ell_2 b(t+log2)`, with `ell_d=Lambda(d)/sqrt d`. There the
route produces jumps in value and derivative

\[
 \ell_2b_\epsilon(T),\qquad \ell_2b_\epsilon'(T).        \tag{3.2}
\]

The only possible collision is the reflected entry of
`d'=e^(2T)/2`, when this is an active prime power. There are no
multi-collisions because `log` is injective. The total jumps are

\[
 b_\epsilon(T)(\ell_2-\epsilon\ell_{d'}),
 \qquad
 b_\epsilon'(T)(\ell_2+\epsilon\ell_{d'}).               \tag{3.3}
\]

For `epsilon=-1`, the value jump cannot vanish. For
`epsilon=+1`, if the value jump vanishes, the derivative jump is
strictly positive. Hence `PA_Mb_epsilon` keeps either a jump or an
interior kink.

The term `P mathcal M b_epsilon` is smooth in the interior by
pseudolocality; this is also verified directly with the kernel of
R170_806. The projection `Pi_epsilon` only subtracts an analytic multiple
of `b_epsilon`. By contrast `Pi_epsilon dot b_epsilon` is analytic. Hence
the two representatives cannot be proportional, which proves (0.5).

At a threshold `e^(2T)=p^k`, the nascent route acts on a set of measure
zero. Crossing it, it appears in a collar of length `O(delta)`;
the dependence is continuous in `L2`, but does not authorize a uniform
derivative. At thresholds after the first, the route `2` already remains
active.

## 4. Exact limit of the theorem

Minimality acts on the spectral projections

\[
 a_\epsilon^0=\mathsf Z_Ta_\epsilon,
 \qquad s_\epsilon^0=\mathsf Z_Ts_\epsilon.              \tag{4.1}
\]

Independence on the whole primitive space does not imply independence
after projecting onto the radical. If the radical is one-dimensional, both
projections are automatically collinear. The determinant

\[
 \|\mathsf Za_\epsilon\|^2\|\mathsf Zs_\epsilon\|^2
 -|(\mathsf Za_\epsilon,\mathsf Zs_\epsilon)|^2           \tag{4.2}
\]

is not decided by the current identities. It is not substituted by the
primitive determinant of (0.5).

```text
primitive representatives of rho and sigma                 PROVED
exact Gram matrix                                           PROVED
primitive independence for T>log(2)/2                        PROVED TWICE
independence after radical projection                        OPEN / FALSE IN DIM 1
signed rho--sigma--Omega relation on the radical              OPEN
VIR--LB / D                                                   OPEN
```
