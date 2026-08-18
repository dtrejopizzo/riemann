# D.181 — Sub-Markov resolvent and the exact Tate rank-two correction

## Verdict

The localization still missing after D.180 can be obtained without a
Wiener inverse theorem.  Before imposing the two Tate moments, the complete
positive reference

\[
 \overline{\mathcal R}_T=\mathcal H_{5/4}
 +\sum_{p^j\le e^{2T}}{\log p\over p^{j/2}}
                   J_{p^j,-}^*J_{p^j,-}                 \tag{0.1}
\]

is a closed symmetric Dirichlet form.  Thus its semigroup is sub-Markov.
For every \(a>0\), its Green operator has the exact decomposition

\[
 \overline G_T
 =K_a+H_a,
 \qquad
 K_a=\int_0^{1/a}e^{-t\overline{\mathcal R}_T}\,dt,
 \qquad
 H_a=e^{-\overline{\mathcal R}_T/a}\overline G_T .    \tag{0.2}
\]

The first term has a nonnegative kernel and

\[
 \boxed{\|K_a\|_{1\to1},\ \|K_a\|_{\infty\to\infty}
       \le a^{-1}.}                                    \tag{0.3}
\]

Choose the prolate parameters of D.180 and put

\[
 a=(1-\eta)h_{5/4}(R),\qquad
 r_{T,R,\eta}={2TR\over\pi\eta}.                      \tag{0.4}
\]

If \(E_{<a}=\mathbf1_{(0,a)}(\overline{\mathcal R}_T)\), then

\[
 \boxed{\mathrm{rank}\,E_{<a}\le r_{T,R,\eta}.} \tag{0.5}
\]

Consequently

\[
 H_a=H_a^{\rm hi}+H_a^{\rm lo},\qquad
 \|H_a^{\rm hi}\|\le {e^{-1}\over a},\qquad
 \mathrm{rank}\,H_a^{\rm lo}\le r_{T,R,\eta}.  \tag{0.6}
\]

Finally impose the exact two A--B--C Tate jets.  The constrained Green
operator is

\[
 \boxed{
 G_T^{\rm prim}=\overline G_T-overline G_TM^*
 (M\overline G_TM^*)^{-1}M\overline G_T,}             \tag{0.7}
\]

where \(M\) is the two-moment map.  The second summand has rank at most
two.  Combining (0.2), (0.5)--(0.7) gives the exact localization

\[
 \boxed{
 G_T^{\rm prim}=K_a+H_a^{\rm hi}+F_a,\quad
 \|K_a\|_{1,\infty}\le a^{-1},\quad
 \|H_a^{\rm hi}\|\le e^{-1}a^{-1},\quad
 \mathrm{rank}\,F_a\le r_{T,R,\eta}+2.}         \tag{0.8}
\]

All prime powers and the complete Gamma place occur inside the same
sub-Markov generator in (0.1).  Tate is not discarded or estimated: its
entire effect on the Green operator is the explicit rank-two Schur
correction (0.7).

This proves the requested localized inverse structure.  It does not by
itself prove the D.178 word-simplex inequality: (0.3) controls total kernel
mass, whereas the simplex constant also uses the multiplicative support
constraint on the ordered prime labels.  The remaining task is now
sharply typed: prove that insertion of the sub-Markov potential \(K_a\)
preserves that label-simplex gain; every failure either receives the
factor \(e^{-1}\) from \(H_a^{\rm hi}\) or passes through a block of rank
at most \(r_{T,R,\eta}+2\).

## 1. The complete reference is a Dirichlet form

Extend \(F\in L^2(I_T)\) by zero.  D.134 gives

\[
 \mathcal H_{5/4}(F)
 ={1\over2}\iint_{\mathbb R^2}
 \gamma_{5/4}(|t-s|)|\widetilde F(t)-\widetilde F(s)|^2\,dt\,ds,
 \quad
 \gamma_{5/4}(r)={e^{-5r/2}\over1-e^{-2r}}.          \tag{1.1}
\]

For \(b=\log(p^j)\),

\[
 \|J_{p^j,-}F\|^2
 ={1\over2}\int_{I_T\cap(I_T-b)}|F(t+b)-F(t)|^2\,dt. \tag{1.2}
\]

Both (1.1) and (1.2) decrease under every normal contraction
\(C:\mathbb R\to\mathbb R\), because
\(|C(x)-C(y)|\le|x-y|\) and \(|C(x)|\le|x|\).  The Gamma form is closed;
on a fixed window the prime-power sum is finite and each summand is a
bounded Dirichlet form.  Hence (0.1) is a densely defined closed symmetric
Dirichlet form.

Its associated semigroup \(S_t=e^{-t\overline{\mathcal R}_T}\) is
positivity preserving and contractive on every \(L^q\),
\(1\le q\le\infty\).  The exterior killing in (1.1) gives strict
positivity on the bounded window, so \(\overline G_T\) exists and is
compact.

Integrating the \(L^1\)- and \(L^\infty\)-contractions for
\(0\le t\le1/a\) proves (0.3).  On a finite measure interval a positive
\(L^1\)-to-\(L^1\) and \(L^\infty\)-to-\(L^\infty\) operator has a
nonnegative kernel in the usual extended sense; finite-cell
approximations give the same statement entrywise.

## 2. Exact semigroup decomposition

Functional calculus gives

\[
 \int_0^{1/a}e^{-t\overline{\mathcal R}_T}\,dt
 =\overline G_T(I-e^{-\overline{\mathcal R}_T/a}),    \tag{2.1}
\]

which proves (0.2).  Split the residual by the spectral projections

\[
 E_{<a}=\mathbf1_{(0,a)}(\overline{\mathcal R}_T),
 \qquad E_{\ge a}=I-E_{<a}.                           \tag{2.2}
\]

Then

\[
 H_a^{\rm lo}=\overline G_Te^{-\overline{\mathcal R}_T/a}E_{<a},
 \qquad
 H_a^{\rm hi}=\overline G_Te^{-\overline{\mathcal R}_T/a}E_{\ge a}.
                                                                    \tag{2.3}
\]

The scalar function \(e^{-\lambda/a}/\lambda\) is decreasing, so on
\([a,\infty)\)

\[
 \|H_a^{\rm hi}\|
 \le\sup_{\lambda\ge a}{e^{-\lambda/a}\over\lambda}
 ={e^{-1}\over a}.                                   \tag{2.4}
\]

## 3. The low spectral rank is prolate-finite

Let \(C_{T,R}\), \(P_{\rm lo}\), and \(P_{\rm hi}\) be the concentration
operators of D.180, now on the ambient supported space.  The same
Plancherel argument gives

\[
 \overline{\mathcal R}_T\ge
 h_{5/4}(R)(I-C_{T,R})\ge aP_{\rm hi}.                \tag{3.1}
\]

Moreover

\[
 \mathrm{rank}\,P_{\rm lo}\le{2TR\over\pi\eta}. \tag{3.2}
\]

If \(\dim E_{<a}>\mathrm{rank}\,P_{\rm lo}\), the range of
\(E_{<a}\) contains a nonzero vector orthogonal to \(P_{\rm lo}\), hence
in \(P_{\rm hi}\).  Its Rayleigh quotient is strictly below \(a\) by
the spectral definition of \(E_{<a}\), but at least \(a\) by (3.1), a
contradiction.  This proves (0.5), and therefore the rank assertion in
(0.6).

## 4. Exact imposition of the two Tate moments

Let

\[
 M:F\longmapsto\bigl(J_0(F),J_1(F)\bigr)             \tag{4.1}
\]

be the two primitive moments already identified with the A--B--C Tate
jets in D.137.  They are bounded on the supported form domain.  Assume
they are independent; otherwise replace the inverse below by the
Moore--Penrose inverse and the rank only decreases.

For a load \(f\), the unconstrained minimizer of

\[
 {1\over2}\langle u,\overline{\mathcal R}_Tu\rangle
 -\mathrm{Re}\,\langle f,u\rangle               \tag{4.2}
\]

is \(u=\overline G_Tf\).  Adding a multiplier \(M^*\lambda\) and imposing
\(Mu=0\) gives

\[
 \lambda=(M\overline G_TM^*)^{-1}M\overline G_Tf.    \tag{4.3}
\]

Substitution proves (0.7).  It is the Green operator of the form
compressed to \(\ker M\), and its difference from \(\overline G_T\) has
rank at most two.  Combining this correction with \(H_a^{\rm lo}\)
proves (0.8).

## 5. Consequence for the return expansion

At every exact inverse in D.175--D.178 insert (0.8).  A word has one of
three types.

1. Every inverse is a sub-Markov potential \(K_a\).  Each insertion has
   nonnegative row and column mass at most \(a^{-1}\); the arithmetic
   labels remain the exact \(p^j\) labels of the contact channels.
2. At least one inverse is \(H_a^{\rm hi}\).  That occurrence contributes
   the strict spectral factor \(e^{-1}a^{-1}\).  Repeating the splitting
   gives a geometric return ledger.
3. At least one inverse is \(F_a\).  The word factors through a space of
   dimension at most \(2TR/(\pi\eta)+2\); the final two dimensions are
   exactly the two Tate jets.

The decomposition is uniform in the number and location of prime-power
channels.  It therefore replaces the unavailable solid-Wiener estimate
by a Markov/localized term, a contractive term, and an explicitly counted
finite-dimensional term.

