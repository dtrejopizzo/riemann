# D.118 — Matrix Doob transform, the two Tate jets and the killing defect

## Verdict

There is a canonical rank-two ground-state transform of the finite-cutoff
arithmetic jump operator.  Its two diagonal ground states are exactly
\(e^{-t/2}\) and \(e^{t/2}\), and conjugation by them splits the central rate

\[
 {\Lambda(n)\over\sqrt n}
\]

into the two oriented rates

\[
 \Lambda(n),\qquad {\Lambda(n)\over n}.                \tag{0.1}
\]

Thus the transform recovers, from the central torsor, the two finite
orientations occurring in the completed explicit formula.

It does not close row D.  The potential which makes the jets harmonic is
positive when added to \(L_X\), whereas row D requires subtracting the
positive contact mass \(2A_X+m_0\).  Arithmetically the Doob potential grows
like \(\sum_{n\leq X}\Lambda(n)\), not like
\(\sum_{n\leq X}\Lambda(n)/\sqrt n\).  At Gamma, the corresponding
ground-state compensation diverges linearly because the jets sit exactly at
the first quarter-shift pole.  Hence there is no cofinal conservative
rank-two Doob transform with finite Gamma killing.

The source maximum principle proves a lower bound with the opposite sign.
Obtaining the desired positive spectral gap after subtracting the completed
contact mass is again exactly row D.

## 1. Scalar ground-state identity

Let

\[
 L_a=2I-S_a-S_{-a},\qquad S_aF(t)=F(t-a),              \tag{1.1}
\]

and put \(h_s(t)=e^{st}\).  Since

\[
 S_a h_s=e^{-sa}h_s,
\]

one has the formal eigenvalue identity

\[
 L_a h_s=\lambda_a(s)h_s,
 \qquad
 \lambda_a(s)=2-e^{sa}-e^{-sa}leq0.                  \tag{1.2}
\]

Set

\[
 c_a(s)=-\lambda_a(s)=2(\cosh(sa)-1)\geq0.            \tag{1.3}
\]

For compactly supported \(g\), direct conjugation gives

\[
\begin{aligned}
 h_s^{-1}(L_a+c_a(s))h_sg
  ={}&(e^{sa}+e^{-sa})g\\
    &-e^{-sa}S_ag-e^{sa}S_{-a}g.                     \tag{1.4}
\end{aligned}
\]

The right side is the positive reversible jump generator with rates
\(e^{-sa}\) and \(e^{sa}\).  It kills the constant function.  Equivalently,
\(L_a+c_a(s)\) kills \(h_s\).

The reversible measure of (1.4) is

\[
 d\pi_s(t)=h_s(t)^2dt=e^{2st}dt.                      \tag{1.5}
\]

Indeed the forward and reverse fluxes satisfy detailed balance:

\[
 e^{2st}e^{-sa}=e^{2s(t-a)}e^{sa}.                    \tag{1.6}
\]

The measure (1.5) is infinite on \(\mathbb R\), so the harmonic constant is
not an invariant probability state.  Nevertheless (1.4) is an exact
ground-state representation at every finite contact cutoff.

## 2. Rank-two transform and the central torsor

Let

\[
 H(t)=\operatorname{diag}(e^{-t/2},e^{t/2}).           \tag{2.1}
\]

For the two components \(s=\mp1/2\), apply (1.4) diagonally.  Since
\(c_a(1/2)=c_a(-1/2)\), the transformed arithmetic operator is a direct sum
of two conservative reversible jump generators, and its two constant
sections pull back to the Tate jets

\[
 h_-(t)=e^{-t/2},\qquad h_+(t)=e^{t/2}.                \tag{2.2}
\]

Now take \(a=\log n\) and the source-derived central rate

\[
 w_n={\Lambda(n)\over\sqrt n}.                         \tag{2.3}
\]

Writing \(q=e^{a/2}=\sqrt n\), the two oriented rates in (1.4) are

\[
 w_nq=\Lambda(n),
 \qquad
 w_nq^{-1}={\Lambda(n)\over n}.                        \tag{2.4}
\]

Thus the matrix transform recovers precisely the two finite-place
orientations of row C.  This calculation uses every power \(p^k\), since
\(w_{p^k}=(\log p)p^{-k/2}\), and it vanishes away from prime powers because
the A--B cyclotomic contact does.

The required arithmetic killing at cutoff \(X\) is

\[
\begin{aligned}
 C_{{\rm fin},X}^{\rm Doob}
 &=\sum_{n\leq X}w_n c_{\log n}(1/2)\\
 &=\sum_{n\leq X}\Lambda(n)
     \left(1+{1\over n}-{2\over\sqrt n}\right).      \tag{2.5}
\end{aligned}
\]

It is nonnegative, and the transform proves

\[
 L_{{\rm fin},X}+C_{{\rm fin},X}^{\rm Doob}I\geq0.   \tag{2.6}
\]

This is a lower bound

\[
 L_{{\rm fin},X}\geq-C_{{\rm fin},X}^{\rm Doob}I,   \tag{2.7}
\]

not the row-D lower bound by the positive scalar \(2A_X\).

## 3. The killing has the wrong cofinal scale

The central contact mass is

\[
 2A_X=2\sum_{n\leq X}{\Lambda(n)\over\sqrt n}.        \tag{3.1}
\]

By contrast, (2.5) contains the leading term
\(\sum_{n\leq X}\Lambda(n)\).  The prime number theorem gives

\[
 C_{{\rm fin},X}^{\rm Doob}=X+o(X),
 \qquad
 2A_X=4\sqrt X+o(\sqrt X).                             \tag{3.2}
\]

Consequently the ground-state killing is neither the completed contact mass
nor a bounded perturbation of it.  Its much larger scale is forced by the
same uncentering that produces the two correct orientations in (2.4).

This is not a normalization error.  If a positive exponential \(e^{st}\)
is to be harmonic for the transform of a symmetric jump by \(a\), the
eigenvalue (1.2) uniquely forces the compensation (1.3).

## 4. Gamma compensation diverges at both jets

For the Gamma jump density

\[
 g_\infty(r)={e^{-r/2}\over1-e^{-2r}},                \tag{4.1}
\]

the ground-state compensation truncated at range \(R\) is

\[
 C_{\infty,R}^{\rm Doob}(s)
 =2\int_0^R g_\infty(r)(\cosh(sr)-1)\,dr.             \tag{4.2}
\]

For \(s=\pm1/2\),

\[
 2g_\infty(r)(\cosh(r/2)-1)\longrightarrow1
 \qquad(r\to\infty).                                 \tag{4.3}
\]

Therefore

\[
 C_{\infty,R}^{\rm Doob}(\pm1/2)=R+O(1).              \tag{4.4}
\]

This is the real-place form of the quarter-shift pole.  The finite completed
constant

\[
 m_0=\log\pi-\psi(1/4)                                \tag{4.5}
\]

is not the Doob compensation (4.2).  Replacing (4.4) by a finite part would
require subtracting its positive linear divergence.  That subtraction is a
renormalization of the generator, not a conservative Markov/Doob transform,
and its sign is not controlled by the maximum principle.

## 5. Why the matrix transform does not produce the row-D gap

At finite arithmetic and Gamma-range cutoffs, let

\[
 C_{X,R}^{\rm Doob}
 =C_{{\rm fin},X}^{\rm Doob}+C_{\infty,R}^{\rm Doob}. \tag{5.1}
\]

The rank-two ground-state representation proves

\[
 L_{X,R}+C_{X,R}^{\rm Doob}I\geq0                     \tag{5.2}
\]

in each jet component.  Row D, however, is

\[
 L_X|_{\ker(M_-,M_+)}
 \geq(2A_X+m_0)I.                                     \tag{5.3}
\]

The scalar in (5.2) is added and divergent; the scalar in (5.3) is
subtracted from \(L_X\) and finite after the explicit-formula boundary
assembly.  No maximum principle changes one assertion into the other.

The transformed generators have zero as the bottom of their spectrum
before boundary conditions because constants are harmonic.  Their direct
sum has a two-dimensional distributional harmonic space corresponding to
the two jets, but it does not have a source-forced positive gap on the
orthogonal complement.  On finite windows such a gap depends on the window
and on the chosen boundary condition; detailed balance fixes neither its
value nor its cofinal limit.

## 6. Matrix mixing cannot repair the sign for free

One might add an off-diagonal matrix potential coupling the two jet
components.  To keep both columns of \(H(t)\) harmonic, however, its value on
their span is fixed by

\[
 V(t)H(t)=-L_XH(t).                                    \tag{6.1}
\]

Since the two columns of \(H(t)\) are pointwise independent, (6.1) uniquely
recovers the diagonal Doob compensation above.  Any additional Hermitian
mixing must vanish on the whole two-dimensional jet fibre and hence cannot
alter the primitive spectral edge through a pointwise maximum principle.

If instead one equips the two components with the crossed Tate/Krein metric,
the required scalar may appear with the desired sign, but ordinary complete
positivity and the Markov maximum principle are then lost.  Positivity of
the resulting crossed primitive form is precisely the Hodge/Weil assertion
being sought.

## 7. Cofinal conclusion

The matrix Doob construction provides an exact and useful comparison:

\[
 \boxed{
 \text{central weight }{\Lambda(n)\over\sqrt n}
 \xrightarrow{\ e^{\pm t/2}\text{ Doob}\ }
 \left(\Lambda(n),{\Lambda(n)\over n}\right).}
\]

It also identifies the two Tate jets as the two reciprocal ground-state
characters of the finite arithmetic dynamics.  But the associated killing
potential has the opposite sign, the wrong arithmetic scale, and an
unavoidable Gamma divergence.  There is no cofinal conservative
ground-state transform giving the spectral gap \(2A_X+m_0\).

Hence the torsor, product formula, detailed balance and maximum principle
do not prove row D.  After the exact A--B--C identification, the remaining
claim is still the sharp positivity of the renormalized crossed form.

