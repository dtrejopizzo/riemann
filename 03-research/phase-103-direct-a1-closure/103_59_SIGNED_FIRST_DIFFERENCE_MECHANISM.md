# Signed first difference: exact strength audit and surviving mechanism

## Verdict

The proposed induction target is

\[
 \Delta D_n\geq0,\qquad D_n=2\lambda_n-\lambda_n^{\rm arch}.
 \tag{1}
\]

It is a valid sufficient condition for A1 after the finite certificate, but
it is **strictly stronger than RH as a structural zero condition**.  Even an
entire function all of whose zeros lie on the critical line can have a
negative first Li difference.  Thus (1) cannot be inferred merely by putting
the zeros on the line, and a decomposition into nonnegative contributions of
individual critical-line zeros is impossible.

For the actual zeta function, integration by parts against the exact
primitive of \(E(u)=\psi(e^u)-e^u\) is legitimate with the paired Abel
regulator.  The resulting kernel is computed below.  It still changes sign.
Likewise, prime-power support, positivity of the jump measure, monotonicity of
\(\psi\), and total positivity of the Laplace kernel do not force (1): an
exact mass-transport calculation gives both signs while preserving all those
generic properties.

What survives is a genuinely arithmetic, one-sided transport inequality for
the **fixed** masses \(\Lambda(p^k)=\log p\), stated in (30) below.  Proving
that inequality would prove (1), hence A1 and RH after the finite range.  No
proof of that arithmetic inequality, and therefore no proof of RH, is claimed
in this note.

## 1. Coefficient form of the target

Let

\[
 Y(s)={\xi(s)^2\over s\pi^{-s/2}\Gamma(s/2)},\qquad
 L(s)={Y'(s)\over Y(s)},\qquad s={1\over1-z}.
 \tag{2}
\]

By the definition of the strong-margin coefficients,

\[
 \log {Y((1-z)^{-1})\over Y(1)}
 =\sum_{n\geq1}{D_n\over n}z^n.
 \tag{3}
\]

Differentiating (3) and taking one forward difference gives the exact germ
identity

\[
 \boxed{\quad
 sL(s)-D_1=\sum_{n\geq1}\Delta D_n z^n.
 \quad}
 \tag{4}
\]

Indeed, the derivative of (3) is
\(s^2L(s)=\sum_{n\geq1}D_nz^{n-1}\), and multiplication by
\(1-z=1/s\) followed by subtraction of the constant term proves (4).
Consequently (1) is coefficientwise absolute monotonicity, at the germ
\(z=0\), of the very particular completed logarithmic derivative in (4).
Real-axis positivity of \(L\), or positivity of \(Y\), is not enough for
this coefficientwise assertion.

For \(s>1\), (4) may be evaluated without zeros:

\[
 sL(s)=1+{2s\over s-1}-{s\over2}\log\pi
       +{s\over2}\psi(s/2)+2s{\zeta'\over\zeta}(s).
 \tag{5}
\]

The pole and the last term in (5) must remain paired as \(s\downarrow1\).

## 2. Why first-difference monotonicity is stronger than RH

Assume RH only for the calculation in this section.  For a zero
\(\rho=\tfrac12+i\gamma\), put

\[
 w_\gamma=1-{1\over\rho}=e^{i\theta_\gamma}.
 \tag{6}
\]

Pairing \(\rho\) with its conjugate gives the absolutely convergent fixed-
\(n\) identity

\[
 \Delta\lambda_n
 =2\sum_{\gamma>0}
 \{\cos(n\theta_\gamma)-\cos((n+1)\theta_\gamma)\}.
 \tag{7}
\]

The convergence follows directly from
\(\theta_\gamma=O(1/\gamma)\): for fixed \(n\), the braced paired term is
\(O_n(\gamma^{-2})\), and the zero count has order \(T\log T\).  Hence

\[
 \Delta D_n=4\sum_{\gamma>0}
 \{\cos(n\theta_\gamma)-\cos((n+1)\theta_\gamma)\}
 -\Delta A_n.
 \tag{8}
\]

The summands in (8) do not have one sign.  This is not merely a defect of a
bound.  Consider the real entire polynomial

\[
 X(s)=\left(s-\frac12\right)^2+\frac14.
 \tag{9}
\]

It satisfies \(X(1-s)=X(s)\), and its two zeros
\(\frac12\pm\frac i2\) lie on the critical line.  They have
\(w=i,\bar w=-i\).  The associated Li pair is exactly

\[
 \lambda_n[X]=2\{1-\cos(n\pi/2)\}\geq0,
 \tag{10}
\]

but

\[
 \Delta\lambda_2[X]
 =2\{\cos\pi-\cos(3\pi/2)\}=-2<0.
 \tag{11}
\]

Taking any positive integral power of \(X\) makes the negative value in
(11) arbitrarily large while keeping every zero on the line and every Li
coefficient nonnegative.  In particular, after subtracting any fixed
archimedean sequence \(A_n\), the corresponding
\(2\lambda_n[X^M]-A_n\) has a negative first difference at \(n=2\) for
all sufficiently large integers \(M\).  Therefore:

* RH does not imply monotonicity of Li coefficients for the natural class of
  symmetric entire functions;
* no additive per-zero square identity can prove a first-difference sign;
* a proof of (1) for zeta must use the special global distribution of its
  zeros, equivalently special arithmetic information about its prime
  weights, beyond the assertion \(\Re\rho=1/2\).

This countermodel does not say that (1) is false for zeta.  It identifies
precisely why (1) is a stronger proposed route to RH rather than an equivalent
rephrasing of the location of each zero.

## 3. Exact integration by parts against the primitive of \(E\)

For \(\varepsilon>0\), set

\[
 \begin{split}
 K_{n,\varepsilon}(u)
  &=(1+\varepsilon)L_n^{(1)}(u)
       -\varepsilon L_{n-1}^{(1)}(u),\\
 F(u)&=\int_0^u E(v)\,dv.
 \end{split}
 \tag{12}
\]

The completed Abel integral of `103_56` is

\[
 \mathcal I_{n,\varepsilon}^{(1)}
 =\int_0^\infty E(u)e^{-(1+\varepsilon)u}
 K_{n,\varepsilon}(u)\,du.
 \tag{13}
\]

Since \(F(0)=0\), \(F(u)=O(e^u)\), and the other factor is a polynomial
times \(e^{-(1+\varepsilon)u}\), both boundary terms vanish.  Ordinary
integration by parts and
\((L_j^{(1)})'=-L_{j-1}^{(2)}\) give

\[
 \boxed{\quad
 \mathcal I_{n,\varepsilon}^{(1)}
 =\int_0^\infty F(u)e^{-(1+\varepsilon)u}
 H_{n,\varepsilon}(u)\,du,
 \quad}
 \tag{14}
\]

where

\[
 \begin{split}
 H_{n,\varepsilon}(u)
  ={}&(1+\varepsilon)K_{n,\varepsilon}(u)
   +(1+\varepsilon)L_{n-1}^{(2)}(u)
   -\varepsilon L_{n-2}^{(2)}(u).
 \end{split}
 \tag{15}
\]

For \(n=1\), the term with index \(-1\) is interpreted as zero.  Formula
(14) is an exact primitive formulation, with no RH input and no discarded
Abel term.

It does not create positivity.  The leading term of (15) is
\((1+\varepsilon)^2(-1)^nu^n/n!\), whereas

\[
 H_{n,\varepsilon}(0)
 =(1+\varepsilon)\{(1+\varepsilon)(n+1)-\varepsilon n\}
 +(1+\varepsilon){n(n+1)\over2}
 -\varepsilon{n(n-1)\over2}>0.
 \tag{16}
\]

Thus for every odd \(n\), \(H_{n,\varepsilon}\) is positive at zero and
negative for large \(u\).  Repeated integration by parts only raises the
Laguerre parameter and retains a polynomial with alternating lobes.  A sign
of \(F\), even if one were available globally, would therefore not prove the
required bound.

## 4. Exact prime-mass transport and a generic no-go

At fixed \(\varepsilon>0\), define the tail response

\[
 T_{n,\varepsilon}(a)
 =\int_a^\infty e^{-(1+\varepsilon)u}
 K_{n,\varepsilon}(u)\,du.
 \tag{17}
\]

Tonelli applies to the positive jump measure before its signed Laguerre
response is taken, and Stieltjes summation gives the exact paired formula

\[
 \mathcal I_{n,\varepsilon}^{(1)}
 =\sum_{q=p^k}\Lambda(q)T_{n,\varepsilon}(\log q)
  -\int_0^\infty e^{-\varepsilon u}K_{n,\varepsilon}(u)\,du.
 \tag{18}
\]

The two terms in (18) must not be separated in the Abel limit.  For fixed
positive \(\varepsilon\), however, (18) permits an exact audit of any
purported monotonicity or total-positivity argument.

Move a mass \(W>0\) from an atom at \(b\) to an earlier atom at \(a<b\).
Both the old and new cumulative jump functions are nondecreasing positive
step functions, have the same total mass, and may have their atoms on any
prescribed sufficiently rich discrete support.  The change of (18) is

\[
 \delta\mathcal I_{n,\varepsilon}^{(1)}
 =W\{T_{n,\varepsilon}(a)-T_{n,\varepsilon}(b)\}
 =W\int_a^b e^{-(1+\varepsilon)u}K_{n,\varepsilon}(u)\,du.
 \tag{19}
\]

Already for \(n=1\),

\[
 K_{1,\varepsilon}(u)
 =2+\varepsilon-(1+\varepsilon)u
 \tag{20}
\]

is positive below \((2+\varepsilon)/(1+\varepsilon)\) and negative above
it.  Choosing \([a,b]\) wholly on either side of that rationally explicit
zero gives opposite signs in (19).  Therefore positivity and monotonicity
of the prime counting step function, prime-power support, and preservation
of its total mass do not imply a sign for (13).

The same calculation also explains why total positivity of the elementary
Laplace kernel is insufficient.  Total positivity controls variation under
the transform \(e^{-su}\), but extraction of the \(n\)-th Möbius--Taylor
coefficient applies the signed response \(K_{n,\varepsilon}\).  A single
positive atom has response proportional to a Laguerre polynomial and hence
changes sign.  No closure property of the positive Laplace transform removes
that final signed functional.

## 5. Canonical transport identity for the actual von Mangoldt masses

Formula (18) admits a sharper interpretation in which the pole is not a
separate divergent object.  First, the Laguerre generating function gives,
with \(r=\varepsilon/(1+\varepsilon)\),

\[
 \int_0^\infty e^{-(1+\varepsilon)u}L_m^{(1)}(u)\,du
 =1-r^{m+1}.
 \tag{21}
\]

Since \((1+\varepsilon)r=\varepsilon\), (21) and (12) imply the exact
normalization

\[
 \boxed{T_{n,\varepsilon}(0)=1.}
 \tag{22}
\]

Let \(d\mu=d\psi(x)\) and \(d\nu=dx\) on \([1,\infty)\), and put
\(\tau_{n,\varepsilon}(x)=T_{n,\varepsilon}(\log x)\).  Integration by
parts, using (22), gives

\[
 \int_1^\infty\tau_{n,\varepsilon}(x)\,dx
 =-1+\int_0^\infty e^{-\varepsilon u}
 K_{n,\varepsilon}(u)\,du.
 \tag{23}
\]

Consequently (18) becomes

\[
 \mathcal I_{n,\varepsilon}^{(1)}
 =\int_1^\infty\tau_{n,\varepsilon}\,d(\mu-\nu)-1.
 \tag{24}
\]

This equality explains the otherwise isolated \(-1\) in the first-
difference formula: it is exactly the lower endpoint of the continuous
mass, not a remainder to be estimated.

There is now a canonical coupling of the two measures.  Define the
generalized inverse of the actual Chebyshev step function by

\[
 Q(y)=\inf\{x\geq1:\psi(x)\geq y\},\qquad y>0.
 \tag{25}
\]

The quantile of Lebesgue measure on \([1,\infty)\) is \(1+y\).  The standard
layer-cake identity for a positive atomic measure (first for compactly
supported test functions, then by dominated convergence at fixed
\(\varepsilon>0\)) yields

\[
 \int_1^\infty\tau\,d\mu=\int_0^\infty\tau(Q(y))\,dy,
 \qquad
 \int_1^\infty\tau\,d\nu=\int_0^\infty\tau(1+y)\,dy.
 \tag{26}
\]

Thus the completed prime--pole collision is exactly the Monge transport
cost

\[
 \boxed{\quad
 C_{n,\varepsilon}:=
 \int_0^\infty
 \{T_{n,\varepsilon}(\log Q(y))
   -T_{n,\varepsilon}(\log(1+y))\}\,dy.
 \quad}
 \tag{27}
\]

Indeed, (13), (24), and the first-difference identity give

\[
 \Delta P_n(\varepsilon)=-C_{n,\varepsilon},
 \qquad
 \boxed{\quad
 \Delta D_n=\Delta A_n-2\lim_{\varepsilon\downarrow0}
 C_{n,\varepsilon}.
 \quad}
 \tag{28}
\]

No pole or prime series is taken separately in the limit in (28).  Moreover,
the cost can be written without the tail response.  Since

\[
 {d\over dx}T_{n,\varepsilon}(\log x)
 =-x^{-2-\varepsilon}K_{n,\varepsilon}(\log x),
\]

the integrand of (27) is the oriented lobe integral

\[
 T_{n,\varepsilon}(\log Q(y))
 -T_{n,\varepsilon}(\log(1+y))
 =-\int_{1+y}^{Q(y)}x^{-2-\varepsilon}
 K_{n,\varepsilon}(\log x)\,dx.
 \tag{29}
\]

Equations (27)--(29) are more than a relabelling of \(E\): they give a
canonical mass-preserving pairing between the continuous pole density and
each actual von Mangoldt atom.  They also display the precise missing
theorem:

\[
 \boxed{\quad
 \limsup_{\varepsilon\downarrow0}C_{n,\varepsilon}
 \leq{1\over2}\Delta A_n\qquad(n\geq149).
 \quad}
 \tag{30}
\]

The finite certificate and (28) show that (30) would prove
\(\Delta D_n\geq0\) for every \(n\).  It fixes not only the prime-power
support but also every mass through the quantile \(Q\).  The transport
counterexample (19)--(20) proves that replacing \(Q\) by an arbitrary
nondecreasing atomic quantile makes (30) false.  Hence a proof must exploit a
new quantitative property of the **actual** von Mangoldt quantile across
the alternating oriented intervals in (29).  An envelope for \(|E|\), a
sign of its primitive, or total positivity of the underlying Laplace kernel
cannot supply it.

For reference, the right side of (30) is completely explicit:

\[
 {1\over2}\Delta A_n
 =-{\gamma+\log(4\pi)\over4}
 +{1\over2}\sum_{\ell\ \mathrm{odd}}{1-(1-1/\ell)^n\over\ell}.
 \tag{31}
\]

Thus (30) compares one canonical arithmetic transport cost with a positive
Hausdorff-type archimedean budget of order \(\frac14\log n\); it contains no
unspecified reserve constant.

The quantile integral also has an exact prime-power cell decomposition.  If
\(q\) runs increasingly over prime powers and \(\psi(q^-)\) denotes the
left limit, then

\[
 C_{n,\varepsilon}
 =\sum_{q=p^k}\int_{1+\psi(q^-)}^{1+\psi(q)}
 \{T_{n,\varepsilon}(\log q)
   -T_{n,\varepsilon}(\log x)\}\,dx.
 \tag{32}
\]

At every fixed \(\varepsilon>0\), (32) is absolutely convergent.  It assigns
the interval of continuous mass of length
\(\psi(q)-\psi(q^-)=\Lambda(q)\) to the atom \(q\), so no arbitrary lobe
pairing remains.  In addition, the pointwise zero-regulator response is
elementary:

\[
 \lim_{\varepsilon\downarrow0}T_{n,\varepsilon}(a)
 =e^{-a}L_n^{(0)}(a),
 \tag{33}
\]

because
\((e^{-a}L_n^{(0)}(a))'=-e^{-a}L_n^{(1)}(a)\) and the expression vanishes
at infinity.  Formula (33) must not be inserted termwise into the infinite
sum (32); the correct assertion is its Abel limit.  It nevertheless shows
that each cell compares the explicit values
\(q^{-1}L_n^{(0)}(\log q)\) and
\(x^{-1}L_n^{(0)}(\log x)\).  This is the narrowest cellwise form of the
remaining signed arithmetic problem.

## Status

This audit produces three rigorous conclusions.

1. First-difference positivity is stronger than critical-line location as a
   general zero principle; the exact polynomial (9) falsifies the contrary
   claim.
2. Primitive integration, prime-power partition, and Laplace total
   positivity have been carried through exactly and do not yield a generic
   sign; (14)--(20) identify the obstruction without taking absolute values.
3. The remaining sufficient theorem is the canonical von Mangoldt transport
   estimate (30).  It is noncircular but presently unproved, and its
   proof would contain the required RH-strength arithmetic input.

Thus the finite monotonicity certificate through \(n=148\) remains valid,
but it has not been extended uniformly.  No A1 or RH conclusion follows
from this note alone.
