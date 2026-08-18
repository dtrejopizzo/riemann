# E101.081 - Finite border graph no-go

## 1. Decision

The exact translation border retained in E101.080 cannot create the missing
same-p conjugate tensor through a universal finite identity which is
covariant under freely displaced and independently weighted controlled
insertions.

There are two independent reasons.

```text
one-atom obstruction:
  every linear extraction from a fixed finite source, its complex
  translations and its exact borders is holomorphic, antiholomorphic, or
  harmonic in p; the graph leg conj(R_p)R_p^T is genuinely mixed in p and
  conj(p).  A product can form that leg only after the atom has already been
  matched;

aggregate obstruction:
  multiplying or conjugating aggregated channels can create mixed dependence,
  but it also creates independent pole tuples.  Exact cancellation of every
  mixed tuple for arbitrary controlled insertions makes the resulting
  polynomial atomwise additive.  Additivity forces linearity, whereas the
  required exterior detector is homogeneous of degree six.                (1.1)
```

Thus the universal controlled-position/strength version of finite
`GRAPH-BORDER-CANCELLATION` is closed negatively.
This is not a new general identity theorem: it is the exact application of
the holomorphic and additive no-go mechanisms of E101.076 and E101.078 to the
border formula which remained open in E101.080.

The conclusion does not eliminate either of the following:

```text
an unbounded, nonnormal cofinal limit in which local holomorphic normality is
lost before an exact diagonal distribution emerges;

an Xi-specific higher-level Gamma--Euler identity which supplies the
same-atom tensor before the CCM matrices are aggregated.                  (1.2)
```

The first escape must expose its norm growth and all limit interchanges.  The
second is the remaining algebraic form of `GRAPH-GAMMA-EULER`; it may be
finite only if a specific Xi identity deliberately fails the generic
controlled-insertion test.

## 2. Finite Cauchy and reflection calculus

Fix a real Fourier lattice

```text
d_n=hn, |n|<=N,
Lambda_N={d_n:|n|<=N},                              (2.1)
```

and put

```text
R_N(p)=(1/(d_n-p))_(|n|<=N).                       (2.2)
```

Let `U` be a connected conjugation-invariant open subset of
`C minus Lambda_N`.  For a fixed vector `u in C^(2N+1)`, define

```text
L_u(p)=R_N(p)^T u
      =sum_(|n|<=N)u_n/(d_n-p).                    (2.3)
```

Then `L_u` is holomorphic on `U`.  For any function on a
conjugation-invariant domain, write

```text
f^sharp(p)=conj(f(conj p)).                         (2.4)
```

If `f` is holomorphic, so is `f^sharp`.  Since the lattice is real,

```text
u^*R_N(p)
=sum_n conj(u_n)/(d_n-p)
=L_u^sharp(p),                                     (2.5)
```

whereas

```text
u^*conj(R_N(p))
=sum_n conj(u_n)/(d_n-conj p)
=conj(L_u(p)).                                     (2.6)
```

Equation (2.5), not (2.6), is produced when a fixed Hermitian row is paired
with the complex-symmetric atom `R_N(p)R_N(p)^T`.

### Lemma 2.1 - Fixed Hermitian rows do not conjugate the pole

For fixed vectors `u,v` and a holomorphic scalar weight `K(p)`,

```text
u^*[K(p)R_N(p)R_N(p)^T]v
=K(p)L_u^sharp(p)L_v(p)                            (2.7)
```

is holomorphic on `U`.

### Proof

Equation (2.7) follows from (2.3) and (2.5).  Every factor on its right side
is holomorphic. `QED`

The distinction is not a convention about transposes.  Replacing the atom by

```text
K(p)conj(R_N(p))R_N(p)^T                           (2.8)
```

would produce (2.6), but (2.8) is exactly the graph atom which has not been
constructed.

## 3. The exact border is entire in the pole

Let `c=(c_n)` be a fixed finite source and

```text
U_(a,N)=diag(exp(-iad_n)),

C_(a,N)(p)=R_N(p)^TU_(a,N)c.                       (3.1)
```

E101.080 gives the exact off-grid defect

```text
B_(a,N)(p)
=C_(a,N)(p)-exp(-iap)C_(0,N)(p)

=sum_(|n|<=N)c_n
 [exp(-iad_n)-exp(-iap)]/(d_n-p).                  (3.2)
```

The divided difference has the integral representation

```text
[exp(-iad)-exp(-iap)]/(d-p)
=-ia integral_0^1
 exp(-ia[(1-theta)p+theta d])dtheta.               (3.2a)
```

### Proposition 3.1 - Removable-border theorem

For every fixed `a,N,c`, the function `B_(a,N)` is entire in `p`.

### Proof

Each summand in (3.2) is entire away from `p=d_n`.  At that point its numerator
vanishes and

```text
lim_(p->d_n)
 [exp(-iad_n)-exp(-iap)]/(d_n-p)
=-ia exp(-iad_n).                                  (3.3)
```

Thus every apparent pole is removable.  The sum is finite. `QED`

In particular,

```text
B_(a,N)^sharp(p;c)
=conj(B_(a,N)(conj p;c))
=B_(-conj a,N)(p;conj c),                          (3.4)

conj(B_(-a,N)(conj p;c))
=B_(conj a,N)(p;conj c).                           (3.4a)
```

is also entire.  Substituting

```text
C_(a,N)(p)=exp(-iap)C_(0,N)(p)+B_(a,N)(p)          (3.5)
```

in (2.7) produces only products of holomorphic functions of `p`.  The border
can retain both translation parameters in its coefficients, but parameter
retention is not pole conjugation.

### Corollary 3.2 - Exact finite borders remain on the holomorphic side

Any finite sum, product, tensor product or fixed contraction formed from

```text
R_N(p),
C_(a,N)(p),
B_(a,N)(p),
their sharp reflections,
holomorphic CCM weights K(p),
and p-independent finite matrices                            (3.6)
```

is holomorphic in the individual pole variable before an external complex
conjugation is applied.

An external conjugation replaces a holomorphic output by an antiholomorphic
one.  It still does not multiply both dependences inside one atom.

## 4. The graph leg is not a holomorphic or real-linear border response

The entries of the desired graph leg are

```text
Q_(m,n)(p)
=conj(R_N(p)_m)R_N(p)_n
=1/[(d_m-conj p)(d_n-p)].                          (4.1)
```

Using Wirtinger derivatives,

```text
partial_(conj p) Q_(m,n)(p)
=1/[(d_m-conj p)^2(d_n-p)],                        (4.2)

partial_p partial_(conj p) Q_(m,n)(p)
=1/[(d_m-conj p)^2(d_n-p)^2].                     (4.3)
```

Both are nonzero on `U`.

### Theorem 4.1 - Holomorphic and harmonic graph impossibility

No holomorphic matrix function on a nonempty open subset of `U` equals

```text
conj(R_N(p))R_N(p)^T.                              (4.4)
```

More generally, (4.4) does not belong entrywise to the real-linear space

```text
O(U)+conj(O(U)),                                   (4.5)
```

where `O(U)` denotes the holomorphic functions on `U`.

### Proof

The first assertion follows from (4.2).  Every function in (4.5) is harmonic
and hence has zero mixed Wirtinger derivative.  Equation (4.3) excludes the
second assertion. `QED`

This theorem does not exclude a finite product after one atom has already
been labelled.  Indeed, `conj(R_m(p))R_n(p)` and
`conj(B_(a,N)(p))B_(a,N)(p)` are finite mixed products.  Their first factors
require atomwise conjugation before aggregation.  The theorem excludes their
linear extraction from the available holomorphic aggregate; the obstruction
is the same-atom matching, not the algebraic existence of the product.

The scalar atomwise character has the same obstruction.  If `A` and `C` are
nonconstant holomorphic Cauchy coordinates, then

```text
G(p)=conj(A(p))C(p),

partial_p partial_(conj p)G(p)
=conj(A'(p))C'(p).                                 (4.6)
```

The last expression is not identically zero.  For the ideal translated
coordinates of E101.080, (4.6) is the local analytic content of

```text
conj(C_(-a)(p))C_a(p)
=exp(-i[t Re p+s Im p])|C_0(p)|^2.                (4.7)
```

Thus the desired two-dimensional character cannot be one of the finite
holomorphic border terms omitted from the bulk calculation.

## 5. Why quartet symmetry does not repair the one-atom obstruction

For an off-line control `zeta`, the quartet is

```text
P_zeta={zeta,-zeta,conj zeta,-conj zeta}.          (5.1)
```

Summing a holomorphic atom response over (5.1) produces a real-analytic
function of `zeta`.  It can contain both a holomorphic term and its complex
conjugate.  It does not create their same-atom product.

For example, if `H` is holomorphic and respects the parity of the quartet,
then its real orbit sum has the form

```text
H(zeta)+epsilon H(-zeta)
+conj(H(zeta)+epsilon H(-zeta)).                  (5.2)
```

This belongs to the harmonic space (4.5).  The graph entry (4.1) does not.

One can multiply the two terms in (5.2), but that operation is nonlinear in
the full spectral aggregate.  For several orbits it produces every pair of
orbit labels.  The next section shows that no finite polynomial cancellation
which is valid for every controlled position and strength can keep only the
equal labels.

## 6. Polynomial additivity for a bundle of border channels

Fix finitely many translations, jets, faces and finite sections.  Bundle all
resulting linear CCM and border outputs into one finite-dimensional real
space `V`.  A controlled orbit `O` of strength `chi` contributes

```text
chi v_O in V.                                      (6.1)
```

For a finite family of independent controlled orbits, the available bundle
is

```text
v_total=sum_O chi_O v_O.                           (6.2)
```

Every finite multilinear or polynomial postprocessing of these aggregated
channels is a polynomial map

```text
Phi:V->W.                                          (6.3)
```

The conclusion remains the same if several copies of the bundle are used:
take their direct sum as `V`.

Let the controlled positions range over an open real parameter domain `S`.
The map

```text
S -> V,  O -> v_O                                    (6.3a)
```

is continuous for the finite Cauchy, translation and border channels away
from their fixed lattice poles.  Assume that its image spans `V`, after
replacing `V` by that span.  Removing finitely many points of `S` does not
change the span: every removed point is a limit of unremoved points, and a
linear subspace of the finite-dimensional space `V` is closed.  It follows
that the controlled image contains two disjoint finite families, each of
which is a basis of `V`.

### Theorem 6.1 - Exact mixed-term cancellation forces linearity

Assume the continuous controlled-position hypotheses above, and let the
strengths vary in nonempty real intervals.  Suppose a polynomial `Phi`
satisfies

```text
Phi(sum_O chi_Ov_O)=Phi(0)+sum_O T_O(chi_O)         (6.4)
```

for all finite families of distinct controlled orbits, with
`T_O(0)=0` and no mixed-orbit term.  Then `Phi` is affine on `V`.  If
`Phi(0)=0`, it is linear.

### Proof

Choose two disjoint controlled families

```text
(v_1,...,v_d), (w_1,...,w_d),                      (6.4a)
```

each a basis of `V`; their existence was proved above.  Independently
variable strengths parametrize open boxes `U_v,U_w` in `V`.  Applying (6.4)
to the first family, the second family and their disjoint union gives

```text
Phi(X+Y)-Phi(0)
 =[Phi(X)-Phi(0)]+[Phi(Y)-Phi(0)]                  (6.5)
```

for `(X,Y)` in the nonempty open set `U_v x U_w`.  Because both sides are
polynomial in `(X,Y)`, (6.5) extends to all `V x V`.  The
additive-polynomial theorem of E101.078 makes `Phi-Phi(0)` linear. `QED`

The exterior-cube detector of one orbit scales differently.  Since

```text
X_O(chi)=chi X_O(1),

P_3(X_O(chi))=chi^6P_3(X_O(1)),                   (6.6)
```

a linear `Phi` cannot equal the right side of (6.6) on an interval of
strengths when the orbit is off-line and `P_3(X_O(1))>0`.

### Corollary 6.2 - Finite aggregate trilemma

A finite polynomial of aggregated border channels must satisfy at least one
of:

```text
retain mixed-orbit terms;
be linear and fail the degree-six rank discriminator;
receive an atomwise nonlinear feature before aggregation.            (6.7)
```

The third alternative is precisely the missing diagonal lift, not a result
of finite border algebra.

## 7. Six-linear border contractions

Consider any proposed finite version of the E101.079 projector built by
inserting the exact decomposition (3.5) in six translated aggregate channels
and then applying the polarization `p_3`.  Before an infinite mean is taken,
its expansion has the form

```text
sum_(p_1,...,p_6)
 H_(N,A)(p_1,...,p_6)
 p_3(Y_(p_1),...,Y_(p_6)),                         (7.1)
```

where `A` denotes the finite translation parameters and
`H_(N,A)` is built from the functions in (3.6).

At finite `N,A`, equation (7.1) is a polynomial of the aggregated channel
bundle.  If all terms with unequal orbit labels cancelled identically for
every controlled finite spectrum, Theorem 6.1 would make the result linear.
It could not retain the nonzero degree-six diagonal in (6.6).

### Theorem 7.1 - Universal finite border cancellation no-go

Under the continuous controlled-position and independent-strength hypotheses
of Section 6, there is no finite Fourier section, finite collection of
complex translations, or finite polynomial/six-linear contraction of the
exact borders which simultaneously

```text
is derived from the aggregated CCM response;
cancels every mixed controlled orbit exactly;
retains sum_O P_3(X_O) for every off-line controlled orbit.           (7.2)
```

### Proof

If the proposed contraction is a real-linear extraction from the aggregate
and its conjugate, Theorem 4.1 excludes the same-p graph and (6.6) excludes
the exterior detector.  If it is polynomial and nonlinear, exact removal of
the mixed labels throughout the controlled family invokes Theorem 6.1 and
again makes it affine, with linear centered part. `QED`

A finite phase-box integral does not change the conclusion.  Integration over
a finite box changes the coefficients of the polynomial (7.1), but it remains
a finite continuous polynomial of the same aggregate channels.  An infinite
invariant mean is different: it can produce a distributional diagonal, but
only after a bounded or otherwise mean-admissible character signal has been
constructed.  E101.080 proves that the available border family does not yet
supply such a signal.

### Theorem 7.2 - No universal finite analytic diagonal selector

Let `D` be a connected pole domain and let

```text
K_N:D^6->C                                           (7.3)
```

be holomorphic, or real-analytic after quartet symmetrization.  If, as an
identity on the continuous controlled domain,

```text
K_N(p_1,...,p_6)=0
whenever the six labels are not all equal,            (7.4)
```

then `K_N` vanishes identically, including on the diagonal.

### Proof

The complement of the full diagonal in `D^6` contains a nonempty open set.
Equation (7.4) makes the function vanish on that open set.  Holomorphic
uniqueness applies in the first case and real-analytic uniqueness in the
second, so it vanishes on the connected domain. `QED`

For known finite nodes `P={p_1,...,p_J}`, Lagrange polynomials do give

```text
K_P(z_1,...,z_6)
=sum_(j=1)^J product_(ell=1)^6 L_j(z_ell),          (7.5)
```

which is one exactly on equal node labels and zero on unequal labels when
restricted to `P^6`.  Formula (7.5) uses every node position in advance.  It
is the forbidden divisor-adapted diagonal lift, and shows precisely which
information evades Theorem 7.2.  The theorem does not exclude an identity
only on tuples of actual Xi zeros, an approximate or distributional selector,
or an arithmetic identity specific to Xi.

### Theorem 7.3 - Finite transverse boundedness forces blindness

Let

```text
a=(t-is)/2,
u_a=exp(-iaD_N)c,                                  (7.6)
```

and let `A` be any fixed finite matrix, independent of `s`.  Then

```text
u_(-a)^*Au_a
=sum_(n,m)conj(c_n)A_(n,m)c_m
 exp(-it[d_n+d_m]/2)exp(s[d_n-d_m]/2).             (7.7)
```

Every finite product and contraction of such translated channels is an
exponential polynomial in `s` with real exponents.  If it is bounded for all
real `s`, or if

```text
sup_(T>1)(2T)^(-1)integral_(-T)^T|E(s)|ds<infinity, (7.8)
```

then every nonzero transverse exponent cancels and `E` is independent of
`s`.

### Proof

Equation (7.7) follows by direct substitution.  Combine equal exponents in a
finite exponential polynomial and choose its largest exponent.  If it is
positive, the corresponding term forces exponential growth as `s->infinity`;
if the smallest exponent is negative, it forces exponential growth as
`s->-infinity`.  Either growth also violates (7.8).  Iteration leaves only
exponent zero. `QED`

For `Im p!=0`, neither

```text
exp(-i[t Re p+s Im p])
```

nor its quartet sum is identically independent of `s` as a function of
`(t,s)`.  Exceptional values of `t` may cancel a quartet coefficient, but do
not give an identity.  Thus a finite mean-admissible translation contraction
cannot produce the bounded transverse character.  A fixed, `s`-independent
heat multiplier alters the coefficients in (7.7), not its real exponents.

The conclusion does not cover an `s`-dependent normalization, a quotient or
other nonpolynomial processing, a regularization parameter coupled to `s`,
or an ordered singular limit.  Each is a possible escape only after its
growth and limit interchange have been proved.

A signed centered mean without (7.8) is not an escape: an odd exponential
combination may have a formal centered cancellation while its absolute mean
diverges.  Such a cancellation does not satisfy `BOC-3`.

## 8. Scope of the controlled-insertion conclusion

Theorems 4.1 and 7.1 use an open family of planted pole positions and
independently variable strengths.  This is the correct test for a purported
universal finite identity in the Cauchy, translation and border kernels.  Such
an identity cannot know that a point is a zero of `Xi`, so it must persist
under an admissible displacement of the controlled quartet.

The argument does not exclude an identity valid only on the actual Xi divisor
because of a special Gamma--Euler relation.  Such an identity would fail the
generic controlled-position test for a declared arithmetic reason.  It must
therefore exhibit that reason explicitly; merely evaluating a universal
formula at Xi zeros is node selection.

This is the analytic specialization of the node-blind warning in E72.355.
The advance here is that the exact border formula (3.2) has now been placed
inside the class rejected by the warning.

## 9. Cofinal escape and its mandatory singularity

Suppose a sequence of finite holomorphic border responses converges locally
uniformly on a fixed pole domain.  Its limit is holomorphic.  If holomorphic
and antiholomorphic pieces are combined real-linearly with locally uniform
bounds, the limit remains harmonic.  The graph entries violate both
conclusions by (4.2)--(4.3).

Therefore any cofinal border construction which remains universal under the
controlled family must lose at least one of:

```text
local boundedness in the pole variable;
locally uniform convergence;
finite polynomial dependence on the aggregate;
independence from the Xi divisor.                                  (9.1)
```

This identifies the force-bearing estimate rather than merely saying that a
limit is difficult.  A legitimate singular construction must provide

```text
the exact order of N, translation-box and heat limits;
a signed cancellation of the growing holomorphic pieces before the limit;
uniform control of every mixed-orbit term after that cancellation;
eventual inclusion and detection of each off-line orbit;
identification of the remaining diagonal with the arithmetic value zero.
                                                                    (9.2)
```

The last clause is RH-strength by E101.079(4.8).

## 10. Nonduplication gate

The components of the proof have classical antecedents and are not presented
as new general principles.

```text
holomorphic reflection and the identity theorem:
  standard one-variable complex analysis;

covariance versus pseudocovariance:
  the classical distinction behind complex Hermitian lifting;

polynomial additivity:
  the Cauchy functional equation in finite dimension;

phase and ambiguity lifts:
  established mechanisms which begin with same-sample conjugate data;

one-level Weil and CCM formulas:
  linear spectral aggregates, not exact nonlinear spectral diagonals. (10.1)
```

The primary references and exact import boundary are recorded in
E101.076--E101.080.  The closest additional antecedents are:

```text
Moran Ledezma:
  https://arxiv.org/abs/2311.08519

Burnol:
  https://arxiv.org/abs/math/9809119

Booker:
  https://arxiv.org/abs/1308.3067

Groskin, finite Guinand--Weil dictionary:
  https://arxiv.org/abs/2607.02828

Groskin, moving von Mangoldt event measure:
  https://doi.org/10.5281/zenodo.21242028

Conrey--Snaith:
  https://arxiv.org/abs/0803.2795

Lagarias--Rodgers:
  https://arxiv.org/abs/1905.12123                 (10.2)
```

Moran Ledezma already uses Bohr characters for prime-frequency covariance
and multiplicative matching; that mechanism must not be presented as new.
An ordinary sixth Bohr moment retains all balanced multiplicative relations,
not only six equal prime-power events, and in either case it does not
transport matching to same-zero conjugate columns.  Burnol already
explains why postulating a positive covariance for the Weil distribution
contains the positivity criterion rather than proving it.  Booker formulates
the explicit formula linearly at distribution level; tensor products contain
all tuples, while diagonal restriction is an additional singular operation.

The finite Guinand--Weil dictionary factors a fixed Galerkin source through a
finite-dimensional quotient and explicitly does not recover individual
events.  Varying the prime cutoff produces exact rank-one von Mangoldt events,
but those labels are prime powers, not spectral zero labels.  This supplies a
new source-first coordinate worth testing; it does not yet supply the graph.

The inspected selfadjoint CCM and screw-function constructions remain
one-level.  In the inspected Conrey--Snaith and Lagarias--Rodgers frameworks,
higher-correlation formulas are asymptotic, conditional or support-restricted
and do not exclude an exceptional off-line orbit.  None of the inspected
works constructs the matched spectral graph from a pre-aggregation
arithmetic current.

No novelty is claimed for (2.4), (4.3), or Theorem 6.1.  The potentially new
result is the source-specific controlled-family closure: the complete exact
border (3.2), which had remained a live possibility, cannot supply the CCM
graph through a universal finite polynomial identity.  A finite identity
specific to the Xi divisor remains outside this conclusion.

## 11. Revised live targets

The target

```text
UNIVERSAL-GRAPH-BORDER-CANCELLATION at finite level (11.1)
```

is closed negatively by Theorem 7.1.

The surviving alternatives are:

```text
GRAPH-GAMMA-EULER:
  construct a genuinely higher-level atomwise current from the signed
  Gamma--Euler source before the one-level CCM sum is formed;

PRIME-EVENT-TO-SPECTRAL-GRAPH:
  use the moving-cutoff rank-one von Mangoldt events as independently labelled
  source data and prove, rather than assume, their transport to a same-zero
  conjugate tensor;

SINGULAR-DIAGONAL-PULLBACK:
  derive an arithmetic approximate diagonal whose norm growth and mixed
  terms cancel in a proved ordered limit, without zero interpolation;

WEIGHTED-JET-POTENTIAL-CONVERGENCE:
  prove the scalar potential transfer of E101.079 directly, accepting it as
  the force-RH theorem.                                              (11.2)
```

E101.084 closes `TERMINAL-RANKONE-COMPOUND` as an independent route: the
complete compound vector is affine in the sampled boundary values and its
cofinal inverse is an IDENT inf-sup problem; its scalar norm is not an
all-real discriminator.

The first two are not allowed to cite the formal graph tensor on their
hypothesis side.  They must output its contracted value from prime,
archimedean and boundary data.

## 12. Stop rule

The following operations are now frozen:

```text
searching individual terms of the finite translation border for conj(p);
adding more fixed complex translations to the same finite CCM atom;
external conjugation of an aggregate followed by an unprojected product;
finite phase quadrature claimed to be an exact spectral diagonal;
finite polynomial cancellation of all mixed orbit labels uniformly on the
controlled-position and independent-strength family;
heat regularization presented as changing the analytic type of one atom.
                                                                    (12.1)
```

Further border work is justified only if it explicitly violates one finite
hypothesis of Theorem 7.1 and proves the corresponding control in (9.2).

## 13. Status

```text
proved:
  holomorphic fixed-row calculus for the complex-symmetric CCM atom;
  entire removability of the exact finite translation border;
  nonholomorphic and nonharmonic character of the same-p graph leg;
  additive-polynomial obstruction for every controlled finite
  border-channel bundle satisfying the double-basis hypothesis;
  universal finite six-linear border cancellation no-go;

closed negatively:
  universal finite GRAPH-BORDER-CANCELLATION under controlled positions and
  strengths;
  TERMINAL-RANKONE-COMPOUND as an independent bypass, by E101.084;

not excluded:
  finite Xi-specific Gamma--Euler cancellation;
  singular cofinal diagonal pullback;
  pre-aggregation higher-level Gamma--Euler current;
  Xi-specific weighted potential transfer;

still open:
  BOUNDED-ORBIT-CHARACTER-LIFT, DIRECTIONAL-IDENT and Omega7.
```
