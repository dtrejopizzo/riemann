# 104_55 — Three-mark unitary Palm and cubic orientation gate

**Goal.** Attack, before taking the logarithm, the margin

\[
 B_n\le\kappa A_n,\qquad
 \kappa={1501\over2002},\qquad n\ge150,                  \tag{1}
\]

using three marks of the exact selector
\(\Lambda(p^k)=\log p\). All primes and powers, the polar comparator and
the exact archimedean Gamma block \(A_n\) are preserved.

The third-order Palm exists and retains tuples of distinct towers:

\[
 m_3(s)\,\mathbb E_s^{[3]}
   \{f(Z_1)g(Z_2)h(Z_3)\}
 =\mathbb E_s\{J_f(N)J_g(N)J_h(N)\}.                     \tag{2}
\]

However, none of the three canonical orientations yield (1):

1. the completed third moment contains a central asymmetry with no sign;
2. the alternating determinant of three marks has zero expectation, while
   its square is PSD for any selector;
3. a canonical cubic polarization that exactly removes the asymmetry,

   \[
   \mathbb E[(Z^{(1)}-Z^{(2)})^2(Z^{(3)}-c)]
   =2\mathrm{Var}(D_f)\{M_s(f)-c\},                 \tag{3}
   \]

   recovers the correct orientation, but its sign is **equivalent** to the
   sign of the margin being sought.

The uniformity within a tower does produce an identity that the shifted
system loses: all odd powers of
\(K-(a+1)/2\) average to zero for \(K\) uniform on
\(\{1,\ldots,a\}\). But after mixing towers, even the third central moment
of the real unitary selector has both signs: it is negative
for \(N=6\) and positive for \(N=18\). The third Laguerre difference also
has both signs at every degree \(n\ge5\).

The falsifier \(Z_c(s)=\zeta(s+c)\zeta(s-c)\) preserves (2), the algebraic
identity (3) and all determinantal positivity. Its local selector already
violates the unitary reflection rationally at \(p=5,5^c=2,a=2\), but that
distinction does not produce an oriented bound in any of the global forms
audited here.

Therefore the narrow mechanism

```text
three-mark unitary Palm
+ third moment / 3x3 determinant / third difference
+ canonical positivity
    => B_n <= (1501/2002) A_n.
```

is ruled out. A non-canonical nonlinear inequality that correlates the
local unitary reflection with the total integer and the Laguerre test is
not ruled out. This document does not prove (1), A1 or RH.

## 0. Relation to the earlier gates

`104_49` constructs a uniform mark within each prime exponent.
`104_50` lifts to two marks and shows that the completed square loses
orientation. `104_52`--`104_53` prove that additive cumulants eliminate
interactions between towers at every order. That theorem is not counted
again here: the **disconnected third-order moment before the logarithm**
is kept, its oriented polarizations are computed, and the local uniformity
is subjected to a shifted falsifier.

## 1. Exact three-mark Palm

Fix \(s=1+\varepsilon>1\),

\[
 \mathbb P_s(N=m)={m^{-s}\over\zeta(s)},\qquad
 X=\log N,\qquad m_r(s)=\mathbb E_sX^r.                 \tag{4}
\]

For an admissible test, let

\[
 J_f(N)=\sum_{d\mid N}\Lambda(d)f(\log d).               \tag{5}
\]

Size-bias the law (4) by \(X^3\):

\[
 \mathbb P_s^{[3]}(N^{[3]}=m)
 ={(\log m)^3m^{-s}\over\zeta(s)m_3(s)}.                 \tag{6}
\]

Conditioned on \(N^{[3]}=m>1\), choose \(Z_1,Z_2,Z_3\)
independent with

\[
 \mathbb P(Z_i=\log d\mid m)
 ={\Lambda(d)\over\log m}\mathbf1_{d\mid m}.            \tag{7}
\]

At \(m=1\) a cemetery state is used; the factor \((\log m)^3\) kills it.
Since \(\sum_{d\mid m}\Lambda(d)=\log m\), (7) is a probability. Canceling
the three denominators in the conditional expectation yields
(2). Equivalently,

\[
 \boxed{
 \mathbb E_s[J_fJ_gJ_h]
 =\sum_{d,e,r\ge2}{\Lambda(d)\Lambda(e)\Lambda(r)
 \over\mathrm{lcm}(d,e,r)^s}
 f(\log d)g(\log e)h(\log r).}                            \tag{8}
\]

Formula (8) contains three distinct towers when \(d,e,r\) are
coprime. They only vanish once the connected cumulant is formed, as
`104_53` explains; here the logarithm has not yet been taken.

## 2. Third-order polar comparator

Let \(Y\sim\mathrm{Exp}(\varepsilon)\) and

\[
 C_f(Y)=\int_0^Y f(x)\,dx.                                \tag{9}
\]

Since \(\mathbb EY^3=6/\varepsilon^3\), size-biasing by \(Y^3\) produces

\[
 Y^{[3]}\sim\Gamma(4,\varepsilon).                        \tag{10}
\]

Conditioned on \(Y^{[3]}=y\), choose \(U_1,U_2,U_3\)
independent and uniform on \([0,y]\). Then

\[
 \boxed{
 {6\over\varepsilon^3}\mathbb E^{[3]}
 \{f(U_1)g(U_2)h(U_3)\}
 =\mathbb E\{C_f(Y)C_g(Y)C_h(Y)\}.}                      \tag{11}
\]

The factor \(6\) is mandatory. For example, for
\(f(x)=x^{a-1},g(x)=x^{b-1},h(x)=x^{c-1}\), both sides of (11) are

\[
 {(a+b+c)!\over abc\,\varepsilon^{a+b+c}}.               \tag{12}
\]

This is the probabilistic Gamma of the polar size-bias. The archimedean
Gamma factor of \(\xi\) is not replaced by (10): it remains exactly in
\(A_n=n[z^n]\log G((1-z)^{-1})\), with
\(G(s)=\tfrac12s\pi^{-s/2}\Gamma(s/2)\), inside the budget of (1).

## 3. Cubic moment of the completed defect

As in `104_50`, define

\[
 U_f(X)=\int_0^X f(x)\,dx,\qquad
 D_f=J_f-U_f(X),                                          \tag{13}
\]

\[
 T_s(f)=\mathbb E_sU_f(X)-\mathbb E U_f(Y),\qquad
 Z_f=D_f+T_s(f),                                          \tag{14}
\]

and

\[
 M_s(f)=\mathbb E_sZ_f
 =\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d)
  -\int_0^\infty e^{-\varepsilon x}f(x)\,dx.             \tag{15}
\]

Set \(\widetilde D_f=D_f-\mathbb E_sD_f\). For three tests,

\[
\boxed{
\begin{aligned}
 \mathbb E_s[Z_fZ_gZ_h]
 ={}&\mathbb E_s[\widetilde D_f\widetilde D_g\widetilde D_h]\\
 &+M_s(f)\mathrm{Cov}_s(D_g,D_h)
  +M_s(g)\mathrm{Cov}_s(D_f,D_h)\\
 &+M_s(h)\mathrm{Cov}_s(D_f,D_g)
  +M_s(f)M_s(g)M_s(h).
\end{aligned}}                                             \tag{16}
\]

For \(f=g=h\),

\[
 \mathbb E_sZ_f^3
 =\mu_{3,s}(D_f)+3M_s(f)\mathrm{Var}_s(D_f)+M_s(f)^3. \tag{17}
\]

The first term of (17) has no sign. Shifting by a constant
\(c\) only replaces \(M_s(f)\) by \(M_s(f)-c\):

\[
 \boxed{
 \mathbb E_s(Z_f-c)^3
 =\mu_{3,s}(D_f)+3\{M_s(f)-c\}\mathrm{Var}_s(D_f)
   +\{M_s(f)-c\}^3.}                                     \tag{18}
\]

Thus the raw third moment does not orient the margin while the central
asymmetry remains uncontrolled.

## 4. The oriented polarization is exactly the margin

Let \(Z_f^{(1)},Z_f^{(2)},Z_f^{(3)}\) be independent copies of \(Z_f\).
The U-statistic identity

\[
 \boxed{
 \mathcal O_{s,c}(f):=
 \mathbb E_s[(Z_f^{(1)}-Z_f^{(2)})^2(Z_f^{(3)}-c)]
 =2\mathrm{Var}_s(D_f)\{M_s(f)-c\}}                \tag{19}
\]

exactly removes \(\mu_3(D_f)\) and preserves the orientation. But it does
not determine it: the orientation of the left-hand side is that of the
mean being bounded.

This is not an accident of the quadratic choice. Let
\(Z^{(1)},\ldots,Z^{(k+1)}\) be independent copies and let
\(H=H(Z^{(1)},\ldots,Z^{(k)})\ge0\) be integrable, with no dependence on
the last copy. Then

\[
 \boxed{
 \mathbb E\{H(Z^{(1)},\ldots,Z^{(k)})(Z^{(k+1)}-c)\}
 =\mathbb EH\,\{\mathbb EZ-c\}.}                         \tag{19a}
\]

If \(\mathbb EH>0\), every orientation obtained this way is exactly
equivalent to the sign of the mean. The corollary does not cover weights
that also depend on the oriented copy \(Z^{(k+1)}\); a correlation of that
kind remains outside this no-go.

For the A1 test,

\[
 f_{n,s}(x)=L_{n-1}^{(1)}(sx),\qquad
 sM_s(f_{n,s})=\mathcal B_{n,s}\longrightarrow B_n.      \tag{20}
\]

Take the exact Gamma block

\[
 c_{n,s}={\kappa A_n\over s}.                             \tag{21}
\]

Then

\[
 \boxed{
 {s\over2}\mathcal O_{s,c_{n,s}}(f_{n,s})
 =\mathrm{Var}_s(D_{f_{n,s}})
   \{\mathcal B_{n,s}-\kappa A_n\}.}                     \tag{22}
\]

For \(n\ge2\), the variance in (22) is strictly positive. Indeed,
\(D_{f_{n,s}}(1)=0\). If it also vanished at every prime \(p\), the
polynomial

\[
 H(x)=x f_{n,s}(x)-\int_0^x f_{n,s}(u)\,du                \tag{23}
\]

would vanish at the infinitely many points \(\log p\), hence would be
identically zero. But \(H'(x)=xf'_{n,s}(x)\), which would force
\(f_{n,s}\) to be constant, a contradiction for \(n\ge2\). The zeta law
gives positive mass to \(1\) and to each prime, so the variance is
positive.

Therefore

\[
 \boxed{
 \mathcal O_{s,c_{n,s}}(f_{n,s})\le0
 \quad\Longleftrightarrow\quad
 \mathcal B_{n,s}\le\kappa A_n.}                        \tag{24}
\]

The oriented cubic form exists, but (24) shows that it is not an
intermediate lemma: it is the goal itself multiplied by a positive
quantity.

## 5. Three-mark determinant

Conditioned on any total integer, let \(Z_1,Z_2,Z_3\) be iid marks and
let \(g_1,g_2,g_3\) be tests. By independence of the columns,

\[
 \boxed{
 \mathbb E\det[g_i(Z_j)]_{i,j=1}^3
 =\det[\mathbb E g_i(Z_j)]_{i,j=1}^3=0,}                  \tag{25}
\]

because the three columns of the mean matrix are equal. If squared,

\[
 \mathbb E\det[g_i(Z_j)]^2\ge0,                           \tag{26}
\]

but (26) holds for any distribution of marks, including the shifted one.
The determinant without squaring loses all orientation by
exchangeability; the square loses the sign through PSD.

## 6. Local uniformity distinguishes the shifted system, but does not orient

Conditioned on having chosen the tower \(p\) with total exponent \(a\),
the zeta selector satisfies

\[
 K\mid(p,a)\sim\mathrm{Unif}\,\{1,\ldots,a\}.         \tag{27}
\]

By reflection,

\[
 \boxed{
 \mathbb E\left[\left(K-{a+1\over2}\right)^{2j+1}
       \middle|p,a\right]=0\qquad(j\ge0).}                \tag{28}
\]

This identity is specific: for the shifted selector of `104_49`, with
\(p=5,5^c=2,a=2\),

\[
 \mathbb P(K=1)={25\over42},\qquad
 \mathbb P(K=2)={17\over42},                              \tag{29}
\]

and therefore

\[
 \mathbb E(K-3/2)^3=-{1\over42},\qquad
 \mathbb E(K-\mathbb EK)^3={425\over9261}>0.             \tag{30}
\]

The first quantity in (30) is centered at the geometric midpoint
\(3/2\), as required by the reflection (28); the second is centered at
the real mean of the selector and is its third central moment. The two
are not identified.

However, when mixing real towers, the unitary selector likewise has no
global third sign. For \(N=6\), write
\(x=\log2<y=\log3\). Its two atoms have probabilities
\(x/(x+y),y/(x+y)\), and

\[
 \boxed{
 \mathbb E[(Z-\mathbb EZ)^3\mid N=6]
 =-{xy(y-x)^4\over(x+y)^3}<0.}                            \tag{31}
\]

For \(N=18=2\cdot3^2\), the atoms are \(x,y,2y\), with weights
\(x/L,y/L,y/L\), \(L=x+2y\). Setting \(r=y/x\),

\[
 \mathbb E[(Z-\mathbb EZ)^3\mid N=18]
 ={x^3r\over(1+2r)^3}
 \{-2+13r-33r^2+33r^3-9r^4\}.                            \tag{32}
\]

The integer inequalities

\[
 2^3<3^2,\qquad 3^5<2^8
\]

give \(3/2<r<8/5\). If \(r=3/2+t\), \(0<t<1/10\), the polynomial in
braces in (32) is

\[
 {145\over16}+{61\over4}t-6t^2-21t^3-9t^4>0.             \tag{33}
\]

Indeed, even omitting the positive linear term, its right-hand side is
greater than
\(145/16-6/100-21/1000-9/10000>0\). By (31)--(33), the third
conditional asymmetry has both signs within the real arithmetic.

## 7. Third difference of the Laguerre phase

For positive increments \(u,v,w\), define

\[
 \Delta_{u,v,w}^{(3)}P_n(t)
 =\Delta_u\Delta_v\Delta_wP_n(t),\qquad
 P_n=L_{n-1}^{(1)}.                                      \tag{34}
\]

Since

\[
 P_n'''(x)=-L_{n-4}^{(4)}(x),
\]

we have

\[
 \boxed{
 \Delta_{u,v,w}^{(3)}P_n(t)
 =-\int_0^u\!\int_0^v\!\int_0^w
 L_{n-4}^{(4)}(t+a+b+c)\,dc\,db\,da.}                   \tag{35}
\]

For \(n\ge5\), \(L_{n-4}^{(4)}\) has \(n-4\) simple positive zeros and
alternates sign. Taking a sufficiently small cube within successive
intervals, (35) takes both signs. This includes every \(n\ge150\).
Consequently, the third difference does not turn the reflection (28) into
a term-by-term bound for the Laguerre vector.

## 8. Shifted falsifier and scope

For

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c),\qquad0<c<1/2,               \tag{36}
\]

the coefficients are positive and the renewal

\[
 (\log n)a_c(n)=\sum_{d\mid n}\omega_c(d)a_c(n/d),\qquad
 \omega_c(d)=2\Lambda(d)\cosh(c\log d)>0                \tag{37}
\]

produces a three-mark Palm identical to (2), with its corresponding
conditioned selector. The identities (16), (19), (25) and the positivity
(26) are purely probabilistic and remain valid. But the completed
\(\xi(s+c)\xi(s-c)\) has zeros off \(\Re s=1/2\) and Li coefficients that
are exponentially negative along a subsequence (`104_48`).

The local reflection (28) does reject the shifted system via (29)--(30).
What fails is promoting that reflection to a global inequality:
(31)--(33) show that not even the third asymmetry of the real unitary
selector has a sign, and (35) shows that the Laguerre test does not
supply one either.

## 9. Verdict

The following is proved unconditionally:

1. the three-mark unitary Palm and the triple `lcm` kernel (2), (6)--(8);
2. the polar comparator \(\Gamma(4,\varepsilon)\) with the exact factor
   six (10)--(12);
3. the completed cubic decomposition (16)--(18);
4. the oriented form (19) and its exact equivalence with the margin
   (22)--(24);
5. the collapse of the alternating determinant and the genericity of its
   square (25)--(26);
6. the unitary reflection and its rational shifted failure (28)--(30);
7. the two real arithmetic signs (31)--(33);
8. the two signs of the third Laguerre difference (35).

Using these canonical cubic forms as an autonomous source of the bound
(1) is ruled out. A successor would have to correlate the local
reflection (28) with the global factorization of \(N\) in a way that
reduces neither to the third central moment nor to (19), and that retains
a sign after averaging the oscillatory Laguerre test. No such inequality
has been constructed.

## 10. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 three_mark_unit_palm_orientation_check.py
```

The checker uses only integers and `Fraction`. It verifies the
conditioned Palm, the factor six of the polar Gamma, the cubic
identities, the oriented U-statistic, the alternating determinant, the
local rational falsifier, the two signs of (31)--(33), and the third
Laguerre differences at
\(n=150,151,152\). It does not evaluate zeta, A1 or RH.
