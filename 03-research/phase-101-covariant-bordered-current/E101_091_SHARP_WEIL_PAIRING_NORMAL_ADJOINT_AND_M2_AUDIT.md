# E101.091 - Sharp Weil pairing, normal adjoint lift and M2 audit

## 1. Decision

Three questions which had been treated as one are now separated exactly.

First, the unconditional Weil form already has linear divisor multiplicity
and an exact one-level pairing,

```text
Q_W(v_1,v_2)
 =sum_gamma m_gamma vhat_1(gamma)
                    conj(vhat_2(conj gamma)).       (1.1)
```

This is the sharp pairing.  For a real-type CCM atom it returns the
holomorphic square at `gamma`, not the pointwise Hermitian square.  Replacing
the last factor by `conj(vhat_2(gamma))` is precisely the missing conjugate
graph and is not an innocuous polarization.

Second, every scalar holomorphic two-parameter deformation has the exact
local response

```text
-partial_u partial_v log F
 =m p_u p_v/(z-p)^2+m p_(uv)/(z-p)+regular.         (1.2)
```

Translations, Euler twists, Schwarz reflection and the functional equation
can produce the four symmetry transports of `p_u`; none produces
`conj(p_u)` at the same spectral point.  Requiring it on the divisor is
conjugate interpolation.  Thus scalar mixed deformations are closed as a
route to `PARITY-GRAM-GRAPH-TRACE`.

Third, an operator-valued deformation with an adjoint does produce the
right graph:

```text
-partial_u partial_v log det(z-D-uA-vB^*)|_(0,0)
 =Tr((z-D)^(-1)A(z-D)^(-1)B^*).                   (1.3)
```

For normal `D`, `A=q_a(D)`, `B=q_b(D)`, its spectral side is

```text
sum_p m_p q_a(p)conj(q_b(p))/(z-p)^2.             (1.4)
```

The identity is exact and preserves linear multiplicity.  Its abstract
realization, however, is the divisor graph in operator notation.  In finite
dimension, every positive metric which makes a companion normal necessarily
realizes the interpolation rule `r(p)=conj(p)` in its adjoint.  In the
infinite divisor model, multiplication on the Poincare--Lelong measure starts
by inserting the zero divisor.  Therefore only the following source-first
version remains live:

```text
NORMAL-ADJOINT-GAMMA-EULER-LIFT:
construct the star operation and the connected trace (1.3) directly from
the Gamma--Euler source, before divisor extraction, and identify its
contracted source side with the vanishing rank-one channel.               (1.5)
```

This document also audits the `M2/X3` closure claimed in paper 36.  The
displayed argument does not establish the stated conditional theorem: `X3`
applies only to classes of positive square, while the proof invokes it on a
class of negative square.  The finite shadow `M2_N` is untyped, nonconvex
and becomes automatic under a common cone shift.  A corrected conic
membership problem is given below, but it does not imply Omega7 without an
additional Castelnuovo inequality.

No assertion in this document proves Omega7.  The advance is a rigorous
elimination of two circular fronts and an exact specification of the one
operator-valued construction which has not been reduced to an earlier
no-go.

## 2. The parity-Gram target

Retain the notation of E101.085.  For each parity block `sigma`,

```text
Q_sigma(z)=K(z)v_sigma(z)v_sigma(z)^T,             (2.1)
```

is a symmetric rank-at-most-one matrix.  Define the bilinear contraction

```text
b(U,V)={tr(UV)-tr(U)tr(V)}/4.                      (2.2)
```

Then

```text
g_sigma(z)=b(Q_sigma(z),conj(Q_sigma(z)))>=0,
b(Q_sigma(z),Q_sigma(z))=0.                        (2.3)
```

The second identity follows from

```text
tr(Q_sigma^2)=tr(Q_sigma)^2                       (2.4)
```

for a rank-one matrix.  The finite target is

```text
G_PAR(z)=g_e(z)+g_o(z),                            (2.5)
```

which vanishes for real `z` and is strictly positive for each fixed
resolved nonreal quartet.  A finite-window or properly regularized spectral
trace must have the form

```text
sum_p m_p G_PAR(p),                                (2.6)
```

with one divisor weight, not `m_p^2`.

The finite CCM atoms have the two exact symmetries

```text
Q_sigma(-z)=Q_sigma(z),
Q_sigma^sharp(z):=conj(Q_sigma(conj z))=Q_sigma(z). (2.7)
```

Consequently,

```text
Q_sigma(conj p)=conj(Q_sigma(p)).                  (2.8)
```

The target (2.3) may therefore be described in either of two equivalent
ways:

```text
same-point Hermitian graph:
  Q_sigma(p) tensor conj(Q_sigma(p));

conjugate-point bilinear graph:
  Q_sigma(p) tensor Q_sigma(conj p).               (2.9)
```

The distinction between sharp conjugation and pointwise conjugation is the
complete obstruction studied below.

## 3. The exact Weil pairing is sharp, not pointwise Hermitian

Let

```text
Xi(z)=xi(1/2-iz),                                  (3.1)
```

so RH is the statement that the zero multiset `Gamma` of `Xi` is contained
in the real axis.  For compactly supported smooth test functions, the Weil
explicit formula gives unconditionally

```text
Q_W(v_1,v_2)
 =sum_(gamma in Gamma)m_gamma
   vhat_1(gamma)conj(vhat_2(conj gamma)).           (3.2)
```

The formula includes all zeros with their ordinary divisor multiplicities.
It is already a one-trace formula; no all-pairs product is present.

### Proposition 3.1 - Sharp collapse for real-type atoms

If `h^sharp=h`, then the summand in (3.2) with `vhat_1=vhat_2=h` is

```text
h(gamma)conj(h(conj gamma))=h(gamma)^2.            (3.3)
```

It is not `|h(gamma)|^2` unless `h(gamma)` is real.

### Proof

Real type means

```text
h(conj gamma)=conj(h(gamma)).                      (3.4)
```

Conjugating (3.4) gives (3.3). `QED`

For the matrix atom `Q_sigma`, place each entry in the admissible finite test
class, or retain the same cutoff required by `PGT-2`, apply (3.2) entry by
entry and contract with `b`.  Equations (2.3) and (3.3) give

```text
b(Q_sigma(gamma),Q_sigma(gamma))=0,                (3.5)
```

not `g_sigma(gamma)`.  The exact Weil formula therefore lands on the
rank-one null channel.

The desired replacement would be

```text
conj(vhat_2(conj gamma))
       --> conj(vhat_2(gamma)).                    (3.6)
```

For a real-type test this is the replacement

```text
h(gamma) --> conj(h(gamma))=h(conj gamma).         (3.7)
```

On RH, `conj gamma=gamma`, so (3.2) and the pointwise Hermitian form agree.
Off RH they differ.  Thus using positivity of (3.2) as if it were the
pointwise Gram is exactly the classical Weil criterion, not a derivation of
the missing graph.

### Corollary 3.2 - Suzuki's formula does not close PGT-1

The exact formula (3.2) supplies Gamma--Euler access and linear
multiplicity, but its spectral involution is

```text
h(gamma) -> conj(h(conj gamma))=h^sharp(gamma).    (3.8)
```

`PARITY-GRAM-GRAPH-TRACE` instead needs

```text
h(gamma) -> conj(h(gamma)).                        (3.9)
```

For the even real-type CCM atom, (3.8) is the identity and (3.9) is the
missing conjugate-point transport.  No novelty is claimed for (3.2); the
new datum is the exact reason it cannot be substituted for (2.6).

## 4. Local mixed deformation calculus

Let `F(z;u,v)` be holomorphic near `(p,0,0)`.  Suppose a zero of constant
multiplicity `m` persists as a holomorphic branch `p(u,v)` and write, with
`a` holomorphic,

```text
F(z;u,v)=a(z;u,v)[z-p(u,v)]^m,
a(p;0,0)!=0.                                      (4.1)
```

### Theorem 4.1 - Mixed logarithmic principal part

At `(u,v)=(0,0)`,

```text
-partial_u partial_v log F(z;u,v)
 =m p_u p_v/(z-p)^2+m p_(uv)/(z-p)+H(z),           (4.2)
```

where `H` is holomorphic near `p`.

### Proof

The factor `a` contributes only a holomorphic term.  Direct differentiation
gives

```text
-partial_u partial_v log[z-p(u,v)]
 =p_u p_v/(z-p)^2+p_(uv)/(z-p).                   (4.3)
```

Multiplication by `m` proves (4.2). `QED`

If instead the Taylor expansion is

```text
F=f+uA+vB+uvC+(u^2/2)A_(20)+(v^2/2)A_(02)+O_3,   (4.4)
```

where `A=F_u|_0`, `B=F_v|_0`, `C=F_(uv)|_0`, and `O_3` has total parameter
degree at least three,

and `p` is a simple zero of `f`, implicit differentiation gives

```text
p_u=-A(p)/f'(p),
p_v=-B(p)/f'(p),                                  (4.5)

p_(uv)
 =-[C+A'p_v+B'p_u+f''p_up_v](p)/f'(p).            (4.6)
```

Thus the mixed simple pole is not optional.  Any proposal which reads only
the double pole must either prove `p_(uv)=0` or include its cancellation.

### Proposition 4.2 - Multiplicity-preserving scalar transport

Let `q,r` be holomorphic and put

```text
Phi(z;u,v)
 =z-uq(z)-vr(z)+uv[q'(z)r(z)+r'(z)q(z)],          (4.7)

F(z;u,v)=G(z;u,v)Xi(Phi(z;u,v)),                  (4.8)
```

where `G` is locally nonzero.  Locally at each zero `p` of `Xi`, with its
full multiplicity, the corresponding zero branch moves with

```text
p_u=q(p),
p_v=r(p),
p_(uv)=0.                                         (4.9)
```

### Proof

The zero equation is

```text
Phi(p(u,v);u,v)=p.                                (4.10)
```

At the origin, `Phi_z=1`, `Phi_u=-q`, `Phi_v=-r`, so the first two
identities follow.  Mixed differentiation gives

```text
p_(uv)-q'(p)r(p)-r'(p)q(p)
       +q'(p)r(p)+r'(p)q(p)=0.                    (4.11)
```

The map `Phi` is locally biholomorphic, hence composition preserves the
order of the zero. `QED`

Formula (4.7) proves that scalar holomorphy, linear multiplicity and removal
of the connection pole can coexist.  The remaining obstruction is exactly
the demanded choice

```text
r(p)=conj(q(p)).                                  (4.12)
```

## 5. Scalar conjugate-velocity no-go

### Lemma 5.1 - Open-set obstruction

Let `q,r` be holomorphic on a connected open set.  If

```text
r(z)=conj(q(z))                                   (5.1)
```

throughout that set, then both functions are constant.

### Proof

The right side of (5.1) is antiholomorphic.  A function which is both
holomorphic and antiholomorphic on a connected open set is constant. `QED`

The lemma does not forbid interpolation on a discrete divisor.  It says
that such interpolation cannot arise from a universal local holomorphic
identity.  On a discrete set, constructing `r` with (4.12) is precisely the
missing zero-adapted operation.

Now write, for a scalar perturbation,

```text
q_H(p)=-H(p)/Xi'(p)                               (5.2)
```

for the velocity generated by an additive scalar perturbation `H` at a
simple zero.  Matrix-valued velocities are obtained only entry by entry,
using `H_(ij)=-Xi' q_(ij)`.  Since `Xi` is even and real type, the source operations
available from reflection and the functional equation give

```text
source perturbation       velocity at p

H(z)                      q_H(p)
H(-z)                    -q_H(-p)
H^sharp(z)                conj(q_H(conj p))
H^sharp(-z)              -conj(q_H(-conj p)).     (5.3)
```

No row of (5.3) is formally the same-point conjugate `conj(q_H(p))`.
Special perturbations or points may make two values coincide, but that is
not an identity of transports.  Within a covariantly completed additive
family, Euler coefficient conjugation gives the third row, the even
functional equation gives the second, and combining them gives the fourth.
Terms added to `H` which are proportional to `Xi` vanish at the zero and do
not change (5.2).  Multiplying `H` by an arbitrary fixed completion factor
would instead rescale the velocity and is not included in this statement.
The table concerns simple zeros; the arbitrary-multiplicity closure rests
on Proposition 4.2.

For `q=Q_sigma`, (2.7) reduces every row of (5.3) to either
`Q_sigma(p)` or `-Q_sigma(p)`.  The sign can be absorbed in the deformation
parameter, and the one-trace contraction is always

```text
b(Q_sigma(p),Q_sigma(p))=0.                       (5.4)
```

To identify one of these available velocities with the required
`Q_sigma(conj p)`, one would have to impose

```text
Q_sigma(p)=Q_sigma(conj p)                        (5.5)
```

inside the transport, or otherwise manufacture the value at `conj p`.
Equation (5.5) does not construct the Gram: it makes
`g_sigma(p)=b(Q_sigma(p),Q_sigma(conj p))` vanish.  The legitimate target
must transport the second factor to `Q_sigma(conj p)` without identifying
the two values.  Cofinal discrimination in E101.085 shows that (5.5) for
the complete parity jet excludes every resolved off-line quartet.  It is
not a harmless symmetry premise; it contains the desired conclusion.

### Stop rule 5.2

Freeze all scalar variants generated only by

```text
additional Euler parameters;
holomorphic translations or heat flows;
z -> -z;
Schwarz reflection;
completion-factor twists;
finite compositions of these operations.          (5.6)
```

A scalar successor is admissible only if it displays a new Xi-specific
source identity which proves (4.12) on the divisor without extracting that
divisor or assuming (5.5).

## 6. Why nonholomorphic contour insertion is divisor extraction

A natural response to Lemma 5.1 is to insert the pointwise conjugate weight
directly in a contour formula.  The resulting identity is exact, but it is
Poincare--Lelong in another notation.

Let `D` be a bounded domain with smooth boundary, let `F` be holomorphic and
nonzero on the boundary, and let `Phi` be a smooth matrix-valued function.
Then Cauchy--Pompeiu gives

```text
sum_(p in D)m_p Phi(p)
 =1/(2 pi i) int_(partial D)Phi(z)F'(z)/F(z) dz
  -1/pi int_D F'(z)/F(z) partial_bar Phi(z) dA(z). (6.1)
```

### Proof

In distributions,

```text
partial_bar(F'/F)=pi sum_p m_p delta_p.            (6.2)
```

Apply Stokes to `Phi F'/F` and rearrange. `QED`

For a holomorphic `Phi`, the area term vanishes and (6.1) is the ordinary
residue theorem.  For

```text
Phi(z)=Q_sigma(z) tensor conj(Q_sigma(z)),         (6.3)
```

the area term is the price of the same-point Hermitian graph.  It contains
`F'/F` throughout the domain, hence the full divisor current.  Compactly
supported versions of (6.1) are equivalent to applying

```text
(1/(2 pi)) Delta log|F|=sum_p m_p delta_p.         (6.4)
```

Thus (6.1) is a valid exact detector once the divisor is allowed, but it is
not a source-first Gamma--Euler transport.

### Proposition 6.1 - Two-residue multiplication has the wrong graph

The bi-principal part of the product of two ordinary logarithmic derivatives
is

```text
PP_(z,w){[F'(z)/F(z)][F'(w)/F(w)]}
  =sum_(p,q in D)m_pm_q/[(z-p)(w-q)].             (6.5)
```

This is a finite local statement.  Zeros exterior to `D` are absorbed into
the singly polar or holomorphic terms of the chosen local decomposition;
the displayed bi-principal term contains every pair in `D`.  Restriction to
the diagonal produces
`m_p^2`, not `m_p`; ordinary smoothing does not change this multiplicity.

Moreover, the set

```text
G_conj={(z,w) in C^2 : w=conj(z)}                 (6.6)
```

is totally real and is not a complex analytic divisor.  Therefore no
universal meromorphic residue kernel can have (6.6) as its polar divisor.
A meromorphic kernel can select `w=z`, `w=-z` or another holomorphic graph;
it cannot select `w=conj(z)` without nonholomorphic data or poles tailored
to the chosen divisor.

### Proof

The multiplicity assertion is immediate from (6.5).  If (6.6) were a
complex curve, its tangent space would be invariant under multiplication by
`i`.  The tangent vectors have the form `(h,conj h)`, while multiplication
by `i` gives `(ih,i conj h)`, which has the required form
`(k,conj k)` only when `h=0`.  Hence (6.6) is totally real. `QED`

## 7. A discriminant test for universal analytic formulas

The obstruction can be seen in a one-parameter polynomial family without
zeta.  Fix `A>0` and consider

```text
P_t(z)=(z^2-A)^2-t,                               (7.1)
```

for real `t` with `0<|t|<A^2`.

For `t>0`,

```text
z^2=A+sqrt(t),  A-sqrt(t),                        (7.2)
```

so all four roots are real.  For `t<0`,

```text
z^2=A+i sqrt(|t|),  A-i sqrt(|t|),                (7.3)
```

and the roots form a nonreal quartet.

Choose one `t_-<0` in the interval and a finite parity jet which resolves
the quartet of `P_(t_-)`.  Keep that jet fixed and let

```text
S(t)=sum_(P_t(p)=0)G_PAR(p).                       (7.4)
```

Then

```text
S(t)=0 for t>0,
S(t_-)>0.                                         (7.5)
```

### Proposition 7.1 - Holomorphic parameter formulas cannot produce `S`

There is no fixed-contour residue expression for (7.4) whose integrand is
holomorphic in `t` across `t=0` and whose only spectral input is the
holomorphic family `P_t`.

### Proof

Choose the common parameter domain large enough to contain `t_-` and a
positive interval.  Such a contour integral would be holomorphic in complex
`t` on that connected domain.  Equation (7.5) makes it vanish on a real
interval with an interior accumulation point, so the identity theorem would
make it vanish identically.  This contradicts the second line of (7.5).
`QED`

Any exact finite formula must therefore leave the fixed-contour,
parameter-holomorphic class of Proposition 7.1.  Standard ways to leave it
include

```text
coefficient conjugation tied to a real parameter;
a discriminant sign or Hermite signature;
a partial_bar area term;
primary factorization of the polynomial;
a singular nonnormal limit.                       (7.6)
```

These are standard locations at which the conjugate-root graph can enter.

## 8. The finite Hermite graph

Let `P` be a squarefree polynomial stable under conjugation and let

```text
A_P=C[z]/(P).                                     (8.1)
```

In the idempotent evaluation basis, define the linear involution

```text
(kappa_P f)(p)=f(conj p).                         (8.2)
```

Then

```text
Tr(M_f kappa_P M_g kappa_P)
 =sum_(P(p)=0)f(p)g(conj p).                      (8.3)
```

For real-type `g`, this is the pointwise Hermitian graph.  Formula (8.3) is
exact and has linear multiplicity in the squarefree case.

The involution is not supplied by ordinary multiplication in `A_P`.  It is
equivalent to the unique interpolation polynomial `r_P`, of degree less
than `deg P`, satisfying

```text
r_P(p)=conj(p),
kappa_P f=f composed with r_P modulo P.            (8.4)
```

Thus the square-free quotient implementation is Lagrange interpolation; its
multiple-root extension is confluent Hermite interpolation.  For multiple
roots, one must either add confluent jet data in each primary
factor or semisimplify and attach the multiplicity as a weight.  Neither
operation is furnished by the coefficients of an ordinary one-trace
convolution without solving the conjugate graph problem.

The finite quotient does not prove a nonexistence theorem for an
Xi-specific arithmetic construction.  It proves the classification needed
for the novelty gate:

```text
an explicitly inserted kappa_P, r_P, root idempotent basis, Hermite matrix
or primary decomposition is divisor-side data, not PGT-1.                 (8.5)
```

## 9. The normal-adjoint Hessian

After the divisor-explicit quotient involution of Section 8, the adjoint is
the first surviving candidate operation in this audit which can create
pointwise conjugation before multiplying spectral values.

Let `D` be a finite-dimensional normal operator, let

```text
R(z)=(z-D)^(-1),
A=q_a(D),
B=q_b(D),                                         (9.1)
```

and define

```text
D(u,v)=D+uA+vB^*.                                 (9.2)
```

### Theorem 9.1 - Connected adjoint trace

For `z` outside the spectrum,

```text
-partial_u partial_v log det[z-D(u,v)]|_(0,0)
 =Tr[R(z)A R(z)B^*]
 =sum_p m_p q_a(p)conj(q_b(p))/(z-p)^2.           (9.3)
```

### Proof

The determinant derivative gives

```text
partial_u log det[z-D(u,v)]|_0=-Tr(RA).           (9.4)
```

Since `partial_v R=RB^*R`, differentiating (9.4) gives the first equality.
Normality supplies an orthogonal spectral resolution

```text
D=sum_p p E_p,
A=sum_p q_a(p)E_p,
B^*=sum_p conj(q_b(p))E_p,                        (9.5)
```

with `Tr(E_p)=m_p`; substitution proves the second equality. `QED`

The logarithm is essential.  The mixed Hessian of the determinant itself is

```text
partial_u partial_v det M
 =det M[(partial_u log det M)(partial_v log det M)
        +partial_u partial_v log det M],          (9.6)
```

and the product of the first derivatives restores all spectral pairs and
quadratic multiplicity.

For the matrix-valued CCM atom, apply (9.3) on the tensor product of the
spectral space with the finite parity-jet space.  On the spectral fibre
`E_p`,

```text
[Q_sigma(D)^*]|_(E_p)
 =Q_sigma(p)^*=conj(Q_sigma(p)),                  (9.7)
```

because `Q_sigma(p)^T=Q_sigma(p)`.  Notice that (9.7) is the operator
adjoint, not coefficientwise Schwarz reflection in a holomorphic functional
calculus.

One tensor-product determinant gives only the first term

```text
sum_p m_p tr[Q_sigma(p)Q_sigma(p)^*]/(z-p)^2.     (9.8)
```

To realize the complete contraction `b`, define the connected scalar
Hessian

```text
H_z(f,g)
 :=Tr[R(z)f(D)R(z)g(D)^*]
  =sum_p m_p f(p)conj(g(p))/(z-p)^2.              (9.9)
```

If `Q_sigma=(q_(ij))` is symmetric, the exact finite linear combination

```text
1/4[sum_(i,j)H_z(q_(ij),q_(ji))
    -sum_(i,j)H_z(q_(ii),q_(jj))]
 =sum_p m_p g_sigma(p)/(z-p)^2                   (9.10)
```

supplies the trace subtraction in (2.2).  Thus the result is not obtained
from the tensor determinant alone; it is a finite contraction of connected
logarithmic Hessians.

The normal-adjoint lift therefore yields

```text
sum_p m_p g_sigma(p)/(z-p)^2.                     (9.11)
```

Hence the normal-adjoint lift meets simultaneously:

```text
same spectral fibre;
pointwise conjugation;
linear multiplicity;
removal of the mixed simple pole;
connected rather than all-pairs response.         (9.12)
```

This is why (1.5) is the minimal surviving target identified in this audit.

## 10. Why the abstract normal model is not source-first

### 10.1 Poincare--Lelong multiplication model

The zero divisor defines the positive atomic measure

```text
mu_Xi=(1/(2 pi))Delta log|Xi|
     =sum_p m_p delta_p.                          (10.1)
```

The scalar space `L^2(mu_Xi)` records the mass of an atom in its norm but
still gives that atom a one-dimensional eigenspace.  To reproduce divisor
multiplicity as operator trace, use instead

```text
H_Xi=direct-sum_p C^(m_p),                        (10.2)

Dom(D)={x:sum_p |p|^2||x_p||^2<infinity},
(Dx)_p=p x_p.                                     (10.3)
```

The masses in (10.1) determine the fibre dimensions.  The operator `D` is
closed, densely defined and normal, and it has compact resolvent.  On this
space, `q(D)^*` acts on the `p` fibre by `conj(q(p))`.  Every finite height
truncation satisfies Theorem 9.1 exactly.

Since `Xi(0)!=0`, the inverse is defined, and the zero-counting law gives

```text
D^(-1) in S_s for every s>1,
D^(-1) not in S_1.                                (10.4)
```

Accordingly, the Hilbert--Schmidt determinant converges canonically with
genus one.  The complete divisor is invariant under `p -> -p`, so pairing
the two determinant factors gives `1-z^2/p^2`.  Parity and the value at zero
therefore give the exact normalization

```text
Xi(z)=Xi(0) det_2(I-zD^(-1)).                     (10.5)
```

Without the known parity and normalization of `Xi`, Hadamard factorization
would leave an exponential `exp(a+bz)`.  Here parity forces `b=0` and the
value at zero fixes `exp(a)=Xi(0)`.

For a relative perturbation, one needs at least

```text
R(z)q_a(D), R(z)q_b(D) in S_2,

sum_p m_p|q_a(p)|^2/|z-p|^2<infinity,
sum_p m_p|q_b(p)|^2/|z-p|^2<infinity.             (10.6)
```

These conditions hold for appropriately decaying probes and need not hold
for polynomially growing ones.  For the single relative determinant

```text
det_2[I-uR(z)q_a(D)-vR(z)q_b(D)^*],               (10.6a)
```

the linear subtraction in `det_2` does not alter the mixed derivative.
Factoring regularized determinants can create the standard multiplicative
anomaly, so any factorization or additional normalization must be proved to
have no uncontrolled `uv` counterterm.

Thus the formal multiplication rule

```text
(Df)(p)=p f(p)                                    (10.7)
```

is rigorously meaningful with the domain and fibre convention above.  The
model proves abstract existence but begins with (10.1), which is the
full divisor extracted by Poincare--Lelong.  It does not derive the adjoint
graph from Gamma--Euler.

### 10.2 Finite normality equals conjugate interpolation

Let `f` be monic and let `C_f` be its companion matrix.  When `f` is
square-free, enumerate its roots as `p_1,...,p_n` and choose an eigenvector
matrix `S` such that

```text
C_f=S diag(p_1,...,p_n)S^(-1).                   (10.8)
```

For a positive definite metric `G`, write

```text
C_f^(dagger_G)=G^(-1)C_f^*G.                     (10.9)
```

### Theorem 10.1 - A normal metric forces the conjugate graph

There exists a positive metric for which the cyclic companion `C_f` is
normal if and only if `f` is square-free.  In that case, `C_f` is normal for
the `G` inner product if and only if

```text
G=S^(-*)W S^(-1)                                 (10.10)
```

for some positive diagonal matrix `W`.  In that case

```text
C_f^(dagger_G)
 =S diag(conj p_1,...,conj p_n)S^(-1)
 =r_f(C_f),                                       (10.11)
```

where `r_f` is the unique polynomial of degree less than `n` such that

```text
r_f(p_j)=conj(p_j).                               (10.12)
```

### Proof

Normality in a positive metric is equivalent to orthogonality of the
eigenspaces.  In the eigenvector basis this says exactly that `S^*GS=W` is
positive diagonal, proving (10.10).  Substitution into (10.9) gives the
first equality in (10.11).  Lagrange interpolation and the functional calculus give
the second. `QED`

Thus constructing the positive normalizing metric also constructs the
conjugate-root polynomial through

```text
r_f(C_f)=G^(-1)C_f^*G.                            (10.13)
```

When the root set of `f` is stable under conjugation, this is the same `r_f`
as (8.4), and it induces the quotient involution.  Without that stability,
the interpolant still exists but does not define an endomorphism which
permutes the root algebra.  If `f` is not square-free, the minimal
polynomial of its cyclic companion equals `f`, so the companion is not
diagonalizable; a normal operator in a positive metric is diagonalizable.
This also proves the first assertion of the theorem.  To retain a zero of
multiplicity `m`, one must first
semisimplify the local algebra and then attach an `m`-dimensional spectral
fibre, or supply the equivalent primary data.

Theorem 10.1 does not assert that no coefficient algorithm can ever produce
`G`.  It identifies exactly what every such metric contains: a positive
source construction which realizes the conjugate-root graph, including
multiplicity.  Conversely, `r_f` alone does not determine `G`; after finding
the interpolant one must still solve

```text
C_f^*G=G r_f(C_f)                                 (10.13a)
```

and certify `G>0`, with the diagonal weights `W` remaining free.  Calling
the output a metric or an adjoint does not lower the graph burden.

### 10.3 The mixed-moment form contains the same graph

Use the companion convention in which `C_f` is multiplication by `z` on
`C[z]/(f)`.  In the monomial basis, let

```text
V_(j,r)=p_j^r.                                    (10.14)
```

Then `VC_f=diag(p_j)V` and `S=V^(-1)`.  Every normalizing metric is
transported from a positive diagonal weight,
so its moment matrix has entries

```text
M_(r,s)=[V^*WV]_(r,s)
       =sum_j w_j conj(p_j)^r p_j^s.              (10.15)
```

Newton sums and ordinary companion traces provide holomorphic moments

```text
sum_j p_j^k                                       (10.16)
```

and the classical bilinear Hermite matrix uses moments of `p_j^(r+s)`.
The positive Gram (10.15) instead contains the mixed conjugate graph.
Therefore a normal Hessenberg realization obtained by Gram--Schmidt does
not avoid the obstruction: its required input matrix `M` already is the
missing graph.  For the transposed Frobenius convention the matrices reverse
orientation, but the mixed moments and the conclusion are unchanged.

## 11. Relation to current spectral constructions

The normal-adjoint target must not be confused with finite self-adjoint
operators whose low spectrum numerically approaches the on-line zeros.

The closed localized Weil form of Connes--Consani--Moscovici has a canonical
self-adjoint operator unconditionally.  A separate rank-one perturbation of
the finite scaling operator is the object used for the real-zero and
determinant construction; its asserted self-adjoint realization uses the
finite simple-lowest-eigenvalue and even-eigenvector hypotheses.  Their
analysis lists those finite hypotheses and convergence of the normalized
determinants to `Xi` as distinct missing steps.

The mode of convergence matters.  Strong-resolvent convergence alone does
not give complete pointwise convergence of spectra and permits spectral
loss.  A route to RH would instead need, for example, locally uniform
convergence of real-rooted entire determinants followed by Hurwitz, or
norm-resolvent convergence with compact-resolvent eigenvalue control.  It is
that strengthened convergence, not formal self-adjointness of each
approximant, which carries the force.

Suzuki's localized screw-function operators are likewise self-adjoint at
finite support.  The operator whose spectrum is the complete zero set is a
limiting conjecture; the exact Hilbert space in which the zeros are a
self-adjoint spectrum is constructed under RH.

Clark perturbations do not supply an exception.  Their unitary spectral
measures live on the boundary once the underlying characteristic function
is inner.  A compressed shift encoding interior zeros is generally
completely nonunitary, not normal.  In the zeta setting, passage to a
positive de Branges or Clark model requires the Hermite--Biehler/inner
condition, which is itself a zero-free statement.  The cost has moved to
innerness, not disappeared.

These works supply important finite arithmetic operators, but they do not
supply an unconditional exact normal `D` with

```text
det_reg(z-D)=Xi(z)                                (11.1)
```

and a source-computable adjoint Hessian (9.3).  Rebuilding their finite
operators without addressing their convergence would repeat an existing
front.

## 12. Audit of the M2/X3 closure in paper 36

Paper 36 proposes a positivity-bearing realization with the following two
relevant clauses:

```text
X3: every primitive class alpha with <alpha,alpha>>0 admits an effective
    representative, and effective classes pair nonnegatively with theta;

X4: J_N is a compression of the H1 pairing.        (12.1)
```

The conditional proof then supposes

```text
c^*J_Nc<0                                         (12.2)
```

and lifts `c` to a primitive class `alpha` with

```text
<alpha,alpha><0.                                  (12.3)
```

It invokes X3 to claim a Castelnuovo inequality for this `alpha`.

### Proposition 12.1 - The invoked effectivity inference does not follow

The X3 effectivity clause, together with the X4 compression clause, does not
imply `J_N>=0`.  Consequently, the displayed proof of the X1--X4 conditional
closure has a missing premise.

### Proof

X3 has the antecedent `<D,D>>0`; it says nothing about the class in (12.3).
This quantifier mismatch already prevents the asserted inference.

For a concrete model, take

```text
H=H0 direct-sum H2 direct-sum V,
V=R^2,
q(x_1,x_2)=x_1^2-x_2^2.                          (12.4)
```

Let `theta` lie in `H0`, orthogonal to `V`, and declare every element of `V`
effective.  Then every positive-square primitive class has an effective
representative and every effective class pairs with `theta` as zero.  Thus
X3 is satisfied.  Let X4 be the identity compression on `V`; then

```text
J=diag(1,-1),                                     (12.5)
```

which is not positive semidefinite. `QED`

This model is not asserted to realize X1 or X2 for the actual `Xi` explicit
formula; it isolates only the invalid X3-to-Castelnuovo inference used in the
displayed proof.  That derivation invokes no stated consequence of X1 or X2,
and no separate deduction of (12.6) from them is supplied.  If an additional
property of the explicit-formula realization is intended to rule out the
countermodel, that property is exactly a new premise and must be stated and
proved.

The inequality used in the paper,

```text
q(alpha)>=-|B(alpha,theta)|^2/q(theta),            (12.6)
```

does not follow merely from effectivity of classes which already have
positive square.  A Castelnuovo derivation needs additional structure:

```text
a divisor group and a defined linear equivalence;
intersection invariance under that equivalence;
Riemann--Roch for the family alpha+r theta;
a moving lemma or nonnegative intersection of effective representatives;
quadratic control of degrees or dimensions.        (12.7)
```

Paper 36 later states that linear equivalence on the arithmetic square is
still undefined.  That missing structure cannot be used inside the earlier
conditional theorem.

Even if (12.6) were assumed, positivity of `q(alpha)` would follow only
after also proving

```text
B(alpha,theta)=0.                                 (12.8)
```

Orthogonality to the two pole classes does not imply (12.8) unless `theta`
is declared to lie in their span or the compression is shorted by `theta`
as well.

### Sign audit

The later Gibbs proposal states on primitive classes

```text
<D,D>_W=-lim c(beta)Var(Dhat)<=0.                 (12.9)
```

X4, however, calls `J_N` a compression of the same pairing, while the target
is `J_N>=0`.  One of the conventions must be changed explicitly, for
example

```text
c^*J_Nc=-<iota_Nc,iota_Nc>_int,                  (12.10)
```

or the sign in (12.9) must be reversed.  Without such a declaration, X4
and the Gibbs proposal point in opposite directions.

If (12.9) and M2 use literally the same pairing, every primitive class has
nonpositive square and the M2 antecedent `<D,D>_W>0` is vacuous.  If `J_N`
is instead the negative of an intersection compression, M2 and X3 must also
be rewritten in that sign convention.

## 13. Type and convexity audit of M2_N

The finite problem in paper 36 asks for

```text
c=e_+-e_-,
e_+,e_- in E_N,
q(e_+)>=q(c)-epsilon_N.                           (13.1)
```

The following spaces are not identified in the statement:

```text
c                    coefficient vector in C^N;
J_N and A            forms or matrices;
S_(log n)            operators;
D                    correspondence class;
S_(log n)v           test vector.                 (13.2)
```

No compression map sends a coefficient vector `c` to a correspondence
class.  In particular, the Weil test associated with `c` is typically the
quadratic object `|R_c|^2`, not `c` itself.

The proposed set

```text
cone{prime shifts} union archimedean cone          (13.3)
```

also need not be a cone.  The closed conic hull of the union, equivalently
the Minkowski sum of the two cones, is required.  For real inequalities the
prime generators must be self-adjoint combinations or a real part must be
specified.

### Proposition 13.1 - The quadratic superlevel is not an SDP constraint

Even when `E_N={Gx:x>=0}` and `J_N>=0`, the condition

```text
(Gx)^*J_N(Gx)>=r                                  (13.4)
```

is generally nonconvex.  Hence (13.1) is not an SDP.

### Proof

Take

```text
E_N=R_+^2,
J_N=I,
c=(1,-1),
epsilon=0.                                        (13.5)
```

The feasible `e_+` satisfy

```text
e_+>=0,
e_+-c>=0,
||e_+||^2>=2.                                     (13.6)
```

Both

```text
x=(sqrt(2),0),
y=(1,1)                                           (13.7)
```

are feasible, but

```text
||(x+y)/2||^2=1+sqrt(2)/2<2.                      (13.8)
```

Thus the feasible set is nonconvex.  Every SDP feasible set and every
linear projection of one is convex. `QED`

Introducing a matrix variable `X=e_+e_+^*` adds a rank-one constraint.
Dropping that constraint is only a relaxation and allows `X` to be inflated
independently of `e_+`.

### Proposition 13.2 - Common-shift degeneracy

Let `K` be a cone, let `q(x)=B(x,x)`, and suppose

```text
c=e_+-e_-,
e_+,e_- in K.                                    (13.9)
```

If `K` contains `h` with `q(h)>0`, then for every sufficiently large `R`
the same difference has a representation with `q(e_+)>=R`.

### Proof

For `t>=0`,

```text
c=(e_++th)-(e_-+th),                              (13.10)
```

and both shifted vectors remain in `K`.  Moreover,

```text
q(e_++th)=q(e_+)+2tB(e_+,h)+t^2q(h) -> infinity. (13.11)
```

`QED`

Thus (13.1) reduces to the span test

```text
c in K-K=span(K)                                  (13.12)
```

whenever the cone contains one positive direction.

### Corollary 13.3 - An abstract finite falsifier of the proposed implication

Take

```text
J=diag(1,-1),
K=R_+^2,
theta=(2,-1).                                     (13.13)
```

Take the polar plane to be zero, or embed this block orthogonally in its
primitive complement.

For every `e in K`,

```text
B_J(e,theta)=2e_1+e_2>=0.                         (13.14)
```

Also `K-K=R^2` and `h=(1,0)` has `q(h)=1`.  Therefore M2_N passes for every
positive-square `c` after a large common shift.  Nevertheless,

```text
q(0,1)=-1,                                        (13.15)
```

so `J` is indefinite.  A complete numerical pass of M2_N would not imply
the desired positivity.  This is an abstract falsifier of the proposed
M2_N-to-positivity inference, not a model of the still-undefined concrete
arithmetic cone.

## 14. A well-typed finite cone problem

The finite shadow can be repaired as a test of effectivity, but not as a
proof of the missing Castelnuovo theorem.

Let

```text
C_N subset Herm(N)                                (14.1)
```

be a declared real space of compressed correspondences, let `T_N` be the
trivial subspace, and define self-adjoint prime generators

```text
G_(n,N)=P_N[S_(log n)+S_(log n)^*]P_N.            (14.2)
```

Given a specified archimedean cone `K_(infinity,N)`, put

```text
K_N=closure cone(
 {Lambda(n)n^(-1/2)G_(n,N)} union K_(infinity,N)). (14.3)
```

For a fixed compressed correspondence `D_N`, effectivity modulo the trivial
plane means

```text
there exist E in K_N and T in T_N such that
D_N=E+T.                                          (14.4)
```

This is linear conic feasibility.  It is an LP when `K_N` is finitely
generated and an SDP only after a spectrahedral representation has been
proved.

An approximate convex version for fixed `D_N` is

```text
there exist E in K_N and T in T_N such that
||D_N-E-T||_(R_N)^2<=epsilon_N,
R_N>=0.                                           (14.5)
```

Ampleness is a declared linear functional

```text
ell_(theta,N)(E)>=0 for E in K_N,                 (14.6)
```

which, when continuous, can be checked on every prime and archimedean
generator.  If the intended ampleness is the operator inequality

```text
Re <Sv,Av>>=0 for every v,                        (14.6a)
```

then the correctly typed finite condition is instead

```text
(S^*A+AS)/2>=0.                                   (14.6b)
```

Equations (14.4)--(14.6) are a template: one must still prove that the
operators (14.2) are the actual compressed images of the effective
generators.  Once that map is supplied, the template removes the type
mismatch, nonconvex superlevel and common-shift degeneracy for each fixed
`D_N`.  The universal assertion

```text
Q(D_N)>0 => [D_N] in projection(K_N)              (14.6c)
```

is a cone-containment problem with a generally nonconvex quadratic
antecedent; it is not one SDP.

They still do not imply `J_N>=0`.  The force-bearing statement must be
declared separately.  With one consistent sign convention, a sufficient
form is

```text
Q(theta)>0,
CI: Q(D)>=-|B(D,theta)|^2/Q(theta) for every D,    (14.7)

c^*J_Nc=Q(iota_Nc),
B(iota_Nc,theta)=0.                               (14.8)
```

Then `J_N>=0` follows immediately.  Deriving (14.7) from effectivity would
require the arithmetic Riemann--Roch, linear-equivalence and intersection
machinery listed in (12.7).  That derivation, not (14.4), is the
RH-strength milestone.

Accordingly:

```text
M2 may be retained as a cone-coverage conjecture;
M2_N must be replaced by (14.4) or (14.5);
the stated M2-to-Castelnuovo argument does not close Omega7 unless CI,
or another explicitly proved premise implying CI, is added;
optimizing the old M2_N experiment is frozen.      (14.9)
```

## 15. Primary-literature boundary

The following primary sources delimit the constructions used here:

```text
M. Suzuki,
Weil's quadratic form via the screw function:
  https://arxiv.org/abs/2606.09096

M. Suzuki,
On the Hilbert space derived from the Weil distribution:
  https://arxiv.org/abs/2301.00421

M. Suzuki,
A canonical system of differential equations arising from the Riemann
zeta-function:
  https://arxiv.org/abs/1204.1827

C. Liaw, S. Treil,
Clark model in general situation:
  https://arxiv.org/abs/1308.3298

D. N. Clark,
One dimensional perturbations of restricted shifts:
  https://doi.org/10.1007/BF02790036

L. de Branges,
Hilbert Spaces of Entire Functions:
  https://search.worldcat.org/title/440600

A. Connes, C. Consani, H. Moscovici,
Zeta Spectral Triples:
  https://arxiv.org/abs/2511.22755

P. Doerfler, G. Schmeisser,
Construction of unitary and normal companion matrices:
  https://doi.org/10.1016/0024-3795(94)90190-2

J. Liesen,
When is the Adjoint of a Matrix a Low Degree Rational Function in the
Matrix?:
  https://doi.org/10.1137/060675538

C.-K. Li, J. C.-H. Lin,
Confluent Vandermonde matrix and related topics:
  https://arxiv.org/abs/2403.01474

M. B. Nathanson,
The Hermite--Sylvester criterion for real-rooted polynomials:
  https://arxiv.org/abs/1911.01745

I. Janovitz-Freireich, B. Mourrain, L. Ronyai, A. Szanto,
On the computation of matrices of traces and radicals of ideals:
  https://arxiv.org/abs/0901.2778

T. Britz, A. Carey, F. Gesztesy, R. Nichols, F. Sukochev, D. Zanin,
The product formula for regularized Fredholm determinants:
  https://arxiv.org/abs/2007.12834

L. Hartmann, M. Lesch,
Zeta and Fredholm determinants of self-adjoint operators:
  https://arxiv.org/abs/2106.02444

P. Lelong,
Integration sur un ensemble analytique complexe:
  https://doi.org/10.24033/bsmf.1488               (15.1)
```

Equation (3.2) is the exact formula labelled `(3.1)` in Suzuki's
screw-function paper.  The companion/Vandermonde literature makes explicit
that diagonalization and interpolation are the same finite data.  The
Hermite--Sylvester literature gives the classical signature route to real
roots.  Liesen is the closest direct antecedent for an adjoint represented
as a function of a normal matrix.  Doerfler--Schmeisser concerns structured
normal/unitary companion construction and its general obstruction; it is
not the source of the positive-metric classification in Theorem 10.1.
The regularized-determinant sources record the `det_2` product anomaly and
the relation to zeta determinants.  Poincare--Lelong, quotient trace
matrices, companion normality, Clark models and de Branges positivity are
therefore antecedents, not new mechanisms.

No inspected source provides the combined statement

```text
an exact Gamma--Euler construction, independent of the zero divisor, of a
normal star representation whose contracted connected mixed determinant
trace is (9.11), whose source contraction is the rank-one null channel, and whose
cofinal regularization preserves every correction term.                  (15.2)
```

The absence of such a source in this audit is not evidence that (15.2) is
true.  It only leaves (15.2) outside the no-go classes proved here.

## 16. Revised work order

The anti-circularity gate now has the following order.

```text
closed:
  scalar mixed Euler deformation;
  Schwarz/functional-equation conjugate transport;
  sharp Weil pairing relabelled as pointwise Gram;
  nonholomorphic contour insertion without its area term;
  double-residue diagonal selection;
  companion normality with a root-built metric;
  old M2_N feasibility experiment;

retained only as infrastructure:
  abstract Poincare--Lelong multiplication model;
  Hermite quotient involution;
  finite self-adjoint Weil and spectral-triple approximants;
  corrected finite cone membership (14.4);

single operator-valued front:
  NORMAL-ADJOINT-GAMMA-EULER-LIFT;

separate geometric front, only after reformulation:
  derive CI from a genuinely defined arithmetic square and
  Riemann--Roch/effectivity theorem.                (16.1)
```

Before any construction for the operator-valued front is developed, it must
answer four questions at finite level:

```text
NA-1  What is the source-defined algebra and positive star operation?

NA-2  Why is the adjoint spectral fibre q(p) -> conj(q(p)) obtained without
      a root idempotent, Hermite interpolant or Poincare--Lelong measure?

NA-3  What exact Gamma--Euler formula computes the connected trace (9.3),
      including archimedean, polar and cutoff terms?

NA-4  What algebraic identity makes the b-contracted source trace vanish,
      while its spectral side is sum m_p G_PAR(p)?  (16.2)
```

Failure at `NA-2` means divisor insertion.  Failure at `NA-3` means an
abstract spectral model without arithmetic content.  Failure at `NA-4`
means a positive detector with no route to excluding off-line zeros.

## 17. Status

```text
proved here:
  sharp-versus-pointwise distinction for the exact Weil form;
  exact scalar mixed-zero principal part, including multiplicity;
  multiplicity-preserving transport with p_(uv)=0;
  scalar conjugate-velocity no-go for all standard Xi symmetries;
  Cauchy--Pompeiu divisor-current identity;
  all-pairs and multiplicity wall for double residues;
  totally-real obstruction to a meromorphic conjugate graph;
  polynomial discriminant analytic-family falsifier;
  finite Hermite quotient realization of the graph;
  exact normal-adjoint connected determinant Hessian;
  equivalence between companion normalizing metric and conjugate
  interpolation;
  logical countermodel to the X3--X4 inference used in the conditional
  closure;
  nonconvexity and common-shift degeneracy of M2_N;
  corrected finite cone-membership formulation;

frozen:
  scalar Gamma--Euler twists for the parity Gram;
  use of the unconditional sharp Weil form as the missing Gram;
  zero-built normal models as source-first progress;
  the old M2_N numerical protocol;

open:
  NORMAL-ADJOINT-GAMMA-EULER-LIFT, NA-1--NA-4;
  a global regularization compatible with its mixed derivatives;
  a correctly signed and typed arithmetic Castelnuovo theorem;
  DIRECTIONAL-IDENT and Omega7.                    (17.1)
```
