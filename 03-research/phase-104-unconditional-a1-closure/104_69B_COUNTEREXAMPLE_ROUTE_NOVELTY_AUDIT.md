# 104_69B — Background audit of the counterexample-route Fermi path

## Executive verdict

The directed primary search did not locate a source containing the exact
form

\[
 a_n={1\over1+(n+1)e^{\lambda_n}},\qquad
 I_L=\{L^2,\ldots,L^2+L-1\},                              \tag{1}
\]

\[
 \sum_{n\in I_L}a_n\longrightarrow0,
 \qquad
 \prod_{n\in I_L}(1-a_n)\longrightarrow1,                \tag{2}
\]

nor the prime–Laguerre diagonal

\[
 \varepsilon_X=e^{-X/100},\qquad
 \varepsilon_L=e^{-(L^2+L-1)/100}=e^{-(1+o(1))L^2/100}.  \tag{3}
\]

This **does not prove priority**. The attribution level the reviewed
sources allow is more modest:

1. the dominant exterior shell and exponential negativity infinitely
   often under non-RH are known from Bombieri–Lagarias and are written
   in explicit trigonometric form by Bucur–Ernvall-Hytönen–Odžak–Smajlović;
2. the possible genuine substantive content is the strengthening of
   `104_56` from "infinitely often" to a positive natural-density and
   syndetic set, provided that proof remains intact;
3. the Fermi logistic, the finite product, the quadratic window, and the
   Euler diagonal are exact *repackagings* or corollaries of that
   strengthening, not a new estimate on the zeros;
4. the equivalence between the logarithmic Cesàro and Abel averages
   belongs to classical summability theory. What was not located is its
   application to the Fermi detector of the Li coefficients, not the
   summability theorem.

Hence `104_68`--`104_69` must be presented as bounded criteria and finite
normalizations of the exterior-mode route. They prove neither A1 nor RH
and contribute no new information about zero localization.

---

## 1. Audited objects

Besides (1)--(3), the two averages used in `104_64` and `104_69` were
searched for:

\[
 \mathfrak F(X)
 ={1\over H_X}\sum_{n\le X}{a_n\over n},
 \qquad H_X=\sum_{n\le X}{1\over n},                     \tag{4}
\]

\[
 L(h)=-\log(1-e^{-h}),\qquad
 \mathfrak A(h)={1\over L(h)}
 \sum_{n\ge1}{e^{-hn}a_n\over n}.                       \tag{5}
\]

The finite expansion called "polymer" was also audited:

\[
\begin{aligned}
 P_L^{-1}
 &=\prod_{n\in I_L}(1+z_n)\\
 &=\sum_{S\subseteq I_L}
 \exp\!\left(-\sum_{n\in S}
       \{\lambda_n+\log(n+1)\}\right),
 \qquad z_n={e^{-\lambda_n}\over n+1}.                  \tag{6}
\end{aligned}
\]

Identity (6) is the elementary expansion of a finite product. Its
prime–Laguerre lift jointly preserves the pole, archimedean block,
primes, and prime powers, but creates no new interaction: the product
again factors degree by degree.

---

## 2. Background table

| object or claim | classification | background and exact distinction |
|---|---|---|
| Criterion \(\mathrm{RH}\Longleftrightarrow\lambda_n\ge0\) for all \(n\) | **known** | Li, JNT 65 (1997), 325--333, [DOI 10.1006/jnth.1997.2137](https://doi.org/10.1006/jnth.1997.2137) |
| Abstract multiset, subexponential lower condition, and exponential negative excursions i.o. | **known** | Bombieri–Lagarias, JNT 77 (1999), 274--287, [DOI 10.1006/jnth.1999.2392](https://doi.org/10.1006/jnth.1999.2392) |
| Dominant term \(-2R^n\sum_j\cos(n\phi_j)\) for \(R>1\) | **known** | Bucur–Ernvall-Hytönen–Odžak–Smajlović, eq. (3.9), [primary PDF](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/9D6498CFDB802707E1A0EDFFE5B81C34/S1461157016000115a.pdf/on-a-li-type-criterion-for-zerofree-regions-of-certain-dirichlet-series-with-real-coefficients.pdf), [DOI 10.1112/S1461157016000115](https://doi.org/10.1112/S1461157016000115) |
| \(\tau\)-Li criteria for zero-free half-planes | **known** | Freitas, JLMS 73 (2006), 399--414, [arXiv:math/0507368](https://arxiv.org/abs/math/0507368), [DOI 10.1112/S0024610706022599](https://doi.org/10.1112/S0024610706022599) |
| Finite index intervals certifying zero-free regions | **adjacent** | Palojärvi, Albanian J. Math. 14 (2020), 47--77, [arXiv:1807.01506](https://arxiv.org/abs/1807.01506), [journal PDF](https://www.albanian-j-math.com/archives/2020-04.pdf). Her explicit intervals \([N_1,N_2]\) are not the moving windows \(I_L\) nor do they form a product limit criterion |
| Asymptotic dichotomy \(n(A\log n+B)\) versus non-tempered oscillation | **known** | Voros, MPAG 9 (2006), 53--63, [arXiv:math/0506326](https://arxiv.org/abs/math/0506326), [DOI 10.1007/s11040-005-9002-8](https://doi.org/10.1007/s11040-005-9002-8) |
| Global \(\ell^2\) criterion for the Keiper–Li error | **adjacent** | Arias de Reyna, FACA 45 (2011), 7--21, [institutional PDF](https://idus.us.es/bitstream/handle/11441/47018/Asymptotics%20of%20Keiper-Li%20coefficients.pdf?sequence=1), [DOI 10.7169/facm/1317045228](https://doi.org/10.7169/facm/1317045228) |
| Logarithmic methods \(\ell\), \(L\), and moving averages | **known as summability** | Bingham–Gashi, JMAA 421 (2015), 1790--1802, [arXiv:1408.1301](https://arxiv.org/abs/1408.1301), [author PDF](https://www.ma.imperial.ac.uk/~bin06/Papers/BiG1.pdf), [DOI 10.1016/j.jmaa.2014.08.031](https://doi.org/10.1016/j.jmaa.2014.08.031) |
| Exponential negativity on a positive-density, syndetic set | **not explicitly located** | topological-dynamical strengthening of `104_56` over the known dominant term; not a new zero bound, and no priority is claimed |
| Fixed detector \(a_n=[1+(n+1)e^{\lambda_n}]^{-1}\) equivalent to RH | **not located exactly** | functional corollary of RH positivity and of the density/syndeticity strengthening under non-RH |
| Deterministic windows \([L^2,L^2+L)\) | **not located exactly** | corollary of syndeticity plus \(|I_L|/\min I_L\to0\); Palojärvi is only adjacent |
| Product \(P_L\) and polymer expansion | **not located exactly; algebraic repackaging** | \(P_L\to1\Longleftrightarrow\sum_{I_L}a_n\to0\) and (6) are elementary identities for nonnegative numbers |
| Diagonal \(\varepsilon_X=e^{-X/100}\), or \(e^{-cL^2}\) in blocks | **not located exactly; technical corollary** | follows from the uniform bound \(|\lambda_{n,\varepsilon}-\lambda_n|\ll n\varepsilon r^{-n}\); it is not an independent RH criterion |
| Li–Fermi application of the log-Cesàro/Abel averages | **not located exactly** | the summability machinery is classical; the substitution \(s_n=a_n\) and the prime–Laguerre lift are the project-specific layer |

"Not located" means exclusively "did not appear in this directed primary
search." It does not mean it does not exist in the literature at large.

---

## 3. The counterexample route that does have direct background

### 3.1 Li and Bombieri–Lagarias

The complete coefficients are

\[
 \lambda_n=\sum_\rho
 \left[1-\left(1-{1\over\rho}\right)^n\right].           \tag{7}
\]

Li proves that their nonnegativity at every degree is equivalent to RH.
Bombieri–Lagarias extends the mechanism to abstract multisets and proves
a one-sided subexponential condition equivalent to the localization.
When a transformed point of modulus greater than one exists, the proof
separates the maximal exterior-radius modes and obtains exponential
negative values infinitely often via simultaneous Diophantine
approximation.

This is the mathematical source of the non-RH direction of
`104_56`--`104_69`. The mere fact that exponential excursions exist
should not be presented as a new result.

### 3.2 Published trigonometric form

For the \(\tau\)-Li coefficients

\[
 \lambda_F(n,\tau)
 =\sum_\rho\left[1-\left({\rho\over\rho-\tau}\right)^n\right], \tag{8}
\]

Bucur et al. prove that a zero-free region is equivalent, among other
forms, to

\[
 \lambda_F(n,\tau)>-c(\delta)e^{\delta n}
 \quad\hbox{for every }\delta>0,                          \tag{9}
\]

and to a spectral-radius condition

\[
 \limsup_{n\to\infty}|\lambda_F(n+1,\tau)|^{1/n}\le1.    \tag{10}
\]

If

\[
 R=\max_\rho\left|{\rho\over\rho-\tau}\right|>1,       \tag{11}
\]

their equation (3.9) contains the dominant block

\[
 -2R^n\sum_{j=1}^k\cos(n\phi_j),                         \tag{12}
\]

plus strictly smaller radii and polynomial terms. They apply
simultaneous approximation to obtain exponential negativity infinitely
often. They do not state there positive density, syndeticity, the Fermi
detector, or the windows (1).

### 3.3 What `104_56` may add

The additional step of `104_56` considers the compact closure

\[
 H=\overline{\{n\alpha:n\in\mathbb Z\}}\subset\mathbb T^k \tag{13}
\]

and a regular-level open set

\[
 U_\eta=\left\{x\in H:\sum_{j=1}^k\cos x_j>\eta\right\}. \tag{14}
\]

Minimality gives syndetic returns; unique ergodicity and the choice of
a level with zero Haar boundary give positive natural density
\(\mu_H(U_\eta)>0\). If every detail of that argument is correct,
this is the potentially substantive jump relative to the primary
sources:

\[
 \neg\mathrm{RH}\Longrightarrow
 \lambda_n\le-cR^n
 \quad\hbox{on a syndetic set of positive density}. \tag{15}
\]

Windows (1) and the logistic are short consequences of (15), not a new
proof of the exterior mode.

---

## 4. Palojärvi: finite intervals, but not quadratic blocks

Palojärvi uses (8) and produces explicit numbers \(N_1,N_2\) such that
the nonnegativity of \(\Re\lambda_F(n,\tau)\) for
\(N_1\le n\le N_2\) excludes zeros with

\[
 \left|{\rho\over\rho-\tau}\right|\ge R.                \tag{16}
\]

She also gives explicit intervals \([n_1,n_2]\) in which a negative
coefficient forces the existence of a zero in the studied exterior
region. She is therefore direct background for **using several
consecutive indices**.

She does not duplicate (1)--(2): her endpoints depend on the parameters
of the zero-free region, the statement is finite and computational, and
no cofinal family of short deterministic intervals nor a Fermi sum or
product over them appears.

---

## 5. Bingham–Gashi: the log-Cesàro/Abel layer is classical

Bingham–Gashi define the logarithmic method \(\ell\) by

\[
 {1\over\log n}\sum_{i=0}^n{s_i\over i+1}\longrightarrow s, \tag{17}
\]

and the logarithmic Abel method \(L\) by

\[
 {1\over-\log(1-x)}
 \sum_{i=0}^\infty{s_i\over i+1}x^{i+1}\longrightarrow s
 \qquad(x\uparrow1).                                     \tag{18}
\]

They further introduce the moving logarithmic average

\[
 {1\over\log n}
 \sum_{n^{1/\lambda}<i\le n}{s_i\over i+1}
 \longrightarrow(1-\lambda^{-1})s,\qquad\lambda>1,       \tag{19}
\]

and prove its equivalence with \(\ell\), together with Abelian and
Tauberian results. Taking \(x=e^{-h}\), (18) has exactly the
normalizer of (5), up to a harmless index shift.

For \(0\le a_n\le1\), the equivalence of the **zero limit** used in
`104_64` is also obtained directly by positivity: the Cesàro–Abel
direction is Abelian, and the converse follows by taking \(h=1/X\),
since \(e^{-hn}\ge e^{-1}\) for \(n\le X\). Hence the bridge
(4)--(5) should not be claimed as new.

The specialization

\[
 s_n=a_n={1\over1+(n+1)e^{\lambda_n}}                    \tag{20}
\]

and its regulated prime–Laguerre representation were not located in the
reviewed sources. They are a specific application, not an extension of
Tauberian theory.

---

## 6. Other adjacent average criteria

Arias de Reyna uses Keiper's normalization, in which the Li coefficients
are \(m\lambda_m^{K}\), and writes

\[
 \lambda_m^{K}
 ={1\over2}\{\log m+\gamma-\log(2\pi)-1\}+y_m.           \tag{21}
\]

He proves

\[
 \mathrm{RH}\quad\Longleftrightarrow\quad(y_m)\in\ell^2. \tag{22}
\]

This shows global conditions on the whole Li sequence already exist. It
neither implies nor contains the Fermi criterion: (22) measures
quadratic error relative to an asymptotic, while (4) applies a bounded
nonlinearity that saturates the negative excursions.

---

## 7. Euler diagonal and product: correct scope

The diagonal (3) comes from the estimate already proved in
`104_66`--`104_69`

\[
 |\lambda_{n,\varepsilon}-\lambda_n|
 \le 2Mn\varepsilon r^{-n},\qquad r={199\over200}.        \tag{23}
\]

For all degrees \(n\le X\), choosing \(\varepsilon_X=e^{-X/100}\)
gives

\[
 \sup_{n\le X}|\lambda_{n,\varepsilon_X}-\lambda_n|
 \le2MXe^{-\eta X},
 \qquad \eta={1\over100}-\log{200\over199}>0.            \tag{24}
\]

In the window (1), \(X=L^2+L-1\), and the scale \(e^{-cL^2}\)
appears. This choice makes the Euler formulas of a finite number of
degrees converge simultaneously. It adds no new implication about zeros
and should not be announced as an independent criterion.

Similarly, the equivalence between sum and product uses only

\[
 {z\over1+z}\le\log(1+z)\le z\qquad(z\ge0),              \tag{25}
\]

and the union bound

\[
 1-\sum_{n\in I_L}a_n
 \le\prod_{n\in I_L}(1-a_n)\le1.                        \tag{26}
\]

The polymer terminology is useful for keeping the arithmetic channels
together in the exact formula, but it should not be confused with a new
collective estimate.

---

## 8. Search scope and editorial language

Up to the 26th, combinations of *Li/Keiper coefficients* with
*logistic*, *Fermi*, *Fermi–Dirac*, *partition function*, *polymer*,
*product criterion*, *syndetic*, *positive density*, *natural density*,
*logarithmic density*, *arbitrarily long blocks*, *moving blocks*,
*logarithmic Cesàro*, *logarithmic Abel*, and diagonal regularizations
were searched on arXiv, journals, and institutional repositories. The
primary texts cited above and their nearby references were reviewed.

The recommended wording for a paper is:

> Starting from the known dominant exterior term of
> Bombieri–Lagarias and Bucur et al., a recurrence argument on a compact
> torus strengthens, apparently in a way unrecorded in the reviewed
> sources, the negative excursions to a syndetic set of positive density.
> The Fermi, deterministic-block, finite-product, and Euler-diagonal
> criteria are exact corollaries and normalizations of that
> strengthening. The log-Cesàro/Abel equivalence is an instance of
> classical summability.

"First criterion," "new in the literature," or a priority claim based
solely on this search should not be used. An editorial claim of novelty
would require an additional professional search and consultation with
specialists.
