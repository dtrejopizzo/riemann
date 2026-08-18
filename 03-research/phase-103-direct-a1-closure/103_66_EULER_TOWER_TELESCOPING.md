# Euler-tower telescoping: exact multiplicative annuli and the normalized germ

## Result

The prime-tower response admits an exact telescoping which should be made
before any estimate.  Fix \(n\geq0\) and \(\varepsilon>0\), and retain the
completed kernel of `103_59`,

\[
 K_{n,\varepsilon}(u)
 =(1+\varepsilon)L_n^{(1)}(u)
   -\varepsilon L_{n-1}^{(1)}(u),
 \qquad
 T_{n,\varepsilon}(v)
 =\int_v^\infty e^{-(1+\varepsilon)u}
       K_{n,\varepsilon}(u)\,du .
\tag{1}
\]

For \(n=0\) the convention is \(L_{-1}^{(1)}=0\).

There are three compatible exact collapses:

\[
 \boxed{\quad T_{n,\varepsilon}(v)
 =e^{-(1+\varepsilon)v}L_n(v),\quad}
\tag{2}
\]

\[
 \boxed{\quad
 \log p\sum_{k\geq1}T_{n,\varepsilon}(k\log p)
 =\sum_{k\geq1}k\log p
   \{T_{n,\varepsilon}(k\log p)
      -T_{n,\varepsilon}((k+1)\log p)\},
 \quad}
\tag{3}
\]

and, after summing the multiplicative annuli in (3) over all primes,

\[
 \boxed{\quad
 \sum_p\log p\sum_{k\geq1}T_{n,\varepsilon}(k\log p)
 =\int_1^\infty \psi(x)x^{-2-\varepsilon}
       K_{n,\varepsilon}(\log x)\,dx .
 \quad}
\tag{4}
\]

Here the identity in the annular interior is

\[
 \sum_{p\leq x}\left\lfloor{\log x\over\log p}\right\rfloor\log p
 =\psi(x)
 =\log\mathrm{lcm}(1,2,\ldots,\lfloor x\rfloor).
\tag{5}
\]

Consequently the whole prime--pole collision, not merely one tower, is
the single normalized analytic germ

\[
 \boxed{\quad
 \sum_{n\geq0}C_{n,\varepsilon}z^n
 ={1\over1-z}\,
 R\!\left(\varepsilon+{z\over1-z}\right),
 \qquad
 R(t)=-{\zeta'\over\zeta}(1+t)-{1\over t}
     =-{d\over dt}\log\{t\zeta(1+t)\}.
 \quad}
\tag{6}
\]

Formula (6) proves the Abel passage coefficientwise without separating the
divergent prime and pole pieces.  In particular,

\[
 \boxed{\quad
 \lim_{\varepsilon\downarrow0}C_{n,\varepsilon}
 =\sum_{j=0}^n {n\choose j}{R^{(j)}(0)\over j!}.
 \quad}
\tag{7}
\]

Thus the remaining first-difference A1 inequality is exactly

\[
 \sum_{j=0}^n {n\choose j}{R^{(j)}(0)\over j!}
 \leq {1\over2}\Delta A_n .
\tag{8}
\]

Equations (3)--(7) are a constructive compression: no individual tower,
prime cutoff, or pole term survives.  They do not by themselves prove the
one-sided estimate (8).

## 1. Closed form of the completed tail

Use the standard Laguerre generating functions, with
\(s=(1-z)^{-1}\) and \(t=z/(1-z)=s-1\):

\[
 \sum_{n\geq0}L_n^{(1)}(u)z^n
 ={1\over(1-z)^2}e^{-tu},
 \qquad
 \sum_{n\geq0}L_{n-1}^{(1)}(u)z^n
 ={z\over(1-z)^2}e^{-tu}.
\tag{9}
\]

The numerator in (1) therefore sums to

\[
 \sum_{n\geq0}K_{n,\varepsilon}(u)z^n
 =(s^2+\varepsilon s)e^{-tu}.
\tag{10}
\]

Integrating (10) from \(v\) to infinity gives

\[
 \sum_{n\geq0}T_{n,\varepsilon}(v)z^n
 ={s^2+\varepsilon s\over s+\varepsilon}
   e^{-(s+\varepsilon)v}
 =s e^{-(s+\varepsilon)v}.
\tag{11}
\]

On the other hand,

\[
 \sum_{n\geq0}e^{-(1+\varepsilon)v}L_n(v)z^n
 =e^{-(1+\varepsilon)v}s e^{-tv}
 =s e^{-(s+\varepsilon)v}.
\tag{12}
\]

Equality of coefficients proves (2).  This also proves directly that every
fixed-regulator tower in (3) is absolutely convergent.

## 2. Discrete telescoping inside one tower

Write \(\tau_k=T_{n,\varepsilon}(k\log p)\).  From (2), for fixed
\(n,\varepsilon\),

\[
 \tau_k=O_{n,p}(k^n p^{-k(1+\varepsilon)}),
 \qquad k\tau_{k+1}\longrightarrow0.
\tag{13}
\]

For a finite cutoff \(K\), ordinary summation by parts gives

\[
 \sum_{k=1}^K\tau_k
 =\sum_{k=1}^K k(\tau_k-\tau_{k+1})+K\tau_{K+1}.
\tag{14}
\]

Letting \(K\to\infty\) in (14), using (13), and multiplying by
\(\log p\) proves (3).  Differentiation of (1) also gives

\[
 T_{n,\varepsilon}(\log a)-T_{n,\varepsilon}(\log b)
 =\int_a^b x^{-2-\varepsilon}
       K_{n,\varepsilon}(\log x)\,dx .
\tag{15}
\]

Therefore the right side of (3) is

\[
 \sum_{k\geq1}k\log p
 \int_{p^k}^{p^{k+1}}x^{-2-\varepsilon}
       K_{n,\varepsilon}(\log x)\,dx .
\tag{16}
\]

For a fixed \(x\geq1\), the coefficient contributed by the \(p\)-tower
in (16) is

\[
 \log p\left\lfloor{\log x\over\log p}\right\rfloor
\quad(p\leq x),
\tag{17}
\]

and is zero for \(p>x\).  Summation over primes gives the first equality
in (5), since \(\lfloor\log x/\log p\rfloor\) is precisely the number of
powers \(p^j\leq x\).  The prime factorization of the least common multiple
gives the second equality in (5).

All interchanges at fixed \(\varepsilon>0\) are absolute.  Indeed the
elementary estimate

\[
 0\leq\psi(x)\leq\lfloor x\rfloor\log x
\tag{18}
\]

and the fact that \(K_{n,\varepsilon}\) is a fixed polynomial show that
the absolute majorant in (4) is
\(O_{n,\varepsilon}(x^{-1-\varepsilon}\log^{n+1}x)\), which is
integrable at infinity.  This proves (4), including convergence.

## 3. The pole annulus and the collective Euler divergence

Let \(d\alpha=\sum_{q=p^k}\Lambda(q)\delta_{\log q}\), and let
\(d\beta=e^u\,du\).  The canonical cost is

\[
 C_{n,\varepsilon}
 =\langle T_{n,\varepsilon},\alpha-\beta\rangle.
\tag{19}
\]

Using (15), the continuous part telescopes in the same annular form:

\[
 \int_1^\infty T_{n,\varepsilon}(\log x)\,dx
 =\int_1^\infty(x-1)x^{-2-\varepsilon}
       K_{n,\varepsilon}(\log x)\,dx.
\tag{20}
\]

The boundary term is zero because (2) is
\(O_{n,\varepsilon}(x^{-1-\varepsilon}\log^n x)\).  Subtracting
(20) from (4) recovers, now by tower telescoping,

\[
 C_{n,\varepsilon}
 =\int_1^\infty
 \{\log\mathrm{lcm}(1,\ldots,\lfloor x\rfloor)-x+1\}
 x^{-2-\varepsilon}K_{n,\varepsilon}(\log x)\,dx.
\tag{21}
\]

This is the exact arithmetic specialization of the sawtooth formula in
`103_61` and `103_64`.

To sum (19) in \(n\), use (11).  Absolute convergence for \(|z|\) small
and \(\varepsilon>0\) gives

\[
 \begin{split}
 \sum_{n\geq0}C_{n,\varepsilon}z^n
 &=s\left\{\sum_{m\geq2}{\Lambda(m)\over
             m^{s+\varepsilon}}
          -\int_1^\infty x^{-s-\varepsilon}\,dx\right\}\\
 &=s\left\{-{\zeta'\over\zeta}(s+\varepsilon)
          -{1\over s+\varepsilon-1}\right\}\\
 &=sR(\varepsilon+t),
 \end{split}
\tag{22}
\]

which is (6).  On the Euler-product side, each tower is already an exact
derivative:

\[
 {\log p\over p^{1+t}-1}
 ={d\over dt}\log(1-p^{-1-t}),
\tag{23}
\]

so summing (23) before removing the pole gives

\[
 R(t)=-{d\over dt}\log\{t\zeta(1+t)\}.
\tag{24}
\]

Equation (24), rather than either divergent summand at \(t=0\), is the
exact collective Euler divergence.

## 4. Abel limit and coefficient formula

The function

\[
 Z(t)=t\zeta(1+t)
\tag{25}
\]

is analytic at \(t=0\) and satisfies \(Z(0)=1\).  Hence there is a disk
\(|t|<r\) on which \(Z\) has no zero and \(R=-Z'/Z\) is analytic.  Choose
\(|z|<r_0\) so small that

\[
 \left|\varepsilon+{z\over1-z}\right|<r
\tag{26}
\]

for every sufficiently small \(\varepsilon\geq0\).  Then (6) converges
uniformly on every smaller \(z\)-disk as \(\varepsilon\downarrow0\).
Cauchy's coefficient formula permits the Abel limit coefficient by
coefficient; no prime or pole limit is taken separately.

Finally expand

\[
 R(\varepsilon+t)
 =\sum_{j\geq0}{R^{(j)}(\varepsilon)\over j!}t^j,
 \qquad
 {1\over1-z}t^j={z^j\over(1-z)^{j+1}}.
\tag{27}
\]

Since

\[
 [z^n]{z^j\over(1-z)^{j+1}}={n\choose j},
\tag{28}
\]

equations (27)--(28) prove

\[
 C_{n,\varepsilon}
 =\sum_{j=0}^n{n\choose j}{R^{(j)}(\varepsilon)\over j!},
\tag{29}
\]

and continuity at \(\varepsilon=0\) proves (7).  Combining (7) with the
exact first-difference identity

\[
 \Delta D_n=\Delta A_n-2\lim_{\varepsilon\downarrow0}
 C_{n,\varepsilon}
\tag{30}
\]

proves the equivalence (8).

## Status

The double prime-power sum, the continuous pole, and the Abel regulator
have now been compressed into one analytic object in (6).  The discrete
telescoping (3) proves that the relevant collective arithmetic weight is
not an arbitrary prime-power measure: it is exactly the logarithm of the
least common multiple in (5) and (21).  The only remaining mathematical
step in this formulation is the one-sided binomial-derivative estimate
(8).  No proof of that estimate, A1, or RH is asserted here.
