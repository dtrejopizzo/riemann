# E101.070 - Scalar Pearson obstruction and theta hierarchy no-go

## 1. Decision

E101.069 leaves open the possibility that a source-specific Pearson equation
could control the complete Loewner boundary vector.  There are two natural
ways to try to obtain such an equation:

```text
the prime-power distribution might satisfy a scalar polynomial Pearson law;
the theta heat equation might close a finite recurrence for the arithmetic
Fourier radical.                                                   (1.1)
```

Both possibilities can be decided exactly.  The first is incompatible with
the interior prime-power atoms unless the Pearson coefficients are trivial.
The second projects to an infinite dense Fourier hierarchy with an explicit
endpoint flux; it does not close on the radical coefficients.  Finite
differences improve the endpoint decay at fixed order, but the improvement is
universal and is transferred exactly back into the Loewner boundary by
E101.068.

The scalar Pearson target in E101.069(8.3) is therefore withdrawn.  The
source-specific structure already available is the nonlocal multiplicative
Gamma--Euler connection of E83.004--E83.007.  Its remaining burden is a
signed bilateral boundary pairing, not a scalar finite-band recurrence.

## 2. Distributional scalar Pearson obstruction

Fix `L>0`.  The prime part of the truncated Weil distribution has the form

```text
nu_L^P=sum_(p^r<=exp(L)) a_(p,r) delta_(r log p),
a_(p,r)=(log p)p^(-r/2)>0.                          (2.1)
```

The precise positive normalization is irrelevant below.  Write

```text
nu_L^W=nu_L^A-nu_L^P,                               (2.2)
```

where the archimedean distribution is smooth in a neighborhood of every
interior prime-power location.  Endpoint distributions, if present, are
kept separate.

### Theorem 2.1 - No nontrivial fixed polynomial Pearson pair

Suppose two polynomials `sigma,tau`, independent of `L`, satisfy

```text
(sigma nu_L^W)'=tau nu_L^W                          (2.3)
```

as distributions on the interior of `(0,L)` for every `L`.  Then

```text
sigma=0,
tau=0.                                              (2.4)
```

### Proof

Let

```text
x_(p,r)=r log p<L.                                  (2.5)
```

Localize (2.3) to a small interval containing `x_(p,r)` and no other
prime-power location.  The singular part of the left side is

```text
-a_(p,r) sigma(x_(p,r)) delta'_(x_(p,r)),           (2.6)
```

while the right side contains no derivative of a Dirac mass.  Hence

```text
sigma(x_(p,r))=0.                                   (2.7)
```

After (2.7), the prime atom disappears from `sigma nu_L^W`.  The remaining
Dirac coefficient on the right side of (2.3) is

```text
-a_(p,r) tau(x_(p,r)),                              (2.8)
```

so

```text
tau(x_(p,r))=0.                                     (2.9)
```

As `L` varies, (2.7) and (2.9) hold at every point `r log p`.  There are
infinitely many distinct such points.  A nonzero polynomial has only
finitely many zeros, proving (2.4). `QED`

### Corollary 2.2 - Finite cutoffs do not have fixed band

For a single finite `L`, one can annihilate the prime atoms by choosing

```text
sigma_L(x)=product_(p^r<=exp(L))(x-r log p).         (2.10)
```

But

```text
deg sigma_L=#{p^r:p^r<=exp(L)},                     (2.11)
```

which diverges with `L`.  The associated moment relation has growing band
width and supplies no fixed Laguerre--Freud closure.

The theorem is local at the atoms.  It is unaffected by a smooth
archimedean density or by distributions supported at the two endpoints.  It
also does not forbid a nonlocal shift equation.  It forbids precisely the
fixed scalar polynomial Pearson input contemplated in E101.069.

## 3. The multiplicative equation already present

Let `S_y` be the one-sided shift on `L^2(0,L)`:

```text
(S_y f)(t)=1_[y,L](t)f(t-y),
S_yS_z=S_(y+z).                                     (3.1)
```

With `Xf(t)=tf(t)`, one has

```text
[X,S_y]=yS_y.                                       (3.2)
```

For `epsilon>=0`, define the finite Euler and Mobius units

```text
Z_(L,epsilon)
 =sum_(n<=exp(L))n^(-1/2-epsilon)S_(log n),

M_(L,epsilon)
 =sum_(n<=exp(L))mu(n)n^(-1/2-epsilon)S_(log n).    (3.3)
```

The truncated semigroup law gives the exact identities

```text
M_(L,epsilon)Z_(L,epsilon)=I,

M_(L,epsilon)[X,Z_(L,epsilon)]
 =sum_(n<=exp(L))Lambda(n)n^(-1/2-epsilon)S_(log n).
                                                            (3.4)
```

Thus the natural prime equation is multiplicative and nonlocal.  It is not a
differential equation for a scalar measure.

Let `H_L^A` be the archimedean CCM operator and write its one-sided shift
coefficient as `a_L(y)`.  E83.005 proves

```text
[H_L^A,Z_(L,epsilon)]
 =sum_(n<=exp(L))n^(-1/2-epsilon)
   integral_0^L a_L(y)[S_y^*,S_(log n)]dy.          (3.5)
```

The commutator in (3.5) is supported on the two physical boundary wedges.
This is the genuine Gamma--Euler flux law already present in the program.
It leaves a complete signed boundary integral.

The boundary is not small as an operator.  E83.007 constructs `y_0` with

```text
norm R_(y_0)>=2^(-sigma),                            (3.6)
```

uniformly once the interval contains the relevant wedge.  Therefore neither
termwise estimates nor an operator-norm limit can close (3.5).  Any use of
(3.5) must retain simultaneously

```text
the actual Euler-generated source;
the signed y-integral;
both physical endpoints;
the finite Fourier collar;
the terminal safe functional.                       (3.7)
```

This is the multiplicative analogue of the radical conservation law in
E101.068: localization is exact, but localization is not smallness.

## 4. Exact theta and scale identities

Put

```text
g(v)=exp(-pi v^2),
D=v partial_v,
h(v)=(1/4)D(D+1)g(v)
    =(pi/2)v^2(2pi v^2-3)exp(-pi v^2).              (4.1)
```

Define

```text
vartheta(t,z)
 =sum_(ell in Z)exp(-pi ell^2 t)exp(2pi i ell z),

T(x,z)=vartheta(exp(2x),z),                         (4.2)

k(x)=exp(x/2)sum_(ell>=1)h(ell exp x).              (4.3)
```

### Proposition 4.1 - Theta representation of the arithmetic source

One has

```text
k(x)=(1/8)exp(x/2)(T_xx(x,0)+T_x(x,0)).             (4.4)
```

If

```text
F(x)=exp(x/2)T(x,0),                                (4.5)
```

then Poisson summation gives `F(-x)=F(x)` and

```text
k(x)=(1/8)(partial_x^2-1/4)F(x).                   (4.6)
```

### Proof

Differentiation with respect to `x` acts as `D` on each term
`g(ell exp x)`.  Since the nonzero theta terms occur in opposite pairs,

```text
T_xx+T_x
 =2 sum_(ell>=1)D(D+1)g(ell exp x)
 =8 sum_(ell>=1)h(ell exp x),                       (4.7)
```

which proves (4.4).  The modular identity

```text
vartheta(t,0)=t^(-1/2)vartheta(t^(-1),0)            (4.8)
```

implies the parity of `F`.  Substitution of `T=exp(-x/2)F` in (4.4) gives
(4.6). `QED`

Equation (4.6) is a useful exact source identity, but it introduces the
theta primitive `F`.  It is not a recurrence closed on the coefficients of
`k`.

## 5. Heat projection produces a dense infinite hierarchy

The theta heat equation becomes

```text
partial_x T(x,z)
 =exp(2x)/(2pi) partial_z^2T(x,z).                  (5.1)
```

For

```text
T_q(x)=partial_z^(2q)T(x,z)|_(z=0),                 (5.2)
```

it reads

```text
partial_xT_q(x)=exp(2x)/(2pi)T_(q+1)(x).            (5.3)
```

Let `a=L/2`, `omega_n=2pi n/L`, and define symmetric Fourier coefficients

```text
t_(q,n)=(1/L)integral_(-a)^a T_q(x)exp(-i omega_n x)dx.  (5.4)
```

The Fourier coefficients of `exp(2x)` are

```text
E_r(L)=2(-1)^r sinh(L)/[L(2-i omega_r)],            (5.5)
```

and are nonzero for every integer `r`.  Projecting (5.3) gives

```text
i omega_n t_(q,n)+beta_(q,n)
 =(1/(2pi))sum_(r in Z)E_(n-r)(L)t_(q+1,r),         (5.6)

beta_(q,n)
 =(-1)^n[T_q(a)-T_q(-a)]/L.                        (5.7)
```

### Consequence 5.1

The direct heat projection has all three features

```text
infinite support in the Fourier index;
passage from layer q to layer q+1;
an explicit nonzero endpoint flux.                  (5.8)
```

It is therefore not a finite-band recurrence on the coefficients of `k`.
Eliminating the auxiliary layers would require an additional identity not
contained in Poisson summation, the heat equation or scale covariance.

This conclusion is deliberately limited.  It does not assert that no
artificial variable-coefficient recurrence can ever be written.  It asserts
that the natural theta identities project exactly to (5.6), not to the
finite closure required by a scalar Pearson route.

## 6. Endpoint formula for the radical coefficients

Let

```text
f_n=(1/L)integral_(-a)^a F(x)exp(-i omega_nx)dx,

c_n^o=(1/L)integral_(-a)^a k(x)exp(-i omega_nx)dx.  (6.1)
```

Because `F` is even, two integrations by parts in (4.6) give

```text
c_n^o
 =-(omega_n^2+1/4)f_n/8
  +(-1)^nF'(a)/(4L).                                (6.2)
```

In the interval coordinate `y=x+a`, define

```text
kappa_n
 =(1/L)integral_0^L k(y-a)exp(-2pi i n y/L)dy
 =(-1)^n c_n^o.                                    (6.3)
```

Then

```text
kappa_(-n)=kappa_n in R.                            (6.4)
```

Repeated integration by parts gives, for every fixed `R>=1`,

```text
kappa_n
 =-sum_(r=1)^R 2k^((2r-1))(a)/[L(i omega_n)^(2r)]
  +widehat(k^((2R)))_n/(i omega_n)^(2R).            (6.5)
```

In particular,

```text
kappa_n~Lk'(L/2)/(2pi^2n^2).                        (6.6)
```

The theta source is rapidly decreasing on the real line, but its periodic
restriction has a derivative mismatch at the endpoints.  For fixed `L`,
that mismatch produces the `n^(-2)` Fourier tail in (6.6).

## 7. What finite differences actually buy

Define the forward coefficient difference

```text
(Delta_+ kappa)_n=kappa_n-kappa_(n+1).              (7.1)
```

From (6.3),

```text
Delta_+^K kappa_n
 =(1/L)integral_0^L k(y-a)
   (1-exp(-2pi i y/L))^K exp(-2pi i n y/L)dy.       (7.2)
```

The multiplier in (7.2) vanishes to order `K` at both endpoints.  Applied
to the leading tail, the elementary Laplace representation yields

```text
0<=Delta_+^K(n^(-2))
 =integral_0^infinity t exp(-nt)(1-exp(-t))^Kdt
 <=(K+1)!/n^(K+2).                                  (7.3)
```

Thus a fixed difference order improves the endpoint power.  It does not
give a uniform growing-order theorem.  The corresponding binomial shift
polynomial satisfies

```text
norm[1-(1-U)^K]=2^K-1                               (7.4)
```

on bilateral `ell^2`, and the right-bordered decomposition creates a collar
whose width grows with `K`.  E101.068 then gives exactly

```text
S_(Z,K)(kappa_Z,phi)=Bcal_(Z,K)(kappa_Z,phi).        (7.5)
```

Therefore fixed differences remain useful only for the auxiliary endpoint
module.  They do not estimate the force-bearing boundary scalar.

## 8. Build-neutrality and the controlled quartet

Keep `kappa_Z` fixed and change the Loewner symbol from `s_Z` to

```text
s_P=s_Z+delta s.                                    (8.1)
```

Off the diagonal, the induced kernel variation is

```text
delta M(n,j)
 =-a[delta s_n-delta s_j]/[d_n-d_j], n!=j.         (8.2)
```

For the complete fixed-level CCM operator one must also retain the cosine
symbol:

```text
delta M(n,n)=2delta c(d_n)-a delta s'(d_n).         (8.3)
```

The shifted exterior commutator is

```text

delta D_m^sigma(n,j)
 =-a[delta s_n-delta s_(n-sigma m)]
    /[d_n-d_(j+sigma m)].                           (8.4)
```

For the complete boundary vector of E101.069,

```text
H_(P,N,eta)(kappa_Z)-H_(Z,N,eta)(kappa_Z)
 =sum_(sigma=+,-){
    delta D_eta^sigma P_N^sigma kappa_Z
   -G_eta^sigma(U)delta M(I-P_N^sigma)kappa_Z}.     (8.5)
```

Every identity in Sections 4--7 concerns the fixed source `kappa_Z` and is
unchanged under (8.1).  Hence theta parity, heat flow, endpoint differences
and their Fourier decay cannot determine the sign of (8.5), nor can they
prevent its cancellation with the explicit quartet functional in
E101.068(7.2).

This is the decisive novelty filter:

```text
a source identity which is identical for Z and P is auxiliary;
the force-bearing theorem must use the explicit rational shapes of
delta s and delta c and prove noncancellation in the complete paired
response.                                                           (8.6)
```

## 9. Revised live target

The following routes are now frozen:

```text
fixed scalar polynomial Pearson equations for the complete Weil source;
finite-band closure obtained directly from the theta heat equation;
constant-coefficient recurrences for the radical tail;
integration by parts without the full right-bordered collar;
fixed-order endpoint differences promoted to a discriminant;
operator-norm smallness of the Gamma--Euler boundary commutator.      (9.1)
```

The surviving force-bearing problem is narrower.  For an explicit
controlled quartet, derive its symbol increment `delta s_n` from the CCM
cell formula, insert it into (8.2)--(8.4), and calculate the complete scalar

```text
Response_(N,eta)
 =Quartet_(delta s)(kappa_Z,A_eta phi)
  +phi[H_P(kappa_Z)-H_Z(kappa_Z)].                  (9.2)
```

The next theorem must decide one of two mutually exclusive outcomes:

```text
Response_(N,eta)=0 identically,
in which case this entire Loewner coordinate is another conservation no-go;

or

Response_(N,eta) has an explicit nonzero residue depending on the off-line
parameter, with a source-first estimate uniform on the declared tests. (9.3)
```

Only the second outcome can feed `ARITHMETIC-LOEWNER-DISCRIMINANT`.  It must
still be connected to the arithmetic build without inserting a zero
location into the zeta-side forcing step.

## 10. Status

```text
proved:
  distributional obstruction to a fixed scalar polynomial Pearson law;
  exact theta-scale representation of the arithmetic source;
  exact dense Fourier heat hierarchy and endpoint flux;
  fixed-order endpoint improvement and its growing-order cost;
  build-neutrality of all theta-only identities;

imported and retained:
  the nonlocal multiplicative Gamma--Euler connection and its exact boundary
  commutator from E83.004--E83.007;

rejected:
  scalar Pearson and finite theta recurrence as force-bearing routes;

open:
  the explicit quartet Loewner response (9.2),
  ARITHMETIC-LOEWNER-DISCRIMINANT,
  UNIFORM-BETA-ENDPOINT, DIRECTIONAL-IDENT and Omega7.

subsequent resolution:
  E101.071 evaluates (9.2) exactly, restores the cosine-symbol diagonal and
  reduces the noncancelled part to one rational exterior current.
```
