# Collective prime-tower square identity

## Result

The first-order cell expansion in `103_61` has a collective completion in
which its entire Taylor remainder is known exactly.  Let

\[
 q_1<q_2<\cdots,
 \qquad \ell_j=\Lambda(q_j),
 \qquad \Psi_j=\sum_{i\leq j}\ell_i=\psi(q_j),
 \tag{1}
\]

and put

\[
 d_j=q_j-1-\Psi_{j-1}-{\ell_j\over2}.
 \tag{2}
\]

For every \(n\geq0\) and \(\varepsilon>0\), set

\[
 \tau(x)=x^{-1-\varepsilon}L_n(\log x),
 \qquad
 E(x)=\psi(x)-x+1.
 \tag{3}
\]

Then the regulated canonical transport cost satisfies

\[
 \boxed{
 C_{n,\varepsilon}
 =\sum_{j\geq1}\ell_jd_j\tau'(q_j)
   -{1\over2}\int_1^\infty E(x)^2\tau''(x)\,dx.
 }
 \tag{4}
\]

Thus the correlated cell remainders are not an error to be bounded cell by
cell: together they are one signed square integral.  The first term is also
collective.  If

\[
 \mathcal H_j=\sum_{i\leq j}\ell_i(q_i-1)-{\Psi_j^2\over2},
 \qquad w_j=\tau'(q_j),
 \tag{5}
\]

then

\[
 \boxed{
 \sum_j\ell_jd_jw_j
 =\sum_j\mathcal H_j(w_j-w_{j+1})
 =\sum_j\ell_j(q_j-1)w_j
  -{1\over2}\sum_{i,j}\ell_i\ell_jw_{\max(i,j)}.
 }
 \tag{6}
\]

All three expressions converge at fixed regulator.  Equations (4)--(6)
use the exact weights \(\Lambda(p^k)=\log p\), couple different prime
towers through their cumulative mass, and contain no zero hypothesis.

## 1. The tail kernel is elementary

For the kernel of `103_59`, direct differentiation of the Laguerre identity

\[
 {d\over dv}\{e^{-(1+\varepsilon)v}L_n(v)\}
 =-e^{-(1+\varepsilon)v}
 \{(1+\varepsilon)L_n^{(1)}(v)
       -\varepsilon L_{n-1}^{(1)}(v)\}
 \tag{7}
\]

and decay at infinity give the exact simplification

\[
 T_{n,\varepsilon}(v)=e^{-(1+\varepsilon)v}L_n(v).
 \tag{8}
\]

Consequently (3) is precisely
\(T_{n,\varepsilon}(\log x)\), not a replacement kernel.  If

\[
 R(\varepsilon)=-{\zeta'\over\zeta}(1+\varepsilon)-{1\over\varepsilon},
 \tag{9}
\]

then absolute convergence at \(\varepsilon>0\), followed by the polynomial
formula for \(L_n\), also gives

\[
 \boxed{
 C_{n,\varepsilon}
 =\sum_{k=0}^n {\binom nk\over k!}R^{(k)}(\varepsilon).
 }
 \tag{10}
\]

Equivalently, as a germ at \(z=0\),

\[
 \boxed{
 \sum_{n\geq0}C_{n,\varepsilon}z^n
 ={1\over1-z}
 R\!\left(\varepsilon+{z\over1-z}\right).
 }
 \tag{11}
\]

This is a scalar check on every index and keeps the pole and all prime
towers paired before the Abel limit.

## 2. Cumulative first moments and the max kernel

Define the step function

\[
 \mathcal H(x)=\sum_{q_j\leq x}\ell_jd_j.
 \tag{12}
\]

Using (2) and expanding the square of the cumulative mass gives, at
\(q_r\leq x<q_{r+1}\),

\[
 \mathcal H(x)
 =\sum_{j\leq r}\ell_j(q_j-1)-{1\over2}\Psi_r^2.
 \tag{13}
\]

Indeed, the jump of the right side at \(q_j\) is

\[
 \ell_j(q_j-1)-\Psi_{j-1}\ell_j-{\ell_j^2\over2}
 =\ell_jd_j.
 \tag{14}
\]

Abel summation of (12), with \(w_j=\tau'(q_j)\), now proves the middle
expression in (6).  To prove the last one directly, observe that

\[
 {1\over2}\sum_{i,j}\ell_i\ell_jw_{\max(i,j)}
 =\sum_j\ell_j\left(\Psi_{j-1}+{\ell_j\over2}\right)w_j.
 \tag{15}
\]

Subtracting (15) from the first term on the last line of (6) gives (2).
This is the promised exact coupling between all prime towers through a
kernel of order \(\max(i,j)\).

For convergence, elementary Chebyshev growth gives
\(\Psi_j=O(q_j\log q_j)\), whereas
\(w_j=O_{n,\varepsilon}(q_j^{-2-\varepsilon}\log^n q_j)\).
The boundary term in Abel summation therefore vanishes, and the single and
double series in (6) converge after grouping by their maximal index.

## 3. Exact aggregation of every curvature remainder

There is a useful continuous form of (13).  Put

\[
 G(x)=\int_1^xE(t)\,dt.
 \tag{16}
\]

Stieltjes integration by parts gives

\[
 \sum_{q_j\leq x}\ell_j(q_j-1)
 =(x-1)\psi(x)-\int_1^x\psi(t)\,dt.
 \tag{17}
\]

Substituting \(\psi(x)=x-1+E(x)\) into (13) yields the exact identity

\[
 \boxed{\mathcal H(x)=-G(x)-{1\over2}E(x)^2.}
 \tag{18}
\]

The right side is constant between consecutive prime powers: there
\(G'=E\) and \(E'=-1\).  Its jumps are exactly (14).

The cumulative discrepancy form of the transport cost is

\[
 C_{n,\varepsilon}=-\int_1^\infty E(x)\tau'(x)\,dx.
 \tag{19}
\]

One integration by parts gives

\[
 C_{n,\varepsilon}=\int_1^\infty G(x)\tau''(x)\,dx.
 \tag{20}
\]

Insert (18) in (20).  Since
\(d\mathcal H=\sum_j\ell_jd_j\delta_{q_j}\), a second Stieltjes integration
by parts gives

\[
 -\int_1^\infty\mathcal H(x)\tau''(x)\,dx
 =\int_1^\infty\tau'(x)\,d\mathcal H(x)
 =\sum_j\ell_jd_j\tau'(q_j).
 \tag{21}
\]

Equations (20)--(21) prove (4).  The boundary terms vanish because
\(E(x)=O(x\log x)\), \(G(x),\mathcal H(x)=O(x^2\log^2x)\), and the
regulator supplies \(x^{-\varepsilon}\); sharper PNT input is unnecessary.

In particular (4) immediately gives the one-sided reduction

\[
 C_{n,\varepsilon}
 \leq
 \sum_j\mathcal H_j(w_j-w_{j+1})
 +{1\over2}\int_{\{\tau''<0\}}E(x)^2|\tau''(x)|\,dx.
 \tag{22}
\]

Unlike a cellwise absolute remainder, (22) discards every favorable
positive-curvature square and retains the arithmetic first moments only in
their collectively telescoped form.  Combining (22) with the exact target
of `103_59` reduces the remaining A1 step to bounding these two displayed
collective terms by \(\Delta A_n/2\), uniformly before
\(\varepsilon\downarrow0\).  No such bound is assumed in deriving the
identity.  That uniform estimate can still be as difficult as A1 itself:
(22) is a sharper exact reduction, not a closure of A1 or a proof of RH.
