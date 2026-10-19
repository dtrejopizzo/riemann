# 104_111 — Exact reduction of Deep to the Blaschke factor

**Result.** The adversarial audit of 104_75 and 104_76 finds no flaw that
weakens the deep criterion. The canonical disc factorization identifies
exactly what it measures:

\[
 \boxed{\lambda_n=C_n-Z_n,\qquad C_n=O(n^2\log(n+1)),}   \tag{1}
\]

where \(Z_n\) is the coefficient of the inner factor formed by the zeros
of \(\zeta\) with real part greater than \(1/2\). For
\(S_X=e^{\sqrt X}\), the observable of 104_75 is trapped between the
events \(Z_n\ge(1+o(1))S_X\). The entire deep tail lies in the inner
factor; the archimedean and exterior factors have polynomial size.

Thus,

\[
 \boxed{\Omega_X\longrightarrow0
 \quad\Longleftrightarrow\quad B\equiv1
 \quad\Longleftrightarrow\quad \mathrm{RH}.}            \tag{2}
\]

Equality (2) does not prove that \(B\equiv1\). It proves that the
threshold \(e^{\sqrt X}\), the logarithmic density, and the diagonal
regulator neither eliminate nor dampen the RH content: they isolate
exactly the inner factor. Control of the modulus in the Euler horodisc
and the theta growth bounds control the exterior factor, but they do not
make \(B\) vanish.

This document also corrects the expository justification of the hard
lift in 104_75: an \(o(1)\) error does not automatically transport
indicators; the inclusions (22b) of that document do.

---

## 1. Disc coordinate and Li's generating function

Set

\[
 F(s)=(s-1)\zeta(s),\qquad
 s=s(z)={1\over1-z},\qquad
 E(z)=F(s(z)).                                           \tag{3}
\]

The unit disc maps to \(\Re s>1/2\), \(z=0\) corresponds to
\(s=1\), and \(E(0)=1\). The completed function satisfies

\[
 {\xi(s(z))\over\xi(1)}
 =s(z)\pi^{-s(z)/2}\Gamma(s(z)/2)E(z).                  \tag{4}
\]

With the branch normalized at zero,

\[
 \log{\xi(s(z))\over\xi(1)}
 =\sum_{n\ge1}{\lambda_n\over n}z^n.                   \tag{5}
\]

The interior zeros of \(E\) are

\[
 a_\rho={\rho-1\over\rho},\qquad \Re\rho>{1\over2},
 \qquad |a_\rho|<1.                                    \tag{6}
\]

## 2. Canonical factorization

Fix an integer \(M\) larger than a uniform polynomial growth exponent of
\(F(s)\) in \(\Re s>1/2\). Then

\[
 g(z)=(1-z)^M E(z)\in H^\infty(\mathbb D).               \tag{6a}
\]

Since \((1-z)^M\) is exterior, \(E=g/(1-z)^M\) belongs to the Smirnov
class \(N^+\). Its canonical factorization initially has the form

\[
 E(z)=B(z)S(z)O(z).                                      \tag{6b}
\]

\(E\) continues holomorphically across every arc of
\(\partial\mathbb D\) not containing \(1\). Hence the measure of the
singular inner factor \(S\), if it exists, is supported on \(\{1\}\), and

\[
 S(z)=S_c(z):=\exp\!\left\{-c{1+z\over1-z}\right\},
 \qquad c\ge0.                                          \tag{6c}
\]

Membership in \(N^+\) gives
\[
 u(\theta):=\log|E^*(e^{i\theta})|\in L^1(d\theta),
\]
and the exterior factor satisfies
\[
 \log|O(r)|=P_r*u=o((1-r)^{-1})\qquad(r\uparrow1).       \tag{6d}
\]
Indeed, \(P_r(\theta)(1-r)\to0\) for almost every \(\theta\), is
uniformly bounded by \(2\), and dominated convergence applies to
\(|u|\).

On the real radius, \(s=(1-r)^{-1}\to\infty\) and
\[
 E(r)=(s-1)\zeta(s)\sim s-1,
 \qquad \log|E(r)|=o(s).                                 \tag{6e}
\]
But \(\log|B(r)|\le0\),
\(\log|S_c(r)|=-c(1+r)/(1-r)=-2cs+O(1)\), and (6d) is
\(o(s)\). If \(c>0\), (6b) would imply
\(\limsup s^{-1}\log|E(r)|\le-2c\), contradicting (6e).
Hence \(c=0\): there is no singular inner factor. The factorization is

\[
 E(z)=B(z)O(z),                                         \tag{7}
\]

with \(B\) the Blaschke product of the zeros (6), counted with
multiplicity, and \(O\) exterior. For

\[
 b_a(z)={|a|\over a}{a-z\over1-\bar a z},
 \qquad b_a(0)=|a|,                                     \tag{8}
\]

one has, locally at zero,

\[
 \log{b_a(z)\over b_a(0)}
 =-\sum_{n\ge1}{a^{-n}-\bar a^{\,n}\over n}z^n.         \tag{9}
\]

The Blaschke condition guarantees convergence of the coefficients grouped
by conjugation: for fixed \(n\) and \(a=re^{i\theta}\),
\[
 |a^{-n}-\bar a^{\,n}|=r^{-n}-r^n\ll_n1-r.
\]
Define

\[
 Z_n=\sum_{\Re\rho>1/2}m_\rho
       \left(a_\rho^{-n}-\bar a_\rho^{\,n}\right).      \tag{10}
\]

The sum is real after grouping conjugate zeros. From (4)–(10),

\[
 \lambda_n=C_n-Z_n,                                    \tag{11}
\]

where

\[
 C_n=n[z^n]\left\{
 \log\big(s\pi^{-s/2}\Gamma(s/2)\big)
 +\log{O(z)\over O(0)}\right\}.                        \tag{12}
\]

## 3. The non-interior block is polynomial

The \(N^+\) proof in §2 already gives, on the circle,

\[
 u(\theta)=\log|E(e^{i\theta})|.                        \tag{13}
\]

For the exterior factor,

\[
 n[z^n]\log{O(z)\over O(0)}=2n\widehat u(n)=O(n).       \tag{14}
\]

The archimedean factor is analytic in the disc. On
\(|z|=1-1/n\), one has \(|s(z)|\le n\); Stirling, uniform in
\(\Re s>1/2\), gives

\[
 \left|\log\big(s\pi^{-s/2}\Gamma(s/2)\big)\right|
 =O(n\log(n+1)).                                        \tag{15}
\]

Cauchy's formula on that circle, where
\((1-1/n)^{-n}=O(1)\), proves

\[
 \boxed{C_n=O(n^2\log(n+1)).}                           \tag{16}
\]

Neither RH nor absence of zeros on the boundary was used.

## 4. Exact sandwich of the deep observable

Let

\[
 S_X=e^{\sqrt X},\qquad
 \delta_X=\sup_{n\le X}|\lambda_{n,\varepsilon_X}-\lambda_n|=o(1),
 \qquad \varepsilon_X=e^{-X/100}.                       \tag{17}
\]

Set

\[
 \eta_X={\max_{n\le X}|C_n+\log(n+1)|+\delta_X\over S_X}.
                                                                    \tag{18}
\]

By (16), \(\eta_X\to0\). The identity

\[
 \lambda_{n,\varepsilon_X}+\log(n+1)
 =C_n-Z_n+\log(n+1)
  +(\lambda_{n,\varepsilon_X}-\lambda_n)                \tag{19}
\]

gives, term by term,

\[
 \boxed{
 {1\over H_X}\sum_{n\le X}{\mathbf1_{\{Z_n\ge(1+\eta_X)S_X\}}\over n}
 \le\Omega_X\le
 {1\over H_X}\sum_{n\le X}{\mathbf1_{\{Z_n\ge(1-\eta_X)S_X\}}\over n}.}
                                                                    \tag{20}
\]

This is a reduction of the observable, not an estimate.

## 5. Why (20) exactly preserves RH

If \(B\equiv1\), then \(Z_n=0\). By (16), the deep event is empty for
every \(n\le X\) when \(X\) is large, and \(\Omega_X=0\).

Suppose \(B\not\equiv1\). Since \(|a_\rho|\to1\) as
\(|\Im\rho|\to\infty\), there exists

\[
 r=\min_\rho|a_\rho|<1,\qquad R=r^{-1}>1,              \tag{21}
\]

and only finitely many zeros attain \(r\). Choose \(q\in(r,1)\) smaller
than the modulus of any other interior zero. The meromorphic expansion of
the derivative of (5), or directly (9), gives

\[
 Z_n=R^nF(n\phi)+O(R_1^n),\qquad1<R_1<R,                \tag{22}
\]

where \(F\) is a finite sum of cosines with positive coefficients and
\(F(0)>0\). In the compact group

\[
 H=\overline{\{n\phi:n\in\mathbb Z\}},                  \tag{23}
\]

the returns to an open set \(\{F>\eta\}\),
\(0<\eta<F(0)\), form a syndetic set \(D\) of natural density
\(d>0\). On \(D\), eventually,

\[
 Z_n\ge{\eta\over2}R^n.                                 \tag{24}
\]

If \(K>1/\log R\), (24) exceeds \((1+\eta_X)S_X\) for
\(n\in D\cap[K\sqrt X,X]\). Partial summation gives

\[
 {1\over H_X}\sum_{\substack{K\sqrt X\le n\le X\\n\in D}}{1\over n}
 \longrightarrow {d\over2}>0.                           \tag{25}
\]

By (20), \(\liminf\Omega_X\ge d/2\). Thus (2) is proved.

## 6. The exact point that does not close

The inner factor is invisible to the modulus on the boundary:

\[
 |B(e^{i\theta})|=1\quad\hbox{almost everywhere}.     \tag{26}
\]

In the half-plane coordinate, the factor of an exterior zero is

\[
 b_\rho(s)={s-\rho\over s-(1-\bar\rho)},                \tag{27}
\]

and satisfies

\[
 \inf_{\Re s\ge1}|b_\rho(s)|={1-\beta\over\beta}>0,
 \qquad \rho=\beta+i\gamma.                              \tag{28}
\]

Hence the available lower bounds on the Euler product in
\(\Re s\ge1\) are compatible with a nontrivial inner factor. Forcing
\(B\equiv1\) would require controlling \(1/B\) over the whole disc or
proving that \(|B|=1\) at an interior point; either claim already
excludes its zeros.

The corresponding scalar quantity is precisely the BSY defect of
104_89:

\[
 -\log|B(0)|
 =\sum_{\Re\rho>1/2}m_\rho\log{1\over|a_\rho|}
 =\int_{\mathbb R}\log|F(1/2+it)|
   {dt\over2\pi(t^2+1/4)}.                              \tag{29}
\]

Proving that (29) equals zero, or proving the limit of (20), are two ways
of making the same inner factor vanish. Hardy identities, root-of-unity
filters, linear averages, and boundary moduli control the exterior
factor; they provide no inequality that makes \(B\) vanish.

## 7. Verdict

* **Audited:** the Deep equivalence of 104_75, the regulated diagonal,
  and the localization of 104_76 survive.
* **Corrected:** lifting a hard indicator uses event inclusions, not
  merely the phrase "\(o(1)\) against the threshold."
* **Proved:** every deep excursion lies in the Blaschke factor, with
  error \(O(n^2\log n)\), and (20) is exact.
* **Not proved:** \(B\equiv1\), the Deep limit, A1, or RH.

The short form of the remaining obstacle is

\[
 \boxed{\text{unconditionally prove that }
 (s-1)\zeta(s)\text{ is exterior in }\Re s>{1\over2}.}
\]

This is exactly RH, not a consequence already obtained from the literal
Mangoldt weights.
</content>
