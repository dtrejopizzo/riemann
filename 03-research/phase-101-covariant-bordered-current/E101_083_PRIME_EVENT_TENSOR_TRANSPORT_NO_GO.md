# E101.083 - Positive prime-event tensor-power transport no-go

## 1. Decision

The moving prime cutoff supplies exact, independently located von Mangoldt
events before spectral aggregation.  Their marked diagonal tensor cannot be
transported by an exact real positive tensor power, or by an exact Hermitian
`ell^6` isometry, to the same-zero spectral diagonal.

The obstruction is finite and elementary.  Let `e_q` label prime-power
events and `f_omega` label spectral orbits.  If a linear transport `T` were to
send the positive sixth diagonal tensor

```text
D_P=sum_q w_q e_q^(tensor 6), w_q>0,               (1.1)
```

to

```text
D_Z=sum_omega v_omega f_omega^(tensor 6),
v_omega>0,                                         (1.2)
```

then the rows of the matrix of `T` would have pairwise disjoint supports.
Every prime event could feed at most one spectral orbit.  Therefore a mixing
map cannot satisfy this positive factorization.

The qualifier is essential.  A general complex symmetric sixth tensor can
use root-of-unity cancellation while every source column mixes.  Signed
archimedean, polar or cutoff channels can also cancel mixed coefficients, and
the CCM exterior detector has not been reduced to a Hermitian `ell^6` moment
of one linear map.  The finite theorem below excludes none of those escapes.

This does not contradict E101.082.  Its one-trace same-zero identity applies
the explicit formula to a *convolution* of sources.  On the arithmetic side
that convolution contains mixed prime events.  It is not the image of the
same-prime tensor (1.1).

Consequently,

```text
prime-label diagonalization
  does not functorially become
zero-label diagonalization.                         (1.3)
```

Any surviving event route must violate at least one proved hypothesis: it may
use a complex signed cancellation, retain indispensable auxiliary channels,
cease to be a tensor power of one linear map, or pass through a controlled
singular limit.  In every case it must explain arithmetically why the complete
operation creates conjugate zero pairs.

## 2. Exact moving-cutoff event measure

Fix a Galerkin level `N` and let

```text
u=log c                                             (2.1)
```

be the moving prime cutoff.  The singular part of the second derivative of
the finite Weil path has the form

```text
d(Q_N')_sing(u)
=-2 sum_(q=p^m)
 [Lambda(q)/(sqrt(q)log q)]
 J_N delta_(log q)(du),                            (2.2)

J_N=1 1^T.                                         (2.3)
```

Equivalently, the first derivative has the displayed rank-one jump at each
threshold.  Every event is finite, exact and source-first.

Two features must be separated:

```text
matrix direction:
  all events are collinear multiples of J_N;

event label:
  q is retained only by the support point u=log q and its scalar weight.
                                                               (2.4)
```

If the support coordinate is discarded, every tensor power of the jump
matrices collapses to one scalar multiple of `J_N^(tensor 6)`.  Hence a
labelled construction must retain the event measure in `u`, not only the
assembled matrix path at one cutoff.

Writing

```text
a_q=2Lambda(q)/(sqrt(q)log q),                    (2.5)
```

the marked sixth divided power of the actual jumps has positive event
weights

```text
sum_q (-a_qJ_N)^(tensor 6) e_q^(tensor 6)
 =J_N^(tensor 6)sum_q a_q^6e_q^(tensor 6).        (2.6)
```

Thus the abstract weight in (1.1) is `w_q=a_q^6` for this construction.

For `q=p^m`, the jump size simplifies to

```text
a_(p^m)=2/(m p^(m/2)).                            (2.6a)
```

Hence the marked sixth tensor has an honest cofinal total variation:

```text
sum_q a_q^6
 =64 sum_p Li_6(p^(-3))<infinity.                 (2.6b)
```

This does not produce a convergent first-level colored field.  Indeed,

```text
sum_q a_q^2>=4 sum_p 1/p=infinity.                (2.6c)
```

Thus the natural cofinal object is the marked `ell^6` tensor or cumulant,
not an `L^2` randomization of the unassembled jumps.

Ordinary Bohr characters

```text
q^(it)=exp(it log q)                                (2.7)
```

preserve multiplicative frequencies, but a balanced sixth moment enforces

```text
q_1q_2q_3=r_1r_2r_3,                              (2.8)
```

not equality of all six prime-power events.  For example,
`2*2*8=2*4*4`.  Exact same-event selection therefore requires the marked
divided power (2.6), or an independent event-label projector stronger than
the ordinary one-parameter Bohr mean.  No such projector is being credited
to classical prime-phase averaging here.

## 3. Abstract finite label transport

Let `P` and `Z` be finite sets.  Write

```text
V_P=R^P with basis {e_q},
V_Z=R^Z with basis {f_omega}.                       (3.1)
```

For positive weights define the symmetric diagonal tensors

```text
D_P^((6))=sum_(q in P)w_q e_q^(tensor 6),

D_Z^((6))=sum_(omega in Z)v_omega
                         f_omega^(tensor 6).       (3.2)
```

Let `T:V_P->V_Z` be linear:

```text
Te_q=sum_omega a_(omega,q)f_omega.                 (3.3)
```

### Theorem 3.1 - Sixth-diagonal transport forces disjointness

If

```text
T^(tensor 6)D_P^((6))=D_Z^((6)),                  (3.4)
```

then for every `q` and every two distinct target labels
`omega!=nu`,

```text
a_(omega,q)a_(nu,q)=0.                             (3.5)
```

Thus each source label contributes to at most one target label.

### Proof

The coefficient of

```text
f_omega^(tensor 4) tensor f_nu^(tensor 2)          (3.6)
```

in the symmetrization of the left side of (3.4) is

```text
sum_q w_q a_(omega,q)^4a_(nu,q)^2.                (3.7)
```

The corresponding coefficient on the diagonal tensor `D_Z^((6))` is zero.
Every summand in (3.7) is nonnegative and every `w_q` is positive.  Therefore
each product in (3.5) vanishes. `QED`

### Corollary 3.2 - No mixing transform preserves the sixth diagonal

If one column of `T` has two nonzero target coordinates, (3.4) is impossible.

The conclusion permits several source labels to feed one target label.  It
does not require a bijection.  What it forbids is the feature essential to an
explicit-formula kernel: one source event spreading over many spectral
coordinates.

## 4. Hermitian version

The conjugate graph naturally uses complex coordinates.  Let

```text
T:C^P->C^Z,
Te_q=(a_(omega,q))_omega.                          (4.1)
```

Suppose the proposed transport preserves the positive sixth Hermitian moment
in the sense that

```text
sum_q w_q |<Te_q,z>|^6
=sum_omega v_omega|z_omega|^6
for every z in C^Z.                                (4.2)
```

### Theorem 4.1 - Hermitian sixth-moment disjointness

Equation (4.2) implies

```text
a_(omega,q)a_(nu,q)=0
for omega!=nu and every q.                         (4.3)
```

### Proof

Choose `z` supported on two coordinates `omega,nu`, expand (4.2), and average
over the relative unit-circle phase.  The coefficient of

```text
|z_omega|^4|z_nu|^2                               (4.4)
```

is a positive constant times

```text
sum_q w_q |a_(omega,q)|^4|a_(nu,q)|^2.            (4.5)
```

The right side of (4.2) contains no mixed monomial, so (4.5) is zero.  Swap
`omega,nu` and use positivity to obtain (4.3). `QED`

This is the finite weighted `ell^6` disjointness principle.  The special role
of the exponent is only that it is even and greater than two.  At exponent
two, unitary mixing is possible; at exponent six, exact diagonal preservation
forces coordinate disjointness.

### Proposition 4.2 - Complex symmetric cancellation escape

The real theorem does not extend to an unstarred complex symmetric sixth
tensor.  Let `zeta_j=exp(2pi i j/6)`, `0<=j<=5`, and define six mixing columns

```text
Te_j=f_1+zeta_jf_2.                                (4.6)
```

Then

```text
(1/6)sum_(j=0)^5(Te_j)^(tensor 6)
 =f_1^(tensor 6)+f_2^(tensor 6).                  (4.7)
```

### Proof

The coefficient with `k` copies of `f_2` contains

```text
(1/6)sum_(j=0)^5 zeta_j^k.                        (4.8)
```

This is zero for `1<=k<=5` and one for `k=0,6`. `QED`

Every column in (4.6) has two nonzero target coordinates.  Thus positivity
of the real even monomials in Theorem 3.1, or the modulus identity in Theorem
4.1, is indispensable.  Merely saying that a construction has six complex
legs does not invoke either theorem.

The CCM statistic is

```text
P_3(X)=sum_(I,J)|det X_(I,J)|^2,                  (4.9)
```

a squared norm of cubic minor features.  It has not been shown to equal the
`ell^6` moment (4.2) of one linear event map.  Theorem 4.1 may be applied to a
CCM transport only after such a factorization is proved exactly.

### Proposition 4.3 - Exact colored mixed-bidegree projector

Let `Q` be a finite label set, let `zeta=exp(2pi i/6)`, and let `P` be a
homogeneous polynomial of degree six with symmetric polarization `p`.  For
two labelled families `U_q,V_q` and `1<=ell<=5`,

```text
1/6^(|Q|+1)
 sum_(epsilon in mu_6^Q) sum_(r=0)^5 zeta^(-r ell)
 P(sum_q epsilon_q[U_q+zeta^rV_q])

 =sum_q binom(6,ell)
   p(U_q^[6-ell],V_q^[ell]).                      (4.10)
```

### Proof

Expand the degree-six polynomial.  Averaging the independent color
`epsilon_q` kills a monomial unless the number of occurrences of every
label is divisible by six.  Since the total degree is six, all six factors
must have one common label `q`.  For that label, the remaining cyclic
Fourier average is

```text
1/6 sum_(r=0)^5 zeta^(-r ell)P(U_q+zeta^rV_q),    (4.11)
```

which extracts exactly the term containing `ell` copies of `V_q`. `QED`

For the CCM polynomial, only `ell=2,3,4` survive by E101.085.  Formula
(4.10) therefore closes the finite polarization combinatorics *provided*
`U_q` and `V_q` are already the holomorphic and conjugate half-orbits of one
common spectral label.  It does not construct that shared label.

### Corollary 4.4 - Coloring primes alone deletes the auxiliary coupling

Let `A` be an uncolored aggregate and `B_q` the colored prime-event atoms.
Then

```text
1/6^|Q| sum_(epsilon in mu_6^Q)
 P(A+sum_q epsilon_qB_q)
 =P(A)+sum_qP(B_q).                               (4.12)
```

All terms containing between one and five colored factors vanish.  For the
moving cutoff `B_q=a_qJ_N` has rank one, so

```text
P_3(B_q)=0,

colored-prime average=P_3(A).                     (4.13)
```

Consequently, leaving the Gamma, polar and cutoff channels in one global
uncolored block removes every prime--auxiliary mixed term.  To use (4.10),
those channels would need a canonical nonlocal decomposition into packages
`A_q` carrying the same event color.  The ordinary explicit formula supplies
no such decomposition.

## 5. Application to the explicit formula

The explicit formula is an equality of linear functionals on tests:

```text
sum_rho m_rho H(rho)
=Prime(h)+Arch(h)+Pole(h),
H=F[h].                                            (5.1)
```

It does not define an atomwise map `q->rho`.  If one nevertheless models a
finite proposed event transport by

```text
Te_q=sum_omega a_(omega,q)f_omega,                 (5.2)
```

then a Fourier or Guinand kernel has many nonzero `a_(omega,q)` for one fixed
`q`.  Theorems 3.1 and 4.1 show that such a map cannot send the same-prime
diagonal to the same-zero diagonal through either of the exact positive
factorizations stated below.

### Theorem 5.1 - Positive tensor-power matched-event transport is impossible

No finite transport which

```text
is linear in the marked von Mangoldt event measure;
mixes one prime-power event across two or more spectral labels;
obtains its sixth-order graph by an exact real positive tensor identity
of the form (3.4), or an exact Hermitian ell^6 identity (4.2);
and has no additional signed channel cancelling mixed coefficients       (5.3)
```

can produce the exact positive spectral diagonal.

### Proof

After choosing finite source and target windows, (5.3) is exactly the setting
of Theorem 3.1 or Theorem 4.1.  Mixing contradicts the required disjointness.
`QED`

The theorem is conditional on the claimed positive factorization through a
linear atom transport and on the absence of auxiliary signed terms.  It does
not assert that the explicit formula itself comes with a matrix `T`; rather,
it proves that this restricted introduction of `T` cannot solve the graph
unless `T` already performs atomwise spectral routing.

The actual explicit formula contains archimedean, polar and cutoff channels.
If they enter the sixth identity with signs, their mixed coefficients can in
principle cancel those of the prime events, and the positivity proof no longer
applies.  A finite identity with those terms retained remains open.  An
approximate or merely cofinal identity also remains outside this exact finite
theorem unless quantitative lower bounds on the event weights and mixing
coefficients are supplied.

There is also a multiplicity mismatch.  Applying a sixth tensor power to a
one-level spectral atom of weight `m_rho` produces weight `m_rho^6`, whereas
the one-trace graph convention of E101.082 uses `m_rho`.  The abstract
weights `v_omega` in (3.2) may encode either convention, but an application
must derive the conversion.  It cannot normalize by unknown zero
multiplicities on the source side.

## 6. Why one-trace convolution is not a counterexample

For fixed sources `h_j`, E101.082 proves

```text
W(h_1*...*h_6)
=sum_rho m_rho product_j H_j(rho).                 (6.1)
```

The spectral side of (6.1) has one common zero.  On the source side, however,
the argument of `W` is

```text
h_1*...*h_6.                                       (6.2)
```

Convolution at a prime-event location includes every additive decomposition
of that source coordinate.  It is not the weighted marked-event diagonal

```text
sum_q w_q product_j h_j(log q).                    (6.3)
```

Thus (6.1) transports a source convolution, not the prime diagonal tensor
(1.1).  Fourier duality exchanges pointwise spectral multiplication with
source convolution; it does not exchange spectral diagonal labels with equal
prime labels.

This gives a useful correction to the route:

```text
same-zero holomorphic product
  <-> source convolution;

marked same-prime divided power
  <-> arithmetic event diagonal;

the two source operations are different.                           (6.4)
```

Any proposed bridge between them is already a new nonlinear explicit formula.

Root-of-unity coloring does not alter this dichotomy.  If the color average
is performed inside one Weil trace, Proposition 4.3 and the convolution
theorem give

```text
W(sum_q h_(q,1)*...*h_(q,6))
 =sum_rho m_rho sum_q product_j H_(q,j)(rho).      (6.5)
```

This retains one zero, linear multiplicity and every Gamma, polar and Euler
channel, but it is the same holomorphic diagonal as E101.082.  If instead
the average is performed outside the trace, then

```text
E_epsilon product_(j=1)^6 W(h_(epsilon,j))
 =sum_(rho_1,...,rho_6)m_(rho_1)...m_(rho_6)
   sum_q product_j H_(q,j)(rho_j).                 (6.6)
```

All spectral sextuples remain, and a repeated zero carries multiplicity
`m_rho^6`.  The color forces a common source label, not a common spectral
label.  Expanding each `W` retains, rather than removes, the full family of
prime--Gamma--pole--cutoff products.

## 7. Finite source quotient does not add event routing

At fixed Galerkin level, the finite Guinand--Weil dictionary factors signed
source distributions through an exact quotient of dimension `2N+1`.  This
proves exact transport from a coefficient vector to one admissible zero-sum
test.  It does not identify the individual zeros contributing to that sum.

The moving event path enriches the input by retaining all support locations
`log q`.  Yet its matrix jump direction is the same `J_N` at every event.
Therefore:

```text
fixed quotient without event locations:
  loses the labels immediately;

full event measure with locations:
  retains prime labels but has no atomwise zero routing;

positive exact tensor-power transport of the event measure:
  is ruled out by Theorem 5.1 under its no-auxiliary-term
  hypothesis.                                                    (7.1)
```

Multiple probes can improve identification of the source event measure.
They cannot alter Theorem 5.1 unless the transport ceases to be the tensor
power of a mixing linear map or introduces one of the signed or limiting
escapes stated after that theorem.

The natural exponential event kernel also has an exact false positive.  If

```text
H_q(z)=b_q exp(-iu_qz),                            (7.2)
```

then its `(3,3)` colored contraction contains

```text
sum_q |b_q|^6
 exp[-iu_q(rho_1+rho_2+rho_3
                 -conj(sigma_1)-conj(sigma_2)-conj(sigma_3))].       (7.3)
```

Choose three distinct zeros and put `sigma_j=conj(rho_j)`.  The exponent in
(7.3) is zero, so the value is `sum_q|b_q|^6>0`, although a one-orbit tensor
must vanish on six distinct labels.  The Fourier kernel detects a balanced
sum relation; it does not detect equality of the orbit labels.

## 8. Relation to quotient-algebra real-rootedness

For a finite real polynomial, its coefficients determine the roots and hence
their conjugate pairing.  Recovering that pairing without listing roots is
possible through Hermite--Bezout matrices, resultants or quotient-algebra
traces.  Positivity of the resulting Hermite form is exactly a real-rootedness
criterion.

The infinite Xi analogue therefore has two known realizations:

```text
root-adapted:
  list the divisor or use Xi'/Xi and form the graph directly;

coefficient-adapted:
  build a Hermite/Laguerre/Jensen hierarchy whose positivity is
  RH-equivalent.                                                   (8.1)
```

The prime-event data determine the coefficients globally, so they can in
principle feed (8.1).  That does not lower the force.  E101.078 already
freezes this quotient-algebra return unless a new arithmetic identity proves
the required sign rather than restating it.

## 9. Surviving higher-order target

Define `NONLINEAR-MATCHED-EVENT-TRANSPORT` to be a source-first identity
which starts with the complete marked event measure (2.2) and produces the
mixed-bidegree current of E101.082 without factoring through

```text
T^(tensor 6)D_P^((6))                              (9.1)
```

for a mixing linear `T`.

This name includes a genuinely sixth-order operator which is linear on the
marked tensor `D_P^((6))` but does not factor as `T^(tensor 6)`.  Such an
operator is nonlinear relative to the original one-level event measure.  A
complex symmetric construction using Proposition 4.2, or a complete signed
Gamma--Euler identity with compensating auxiliary channels, also belongs to
the surviving class.

It must include:

```text
NET-1  an explicit nonlinear operation on the event measure, with all
       diagonal renormalizations declared;

NET-2  an exact Gamma--Euler identity showing that its zero side is the
       conjugation graph, not an all-pairs correlation;

NET-3  compatibility with the weights a_q^6, the declared zero-multiplicity
       convention and the rank-two/rank-four CCM atom;

NET-4  fixed-cutoff bounds followed by a justified cofinal order;

NET-5  an arithmetic proof that the resulting nonnegative mixed-bidegree
       sum vanishes.                                                (9.2)
```

By E101.082, `NET-5` or a hidden premise in `NET-2`--`NET-4` must carry full
RH strength.

## 10. Literature gate

The imported mechanisms are:

```text
Moran Ledezma, Bohr matching of arithmetic labels:
  https://arxiv.org/abs/2311.08519

Groskin, finite source quotient:
  https://arxiv.org/abs/2607.02828

Groskin, moving von Mangoldt event measure:
  https://doi.org/10.5281/zenodo.21242028

Booker, the explicit formula as a linear distributional identity:
  https://arxiv.org/abs/1308.3067

Conrey--Snaith, conditional higher correlations:
  https://arxiv.org/abs/0803.2795

Lagarias--Rodgers, limits of known band-limited correlations:
  https://arxiv.org/abs/1905.12123                 (10.1)

Iudelevich--Iudelevich, higher prime-power diagonal:
  https://arxiv.org/abs/2508.18280

Fazzari--Gerspach, prime-twisted pair correlation:
  https://arxiv.org/abs/2412.20099

Tanaka, absolute tensor products and all-tuples Euler products:
  https://arxiv.org/abs/2008.07752

Lamperti, disjointness for ell^p isometries:
  https://doi.org/10.2140/pjm.1958.8.459           (10.2)
```

Linear isometries of `ell^p` for `p!=2` and uniqueness of diagonal symmetric
tensors are classical; Lamperti is the standard antecedent.  Theorems 3.1
and 4.1 are included with elementary proofs, and no novelty is claimed for
the abstract disjointness principle.

Higher arithmetic diagonals with coefficients `Lambda(n)^m`, twisted
prime--zero correlations, and exact tensor products producing all prime and
zero tuples also predate this document.  They confirm that higher moments do
not by themselves select one zero and its conjugate.  No novelty is claimed
for the idea of raising a marked prime event to sixth order.

No inspected source applies that principle to the restricted positive
tensor-power ansatz from the moving von Mangoldt event tensor to the CCM
conjugate-zero graph.  The potentially new result is this source-specific
early-kill for that ansatz and any future construction satisfying (9.2),
together with the exact accounting (4.10)--(4.13) of what sixth-root colors
do and do not preserve.

## 11. Stop rule

Freeze:

```text
identifying equal prime labels with equal zero labels;
applying a positive real or Hermitian tensor power to the one-level explicit
formula while discarding all auxiliary channels;
treating the fixed finite source quotient as event recovery;
discarding the support locations of the rank-one cutoff jumps;
using an ell^2/unitary analogy for a sixth diagonal tensor;
returning to Hermite--Bezout positivity without a new arithmetic sign law.
                                                                    (11.1)
```

Further event work must violate a stated hypothesis of Theorem 5.1 by a fully
specified arithmetic identity, not by an unnamed nonlinear transform.

E101.085 proves that the CCM exterior-cube detector factors through a
parity-resolved quadratic conjugate Gram.  Therefore a sixth-order transport,
although still logically admissible outside the no-go hypotheses above,
solves a strictly stronger matching problem than the current detector needs.
Freeze it as a primary route unless the quadratic
`PARITY-GRAM-GRAPH-TRACE` target is independently shown to fail.

## 12. Status

```text
proved:
  exact separation of matrix direction and event location;
  real sixth-diagonal disjointness theorem;
  Hermitian sixth-moment disjointness theorem;
  impossibility of exact finite real positive tensor-power mixing transport;
  impossibility under the complete Hermitian ell^6 identity;
  complex symmetric root-of-unity escape from the real theorem;
  distinction between source convolution and prime-event matching;
  exact sixth-root mixed-bidegree projector;
  collapse when only prime jumps are colored;
  absolute cofinal summability of the marked sixth tensor;
  balanced-sum false positive for the exponential event kernel;

closed negatively:
  exact finite positive real tensor-power transport without correction
  channels;
  exact finite complex transport satisfying the full Hermitian ell^6
  identity without correction channels;

still admissible:
  general MATCHED-EVENT-TRANSPORT;
  nonfactorized sixth-order transport;
  complex symmetric cancellation;
  signed Gamma--Euler compensating channels;
  approximate or cofinal transport;
  NONLINEAR-MATCHED-EVENT-TRANSPORT;
  MIXED-BIDEGREE-GAMMA-EULER;
  SINGULAR-DIAGONAL-PULLBACK;
  WEIGHTED-JET-POTENTIAL-CONVERGENCE;

preferred lower-arity target:
  PARITY-GRAM-GRAPH-TRACE;

still open:
  DIRECTIONAL-IDENT and Omega7.
```
