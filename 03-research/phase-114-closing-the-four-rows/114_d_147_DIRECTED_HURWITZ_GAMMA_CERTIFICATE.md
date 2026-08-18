# D.147 — Directed Hurwitz--Lerch certificate for the full Gamma block

## Verdict

The finite Legendre compression of the **complete** archimedean multiplier

\[
 \operatorname {Re}\psi(1/4+i\tau/2)-\psi(1/4)
\]

can be enclosed directly by Arb intervals.  The calculation contains every
quarter-shift oscillator; it has neither a Fourier grid nor an oscillator
cutoff.  Its implementation is
`114_d_147_hurwitz_gamma_arb.py`.

At \(T=\frac12\log5\), the directed calculation passed at

\[
 (N,\mathrm{dps})=(80,500),\qquad(170,1300).
\]

For \(N=170\), the last diagonal entry was enclosed as

\[
 9.5775652753006086463\ldots\quad
 \text{with radius }<5.8\,10^{-453}.
\]

The same calculation at 850 decimal digits left a radius of order
\(10^{-3}\) in that entry.  Thus the endpoint formulas cancel about 847
digits at mode 169; ordinary double precision or a few hundred bits cannot
certify this block.

This note certifies the archimedean matrix only.  Contact matrices, the two
Tate columns and the final constrained congruence are separate directed
objects.  No sign of the completed primitive form and no instance of RH is
assumed.  The paper is not modified.

## 1. Exact finite formula

Let \(D\) be differentiation in the Legendre basis
\((P_0,\ldots,P_{N-1})\),

\[
 W=\operatorname {diag}\bigl((2m+1)^{-1}\bigr),\qquad
 \mathcal N_T(M)={T\over2}S M S,
 \quad S=\operatorname {diag}\sqrt{2m+1}.
\]

Since \(D^N=0\),

\[
 Q(x)=x(I+xD)^{-1}=\sum_{r=0}^{N-1}(-1)^r x^{r+1}D^r. \tag{1.1}
\]

Write

\[
 a_m(x)=\sum_{r=0}^mP_m^{(r)}(-1)x^{r+1},\qquad
 b_m(x)=\sum_{r=0}^mP_m^{(r)}(1)x^{r+1},              \tag{1.2}
\]

and \(q^-(x)=Q(x)^t(1,-1,1,-1,\ldots)^t\).  The stable
one-sided Green calculation gives

\[
 E_b(T)=\mathcal N_T\left(
 2WQ(b^{-1}T^{-1})-a(b^{-1}T^{-1})q^-(b^{-1}T^{-1})^t
 +\text{transpose}
 +e^{-2bT}\bigl(bq^{-t}+\text{transpose}\bigr)
 \right).                                             \tag{1.3}
\]

The coefficient of \(b^{-1}\) in (1.3) is exactly \(2b^{-1}I\).
It therefore cancels before summing the oscillators
\(b_j=2j+\frac12\).  Every coefficient left has order at least two.
Consequently the full matrix is the finite expression

\[
 \begin{aligned}
 G_{\Gamma,N}(T)=-\mathcal N_T\sum_{r=2}^{2N}{T^{-r}\over2^r}
 \bigg[&\zeta(r,1/4)R_r\\
 &+e^{-T}\Phi(e^{-4T},r,1/4)S_r\bigg],               \tag{1.4}
 \end{aligned}
\]

where \(R_r,S_r\) are integer/rational matrices obtained from (1.1)--(1.3).
Formula (1.4) is D.146, rewritten in precisely the evaluation order used by
the directed implementation.

## 2. Why every enclosure is rigorous

The endpoint derivatives are evaluated as exact integers:

\[
 P_n^{(r)}(1)={(n+r)!\over2^r r!(n-r)!},\qquad
 P_n^{(r)}(-1)=(-1)^{n+r}P_n^{(r)}(1).                 \tag{2.1}
\]

The differentiation matrix is applied by exact parity suffix sums using

\[
 P_\ell'=\sum_{\substack{j<\ell\\\ell-j\ \mathrm{odd}}}(2j+1)P_j.   \tag{2.2}
\]

Arb evaluates \(\log5\), square roots, exponentials and Hurwitz zeta with
outward-rounded balls.  At the target window, \(e^{-4T}=1/25\).  For
\(r\ge2\), the Lerch factor is evaluated from the positive series

\[
 \Phi(1/25,r,1/4)=\sum_{j=0}^{J-1}{25^{-j}\over(j+1/4)^r}+\mathcal R_J,
\]

with the explicit directed bound

\[
 0<\mathcal R_J\le
 {25^{-J}\over(1-1/25)(J+1/4)^r}.                     \tag{2.3}
\]

All subsequent additions and matrix products are interval operations.
Thus every returned entry contains the corresponding exact integral.  The
program also verifies interval symmetry and strict positivity of all
diagonal entries, as required for the positive Gamma-difference form.

## 3. Independent normalization check

For the constant Legendre mode, the stable kernel has the closed form

\[
 E_{00}(b,T)={T\over2}\left(
 {4\over bT}-{2(1-e^{-2bT})\over(bT)^2}\right).        \tag{3.1}
\]

Therefore

\[
 \sum_{j\ge0}\left({2\over b_j}-E_{00}(b_j,T)\right)
 =3.1160937506669805958028028456487986543855\ldots .  \tag{3.2}
\]

An independent high-precision summation of the left side agrees with the
Arb enclosure of `exact_gamma_block(170,1300)[0,0]` to all checked digits.
This checks the sign, the \(T/2\) normalization, the quarter shift and the
exponential boundary term independently of the finite matrix algebra.

## 4. Consequence for the row-D calculation

The previous oscillator-truncation uncertainty is eliminated: on a chosen
finite polynomial subspace, the entire Gamma place is now one explicit
directed matrix.  After subtracting

\[
 m_0I,\qquad m_0=\log\pi-\psi(1/4),                   \tag{4.1}
\]

and the exact translated contacts for all active \(p^k\), one may short the
two columns

\[
 M_{\pm,n}=\int_{-T}^T\phi_n(t)e^{\pm t/2}\,dt        \tag{4.2}
\]

by an interval congruence.  This gives a genuine finite-block certificate.
It does not by itself prove the uniform all-window contractivity required
for row D.
