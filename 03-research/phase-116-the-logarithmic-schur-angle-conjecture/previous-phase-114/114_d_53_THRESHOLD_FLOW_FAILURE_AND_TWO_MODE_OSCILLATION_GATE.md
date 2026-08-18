# D.53 — Prime-power threshold flow: exact failure and the two-mode oscillation gate

## 1. Purpose

D.52 gives two exact realizations of the same primitive problem:

\[
 B_T=\Gamma_T+\sum_{a=k\log p\leq 2T}c_a(S_a+S_{-a}),
 \qquad c_a={\log p\over p^{k/2}}>0,                       \tag{1.1}
\]

and, for the continuous function `g` of D.52,

\[
 -B_T(F,F)=\langle K_{g,T}F',F'\rangle,
 \qquad F\in\ker M_+\cap\ker M_-.                         \tag{1.2}
\]

This note tests the most favorable possible spectral-flow mechanism: keep
the window fixed and turn on the prime-power summands in (1.1), one at a
time.  The calculation is unconditional and uses neither positivity of the
screw kernel nor information about zeta zeros.

The result is negative but decisive.  A prime-power crossing has no fixed
orientation.  Therefore the index theorem `n_+(B_T)=1` cannot follow from a
monotone threshold count.  The continuous kernel gives the same obstruction
through its hinge functions.  The correct replacement is a two-mode
oscillation theorem stated precisely in Section 6.

## 2. The exact crossing form

Fix a prime-power displacement `a` and write

\[
 W_a=c_a(S_a+S_{-a}).                                      \tag{2.1}
\]

Let `B_-` contain the Gamma term and any previously activated prime-power
terms, and consider

\[
 B(s)=B_-+sW_a,\qquad 0\leq s\leq1.                        \tag{2.2}
\]

If `lambda(s)` is a simple eigenvalue with normalized eigenvector `f(s)`,
the Feynman--Hellmann formula gives

\[
 \boxed{\lambda'(s)=
  \langle f(s),W_af(s)\rangle
  =2c_a\operatorname{Re}\langle f(s),S_af(s)\rangle.}     \tag{2.3}
\]

In particular, at a regular zero crossing the spectral-flow orientation is
the sign of a translated autocorrelation.  There is no positivity theorem
for that autocorrelation.

This is not merely an abstract possibility.  Choose a nonzero smooth bump
`h` such that `h`, `S_a h` and `S_(2a)h` have pairwise disjoint supports in
the window, and put

\[
 f_+=h+S_ah,\qquad f_-=h-S_ah.                              \tag{2.4}
\]

With either consistent convention for the compressed shift,

\[
 \langle f_+,W_af_+\rangle= 2c_a\|h\|^2,
 \qquad
 \langle f_-,W_af_-\rangle=-2c_a\|h\|^2.                  \tag{2.5}
\]

Thus the same arithmetic summand can drive an eigenvalue upward or
downward.  Positivity of the coefficient `c_a` does not orient the crossing.

## 3. An exact nonmonotone finite model

The absence of a sign in (2.3) can change the positive index in both
directions along one and the same activation path.  Let

\[
 A=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad
 \Gamma=\left(-{1\over3}I_2\right)\oplus
          \left({2\over3}I_2\right),\qquad
 W=A\oplus A,                                               \tag{3.1}
\]

and `B(s)=Gamma+sW`.  These are real self-adjoint, reflection-compatible
blocks, and `W` is exactly a direct sum of symmetrized shifts.  The four
eigenvalues are

\[
 -{1\over3}+s,\quad -{1\over3}-s,
 \quad {2\over3}+s,\quad {2\over3}-s.                      \tag{3.2}
\]

Consequently

\[
 n_+(B(s))=
 \begin{cases}
 2,&0\leq s<1/3,\\
 3,&1/3<s<2/3,\\
 2,&2/3<s\leq1.
 \end{cases}                                                \tag{3.3}
\]

The crossing at `s=1/3` has form `+1`; the crossing at `s=2/3` has form
`-1`.  This exact example disproves any proposed monotonicity argument that
uses only self-adjointness, reflection, positive arithmetic coefficients
and the symmetrized-shift form of a new threshold term.

It does not assert that the complete arithmetic operator has the behavior
of (3.3).  It proves that an additional arithmetic oscillation theorem is
indispensable.

## 4. Why varying the window does not repair the argument

The coupling path (2.2) is more favorable than the literal path in `T`.
When `T` crosses `a/2`, not only does the overlap supporting `S_a` begin to
open; simultaneously

1. the Hilbert space `L^2([-T,T])` changes;
2. every previously present compressed shift changes its boundary;
3. the compressed Gamma operator changes;
4. the two exponential boundary vectors change.

After transporting to a fixed Hilbert space, the derivative therefore has
boundary and dilation terms in addition to (2.3).  Since the isolated term
(2.3) already has both signs, literal support-threshold flow cannot acquire
monotonicity without a new theorem controlling all these correlations.

## 5. The identical obstruction in the continuous kernel

The contribution of `n=p^k`, with `a=log n` and `c_a=Lambda(n)/sqrt(n)`, to
the source function `g` is the hinge

\[
 g_a(t)=c_a(|t|-a)_+.                                      \tag{5.1}
\]

For compactly supported smooth `F`, two integrations by parts, in the sense
of distributions, give

\[
 \begin{aligned}
 \int\!\!\int g_a(t-s)F'(s)\overline{F'(t)}\,ds\,dt
 &=-\int\!\!\int g_a''(t-s)F(s)\overline{F(t)}\,ds\,dt\\
 &=-c_a\langle (S_a+S_{-a})F,F\rangle.                    \tag{5.2}
 \end{aligned}
\]

because

\[
 g_a''=c_a(\delta_a+\delta_{-a}).                          \tag{5.3}
\]

The centered terms in `K_(g_a)` vanish on derivatives, exactly as in D.52.
Equations (2.3) and (5.2) show that the continuous and direct pictures have
opposite signs on the primitive pullback, as required by (1.2), but the
same lack of a crossing orientation.  Each hinge kernel is indefinite; a
sum of positive hinge coefficients is not an operator-monotone path.

## 6. The correct pivot: a two-mode oscillation theorem

The continuous formulation isolates a precise noncircular theorem that
would close the primitive inequality.  Put

\[
 H_T^0=\{u\in L^2([-T,T]):\int u=0\},\qquad
 N_Tu=\left(\int e^{-t/2}u(t)dt,
             \int e^{t/2}u(t)dt\right),                    \tag{6.1}
\]

and let `A_T` denote `K_(g,T)` restricted to `H_T^0`.  For an invertible
Galerkin compression define

\[
 \mathcal G_T=N_TA_T^{-1}N_T^*.                            \tag{6.2}
\]

The following is a direct consequence of the constrained Haynsworth
identity and is the exact useful replacement for threshold monotonicity.

> **Two-mode oscillation gate.**  Suppose, uniformly under Galerkin
> exhaustion and with the Moore--Penrose range conditions at singular
> parameters, that for some `r_T in {0,1,2}`
> \[
> n_-(A_T)=r_T,
> \qquad n_-(\mathcal G_T)=r_T.                            \tag{6.3}
> \]
> Then
> \[
> A_T|_{\ker N_T}\geq0.                                   \tag{6.4}
> \]

Indeed,

\[
 n_-(A_T|_{\ker N_T})
 =n_-(A_T)-n_-(\mathcal G_T)=r_T-r_T=0.                    \tag{6.5}
\]

By D.52, (6.4) is exactly `B_T<=0` on the two-ruling primitive space.  The
strict version additionally requires no primitive zero mode.

Condition (6.3) has a genuine oscillation meaning: the complete kernel may
have at most two negative modes on the zero-mass space, and every negative
mode that occurs must be detected and removed by the two exponential
moments.  It does not assume screw positivity; it asks for a finite
negative-square bound and an independently checkable equality of negative
indices.  Under the stronger full Weil positivity one has `r_T=0`; the
criterion does not incorrectly force two negative modes in that case.

For a fully rigorous finite approximation, let `P` range over finite
partitions of `[-T,T]`, let `A_(T,P)` be the matrix of cell averages of
`K_g`, restricted to the cellwise zero-mass hyperplane, and let `N_(T,P)`
contain the corresponding cell averages of `e^(+-t/2)`.  Density of step
functions gives

\[
 n_-(A_T)=\sup_P n_-(A_{T,P}).                              \tag{6.6}
\]

Thus the missing source-side estimate can be stated without spectral
labels:

\[
 \boxed{
 n_-(A_{T,P})\leq2\ \text{for every }P,
 \quad n_-(\mathcal G_{T,P})=n_-(A_{T,P}).}                 \tag{6.7}
\]

This is the concrete oscillation/negative-squares problem for the explicit
function (2.1) of D.52.  A proof may use the Gamma--Lerch representation,
prime-power hinge structure, total positivity or variation diminution.  It
may not infer (6.7) from positivity of the Weil form, because that is the
conclusion.

## 7. Relation with the direct `B_nuc` gate

The continuous gate (6.3) and the direct D.52 gate

\[
 n_+(B_T)=1,\qquad
 \operatorname{In}(M_TB_T^{-1}M_T^*)=(1,1,0)               \tag{7.1}
\]

are two Schur-complement presentations of the same primitive conclusion,
not termwise equivalent index assertions.  The polar rank-two block is
present in `A_T=K_(g,T)` and absent from `B_T`; therefore one must not
identify `n_-(A_T)` with `n_+(B_T)` before applying the boundary Schur
complement.

The direct threshold flow fails because its crossing form is an unsigned
translation correlation.  The continuous pivot succeeds in reducing the
open theorem to exactly two statements: an at-most-two-negative-square
oscillation bound for `K_g` on the zero-mass space, and exhaustion of every
negative mode that actually occurs by the two Tate exponential moments.

## 8. Verdict

Prime-power activation does not give a monotone spectral flow.  The failure
is exact both in the shift operator and in the continuous hinge kernel, and
an explicit four-dimensional path exhibits upward and downward crossings.

Accordingly, D is **not** closed by threshold counting.  The next valid
target is the source-defined estimate (6.7), together with the matching
boundary negative index in (6.3).  Proving those estimates directly from the explicit
prime-power plus Gamma--Lerch kernel would establish the primitive Hodge
inequality without assuming screw positivity, the Weil criterion or the
location of zeta zeros.
