# D.143 — Critical Dirichlet Hilbertization and the missing mixed coupling

## Verdict

The common A--B--C coefficient action has a canonical positive Hilbert
realization at the central metric.  Put

\[
 \mathcal H_{1/2}=\ell^2\!\left(\mathbb N,{1\over n}\right),
 \qquad
 \|a\|_{1/2}^2=\sum_{m\geq1}{|a_m|^2\over m}.
\]

If (L_n) is left Dirichlet translation, then

\[
 \boxed{\|L_n a\|_{1/2}=n^{-1/2}\|a\|_{1/2}.}        \tag{0.1}
\]

Thus the positive regular representation recovers exactly the self-dual
metric character of row B and retains every label (p^k).  It does **not**,
however, construct the comparison (C_TX_T=Y_T) of D.137.  There are two
separate, rigorous reasons.

1.  The logarithmic Euler contact is only a nuclear distribution at this
    Hilbert boundary.  Neither the vector
    \(
       \sum_n\Lambda(n)L_n\delta_1
    \)
    nor the Riesz representative of the Mangoldt functional belongs to
    \(\mathcal H_{1/2}\).
2.  The positive feature with the exact D weight
    \(w_n=\Lambda(n)/\sqrt n\) cannot be assembled as an orthogonal global
    Hilbert sum at the critical metric, because
    \(
      \sum_n\Lambda(n)/\sqrt n=\infty.
    \)
    On a compact support window only finitely many channels occur, but the
    existing A--B--C scalar action supplies no map coupling those discrete
    channels to the Gamma screw and resolvent channels.  Such a coupling is
    precisely the extra transformation (C_T).

A logarithmic rigging makes the Euler distribution Hilbert-valued, but no
finite logarithmic rigging makes the exact D feature Hilbert-valued.  A
power damping would do so only by moving off the central exponent and
changing (B_{\rm nuc}).  Therefore changing the completion cannot prove
D.  The live object must be a support-local, non-product positive coupling
of the prime-power and Gamma sectors, with contractivity proved before the
Weil sign is invoked.

No zero of \(\xi\), RH, or sign of (B_{\rm nuc}) is used.  The paper is
not modified.

## 1. The exact central Hilbert representation

For a sequence (a=(a_m)), define

\[
 (L_na)_r=
 \begin{cases}
  a_{r/n},&n\mid r,\\
  0,&n\nmid r.
 \end{cases}                                         \tag{1.1}
\]

Then a change of index gives

\[
 \|L_na\|_{1/2}^2
 =\sum_{r:n\mid r}{|a_{r/n}|^2\over r}
 ={1\over n}\sum_{m\geq1}{|a_m|^2\over m}.
                                                               \tag{1.2}
\]

Consequently (L_mL_n=L_{mn}) and (0.1) holds.  If
(c=(c_n)\in\mathcal C_{\mathbb R}), the series

\[
 \pi_{1/2}(c)=\sum_{n\geq1}c_nL_n                  \tag{1.3}
\]

converges in operator norm, since

\[
 \|\pi_{1/2}(c)\|
 \leq\sum_n|c_n|n^{-1/2}
 \leq q_0(c).                                        \tag{1.4}
\]

It is a faithful representation: if (Omega=\delta_1), then
(pi_{1/2}(c)\Omega=c), and every rapidly decreasing (c) belongs to
(\mathcal H_{1/2}).  Moreover

\[
 \|L_n\Omega\|=n^{-1/2},                             \tag{1.5}
\]

which is exactly the metric character attached to (Gamma_n).  This is a
genuine positive result: the commutative arithmetic semigroup itself has a
critical Hilbert realization, so the factorial obstruction of the free
Fock lift is avoided.

## 2. The Mangoldt contact is not a Hilbert vector

Let

\[
 G_N=\sum_{2\leq n\leq N}\Lambda(n)L_n\Omega.
                                                               \tag{2.1}
\]

The point masses are orthogonal, hence

\[
 \|G_N\|_{1/2}^2
 =\sum_{2\leq n\leq N}{\Lambda(n)^2\over n}.         \tag{2.2}
\]

Already the prime terms diverge.  The prime number theorem and partial
summation give

\[
 \sum_{p\leq N}{(\log p)^2\over p}
 ={1\over2}(\log N)^2+O(\log N),                     \tag{2.3}
\]

so (G_N) has no limit in (\mathcal H_{1/2}).

The obstruction for the contact functional is stronger.  If

\[
 \ell(a)=\sum_na_n\Lambda(n)                         \tag{2.4}
\]

were continuous for the Hilbert norm, its Riesz vector (g) would have to
satisfy

\[
 {\overline{g_n}\over n}=\Lambda(n),
 \qquad g_n=n\Lambda(n).                              \tag{2.5}
\]

But

\[
 \|g\|_{1/2}^2=\sum_nn\Lambda(n)^2=\infty.           \tag{2.6}
\]

Thus nuclear continuity of (ell) on (mathcal C_{\mathbb R}) does not
become Hilbert continuity at the central boundary.  This is consistent
with row C: (Z\partial Z^{-1}) is an operator-valued distribution on the
test space, not a bounded operator on this regular Hilbert module.

## 3. Why the normalized scalar sequence is not the D feature

There is a tempting but incorrect shortcut.  The sequence

\[
 c_n={\Lambda(n)\over\sqrt n}                         \tag{3.1}
\]

does belong to (\mathcal H_{1/2}), because

\[
 \|c\|_{1/2}^2=\sum_n{\Lambda(n)^2\over n^2}<\infty. \tag{3.2}
\]

Its Gram weight, however, is quadratic in (Lambda): it is
(\Lambda(n)^2/n^2), not the linear D weight

\[
 w_n={\Lambda(n)\over\sqrt n}.                       \tag{3.3}
\]

To realize (3.3) as the squared norm of an orthogonal (n)-channel in
(\mathcal H_{1/2}), its coefficient (b_n) must obey

\[
 {|b_n|^2\over n}={\Lambda(n)\over\sqrt n},
 \qquad |b_n|^2=\Lambda(n)\sqrt n.                   \tag{3.4}
\]

The norm of the global feature is therefore

\[
 \sum_n{|b_n|^2\over n}
 =\sum_n{\Lambda(n)\over\sqrt n}=\infty.             \tag{3.5}
\]

Again the prime terms suffice; by partial summation their sum up to (N)
is asymptotic to (2\sqrt N).

For a compactly supported logarithmic test (F), D.137 avoids (3.5) by
using only translations (k\log p\) that meet its support window.  The
positive sides separately acquire a new nonzero channel at each threshold,
whereas their signed difference has a canonical cancellation.  This is
why the coherent Krein line globalizes and the two positive feature
Hilbert spaces do not globalize by a naive orthogonal sum.

## 4. Logarithmic rigging: what it repairs and what it cannot repair

For (s\geq0), set

\[
 \mathcal H_{1/2,-s}
 =\ell^2\!\left(\mathbb N,
 {1\over n(1+\log n)^{2s}}\right).                   \tag{4.1}
\]

The same calculation as (1.2) gives

\[
 \|L_na\|_{1/2,-s}^2
 \leq n^{-1}\|a\|_{1/2,-s}^2.                       \tag{4.2}
\]

The Euler vector with coefficients (\Lambda(n)) belongs to this space
for (s>1), since

\[
 \sum_n{\Lambda(n)^2\over n(1+\log n)^{2s}}<\infty
 \quad(s>1).                                         \tag{4.3}
\]

This gives a valid rigged-Hilbert interpretation of the row-C contact.
It does not make the D feature (3.4) square summable.  For every finite
(s),

\[
 \sum_n{\Lambda(n)\over
  \sqrt n(1+\log n)^{2s}}=\infty,                    \tag{4.4}
\]

because its prime part is comparable, after (x=e^u), to
(\int^\infty e^{u/2}u^{-2s}\,du).

A weight (n^{-\varepsilon}) would make (4.4) converge, but it replaces
(n^{-1/2}) by (n^{-1/2-\varepsilon}).  That is a different vertical
line and its pullback is not the form (B_{\rm nuc}) proved in D.137.

## 5. Exact categorical consequence

In row A the arithmetic action on intrinsic periodic cohomology is
coefficient-only:

\[
 \rho_n^{\rm int}=\operatorname{id}_{P}\otimes L_{\delta_n}. \tag{5.1}
\]

The reduced contact has zero periodic component, while row C realizes
(L_{\delta_n}) as the multiplier (U_n).  These maps prove equality of
labels, composition and determinant contact, but they do not specify any
morphism between the Hilbert channels

\[
 \mathcal X_T=
 \mathcal H_{\Gamma,\rm screw}
 \oplus\bigoplus_{p^k}\mathcal H_{p^k,-}
\]

and

\[
 \mathcal Y_T=
 \mathcal H_{\beta}\oplus\mathcal H_{\rm resolvent}
 \oplus\bigoplus_{p^k}\mathcal H_{p^k,+}.            \tag{5.2}
\]

The scalar regular representation (1.3) acts on the labels inside both
sides; it neither maps antisymmetric translation differences to symmetric
translation sums nor couples the Gamma screw to the central and resolvent
channels.  Consequently it does not define the algebraic comparison
(C_T^0(X_TF)=Y_TF), much less prove its contractivity.

The exact remaining datum is therefore unchanged but better localized:

\[
 C_T:\overline{X_T(\mathcal P_T)}\longrightarrow\mathcal Y_T,
 \qquad C_TX_T=Y_T,\qquad\|C_T\|\leq1.               \tag{5.3}
\]

The first two clauses require a mixed prime--Gamma natural transformation;
the third is the row-D inequality.  Equations (1.1)--(4.4) prove that this
transformation cannot be obtained merely by completing the existing
coefficient algebra at the critical character.

## 6. Live pivot

The commutative Hilbertization is useful but not sufficient.  It fixes the
correct acceptance test for the next construction:

* it must be defined support by support, so no divergent global positive
  channel is introduced;
* it must preserve the individual (p^k) labels and the coefficient
  (\Lambda(p^k)/p^{k/2});
* it must include the Gamma screw, central atom and resolvent as parts of
  the same positive map; and
* its norm bound must follow from an independent geometric or operator
  theorem, not from the identity
  (B_{\rm nuc}=\|Y_T\cdot\|^2-\|X_T\cdot\|^2).

This rules out a completion-only proof and directs the construction toward
a non-product adelic conditional expectation or an equivalent
support-local transfer operator.
