# Cell--lobe matrix: exact collapse and the first sign obstruction

## Verdict

The tent matrix of `103_61` has an exact sum over its cell index.  If the distinct prime
powers are \(q_1<q_2<\cdots\), \(w_r=\Lambda(q_r)\), and

\[
 a_r=1+\psi(q_r^-),\qquad b_r=1+\psi(q_r)=a_r+w_r,
 \tag{1}
\]

then, for \(t>1\) away from the countable set of endpoints,

\[
 \boxed{\qquad \sum_{r\geq1}M_{a_r,b_r,q_r}(t)
       =t-1-\psi(t)=-S(t).\qquad}
 \tag{2}
\]

Thus summing the cells inside a Laguerre lobe does not leave an unknown
two-dimensional matrix: it collapses exactly to the Chebyshev sawtooth.
This gives a useful gap--lobe moment formula below and retains every exact
endpoint (1).

It also gives a sharp no-go result.  Positivity, sign regularity, a
pointwise Gram/sum-of-squares factorization, and decreasing sign variation
all fail already upon adding the cell \(q=5\).  In fact, at the two rational
points

\[
 t_-={9\over2},\qquad t_+={101\over20},
 \tag{3}
\]

the total multiplier in (2) is respectively positive and negative.  Both
points lie in the first lobe of the lowest admissible Laguerre kernel
\(L_1^{(1)}(\log t)=2-\log t\).  Hence even ``sum all cells before taking the
lobe sign'' has no pointwise positivity, at the smallest possible index
\(n=1\).

Finally, the transport cost is separable:
\(c_\tau(x,q)=\tau(q)-\tau(x)\).  Its Monge cross difference is identically
zero, not strictly signed.  Monge optimality therefore cannot furnish the
missing A1 inequality.  Formula (2) does not prove A1 or RH; it proves that
any successful continuation must estimate a signed correlation of the
**actual** sawtooth \(S\) with consecutive Laguerre lobes.

## 1. A pointwise formula for one tent

For an interval \(a<b\), a target \(c>0\), and a point outside the
endpoints, the oriented-indicator definition in `103_61` gives

\[
 {\bf1}^{\rm or}_{[x,c]}(t)
 ={\bf1}_{x<t}-{\bf1}_{c<t}.
 \tag{4}
\]

Indeed, (4) is \(1\) when \(x<t<c\), is \(-1\) when \(c<t<x\), and is zero
otherwise.  Integrating in \(x\) yields the useful formula

\[
 \boxed{\quad
 M_{a,b,c}(t)
 =\bigl|[a,b]\cap(-\infty,t)\bigr|
  -(b-a){\bf1}_{c<t}.
 \quad}
 \tag{5}
\]

This single expression contains all three piecewise shapes in `103_61`.

The intervals in (1) are consecutive:

\[
 a_1=1,\qquad a_{r+1}=b_r,
 \tag{6}
\]

because the next interval starts after the cumulative jump just added.
The jump of \(\psi\) at \(p^k\) is \(\log p\).  Since
\(\psi(x)\to\infty\), the intervals tile \([1,\infty)\).  For fixed \(t\),
summing the first term of (5) over this tiling gives \(t-1\); summing the
second gives

\[
 \sum_{q_r<t}w_r=\psi(t^-).
 \tag{7}
\]

Equations (5)--(7) prove (2) off the endpoints.  Either convention at the
endpoints is harmless in every integral below.  Notice that (2) is a
pointwise theorem, stronger than merely comparing the two integral forms
in `103_61`.

There is also an exact finite-prefix version.  Put
\(W_R=\psi(q_R)\) and
\(P_R(t)=\sum_{r\leq R}M_{a_r,b_r,q_r}(t)\).  Then

\[
 \boxed{\quad
 P_R(t)=\min\{(t-1)_+,W_R\}
       -\sum_{\substack{r\leq R\\q_r<t}}w_r.
 \quad}
 \tag{8}
\]

This is the appropriate exact object for testing any induction in the
prime-power cells.

## 2. Explicit summation by Laguerre lobes

Fix \(n\geq1\) and \(\varepsilon>0\).  Let
\(I_j=(z_j,z_{j+1})\) be a lobe of
\(K_{n,\varepsilon}(\log t)\), and put

\[
 \sigma_j=\mathrm{sgn}\,K_{n,\varepsilon}(\log t)
 \quad(t\in I_j),\qquad
 h_{n,\varepsilon}(t)
 =t^{-2-\varepsilon}|K_{n,\varepsilon}(\log t)|.
 \tag{9}
\]

Let \(q_0=1\), let \(q_{r+1}\) be the next prime power after \(q_r\), and
write

\[
 B_r=1+\psi(q_r)\quad(r\geq1),\qquad B_0=1.
 \tag{10}
\]

On the prime-power gap \(G_r=(q_r,q_{r+1})\), one has
\(S(t)=B_r-t\).  Consequently (2) turns the cell--lobe entry sum into

\[
 \boxed{\quad
 \mathcal C_{j;n,\varepsilon}
 =\sigma_j\sum_{r\geq0}
   \int_{I_j\cap G_r}(B_r-t)h_{n,\varepsilon}(t)\,dt.
 \quad}
 \tag{11}
\]

If

\[
 H_{k,jr}=\int_{I_j\cap G_r}t^k
               h_{n,\varepsilon}(t)\,dt\qquad(k=0,1),
 \tag{12}
\]

the completely explicit matrix form is

\[
 \boxed{\quad
 \mathcal C_{j;n,\varepsilon}
 =\sigma_j\sum_{r\geq0}
       \{B_rH_{0,jr}-H_{1,jr}\}.
 \quad}
 \tag{13}
\]

Every arithmetic entry in (13) is the exact endpoint
\(B_r=1+\psi(q_r)\); no PNT envelope has replaced it.  The sign of an
overlap is determined by whether its weighted barycenter lies to the left
or right of \(B_r\).  Since \(B_r\) can lie inside \(G_r\), even one
gap--lobe overlap need not have a sign.

Summing (11) over \(j\) recovers exactly

\[
 C_{n,\varepsilon}
 =\int_1^\infty S(t)t^{-2-\varepsilon}
                K_{n,\varepsilon}(\log t)\,dt.
 \tag{14}
\]

Thus (11)--(13) are a genuine factorization of the cell bookkeeping, but
not a positive factorization.

## 3. Double summation by parts and its exact arithmetic primitive

For completeness, a second summation by parts can be performed without
losing the endpoints.  Define

\[
 G(x)=\int_1^xS(t)\,dt.
 \tag{15}
\]

Termwise integration of the step function \(\psi\) gives the exact finite
formula

\[
 \boxed{\quad
 G(x)=\sum_{q\leq x}\Lambda(q)(x-q)-{(x-1)^2\over2}.
 \quad}
 \tag{16}
\]

With
\(f_{n,\varepsilon}(x)=x^{-2-\varepsilon}
K_{n,\varepsilon}(\log x)\), ordinary integration by parts at fixed
\(\varepsilon\) yields

\[
 C_{n,\varepsilon}
 =-\int_1^\infty G(x)f'_{n,\varepsilon}(x)\,dx,
 \tag{17}
\]

where

\[
 f'_{n,\varepsilon}(x)
 =x^{-3-\varepsilon}
  \{K'_{n,\varepsilon}(\log x)
       -(2+\varepsilon)K_{n,\varepsilon}(\log x)\}.
 \tag{18}
\]

The boundary terms vanish at fixed regulator, using the same elementary
growth bounds as `103_61`.  Equations (16)--(18) preserve all prime-power
locations and weights.  They do not produce positivity: (18) is another
oscillatory Laguerre polynomial, while (16) is a signed discrepancy.  A
second integration therefore relocates, rather than removes, the required
cancellation.

In fact, neither orientation of (16) has a global sign.  This can be
proved by finite rational arithmetic:

\[
 \boxed{\qquad G(2976)>10,
 \qquad G(4000)<-3700.\qquad}
 \tag{18a}
\]

The exact verifier
`tools/cell_lobe_convex_order_certificate.py` proves (18a) as follows.  For
an integer \(m\), write \(m=2^kr\), with \(1\leq r<2\), and use

\[
 \log r=2\sum_{j=0}^{M}{z^{2j+1}\over2j+1}+R_M,
 \quad z={r-1\over r+1},
 \quad 0<R_M< {2z^{2M+3}\over(2M+3)(1-z^2)}.
 \tag{18b}
\]

It takes \(M=15\), rounds every logarithm outwards to the common rational
scale \(10^{20}\), enumerates the prime powers by an integer sieve, and
substitutes them in (16).  Its exact integer output is

\[
\begin{array}{c|rr}
x&10^{20}G(x)\text{ lower}&10^{20}G(x)\text{ upper}\\ \hline
2976&1009313655709241531976&1009313655716648191362\\
4000&-379008832999902707853844&-379008832999889300101502.
\end{array}
\tag{18c}
\]

All coefficients multiplying the logarithms in (16) are nonnegative, so
outward rounding is preserved by the final sum.  Equations (18b)--(18c)
are therefore a rational certificate, not floating-point evidence.
Consequently a direct convex-order closure requiring either \(G\geq0\) or
\(G\leq0\) is false for the actual von Mangoldt weights.

## 4. Exact minimal counterexample to cell-prefix positivity

The first distinct prime powers are \(2,3,4,5\).  Their right source
endpoints are

\[
 1+\log2,\quad1+\log6,\quad1+\log12,\quad1+\log60.
 \tag{19}
\]

For \(q=2,3,4\), these endpoints lie to the left of their targets:

\[
 1+\log2<2,\qquad1+\log6<3,\qquad1+\log12<4.
 \tag{20}
\]

Hence each of the first three tents is nonnegative, by the first shape in
`103_61`, and the prefix through \(q=4\) is nonnegative everywhere.

At \(q=5\), however,

\[
 a_5=1+\log12<5<1+\log60=b_5.
 \tag{21}
\]

This is the middle tent.  More sharply, the two rational points (3) obey

\[
 a_5<t_-<5<t_+<b_5.
 \tag{22}
\]

Therefore

\[
 M_{a_5,b_5,5}(t_-)=t_--a_5>0,
 \qquad
 M_{a_5,b_5,5}(t_+)=-(b_5-t_+)<0.
 \tag{23}
\]

All tents with target at most \(4\) have ended before either point, and
the next source interval starts at \(b_5>t_+\).  Thus (23) is also the sign
of the **total** sum (2) at those points.  Equivalently, directly from (2),

\[
 \sum_rM_r(t_-)={7\over2}-\log12>0,
 \qquad
 \sum_rM_r(t_+)={81\over20}-\log60<0.
 \tag{24}
\]

Here every comparison is rigorous and elementary.  The series for \(e\)
gives \(e>8/3\), proving \(\log12<3\).  Moreover, bounding the tail after
the fifth term by a geometric series gives

\[
 e=\sum_{k=0}^5{1\over k!}+\sum_{k=6}^\infty{1\over k!}
 <{163\over60}+{1\over600}
 ={1631\over600}<{87\over32}.
 \tag{25}
\]

For \(0<x<1\), \(e^x<1/(1-x)\).  Hence

\[
 e^{81/20}<\left({87\over32}\right)^4{20\over19}
 ={286448805\over4980736}<60,
 \tag{26}
\]

which proves \(\log60>81/20\).  These rational inequalities establish
(20)--(24) without decimal approximations.

The failure occurs inside one actual Laguerre lobe at the lowest index.
Indeed

\[
 K_{1,0}(\log t)=L_1^{(1)}(\log t)=2-\log t,
 \tag{27}
\]

whose first lobe is \(1<t<e^2\), and

\[
 e^2>{64\over9}>{101\over20}.
 \tag{28}
\]

Thus the total tent multiplier changes sign inside the first \(n=1\)
lobe.  No higher-index or asymptotic phenomenon is involved.

This also falsifies the natural lobe-local PSD proposal, not merely a
pointwise slogan.  If
\(0\ne g_+\in C_c^\infty((5,101/20))\), then throughout its support,

\[
 \sum_rM_r(t)=t-1-\log60<0,
 \qquad t^{-2}K_{1,0}(\log t)>0.
 \tag{28a}
\]

On the other hand, if
\(0\ne g_-\in C_c^\infty((9/2,19/4))\), then throughout its support,
\(\sum_rM_r(t)=t-1-\log12>0\), and the Laguerre factor is again positive.
Therefore the two possible global orientations of the multiplication form,

\[
 \mathscr Q_\pm[g]=\pm\int_1^{e^2}
 \left\{\sum_rM_r(t)\right\}t^{-2}K_{1,0}(\log t)
 |g(t)|^2\,dt
 \tag{28b}
\]

satisfy \(\mathscr Q_+[g_+]<0\) and \(\mathscr Q_-[g_-]<0\).  Hence neither
lobe-local orientation is PSD, already at \(n=1\).  This does not exclude a genuinely nonlocal Gram
operator with additional signed arithmetic terms; such an operator would
need a new identity not present in the tent matrix.

## 5. Consequences for the proposed positivity mechanisms

The exact example above has the following separate consequences.

1. **Pointwise positivity fails.**  Equation (24) has both signs.

2. **Prime-power prefix positivity and decreasing variation fail.**  The
   prefix ending at \(q=4\) is nonnegative by (20), whereas adding \(q=5\)
   creates a positive part before \(5\) and a negative part after \(5\).
   The number of sign regions can increase under the cell induction.

3. **Sign regularity fails at order one.**  The single row corresponding
   to \(q=5\) has opposite signs at the two rational columns (3).  No fixed
   row sign makes the tent kernel entrywise nonnegative.  Total positivity,
   which includes order-one minors, is therefore impossible for this
   matrix.

4. **Local PSD and pointwise Gram representations fail.**  Equations
   (28a)--(28b) give an exact negative quadratic form at \(n=1\).  In
   particular, any
   identity of the form
   \(\sum_rM_r(t)=\sum_k\alpha_k|v_k(t)|^2\) with
   \(\alpha_k\geq0\) is contradicted by the second inequality in (24).
   Of course one can write a *difference* of two Gram forms; that supplies
   no positivity theorem.

5. **Lobe-first positivity fails already for \(n=1\).**  Equations
   (24), (27), and (28) put both signs of the total multiplier under one
   fixed positive Laguerre lobe.  Assigning the lobe sign before integration
   cannot make its density nonnegative.

These claims concern precisely the proposed positive factorizations.  A
signed integral over the whole lobe can still have a useful sign through
nonlocal cancellation; (24) neither proves nor disproves such an estimate.

## 6. Why Monge and convex order give no additional inequality

The cell cost in `103_61` is generated by

\[
 c_\tau(x,q)=\tau(q)-\tau(x).
 \tag{29}
\]

For \(x_1<x_2\) and \(q_1<q_2\), its Monge cross difference is exactly

\[
 \begin{split}
 &c_\tau(x_1,q_1)+c_\tau(x_2,q_2)
  -c_\tau(x_1,q_2)-c_\tau(x_2,q_1)\\
 &\hspace{35mm}=0.
 \end{split}
 \tag{30}
\]

Thus every coupling of the same marginals has the same total separable
cost whenever the integrals converge.  The increasing quantile coupling is
canonical bookkeeping, but it is not selected by a strict Monge
inequality.  Similarly, a convex-order theorem would require inequalities
for an appropriate class of convex test functions; the actual test
\(x^{-1}L_n^{(0)}(\log x)\) is oscillatory, and (24) shows that even the
first integrated marginal discrepancy lacks one sign.

## Status

The exact cell--lobe matrix has been reduced to the gap moments (11)--(13),
and all endpoint dependence is retained through \(B_r=1+\psi(q_r)\).
The simplest Gram, total-positivity, Monge, convex-order, and
variation-decreasing routes are now rigorously excluded, with their first
failure at \(q=5\) and Laguerre index \(n=1\).

The surviving statement is a signed, nonlocal comparison of the quantities

\[
 \sigma_j\sum_r\{B_rH_{0,jr}-H_{1,jr}\}
 \tag{31}
\]

across consecutive lobes, followed by the completed Abel limit.  Proving
the required upper bound for (31) would be new arithmetic cancellation of
A1/RH strength.  It is not proved here, so no proof of A1 or RH is claimed.
