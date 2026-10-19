# 104_13 — M5 Selberg–Riccati: exact recurrence and scale barrier

**Status.** Selberg's positive identity

\[
 b=\Lambda\log+\Lambda*\Lambda=\mu*\log ^2\geq0
\]

does induce an exact recurrence in the Laguerre degree for the regulated
correlator of `104_12`. However, it induces no one-sided inequality. When the
double pole is separated, the centered Selberg coefficient cancels a term of the
recurrence of size \(\varepsilon^{-n-1}\). The classical summatory estimate
\(O(x)\) controls both pieces only at that same scale; with
\(\varepsilon=1/n\), its dual norm is at least
\(n(n-1)^n-1\), against the budget \(O(\log n)\).

Hence, **the positivity of \(b\), its effective summatory formula, and the
Riccati identity do not produce the new unconditional bound**. A coupled-residue
estimate that actually sufficed would again explicitly contain the correlator
\(C_{n,\varepsilon}\). This document is a stop-gate on the autonomous use of
Selberg–Riccati; it does not rule out a new arithmetic theorem on the real von
Mangoldt weights, and it proves neither A1 nor RH.

## 1. Regulated notation

Fix

\[
 a=1+\varepsilon>1,\qquad t={z\over1-z},\qquad s=a+t,
\]

and set

\[
 \ell(s)=-{\zeta'(s)\over\zeta(s)}
       =\sum_{m\ge2}{\Lambda(m)\over m^s}.
\tag{1}
\]

We define

\[
 p_n=\sum_{m\ge2}{\Lambda(m)\over m^a}L_n(\log m),
 \qquad
 j_n=\int_1^\infty x^{-a}L_n(\log x)\,dx
     ={(\varepsilon-1)^n\over\varepsilon^{n+1}},
\tag{2}
\]

\[
 c_n=p_n-j_n.
\tag{3}
\]

So \(c_n=C_{n,\varepsilon}\) in the `104_11`–`104_12` normalization.
Its generating functions are

\[
 P(z)=\sum_{n\ge0}p_nz^n={1\over1-z}\ell(a+t),
 \quad
 J(z)=\sum_{n\ge0}j_nz^n={1\over(1-z)(\varepsilon+t)},
 \quad C=P-J.
\tag{4}
\]

Selberg's identity is

\[
 {\zeta''\over\zeta}(s)=-\ell'(s)+\ell(s)^2
  =\sum_{m\ge1}{b(m)\over m^s},
\qquad
 b(m)=\Lambda(m)\log m+(\Lambda*\Lambda)(m)\ge0.
\tag{5}
\]

The last equality is also \(b=\mu*\log^2\). In particular,

\[
 b(p^k)=(2k-1)(\log p)^2,
 \qquad
 b(p^rq^s)=2\log p\log q\quad(p\ne q),
\tag{6}
\]

and \(b(m)=0\) if \(m\) has at least three distinct prime divisors.

Let

\[
 \beta_n=\sum_{m\ge1}{b(m)\over m^a}L_n(\log m),
 \qquad
 {\mathcal B}(z)=\sum_{n\ge0}\beta_nz^n
 ={1\over1-z}{\zeta''\over\zeta}(a+t).
\tag{7}
\]

The double pole of (7) has generating function

\[
 Q(z)={2\over(1-z)(\varepsilon+t)^2}
     ={2(1-z)\over\{\varepsilon+(1-\varepsilon)z\}^2}
     =\sum_{n\ge0}q_nz^n.
\tag{8}
\]

We write

\[
 d_n=\beta_n-q_n,
 \qquad D(z)={\mathcal B}(z)-Q(z).
\tag{9}
\]

## 2. Exact recurrence in the degree

For two sequences \(x,y\), denote

\[
 (x*y)_n=\sum_{k=0}^nx_ky_{n-k},
 \qquad x_{-1}=0.
\]

**Theorem 1 (Selberg–Riccati recurrence).** For every
\(n\ge0\) and \(\varepsilon>0\),

\[
\boxed{
\begin{aligned}
 d_n={}&-(n+1)c_{n+1}+(2n+1)c_n-nc_{n-1}\\
 &+2\{(j*c)_n-(j*c)_{n-1}\}
   +\{(c*c)_n-(c*c)_{n-1}\}.
\end{aligned}}
\tag{10}
\]

In particular,

\[
\boxed{
\begin{aligned}
 (n+1)c_{n+1}={}&(2n+1)c_n-nc_{n-1}\\
 &+2\{(j*c)_n-(j*c)_{n-1}\}
  +\{(c*c)_n-(c*c)_{n-1}\}-d_n.
\end{aligned}}
\tag{11}
\]

**Proof.** From (4), \(\ell=(1-z)P\), while
\(ds/dz=(1-z)^{-2}\). Hence

\[
 {1\over1-z}\{-\ell'(s)+\ell(s)^2\}
 =(1-z)P-(1-z)^2P'+(1-z)P^2.
\tag{12}
\]

The same identity with \(P\) replaced by \(J\) gives exactly \(Q\),
because for \(r=s-1\)

\[
 -\left({1\over r}\right)'+{1\over r^2}={2\over r^2}.
\]

Subtracting both identities and using \(P=J+C\),

\[
 D=(1-z)C-(1-z)^2C'
       +2(1-z)JC+(1-z)C^2.
\tag{13}
\]

Extracting \([z^n]\) in (13) proves (10), and solving for \(c_{n+1}\)
proves (11). \(\square\)

The recurrence is triangular, but it is not a signed induction: the new
input \(d_n\) is a signed Laguerre coefficient of the Selberg measure.

## 3. The pole collision occurs inside the recurrence

Set

\[
 h(s)=\ell(s)-{1\over s-1}.
\tag{14}
\]

The function \(h\) is analytic at \(s=1\) and

\[
 h(1)=-\gamma.
\tag{15}
\]

The centered identity behind (13) is

\[
 {\zeta''\over\zeta}(s)-{2\over(s-1)^2}
 =-h'(s)+{2h(s)\over s-1}+h(s)^2.
\tag{16}
\]

Since

\[
 {2h(s)\over s-1}=-{2\gamma\over s-1}+\text{a function analytic at }s=1,
\]

for each fixed \(n\) one has

\[
 \boxed{d_n=-2\gamma j_n+O_n(1)
 \qquad(\varepsilon\downarrow0).}
\tag{17}
\]

On the other hand, \(c_0=h(1+\varepsilon)=-\gamma+O(\varepsilon)\), and so

\[
 2\{(j*c)_n-(j*c)_{n-1}\}
 =-2\gamma j_n+O_n(\varepsilon^{-n}).
\tag{18}
\]

The two leading quantities of (17)–(18), each of order
\(\varepsilon^{-n-1}\), cancel in (10). The lower orders also cancel
exactly because the remaining term of (10) has a finite limit. Estimating
\(d_n\) and \((j*c)_n\) separately destroys the pole–prime renormalization
that made \(c_n\) finite.

The coefficient of the double pole in (8) is explicit. If
\(r=(1-\varepsilon)/\varepsilon\),

\[
 q_n={2(-1)^n\over\varepsilon^2}
 \left\{(n+1)r^n+n r^{n-1}\right\},
\tag{19}
\]

where the second summand is interpreted as zero for \(n=0\). In
particular,

\[
 \beta_n=q_n-2\gamma j_n+O_n(1)
 =2(n+1)(-1)^n\varepsilon^{-n-2}\{1+O_n(\varepsilon)\}.
\tag{20}
\]

Thus, even for the real, positive arithmetic coefficients \(b(m)\), the
Laguerre pullback alternates sign near the critical limit.

## 4. Sign falsifier within the real arithmetic measure

The loss of sign requires no competing measure. For \(n=1\), (20)
gives

\[
 \beta_1<0
\]

when \(a>1\) is sufficiently close to \(1\). On the other hand, as
\(a\to\infty\), the term \(m=2\) dominates the absolutely convergent series
and

\[
 \beta_1
 =b(2)2^{-a}L_1(\log2)+O(3^{-a}\mathrm{poly}(a))>0,
\tag{21}
\]

because \(b(2)=(\log2)^2\) and \(L_1(\log2)=1-\log2>0\). By continuity,
\(\beta_1(a)\) changes sign on \((1,\infty)\).

Consequently, \(b(m)\ge0\) does not even supply the sign of the first
transformed coefficient along the real regulator. Any use of (11) needs
additional signed information.

## 5. Exact price of Selberg's summatory formula

Let

\[
 S_b(x)=\sum_{m\le x}b(m),
\qquad
 R_b(x)=S_b(x)-2\{x\log x-x+1\}.
\tag{22}
\]

The subtracted term is exact, since

\[
 \int_1^\infty 2\log x\,x^{-s}\,dx={2\over(s-1)^2}.
\]

Selberg's symmetry formula gives the scale

\[
 |R_b(x)|\le Kx
\tag{23}
\]

with an effective constant after enlarging it for the initial range. Stieltjes
integration by parts, with
\(f_{n,a}(x)=x^{-a}L_n(\log x)\), gives

\[
 d_n=-\int_1^\infty R_b(x)f_{n,a}'(x)\,dx.
\tag{24}
\]

Hence, using (23) by duality produces exactly the load

\[
 |d_n|\le K\,\mathcal N_n(\varepsilon),
\quad
 \mathcal N_n(\varepsilon)
 =\int_0^\infty e^{-\varepsilon u}
   |L_n'(u)-aL_n(u)|\,du.
\tag{25}
\]

This is the operator norm of functional (24) on the ball
\(|R_b(x)|\le Kx\): the sign of \(R_b\) can approximate the sign of
\(-f_{n,a}'\). It is not merely a clumsily chosen bound.

The load has the following exact lower bound. Integrating once by
parts and using (2),

\[
 \int_0^\infty e^{-\varepsilon u}
 \{L_n'(u)-aL_n(u)\}\,du
 =-1-j_n.
\tag{26}
\]

Hence

\[
 \boxed{\mathcal N_n(\varepsilon)\ge |1+j_n|.}
\tag{27}
\]

Choosing the diagonal \(\varepsilon=1/n\), \(n\ge2\),

\[
 j_n=(-1)^n n(n-1)^n,
\]

and hence

\[
 \boxed{
 \mathcal N_n(1/n)\ge n(n-1)^n-1
       =\exp\{(1+o(1))n\log n\}.}
\tag{28}
\]

The budget of the first-difference gate is
\(\frac12\Delta A_n=O(\log n)\). So the \(O(x)\) summatory formula loses a
superexponential factor in the degree. Positivity does not repair (28): Section 4
shows that the pullback of the real positive measure already has both signs, and
`103_63` further builds positive-measure models that satisfy Selberg's
summatory scale and give both signs to the quantile functional.

## 6. Non-circularity certificate

The only subtraction that removes the leading divergence of (10) is

\[
 \widetilde d_n
 :=d_n-2\{(j*c)_n-(j*c)_{n-1}\}.
\tag{29}
\]

But (29) contains the original sequence \(c\). The recurrence becomes

\[
 \widetilde d_n
 =-(n+1)c_{n+1}+(2n+1)c_n-nc_{n-1}
  +\{(c*c)_n-(c*c)_{n-1}\}.
\tag{30}
\]

Hence, postulating a signed bound for \(\widetilde d_n\) strong enough to
control \(c_{n+1}\) is not a consequence of the positivity or the summation of
\(b\): it is a new coupled theorem that already reintroduces the A1 correlator.
Identities (10) and (30) are valid and may serve as a coordinate for such a
theorem, but they supply no sign.

## 7. Decision

```text
proved:
  exact Selberg–Riccati recurrence in the Laguerre degree;
  internal cancellation of the epsilon^(-n-1) scale within that recurrence;
  sign change of the first pullback for the real measure b;
  dual load >= |1+j_n| for any use of the O(x) summation;
  load >= n(n-1)^n-1 when taking epsilon=1/n.

ruled out:
  positivity of b as a coefficient-by-coefficient sign;
  Selberg summatory formula + partial summation as an A1 bound;
  Riccati as an autonomous one-sided induction;
  separate estimation of the centered coefficient and the pole–prime collision.

not ruled out:
  a new signed theorem for the real arithmetic that directly estimates the
  coupled residue (29) without assuming the sought bound.

not proved:
  the first-difference bound, A1, or RH.
```

## Mechanical verification

`tools/m5_riccati_degree_check.py` verifies (10), (19), and the subtraction of
the double pole using `Fraction` arithmetic for a formal atomic Dirichlet series.
It uses no values of \(\zeta\), no floating point, and no zero localization.
</content>
