# D.120 — Cheeger profile of the source-derived prime--Gamma graph

## Verdict

The positive operator \(L_X\) is the Laplacian of a canonical weighted
translation graph on \(\mathbb R\): its atomic conductances are
\((\log p)p^{-k/2}\) at lengths \(k\log p\), and its continuous conductance
is the quarter-shift Gamma density.  Its isoperimetric profile can be
calculated exactly on intervals.

At every fixed arithmetic cutoff this graph is amenable.  Its Cheeger
constant is zero, even with the full Gamma oscillator, because the Gamma
measure has finite first moment.  The two Tate moment constraints do not
repair fixed-cutoff expansion: an exact three-translate construction makes
Følner tests primitive.

This does not disprove row D, because the explicit-formula cofinal regime
couples the arithmetic cutoff to the support diameter.  It does prove that
no cutoff-independent Cheeger/Poincare theorem, based only on the positive
prime--Gamma graph and removal of two boundary modes, can yield the sharp
gap \(2A_X+m_0\).  In the coupled regime the missing remainder after the
bulk long-jump conductance is exactly \(-B_{\rm nuc}\), so estimating it is
again D.

## 1. Source-derived conductance

At cutoff \(X\), set

\[
 w_{p^k}=(\log p)p^{-k/2},\qquad a_{p^k}=k\log p,       \tag{1.1}
\]

and

\[
 g_\infty(r)={e^{-r/2}\over1-e^{-2r}}.                \tag{1.2}
\]

The Dirichlet form of the stratified graph is

\[
\begin{aligned}
 \mathcal E_X(F)={}&
 \sum_{p^k\leq X}w_{p^k}\|F-S_{a_{p^k}}F\|_2^2\\
 &+\int_0^\infty g_\infty(r)\|F-S_rF\|_2^2\,dr
 =\langle F,L_XF\rangle.                              \tag{1.3}
\end{aligned}
\]

Every coefficient in (1.3) is obtained from A--B contact, ordered Green
depth or the Gamma heat module.  No zero or sign of the explicit formula is
used.

## 2. Exact interval profile

Let \(E_L=[0,L]\).  For every \(a>0\),

\[
 \|1_{E_L}-S_a1_{E_L}\|_2^2=2\min(a,L).               \tag{2.1}
\]

Therefore

\[
 {\mathcal E_X(1_{E_L})\over\|1_{E_L}\|_2^2}
 ={2\over L}\left(
   \sum_{p^k\leq X}w_{p^k}\min(a_{p^k},L)
  +\int_0^\infty g_\infty(r)\min(r,L)\,dr
  \right).                                            \tag{2.2}
\]

At fixed \(X\), the atomic first moment is finite.  The Gamma first moment
is also finite, since

\[
 rg_\infty(r)\sim\tfrac12\quad(r\downarrow0),
 \qquad
 rg_\infty(r)\sim re^{-r/2}\quad(r\to\infty).        \tag{2.3}
\]

Dominated convergence in (2.2) gives

\[
 \lim_{L\to\infty}
 {\mathcal E_X(1_{E_L})\over\|1_{E_L}\|_2^2}=0.       \tag{2.4}
\]

After smoothing the two endpoints, the same holds for form-domain tests.
Thus the infinite translation graph has Cheeger constant zero and
\(\inf\operatorname{Spec}L_X=0\) for every fixed \(X\).

## 3. Exact removal of both Tate moments

The moment map is

\[
 M_\pm(F)=\int_{\mathbb R}F(t)e^{\pm t/2}\,dt.         \tag{3.1}
\]

Translations satisfy

\[
 M_\pm(S_aF)=e^{\pm a/2}M_\pm(F).                     \tag{3.2}
\]

Fix a nonzero compactly supported \(F\), a separation \(R>0\), and put
\(z=e^{R/2}\).  The coefficients

\[
 \alpha=z^{-1}-z,qquad
 \beta=z^2-z^{-2}                                     \tag{3.3}
\]

give the exact primitive combination

\[
 F_R=\alpha S_{-R}F+\beta F+\alpha S_RF.              \tag{3.4}
\]

Indeed

\[
 \alpha(z+z^{-1})+\beta=0,                            \tag{3.5}
\]

so (3.2) implies

\[
 M_-(F_R)=M_+(F_R)=0.                                 \tag{3.6}
\]

After division by \(\beta\), the two side coefficients are
\(O(e^{-R/2})\).  For fixed \(X\), finite-place cross terms vanish once the
translates are farther apart than the largest atomic jump, while Gamma cross
terms tend to zero exponentially.  Hence

\[
 {\mathcal E_X(F_R)\over\|F_R\|^2}
 ={\mathcal E_X(F)\over\|F\|^2}+o(1)
 \qquad(R\to\infty).                                  \tag{3.7}
\]

Choosing \(F\) to be a smoothed long interval and then \(R\) large shows
that the fixed-cutoff primitive subspace also has bottom zero.  Removing two
exponential moments is not an isoperimetric compactification of the
translation graph.

## 4. Why this is not a counterexample to row D

For a test supported in a window of diameter \(L\), the explicit-formula
identity uses a contact cutoff large enough to include all correlations in
that window; in logarithmic terms \(\log X\) grows with \(L\).  The limits
\(L\to\infty\) at fixed \(X\) used above are therefore not the row-D cofinal
limit.

When \(\log n>L\), translated supports are disjoint and

\[
 \|F-S_{\log n}F\|^2=2\|F\|^2.                       \tag{4.1}
\]

Those long edges contribute exactly the bulk scalar \(2A_X\|F\|^2\).
Subtracting the completed mass \((2A_X+m_0)\|F\|^2\) leaves only the
correlation remainder

\[
 \mathcal E_X(F)-(2A_X+m_0)\|F\|^2
 =-B_{{\rm nuc},X}(F,F).                              \tag{4.2}
\]

Thus the coupled cofinal problem is not ordinary graph expansion: it asks
for the sign of the renormalized remainder after the dominant long-edge
conductance has been removed.

## 5. Cheeger bounds cannot have the required sharp constant

Ordinary Cheeger inequalities control a spectral gap by a quadratic
expression in boundary/volume conductance and a degree bound.  Here the
unconditioned infinite graph has zero Cheeger constant.  On finite windows,
both the conductance and the resulting Poincare constant depend on the
window and boundary condition.

More importantly, complete positivity only gives \(L_X\geq0\), whereas row
D requires

\[
 L_X|_{\ker(M_-,M_+)}\geq(2A_X+m_0)I.                 \tag{5.1}
\]

The constant on the right is essentially the full long-jump degree, not a
small Cheeger lower bound.  Neither source-derived conductance nor deletion
of two modes forces a normalized spectral gap of one.

The prime expansion and Gamma oscillator do calculate every term of
\(L_X\), but the sharp deficit between its primitive spectral edge and
\(2A_X+m_0\) is precisely the Weil form.  Any isoperimetric assertion strong
enough to prove (5.1) is therefore an equivalent reformulation of D, not an
independent consequence of the graph construction.

## 6. Conclusion

The stratified prime--Gamma graph is canonical and its interval profile is
explicit.  It is amenable at fixed cutoff, and the two Tate moments can be
removed without creating expansion.  Coupling cutoff and support restores
the large bulk contact mass, but after its necessary subtraction the
remaining sign is exactly \(-B_{\rm nuc}\).

Therefore a Cheeger/Poincare argument based solely on the positive graph,
even with all prime powers and Gamma, does not close row D.  A successful
argument would need a genuinely global estimate on the renormalized
prime--Gamma correlations, not ordinary isoperimetry.

