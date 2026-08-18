# Von Mangoldt quantile cost: exact cells, Laguerre lobes, and tower no-go

## Verdict

The canonical transport of `103_59` can be decomposed completely into one
cell for every prime power.  If \(q=p^k\), the cell has exactly the length
\(\log p\), its endpoints are

\[
 a_q=1+\psi(q^-),\qquad b_q=1+\psi(q)=a_q+\log p,
 \tag{1}
\]

and it transports the continuous interval \([a_q,b_q]\) to the atom at
\(q\).  Its cost is an exact quadrature error.  This note gives two useful
forms of that error:

1. an integral against the Laguerre kernel with an explicit signed tent
   multiplier, which permits a rigorous split at every zero of the kernel;
2. an exact first-moment term involving the local Chebyshev deficit
   \(q-1-\psi(q)+\frac12\log p\), plus a second-derivative remainder.

These identities do not produce a uniform sign.  Even after every
prime-power position \(p^k\) is tied to its exact weight \(\log p\), the
response of one complete prime tower has both signs: at index \(n=2\), the
\(p=2\) tower is strictly negative and the \(p=101\) tower is strictly
positive.  This is proved by rational inequalities, not numerics.  Hence no
rearrangement assigning one nonnegative contribution to each prime tower can
close A1.

The remaining possible mechanism is collective cancellation between towers
and consecutive Laguerre lobes in the exact matrix (18) below.  A
Vinogradov--Korobov envelope makes the cells logarithmically short, but it
does not control that signed matrix: outside the few zero-crossing cells,
the leading cell signs still alternate with \(L_n^{(1)}(\log q)\).  No
uniform first-difference theorem, A1 proof, or RH proof is claimed.

## 1. Exact quantile cells

Fix \(n\geq1\) and \(\varepsilon>0\), and retain the completed kernel and
tail response of `103_59`:

\[
 \begin{split}
 K_{n,\varepsilon}(u)
  &=(1+\varepsilon)L_n^{(1)}(u)
    -\varepsilon L_{n-1}^{(1)}(u),\\
 T_{n,\varepsilon}(v)
  &=\int_v^\infty e^{-(1+\varepsilon)u}
       K_{n,\varepsilon}(u)\,du,\\
 \tau_{n,\varepsilon}(x)
  &=T_{n,\varepsilon}(\log x).
 \end{split}
 \tag{2}
\]

List the distinct prime powers increasingly.  There is no collision between
powers of distinct primes, since \(p^j=r^k\) with primes \(p,r\) forces
\(p=r\).  On the mass interval

\[
 \psi(q^-)<y\leq\psi(q),
 \tag{3}
\]

the generalized inverse \(Q(y)=\inf\{x:\psi(x)\geq y\}\) is exactly \(q\).
Changing variables \(x=1+y\) in the quantile cost therefore gives

\[
 \boxed{\quad
 C_{n,\varepsilon}
 =\sum_{q=p^k}C_{q;n,\varepsilon},\qquad
 C_{q;n,\varepsilon}
 =\int_{a_q}^{b_q}\{\tau_{n,\varepsilon}(q)
                     -\tau_{n,\varepsilon}(x)\}\,dx.
 \quad}
 \tag{4}
\]

At fixed \(\varepsilon>0\), both sides are absolutely convergent.  Formula
(4) is not an arbitrary allocation of the continuous pole mass: (1) is the
unique increasing quantile coupling.  The first-difference identity becomes

\[
 \boxed{\quad
 \Delta D_n=\Delta A_n-2\lim_{\varepsilon\downarrow0}
  \sum_{q=p^k}C_{q;n,\varepsilon}.
 \quad}
 \tag{5}
\]

The regulator is retained outside the whole sum in (5).

## 2. Exact tent multiplier and the zero partition

For real \(a<b\) and \(c>0\), define the oriented tent multiplier

\[
 M_{a,b,c}(t)=\int_a^b {\bf 1}^{\rm or}_{[x,c]}(t)\,dx,
 \tag{6}
\]

where the oriented indicator is \(+1\) on \((x,c)\) if \(x<c\), \(-1\)
on \((c,x)\) if \(c<x\), and zero otherwise.  Fubini's theorem on the
compact support of this function gives

\[
 \int_a^b\{\tau(c)-\tau(x)\}\,dx
 =\int_0^\infty M_{a,b,c}(t)\tau'(t)\,dt.
 \tag{7}
\]

There are only three shapes.  Writing \(w=b-a\):

\[
 M_{a,b,c}(t)=
 \begin{cases}
  t-a,&a\leq t\leq b,\\
  w,&b\leq t\leq c,\\
  0,&\text{otherwise},
 \end{cases}
 \quad(c\geq b),
 \tag{8}
\]

\[
 M_{a,b,c}(t)=
 \begin{cases}
  t-a,&a\leq t\leq c,\\
  -(b-t),&c\leq t\leq b,\\
  0,&\text{otherwise},
 \end{cases}
 \quad(a<c<b),
 \tag{9}
\]

and

\[
 M_{a,b,c}(t)=
 \begin{cases}
  -w,&c\leq t\leq a,\\
  -(b-t),&a\leq t\leq b,\\
  0,&\text{otherwise},
 \end{cases}
 \quad(c\leq a).
 \tag{10}
\]

Direct differentiation of (2) gives

\[
 \tau_{n,\varepsilon}'(t)
 =-t^{-2-\varepsilon}K_{n,\varepsilon}(\log t).
 \tag{11}
\]

Thus every prime-power cell has the exact form

\[
 \boxed{\quad
 C_{q;n,\varepsilon}
 =-\int_0^\infty
 M_{a_q,b_q,q}(t)t^{-2-\varepsilon}
 K_{n,\varepsilon}(\log t)\,dt.
 \quad}
 \tag{12}
\]

Let \(r_1<\cdots<r_m\) be the distinct real zeros of
\(K_{n,\varepsilon}\), and set

\[
 z_0=0,\quad z_j=e^{r_j}\ (1\leq j\leq m),\quad z_{m+1}=\infty.
 \tag{13}
\]

No assertion about simplicity is needed: repeated zeros may simply be
listed once.  Splitting (12) at (13) is finite and exact:

\[
 C_{q;n,\varepsilon}
 =-\sum_{j=0}^{m}\int_{z_j}^{z_{j+1}}
 M_{a_q,b_q,q}(t)t^{-2-\varepsilon}
 K_{n,\varepsilon}(\log t)\,dt.
 \tag{14}
\]

On each open interval in (14), the Laguerre factor has one fixed sign.  The
tent factor also has a fixed sign except, in the middle case (9), at the
single point \(q\).  In particular:

* if \(q\geq b_q\), the tent is nonnegative, so a cell contained in one
  Laguerre lobe has sign opposite to that lobe;
* if \(q\leq a_q\), the tent is nonpositive, so its sign agrees with that
  lobe;
* if \(a_q<q<b_q\), the two halves must be retained with opposite signs.

This proves that a root-free cell has a decidable sign, but not a common
sign across cells.

For a global bookkeeping form, put

\[
 W_{qj}(t)=M_{a_q,b_q,q}(t){\bf1}_{(z_j,z_{j+1})}(t)
 \tag{15}
\]

and

\[
 \mathcal C_{j;n,\varepsilon}
 =-\sum_{q=p^k}\int_{z_j}^{z_{j+1}}
 W_{qj}(t)t^{-2-\varepsilon}K_{n,\varepsilon}(\log t)\,dt.
 \tag{16}
\]

Absolute convergence at fixed regulator permits the interchange, and

\[
 C_{n,\varepsilon}=\sum_{j=0}^{m}\mathcal C_{j;n,\varepsilon}.
 \tag{17}
\]

There is an independent cumulative check on this tent matrix.  The signed
measure \(d\psi(x)-dx\) on \([1,\infty)\) has cumulative function

\[
 S(x)=\psi(x)-(x-1)=\psi(x)-x+1.
 \tag{17a}
\]

Stieltjes integration by parts is ordinary at fixed \(\varepsilon>0\); its
two boundary terms vanish because \(S(1)=0\) and
\(\tau_{n,\varepsilon}(x)=O_{n,\varepsilon}
(x^{-1-\varepsilon}\log^n x)\).  Hence

\[
 \boxed{\quad
 C_{n,\varepsilon}
 =\int_1^\infty S(x)x^{-2-\varepsilon}
 K_{n,\varepsilon}(\log x)\,dx.
 \quad}
 \tag{17b}
\]

Splitting (17b) at the same \(z_j\) proves that the sum of all cell tents
inside a lobe is exactly the weighted cumulative discrepancy on that lobe.
In particular, no mass is lost in exchanging the cell and lobe sums.  It
also shows the remaining sign obstruction sharply: the Laguerre sign is
fixed on a lobe, but the actual cumulative discrepancy \(S\) has no
available uniform sign of the required strength.

Consequently the exact surviving lobe theorem would be

\[
 \boxed{\quad
 \limsup_{\varepsilon\downarrow0}
 \sum_{j=0}^{m}\mathcal C_{j;n,\varepsilon}
 \leq {1\over2}\Delta A_n.
 \quad}
 \tag{18}
\]

Unlike an absolute Laguerre load, (18) sums the signed cells within each
lobe first and retains the completed Abel limit.

## 3. Exact first moment and curvature remainder

The center and signed displacement of the \(q=p^k\) cell are

\[
 m_q={a_q+b_q\over2}
 =1+\psi(q)-{1\over2}\log p,
 \qquad
 d_q=q-m_q=q-1-\psi(q)+{1\over2}\log p.
 \tag{19}
\]

Taylor's theorem with integral remainder, applied on the convex hull of
\(\{a_q,b_q,q\}\), gives the exact decomposition

\[
 \boxed{\quad
 C_{q;n,\varepsilon}
 =(\log p)d_q\tau_{n,\varepsilon}'(q)
 +R_{q;n,\varepsilon}
 =-(\log p)d_q q^{-2-\varepsilon}
 K_{n,\varepsilon}(\log q)+R_{q;n,\varepsilon}.
 \quad}
 \tag{20}
\]

If \(J_q\) is that convex hull, then

\[
 |R_{q;n,\varepsilon}|
 \leq {1\over2}\sup_{t\in J_q}|\tau_{n,\varepsilon}''(t)|
       \int_{a_q}^{b_q}(x-q)^2\,dx
 \tag{21}
\]

and hence

\[
 |R_{q;n,\varepsilon}|
 \leq {1\over6}\sup_{t\in J_q}|\tau_{n,\varepsilon}''(t)|
 \{(b_q-q)^3-(a_q-q)^3\}.
 \tag{22}
\]

The expression in braces is positive because \(b_q>a_q\).  The derivative
needed in (21) is again explicit:

\[
 \tau_{n,\varepsilon}''(t)
 =t^{-3-\varepsilon}
 \{(2+\varepsilon)K_{n,\varepsilon}(\log t)
   -K_{n,\varepsilon}'(\log t)\}.
 \tag{23}
\]

Thus a proof based on local cells must control the signed main sum

\[
 -\sum_{q=p^k}(\log p)d_q q^{-2-\varepsilon}
 K_{n,\varepsilon}(\log q)
 \tag{24}
\]

and the correlated remainders (21), rather than the much larger absolute
Laguerre load.  Formula (19) shows why the exact arithmetic weights matter:
the displacement of the \(p^k\) atom depends on all earlier prime powers
through \(\psi(p^k)\), not only on \(p\) and \(k\).

## 4. What an unconditional PNT envelope does to a cell

Suppose, only in this section, that an available effective PNT estimate is
written in the form

\[
 |\psi(x)-x|\leq x\delta(x),\qquad
 \delta(x)=C\exp\{-\eta(\log x)\},
 \tag{25}
\]

for all sufficiently large \(x\).  From (1), without estimating a prime
gap, one gets

\[
 |q-a_q|\leq q\delta(q)+\log q+1,
 \qquad
 |q-b_q|\leq q\delta(q)+1.
 \tag{26}
\]

Once the right sides are at most \(q/2\), every point in the support of the
tent satisfies

\[
 |\log t-\log q|
 \leq 2\delta(q)+{2(\log q+1)\over q}.
 \tag{27}
\]

Therefore a cell can cross a zero \(r_j\) of the Laguerre kernel only if

\[
 |\log q-r_j|
 \leq2\delta(q)+{2(\log q+1)\over q}.
 \tag{28}
\]

This is a genuine localization result: in the oscillatory bulk, whose zero
spacing is of order one, the cells become logarithmically much shorter than
a lobe.  It does not prove (18).  For every cell not satisfying (28), (20)
still has the alternating leading factor
\(-K_{n,\varepsilon}(\log q)\).  Bounding its magnitude with (25) returns
an absolute PNT-error load of the type already scaled out in `103_56`.
What is missing is cancellation of the actual signed main terms (24) across
successive lobes.

## 5. Exact prime-tower response has both signs

It remains to test whether the relation

\[
 q=p^k,\qquad \Lambda(q)=\log p
 \tag{29}
\]

could itself force a useful sign after all powers of one prime are grouped.
At zero regulator, `103_59` gives

\[
 T_{n,0}(k\log p)=p^{-k}L_n^{(0)}(k\log p).
 \tag{30}
\]

The full response of the \(p\)-tower is therefore the absolutely convergent
quantity

\[
 R_{p,n}=\log p\sum_{k\geq1}p^{-k}L_n^{(0)}(k\log p).
 \tag{31}
\]

Summing first over \(n\) with the Laguerre generating function gives the
exact germ

\[
 \boxed{\quad
 \sum_{n\geq0}R_{p,n}z^n
 ={\log p\over1-z}\,{1\over p^{1/(1-z)}-1}.
 \quad}
 \tag{32}
\]

This generating function has positive values on a real neighborhood of
zero, but its Taylor coefficients do not have one sign.  For an exact
low-degree proof, use

\[
 L_2^{(0)}(x)=1-2x+{x^2\over2}
 \tag{33}
\]

and the geometric moment sums

\[
 \sum_{k\geq1}p^{-k}={1\over p-1},\quad
 \sum_{k\geq1}kp^{-k}={p\over(p-1)^2},\quad
 \sum_{k\geq1}k^2p^{-k}={p(p+1)\over(p-1)^3}.
 \tag{34}
\]

Writing \(l=\log p\), equations (31)--(34) give

\[
 R_{p,2}={l\over(p-1)^3}
 \left\{(p-1)^2-2lp(p-1)+{l^2\over2}p(p+1)\right\}.
 \tag{35}
\]

For \(p=2\), the braces reduce to

\[
 1-4l+3l^2=(3l-1)(l-1)<0,
 \tag{36}
\]

because \(1/2<\log2<1\).  Hence \(R_{2,2}<0\).

For \(p=101\), the quadratic in braces is increasing for \(l\geq4\),
since its derivative is

\[
 -2\cdot101\cdot100+l\cdot101\cdot102>0
 \qquad(l\geq4).
\]

Also \(\log101>4\), and evaluation at \(l=4\) gives

\[
 10000-8\cdot101\cdot100+8\cdot101\cdot102=11616>0.
 \tag{37}
\]

Therefore \(R_{101,2}>0\).  For completeness, all logarithmic comparisons
used here follow from the exact elementary bound \(2<e<3\).  The lower bound
is the first two terms of \(e=\sum_{m\geq0}1/m!\); for the upper bound use
\(m!\geq2^{m-1}\) for \(m\geq1\).  Hence
\(e^{1/2}<\sqrt3<2<e\), giving \(1/2<\log2<1\), and
\(e^4<3^4=81<101\), giving \(\log101>4\).  Thus (36)--(37) require no
decimal approximation.

Equations (36)--(37) are an exact counterexample to any lemma asserting
that grouping the positions \(k\log p\) with their prescribed common weight
\(\log p\) creates a fixed sign.  They do not falsify a collective theorem
which also uses the canonical cell endpoints (1), since those endpoints
couple different prime towers through \(\psi\).  They prove that such a
collective coupling is indispensable.

## Status

The von Mangoldt quantile mechanism is now explicit at three compatible
levels:

* individual cells: the quadrature identity (4);
* Laguerre lobes: the signed tent matrix (14)--(18);
* local arithmetic displacement: the main-term/remainder formula (19)--(24).

The PNT envelope localizes zero-crossing cells by (28), but supplies no sign
for the remaining alternating cells.  Exact prime-tower algebra eliminates
the simplest multiplicative rearrangement through the opposite signs
(36)--(37).  The unresolved theorem is a collective signed comparison for
the matrix (18), using the actual interlacing of all prime powers.  That is
still RH-strength through (5), and it has not been proved here.
