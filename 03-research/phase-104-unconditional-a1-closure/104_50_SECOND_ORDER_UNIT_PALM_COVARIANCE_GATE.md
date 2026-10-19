# 104_50 — Second-order unit Palm and orientation gate

**Result.** The unit selector of `104_49` admits an exact quadratic
extension. If the zeta law is size-biased by \((\log N)^2\) and,
conditioned on \(N\), two independent unit marks are chosen, then

\[
 m_2(s)\,\mathbb E_s^{[2]}\{f(Z_1)g(Z_2)\}
 =\mathbb E_s\{J_f(N)J_g(N)\}.                              \tag{1}
\]

Here \(J_f\) simultaneously preserves all primes and all their powers.
Centering (1), however, makes the towers of distinct primes cancel exactly
by independence. One way to reintroduce them without abandoning this
construction is to form the selector--continuous defect

\[
 D_f(N)=J_f(N)-\int_0^{\log N}f(x)\,dx.                    \tag{2}
\]

This defect does contain correlations between distinct towers. The pole can
be reinserted without separating channels, but then the complete bilinear
identity is

\[
 \boxed{\mathbb E_s[Z_fZ_g]
 =\mathrm{Cov}_s(D_f,D_g)+M_s(f)M_s(g),}              \tag{3}
\]

where \(M_s(f)\) is exactly the prime--pole functional of `104_45`.
For the fixed Laguerre test, \(sM_s(f_{n,s})=\mathcal B_{n,s}\to B_n\).
Therefore the completed square around the required margin equals

\[
 \boxed{
 s^2\mathbb E_s\left(Z_{f_{n,s}}-{\kappa A_n\over s}\right)^2
 =s^2\mathrm{Var}_s(D_{f_{n,s}})
  +(\mathcal B_{n,s}-\kappa A_n)^2,}
 \qquad \kappa={1501\over2002}.                             \tag{4}
\]

The second-order energy exactly loses the orientation of the margin: it
does not distinguish \(\mathcal B_{n,s}-\kappa A_n\) from its opposite.
Polarizing with two different tests does not help automatically either: it
only replaces the square by the product of its two means, as shown by (3).
The natural Stein candidates, the derivative and the primitive of the
Laguerre test, produce products with other unknown coefficients
\(\mathcal B_{k,s}\), not a known sign anchor.

The gate is adversarially correct. An analogous second-order Palm
construction and every conclusion based solely on positivity of the
covariance also hold for

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c),                               \tag{5}
\]

which has positive coefficients and logarithmic weights, but whose
completion has zeros off the line of symmetry. A fully exact local example,
\(p=5\), \(5^c=2\), already exhibits the shifted selector and its positive
covariance with rational probabilities. For this reason closing A1 via
**positivity/PSD of the quadratic Palm covariance** is ruled out, even while
keeping the real test and the pole. What is not ruled out is an additional
signed inequality correlating a conditional covariance with a function of
the total integer; that would be a higher-order input, not a consequence of
(1)--(4).

This document does not prove

\[
 B_n\le {1501\over2002}A_n,\qquad n\ge150,                  \tag{6}
\]

nor A1 nor RH.

## 0. Internal non-duplication audit

`E101_089` §12 already shows that tensoring two renewals produces, in the
Hermitian slice, only \(|\zeta|^2\) and loses the interior Hardy factor.
That no-go is not claimed again, nor is any general novelty for Palm,
size-bias, or covariances. `104_43`--`104_45` build the first mark and the
crossed Stein; `104_49` refines the mark to the uniform height within each
tower and proves the linear moment--cumulant cancellation.

What is added here is narrow: the quadratic Palm law (9)--(10), the exact
diagonalization (15)--(16), the explicit multi-tower covariance of the
defect (23), the bilinear collapse with the real budget (29), the
derivative/primitive audit (30)--(34), and the shifted-divisor rational test
(39)--(43).

## 1. Second Palm law of the unit selector

Fix \(s=1+\varepsilon>1\) and

\[
 \mathbb P_s(N=n)={n^{-s}\over\zeta(s)},\qquad
 N=\prod_p p^{A_p},\qquad X=\log N.                        \tag{7}
\]

For a function of polynomial growth, set

\[
 \boxed{
 J_f(n)=\sum_{p^{a_p}\parallel n}(\log p)
              \sum_{k=1}^{a_p}f(k\log p)
       =\sum_{d\mid n}\Lambda(d)f(\log d).}                \tag{8}
\]

In particular, the unit renewal gives \(J_1(n)=\log n=X\). Let

\[
 m_j(s)=\mathbb E_sX^j,\qquad
 \mathbb P_s^{[2]}(N^{[2]}=n)
 ={(\log n)^2n^{-s}\over\zeta(s)m_2(s)}.                  \tag{9}
\]

Conditioned on \(N^{[2]}=n\), independently choose \(Z_1,Z_2\) in the
multiset

\[
 \mathcal M(n)=\{(p,k):p^{a_p}\parallel n,\ 1\le k\le a_p\}
\]

via

\[
 \boxed{
 \mathbb P(Z_i=k\log p\mid n)={\log p\over\log n}.}       \tag{10}
\]

The sum in (10) is one since \(\sum_pa_p\log p=\log n\). Moreover,

\[
 (\log n)^2\mathbb E\{f(Z_1)g(Z_2)\mid n\}=J_f(n)J_g(n).
\]

Averaging with (9) proves (1). No tower has been replaced by its first
level, nor have the other primes been separated out.

The polar comparator is equally exact. If \(Y\sim\mathrm{Exp}
(\varepsilon)\) and

\[
 C_f(Y)=\int_0^Y f(x)\,dx,                                  \tag{11}
\]

then \(\mathbb EY^2=2/\varepsilon^2\). Size-biasing by \(Y^2\) gives
\(Y^{[2]}\sim\Gamma(3,\varepsilon)\); conditioned on \(Y^{[2]}=y\),
independently choose \(U_1,U_2\) uniform on \([0,y]\). One obtains

\[
 {2\over\varepsilon^2}\mathbb E\{f(U_1)g(U_2)\}
 =\mathbb E\{C_f(Y)C_g(Y)\}.                               \tag{12}
\]

## 2. What happens when centering: diagonalization by tower

From \(\mathbb P_s(A_p\ge k)=p^{-ks}\),

\[
 \mu_s^\Lambda(f):=\mathbb E_sJ_f
 =\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d).              \tag{13}
\]

The probability that two prime powers simultaneously divide
\(N\) is

\[
 \mathbb P_s(d\mid N,\ e\mid N)=\mathrm{lcm}(d,e)^{-s}.
\]

Hence (1) has the closed form

\[
 \mathbb E_s[J_fJ_g]
 =\sum_{d,e\ge2}{\Lambda(d)\Lambda(e)\over
             \mathrm{lcm}(d,e)^s}f(\log d)g(\log e). \tag{14}
\]

Subtracting the product of means,

\[
\begin{aligned}
 \Gamma_s^\Lambda(f,g)
 :={}&\mathrm{Cov}_s(J_f,J_g)\\
 ={}&\sum_{d,e\ge2}\Lambda(d)\Lambda(e)f(\log d)g(\log e)
 \{\mathrm{lcm}(d,e)^{-s}-d^{-s}e^{-s}\}.           \tag{15}
\end{aligned}
\]

Since \(\Lambda\) is supported on prime powers, the bracket in (15)
is zero if \(d\) and \(e\) belong to distinct towers. Thus

\[
 \boxed{
 \Gamma_s^\Lambda(f,g)
 =\sum_p(\log p)^2\sum_{k,l\ge1}f(k\ell_p)g(l\ell_p)
 \{p^{-s\max(k,l)}-p^{-s(k+l)}\},}                         \tag{16}
\]

where \(\ell_p=\log p\). The form is PSD, since it is the covariance of
the additive observables \(J_f,J_g\) under the base law, but it is a direct
sum of single-tower forms. It is not claimed here that (15) is the
covariance of \(Z_1,Z_2\) under the biased law: their biased marginals are
different. In particular, the canonical centered form induced by (1)
**cannot** be the global multi-tower mechanism being sought.

The continuous side has exactly the same tail structure:

\[
 \boxed{
 \Gamma_\varepsilon^0(f,g)
 =\int_0^\infty\!\int_0^\infty f(x)g(y)
 \{e^{-\varepsilon\max(x,y)}-e^{-\varepsilon(x+y)}\}
 \,dx\,dy.}                                                \tag{17}
\]

Both (16) and (17) are PSD separately. Their difference has no fixed sign.
For example, a nonzero test supported inside
\((0,\log2)\) annihilates (16) and makes (17) strictly positive; a test
concentrated around a single prime level makes the opposite sign appear
in the difference. This observation only rules out an operator ordering;
the A1 test is treated without localization in the next section.

## 3. A covariance that does preserve distinct towers and the pole

Define

\[
 U_f(x)=\int_0^x f(t)\,dt,\qquad
 D_f(N)=J_f(N)-U_f(X),                                     \tag{18}
\]

and the deterministic transport between the total zeta law and the pole

\[
 T_s(f)=\mathbb E_sU_f(X)-\mathbb E U_f(Y).                 \tag{19}
\]

Finally set

\[
 Z_f=D_f+T_s(f),\qquad
 M_s(f)=\mu_s^\Lambda(f)-\int_0^\infty e^{-\varepsilon x}f(x)\,dx.
                                                                    \tag{20}
\]

Then

\[
 \mathbb E_sZ_f=M_s(f).                                    \tag{21}
\]

The variable \(D_f\) is precisely the conditioned unit defect of
`104_49`; unlike (16), its covariance contains the whole product integer.
Indeed, for any \(h\), the divisor Mecke identity is

\[
 \boxed{
 \mathbb E_s\{J_f(N)h(X)\}
 =\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d)
       \mathbb E_s h(X+\log d).}                            \tag{22}
\]

Using (14) and (22),

\[
\begin{aligned}
 \mathbb E_s[D_fD_g]={}&
 \sum_{d,e\ge2}{\Lambda(d)\Lambda(e)\over
    \mathrm{lcm}(d,e)^s}f(\log d)g(\log e)\\
 &-\sum_{d\ge2}{\Lambda(d)\over d^s}f(\log d)
       \mathbb E_sU_g(X+\log d)\\
 &-\sum_{e\ge2}{\Lambda(e)\over e^s}g(\log e)
       \mathbb E_sU_f(X+\log e)
 +\mathbb E_s\{U_f(X)U_g(X)\}.                            \tag{23}
\end{aligned}
\]

The last three terms of (23) retain the interactions between all towers
through the law of \(X\). This is the second-order identity that was not
present in `104_49`.

Now center (21). For **every pair** of admissible tests,

\[
\begin{aligned}
 \mathbb E_s[Z_fZ_g]
 &=\mathrm{Cov}_s(Z_f,Z_g)+\mathbb E_sZ_f\,\mathbb E_sZ_g\\
 &=\boxed{\mathrm{Cov}_s(D_f,D_g)+M_s(f)M_s(g).}      \tag{24}
\end{aligned}
\]

The second equality uses that \(T_s(f),T_s(g)\) are deterministic. This is
the general bilinear identity: no choice of polarization avoids the
product of the two means.

## 4. Fixed Laguerre test and derivative/primitive audit

Let

\[
 P_n(x)=L_{n-1}^{(1)}(x),\qquad f_{n,s}(x)=P_n(sx).          \tag{25}
\]

Then

\[
 U_{f_{n,s}}(X)={1-L_n(sX)\over s}                         \tag{26}
\]

and

\[
 \boxed{
 D_{n,s}(N)=
 \sum_{p^{a_p}\parallel N}(\log p)
       \sum_{k=1}^{a_p}P_n(sk\log p)
 -{1-L_n(s\log N)\over s}.}                               \tag{27}
\]

This is exactly the defect \(\Delta_{n,s}\) of `104_49`, without taking
signs term by term. Moreover,

\[
 \boxed{sM_s(f_{n,s})=\mathcal B_{n,s},\qquad
        \mathcal B_{n,s}\longrightarrow B_n.}             \tag{28}
\]

Substituting (28) into (24), first with \(f=g=f_{n,s}\) and then shifting
by the deterministic budget \(\kappa A_n/s\), proves (4). More generally,

\[
\begin{aligned}
 &s^2\mathbb E_s
 \left(Z_{f_{n,s}}-{\kappa A_n\over s}\right)
 \left(Z_{f_{m,s}}-{\kappa A_m\over s}\right)\\
 &\quad=s^2\mathrm{Cov}_s(D_{n,s},D_{m,s})
 +(\mathcal B_{n,s}-\kappa A_n)
  (\mathcal B_{m,s}-\kappa A_m).                           \tag{29}
\end{aligned}
\]

Hence polarization only produces products of margins. To rule out the two
most natural Stein anchors, we use the identities

\[
 f'_{n,s}(x)=-s\sum_{k=1}^{n-1}f_{k,s}(x),                  \tag{30}
\]

\[
 U_{f_{n,s}}(x)={f_{1,s}(x)-f_{n+1,s}(x)+f_{n,s}(x)\over s}.
                                                                    \tag{31}
\]

By linearity of \(M_s\),

\[
 \boxed{
 M_s(f'_{n,s})=-\sum_{k=1}^{n-1}\mathcal B_{k,s},\qquad
 M_s(U_{f_{n,s}})
 ={\mathcal B_{1,s}-\mathcal B_{n+1,s}+\mathcal B_{n,s}\over s^2}.}
                                                                    \tag{32}
\]

Thus, polarizing with the derivative introduces the product of
\(\mathcal B_{n,s}\) with a sum of earlier coefficients; polarizing
with the primitive introduces the product with an adjacent difference.
Neither is a linear term of known sign.

The only elementary anchor with known mean is \(f\equiv1\). In that case

\[
 D_1=J_1-X=0,\qquad Z_1=M_s(1)=R(\varepsilon)<0,            \tag{33}
\]

and (24) reduces to

\[
 \mathbb E_s[Z_fZ_1]=R(\varepsilon)M_s(f).                 \tag{34}
\]

Equation (34) recovers orientation only because its left side is already
the sought functional multiplied by the known scalar
\(R(\varepsilon)\): proving the required sign for it is exactly proving the
sign of \(M_s(f)\). No covariance inequality appears, since
\(Z_1\) is constant. This closes the derivative/primitive/anchor audit.

There is another natural oriented polarization: use as the second test the
total score \(X=\log N\). For a test \(f\) independent of \(s\), differentiating
the exponential family and using the continuous comparator gives

\[
 \boxed{
 \mathrm{Cov}_s(J_f,X)
 -\mathrm{Cov}_\varepsilon(C_f(Y),Y)
 =-\partial_sM_s(f).}                                      \tag{34a}
\]

Indeed, \(\partial_s\mathbb E_sJ_f=-\mathrm{Cov}_s(J_f,X)\),
while

\[
 \mathrm{Cov}_\varepsilon(C_f(Y),Y)
 =\int_0^\infty xe^{-\varepsilon x}f(x)\,dx.
\]

If the test depends on \(s\), the right side of (34a) is replaced by

\[
 M_s(\partial_sf_s)-\partial_sM_s(f_s).                    \tag{34b}
\]

For \(f_{n,s}=P_n(s\,\cdot)\), (34b) is exactly another way of writing
the flow law already proved in `104_47`,

\[
 s\,\partial_s\mathcal B_{n,s}
 =n(\mathcal B_{n+1,s}-\mathcal B_{n,s}).                  \tag{34c}
\]

Therefore the score does preserve an oriented linear quantity, but it is
the exact derivative of the first-order functional. Integrating it
recomposes \(\mathcal B_{n,s}\) and its residues; it does not supply an
additional inequality.

## 5. Shifted falsifier that passes the quadratic PSD gate

Identity (24) is even more general. Let

\[
 Z(s)=\sum_{n\ge1}{a(n)\over n^s},\qquad a(n)>0,
\]

and suppose the positive renewal

\[
 (\log n)a(n)=\sum_{d\mid n}\omega(d)a(n/d).               \tag{35}
\]

Define

\[
 J_f^Z(n)={1\over a(n)}\sum_{d\mid n}
       \omega(d)a(n/d)f(\log d).                            \tag{36}
\]

Then \(J_1^Z(n)=\log n\), and the arithmetic Palm (9)--(10) and the
bilinear algebra (18)--(24) repeat with the law
\(a(n)n^{-s}/Z(s)\). The continuous comparator is replaced by the real
poles of the system. For (37), if
\(\varepsilon_\pm=s-1\mp c\), one takes exactly

\[
 T_{s,c}(f)=\mathbb E_{s,c}U_f(X)
 -\int_0^\infty\{e^{-\varepsilon_-x}
                 +e^{-\varepsilon_+x}\}f(x)\,dx.           \tag{36a}
\]

Each of the two polar summands separately has the Gamma construction of
(11)--(12), and identity (24) remains purely algebraic. In particular,
every Palm covariance positivity is a generic consequence of (35), not of
the location of the zeros.

Now take

\[
 Z_c(s)=\zeta(s+c)\zeta(s-c),\qquad 0<c<{1\over2}.          \tag{37}
\]

Its coefficients are positive and

\[
 \omega_c(d)=2\Lambda(d)\cosh(c\log d)>0                  \tag{38}
\]

satisfies (35). Hence its second Palm, its covariance matrix, and the
bilinear identity (24) are all valid for \(s>1+c\).

The difference with the unit selector can be seen with rationals. Choose

\[
 p=5,\qquad 5^c=2,\qquad s=2.                             \tag{39}
\]

Since \(2<\sqrt5\), we have \(0<c<1/2\). For the shifted local factor,
with \(r=5^c=2\),

\[
 b_1=r+r^{-1}={5\over2},\qquad
 b_2=r^2+1+r^{-2}={21\over4}.                              \tag{40}
\]

Conditioned on the total exponent being two, (35) gives

\[
 \boxed{\pi(1)={25\over42},\qquad \pi(2)={17\over42}.}     \tag{41}
\]

In particular,

\[
 \mathrm{Var}(K\mid A=2)
 ={25\cdot17\over42^2}={425\over1764}>0,                  \tag{42}
\]

while the unit selector gives \(1/4=441/1764\). The second order
quantitatively detects that the shifted mark is not uniform, but its
automatic conclusion is still only PSD, and (42) satisfies it. In the
two-color latent representation, the local geometric parameters
are

\[
 q_-={2\over25},\qquad q_+={1\over50},                     \tag{43}
\]

and the covariance of the **colored score before conditioning on the total
exponent** is the sum of two PSD kernels of the form (16). For a general
test, the covariance of the conditioned selector \(J_f^Z\) is not equal to
that sum: by total variance it is less than or equal to it on the
diagonal, and the difference is the lost conditional variance. The
inequality can be strict: for
\(f(k\log p)=k\), conditioned on total exponent two, the latent score takes
the values \(3,2,3\) on the partitions \((0,2),(1,1),(2,0)\), all of
positive probability. The only necessary conclusion here is that both
covariances are PSD; no equality between them is used.

Finally, the completion

\[
 \Xi_c(s)=\xi(s+c)\xi(s-c)                                 \tag{44}
\]

is symmetric about \(1/2\) and has zeros
\(1/2\pm c+i\gamma\) off that line. For an outer quartet,
if \(1-1/\rho=e^{\alpha+i\theta}\), its Li response is

\[
 4-4\cosh(n\alpha)\cos(n\theta).                           \tag{45}
\]

If \(R>1\) is the maximal outer modulus and its dominant multiset has
cardinality \(M\), simultaneous Dirichlet approximation gives infinitely
many degrees with

\[
 \lambda_n[\Xi_c]\le-{M\over2}R^n.                         \tag{46}
\]

Thus an inference using only (35), second-order Palm, and PSD would also
prove a quantitatively false conclusion for (44). The special uniformity
equality can exclude (41), but once converted into mere positive
covariance it loses that sign distinction.

## 6. Verdict

The following is proved unconditionally:

1. the second-order unit Palm law (1), (9)--(10);
2. the closed-form covariance (14)--(17);
3. the exact cancellation between distinct towers when centering \(J_f\);
4. the multi-tower identity of the defect (22)--(23);
5. the completed bilinear identity (24) and its specialization to the
   Laguerre margin (4), (29);
6. the explicit collapse of the derivative and primitive polarizations (32);
7. the collapse of the polarization with the score to the known flow
   (34a)--(34c);
8. the rational shifted gate (39)--(43).

The following is ruled out:

```text
second Palm law
+ PSD/covariance of the unit selector
+ square or polarization of the completed defect
    => one-sided bound B_n <= (1501/2002) A_n.
```

A successor that is not ruled out must preserve **orientation** before
centering: for instance, a signed correlation between the conditional
variance of the uniform mark and a nonconstant function of the total
integer. It must use the exact uniformity equality, not merely its PSD
consequence, and fail for (41). Such a correlation is of higher order than
the mechanism audited here.

## 7. Reproduction

```bash
cd 03-research/phase-104-unconditional-a1-closure/tools
python3 second_order_unit_palm_covariance_check.py
```

The checker uses only integers, `Fraction`, and rational polynomials. It
verifies the conditioned Palm identity, the cancellation between distinct
towers in (15), the Laguerre identities (26), (30)--(31), the bilinear
decomposition (24), the shifted selector (40)--(42), and the exact
positivity of the local rational kernels (43). It does not evaluate zeta,
A1, or RH.
