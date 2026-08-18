# E101.092 - Nonnormal adjoint overlap and commutator wall

## 1. Decision

The ordinary adjoint of a source-built nonnormal companion does not provide
the graph required by E101.091.  It replaces the diagonal graph by the
classical left--right eigenvector overlap matrix.

For a diagonalizable matrix

```text
C=S Lambda S^(-1),
H=S^*GS,                                           (1.1)
```

in a fixed positive source metric `G`, define

```text
O_(ij)=(H^(-1))_(ij)H_(ji).                       (1.2)
```

The exact connected Hessian is

```text
Tr[(z-C)^(-1)q(C)(z-C)^(-1)r(C)^(dagger_G)]
 =sum_(i,j)O_(ij)q(p_i)conj(r(p_j))/(z-p_i)^2.    (1.3)
```

Thus the resolvent denominator stays at `p_i`, but the adjoint value is an
all-points mixture.  The parity-Gram contraction becomes

```text
sum_(i,j)O_(ij)b(Q(p_i),Q(p_j)^*)/(z-p_i)^2,      (1.4)
```

not

```text
sum_i b(Q(p_i),Q(p_i)^*)/(z-p_i)^2.               (1.5)
```

The overlap matrix is the identity exactly when `C` is normal in the chosen
metric.  For a fixed CCM feature, accidental global cancellation is
possible, but it is an additional identity and not a consequence of
rank-one factorization.

There is a stronger falsifier.  An even real companion with the four roots
`{-2,-1,1,2}` and a globally even rank-one real polynomial atom has zero
diagonal Gram at every root, while (1.4) is nonzero.  Hence the nonnormal
adjoint produces false positives even on a parity-symmetric all-real divisor.

Finally, adding a commutator correction cannot change (1.3).  Every factor
preceding the adjoint commutes with `C`, so

```text
Tr[F(C)[C,X]]=0.                                  (1.6)
```

Changing the diagonal overlap values requires a central interpolation term,
which is the conjugate graph again.  Standard companion adjoints and
Sylvester/commutator corrections are therefore frozen inside the
fixed-metric affine Hessian class with central probes.  This no-go does not
cover parameter-dependent metrics, nonaffine deformations, noncentral legs
or corrections which modify the resolvent.  A singular nonnormal limit
remains admissible if it proves quantified disappearance of the complete
leakage in the Gamma--Euler topology and preserves the arithmetic source
identity before the limit.

No claim is made that the overlap formula is new.  It is the standard
Chalker--Mehlig/Petermann structure.  The contribution here is its exact
insertion into the parity-CCM contraction and the resulting all-real
falsifier and stop rule.

## 2. Positive metric and spectral coordinates

Let `C` act on `C^n`, let `G=G^*>0`, and use

```text
<x,y>_G=x^*Gy,
X^(dagger_G)=G^(-1)X^*G.                          (2.1)
```

Assume first that `C` has distinct eigenvalues `p_1,...,p_n`.  Choose right
eigenvectors as the columns of `S`:

```text
C=S Lambda S^(-1),
Lambda=diag(p_1,...,p_n).                         (2.2)
```

The eigenvector Gram and its inverse are

```text
H=S^*GS,
H^(-1)=S^(-1)G^(-1)S^(-*).                       (2.3)
```

Let

```text
P_i=SE_(ii)S^(-1)                                (2.4)
```

be the oblique spectral projectors.  They obey

```text
P_iP_j=delta_(ij)P_i,
sum_iP_i=I,
Tr(P_i)=1.                                        (2.5)
```

The projectors are algebraic, not orthogonal in general.

## 3. Exact nonnormal mixed Hessian

Let `q,r` be holomorphic on a neighborhood of the spectrum and put

```text
A=q(C),
B=r(C),
R(z)=(z-C)^(-1).                                  (3.1)
```

### Theorem 3.1 - Overlap decomposition

For `z` outside the spectrum,

```text
Tr[R(z)A R(z)B^(dagger_G)]
 =sum_(i,j)
   O_(ij)q(p_i)conj(r(p_j))/(z-p_i)^2,            (3.2)

O_(ij)=(H^(-1))_(ij)H_(ji)
      =Tr(P_iP_j^(dagger_G)).                     (3.3)
```

Equivalently,

```text
-partial_u partial_v log det
 [z-C-uq(C)-v r(C)^(dagger_G)]|_(0,0)
 =right side of (3.2).                            (3.4)
```

### Proof

In the eigenbasis,

```text
R A R
 =S diag(q(p_i)/(z-p_i)^2)S^(-1),                (3.5)

S^(-1)B^(dagger_G)S
 =H^(-1)diag(conj(r(p_j)))H.                     (3.6)
```

Taking the trace of the product gives

```text
sum_i q(p_i)/(z-p_i)^2
 [H^(-1)diag(conj(r(p_j)))H]_(ii),                (3.7)
```

which expands to (3.2).  Substitution of (2.4) gives (3.3).  The logarithmic
determinant identity follows from Jacobi differentiation. `QED`

There is no second resolvent denominator involving `p_j`.  Nonnormality is
carried entirely by the overlap coefficient and the value `r(p_j)`.

## 4. Structure of the overlap matrix

### Proposition 4.1 - Gram, sum and condition-number identities

The matrix `O=(O_(ij))` satisfies

```text
O=O^*>=0,

sum_j O_(ij)=1,
sum_i O_(ij)=1,
sum_(i,j)O_(ij)=n,                                (4.1)

O_(ii)=H_(ii)(H^(-1))_(ii)>=1.                   (4.2)
```

It is unchanged when any eigenvector is rescaled.  Moreover,

```text
O=I
 <=> H is diagonal
 <=> C is normal in <.,.>_G.                      (4.3)
```

### Proof

Equation (3.3) represents `O` as the Hilbert--Schmidt Gram of the oblique
projectors, so it is Hermitian positive semidefinite.  The row identity is

```text
sum_j(H^(-1))_(ij)H_(ji)=[H^(-1)H]_(ii)=1,       (4.4)
```

and the column identity follows from `HH^(-1)=I`.  Formula (4.2) is the
Schur-complement inequality for a positive matrix.  Equality in (4.2) holds
exactly when row and column `i` of `H` have no off-diagonal entries.

If `H` is diagonal, (1.2) gives `O=I`.  Conversely, `O=I` gives equality in
(4.2) for every `i`, hence `H` is diagonal.  Orthogonality of distinct
eigenspaces is equivalent to normality for a simple-spectrum matrix.  Direct
diagonal rescaling in (1.2) proves the invariance. `QED`

If `s_i` is the right eigenvector and `ell_i` its algebraic dual left
eigenvector, then

```text
O_(ii)=||s_i||_G^2||ell_i||_(G^(-1))^2.           (4.5)
```

This is the squared eigenvalue condition number, also called the diagonal
Petermann factor.  The row rule implies

```text
sum_(j!=i)O_(ij)=1-O_(ii)<=0,                     (4.6)
```

although individual off-diagonal entries need not be real when `n>=3`.

### Corollary 4.2 - Universal graph recovery is normality

The equality

```text
Tr[Rq(C)Rr(C)^(dagger_G)]
 =sum_i q(p_i)conj(r(p_i))/(z-p_i)^2              (4.7)
```

for every pair of polynomial probes `q,r` holds if and only if `C` is
`G`-normal.

### Proof

Polynomials of degree less than `n` interpolate arbitrary values on the
simple spectrum.  Equality of the distinct double-pole coefficients in
(3.2) and (4.7) therefore gives `O=I`.  Apply (4.3). `QED`

For one fixed pair, the exact condition is weaker:

```text
q(p_i){sum_jO_(ij)conj(r(p_j))-conj(r(p_i))}=0
for every i.                                      (4.8)
```

This is a feature-specific cancellation theorem which must be proved, not a
formal property of the adjoint.

## 5. Multiplicity blocks

If `C` is diagonalizable with distinct eigenvalues indexed by `alpha` and
semisimple multiplicities `m_alpha`, let `P_alpha` be its spectral
projectors and define

```text
O_(alpha,beta)=Tr(P_alpha P_beta^(dagger_G)).      (5.1)
```

Then

```text
Tr[Rq(C)Rr(C)^(dagger_G)]
 =sum_(alpha,beta)
  O_(alpha,beta)q(p_alpha)conj(r(p_beta))
  /(z-p_alpha)^2,                                 (5.2)

sum_beta O_(alpha,beta)=m_alpha,
sum_alpha O_(alpha,beta)=m_beta,
O_(alpha,alpha)>=m_alpha.                         (5.3)
```

The exact block diagonal collapse

```text
O_(alpha,beta)=m_alpha delta_(alpha,beta)          (5.4)
```

is equivalent to orthogonality of the spectral subspaces and hence to
normality.  A cyclic companion with a repeated root is not diagonalizable,
so it does not even enter (5.2).  Its Jordan response contains higher-order
poles rather than the required linear-multiplicity semisimple fibre.

## 6. Parity-CCM contraction

Retain the parity-CCM hypothesis of E101.091: let
`Q(z)=(q_(ab)(z))` be a symmetric matrix-valued holomorphic atom satisfying
`rank Q(z)<=1` for every `z`.  Define

```text
b(U,V)={tr(UV)-tr(U)tr(V)}/4.                     (6.1)
```

For each pair of spectral points put

```text
g_(ij)=b(Q(p_i),Q(p_j)^*).                        (6.2)
```

The diagonal value is the desired Gram.  Indeed, if
`Q(p_i)=kappa v v^T`, then

```text
g_(ii)=b(Q(p_i),Q(p_i)^*)
      =|kappa|^2[||v||^4-|v^Tv|^2]/4
      =g(p_i)>=0.                                 (6.3)
```

### Theorem 6.1 - Exact overlap leakage

The contracted connected adjoint Hessian is

```text
C_(C,G,Q)(z)
 =1/4[sum_(a,b)Tr(Rq_(ab)(C)R q_(ba)(C)^(dagger_G))
      -sum_(a,b)Tr(Rq_(aa)(C)R q_(bb)(C)^(dagger_G))]

 =sum_i 1/(z-p_i)^2 sum_j O_(ij)g_(ij).           (6.4)
```

Its difference from the desired diagonal current

```text
G_Q(z)=sum_i g_(ii)/(z-p_i)^2                     (6.5)
```

is exactly

```text
L_(C,G,Q)(z)
 =C_(C,G,Q)(z)-G_Q(z)

 =sum_i 1/(z-p_i)^2
   sum_(j!=i)O_(ij)[g_(ij)-g_(ii)].               (6.6)
```

### Proof

Apply Theorem 3.1 entry by entry.  The two matrix-index contractions give
`b(Q(p_i),Q(p_j)^*)`, proving the second line of (6.4).  Subtract (6.5) and
use the row identity in (4.1) to obtain (6.6). `QED`

The contraction `b` acts only in the finite jet indices.  The overlap matrix
acts in the spectral indices.  Rank one gives

```text
b(Q(p_i),Q(p_i))=0,                               (6.7)
```

but it says nothing about `g_(ij)` for `i!=j` and does not diagonalize `O`.

## 7. Holomorphic null channel versus adjoint channel

Because all entries of `Q(C)` are functions of the same matrix `C`, they
commute.  Replacing every metric adjoint in (6.4) by the corresponding
holomorphic entry gives

```text
1/4[sum_(a,b)Tr(Rq_(ab)(C)R q_(ba)(C))
    -sum_(a,b)Tr(Rq_(aa)(C)R q_(bb)(C))]=0.       (7.1)
```

Indeed, its spectral coefficient at `p_i` is
`b(Q(p_i),Q(p_i))=0`.

The source-built standard adjoint changes (7.1) into (6.4), not into (6.5).
Therefore the two requirements in `NA-4` remain separate:

```text
rank-one algebra proves the holomorphic channel is zero;
positive adjunction creates an overlap-contaminated channel;
identifying them requires a new identity.          (7.2)
```

Normality removes the overlap contamination but does not by itself identify
the adjoint channel with the holomorphic null channel.  The latter
identification remains the force-bearing arithmetic statement of E101.091.

## 8. A parity-symmetric all-real false positive

The falsifier can be made compatible with the real and parity symmetries of
the CCM atom.  Consider the even polynomial and its Frobenius companion

```text
f(w)=(w^2-1)(w^2-4)=w^4-5w^2+4,

C=[[ 0,1,0,0],
   [ 0,0,1,0],
   [ 0,0,0,1],
   [-4,0,5,0]].                                   (8.1)
```

Order the roots as `(-2,-1,1,2)`.  The right eigenvector matrix and the
Euclidean overlap matrix are

```text
S=[[ 1, 1,1,1],
   [-2,-1,1,2],
   [ 4, 1,1,4],
   [-8,-1,1,8]],

H=S^TS
 =[[ 85,15,-5,-51],
   [ 15, 4, 0, -5],
   [ -5, 0, 4, 15],
   [-51,-5,15, 85]],                              (8.2)

O=[[ 425/72,-25/8, 25/72,-17/8],
   [   -25/8, 34/9,     0, 25/72],
   [    25/72,   0,  34/9, -25/8],
   [    -17/8,25/72,-25/8,425/72]].               (8.3)
```

Direct multiplication gives `S^(-1)CS=diag(-2,-1,1,2)`, and (8.3) follows
from `O_(ij)=(H^(-1))_(ij)H_(ji)`.  Define the even real polynomial vector
and rank-one atom

```text
v(w)=((4-w^2)/3,(w^2-1)/3)^T,
Q(w)=v(w)v(w)^T.                                  (8.4)
```

At the four roots,

```text
Q(-1)=Q(1)=E_(11),
Q(-2)=Q(2)=E_(22).                                (8.5)
```

Every desired diagonal Gram vanishes.  The pair contraction is zero when
the two roots have the same absolute value and is `-1/4` otherwise:

```text
g_(ij)=0       if |p_i|=|p_j|,
g_(ij)=-1/4   if |p_i|!=|p_j|.                   (8.6)
```

Each row of (8.3) has cross-class sum `-25/9`.  Therefore

```text
sum_j O_(ij)g_(ij)=25/36
for p_i in {-2,-1,1,2},                           (8.7)

C_(C,I,Q)(z)
 =25/36 sum_(p in {-2,-1,1,2})1/(z-p)^2,         (8.8)

G_Q(z)=0.                                         (8.9)
```

This is an exact false positive on an entirely real spectrum.  It obeys the
finite structural conditions used in the proposal:

```text
real even coefficients;
simple real divisor invariant under p -> -p;
globally even symmetric rank-one atom;
ordinary positive adjoint in the Euclidean metric;
connected affine logarithmic Hessian with central probes.                (8.10)
```

Thus no argument based only on these properties can turn (6.4) into the
off-line discriminator (6.5).  The statement is deliberately limited to the
fixed-metric affine central-probe class.

## 9. Companion condition numbers

For a simple-root Frobenius companion in standard monomial coordinates and
the Euclidean metric `G=I`, the eigenvector matrix is a Vandermonde matrix up
to the chosen transpose convention.  If

```text
f(w)/(w-p_i)=sum_(k=0)^(n-1)b_(ik)w^k,            (9.1)
```

then the diagonal overlap has the explicit form

```text
O_(ii)
 ={[sum_(k=0)^(n-1)|p_i|^(2k)]
   [sum_(k=0)^(n-1)|b_(ik)|^2]}/|f'(p_i)|^2.      (9.2)
```

The off-diagonal entries are the corresponding product of the right and
left eigenvector Grams.  Therefore small `|f'(p_i)|`, root clustering and
Vandermonde ill-conditioning enlarge the overlap weights.  They do not
approximate the diagonal graph.

For every row,

```text
sum_(j!=i)|O_(ij)|>=O_(ii)-1.                     (9.3)
```

Hence a coefficient-blind estimate based on absolute overlap mass becomes
worse as the Petermann factor grows.  Cofinal escape may instead come from
weighted near-normality, overlap localization, feature flattening, signed
cancellation in the complete expression (6.6), or a combination of them.

## 10. Commutator corrections are invisible

### Theorem 10.1 - Connected trace descends modulo commutators

Let `F(C)` be any rational function defined on the spectrum and let `X` be
arbitrary.  Then

```text
Tr[F(C)[C,X]]=0.                                  (10.1)
```

In particular, replacing `r(C)^(dagger_G)` in Theorem 3.1 by

```text
r(C)^(dagger_G)+[C,X]                             (10.2)
```

does not change the connected Hessian.

### Proof

Since `F(C)C=CF(C)`, cyclicity gives

```text
Tr[F(C)CX]-Tr[F(C)XC]
 =Tr[CF(C)X]-Tr[CF(C)X]=0.                        (10.3)
```

`QED`

This closes corrections obtained only by solving a Sylvester equation for
off-diagonal entries in the fixed-metric affine Hessian.  In the
simple-spectrum regime of Sections 2--4, a commutator has zero diagonal in
the eigenbasis and cannot alter

```text
[H^(-1)diag(conj(r(p_j)))H]_(ii)
 =sum_jO_(ij)conj(r(p_j)).                        (10.4)
```

To replace (10.4) by `conj(r(p_i))`, one must add a central function `h(C)`
with interpolated values

```text
h(p_i)
 =conj(r(p_i))-sum_jO_(ij)conj(r(p_j)).           (10.5)
```

Formula (10.5) uses the individual spectral values and overlap matrix.  A
root-projector construction of `h` is divisor interpolation.  A source-first
formula for the same `h` would be genuinely new and must be exhibited; it
cannot be replaced by a commutator estimate.

## 11. Cofinal singular route

For a sequence of source-built diagonalizable simple-spectrum companions or
nonnormal sections, define the exact leakage by (6.6).  Semisimple repeated
eigenvalues use the block formula (5.2); Jordan sections require a separate
higher-pole analysis.  Recovery of the desired graph through this Hessian
requires

```text
L_(C_N,G_N,Q_N)(z)->0                             (11.1)
```

in the precise topology and limit order used by the Gamma--Euler identity.
The sum rules (4.1) alone guarantee (11.1) for spectrally constant
contractions.  Nonconstant feature-specific cancellations can occur, but
the parity CCM atom has no formal cancellation of that kind: the all-real
example proves that rank one, real type and parity do not suffice at fixed
dimension.

The leakage can nevertheless vanish cofinally through metric normality,
localization of `O_N`, flattening of the feature differences, signed
cancellation, or a combination of these mechanisms.  The lower bound
`sum_(j!=i)|O_(ij)|>=O_(ii)-1` only rules out an argument which discards all
signs while allowing the Petermann factor to grow.  A valid singular
construction must prove all of

```text
NO-1  an explicit mechanism for the complete leakage, such as weighted
      O_N->I, overlap localization, feature flattening or signed
      cancellation;

NO-2  L_(C_N,G_N,Q_N)->0 in the exact locally uniform, distributional or
      trace topology required by the Gamma--Euler limit;

NO-3  zero limiting response on every all-real controlled divisor;

NO-4  nonzero response for each resolved planted off-line quartet;

NO-5  linear multiplicity after semisimplification;

NO-6  compatibility with the Gamma, polar, prime and cutoff channels;

NO-7  source-side identification with the rank-one null value before the
      cofinal limit.                               (11.2)
```

The mechanism and topology in `NO-1`--`NO-2` must be declared before a
generic overlap or gap estimate is promoted.  The finite falsifier rules out
formal cancellation from parity and rank one; it does not rule out a proved
cofinal cancellation.

## 12. Literature and nonduplication

The overlap kernel in (3.3) is classical.  A selected primary boundary is:

```text
J. T. Chalker, B. Mehlig,
Eigenvector Statistics in Non-Hermitian Random Matrix Ensembles:
  https://arxiv.org/abs/cond-mat/9809090
  https://doi.org/10.1103/PhysRevLett.81.3367

B. Mehlig, J. T. Chalker,
Statistical properties of eigenvectors in non-Hermitian Gaussian random
matrix ensembles:
  https://arxiv.org/abs/cond-mat/9906279
  https://doi.org/10.1063/1.533302

P. Bourgade, G. Dubach,
The distribution of overlaps between eigenvectors of Ginibre matrices:
  https://arxiv.org/abs/1801.01219
  https://doi.org/10.1007/s00440-019-00953-x

F. Benaych-Georges, O. Zeitouni,
Eigenvectors of non normal random matrices:
  https://arxiv.org/abs/1806.06806
  https://doi.org/10.1214/18-ECP171

K. Esaki, M. Katori, S. Yabuoku,
Eigenvalues, eigenvector-overlaps, and regularized Fuglede--Kadison
determinant of the non-Hermitian matrix-valued Brownian motion:
  https://arxiv.org/abs/2306.00300
  https://doi.org/10.1063/5.0179558

G. Cipolloni, L. Erdos, J. Xu,
Optimal decay of eigenvector overlap for non-Hermitian random matrices:
  https://arxiv.org/abs/2411.16572
  https://doi.org/10.1016/j.jfa.2025.111180

K. Petermann,
Calculated spontaneous emission factor for double-heterostructure
injection lasers with gain-induced waveguiding:
  https://doi.org/10.1109/JQE.1979.1070064

A. E. Siegman,
Excess spontaneous emission in non-Hermitian optical systems:
  https://doi.org/10.1103/PhysRevA.39.1253

J. Liesen,
When is the Adjoint of a Matrix a Low Degree Rational Function in the
Matrix?:
  https://doi.org/10.1137/060675538

K.-C. Toh, L. N. Trefethen,
Pseudozeros of polynomials and pseudospectra of companion matrices:
  https://doi.org/10.1007/s002110050069

C.-K. Li, J. C.-H. Lin,
Confluent Vandermonde matrix and related topics:
  https://arxiv.org/abs/2403.01474                 (12.1)
```

Chalker--Mehlig already define the left--right overlap matrix, prove its sum
rule and use it in two-resolvent statistics.  Esaki--Katori--Yabuoku write
the same matrix as `H^(-1)_(ij)H_(ji)` and connect overlaps to logarithmic
determinant derivatives.  Petermann and Siegman identify the diagonal
condition factor.  Companion/Vandermonde eigenvector conditioning and
adjoint interpolation are also established.

No novelty is claimed for

```text
Jacobi differentiation of log det;
left--right overlap matrices;
Petermann factors;
Vandermonde companion conditioning;
the polarization b of the rank-one determinant.   (12.2)
```

Equations (6.4)--(6.6) are a direct specialization of the classical overlap
formalism and are retained as a CCM bookkeeping lemma, not claimed as an
external novelty.  The program-specific contribution is the
parity-symmetric all-real falsifier (8.8) and the precisely scoped stop rule.
They do not remove the classical overlap wall.

## 13. Stop rule and status

Inside fixed-metric affine determinant Hessians built from one central probe
`q(C)` and the metric adjoint of another central probe `r(C)`, freeze:

```text
generic nonnormal ordinary-adjoint companion Hessians as a formal or
  universal construction of the missing graph, unless a feature-specific
  cancellation of (4.8) or (6.6) is proved;
Petermann or eigenvector-overlap estimates without the signed CCM leakage;
commutator and Sylvester corrections to the adjoint leg;
claims that rank one kills the spectral off-diagonal terms;
cofinal normality inferred from small residuals without a metric theorem.
                                                               (13.1)
```

Retain only:

```text
NORMAL-ADJOINT-GAMMA-EULER-LIFT of E101.091, if the positive star is
constructed before divisor extraction;

FEATURE-SPECIFIC-NONNORMAL-CANCELLATION, if (4.8) or (6.6) is proved exactly
at finite level from the Gamma--Euler source;

SINGULAR-NONNORMAL-CCM-CANCELLATION, only with the quantified package
NO-1--NO-7;

a direct arithmetic Castelnuovo theorem after the M2 correction.         (13.2)
```

```text
proved:
  exact nonnormal connected-Hessian overlap decomposition;
  Gram and sum identities for the overlap matrix;
  universal diagonal recovery iff metric normality;
  semisimple multiplicity-block formula;
  exact CCM overlap leakage identity;
  all-real rank-one false positive;
  companion Petermann amplification;
  commutator invisibility;

not new in general form:
  overlap decomposition, its CCM specialization and Petermann structure;

still open:
  a source-specific proof of NO-1--NO-7;
  NA-1--NA-4 of E101.091;
  DIRECTIONAL-IDENT and Omega7.                    (13.3)
```
