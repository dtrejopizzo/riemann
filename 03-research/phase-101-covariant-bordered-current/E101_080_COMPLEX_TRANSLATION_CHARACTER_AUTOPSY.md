# E101.080 - Complex-translation character autopsy

## 1. Decision

Complex translation appears to provide exactly the missing bounded
two-coordinate character of E101.079.  At the level of one already labelled
spectral atom, it does:

```text
conj(C_(-a)(p))C_a(p)
=exp(-i[t Re p+s Im p])|C_0(p)|^2,

a=(t-is)/2.                                         (1.1)
```

Equation (1.1) is correct.  It is not the response of the available CCM
matrix.

The CCM quartet is complex symmetric before orbit summation:

```text
M=sum_p K_p R_pR_p^T.                               (1.2)
```

In the exact full-line covariant term, its bilinear pairing cancels every
translation phase.  The corresponding Hermitian term conjugates the pole
together with the first Cauchy vector and retains only the one-dimensional
holomorphic phase `exp(-ipt)`; the transverse parameter `s` cancels
identically.  Finite CCM borders break this ideal covariance and must be kept
separately.  To obtain (1.1) from the covariant bulk by a matrix pairing one
must first introduce

```text
M_graph=sum_p K_p conj(R_p)R_p^T.                   (1.3)
```

Matrix (1.3) couples each pole to its own conjugate Cauchy vector.  It is the
minimal conjugate-graph character carrier.  To retain the original atom
`Y_p=K_pR_pR_p^T` at the same time, the actual lift is the tensor current

```text
Gcal=sum_p Y_p tensor [conj(R_p)R_p^T],             (1.3a)
```

or an exactly equivalent contraction.  Supplying the common label `p` in
(1.3a) is precisely the same-p diagonal information E101.079 leaves open.
Thus the proposed construction assumed the missing lift in its first
sesquilinear step.  No symmetry or rank property of `M_graph` itself is used;
in general its quartet sum need not be symmetric.

There are two further independent obstructions.  The available unregularized
theta-source representation and contour estimates control complex translation
only in a fixed strip, whereas exact phase diagonalization requires an
unbounded transverse mean.  On the finite Fourier mesh, the corresponding
diagonal translation has exponential condition number and amplifies the known
border and collar defects.

Heat regularization repairs the analytic strip and finite-mesh norm for each
fixed transverse parameter.  It does not create (1.3).  Consequently it is
valid infrastructure but not a new route around the diagonal wall.

The live target remains `BOUNDED-ORBIT-CHARACTER-LIFT`, now sharpened to:

```text
construct Gcal, or its fully contracted five-phase value, from the
Gamma--Euler source before spectral aggregation.                    (1.4)
```

## 2. Ideal translated Cauchy coordinate

Let `f` be a real source on the full line and write

```text
C_0(p)=integral_R f(x)exp(-ipx)dx.                  (2.1)
```

For the position jets used in E101.075,

```text
f(x)=x^r k(x),
C_0(p)=i^r Xi^((r))(p).                             (2.1a)
```

The unjetted choice `f=k` is useless on the actual divisor because
`C_0(p)=Xi(p)=0` at every Xi zero.  Complex translation must therefore be
combined with the jet frame; it cannot restore the fixed radical channel.

For a complex translate `a` in a domain where the contour shift is valid,
put

```text
f_a(x)=f(x-a).                                      (2.2)
```

Then

```text
C_a(p)=exp(-ipa)C_0(p).                             (2.3)
```

For a real source,

```text
conj(C_0(p))=C_0(-conj p),
conj(C_0(conj p))=C_0(-p).                         (2.4)
```

For `f=x^rk` with even `k`,

```text
C_0(-p)=(-1)^rC_0(p).                              (2.4a)
```

Set

```text
p=x+iy,
a=(t-is)/2,
conj(a)=(t+is)/2.                                  (2.5)
```

Since

```text
pa+conj(p)conj(a)=tx+sy,                            (2.6)
```

equations (2.3)--(2.5) give the desired atomwise identity.

### Proposition 2.1 - Two-dimensional atom character

```text
conj(C_(-a)(p))C_a(p)
=exp(-i[tx+sy])|C_0(p)|^2.                         (2.7)
```

### Proof

Directly,

```text
conj(C_(-a)(p))
=exp(-i conj(p)conj(a))conj(C_0(p)).                (2.8)
```

Multiply by (2.3) and use (2.6). `QED`

The right side of (2.7) has unit modulus apart from the fixed atom weight.
It is the exact character required by E101.079(4.4).

## 3. The CCM bilinear form is phase blind

For a pole `p`, define the Cauchy column

```text
R_p(n)=1/(d_n-p).                                   (3.1)
```

In the ideal translation calculation, choose coefficient vectors `u_a`
such that

```text
R_p^Tu_a=C_a(p).                                    (3.2)
```

The controlled response of E101.071 is

```text
delta M=sum_(p in P_zeta)K_pR_pR_p^T.              (3.3)
```

The natural CCM form is bilinear.  It gives

```text
u_(-a)^T(delta M)u_a
=sum_p K_p C_(-a)(p)C_a(p).                        (3.4)
```

By (2.3),

```text
C_(-a)(p)C_a(p)=C_0(p)^2.                          (3.5)
```

Thus both `t` and `s` disappear.  Bilinear translation covariance cannot
label even the ordinate of a spectral atom.

This bulk cancellation is not a truncation error.  It occurs in the ideal
full-line formula before any finite boundary is introduced.  At finite
`L,N`, the border terms of Section 6 can retain both parameters; this is why
`GRAPH-BORDER-CANCELLATION` remains a logically open contracted target.

## 4. The available Hermitian form loses the transverse phase

One may instead try the Hermitian pairing

```text
u_(-a)^*(delta M)u_a.                               (4.1)
```

The first Cauchy factor is then

```text
u_(-a)^*R_p
=conj(R_p^*u_(-a))
=conj(R_(conj p)^Tu_(-a))
=conj(C_(-a)(conj p)).                              (4.2)
```

Therefore

```text
u_(-a)^*(delta M)u_a
=sum_p K_p
 conj(C_(-a)(conj p))C_a(p).                       (4.3)
```

Using (2.3)--(2.5),

```text
conj(C_(-a)(conj p))C_a(p)
=exp(-ip[conj(a)+a])C_0(-p)C_0(p)
=exp(-ipt)C_0(-p)C_0(p).                           (4.4)
```

For the parity-`r` jet this becomes

```text
(-1)^r exp(-ipt)C_0(p)^2.                          (4.4a)
```

The parameter `s` cancels exactly.

### Theorem 4.1 - Sesquilinear bulk cancellation

For the ideal covariant part of the complex-symmetric CCM atom (3.3),
opposite complex translations produce only the holomorphic one-coordinate
signal

```text
sum_p K_p exp(-ipt)C_0(-p)C_0(p),                  (4.5)
```

They do not produce the bounded two-coordinate signal (2.7).  The exact
finite response is this term plus the borders obtained by substituting (6.4)
in both factors.

The modulus of the individual phase in (4.5) is

```text
|exp(-ipt)|=exp(ty).                                (4.6)
```

Hence one time direction grows exponentially at every off-line pole.  The
five independent means of E101.079 cannot be justified by bounded
almost-periodic convergence for (4.5).

## 5. The missing conjugate-graph carrier

To realize (2.7), define formally

```text
delta M_graph
=sum_p K_p conj(R_p)R_p^T.                         (5.1)
```

Then

```text
u_(-a)^*(delta M_graph)u_a
=sum_p K_p conj(C_(-a)(p))C_a(p),                  (5.2)
```

and Proposition 2.1 gives

```text
u_(-a)^*(delta M_graph)u_a
=sum_p K_p exp(-i[t Re p+s Im p])|C_0(p)|^2.       (5.3)
```

Equation (5.3) is the desired scalar signal term by term.  It defines an
actual summed signal only under the cutoff, summability and cofinal passages
declared below; none is inferred from the formal graph definition.

It is a scalar character signal for the selected source.  A fixed jet can
vanish at a multiple zero, and this scalar does not by itself retain the
matrix atom `Y_p` required by E101.079.  The complete construction must use
the full factorial jet family and keep `Y_p` in an auxiliary tensor leg as in
(1.3a).  The full jet prevents simultaneous vanishing; the common same-p
label is what supplies the matrix-valued signal.

More precisely, define

```text
W_Xi(p)=sum_(r>=0)|Xi^((r))(p)/r!|^2.              (5.3a)
```

E101.077 proves convergence.  Since an entire function whose complete jet
vanishes at one point is identically zero,

```text
W_Xi(p)>0 for every p.                              (5.3b)
```

Reality and evenness of `Xi` give

```text
W_Xi(-p)=W_Xi(conj p)=W_Xi(p).                     (5.3c)
```

Termwise contraction of the graph leg of `Gcal` against all factorial jets
formally produces the matrix character expression

```text
F_W(t,s)
=sum_p Y_p W_Xi(p)
 exp(-i[t Re p+s Im p]).                            (5.3d)
```

On an orbit `O`, the matrix atom is `W_Xi(O)X_O`.  Its rank is the rank of
`X_O`, and

```text
P_3(W_Xi(O)X_O)=W_Xi(O)^6P_3(X_O).                 (5.3e)
```

Thus, whenever the displayed contraction and sums are justified, the full-jet
weight preserves exact off-line detection.  What remains open is not
nonvanishing but the source-first construction, summability and cofinal
passage for `Gcal`.

The distinction between (3.3) and (5.1) is structural:

```text
R_pR_p^T:
  holomorphic bilinear atom supplied by the explicit formula;

conj(R_p)R_p^T:
  nonholomorphic same-p graph atom required for the two-dimensional
  character.                                       (5.4)
```

Summing the quartet does not repair (5.4).  Relabelling `p` by `conj p`
turns the conjugate of (3.3) back into the same real aggregate; it does not
create a mixed column `conj(R_p)R_p^T` with the same label in both factors.

Nor can ordinary multiplication produce it:

```text
(sum_p K_pR_pR_p^T)^*
 (sum_q K_qR_qR_q^T)                               (5.5)
```

contains every pair `(p,q)`.  Selecting `p=q` in (5.5) is again the diagonal
problem.

An aggregate alone does not determine the atomwise graph.  Already in one
scalar dimension,

```text
1^2+i^2=0,
|1|^2+|i|^2=2.                                     (5.6)
```

The same symmetric aggregate can therefore have different same-atom
Hermitian lifts.  Extra Gamma--Euler structure could in principle select the
physical decomposition, but no polynomial, tensor power, or log determinant
of the aggregate does so.

## 6. Finite Fourier translation has an exact border defect

On the finite mesh, put

```text
D_N=diag(d_n)_(|n|<=N),
U_(a,N)=exp(-iaD_N).                                (6.1)
```

At grid frequencies, (6.1) is the coefficient action of periodic
translation.  Off the grid it does not imply

```text
R_p^TU_(a,N)u_0=exp(-ipa)R_p^Tu_0.                 (6.2)
```

Indeed, if `c_n` are the coefficients of `u_0`, then the defect is exactly

```text
C_(a,N)(p)-exp(-iap)C_(0,N)(p)
=sum_(|n|<=N)c_n
 [exp(-iad_n)-exp(-iap)]/(d_n-p).                  (6.2a)
```

For a physical interval `I`, direct substitution gives

```text
integral_I f(x-a)exp(-ipx)dx
=exp(-ipa)integral_(I-a)f(u)exp(-ipu)du.            (6.3)
```

The difference between the last integral and the one over `I` is an endpoint
contour.  For periodic translation it is the wrap term; for truncated
one-sided shifts it is the boundary commutator of E83.005.  Thus the exact
finite identity is

```text
C_(a,N)(p)
=exp(-ipa)C_(0,N)(p)+Border_(a,N)(p).              (6.4)
```

The border in (6.4) must be retained through both faces and through the
complete Gamma--Euler recombination.  Dropping it repeats the false
projective-constancy step rejected in E101.064.

For the even centered kernel, two integrations by parts give the generic
endpoint asymptotic

```text
c_n
~L k'(L/2)/(2pi^2n^2)                              (6.5)
```

up to the known centering phase.  Odd position jets have an `O(1/n)` collar
unless their first endpoint moment is subtracted.  Thus every available raw
or corrected collar is polynomial, while the translation multiplier in the
next section is exponential.

## 7. Exponential finite-section conditioning

With (2.5),

```text
|U_(a,N)(n,n)|=exp(-d_n s/2).                       (7.1)
```

Since `d_n=hn`,

```text
||U_(a,N)||=exp(|s|hN/2),
||U_(a,N)^(-1)||=exp(|s|hN/2),
cond U_(a,N)=exp(|s|hN).                            (7.2)
```

The unshifted jet and border collars decay only polynomially in `N` in the
available estimates.  Multiplication by (7.2) destroys those bounds for any
fixed nonzero `s` as `N` tends to infinity.

Therefore the order

```text
N->infinity first, then |s|->infinity              (7.3)
```

is not justified by the E101.078 collar theorem.  Reversing the order is
worse, because every fixed finite section already grows exponentially in
`|s|`.

## 8. Fixed analytic strip versus an unbounded mean

The classical Riemann Fourier kernel has a theta-series representation whose
direct complex continuation is controlled in

```text
|Im a|<pi/4.                                        (8.1)
```

For `a=(t-is)/2`, this gives

```text
|s|<pi/2.                                           (8.2)
```

The five-phase projector also evaluates a sixth signal at the negative sum
of five phase variables.  If each transverse variable ranges in `[-T,T]`,
the unregularized source requires

```text
5T/2<pi/4,
T<pi/10.                                            (8.3)
```

The invariant mean needs `T->infinity`.  Equations (8.2)--(8.3) make this
impossible inside the fixed translation strip.

This obstruction is independent of zero gaps and of the CCM truncation.  It
is already present for the full-line source.

## 9. Heat regularization repairs only the infrastructure

Introduce the finite heat multiplier

```text
H_(epsilon,N)=exp(-epsilon D_N^2), epsilon>0.        (9.1)
```

Then

```text
||U_(a,N)H_(epsilon,N)||
<=sup_(d in R)exp(|s||d|/2-epsilon d^2)
=exp(s^2/(16epsilon)),                              (9.2)
```

uniformly in `N`.  The heated periodic source is entire, so its periodic
coefficient translation is defined for every complex `a`.  Heating does not
by itself remove the off-grid seam (6.2a); an exact periodized Cauchy boundary
correction must still accompany it.  In the ideal full-line spectral
coordinate, heating multiplies each Cauchy/source coordinate by

```text
exp(-epsilon p^2).                                 (9.3)
```

On two bilinear legs the factor is `exp(-2epsilon p^2)`; on the same-p graph
legs it is

```text
exp(-epsilon[p^2+conj(p)^2])
=exp(-2epsilon Re(p^2)).                            (9.3a)
```

Every finite-section heat matrix is invertible, so congruence preserves the
finite isolated rank.  A statement after the full-line limit additionally
requires convergence of the heated coordinates; nonvanishing of (9.3) alone
does not justify that limit.

Thus heat supplies a legitimate regularized family for every fixed
`epsilon,t,s`.  It does not alter the algebra in Sections 3--5:

```text
the ideal bilinear CCM bulk remains phase blind;
the ideal Hermitian CCM bulk still loses s;
the desired matrix signal still requires Gcal.      (9.4)
```

Moreover, the bound in (9.2) grows like a Gaussian in the phase box.  A
five-variable mean cannot be passed by an absolute bound uniform in `T`.
Choosing `epsilon` as a function of `T` changes the spectral weight before
the mean, while removing `epsilon` afterward returns the same
finite-to-infinite heat/determinant convergence already isolated in
E101.036--E101.041.

Heat regularization is therefore retained as infrastructure only.  It is not
the force-bearing identity.

If the graph signal were independently constructed, the legitimate order
would be

```text
fix epsilon>0 and a finite spectral cutoff;
establish the exact CCM and border identities;
take the five phase-box limits defining the means;
remove the spectral cutoff using epsilon-summability;
then let epsilon decrease to zero using a separately proved unheated
convergence theorem.                                (9.5)
```

Without the graph signal, (9.5) merely regularizes mixed pairs and does not
make their labels equal.

## 10. Cross terms diverge without the graph lift

Suppose one forms products of aggregated translated signals before the graph
pairing is available.  A typical mixed pair `(p,q)` contains an exponential
factor whose modulus has the form

```text
exp({s[Re p-Re q]+t[Im q-Im p]}/2).                (10.1)
```

Unless both real and imaginary coordinates match, one of the phase-box
directions makes (10.1) grow exponentially.  Hence the rectangular invariant
mean is not absolutely convergent.

If the bounded same-p matrix signal (5.3d) were available, E101.079 would replace
these cross terms by five sinc kernels and retain only exact coordinate
equalities.  Without (5.3d), phase averaging cannot be used to manufacture
the bounded signal from the exploding aggregate.  That would reverse the
logical order of the diagonal theorem.

## 11. Relation to the terminal and divisor walls

There are now three algebraic, zero-adapted realizations of the same missing
object:

```text
spectral graph:
  Gcal=sum_p Y_p tensor [conj(R_p)R_p^T];

divisor current:
  (2pi)^(-1)Delta log|Xi| with the pole atom attached;

finite terminal form:
  an isolated delta M_Q passed through the multirow dual compound.
                                                               (11.1)
```

The first uses the same-p conjugate tensor, the second uses the complete divisor
potential, and the third requires the quartet to be labelled before the
terminal identity collapses its isolated rank-four response to a rank-one
residual.  None is currently produced by the aggregated Gamma--Euler CCM
matrix.

E101.084 further shows that every compound formed after that collapse is
affine in the sampled boundary vector, while its normalized squared norm is
a constant plus the sampled DIRECTIONAL-IDENT energy.  The terminal form is
therefore not an independent fourth construction of the graph.

Consequently, a valid complex-translation continuation must prove an identity
of the form

```text
contracted Gamma--Euler six-current
=five-phase contraction of Gcal                     (11.2)
```

without constructing `Gcal` from zero data.  Merely writing (1.3a), (5.1),
(5.3d), or the Poincare--Lelong current is zero-adapted and does not count.

## 12. Literature and nonduplication gate

Complex translations, ambiguity functions, complex covariance and
phase-retrieval lifts already use the general principle that conjugate
measurements recover a two-dimensional phase.  These antecedents show why
conjugation data are essential; they do not produce the CCM same-p tensor.

The recent CCM determinant construction supplies selfadjoint finite spectra
and real-zero approximants, not the nonholomorphic graph (5.1) of the Riemann
divisor.  The recent screw-function realization remains a one-level Weil
form.  Higher-correlation and ratios formulas either assume conjectural input
or control density/asymptotics rather than the exact same-p graph.

Primary references already audited in E101.076--E101.079 include:

```text
Liehr:
  https://arxiv.org/abs/2308.05722

Wellershoff:
  https://arxiv.org/abs/2202.03733

Connes--Consani--Moscovici:
  https://arxiv.org/abs/2511.22755

Suzuki:
  https://arxiv.org/abs/2606.09096

Conrey--Snaith:
  https://arxiv.org/abs/0803.2795

Lagarias--Rodgers:
  https://arxiv.org/abs/1905.12123

Jaming:
  https://doi.org/10.1007/BF01259373

Picinbono:
  https://doi.org/10.1109/78.539051

Candes--Strohmer--Voroninski:
  https://arxiv.org/abs/1109.4499

Thomas:
  https://arxiv.org/abs/1309.1275                  (12.1)
```

No inspected primary source constructs (1.3a), or its required contraction,
arithmetically from the one-level Gamma--Euler CCM aggregate.  The only
potentially new content here is that source-specific construction and the
exact transverse-phase cancellation in the ideal CCM bulk.  No novelty is
claimed for complex translation, Hermitian lifting, polarization, or
character orthogonality themselves.

## 13. Stop rule and exact next target

The following routes are frozen:

```text
bilinear opposite translations;
Hermitian pairing of the original CCM aggregate;
discarding the conjugation p -> conj p in (4.2);
finite Fourier translation without the exact border term;
unregularized transverse means outside the source strip;
heat regularization presented as creation of the graph lift;
averaging exploding aggregate cross terms before bounded signal formation.
                                                               (13.1)
```

Further work is justified only by one of:

```text
GRAPH-GAMMA-EULER:
  derive the contracted value of (1.3a) from the complete signed
  Gamma--Euler source before aggregation;

GRAPH-BORDER-CANCELLATION:
  prove that the six-linear combination of the exact borders in (6.4)
  creates the graph contraction while all mixed labels cancel;

WEIGHTED-JET-POTENTIAL-CONVERGENCE:
  prove E101.079(8.2) directly from the signed source, accepting that this
  is the force-RH step rather than a character bypass.               (13.2)
```

No exact antecedent for the first two source-specific targets was located.
They may not use `Gcal`, `M_graph`, `log|Xi|`, `Xi'/Xi`, or spectral
projectors on the hypothesis side.

E101.081 subsequently closes the universal finite, bounded and polynomial
version of `GRAPH-BORDER-CANCELLATION` under continuously variable controlled
positions and independent strengths.  Linear border extraction remains
holomorphic or harmonic, exact cancellation of all controlled mixed labels
forces affine dependence, and finite transverse mean-admissibility forces
loss of the transverse parameter.  This does not exclude a finite identity
specific to the Xi divisor.  E101.082 also separates the one-trace
holomorphic diagonal, which is available by convolution, from the mixed
conjugate bidegrees which remain open.  Thus (13.2) is retained only through
`MIXED-BIDEGREE-GAMMA-EULER`, `MATCHED-EVENT-TRANSPORT`, or a singular
cofinal diagonal pullback.

## 14. Status

```text
proved:
  exact atomwise two-coordinate character under same-p conjugation;
  phase blindness of the ideal bilinear CCM bulk;
  exact loss of the transverse phase in the ideal Hermitian CCM bulk;
  identification of the missing same-p conjugate tensor;
  positive orbit-invariant full-jet weight;
  exact finite translation border term;
  exponential finite-section conditioning;
  fixed-strip obstruction to the unregularized five-phase mean;
  heat-regularized norm bound;

closed as circular or insufficient:
  inserting same-p conjugation by hand;
  ordinary complex translation of the CCM aggregate;
  heat regularization without a graph identity;

refined open targets:
  MIXED-BIDEGREE-GAMMA-EULER;
  MATCHED-EVENT-TRANSPORT;
  SINGULAR-DIAGONAL-PULLBACK;

still open:
  BOUNDED-ORBIT-CHARACTER-LIFT;
  DIRECTIONAL-IDENT;
  Omega7.
```
