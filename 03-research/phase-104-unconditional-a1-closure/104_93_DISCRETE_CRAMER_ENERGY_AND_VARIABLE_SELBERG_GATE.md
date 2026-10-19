# 104_93 — Discrete Cramér energy and variable-order Selberg gate

**Bibliographic priority correction.** The underlying continuous (L^2)
equivalence between RH and the weighted energy of (psi(x)-x) belongs
to the classical Cramér--Ingham--Titchmarsh framework. Until an
external gate with exact references and numbering is completed, no
novelty is claimed for equivalence (3) nor for its standard discrete
transfer. In any case, this coordinate is outside the active frontier:
it removes the compact--tail scaffolding and again presents RH as a
global energy.

**Result (equivalence, not a proof of RH).** Define

\[
 b_n={\Lambda(n)-1\over\log n},\qquad
 B_m=\sum_{2\le n\le m}b_n,
 \tag{1}
\]

and the increasing energy

\[
 \mathcal E(N)=\sum_{m=2}^{N}{B_m^2\over m(m+1)}.
 \tag{2}
\]

Then

\[
 \boxed{
 \mathrm {RH}
 \quad\Longleftrightarrow\quad
 \sup_N\mathcal E(N)<\infty
 \quad\Longleftrightarrow\quad
 \mathcal E(N)=N^{o(1)}.}
 \tag{3}
\]

Moreover, if \(\rho=\beta+i\gamma\) is a nontrivial zero with
\(\beta>1/2\), then

\[
 \boxed{
 \limsup_{N\to\infty}{\log\mathcal E(N)\over\log N}
 \ge 2\beta-1.}
 \tag{4}
\]

The energy has the exact finite identity

\[
 \boxed{
 \mathcal E(N)=
 \sum_{r,s\le N}b_rb_s
 \left\{{1\over\max(r,s)}-{1\over N+1}\right\}.}
 \tag{5}
\]

Therefore the term that would need to be bounded is not a Selberg
convolution: it is a Hermitian covariance in the ratio variable, since

\[
 {1\over\max(r,s)}
 ={1\over\sqrt{rs}}
   \exp\!\left(-{1\over2}|\log(r/s)|\right).
 \tag{6}
\]

The Selberg hierarchy, even allowing a variable order, does not
automatically give (3). Once centered by the comparator \(1\), its
second coefficient already has both signs. Without centering, the
positive hierarchy preserves only the product coordinate \(rs\), and
subtracting the comparator returns precisely the signed form.
Preserving instead the ratio mark \(r/s\) leaves (5) as the residual,
which by (3) has RH strength.

This is a **no-go for the Selberg/Vaughan class of rewritings**, not a
universal impossibility theorem. A new inequality specific to the
placement of ordinary primes could still prove
\(\mathcal E(N)=N^{o(1)}\); doing so would prove RH. This document does
not prove that inequality, Deep-\(\Lambda\), A1, or RH.

**No internal duplication.** `E101_090` isolates the ratio covariance
for the coefficients \(\Lambda(n)-1\) with a balanced cutoff, and
`104_89` uses the continuous energy of \(J(x)-\mathrm{Li}(x)\) for the
BSY gate. Here the exact discrete version (1)--(5) is closed, the
minimal threshold \(N^{o(1)}\) is identified, the quantitative
obstruction (4) is obtained, and the entire centered Selberg hierarchy
is audited against it.

---

## 1. The max form is exactly the energy

Extend \(B_m\) to the step function

\[
 B(x)=B_m\qquad(m\le x<m+1).
 \tag{7}
\]

Then

\[
 \int_2^{N+1}{B(x)^2\over x^2}\,dx
 =\sum_{m=2}^{N}B_m^2
   \left({1\over m}-{1\over m+1}\right)
 =\mathcal E(N).
 \tag{8}
\]

Expanding \(B_m^2\), all sums are finite and

\[
\begin{aligned}
 \mathcal E(N)
 &=\sum_{r,s\le N}b_rb_s
   \sum_{m=\max(r,s)}^N{1\over m(m+1)}\\
 &=\sum_{r,s\le N}b_rb_s
   \left\{{1\over\max(r,s)}-{1\over N+1}\right\},
\end{aligned}
\tag{9}
\]

which proves (5). The term \(-(N+1)^{-1}B_N^2\) is the moving
boundary; it cannot be dropped before taking the limit.

Identity (6) shows the two incompatible geometries:

\[
 \text{Selberg/Dirichlet: }\log(rs)=\log r+\log s,
 \qquad
 \text{Cramér: }|\log(r/s)|=|\log r-\log s|.
 \tag{10}
\]

## 2. RH implies finite energy

Set

\[
 J(x)=\sum_{2\le n\le x}{\Lambda(n)\over\log n},
 \qquad
 L_2(x)=\int_2^x{dt\over\log t},
 \qquad
 A(x)=J(x)-L_2(x).
 \tag{11}
\]

The Stieltjes partial sum is exact:

\[
 A(x)={\psi(x)-x\over\log x}
 +\int_2^x{\psi(t)-t\over t\log^2t}\,dt
 +{2\over\log2}.
 \tag{12}
\]

Under RH, the Cramér quadratic bound gives

\[
 \int_Y^{2Y}|\psi(t)-t|^2dt\ll Y^2.
 \tag{13}
\]

On the block \([Y,2Y]\), (13) implies

\[
 \int_Y^{2Y}{|\psi(x)-x|^2\over x^2\log^2x}\,dx
 \ll {1\over\log^2Y}.
 \tag{14}
\]

The sum of (14) over dyadic blocks converges. Likewise,
Cauchy--Schwarz on each block gives

\[
 \int_2^x{\psi(t)-t\over t\log^2t}\,dt
 =O\!\left({\sqrt x\over\log^2x}\right)+O(1),
 \tag{15}
\]

and hence the square of (15), divided by \(x^2\), is also integrable.
From (12)--(15),

\[
 \int_2^\infty {A(x)^2\over x^2}\,dx<\infty.
 \tag{16}
\]

It remains only to compare the integral with the discrete comparator.
Since \(f(x)=1/\log x\) is positive and decreasing, for every integer
\(m\ge2\),

\[
 0\le
 \sum_{n=2}^m f(n)-\int_2^m f(t)dt
 \le f(2).
 \tag{17}
\]

Indeed, on each interval \([n,n+1]\),
\(f(n+1)\le\int_n^{n+1}f\le f(n)\), and the errors telescope. By (1),
\(B(x)\) differs from \(A(x)\) by a bounded function. Equations
(16)--(17) and (8) prove

\[
 \mathrm {RH}\quad\Longrightarrow\quad
 \sup_N\mathcal E(N)<\infty.
 \tag{18}
\]

## 3. Subpolynomial energy excludes every right-hand zero

For \(\Re s>1\), define

\[
 G(s)=\sum_{n\ge2}{\Lambda(n)-1\over\log n}\,n^{-s}.
 \tag{19}
\]

The Euler product and term-by-term differentiation give

\[
 G(s)=\log\zeta(s)-C(s),
 \qquad
 C(s)=\sum_{n\ge2}{n^{-s}\over\log n},
 \qquad
 C'(s)=1-\zeta(s),
 \tag{20}
\]

and therefore

\[
 \boxed{G'(s)={\zeta'(s)\over\zeta(s)}+\zeta(s)-1.}
 \tag{21}
\]

By Abel summation,

\[
 G(s)=s\int_2^\infty B(x)x^{-s-1}\,dx.
 \tag{22}
\]

Now suppose \(\mathcal E(N)=N^{o(1)}\). For each \(\delta>0\), partial
summation applied to the positive increments of (2) gives

\[
 \int_2^\infty B(x)^2x^{-2-\delta}dx<\infty.
 \tag{23}
\]

More explicitly, use
\(\mathcal E(N)\ll_\delta N^{\delta/2}\) and

\[
 \int_m^{m+1}B(x)^2x^{-2-\delta}dx
 \le m^{-\delta}{B_m^2\over m(m+1)}.
\]

The resulting series converges because
\(\sum m^{-\delta}d\mathcal E(m)\) converges by Abel's theorem.

Fix \(\sigma>1/2\) and choose \(0<\delta<2\sigma-1\). By
Cauchy--Schwarz,

\[
\begin{aligned}
 \int_2^\infty |B(x)|x^{-\sigma-1}dx
 &\le
 \left(\int_2^\infty B(x)^2x^{-2-\delta}dx\right)^{1/2}
 \left(\int_2^\infty x^{-2\sigma+\delta}dx\right)^{1/2}
 <\infty.
\end{aligned}
\tag{24}
\]

The same argument is uniform on compacts. Thus (22) extends \(G\)
holomorphically to \(\Re s>1/2\).

Identity (21), initially valid on \(\Re s>1\), continues onto the
half-plane punctured by the zeros. If \(\rho\), \(\Re\rho>1/2\), were a
zero of multiplicity \(m_\rho\), then \(\zeta'/\zeta\) would have at
\(\rho\) a simple pole of residue \(m_\rho\), while \(G'\) and
\(\zeta-1\) would be holomorphic there. This is impossible. There are
no zeros to the right of the line; the functional equation also
excludes them to the left. This proves

\[
 \mathcal E(N)=N^{o(1)}\quad\Longrightarrow\quad\mathrm {RH}.
 \tag{25}
\]

Together with (18) this proves (3).

### 3.1 Quantitative cost of an exterior zero

Suppose a zero with real part \(\beta>1/2\) exists. If

\[
 L:=\limsup_{N\to\infty}{\log\mathcal E(N)\over\log N}
 <2\beta-1,
\]

choose \(\alpha\) with \(L<\alpha<2\beta-1\). Then
\(\mathcal E(N)=O(N^\alpha)\). The proof of (23)--(24), now with
\(\delta>\alpha\), extends \(G\) to
\(\Re s>(1+\alpha)/2\), a half-plane containing the given zero. The
same contradiction with (21) proves (4).

## 4. The centered Selberg identity loses the sign

Let \({\bf u}(1)=0\), \({\bf u}(n)=1\) for \(n\ge2\), and set

\[
 e=\Lambda-{\bf u},
 \qquad
 (\mathsf D f)(n)=(\log n)f(n).
 \tag{26}
\]

The positive Selberg identity is

\[
 b_{\rm S}=\mathsf D\Lambda+\Lambda*\Lambda\ge0.
 \tag{27}
\]

Centering it by the comparator defining (1) gives exactly

\[
\boxed{
 r:=\mathsf De+e*e
 =b_{\rm S}+2\Lambda-3\log+\tau-2,
}
\tag{28}
\]

for \(n\ge2\), where \(\tau(n)\) is the number of divisors. Indeed,

\[
 \Lambda*{\bf u}=\log-\Lambda,
 \qquad
 {\bf u}*{\bf u}=\tau-2.
 \tag{29}
\]

The centered coefficient already changes sign on primes:

\[
 r(p)=\log p\,(\log p-1),
 \qquad r(2)<0<r(3),
 \tag{30}
\]

because \(2<e<3\). Therefore (27) does not turn into a one-sided
induction for (1).

The full hierarchy exhibits the same subtraction. On \(\Re s>1\), set

\[
 H(s)=e^{G(s)}=\zeta(s)e^{-C(s)},
 \qquad
 E(s)=\sum_{n\ge2}e(n)n^{-s}=-{H'(s)\over H(s)}.
 \tag{31}
\]

Define \(S_1=e\) and

\[
 S_{k+1}=\mathsf D S_k+e*S_k.
 \tag{32}
\]

An induction by differentiation proves

\[
 \sum_{n\ge1}{S_k(n)\over n^s}
 =(-1)^k{H^{(k)}(s)\over H(s)}.
 \tag{33}
\]

For \(k=2\), (33) is exactly (28). In contrast, the uncentered
hierarchy, obtained by replacing \(e\) with \(\Lambda\), does have
nonnegative coefficients at every order; but subtracting the
continuous channel brings back (28) and its iterates. Estimating the
positive pieces separately destroys the pole--primes cancellation.

## 5. Why varying the order does not create the missing energy

The operations \(\mathsf D\) and \(*\) of (27)--(33) produce
polynomial weights in \(\log r+\log s\) on fibers \(rs=n\). Raising the
order changes the polynomial, not the projection map

\[
 (r,s)\longmapsto rs.
 \tag{34}
\]

The energy (5) needs, instead, the ratio mark \(r/s\). If that mark is
preserved before applying Cauchy--Schwarz, exactly the ratio
covariance (5) remains; if it is discarded, no collection of moments
of \(\log(rs)\) alone controls the kernel (6) as a one-sided
inequality. The information loss of the projection is already visible
in the two positive measures on \(\mathbb R_+^2\)

\[
 \nu_1=\delta_{(0,2)}+\delta_{(2,0)},
 \qquad
 \nu_2=2\delta_{(1,1)}.
 \tag{34a}
\]

Both have the same pushforward \(2\delta_2\) under
\((u,v)\mapsto u+v\), even with all their moments, but they integrate
\(e^{-|u-v|/2}\) to \(2e^{-1}\) and to \(2\), respectively. This
witness is not meant to replace the tensor structure of the Mangoldt
vector; it proves precisely that an estimate that first projects a
bivariate form onto the sum channel no longer contains the required
mark. Inverting the projection by using all Mangoldt coefficients
again restores the original vector, but supplies no bound. This is the
same product/ratio wall proved for the balanced cutoff in `E101_090`.

There is an additional test against diagonal estimates. For a prime,

\[
 b_p=1-{1\over\log p},
\]

so Mertens' theorem implies

\[
 \sum_{p\le N}{b_p^2\over p}\sim\log\log N.
 \tag{35}
\]

The positive diagonal of the first term of (5) diverges, while under
RH the full sum is bounded by (3). Any proof using absolute values, a
Montgomery--Vaughan diagonal, or separate Type I/II norms necessarily
loses the negative off-diagonal cancellation and the moving boundary.
A Vaughan decomposition remains a valid identity, but its useful
estimate would have to preserve that global cancellation; that is
again (5), not an automatic consequence of the decomposition.

### Scope of the no-go

`104_78` supplies the exact class falsifier. Its free monoid satisfies
unital renewal, prime towers of multiplicity one, positive weights, a
functional equation, an exponentially precise prime law in the degree,
and the positive Selberg hierarchy at **every** order. However it has

\[
 \beta_+=\log_6 3>{1\over2}
\]

and Deep density equal to \(1/4\). Applying the proof of Section 3 to
its graded counting function, its analogous centered energy cannot be
subpolynomial and has lower exponent at least

\[
 2\log_6 3-1>0.
 \tag{36}
\]

The model is lattice-based and does not use the placement of the
integers or of the ordinary primes. Hence it does not contradict (3).
It does prove that renewal, positivity, and the variable-order Selberg
hierarchy, taken as abstract axioms, do not imply the required energy.
What a successor must use is still the literal placement of the
ordinary weights \(\Lambda(m)\).

## 6. Logical status

```text
PROVED EQUIVALENCE:
  RH <=> sup_N E(N)<infinity <=> E(N)=N^{o(1)}.

PROVED IDENTITIES:
  discrete max/quotient form (5)--(6);
  centered Selberg identity (28);
  variable-order centered hierarchy (32)--(33);
  sign change r(2)<0<r(3);
  energy cost of an exterior zero (4).

PROVED CLASS NO-GO:
  positivity of the uncentered Selberg hierarchy,
  and Vaughan/Type I--II rewritings estimated by separate diagonals,
  do NOT imply subpolynomial energy.

NOT RULED OUT:
  a new inequality for the signed covariance (5) using the
  exact placement of all ordinary primes.

NOT PROVED:
  E(N)=N^{o(1)} unconditionally;
  Deep-Lambda, A1, or RH.
```

## 7. Reproduction

From the `tools` directory:

```bash
python3 discrete_cramer_selberg_gate_check.py
```

The checker uses only `Fraction`. It verifies (5) for arbitrary
rational families, the telescoping of the boundary, and rational
bounds on the \(\mathrm{arctanh}\,\) series that certify
\(\log2<1<\log3\). It uses no values of \(\zeta\), no zeros, and no
floating point.
