# E101.079 - Exact phase diagonalization and the divisor wall

## 1. Decision

The cross-term obstruction of E101.078 has an exact algebraic solution.
It does not require Kronecker recurrence, a nonresonance hypothesis, or a
limit which matches all spectral phases at once.

Let

```text
P_3(X)=||wedge^3 X||_(HS)^2.                       (1.1)
```

This is a homogeneous polynomial of degree six.  If an absolutely summable,
or otherwise explicitly mean-admissible, character signal

```text
F(u)=sum_omega X_omega exp(i<lambda_omega,u>)       (1.2)
```

is already available with distinct real labels `lambda_omega`, then five
independent invariant means applied to the six-linear polarization of
`P_3` retain exactly

```text
sum_omega P_3(X_omega).                            (1.3)
```

Every mixed orbit tuple disappears.  There is also a symmetry-covariant
version which starts with individual pole atoms and assembles their complete
quartets inside the same average.

Thus `JET-DIAGONAL-LIFT` splits into two logically different tasks:

```text
phase diagonalization:
  closed exactly and unconditionally;

bounded orbit-character lift:
  open, arithmetic and force-bearing.               (1.4)
```

The canonical two-dimensional character uses

```text
q_p=(Re p,Im p).                                    (1.5)
```

It is unitary and separates points, but it is nonholomorphic in `p`.
Poincare--Lelong constructs the resulting signal exactly from
`log|Xi|`; equivalently it uses the full divisor current.  This is not a
source-first Gamma--Euler construction.  An additional integration exposes
the hidden factor `Xi'/Xi`.

Two independent no-go theorems delimit the wall.

```text
1. No locally bounded translation-invariant holomorphic approximate
   diagonal can separate the nonzero differences of real Xi zeros from
   zero.  The same holds for recentered slices with a height-uniform bound.

2. In the actual terminal system, an isolated rank-four quartet reaches a
   multirow terminal compound, but the moving dual identity collapses its
   additive rank-four response to a rank-one terminal residual.
                                                               (1.6)
```

The new admissible target is therefore
`BOUNDED-ORBIT-CHARACTER-LIFT`: derive (1.2), or its pole-level form, from
finite Gamma--Euler/CCM data without `log|Xi|`, `Xi'/Xi`, zero locations,
spectral projectors, or determinant convergence to `Xi`.

## 2. The exterior-cube polynomial

Let `X` be a real symmetric finite matrix.  Its singular values squared are
the eigenvalues of `X^2`, so

```text
P_3(X)
=e_3(spec(X^2))
=1/6[(Tr X^2)^3-3(Tr X^2)(Tr X^4)+2Tr X^6].        (2.1)
```

Equivalently,

```text
P_3(X)
=sum_(|I|=|J|=3)|det X_(I,J)|^2
>=0.                                               (2.2)
```

In particular,

```text
P_3(X)=0 <=> rank X<=2.                             (2.3)
```

Let `p_3` denote the unique symmetric six-linear form on the complexification
of the matrix space satisfying

```text
p_3(X,X,X,X,X,X)=P_3(X).                           (2.4)
```

It may be defined without choosing coordinates by

```text
p_3(X_1,...,X_6)
=1/6! partial_(t_1)...partial_(t_6)
 P_3(sum_(j=1)^6 t_jX_j)|_(t=0).                   (2.5)
```

The complexification in (2.5) is used only during phase averaging.  The
final value in every application below is real and nonnegative.

## 3. Five independent phases extract the diagonal

For a bounded almost-periodic function on `R^d`, write

```text
M_u f
=lim_(T->infinity)(2T)^(-d)
 integral_([-T,T]^d)f(u)du                         (3.1)
```

whenever the limit exists.  On characters,

```text
M_u exp(i<lambda,u>)
=1 if lambda=0,
=0 otherwise.                                      (3.2)
```

### Theorem 3.1 - Exact six-fold diagonal projector

Let `Omega` be finite or countable.  Suppose

```text
all X_omega belong to one finite-dimensional real symmetric matrix space,

lambda_omega in R^d,
lambda_omega=lambda_nu <=> omega=nu,                (3.3)

sum_omega ||X_omega||<infinity.                    (3.4)
```

Define the uniformly convergent signal

```text
F(u)=sum_omega X_omega exp(i<lambda_omega,u>).       (3.5)
```

Then

```text
M_(u_1)...M_(u_5)
 p_3(F(u_1),F(u_2),F(u_3),F(u_4),F(u_5),
     F(-u_1-u_2-u_3-u_4-u_5))
=sum_omega P_3(X_omega).                            (3.6)
```

### Proof

Absolute convergence permits expansion of the left side into a six-fold
sum.  The phase of a tuple `(omega_1,...,omega_6)` is

```text
product_(j=1)^5
 exp(i<lambda_(omega_j)-lambda_(omega_6),u_j>).     (3.7)
```

The five means in (3.2) impose the five separate equations

```text
lambda_(omega_j)=lambda_(omega_6), 1<=j<=5.         (3.8)
```

Injectivity in (3.3) gives

```text
omega_1=...=omega_6.                               (3.9)
```

The surviving summand is (2.4). `QED`

### Corollary 3.2 - No additive resonance problem

A one-parameter sixth moment imposes only an additive relation among six
frequencies and retains many mixed tuples.  Equation (3.6) imposes five
pairwise equality relations.  Therefore it requires neither rational
independence of the labels nor a quantitative recurrence theorem.

The Tower-versus-geometric mismatch of the almost-periodic gauge route is
not present in (3.6).  Its replacement burden is the prior construction of
the absolutely summable or mean-admissible signal (3.5).

## 4. Pole-level quartet assembly

The preceding theorem assumes that each `X_omega` has already been assembled
from one symmetry orbit.  The same independent-phase idea can perform the
assembly and the diagonal extraction simultaneously.

Identify `C` with `R^2` by

```text
q_p=(Re p,Im p).                                    (4.1)
```

Let the Klein four group be represented on `R^2` by

```text
G={I,-I,C,-C},
C=diag(1,-1).                                       (4.2)
```

These matrices implement

```text
p, -p, conj(p), -conj(p).                           (4.3)
```

Let `Y_p` be the individual pole matrix and suppose

```text
F(u)=sum_p Y_p exp(i<q_p,u>)                        (4.4)
```

converges absolutely, the pole multiset is `G`-invariant, and the map
`p -> q_p` is injective on the spectral multiset after multiplicities have
been absorbed into `Y_p`.  Assume also that the atoms are symmetry-covariant
and every orbit sum

```text
X_O=sum_(p in O)Y_p                                (4.4a)
```

is a real symmetric matrix in the space of Section 2.  These hypotheses hold
for the quartet atoms of E101.078; they are not asserted for arbitrary
complex matrices.

### Theorem 4.1 - Symmetry-covariant diagonal projector

Define

```text
A_G(F)
=sum_(g_2,...,g_6 in G)
 M_(u_2)...M_(u_6)
 p_3(
   F(-sum_(j=2)^6 g_j^T u_j),
   F(u_2),...,F(u_6)).                              (4.5)
```

For every free quartet orbit `O`, its contribution to (4.5) is exactly

```text
P_3(X_O),
X_O=sum_(p in O)Y_p.                                (4.6)
```

An orbit with stabilizer of size `h` contributes

```text
h^5 P_3(X_O).                                       (4.7)
```

In the Xi application the only nonfree nontrivial orbits are on the real
axis.  Indeed, a zero on the imaginary axis in the `z` coordinate would give
a real zero of `xi(s)` with `0<s<1`, which does not occur.  E101.078 gives
`rank X_O<=2` for the real-axis orbit matrices, so (4.7) vanishes.
Consequently,

```text
A_G(F)=sum_(off-line orbits O)P_3(X_O).             (4.8)
```

### Proof

After expanding (4.5), the mean in `u_j` imposes

```text
q_(p_j)=g_jq_(p_1), 2<=j<=6.                       (4.9)
```

This is the exact quartet relation, not an additive resonance.  For a fixed
`p_1` in a free orbit, summing `g_j` makes each of the last five arguments
equal to `X_O`.  Summing the first atom over `p_1 in O` makes the first
argument `X_O` as well.  Multilinearity and (2.4) give (4.6).

If the stabilizer has size `h`, each orbit point occurs `h` times in each of
the last five group sums, giving (4.7). `QED`

This theorem removes two earlier concerns at once:

```text
the pole atoms need not be grouped in advance;
the spectral labels need no gap and no arithmetic independence.       (4.10)
```

The required input is now exactly the absolutely summable, or otherwise
mean-admissible, two-dimensional signal (4.4).

## 5. Cumulants are equivalent only after labels exist

There is a probabilistic coordinate for the same projector.  Let
`epsilon_omega` be independent Rademacher variables and put

```text
S=sum_omega epsilon_omega X_omega.                  (5.1)
```

Under (3.4), this series converges absolutely almost surely and all tensor
expansions below are justified.

Since the sixth scalar cumulant of a Rademacher variable is `16`, independence
gives

```text
Cum_6(S)=16sum_omega X_omega^(tensor 6).            (5.2)
```

Contracting (5.2) with `p_3` yields

```text
16sum_omega P_3(X_omega).                           (5.3)
```

This does not construct the missing lift.  Assigning one independent random
sign to each spectral orbit already presupposes the orbit decomposition.
The five-phase theorem is stronger operationally because a deterministic
character signal suffices, but that signal still contains the labels.

Ordinary log determinants do not fix the problem.  For

```text
M=sum_omega X_omega,                                (5.4)
```

one has

```text
log det(I+tM)
=sum_(k>=1)(-1)^(k+1)t^k/k
 sum_(omega_1,...,omega_k)
 Tr(X_(omega_1)...X_(omega_k)).                     (5.5)
```

Taking a logarithm keeps connected cyclic words, including mixed orbit
words.  It does not impose equality of their labels.

The failure is information-theoretic, not merely algebraic.  The same
aggregate has the two decompositions

```text
I_4 as one atom:              P_3(I_4)=4;
I_4=sum_(j=1)^4 E_(j,j):     sum_j P_3(E_(j,j))=0.  (5.6)
```

No function of the aggregate alone can distinguish (5.6).  A direct-sum
determinant would be additive by blocks, but supplying those blocks is the
diagonal lift itself.

## 6. Canonical Poincare--Lelong realization

Write the completed function in the real-zero coordinate used throughout
E101.074--E101.078.  Its nontrivial zeros lie in

```text
|Im z|<1/2.                                         (6.1)
```

Let

```text
a_r(z)=Xi^((r))(z)/r!,
G_M(z)=sum_(0<=r<s<=M)
       Im(a_r(z)conj(a_s(z)))^2.                   (6.2)
```

Then `G_M>=0`, `G_M` increases with `M`, and E101.077 gives

```text
G_Xi(z)=lim_(M->infinity)G_M(z),
G_Xi(z)=0 <=> z is real.                            (6.3)
```

Choose a smooth real function `eta` of compact support such that

```text
eta(y)=1 for |y|<=1/2.                              (6.4)
```

### Theorem 6.1 - Exact jet-potential identity

For every finite `M`,

```text
D_M
:=1/(2pi) integral_C
 log|Xi(z)| Delta[eta(Im z)G_M(z)]dA(z)
=sum_(Xi(rho)=0)m_rho G_M(rho).                    (6.5)
```

The integrals and sums converge.  Moreover,

```text
D_M increases to D,

D=sum_rho m_rho G_Xi(rho)
 =1/(2pi)integral_C
   log|Xi| Delta(eta G_Xi)dA,

D>=0,
D=0 <=> every Xi zero is real <=> RH.               (6.6)
```

### Proof

The Poincare--Lelong identity in one complex variable is

```text
Delta log|Xi|
=2pi sum_rho m_rho delta_rho.                      (6.7)
```

Distributional integration by parts, (6.4), and (6.7) give (6.5).
Near a zero, `log|Xi|` has only a logarithmic singularity and is locally
integrable.

For each fixed horizontal strip and `|alpha|<=2`, the circular jet formula
of E101.077 together with Stirling bounds for the completed function gives

```text
|partial^alpha G_Xi(x+iy)|
<=C_(H,alpha)(1+|x|)^A exp(-pi|x|), |y|<=H.        (6.8)
```

The same estimate holds uniformly for the truncations:

```text
sup_M |partial^alpha G_M(x+iy)|
<=C'_(H,alpha)(1+|x|)^A exp(-pi|x|),               (6.9)

G_M->G_Xi in weighted C^2 on |y|<=H.              (6.10)
```

To see this, differentiate the finite minor sum.  A derivative of order at
most two shifts each Taylor index by at most two and introduces only a
quadratic polynomial in that index.  Choose a Taylor circle of radius greater
than one, for example radius four.  Its geometric weight absorbs every such
polynomial.  Parseval and Cauchy estimates then bound the resulting coefficient
tails by circle integrals of `Xi` and its first two derivatives at
`z+4exp(i theta)`.  Uniform Stirling bounds on the enlarged strip give (6.9),
and the geometric coefficient tails give (6.10).

Hadamard factorization and the order-one zero count also give, on every fixed
strip containing the support of `eta`,

```text
integral_(j<=|x|<j+1)|log|Xi(x+iy)||dA
<=C_H(1+j)^B.                                      (6.11)
```

This includes the locally integrable logarithmic singularities at the
`O(log j)` zeros in a unit strip box.  Equations (6.9)--(6.11) supply an
integrable exponential majorant for

```text
log|Xi| Delta(eta G_M).                             (6.12)
```

The zero count `N(T)=O(Tlog T)` makes the spectral sum absolutely
convergent.  Insert a compact cutoff in `x` when applying (6.7), pass the
cutoff to infinity using (6.9)--(6.11), and then pass `M` to infinity by
weighted `C^2` convergence and dominated convergence.  This proves the
integral equality in (6.6).  Monotone convergence applies separately to the
nonnegative spectral sums in (6.2), and (6.3) proves the last equivalence in
(6.6). `QED`

The elementary product rule makes the bulk content explicit:

```text
Delta(eta G_M)
=eta Delta G_M+2eta' partial_yG_M+eta''G_M.         (6.13)
```

The volume term `eta Delta G_M` is generally nonzero.  Poincare--Lelong
does not turn the criterion into a boundary identity.

## 7. The hidden divisor inverse

The appearance of `log|Xi|` in (6.5) is not a harmless root-free
replacement.  It is exactly the potential of the divisor.  With the
normalization

```text
barpartial(1/(z-rho))=pi delta_rho,                (7.1)
```

one has

```text
barpartial(Xi'/Xi)
=pi sum_rho m_rho delta_rho.                       (7.2)
```

Therefore another integration by parts yields

```text
D_M
=-1/pi integral_C
 (Xi'(z)/Xi(z))barpartial[eta(Im z)G_M(z)]dA(z).    (7.3)
```

Equation (7.3) exhibits the zero-adapted inverse hidden in (6.5).  It also
shows why the construction is unavailable from a one-level CCM aggregate:
it evaluates the complete logarithmic derivative, including every local
principal part.

A strip boundary form makes the same obstruction visible.  Recall the
coordinate convention

```text
Xi(z)=xi(1/2+iz).                                   (7.4a)
```

For `H>1/2`, Green's identity and the functional symmetries give

```text
2pi D_M
=integral_(|Im z|<H)log|Xi(z)|Delta G_M(z)dA(z)

 +2integral_R
   [G_M partial_ylog|Xi|-log|Xi|partial_yG_M]_(z=x+iH)dx.
                                                               (7.4)
```

At the top boundary `z=x+iH`, the direct argument of `xi` is
`1/2-H+ix`.  The functional equation followed by conjugation gives

```text
log|xi(1/2-H+ix)|=log|xi(1/2+H+ix)|.               (7.4b)
```

Thus, with `a=H+1/2>1`, both the boundary value and its outward normal
derivative are respectively `log|xi(a+ix)|` and
`partial_a log|xi(a+ix)|`; the two changes of variable produce no residual
sign.  On this right-hand line the Euler--Gamma expansion is absolutely
convergent:

```text
log|xi(s)|
=-log 2+log|s(s-1)|-(a/2)log pi+log|Gamma(s/2)|
 +sum_(p,k>=1)p^(-ka)cos(kxlog p)/k,               (7.5)

partial_a log|xi(s)|
=Re[1/s+1/(s-1)-(1/2)log pi+(1/2)psi(s/2)]
 -sum_(n>=2)Lambda(n)n^(-a)cos(xlog n).             (7.6)
```

For a wider fixed boundary strip, the required finite jets also have
absolute Euler--Gamma expansions.  The first term in (7.4), however, remains
inside the critical strip.  Since `G_M` is not harmonic, neither the
functional equation nor Green's identity removes it.

Thus Poincare--Lelong closes the analytic construction of the diagonal but
not its arithmetic evaluation.

## 8. Real finite determinants and the exact convergence wall

Let `F_N` be one of the real-zero finite determinants produced by the
selfadjoint CCM construction.  Applying (6.7) to `F_N` gives

```text
1/(2pi)integral_C
 log|F_N(z)|Delta[eta G_M(z)]dA(z)=0,              (8.1)
```

because every zero of `F_N` is real and `G_M` vanishes on the real axis.
Consequently, the sufficient transfer statement is

```text
WEIGHTED-JET-POTENTIAL-CONVERGENCE(M):

integral_C [log|F_N|-log|Xi|]
 Delta[eta G_M]dA ->0.                             (8.2)
```

Equations (8.1)--(8.2) imply `D_M=0`.  If (8.2) is proved for every `M`,
then (6.6) proves RH.

Statement (8.2) is one scalar weighted convergence statement, not a weaker
topology.  Local `L^1` convergence implies it only after a separate uniform
tail-tightness estimate against the exponentially decaying but noncompact
weight `Delta(eta G_M)`.  Conversely, (8.2) alone controls no other test
function.  Despite this narrowness, it implies the RH-equivalent conclusion
after the declared all-depth limit.  It must therefore be treated as an
RH-strength target, not as build-neutral compactness.

The distinction matches the primary CCM result.  Finite regularized
determinants have only real zeros, while rigorous convergence of their zeros
or determinants to the Riemann divisor is explicitly a missing step whose
proof would establish RH.  Equation (8.2) is the exact scalar projection of
that missing convergence selected by the jet detector.

No uniform positive gap is available.  From (6.8) and real-axis vanishing,

```text
G_Xi(gamma+ibeta)
<=C(1+|gamma|)^Aexp(-pi|gamma|),

G_Xi(x+ibeta)=O_x(beta^2) as beta->0.              (8.3)
```

A hypothetical off-line zero can therefore contribute arbitrarily little
when it is high or close to the line.  Finite verification cannot provide a
uniform remainder gap for (6.6).

## 9. Exact terminal compound for an isolated quartet

There is a finite terminal realization of the rank jump, provided the
quartet matrix has already been isolated.

Let

```text
A_N=[ell_N;M_N],
iota(u)=(0,u),                                     (9.1)
```

where `A_N` is the normalized square boundary system, and define

```text
Pcal_Nu(z)=c_zA_N^(-1)iota(u)=p_(N,z)u.             (9.2)
```

E101.048 makes `Pcal_N` injective.  Let `J_R` be the finite jet frame and
let `delta M_Q` be one isolated quartet response.  By E101.078,

```text
rank(delta M_Q J_R)=4 eventually for an off-line quartet,
rank(delta M_Q J_R)<=2 for an on-line orbit.        (9.3)
```

Injectivity of (9.2) preserves these ranks as functions of `z`.  Hence a
finite set of safe evaluations `Z=(z_1,...,z_q)` and jet columns can be
chosen so that

```text
T_(Z,R)
=[p_(N,z_a)delta M_Qj_(r_b)]_(a,b)                 (9.4)
```

has rank four off-line, whereas every `3 x 3` minor vanishes on-line.

For a square selected minor, the exact cofactor formula is

```text
det T_(Z,R)
=(-1)^q
 det[[A_N,iota delta M_QJ_R],[C_Z,0]]/det A_N.     (9.5)
```

Thus `ISOLATED-TERMINAL-COMPOUND` is algebraically closed.

## 10. What the moving terminal identity actually collapses

The isolated formula (9.4) is not the terminal observable of the arithmetic
system.  For the complete build matrix,

```text
p_(B,z)M_B=q_(B,z)=c_z-B_B(z)ell_N.                (10.1)
```

Therefore

```text
[p_(B,z_a)M_Bj_(r_b)]
=C_ZJ_R-B_B(Z)(ell_NJ_R).                          (10.2)
```

All build dependence in (10.2) is a rank-one update.  Between two builds,

```text
T_(B_1)-T_(B_0)
=-[B_(B_1)(Z)-B_(B_0)(Z)](ell_NJ_R).               (10.3)
```

Infinitesimally,

```text
dot p M+p dot M=-dot B ell_N.                       (10.4)
```

The additive term `p dot M J_R` can have rank four before the row moves, but
the complete first variation in (10.4) is the rank-one matrix
`-dot B(Z)(ell_NJ_R)`.  This is the exact collapse proved here.  Retaining the
isolated additive response requires keeping `dot M=delta M_Q` labelled before
the aggregate is formed; that is the diagonal lift.

The rank-one difference (10.3) does not make exterior compounds invariant.
For example,

```text
A=diag(1,1,0),
E=E_(3,3),
rank E=1,
wedge^3 A=0,
wedge^3(A+E)=1.                                    (10.5)
```

Hence nonlinear mixed terms between the baseline and the rank-one update can
change a third compound.  Equations (10.1)--(10.4) prove neither cancellation
of every terminal minor nor absence of an aggregate nonlinear discriminator.
They prove only that such a discriminator cannot be justified by carrying
the isolated rank-four *linear* response unchanged through the moving dual
row.

There is no single-row realization of the isolated third compound: one
terminal row has scalar output.  A proposed multirow escape must therefore
establish its own cofinal exterior lower bound and eliminate the baseline
mixed terms in (10.5).  That obligation is analogous to the directional
inf-sup burden of E101.045, but no equivalence with `RDC-4` is proved here.
Finite existence of a nonzero isolated minor supplies no such bound.

E101.084 subsequently resolves this remaining compound audit.  For
`T_B=C-B_B(Z)(ell_NJ_R)`, every compound vector is affine in the sampled
boundary vector:

```text
C_k(T_B)=C_k(C)-L_kB_B(Z).                        (10.6)
```

Under a finite rank condition realized by sufficiently many safe
evaluations, `L_3` is injective.  Hence the complete third-compound vector is
only a linear recoding of the sampled IDENT data.  Its squared norm is a
quadratic boundary energy which can be nonzero for an all-real aggregate,
while the compound of a build difference vanishes in order at least two.
Thus the terminal compound does not provide an independent rank-four bypass.

## 11. Normal-family no-go for holomorphic diagonal kernels

The Xi divisor has distinct real zeros with nonzero gaps tending to zero.
For example, a positive proportion of its zeros are known unconditionally
to be simple and on the critical line.  If `gamma_j` denotes a suitable
sequence of consecutive real zeros, then

```text
delta_j=gamma_(j+1)-gamma_j !=0,
delta_j->0.                                         (11.1)
```

### Theorem 11.1 - Holomorphic diagonal extraction must blow up

Let `D(0,r)` be a fixed disk containing all sufficiently small `delta_j`.
Suppose `K_N` is holomorphic on that disk and

```text
K_N(0)->1,
K_N(delta_j)->0 for every fixed j.                  (11.2)
```

Then `{K_N}` is not locally bounded near zero.

### Proof

If it were locally bounded, Montel's theorem would give a subsequence
converging uniformly on compact subsets to a holomorphic function `K`.
Equation (11.2) would give

```text
K(0)=1,
K(delta_j)=0 for every j.                           (11.3)
```

The zeros in (11.3) accumulate at zero.  The identity theorem would force
`K` to vanish identically, contradicting `K(0)=1`. `QED`

There is also a quantitative form which allows the index to depend on the
small difference.  If

```text
K_N(0)=1,
|K_(N_j)(delta_j)|<=eta<1,                          (11.4)
```

and the family is bounded by `M_R` on `|z|<=R`, Cauchy's estimate gives,
for `|delta_j|<=R/2`,

```text
1-eta
<=|K_(N_j)(delta_j)-K_(N_j)(0)|
<=2M_R|delta_j|/R.                                 (11.5)
```

Thus

```text
M_R>=R(1-eta)/(2|delta_j|)->infinity.              (11.6)
```

The standard one-phase kernel displays the transverse explosion:

```text
K_T(z)=sin(Tz)/(Tz),
K_T(iy)=sinh(Ty)/(Ty).                              (11.7)
```

Theorem 11.1 applies directly to translation-invariant projectors whose
two-atom kernel depends holomorphically on the spectral difference.  It also
applies to an absolute-position-dependent multivariable family if, after
recentering at each real zero, the corresponding one-difference slices obey
one height-independent local bound.  Under either hypothesis the available
exits are:

```text
lose local boundedness;
develop moving poles;
use a nonholomorphic two-dimensional label;
allow recentered norms to grow with spectral height;
use absolute-position adaptation not reducible to a difference kernel;
or insert divisor-dependent interpolation data.    (11.8)
```

The first two exits require a new signed cancellation at exactly the scale
where off-line characters grow.  Divisor-dependent interpolation inserts the
answer by construction.  A nonholomorphic label or height-dependent family
does not by itself reconstruct the divisor; it remains admissible only if its
complete signal is obtained from the source before zero selection.

The scope is important.  The theorem rejects a universal holomorphic
translation-invariant projector normalized to one on the atomwise diagonal,
and uniformly normal recentered variants.  It does not reject an arbitrary
absolute-position-dependent multivariable kernel.  It also does not reject a
specific contracted identity whose diagonal value already vanishes on every
on-line orbit after `P_3` is applied, or a nonnormal family whose growth is
cancelled exactly before the limit.  These are the exits retained in (14.3).

## 12. The bounded-character trilemma

For an individual pole `p=x+iy`, three natural labels behave differently.

```text
holomorphic phase exp(itp):
  compatible with a one-level explicit formula, but has modulus exp(-ty)
  and grows exponentially in one time direction off-line;

ordinate phase exp(it Re p):
  unitary, but does not separate distinct zeros with the same ordinate;

two-dimensional phase exp(i[t Re p+s Im p]):
  unitary and point-separating, but nonholomorphic in p.               (12.1)
```

The open mapping theorem makes this structural: a holomorphic real-valued
label on a connected open set is constant.  Hence a nonconstant unitary
character label cannot simultaneously be holomorphic in the spectral
variable.

The two-dimensional signal can be written without listing zeros as a divisor
current.  Let `chi` be a scalar compact cutoff and `Y(z)` a smooth matrix
weight on its support.  Then

```text
F_chi(u)
=1/(2pi)integral_C
 log|Xi(z)|
 Delta[chi(z)Y(z)exp(i<q_z,u>)]dA(z),              (12.2)

q_z=(Re z,Im z).                                   (12.3)
```

Poincare--Lelong turns (12.2), term by term, into the cutoff signal

```text
F_chi(u)=sum_rho m_rho chi(rho)Y(rho)
                         exp(i<q_rho,u>).           (12.4)
```

Fourier inversion of all `u` recovers the weighted measure
`sum m_rho chi(rho)Y(rho)delta_(q_rho)`.  It recovers the naked divisor only
where the matrix weight is nondegenerate and can be divided out.  Passing to
a global signal requires cutoffs `chi_R->1`, summability or bounded variation
uniform in `R`, and an interchange of this limit with all five invariant
means.  None of those global passages is supplied by (12.2).  Thus (12.2) is
an exact cutoff realization of (4.4), but not a bypass: it is another form of
the divisor potential in Section 7.

## 13. Literature gate

The following primary results delimit what is and is not supplied by recent
work.

1. Balazard--Saias--Yor and the generalized Littlewood-formula criteria of
   Sekatskii--Beltraminelli--Merlini already turn logarithmic integrals of
   zeta into positive sums over off-line zeros.  Bui--Lester--Milinovich give
   quantitative truncation results for the Balazard--Saias--Yor criterion
   under RH; those rates are not an unconditional input here.
   Section 6 is a jet-weighted Poincare--Lelong member of this broad
   logarithmic family, not a new reason for its value to vanish.

2. Connes--Consani--Moscovici construct finite selfadjoint operators and
   real-zero regularized determinants from truncated Weil forms.  Their
   stated missing step is rigorous convergence of the determinants or their
   zeros to the Riemann divisor; such convergence would establish RH.
   Equation (8.2) is a selected weak projection of that same step.

3. Recent pair-correlation work can obtain proportions of critical zeros
   under narrow-box hypotheses, and the pair-correlation conjecture can
   force density one on the line.  Density one does not exclude a single
   off-line orbit and therefore cannot imply (4.8) is zero.

4. Conrey--Snaith higher-correlation formulas use the ratios conjecture.
   Lagarias--Rodgers show that the presently known higher-correlation
   information does not rule out their Alternative Hypothesis.  This is the
   precise nonuniqueness statement used here.  Determinantal cumulant formulas
   require a determinantal random law which is not known for zeta zeros.

5. The unconditional positive proportion of simple critical zeros is used
   only to prove the local no-go (11.1).  It contributes no zero-location
   input toward RH.

Primary references:

```text
Balazard--Saias--Yor:
  https://doi.org/10.1006/aima.1998.1797

Sekatskii--Beltraminelli--Merlini:
  https://arxiv.org/abs/0806.1596

Bui--Lester--Milinovich:
  https://arxiv.org/abs/1306.0856

Connes--Consani--Moscovici:
  https://arxiv.org/abs/2511.22755

Conrey:
  https://doi.org/10.1515/crll.1989.399.1

Pratt--Robles--Zaharescu--Zeindler:
  https://arxiv.org/abs/1802.10521

Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh:
  https://arxiv.org/abs/2501.14545

Goldston--Lee--Schettler--Suriajaya:
  https://arxiv.org/abs/2503.15449

Conrey--Snaith:
  https://arxiv.org/abs/0803.2795

Lagarias--Rodgers:
  https://arxiv.org/abs/1905.12123

Suzuki:
  https://arxiv.org/abs/2606.09096

Andersson:
  https://arxiv.org/abs/math/0412446

Bleher--Shiffman--Zelditch:
  https://arxiv.org/abs/math-ph/9903012

Thomas:
  https://arxiv.org/abs/1309.1275
                                                               (13.1)
```

The five-phase projector itself is a classical convolution and character-
orthogonality identity combined with polarization; Poincare--Lelong with a
jet weight is likewise a classical divisor-current specialization.  No exact
CCM-jet instance of the joint pole-level quartet assembly was located, and no
inspected primary source supplies that assembly together with a source-first
bounded two-dimensional zero signal.  Any potential novelty is restricted to
this CCM-specific composition, not to polarization, Fourier orthogonality, or
Poincare--Lelong.

## 14. New target and stop rule

Define `BOUNDED-ORBIT-CHARACTER-LIFT` to mean a cofinal construction of
cutoff matrix signals `F_(N,R)(u)` satisfying all of:

```text
BOC-1  F_(N,R) is derived from finite Gamma--Euler/CCM data before any zero is
       selected;

BOC-2  for every fixed spectral cutoff R, the limit N->infinity is the
       corresponding finite/cutoff pole signal (4.4), with the actual jet
       atom Y_p and real two-coordinate character q_p; as R->infinity every
       pole orbit is eventually included with its nonzero detector weight;

BOC-3  absolute or uniform estimates justify, in a declared order, expansion
       of the six-linear form, N->infinity, each of the five phase-box means,
       R->infinity, and all sum/integral interchanges;

BOC-4  the construction uses neither log|Xi|, Xi'/Xi, zero positions,
       spectral projectors, Hermite--Bezout quotient signatures, nor an
       assumed determinant/divisor convergence;

BOC-5  after applying (4.5), the cofinal arithmetic value is proved to tend
       to zero, while BOC-2--BOC-3 identify that same limit with the
       nonnegative sum in (4.8).                                  (14.1)
```

By (4.8), eventual inclusion of every off-line orbit and positivity of its
`P_3` contribution make `BOC-1`--`BOC-5` imply RH directly.  Clause `BOC-5`,
or a hidden input needed to justify `BOC-2`--`BOC-3`, must therefore carry
full RH strength.

The following routes are frozen:

```text
one-parameter Bohr or Fejer averaging;
Kronecker matching of all zero phases;
ordinary cumulants without independently labelled orbit variables;
log-det or connected expansions of the aggregate;
translation-invariant holomorphic approximate diagonals with a claimed
uniform recentered bound;
Poincare--Lelong presented as a root-free arithmetic evaluation;
terminal compounds formed only after the full matrix is aggregated;
finite real-zero determinants without the weighted potential transfer. (14.2)
```

Further work is justified only if it attacks one of:

```text
a finite two-coordinate character identity with exact boundary correction;
a complex-translation pairing whose exponential growth cancels before any
limit or absolute estimate;
a Gamma--Euler construction of (12.2) which does not pass through the
divisor potential;
the scalar weighted convergence (8.2), proved directly from the complete
signed source rather than from determinant convergence.               (14.3)
```

## 15. Status

```text
proved:
  trace formula for the exterior-cube polynomial;
  exact five-phase diagonal projector;
  exact pole-level quartet assembly;
  exact labelled Rademacher cumulant coordinate;
  log-det/aggregate non-identifiability;
  convergent Poincare--Lelong jet-potential formula;
  D>=0 and D=0 iff RH;
  hidden Xi'/Xi identity;
  isolated terminal compound bridge;
  rank-one collapse of its complete first variation in the moving terminal
  system;
  subsequent exact affine factorization of every moving terminal compound
  and its reduction to sampled IDENT energy in E101.084;
  normal-family blow-up for difference kernels and uniformly recentered
  holomorphic diagonal kernels;

closed as known or circular:
  logarithmic divisor criteria as an arithmetic proof;
  finite selfadjoint determinants without weighted potential convergence;
  ordinary correlation asymptotics;
  cumulants or log determinants of the aggregate;
  moving terminal compounds as an independent bypass of IDENT;

new exact reduction:
  JET-DIAGONAL-LIFT reduces to BOUNDED-ORBIT-CHARACTER-LIFT;

still open:
  BOUNDED-ORBIT-CHARACTER-LIFT;
  DIRECTIONAL-IDENT;
  Omega7.
```
