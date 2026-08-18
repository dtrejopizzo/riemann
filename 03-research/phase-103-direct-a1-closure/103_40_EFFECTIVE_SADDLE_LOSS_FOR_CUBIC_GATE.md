# Effective saddle audit for the cubic Jensen gate

## Objective and outcome

Let
\[
 M_k=2\int_0^\infty u^k\Phi(u)\,du,
 \qquad c_N={M_{2N}\over(2N)!},                                  \tag{1}
\]
with the theta kernel of `103_34`.  The cubic gate of `103_36` is
\[
 d_N(d_N+d_{N+1})^2
 >r_N(d_N-d_{N+1})^2,                                           \tag{2}
\]
where \(r_N=c_{N+1}/c_N\) and \(d_N=r_N-r_{N+1}\).

This note tests a direct effective Laplace method.  The saddle is unique and
can be bracketed explicitly; the terms \(m\ge2\) in the theta series are
negligible there.  However, a Gaussian enclosure based on curvature gives a
relative error of natural size \((\log N)/N\), whereas the cubic
discriminant is a relative cancellation of third order, of size
approximately \(N^{-3}\).  Consequently the proposed one-saddle Gaussian
argument cannot certify (2).  A third-order *correlated* Laplace expansion,
with a uniform fourth-order remainder, is required before an explicit
threshold \(N_0\) can be asserted.

No threshold is claimed here.

## 1. The exact saddle is unique

For real \(k>0\), put
\[
 S_k(u)=k\log u+L(u),\qquad L(u)=\log\Phi(u).                     \tag{3}
\]
By `103_34`,
\[
 L''(u)<-4\pi e^{2u}+2.49<0.                                    \tag{4}
\]
Therefore
\[
 S_k''(u)=-{k\over u^2}+L''(u)<0.                               \tag{5}
\]
Moreover \(S_k'(u)\to+\infty\) as \(u\downarrow0\), while the
factor \(e^{-\pi e^{2u}}\) gives \(S_k'(u)\to-\infty\) as
\(u\to\infty\).  Hence there is a unique saddle \(u_k>0\), determined
exactly by
\[
 {k\over u_k}+L'(u_k)=0.                                        \tag{6}
\]

For the first theta summand, with \(x=\pi e^{2u}\),
\[
 \ell_1'(u)={5\over2}+{4x\over2x-3}-2x.                         \tag{7}
\]
Since \(4x/(2x-3)=2+O(x^{-1})\), its saddle equation is
\[
 2\pi e^{2u}={k\over u}+{9\over2}+O(e^{-2u}).                   \tag{8}
\]
It follows directly, by evaluating the two sides at constant multiples of
\(\log(k+2)\), that
\[
 u_k={1\over2}\log k-{1\over2}\log\log k+O(1).                 \tag{9}
\]
This qualitative bracket can be made numerical using only monotonicity in
(6); it is not the source of the loss below.

## 2. The other theta summands are not the obstruction

The estimates proved in `103_34` give, for \(x=\pi e^{2u}\),
\[
 R(u):={\sum_{m\ge2}f_m(u)\over f_1(u)}
 \le2\sum_{m\ge2}m^4e^{-(m^2-1)x}.                              \tag{10}
\]
The first term is \(32e^{-3x}\), and the rest is bounded by a geometric
tail once \(x\ge\pi\).  At the saddle, (8)--(9) give
\[
 x_k\asymp {k\over\log k},
\]
so
\[
 R(u_k)\le
 \exp\left(-{3k\over C\log k}\right)                           \tag{11}
\]
for an explicit constant \(C\) beyond an explicit elementary threshold.
The same estimate, multiplied by fixed powers of \(m^2x\), controls any
fixed number of derivatives.  Thus replacing \(L\) by \(\ell_1\) in a
finite-order saddle expansion costs less than every power of \(k^{-1}\).
The difficulty is the precision of the saddle expansion itself, not the
theta sum over \(m\).

## 3. Natural Gaussian scale and its error

Let
\[
 A_k=-S_k''(u_k)>0.                                              \tag{12}
\]
Equations (4), (8), and (9) give the scales
\[
 A_k\asymp {k\over u_k},\qquad
 \sigma_k=A_k^{-1/2}\asymp\sqrt{u_k\over k}.                    \tag{13}
\]
For the dominant summand, differentiation of (7) shows
\[
 S_k^{(3)}(u_k)=O(k/u_k),\qquad
 S_k^{(4)}(u_k)=O(k/u_k),                                       \tag{14}
\]
and similarly for every fixed higher derivative.  On the Gaussian scale,
the standardized cubic and quartic terms therefore have sizes
\[
 {S_k^{(3)}\over A_k^{3/2}}
 =O\left(\sqrt{u_k/k}\right),qquad
 {S_k^{(4)}\over A_k^2}=O(u_k/k).                               \tag{15}
\]
The odd cubic contribution integrates to zero in the symmetric leading
Gaussian approximation, but its square and the quartic term give a first
relative correction of size
\[
 \eta_k={u_k\over k}\asymp{\log k\over k}.                      \tag{16}
\]
Thus a curvature-only enclosure has the form
\[
 M_k=e^{S_k(u_k)}\sqrt{2\pi/A_k}\,[1+O(\eta_k)],                \tag{17}
\]
even after the tails outside a fixed Gaussian window are made
exponentially small.  The constant in (17) can be made explicit by Taylor
remainders, but doing so does not improve its order.

## 4. Precision demanded by the cubic discriminant

Let
\[
 g_N=\log c_N.
\]
The saddle scales (9), (13) imply at leading order
\[
 r_N=e^{g_{N+1}-g_N}\asymp {u_{2N}^2\over(2N)^2},               \tag{18}
\]
and
\[
 {d_N\over r_N}=1-{r_{N+1}\over r_N}=\Theta(N^{-1}),qquad
 {d_N-d_{N+1}\over d_N}=O(N^{-1}).                              \tag{19}
\]
Substitution in the exact factorization from `103_36`,
\[
 {\Delta_N\over27c_N^4}
 =r_N^2r_{N+1}\left[
 d_N(d_N+d_{N+1})^2-r_N(d_N-d_{N+1})^2\right],                 \tag{20}
\]
shows that the bracket is a cancellation on the relative scale
\[
 {d_N^3\over r_N^3}=\Theta(N^{-3}).                             \tag{21}
\]
This is the decisive precision requirement.

If the four moments \(M_{2N},M_{2N+2},M_{2N+4},M_{2N+6}\) are enclosed
independently using (17), their relative uncertainty is
\[
 O\left({\log N\over N}\right),                                \tag{22}
\]
which is larger than (21) by approximately \(N^2\log N\).  Interval
subtraction cannot recover the sign: the five quartic terms in the
discriminant each inherit the error (22) before canceling.

The same issue appears if one first forms ratios.  Independent relative
intervals of width \(O(\eta_k)\) do not even certify the size
\(d_N/r_N=\Theta(N^{-1})\) once the harmless logarithmic factor in (22) is
retained, much less the difference \(d_N-d_{N+1}\).

## 5. What an effective eventual proof would require

A workable saddle proof must expand the *single smooth function*
\(k\mapsto\log M_k\), rather than bound four moments independently.  In
view of (16) and (21), it must include at least the first three Laplace
corrections and prove a correlated remainder of the form
\[
 E(k)=O\left((\log k/k)^4\right),                                \tag{23}
\]
with corresponding derivative or finite-difference bounds for
\(E(k+2)-E(k)\).  Only then is the remainder eventually smaller than the
\(N^{-3}\) discriminant scale.

Concretely, completion requires all of the following.

1. Explicit brackets for \(u_k\) and \(A_k\), uniform for four consecutive
   even values of \(k\).
2. Taylor coefficients through at least order eight at the moving saddle,
   because the third Laplace correction contains derivatives through that
   order.
3. A common majorant for the Taylor remainder on a Gaussian window and an
   explicit strong-concavity tail bound outside it.
4. Finite-difference bounds for the resulting remainder, not merely four
   independent absolute bounds.
5. An explicit positive lower bound for the main expression in (20), then
   an explicit crossing threshold \(N_0\).

The elementary curvature estimate of `103_34` supplies items 1 and the tail
part of item 3, and (10)--(11) remove the higher theta summands.  It does not
supply items 2, 4, or 5.  Therefore the requested eventual theorem and a
numerical \(N_0\) do not follow from Gaussian interval control alone.

## Status

The saddle route is viable only after a substantially higher-order,
correlated effective Laplace calculation.  The exact present loss is
\[
 \boxed{\quad
 \text{available Gaussian relative error }O((\log N)/N)
 \quad\text{versus required cubic scale }\Theta(N^{-3}).\quad}
\]
No numerical fit or unproved asymptotic remainder has been promoted to an
eventual certificate.
