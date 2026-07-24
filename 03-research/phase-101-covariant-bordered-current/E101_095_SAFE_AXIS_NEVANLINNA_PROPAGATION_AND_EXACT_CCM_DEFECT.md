# E101.095 - Safe-axis Nevanlinna propagation and the exact CCM defect

## 1. Decision

The finite CCM determinant and its logarithmic derivative do not define a new
route.  They are already present in the source construction, and the
safe-axis formula has the same analytic shape as `SR-LOG`.  The exact
calculation nevertheless makes two load-bearing distinctions.

First, the Cauchy transform of the finite Weil ground vector is not one
bordered transfer `T_+`, but it is not unrelated to the boundary construction.
The exact two-boundary Schur identity of P76.013 gives it as the linear
antisymmetrization `T_+(z)-T_+(-z)`.  The Phase-76 bilateral characteristic
instead uses the multiplicative combination `T_+(z)T_+(-z)`.  Confusing the
linear and multiplicative combinations erases a nontrivial phase defect.

Second, safe-axis identification is not a harmless Euler-region module once
the approximants are real-rooted.  A Pick--Nevanlinna normal-family theorem
proved below gives

```text
pointwise logarithmic-derivative identification
on any nonempty safe interval
+ real, even, order-at-most-one finite real-rootedness
=> every zero of the target is real.                         (1.1)
```

Thus `SR-LOG` itself has the full force of `Omega7`.  Absolute convergence of
the Euler tail remains elementary.  The force is entirely in making the
source Cauchy transform match the Gamma--Euler target.

The surviving defect is written explicitly in this document.  Before removal
of the known exterior mesh, it is

```text
C_(L,N)(s)
 =M_src_(L,N)'(s)/M_src_(L,N)(s)
  +(L/2)coth(L(s-1/2)/2)
  -A_infty(s)
  +sum_(n<=exp(L)) Lambda(n)n^(-s).                 (1.2)
```

An exact source core/exterior factorization reduces `(1.2)` further to

```text
C_core_(L,N)(s)
 =Q_(L,N)'(s)/Q_(L,N)(s)
  -A_infty(s)
  +sum_(n<=exp(L))Lambda(n)n^(-s),                    (1.3)
```

where `Q_(L,N)` is a monic even polynomial obtained directly from the finite
Weil matrix.  On the positive real safe axis, the difference `C-C_core` is an
explicit positive exterior-mesh tail.

No currently proved build-neutral consequence of the commutator,
displacement identity or finite self-adjointness controls `(1.3)` by itself:
all of that infrastructure also holds for the planted build.  A proof that
`C_core_(L,N)` tends to zero on a safe interval must therefore contain the
arithmetic discriminator.

## 2. The source ground characteristic

Fix `lambda>1`, put

```text
L=2 log lambda,
d_j=2 pi j/L,
sigma=s-1/2.                                           (2.1)
```

Assume the finite lowest Weil eigenvalue is simple and has a real even
eigenvector.  Use the normalization of E101.093,

```text
sum_(|j|<=N) xi_(eta,j)=1.                             (2.2)
```

Define

```text
S_(L,N)(z)=sum_(|j|<=N) xi_(eta,j)/(z-d_j),

X_(L,N)(z)
 =2 sin(zL/2) S_(L,N)(z).                              (2.3)
```

The factor `L^(-1/2)` in the CCM Fourier formula has disappeared because
`xi_delta=L^(1/2)xi_eta`.  Formula `(2.3)` is exactly E101.093(9.2).
Evenness of `xi_eta` gives

```text
S_(L,N)(-z)=-S_(L,N)(z),
X_(L,N)(-z)=X_(L,N)(z).                                (2.4)
```

The function `X_(L,N)` is real entire, even, of exponential type and has only
real zeros.  The last assertion follows from the finite source-built
self-adjoint quotient, conditionally on the even-simple hypothesis.

The regularized determinant is

```text
F_(L,N)(z)
 :=det_reg(Dpert_(lambda,N)-z)
 =-i lambda^(-iz) X_(L,N)(z).                          (2.5)
```

The zero-free factor in `(2.5)` changes the first logarithmic derivative but
not the divisor.

## 3. Exact safe-axis formulas

For `Re(s)>1`, define the source Cauchy transform

```text
M_src_(L,N)(s)
 :=sum_(|j|<=N) xi_(eta,j)/(sigma-i d_j),

M_src_(L,N)'(s)
 =-sum_(|j|<=N) xi_(eta,j)/(sigma-i d_j)^2.             (3.1)
```

The sign and scale follow from

```text
z-d_j at z=-i sigma =-i(sigma-i d_j),
S_(L,N)(-i sigma)=i M_src_(L,N)(s).                     (3.2)
```

Consequently,

```text
X_(L,N)(-i sigma)
 =2 sinh(L sigma/2) M_src_(L,N)(s),                     (3.3)

F_(L,N)(-i sigma)
 =i(exp(-L sigma)-1) M_src_(L,N)(s).                    (3.4)
```

Both identities are exact.  Differentiation gives

```text
partial_s log X_(L,N)(-i sigma)
 =(L/2)coth(L sigma/2)+M_src_(L,N)'/M_src_(L,N),        (3.5)

partial_s log F_(L,N)(-i sigma)
 =L/(exp(L sigma)-1)+M_src_(L,N)'/M_src_(L,N).          (3.6)
```

The difference between `(3.5)` and `(3.6)` is exactly `L/2`, since

```text
(L/2)coth(L sigma/2)
 =L/2+L/(exp(L sigma)-1).                               (3.7)
```

Equivalently,

```text
i exp(L sigma/2)F_(L,N)(-i sigma)=X_(L,N)(-i sigma).    (3.8)
```

Thus the de-regularizing exponential is source-canonical.  It does not use a
target value or a zero of `Xi`.

In the spectral variable, if

```text
A_2(z)=sum_(|j|<=N)xi_(eta,j)/(z-d_j)^2,                (3.9)
```

then

```text
X_(L,N)'(z)/X_(L,N)(z)
 =(L/2)cot(zL/2)-A_2(z)/S_(L,N)(z),                    (3.10)

F_(L,N)'(z)/F_(L,N)(z)
 =-iL/2+(L/2)cot(zL/2)-A_2(z)/S_(L,N)(z).              (3.11)
```

An additional normalization `exp(a+ibz)` adds the constant `ib` to
`(3.11)` and changes no second logarithmic derivative.

## 4. Exact Gamma--Euler split

Write the completed Riemann function as `xi_R(s)` and the centered function as

```text
Xi(z)=xi_R(1/2+iz).                                    (4.1)
```

On `Re(s)>1`, put

```text
A_infty(s)
 =1/s+1/(s-1)-(1/2)log pi+(1/2)psi(s/2).               (4.2)
```

Absolute Euler convergence gives

```text
xi_R'(s)/xi_R(s)
 =A_infty(s)+zeta'(s)/zeta(s)
 =A_infty(s)-sum_(n>=2)Lambda(n)n^(-s).                (4.3)
```

Define the closed tail

```text
R_L(s)=sum_(n>exp(L))Lambda(n)n^(-s).                  (4.4)
```

For every compact `K` contained in `Re(s)>1`, P76.039 gives

```text
sup_(s in K)|R_L(s)|
 =O_K(exp(-(min_(s in K)Re(s)-1)L)).                   (4.5)
```

The complete safe defect of the Fourier characteristic is

```text
Delta_(L,N)(s)
 :=partial_s log[X_(L,N)(-i sigma)/xi_R(s)]

 =M_src_(L,N)'/M_src_(L,N)
  +(L/2)coth(L sigma/2)
  -A_infty(s)
  +sum_(n>=2)Lambda(n)n^(-s).                          (4.6)
```

Split it as

```text
Delta_(L,N)(s)=C_(L,N)(s)+R_L(s),                      (4.7)

C_(L,N)(s)
 =M_src_(L,N)'/M_src_(L,N)
  +(L/2)coth(L sigma/2)
  -A_infty(s)
  +sum_(n<=exp(L))Lambda(n)n^(-s).                     (4.8)
```

Equation `(4.7)` is the exact defect decomposition.  The term `(4.5)` is
closed.  Section 5 removes the remaining explicit exterior mesh from `(4.8)`
and leaves the core defect `(1.3)`.

For the regularized determinant itself one instead has

```text
partial_s log[F_(L,N)(-i sigma)/xi_R(s)]
 =C_(L,N)(s)-L/2+R_L(s).                               (4.9)
```

The constant `-L/2` is only the regularization phase and is removed by
`(3.8)`.

## 5. Exact source core, exterior mesh and divisor curvature

### 5.1 Core/exterior factorization

Define

```text
D_(L,N)(sigma)
 :=product_(j=-N)^N(sigma-i d_j)
 =sigma product_(j=1)^N(sigma^2+d_j^2),

Q_(L,N)(sigma)
 :=D_(L,N)(sigma)M_src_(L,N)(s).                       (5A-1)
```

Because `sum_j xi_(eta,j)=1`, the polynomial `Q_(L,N)` is monic of degree
`2N`.  Both `D` and `M_src` are odd, so `Q` is even.  Its zeros are

```text
sigma=i theta,
theta in spec(Dphys_(lambda,N)),                       (5A-2)
```

with multiplicity.  They lie on the imaginary axis by finite
self-adjointness.

Put

```text
E_ext_(L,N)(sigma)
 :=2sinh(L sigma/2)/D_(L,N)(sigma).                    (5A-3)
```

The apparent singularities at `sigma=i d_j`, `|j|<=N`, are removable.
The zeros retained by `E_ext` are exactly the exterior mesh

```text
sigma=i d_k,  |k|>N.                                   (5A-4)
```

Equations `(3.3)`--`(3.4)` factor exactly as

```text
X_(L,N)(-i sigma)
 =E_ext_(L,N)(sigma)Q_(L,N)(sigma),

exp(L sigma/2)F_(L,N)(-i sigma)
 =-i E_ext_(L,N)(sigma)Q_(L,N)(sigma).                 (5A-5)
```

The exterior logarithmic derivative is

```text
B_ext^src_(L,N)(sigma)
 :=E_ext_(L,N)'(sigma)/E_ext_(L,N)(sigma)

 =(L/2)coth(L sigma/2)-D_(L,N)'(sigma)/D_(L,N)(sigma)

 =2 sigma sum_(k>N)1/(sigma^2+d_k^2).                 (5A-6)
```

For every compact safe set `K`, once `d_N` dominates `K`,

```text
sup_(sigma in K)|B_ext^src_(L,N)(sigma)|
 =O_K(L^2/N).                                          (5A-7)
```

Thus the uncorrected logarithmic derivative needs `N/L^2->infinity` to make
this term vanish directly.  No rate is needed if the known exterior factor is
divided out exactly.

Define the core defect

```text
Delta_core_(L,N)(s)
 :=Q_(L,N)'(sigma)/Q_(L,N)(sigma)-xi_R'(s)/xi_R(s)

 =C_core_(L,N)(s)+R_L(s),                              (5A-8)

C_core_(L,N)(s)
 :=Q_(L,N)'/Q_(L,N)
   -A_infty(s)
   +sum_(n<=exp(L))Lambda(n)n^(-s).                    (5A-9)
```

Then

```text
Delta_(L,N)=B_ext^src_(L,N)+Delta_core_(L,N),
C_(L,N)=B_ext^src_(L,N)+C_core_(L,N).                  (5A-10)
```

This is an exact, nonperturbative removal of every known exterior term.

There is also a root-free construction of `Q`.  Let

```text
A_0=diag(d_(-N),...,d_N),
B(sigma)=sigma I-iA_0,
R(sigma)=B(sigma)^(-1),
T=W_(lambda,N)-epsilon_(lambda,N)I.                    (5A-11)
```

Let `eta` be the all-ones coordinate vector.  Since `ker(T)=C xi_eta` and
`eta^T xi_eta=1`,

```text
Q_(L,N)(sigma)
 =det [[B(sigma), xi_eta],[-eta^T,0]].                 (5A-12)
```

Moreover `T` is real symmetric of corank one, so

```text
adj(T)=kappa xi_eta xi_eta^T,
kappa=eta^T adj(T)eta.                                 (5A-13)
```

It follows that

```text
Q_(L,N)(sigma)^2
 =D_(L,N)(sigma)^2
  [eta^T R(sigma)adj(T)R(sigma)eta]
  /[eta^T adj(T)eta].                                  (5A-14)
```

This formula constructs the squared core characteristic from
`(W,epsilon,A_0,eta)` without selecting a sign or listing a root.  In
particular,

```text
2Q'/Q
 =2D'/D
  +partial_sigma log[eta^T R adj(T)R eta].             (5A-15)
```

If

```text
Q_(L,N)(sigma)
 =sigma^(2m_0)
  product_(theta>0)(sigma^2+theta^2)^(m_theta),         (5A-16)
```

then, for `x=sigma^2>0`,

```text
g_src_(L,N)(x)
 :=[1/sigma]Q_(L,N)'(sigma)/Q_(L,N)(sigma)

 =2m_0/x+2sum_(theta>0)m_theta/(x+theta^2).             (5A-17)
```

Thus the exact source core is a positive Stieltjes transform.  Identifying
`(5A-17)` with

```text
g_Xi(x)
 =[1/sigma]xi_R'(1/2+sigma)/xi_R(1/2+sigma)            (5A-18)
```

on a safe interval is the source version of `STIELTJES-IDENT`.  By Theorem
7.1 below, it already has the force of `Omega7`.

### 5.2 Curvature is the uncontracted divisor defect

Let

```text
mathcal_F_(L,N)(s)=F_(L,N)(-i(s-1/2)).                 (5.1)
```

Its zeros have the form

```text
alpha=1/2+i theta,
theta in Z(F_(L,N)) subset R.                          (5.2)
```

For canonical products of order at most one, affine exponential factors
disappear after two derivatives.  Hence

```text
(log mathcal_F_(L,N))''(s)
 =-sum_alpha m_alpha/(s-alpha)^2,

(log xi_R)''(s)
 =-sum_rho m_rho/(s-rho)^2.                            (5.3)
```

If

```text
K_(L,N)(s)
 :=partial_s^2 log[mathcal_F_(L,N)(s)/xi_R(s)],         (5.4)
```

then, with no extra sign or scale,

```text
K_(L,N)(s)
 =sum_rho m_rho/(s-rho)^2
  -sum_alpha m_alpha/(s-alpha)^2.                      (5.5)
```

In arithmetic coordinates,

```text
K_(L,N)
 =(M_src'/M_src)'
  -L^2 exp(L sigma)/(exp(L sigma)-1)^2
  -A_infty'(s)
  -sum_(n>=2)Lambda(n)log(n)n^(-s),                    (5.6)

A_infty'(s)
 =-1/s^2-1/(s-1)^2+(1/4)psi_1(s/2).                   (5.7)
```

Formula `(5.5)` is the normalization-invariant uncontracted divisor defect.
Convergence of `(5.5)` in a topology which controls its principal parts is a
form of `TRUE-DIVISOR-IDENT`.  Convergence only on a safe interval needs one
first-derivative normalization and locally uniform, or at least local
`L1`, control in order to integrate back to `(4.6)`; the affine ambiguity and
the convergence mode must not be silently discarded.

The bilateral characteristic of Phase 76 carries a factor two because it is a
product of two reflected characteristics.  Its curvature defect is therefore
twice `(5.5)` only when the two underlying finite characteristics coincide.
No such coincidence with the source ground characteristic is asserted here.

## 6. Exact two-boundary crosswalk and the phase defect

Phase 76 uses the two-component boundary Schur transfer

```text
T_(L,N)(z)=(T_-(z),T_+(z)),

T_+(z)
 =1/(z-d_b)-sum_n x_n/(z-d_n).                         (6.1)
```

If `v=(v_-,v_+)` is the boundary part of the finite ground vector, P76.013
proves the exact identity

```text
S_(L,N)(z)=r_z xi_eta=T_-(z)v_-+T_+(z)v_+.             (6.2)
```

For an even ground vector, `v_-=v_+=c`, with `c!=0` under the strict
interlacing hypothesis used by the Schur solve.  P76.030 gives

```text
T_-(z)=-T_+(-z).                                      (6.3)
```

Therefore

```text
S_(L,N)(z)=c[T_+(z)-T_+(-z)].                          (6.4)
```

This is the correct bridge.  The source Cauchy transform is not one boundary
component; it is the linear antisymmetrization of the two components.

Put

```text
E_+(z)=sin(zL/2)T_+(z).                                (6.5)
```

Equations `(2.3)` and `(6.4)` give

```text
X_(L,N)(z)=2c[E_+(z)+E_+(-z)].                         (6.6)
```

The raw bilateral characteristic instead has the multiplicative form

```text
Psi_raw_(L,N)(z)
 =constant E_+(z)E_+(-z).                              (6.7)
```

On the safe axis, real-type symmetry gives

```text
X_(L,N)(i sigma)=4c Re E_+(i sigma),
Psi_raw_(L,N)(i sigma)=constant |E_+(i sigma)|^2.       (6.8)
```

Since

```text
E_+(i sigma)=i sinh(sigma L/2)T_+(i sigma),            (6.9)
```

the source characteristic depends on `Im T_+(i sigma)`, while the bilateral
characteristic depends on the full modulus of `T_+(i sigma)`.

Where neither side vanishes, define the raw derivatives

```text
J_src^raw(sigma)
 :=2 partial_sigma log|X_(L,N)(-i sigma)|,

J_bd^raw(sigma)
 :=partial_sigma log Psi_raw_(L,N)(-i sigma)

 =L coth(sigma L/2)
  +2 Re[i T_+'(i sigma)/T_+(i sigma)].                 (6.10)
```

Then the exact phase defect is

```text
J_src^raw-J_bd^raw
 =partial_sigma log{
    [Im T_+(i sigma)]^2/|T_+(i sigma)|^2}

 =partial_sigma log cos^2(arg E_+(i sigma)).           (6.11)
```

Thus the two routes coincide at the logarithmic-derivative level only if the
phase ratio in `(6.11)` is constant.  Numerical smallness of one component
does not prove that statement.

The core comparison must remove each route's own exact exterior divisor.  By
`(5A-6)` and E101.025,

```text
J_src^core
 :=J_src^raw-2B_ext^src,

J_bd^core
 :=J_bd^raw-B_ext^exact,                               (6.12)

B_ext^exact
 =2sigma/(d_N^2+sigma^2)
  +4sigma sum_(k>N)1/(d_k^2+sigma^2),

2B_ext^src
 =4sigma sum_(k>N)1/(d_k^2+sigma^2).                  (6.13)
```

Consequently the core/core crosswalk is

```text
J_src^core-J_bd^core
 =partial_sigma log cos^2(arg E_+(i sigma))
  +2sigma/(d_N^2+sigma^2).                             (6.14)
```

Equation `(6.14)`, rather than `M_src=T_+`, is the exact relation between the
source-ground and bilateral boundary routes.  The remaining edge term is
explicit.  The phase term is not an independent easy error: if either core
is identified with the `Xi` target, control of the other is again a
force-bearing identification.

## 7. Pick--Nevanlinna propagation

The next theorem shows exactly why safe-axis convergence already carries the
full divisor information.

### Theorem 7.1 - Safe-axis real-rootedness propagation

Let `(f_n)` be nonzero real even entire functions of order at most one, all of
whose zeros are real.  Let `F` be a nonzero real even entire function.  Let
`I` be a nonempty open interval in `(0,infinity)` such that

```text
F(-i sigma)!=0,  sigma in I.                           (7.1)
```

For a nonvanishing value on the safe ray define

```text
A_f(sigma)=partial_sigma log|f(-i sigma)|.              (7.2)
```

Assume pointwise convergence

```text
A_(f_n)(sigma)->A_F(sigma),  sigma in I.                (7.3)
```

Then every zero of `F` is real.  In fact,

```text
f_n'/f_n -> F'/F                                      (7.4)
```

locally uniformly in the lower half-plane.

### Proof

The zeros of `f_n`, with multiplicity, can be written as a zero of even
multiplicity `2m_n` at the origin and pairs

```text
+/-a_(n,k),  a_(n,k)>0.                                (7.5)
```

Hadamard factorization and evenness give

```text
f_n(z)
 =c_n z^(2m_n)
  product_k(1-z^2/a_(n,k)^2)^(mu_(n,k)),               (7.6)
```

because

```text
sum_k mu_(n,k)/a_(n,k)^2<infinity,                     (7.7)
```

and the possible zero-free factor `exp(alpha_n z+beta_n)` is constant by
evenness.  Logarithmic differentiation gives, locally uniformly off the real
axis,

```text
h_n(z):=f_n'(z)/f_n(z)
 =2m_n/z
  +sum_k mu_(n,k)
   [1/(z-a_(n,k))+1/(z+a_(n,k))].                      (7.8)
```

For `z=x+iy`, `y<0`,

```text
Im h_n(z)
 =(-y){2m_n/|z|^2
       +sum_k mu_(n,k)[1/|z-a_(n,k)|^2
                       +1/|z+a_(n,k)|^2]}
 >=0.                                                  (7.9)
```

Thus `h_n` maps the lower half-plane to the closed upper half-plane.  The
correct equivalent upper-half-plane statement is that `-f_n'/f_n` is a
Pick--Nevanlinna function.

At a safe point, real evenness gives

```text
f_n(-i sigma) in R,
h_n(-i sigma) in iR,
A_(f_n)(sigma)=-i h_n(-i sigma),
h_n(-i sigma)=i A_(f_n)(sigma).                        (7.10)
```

Choose `sigma_0 in I`.  By `(7.3)` and `(7.10)`, the sequence
`h_n(-i sigma_0)` is bounded.  Apply the Cayley transform

```text
phi_n(z)=[h_n(z)-i]/[h_n(z)+i].                        (7.11)
```

It satisfies `|phi_n|<=1` in the lower half-plane.  Montel compactness gives
a locally convergent subsequence of every subsequence.  The bounded value at
`-i sigma_0` prevents a limit from being the constant `1`.  The maximum
principle then prevents the limit from taking the value `1` at any interior
point.  Inverting `(7.11)` gives a finite holomorphic subsequential limit `h`
on the whole lower half-plane.

Equation `(7.3)` identifies `h` with `F'/F` on the set
`{-i sigma:sigma in I}`.  The meromorphic identity theorem extends the
identity through the lower half-plane away from the zeros of `F`.  If `F` had
a zero `rho` there of multiplicity `m`, then

```text
F'(z)/F(z)=m/(z-rho)+O(1),                              (7.12)
```

contradicting holomorphy of `h`.  Hence `F` has no zero in the lower
half-plane.  Reality of `F` excludes upper-half-plane zeros by conjugation.

Every subsequence has the same subsequential limit, proving `(7.4)` for the
full sequence. `QED`

### Corollary 7.2 - Squared-modulus version

The conclusion is unchanged if `(7.3)` is stated with

```text
partial_sigma log|f_n(-i sigma)|^2,
partial_sigma log|F(-i sigma)|^2,                      (7.13)
```

because both sides of `(7.3)` are merely multiplied by two.

### Sharpness

One safe point does not suffice.  For `0<sigma_0<1`, let

```text
F(z)=1+z^4,
f(z)=1-z^2/a^2,
a^2=(1-sigma_0^4)/(2 sigma_0^2).                       (7.14)
```

Then the two logarithmic derivatives agree at `-i sigma_0`, although `F` has
only nonreal zeros.

The order-at-most-one hypothesis also cannot be dropped.  Put

```text
p_n(z)=sum_(k=1)^n (-1)^(k+1)z^(2k)/k,
f_n(z)=exp(p_n(z)).                                    (7.15)
```

Every `f_n` is real, even and zero-free, but has order `2n`.  On `|z|<1`,

```text
f_n'(z)/f_n(z)->2z/(1+z^2)=F'(z)/F(z),
F(z)=1+z^2,                                            (7.16)
```

and `F` has the nonreal zeros `+/-i`.

Theorem 7.1 does not reopen the route rejected in E78.148.  That autopsy
concerns an incremental rational transfer whose pole residues have mixed
signs, so the transfer is not a Pick function.  Here the Pick function is the
logarithmic derivative of the complete real-rooted characteristic; its
residues are the positive zero multiplicities.  The two hypotheses are
different.

## 8. Consequences for the two closure routes

### 8.1 Source ground characteristic

Suppose a cofinal even-simple family satisfies, pointwise on one nonempty
interval `I subset (1/2,infinity)`,

```text
partial_s log X_(L,N)(-i(s-1/2))
 ->xi_R'(s)/xi_R(s).                                   (8.1)
```

Theorem 7.1 with `f_n=X_(L,N)` and `F=Xi` gives RH and hence `Omega7`.
If, in addition, the interval satisfies `I subset (1,infinity)`, then `(4.7)`
and the absolute Euler tail show that a sufficient statement is

```text
C_(L,N)(s)->0,  s in I,                                (8.2)
```

because the Euler tail already tends to zero.

Therefore `(8.2)` is not an auxiliary estimate.  It is a force-bearing
statement.

### 8.2 Bilateral Phase-76 characteristic

For the core bilateral characteristic, `CORE-SR-LOG` states

```text
partial_sigma log Psi_core_(L,N)(-i sigma)
 ->2 xi_R'(1/2+sigma)/xi_R(1/2+sigma).                 (8.3)
```

Under the simplicity and nondegeneracy hypotheses of P76.023, every finite
`Psi_core` is an even real-rooted polynomial.  Apply Theorem 7.1 to the target

```text
[Xi(z)/xi_R(1/2+sigma_0)]^2.                           (8.4)
```

Even pointwise convergence in `(8.3)` on any nonempty safe interval implies
RH.  Local uniform convergence, integration of the derivative and a separate
normal-family argument are not needed for this implication.

This sharpens the attribution:

```text
Euler tail                         build-neutral and closed;
finite real-rootedness             build-neutral infrastructure;
safe log-derivative identification full force of Omega7.             (8.5)
```

## 9. Planted-system obstruction

Let `F_plant` be real and even with at least one nonreal zero.  No sequence
`f_n` satisfying the hypotheses of Theorem 7.1 can obey

```text
partial_sigma log|f_n(-i sigma)|
 ->partial_sigma log|F_plant(-i sigma)|                (9.1)
```

on a nonempty interval avoiding target zeros.  Otherwise Theorem 7.1 would
force every zero of `F_plant` to be real.

Thus any planted build which retains finite self-adjointness and
real-rootedness must fail at the safe source identification itself.  It cannot
fail first at the Euler tail, at the commutator, or at the abstract diagonal
lemma.  This is the precise falsifier location for `(4.8)`.

## 10. Why the finite eigenvalue equation does not estimate the defect

Write

```text
W_(L,N)=P_(L,N)-A_(L,N)-E_(L,N),
W_(L,N)xi_eta=epsilon_(L,N)xi_eta.                     (10.1)
```

Let the bilinear Cauchy row be

```text
r_s(j)=1/(sigma-i d_j),
M_src_(L,N)(s)=r_s^T xi_eta.                           (10.2)
```

Set

```text
p(s)=r_s^T P xi_eta,
a(s)=r_s^T A xi_eta,
e(s)=r_s^T E xi_eta.                                   (10.3)
```

Then

```text
p(s)-a(s)-e(s)=epsilon_(L,N)M_src_(L,N)(s).            (10.4)
```

If `epsilon_(L,N)!=0`, differentiation and division give

```text
M_src_(L,N)'/M_src_(L,N)
 =partial_s log[p(s)-a(s)-e(s)],                       (10.5)

Q_(L,N)'/Q_(L,N)
 =D_(L,N)'/D_(L,N)
  +[p'(s)-a'(s)-e'(s)]/[p(s)-a(s)-e(s)].               (10.6)
```

Equations `(10.5)`--`(10.6)` are tautological rewritings of the same Cauchy
quotient.  The Euler cell is exactly

```text
e(s)
 =sum_(1<k<=exp(L))Lambda(k)k^(-1/2)
   r_s^T Omega(log k)xi_eta.                            (10.7)
```

It is not equal to

```text
M_src_(L,N)(s)sum_(k<=exp(L))Lambda(k)k^(-s).           (10.8)
```

The exact discrepancy which such a replacement would have to control is

```text
C_E(s)
 :=sum_(1<k<=exp(L))Lambda(k)
   {k^(-1/2)r_s^T Omega(log k)xi_eta
    -k^(-s)M_src_(L,N)(s)}.                            (10.9)
```

This term remains coupled to the polar and archimedean cells inside the
ratio `(10.6)`.  P76.040 falsifies the analogous hard-Euler replacement for
the bordered transfer.  It does not prove that the new source-ground
quantity `(10.9)` is large; it requires `(10.9)` to be estimated directly
rather than declared small by the same replacement.

When `epsilon_(L,N)=0`, the displayed quotient is `0/0`.  Splitting
`P`, `A` and `E` before the cancellation supplies no estimate for `(4.8)`.

The displacement commutator proves self-adjointness and real-rootedness, but
it also holds in the planted control.  It cannot prove `(8.2)` without an
additional source identity which discriminates the arithmetic build.

## 11. A concrete model-to-ground target

The CCM source proves that the Fourier transform of its explicit model
`k_lambda` converges to `Xi` uniformly on closed substrips of
`|Im(z)|<1/2`.  It does not prove that the actual Weil ground vector is close
to that model.

Let `xi_(lambda,N)` denote a cofinal finite even-simple ground vector as a
function on `[lambda^(-1),lambda]`, extended by zero.  For
`0<epsilon<1/2`, put

```text
B=1/2-epsilon,

E_(lambda,epsilon)
 :=sup_(|beta|<=B)
   integral_(lambda^(-1))^lambda
   |c_lambda xi_(lambda,N(lambda))(u)-k_lambda(u)|
   u^beta d*u.                                         (11.1)
```

The constants `c_lambda` must be fixed by source normalization, not by zero
matching.

### Theorem 11.1 - Weighted ground-model closure

If the finite family is even-simple and

```text
E_(lambda,epsilon)->0                                  (11.2)
```

for every `0<epsilon<1/2`, then

```text
c_lambda widehat(xi_(lambda,N(lambda)))(z)
 ->Xi(z)                                               (11.3)
```

uniformly on every closed substrip of `|Im(z)|<1/2`.
Consequently RH and `Omega7` hold.

### Proof

For `|Im(z)|<=B`,

```text
|u^(-iz)|=u^(Im(z)).                                   (11.4)
```

Therefore

```text
|widehat(c_lambda xi-k_lambda)(z)|
 <=integral |c_lambda xi-k_lambda|u^(Im(z))d*u
 <=E_(lambda,epsilon).                                 (11.5)
```

The known model convergence and `(11.5)` give `(11.3)`.  Every finite
ground transform is real-rooted.  Hurwitz excludes a nonreal zero of the
nonzero limit `Xi`. `QED`

The weighted estimate is strictly stronger than qualitative `L^2`
convergence on the growing interval.  The finite spectral reduction must use
the projected model, not the continuous vector directly.

Let

```text
H_lambda=L^2([lambda^(-1),lambda],d*u),
P_(lambda,N):H_lambda->E_(lambda,N)                    (11.6)
```

be the orthogonal Fourier projection.  Replace `k_lambda` by its even part if
needed; this does not change its limiting even transform.  Put

```text
k_(lambda,N)=P_(lambda,N)k_lambda,
kappa_(lambda,N)=||k_(lambda,N)||_2,
q_(lambda,N)=k_(lambda,N)/kappa_(lambda,N).             (11.7)
```

Assume `kappa_(lambda,N)!=0`.  In the even block of the finite Weil matrix,
let

```text
nu_0<nu_1                                             (11.8)
```

be the first two eigenvalues, and let `xi_0` be the unit ground vector.  The
next even eigenvalue is the relevant one; the second global eigenvalue may be
odd.  With

```text
R_(lambda,N)=<q_(lambda,N),W_(lambda,N)q_(lambda,N)>,  (11.9)
```

Rayleigh--Ritz gives

```text
min_phi ||q_(lambda,N)-exp(i phi)xi_0||_2^2
 <=2 [R_(lambda,N)-nu_0]/[nu_1-nu_0].                 (11.10)
```

Indeed, expansion in an eigenbasis first yields

```text
1-|<q_(lambda,N),xi_0>|^2
 <=[R_(lambda,N)-nu_0]/[nu_1-nu_0],                   (11.11)
```

and the squared distance to the ground line is at most twice the left side.
Choose the real sign, or complex phase, which realizes `(11.10)` and put

```text
c_(lambda,N)=kappa_(lambda,N)exp(i phi).               (11.12)
```

This normalization uses only the explicit model and the finite source
ground line; it does not fit a zero.

For `B>0`, define

```text
W_(lambda,B)
 :=[(lambda^(2B)-lambda^(-2B))/(2B)]^(1/2),            (11.13)
```

with `W_(lambda,0)=(2 log lambda)^(1/2)`.  Cauchy--Schwarz gives

```text
sup_(|beta|<=B) integral |h(u)|u^beta d*u
 <=W_(lambda,B)||h||_(L^2(d*u)).                       (11.14)
```

The projection triangle inequality and `(11.10)` now give the complete
finite sufficient bound

```text
E_(lambda,epsilon)
 <=W_(lambda,B){
    kappa_(lambda,N)
    [2(R_(lambda,N)-nu_0)/(nu_1-nu_0)]^(1/2)
    +||(I-P_(lambda,N))k_lambda||_2}.                  (11.15)
```

Therefore the autosufficient spectral target is

```text
W_(lambda,B){
 kappa_(lambda,N)
 [2(R_(lambda,N)-nu_0)/(nu_1-nu_0)]^(1/2)
 +||(I-P_(lambda,N))k_lambda||_2}
 ->0                                                   (11.16)
```

for every `B<1/2` along one specified cofinal path.  No audited source proves
simultaneous control of the projection tail, Rayleigh excess and next-even
gap at the rate in `(11.16)`.

E71.17 already reduced stable-divisor identification to ground-model
convergence and an operator-gap criterion.  Equations `(11.13)`--`(11.16)`
are the growing-support weighted refinement needed for a whole critical
substrip; they are not a new ground/gap route.

## 12. Literature and nonduplication audit

The following pieces predate this document.

```text
CCM, arXiv:2511.22755:
  exact Fourier formula, regularized determinant, finite real-rootedness,
  model convergence, and the explicit statement that simple-even ground
  structure and model-to-ground approximation are missing;

Connes--van Suijlekom, arXiv:2511.23257:
  finite determinant identity and fixed-support finite-section convergence
  under an isolated simple ground hypothesis;

Suzuki, arXiv:2606.09096 and its earlier source:
  the exact screw-function transform
  g_hat(z)=z^(-2)xi_R'(1/2-iz)/xi_R(1/2-iz), not a bound for the CCM
  ground-model defect;

Groskin, arXiv:2607.02828:
  finite one-level Weil dictionary and fixed-parameter archimedean tail;

E71.6 and E73.178:
  the raw pole-killed ground characteristic and its exact Cauchy-numerator
  node identity;

E72.23 and E72.310--E72.311:
  the Weyl log-current formula, the finite Cauchy numerator and the identity
  Q'/Q=M_src'/M_src+D'/D;

E71.17:
  reduction of stable-divisor identification to ground-model convergence
  and an operator residual/gap theorem;

P76.013, P76.030, P76.035, E77.6 and E78.98:
  the exact two-boundary Schur bridge, reflection, SR-LOG, the iterated-limit
  formulation and the closed Euler/high-divisor tails;

E101.019--E101.021 and E101.025:
  one-interval closure, the positive Stieltjes criterion with full
  Omega7 force, and the corrected exact boundary exterior mesh.      (12.1)
```

Therefore none of the following may be counted as new progress:

```text
deriving the finite determinant again;
differentiating it to obtain a rational log derivative;
writing xi_R'/xi_R as an Euler--Gamma expression;
estimating the absolute prime-power tail;
using only fixed-support finite-section convergence;
presenting the Cauchy numerator or the ground/gap route as new;
replacing the source antisymmetrization by one bordered component.   (12.2)
```

The contributions of this document are narrower:

```text
the exact normalization crosswalk for the source-ground defect;
the two-boundary linear/product phase defect (6.11)--(6.14);
the pointwise Pick refinement of the earlier locally uniform
one-interval closure;
the weighted growing-support projection refinement (11.13)--(11.16). (12.3)
```

Theorem 7.1 is a classical Pick--Nevanlinna normal-family argument.  Its use
here is a pointwise sharpening and force audit, not a claim of a new general
theorem.  The general conclusion that safe-interval identification has
`Omega7` force was already proved in E101.019--E101.021.

## 13. Stop rules

```text
1. Use the exact P76.013 crosswalk.  Do not replace the linear
   antisymmetrization T_+(z)-T_+(-z) by one boundary component or by the
   bilateral product.

2. Do not spend further work on the absolute Euler tail.

3. Do not call safe-axis identification build-neutral: together with finite
   real-rootedness it already implies Omega7.

4. Do not split P-A-E into absolute estimates before the source cancellation.

5. Do not infer the weighted estimate (11.1) from qualitative L2 proximity on
   an interval whose support grows with lambda.

6. Do not use a gap estimate without the projection tail and weighted
   Rayleigh-excess/even-gap rate (11.16).

7. Test every proposed estimate for C_(L,N) on the planted build; it must fail
   there at a named source identity.                                 (13.1)
```

## 14. Revised work order

The live alternatives are now explicit.

```text
Route A - direct cell defect:
  derive a coupled source identity for C_core_(L,N);
  retain polar, archimedean and prime cells before cancellation;
  prove C_core_(L,N)->0 for zeta and exhibit the failed identity for the
  plant.

Route B - model-to-ground:
  prove eventual simple-even ground structure;
  estimate the projected model Rayleigh excess and next-even gap together;
  include the finite projection tail and reach (11.16), or prove (11.1) by a
  stronger norm.

Route C - divisor current:
  control K_(L,N) in a topology sensitive to principal parts;
  fix the one remaining affine normalization on a safe base point;
  commute the uncontracted divisor limit before parity contraction.  (14.1)
```

These are not three independent missing RH steps.  They are three
realizations of the same force-bearing identification.

## 15. Status

```text
proved:
  exact safe-axis source-ground determinant formulas;
  exact Gamma--Euler defect and closed-tail split;
  exact source core/exterior and root-free cofactor factorizations;
  curvature equals the uncontracted divisor-current defect;
  safe-axis Pick--Nevanlinna propagation from pointwise data;
  safe log-derivative identification on any safe interval implies Omega7;
  exact linear/product boundary phase defect;
  weighted model-to-ground closure theorem;
  projected Rayleigh-excess/even-gap sufficient bound;

autopsied:
  replacing the exact two-boundary antisymmetrization by one T_+ component
  or by the bilateral product;
  treating Euler-tail convergence as the missing arithmetic theorem;
  extracting M_src'/M_src from the eigenvalue equation as an independent
  estimate;

closed as infrastructure:
  determinant differentiation;
  regularization removal;
  Euler prime-power tail;
  force attribution of the safe-axis limit;

open and force-bearing:
  eventual/cofinal simple-even ground structure;
  C_core_(L,N)->0, equivalently a source-first safe identification;
  the weighted ground-model estimate (11.1), or another theorem implying it;
  TRUE-DIVISOR-IDENT, DIRECTIONAL-IDENT, the DISCRIMINANT and Omega7.       (15.1)
```
