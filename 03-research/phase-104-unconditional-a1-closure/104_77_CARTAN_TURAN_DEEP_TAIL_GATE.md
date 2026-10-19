# 104_77 — Safe contour, Cartan--Turán, and deep tail gate

**Result.** The deep criterion of `104_75` was attacked directly,

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{\lambda_n+\log(n+1)\le-e^{\sqrt X}\}}\longrightarrow0.
 \tag{1}
\]

The safe contour of `104_74` allows rigorously separating, degree by
degree, a polynomial exterior part and a finite sum of interior
residues. At the scale of (1), the exterior part is negligible:

\[
 \lambda_n=C_{n,n}-Z_n,\qquad
 |C_{n,n}|\ll n^5\log^2n,
 \qquad
 Z_n=\sum_{|w_\rho|<r_n}m_\rho w_\rho^{-n}.              \tag{2}
\]

Therefore (1) is equivalent, in the RH/non-RH dichotomy, to a
one-sided density bound for \(Z_n\). This separation is unconditional
and does not assume the sum is empty.

The complex-analytic attack does not close that bound. Jensen exactly
measures the mass of those same poles, while Turán forces large power
sums whenever one exists. Both mechanisms have the opposite sign to
the one required to eliminate \(Z_n\). Cartan can remove disks
containing zeros, but a single removed disk may contain the pole that
produces a positive density of deep excursions; discarding it loses
precisely the information that must be controlled.

A quantitative falsifier stronger than the radial one of `104_74` is
added. The quartet \(w=2i\) preserves conjugation and functional
symmetry, has exponentially negative coefficients on a class of
density \(1/4\), but its continued generating function is **strictly
positive on the entire real ray** \(0<r<1\). Hence neither
Jensen/Cartan, nor Turán, nor the positivity and growth of the
continuation on the Euler ray can prove (1) without using an
additional inequality specific to the real weights \(\Lambda(m)\).

The document proves a reduction and a no-go for this complex-analysis
package. It does not prove (1), A1, or RH.

---

## 1. The interior residue is the whole deep observable

Set

\[
 \Phi(z)={\xi(1/(1-z))\over\xi(1)},\qquad
 \mathcal G(z)=z{\Phi'(z)\over\Phi(z)}
              =\sum_{n\ge1}\lambda_nz^n,                \tag{3}
\]

and, for each nontrivial zero \(\rho\),

\[
 w_\rho=1-{1\over\rho}.                                  \tag{4}
\]

Theorem 4.1 of `104_74` constructs, for every large \(N\), a radius

\[
 r_N\in[1-2/N,1-1/N]                                    \tag{5}
\]

that does not cross poles and for which

\[
 \lambda_n=C_{n,N}-
 \sum_{|w_\rho|<r_N}m_\rho w_\rho^{-n},
 \qquad
 |C_{n,N}|\le K N^5\log^2N\quad(N\le n\le2N),           \tag{6}
\]

with an absolute constant \(K\). RH has not been used. The sum in (6)
is real, because the set of poles is stable under conjugation.

Taking \(N=n\) (which is legitimate because the endpoint \(n=N\)
belongs to the range \(N\le n\le2N\) of Theorem 4.1), define, for
\(n\) large enough,

\[
 Z_n:=\sum_{|w_\rho|<r_n}m_\rho w_\rho^{-n},
 \qquad P_n:=K n^5\log^2n.                              \tag{7}
\]

The sum is finite: for each \(r_n<1\), the condition
\(|w_\rho|<r_n\) forces \(|\Im\rho|\) to be bounded. We set
\(Z_n:=0\) on the finite prefix the theorem does not cover; this
convention does not alter any of the densities below. From the first
covered index on, for \(S_X=e^{\sqrt X}\) and \(n\le X\), (6) gives
the exact inclusions

\[
 \begin{aligned}
 \{Z_n\ge S_X+P_n+\log(n+1)\}
 &\subseteq
 \{\lambda_n+\log(n+1)\le-S_X\},\\
 \{\lambda_n+\log(n+1)\le-S_X\}
 &\subseteq
 \{Z_n\ge S_X-P_n\}.
 \end{aligned}                                          \tag{8}
\]

On the interval \(K_0\sqrt X\le n\le X\), the error
\(P_n+\log(n+1)=e^{o(\sqrt X)}\) is negligible compared with \(S_X\).
This does not authorize replacing hard indicators by a Lipschitz
estimate. The correct equivalence uses the residue dichotomy.

### Proposition 1.1 (deep dichotomy of the residue sum)

The following statements are equivalent:

1. RH;
2. the mean of (1) tends to zero;
3. one has

   \[
   {1\over H_X}\sum_{n\le X}{1\over n}
   {\bf1}_{\{Z_n\ge e^{\sqrt X}+P_n+\log(n+1)\}}
   \longrightarrow0.                                    \tag{9}
   \]

**Proof.** If RH holds, there is no \(w_\rho\) with \(|w_\rho|<1\), so
\(Z_n=0\) and (9) is identically zero; (1) is as well, by
\(\lambda_n\ge0\).

If RH is false, `104_56` gives a dominant modulus \(R>1\), constants
\(c>0\), \(R_1<R\), and a syndetic set \(D\) of natural density
\(d>0\) such that

\[
 \lambda_n=-R^nS(n)+O(n^2R_1^n+n^2),
 \qquad S(n)>c\quad(n\in D).                            \tag{10}
\]

For large \(n\), the radius \(r_n\) contains all dominant poles.
Comparing (6) and (10), or directly separating those poles in (7),
gives

\[
 Z_n\ge {c\over2}R^n\qquad(n\in D)                      \tag{11}
\]

from a fixed index on. Choose \(K_0>1/\log R\). For
\(n\in D\cap[K_0\sqrt X,X]\), (11) dominates
\(e^{\sqrt X}+P_n+\log(n+1)\). By partial summation,

\[
 {1\over H_X}
 \sum_{\substack{K_0\sqrt X\le n\le X\\n\in D}}{1\over n}
 \longrightarrow {d\over2}>0.                          \tag{12}
\]

Thus (9) fails. The equivalence between 1 and 2 is Theorem 2.1 of
`104_75`. \(\square\)

Proposition 1.1 is not a new proof of RH: it identifies exactly what
would have to be bounded after the contour has removed all
subexponential error.

---

## 2. Jensen turns the question into vanishing interior mass

For \(0<r<1\) not crossing a zero, Jensen applied to (3) gives

\[
 J(r):={1\over2\pi}\int_0^{2\pi}
 \log|\Phi(re^{i\theta})|\,d\theta
 =\sum_{|w_\rho|<r}m_\rho\log{r\over|w_\rho|}\ge0.       \tag{13}
\]

Since \(\Phi(0)=1\), there is no central term. From (13),

\[
 \boxed{
 \mathrm {RH}\quad\Longleftrightarrow\quad
 J(r)=0\ \text{for every }0<r<1
 \quad\Longleftrightarrow\quad
 \liminf_{r\uparrow1}J(r)=0.}                           \tag{14}
\]

The last equivalence is rigorous: if there is an interior zero
\(w_0\) of \(\Phi\) (equivalently, a pole of \(\mathcal G\)), then,
for every \(r>|w_0|\),

\[
 J(r)\ge m_0\log{r\over|w_0|}
 \longrightarrow m_0\log{1\over|w_0|}>0.               \tag{15}
\]

Therefore a Jensen route must prove an **upper bound tending to
zero** for the non-negative quantity (13). Subharmonicity only
delivers the sign \(J(r)\ge0\). The ordinary growth bounds for
\(\xi\) give a positive bound for \(J(r)\), not the vanishing in
(15).

Cartan does not improve this logical point. When applied to a
truncated product, its lemmas give lower bounds for \(|\Phi|\) outside
a union of disks covering the zeros; the allowed sum of radii is a
parameter of the lemma, and Jensen supplies the weighted count used to
choose the truncation. But (15) shows that a single disk, however
small, may contain the zero that generates all the excursions in (11).
Removing the Cartan disks removes exactly the term \(Z_n\) that
appears in (9).

The loss is quantitative, not merely logical. For \(0<|a|<1\), the
elementary meromorphic function

\[
 f_a(z)={1\over1-z/a}=\sum_{n\ge0}a^{-n}z^n
 \qquad(|z|<|a|)                                        \tag{15a}
\]

has exponential coefficients, while its Nevanlinna characteristic
remains bounded as \(r\uparrow1\): the counting term for the single
pole is \(N(r,f_a)=\log(r/|a|)\) for \(r>|a|\), and the proximity term
is \(O_a(1)\). Thus even a uniform bound on the Nevanlinna
characteristic is compatible with coefficients \(|a|^{-n}\). To
recover those coefficients one must explicitly add the principal part
at \(a\), which is exactly the \(Z_n\) summand in (7).

---

## 3. Turán forces the bad tail; it does not exclude it

Let \(R>1\) be the maximum of \(|w_\rho|^{-1}\) over the interior poles
of \(\mathcal G\) (the interior zeros of \(\Phi\)) and
write the dominant modes as

\[
 w_j^{-1}=Re^{i\phi_j}\qquad(1\le j\le M).              \tag{16}
\]

The dominant power sum is

\[
 R^nS(n),\qquad S(n)=\sum_{j=1}^M m_j\cos(n\phi_j).      \tag{17}
\]

Turán's power-sum theorems prove that a nonzero family like (17)
reaches a size comparable with \(R^n\) on blocks of length controlled
by the number of modes. For the real sign needed here, no quantitative
version is needed: the compact closure of the rotation
\(n(\phi_1,\ldots,\phi_M)\) contains the origin, and every neighborhood
of the origin has a syndetic set of returns. On those returns,

\[
 S(n)>{1\over2}\sum_{j=1}^Mm_j>0.                       \tag{18}
\]

Equations (17)--(18) are precisely the mechanism of (11). Thus, Turán
confirms that every interior pole of \(\mathcal G\) produces the deep
tail with positive density. To deduce (9), one would first have to
prove that no mode \(|w_j|^{-1}>1\) exists, or that all its residues
vanish. In the logarithmic derivative, the residues are the positive
multiplicities \(m_j\), so they cannot vanish mode by mode.

This is the exact meaning of the gate: Turán is an effective non-RH
detector, but its natural inequality is a **lower bound on
excursions**, while (9) needs an upper bound that eliminates them.

---

## 4. Falsifier on the real Euler ray

The Jensen--Cartan--Turán package might try to strengthen itself by
using that, for \(s>1\), the real logarithmic derivative comes from
the positive weights \(\Lambda(m)\). Positivity or growth on that
single ray do not control the complex poles.

Consider the rational quartet with \(w=2i\) and coefficients

\[
 q_n=4-2\Re\{w^n+w^{-n}\}.                              \tag{19}
\]

Its generating function, initially for \(|z|<1/2\), has the rational
continuation

\[
 \mathcal Q(z)
 ={4z\over1-z}
 -{wz\over1-wz}-{\bar w z\over1-\bar w z}
 -{w^{-1}z\over1-w^{-1}z}
 -{\bar w^{-1}z\over1-\bar w^{-1}z}.                   \tag{20}
\]

For real \(z=r\), the conjugate terms of (20) can be grouped into two
real parts. On the whole ray \(0<r<1\), (20) is regular and satisfies
the exact identity

\[
 \boxed{
 \mathcal Q(r)
 ={4r\over1-r}
  +{8r^2\over1+4r^2}
  +{2r^2\over4+r^2}>0.}                                 \tag{21}
\]

However, for \(4\mid n\),

\[
 q_n=4-2(2^n+2^{-n})=-2^{n+1}+4+O(2^{-n}),              \tag{22}
\]

and the other three classes have no negative excursion of that rate.
From (22),

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\{q_n+\log(n+1)\le-e^{\sqrt X}\}}
 \longrightarrow{1\over8}.}                            \tag{23}
\]

Indeed, the multiples of four that count begin at
\(n=(1/\log2+o(1))\sqrt X\), and their harmonic mass is

\[
 {1\over4}\left(\log X-{1\over2}\log X+O(1)\right)
 ={1\over8}\log X+O(1).                                \tag{24}
\]

The quartet does not have the Euler product of \(\zeta\), and
therefore does not refute a new inequality that uses the exact
sequence \(\Lambda(m)\). It does refute the inference

\[
 \begin{gathered}
 \text{functional symmetry + conjugation + finite growth}\cr
 \text{+ Jensen/Cartan/Turán + positivity on the real ray}
 \end{gathered}
 \quad\Longrightarrow\quad\text{vanishing deep tail}.   \tag{25}
\]

The key detail is that the continuation of (20) is positive for
\(r>1/2\), but there it no longer coincides with the sum of its Taylor
series: the poles \(z=\pm i/2\) reduce the radius to \(1/2\). Using the
real continuation as an Abel sum of the coefficients after crossing
those poles would omit exactly the interior residues.

---

## 5. Balance and missing theorem

**Proved unconditionally:**

* the safe reduction (6)--(9), without assuming the absence of poles;
* the scalar Jensen equivalence (14);
* that Turán and compact recurrence force, rather than suppress, the
  deep tail produced by a pole;
* the falsifier (21)--(23), which keeps the entire real ray positive.

**Not proved:** the bound (9) for the residues of the real \(\zeta\),
the arithmetic criterion (22a) of `104_75`, A1, or RH.

The missing input can be written without contours:

\[
 {1\over H_X}\sum_{n\le X}{1\over n}
 {\bf1}_{\left\{
 Q_{n,\varepsilon_X}\ge
 A_n+p_n(\varepsilon_X)+\log(n+1)+e^{\sqrt X}
 \right\}}\longrightarrow0,                            \tag{26}
\]

or, after the safe contour, as (9). Either statement is equivalent to
RH; assuming that \(\mathcal G\) is holomorphic in the disk, that
\(J(r)=0\), that \(Z_n=0\), or that the Hadamard semigroup has
positive radius would be using that conclusion circularly.

The complex route can only advance if it produces, from the exact
weights \(\Lambda(m)\), a one-sided bound for (26) that includes the
residues instead of removing them via Cartan disks or a holomorphy
hypothesis.

---

## 6. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 cartan_turan_deep_tail_check.py
```

The checker verifies the positive formula (21), the coefficient
identity (19)--(20), the exponential sign (22), and the numerical
convergence of the harmonic mass of (23) toward \(1/8\).
