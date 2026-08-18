# E101.090 - Endpoint Toeplitz--Hankel separation

## 1. Decision

The endpoint-renormalized energy of E101.087 admits an exact finite split
which removes the floor discrepancy and isolates the only dangerous
two-variable channel.

For an integer cutoff `N`, one has

```text
sM_N(s)=P_N(s)+R_N(s),                                      (1.1)
```

where `R_N` has a Gaussian norm bounded uniformly in `N`, and `P_N` is a
balanced Dirichlet polynomial with coefficients `Lambda(n)-1`.  Its
Hermitian energy is a diagonally weighted multiplicative-Toeplitz form
indexed by quotients `m/n`.

The corresponding holomorphic square is a Helson, or multiplicative-Hankel,
form indexed by products `mn`.  That entire product channel is
unconditionally and uniformly bounded:

```text
sup_N | integral w(t)P_N(a+it)^2dt |<infinity.               (1.2)
```

Consequently, a bound on `Lambda*Lambda`, the first Selberg pushforward or
the same-sign product form alone does not close the problem.  The remaining
force is exactly

```text
P_N(s)P_N(conj s),

equivalently the centered quotient correlation m/n.                         (1.3)
```

There is also an exact dichotomy for the linear divisor-incidence projections
defined below.  A genuinely truncated system is not coercive on the full
coefficient space because it cannot distinguish two primes beyond its
level.  Completing all divisor rows makes that particular incidence matrix
triangular and its inverse is Moebius.  Completing the product support beyond
the actually attained divisors without a separate theorem repeats the
support error of E101.088.

Thus the live target of E101.089 is sharpened to one object:

```text
BALANCED-QUOTIENT-COVARIANCE.                               (1.4)
```

The subsequent audits in this document close five apparent escapes without
changing that target:

```text
a compact causal outer filter turns it into an invertible Cramer window;

common dilation multiplies it by zeta(1+epsilon);

ordinary cutoff variation is subcritical, while critical variation is the
Cramer norm;

the logarithmic divisor commutator hides the exact Moebius inverse;

the full binomial-carry system is a postcomposition of divisor incidence,
and its critical frame restores the same inverse.                         (1.5)
```

Each statement is proved below and checked against the prime-tower and
single-mode falsifiers.  They prevent another equivalent-coordinate loop;
they do not furnish the missing signed estimate.

No upper bound for (1.4), RH or Omega7 is claimed here.

## 2. Integer endpoint formula

Fix

```text
epsilon>0,

a=(1+epsilon)/2,

s=a+it,

w(t)=|H_(T,tau)(t-i epsilon/2)|^2
    =exp{-2tau[(t-T)^2-epsilon^2/4]}.                        (2.1)
```

Throughout this document,

```text
||F||_(L2(w))^2=1/(2pi)integral_R w(t)|F(t)|^2dt.            (2.1a)
```

For an integer `N>=2`, E101.087 gives

```text
sM_N(s)
 =sum_(n<=N)Lambda(n)[n^(-s)-N^(-s)]
  -s[N^(1-s)-1]/(1-s)+1-N^(-s).                             (2.2)
```

At `s=1`, every quotient containing `1-s` is interpreted by its removable
continuous value.

The summand at `n=N` is zero.  Define

```text
P_N(s)
 =sum_(2<=n<N)[Lambda(n)-1][n^(-s)-N^(-s)],                 (2.3)

R_N(s)
 =-s integral_1^N {x}x^(-s-1)dx.                            (2.4)
```

### Proposition 2.1 - Exact floor split

For every integer `N>=2`, (1.1) holds.  Moreover,

```text
|R_N(a+it)|<=|a+it|/a.                                      (2.5)
```

### Proof

Subtract (2.3) from (2.2).  The result is

```text
sum_(n=1)^(N-1)n^(-s)
 -(N-1)N^(-s)
 -s[N^(1-s)-1]/(1-s).                                       (2.6)
```

Integration by parts against `floor(x)` gives

```text
-s integral_1^N {x}x^(-s-1)dx
 =sum_(n=1)^N n^(-s)-N^(1-s)
  -s[N^(1-s)-1]/(1-s),                                      (2.7)
```

and (2.6) equals (2.7).  Since `0<={x}<1`,

```text
|R_N(s)|
 <=|s| integral_1^infinity x^(-a-1)dx
 =|s|/a.                                                     (2.8)
```

This proves both assertions. `QED`

Because `w(t)` is Gaussian,

```text
sup_N 1/(2pi)integral_R w(t)|R_N(a+it)|^2dt<infinity.        (2.9)
```

By the triangle inequality in the weighted Hilbert space,

```text
liminf_N ||sM_N||_(L2(w))<infinity

iff

liminf_N ||P_N||_(L2(w))<infinity.                          (2.10)
```

Thus the fractional-part channel is rigorously neutral.

### Proposition 2.2 - Integer cutoffs are cofinal

The `liminf` criterion of E101.087 is unchanged when `X` is restricted to
positive integers.

### Proof

If `N=floor(X)`, then

```text
M_X(s)-M_N(s)=integral_N^X E_0(x)x^(-s-1)dx.                (2.11)
```

The elementary bound `E_0(x)=O(x log x)` gives, uniformly for
`N<=X<N+1`,

```text
|s[M_X(s)-M_N(s)]|
 <<|s|N^(-a)log N.                                          (2.12)
```

After squaring and integrating against the Gaussian `w(t)`, the right side
of (2.12) tends to zero.  Every cofinal real sequence can therefore be
replaced by its integer parts without changing boundedness of the selected
norms.  The converse is immediate because the integers are cofinal. `QED`

## 3. Balanced coefficient form

Put, with the cutoff dependence displayed when needed,

```text
beta_n^(N)=Lambda(n)-1,              2<=n<N,

beta_N^(N)=-sum_(2<=n<N)beta_n^(N).                          (3.1)
```

Then

```text
sum_(n=2)^N beta_n^(N)=0,

P_N(s)=sum_(n=2)^N beta_n^(N)n^(-s).                         (3.2)
```

The superscript is suppressed inside fixed-`N` formulas.  The moving
coefficient `beta_N^(N)` is not discarded.  Chebyshev's estimate
gives the unconditional bound

```text
|beta_N^(N)|=O(N).                                           (3.3)
```

Define

```text
c_epsilon
 =exp(tau epsilon^2/2)/[2sqrt(2pi tau)],

Phi(r)=exp[-log^2(r)/(8tau)]r^(-iT).                         (3.4)
```

### Proposition 3.1 - Exact quotient covariance

The finite Hermitian energy is

```text
Q_N
 :=1/(2pi)integral_R w(t)|P_N(a+it)|^2dt

 =c_epsilon sum_(m,n=2)^N
   beta_m beta_n (mn)^(-a)Phi(m/n).                          (3.5)
```

### Proof

Expand the square.  The Gaussian integral is

```text
1/(2pi)integral_R w(t)exp[-it log(m/n)]dt
 =c_epsilon Phi(m/n).                                       (3.6)
```

Substitution gives (3.5).  Symmetry under `(m,n)->(n,m)` makes the right
side real and nonnegative, as required by the first line of (3.5). `QED`

The balance in (3.2) is the finite endpoint subtraction, not an optional
centering.  Omitting `beta_N` reconstructs the dangerous moving boundary of
E101.087.

## 4. Quotient and product organizations

Every pair `(m,n)` has a unique representation

```text
m=dr,

n=ds,

(r,s)=1.                                                     (4.1)
```

Therefore (3.5) becomes

```text
Q_N
 =c_epsilon sum_((r,s)=1)(rs)^(-a)Phi(r/s)
   sum_(d<=N/max(r,s))
    beta_(dr)beta_(ds)d^(-2a),                              (4.2)
```

where a coefficient outside `{2,...,N}` is understood as zero.

Alternatively, group by `k=mn`:

```text
Q_N
 =c_epsilon sum_(k<=N^2)k^(-a)
   sum_(mn=k; 2<=m,n<=N)
    beta_m beta_n Phi(m/n).                                 (4.3)
```

Equations (4.2) and (4.3) are exact.  The first retains the quotient and a
common-multiple correlation.  The second exposes why a one-variable
Dirichlet convolution loses information: at fixed `k`, the factor
`Phi(m/n)` still distinguishes different divisors of the same product.

## 5. The holomorphic product channel is uniformly safe

Define the same-sign form

```text
H_N
 =1/(2pi)integral_R w(t)P_N(a+it)^2dt.                       (5.1)
```

Its kernel is indexed by `mn`, not `m/n`:

```text
H_N
 =c_epsilon sum_(m,n=2)^N
   beta_m beta_n(mn)^(-a)
   exp[-log^2(mn)/(8tau)](mn)^(-iT).                         (5.2)
```

### Theorem 5.1 - Uniform Hankel bound

For every fixed `epsilon>0`, `T in R` and `tau>0`,

```text
sup_(N>=2)|H_N|<infinity.                                   (5.3)
```

### Proof

For `n<N`,

```text
|beta_n|<=log n+1.                                          (5.4)
```

The infinite double series

```text
sum_(m,n>=2)
 (log m+1)(log n+1)(mn)^(-a)
 exp[-log^2(mn)/(8tau)]                                     (5.5)
```

converges for every real `a`, because the log-Gaussian beats every power of
`mn`.

It remains to control the moving coefficient.  From (3.3), its diagonal
contribution is bounded by

```text
N^2 N^(-2a)exp[-log^2(N^2)/(8tau)],                          (5.6)
```

which is uniformly bounded and tends to zero.  Its cross contribution is at
most a constant times

```text
N^(1-a) sum_(m>=2)(log m+1)m^(-a)
 exp[-log^2(Nm)/(8tau)],                                    (5.7)
```

and the log-Gaussian again dominates the polynomial factor uniformly in
`N`.  Equations (5.5)--(5.7) prove the uniform bound (5.3); after separating
the moving row and column they also show that those moving contributions
tend to zero. `QED`

The terminology is standard and already occurs earlier in the project.
Here `(Phi(m/n))` is used only as a finite multiplicative-Toeplitz matrix;
no bounded infinite Toeplitz operator or `L^infinity` symbol is asserted.
The specific role here is the exact endpoint-renormalized finite separation
(3.5) versus (5.2), with no asymptotic Toeplitz approximation.

## 6. Exact real--imaginary polarization

Pointwise for a complex number `z`,

```text
|z|^2-Re(z^2)=2[Im z]^2,

|z|^2+Re(z^2)=2[Re z]^2.                                   (6.1)
```

Apply (6.1) to `P_N(a+it)` and integrate.

### Corollary 6.1 - Real--imaginary localization after product subtraction

```text
Q_N-Re H_N
 =1/pi integral_R w(t)[Im P_N(a+it)]^2dt,                   (6.2)

Q_N+Re H_N
 =1/pi integral_R w(t)[Re P_N(a+it)]^2dt.                   (6.3)
```

Since `H_N` is uniformly bounded, bounding `Q_N` along a cofinal sequence is
equivalent to bounding either right side of (6.2) or (6.3).  In particular,
the obstruction remains in either real component after the bounded
same-sign product form is subtracted.  Expanding `[Im P_N]^2` still mixes a
quotient form with a product form; it becomes equivalent to the quotient
target only because Theorem 5.1 has already bounded the latter product
correction.

## 7. The first Selberg identity is a same-sign pushforward

Let `one(n)=1` and

```text
u=Lambda-one,

tau_div=one*one.                                             (7.1)
```

Then

```text
u*u=Lambda*Lambda-2log+tau_div.                              (7.2)
```

Let

```text
Lambda_2=D Lambda+Lambda*Lambda.                             (7.3)
```

Since `Du=D Lambda-log`,

```text
u*u+Du=Lambda_2-3log+tau_div.                                (7.4)
```

Selberg's symmetry formula gives

```text
sum_(n<=x)[(u*u)(n)+Du(n)]=O(x).                             (7.5)
```

This controls a one-variable product pushforward.  Even if one replaces the
actual truncated divisor band in (4.3) by all divisors and grants (7.5) with
the required coefficient, partial summation against `k^(-a)` up to `N^2`
gives only

```text
O(N^(1-epsilon)),       0<epsilon<1,

O(log N),               epsilon=1,

O(1),                   epsilon>1.                           (7.6)
```

Thus it fails to give `O(1)` precisely in the difficult range
`0<epsilon<=1`.

More importantly, (7.5) does not retain `Phi(m/n)`.  Taking absolute values
to remove that factor uses

```text
|P_N(s)^2|=|P_N(s)|^2,                                      (7.7)
```

which is precisely the target `Q_N`.  Selberg controls `u*u+Du`, not
literally the finite form `H_N`, whose moving endpoint and truncated divisor
band are different.  The relevant conclusion is only that Selberg is a
same-sign product pushforward and, by itself, supplies no upper bound for the
multiplicative-Toeplitz quotient channel.  The independent Gaussian proof of
Theorem 5.1 is what makes `H_N` safe.

## 8. Truncated divisor-incidence projections have an exact kernel

Fix `R`, and consider any collection of linear divisor observables which
depends only on

```text
sum_(d|n; d<=R)c_d                                           (8.1)
```

for prescribed weights `c_d`.  Choose two distinct primes `p,q>R`, and then
choose a section size `N>=max(p,q)`.  Among the observed divisors, both
primes have only `d=1`.  Therefore the vector

```text
x=e_p-e_q                                                    (8.2)
```

is invisible to every observable of the form (8.1).

Its endpoint feature is not zero:

```text
||p^(-a-it)-q^(-a-it)||_(L2(w))^2

 =c_epsilon[p^(-2a)+q^(-2a)
  -2(pq)^(-a)exp(-log^2(p/q)/(8tau))
    cos(T log(p/q))]
 >0.                                                         (8.3)
```

Strict positivity follows because two distinct exponential functions cannot
agree on a set of positive `t` measure.  Consequently no projection in the
linear class (8.1) is uniformly coercive on the full balanced coefficient
space.

This is not a dimension count.  Equation (8.2) is an explicit kernel vector
which survives every choice of truncated weights.  It does not exclude an
estimate specialized to the arithmetic vector `beta^(N)`, and it is not a
statement about sieve mechanisms using additional Type II or nonlinear
information.

## 9. The complete divisor system is Moebius inversion

If all divisor rows are included, the finite incidence matrix

```text
A_(d,n)=1_(d|n),                  1<=d,n<=N                  (9.1)
```

is triangular in the natural order and has diagonal one.  Its inverse has
entries given by the Moebius function.

For the exact coefficient `u=Lambda-one`,

```text
sum_(d|n)u(d)=log n-tau_div(n),                              (9.2)

u=mu_Moebius*(log-tau_div).                                 (9.3)
```

Thus completing the divisor observations removes the kernel of Section 8
by restoring the classical convolution inverse for this full linear system.
A general inverse-norm estimate would return to the Moebius wall.  This does
not exclude an estimate tailored to the special datum `log-tau_div` or an
identity carrying additional marked structure.

The dichotomy is exact:

```text
truncated divisor system: nontrivial kernel;

complete divisor system: Moebius inversion.                 (9.4)
```

## 10. Product-support completion requires a theorem

At a fixed product `k`, the inner sum in (4.3) contains only pairs satisfying

```text
mn=k,

m<=N,

n<=N.                                                       (10.1)
```

When `k>N`, writing `n=k/m` shows that the attained divisor band is

```text
k/N<=m<=N.                                                   (10.2)
```

Divisors outside (10.2) are absent.  Replacing the inner sum in (4.3) by a
complete divisor convolution changes the form.  It is the product analogue
of replacing the floor-quotient support `Q_N` by every integer in E101.088.

Any use of Selberg on (4.3) must first prove a completion theorem controlling
the omitted divisors with their signs and the ratio kernel.  Positivity of a
different complete convolution cannot fill this support.

## 11. Large-sieve scale does not close a fixed Gaussian window

The frequencies of `P_N(a+it)` are `log n`.  Adjacent frequencies near `N`
have spacing

```text
log(n+1)-log n asymp 1/N.                                   (11.1)
```

The Montgomery--Vaughan mean-value inequality for a Dirichlet polynomial on
a fixed-length `t` window therefore carries a cost of order `N` from the
reciprocal minimal spacing.  The Gaussian window has fixed effective length,
so the general large-sieve bound is much larger than (1.4).  The Gaussian
weight improves remote `t` tails, not the near-collision of the logarithmic
frequencies.

To pass from interval to Gaussian weight, partition the real line into unit
intervals.  Apply the translated Montgomery--Vaughan inequality on each
interval and multiply by the supremum of `w` there.  Those suprema form a
summable Gaussian sequence, while the reciprocal-spacing cost remains
`O(N)`.  Thus the weighted version has the same obstructing scale.

Accordingly, the coefficient-blind fixed-window Montgomery--Vaughan bound
does not provide the missing scale.  A successful quotient estimate may
still be a Dirichlet-polynomial inequality, but it must use the particular
signed coefficients, exact endpoint balance or additional arithmetic
structure.

## 12. Literature and nonduplication gate

The governing primary antecedents are

```text
A. Selberg, An Elementary Proof of the Prime-Number Theorem:
  https://www.jstor.org/stable/1969455

H. L. Montgomery, R. C. Vaughan,
Hilbert's inequality:
  https://doi.org/10.1112/jlms/s2-8.1.73

H. Hedenmalm, P. Lindqvist, K. Seip,
A Hilbert space of Dirichlet series and systems of dilated functions in
L2(0,1):
  https://doi.org/10.1215/S0012-7094-97-08601-4

N. Nikolski, A. Pushnitski,
Szego-type limit theorems for multiplicative Toeplitz operators and
non-Folner approximations:
  https://arxiv.org/abs/2001.01474

O. F. Brevig, K.-M. Perfekt,
Weak product spaces of Dirichlet series:
  https://doi.org/10.1007/s00020-016-2320-3

M. Miheisi, A. Pushnitski,
A Helson matrix with explicit eigenvalue asymptotics:
  https://arxiv.org/abs/1709.06326

K. Ford, J. Maynard,
On the theory of prime producing sieves:
  https://arxiv.org/abs/2407.14368                           (12.1)
```

The natural sections `{1,...,N}` are not multiplicatively Folner, so ordinary
Szego intuition cannot be imported into (3.5).  Modern prime-producing
sieves also use Type II or nonlinear information beyond the linear
divisor-incidence class of Section 8.  No novelty is claimed for
Toeplitz/Helson terminology, Dirichlet-series Hardy spaces,
Dirichlet-polynomial mean values, Selberg symmetry, divisor incidence, sieve
weights or Moebius inversion.  The program-specific advance is only the
exact finite combination

```text
integer endpoint split;
balanced moving coefficient;
uniformly safe holomorphic product channel;
dangerous Hermitian quotient channel;
truncated-kernel versus complete-Moebius dichotomy.          (12.2)
```

No inspected antecedent is used as an unconditional bound for (1.4), and no
new Omega7 mechanism is claimed in this document.

## 13. Live theorem and stop rule

Fix `T in R` and `tau>0`.  The remaining finite theorem is

```text
BALANCED-QUOTIENT-COVARIANCE:

for every epsilon>0, there is a cofinal sequence N_j=N_j(epsilon)
such that

sum_(m,n=2)^(N_j)
 beta_m^(N_j) beta_n^(N_j)(mn)^(-(1+epsilon)/2)
 exp[-log^2(m/n)/(8tau)]exp[-iT log(m/n)]

is bounded above.                                           (13.1)
```

The expression is real and nonnegative: it is `Q_(N_j)/c_epsilon`.  By
Sections 2--3 and E101.087, (13.1) for every `epsilon>0`, with `T,tau` fixed
as above, is equivalent to RH and Omega7.

The next mechanism must satisfy all four tests:

```text
retain the endpoint coefficient beta_N^(N);

use the special signed arithmetic coefficients rather than a
coefficient-blind coercivity statement;

preserve the attained divisor support, or prove a signed completion theorem;

produce a signed upper bound for the quotient form before taking absolute
values.                                                       (13.2)
```

Freeze:

```text
the same-sign P_N(s)^2 estimate as a standalone closure mechanism;

Lambda*Lambda or the first Selberg identity as the open channel;

coefficient-blind fixed-window large-sieve bounds;

uniform full-space coercivity for the linear truncated class (8.1);

unsupported completion of missing product divisors;

the generic complete divisor inverse presented as a new mechanism.       (13.3)
```

Status:

```text
proved:
  exact floor-discrepancy split;
  uniform neutrality of R_N;
  exact balanced quotient covariance;
  quotient--multiple and product organizations;
  uniform bound for the holomorphic Hankel form;
  exact real--imaginary localization;
  linear truncated-incidence kernel on the full coefficient space;
  complete-system Moebius dichotomy for linear incidence;
  product-support completion obligation;

open:
  BALANCED-QUOTIENT-COVARIANCE;
  MARKED-DIFFERENCE-ARITHMETIC-RIGIDITY;
  ENDPOINT-RENORMALIZED-GAUSSIAN-LIMINF;
  PARITY-GRAM-GRAPH-TRACE;
  DIRECTIONAL-IDENT and Omega7;

not claimed:
  an unconditional bound for Q_N;
  RH or Omega7.
```

## 14. A compact causal outer multiplier

The quotient--product separation can be made exact at the level of support.
This gives a strong audit of every proposed Hardy or phase bridge.

Use the Fourier convention

```text
Fourier[f](t)=integral_R f(y)exp(-ity)dy,

f(y)=1/(2pi)integral_R Fourier[f](t)exp(ity)dt.              (14.1)
```

Fix

```text
b>1/2,       A>0,       T in R,       r>=4,

L=rA.                                                         (14.2)
```

Define

```text
h_0(y)=exp[(-b+iT)y]1_[0,A](y),

H_0(z)=integral_R h_0(y)exp(-izy)dy
      ={1-exp[-A(b+i(z-T))]}/{b+i(z-T)},

h=h_0^(*r),

H=H_0^r.                                                     (14.3)
```

At `z=T+ib`, the displayed quotient has the removable value `A`.  Its
nonremovable zeros are

```text
z=T+2pi ell/A+ib,                ell in Z\{0}.               (14.4)
```

In particular, `H` is nonzero throughout the closed critical strip
`|Im z|<=1/2`.

Let

```text
B_(r,A)=1_[0,A]^(*r).                                       (14.5)
```

Then

```text
h(y)=exp[(-b+iT)y]B_(r,A)(y),

supp h=[0,L],

B_(r,A)(y)
 =1/(r-1)! sum_(k=0)^r (-1)^k binom(r,k)(y-kA)_+^(r-1).
                                                               (14.6)
```

### Proposition 14.1 - Outer and zero-free

`H_0` and `H` are outer in `H2(C_-)`.  On every closed substrip of
`Im z<b`,

```text
H(x+iy)=O((1+|x|)^(-r)).                                    (14.7)
```

### Proof

Paley--Wiener identifies `H_0` with the transform of an `L2` function
supported in `[0,infinity)`, hence with an element of `H2(C_-)`.  Formula
(14.4) gives no Blaschke factor in `C_-`.  The analytic continuation through
the real boundary, where `H_0` is nonzero, excludes a singular inner factor.
An exponential inner factor would be a positive delay of the source.  Such a
delay is impossible because the essential support of `h_0` begins at zero;
equivalently,

```text
log|H_0(T-iR)|=-log R+O(1),                 R->infinity,     (14.8)
```

rather than a negative linear function of `R`.  Thus the inner factor is
constant.  The same conclusions hold for the positive integer power `H`.
The denominator in (14.3), together with the numerator bounded away from its
upper zero line on a closed substrip, proves (14.7). `QED`

The function in (14.6) is an exponential B-spline.  Neither the spline nor
its Fourier transform is asserted to be new.

## 15. Complete trace and exact abscissa

Let `S_H(u)` be the translated Weil trace associated with `h`.  The complete
source formula is

```text
S_H(u)
 =H(i/2)exp(-u/2)+H(-i/2)exp(u/2)

  +1/(2pi)integral_R H(t)Gamma_infinity(t)exp(iut)dt

  -sum_(n>=2) Lambda(n)/sqrt(n)
    [h(u-log n)+h(u+log n)].                                (15.1)
```

The two Euler sums are finite for each `u`, the Gamma integral is absolutely
convergent, and the spectral form

```text
S_H(u)=sum_p m_p H(p)exp(iup)                               (15.2)
```

is absolutely convergent.  The decay order `r>=4` is more than is needed
for these assertions.

### Theorem 15.1 - One-filter abscissa

Put

```text
Y=sup_(Xi(p)=0)|Im p|.                                      (15.3)
```

Then

```text
inf{s>0: integral_R exp(-s|u|)|S_H(u)|^2du<infinity}=2Y.    (15.4)
```

The same abscissa is obtained from the positive half-line.

### Proof

Absolute convergence of (15.2) gives

```text
|S_H(u)|<=C_H exp(Y|u|),                                    (15.5)
```

so every `s>2Y` is admissible.  Conversely, suppose the integral on the
positive half-line is finite.  Cauchy--Schwarz makes

```text
L_H(z)=integral_0^infinity exp(-zu)S_H(u)du                 (15.6)
```

holomorphic for `Re z>s/2`.  In the initial half-plane of absolute
convergence,

```text
L_H(z)=sum_p m_p H(p)/(z-ip).                               (15.7)
```

The right side is locally normally convergent away from its poles.  Every
residue `m_pH(p)` is nonzero by (14.4).  Analytic continuation from the
initial half-plane therefore contradicts (15.6) if a pole satisfies
`-Im p>s/2`.  Conjugation symmetry of the divisor supplies the opposite
sign and gives `|Im p|<=s/2`.  Hence `s>=2Y`. `QED`

For `u>L`, define

```text
w_u(x)=x^(-1/2)h(u-log x).                                  (15.8)
```

Its support is the multiplicative window

```text
exp(u-L)<=x<=exp u.                                         (15.9)
```

Direct substitution gives

```text
integral_0^infinity w_u(x)dx=H(-i/2)exp(u/2).               (15.10)
```

Since `h(u+log n)=0` in this range, (15.1) becomes

```text
S_H(u)
 =H(i/2)exp(-u/2)

  +1/(2pi)integral_R H(t)Gamma_infinity(t)exp(iut)dt

  +integral_[exp(u-L),exp u] w_u(x)d[x-Psi_Cheb(x)].        (15.11)
```

The first two terms belong to every exponentially damped `L2` space on the
positive half-line.  For the Gamma term, shift its two meromorphic digamma
halves by any height strictly below `1/2` and use (14.7).  Thus the last line
of (15.11) alone has the abscissa (15.4).  This is an exact arithmetic window,
but Theorem 17.1 below shows why it is not an intermediate estimate.

## 16. Finite B-spline window and exact product annihilation

Fix `epsilon>0` and put

```text
a=(1+epsilon)/2,

c=b+epsilon/2,

H_epsilon(t)=H(t-i epsilon/2).                              (16.1)
```

For the moving balanced coefficients of Section 3, let

```text
F_N(t)=H_epsilon(t)P_N(a+it).                               (16.2)
```

Its inverse Fourier transform is

```text
f_N(y)
 =exp[(-c+iT)y]
  sum_(2<=n<=N; exp(y-L)<=n<=exp y)
   beta_n^(N)n^(b-1/2-iT)B_(r,A)(y-log n).                  (16.3)
```

In particular,

```text
supp f_N subset [log 2,log N+L].                            (16.4)
```

Plancherel now gives the exact Hermitian energy

```text
Q_N^cau
 :=1/(2pi)integral_R |H_epsilon(t)|^2|P_N(a+it)|^2dt

 =integral_2^(N exp L) x^(-2c-1)
   |sum_(2<=n<=N; x exp(-L)<=n<=x)
     beta_n^(N)n^(b-1/2-iT)B_(r,A)(log(x/n))|^2dx.          (16.5)
```

Thus a fixed outer multiplier converts the dangerous quotient form into one
exact B-spline variance on multiplicative windows.

Define

```text
W_epsilon(v)
 =1/(2pi)integral_R |H_epsilon(t)|^2exp(-itv)dt.             (16.6)
```

It is an autocorrelation of the source in (16.3), so

```text
supp W_epsilon subset [-L,L].                               (16.7)
```

Consequently,

```text
Q_N^cau
 =sum_(m,n=2)^N beta_m^(N)beta_n^(N)(mn)^(-a)
   W_epsilon(log(m/n)),                                     (16.8)
```

and only ratios `exp(-L)<=m/n<=exp L` occur.

The corresponding holomorphic weighted form is

```text
K_N^cau
 :=1/(2pi)integral_R |H_epsilon(t)|^2P_N(a+it)^2dt

 =sum_(m,n=2)^N beta_m^(N)beta_n^(N)(mn)^(-a)
   W_epsilon(log(mn)).                                      (16.9)
```

Choose the parameters in (14.2) so that

```text
L<log 4.                                                     (16.10)
```

Since `log(mn)>=log 4` for `m,n>=2`, (16.7) proves

```text
K_N^cau=0                         for every N.               (16.11)
```

There is an even simpler support identity:

```text
1/(2pi)integral_R F_N(t)^2dt
 =integral_R f_N(y)f_N(-y)dy=0.                             (16.12)
```

The first equality is Fourier inversion and the second follows from (16.4).
Thus the same-sign channel may vanish identically while the Hermitian channel
retains all of the target.

### Proposition 16.1 - The causal criterion is still RH-equivalent

For any fixed parameters (14.2),

```text
RH

iff

for every epsilon>0,
liminf_(N->infinity) Q_N^cau<infinity.                       (16.13)
```

### Proof

On the shifted line,

```text
|H_0(t-i epsilon/2)|
 >=[1-exp(-Ac)]/[c^2+(t-T)^2]^(1/2).                        (16.14)
```

Every fixed Gaussian centered at `T` is bounded above by a constant times
the `2r`-th power of the right side.  Hence boundedness in (16.13) implies
the Gaussian criterion of Section 13 and therefore RH.

Under RH,

```text
E_0(x)=O(x^(1/2)log^2 x).                                   (16.15)
```

Partial summation in the finite window of (16.5), including its moving
endpoint, bounds the inner sum by

```text
O(x^b log^2(2x)).                                           (16.16)
```

The resulting majorant is `x^(-1-epsilon)log^4(2x)`, which is
integrable.  It is independent of `N`, and proves the reverse implication.
`QED`

## 17. The window is the Cramer norm in invertible disguise

The force of (16.5) can be seen without the smoothing needed for the full
trace.  In this section only, take the finite model

```text
b=1/2,       r=1,       T=0.                                (17.1)
```

Put

```text
C_N(x)=sum_(2<=n<=min(x,N)) beta_n^(N).                      (17.2)
```

Outside a set of endpoints of measure zero,

```text
C_N(x)=E_0(x)+{x},                    2<=x<N,

C_N(x)=0,                             x>=N.                  (17.3)
```

The window sum is

```text
W_N(x)=C_N(x)-C_N(x exp(-A)).                               (17.4)
```

Let

```text
G_N(y)=exp(-ay)C_N(exp y),

q_A=exp(-aA).                                                (17.5)
```

Then the energy in (16.5) is exactly

```text
E_N=||G_N-q_A G_N(.-A)||_2^2.                               (17.6)
```

Translation is unitary on `L2(R)`, so

```text
(1-q_A)^2||G_N||_2^2
 <=E_N
 <=(1+q_A)^2||G_N||_2^2.                                   (17.7)
```

The inverse of the window difference is the norm-convergent Neumann series

```text
[I-q_A shift_A]^(-1)
 =sum_(k>=0)q_A^k shift_(kA).                               (17.8)
```

Moreover,

```text
||G_N||_2^2
 =integral_2^N |E_0(x)+{x}|^2x^(-2-epsilon)dx.              (17.9)
```

The fractional-part term belongs to this space unconditionally.  Therefore
(17.7)--(17.9) show that a cofinal bound for the multiplicative-window
energy is equivalent, with constants independent of `N`, to the classical
Cramer `L2` criterion.  Since the integrals in (17.9) are increasing with
`N`, the `liminf` formulation creates no weaker intermediate statement.

For completeness, the signed pair form of the same identity, now allowing
arbitrary `T`, is

```text
E_N
 =1/(2a) sum_(m,n=2)^N
   1_(exp(-A)<=m/n<=exp A)
   beta_m^(N)beta_n^(N)(m/n)^(-iT)

   *[max(m,n)^(-2a)
     -exp(-2aA)min(m,n)^(-2a)].                             (17.10)
```

It is real and nonnegative only after the complete symmetric sum.  Equation
(17.7) proves that obtaining its required upper bound is already the full
RH-strength step.

The moving coefficient exposes the same wall pointwise.  If

```text
u(n)=Lambda(n)-1,                 n>=2,                     (17.11)
```

then, as finite vectors,

```text
beta^(N)=u 1_[2,N]-E_0(N)e_N.                               (17.12)
```

Thus the endpoint atom is exactly the global prime-number error.  A
short-interval estimate which drops or treats that atom independently has
removed the force-bearing term.

## 18. Common dilation preserves the ratio but is neutral

There is a natural nonfactorized operator which appears to avoid the Selberg
sum pushforward.  For a finitely supported two-variable array `A`, define

```text
[C A](m,n)=sum_(d|gcd(m,n)) A(m/d,n/d).                     (18.1)
```

Its double Dirichlet series satisfies, in absolute convergence,

```text
D_2[C A](s,t)=zeta(s+t)D_2[A](s,t).                         (18.2)
```

On the Hermitian slice `t=conj(s)` used here,

```text
s+t=1+epsilon.                                               (18.3)
```

Consequently `C` is invertible there by the absolutely convergent common
Moebius convolution.  This avoids a critical zeta factor, but it does not
produce a new estimate.

### Proposition 18.1 - Common-dilation neutrality

Let `K` be any quotient kernel with

```text
K(dm,dn)=d^(-1-epsilon)K(m,n).                              (18.4)
```

For every finitely supported `A`, when the output of `C` is not truncated,

```text
sum_(m,n>=1)[C A](m,n)K(m,n)
 =zeta(1+epsilon)sum_(m,n>=1)A(m,n)K(m,n).                  (18.5)
```

If `A=beta beta^*`, then `C A` is positive semidefinite and (18.5) still
only multiplies its energy by the scalar `zeta(1+epsilon)`.

### Proof

Write `m=dr`, `n=dq` in (18.1), interchange the finite `A` sum with the
absolutely convergent `d` sum and apply (18.4).  This proves (18.5).  If
`D_d beta` denotes the vector supported on the multiples `dn` with value
`beta_n`, then

```text
C(beta beta^*)=sum_(d>=1)(D_d beta)(D_d beta)^*.             (18.6)
```

This proves positivity.  Pairing (18.6) with `K` and using (18.4) again
gives exactly (18.5), not a spectral gap. `QED`

The source identity makes the obstruction explicit.  Put, now including
the value at one,

```text
u=Lambda-one,

f=u*one=log-tau_div.                                        (18.7)
```

If `U,F` are their Dirichlet series, then

```text
U(s)=F(s)/zeta(s),                                          (18.8)
```

and hence

```text
D_2[C(u tensor u)](s,t)
 =zeta(s+t)F(s)F(t)/[zeta(s)zeta(t)].                       (18.9)
```

At `t=conj(s)`, the harmless numerator `zeta(1+epsilon)` leaves the critical
factor `1/|zeta(s)|^2` untouched.  Thus using `C` without the known source is
the target multiplied by a scalar; inserting the source restores the
separate critical inverse.

The prime-power support does not repair this.  If `(r,q)=1`, `r,q>1`,
`sigma=1+epsilon` and

```text
I_(r,q)(D)=sum_(d<=D)u(dr)u(dq)d^(-sigma),                  (18.10)
```

then direct support classification gives

```text
I_(r,q)(D)
 =Z_D(sigma)

  -1_(r=p^k)log p sum_(0<=j<=log_p D)p^(-j sigma)

  -1_(q=l^k)log l sum_(0<=j<=log_l D)l^(-j sigma)

  +Lambda(r)Lambda(q),                                      (18.11)
```

where the last term can occur only for powers of distinct primes.  There is
no sign: `r=5`, `q=6`, `D=1` gives `1-log 5<0`.  With the finite vector
`beta^(N)`, formula (17.12) inserts an additional defect proportional to
`E_0(N)` on exactly the terminal ray.  The common-dilation completion has
therefore returned to the same endpoint obstruction.

## 19. Literature gate and strengthened stop rule

The additional primary antecedents are

```text
P. X. Gallagher,
A Large Sieve Density Estimate Near sigma=1:
  https://doi.org/10.1007/BF01403187

G. Coppola, M. Laporta,
A Generalization of Gallagher's Lemma for Exponential Sums:
  https://arxiv.org/abs/1411.1739

T. H. Chan,
More Precise Pair Correlation of Zeros and Primes in Short Intervals:
  https://doi.org/10.1112/S0024610703004769

S. B. Stechkin, A. Yu. Popov,
The Asymptotic Distribution of Prime Numbers on the Average:
  https://doi.org/10.1070/RM1996v051n06ABEH003000

J. Pintz,
On the Remainder Term of the Prime Number Formula and the Zeros of
Riemann's Zeta-Function:
  https://doi.org/10.1007/BFb0099452

R. P. Brent, D. J. Platt, T. S. Trudgian,
The Mean Square of the Error Term in the Prime Number Theorem:
  https://arxiv.org/abs/2008.06140

P. Massopust,
Exponential Splines of Complex Order:
  https://arxiv.org/abs/1311.0140                            (19.1)
```

Gallagher--Coppola--Laporta already connect local compact weights with
mean squares of Dirichlet polynomials.  Chan treats additive and
multiplicative prime windows.  Stechkin--Popov, Pintz and
Brent--Platt--Trudgian show that compact sinc-type smoothing and mean-square
detection of an off-line zero are classical mechanisms.  Massopust contains
the exponential-spline construction.  No novelty is claimed for any of
these components.

The program-specific result is the exact finite package

```text
one causal outer multiplier nonzero on the complete critical strip;
one complete explicit arithmetic trace;
exact abscissa 2Y;
arbitrarily short multiplicative support;
identically zero holomorphic product channel;
Hermitian window exactly equivalent to the Cramer norm.     (19.2)
```

This is a reduction and a closure audit, not progress on the force-RH
inequality.

Add to the freeze list:

```text
causality or outer factorization as an estimate for Q_N;

Hilbert-transform polarization or inner phase recovery;

compact-window Selberg estimates which omit beta_N^(N);

the common-dilation completion C or any iteration of it;

the B-spline window criterion relabelled as weaker than Cramer.          (19.3)
```

The surviving problem remains an arithmetic-specific signed estimate for
the balanced quotient covariance.  Sections 17--18 prove that neither the
causal window nor a ratio-preserving common-dilation convolution supplies an
intermediate inequality.  Any successor must change the arithmetic input,
not merely the kernel or the organization of the same quadratic form.

## 20. Cutoff recurrence and the quadratic-variation wall

The moving endpoint has an exact one-step law.  Retain

```text
u(n)=Lambda(n)-1,                  n>=2,

E_0(N)=sum_(n=2)^N u(n).                                    (20.1)
```

From the definition of `P_N`, direct subtraction gives

```text
P_(N+1)(s)-P_N(s)
 =E_0(N)[N^(-s)-(N+1)^(-s)].                               (20.2)
```

Put

```text
d_N(s)=N^(-s)-(N+1)^(-s).                                  (20.3)
```

Since `P_2=0`, (20.2) also gives

```text
P_N(s)=sum_(k=2)^(N-1)E_0(k)d_k(s).                         (20.4)
```

Thus every finite endpoint polynomial is a path whose increments are the
global PNT error multiplied by a deterministic Mellin difference.

Use the Gaussian norm of Section 2 and set

```text
kappa_w
 =1/(2pi)integral_R w(t)|a+it|^2dt>0.                      (20.5)
```

### Proposition 20.1 - Subcritical and critical variation

For fixed `epsilon,T,tau`,

```text
||d_N||_(L2(w))^2
 =kappa_w N^(-3-epsilon)[1+O_w(N^(-1))].                   (20.6)
```

Consequently,

```text
sum_(N>=2)||P_(N+1)-P_N||_(L2(w))^2<infinity               (20.7)
```

holds unconditionally, whereas

```text
sum_(N>=2)N||P_(N+1)-P_N||_(L2(w))^2<infinity              (20.8)
```

is equivalent to

```text
sum_(N>=2)|E_0(N)|^2N^(-2-epsilon)<infinity,               (20.9)
```

and hence to the Cramer `L2` criterion at `epsilon`.

### Proof

The exact integral

```text
d_N(s)=s integral_N^(N+1)x^(-s-1)dx                        (20.10)
```

and Gaussian dominated convergence give

```text
N^(a+1)d_N(a+it)->a+it                                     (20.11)
```

in the weighted `L2` space, with a first relative error `O_w(N^(-1))`.
This proves (20.6).  Chebyshev's bound `E_0(N)=O(N)` then turns (20.7) into
the convergent majorant `sum N^(-1-epsilon)`.  Multiplying (20.6) by
`N|E_0(N)|^2` proves the equivalence of (20.8) and (20.9).

For `N<=x<N+1`, outside the jump endpoint,

```text
E_0(x)=E_0(N)-(x-N).                                       (20.12)
```

The error made by replacing the weighted integral on each unit interval by
its value at `N` is summable.  Therefore (20.9) is equivalent to

```text
integral_2^infinity |E_0(x)|^2x^(-2-epsilon)dx<infinity.    (20.13)
```

This is the claimed Cramer criterion. `QED`

The exact energy increment is

```text
Q_(N+1)-Q_N
 =2E_0(N)Re <P_N,d_N>_(L2(w))
  +E_0(N)^2||d_N||_(L2(w))^2.                              (20.14)
```

After summation,

```text
Q_M
 =2sum_(N<M)E_0(N)Re <P_N,d_N>_(L2(w))

  +sum_(N<M)E_0(N)^2||d_N||_(L2(w))^2.                     (20.15)
```

The second line converges unconditionally by (20.7).  All force is in the
first, coherent signed line.  It has no universal sign.  Discarding it proves
only the subcritical statement (20.7).

### Proposition 20.2 - A single forbidden mode survives every cofinal cut

Fix `rho=beta+i gamma`, `beta>a`, and `K!=0`.  In the planted model put

```text
P_N^rho(s)
 =K sum_(n=2)^(N-1)n^rho[n^(-s)-(n+1)^(-s)].                (20.16)
```

Then, in the Gaussian `L2` space,

```text
N^(s-rho)P_N^rho(s)->K s/(rho-s),                           (20.17)
```

and

```text
||P_N^rho||_(L2(w))^2
 =|K|^2 C_(rho,w)N^(2beta-1-epsilon)[1+o(1)],               (20.18)

C_(rho,w)
 =1/(2pi)integral_R w(t)
   |(a+it)/(rho-a-it)|^2dt>0.                               (20.19)
```

### Proof

Euler--Maclaurin applied to (20.16) gives (20.17); the denominator cannot
vanish because `beta>a`.  Gaussian domination then permits passage to the
norm and proves (20.18). `QED`

In particular, this one-mode model has no bounded cofinal subsequence.  Any
positive regular averaging matrix whose mass eventually leaves every fixed
initial segment also sends (20.18) to infinity.  Conversely, a uniformly
bounded family of such positive averages of a nonnegative sequence forces a
bounded cofinal subsequence.  Thus Cesaro, logarithmic Cesaro and positive
Riesz averaging do not weaken the `liminf` target.  No corresponding claim
is made here for signed averages or for an arbitrary superposition of modes.

For the perturbation of E101.089, the added exponent is `rho=1-c`.  Therefore

```text
Q_N^pert asymp N^(1-2c-epsilon),                            (20.20)
```

while its unweighted quadratic variation still has the convergent scale

```text
sum_N N^(-1-2c-epsilon).                                   (20.21)
```

The critically weighted variation diverges exactly at the same threshold
`epsilon<=1-2c` as the energy.  The cutoff recurrence is therefore exact
bookkeeping, not a new source of cancellation.

## 21. Divisor commutators and the hidden Moebius inverse

Let `H_N=C^{1,...,N}` and define the finite convolution matrices

```text
[T_g f](n)=sum_(d|n)g(n/d)f(d),

T=T_one,

[D f](n)=log(n)f(n).                                       (21.1)
```

The matrix `T` is triangular unipotent.  For every arithmetic kernel `g`,

```text
[D,T_g]=T_(Dg).                                             (21.2)
```

In particular,

```text
C:=[D,T]=T_log=T_Lambda T=T T_Lambda.                      (21.3)
```

Thus the direct solution is already

```text
T_Lambda=C T^(-1).                                         (21.4)
```

There is a more attractive expression which appears not to contain an
inverse.  Put

```text
U=T-I,

L=log T
 =sum_(k>=1)(-1)^(k+1)U^k/k.                               (21.5)
```

The sum is finite.  In the Dirichlet incidence algebra,

```text
L=T_ell,

ell(1)=0,

ell(n)=Lambda(n)/log n,                    n>1.             (21.6)
```

Hence

```text
[D,log T]=T_Lambda.                                        (21.7)
```

### Proposition 21.1 - The logarithmic commutator is the inverse formula

One has exactly

```text
[D,log T]=T^(-1)[D,T]=[D,T]T^(-1).                         (21.8)
```

Moreover,

```text
T^(-1)
 =sum_(j=0)^(floor(log_2 N))(-U)^j
 =T_(mu_Moebius).                                          (21.9)
```

### Proof

Each factor of `U` multiplies an index by at least two, so
`U^j=0` once `2^j>N`.  This proves the finite inverse series in (21.9).
Since `C=[D,U]` commutes with `U`,

```text
[D,U^k]=kU^(k-1)C.                                         (21.10)
```

Insert (21.10) in (21.5):

```text
[D,log T]
 =sum_(j>=0)(-U)^j C
 =T^(-1)C.                                                  (21.11)
```

The convolution coefficients of the inverse series are the classical
Moebius function.  Equations (21.3) and (21.7) give the same identity.
`QED`

The moving coefficient can be retained exactly in this language.  Let

```text
v=([D,log T]-T+I)e_1,

Pi_N=I-e_N 1_N^*,                                          (21.12)
```

where `1_N` is the all-one vector.  Then

```text
v_1=0,

v_n=Lambda(n)-1,                         2<=n<=N,

beta^(N)=Pi_N v.                                            (21.13)
```

Equivalently, if `R_N=|e_N><e_1|`, then

```text
T_(beta^(N))T
 =C-T^2+T-E_0(N)R_N.                                       (21.14)
```

Thus either the oblique balance `Pi_N` or the rank-one term in (21.14)
contains the exact endpoint `E_0(N)`.  Neither representation removes it.

### Proposition 21.2 - Positive commutators do not occur finitely

Every nonzero Hermitian matrix which is itself a commutator expression of
the form

```text
i[D,A],

[D,B]+[D,B]^*,

i^k ad_D^k(A),                                              (21.15)
```

with the displayed expression Hermitian, has trace zero and is indefinite.
In particular, the Hermitian and anti-Hermitian parts of `[D,T]` and
`[D,log T]` are indefinite already at `N=2`.

### Proof

Every finite commutator has trace zero.  A positive or negative semidefinite
Hermitian matrix with trace zero must vanish.  At `N=2`, writing
`ell=log 2`,

```text
[D,T]=[[0,0],[ell,0]],                                     (21.16)
```

whose two Hermitian polarizations have eigenvalues `+ell/2` and `-ell/2`.
`QED`

The remaining universal positivity consists of Gram forms.  Let `K` be an
invertible positive quotient kernel and put

```text
S=T_(beta^(N))T.                                            (21.17)
```

Then

```text
S^*KS=T^*T_beta^*K T_beta T>=0,                            (21.18)
```

but the target is

```text
T_beta^*K T_beta
 =T^(-*)S^*KS T^(-1).                                      (21.19)
```

The block Gram of `K^(1/2)T` and `K^(1/2)S` has identically zero Schur
complement, because `K^(1/2)T` is invertible.  Hence its positivity leaves
no residual coercivity.  Removing the two exterior copies of `T` in
(21.18) is exactly the inverse in (21.19).

In Mellin coordinates that inverse contributes

```text
|zeta(a+it)|^(-2).                                         (21.20)
```

In coefficient coordinates its kernel is

```text
[T^(-*)KT^(-1)]_(k,l)
 =sum_(d<=N/k,e<=N/l)
   mu_Moebius(d)mu_Moebius(e)K(kd,le).                     (21.21)
```

Independent `d,e` destroy the marked ratio `k/l`.  Restricting to common
dilation preserves the ratio but returns exactly the neutral scalar of
Proposition 18.1.

Finally, the perturbations of E101.089 also have positive prime-power
generators

```text
L_eta=T_(lambda_(eta,c)/log),

[D,L_eta]=T_(lambda_(eta,c)).                               (21.22)
```

Therefore positivity of the generator, its support and any argument stable
under a prescribed finite commutator hierarchy cannot distinguish the
forbidden planted mode.  The exact rigidity which does distinguish ordinary
integers is

```text
exp(log T)=T.                                               (21.23)
```

Differentiating (21.23) gives (21.8) because the convolution matrices
commute.  Fixed nilpotent depth is covered by the finite-hierarchy stress
test; depth growing with `N` is the complete Moebius polynomial (21.9).

Thus the divisor commutator reconstructs the Euler product exactly, but its
only sign-free extraction of `Lambda` is the critical inverse already
frozen.  It supplies no new signed inequality for the balanced quotient
energy.

## 22. Commutator literature and final search gate

The exact primary antecedents for Section 21 include

```text
W. Y. Pong,
Applications of differential algebra to algebraic independence of
arithmetic functions:
  https://doi.org/10.4064/aa8112-12-2015

P. Sin, C. Thompson,
The Divisor Matrix, Dirichlet Series and SL(2,Z):
  https://arxiv.org/abs/0712.0837

T. Hilberdink, A. Pushnitski,
Spectral asymptotics for a family of LCM matrices:
  https://arxiv.org/abs/2110.14323

A. Connes, C. Consani,
The Scaling Hamiltonian:
  https://arxiv.org/abs/1910.14368

J.-F. Burnol,
The Explicit Formula and the conductor operator:
  https://arxiv.org/abs/math/9902080                         (22.1)
```

Pong's logarithmic derivation gives, in arithmetic-function language, the
same identities as (21.3) and (21.7).  Sin--Thompson identify the divisor
matrix and its Moebius inverse.  Hilberdink--Pushnitski show that the modulus
of related finite multiplicative incidence matrices leads to LCM spectral
geometry, so passing to the polar modulus is not an untouched replacement
for convolution.  Connes--Consani and Burnol provide nearby operator
commutator and logarithmic-derivative frameworks; they do not supply the
positive quotient estimate required here.

Accordingly, no novelty is claimed for

```text
the logarithmic derivation of Dirichlet convolution;

the identity [D,T]=T_log;

log T and its prime-power coefficients Lambda/log;

the divisor matrix or its Moebius inverse;

polar, LCM or conductor-commutator terminology.             (22.2)
```

Sections 14--21 impose the following final gate on a successor to E101.090.
It must

```text
use exact ordinary-integer arithmetic not shared by the E101.089
perturbations;

retain the prime--integer cross cancellation and beta_N^(N);

produce a signed upper bound before applying an absolute value;

not be an invertible transform, positive average or scalar completion of
Q_N;

not remove a divisor factor through T^(-1), log T, a Schur complement or an
equivalent 1/zeta multiplier;

reject a planted mode N^rho, Re rho>1/2, at the new arithmetic identity
itself.                                                       (22.3)
```

A proposal which reaches only another norm equivalent to Cramer, another
positive Gram of a divisor-smoothed vector, or another homogeneous
completion has failed this gate.  The remaining admissible classes must add
an arithmetic relation not contained in the one-variable renewal algebra,
or return to the Xi-specific Gamma--Euler discriminant.  This statement is a
search restriction, not a claim that either class has been solved.

## 23. Binomial carries return exactly to divisor incidence

The first candidate tested against the gate in Section 22 is the complete
finite carry system.  It looks genuinely two-variable and it has many more
rows than columns.  The exact calculation below shows that this redundancy
does not add an arithmetic relation: every carry row is a linear combination
of the divisor rows already frozen in Section 21.

For `N>=3`, put

```text
R_N={(m,n) in positive integers^2:m+n<=N},

c_(m,n)(d)
 =floor((m+n)/d)-floor(m/d)-floor(n/d) in {0,1},

(C_N v)(m,n)=sum_(d<=N)v(d)c_(m,n)(d).             (23.1)
```

The simplex `m+n<=N` is essential.  If both coordinates range independently
through `N`, the source is needed through `2N`; truncating the columns at
`N` then introduces a second tail and destroys the exact arithmetic formula.

Let `T` be divisor summation, `P` ordinary summation and `B` the additive
coboundary:

```text
(Tv)(k)=sum_(d|k)v(d),

(Pf)(x)=sum_(k<=x)f(k),

(BF)(m,n)=F(m+n)-F(m)-F(n).                        (23.2)
```

### Proposition 23.1 - Exact carry factorization

On `R_N`, one has

```text
C_N=BPT.                                            (23.3)
```

More strongly,

```text
c_(m,n)(d)
 =sum_(j=1)^n[1_(d|m+j)-1_(d|j)],                  (23.4)

c_(1,k-1)(d)=1_(d|k),                 d>=2.         (23.5)
```

Thus every row of `C_N` is a signed sum of the rows `(1,k-1)`, and those
rows are exactly the divisor-incidence matrix.

### Proof

For every `x<=N`, interchange the finite sums:

```text
sum_(d<=N)v(d)floor(x/d)
 =sum_(k<=x)sum_(d|k)v(d)
 =(PTv)(x).                                         (23.6)
```

Taking its additive coboundary proves (23.3).  On the other hand,

```text
floor((m+n)/d)-floor(m/d)
 =sum_(j=1)^n 1_(d|m+j),                            (23.7)

floor(n/d)=sum_(j=1)^n1_(d|j),                     (23.8)
```

which proves (23.4).  Setting `m=1,n=k-1` gives

```text
floor(k/d)-floor((k-1)/d)=1_(d|k)                  (23.9)
```

for `d>=2`, proving (23.5). `QED`

Since `c_(m,n)(1)=0`,

```text
ker C_N=span{e_1}.                                  (23.10)
```

Indeed, (23.5) and triangular divisor inversion show that `C_Nv=0` and
`v(1)=0` imply `v=0`.  The inverse of the distinguished submatrix (23.5) is
the Moebius matrix.  For example, the elementary Frobenius estimate gives

```text
sigma_min(C_N restricted to v(1)=0)
 >=||T_N^(-1)||_2^(-1)
 >> (N log N)^(-1/2).                               (23.11)
```

The additional rows can improve ordinary finite-dimensional singular values.
Equation (23.3) therefore is not, by itself, an unweighted singular-value
no-go.  Its force is arithmetic: the apparent two-variable data contain no
relation beyond signed recombination of `Tv`.

## 24. Exact arithmetic carry source and the critical frame wall

Put

```text
u(1)=-1,

u(d)=Lambda(d)-1,                         d>=2.     (24.1)
```

Changing `u(1)` to zero does not change `C_Nu`.  Since

```text
u*1=log-tau,                                       (24.2)
```

Proposition 23.1 gives the following exact source evaluation.

### Proposition 24.1 - Binomial--divisor identity

Let

```text
D(x)=sum_(k<=x)tau(k).                              (24.3)
```

Then

```text
R_u(m,n):=(C_Nu)(m,n)

 =log binom(m+n,m)-[D(m+n)-D(m)-D(n)].             (24.4)
```

If

```text
D(x)=x log x+(2 gamma_E-1)x+Delta_D(x),            (24.5)
```

then, uniformly on `R_N`,

```text
R_u(m,n)
 =-Delta_D(m+n)+Delta_D(m)+Delta_D(n)
  +(1/2)log[(m+n)/(2 pi m n)]
  +O(1/m+1/n).                                     (24.6)
```

In particular, the elementary divisor bound gives

```text
|R_u(m,n)|<<sqrt(m+n).                              (24.7)
```

### Proof

Equation (24.2) gives

```text
P(Tu)(x)
 =sum_(k<=x)log k-D(x)
 =log Gamma(x+1)-D(x).                             (24.8)
```

Its additive coboundary is (24.4).  Substitute (24.5) and Stirling's
formula in (24.4).  The entropy terms cancel exactly, leaving (24.6).
Equation (24.7) follows. `QED`

The identity with only `Lambda` is the classical factorial identity

```text
sum_d Lambda(d)c_(m,n)(d)=log binom(m+n,m).         (24.9)
```

Prime-power by prime-power, (24.9) is Kummer's carry formula for the
valuation of a binomial coefficient.  The subtraction by one merely replaces
the same carry sum by the additive defect of `D(x)`.

### The moving endpoint

Return to the vector of (17.12):

```text
beta^(N)=u 1_[2,N]-E_0(N)e_N.                      (24.10)
```

For `m+n<N`, its carry is `R_u(m,n)`.  On the top antidiagonal,

```text
(C_N beta^(N))(m,N-m)=R_u(m,N-m)-E_0(N),           (24.11)
```

because `c_(m,N-m)(N)=1`.  Hence the carry system retains the moving
coefficient exactly; it does not make that coefficient small.

For `epsilon>0`, define

```text
Car_(epsilon,N)(v)
 =sum_((m,n) in R_N)(m+n)^(-3-epsilon)
   |(C_Nv)(m,n)|^2.                                (24.12)
```

### Proposition 24.2 - Unconditional carry energy

For every `epsilon>0`,

```text
sup_N Car_(epsilon,N)(beta^(N))<infinity.           (24.13)
```

### Proof

At level `k=m+n<N` there are `k-1` rows.  Equations (24.6)--(24.7) give

```text
sum_(m+n=k)k^(-3-epsilon)|R_u(m,n)|^2
 <<k^(-1-epsilon).                                 (24.14)
```

These bounds are summable.  Equations (24.7), (24.11) and Chebyshev's
`E_0(N)=O(N)` bound give for the terminal level

```text
sum_(m+n=N)N^(-3-epsilon)
 |R_u(m,n)-E_0(N)|^2
 <<N^(-epsilon).                                   (24.15)
```

This proves (24.13). `QED`

The tempting bridge would be a constant independent of `N` such that

```text
Q_N(v)<=C_epsilon Car_(epsilon,N)(v)                (24.16)
```

on the balanced coefficient space.  Applied only to `beta^(N)`, the family
(24.16) for every `epsilon>0` is already equivalent to the Cramer bound and
hence to RH.  The right side is uniformly bounded by Proposition 24.2 and is
bounded below away from zero by the fixed row `(1,1)`.  Thus (24.16) is not
an intermediate estimate extracted from the divisor problem.

The operator identity locates the complete inverse.  Write

```text
L=BP,

W_epsilon(m,n)=(m+n)^(-3-epsilon),

G_(epsilon,N)=C_N^*W_epsilon C_N
             =T^*L^*W_epsilon LT.                 (24.17)
```

If `K_N` is the quotient kernel in (3.5), then the universal domination

```text
K_N<=C_epsilon G_(epsilon,N)                       (24.18)
```

is equivalent, after conjugating by the finite divisor inverse, to

```text
T^(-*)K_NT^(-1)
 <=C_epsilon L^*W_epsilon L.                       (24.19)
```

Its left side has entries

```text
[T^(-*)K_NT^(-1)]_(k,l)
 =sum_(d,e)mu_Moebius(d)mu_Moebius(e)K_N(kd,le),   (24.20)
```

with the finite support restrictions understood.  In Mellin coordinates it
contains the multiplier

```text
|zeta(a+it)|^(-2).                                 (24.21)
```

Redundant carry rows can improve an ordinary Euclidean condition number, but
the critical quotient frame still asks for exactly the divisor inverse.
Allowing an arbitrary dense positive row weight does not help: a left inverse
of `C_N` can manufacture equality with `K_N`, but that weight already contains
`T^(-1)` and has no uniform source estimate.

### Perturbative discrimination does not remove the zero wall

The carry norm is not completely blind.  For the E101.089 perturbation

```text
Lambda_(eta,c)(d)=Lambda(d)(1+eta d^(-c)),

0<c<1/2,                                            (24.22)
```

take `m,n` in fixed positive proportions of `k=m+n`.  Every integer

```text
max(m,n)<d<=k                                      (24.23)
```

has carry one.  The prime number theorem therefore gives a perturbative
contribution of order `k^(1-c)`.  There are a positive proportion of `k`
such rows, so (24.12) contains

```text
sum_k k^(-2c-epsilon),                             (24.24)
```

which diverges when `epsilon<=1-2c`.  Thus the proposed carry condition
correctly rejects the prime-tower falsifiers of E101.089.

It does not reject a zero of the actual zeta function outside the critical
line.  The exact source (24.4) and its unconditional bound (24.13) remain
valid, while E101.087 and the planted-mode calculation (20.18) make `Q_N`
grow at the corresponding geometric rate.  Therefore (24.16) fails in that
world.  Proving (24.16) would exclude the zero itself; this is the full
force-bearing step.

## 25. Carry literature, novelty boundary and decision

The exact classical antecedents include

```text
E. E. Kummer,
Ueber die Ergaenzungssaetze zu den allgemeinen Reciprocitaetsgesetzen:
  https://eudml.org/doc/147500

J. C. Lagarias, H. Mehta,
Products of Binomial Coefficients and Unreduced Farey Fractions:
  https://arxiv.org/abs/1409.4145

J. C. Lagarias, H. Mehta,
Products of Farey Fractions:
  https://arxiv.org/abs/1503.00199

J. M. Holte,
Carries, Combinatorics, and an Amazing Matrix:
  https://doi.org/10.1080/00029890.1997.11990612

P. Diaconis, J. Fulman,
Carries, Shuffling, and an Amazing Matrix:
  https://doi.org/10.4169/000298909X474864

A. Aistleitner, I. Berkes, K. Seip, M. Weber,
Convergence of series of dilated functions and spectral norms of GCD
matrices:
  https://doi.org/10.4064/aa168-3-2

T. Hilberdink, A. Pushnitski,
Spectral asymptotics for a family of LCM matrices:
  https://arxiv.org/abs/2110.14323

L. Baez-Duarte,
A strengthening of the Nyman--Beurling criterion for the Riemann
hypothesis:
  https://eudml.org/doc/252348

F. Alouges, S. Darses, E. Hillion,
Polynomial approximations in a generalized Nyman--Beurling criterion:
  https://arxiv.org/abs/2006.02953                     (25.1)
```

Kummer contains the prime-power carry mechanism behind (24.9).  The
Lagarias--Mehta work connects binomial products, carries, Chebyshev functions
and Farey products; the reduced Farey channel acquires its RH-sensitive
remainder only through Moebius inversion.  Holte and Diaconis--Fulman are
primary matrix antecedents for carry operators.  GCD/LCM Gram positivity and
spectral structure are already classical in the cited matrix literature.
The Nyman--Beurling antecedents similarly locate the hard step in signed
coefficient control, not in positivity of the ambient Gram.

No novelty is claimed for

```text
the Lambda--carry--binomial identity;

its multinomial or prime-power versions;

carry transition matrices or their positive Grams;

GCD/LCM covariance obtained by averaging residues;

the additive divisor-error representation;

positive cross-base averaging.                            (25.2)
```

The exact factorization (23.3)--(23.5) decides the candidate inside this
program.  It violates the Section 22 successor gate: its apparently
two-variable arithmetic is a signed postcomposition of the same divisor
incidence `T`.  Its only critical frame statement is (24.16), and
(24.19)--(24.21) place the full Moebius inverse inside that statement.

Accordingly, binomial carries are frozen as a closure route.  They remain a
useful falsifier because they separate the E101.089 prime-tower perturbations
from ordinary integers, but they do not supply the Xi-specific signed
inequality needed for Omega7.  No further carry, multinomial, residue-average
or carry-Gram variant is admissible unless it first exhibits an exact signed
identity which is not a postcomposition of `T` and rejects the planted
off-line zeta mode before a divisor inverse is invoked.
