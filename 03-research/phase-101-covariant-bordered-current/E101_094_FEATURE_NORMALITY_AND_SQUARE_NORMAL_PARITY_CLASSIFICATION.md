# E101.094 - Feature normality and square-normal parity classification

## 1. Decision

The feature-specific escape left open by E101.092 has an exact
classification.  It is not an unexplained cancellation of the nonnormal
overlap matrix.

For a diagonalizable matrix `C` with simple spectrum in a positive metric
`G`, let

```text
C=S Lambda S^(-1),
H=S^*GS,
O_(ij)=(H^(-1))_(ij)H_(ji).                         (1.1)
```

Then

```text
O-I>=0.                                             (1.2)
```

For a scalar spectral feature `r`, the overlap acts diagonally on that
feature,

```text
O conj(r(p))=conj(r(p)),                             (1.3)
```

if and only if `r(C)` is `G`-normal.  Thus every scalar cancellation of the
complete leakage equation in E101.092 with a first leg nonzero on the whole
spectrum is a normality statement for the selected feature.

The CCM parity atoms are even.  Consequently they do not need `C` itself to
be normal.  A sufficient structural condition for every such atom is the
weaker statement

```text
[C^2,(C^2)^(dagger_G)]=0.                           (1.4)
```

Under (1.4), overlap may remain inside each pair `{p,-p}`, but every even
feature is constant on that pair and the row-sum identity cancels the
internal overlap exactly.  For the complete scalar class, graph recovery for
the single even probe `r(z)=z^2`, with a nonvanishing first leg, implies
(1.4).  A fixed degenerate matrix atom can be blind and need not imply it.

For one nondegenerate quartet, vanishing of the complete CCM leakage is
equivalent to `G`-orthogonality of its two squared-eigenvalue spaces, hence
to (1.4).  The condition is not implied by parity, real structure,
reciprocal pairing or indefinite `J`-unitarity.  A rational four-dimensional
counterexample with a synthetic even rank-one atom gives the exact nonzero
false current

```text
(1/9) sum_(p in {2,1/2,-2,-1/2})(z-p)^(-2).         (1.5)
```

This closes scalar `feature flattening` with a nonvanishing first leg and
the isolated-quartet cancellation escape of E101.092.  It does not assert a
global converse for one arbitrary CCM atom.  A square-normal metric remains
source-admissible only if it is constructed from Gamma--Euler data before
spectral factorization.  Root-block orthogonalization is divisor
interpolation.  Moreover, conditionally on finite even-simplicity, E101.093
constructs a stronger self-adjoint finite quotient; square-normality cannot
by itself provide the missing cofinal identification with `Xi`.

## 2. Setup and overlap matrix

Let `C in M_n(C)` have simple spectrum

```text
spec C={p_1,...,p_n}.                                (2.1)
```

Let `G=G^*>0`, choose a right-eigenvector matrix `S`, and put

```text
C=S diag(p_1,...,p_n)S^(-1),
H=S^*GS.                                             (2.2)
```

The matrix `H` is positive definite.  Define

```text
O=H^(-1) circle H^T,
O_(ij)=(H^(-1))_(ij)H_(ji),                         (2.3)
```

where `circle` denotes entrywise multiplication.  As proved in E101.092,

```text
O=O^*>=0,
sum_j O_(ij)=sum_i O_(ij)=1.                        (2.4)
```

For a vector `x=(x_i)`, define the spectral function

```text
F_x=S diag(conj(x_1),...,conj(x_n))S^(-1).          (2.5)
```

The next result sharpens (2.4).

## 3. Sharp overlap inequality

### Theorem 3.1 - Overlap excess is positive

One has

```text
O-I>=0.                                             (3.1)
```

For every `x in C^n`, the following are equivalent:

```text
(a) Ox=x;

(b) x^*(O-I)x=0;

(c) F_x is G-normal;

(d) H_(ij)=0 whenever x_i!=x_j.                     (3.2)
```

### Proof

Put

```text
S_tilde=G^(1/2)S,
A_x=G^(1/2)F_xG^(-1/2)
   =S_tilde diag(conj(x_i))S_tilde^(-1).            (3.3)
```

Direct cyclic trace calculation gives

```text
||A_x||_F^2
 =Tr[diag(x_i)H diag(conj(x_i))H^(-1)]
 =x^*Ox.                                            (3.4)
```

The eigenvalues of `A_x` are `conj(x_i)`.  Let

```text
A_x=UTU^*                                            (3.5)
```

be a unitary Schur decomposition.  Its Frobenius norm is

```text
||A_x||_F^2
 =sum_i|x_i|^2+sum_(i<j)|T_(ij)|^2
 >=||x||_2^2.                                       (3.6)
```

Equations (3.4)--(3.6), valid for every `x`, prove (3.1).  Equality in
(3.6) holds exactly when `T` is diagonal, equivalently when `A_x` is normal.
Similarity by `G^(1/2)` carries the ordinary adjoint of `A_x` to the
`G`-adjoint of `F_x`, so this is equivalent to `(c)`.

Because `O-I>=0`, equality of the quadratic form is equivalent to membership
in its kernel.  This proves `(a)<=> (b)<=> (c)`.

Finally, a diagonalizable matrix is normal exactly when its eigenspaces for
distinct eigenvalues are mutually orthogonal.  The eigenspace of `F_x` for
a value `conj(a)` is the span of those columns of `S` for which `x_i=a`.
Their `G`-Gram matrix is `H`.  This proves `(c)<=> (d)`. `QED`

The inequality (3.1) is a form of the classical Hadamard inverse inequality

```text
A circle A^(-T) >= I                                (3.7)
```

for positive definite Hermitian matrices.  A direct primary antecedent is

```text
C. R. Johnson and L. Elsner,
The relationship between Hadamard and conventional multiplication for
positive definite matrices,
https://doi.org/10.1016/0024-3795(87)90260-6.        (3.8)
```

No novelty is claimed for (3.1) itself.  The fixed-space statement (3.2)
and its CCM consequences below are the required specialization.

## 4. Scalar feature cancellation is feature normality

For scalar probes `q,r`, E101.092 gives the exact coefficient at the pole
`p_i`:

```text
q(p_i){sum_j O_(ij)conj(r(p_j))-conj(r(p_i))}.       (4.1)
```

### Corollary 4.1 - Exact scalar classification

Assume

```text
q(p_i)!=0 for every i.                               (4.2)
```

Then (4.1) vanishes for every `i` if and only if `r(C)` is `G`-normal.

### Proof

Under (4.2), vanishing is exactly

```text
O conj(r_vec)=conj(r_vec),
r_vec=(r(p_i))_i.                                   (4.3)
```

Apply Theorem 3.1 with `x=conj(r_vec)`.  Formula (2.5) then gives

```text
F_x=S diag(r(p_i))S^(-1)=r(C).                      (4.4)
```

Thus (4.3) is equivalent to `G`-normality of `r(C)`. `QED`

If `q` vanishes on part of the spectrum, (4.1) tests only the remaining
rows and does not imply global feature normality.  This is why a
nonvanishing first leg is essential in the converse.

Corollary 4.1 rules out a separate scalar signed-cancellation mechanism.
The overlap excess is positive semidefinite, and its fixed vectors are
exactly the normal spectral features.

## 5. Even features and square-normality

Assume the spectrum is invariant under sign:

```text
p in spec C => -p in spec C.                        (5.1)
```

Let `r` be even, so `r(-z)=r(z)`.

### Theorem 5.1 - Square-normal graph recovery

If `C^2` is `G`-normal, then for every even scalar feature `r`,

```text
O conj(r_vec)=conj(r_vec).                          (5.2)
```

Consequently the exact scalar graph formula of E101.092 holds for every
pair of even probes.

Conversely, if the graph formula holds with a nonvanishing first probe and
with

```text
r(z)=z^2,                                           (5.3)
```

then `C^2` is `G`-normal.

### Proof

If `C^2` is normal, its eigenspaces for distinct squared eigenvalues are
`G`-orthogonal.  Hence

```text
H_(ij)=O_(ij)=0 when p_i^2!=p_j^2.                  (5.4)
```

Within a fixed square block, simple spectrum gives `p_j=+/-p_i`.  Evenness
then gives `r(p_j)=r(p_i)`.  Using the row sum in (2.4),

```text
sum_j O_(ij)conj(r(p_j))
 =conj(r(p_i))sum_(j:p_j^2=p_i^2)O_(ij)
 =conj(r(p_i)).                                     (5.5)
```

This proves (5.2).  Conversely, Corollary 4.1 applied to (5.3) says exactly
that `r(C)=C^2` is `G`-normal. `QED`

Thus, for the complete class of even scalar features,

```text
graph recovery
 <=> square-normality,                               (5.6)
```

provided the converse includes one nonvanishing first leg.  Full normality
of `C` is stronger than necessary: nonorthogonality between the eigenspaces
of `p` and `-p` is invisible to every even feature.

## 6. Complete parity-CCM leakage

Let `Q(z)` be an even, real-type, symmetric rank-one CCM atom:

```text
Q(-z)=Q(z),
Q(conj z)=conj(Q(z)),
rank Q(z)<=1.                                       (6.1)
```

Define

```text
g_(ij)=b(Q(p_i),Q(p_j)^*),

b(A,B)={tr(AB)-tr(A)tr(B)}/4.                      (6.2)
```

E101.092 gives the complete leakage

```text
L_(C,G,Q)(z)
 =sum_i [sum_j O_(ij)g_(ij)-g_(ii)]/(z-p_i)^2.     (6.3)
```

### Theorem 6.1 - Square-normal parity cancellation

If `C^2` is `G`-normal, then

```text
L_(C,G,Q)(z)=0                                      (6.4)
```

identically.

### Proof

Equation (5.4) restricts the inner sum in (6.3) to `p_j=+/-p_i`.  By
evenness, `Q(p_j)=Q(p_i)`, so

```text
g_(ij)=g_(ii)                                       (6.5)
```

throughout the square block.  Therefore

```text
sum_jO_(ij)g_(ij)
 =g_(ii)sum_(j:p_j^2=p_i^2)O_(ij)
 =g_(ii).                                           (6.6)
```

Every coefficient in (6.3) vanishes. `QED`

Theorem 6.1 is only sufficient for a single fixed atom.  A specially
degenerate atom can be blind to a nonorthogonal pair, and pairwise separation
alone does not exclude cancellations among three or more square blocks.  No
global converse for an unspecified CCM family is claimed.  The converse is
exact for the isolated quartet below.

## 7. Exact isolated-quartet criterion

Let

```text
A={p,-p},
B={conj(p),-conj(p)},
p^2 not real.                                       (7.1)
```

Assume `Q` satisfies (6.1), and put

```text
Q_A=Q(p),
Q_B=conj(Q_A),
g=b(Q_A,Q_A^*)>0.                                   (7.2)
```

### Lemma 7.1 - Quartet contraction table

For the four spectral labels,

```text
g_(ij)=g  if i,j both belong to A or both belong to B;

g_(ij)=0  if one belongs to A and the other to B.   (7.3)
```

### Proof

Within `A`, evenness makes both atoms `Q_A`; within `B`, real type makes
both atoms `Q_B`, and both Gram values equal `g`.  Across the two sets,

```text
Q(conj p)^*=conj(Q_A)^*=Q_A^T=Q_A,                 (7.4)
```

because `Q_A` is symmetric.  Thus the cross value is

```text
b(Q_A,Q_A)=0                                       (7.5)
```

by rank one. `QED`

For `i in A`, define

```text
s_i=sum_(j in B)O_(ij).                             (7.6)
```

The coefficient in (6.3) is

```text
ell_i=-g s_i.                                       (7.7)
```

The symmetric statement holds for `i in B`.

### Theorem 7.2 - Quartet leakage equivalence

Under (7.1)--(7.2), the following are equivalent:

```text
(a) L_(C,G,Q)=0;

(b) O 1_A=1_A;

(c) the spectral projector P_A is G-normal;

(d) span(A) is G-orthogonal to span(B);

(e) C^2 is G-normal on the quartet space.           (7.8)
```

### Proof

Equations (7.3), (7.6) and the row-sum identity give (7.7).  Vanishing on
both halves is therefore equivalent to

```text
sum_(j in B)O_(ij)=0 for i in A,
sum_(j in A)O_(ij)=0 for i in B,                    (7.9)
```

which is exactly `(b)`.  Apply Theorem 3.1 to `x=1_A`.  Formula (2.5) gives
`F_x=P_A`, proving `(b)<=> (c)`.  A normal idempotent in a Hilbert metric is
an orthogonal projector, which proves `(c)<=> (d)`.  Finally, `C^2` has the
two distinct eigenvalues `p^2` and `conj(p)^2` on the spaces in `(d)`.
Their orthogonality is exactly its normality. `QED`

There is no cancellation among signed off-diagonal contributions hidden in
this quartet.  The diagonal factors satisfy `O_(ii)>=1`.  The full condition
is orthogonality of the two squared spectral blocks.

## 8. Actual CCM atoms separate two real parity pairs

Take distinct `a,b>0` away from the removable-lattice presentation of one
chosen support length.  For one parity block, write

```text
Q_sigma(x)=K(x)v_sigma(x)v_sigma(x)^T.              (8.1)
```

Assume the CCM kernel has its source representation

```text
K_L(t)=integral_(-ell)^ell k(x)exp(-itx)dx,          (8.1a)
```

where `k` is real and even and is nonzero almost everywhere on some
subinterval.  Assume also that the real scalar multiplier `K` in (8.1) is
nonzero at `a` and `b`.  These are the hypotheses used in the translate-jet
independence theorem of E101.078.

At real `x`, all entries are real.  Direct Cauchy--Binet expansion gives

```text
eta_sigma(a,b)
 =b(Q_sigma(a),Q_sigma(b))

 =-K(a)K(b)/4
  sum_(r<s, r=s mod 2)
  [c_r(a)c_s(b)-c_s(a)c_r(b)]^2.                   (8.2)
```

Since `K` is a fixed real multiple of `sin(xL/2)^2`,

```text
K(a)K(b)>0                                         (8.3)
```

away from resonance.  Hence

```text
eta_sigma(a,b)<=0,                                 (8.4)
```

with equality exactly when the two finite parity-jet vectors are
proportional.

### Proposition 8.1 - Eventual strict separation

For `a!=b`, each bilateral parity-jet family contains a finite pair of
coordinates for which the determinant in (8.2) is nonzero.  Consequently,
after some finite jet depth and sufficiently large Fourier collar,

```text
eta_e(a,b)<0,
eta_o(a,b)<0.                                       (8.5)
```

### Proof

At bilateral depth, the jet coordinates are fixed nonzero scalar multiples
of derivatives of the band-limited kernel `K_L`.  Suppose first that every
minor of the even derivative sequences at `a` and `b` vanished.  The two
sequences would be proportional, so there would be constants `alpha,beta`,
not both zero, such that

```text
alpha K_L^((2m))(a)+beta K_L^((2m))(b)=0
for every m>=0.                                     (8.6)
```

Taylor expansion would make the entire function

```text
alpha[K_L(a+w)+K_L(a-w)]
+beta [K_L(b+w)+K_L(b-w)]                           (8.7)
```

identically zero.  Insert (8.1a), use that `k` is even, and apply Fourier
uniqueness on a subinterval where `k` is nonzero.  This gives

```text
alpha cos(at)+beta cos(bt)=0                        (8.8)
```

on an interval, impossible for distinct positive `a,b`.  The odd derivative
case uses the differences in place of the sums and gives independence of
`sin(at)` and `sin(bt)`.

Thus a nonzero minor occurs at finite derivative depth.  Finite symmetric
Fourier collars converge coordinatewise to that bilateral jet, so the same
minor remains nonzero for every sufficiently large collar.  Equations
(8.2)--(8.4) give (8.5). `QED`

Therefore the genuine CCM features have a nonzero pair contraction between
distinct squared real fibres at some finite resolution.  This is a pairwise
statement.  It does not prove a global converse to Theorem 6.1 when several
square blocks contribute to the same row.

## 9. Rational parity and J-unitary counterexample

Let

```text
T=[[2,1],
   [0,1/2]],

J_0=[[0,i],
     [-i,0]].                                       (9.1)
```

Then

```text
J_0=J_0^*,
J_0^2=I,
T^*J_0T=J_0.                                        (9.2)
```

Define

```text
C_0=diag(T,-T),
J=diag(J_0,J_0),

P=[[0,I_2],
   [I_2,0]],

G=I_4.                                              (9.3)
```

Direct multiplication gives

```text
C_0^*JC_0=J,
PC_0P=-C_0,
P^*GP=G.                                            (9.4)
```

Thus the example has a real rational matrix, sign parity, reciprocal
spectrum, an indefinite conserved form and a parity-invariant positive
metric.  Its spectrum is

```text
{2,1/2,-2,-1/2}.                                    (9.5)
```

Nevertheless,

```text
T^2=[[4,5/2],
     [0,1/4]],                                      (9.6)

T^2(T^2)^*-(T^2)^*T^2
 =[[25/4,-75/8],
   [-75/8,-25/4]]!=0.                               (9.7)
```

Hence `C_0^2` is not `G`-normal.

An eigenvector matrix for `T` and its Gram are

```text
S=[[1,-2/3],
   [0,1]],

H=S^*S
 =[[1,-2/3],
   [-2/3,13/9]],                                    (9.8)

H^(-1)
 =[[13/9,2/3],
   [2/3,1]].                                        (9.9)
```

Therefore

```text
O=[[13/9,-4/9],
   [-4/9,13/9]],

O-I=(4/9)[[1,-1],[-1,1]]>=0.                       (9.10)
```

Use the even rational polynomial vector and synthetic rank-one atom

```text
v(z)=[(4z^2-1)/15,
      (16-4z^2)/15]^T,

Q(z)=v(z)v(z)^T.                                    (9.11)
```

It satisfies

```text
Q(+/-2)=E_(11),
Q(+/-1/2)=E_(22).                                   (9.12)
```

The desired diagonal Gram vanishes at every one of the four real points,
whereas

```text
b(E_(11),E_(22))=-1/4.                              (9.13)
```

Each spectral row has one off-diagonal contribution

```text
(-4/9)(-1/4)=1/9.                                   (9.14)
```

Thus the nonnormal-adjoint current is exactly

```text
L_(C_0,I,Q)(z)
 =(1/9)sum_(p in {2,1/2,-2,-1/2})1/(z-p)^2,
                                                        (9.15)
```

which is not zero.  The polynomial in (9.11) is an exact interpolating
falsifier, not itself a CCM atom.

There is also a genuine CCM falsifier on the same matrix.  Choose a support
length satisfying the hypotheses of Section 8 at `a=2` and `b=1/2`.  For
either parity and all sufficiently resolved collars, Proposition 8.1 gives

```text
eta_sigma(2,1/2)<0.                                  (9.16)
```

The diagonal real rank-one Grams are zero, and the only nonzero overlap in
each two-dimensional block is `O_(12)=O_(21)=-4/9`.  Hence the actual CCM
leakage is

```text
L_(C_0,I,Q_sigma)(z)
 =kappa_sigma
  sum_(p in {2,1/2,-2,-1/2})1/(z-p)^2,

kappa_sigma=-(4/9)eta_sigma(2,1/2)>0.               (9.17)
```

Thus parity, reality, reciprocal pairing, positive-metric parity and
indefinite `J`-unitarity imply neither square-normality nor even-feature
graph recovery.  Equation (9.15) is the exact synthetic coefficient; (9.17)
is the genuine CCM conclusion with a source-determined nonzero coefficient.

## 10. Source-first boundary

For any diagonalizable `C`, one can force normality by choosing

```text
G=S^(-*)DS^(-1),
D>0 diagonal.                                       (10.1)
```

One can force only square-normality by orthogonalizing the coarser spectral
blocks of `C^2`.  Both operations use `S` or the Lagrange projectors of the
divisor.  They are therefore interpolation, not a Gamma--Euler
construction.

A source-admissible square-normal theorem must instead provide:

```text
SN-1  C and G from finite arithmetic data before factorization;

SN-2  G>0 by a source identity;

SN-3  [C^2,(C^2)^(dagger_G)]=0 by an exact Gamma--Euler relation;

SN-4  all polar, archimedean, prime and boundary terms;

SN-5  a planted-system audit locating the source identity that fails;

SN-6  cofinal control if G becomes singular or parameter dependent. (10.2)
```

Conditionally on the finite even-simple hypothesis, E101.093 already supplies
`SN-1`--`SN-4` in stronger form for the finite Weil quotient: its operator is
self-adjoint.  Under the same hypothesis for a planted build, that finite
normality is nondiscriminating there as well.
Accordingly, another square-normal finite model is not the primary front.
Only a model satisfying `SN-5` through an Xi-specific identification can
advance `Omega7`.

## 11. Stop rules

The classification gives the following exact rules.

```text
1. With a first leg nonzero on the spectrum, replace any claimed scalar
   overlap cancellation by Corollary 4.1.  It is normality of the selected
   feature.  Without that hypothesis only the tested rows are constrained.

2. For even probes, test C^2 rather than C.  Full normality is stronger
   than the CCM contraction requires.

3. Do not infer square-normality from sign parity, real structure,
   reciprocal roots or J-unitarity; (9.1)--(9.17) refute the inference.

4. Do not build the square-normal metric from root projectors.  That is
   the missing conjugate graph expressed as spectral orthogonalization.

5. For a singular cofinal metric, prove convergence of the complete
   overlap leakage.  Pointwise commutator decay is insufficient.

6. Do not count finite square-normality as progress toward Omega7.
   Under finite even-simplicity, the Weil quotient already has full
   self-adjointness; the open point is its arithmetic identification with
   the Xi divisor.                                            (11.1)
```

## 12. Status

```text
proved:
  O-I>=0 and the exact fixed-space classification;
  scalar cancellation iff feature normality under a nonvanishing first leg;
  even-feature graph recovery from square-normality;
  converse from the probe z^2;
  complete parity-CCM cancellation under square-normality;
  exact isolated-quartet equivalence;
  eventual separation of distinct real square fibres by CCM jets;
  rational parity/J-unitary counterexample with exact synthetic leakage;
  genuine CCM leakage on the same counterexample at finite resolution;

closed:
  unexplained scalar signed overlap cancellation under the nonvanishing
  first-leg hypothesis;
  parity alone as a leakage-cancellation mechanism;
  J-unitarity alone as a square-normality mechanism;
  full normality as a necessary condition for even CCM probes;

retained only with source-first proof:
  a Gamma--Euler metric making C^2 normal;

force-bearing open point:
  TRUE-DIVISOR-IDENT of E101.093,
  DIRECTIONAL-IDENT, the DISCRIMINANT and Omega7.                    (12.1)
```
