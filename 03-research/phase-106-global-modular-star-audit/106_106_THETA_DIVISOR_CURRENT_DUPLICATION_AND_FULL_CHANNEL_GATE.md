# 106.106 — The theta--divisor current duplication and full-channel gate

## 1. Purpose and decision

The proposed successor to the heat-localized signed source identity is to
retain the theta index \(b\), sum all prime-power divisors of that index, and
use

\[
 \sum_{n\mid b}\Lambda(n)=\log b.                 \tag{1}
\]

This note performs that calculation before any norm estimate.  It has a
precise outcome.

1.  The theta--divisor current is an exact identity.
2.  It is exactly the spatial Möbius connection
    \(Z^{-1}\delta Z\) of 106.40, not a new source identity.
3.  Repeated differentiation produces exactly the generalized von Mangoldt
    hierarchy of 106.99.  In particular, its second current is
    \(j_2=\delta\Lambda+\Lambda*\Lambda\).
4.  The divisor regrouping sees only the divisible theta tail.  It does not
    contain the fractional theta indices or the central crossing channel.
5.  The most direct positive polarization is already indefinite on the
    literal ordinary-prime tower \(\{p,p^2\}\).

Consequently the divisor current can be used as bookkeeping inside a future
signed proof, but it does not by itself prove the heat/hybrid physical
surplus.  A genuinely new step would have to couple this current to the
fractional, central, Gamma and polar channels before taking a square or an
absolute value.

No zero location is used below.

## 2. The exact divisor-current identity

Let

\[
 T_n=n^{-1/2}S_{\log n}.
\]

The translations form a commutative multiplicative representation:

\[
 T_mT_n=T_{mn}.                                    \tag{2}
\]

On the orbit of the primitive theta atom \(k_1\), define

\[
 Z=\sum_{m\geq1}T_m,
 \qquad
 M=\sum_{d\geq1}\mu(d)T_d,
 \qquad
 A=\sum_{n\geq2}\Lambda(n)T_n.                    \tag{3}
\]

All series in this section converge absolutely and locally uniformly after
application to \(k_1\), because its translated theta orbit has
double-exponential decay.  Equivalently, the following calculations may be
read first as identities in the formal Dirichlet-convolution algebra.

Let the logarithmic derivation be

\[
 \delta T_n=(\log n)T_n.
\]

### Theorem 1 — Divisor current equals the Möbius connection

One has

\[
 \boxed{AZ=\delta Z,\qquad A=M\delta Z=Z^{-1}\delta Z.} \tag{4}
\]

#### Proof

The coefficient of \(T_b\) in \(AZ\) is

\[
 \sum_{n\mid b}\Lambda(n)=\log b,
\]

which is the coefficient of \(T_b\) in \(\delta Z\).  This proves the first
identity.  Since \(MZ=ZM=I\) by Möbius inversion, multiplication by \(M\)
gives the second and third identities. \(\square\)

Thus (1) is not an additional estimate.  It is precisely the coefficient
form of the theta--Möbius identity already realized spatially in 106.40.
Indeed, with

\[
 K=Zk_1,
\]

equation (4) gives

\[
 AK=\delta Z\,k_1
    =\sum_{b\geq1}(\log b)k_b.                     \tag{5}
\]

For a multiplier \(r\), the corresponding one-sided spatial current is the
commutator

\[
 \boxed{
 [A,M_r]f(x)
 =\sum_{n\geq2}\frac{\Lambda(n)}{\sqrt n}
   \{r(x+\log n)-r(x)\}f(x+\log n).}               \tag{6}
\]

After the opposite orientation and Gamma displacement continuum are added,
(6) is the prime part of the joint star current of 106.49.  Hence the
current formulation and the divisor formulation are two coordinates of the
same already-known object.

## 3. Differentiation gives exactly the old hierarchy

Put

\[
 J_k=M\delta^kZ,
 \qquad k\geq0.
\]

### Theorem 2 — Closure under logarithmic differentiation

For every \(k\geq0\),

\[
 \boxed{
 J_k=\sum_{n\geq1}\frac{\Lambda_k(n)}{\sqrt n}
 S_{\log n},
 \qquad
 \Lambda_k=\mu*(\log)^k,}                          \tag{7}
\]

and

\[
 \boxed{J_{k+1}=\delta J_k+AJ_k.}                  \tag{8}
\]

In particular,

\[
 J_1=A,
 \qquad
 J_2=\delta A+A^2,
\]

whose arithmetic coefficient is

\[
 \boxed{j_2=\delta\Lambda+\Lambda*\Lambda.}       \tag{9}
\]

#### Proof

The coefficient statement (7) is immediate from multiplication by the
Möbius series \(M\).  Differentiating \(MZ=I\) gives

\[
 \delta M=-M(\delta Z)M=-AM,
\]

where commutativity was used.  Therefore

\[
 \delta J_k
 =(\delta M)\delta^kZ+M\delta^{k+1}Z
 =-AJ_k+J_{k+1},
\]

which is (8).  Taking \(k=1\) gives (9). \(\square\)

Consequently every finite current obtained solely by applying the
logarithmic derivation to (4) belongs to the ordered Jordan/Bell hierarchy
already audited in 106.99.  At order two it reproduces 106.40 and 106.51;
at higher order it reproduces the all-order gate of 106.99.

## 4. The exact channel missed by divisor regrouping

In the latent theta lift of 106.65, a prime-power tail with \(a_n=\log n\)
has marks

\[
 (n,j),\qquad k_{j/n}(x),\qquad x\geq a_n.          \tag{10}
\]

The factorization \(b=nm\) used in (1) is available exactly when

\[
 n\mid j.
\]

Thus the coefficient regrouping in Theorem 1 acts on the divisible tail
channel.  It has no divisor variable for either of the remaining pieces:

\[
 \begin{aligned}
 &n\nmid j &&\text{(fractional theta channel)},\\
 &0<x<\log n &&\text{(central crossing channel)}.
 \end{aligned}                                      \tag{11}
\]

These are not negligible boundary errors.  Let

\[
 r_1=K''/K.
\]

Both omitted channels have strictly positive energy on \(r_1\).  For the
fractional channel, vanishing on a positive-measure subset of a tail would
give

\[
 r_1(x)=r_1(x-\log n)
\]

on an interval and hence everywhere by analyticity.  This would make

\(r_1\) periodic, contradicting its growth at \(+\infty\).  For the central
channel, vanishing would give

\[
 r_1(x)=r_1(\log n-x)
\]

on an interval.  Together with evenness, the two reflections generate the
nonzero period \(\log n\), giving the same contradiction.  Hence

\[
 \boxed{
 \mathscr X_{\rm frac}(r_1)>0,
 \qquad
 \mathscr X_{\rm ctr}(r_1)>0.}                     \tag{12}
\]

But \(r_1\) is an exact radical multiplier, so the complete
prime--Gamma--polar defect is zero on it.  Therefore the terms in (12)
cannot be appended as independent nonnegative remainders in a sharp proof.
They must take part in a signed cancellation with the divisible current,
Gamma and the polar threshold before the final norm is formed.

## 5. Literal finite falsifier to a positive current lift

The second derivative of the divisor current has positive scalar
coefficients, but its natural polarization is not positive.  For an
ordinary prime \(p\),

\[
 \Lambda(p^a)=\log p,
 \qquad
 j_2(p^a)=(2a-1)(\log p)^2.                         \tag{13}
\]

The polarized kernel

\[
 \mathcal H(m,n)=j_2(mn)-\Lambda(m)\Lambda(n)       \tag{14}
\]

on \(\{p,p^2\}\), divided by \((\log p)^2\), is

\[
 \begin{pmatrix}2&4\\4&6\end{pmatrix}.           \tag{15}
\]

For \(v=(2,-1)^T\),

\[
 \boxed{v^*\mathcal Hv=-2(\log p)^2<0.}            \tag{16}
\]

This is a finite falsifier made from a literal ordinary prime.  It rules
out a positive Gram or conditional-expectation lift of the divisor current;
it is not a counterexample to the complete Riemann inequality.

There is also no ordinary-prime specificity in (1) by itself.  On any free
commutative Euler monoid with a multiplicative norm \(N\), defining

\[
 \Lambda_N(\mathfrak p^a)=\log N(\mathfrak p)
\]

gives

\[
 \sum_{\mathfrak d\mid\mathfrak b}
       \Lambda_N(\mathfrak d)=\log N(\mathfrak b). \tag{17}
\]

Thus an argument whose arithmetic input is only the divisor current (4)
also applies to abstract Euler systems.  It cannot distinguish the
ordinary Riemann source from the off-line abstract systems already used as
falsifiers in Phases 104 and 106.

## 6. Exact novelty boundary

The theta--divisor idea is genuinely new only if it supplies an estimate
which is not generated by (4) and which simultaneously has all of the
following properties.

1.  It contains the nondivisible indices \(n\nmid j\).
2.  It contains the central crossing interval \(0<x<\log n\).
3.  It assembles Gamma and the polar threshold before taking a norm.
4.  It vanishes on every radical multiplier \(K^{(2j)}/K\).
5.  It fails in the finite subthreshold heat/mean-periodic model of 106.99.

In the heat-localized coordinate of 106.102, that missing statement is
still exactly

\[
 \int_0^\infty \mathcal J_u[\Gamma_{t_k}]\,d\sigma(u)
 \geq-o(\operatorname {Tr}\Gamma_{t_k})            \tag{18}
\]

along one unbounded sequence \(t_k\).  Theorems 1--2 reorganize the
divisible prime part of (18), but do not determine its sign.

## 7. Status

Proved here:

* the exact identity \(AZ=\delta Z\);
* its equivalence with the spatial Möbius connection;
* the exact commutator form of the prime current;
* closure of all logarithmic derivatives into the already-known
  generalized von Mangoldt hierarchy;
* the absence of the fractional and central channels from divisor
  regrouping;
* strict load-bearing of those channels on an exact radical multiplier;
* the literal \(\{p,p^2\}\) polarization falsifier;
* the generic Euler-monoid nature of the divisor identity.

Not proved here:

\[
 \int_0^\infty \mathcal J_u[\Gamma_{t_k}]\,d\sigma(u)
 \geq-o(\operatorname {Tr}\Gamma_{t_k}).
\]

The divisor current therefore does not close the physical surplus.  The
remaining admissible class is a globally signed full-channel operator, not
another derivative or positive polarization of \(AZ=\delta Z\).
