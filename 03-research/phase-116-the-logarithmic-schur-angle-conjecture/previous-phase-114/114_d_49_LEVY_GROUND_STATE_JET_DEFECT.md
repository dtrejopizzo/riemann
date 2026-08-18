# D.49 — Levy ground state, Doob transform and rank-two jet defect

## 1. Exact decomposition

Work in logarithmic coordinates on `I_T=[-T,T]`, with zero extension.  Put

\[
 \phi_-(t)=e^{-t/2},\quad \phi_+(t)=e^{t/2},\quad
 M_TF=(\langle\phi_-,F\rangle,\langle\phi_+,F\rangle),
 \quad C=\begin{pmatrix}0&1\\1&0\end{pmatrix}.                 \tag{1.1}
\]

The polar block in the CCM convention is genuinely crossed.  Indeed, for
`h=f star f^vee`, Mellin convolution and the Tate involution give

\[
 \widehat h(0)=\widehat f(0)\overline{\widehat f(1)},\qquad
 \widehat h(1)=\widehat f(1)\overline{\widehat f(0)}.          \tag{1.2}
\]

Consequently the CCM term `W_(0,2)` is

\[
 W_{0,2}(h)=2\operatorname{Re}
   \bigl(M_-(F)\overline{M_+(F)}\bigr)
 =\langle M_TF,CM_TF\rangle,                                 \tag{1.3}
\]

not `|M_-|^2+|M_+|^2`.  This agrees with the rank-two matrix computed in
CCM and with the polar matrix in the row-C explicit formula.  Since CCM use
`QW=W_(0,2)-W_fin-W_infty`, whereas D.10 calls the completed local term
`B_nuc=W_fin+W_infty`, the exact window decomposition is

\[
 \boxed{QW_T(F,F)=\langle F,(L_T-m_TI)F\rangle
                  +\langle M_TF,CM_TF\rangle.}                 \tag{1.4}
\]

Here

\[
 m_T=2\sum_{2\le n\le e^{2T}}{\Lambda(n)\over\sqrt n}+m_0,   \tag{1.5}
\]

and

\[
 \begin{aligned}
 \langle F,L_TF\rangle={}&
 \sum_{2\le n\le e^{2T}}{\Lambda(n)\over\sqrt n}
       \|F-S_{\log n}F\|_2^2\\
 &+\int_0^\infty {e^{-r/2}\over1-e^{-2r}}
       \|F-S_rF\|_2^2\,dr.                                   \tag{1.6}
 \end{aligned}
\]

The second line is equivalently the Gamma sum in D.10/D.32.  On
`K_T=ker M_T`,

\[
 QW_T|_{K_T}=\Delta_{H,T}=L_T-m_TI=-B_{{\rm nuc},T}.           \tag{1.7}
\]

Thus the full operator is

\[
 A_T=H_{0,T}+R_{2,T},\qquad
 H_{0,T}=L_T-m_TI,\qquad R_{2,T}=M_T^*CM_T.                    \tag{1.8}
\]

## 2. The Tate exponentials are not ground-state solutions

For `sigma=+/-1/2`, a smooth cutoff `chi_T`, and `a>0`,

\[
 \begin{aligned}
 &(2I-S_a-S_{-a})(\chi_Te^{\sigma t})\\
 &=e^{\sigma t}\bigl(2\chi_T(t)-e^{-\sigma a}\chi_T(t-a)
                   -e^{\sigma a}\chi_T(t+a)\bigr).            \tag{2.1}
 \end{aligned}
\]

Even where all cutoffs equal one, the coefficient is
`2-2 cosh(sigma a)`, which is nonzero.  Near the cutoff there are additional
translated boundary layers.

The holomorphic continuation of the Gamma-energy multiplier is

\[
 \ell_\infty(\tau)=\sum_{j=0}^\infty {1\over a_j}
 {\tau^2\over4a_j^2+\tau^2},\qquad a_j=j+\tfrac14.             \tag{2.2}
\]

Formally `e^(sigma t)` corresponds to `tau=-i sigma`.  At
`|sigma|=1/2`, the `j=0` denominator is

\[
 4(1/4)^2-\sigma^2=0.                                        \tag{2.3}
\]

This is exactly the Gamma pole represented by the two residue charts in
D.40--D.42.  With cutoff the exact expression is

\[
 \begin{aligned}
 L_{\infty,T}(\chi_Te^{\sigma t})(t)
 =e^{\sigma t}\int_0^\infty {e^{-r/2}\over1-e^{-2r}}
 \bigl(&2\chi_T(t)-e^{-\sigma r}\chi_T(t-r)\\
                   &-e^{\sigma r}\chi_T(t+r)\bigr)dr.         \tag{2.4}
 \end{aligned}
\]

It is not proportional to the cutoff exponential.  Hence

\[
 \boxed{e^{\pm t/2}\text{ are boundary jets/residue vectors, not formal
 ground states of }A_T.}                                      \tag{2.5}
\]

## 3. The Levy part is positivity improving

The form `E_T(F)=<F,L_TF>` is a symmetric Dirichlet form.  Normal
contractions decrease every difference in (1.6), so the Markov property
holds term by term.  The Gamma jump density is strictly positive for every
`r>0`; therefore the killed jump process on a nonempty interval is
irreducible.  Direct iteration of its positive jump kernel, equivalently
standard Dirichlet-form irreducibility, gives

\[
 e^{-sL_T}\text{ positivity improving for every }s>0.         \tag{3.1}
\]

The scalar shift preserves this property:

\[
 e^{-sH_{0,T}}=e^{sm_T}e^{-sL_T}.                              \tag{3.2}
\]

Together with compact resolvent on a fixed window, this proves that
`H_(0,T)` has a simple strictly positive ground state.  Reflection symmetry
makes it even.  This proves the simple-even assertion for the Levy part,
not for the full CCM operator.

## 4. The exact rank-two obstruction

The jet perturbation is

\[
 R_{2,T}=|\phi_-\rangle\langle\phi_+|
        +|\phi_+\rangle\langle\phi_-|.                        \tag{4.1}
\]

Its kernel is

\[
 K_2(t,s)=2\cosh((t-s)/2)>0.                                  \tag{4.2}
\]

Nevertheless it is indefinite: if
`Phi(c_-,c_+)=c_-phi_-+c_+phi_+`, then `Phi` is injective and
`R_(2,T)=Phi C Phi*`.  Sylvester inertia gives one positive and one negative
direction.

The short-time sign test must include the off-diagonal part of `L_T`, not
only the jet block.  Away from the finitely many active prime-shift
distances, the continuous Gamma part has off-diagonal kernel

\[
 -w_\infty(|t-s|),\qquad
 w_\infty(r)={e^{-r/2}\over1-e^{-2r}}>0,                     \tag{4.3}
\]

up to the fixed normalization in (1.6), whereas the jet block contributes
`2 cosh(|t-s|/2)`.  Since `w_infty(r)` decays and `2 cosh(r/2)` grows, one
can choose a separation `r` in every sufficiently large window, avoiding
all active prime-shift distances, such that

\[
 2\cosh(r/2)>w_\infty(r).                                    \tag{4.4}
\]

Choose nonnegative smooth `f,g` with disjoint sufficiently small supports
around the two endpoints.  Shrinking the supports avoids every prime-shift
atom, and continuity of the remaining kernel gives

\[
 QW_T(f,g)>0.                                                 \tag{4.5}
\]

For a lower-bounded real symmetric form, positivity preservation of its
semigroup implies the first Beurling--Deny inequality
`q(u^+,u^-)<=0`.  Taking `u=f-g` in (4.5) violates that inequality (a scalar
shift has zero cross term on disjoint supports).  Thus, in the
expanding-window regime relevant to D.48, the full semigroup is not
positivity preserving.  The exact obstruction is the competition

\[
 K_{A_T}^{\rm off}(t,s)
 =-w_\infty(|t-s|)+2\cosh((t-s)/2)                            \tag{4.6}
\]

away from the prime atoms.  Adding `R_(2,T)` is therefore not a
positivity-preserving perturbation, and Perron--Frobenius cannot prove the
full CCM ground state simple-even.  No assertion is made here for windows
too short to contain a pair satisfying (4.4).

## 5. Birman--Schwinger reduction to two parity channels

Let

\[
 R_0(z)=(H_{0,T}-z)^{-1},\qquad G_T(z)=M_TR_0(z)M_T^*.         \tag{5.1}
\]

Since `C^(-1)=C`, the finite-rank resolvent identity is

\[
 \boxed{(A_T-z)^{-1}=R_0(z)-R_0(z)M_T^*
 (C+G_T(z))^{-1}M_TR_0(z).}                                  \tag{5.2}
\]

Eigenvalues not inherited from `H_(0,T)` are the zeros of

\[
 d_T(z)=\det(C+G_T(z)).                                       \tag{5.3}
\]

In the orthonormal even/odd jet basis

\[
 \phi_e=2^{-1/2}(\phi_++\phi_-),\qquad
 \phi_o=2^{-1/2}(\phi_+-\phi_-),                             \tag{5.4}
\]

reflection diagonalizes `G_T`, while `C=diag(1,-1)`.  Therefore

\[
 d_T(z)=(1+g_e(z))(-1+g_o(z)).                                \tag{5.5}
\]

This is an exact separation.  It does not order the first zeros of the two
factors.  Proving that the lowest zero is simple and in the even channel
requires a quantitative comparison of `g_e` and `g_o`; positivity improving
of `R_0` alone does not compare equations with opposite signs.

There can also be persistent eigenvalues: an eigenvector `v` of `H_(0,T)`
with `M_Tv=0` remains an eigenvector of `A_T` and is not detected as a new
zero of (5.3).  Positivity of the unperturbed ground state and
`phi_e>0` exclude persistence of the first even state.  They do not prove

\[
 \langle\phi_o,v_{o,0}\rangle\ne0                            \tag{5.6}
\]

for the first odd state.  Hence a reduction of the complete ground-state
ordering to the two first secular zeros requires (5.6), or full cyclicity in
each parity channel.  The cyclicity-free alternative is the rank-one Schur
inequality stated in D.50.

## 6. Schur complement on the primitive space

The jet term vanishes as a form on `K_T=ker M_T`, but `K_T` need not reduce
`H_(0,T)`.  When `H_(0,T)` is invertible, the constrained Green matrix is

\[
 \mathcal G_T=M_TH_{0,T}^{-1}M_T^*.                            \tag{6.1}
\]

D.47 gives the exact inertia identity

\[
 \operatorname{In}(H_{0,T}|_{K_T})
 =\operatorname{In}(H_{0,T})-\operatorname{In}(\mathcal G_T). \tag{6.2}
\]

In Markov language the missing primitive sign is

\[
 \boxed{
 \inf_{0\ne F\in K_T}{\langle F,L_TF\rangle\over\|F\|^2}
 \ge m_T.}                                                    \tag{6.3}
\]

The Markov property only gives `L_T>=0`.  Its ordinary spectral gap does not
give (6.3), because the two exponential constraints are not the first two
eigenfunction orthogonality conditions.  Thus the Schur complement removes
the jets algebraically but leaves precisely the D.47 index/gap theorem.

## 7. Doob audit

Let `h_T>0` be the simple ground state of `H_(0,T)`, with energy
`lambda_(0,T)`.  The Doob transform

\[
 \widetilde L_Tf=h_T^{-1}(H_{0,T}-\lambda_{0,T})(h_Tf)         \tag{7.1}
\]

is Markov and nonnegative.  It proves only

\[
 H_{0,T}\ge\lambda_{0,T}I.                                   \tag{7.2}
\]

Row D needs `H_(0,T)|_(K_T)>=0`, or (6.3).  The Doob transform subtracts
the unknown ground energy; it does not show that energy, or the constrained
third level, lies above zero.  Applying a Doob transform after adding the
jet block is unavailable because Section 4 destroys cone preservation.

## 8. Consequence for D.48 and viable continuation

This note proves a genuine partial result: before the polar jet block, the
exact `p^k+Gamma` operator has a simple even ground state on every fixed
window.  After proving the nonorthogonality/cyclicity condition (5.6), the
full CCM simple-even question reduces to the first-zero ordering of the two
scalar Birman--Schwinger factors in (5.5).  Without cyclicity, D.50 gives the
equivalent Schur-complement ordering test which also sees persistent states.

A viable next estimate is to show, with the appropriate sign convention,
that one parity factor has no zero below the first simple zero of the other.
Since `phi_e>0`, `phi_o` changes sign, and `R_0(z)` is positivity improving
below its spectrum, this contains more structure than the original matrix
problem.  It still requires a uniform quantitative inequality and is not
proved here.

For the CCM convergence step, (5.2) can also compare the true ground
projection with the prolate candidate once uniform estimates for
`g_e,g_o`, their derivatives, and the D.48 residual are obtained.

## 9. Exact answers

1. `e^(+/-t/2)` are boundary/residue functionals.  Prime jumps act by
   (2.1), cutoff creates boundary layers, and Gamma has the pole (2.3).
2. The Levy semigroup is positivity improving and its ground state is
   simple-even.  The full Weil semigroup has the exact off-diagonal defect
   \[
   R_{2,T}=M_T^*\begin{pmatrix}0&1\\1&0\end{pmatrix}M_T,
   \]
   which prevents that argument.
3. Schur complement yields the two scalar factors (5.5), but the primitive
   gap is (6.3), exactly the D.47/Weil gate.  No circular gap estimate has
   been obtained.
