# E101.078 - Finite jet compression, isolated rank jump and diagonal-lift wall

## 1. Decision

The full-jet detector of E101.077 admits an exact finite realization inside
the CCM matrix.  That realization separates three statements which must not
be conflated.

```text
ordinary jet-compressed positivity:
  exactly the original Weil form restricted to a dense core;

isolated-quartet jet rank:
  at most two on-line and eventually four off-line;

nonlinear discrimination after all zero contributions are aggregated:
  invalid, because distinct on-line orbits create cross terms and arbitrary
  high rank.                                                         (1.1)
```

The isolated rank jump is an exact, source-first falsifier.  It does not
survive aggregation.  A general additivity theorem proves that no continuous
polynomial of the aggregated jet matrix can both avoid cross terms and remain
nonlinear: additivity forces linearity, and a linear holomorphic orbit
response which vanishes on every real orbit vanishes on every orbit.

Thus the only surviving construction is a `JET-DIAGONAL-LIFT`: apply the
nonlinear exterior-power detector to each spectral orbit before summing.  The
ordinary CCM form supplies only the sum of the orbit matrices.  Tensoring
that sum creates product-measure cross terms, not the required diagonal.

Constructing the diagonal lift arithmetically without zero positions,
`1/Xi`, multiplicities or global Weil positivity is the new force-bearing
problem.  Proving its vanishing would prove RH directly.

## 2. Conventions and real jet frame

Put

```text
ell=L/2,
alpha=2/L,
h=2pi/L,
d_n=hn.                                             (2.1)
```

For `r>=0`, let

```text
kappa_n^((r))
=(1/L)integral_0^L
 (y-ell)^r k(y-ell)exp(-id_ny)dy.                  (2.2)
```

Define the phase-corrected jet column

```text
j_n^((r))=i^(-r)kappa_n^((r)).                     (2.3)
```

If

```text
K_L(t)=integral_(-ell)^ell k(x)exp(-itx)dx,         (2.4)
```

then E101.075(3.3) gives

```text
j_n^((r))
=(1/L)(-1)^n K_L^((r))(d_n).                       (2.5)
```

Hence every `j_n^((r))` is real.  The same fact follows from parity: the
centered Fourier coefficient is real in even order and purely imaginary in
odd order, and (2.3) removes the known phase.

For a Fourier section `|n|<=N` and jet depth `0<=r<=R`, define

```text
J_(N,R)=(j_n^((r)))_(|n|<=N,0<=r<=R).              (2.6)
```

The factorially weighted full-jet frame is obtained by right multiplication
with

```text
D_(R,tau)=diag(tau^r/r!)_(0<=r<=R), tau>0.         (2.7)
```

Finite positive diagonal rescaling does not change rank.

## 3. Exact CCM jet compression

For a build `B`, let `M_B` be the complete two-symbol CCM matrix, including
the cosine-symbol diagonal as required by E101.068 and E101.071.  Define

```text
Wcal_(B;N,R)
=J_(N,R)^T(P_NM_BP_N)J_(N,R).                      (3.1)
```

This is a real symmetric `(R+1) x (R+1)` matrix.

### Proposition 3.1 - No new positivity criterion

For every real symmetric matrix `A`,

```text
Tr(A Wcal_(B;N,R))                                 (3.2)
```

is one ordinary CCM/Weil test.  Positivity of (3.1) for every `R` and every
cofinal `N` is positivity of the same Weil form on the position-jet core.

### Proof

The CCM kernel representation has the form

```text
M_B(n,j)=W_B(q_(n,j))-mu delta_(n,j),               (3.3)
```

in the notation of E101.071(2.5)--(2.6).  Therefore

```text
Wcal_(B;N,R)(r,s)
=W_B(Q_(r,s)^N)-mu(J_(N,R)^TJ_(N,R))(r,s),         (3.4)

Q_(r,s)^N
=sum_(|n|,|j|<=N)j_n^((r))j_j^((s))q_(n,j).        (3.5)
```

Pairing (3.4) with `A` merely replaces the family (3.5) by its prescribed
linear combination.  This proves the first assertion.

For density, suppose `f in L^2(-ell,ell)` is orthogonal to

```text
{x^r k(x):r>=0}.                                   (3.6)
```

Then the finite complex measure

```text
dnu(x)=f(x)conj(k(x))dx                            (3.7)
```

has every polynomial moment equal to zero.  Polynomials are dense in the
continuous functions on the compact interval, so `nu=0`.  The Riemann
kernel is nonzero almost everywhere; hence `f=0`.  Thus (3.6) is dense.

After closure in the CCM form domain, positivity of every finite jet
compression is positivity of the original form on a core. `QED`

Consequently, none of the following changes the problem:

```text
J^TJ;
J^TM_B^2J;
a Cauchy or Pick Gram of the same columns;
a Hankel matrix of K_L derivatives;
all-depth positivity of Wcal_(B;N,R).               (3.8)
```

The first two are automatic positive Grams or squares, the third is RKHS
positivity, the fourth returns to Jensen--Laguerre structure, and the last is
the original Weil criterion on a dense core.

## 4. Exact quartet compression

For the controlled quartet

```text
P_zeta={zeta,-zeta,conj zeta,-conj zeta}           (4.1)
```

as a multiset, E101.071 gives

```text
delta M
=sum_(p in P_zeta)K_pR_pR_p^T,

R_p(n)=1/(d_n-p),

K_p
=alpha chi[1-cos(pL)]/2
=alpha chi sin(pL/2)^2.                            (4.2)
```

For finite `N,R`, define the Cauchy-jet matrix

```text
C_(N,R)(p,r)
=R_(p,N)^Tj^((r))
=i^(-r)sum_(|n|<=N)kappa_n^((r))/(d_n-p),          (4.3)

D_K=diag(K_p)_(p in P_zeta).                       (4.4)
```

### Theorem 4.1 - Finite rank-four factorization

The quartet perturbation of the jet compression is exactly

```text
delta Wcal_(N,R)
=C_(N,R)^T D_K C_(N,R).                            (4.5)
```

### Proof

Insert (4.2) into

```text
J^T(delta M)J.                                     (4.6)
```

Each rank-one term becomes

```text
K_p(J^TR_p)(R_p^TJ),                               (4.7)
```

which is (4.5). `QED`

The bilateral Cauchy evaluation of E101.075 gives

```text
C_(infinity)(p,r)
=-K_L^((r))(p)/[2sin(pL/2)].                       (4.8)
```

The trigonometric factors cancel exactly:

### Corollary 4.2 - Bilateral derivative Gram

```text
delta Wcal_(infinity,R)(r,s)
=(alpha chi/4)sum_(p in P_zeta)
 K_L^((r))(p)K_L^((s))(p).                         (4.9)
```

No conjugates occur inside an individual outer product because CCM uses its
real bilinear form.  The full quartet sum makes (4.9) real.

With factorial weights, (4.9) becomes

```text
D_(R,tau) delta Wcal_(infinity,R) D_(R,tau),       (4.10)
```

whose columns are the truncated Taylor jets

```text
{tau^r K_L^((r))(p)/r!}_(0<=r<=R).                 (4.11)
```

## 5. Exact collar control

Let

```text
epsilon_(p,N,r)
=C_(infinity)(p,r)-C_(N,R)(p,r)
=i^(-r)sum_(|n|>N)kappa_n^((r))/(d_n-p).           (5.1)
```

Set

```text
f_r(y)=(y-ell)^r k(y-ell),

B_(r,L)
={|f_r(L)-f_r(0)|+||f_r'||_1}/L.                  (5.2)
```

One integration by parts gives

```text
|kappa_n^((r))|<=B_(r,L)/(h|n|).                  (5.3)
```

If

```text
N>=2|p|/h,                                         (5.4)
```

then `|d_n-p|>=h|n|/2` on the tail and

```text
|epsilon_(p,N,r)|
<=4B_(r,L)/(h^2N).                                 (5.5)
```

For even `r`, the endpoint jump in (5.2) vanishes.  A second integration by
parts gives an `O(N^(-2))` tail with the corresponding first-derivative
jump and `L^1` second derivative.  For odd `r`, the `O(N^(-1))` rate is in
general optimal, exactly as predicted by E101.075(9.1)--(9.2).

For every fixed `tau`,

```text
sum_(r>=0)tau^(2r)B_(r,L)^2/(r!)^2<infinity,       (5.6)

sum_(r>=0)tau^(2r)|K_L^((r))(p)|^2/(r!)^2
<infinity.                                         (5.7)
```

The first follows from compact support and the factorial weight; the second
is the square-summable Taylor-jet lemma of E101.077.  Hence, for `p` in a
fixed compact set,

```text
||[C_N-C_infinity]D_(R,tau)||_(HS)=O(N^(-1)),       (5.8)

||D_(R,tau)[delta Wcal_N-delta Wcal_infinity]
  D_(R,tau)||_1=O(N^(-1)),                          (5.9)
```

uniformly in the cofinal jet depth after passing to the infinite weighted
column space.  No uniformity in an unbounded transverse parameter is claimed.

Thus the finite Fourier collar does not destroy the jet construction.  The
obstruction below is algebraic, not a missing tail estimate.

## 6. Independence of translated jets

### Lemma 6.1 - Translate-jet independence

Let `p_1,...,p_q` be distinct complex points.  Assume `k` is nonzero almost
everywhere on some interval inside `(-ell,ell)`.  Then the `q` sequences

```text
{K_L^((r))(p_j)}_(r>=0), 1<=j<=q,                  (6.1)
```

are linearly independent.

### Proof

Suppose

```text
sum_j lambda_jK_L^((r))(p_j)=0                     (6.2)
```

for every `r`.  The entire function

```text
F(w)=sum_j lambda_jK_L(p_j+w)                      (6.3)
```

has every derivative at zero equal to zero, so `F` is identically zero.
Using (2.4),

```text
F(w)=integral_(-ell)^ell
 k(x)[sum_j lambda_jexp(-ip_jx)]exp(-iwx)dx.       (6.4)
```

Uniqueness of the Fourier transform gives

```text
k(x)sum_j lambda_jexp(-ip_jx)=0                    (6.5)
```

almost everywhere.  On an interval where `k` is nonzero, the exponential
polynomial in (6.5) vanishes on a set with an accumulation point.  It is
identically zero, and distinct exponentials are linearly independent.  Thus
every `lambda_j=0`. `QED`

### Corollary 6.2

For each finite set of distinct points, there is a finite jet depth `R_0`
at which the corresponding truncated jet columns already have full rank.

No uniform `R_0` over all possible points is asserted.

## 7. On-line rank two and off-line rank four

Write

```text
zeta=gamma-i beta,
gamma>0,
beta>=0.                                           (7.1)
```

### Theorem 7.1 - Isolated-orbit rank dichotomy

For the quartet compression (4.5):

```text
beta=0  => rank(delta Wcal_(N,R))<=2 for every N,R;

beta>0  => for every fixed nondegenerate quartet there exist N_0,R_0
           such that rank(delta Wcal_(N,R))=4
           whenever N>=N_0 and R>=R_0.             (7.2)
```

### Proof

When `beta=0`, the multiset (4.1) contains only `gamma` and `-gamma`, each
twice.  Since `K_L` is real and even,

```text
K_L^((r))(-gamma)=(-1)^rK_L^((r))(gamma).          (7.3)
```

Thus (4.9) is the sum of one even-coordinate outer product and one
odd-coordinate outer product.  Its rank is at most two.  The finite matrix
already factors through the two Cauchy vectors `R_gamma,R_(-gamma)`, so the
same rank bound holds before the bilateral limit.

When `beta>0`, the four points in (4.1) are distinct for the nontrivial-zero
regime `gamma>0`.  Lemma 6.1 and Corollary 6.2 give full row rank four for
the limiting Cauchy-jet matrix at some finite `R_0`.  Every `K_p` in (4.2)
is nonzero away from the lattice resonance handled in E101.071.  Hence
`D_K` is invertible.  If `C` has row rank four, then `C^T` is injective and

```text
rank(C^TD_KC)=4.                                   (7.4)
```

A nonzero four-by-four minor persists under the collar convergence (5.8)
for all sufficiently large `N`. `QED`

The distinction starts at transverse scale `beta^2`, in agreement with
E101.071.  Rank detects the completed quartet, not a first transverse
derivative.

## 8. A valid isolated-quartet discriminator

Define

```text
Dcal_(N,R)^((3))
=||wedge^3(delta Wcal_(N,R))||_(HS)^2              (8.1)

=sum_(|I|=|J|=3)
 |det delta Wcal_(N,R)[I,J]|^2.                    (8.2)
```

### Corollary 8.1

For an isolated controlled orbit,

```text
on-line:  Dcal_(N,R)^((3))=0 for every N,R;

off-line: Dcal_(N,R)^((3))>0 for N,R sufficiently large.  (8.3)
```

This is a genuine finite algebraic discriminator.  It uses the same
predetermined jet family on both builds, keeps the exact collar, requires no
multiplicity choice, and cannot suffer quartet parity cancellation.

It is not additive.  Each three-by-three minor is cubic in the matrix
entries and (8.2) has degree six.

## 9. Why applying the discriminator after aggregation is false

Suppose a full build contributes orbit matrices `X_omega`.  CCM records

```text
X_total=sum_omega X_omega.                          (9.1)
```

Even under RH, every `X_omega` may have rank at most two while `X_total`
has arbitrarily large rank.  In general,

```text
||wedge^3(sum_omega X_omega)||^2
!=sum_omega||wedge^3X_omega||^2.                   (9.2)
```

The left side contains mixed minors from different real orbits and can be
strictly positive when every term on the right is zero.  Thus (8.1) applied
to the complete CCM matrix is a false positive under RH.

This is not repaired by subtracting finitely many lower moments: the mixed
terms occur at every degree once three independent on-line ranges are
present.

## 10. Additive-polynomial no-go

### Theorem 10.1 - Additivity forces linearity

Let `V` be a finite-dimensional real matrix space and let `P:V->R` be
continuous with

```text
P(0)=0,
P(X+Y)=P(X)+P(Y)                                   (10.1)
```

for all admissible independent insertion matrices, where those matrices
span `V` and the identity extends to their generated open set.  Then `P` is
linear.  If `P` is polynomial, the same conclusion follows algebraically.

### Proof

Equation (10.1) gives integer and rational homogeneity.  Continuity gives

```text
P(tX)=tP(X)                                        (10.2)
```

for every real `t`, and additivity then gives real linearity.

Alternatively, write a polynomial as a sum of homogeneous parts

```text
P=sum_(m>=0)P_m.                                   (10.3)
```

From (10.2),

```text
sum_m t^mP_m(X)=t sum_mP_m(X)                      (10.4)
```

for all `t`.  Hence `P_m=0` unless `m=1`. `QED`

Every linear matrix functional has the form

```text
P(X)=Tr(A^TX).                                     (10.5)
```

By Proposition 3.1 this is one ordinary Weil test.

There is a second rigidity.  For an individual pole response `X(p)`, the
scalar

```text
h_A(p)=Tr(A^TX(p))                                 (10.6)
```

is holomorphic or meromorphic in `p` away from the fixed Fourier lattice.
If the symmetric real-orbit response vanishes for every real `x`, then

```text
h_A(x)+h_A(-x)=0.                                  (10.7)
```

The identity theorem makes the even part in (10.7) vanish identically.
Adding conjugates then gives zero for every off-line quartet as well.

Therefore no continuous polynomial of the aggregated finite jet matrix can
simultaneously satisfy

```text
atomwise additivity;
zero response on every on-line orbit;
positive response on every off-line quartet.        (10.8)
```

Nonlinearity is necessary for discrimination; additivity is necessary to
avoid cross terms; the aggregated matrix cannot supply both.

## 11. The diagonal spectral lift

The valid abstract scalar is

```text
D_diag
=sum_(spectral orbits omega)
 ||wedge^3 X_omega||_(HS)^2.                       (11.1)
```

With factorial jet weights, the same definition extends cofinally in `R`
whenever the orbit sum converges.  The rank theorem gives

```text
D_diag>=0,
D_diag=0 <=> every nontrivial orbit is on-line.     (11.2)
```

Equation (11.2) is an RH-equivalent discriminant, not a proved arithmetic
identity.

To construct (11.1) from an aggregate, one would need a map which applies
the sixth-degree polynomial to each orbit before summation.  Ordinary
tensorization gives

```text
(sum_omega X_omega)^(tensor 6)
=sum_(omega_1,...,omega_6)
 X_(omega_1) tensor ... tensor X_(omega_6),         (11.3)
```

which contains every mixed tuple.  The desired term retains only

```text
omega_1=...=omega_6.                               (11.4)
```

A projection onto (11.4) is the missing diagonal spectral lift.

The one-level Weil formula, the CCM matrix and the screw-function realization
all provide the aggregate (9.1).  Standard product constructions provide
(11.3).  None of the inspected primary mechanisms supplies the exact
source-first projector (11.4) with the required conjugate-orbit matching.

There is a classical algebraic way to preserve root labels without listing
them: pass to the quotient algebra of a polynomial divisor and take a
Hermite--Bezout trace or signature.  It does not bypass the wall here.

```text
for a finite polynomial approximant:
  the Hermite--Bezout matrix is the classical real-rootedness criterion;

for all Taylor/Jensen approximants:
  its positivity is the Jensen--Laguerre--Polya hierarchy;

for the characteristic polynomial of a finite selfadjoint CCM section:
  the roots are real build-neutrally, while identifying their cofinal divisor
  with the Xi divisor is precisely IDENT.                            (11.5)
```

Thus quotient-algebra diagonalization either returns a known RH-equivalent
criterion or moves the entire force into the same finite-to-infinite
identification already isolated by the program.

## 12. Why the diagonal lift is the force-bearing step

A zero-adapted construction can obtain (11.4) immediately by labelling the
zeros, using spectral projectors, or inserting confluent Cauchy duals.  Those
operations require some combination of

```text
zero positions;
multiplicities;
1/Xi or 1/Xi^((m))(rho);
a global selfadjoint spectral resolution;
Hermite--Biehler or Weil/Pick positivity.           (12.1)
```

Every item in (12.1) violates the root-free source-first rule or imports an
RH-equivalent theorem.

An admissible `JET-DIAGONAL-LIFT` must instead be derived from the finite
Gamma--Euler/CCM data and must prove, not assume,

```text
an exact diagonal extraction before aggregation;
conjugate and parity orbit matching;
cofinal factorial jet convergence;
the absence or cancellation of every mixed prime/archimedean term;
the arithmetic value or sign which forces D_diag=0.                  (12.2)
```

If (12.2) proves `D_diag=0`, then (11.2) proves RH directly.  H0 therefore
predicts that one clause of (12.2) must carry full RH strength.  The present
work locates that clause rather than hiding it in a Gram positivity claim.

The internal no-go E72.355--E72.356 is consistent with this conclusion: a
node-blind universal projector cannot manufacture the spectral diagonal.
Divisor-specific structure is necessary, but it must be obtained without
localizing the divisor.

## 13. Terminal-row bridge remains separate

Even a successful construction of (11.1) would not automatically prove the
specific terminal scalar of the LP+IDENT chain.  To remain within that
chain, one would still need an equality or signed comparison with

```text
p_(N,z)e_N/B_(k_N)(z)                              (13.1)
```

in the notation of E101.045, uniformly on the declared safe set and in the
ordered limit

```text
N->infinity, then R->infinity.                     (13.2)
```

The density theorem of Proposition 3.1 and the collar bounds (5.8)--(5.9)
do not control the terminal inf-sup constant of E101.045.  They therefore do
not imply DIRECTIONAL-IDENT.

There are two logically distinct possible closures:

```text
direct closure:
  construct D_diag arithmetically and prove D_diag=0, obtaining RH without
  the terminal row;

chain closure:
  identify the diagonal lift with the actual terminal scalar and use it to
  prove DIRECTIONAL-IDENT.                            (13.3)
```

Both require the same new diagonal extraction; the second also requires the
terminal identification.

## 14. Stop rule

The following routes are now frozen:

```text
ordinary all-depth jet Gram positivity;
J^TJ, J^TM^2J and Cauchy/Pick Grams;
Hankel or Wronskian positivity of the derivative columns;
wedge^3 applied after summing all spectral atoms;
another polynomial of the aggregated jet matrix;
tensor powers without an exact diagonal projector.                  (14.1)
```

Further work is justified only if it supplies one of:

```text
an exact Gamma--Euler formula for the diagonal tensor (11.4);
a connected-cumulant identity which cancels every mixed orbit term;
a finite spectral-diagonal projector derived without zero data;
an exact terminal-row identity which realizes the same diagonal lift. (14.2)
```

## 15. Status

```text
proved:
  real finite jet frame;
  exact CCM jet compression;
  dense-core equivalence with the original Weil form;
  exact rank-four quartet factorization;
  factorially weighted collar convergence;
  independence of translated complete jets;
  isolated on-line rank <=2 and off-line rank 4;
  positive exterior-cube discriminator for one isolated quartet;
  additive-polynomial no-go;
  failure of nonlinear discrimination after aggregation;

rejected:
  jet-Gram positivity as a new RH criterion;
  a polynomial of the aggregate as an atomwise detector;
  tensorization without diagonal extraction;

new open target:
  JET-DIAGONAL-LIFT;

additional open bridge:
  identification with the actual terminal row;

still open:
  DIRECTIONAL-IDENT and Omega7.
```
