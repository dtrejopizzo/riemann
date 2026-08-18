# D.84 — Bilateral landing and the two Tate boundary states

## Status

D.83 shows that a zero-initial-state pure Hankel correction misses a
Toeplitz feedthrough.  This note allows a full bi-infinite conservative
trajectory with initial and final states and asks whether the two Tate jets
cancel those states.

The bilateral energy identity is exact.  Its boundary is the difference
`||x_-||^2-||x_+||^2`.  The two primitive moments cancel the two polar
coordinates, but they cannot determine the complete Poisson boundary
state: an operator which factors only through the two moments has rank at
most two, whereas the Fourier--Poisson boundary block has infinite rank and
remains nonzero on primitive approximants.

There is a genuine global cancellation at the scalar feedthrough level.
The Bohr constant of the finite prime product is
`prod_(p<Q)(1-1/p)` and tends to zero; the Gamma scattering factor has zero
Cesaro mean, so the assembled scalar mean also vanishes.  This removes the
single coefficient which obstructed the discrete local equation in D.83.
It does not remove the infinite Toeplitz row/column or the nonpolar boundary
state.

Consequently a bilateral conservative realization yields either equality
when both states vanish, or the unresolved difference of the two nonpolar
state norms.  The next structure must be a two-boundary scattering
cohomology on the critical strip, in which the incoming and outgoing
nonpolar states are actual cohomology objects and the Tate jets form only
their polar quotient.

No RH, Pick positivity, or sign-selected state is used.  The paper is not
modified.

## 1. Bilateral conservative energy

Let

\[
 \mathcal U=\begin{pmatrix}T&G\\H&R\end{pmatrix}           \tag{1.1}
\]

be the full unitary Fourier--Poisson colligation.  For `n in Z`, consider

\[
 \begin{aligned}
 x_{n+1}&=Tx_n+Gu_n,\\
 y_n&=Hx_n+Ru_n.                                           \tag{1.2}
 \end{aligned}
\]

Unitarity gives

\[
 \|x_n\|^2+\|u_n\|^2
 =\|x_{n+1}\|^2+\|y_n\|^2.                               \tag{1.3}
\]

Summing from `-N` to `N` yields

\[
 \boxed{
 \sum_{n=-N}^N(\|y_n\|^2-\|u_n\|^2)
 =\|x_{-N}\|^2-\|x_{N+1}\|^2.}                           \tag{1.4}
\]

If the two state limits exist in norm, then

\[
 \sum_{n\in\mathbb Z}(\|y_n\|^2-\|u_n\|^2)
 =\|x_-\|^2-\|x_+\|^2.                                   \tag{1.5}
\]

Thus allowing both boundary states does not automatically improve the
sign:

* `x_-=0` gives a contraction, with defect `||x_+||^2`;
* `x_+=0` gives the opposite inequality;
* `x_-=x_+=0` gives equality, not the strict row-D form;
* arbitrary bilateral scattering leaves the difference in (1.5).

For the desired landing `u=J_-F`, `y=K_+F`, equation (1.5) would identify

\[
 B_{\rm nuc}(F,F)=\|x_-(F)\|^2-\|x_+(F)\|^2.              \tag{1.6}
\]

It is an exact boundary-state reformulation only after the landing itself
has been proved.

### 1.1 The Schur tower is not the conservative output

There is a further typing issue before taking limits.  From the unitary
blocks,

\[
 C=T^*T=I-H^*H.                                           \tag{1.7}
\]

Let `H=V_H D_T` be the polar decomposition, where

\[
 D_T=(I-T^*T)^{1/2}.                                      \tag{1.8}
\]

Starting the conservative system with a state `z` and zero input gives

\[
 y_j^{\rm cons}=HT^jz=V_HD_TT^jz.                          \tag{1.9}
\]

Up to the fixed factor and index convention of D.80, the Schur tower is

\[
 y_j^{\rm Schur}={1\over2}V_HD_T(T^*T)^{j/2}z.             \tag{1.10}
\]

Thus identifying the two outputs would require

\[
 D_T\bigl(T^j-(T^*T)^{j/2}\bigr)z=0                       \tag{1.11}
\]

on the landed primitive states.  This is not an operator identity.

For the local symbol `v_r`, the two Hankel blocks satisfy

\[
 H^*H=r^2P_{e_0},
 \qquad GG^*=r^2P_{h_r},                                  \tag{1.12}
\]

where

\[
 h_r=\sqrt{1-r^2}(1,r,r^2,\ldots)\ne e_0.                 \tag{1.13}
\]

Consequently

\[
 T^*T-TT^*=r^2(P_{h_r}-P_{e_0})\ne0.                      \tag{1.14}
\]

The Toeplitz state operator is nonnormal already at one prime.  Hence
`K_+` is not a compression of the canonical conservative output by formal
unitarity.  A landing theorem must prove (1.11) on the actual primitive
image, or construct a state model whose evolution is `|T|` rather than
`T`.

## 2. What the two jets can cancel

Put

\[
 M(F)=(M_-(F),M_+(F))\in\mathbb C^2.                       \tag{2.1}
\]

Any boundary contribution determined solely by the two Tate jets factors
as

\[
 F\xmapsto{M}\mathbb C^2\xrightarrow{A}\mathcal X.        \tag{2.2}
\]

It therefore has rank at most two.  In particular, if the boundary states
split as

\[
 x_\pm(F)=A_\pm M(F)+x_\pm^0(F),                           \tag{2.3}
\]

then primitivity cancels `A_pm M(F)` but leaves

\[
 x_\pm(F)=x_\pm^0(F).                                     \tag{2.4}
\]

D.77 computes the actual Fourier--Poisson boundary operator

\[
 Q_\Lambda\widehat P_\Lambda P_\Lambda.                   \tag{2.5}
\]

It has infinite rank on every nontrivial archimedean window.  Moreover,
the primitive approximate identity of D.75 converges strongly to the
identity.  If (2.5) factored through `M`, it would vanish on the primitive
ideal; strong approximation would then force it to vanish on the full
cyclic representation, a contradiction.

> **Proposition 2.1 (rank-two boundary no-go).**  The two Tate jets can
> remove the polar rank-two state but cannot cancel or determine the full
> incoming/outgoing Poisson state.  Any bilateral landing theorem must
> construct the nonpolar states `x_-^0,x_+^0` in addition to imposing
> `M_-=M_+=0`.

After primitivity, the energy boundary is therefore

\[
 \boxed{
 \|x_-^0(F)\|^2-\|x_+^0(F)\|^2,}                          \tag{2.6}
\]

not zero by formal jet cancellation.

## 3. Prime feedthrough before stabilization

For one prime, with `r_p=p^(-1/2)`, the zero Fourier coefficient of

\[
 v_p(z)={1-r_pz^{-1}\over1-r_pz}                           \tag{3.1}
\]

is

\[
 c_0(v_p)=1-r_p^2=1-{1\over p}.                            \tag{3.2}
\]

Let `P_Q={p:p<Q}`.  The logarithms of distinct primes are rationally
independent over the integers: a relation
`sum_p n_p log p=0` would give `prod_p p^(n_p)=1`, hence every `n_p=0`.
Therefore the only way to obtain total frequency zero in the finite product
is to choose frequency zero in every factor.  Its Bohr coefficient is

\[
 \boxed{
 c_0\left(\prod_{p<Q}v_p\right)
 =\prod_{p<Q}\left(1-{1\over p}\right).}                  \tag{3.3}
\]

Euler's divergence of `sum_p 1/p` gives

\[
 \prod_{p<Q}(1-p^{-1})\longrightarrow0.                   \tag{3.4}
\]

Thus the local feedthrough obstruction `1-r^2` of D.83 disappears in the
directed all-prime scalar mean.

This is only one coefficient.  At every finite `Q`, the Toeplitz row and
column contain all nonzero prime frequencies, and their rank grows with
`Q`.  Equation (3.4) does not imply convergence of those operators to zero.

## 4. Gamma has zero Cesaro feedthrough

Write

\[
 u_\infty(\tau)=e^{i\phi(\tau)}
 =\pi^{i\tau}{\Gamma(1/4-i\tau/2)\over
                    \Gamma(1/4+i\tau/2)}.                 \tag{4.1}
\]

Stirling's formula gives

\[
 \phi'(\tau)
 =\log\pi-\operatorname {Re}\psi(1/4+i\tau/2)
 =-\log|\tau|+O(1),                                       \tag{4.2}
\]

and

\[
 \phi''(\tau)=O(|\tau|^{-1}).                             \tag{4.3}
\]

For every fixed real frequency `lambda`, integration by parts outside a
fixed compact interval, where
`|phi'(tau)+lambda|` is comparable to `log|tau|`, gives

\[
 {1\over2T}\int_{-T}^T
 u_\infty(\tau)e^{i\lambda\tau}\,d\tau\longrightarrow0.   \tag{4.4}
\]

The Fourier series of every finite prime product is absolutely convergent.
Approximating it by a finite trigonometric polynomial and applying (4.4)
termwise proves

\[
 \boxed{
 \operatorname {Mean}_{\rm Cesaro}\Theta_{P_Q}=0}          \tag{4.5}
\]

for the assembled finite-prime--Gamma symbol.

Thus in the natural scalar mean audit, Gamma also removes the zero-time
feedthrough.  In the continuous Hardy model there is no distinguished
single constant basis vector, so (4.5) is a statement about the scalar
renormalized mean, not vanishing of the full Toeplitz edge operator.

## 5. Why the nonzero-frequency edge remains

The local phase identity is

\[
 {1\over i}{d\over d\tau}\log\Theta_{P_Q}(\tau)
 =m_\infty(\tau)+\sum_{p<Q}\log p
 \sum_{k\ne0}p^{-|k|/2}e^{ik\tau\log p}.                  \tag{5.1}
\]

Equation (5.1) displays every nonzero prime-power frequency in both
orientations.  The Gamma term is a continuous archimedean distribution;
it does not turn the growing finite-prime Toeplitz edge into a rank-two
operator.  Removing only the scalar mean in Sections 3--4 leaves the
annulus cocycle and its infinite-rank limit from D.77.

There is also no uniform one-sided Hardy factorization of the finite
symbols.  Writing

\[
 \prod_{p<Q}v_p={B_Q\over Z_Q},
 \qquad
 Z_Q(\tau)=e^{i\tau\sum_{p<Q}\log p},                      \tag{5.2}
\]

shows that the denominator winding grows with `Q`.  Multiplying it away
changes (5.1) by

\[
 -\sum_{p<Q}\log p,                                       \tag{5.3}
\]

the total torsor channel.  Hence scalar feedthrough cancellation does not
license deletion of the opposite Hardy orientation.

## 6. Bilateral landing with a forcing cocycle

If the desired primitive input and output do not satisfy the exact state
recursion, put

\[
 r_n=x_{n+1}-Tx_n-Gu_n.                                   \tag{6.1}
\]

The finite bilateral identity becomes

\[
 \begin{aligned}
 \sum_{n=-N}^N(\|y_n\|^2-\|u_n\|^2)
 ={}&\|x_{-N}\|^2-\|x_{N+1}\|^2\\
 &+\sum_{n=-N}^N
 \left(2\operatorname {Re}\langle x_{n+1},r_n\rangle
       -\|r_n\|^2\right).                                \tag{6.2}
\end{aligned}
\]

The cutoff-annulus cocycle of D.81 is the concrete `r_n` for the attempted
landing.  Neither the two moments nor the scalar cancellation (4.5) makes
the last line vanish.

Therefore the exact A--B--C form would have the boundary decomposition

\[
 \begin{aligned}
 B_{\rm nuc}(F,F)
 ={}&\|x_-^0(F)\|^2-\|x_+^0(F)\|^2\\
 &+\sum_n
 \left(2\operatorname {Re}\langle x_{n+1}(F),r_n(F)\rangle
       -\|r_n(F)\|^2\right),                              \tag{6.3}
\end{aligned}
\]

provided the proposed bilateral realization is trace-exact.  Formula
(6.3) identifies what must be constructed; it has no formal sign.

## 7. The correct next coefficient category

The natural analytic domain is not a single Hardy half-plane.  The two
characters `M_-` and `M_+` are the two boundary evaluations associated to
the strip

\[
 0\le\operatorname {Re}s\le1.                             \tag{7.1}
\]

The semilocal scattering factor is a transition between the two oriented
boundaries, and the primitive source is the kernel of the two polar
evaluations.  This suggests a two-sided scattering complex

\[
 \mathcal H_{\rm in}
 \xrightarrow{\ \mathcal S_{\rm Pois}\ }
 \mathcal H_{\rm out}
 \longrightarrow\mathcal H_{\rm Sonin},                  \tag{7.2}
\]

with an exact polar quotient

\[
 \mathbb C\{M_-,M_+\}.                                    \tag{7.3}
\]

The missing theorem is to construct `x_-^0,x_+^0` as the two boundary
cohomology classes of (7.2), prove the forcing cocycle exact in that
complex, and derive the required norm comparison from a duality on
`H_Sonin`.  The rank argument in Section 2 shows that (7.2) cannot be
replaced by the two-dimensional quotient (7.3).

## 8. Conclusion

Allowing initial and final states repairs the typing of the Redheffer
system but does not prove the row-D sign.  The bilateral energy boundary is
the difference of two state norms.  Primitivity removes two polar
coordinates, not the infinite-dimensional Poisson boundary state.

The scalar global feedthrough does vanish under the natural prime and Gamma
means.  This is a real cancellation, but it does not cancel the remaining
Toeplitz edge or the forcing cocycle.  The next viable construction is a
two-boundary scattering/cohomology quotient on the critical strip, with the
Tate jets as its polar quotient and an independently proved duality on the
nonpolar state space.  It must also resolve (1.11): conservative evolution
uses `T`, while the Schur tower uses its modulus `|T|`.
