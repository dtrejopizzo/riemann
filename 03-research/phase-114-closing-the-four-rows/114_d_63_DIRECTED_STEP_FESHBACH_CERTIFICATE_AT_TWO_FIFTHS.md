# D.63 — A directed step--Feshbach certificate at `T=2/5`

## 1. Result

Let

\[
 T_c={2\over5},\qquad a=\log2,
 \qquad c={\log2\over\sqrt2}.
\]

This note retains the `p=2` translation exactly and proves

\[
 \boxed{QW_T(F,F)>0.0044\|F\|_2^2}                       \tag{1.1}
\]

on the two-Tate-moment primitive space for every

\[
 \boxed{|T-2/5|\leq10^{-12}.}                            \tag{1.2}
\]

The proof is an interval certificate for a finite step compression plus an
analytic Hilbert--Schmidt residual.  Floating eigenvalues are reported only
as diagnostics; the asserted constants use outward-rounded intervals.

## 2. A bounded lower form containing all relevant arithmetic

Put `b_j=2j+1/2` and retain `j=0,...,19`.  Since every omitted exponential
energy is nonnegative,

\[
 QW_T\geq q_{19,T}:=A_{0,T}-K_{19,T},                    \tag{2.1}
\]

on the primitive space, where

\[
 K_{19,T}(x,y)=\sum_{j=0}^{19}e^{-b_j|x-y|},             \tag{2.2}
\]

\[
 A_{0,T}=C_{19}I-cJ_a,qquad
 C_{19}=\sum_{j=0}^{19}{2\over b_j}-m_0,                 \tag{2.3}
\]

and `J_a=S_a+S_{-a}` compressed to `[-T,T]`.

Throughout the first cell `a>T`, hence `S_a^2=S_{-a}^2=0` and

\[
 J_a^2=P_E,                                              \tag{2.4}
\]

where `E` is the union of the two boundary overlap intervals.  In
particular,

\[
 A_{0,T}\geq(C_{19}-c)I>1.3483I.                        \tag{2.5}
\]

The complete Gamma factor is present in (2.1): the first twenty terms are
kept exactly and the omitted terms have the favorable sign.

## 3. Shift-invariant step space

At `T=2/5`, split the window into

\[
 [-T,T-a],\quad[T-a,a-T],\quad[a-T,T].                  \tag{3.1}
\]

Use respectively `36,196,36` equal cells.  The left and right boundary
meshes are translates by `a`, so their normalized indicator bases are
interchanged exactly by `J_a`.  Let `P` be the resulting step projection.
Then

\[
 \dim P=268,qquad [P,A_{0,T_c}]=0,qquad
 h_{max}<0.002992.                                       \tag{3.2}
\]

The entries of `PKP` are closed elementary expressions.  For a cell of
length `l`,

\[
 {1\over l}\iint_{I^2}e^{-b|x-y|}dxdy
 =2\left({1\over b}-{1-e^{-bl}\over b^2l}\right).       \tag{3.3}
\]

For disjoint cells `I=[u,v]`, `J=[r,s]`, `v<=r`, the normalized entry is

\[
 {(e^{bv}-e^{bu})(e^{-br}-e^{-bs})
  \over b^2\sqrt{|I||J|}}.                              \tag{3.4}
\]

Thus every finite entry is evaluated directly, without quadrature.

## 4. Exact treatment of the primitive constraints

Let

\[
 h_+(x)=e^{x/2},\qquad h_-(x)=e^{-x/2},qquad
 H=|h_+\rangle\langle h_+|+|h_-\rangle\langle h_-|.     \tag{4.1}
\]

For every primitive `F`, `<HF,F>=0`.  Hence for any `rho>0`,

\[
 q_{19,T}(F,F)=(q_{19,T}+\rho H)(F,F).                  \tag{4.2}
\]

We take `rho=10`.  This replaces a numerically delicate bordered
constraint by positivity of an ordinary Hermitian form.  Its finite
compression uses the exact cell averages

\[
 \langle |I|^{-1/2}1_I,e^{\pm x/2}\rangle
 ={2\over\sqrt{|I|}}|e^{\pm r/2}-e^{\pm u/2}|.          \tag{4.3}
\]

No approximate moment is declared to vanish.

## 5. Analytic residuals

### 5.1 Kernel residual

For a step projection of maximum cell length `h`, the Neumann Poincare
inequality on each cell gives

\[
 \|K_{19,T}-PK_{19,T}P\|
 \leq2\|(1-P)K_{19,T}\|_{HS}
 \leq {2h\over\pi}\sqrt{I_{19}(T)},                     \tag{5.1}
\]

where

\[
 I_{19}(T)\leq
 4T\sum_{i,j=0}^{19}
 {b_ib_j(1-e^{-2T(b_i+b_j)})\over b_i+b_j}.              \tag{5.2}
\]

Directed evaluation on (1.2) gives

\[
 \sqrt{I_{19}(T)}<71.020,qquad
 \epsilon_K<0.13525.                                    \tag{5.3}
\]

### 5.2 Rank-two moment residual

For the cell-average projection,

\[
 \|(1-P)h_\pm\|_2\leq {h\over\pi}\|h_\pm'\|_2.
\]

Using `||h_±||^2=2sinh T` and `||h_±'||=||h_±||/2`,

\[
 \begin{aligned}
 \rho\|H-PHP\|
 &\leq2\rho\sum_{\pm}\|h_\pm\|\|(1-P)h_\pm\|\\
 &<0.01565.                                               \tag{5.4}
 \end{aligned}
\]

The total infinite-dimensional residual is therefore

\[
 \boxed{\epsilon_{tot}<0.15090.}                         \tag{5.5}
\]

## 6. Directed finite spectral certificate

Form the `268 by 268` interval matrix

\[
 R_T=P(A_{0,T}-K_{19,T}+10H)P                           \tag{6.1}
\]

from (3.3), (3.4), and (4.3).  The constants `log 2`, `sqrt 2`, `pi`, and
Euler's constant are enclosed by the rational series used in D.57--D.59.
The reproducible Arb certificate constructs the two parity blocks, subtracts
`0.15530 I`, and encloses their midpoint spectra at 128-bit outward
rounding.  It then bounds the whole `T`-interval by the Frobenius norm of
the entry radii.  The shifted lower endpoints and common variation bound
are

\[
 \begin{array}{c|c|c}
 &\lambda_{min}(R_{T_c}-0.15530I)&
 \sup_T\|R_T-R_{T_c}\|\\ \hline
 \text{even}&>0.00711126729&<2.991393\,10^{-6}\\
 \text{odd}&>0.00015918236&<2.991393\,10^{-6}.
 \end{array}                                             \tag{6.2}
\]

Weyl's inequality therefore gives uniformly on (1.2)

\[
 \boxed{\lambda_{min}(R_T)>0.15530.}                    \tag{6.3}
\]

The smallest midpoint eigenvalue at the center is
`0.15545918...`; it is not used as an uncertified sign test.  The ball
certificate proves its enclosure and the variation estimate above.  The odd
shifted gap remains greater than `1.56*10^-4` after the complete variation
radius is subtracted.

Combining (5.5) and (6.3),

\[
 q_{19,T}(F,F)+10\langle HF,F\rangle
 >(0.15530-0.15090)\|F\|^2
 =0.0044\|F\|^2.                                        \tag{6.4}
\]

For primitive `F`, the rank-two term vanishes by (4.2).  Equations
(2.1) and (6.4) prove (1.1).

## 7. Parity audit

Reflection preserves the mesh, `A_0`, `K_19`, and `H`.  Reordering the
step basis into even and odd combinations splits (6.1) into two directed
blocks of sizes `134` and `134`.  The two moment vectors reduce respectively
to the `cosh(x/2)` and `sinh(x/2)` channels.  Both ball-certified blocks are positive;
the displayed common lower bound is the smaller one.  Thus the certificate
does not hide a parity channel or replace two primitive moments by one.

## 8. Status

This is the interior seed missing from D.61:

* finite dimension: `268` (`134+134` by parity);
* exact `p=2` shift: retained in `A_0`;
* complete Gamma factor: twenty exact positive energies plus a positive
  omitted tail;
* kernel residual: `<0.13525`;
* moment residual: `<0.01565`;
* certified primitive margin: `>0.0044`;
* certified support interval: `|T-2/5|<=10^-12`.

The next task is interval continuation from this seed across the first
cell and overlap with the endpoint interval of D.61.
