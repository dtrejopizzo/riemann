# E101.082 - One-trace diagonal and the mixed-bidegree wall

## 1. Decision

The statement that Gamma--Euler supplies only a spectral aggregate needs one
important correction.  A single Weil explicit formula applied to a
convolution of six predetermined sources gives an exact same-zero product:

```text
W(h_1*...*h_6)
=sum_rho m_rho product_(j=1)^6 H_j(rho),           (1.1)

H_j=Fourier(h_j).                                  (1.2)
```

No phase recurrence and no second spectral sum are required.  This is an
exact pre-aggregation diagonal, and it is classical Fourier algebra.

It does not close the CCM detector.  The reason is now exact.  Let `A(z)`
denote the finite jet-compressed half-orbit defined in Section 4:

```text
Y_(N,R)(z)=J_(N,R)^T[K(z)R_zR_z^T]J_(N,R),
A_(N,R)(z)=Y_(N,R)(z)+Y_(N,R)(-z).                (1.3)
```

We abbreviate `A_(N,R)` to `A` when the finite section is fixed.  This matrix
is entire and has rank at most two for every complex `z`.
The full quartet matrix is

```text
X(z)=A(z)+A(conj z)=A(z)+conj(A(z)).               (1.4)
```

If `p_3` is the six-linear polarization of the exterior-cube polynomial,
then

```text
P_3(X(z))
=sum_(k=0)^6 binom(6,k)
 p_3(A(z)^[k],conj(A(z))^[6-k]).                   (1.5)
```

The bidegrees `k=0,1,5,6` vanish identically because both half-orbits have
rank at most two.  Every possible off-line signal lies in the three mixed
bidegrees

```text
k=2,3,4.                                           (1.6)
```

A single explicit formula evaluates holomorphic products at one zero.  Its
source involution produces Schwarz reflection

```text
H^sharp(z)=conj(H(conj z)),                        (1.7)
```

which is still holomorphic.  It does not produce the atomwise conjugate
`conj(H(z))`.  Consequently, (1.1) reaches precisely the pure holomorphic
diagonal which is already zero, while (1.6) requires the missing conjugate
graph.

This closes a conceptual ambiguity:

```text
same-zero holomorphic multiplication:
  available from one explicit formula;

same-orbit Hermitian multiplication:
  open and force-bearing.                           (1.8)
```

E101.085 subsequently sharpens the rank argument and factors the complete
mixed sum by exact jet parity.
It proves that a parity-resolved bidegree `(1,1)` Gram energy already detects
every resolved off-line quartet.  Thus the localization (1.5)--(1.6) remains
correct, but transporting all six legs is stronger than necessary.

## 2. Exact convolution diagonal

Use the additive Fourier convention

```text
H(z)=F[h](z)=integral_R h(t)exp(-izt)dt.           (2.1)
```

Let `W` denote the centered Weil distribution in the real-zero coordinate,
normalized on an admissible test by

```text
W(h)=sum_(Xi(rho)=0)m_rho H(rho).                  (2.2)
```

The other side of (2.2) is the complete prime, prime-power, polar and
archimedean functional supplied by the explicit formula.

### Theorem 2.1 - One-trace same-zero product

Let `h_1,...,h_m` be compactly supported smooth sources.  Then

```text
W(h_1*...*h_m)
=sum_rho m_rho product_(j=1)^m H_j(rho).           (2.3)
```

The spectral sum is absolutely convergent.

### Proof

The convolution theorem gives

```text
F[h_1*...*h_m](z)=product_j H_j(z).                (2.4)
```

Every `H_j` is entire of exponential type and rapidly decreasing on the real
direction uniformly in the zero strip.  The zero count is `O(T log T)`, so
the right side of (2.3) converges absolutely.  Apply (2.2) to the convolution
and use (2.4). `QED`

The same identity extends, by the standard Weil-test approximation, to a
compactly supported source whose transform is entire of finite exponential
type and is `O((1+|x|)^(-2-epsilon))` uniformly in the zero strip.  In this
extension the polar and archimedean evaluations are retained, the prime sum
is finite because the source is compactly supported, and the zero sum is
absolutely convergent.  This is the precise extension used for the CCM
products below; it is not a deletion of boundary terms.

Three bookkeeping points are mandatory.

```text
multiplicity:
  (2.3) weights a zero of multiplicity m_rho linearly by m_rho.  It does not
  evaluate Q(m_rho B(rho)) when Q has degree greater than one;

support:
  the convolution support is the Minkowski sum of the source supports.  Its
  prime cutoff is therefore the enlarged Euler unit attached to that total
  support, not the cutoff of one original CCM source;

cofinality:
  (2.3) is a fixed-test identity.  Limits in Fourier section, jet depth or
  support require new uniform domination.                            (2.4a)
```

The linear multiplicity convention is sufficient for a positive zero-
location detector, but it is not automatically identical to the convention
of E101.079 in which multiplicity was absorbed into a matrix atom before the
degree-six polynomial was applied.  Any bridge between the two conventions
must be stated explicitly.

### Corollary 2.2 - Polynomial atom features

Let `B(z)` be a finite matrix whose entries are Fourier transforms of
admissible fixed sources.  Every homogeneous coordinate polynomial `Q` of
degree `m` admits a finite source-first formula

```text
sum_rho m_rho Q(B(rho))
=finite linear combination of W(h_(j,1)*...*h_(j,m)).       (2.5)
```

### Proof

Expand `Q` into coordinate monomials and apply Theorem 2.1 to each monomial.
`QED`

Equation (2.5) is not a tensor power of an already summed spectral matrix.
The multiplication occurs in the test algebra before the one spectral trace
is taken.  It therefore retains one common spectral argument automatically.

## 3. Bilinear square versus Hermitian modulus

For an admissible source define

```text
h^star(t)=conj(h(-t)).                              (3.1)
```

Its transform is

```text
F[h^star](z)=H^sharp(z)=conj(H(conj z)).           (3.2)
```

Thus the source algebra can form the holomorphic bilinear square

```text
H(z)H^sharp(z).                                    (3.3)
```

For a real source,

```text
H^sharp(z)=H(-z).                                  (3.4)
```

If the source is also even, `H^sharp=H`.

The Hermitian modulus required by the graph is instead

```text
|H(z)|^2=H(z)conj(H(z))
        =H(z)H^sharp(conj z).                      (3.5)
```

Equations (3.3) and (3.5) agree on the real axis after the appropriate real
symmetry.  Off the real axis they are different extensions.  The first is
holomorphic; the second satisfies

```text
partial_z partial_(conj z)|H(z)|^2=|H'(z)|^2       (3.6)
```

and is nonharmonic unless `H` is constant.

This is the same distinction as

```text
R_zR_z^T                 versus conj(R_z)R_z^T,
pseudocovariance          versus covariance,
bilinear square           versus modulus square.   (3.7)
```

Calling (3.3) a Hermitian square is therefore incorrect away from the line.

## 4. The entire compressed CCM half-orbit

At fixed Fourier section `N` and jet depth `R`, put

```text
R_z(n)=1/(d_n-z),

K(z)=alpha chi sin(zL/2)^2,

Ytilde_N(z)=K(z)R_zR_z^T,

Y_(N,R)(z)=J_(N,R)^T Ytilde_N(z)J_(N,R).          (4.1)
```

Here `alpha` and `chi` are real, with `chi!=0`, and the jet frame
`J_(N,R)` is the real matrix of E101.078(2.6).

### Lemma 4.1 - Entire rank-one atom

Every entry of `Ytilde_N(z)` and `Y_(N,R)(z)` is entire of exponential type
at most `L`, and

```text
rank Ytilde_N(z)<=1,
rank Y_(N,R)(z)<=1                                 (4.2)
```

for every `z`, including the removable lattice points.

### Proof

Away from the lattice, (4.2) is the displayed outer-product factorization
and its compression.
At `z=d_n`, the double zero of `sin(zL/2)^2` removes the two possible Cauchy
poles.  Entrywise continuation preserves the vanishing of every two-by-two
minor, so the rank bound persists.  The exponential type follows from the
sine factor. `QED`

Define the compressed parity-completed half-orbit

```text
A_(N,R)(z)=Y_(N,R)(z)+Y_(N,R)(-z).                (4.3)
```

### Corollary 4.2 - Holomorphic rank ceiling

```text
A_(N,R) is entire,
rank A_(N,R)(z)<=2 for every z,
A_(N,R)(conj z)=conj(A_(N,R)(z)).                 (4.4)
```

For real `x`, the complete on-line orbit matrix is a scalar-multiplicity
version of `A_(N,R)(x)` and hence has rank at most two.  For nonreal `z`, the
full compressed quartet adds the independent conjugate half-orbit:

```text
X_(N,R)(z)=A_(N,R)(z)+A_(N,R)(conj z).            (4.5)
```

For each fixed nondegenerate off-line quartet, the rank-four theorem of
E101.078 gives finite thresholds `N_0(z),R_0(z)` after which (4.5) has rank
four.  No uniform jet depth over all possible points is asserted.

The entries of `A_(N,R)` are admissible for degree-six use.  On the real
direction they are `O((1+|x|)^(-2))`; by Paley--Wiener each is the transform
of a compactly supported `L^2` source.  A product of six entries is
`O((1+|x|)^(-12))`, is the transform of the compactly supported sixfold
convolution, and belongs to the extended Weil class stated after Theorem
2.1.  The corresponding zero sums are therefore absolutely convergent.
All polar and archimedean terms remain present.  The exponential type and
Euler support are up to six times those of one entry, as required by the
support warning in (2.4a).

## 5. Exact mixed-bidegree localization

Extend `P_3` complex-polynomially and let `p_3` be its symmetric six-linear
polarization.  For compact notation, write

```text
p_3(A^[k],B^[6-k])
=p_3(A,...,A,B,...,B).                             (5.1)
```

### Theorem 5.1 - Only three mixed bidegrees survive

For every `z`,

```text
P_3(X(z))
=sum_(k=2)^4 binom(6,k)
 p_3(A(z)^[k],A(conj z)^[6-k]).                   (5.2)
```

In particular, all nonzero detector content is mixed between `z` and
`conj z`.

### Proof

Write a third minor of `A+B` as a cubic polynomial in the entries of the two
matrices.  Since `rank A<=2` and `rank B<=2`, its pure `A^3` and `B^3`
coefficients vanish.  Every third minor therefore has only the two types

```text
A^2B,  AB^2.                                      (5.3)
```

The square of such a minor has only bidegrees `(4,2)`, `(3,3)` and `(2,4)`.
Summing the squared minors proves (5.2).  In particular, the two extreme
terms

```text
p_3(A^[6])=P_3(A),
p_3(A(conj z)^[6])=P_3(A(conj z))                 (5.4)
```

vanish as a special case. `QED`

### Corollary 5.2 - Exact location of the rank-four force

For an on-line orbit, (5.2) vanishes because the complete orbit has rank at
most two.  For every fixed nondegenerate off-line orbit, the sum in (5.2) is
strictly positive after the finite jet depth of E101.078.  Consequently at
least one mixed bidegree is nonzero, but no individual mixed term is asserted
to have a sign.

The positivity belongs only to their complete real sum.

## 6. What the one-trace construction actually closes

Corollary 2.2 applies to the degree-six coordinate polynomial

```text
z -> P_3(A(z)).                                    (6.1)
```

It gives a finite Gamma--Euler expression for

```text
sum_rho m_rho P_3(A(rho)).                         (6.2)
```

But Lemma 4.1 and Corollary 4.2 give the stronger termwise identity

```text
P_3(A(z))=0 for every complex z.                   (6.3)
```

Thus (6.2) is an exact source-first same-zero diagonal and is identically
zero for an algebraic rank reason which is independent of RH.  Its prime and
archimedean sides cancel before any zero-location conclusion can be drawn.
The statement uses the linear multiplicity weight in (2.2); the conclusion
remains zero under every positive multiplicity convention because (6.3) is
termwise.

This proves that the missing information was never merely equality of six
holomorphic labels.  The missing information is the conjugate half-orbit in
the mixed terms of (5.2).

There is a scalar full-jet version of the same split.  For

```text
a_r(z)=Xi^((r))(z)/r!,

T_Xi(z)=sum_(r>=0)a_r(z)^2,

S_Xi(z)=sum_(r>=0)|a_r(z)|^2,                      (6.4)
```

`T_Xi` is holomorphic; its finite truncations are bilinear source
convolutions.  E101.077 supplies the full-jet limit locally at each fixed
spectral point.  It does not justify interchanging that limit with the zero
sum or with the Weil functional.  Thus only finite jet truncations are
source-accessible here.  `S_Xi` is Hermitian.  Pointwise, E101.077 gives

```text
G_Xi(z)=1/4[S_Xi(z)^2-|T_Xi(z)|^2].               (6.5)
```

The explicit formula can access each finite square-side algebra behind
`T_Xi`; the off-line detector uses the modulus-square data in `S_Xi`.
Equation (6.5) is the scalar form of the bidegree wall.  Spectral summability
of its full-jet limit remains open.

## 7. Why two traces recreate the graph problem

Let `H` and `J` be holomorphic atom features.  Multiplying one trace by the
conjugate of another gives

```text
[sum_p m_p H(p)]conj([sum_q m_q J(q)])
=sum_(p,q)m_pm_q H(p)conj(J(q)).                  (7.1)
```

Every pair `(p,q)` occurs.  The mixed bidegrees in (5.2) require the graph

```text
q=p in the antiholomorphic notation,

equivalently q=conj p when both legs are written holomorphically.      (7.2)
```

Selecting (7.2) from (7.1) is exactly the missing spectral diagonal.

This bilinear graph is necessary but not by itself the degree-six detector.
One must also bind all `k` holomorphic and `6-k` reflected legs to the same
graph point, assemble the `+/-` half-orbits inside `A`, sum `k=2,3,4`, and
choose a multiplicity convention.  These requirements are included in
`MATCHED-EVENT-TRANSPORT` below.

Nor does the source involution solve it.  In one trace it evaluates

```text
J^sharp(p)=conj(J(conj p)),                        (7.3)
```

not

```text
conj(J(p))=J^sharp(conj p).                        (7.4)
```

For real-type CCM coordinates, (7.3) is again a holomorphic coordinate at
`p`; (7.4) is the conjugate graph coordinate.

### Theorem 7.1 - One-trace ceiling

Within the algebra generated by finitely many fixed admissible sources,
convolution, linear combination, differentiation and the source involution,
the response of one Weil trace to a controlled quartet is harmonic in the
two real coordinates of its position.  It cannot produce the complete
nonzero detector (5.2) on a connected open controlled-position domain which
crosses the real axis and contains a sufficiently resolved nondegenerate
off-line point.

### Proof

Every listed source operation preserves holomorphy of the Fourier transform;
the involution acts by (7.3).  For a fixed resulting transform `H`, the
controlled-quartet contribution is

```text
H(z)+H(-z)+H(conj z)+H(-conj z),                  (7.5)
```

up to fixed real weights.  It is a sum of a holomorphic and an
antiholomorphic function, hence harmonic.  By the reality assumptions in
Section 4, the complete right side of (5.2) is

```text
D_(N,R)(z)=P_3(2 Re A_(N,R)(z))>=0.               (7.6)
```

It vanishes at every interior real point because the on-line matrix has rank
at most two, and it is positive at the resolved off-line point.  If it were
harmonic on the connected domain, the strong minimum principle applied at
an interior real zero would make it identically zero, a contradiction.
Therefore no one-trace quartet response equals the complete detector on
that family. `QED`

Individual mixed bidegrees can cancel or vanish and are not assigned separate
signs.  The theorem concerns their complete real sum; it does not assert that
every summand in (5.2) is separately nonholomorphic.

An identity valid only at the actual Xi zeros because of a special arithmetic
relation is not excluded.  Such an identity must exhibit that relation on
the source side; interpolating the discrete divisor is not admissible.

## 8. Prime matching is not spectral matching

Bohr characters retain multiplicative prime frequencies before the explicit
formula is applied.  At second order orthogonality matches equal frequencies,
but an ordinary balanced sixth moment retains every relation
`q_1q_2q_3=r_1r_2r_3`, not only six equal events.  An exact same-event sixth
diagonal therefore requires the marked-event divided power or an independent
label projector.  This is source-first arithmetic data, but its atoms are

```text
q=p^m,                                             (8.1)
```

not Riemann zeros.

The moving-cutoff finite Weil path gives an even sharper source coordinate:
each threshold `u=log q` has an exact rank-one von Mangoldt event.  At a fixed
Galerkin level, one may therefore form directly from the marked events a
labelled source tensor such as

```text
Ecal_N^((6))=sum_q E_(q,N)^(tensor 6).             (8.2)
```

without knowing any zero.

The explicit formula supplies equality of total linear functionals.  It does
not supply an atomwise map

```text
q event -> one zero rho.                           (8.3)
```

Consequently, tensoring the source events does not automatically give

```text
sum_rho Y_rho tensor[conj(R_rho)R_rho^T].         (8.4)
```

### Definition 8.1 - Matched-event transport

`MATCHED-EVENT-TRANSPORT` is an identity, derived before spectral
aggregation, which maps a labelled prime-event divided power such as (8.2)
to the mixed spectral graph contraction in (5.2), with all prime,
archimedean and cutoff terms retained.

It must prove:

```text
the common spectral label, rather than insert it;
compatibility with the Schwarz involution versus atomwise conjugation;
compatibility of the sixth-power jump weights with the declared linear or
higher spectral multiplicity convention;
retention of every archimedean, polar and cutoff correction channel;
cofinal summability and the declared order of limits;
absence of mixed zero pairs;
the arithmetic vanishing required by Omega7.                       (8.5)
```

Without the first clause, the construction merely diagonalizes prime events,
a mechanism already present in the literature.

## 9. Measure form of the same wall

Write the spectral divisor formally as

```text
mu_Xi=sum_rho m_rho delta_rho.                     (9.1)
```

One explicit formula is the linear pairing

```text
<mu_Xi,H>.                                         (9.2)
```

There are two different graph measures.  Since `mu_Xi` is atomic, the Borel
restriction of its product measure to the conjugation graph

```text
Gamma={ (p,q):q=conj p }.                          (9.3)
```

exists unconditionally and equals

```text
(mu_Xi tensor mu_Xi)|_Gamma
 =sum_p m_p^2 delta_((p,conj p)).                  (9.4)
```

The linear-multiplicity graph appropriate to one Weil trace is instead the
pushforward

```text
gamma_Xi=(id,conj)_#mu_Xi
        =sum_p m_p delta_((p,conj p)).             (9.5)
```

Both measures are elementary once the labelled divisor is given.  Neither is
an arithmetic construction from the Gamma--Euler side.  In this document the
target uses (9.5), matching the linear multiplicity in (2.2).  If instead
multiplicity is absorbed into the orbit matrix as in E101.079, then
`P_3(m_pX_p)=m_p^6P_3(X_p)`; that is a third convention and requires a
separate bridge.

The missing operation is therefore not the abstract existence of a Borel
graph measure.  It is a source-side realization of the linear functional

```text
integral_Gamma sum_(k=1)^5 binom(6,k)
 p_3(A(p)^[k],A(q)^[6-k]) d gamma_Xi(p,q),         (9.6)
```

including the `+/-` assembly inside `A`, derived without spectral labels.
A formal distributional pullback may still be useful for a non-atomic
regularization, but then its wavefront, normalization and mixed-pair bounds
must be proved.  It must not be confused with the already defined atomic
measure (9.5).

## 10. Two distinct covariance statements

The graph measure `gamma_Xi` in (9.5) is positive whether or not RH holds.
Its GNS construction is therefore not circular by itself.  It is
spectrally adapted: it begins with the zero labels and hence does not realize
(9.6) arithmetically.

Burnol already formulated a probabilistic interpretation in which the Weil
distribution would serve as a covariance and explained why automatic
positivity of the full Weil form would yield RH.  This different implication
is circular:

```text
declare the Weil form a covariance
  -> obtain a positive spectral measure
  -> conclude Weil positivity.                    (10.1)
```

Thus positivity of the labelled graph is unconditional but source-inadmissible;
positivity of the complete arithmetic Weil form is admissible but
RH-equivalent.  E101.080--E101.082 use covariance language only to distinguish
bilinear and Hermitian algebra and do not identify these two statements.

## 11. Literature and novelty gate

The relevant primary antecedents are:

```text
Weil:
  https://doi.org/10.1070/IM1972v006n01ABEH001866

Burnol:
  https://arxiv.org/abs/math/9809119

Booker:
  https://arxiv.org/abs/1308.3067

Moran Ledezma:
  https://arxiv.org/abs/2311.08519

Picinbono:
  https://doi.org/10.1109/78.539051

Paley--Wiener:
  https://doi.org/10.1090/coll/019

Conrey--Snaith:
  https://arxiv.org/abs/0803.2795

Lagarias--Rodgers:
  https://arxiv.org/abs/1905.12123

Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh:
  https://arxiv.org/abs/2501.14545

Goldston--Lee--Schettler--Suriajaya:
  https://arxiv.org/abs/2503.15449

Iudelevich--Iudelevich:
  https://arxiv.org/abs/2508.18280

Fazzari--Gerspach:
  https://arxiv.org/abs/2412.20099

Tanaka:
  https://arxiv.org/abs/2008.07752

Banks:
  https://arxiv.org/abs/2502.20569

Groskin, finite Guinand--Weil dictionary:
  https://arxiv.org/abs/2607.02828

Groskin, moving von Mangoldt event measure:
  https://doi.org/10.5281/zenodo.21242028           (11.1)
```

The convolution theorem, same-argument product (2.3), Schwarz reflection,
Paley--Wiener support, distributional linearity,
covariance/pseudocovariance distinction and Bohr frequency matching are
known at their stated orders; at sixth order the ordinary Bohr mean enforces
multiplicative balance rather than equality of all event labels.  In the
inspected higher-correlation frameworks of Conrey--Snaith and
Lagarias--Rodgers, the results use conditional input, restricted Fourier
support or asymptotic statistics and do not provide the exact graph (9.3).
The finite Guinand--Weil dictionary identifies an exact finite source quotient
but does not recover individual spectral events.

The same-height or symmetric spectral diagonal is also not new.  For a zero
`rho=beta+i gamma`, the functional-equation partner
`1-conj(rho)=1-beta+i gamma` has the same ordinate.  In the centered
coordinate

```text
z_rho=gamma+i(1/2-beta),                           (11.2)
```

this is exactly `z_rho -> conj(z_rho)`.  The cited pair-correlation work uses
that symmetric diagonal to obtain proportional information about critical or
simple zeros.  It does not derive the exact measure (9.5) from Gamma--Euler
or exclude one exceptional off-line orbit.

The higher-order arithmetic diagonal is known as well.  The cited
Iudelevich--Iudelevich formula produces Dirichlet series with coefficients
`Lambda(n)^m` from correlations of `m` independent zero ordinates.  The
Fazzari--Gerspach framework couples prime powers to a twisted pair
correlation; Tanaka's absolute tensor products and the cited sum-correlation
work naturally generate all tuples.  None selects one spectral atom together
with its conjugate from the source side.  Accordingly, no novelty is claimed
for same-height pairing, higher prime moments, twisted correlations, or
tensoring to obtain all tuples.

No inspected independent primary source contains the CCM-specific
decomposition (5.2) or a source-first transport of the mixed bidegrees from
labelled von Mangoldt events to conjugate zero pairs.  The two Groskin records
are neighboring inputs within the present program and are not independent
evidence of novelty.  Potential novelty is restricted to the localization
(5.2) and to a future proof of `MATCHED-EVENT-TRANSPORT`.  No novelty is
claimed for (1.1).

## 12. Revised strategy

The following point is closed:

```text
Gamma--Euler can select only mixed tuples after multiplication.       false

One trace of a convolution selects one common zero holomorphically.    true
                                                                    (12.1)
```

The following stronger target replaces it:

```text
MIXED-BIDEGREE-GAMMA-EULER:
  derive the sum of the k=1,...,5 terms in (5.2) from a single source-side
  current or a rigorously renormalized graph pullback;

MATCHED-EVENT-TRANSPORT:
  prove that the moving prime-event tensor transports to that mixed spectral
  current, rather than only to a one-level total;

SINGULAR-DIAGONAL-PULLBACK:
  realize the mixed functional (9.6) through a non-atomic regularization with
  explicit norm growth and ordered-limit cancellation;

WEIGHTED-JET-POTENTIAL-CONVERGENCE:
  retain the direct RH-strength potential route of E101.079.         (12.2)
```

After E101.085, the preferred minimal target is

```text
PARITY-GRAM-GRAPH-TRACE:
  derive the parity-resolved bilinear conjugate energy from a complete
  second-order Gamma--Euler pair current.                             (12.3)
```

`MIXED-BIDEGREE-GAMMA-EULER` remains a sufficient stronger target but is no
longer the first construction to attempt.

The first two targets are now preferred because they use genuinely
pre-aggregation source data.  Neither may introduce a zero label, a spectral
projector, `Xi'/Xi`, `log|Xi|`, or a positive Weil covariance on its
hypothesis side.

## 13. Stop rule

Freeze the following repetitions:

```text
another holomorphic convolution power presented as the conjugate graph;
confusing H^sharp(z) with conj(H(z));
calling prime-label Bohr matching a same-zero spectral matching theorem;
tensoring two one-level explicit formulas without a graph restriction;
postulating a positive covariance or GNS space for the full Weil form;
using asymptotic n-level correlations to exclude one exceptional orbit;
presenting the same-height or symmetric spectral diagonal as new;
presenting Lambda(n)^m moments or prime-twisted pair correlations as an exact
same-zero graph;
using density-one or proportional critical-line results to exclude finitely
many off-line zeros;
claiming novelty for the convolution diagonal (2.3).                 (13.1)
```

Further Gamma--Euler work must exhibit a mixed bidegree from (5.2), not only
another pure holomorphic term.  By E101.085, one parity-resolved `(1,1)`
contraction is sufficient.

## 14. Status

```text
proved:
  exact one-trace same-zero convolution diagonal;
  bilinear-square versus modulus-square distinction;
  entire rank-at-most-two CCM half-orbit;
  exact mixed-bidegree expansion of the rank-four detector;
  vanishing of bidegrees k=0,1,5,6;
  one-trace harmonic ceiling on an open controlled family;
  exact formulation of matched-event transport;

closed as force-neutral:
  pure holomorphic same-zero products;
  prime-event matching without spectral transport;
  labelled graph positivity as source-inadmissible infrastructure;
  full Weil covariance when positivity is merely postulated;

still open:
  PARITY-GRAM-GRAPH-TRACE;
  MIXED-BIDEGREE-GAMMA-EULER;
  MATCHED-EVENT-TRANSPORT;
  SINGULAR-DIAGONAL-PULLBACK;
  WEIGHTED-JET-POTENTIAL-CONVERGENCE;
  DIRECTIONAL-IDENT and Omega7.
```
