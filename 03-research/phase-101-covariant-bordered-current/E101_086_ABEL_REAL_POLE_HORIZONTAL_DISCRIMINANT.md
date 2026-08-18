# E101.086 - Abel real-pole horizontal discriminant

## 1. Decision

There is an exact way to use the *all-pairs* zero correlation rather than
trying to manufacture the missing same-zero conjugate graph.

For a bounded ordinate interval `I`, define

```text
F_I(exp(t))
 =sum_(rho,sigma in Z_I)m_rho m_sigma
   exp[t(rho-sigma)] 4/[4-(rho-sigma)^2].          (1.1)
```

Its bilateral Laplace transform with Abel damping is the finite meromorphic
function

```text
A_I(s)
 =sum_(rho,sigma in Z_I)m_rho m_sigma
   4/[4-(rho-sigma)^2]
   2s/[s^2-(rho-sigma)^2].                        (1.2)
```

The poles of (1.2) on the real segment `0<s<1` occur exactly at nonzero
horizontal differences between zeros at one height.  Their residues are
positive.  Therefore

```text
E_I=sum_(0<a<1)a^2 Res_(s=a)A_I(s)>=0             (1.3)
```

vanishes exactly when every zero with ordinate in `I` lies on the critical
line.  Multiplicity and coincident ordinates cause no exception.

This is not a proof of RH or Omega7.  Formula (1.1) uses a spectral interval.
The source-first Gaussian current below removes that cutoff and has an exact
abscissa of convergence

```text
sigma_c=2 sup_(Xi(p)=0)|Im p|.                    (1.3a)
```

Thus RH is equivalent to finiteness of one complete Gamma--Euler Abel current
for every positive damping exponent.  The remaining estimate is a weighted
`L^2` cancellation theorem for a log-Gaussian prime error.  It has full RH
strength, but requires neither a labelled graph nor a global meromorphic
continuation of the zero-difference series.

The route is nevertheless structurally different from E101.079--E101.085:

```text
no labelled conjugate graph is inserted;
all zero pairs and quadratic multiplicity are retained deliberately;
same height is selected by real singular support, not by a bounded phase
projector;
the exponential off-line growth is recorded as a pole instead of being
forced into a uniformly bounded recurrence argument.                (1.4)
```

Thus the missing graph can be bypassed if the exact arithmetic `L^2`
abscissa can be forced down to zero.

## 2. Finite zero set and symmetries

Write a nontrivial zero as

```text
rho=beta+i gamma,
0<beta<1.                                         (2.1)
```

Let `I` be a bounded real interval whose endpoints are not zero ordinates,
and let `Z_I` be the finite set of distinct zero locations with `gamma in I`.
The integer `m_rho` is the divisor multiplicity.  The functional equation and
reality give the same-height involution

```text
rho^dagger=1-conj(rho)
           =(1-beta)+i gamma,                     (2.2)

m_(rho^dagger)=m_rho.                             (2.3)
```

The interval condition is preserved by (2.2).  Consequently, an off-line
zero always supplies two distinct points of `Z_I` at the same ordinate.

Put

```text
w_2(d)=4/(4-d^2).                                 (2.4)
```

For every zero difference, `|Re d|<1`, so the poles `d=+/-2` of `w_2` are never
encountered on a same-height pair.  In particular,

```text
d real and |d|<1  =>  w_2(d)>0.                   (2.5)
```

## 3. Exact positivity factorization

The kernel (2.4) has the bilateral Laplace representation

```text
w_2(d)=integral_R exp(-2|v|)exp(vd)dv,            (3.1)
```

valid for `|Re d|<2`.  Define the finite exponential sum

```text
Z_I(u)=sum_(rho in Z_I)m_rho
       exp[u(rho-1/2)].                            (3.2)
```

### Lemma 3.1 - Same-height reflection gives a modulus square

For real `u`,

```text
Z_I(-u)=conj(Z_I(u)).                              (3.3)
```

### Proof

Use the bijection (2.2):

```text
conj(Z_I(u))
 =sum_rho m_rho exp[u(conj(rho)-1/2)]
 =sum_rho m_rho exp[-u(rho^dagger-1/2)]
 =Z_I(-u).                                        (3.4)
```

`QED`

### Proposition 3.2 - Positive pair correlation

For every real `t`,

```text
F_I(exp(t))
 =integral_R exp(-2|v|)|Z_I(t+v)|^2dv>=0,         (3.5)

F_I(exp(-t))=F_I(exp(t)).                         (3.6)
```

### Proof

Insert (3.1) in (1.1), interchange finite sums and the integral, and group
the two zero sums:

```text
F_I(exp(t))
 =integral_R exp(-2|v|)
   Z_I(t+v)Z_I(-(t+v))dv.                         (3.7)
```

Lemma 3.1 gives (3.5).  Replacing `t` by `-t` and then `v` by `-v` proves
(3.6). `QED`

This positivity and the kernel `w_2` are antecedents of unconditional pair
correlation.  The new use below is the exact Abel real-pole extraction, not
the positivity factorization itself.

## 4. Abel transform and exact residues

For `Re s>1`, put

```text
A_I(s)=integral_R exp(-s|t|)F_I(exp(t))dt.         (4.1)
```

The finite sum grows at most like `exp(kappa_I|t|)` with `kappa_I<1`, so
(4.1) converges absolutely.  For `d=rho-sigma`,

```text
integral_R exp(-s|t|)exp(td)dt
 =1/(s-d)+1/(s+d)
 =2s/(s^2-d^2).                                   (4.2)
```

Termwise integration proves (1.2), which then gives the meromorphic
continuation of the finite transform.

### Theorem 4.1 - Real poles are exactly horizontal pairs

Let `0<a<1`.  Then

```text
Res_(s=a) A_I(s)
 =sum_(rho,sigma in Z_I;
       gamma_rho=gamma_sigma;
       |beta_rho-beta_sigma|=a)
   m_rho m_sigma w_2(beta_rho-beta_sigma)         (4.3)

 >=0.                                             (4.4)
```

It is positive if and only if such a pair exists.

### Proof

A summand in (1.2) can have a pole at the positive real point `s=a` only if

```text
rho-sigma=+a or rho-sigma=-a.                     (4.5)
```

Thus the ordinates agree and the abscissas differ by `a`.  Conversely, every
such ordered pair gives a pole.  Since

```text
Res_(s=a) 2s/[s^2-a^2]=1,                         (4.6)
```

the residue is (4.3).  Every weight in (4.3) is positive by (2.5), and no
cancellation is possible. `QED`

The pole at `s=0` records only the complete diagonal `rho=sigma` and is
intentionally omitted.  Its residue is `2sum_rho m_rho^2`; it does not
distinguish RH.

## 5. A finite exact RH discriminator

Define

```text
E_I
 =sum_(0<a<1)a^2 Res_(s=a)A_I(s)                 (5.1)

 =sum_(rho,sigma in Z_I;
       gamma_rho=gamma_sigma)
   m_rho m_sigma
   (beta_rho-beta_sigma)^2
   4/[4-(beta_rho-beta_sigma)^2].                 (5.2)
```

The two formulas agree because each nonzero ordered horizontal pair occurs
in the residue at `a=|beta_rho-beta_sigma|`.  Terms with equal abscissa are
zero in (5.2).

### Theorem 5.1 - Exact finite equivalence

For every interval `I` as above,

```text
E_I>=0,                                           (5.3)

E_I=0
 <=> every rho in Z_I has beta=1/2.               (5.4)
```

### Proof

Every term in (5.2) is nonnegative, proving (5.3).  If all zeros are on the
critical line, all horizontal differences vanish and `E_I=0`.

Conversely, suppose `rho=beta+i gamma` is off-line.  Its partner
`rho^dagger` from (2.2) is in `Z_I`, has the same ordinate, and satisfies

```text
|beta-(1-beta)|=|2beta-1| in (0,1).               (5.5)
```

The ordered pair contributes strictly positively to (5.2), so `E_I>0`.
`QED`

No simplicity hypothesis appears.  A multiple zero on the critical line
contributes zero, while an off-line location of multiplicity `m` and its
partner contribute a positive weight proportional to `m^2`.

Taking an exhaustion by bounded ordinate intervals gives

```text
RH
 <=> E_I=0 for every bounded admissible I
 <=> A_I has no pole in (0,1) for every such I.    (5.6)
```

Equation (5.6) is a localization of force, not a simplification of RH.

## 6. The height-only no-go

The horizontal pair current must retain more than the vertical counting
measure.  At one ordinate `gamma`, compare

```text
one double zero at 1/2+i gamma;

two simple zeros at (1/2-delta)+i gamma and
                    (1/2+delta)+i gamma.          (6.1)
```

Both configurations have the same projected ordinate measure
`2 delta_gamma`.  The first has `E_I=0`; the second has a positive atom at
`a=2delta`.  Therefore no universal functional on finite
reflection-symmetric divisors which factors only through ordinates, the
vertical counting function, or an ordinary same-height count can imply
(5.4).  This does not exclude a functional using additional arithmetic
restrictions specific to the Xi divisor.

What matters in (4.3) is the real part of the *complex difference*
`rho-sigma`.  This prevents the Abel route from being misread as another
vertical pair-correlation criterion.

## 7. Gaussian source-first Abel current

The spectral cutoff in `Z_I` is not source-admissible.  A legitimate
Gamma--Euler version starts with an admissible Weil test and retains every
zero pair.

Use the centered real-zero coordinate

```text
p=gamma-i(beta-1/2),                               (7.1)
```

so that RH is `p real` and the same-height involution is `p -> conj(p)`.
Fix `T in R` and `tau>0`, and set

```text
H_(T,tau)(p)=exp[-tau(p-T)^2].                    (7.2)
```

Uniformly in `|Im p|<1/2`,

```text
|H_(T,tau)(p)|
 <=exp(tau/4)exp[-tau(Re p-T)^2].                 (7.3)
```

Thus the zero trace and every pair trace below converge absolutely.  Let
`h_(T,tau)` be the Gaussian source with Fourier transform (7.2), using the
convention of E101.082, and translate it by

```text
h_(T,tau;u)(x)=h_(T,tau)(x+u),

F[h_(T,tau;u)](p)=H_(T,tau)(p)exp(iup).           (7.4)
```

Define the complete Weil trace

```text
S_(T,tau)(u)=W_Weil(h_(T,tau;u)).                 (7.5)
```

The source side of (7.5) contains the prime, prime-power, archimedean and
polar terms.  The Gaussian source makes the Euler sum absolutely convergent;
no moving prime cutoff or discarded boundary channel is needed.

On the spectral side,

```text
S_(T,tau)(u)
 =sum_p m_p H_(T,tau)(p)exp(iup),                 (7.6)

S_(T,tau)(-u)=conj(S_(T,tau)(u))                  (7.7)
```

for real `u`.  Now put

```text
F_(T,tau)(t)
 =integral_R exp(-2|v|)
   S_(T,tau)(t+v)S_(T,tau)(-(t+v))dv             (7.8)

 =integral_R exp(-2|v|)|S_(T,tau)(t+v)|^2dv
 >=0,                                             (7.9)

A_(T,tau)(s)
 =integral_R exp(-s|t|)F_(T,tau)(t)dt,
 s>0,                                             (7.10)
```

where the value `+infinity` is allowed.  The integral is finite a priori for
`s>1`.

### Proposition 7.1 - Exact all-channel pair identity

For `Re s>1`,

```text
A_(T,tau)(s)
 =sum_(p,q)m_pm_q H_(T,tau)(p)H_(T,tau)(q)
   4/[4+(p-q)^2]
   2s/[s^2+(p-q)^2].                              (7.11)
```

### Proof

Bounds (7.3) and `|Im(p-q)|<1` justify both interchanges.  The two elementary
integrals are

```text
integral_R exp(-2|v|)exp[iv(p-q)]dv
 =4/[4+(p-q)^2],                                  (7.12)

integral_R exp(-s|t|)exp[it(p-q)]dt
 =2s/[s^2+(p-q)^2].                               (7.13)
```

Substitution in (7.8)--(7.10) proves (7.11). `QED`

This construction deliberately uses a product of two traces.  Consequently
it has all pairs and weight `m_pm_q`; those are features here, not errors.
It is outside the one-trace holomorphic wall of E101.082 and outside the
positive tensor-power ansatz of E101.083.

Unlike the finite unweighted residues of Theorem 4.1, residues obtained by
continuing the Gaussian pair series termwise need not be positive.  At one
height with deviations `+/-a,+/-b`, the coefficient of the gap `b-a`
contains a factor

```text
4w_2(b-a)
 exp[-2tau(gamma-T)^2+tau(a^2+b^2)]
 cos[2tau(gamma-T)(a+b)],                          (7.14)
```

which changes sign.  Difference poles may also accumulate.  Section 8 uses
the positive integral abscissa and depends on neither residue separation nor
termwise meromorphy.

## 8. Exact Abel abscissa

The possible accumulation of zero differences can be avoided completely.
This is an independent replacement for a global residue argument, not a
completion of one: neither the finite discriminator nor `w_2` is used in the
proof below.  Only the one-trace Gaussian signal and its one-sided Laplace
poles are needed.
Define the simpler positive integral

```text
I_(T,tau)(s)
 =integral_R exp(-s|u|)|S_(T,tau)(u)|^2du,
 s>0,                                             (8.1)
```

again allowing `+infinity`.

### Lemma 8.1 - Positive convolution transfer

For every `s>0`, Tonelli's theorem gives

```text
A_(T,tau)(s)
 =integral_R |S_(T,tau)(u)|^2 K_s(u)du,           (8.2)

K_s(u)
 =integral_R exp(-s|t|)exp(-2|u-t|)dt             (8.3)

 ={4exp(-s|u|)-2s exp(-2|u|)}/{4-s^2}, s!=2,

K_2(u)=(|u|+1/2)exp(-2|u|).                       (8.4)
```

For `0<s<2`, there are positive constants `c_s,C_s` such that

```text
c_s exp(-s|u|)<=K_s(u)<=C_s exp(-s|u|).           (8.5)
```

### Proof

Insert (7.8) in (7.10), make the change `u=t+v`, and use nonnegativity to
interchange the two integrals.  Splitting the convolution at `0` and `u`
gives (8.4); the value at `s=2` is its limit.  If `0<s<2`, factor
`exp(-s|u|)` in (8.4).  The remaining bracket lies between `4-2s` and `4`,
which proves (8.5). `QED`

Let

```text
Y=sup_(Xi(p)=0)|Im p|,                            (8.6)
```

so `0<=Y<=1/2` and RH is exactly `Y=0`.

### Theorem 8.2 - Exact convergence abscissa

For every fixed `T in R` and `tau>0`,

```text
inf{s>0:I_(T,tau)(s)<infinity}
 =inf{s>0:A_(T,tau)(s)<infinity}
 =2Y.                                             (8.7)
```

### Proof: upper bound

By (7.3) and the zero count,

```text
C_(T,tau)=sum_p m_p|H_(T,tau)(p)|<infinity.       (8.8)
```

For real `u`,

```text
|S_(T,tau)(u)|<=C_(T,tau)exp(Y|u|).               (8.9)
```

Hence `I_(T,tau)(s)<infinity` whenever `s>2Y`.  Since `2Y<=1<2`, Lemma 8.1
gives the same upper bound for `A_(T,tau)`.

### Proof: lower bound

Suppose `I_(T,tau)(s)<infinity`.  On the positive half-line define

```text
L(z)=integral_0^infinity
     exp(-zu)S_(T,tau)(u)du.                      (8.10)
```

Cauchy--Schwarz shows that `L` is holomorphic on `Re z>s/2`.  On the safe
half-plane `Re z>1/2`, termwise integration in (7.6) gives

```text
L(z)=sum_p m_p H_(T,tau)(p)/(z-ip).               (8.11)
```

The Gaussian bound makes the right side a locally normally convergent
meromorphic sum.  At `z=ip` its residue is

```text
m_p H_(T,tau)(p)!=0.                              (8.12)
```

If a zero had `Im p<-s/2`, then the pole `z=ip` would satisfy
`Re(ip)=-Im p>s/2`.  Equations (8.10)--(8.11) would make the same function
both holomorphic and singular there.  Indeed, remove from `Re z>s/2` all
locally finite poles `iq`.  The remaining domain is connected, and the
identity theorem extends (8.11) there from `Re z>1/2`.  In a punctured
neighborhood of the target pole it equals (8.10), while (8.10) remains
holomorphic across the puncture.  This is a contradiction.
The symmetry
`p -> conj(p)` therefore gives

```text
|Im p|<=s/2 for every zero p.                     (8.13)
```

Thus `s>=2Y`.  Together with the upper bound this proves the first equality
in (8.7).  For `0<s<2`, (8.5) proves the second.  For `s>=2`, finiteness is
already automatic from (8.9) and (8.4), since `2Y<=1`. `QED`

### Corollary 8.3 - One Gaussian family is an exact RH criterion

For any one fixed pair `T in R`, `tau>0`, the following are equivalent:

```text
RH;

I_(T,tau)(s)<infinity for every s>0;

A_(T,tau)(s)<infinity for every s>0;

the same finiteness along one sequence s_j decreasing to zero.      (8.14)
```

No ordinate localization, residue separation or global continuation is
needed.  The nonvanishing Gaussian weight in (8.12) prevents any zero from
being hidden by cancellation.

## 9. Exact source-side target

By (7.5), every value of `S_(T,tau)(u)` is the complete explicit formula for
one translated Gaussian.  With the Fourier convention of E101.082, its
source is

```text
h_(T,tau;u)(x)
 ={1/[2sqrt(pi tau)]}
  exp[-(x+u)^2/(4tau)]exp[iT(x+u)].               (9.1)
```

The complete centered Weil formula is therefore

```text
S_(T,tau)(u)
 =H_(T,tau)(i/2)exp(-u/2)
  +H_(T,tau)(-i/2)exp(u/2)

  +1/(2pi) integral_R H_(T,tau)(r)exp(iur)
    [Re psi(1/4+ir/2)-log pi]dr

  -sum_(n>=2)Lambda(n)/sqrt(n)
   [h_(T,tau;u)(log n)+h_(T,tau;u)(-log n)].      (9.2)
```

Both Euler tails, both polar evaluations and the complete Gamma integral are
retained.  Every series and integral in (9.2) converges absolutely for fixed
`u`.  For `u` large and positive, its potentially exponential part is

```text
H_(T,tau)(-i/2)exp(u/2)

 -exp(iTu)/[2sqrt(pi tau)]
  sum_(n>=2)Lambda(n)n^(-1/2-iT)
  exp[-(u-log n)^2/(4tau)].                       (9.3)
```

Put

```text
w_u(x)=exp(iTu)/[2sqrt(pi tau)]
       x^(-1/2-iT)exp[-(u-log x)^2/(4tau)].        (9.3a)
```

Here

```text
Psi_Cheb(x)=sum_(n<=x)Lambda(n).                   (9.3aa)
```

The polar term and the near Euler tail satisfy the exact Stieltjes identity

```text
H_(T,tau)(-i/2)exp(u/2)
 -sum_(n>=2)Lambda(n)w_u(n)

 =integral_(0,1)w_u(x)dx
  +integral_[1,infinity)w_u(x)d[x-Psi_Cheb(x)].   (9.3b)
```

The first integral is super-Gaussian as `u` tends to positive infinity.  The
second is the precise log-Gaussian prime-number error; this fixes both the
sign and the boundary term.  The remaining Gamma and opposite Euler tail
must still be retained in the full norm until their effect on the abscissa is
proved.

### Proposition 9.1 - Gamma is neutral for every positive abscissa

Split (9.2) exactly as

```text
S_(T,tau)=P_(T,tau)+G_(T,tau)+R_(T,tau),          (9.3c)
```

where `P` is the sum of the two Euler tails, `G` is the complete Gamma
integral, and

```text
R(u)=H(i/2)exp(-u/2)+H(-i/2)exp(u/2).             (9.3d)
```

For every `0<a<1/2` there is a constant `C_(a,T,tau)` such that

```text
|G_(T,tau)(u)|<=C_(a,T,tau)exp(-a|u|).            (9.3e)
```

Consequently, for every `s>0`,

```text
integral_R exp(-s|u|)|S(u)|^2du<infinity

iff

integral_R exp(-s|u|)|P(u)+R(u)|^2du<infinity.    (9.3f)
```

#### Proof

On the real axis write the Gamma multiplier as the sum of the two analytic
functions

```text
1/2 psi(1/4+ir/2)+1/2 psi(1/4-ir/2)-log pi.
```

Its nearest poles have imaginary parts `+-1/2`.  In the strip
`|Im r|<1/2`, multiplication by the shifted Gaussian `H_(T,tau)(r)` gives
Gaussian decay in `Re r`, up to the logarithmic growth of `psi`.  Moving the
Fourier contour to `Im r=+a` or `Im r=-a`, according to the sign of `u`,
proves (9.3e).  Thus `G` belongs to every space
`L^2(exp(-s|u|)du)`.  Since each such space is a vector space, subtracting
`G` proves both directions of (9.3f). `QED`

This removes a possible false target.  The Gamma channel is indispensable in
the exact formula, but it cannot carry a positive convergence abscissa.

### Proposition 9.2 - Exact one-sided centered prime reduction

Put `B=H_(T,tau)(-i/2)` and, for `u>=0`,

```text
E_+(u)=B exp(u/2)-sum_(n>=2)Lambda(n)w_u(n).       (9.3g)
```

For every `s>0`,

```text
integral_R exp(-s|u|)|S(u)|^2du<infinity

iff

integral_0^infinity exp(-su)|E_+(u)|^2du<infinity

iff

integral_0^infinity exp(-su)
 |integral_[1,infinity)w_u(x)d[x-Psi_Cheb(x)]|^2du
 <infinity.                                      (9.3h)
```

In particular, if

```text
sigma_c(f)=inf{s>0:
 integral_0^infinity exp(-su)|f(u)|^2du<infinity},
```

then Theorem 8.2 gives the exact arithmetic identity

```text
sigma_c(u |-> integral_[1,infinity)
 w_u(x)d[x-Psi_Cheb(x)])
   =2 sup_(Xi(p)=0)|Im p|.                        (9.3i)
```

#### Proof

Schwarz reflection gives `S(-u)=conj(S(u))`, so the bilateral norm is twice
its positive half.  Proposition 9.1 removes `G`.  On that half-axis the
difference between `P+R` and `E_+` is

```text
H(i/2)exp(-u/2)
 -sum_(n>=2)Lambda(n)/sqrt(n) h_(T,tau;u)(log n).
```

The first term is in every positively weighted `L^2` space.  For the second,
`(u+log n)^2>=(u^2+log^2 n)/2`; hence its absolute value is bounded by a
constant times

```text
exp[-u^2/(8tau)]
 sum_(n>=2)Lambda(n)n^(-1/2)exp[-log^2(n)/(8tau)],
```

which is super-Gaussian in `u`.  Finally (9.3b) differs from its second
integral by the super-Gaussian integral over `(0,1)`.  These three
subtractions prove (9.3h), and (8.7) proves (9.3i). `QED`

Thus the force does not lie in a separate Gamma estimate or in the remote
Euler tail.  It lies entirely in the centered near-prime error.

### Proposition 9.3 - Finite connected covariance kernel

Use logarithmic coordinates and define the locally finite complex measure

```text
d mu_T(y)
 =exp[(1/2-iT)y]dy
  -sum_(n>=2)Lambda(n)n^(-1/2-iT)delta_(log n)(dy),
                                                    y>=0.            (9.3j)
```

With `c_tau=1/[2sqrt(pi tau)]`, the force-bearing function in (9.3h) is

```text
J_(T,tau)(u)
 =c_tau exp(iTu) integral_[0,infinity)
   exp[-(u-y)^2/(4tau)]d mu_T(y).                 (9.3k)
```

For a finite cutoff `V`, let `mu_(T,V)` be the restriction of `mu_T` to
`[0,V]` and let `J_V` be (9.3k) with that restriction.  Direct Gaussian
integration gives, for every `s>0`,

```text
integral_0^infinity exp(-su)|J_V(u)|^2du
 =double_integral_[0,V]^2 K_(s,tau)(y,z)
   d mu_T(y)d conj(mu_T)(z),                     (9.3l)
```

where

```text
K_(s,tau)(y,z)
 =c_tau^2 exp[-(y-z)^2/(8tau)]
  sqrt(pi tau/2)
  exp[-s(y+z)/2+tau s^2/2]
  erfc({tau s-(y+z)/2}/sqrt(2tau)).              (9.3m)
```

The right side of (9.3l) is nonnegative because it is the squared norm on
the left; no pointwise sign assertion about the complex measure is being
made.  In the remote quadrant,

```text
K_(s,tau)(y,z)
 ~c_tau^2 sqrt(2pi tau)
   exp[-s(y+z)/2]exp[-(y-z)^2/(8tau)]             (9.3n)
```

as `y+z` tends to infinity.  Formula (9.3l), rather than a termwise global
double series, is the safe covariance coordinate.  For `s<=1`, passage
`V->infinity` is part of the estimate and may not be made channel by
channel.  The covariance is connected because the continuous `dx` source
and the atomic `d Psi_Cheb` source have already been combined in the single
measure `d[x-Psi_Cheb(x)]` before squaring.

### Proposition 9.4 - Local diagonal subtraction cannot lower the abscissa

The same-event atomic diagonal inside the finite form (9.3l) has density

```text
D_Delta(u)=c_tau^2 sum_(n>=2)Lambda(n)^2/n
            exp[-(u-log n)^2/(2tau)].            (9.3o)
```

For every `s>0`,

```text
integral_0^infinity exp(-su)D_Delta(u)du
 <=C_(s,tau)sum_(n>=2)Lambda(n)^2/n^(1+s)
 <infinity.                                      (9.3p)
```

At `s=0` this diagonal diverges.  Fixed cross-pairs `p^k,p^ell` belonging to
one prime, with `k!=ell`, are even smaller because (9.3m) supplies the factor
`exp[-(k-ell)^2 log^2(p)/(8tau)]`.  Finite-support corrections, the decaying
polar term, the Gamma channel and the opposite Euler tail likewise belong to
every positively weighted `L^2` space.

Therefore none of these local pieces can determine a positive convergence
abscissa.  The polar subtraction `d Psi_Cheb -> d Psi_Cheb-dx` is different:
it cancels the universal prime-number-theorem mode before the norm is formed.
After that canonical centering, any further argument capable of reducing
the abscissa in (9.3i) must control the global off-diagonal covariance of
`mu_T`.  A diagonal estimate, a finite collection of prime-power matches or
a separate Gamma bound cannot close the target.

Define `LOG-GAUSSIAN-L2-CANCELLATION` to be

```text
for one fixed T,tau and every epsilon>0,

integral_R exp(-epsilon|u|)
 |S_(T,tau)(u)|^2du<infinity.                     (9.4)
```

Theorem 8.2 and Proposition 9.2 prove that (9.4) is equivalent to RH and
Omega7.  It is the remaining force-bearing estimate of the all-pairs route.
Proposition 9.4 narrows it further: the required cancellation is global and
off-diagonal after canonical prime-number-theorem centering.  Proving it from
a classical RH-sized bound for the smoothed prime-number error would only
move the hypothesis; a successful proof must control that connected
covariance unconditionally.

E101.087 subsequently gives the exact finite source form.  Its moving cutoff
must be endpoint-renormalized, and the weakest equivalent target is a
`liminf` of finite Mellin--Gaussian energies.  It also closes the endpoint
`s=1` unconditionally and proves that the only unused structure capable of
distinguishing the prime measure from positive falsifiers is the global
divisor-renewal identity.

The exact stop rules are:

```text
do not infer (9.4) from the separate sizes of Gamma and Prime;
do not use a zero-free region compatible with one off-line zero;
do not continue (7.11) term by term through accumulating differences;
do not replace (9.4) by density-one, average-height or finite-window
information;
do not introduce Xi'/Xi or the divisor to prove the source estimate. (9.5)
```

## 10. Relation to the parity-Gram route

The two active targets now have complementary algebra:

```text
PARITY-GRAM-GRAPH-TRACE:
  isolate one zero and its conjugate;
  linear multiplicity;
  nonnegative quadratic Gram;
  missing operation = conjugate graph.

LOG-GAUSSIAN-L2-CANCELLATION:
  retain all pairs;
  quadratic multiplicity;
  exact abscissa 2 sup|Im p|;
  missing operation = source-side subexponential L2 cancellation. (10.1)
```

The Abel route avoids the graph-selection no-go by refusing to select a
label before the transform.  It does not avoid conservation of difficulty:
arithmetic finiteness for every `s>0` is equivalent to excluding every
off-line zero.

This distinction gives a concrete stop rule.  Continue the quadratic graph
route only if a source operation creates atomwise conjugation.  Continue the
Abel route only if a Gamma--Euler estimate improves the logarithmic prime
error to (9.4) without first reconstructing the divisor.

## 11. Literature and nonduplication gate

The following papers establish the recent horizontal pair-correlation
antecedents:

```text
Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh,
Pair Correlation of Zeros of the Riemann Zeta Function I:
  https://arxiv.org/abs/2501.14545

Goldston--Lee--Schettler--Suriajaya,
Pair Correlation Conjecture for the Zeros of the Riemann Zeta-function I:
  https://arxiv.org/abs/2503.15449

Goldston--Suriajaya, Zeta Zeros on the Critical Line:
  https://arxiv.org/abs/2511.20059

Goldston--Suriajaya, Zeta Zeros in a Narrow Vertical Box:
  https://arxiv.org/abs/2603.28104

Balanzario--Cardenas Romero,
An explicit formula for the zeros of the Riemann zeta function:
  https://arxiv.org/abs/2312.00108

Banks--Sinha, The Riemann Hypothesis via the generalized von Mangoldt
function:
  https://arxiv.org/abs/2209.11768

Gonek--Graham--Lee,
The Lindelof hypothesis for primes is equivalent to the Riemann hypothesis:
  https://doi.org/10.1090/proc/14974

T. Zhao, On the mean values of the error terms in Mertens' theorems:
  https://doi.org/10.1007/s40993-025-00640-y

M. A. K. Akhtar,
A Log-Fractal Spectral Reformulation of the Prime Error Term and a
Cancellation Criterion Equivalent to the Riemann Hypothesis:
  https://ssrn.com/abstract=6695378                (11.1)
```

They already contain the unconditional complex pair function, its positivity,
the symmetric diagonal and asymptotic consequences under pair-correlation or
narrow-box hypotheses.  They do not contain the finite Abel residue energy
(5.1), the real-pole equivalence (5.6), or the exact Gaussian abscissa
(8.7) found in the inspected versions.  Akhtar explicitly uses the normalized
logarithmic error

```text
exp(-v/2)[Psi_Cheb(exp v)-exp v]
```

and its subexponential growth as a classical RH-equivalent reformulation.
That signal, its normalization and the idea of reading RH as logarithmic-scale
cancellation are therefore antecedents, not new outputs of the present route.
Zhao's Lemma 8 also records that, with
`Theta=sup Re rho`, the dyadic mean square of `Psi_Cheb(x)-x` has exponent
`2Theta+1`, up to the stated endpoint loss when `Theta>1/2`.  Thus the broad
principle that the mean-square growth exponent detects the rightmost zeros is
already established.  The exact fixed-Gaussian identity (8.7) is a particular
source-to-divisor realization of that principle, not a claim to have invented
an `L^2` prime-error criterion.

No novelty is claimed for:

```text
the kernel w_2 or positivity of F_I;
bilateral Laplace and Abel transforms;
the symmetric diagonal rho <-> 1-conj(rho);
Gaussian Weil tests;
products of two explicit formulas;
classical abscissa arguments for positive Laplace integrals;
RH-equivalent twisted prime-error estimates;
the normalized logarithmic prime-error signal;
mean-square prime-error exponents governed by sup Re rho;
the fact that the estimate (9.4) is RH-equivalent.                  (11.2)
```

The only potentially new contribution is the exact combination: real Abel
poles turn the symmetric horizontal diagonal into a positive finite
discriminator, and one complete fixed Gaussian Gamma--Euler pair current has
abscissa exactly `2 sup|Im p|`, converting graph selection into one explicit
centered covariance estimate.  Global novelty is not asserted without a
broader literature comparison.

## 12. Status

```text
proved:
  finite positivity factorization;
  exact finite Abel transform;
  positive real-residue formula;
  E_I=0 exactly for a critical-line finite window;
  multiplicity-safe symmetric-pair detection;
  height-only no-go;
  exact Gaussian all-channel pair identity for Re s>1;
  positive convolution transfer A<->I;
  exact abscissa sigma_c=2 sup|Im p|;
  one fixed Gaussian family suffices;
  Gamma neutrality at every positive abscissa;
  exact one-sided reduction to d[x-Psi_Cheb(x)];
  finite connected log-Gaussian covariance kernel;
  positive-abscissa no-go for local diagonal subtraction;

new live target:
  ENDPOINT-RENORMALIZED-GAUSSIAN-LIMINF of E101.087;
  global off-diagonal LOG-GAUSSIAN-L2-CANCELLATION;

not claimed:
  global meromorphic continuation of the Gaussian pair series;
  the source-side estimate (9.4);
  a proof of RH or Omega7;

still open:
  LOG-GAUSSIAN-L2-CANCELLATION;
  PARITY-GRAM-GRAPH-TRACE;
  DIRECTIONAL-IDENT and Omega7.
```
