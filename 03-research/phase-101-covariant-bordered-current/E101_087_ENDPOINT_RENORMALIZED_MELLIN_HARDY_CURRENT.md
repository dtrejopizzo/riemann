# E101.087 - Endpoint-renormalized Mellin--Hardy current

## 1. Decision

The exact Abel abscissa of E101.086 can be written as a finite, purely
arithmetic Gaussian energy without taking a zero sum, continuing a divisor
series or separating Gamma and Euler divergences.

There are three necessary operations:

```text
retain every channel until the finite-u Parseval identity is formed;
center d Psi_Cheb by dx before taking an infinite norm;
subtract the exact moving endpoint before removing a finite prime cutoff.
                                                               (1.1)
```

After these operations, the weakest finite target is

```text
for every epsilon>0,

liminf_(X->infinity) 1/(2pi) integral_R
 |H_(T,tau)(t-i epsilon/2)|^2
 |D_X((1+epsilon)/2+it)
   -X^(-(1+epsilon)/2-it)E_0(X)|^2 dt
 <infinity.                                                   (1.2)
```

Here every object is finite:

```text
E_0(X)=Psi_Cheb(X)-X+1,

D_X(s)=sum_(n<=X)Lambda(n)n^(-s)
       -(X^(1-s)-1)/(1-s).                                   (1.3)
```

Condition (1.2), for one fixed `T in R` and `tau>0`, is equivalent to RH and
Omega7.  This is a sharper source-first coordinate, not a proof.  It removes
four false places in which the missing force might have been hidden:

```text
the separate Gamma channel;
the opposite Euler tail;
the same-event prime diagonal;
the unrenormalized moving endpoint.                           (1.4)
```

The remaining force is a bounded-subsequence theorem for a connected,
off-diagonal, centered prime covariance.  Absolute estimates of the prime
error already have RH strength and are not progress on (1.2).

## 2. Gaussian and arithmetic conventions

Fix `T in R` and `tau>0`.  Put

```text
g(y)=1/[2sqrt(pi tau)] exp[-y^2/(4tau)]exp(iTy),

H_(T,tau)(z)=integral_R g(y)exp(-izy)dy
            =exp[-tau(z-T)^2].                               (2.1)
```

Let

```text
Gamma_infinity(r)
 =Re psi(1/4+ir/2)-log pi.                                   (2.2)
```

The complete translated Gaussian Weil trace of E101.086 is

```text
S(u)=H(i/2)exp(-u/2)+H(-i/2)exp(u/2)

     +1/(2pi) integral_R H(r)Gamma_infinity(r)exp(iur)dr

     -sum_(n>=2)Lambda(n)/sqrt(n)
       [g(u-log n)+g(u+log n)].                              (2.3)
```

All terms in (2.3) converge absolutely for fixed `u`, but some channels do
not have a separate damped norm near the critical abscissa.

Use the centered Stieltjes measure

```text
d mu(x)=d Psi_Cheb(x)-dx=d E_0(x),

E_0(x)=Psi_Cheb(x)-x+1,

E_0(1)=0.                                                     (2.4)
```

In logarithmic coordinates define

```text
F(v)=exp(-v/2)E_0(exp v),              v>=0,
F(v)=0,                               v<0,

k(y)=g'(y)+g(y)/2.                                           (2.5)
```

The harmless `+1` in `E_0` makes the lower Stieltjes endpoint vanish.  It
changes the more usual normalized error by only `exp(-v/2)`.

## 3. Complete finite-interval Parseval identity

For `U>0`, define the one-sided Laplace transform

```text
L_U(z)=integral_0^U exp(-zu)S(u)du.                           (3.1)
```

Put

```text
Pi_U(w)=(1-exp(-wU))/w,             w!=0,
Pi_U(0)=U,                                                   (3.2)
```

and

```text
Phi_(z,U)(a)
 =1/2 exp[-za+tau(z-iT)^2]
  [erfc(sqrt(tau)(z-iT)-a/[2sqrt(tau)])

   -erfc(sqrt(tau)(z-iT)+(U-a)/[2sqrt(tau)])].                (3.3)
```

### Proposition 3.1 - Exact all-channel finite transform

For every complex `z` and every `U>0`,

```text
L_U(z)
 =H(i/2)Pi_U(z+1/2)+H(-i/2)Pi_U(z-1/2)

  +1/(2pi) integral_R
    H(r)Gamma_infinity(r)Pi_U(z-ir)dr

  -sum_(n>=2)Lambda(n)/sqrt(n)
    [Phi_(z,U)(log n)+Phi_(z,U)(-log n)].                     (3.4)
```

Every integral and series in (3.4) is absolutely convergent.

### Proof

The polar terms give the first line by direct integration.  The Gamma
integral permits Fubini because `H(r)` has Gaussian decay and `U` is finite.
For the Euler terms, completing the square gives

```text
integral_0^U exp(-zu)g(u-a)du=Phi_(z,U)(a).                   (3.5)
```

The Gaussian in `a=+-log n` makes the resulting prime-power sums absolutely
convergent.  Substitution in (2.3) proves (3.4). `QED`

### Corollary 3.2 - Safe Hardy boundary norm

For every `epsilon>0`,

```text
integral_(-U)^U exp(-epsilon|u|)|S(u)|^2du
 =1/pi integral_R
   |L_U(epsilon/2+it)|^2dt.                                  (3.6)
```

Indeed, one-sided Plancherel gives a factor `1/(2pi)`, and
`S(-u)=conj(S(u))` doubles the positive half.  Since the left side is
monotone in `U`,

```text
integral_R exp(-epsilon|u|)|S(u)|^2du
 =lim_(U->infinity)1/pi integral_R
   |L_U(epsilon/2+it)|^2dt,                                  (3.7)
```

with the value `+infinity` allowed.

Equation (3.7) is not permission to pass to the limit in each line of (3.4).
When `epsilon<=1`, the growing polar term and the near Euler tail diverge
separately.  Their cancellation exists only in the complete sum.

## 4. Exact centering before the norm

Define the dangerous centered block

```text
B(u)=integral_[1,infinity)
      x^(-1/2)g(u-log x)d mu(x).                              (4.1)
```

### Proposition 4.1 - Prime-error convolution with no boundary term

For every real `u`,

```text
B(u)=integral_0^infinity F(v)k(u-v)dv=(F*k)(u).                (4.2)
```

### Proof

Write `x=exp v`.  The test in (4.1) becomes

```text
x^(-1/2)g(u-log x)=exp(-v/2)g(u-v).                           (4.3)
```

Its `v` derivative is

```text
-exp(-v/2)[g'(u-v)+g(u-v)/2]
 =-exp(-v/2)k(u-v).                                          (4.4)
```

Since `d mu=dE_0`, Stieltjes integration by parts gives (4.2).  The lower
boundary is zero by `E_0(1)=0`; at infinity the Gaussian beats the elementary
bound `Psi_Cheb(x)=O(x log x)` for each fixed `u`. `QED`

### Proposition 4.2 - Every omitted channel is unweighted L2

On `u>=0`,

```text
S(u)=R(u)-B(u),                                               (4.5)
```

where

```text
R(u)
 =H(i/2)exp(-u/2)

  +1/(2pi) integral_R
    H(r)Gamma_infinity(r)exp(iur)dr

  -sum_(n>=2)Lambda(n)/sqrt(n)g(u+log n)

  +C_<(u),                                                    (4.6)
```

and

```text
C_<(u)
 =1/2 H(-i/2)exp(u/2)
   erfc(u/[2sqrt(tau)]+sqrt(tau)(1/2-iT)).                    (4.7)
```

Moreover,

```text
R in L^2(0,infinity).                                        (4.8)
```

### Proof

Expanding (4.1),

```text
B(u)
 =sum_(n>=2)Lambda(n)/sqrt(n)g(u-log n)
  -integral_1^infinity x^(-1/2)g(u-log x)dx.                  (4.9)
```

The complete continuous integral over `(0,infinity)` is
`H(-i/2)exp(u/2)`.  The omitted part over `(0,1)` is (4.7), so (2.3) and
(4.9) give (4.5)--(4.7).

The first term of (4.6) decays exponentially.  The Gamma term decays like
`exp(-a u)` for every `a<1/2`, by the strip shift in E101.086.  The opposite
Euler tail is super-Gaussian because it contains `(u+log n)^2`.  Standard
complex-erfc asymptotics make (4.7) super-Gaussian on the positive half-axis.
This proves (4.8). `QED`

Consequently, for every `epsilon>0`,

```text
integral_0^infinity exp(-epsilon u)|S(u)|^2du<infinity

iff

integral_0^infinity exp(-epsilon u)|B(u)|^2du<infinity.       (4.10)
```

Thus Gamma, the remote prime tail and the residual polar terms do not carry
the positive abscissa.

## 5. Weighted convolution and coercivity

Fix `epsilon>0` and put

```text
a_epsilon=(1+epsilon)/2,

F_epsilon(v)=exp(-epsilon v/2)F(v),

g_epsilon(y)=exp(-epsilon y/2)g(y),

k_epsilon(y)=exp(-epsilon y/2)k(y).                           (5.1)
```

Then

```text
exp(-epsilon u/2)B(u)
 =(F_epsilon*k_epsilon)(u),                                  (5.2)

k_epsilon=g_epsilon'+a_epsilon g_epsilon.                    (5.3)
```

For a finite cutoff `V`, let

```text
F_(epsilon,V)=1_[0,V]F_epsilon,

U_(epsilon,V)=F_(epsilon,V)*g_epsilon.                        (5.4)
```

The function in (5.4) is smooth and rapidly decreasing at both ends.  Hence

```text
||F_(epsilon,V)*k_epsilon||_2^2
 =||U_(epsilon,V)'||_2^2
  +a_epsilon^2||U_(epsilon,V)||_2^2.                          (5.5)
```

The cross term vanishes by integration of
`a_epsilon(|U_(epsilon,V)|^2)'`.  This is an exact coercive decomposition.
There is no favorable derivative--mass cross term left to estimate.

With the Fourier convention of (2.1),

```text
Fourier[g_epsilon](t)=H(t-i epsilon/2),

Fourier[k_epsilon](t)
 =[a_epsilon+it]H(t-i epsilon/2).                             (5.6)
```

Therefore

```text
||F_(epsilon,V)*k_epsilon||_2^2
 =1/(2pi) integral_R W_(epsilon,T,tau)(t)
   |Fourier[F_(epsilon,V)](t)|^2dt,                           (5.7)
```

where

```text
W_(epsilon,T,tau)(t)
 =[a_epsilon^2+t^2]
  exp{-2tau[(t-T)^2-epsilon^2/4]}.                            (5.8)
```

The weight is strictly positive for every real `t`.  Gaussian smoothing
suppresses high frequencies quantitatively but kills no frequency.

## 6. Two finite arithmetic currents and the endpoint wall

Let `X=exp V`.  The direct finite centered-measure current is

```text
B_X^mu(u)=integral_[1,X]
           x^(-1/2)g(u-log x)d mu(x).                         (6.1)
```

For

```text
s=a_epsilon+it,
q=t-i epsilon/2,                                             (6.2)
```

define

```text
D_X(s)=integral_[1,X]x^(-s)d mu(x)

      =sum_(n<=X)Lambda(n)n^(-s)
       -(X^(1-s)-1)/(1-s).                                   (6.3)
```

The value at `s=1` is understood by continuity.

### Proposition 6.1 - Direct finite measure energy

For every `epsilon>0` and finite `X`,

```text
integral_R exp(-epsilon u)|B_X^mu(u)|^2du
 =1/(2pi) integral_R |H(q)|^2|D_X(s)|^2dt.                   (6.4)
```

Equivalently,

```text
 =exp(tau epsilon^2/2)/[2sqrt(2pi tau)]
  double_integral_[1,X]^2
  (xy)^(-a_epsilon)
  exp[-log^2(x/y)/(8tau)]
  exp[-iT log(x/y)]d mu(x)d mu(y).                            (6.5)
```

The value is nonnegative because it is the norm in (6.4).  For `T=0`, the
kernel in (6.5) is also pointwise real and positive, although the centered
measure remains signed.

### Proof

After multiplying (6.1) by `exp(-epsilon u/2)`, Fourier transformation in
`u` gives `H(q)D_X(s)`.  Plancherel proves (6.4).  Expanding the square and
performing the Gaussian `t` integral proves (6.5). `QED`

The direct current has a moving endpoint which is not harmless.  Finite
Stieltjes integration by parts gives exactly

```text
B_X^mu(u)
 =X^(-1/2)E_0(X)g(u-log X)
  +integral_0^(log X)F(v)k(u-v)dv.                            (6.6)
```

Define the endpoint-renormalized current

```text
B_X^ren(u)
 =B_X^mu(u)-X^(-1/2)E_0(X)g(u-log X).                        (6.7)
```

It is exactly the finite convolution on the second line of (6.6).

Now put

```text
M_X(s)=integral_1^X E_0(x)x^(-s-1)dx.                        (6.8)
```

Then

```text
D_X(s)=X^(-s)E_0(X)+sM_X(s),                                 (6.9)
```

and

```text
M_X(s)
 =1/s sum_(n<=X)Lambda(n)[n^(-s)-X^(-s)]

  -(X^(1-s)-1)/(1-s)
  +(1-X^(-s))/s.                                             (6.10)
```

Thus no infinite integral is needed to compute `M_X`.

### Corollary 6.2 - Endpoint-renormalized finite energy

For every finite `X`,

```text
integral_R exp(-epsilon u)|B_X^ren(u)|^2du
 =1/(2pi) integral_R |H(q)|^2|sM_X(s)|^2dt

 =1/(2pi) integral_R |H(q)|^2
  |D_X(s)-X^(-s)E_0(X)|^2dt.                                 (6.11)
```

The endpoint in (6.6) cannot simply be bounded uniformly.  Such a bound
would require RH-sized pointwise control of `E_0(X)`.  Renormalization (6.7)
removes it algebraically before any estimate.

## 7. The minimal finite criterion

The finite norms in (6.11) are not monotone in `X`.  Cross terms can have
either sign, and Gaussian convolution has no bounded inverse on `L^2`.
Consequently, replacing a limit by `sup_X` would introduce an unjustified
and stronger target.

### Theorem 7.1 - Endpoint-renormalized liminf equivalence

For one fixed `T in R` and `tau>0`, the following are equivalent:

```text
RH;

Omega7;

for every epsilon>0,
 liminf_(X->infinity) integral_R
  exp(-epsilon u)|B_X^ren(u)|^2du<infinity;

condition (1.2).                                             (7.1)
```

### Proof

For fixed `u`, the elementary bound `Psi_Cheb(x)=O(x log x)` and the remote
Gaussian tail imply

```text
B_X^ren(u)->B(u).                                             (7.2)
```

If the liminf in (7.1) is finite, choose a cofinal sequence along which the
norms stay bounded.  Fatou's lemma and (7.2) give

```text
integral_R exp(-epsilon u)|B(u)|^2du<infinity.                (7.3)
```

The negative half-axis is super-Gaussian and (4.10) transfers (7.3) to the
complete trace `S`.  If this holds for every `epsilon>0`, Theorem 8.2 of
E101.086 gives RH and Omega7.

Conversely, RH gives the classical bound

```text
E_0(x)=O(x^(1/2)log^2 x).                                    (7.4)
```

Hence `F_epsilon` belongs to `L^2(0,infinity)` for every
`epsilon>0`.  Its truncations converge in `L^2`, while
`k_epsilon in L^1(R)`.  Young's inequality now gives

```text
F_(epsilon,V)*k_epsilon
 ->F_epsilon*k_epsilon in L^2(R).                            (7.5)
```

Thus the norms in (6.11) actually converge under RH, proving the reverse
implication.  Equivalence with (1.2) is (6.11). `QED`

The theorem deliberately uses `liminf`, the weakest statement supplied by
Fatou.  Uniform boundedness in `X` is sufficient and, as an all-`epsilon`
family, also follows from RH, but it is not the minimal target.

## 8. Smoothed Cramer coordinate

The same target has a direct multiplicative mean-square form.  Define

```text
kappa_(T,tau)(r)
 =r^(-1/2-iT)exp[-log^2(r)/(4tau)],

E_kappa(X)
 =integral_[1,infinity)
   kappa_(T,tau)(x/X)d[x-Psi_Cheb(x)].                        (8.1)
```

If `X=exp u`, the source in E101.086 satisfies

```text
J_(T,tau)(log X)=c_tau X^(-1/2)E_kappa(X),

c_tau=1/[2sqrt(pi tau)].                                     (8.2)
```

Therefore

```text
integral_0^infinity exp(-su)|J_(T,tau)(u)|^2du

 =c_tau^2 integral_1^infinity
   |E_kappa(X)|^2 X^(-2-s)dX.                                (8.3)
```

### Proposition 8.1 - Multiplicative block criterion

The following are equivalent:

```text
the integral in (8.3) is finite for every s>0;

for every delta>0,
 integral_X^(eX)|E_kappa(Y)|^2dY
  <<_(delta,T,tau) X^(2+delta).                              (8.4)
```

### Proof

If (8.3) is finite with `s=delta`, then on `[X,eX]`

```text
integral_X^(eX)|E_kappa(Y)|^2dY
 <=(eX)^(2+delta)
   integral_X^(eX)|E_kappa(Y)|^2Y^(-2-delta)dY.               (8.5)
```

Conversely, assume (8.4).  On the blocks `[e^j,e^(j+1)]`, use (8.4) with
`delta=s/2`.  The contribution to (8.3) is then `O(exp(-sj/2))`, and the
geometric sum converges. `QED`

Thus the Gaussian route is a fixed smooth Cramer mean square.  The
multiplicative smoothing makes the complete source identity clean, but it
does not lower the RH strength of the required exponent.

### Proposition 8.2 - The endpoint s=1 is unconditionally closed

Integration by parts in (8.1) gives

```text
E_kappa(X)
 =-kappa(X^(-1))
  -1/X integral_1^infinity
    [x-Psi_Cheb(x)]kappa'(x/X)dx.                            (8.6)
```

The classical prime-number-theorem error

```text
x-Psi_Cheb(x)<<x exp[-c sqrt(log x)]                         (8.7)
```

and the log-Gaussian decay of `kappa'` imply constants `c_1,c_2>0` for
which

```text
J_(T,tau)(u)<<exp[u/2-c_1 sqrt(u)],                           (8.8)

integral_0^infinity
 exp[-u+c_2 sqrt(u)]|J_(T,tau)(u)|^2du<infinity.              (8.9)
```

### Proof

The boundary at infinity in Stieltjes integration by parts vanishes by the
Gaussian in `log(x/X)`; the lower boundary is `-kappa(X^(-1))`, proving
(8.6).  Split the integral into logarithmic annuli around `X`.  On each
annulus use (8.7), while derivatives of `kappa` contribute a fixed polynomial
in `|log(x/X)|` times a Gaussian.  The resulting convolution of
`exp[-c sqrt(log x)]` with that Gaussian is
`O(exp[-c_1 sqrt(log X)])`.  Equations (8.2) and `X=exp u` give (8.8).
Choose `c_2<2c_1`; then the integrand in (8.9) is
`O(exp[-(2c_1-c_2)sqrt u])`, which is integrable. `QED`

Thus the previously safe region `s>1` reaches the boundary `s=1`, with a
subexponential margin.  It supplies no positive distance into `s<1`.

## 9. Exact no-go ledger

### 9.1 Absolute prime-error estimates

Young, Schur, Minkowski or pointwise absolute values give at best

```text
||B_X^ren||_(2,epsilon)
 <=||k_epsilon||_1
   [integral_1^X |E_0(x)|^2x^(-2-epsilon)dx]^(1/2).           (9.1)
```

The all-`epsilon` estimate

```text
integral_1^infinity |E_0(x)|^2x^(-2-epsilon)dx<infinity
for every epsilon>0                                           (9.2)
```

is equivalent to RH.  RH implies it by (7.4); conversely (9.1), (4.10) and
E101.086 imply RH.  Thus (9.1) only replaces the target by a stronger
classical criterion.

The equivalent family of dyadic estimates

```text
integral_X^(2X)|E_0(x)|^2dx<<_delta X^(2+delta)
for every delta>0                                             (9.3)
```

has the same wall.

### 9.2 Meromorphic continuation is not a boundary limit

In the safe half-plane,

```text
integral_1^infinity E_0(x)x^(-s-1)dx
 =1/s[-zeta'(s)/zeta(s)-1/(s-1)].                            (9.4)
```

Continuing the right side meromorphically and evaluating it on one vertical
line does not prove convergence of the Mellin truncations there.  A zero to
the right of that line need not create a singularity on the line itself, but
it destroys the Hardy boundary limit.  Replacing the limit in (6.11) by the
continued value deletes exactly the detector.

### 9.3 The Gaussian has no spectral nullspace

For a zero `rho=beta+i gamma`, put

```text
p=gamma-i(beta-1/2).
```

Then

```text
ip+1/2=rho,

Fourier[k](p)=rho H_(T,tau)(p)!=0.                            (9.5)
```

The corresponding mode of `F` is multiplied by `H(p)`, never annihilated.
Changing `tau`, differentiating the Gaussian or taking finitely many Gaussian
moments changes a nonzero coefficient, not the positive abscissa.

### 9.4 Local covariance cannot carry the obstruction

The same-event prime diagonal in (6.5) is bounded by

```text
sum_(n>=2)Lambda(n)^2/n^(1+epsilon)<infinity                 (9.6)
```

for every `epsilon>0`.  Fixed crosses between powers of one prime have an
additional log-Gaussian factor.  Removing these terms neither controls the
remaining signed covariance nor changes a positive abscissa.  Any correction
which already lies in every damped `L^2` space is similarly neutral.

### 9.5 Cutoff completeness is a separate theorem

The pointwise limit (7.2) plus Fatou yields a `liminf` criterion.  It does not
yield convergence or monotonicity of finite covariance forms.  A proposed
finite proof must either bound a cofinal subsequence of (6.11), or supply an
independent mechanism proving full `L^2` convergence.  Replacing the attained
finite support by a larger fictitious support is not allowed.

### 9.6 Universal positive falsifier

Fix `0<alpha<1/2` and `0<a<1`.  Define a positive comparison measure by

```text
d Psi_alpha(x)=[1-a x^(alpha-1/2)]dx,            x>=1.        (9.7)
```

It has the power-saving prime-number-theorem analogue

```text
Psi_alpha(X)=X+O(X^(1/2+alpha)),                               (9.8)
```

but

```text
d[x-Psi_alpha(x)]=a x^(alpha-1/2)dx.                           (9.9)
```

The corresponding centered Gaussian current is exactly

```text
J_alpha(u)
 =a/2 exp[tau(alpha-iT)^2]exp(alpha u)
  erfc(-u/[2sqrt(tau)]-sqrt(tau)(alpha-iT)).                  (9.10)
```

Consequently,

```text
J_alpha(u)
 ~a exp[tau(alpha-iT)^2]exp(alpha u),

integral_0^infinity exp(-su)|J_alpha(u)|^2du<infinity
 iff s>2alpha.                                                (9.11)
```

The model can also be made atomic.  Put

```text
b_n=integral_n^(n+1)[1-a x^(alpha-1/2)]dx,

d Psi_alpha^at=sum_(n>=1)b_n delta_n.                         (9.12)
```

The primitive of `d Psi_alpha^at-d Psi_alpha` is bounded.  Integration by
parts therefore changes (9.10) by only `O(exp(-u/2))`.  Nevertheless its
same-event diagonal satisfies

```text
sum_(n>=1)b_n^2/n^(1+s)<infinity                              (9.13)
```

for every `s>0`.

This falsifier obeys positivity, centering, a power-saving PNT analogue and
finite local diagonal energy, while realizing every prescribed abscissa in
`(0,1)`.  None of those properties, alone or in combination, can prove
(11.1).  The missing input must distinguish the divisorial support and
weights of `Lambda` from (9.7) and (9.12).

### 9.7 Fixed local operators cannot remove the forbidden modes

Let

```text
L=sum_j p_j(partial_u)tau_(h_j)                                (9.14)
```

be any fixed finite combination of derivatives and translations.  On the
mode `exp(alpha u)`, its symbol is the entire function

```text
ell(alpha)=sum_j p_j(alpha)exp(h_j alpha).                    (9.15)
```

If `L` killed every comparison mode with `0<alpha<1/2`, then `ell` would
vanish on an interval.  The identity theorem would force `ell` to vanish
identically, so `L` would carry no discriminatory information.

This excludes, without further arithmetic input:

```text
fixed differences and increments;
finite differential preconditioners;
additional fixed Gaussian convolutions;
integration-by-parts hierarchies;
Hardy factorizations whose factors do not use divisorial structure.       (9.16)
```

They multiply the prohibited exponential by a nonzero analytic symbol and
preserve its abscissa.

## 10. Literature and nonduplication gate

The normalized logarithmic error

```text
exp(-v/2)[Psi_Cheb(exp v)-exp v]                              (10.1)
```

and its subexponential-growth equivalence to RH appear explicitly in

```text
M. A. K. Akhtar,
A Log-Fractal Spectral Reformulation of the Prime Error Term and a
Cancellation Criterion Equivalent to the Riemann Hypothesis:
  https://ssrn.com/abstract=6695378                            (10.2)
```

The indexed primary abstract was available, but the full manuscript was not.
No absence claim about identities inside the inaccessible text is made.

Mean-square prime-error antecedents include

```text
R. P. Brent, D. J. Platt, T. S. Trudgian,
The mean square of the error term in the prime number theorem:
  https://arxiv.org/abs/2008.06140

T. Zhao, On the mean values of the error terms in Mertens' theorems:
  https://doi.org/10.1007/s40993-025-00640-y

D. R. Johnston, A. Yang,
Some explicit estimates for the error term in the prime number theorem:
  https://arxiv.org/abs/2204.01980                             (10.3)
```

Zhao records the classical dependence of the dyadic prime-error mean square
on `Theta=sup Re rho`.  Johnston--Yang show the scale delivered by current
zero-free-region and density inputs; inserted in (9.1), it diverges below the
safe PNT abscissa.

A recent Hardy-space approximation route is

```text
J. Manzur, W. Noor, G. Quintero,
A Hardy space approximation supporting zero-free half-planes for the
zeta-function:
  https://arxiv.org/abs/2606.16097                             (10.4)
```

It starts from the Bagchi--Baez-Duarte Hardy criterion and proves zero-free
half-planes only when the corresponding approximation holds there.  It does
not supply the boundary convergence in (7.1).

The adjacent renewal, Volterra and correlation literature includes

```text
A. Selberg, An Elementary Proof of the Prime-Number Theorem:
  https://www.jstor.org/stable/1969455

H. Iwata, On an arithmetical Volterra equation:
  https://arxiv.org/abs/2205.06001

H. Iwata, An arithmetic Volterra equation and the Riemann hypothesis:
  https://arxiv.org/abs/2601.11052

A. Alvarez Cruz, E. A. Alvarez Gutierrez,
A Colombeau--Beurling criterion for the Riemann hypothesis:
  https://arxiv.org/abs/2606.22562

S. Bhattacharya, G. Martin, E. Simpson,
Correlations of error terms for weighted prime counting functions:
  https://arxiv.org/abs/2507.13504                            (10.4a)
```

Selberg already contains the first quadratic closure of `Lambda*1=log`.
The Volterra formulas reconstruct the arithmetic convolution inverse, and
their critical estimates contain the corresponding zeta denominator.  The
Hardy approximation papers turn critical convergence into a zero-free
criterion; they do not prove it.  Connected prime-error correlations are
also an existing subject, so that phrase alone is not a novelty claim.

Accordingly, no novelty is claimed for

```text
the normalized logarithmic prime error;
Mellin--Parseval conversion;
Cramer-type mean-square criteria;
Hardy-space zero-free criteria;
linear divisor renewal and its Volterra inversion;
the first Selberg quadratic closure;
Gaussian smoothing of a Stieltjes prime error;
the equivalence of (9.2) or (9.3) with RH.                    (10.5)
```

The only potentially new object is the exact combination of the fixed
Gaussian Weil trace with the endpoint-renormalized finite energy (6.11) and
the weakest `liminf` equivalence (7.1).  Global novelty is not asserted.

## 11. Working target and stop rule

Freeze the broad name `LOG-GAUSSIAN-L2-CANCELLATION`.  Its source-finite
form is

```text
ENDPOINT-RENORMALIZED-GAUSSIAN-LIMINF:

for every epsilon>0,
liminf_(X->infinity) 1/(2pi) integral_R
 W_(epsilon,T,tau)(t)|M_X(a_epsilon+it)|^2dt
 <infinity.                                                   (11.1)
```

The allowed next step must preserve the centered combination inside
`M_X` and control its correlations before absolute values are taken.  It may
use an exact arithmetic recurrence for `Lambda`, a finite energy balance or
a new positive completion.

The one structural input not shared by the falsifiers of Section 9.6 is the
divisor identity.  On the additive logarithmic semigroup define

```text
N=sum_(n>=1)delta_(log n),

L=sum_(n>=2)Lambda(n)delta_(log n),

N_0=L_0=exp(y)dy.                                             (11.2)
```

Dirichlet convolution and its continuous analogue give

```text
L*N=yN,

L_0*N_0=yN_0.                                                (11.3)
```

With

```text
Delta L=L_0-L,
Delta N=N_0-N,                                               (11.4)
```

subtraction yields the exact centered renewal equation

```text
Delta L*N
 =y Delta N-L_0*Delta N.                                    (11.5)
```

This is exact classical arithmetic rigidity: the positive and atomic
falsifiers need not satisfy (11.3), but the identity is the measure form of
`Lambda*1=log`.  It is not by itself a new source of coercivity.  For the
fixed ordinary integer measure
`N`, the simultaneous constraints

```text
L>=0;
support(L) subset {log(p^k)};
L*N=yN.                                                       (11.6)
```

do **not** define a cone.  They define one point.  Coefficient comparison at
`log n` gives recursively

```text
L(1)=0,

L(n)=log n-sum_(d|n,d<n)L(d)=Lambda(n).                       (11.6a)
```

Equivalently, `L=mu_Moebius*log`.  Positivity and prime-power support then
follow from the already identified solution; they do not create a nontrivial
family on which a geometric coercivity theorem could be tested.

There is a second wall.  Since `N=delta_0+N_+`, writing (11.5) as

```text
Delta L=R-Delta L*N_+                                        (11.7)
```

and iterating reconstructs the convolution inverse of `N`, namely the
Moebius measure.  Absolute iteration returns to `s>1`; estimating the inverse
through Moebius sums recreates a classical RH-strength criterion.  The only
admissible future use of (11.5) would require first defining a nontrivial
relaxed class of ordinary-lattice renewal data and proving a uniform stability
estimate on that class.  Applying an estimate only to (11.6) is just restating
the desired bound for `Lambda`; it is not structural progress.

There is also a quadratic stop rule.  Applying the convolution derivation
`D f(n)=log(n)f(n)` to `Lambda*1=log` gives

```text
(D Lambda+Lambda*Lambda)*1=log^2,                           (11.7a)
```

which is the classical Selberg symmetry identity.  Repeated derivation and
reconvolution give its higher-order hierarchy.  These identities push a pair
of logarithmic variables `(u,v)` to `u+v`, whereas the Hermitian energy
(6.11) depends on `u-v`.  Thus the first quadratic energy, or any finite
repetition which has already forgotten the marked difference, is not a new
route to (11.1).

The route may not use:

```text
an absolute or pointwise RH-sized bound for E_0;
termwise continuation of -zeta'/zeta;
an unrenormalized endpoint estimate;
the prime diagonal as a substitute for the full covariance;
sup_X without proving why that stronger quantity is bounded;
termwise Moebius inversion of the renewal equation;
calling the singleton fiber (11.6) a coercive cone;
reintroducing the classical Selberg hierarchy after the difference
coordinate has been pushed forward.                                      (11.8)
```

## 12. Status

```text
proved:
  complete finite-u all-channel Parseval identity;
  exact centered convolution B=F*k;
  unconditional L2 neutrality of the residual channels;
  coercive derivative--mass decomposition;
  direct finite centered-measure energy;
  exact endpoint subtraction;
  finite arithmetic formula for M_X;
  endpoint-renormalized liminf equivalence;
  smoothed Cramer block equivalence;
  unconditional closure of the endpoint s=1;
  continuous and atomic positive-abscissa falsifiers;
  fixed local-operator no-go;
  exact centered divisor-renewal equation;
  singleton renewal rigidity and the first Selberg stop rule;
  absolute-estimate, continuation and local-diagonal no-go results;

new live target:
  ENDPOINT-RENORMALIZED-GAUSSIAN-LIMINF;

not claimed:
  boundedness of the liminf in (11.1);
  convergence or monotonicity of the finite energies;
  a new mean-square criterion in the classical sense;
  a proof of RH or Omega7;

still open:
  a genuinely new centered off-diagonal covariance estimate;
  a nonperturbative marked two-variable arithmetic identity;
  PARITY-GRAM-GRAPH-TRACE;
  DIRECTIONAL-IDENT and Omega7.
```
