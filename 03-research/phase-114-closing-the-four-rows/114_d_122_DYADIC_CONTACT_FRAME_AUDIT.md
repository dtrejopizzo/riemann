# D.122 — Dyadic batching of prime-power contacts

## Verdict

Batching all contacts in \((Y,2Y]\) gives an exact operator-valued Schur
capacity, but it does not produce a Bessel/square-root gain from translation
phases.  The batch is maximally coherent at real frequency \(\tau=0\): every
translation has phase one, so the norm of the positive contact sum is its
full \(\ell^1\) mass, not its \(\ell^2\) mass.

The two Tate conditions do not remove this coherent channel.  They impose
Fourier--Laplace vanishing at \(\tau=\pm i/2\), while compactly supported
primitive functions may have nonzero Fourier value at \(0\).  Moreover the
Gamma multiplier vanishes quadratically at \(0\), so no Loewner domination
of the coherent batch by the Gamma tail is possible with a finite uniform
constant.

In physical space the same obstruction is endpoint coherence: all shifts
in a dyadic block carry a bounded right boundary strip into a bounded left
boundary strip, and nonnegative endpoint tests align their correlations.
Thus a block capacity can only improve on prime-by-prime payment if earlier
arithmetic contacts supply a genuinely joint cancellation.  Orthogonality,
Gamma positivity and elementary Chebyshev bounds alone do not supply it.

## 1. The dyadic block operator

Put

\[
 \mathcal N_Y=\{n=p^k:Y<n\le2Y\},
 \qquad w_n={\log p\over\sqrt n}.                       \tag{1.1}
\]

The centered contact operator of the block is

\[
 K_Y=\sum_{n\in\mathcal N_Y}w_n
       (S_{\log n}+S_{-\log n}).                        \tag{1.2}
\]

Its Fourier multiplier is

\[
 k_Y(\tau)=2\sum_{n\in\mathcal N_Y}w_n\cos(\tau\log n). \tag{1.3}
\]

Consequently

\[
 \|K_Y\|=2W_Y,
 \qquad
 W_Y=\sum_{n\in\mathcal N_Y}w_n,                       \tag{1.4}
\]

because the triangle inequality gives \(\|K_Y\|\le2W_Y\), while

\[
 k_Y(0)=2W_Y.                                           \tag{1.5}
\]

Equation (1.4) is exact for every finite block and uses no prime
asymptotic.  There is no uniform phase cancellation in operator norm.

## 2. The primitive conditions leave frequency zero alive

Let \(u\in C_c^\infty(\mathbb R)\) and define

\[
 F=(\partial_t^2-\tfrac14)u.                            \tag{2.1}
\]

Two integrations by parts give

\[
 \int F(t)e^{\pm t/2}\,dt=0,                            \tag{2.2}
\]

so \(F\) is primitive.  But

\[
 \widehat F(0)=-{1\over4}\widehat u(0),                 \tag{2.3}
\]

which is nonzero whenever \(\int u\ne0\).  Therefore compression to
\(\ker(M_-,M_+)\) does not delete the coherent real-frequency channel in
(1.5).

This is the precise distinction between the two Tate jets and ordinary
mean zero: the jets are located at \(\pm i/2\), not at \(0\).

## 3. Gamma Loewner domination fails at low frequency

The Gamma Laplacian has multiplier

\[
 \ell_\infty(\tau)
 =\operatorname{Re}\psi(1/4+i\tau/2)-\psi(1/4).        \tag{3.1}
\]

Its integral formula shows

\[
 \ell_\infty(\tau)=c_\infty\tau^2+O(\tau^4),
 \qquad c_\infty>0.                                    \tag{3.2}
\]

On the other hand,

\[
 k_Y(\tau)=2W_Y+O_Y(\tau^2).                            \tag{3.3}
\]

Hence

\[
 \sup_{0<|\tau|<\varepsilon}
 {k_Y(\tau)\over\ell_\infty(\tau)}=\infty.             \tag{3.4}
\]

There is no finite \(C_Y\), much less a uniform one, for the Loewner
inequality

\[
 K_Y\le C_YL_\infty                                    \tag{3.5}
\]

on the full primitive source.  Adding an \(L^2\) scalar can control the
zero mode, but that scalar is exactly the gap budget whose sharp value must
be proved in row D.

## 4. Failure of a frame/Bessel square-root gain

If the translations behaved orthogonally, one would hope for a batch size
controlled by

\[
 \left(\sum_{n\in\mathcal N_Y}w_n^2\right)^{1/2}        \tag{4.1}
\]

rather than \(W_Y\).  But the synthesis operator applied to the zero
Fourier character sends the coefficient vector
\((\sqrt{w_n})_n\) to \(W_Y\) times the same character.  Its Gram matrix
therefore has the coherent rank-one direction

\[
 (\sqrt{w_mw_n})_{m,n},                                 \tag{4.2}
\]

whose eigenvalue is \(W_Y\).  Thus any Bessel bound valid for all source
vectors is at least \(W_Y\); (4.1) cannot replace it.

Elementary Chebyshev upper bounds give \(W_Y=O(\sqrt Y)\).  With the usual
prime density heuristic, (4.1) is only of order \(\sqrt{\log Y}\), showing
the scale of the unavailable gain, but the exact obstruction (1.5) needs
neither that heuristic nor the prime number theorem.

## 5. Physical-space endpoint coherence

At the end of the dyadic window

\[
 T={1\over2}\log(2Y),                                   \tag{5.1}
\]

the overlap length for \(n\in(Y,2Y]\) is

\[
 2T-\log n=\log{2Y\over n}\in[0,\log2).                \tag{5.2}
\]

All block contacts therefore act between the same two endpoint strips of
width at most \(\log2\).  Choosing nonnegative tests nearly constant on
smaller endpoint strips makes the translations with nearby \(\log n\)
positively correlated.  The frequencies themselves lie in an interval of
length \(\log2\), while their spacing is much smaller than the Fourier
resolution of a window of length \(O(\log Y)\).

Thus the absence of a Bessel gain is not an artefact of using the full-line
multiplier; it is visible in the finite annular Schur channel.

## 6. Exact block capacity and the missing estimate

Group the new annulus data for \((Y,2Y]\) into a single block.  With the old
core/annulus decomposition, write

\[
 H_{2Y,T}=
 \begin{pmatrix}A_Y&B_Y\\B_Y^*&D_Y-K_Y^{\rm ann}\end{pmatrix}. \tag{6.1}
\]

If \(A_Y\ge0\), the exact shorted block capacity is

\[
 \boxed{
 \operatorname{Cap}_{(Y,2Y]}
 =D_Y-K_Y^{\rm ann}-B_Y^*A_Y^\dagger B_Y.}             \tag{6.2}
\]

The dyadic induction would close if

\[
 \operatorname{Cap}_{(Y,2Y]}\ge0                       \tag{6.3}
\]

uniformly.  Gamma positivity controls a high-frequency portion of \(D_Y\),
and prior contacts contribute to both \(D_Y\) and the Schur correction.
But Sections 1--5 show that neither factor independently dominates the
coherent size \(W_Y\).

The exact missing estimate is therefore a cancellation **inside** (6.2):

\[
 D_Y-B_Y^*A_Y^\dagger B_Y
 \ge K_Y^{\rm ann}.                                    \tag{6.4}
\]

It must use the joint arithmetic structure of all earlier blocks.  A
triangle bound, a Bessel bound for translations, or a Gamma Loewner bound
cannot prove it.  Iterating (6.4) is equivalent to the multiscale capacity
invariant of D.121 and hence to D.

## 7. Conclusion

Dyadic batching is correctly typed and avoids bookkeeping one prime at a
time, but positive contact weights are maximally coherent at frequency
zero.  The Tate primitive conditions do not remove that channel, and the
Gamma operator has zero strength there.  Therefore no source-derived
orthogonality gain over the absolute block mass exists at the operator
level.

The remaining possible dyadic theorem is the joint Schur estimate (6.4).
Its proof would be genuine arithmetic cancellation beyond Chebyshev and
local Gamma positivity; it is another exact form of the unresolved row-D
inequality.

