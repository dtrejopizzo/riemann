# E101.085 - Parity Gram reduction of the mixed bidegrees

## 1. Decision

The degree-six CCM detector of E101.082 is algebraically
overdimensioned.  Exact jet parity splits every completed quartet matrix into
an even block and an odd block, each of rank at most two.  Its third-compound
detector then factors through two quadratic Gram energies.

At every symmetric finite Fourier section and finite jet depth,

```text
P_3(X)
 =e_2(X_e)^2 tr(X_o^2)+e_2(X_o)^2 tr(X_e^2)       (1.1)

 =4096[g_e^2q_o+q_eg_o^2].                        (1.2)
```

Here `X=X_e direct-sum X_o`, `g_e,g_o>=0`, and each `g_sigma` uses only one
holomorphic CCM half-atom and its conjugate:

```text
g_sigma
 ={tr(Q_sigma conj(Q_sigma))
   -tr(Q_sigma)tr(conj(Q_sigma))}/4.               (1.3)
```

For a real spectral point both energies vanish.  For every fixed
nondegenerate off-line quartet, both are strictly positive after the finite
resolution threshold of E101.078.  Consequently,

```text
G_PAR(z)=g_e(z)+g_o(z)                             (1.4)
```

is already an isolated off-line detector of bidegree `(1,1)`.  The six-leg
exterior statistic adds no discrimination.

This is a strategic reduction, not a proof of Omega7.  The conjugate graph
is still missing.  The force-bearing target is now an exact *quadratic*
Gamma--Euler trace for (1.4), not a sixth tensor of marked prime events.

## 2. Finite symmetric jet setup

Fix a symmetric Fourier section `|n|<=N` and jet depths `0<=r<=R`.  Use the
real jet frame of E101.078:

```text
j_n^((r))=(1/L)(-1)^nK_L^((r))(d_n),
d_(-n)=-d_n.                                      (2.1)
```

Since `K_L` is real and even,

```text
j_(-n)^((r))=(-1)^rj_n^((r)).                     (2.2)
```

Let

```text
c_r(z)=sum_(|n|<=N)j_n^((r))/(d_n-z),
c(z)=(c_r(z))_(0<=r<=R).                          (2.3)
```

Define the jet-parity involution and projections

```text
P=diag((-1)^r),
E=(I+P)/2,
O=(I-P)/2,                                        (2.4)

e(z)=Ec(z),
o(z)=Oc(z).                                       (2.5)
```

Let

```text
K(z)=alpha chi sin(zL/2)^2,
Q(z)=K(z)c(z)c(z)^T.                              (2.6)
```

The constants `alpha,chi` are real.  The apparent lattice poles in (2.6)
are removable, as in E101.078 and E101.082.

## 3. Exact parity block diagonalization

### Lemma 3.1 - Finite Cauchy-jet parity

For every `z` off the finite lattice,

```text
c(-z)=-Pc(z).                                     (3.1)
```

### Proof

For each coordinate, change `n` to `-n` and use (2.2):

```text
c_r(-z)
 =sum_n j_n^((r))/(d_n+z)
 =-sum_n j_(-n)^((r))/(d_n-z)
 =-(-1)^r c_r(z).                                 (3.2)
```

This is (3.1). `QED`

The holomorphic parity-completed half-orbit is

```text
A(z)=Q(z)+Q(-z).                                   (3.3)
```

Since `K(-z)=K(z)`, Lemma 3.1 gives

```text
Q(-z)=PQ(z)P,

A(z)=2K(z)[e(z)e(z)^T+o(z)o(z)^T].                (3.4)
```

Thus `A` has no even--odd block.  Put

```text
Q_e=K ee^T,
Q_o=K oo^T,
A_sigma=2Q_sigma.                                 (3.5)
```

The complete quartet matrix is real and block diagonal:

```text
X(z)=A(z)+A(conj z)=X_e(z) direct-sum X_o(z),

X_sigma=2[Q_sigma+conj(Q_sigma)],
rank X_sigma<=2.                                  (3.6)
```

The relation is exact before the bilateral or cofinal limit.

## 4. Factorization of the third compound

For a real symmetric matrix `B`, write

```text
e_2(B)={tr(B)^2-tr(B^2)}/2.                       (4.1)
```

If `rank B<=2`, this is the product of its two possibly nonzero eigenvalues.

### Theorem 4.1 - Parity factorization of `P_3`

For the matrix (3.6),

```text
P_3(X)
 =e_2(X_e)^2tr(X_o^2)+e_2(X_o)^2tr(X_e^2).        (4.2)
```

### Proof

For real symmetric `X`, the squared Hilbert--Schmidt norm of its third
exterior power is

```text
P_3(X)=e_3(lambda_1^2,...,lambda_d^2),             (4.3)
```

where the `lambda_j` are the eigenvalues of `X`.  Each parity block has at
most two nonzero eigenvalues.  A nonzero triple in (4.3) must therefore use
two eigenvalues from one block and one from the other.  The triples with two
even eigenvalues sum to

```text
e_2(X_e)^2tr(X_o^2),                               (4.4)
```

and the opposite distribution gives the second term in (4.2). `QED`

This identity sharpens the mixed-bidegree localization of E101.082.  Every
third minor of `A+conj(A)` contains only the cubic types
`A^2conj(A)` and `Aconj(A)^2`, because both half-orbits have rank at most
two.  After squaring, the bidegrees `k=0,1,5,6` vanish identically and only

```text
(4,2), (3,3), (2,4)                               (4.5)
```

can survive.  Formula (4.2) recombines these three modes into two products
built from quadratic conjugate energies and quadratic real block sizes.

The side modes are genuinely present.  Take an even block `E=C^2`, an odd
block `O=C`, `K=1`, `e=(1,i)^T`, `o=1`, and

```text
A=2(ee^T direct-sum oo^T),
X_theta=exp(i theta)A+exp(-i theta)conj(A).        (4.6)
```

Direct substitution gives

```text
P_3(X_theta)
 =4096 cos(theta)^2
 =2048+1024exp(2i theta)+1024exp(-2i theta).       (4.7)
```

The nonconstant modes in (4.7) are exactly `k=4` and `k=2`; they cannot be
discarded in favor of the central `(3,3)` mode alone.

## 5. Branch-free Gram scalars

Fix one parity `sigma` and abbreviate `v=v_sigma`.  Define

```text
s=v^*v,
t=v^Tv.                                           (5.1)
```

The two branch-free scalars are

```text
g_sigma
 =|K|^2[s^2-|t|^2]/4                              (5.2)

 ={tr(Q_sigma conj(Q_sigma))
   -tr(Q_sigma)tr(conj(Q_sigma))}/4,

q_sigma
 ={|K|^2s^2+Re(K^2t^2)}/2.                        (5.3)
```

### Proposition 5.1 - Exact block invariants

For each parity block,

```text
g_sigma>=0,
q_sigma>=0,

e_2(X_sigma)=-16g_sigma,
tr(X_sigma^2)=16q_sigma.                           (5.4)
```

Consequently,

```text
P_3(X)=4096[g_e^2q_o+q_eg_o^2].                  (5.5)
```

### Proof

Locally choose `kappa` with `kappa^2=K` and write

```text
kappa v=a+ib,
a,b real.                                         (5.6)
```

Then

```text
X_sigma=4[aa^T-bb^T].                             (5.7)
```

Put `A=||a||^2`, `B=||b||^2`, `C=a^Tb`.  Direct calculation gives

```text
g_sigma=AB-C^2,
q_sigma=A^2+B^2-2C^2.                             (5.8)
```

Cauchy--Schwarz proves `g_sigma>=0`, while

```text
q_sigma=(A-B)^2+2g_sigma>=0.                      (5.9)
```

Using (5.7),

```text
e_2(X_sigma)=16(C^2-AB),
tr(X_sigma^2)=16(A^2+B^2-2C^2),                  (5.10)
```

which proves (5.4).  The branch-free formulas follow from

```text
(a+ib)^*(a+ib)=|K|s,
(a+ib)^T(a+ib)=Kt,                                (5.11)
```

and from the rank-one matrix `Q_sigma=Kvv^T`.  Insert (5.4) into (4.2) to
obtain (5.5). `QED`

The equality `g_sigma=0` means that the real and imaginary parts of the
weighted parity jet have one common phase.  Moreover,

```text
K!=0 and rank X_sigma=2 <=> g_sigma>0.            (5.12)
```

If `g_sigma>0`, then `q_sigma>=2g_sigma>0`.  The equality `q_sigma=0`
holds exactly when `X_sigma=0`; in the coordinates (5.6), this means that
`a,b` are parallel with equal norm and hence `b=+/-a`.  Thus `q_sigma=0`
can occur with `v!=0`; it means cancellation in the real block, not
vanishing of the holomorphic jet.  At `K=0` all identities above are read by
continuity from the branch-free formulas (5.2)--(5.3).

## 6. A quadratic isolated-orbit detector

Define

```text
G_PAR(z)=g_e(z)+g_o(z).                            (6.1)
```

### Theorem 6.1 - Finite parity-Gram discrimination

For every finite symmetric section:

```text
z real  => G_PAR(z)=0.                            (6.2)
```

For each fixed nondegenerate off-line quartet, there are finite thresholds
`N_0(z),R_0(z)` such that

```text
N>=N_0, R>=R_0  => g_e(z)>0, g_o(z)>0,
                    G_PAR(z)>0.                   (6.3)
```

### Proof

If `z` is real, `K,e,o` are real and each `Q_sigma` is a real rank-one
matrix.  Formula (5.2) gives `g_sigma=0`.

For a resolved nondegenerate off-line quartet, E101.078 gives
`rank X=4`.  The direct sum (3.6) has two blocks, each of rank at most two.
Both must therefore have rank two.  Equation (5.12) makes both Gram energies
strictly positive. `QED`

No finite depth uniform in all possible off-line points is asserted.  The
same cofinal quantifier used in E101.078 is retained.

The detector (6.1) has bidegree `(1,1)` in the holomorphic half-atom and its
conjugate.  It requires a same-zero conjugate pairing, but no sixfold
polarization and no sixth event tensor.

## 7. Cauchy--Vandermonde horizontal factor

The parity Gram has an explicit horizontal-displacement factor.  For two jet
coordinates define

```text
D_(r,s)(z,q)
 =c_r(z)c_s(q)-c_s(z)c_r(q).                      (7.1)
```

Direct expansion gives

```text
D_(r,s)(z,q)
 =sum_(n<m)
  [j_n^((r))j_m^((s))-j_n^((s))j_m^((r))]
  (z-q)(d_m-d_n)
  /[(d_n-z)(d_m-z)(d_n-q)(d_m-q)].                (7.2)
```

If `r,s` have the same parity, (3.1) also gives

```text
D_(r,s)(z,-z)=0.                                   (7.3)
```

Hence the rational numerator is divisible by both `z-q` and `z+q`:

```text
D_(r,s)(z,q)=(z^2-q^2)V_(r,s)(z,q),               (7.4)
```

where `V_(r,s)` is rational off the fixed lattice.  The quotient need not be
removable at a lattice point by itself.

Put `z=x+iy` and `q=conj z`.  Since the jet frame is real,

```text
Im[c_r(z)conj(c_s(z))]
 =2xy V_(r,s)(z,conj z).                          (7.5)
```

For each parity define

```text
Vcal_sigma(z)
 =sum_(r<s, r=s mod 2)V_(r,s)(z,conj z)^2.        (7.6)
```

On the conjugate graph these quantities are real and nonnegative.  The Gram
identity becomes

```text
g_sigma(z)
 =4|K(z)|^2x^2y^2Vcal_sigma(z).                   (7.7)
```

Combining (5.5) and (7.7) gives

```text
P_3(X(z))
 =65536|K(z)|^4x^4y^4
  [Vcal_e(z)^2q_o(z)+Vcal_o(z)^2q_e(z)].          (7.8)
```

Equations (7.7)--(7.8) hold off the lattice.  At a lattice point they mean
the limit of the complete products on their right sides.  The entire
matrices `Q_sigma` and `X_sigma` give that continuation; neither
`V_(r,s)` nor `Vcal_sigma` is asserted to continue separately.

The factors `x^2y^2` identify the geometry precisely.  For nontrivial zeros
`x` is a nonzero ordinate and `y` is the horizontal displacement from the
critical line.  The detector vanishes on-line because `y=0`, not because of
a cancellation between six unrelated labels.

## 8. Relation to the full-jet Gram detector

E101.077 already constructed the quadratic full-jet Gram

```text
G_Xi(z)=1/4[S_Xi(z)^2-|T_Xi(z)|^2]                (8.1)
```

and proved that it is zero exactly on the real axis.  No novelty is claimed
for the Gram mechanism, Cauchy--Binet positivity, or phase rigidity.

For the finite jet vector `c=c_e+c_o`, write

```text
G(u)=sum_(r<s) Im(u_r conj(u_s))^2.                (8.2)
```

Then the exact relation is

```text
G_PAR
 =|K|^2[G(c_e)+G(c_o)],                           (8.3)

G(c)=G(c_e)+G(c_o)
     +sum_(r even, s odd)Im(c_r conj(c_s))^2.     (8.4)
```

Thus `G_PAR` is a restriction of the full Gram, not the full Gram itself.
For the factorially weighted bilateral frame of E101.077,

```text
c_r^(D)(z)
 =-tau^r K_L^((r))(z)/[2 sin(zL/2)r!],            (8.5)
```

and the kernel factor `K=alpha chi sin(zL/2)^2` gives

```text
G_PAR
 =(alpha^2 chi^2/16)
   [G_even(K_L,tau;R)+G_odd(K_L,tau;R)].          (8.6)
```

Only after the support limit has been justified may `K_L` be replaced by
`Xi`.  In particular, no finite-section identity is silently passed through
that limit.

The new result here is the exact finite CCM crosswalk:

```text
six-linear exterior detector
  -> parity block factorization
  -> two within-parity quadratic Gram energies.    (8.7)
```

`G_PAR` is the within-parity part of the full jet Gram.  It need not detect
every nonreal point at an arbitrarily prescribed shallow depth, but the
rank-four theorem proves its cofinal strict positivity for every fixed
nondegenerate off-line quartet.

Thus E101.077 and E101.082 were not competing routes.  The latter factors
through a parity restriction of the former after the exact CCM jet
compression is used.

## 9. Revised arithmetic target

Define `PARITY-GRAM-GRAPH-TRACE` to be a source-first identity whose spectral
side, at fixed finite `N,R`, is

```text
sum_rho m_rho [g_e(rho)+g_o(rho)],                 (9.1)
```

with linear divisor multiplicity and all prime, archimedean, polar and
cutoff terms retained.

By (1.3), each summand requires only the bilinear conjugate graph

```text
Q_sigma(rho) tensor conj(Q_sigma(rho)).            (9.2)
```

It does not require a sixth tensor.  The arithmetic theorem must still:

```text
PGT-1 derive the same-zero conjugate pairing rather than insert it;

PGT-2 prove fixed-section equality with every correction channel;

PGT-3 justify the cofinal order in N and R;

PGT-4 prove that the nonnegative spectral value (9.1) vanishes;

PGT-5 connect that vanishing to the actual terminal DIRECTIONAL-IDENT
      normalization;

PGT-6 preserve linear divisor multiplicity.  A product of two independent
      one-level traces gives m_rho^2, and absorbing m_rho into Q_sigma also
      makes g_sigma scale quadratically.  The target (9.1) instead applies
      one divisor weight to the unweighted per-zero Gram.         (9.3)
```

`PGT-4` or a hidden premise in `PGT-1`--`PGT-3` carries full RH strength.
The advance is not a reduction in logical difficulty; it is a reduction in
algebraic arity and in the number of auxiliary labels which must be matched.

### Proposition 9.1 - The ordinary one-trace quadratic channel is zero

Define the bilinear contraction

```text
b(U,V)={tr(UV)-tr(U)tr(V)}/4.                     (9.4)
```

Then

```text
g_sigma(z)=b(Q_sigma(z),conj(Q_sigma(z))),        (9.5)

b(Q_sigma(z),Q_sigma(z))=0.                       (9.6)
```

### Proof

Equation (9.5) is (5.2).  Since `Q_sigma` has rank at most one,

```text
tr(Q_sigma^2)=tr(Q_sigma)^2,
```

which proves (9.6). `QED`

The source involution available to one Weil trace is Schwarz reflection:

```text
Q_sigma^sharp(z)=conj(Q_sigma(conj z))=Q_sigma(z), (9.7)
```

because the finite CCM half-atom is real-type.  Thus one-trace convolution
reaches exactly the holomorphic contraction (9.6), which is identically
zero, rather than (9.5).  A product of two traces reaches conjugated values
but retains every zero pair and quadratic multiplicity.  Consequently the
ordinary one-trace quadratic route is closed; `PARITY-GRAM-GRAPH-TRACE`
requires a genuinely new source operation or a controlled all-pairs bypass.

### Mixed Euler deformations do not supply conjugate velocities for free

Let an analytic family `F(z;u,v)` have a zero `p(u,v)` of multiplicity `m`.
Its local mixed logarithmic response is

```text
-partial_u partial_v log F(z;u,v)
 =m p_u p_v/(z-p)^2+m p_(uv)/(z-p)+O(1).          (9.8)
```

Therefore a deformation can generate the Gram pairing only if its zero
velocities satisfy, for the required jet coordinates,

```text
p_u=q_u(p),
p_v=conj(q_v(p))=q_v(conj p).                     (9.9)
```

The second equality is precisely conjugate-graph interpolation at the zero.
It is not a formal consequence of taking two Euler parameters.  Any
multivariate Euler proposal must prove (9.9) from its source coefficients;
postulating it inserts `PGT-1` in differential form.

## 10. Literature and nonduplication gate

The full-jet Gram mechanism and its phase-rigidity antecedents are recorded
in E101.077.  Covariance versus pseudocovariance and same-height spectral
pairing are also known.  Recent pair-correlation work explicitly uses the
symmetric pair `rho` and `1-conj(rho)`:

```text
Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh:
  https://arxiv.org/abs/2501.14545

Goldston--Lee--Schettler--Suriajaya:
  https://arxiv.org/abs/2503.15449                 (10.1)
```

Those results obtain proportional horizontal information from asymptotic
pair correlations.  They do not construct the exact finite functional (9.1)
from Gamma--Euler and cannot exclude a finite exceptional off-line set.

No novelty is claimed for:

```text
same-height or symmetric spectral pairing;
quadratic Gram positivity;
parity decomposition of an even real kernel;
Cauchy or Vandermonde determinant factors.         (10.2)
```

The potentially new finite statement is the combined identity
(3.4)--(5.5), together with the exact horizontal factor (7.7): it lowers the
specific CCM graph target from six mixed legs to one parity-resolved
conjugate pair.  No inspected primary source contains this CCM crosswalk.

## 11. Strategy change and stop rule

The following route is no longer primary:

```text
sixth marked-prime tensor
  -> sixth same-zero tensor
  -> P_3.                                          (11.1)
```

E101.083 remains a valid no-go for its restricted positive tensor-power
ansatz, but even a successful sixth-order transport would solve a stronger
problem than necessary.

The preferred route is

```text
exact second-order Gamma--Euler pair current
  -> parity-resolved same-height graph
  -> G_PAR
  -> terminal IDENT energy.                        (11.2)
```

E101.086 supplies a separate all-pairs bypass:

```text
complete translated Gaussian Weil trace
  -> positive Abel L2 current
  -> exact abscissa 2 sup|Im p|
  -> LOG-GAUSSIAN-L2-CANCELLATION.                (11.2a)
```

It does not construct (9.5); it avoids graph selection and moves the full
force into one source-side prime-error estimate.

Freeze:

```text
introducing six spectral labels when the quadratic graph suffices;
claiming that the three surviving mixed bidegrees are algebraically
independent;
continuing sixth event-tensor work without first failing the quadratic
pair-current target;
presenting G_PAR>=0 as arithmetic progress toward RH;
using asymptotic pair correlation to exclude finitely many off-line zeros.
                                                               (11.3)
```

## 12. Status

```text
proved:
  exact finite Cauchy-jet parity;
  exact even--odd block decomposition of the quartet CCM matrix;
  vanishing of bidegrees k=0,1,5,6 and necessity of k=2,4 in general;
  parity factorization of the third-compound detector;
  branch-free nonnegative block Gram formulas;
  reduction P_3=4096[g_e^2q_o+q_eg_o^2];
  cofinal off-line discrimination by G_PAR;
  Cauchy--Vandermonde horizontal factor;
  zero one-trace quadratic contraction;
  conjugate-velocity condition for a mixed Euler deformation;

strategy closed as unnecessarily strong:
  sixth-order transport as the primary route to the CCM detector;

new preferred target:
  PARITY-GRAM-GRAPH-TRACE;

still open:
  an exact Gamma--Euler construction of the quadratic conjugate graph;
  its linear-multiplicity normalization;
  cofinal interchange and arithmetic vanishing;
  DIRECTIONAL-IDENT and Omega7.
```
