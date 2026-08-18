# D.55 — Explicit high-mode cutoff and a finite Schur core

## 1. Purpose

D.54 supplies an unconditional prime-free base but ordinary
variation-diminution does not propagate it.  This note addresses the
infinite-dimensional obstruction in the first-crossing argument.  It proves
that, on every fixed support window, sufficiently high Fourier modes are
uniformly negative for the direct operator `B_nuc`.  Consequently all
positive index and every possible loss of the primitive Hodge inequality
are governed by an explicitly bounded finite-dimensional Schur complement.

Every prime power in the window and the complete Gamma multiplier are
included.  No screw positivity, zeta zero or RH assumption is used.

The result is a reduction, not a proof that the finite Schur core has the
required inertia.

## 2. Exact Fourier multiplier

Let

\[
 \mathcal P_T=\{(p,k):k\log p\leq2T\},\qquad
 c_{p,k}={\log p\over p^{k/2}},\qquad
 A_T=\sum_{(p,k)\in\mathcal P_T}c_{p,k}.                   \tag{2.1}
\]

For a function supported in `[-T,T]`, extended by zero to the line, D.10
and D.52 give

\[
 B_T(F,F)={1\over2\pi}\int_{\mathbb R}
 b_T(\tau)|\widehat F(\tau)|^2d\tau,                       \tag{2.2}
\]

where

\[
 b_T(\tau)=m_\infty(\tau)
 +2\sum_{(p,k)\in\mathcal P_T}c_{p,k}\cos(k\log p\,\tau), \tag{2.3}
\]

and

\[
 \begin{aligned}
 m_\infty(\tau)&=m_0-\ell(\tau),\\
 m_0&=\log\pi-\psi(1/4),\\
 \ell(\tau)&=\sum_{j=0}^\infty {1\over a_j}
 {\tau^2\over4a_j^2+\tau^2},\qquad a_j=j+1/4.
 \end{aligned}                                             \tag{2.4}
\]

Thus

\[
 b_T(\tau)\leq M_T:=m_0+2A_T                              \tag{2.5}
\]

for every real `tau`.  Formula (2.2) is important: although the shifts are
compressed to the support window, their quadratic forms remain full-line
translation correlations and hence diagonalize under Fourier transform.

## 3. An explicit Gamma cutoff

Fix any margin `eta>0`.  Define

\[
 C_T=M_T+\eta,
 \qquad
 N_T=\left\lceil{e^{2C_T}-5\over4}\right\rceil_+,
 \qquad
 R_T=2(N_T+1/4),                                           \tag{3.1}
\]

where the subscript `+` means the maximum with zero.  For `|tau|>=R_T` and
`0<=j<=N_T`, one has `2a_j<=R_T<=|tau|`, so

\[
 {\tau^2\over4a_j^2+\tau^2}\geq{1\over2}.                \tag{3.2}
\]

Moreover, monotonicity of `1/(x+1/4)` gives

\[
 {1\over2}\sum_{j=0}^{N_T}{1\over j+1/4}
 \geq {1\over2}\int_0^{N_T+1}{dx\over x+1/4}
 ={1\over2}\log(4N_T+5)\geq C_T.                         \tag{3.3}
\]

Combining (2.3)--(3.3) yields the pointwise high-frequency estimate

\[
 \boxed{b_T(\tau)\leq-\eta\qquad(|\tau|\geq R_T).}        \tag{3.4}
\]

This is very coarse—the cutoff is exponential in `A_T`—but it is explicit,
unconditional and contains the complete prime-power sum.

### 3.1 A much sharper certified digamma cutoff

The loss of `m_0` in (3.1) is unnecessary if the digamma function itself
is evaluated with directed error.  Put

\[
 \mathfrak a(\tau)=
 \mathrm{Re}\,\psi\left({1\over4}+{i\tau\over2}\right)
 -\log\pi.                                                   \tag{3.5}
\]

Then `m_infty=-mathfrak a`, and the convergent digamma series gives, for
`tau>0`,

\[
 \mathfrak a'(\tau)
 ={\tau\over2}\sum_{j=0}^\infty
 {j+1/4\over((j+1/4)^2+\tau^2/4)^2}>0.                     \tag{3.6}
\]

Moreover

\[
 \mathfrak a(\tau)=\log{\tau\over2\pi}+O(\tau^{-2}),
 \qquad \tau\longrightarrow+\infty.                       \tag{3.7}
\]

Thus, for every `eta>0`, there is a unique positive number
`R_T^sharp` determined by

\[
 \boxed{\mathfrak a(R_T^\sharp)=2A_T+\eta.}                 \tag{3.8}
\]

Monotonicity and `|cos|<=1` imply directly

\[
 \boxed{b_T(\tau)\leq-\eta
 \qquad(|\tau|\geq R_T^\sharp).}                            \tag{3.9}
\]

This is an exact characterization, not an asymptotic choice.  A rational
enclosure for `R_T^sharp` is certified by evaluating the positive series
for `mathfrak a` with an integral tail bound and bisecting; (3.6) proves
that a single sign change encloses the unique root.  The elementary
`R_T` of (3.1) remains a closed-form fallback, while every statement below
is valid with the substantially smaller `R_T^sharp`.

## 4. Time--band concentration and finite index

Let `Pi_R` be the Fourier projection to `[-R,R]` on the line and let

\[
 C_{T,R}=P_T\Pi_RP_T                                      \tag{4.1}
\]

be the prolate time--band concentration operator on `L^2([-T,T])`.  It is a
positive trace-class contraction and

\[
 \mathrm{Tr}\,C_{T,R}={2TR\over\pi}.                  \tag{4.2}
\]

Equations (2.5) and either (3.4) or (3.9) imply, with respectively
`R=R_T` or `R=R_T^sharp`,

\[
 B_T(F,F)
 \leq(M_T+\eta)\langle C_{T,R}F,F\rangle
       -\eta\|F\|^2.                                      \tag{4.3}
\]

Set

\[
 \beta_T={\eta\over2(M_T+\eta)}                           \tag{4.4}
\]

and let `E_T` be the span of the eigenvectors of `C_(T,R)` whose
eigenvalues exceed `beta_T`.  The trace bound gives

\[
 \boxed{
 d_T:=\dim E_T
 \leq {\mathrm{Tr}\,C_{T,R}\over\beta_T}
 ={4TR(M_T+\eta)\over\pi\eta}.}                           \tag{4.5}
\]

If `Q_T` denotes the orthogonal complement of `E_T`, then (4.3) gives the
uniform form inequality

\[
 \boxed{Q_TB_TQ_T\leq-{eta\over2}Q_T.}                   \tag{4.6}
\]

In particular, no positive direction of `B_T` can be supported wholly in
the high prolate sector.  This removes the possible birth of positive index
from the zero accumulation of the compact screw-kernel representation.

## 5. Exact finite Schur reduction

Write the form of `B_T` in the decomposition `E_T direct-sum Q_T` as

\[
 B_T=\begin{pmatrix}A&C\\C^*&D\end{pmatrix},
 \qquad D\leq-\eta/2.                                     \tag{5.1}
\]

The high block is invertible with

\[
 \|D^{-1}\|\leq2/\eta.                                   \tag{5.2}
\]

The form version of Gaussian elimination gives the congruence

\[
 B_T\sim
 \begin{pmatrix}
 S_T&0\\0&D
 \end{pmatrix},
 \qquad
 \boxed{S_T=A-CD^{-1}C^*.}                                \tag{5.3}
\]

Since `D` is strictly negative,

\[
 \boxed{n_+(B_T)=n_+(S_T),}                               \tag{5.4}
\]

and `S_T` is a matrix of size at most the explicit integer in (4.5).

The two ruling moments can be incorporated by bordering this same matrix
with the two projected exponential vectors.  Equivalently, once `S_T` and
the finite projections of `M_T` are known, the constrained Haynsworth
calculation of D.47 is finite-dimensional.  Thus both requirements

\[
 n_+(B_T)=1,
 \qquad\mathrm{In}(M_TB_T^{-1}M_T^*)=(1,1,0)        \tag{5.5}
\]

are reduced to the finite Schur core plus two boundary coordinates.

## 6. Rigorous certification of the Schur entries

Formula (5.3) is not merely a formal finite matrix.  Its entries can be
certified by residual estimates.  For a core basis vector `e_i`, solve
approximately in the high sector

\[
 Dy_i=-C^*e_i.                                             \tag{6.1}
\]

If `y_i^(N)` is a Galerkin approximation with residual

\[
 r_i=Dy_i^{(N)}+C^*e_i,                                    \tag{6.2}
\]

then (5.2) gives

\[
 \|y_i-y_i^{(N)}\|\leq{2\over\eta}\|r_i\|.              \tag{6.3}
\]

Consequently every entry

\[
 (S_T)_{ij}=\langle e_i,Ae_j\rangle
              +\langle C^*e_i,y_j\rangle                 \tag{6.4}
\]

has an explicit interval error at most

\[
 {2\over\eta}\|C^*e_i\|\,\|r_j\|.                       \tag{6.5}
\]

Interval arithmetic can therefore certify the inertia of `S_T` whenever
its eigenvalue enclosures avoid zero.  A zero enclosure identifies exactly
the finite crossing that requires further analysis; it cannot be blamed on
an uncontrolled high-frequency tail.

## 7. Uniformity on bounded support ranges

For `0<T<=T_max`, replace `A_T` by `A_(T_max)` in (3.1) or (3.8), and use
the corresponding common cutoff `R_(T_max)` (preferably
`R_(T_max)^sharp`).  The same proof yields

\[
 b_T(\tau)\leq-\eta\quad(|\tau|\geq R_{T_{max}})           \tag{7.1}
\]

for every `T` in the range.  The core dimensions are uniformly bounded by

\[
 d_T\leq {4T_{max}R_{T_{max}}
                 (M_{T_{max}}+\eta)\over\pi\eta}.         \tag{7.2}
\]

Hence a spectral-flow proof on any bounded interval of windows is a finite
matrix problem with a uniform high-mode margin.  Letting `T_max` tend to
infinity gives an explicit exhaustion, though not a single finite core for
all supports.

## 8. What this proves and what remains

The high-mode problem is closed in the following precise sense:

1. all `p^k` and the Gamma term have been included in one exact multiplier;
2. modes beyond `R_T` have a fixed negative margin;
3. the positive index is exactly the inertia of a finite Schur matrix;
4. this reduction is uniform on every bounded support range;
5. residual bounds make the finite matrix rigorously certifiable.

What is not proved is that the resulting finite matrix always has the D.47
inertia.  Establishing that statement uniformly in `T` is still equivalent,
through A--B--C, to the missing global primitive inequality.  Merely
computing finitely many windows cannot replace a proof on the continuum.

The reduction is noncircular: it uses only the digamma series, positive
von Mangoldt coefficients, Fourier diagonalization and the trace of the
prolate concentration operator.  It never assumes that `g` is a screw
function or that the Weil form is positive.

## 9. Verdict

There is no uncontrolled creation of positive `B_nuc` modes at arbitrarily
high frequency on a fixed window.  Every possible obstruction to row D is
contained in an explicit finite prolate Schur core, enlarged by the two
ruling vectors.  The remaining global problem is to prove the required
inertia of this finite but `T`-dependent core through all crossings.
