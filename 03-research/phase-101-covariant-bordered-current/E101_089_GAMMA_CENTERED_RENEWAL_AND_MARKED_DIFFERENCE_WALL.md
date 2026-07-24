# E101.089 - Gamma-centered renewal and the marked-difference wall

## 1. Decision

The divisor-renewal branch of E101.087 is closed in its linear form and in
every perturbative form which uses only positivity plus relative
coefficientwise accuracy of a prescribed finite Selberg hierarchy.

There is an exact normalization which is useful.  Adding Euler's constant to
the centered prime error turns its divisor sum into a completely explicit
source of logarithmic size.  Nevertheless, recovering the prime error from
that source is multiplication by `1/zeta` in Mellin space.  The source does
not vanish to the full multiplicity of a zero of `zeta`; division leaves a
simple pole whose residue records that multiplicity.

Three stronger no-go results hold:

```text
the canonical divisor carre-du-champ is exactly |zeta|^2 and has no
new positive gap;

Selberg's positive quadratic identity remembers u+v, while the endpoint
Gaussian energy requires u-v;

positivity, exact prime-power support and relative o(1) accuracy of any
prescribed finite positive Selberg hierarchy remain compatible with a
positive forbidden abscissa.                                               (1.1)
```

The only surviving design requirement is therefore nonperturbative and
two-variable:

```text
MARKED-DIFFERENCE-ARITHMETIC-RIGIDITY:

use exact ordinary-integer arithmetic while retaining the marked
difference u-v before every product or divisor pushforward.               (1.2)
```

The tensor product of two ordinary renewal identities does not meet (1.2):
on the Hermitian slice its symbol is merely `|zeta|^2`, which loses the
Hardy inner factor.  A future identity must couple the two marked variables
nonfactorizably.

This document does not prove (1.2), RH or Omega7.  Its purpose is to prevent
the classical renewal and Selberg mechanisms from being reintroduced under
new notation and to state exactly what information they discard.

## 2. Arithmetic and convolution conventions

Let

```text
Psi(x)=sum_(n<=x)Lambda(n),

E_0(x)=Psi(x)-x+1,

N=sum_(n>=1)delta_(log n),

L=sum_(n>=2)Lambda(n)delta_(log n).                           (2.1)
```

On arithmetic functions, `*` denotes Dirichlet convolution.  On the
logarithmic semigroup it denotes the corresponding additive convolution.
Let

```text
D f(n)=log(n)f(n).                                           (2.2)
```

Then `D` is a convolution derivation:

```text
D(f*g)=Df*g+f*Dg.                                            (2.3)
```

The fundamental identity is

```text
Lambda*1=log,

L*N=yN.                                                      (2.4)
```

For `x>=1`, put

```text
m=floor(x),
theta=x-m,
H_m=sum_(n=1)^m 1/n.                                        (2.5)
```

Euler's constant is denoted by `gamma_E`.

## 3. The exact logarithmic source

Define

```text
A_gamma(y)=E_0(exp y)+gamma_E.                               (3.1)
```

### Theorem 3.1 - Gamma-centered divisor source

For `x=exp y` and `m=floor(x)`, one has the exact identity

```text
sum_(n<=x) A_gamma(log(x/n))
 =q_gamma(y),                                                (3.2)

q_gamma(y)
 =log(m!)-xH_m+m+gamma_E m.                                  (3.3)
```

Moreover,

```text
q_gamma(y)
 =(1/2-theta)log m-gamma_E theta
  +1/2 log(2pi)-1/2+O(1/m),                                 (3.4)

q_gamma(y)=O(1+y).                                           (3.5)
```

### Proof

Coefficient comparison in (2.4) gives

```text
sum_(d|r)Lambda(d)=log r.                                    (3.6)
```

Therefore

```text
sum_(n<=x)Psi(x/n)
 =sum_(r<=m)sum_(d|r)Lambda(d)
 =sum_(r<=m)log r
 =log(m!).                                                   (3.7)
```

Also

```text
sum_(n<=x)x/n=xH_m,

sum_(n<=x)(1+gamma_E)=(1+gamma_E)m.                          (3.8)
```

Equations (3.1), (3.7) and (3.8) prove (3.2)--(3.3).

Use

```text
H_m=log m+gamma_E+1/(2m)+O(1/m^2),

log(m!)=m log m-m+1/2 log(2pi m)+O(1/m).                     (3.9)
```

Substitution of `x=m+theta` gives (3.4), hence (3.5). `QED`

The cancellation of the term of size `x` is exact.  It is not a new prime
identity: it is (3.6), the harmonic-number expansion and Stirling's formula.
Its useful content here is the correct local normalization by `gamma_E`.

## 4. Weighted causal renewal

For `a>0`, define

```text
f_a(y)=exp(-ay)A_gamma(y),

r_a(y)=exp(-ay)q_gamma(y),                                   (4.1)

(T_a f)(y)
 =sum_(n<=exp y)n^(-a)f(y-log n).                            (4.2)
```

Every summand in `T_a f_a` contains

```text
n^(-a)exp[-a(y-log n)]=exp(-ay).                             (4.3)
```

Thus Theorem 3.1 gives

```text
T_a f_a=r_a,

r_a in L^2(0,infinity) for every a>0.                        (4.4)
```

Adding `gamma_E` to `E_0` changes the endpoint-renormalized current of
E101.087 by the convolution of an exponentially decreasing function with a
fixed Gaussian derivative.  That correction lies in every positively
damped `L^2` space.  Consequently the target energy is finite for `E_0` if
and only if it is finite for `E_0+gamma_E`.

On `L^2(0,V)`, the exact adjoint is

```text
(T_(a,V)^*g)(x)
 =sum_(n<=exp(V-x))n^(-a)g(x+log n).                         (4.5)
```

This formula is triangular, but triangularity does not provide a stable
inverse at the critical weights.

## 5. Mellin symbol and the exact inverse wall

For a finite translation section on the whole line, put

```text
T_(a,M)=sum_(n<=M)n^(-a)tau_(log n),

Z_M(a+it)=sum_(n<=M)n^(-a-it).                               (5.1)
```

Then

```text
Fourier[T_(a,M)f](t)=Z_M(a+it)Fourier[f](t).                 (5.2)
```

In the Gaussian norm of E101.087,

```text
||f||_(G_a)^2
 =1/(2pi) integral_R W_(a,T,tau)(t)|Fourier[f](t)|^2dt,      (5.3)

||T_(a,M)f||_(G_a)^2
 =1/(2pi) integral_R W_(a,T,tau)(t)
   |Z_M(a+it)|^2|Fourier[f](t)|^2dt.                         (5.4)
```

For `a>1`, Euler's product gives the safe two-sided bound

```text
zeta(2a)/zeta(a)<=|zeta(a+it)|<=zeta(a).                     (5.5)
```

The lower constant tends to zero at the pole boundary `a=1`; (5.5) does not
enter the critical strip.

### Proposition 5.1 - Exact source transform

Initially for `Re s>1`,

```text
L[A_gamma](s)
 =1/s[gamma_E-1/(s-1)-zeta'(s)/zeta(s)],                    (5.6)

L[q_gamma](s)
 =zeta(s)L[A_gamma](s)
 =1/s[gamma_E zeta(s)-zeta(s)/(s-1)-zeta'(s)].               (5.7)
```

### Proof

Stieltjes integration by parts gives

```text
integral_1^infinity Psi(x)x^(-s-1)dx
 =-zeta'(s)/[s zeta(s)].                                    (5.8)
```

The Mellin integrals of `x`, `1` and `gamma_E` give the other
terms in (5.6).  Equation (5.7) follows either from (3.2) or by direct
multiplication. `QED`

If `rho` is a nontrivial zero of multiplicity `m_rho`, then

```text
ord_rho L[q_gamma]=m_rho-1,                                 (5.9)

Res_(s=rho) L[q_gamma](s)/zeta(s)=-m_rho/rho.                (5.10)
```

Thus the elementary source does not contain a hidden zero which cancels the
divisor zero.  It loses exactly one order, and division restores a simple
pole carrying the full multiplicity.

The special, non-Moebius formulation of the missing theorem is the Hardy
range statement

```text
L[q_gamma] belongs to zeta H^2(Re s>a)
for every a>1/2.                                             (5.11)
```

Here `zeta H^2(Re s>a)` means that there is an `h_a in H^2(Re s>a)` with
`h_a(1)=0` such that the pole of `zeta h_a` at `1` is removable and
`L[q_gamma]=zeta h_a` holomorphically.  With this definition, (5.11) is
equivalent to RH.  A
continued boundary quotient is insufficient: it may have a finite boundary
integral while retaining a pole inside the half-plane.

## 6. The canonical carre-du-champ adds no gap

Let `w_n=n^(-a)`, let `u_n` be vectors in a Hilbert space and put
`W=sum_(n<=M)w_n`.  Direct expansion gives

```text
|sum_n w_nu_n|^2
 =W sum_n w_n|u_n|^2
  -1/2 sum_(m,n)w_mw_n|u_m-u_n|^2.                          (6.1)
```

For `u_n=tau_(log n)u`, (6.1) is exactly (5.4).  The apparent positive
dissipation is the complement of the divisor-polynomial modulus; it does
not control the input from the output.

The Bohr mean is

```text
lim_(R->infinity)1/(2R) integral_(-R)^R |Z_M(a+it)|^2dt
 =sum_(n<=M)n^(-2a).                                        (6.2)
```

When `1/2<a<1`, the right side stays bounded as `M` grows, while

```text
Z_M(a)^2 asymp M^(2-2a).                                    (6.3)
```

Hence no uniform fractional spectral gap relative to total mass can follow
from (6.1).  Define the closed continued multiplier

```text
Fourier[Zeta_a f](t)=zeta(a+it)Fourier[f](t),

Dom(Zeta_a)={f:zeta(a+i.)Fourier[f] belongs to L2(Wdt)}.      (6.4)
```

Bohr--Courant density, and also Voronin universality, imply

```text
essinf_(t in R)|zeta(a+it)|=0,

inf_(0!=f in Dom(Zeta_a))
 ||Zeta_a f||_(G_a)/||f||_(G_a)=0.                          (6.4a)
```

Frequency packets near small values of `zeta` prove the second assertion.
No identification of `Zeta_a` with the causal operator (4.2) is made below
`a=1`; such an identification would itself require a boundary theorem.

For `a>1`, the positive prime-power Levy measure

```text
dPi_a(h)=sum_(p,k>=1)p^(-ak)/k delta_(k log p)(dh)            (6.5)
```

does yield the normalized convolution semigroup with symbol

```text
[zeta(a+it)/zeta(a)]^r.                                     (6.6)
```

Its exact energy identity is dissipative:

```text
||f||_(G_a)^2-||P_(a,1)f||_(G_a)^2
 =integral_0^1 integral
  ||tau_hP_(a,r)f-P_(a,r)f||_(G_a)^2 dPi_a(h)dr.             (6.7)
```

The measure in (6.5) has total mass `log zeta(a)` only for `a>1`.
Prime-power positivity therefore reproduces the safe Euler-product region
and supplies contraction, not inverse coercivity.

## 7. Exact balanced distance identity

The endpoint energy has a useful finite geometric form, but it also exposes
the cancellation wall.  Let

```text
P_X=dPsi restricted to [1,X],

Q_X=dx restricted to [1,X],

E=E_0(X),

E_+=max(E,0),

E_-=max(-E,0),                                              (7.1)

P_X^sharp=P_X+E_- delta_X,

Q_X^sharp=Q_X+E_+ delta_X.                                  (7.2)
```

The two positive measures in (7.2) have equal mass and

```text
P_X^sharp-Q_X^sharp=dPsi-dx-E delta_X.                       (7.3)
```

For `s=a+it`, define the Hilbert-space feature

```text
Phi(x)(t)=1/sqrt(2pi) H(t-i epsilon/2)x^(-a-it),

a=(1+epsilon)/2.                                            (7.4)
```

For positive measures `A,B`, put

```text
Dist(A,B)=double_integral
 ||Phi(x)-Phi(y)||^2dA(x)dB(y).                              (7.5)
```

### Proposition 7.1 - Event--continuum distance square

The finite energy of E101.087 is exactly

```text
1/(2pi) integral_R |H(t-i epsilon/2)|^2|sM_X(s)|^2dt

 =Dist(P_X^sharp,Q_X^sharp)
  -1/2 Dist(P_X^sharp,P_X^sharp)
  -1/2 Dist(Q_X^sharp,Q_X^sharp).                            (7.6)
```

### Proof

For equal-mass measures `A,B`, expansion of the three squared distances
gives

```text
||integral Phi d(A-B)||^2
 =Dist(A,B)-1/2Dist(A,A)-1/2Dist(B,B).                       (7.7)
```

By (7.3), the vector on the left of (7.7) is the Mellin vector
`D_X(s)-X^(-s)E=sM_X(s)`.  Plancherel proves (7.6). `QED`

The pointwise kernel in (7.5) is

```text
C_(epsilon,tau)[
 x^(-2a)+y^(-2a)
 -2(xy)^(-a)exp(-log^2(x/y)/(8tau))
   cos(T log(x/y))],                                        (7.8)

C_(epsilon,tau)
 =exp(tau epsilon^2/2)/[2sqrt(2pi tau)].                     (7.9)
```

All three terms in (7.6) are positive, but the target is their signed
cancellation.  Dropping either self-energy gives an upper bound of the wrong
scale.  Equation (7.6) is an exact coordinate, not a positivity proof.

## 8. Selberg remembers the sum and loses the difference

Apply `D` to `Lambda*1=log`.  Since `D1=log=Lambda*1`,

```text
A_2=D Lambda+Lambda*Lambda>=0,

A_2*1=log^2.                                                (8.1)
```

This is the first positive Selberg closure.  In a pair of logarithmic
variables, convolution sends

```text
(u,v) -> u+v.                                                (8.2)
```

The Gaussian covariance in (7.8) depends instead on

```text
(u,v) -> u-v.                                                (8.3)
```

The loss is strict.  For any `r>0`, the positive pair measures

```text
delta_(r/2,r/2),

1/2 delta_(0,r)+1/2 delta_(r,0)                             (8.4)
```

have the same pushforward under (8.2).  After removing the common weight
`exp(-ar)` attached to their fixed sum, their normalized `T=0` Gaussian
difference moments are respectively

```text
1,

exp[-r^2/(8tau)].                                            (8.5)
```

Equivalently, Selberg controls the holomorphic square `L(s)^2`; the
endpoint target contains the Hermitian square `L(s)L(conj s)`.  No estimate
formed after the pushforward (8.2) can reconstruct (8.5) without additional
marked information.

## 9. Exact renewal has a singleton fiber

Let

```text
L_tilde=sum_(n>=2)ell(n)delta_(log n)                        (9.1)
```

and suppose

```text
L_tilde*N=yN.                                                (9.2)
```

At `log m`, (9.2) says

```text
sum_(d|m)ell(d)=log m.                                       (9.3)
```

For `m=p`, one gets `ell(p)=log p`.  Induction on `p^k` gives
`ell(p^k)=log p`.  If `m` has at least two prime factors, the already fixed
prime-power divisors sum to `log m`; strong induction has already made every
proper mixed divisor coefficient zero, so `ell(m)=0`.  Therefore

```text
L_tilde=L.                                                   (9.4)
```

No positivity or support assumption was used.  Exact renewal supplies no
family on which a geometric cone estimate can be proved; an estimate on
this one point is an estimate on `Lambda` itself.

## 10. Prime-tower falsifier for the listed nonrenewal restrictions

Positivity and exact prime-power geometry still do not distinguish the
critical abscissa.  Fix

```text
delta=3/4,

beta=7/8,

F(x)=x-cx^beta                                              (10.1)
```

with `c>0` and a sufficiently large starting point.  Recursively choose

```text
X_(j+1)=X_j+X_j^delta.                                      (10.2)
```

The prime number theorem in intervals of exponent greater than `7/12`
gives

```text
r_j=pi(X_(j+1))-pi(X_j)
    ~X_j^delta/log X_j.                                     (10.3)
```

Put

```text
M_j=F(X_(j+1))-F(X_j),

w(p)=M_j/r_j for X_j<p<=X_(j+1),                            (10.4)

L_w=sum_p sum_(k>=1)w(p)delta_(k log p).                    (10.5)
```

Assign any fixed positive weights to the finitely many primes at most
`X_0`; they contribute only `O(1)` to the block asymptotics.

Then

```text
w(p)>0,

w(p)/log p ->1.                                             (10.6)
```

The first-prime contributions telescope to `F+O(1)` at every block endpoint.
Within a block their discrepancy is `O(x^delta)`.  The higher powers
contribute `O(sqrt(x)log x)`.  Hence

```text
Psi_w(x)=sum_(p^k<=x)w(p)
        =x-cx^(7/8)+O(x^(3/4)).                             (10.7)
```

This model has all of the following properties:

```text
L_w>=0;

support(L_w) subset {log(p^k)};

one weight w(p) is repeated on the whole p-tower;

w(p) asymp log p;

Psi_w is nondecreasing and is constant between events;

sum_(p,k)w(p)^2/p^(k(1+eta))<infinity for every eta>0.       (10.8)
```

Nevertheless,

```text
exp(-y/2)[Psi_w(exp y)-exp y]
 =-c exp(3y/8)(1+o(1)),                                     (10.9)
```

so its Gaussian energy has positive damping abscissa `3/4`.

The model fails exactly (9.2).  Therefore positivity, prime-power support,
tower coherence, correct asymptotic event weights and the local diagonal do
not replace coefficientwise divisor renewal.

## 11. A perturbative falsifier for every finite Selberg hierarchy

Fix `0<c<1/2` and `eta>0`, and define

```text
lambda_(eta,c)(n)=Lambda(n)[1+eta n^(-c)].                  (11.1)
```

It is positive and is supported on the ordinary prime powers.  Its divisor
defect is

```text
(lambda_(eta,c)*1)(n)-log n=eta r_c(n),                      (11.2)

r_c(n)=sum_(d|n)Lambda(d)d^(-c).                             (11.3)
```

If `n=product_p p^(k_p)`, then

```text
r_c(n)
 <=sum_(p|n) log p/(p^c-1)
 <<_c (log n)^(1-c).                                        (11.4)
```

For completeness, split the primes in (11.4) at `p=log n`.  Chebyshev's
bound and partial summation give

```text
sum_(p<=log n)log p/p^c <<_c (log n)^(1-c).                  (11.5)
```

For `p>log n`, use `p^(-c)<=(log n)^(-c)` and
`sum_(p|n)log p<=log n`.  This proves (11.4).  Primorials show that its
power is sharp.

Thus

```text
[(lambda_(eta,c)*1)(n)-log n]/log n
 =O_c((log n)^(-c))->0.                                     (11.6)
```

On the other hand, the prime number theorem and partial summation give

```text
sum_(n<=x)Lambda(n)n^(-c)
 ~x^(1-c)/(1-c).                                             (11.7)
```

The normalized error therefore contains

```text
eta/(1-c) exp[(1/2-c)y],                                    (11.8)
```

and forces positive damping abscissa at least `1-2c`.  Equality is not
asserted because the original `Lambda` error could have a larger abscissa.

This falsifier can be made horizontally symmetric.  For `gamma!=0` and
small enough `eta`, put

```text
lambda(n)=Lambda(n){1+eta[n^(-c)+n^(-(1-c))]
                    cos(gamma log n+phi)}.                  (11.9)
```

It remains positive and introduces the four Mellin singularities

```text
1-c+i gamma,
1-c-i gamma,
c+i gamma,
c-i gamma.                                                  (11.10)
```

Its divisor defect has the same upper scale as (11.4).

### Theorem 11.1 - Finite positive hierarchies are perturbatively blind

Define

```text
A_1^lambda=lambda_(eta,c),

A_(k+1)^lambda=D A_k^lambda+A_k^lambda*lambda_(eta,c).      (11.11)
```

Every `A_k^lambda` is nonnegative.  If

```text
R_k=A_k^lambda*1-log^k,                                     (11.12)
```

then, for every fixed `k`,

```text
R_k(n)<<_(eta,c,k)(log n)^(k-c).                            (11.13)
```

### Proof

The case `k=1` is (11.2)--(11.4).  From the derivation law (2.3),

```text
R_(k+1)=D R_k+eta A_k^lambda*r_c.                           (11.14)
```

Assume (11.13) through level `k`.  Strong induction, positivity and
(11.14) at all previous levels give

```text
A_k^lambda*1=O_(eta,c,k)(log n)^k.                          (11.15)
```

Using (11.4),

```text
(A_k^lambda*r_c)(n)
 <=C_c(log n)^(1-c)sum_(d|n)A_k^lambda(d)
 <<(log n)^(k+1-c).                                         (11.16)
```

The first term in (11.14) has the same bound.  This proves (11.13) by
induction. `QED`

Consequently every prescribed finite part of the positive Selberg hierarchy
can hold with relative coefficientwise error `O((log n)^(-c))` while the
forbidden mode (11.8) survives.  This rules out arguments whose only inputs
are positivity and that relative accuracy.  It does not rule out every
possible use of the exact identities or of additional marked remainder
structure.

## 12. Why the naive bivariate repair also fails

One may try to retain both variables by tensoring (2.4):

```text
(L tensor L)*(N tensor N)=(yN) tensor (yN).                 (12.1)
```

This identity is exact but factorized.  In two Mellin variables its divisor
symbol is

```text
zeta(s)zeta(t).                                              (12.2)
```

On the Hermitian slice `t=conj(s)`, it becomes

```text
|zeta(s)|^2.                                                 (12.3)
```

A modulus on a fixed boundary line `Re s=a` does not determine the Hardy
inner factor in that half-plane.  Multiplying by a Blaschke factor preserves
the boundary modulus while inserting an interior zero.  Therefore
(12.1)--(12.3) cannot exclude an off-line zero without an
additional range or analyticity theorem, and that theorem is again the
force-bearing step.

The required bivariate identity must therefore be more than two copies of
renewal.  It must couple the marked variables before factorization and
retain enough source information to distinguish an interior Hardy zero.

## 13. Literature and nonduplication gate

The following antecedents govern this branch:

```text
A. Selberg, An Elementary Proof of the Prime-Number Theorem:
  https://www.jstor.org/stable/1969455

G. H. Hardy, M. Riesz, The General Theory of Dirichlet's Series:
  https://archive.org/details/cu31924060184441

H. Bohr, R. Courant, Neue Anwendungen der Theorie der Diophantischen
Approximationen auf die Riemannsche Zetafunktion:
  https://doi.org/10.1515/crll.1914.144.249

S. M. Voronin, Theorem on the universality of the Riemann zeta-function:
  https://doi.org/10.1070/IM1975v009n03ABEH001485

N. Levinson, A motivated account of an elementary proof of the prime
number theorem:
  https://doi.org/10.1080/00029890.1969.12000182

M. N. Huxley, On the difference between consecutive primes:
  https://doi.org/10.1007/BF01418933

L. Guth, J. Maynard, New large value estimates for Dirichlet polynomials:
  https://arxiv.org/abs/2405.20552

H. G. Diamond, H. L. Montgomery, U. M. A. Vorhauer,
Beurling primes with large oscillation:
  https://doi.org/10.1007/s00208-005-0638-2

E. Kowalski, P. Michel, A lower bound for the rank of J_0(q):
  https://doi.org/10.4064/aa-94-4-303-343

H. Iwata, On an arithmetical Volterra equation:
  https://arxiv.org/abs/2205.06001

H. Iwata, An arithmetic Volterra equation and the Riemann hypothesis:
  https://arxiv.org/abs/2601.11052

R. Lyons, Distance covariance in metric spaces:
  https://arxiv.org/abs/1106.5758                            (13.1)
```

No novelty is claimed for `Lambda*1=log`, the Selberg identity, arithmetic
Volterra inversion, divisor-polynomial symbols, universality, Hardy range
criteria, the gamma-centered source, higher von Mangoldt functions,
convolution versus autocorrelation, Hilbert-space distance polarization or
PNT mean-square criteria.  Levinson contains the normalization of Section 3;
Kowalski--Michel records the undeformed higher-von-Mangoldt hierarchy; and
Lyons is an antecedent for the abstract distance geometry of Section 7.
Guth--Maynard improve the short-interval exponent used in Section 10, while
the older Huxley exponent already suffices for `delta=3/4`.

The prime-tower stress test (10.1)--(10.9) and the perturbed finite-hierarchy
stress test (11.1)--(11.16) are used here as program-specific closure tests.
The Beurling-prime construction is a nearby general-system antecedent for
positive prime models with large oscillation.  No global priority claim is
made for the ordinary-prime weighted stress test.

## 14. Stop rule and status

Freeze all of the following:

```text
termwise inversion of T_a;

universal coercivity of the divisor convolution below a=1;

the prime-power Levy semigroup as an inverse estimate;

the first Selberg square as a Hermitian covariance identity;

any argument using only positivity and relative coefficientwise o(1)
accuracy of a fixed finite higher Selberg hierarchy;

approximate renewal controlled only by a relative o(1) coefficient error;

positivity, prime-power support, tower coherence or local diagonal bounds
as substitutes for exact marked cancellation;

the factorized tensor renewal (12.1) as a detector of Hardy inner zeros.
                                                                    (14.1)
```

The live target is now:

```text
construct a nonfactorized, source-accessible two-variable identity which
preserves u-v, uses exact ordinary-integer arithmetic coefficientwise, and
implies the endpoint-renormalized Gaussian liminf without dividing by zeta
or assuming Hardy range membership.                              (14.2)
```

Status:

```text
proved:
  exact gamma-centered O(y) renewal source;
  exact source transform and zero residue;
  failure of universal divisor coercivity;
  exact event--continuum distance decomposition;
  Selberg sum-versus-difference information loss;
  singleton exact-renewal fiber;
  positive coherent prime-tower falsifier;
  positive shifted-Lambda falsifier;
  perturbative stability failure for every prescribed finite positive
  Selberg hierarchy under relative coefficientwise control;
  factorized bivariate renewal no-go;

closed:
  linear renewal as an independent route;
  perturbative renewal as an independent route;
  finite approximate Selberg hierarchy based only on positivity and
  relative coefficientwise accuracy as an independent route;

open:
  MARKED-DIFFERENCE-ARITHMETIC-RIGIDITY;
  ENDPOINT-RENORMALIZED-GAUSSIAN-LIMINF;
  PARITY-GRAM-GRAPH-TRACE;
  DIRECTIONAL-IDENT and Omega7;

not claimed:
  RH or Omega7.
```
