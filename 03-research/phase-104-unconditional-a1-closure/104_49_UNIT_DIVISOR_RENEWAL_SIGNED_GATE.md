# 104_49 — Unit divisor renewal and moment–cumulant cancellation

**Result.** Factoring the zeta law into geometric exponents allows
refining the divisor selector of `104_43`: first a prime tower is chosen,
and then, conditioned on that tower's total exponent, one of its heights
is chosen uniformly. This uniformity uses exactly

\[
 \Lambda(p^k)=\log p.                                      \tag{1}
\]

Keeping the mean difference against the Gamma split gives a global signed
identity. For each order-\(r\) moment, the selector block equals

\[
 \kappa_r(s)-{\mathbb E_sX^r\over r},
\]

and the block transporting the total law to the pole equals

\[
 {\mathbb E_sX^r\over r}-(r-1)!(s-1)^{-r}.
\]

Hence the total moment \(\mathbb E_sX^r\) cancels **exactly**, leaving

\[
 \kappa_r(s)-(r-1)!(s-1)^{-r}.                             \tag{2}
\]

The Laguerre combination of (2) is precisely
\(\mathcal B_{n,s}\to B_n=A_n-\lambda_n\). No additional coercive term
appears. Moreover, the conditioned defect, before averaging, has both
signs for the very test \(P_{151}=L_{150}^{(1)}\), among real primes. So
both the pointwise sign and a bound obtained by separating the two moment
blocks are ruled out.

The shifted system \(\omega_c\) does not have the uniform selector:
already on a tower of exponent two, its probabilities differ from
\(1/2\). This confirms that (1) does distinguish the falsifier. But, when
averaging a test depending only on the marked divisor, uniformity leaves
no **additional defect term**: it produces \(\kappa_r(s)\), and the
resulting moment–cumulant form is generic for logarithmic derivatives
(even though its cumulants change when the weights change). Hence this
attack proves neither

\[
 B_n\le {1501\over2002}A_n,\qquad n\ge150,                 \tag{3}
\]

nor A1, nor RH.

## 1. Geometric Palm theory and the exact uniform mark

Fix \(s=1+\varepsilon>1\). Under the zeta law

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},
 \qquad N=\prod_p p^{A_p},                                 \tag{4}
\]

the exponents are independent and, with \(q_p=p^{-s}\),

\[
 \mathbb P(A_p=a)=(1-q_p)q_p^a,\qquad a\ge0.               \tag{5}
\]

Let

\[
 X=\log N=\sum_p A_p\ell_p,\qquad
 \ell_p=\log p,\qquad
 \mathfrak m(s)=\mathbb E_sX=-{\zeta'\over\zeta}(s).      \tag{6}
\]

Size-biasing by \(X\), one first chooses a coordinate \(P=p\) with

\[
 \mathbb P(P=p)={\ell_pq_p/(1-q_p)\over\mathfrak m(s)},    \tag{7}
\]

and replaces \(A_p\) with its size-biased version \(A_p^*\). If
\(G_p,G_p'\) are geometric as in (5), independent, then

\[
 \boxed{A_p^*\ \buildrel d\over=\ 1+G_p+G_p'.}            \tag{8}
\]

Indeed, both sides have generating function
\(t(1-q_p)^2/(1-q_pt)^2\). Define

\[
 K=1+G_p,\qquad A_p^*-K=G_p'.                               \tag{9}
\]

Conditioned on \(A_p^*=a\), each \(k=1,\ldots,a\) has, before
normalizing, the same mass

\[
 (1-q_p)^2q_p^{a-1}.
\]

Consequently,

\[
 \boxed{\mathbb P(K=k\mid A_p^*=a,P=p)={1\over a}.}       \tag{10}
\]

Conditioning now on the complete integer
\(N^*=\prod p^{a_p}\), the first selector has probability
\(a_p\ell_p/\log N^*\). Combining it with (10),

\[
 \boxed{
 \mathbb P(P=p,K=k\mid N^*)
 ={\ell_p\over\log N^*}\mathbf1_{1\le k\le a_p}.}       \tag{11}
\]

For \(D=P^K\), (11) is exactly
\(\Lambda(D)/\log N^*\). This construction simultaneously keeps every
prime and every power, but it refines the selector of `104_43`; it does
not produce a different marginal law.

## 2. Signed identity without centering the means

For a polynomial function \(f\), define, on
\(m=\prod p^{a_p}\), \(L=\log m\),

\[
 (\mathsf U f)(m)
 ={1\over L}\sum_{p^{a_p}\Vert m}\ell_p
          \sum_{k=1}^{a_p}f(k\ell_p),                      \tag{12}
\]

and the continuous split

\[
 (\mathsf C f)(L)={1\over L}\int_0^L f(x)\,dx.            \tag{13}
\]

Let \(X_0^*\sim\Gamma(2,\varepsilon)\). Conditioned on
\(X_0^*=L\), one of its two exponential coordinates is uniform on
\([0,L]\), so (13) is its selector. The joint identity, with no constants
or means removed, is

\[
\begin{aligned}
 \mathfrak M_\varepsilon(f)
 :={}&\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d)
      -\int_0^\infty e^{-\varepsilon x}f(x)\,dx\\
 ={}&\mathfrak m(s)\,\mathbb E_s^*
       \{\mathsf U f(N^*)-\mathsf C f(\log N^*)\}\\
 &+\mathfrak m(s)\,\mathbb E_s^*\mathsf C f(\log N^*)
      -{1\over\varepsilon}\mathbb E\mathsf C f(X_0^*).
                                                               \tag{14}
\end{aligned}
\]

Equivalently and more directly, if

\[
 \Delta_f(m)=
 \sum_{p^{a_p}\Vert m}\ell_p\sum_{k=1}^{a_p}f(k\ell_p)
 -\int_0^{\log m}f(x)\,dx,                                 \tag{15}
\]

then the two signed rows of (14) are

\[
 \boxed{
 \mathscr S_s(f)={1\over\zeta(s)}
       \sum_{m\ge1}{\Delta_f(m)\over m^s},}               \tag{16}
\]

\[
 \boxed{
 \mathscr T_s(f)=\mathbb E_s\int_0^X f(x)\,dx
       -\int_0^\infty e^{-\varepsilon x}f(x)\,dx,}         \tag{17}
\]

and \(\mathfrak M_\varepsilon=\mathscr S_s+\mathscr T_s\).
In particular, for \(f\equiv1\), (16) is zero and (17) keeps the mass
difference \(\mathfrak m(s)-1/\varepsilon\). No constant term has been
lost by centering.

## 3. Exact moment–cumulant cancellation

Let

\[
 m_r(s)=\mathbb E_sX^r,
 \qquad
 \kappa_r(s)=\left.{d^r\over dt^r}
       \log\mathbb E_se^{tX}\right|_{t=0}.                 \tag{18}
\]

Geometric independence and unit renewal give

\[
 \boxed{
 \kappa_r(s)=
 \sum_{p}\ell_p^r\sum_{k\ge1}k^{r-1}p^{-ks}
 =\sum_{d\ge2}{\Lambda(d)(\log d)^{r-1}\over d^s}.}       \tag{19}
\]

For \(f(x)=x^{r-1}\), Tonelli's theorem in (15) and
\(\mathbb P(A_p\ge k)=q_p^k\) produce

\[
 \boxed{
 \mathscr S_s(x^{r-1})=\kappa_r(s)-{m_r(s)\over r},
 \qquad
 \mathscr T_s(x^{r-1})={m_r(s)\over r}
                         -(r-1)!\varepsilon^{-r}.}         \tag{20}
\]

Hence the complete moments, which contain every interaction between
distinct primes, cancel degree by degree:

\[
 \boxed{
 \mathfrak M_\varepsilon(x^{r-1})
 =\kappa_r(s)-(r-1)!\varepsilon^{-r}.}                     \tag{21}
\]

Now let

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad
 c_{n,r}(s)=(-1)^{r-1}{n\choose r}{s^{r-1}\over(r-1)!}.
                                                                    \tag{22}
\]

Since \(P_n(sx)=\sum_{r=1}^nc_{n,r}(s)x^{r-1}\), (20)–(21) give

\[
\boxed{
 {\mathcal B_{n,s}\over s}
 =\sum_{r=1}^nc_{n,r}(s)
   \{\kappa_r(s)-(r-1)!\varepsilon^{-r}\}.}               \tag{23}
\]

If

\[
 R(q)=-{\zeta'\over\zeta}(1+q)-{1\over q},                \tag{24}
\]

then

\[
 \kappa_r(s)-(r-1)!\varepsilon^{-r}
 =(-1)^{r-1}R^{(r-1)}(\varepsilon),                        \tag{25}
\]

and (23) reduces to

\[
 \boxed{
 \mathcal B_{n,s}
 =s\sum_{j=0}^{n-1}{n\choose j+1}{s^j\over j!}
       R^{(j)}(\varepsilon).}                              \tag{26}
\]

Equation (26) is the same scalar form as `104_03` and `104_45`.
Moreover \(\mathcal B_{n,s}\to B_n\) as \(s\downarrow1\). So, using a
separate inequality on the two terms of (20) breaks an exact
cancellation; keeping it together recomposes the original target.

The same recomposition is visible simultaneously at every degree. With
\(t=s/(1-z)\), \(\tau=t-s=sz/(1-z)\), and

\[
 A_s(\tau)={1-\zeta(s+\tau)/\zeta(s)\over\tau},
 \qquad A_s(0)=\mathfrak m(s),                              \tag{27}
\]

one has

\[
 \sum_{n\ge1}\mathscr S_s(P_n(s\,\cdot))z^{n-1}
 ={\mathcal L(t)-A_s(\tau)\over(1-z)^2},                  \tag{28}
\]

\[
 \sum_{n\ge1}\mathscr T_s(P_n(s\,\cdot))z^{n-1}
 ={A_s(\tau)-1/(\varepsilon+\tau)\over(1-z)^2}.           \tag{29}
\]

The intermediate term cancels, and (28)+(29) equals
\((1-z)^{-2}R(\varepsilon+\tau)\).

## 4. The unit defect has no sign, already at degree 151

For the real A1 test, write

\[
 \Delta_{n,s}(m)=
 \sum_{p^{a_p}\Vert m}\ell_p\sum_{k=1}^{a_p}P_n(sk\ell_p)
 -{1-L_n(s\log m)\over s}.                                \tag{30}
\]

This is (15), since \((L_n)'=-L_{n-1}^{(1)}\). With \(s>1\) fixed, the
leading homogeneous term of (30), for \(n=151\), is a positive constant
times

\[
 \sum_p\ell_p^{151}\sum_{k=1}^{a_p}k^{150}
 -{(\log m)^{151}\over151}.                               \tag{31}
\]

If \(m=p\) is prime, (31) equals
\((1-1/151)(\log p)^{151}>0\). Hence

\[
 \Delta_{151,s}(p)>0                                      \tag{32}
\]

for every sufficiently large prime.

If \(m=pq\), with \(p\ne q\) primes and
\(x=\log p,y=\log q\), (31) equals

\[
 x^{151}+y^{151}-{(x+y)^{151}\over151}.                   \tag{33}
\]

At \(x=y\), (33) equals
\(x^{151}(2-2^{151}/151)<0\), and the sign persists as
\(x/y\to1\). By Bertrand's postulate, for each \(J\) there are primes

\[
 2^J<p_J<2^{J+1},\qquad
 2^{J+1}<q_J<2^{J+2}.                                     \tag{34}
\]

Then \(\log p_J/(J\log2)\to1\) and
\(\log q_J/(J\log2)\to1\). Dividing (30) by
\((J\log2)^{151}\), the lower-degree terms vanish, and (33) implies

\[
 \Delta_{151,s}(p_Jq_J)<0                                 \tag{35}
\]

for every sufficiently large \(J\). Equations (32) and (35) rule out
either pointwise inequality for the real unit selector.

## 5. The shifted falsifier loses the uniform mark

For

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c),\qquad r=p^c>1,               \tag{36}
\]

the local factor's coefficient at \(p^a\) is

\[
 b_a(r)=\sum_{j=0}^a r^{2j-a},                             \tag{37}
\]

and the logarithmic weight of \(p^k\) is
\(\ell_p(r^k+r^{-k})\). The local renewal is

\[
 a b_a(r)=\sum_{k=1}^a(r^k+r^{-k})b_{a-k}(r).              \tag{38}
\]

Hence, conditioned on the total exponent \(a\), the shifted selector is

\[
 \pi_{a,c}(k)={(r^k+r^{-k})b_{a-k}(r)\over a b_a(r)}.      \tag{39}
\]

For \(a=2\),

\[
 b_2=r^2+1+r^{-2},\qquad
 \boxed{
 \pi_{2,c}(1)={1\over2}+{1\over2b_2},\quad
 \pi_{2,c}(2)={1\over2}-{1\over2b_2}.}                  \tag{40}
\]

So (10) is an arithmetic property the falsifier does not satisfy. But
taking the expectation of \(f(p^K)\), (39) again produces its weights
\(\omega_c(p^k)\); the analogous moment–cumulant identity is then the
generic identity for its logarithmic derivative. In other words, the
uniform mark reconstructs the correct cumulants of zeta, but leaves no
separate penalty behind after averaging that could supply coercivity; the
same holds for the shifted system with its different cumulants.

A future proof would have to retain an additional correlation between
that uniform mark and the complete factorization. The two most immediate
linear correlations do not work: defect (30) changes sign by (32)–(35),
and its exact average cancels the moments by (20).

## 6. Verdict

Proved unconditionally:

1. the unit geometric Palm construction (8)–(11);
2. the global signed identity with no centering (14)–(17);
3. the exact moment–cumulant cancellation (20)–(26);
4. the real sign change of \(\Delta_{151,s}\) (32)–(35);
5. the explicit uniformity failure of falsifier (40).

Ruled out:

```text
uniform mark within each exponent
+ pointwise sign of the selector/Gamma defect
=> proportional bound;

separating the moments of the selector and the total
=> gain (the moments cancel exactly).
```

The only unrefuted successor is a global signed inequality using a
nonlinear correlation of the uniform mark across several towers at once,
false for (39), and surviving the average without reducing to (26). That
inequality was not obtained in this attack.

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 unit_divisor_renewal_signed_gate_check.py
```

The checker uses only integers and `Fraction`. It verifies the uniform
Palm construction, the Laguerre primitive, the moment–cumulant
cancellation, the two algebraic signs of the degree-151 defect, and the
shifted renewal (38)–(40).
</content>
