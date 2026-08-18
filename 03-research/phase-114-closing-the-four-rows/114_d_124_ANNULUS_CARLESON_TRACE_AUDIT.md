# D.124 — Joint annulus trace for a dyadic contact block

## Verdict

In boundary coordinates, every contact in a dyadic block is an evaluation
of the same convolution of the right and left endpoint traces.  The exact
sampling points are nested in \([0,\log2]\).  The corresponding weighted
trace map is bounded, but its squared norm is of order the full block mass

\[
 W_Y=\sum_{Y<n\le2Y}{\Lambda(n)\over\sqrt n},           \tag{0.1}
\]

not its square-root or a uniform constant.  Nesting makes the frame vectors
positively correlated.

The nonlocal Gamma form does not improve this asymptotic.  Its high-frequency
symbol grows only logarithmically, and fixed smooth endpoint profiles have
Gamma energy independent of \(Y\), while their dyadic trace mass grows like
the mass of the sampled contacts.  The two Tate conditions can be imposed
inside the endpoint profiles without changing this conclusion.

Therefore a Gamma-controlled Carleson estimate cannot close the block Schur
capacity.  Earlier arithmetic blocks must contribute a capacity of the same
order as \(W_Y\).

## 1. Exact annulus coordinates

Set

\[
 X=e^{2T},\qquad
 R_T(x)=F(T-x),\qquad L_T(x)=F(-T+x).                   \tag{1.1}
\]

For \(n\le X\), put

\[
 a_n=\log n,qquad \delta_n=2T-a_n=\log(X/n).          \tag{1.2}
\]

A change of variables gives the exact contact formula

\[
 \boxed{
 \langle F,S_{a_n}F\rangle
 =\int_0^{\delta_n}R_T(x)
        \overline{L_T(\delta_n-x)}\,dx.}                \tag{1.3}
\]

At the end of the dyadic block, \(X=2Y\), all \(Y<n\le2Y\) satisfy

\[
 0\le\delta_n<\log2.                                   \tag{1.4}
\]

Thus the block is a weighted sampling of the single convolution

\[
 c_{R,L}(\delta)=int_0^\delta R(x)\overline{L(\delta-x)}\,dx. \tag{1.5}
\]

## 2. The weighted trace map

Let

\[
 \mu_Y=\sum_{n\in\mathcal N_Y}w_n\delta_{\delta_n},
 \qquad w_n={\Lambda(n)\over\sqrt n}.                  \tag{2.1}
\]

For fixed \(L\in L^2(0,D)\), \(D=\log2\), define

\[
 (\mathcal T_{Y,L}R)_n
 =\sqrt{w_n}\,c_{R,L}(\delta_n).                       \tag{2.2}
\]

Cauchy--Schwarz gives

\[
 |c_{R,L}(\delta)|\le\|R\|_{L^2(0,D)}\|L\|_{L^2(0,D)}, \tag{2.3}
\]

and hence

\[
 \boxed{
 \|\mathcal T_{Y,L}\|^2\le W_Y\|L\|^2.}             \tag{2.4}
\]

This upper bound has full \(\ell^1\) block mass.

It is sharp in scale.  Take

\[
 R=L=D^{-1/2}1_{[0,D]}.                                \tag{2.5}
\]

Then \(c_{R,L}(\delta)=\delta/D\), so

\[
 \|\mathcal T_{Y,L}R\|^2
 ={1\over D^2}\sum_{n\in\mathcal N_Y}w_n\delta_n^2. \tag{2.6}
\]

For every \(0<d<D\), writing

\[
 W_Y(d)=\sum_{\substack{n\in\mathcal N_Y\\
                         \delta_n\ge d}}w_n,           \tag{2.7}
\]

gives the exact lower bound

\[
 \boxed{
 \|\mathcal T_{Y,L}\|^2\ge {d^2\over D^2}W_Y(d).}    \tag{2.8}
\]

Whenever a fixed interior subblock carries a positive fraction of the block
mass, (2.4) and (2.8) show that the squared trace norm is \(\Theta(W_Y)\).
No prime asymptotic is needed for the exact statement (2.8).

## 3. Nesting creates a positive Gram matrix

For fixed \(L\), the evaluation vector at \(\delta\) is

\[
 v_\delta(x)=1_{[0,\delta]}(x)\overline{L(\delta-x)}.   \tag{3.1}
\]

The frame operator is

\[
 \mathcal T_{Y,L}^*\mathcal T_{Y,L}
 =\sum_nw_n|v_{\delta_n}\rangle\langle v_{\delta_n}|. \tag{3.2}
\]

For the nonnegative profile (2.5), all inner products
\(\langle v_\delta,v_\eta\rangle\) are nonnegative and the supports are
nested.  Thus batching does not create phase orthogonality; it creates a
positive Hankel/Volterra Gram block.

## 4. Gamma regularity is insufficient for a uniform trace constant

The Gamma form has multiplier

\[
 \ell_\infty(\tau)
 =\operatorname{Re}\psi(1/4+i\tau/2)-\psi(1/4).        \tag{4.1}
\]

At high frequency,

\[
 \ell_\infty(\tau)=\log|\tau|+O(1),                    \tag{4.2}
\]

while at low frequency it is quadratic.  Hence its form domain has only
logarithmic high-frequency control, weaker than a positive Sobolev trace
exponent.  Atomic boundary evaluation is not uniformly controlled by Gamma
energy alone.

More concretely, replace (2.5) by fixed smooth nonnegative profiles supported
in \((0,D)\).  Their Gamma energy is a finite constant depending only on the
profiles, not on \(Y\).  If their convolution is bounded below on
\([d,D-d]\), then

\[
 \sum_nw_n|c_{R,L}(\delta_n)|^2\ge c_{R,L,d}W_Y(d),     \tag{4.3}
\]

whereas the available Gamma energy remains \(O_{R,L}(1)\).  Thus any Gamma
trace constant is at least a fixed multiple of \(W_Y(d)\).

## 5. The two Tate moments do not remove endpoint coherence

The primitive constraint can be imposed source-wise by choosing

\[
 F=(\partial_t^2-\tfrac14)u                             \tag{5.1}
\]

with \(u\) a sum of smooth endpoint profiles.  Then integration by parts
gives \(M_\pm(F)=0\) exactly and preserves compact support.  Choosing the two
endpoint pieces compatibly leaves a nonzero convolution on an interior
\(\delta\)-interval.

Equivalently, one may impose the weighted endpoint mean-zero conditions and
solve the remaining two exponentially small cross-end equations.  These
are only two linear constraints on infinite-dimensional endpoint spaces;
they do not annihilate the Volterra frame (3.2).

Therefore (2.8)--(4.3) persist, with different fixed constants, on the
primitive source.

## 6. Consequence for the block Schur capacity

The contact contribution of the dyadic block is

\[
 2\operatorname{Re}\sum_nw_n c_{R_T,L_T}(\delta_n).    \tag{6.1}
\]

Young's inequality can bound (6.1) using the trace norm (2.4), but it spends
a coefficient of order \(W_Y\).  Gamma alone supplies no matching uniform
capacity by Section 4.

Thus the block inequality

\[
 D_Y-B_Y^*A_Y^\dagger B_Y\ge K_Y^{\rm ann}             \tag{6.2}
\]

cannot follow from a standalone Hardy/Carleson trace theorem for the Gamma
boundary.  The left side must receive an order-\(W_Y\) contribution from
earlier arithmetic contacts, with the correct correlation against the
nested frame.

## 7. Conclusion

The annulus calculation identifies the exact trace operator and its size:

\[
 \boxed{
 \|\mathcal T_{Y,L}\|^2\le W_Y\|L\|^2,
 \qquad
 \|\mathcal T_{Y,L}\|^2\ge{d^2\over(\log2)^2}W_Y(d).}
\]

The dyadic contacts are nested and coherent; Gamma nonlocality does not turn
them into a uniformly Carleson family.  Hence boundary trace estimates alone
do not close the block capacity.  The missing estimate remains a joint
arithmetic Schur cancellation across scales.

