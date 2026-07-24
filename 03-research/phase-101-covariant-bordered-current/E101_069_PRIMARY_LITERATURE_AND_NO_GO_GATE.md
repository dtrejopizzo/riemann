# E101.069 - Primary-literature and no-go gate for the shifted-moment route

## 1. Decision

The shifted-moment program must separate three layers which the literature
already distinguishes:

```text
universal polynomial or rational transport of moments;
source-specific Pearson structure;
global arithmetic convergence or positivity.                         (1.1)
```

The first layer is classical and must be imported.  The third layer contains
known RH-equivalent limits and must not be renamed as a technical estimate.
Only the middle layer can contain new mathematics for E101.068.

The source audit gives the following verdict:

```text
no primary source inspected contains the bilateral right-bordered
Gamma--Euler identity ARITHMETIC-LOEWNER-DISCRIMINANT;

the universal shift, factorization and mass-insertion mechanisms needed to
formulate it are already available and must not be redeveloped.        (1.2)
```

## 2. Pearson structure: what may be imported

Branquinho--Foulquie-Moreno--Manas study two-weight multiple orthogonality
under scalar Pearson equations

```text
(sigma w_a)'=tau_a w_a,
a=1,2,                                                (2.1)
```

with `sigma w_a` vanishing at the boundary of the support.  Their Theorem 3
turns integration by parts into a symmetry of the moment matrix; Theorem 4
conjugates that symmetry through a Gauss--Borel factorization; Proposition 8
shows that the resulting Laguerre--Freud matrix is banded; Theorem 5 gives
differential relations for the type-I forms and type-II polynomials.

The logical direction is essential:

```text
Pearson equation plus boundary cancellation
  => moment symmetry
  => finite-band Laguerre--Freud relation.            (2.2)
```

The theory does not infer (2.1) from a freely given moment array.  Therefore
the block-Hankel coordinate of E101.066 is not enough.  To use (2.2), one
must first derive an equation of Pearson strength for the complete
Gamma--Euler source, with all four channels and the selected right border.

This is exactly the part which is not present in the cited theory.  Assuming
it would assume the new theorem rather than import one.

## 3. Christoffel transport: the universal shift is known

Let `dmu` be a `q x p` rectangular matrix of measures and

```text
M=integral X^[q](x)dmu(x)X^[p](x)^T                (3.1)
```

its moment matrix.  For right multiplication by a regular matrix polynomial
`R`, Manas--Rojas, Proposition 4.1, prove

```text
Mhat=M R(Lambda^T).                                 (3.2)
```

Thus polynomial multiplication of the source is already a polynomial in the
moment shift.  Assuming Gauss--Borel factorizations for the original and
perturbed moment matrices gives the connection formulas.  Their Theorem 5.2
states that the perturbed mixed orthogonality exists exactly when the
associated determinants `tau_n` do not vanish.

Equation (3.2) is the abstract moment analogue of

```text
G_eta(U)=sum_m eta_m U^m                            (3.3)
```

in E101.067--E101.068.  It confirms that another finite polynomial in the
shift cannot be advertised as new content.  Christoffel theory transports an
already specified measure and an already specified polynomial.  It does not
produce

```text
the arithmetic radical;
the Loewner symbol commutator;
an independently small terminal boundary;
or a noncancelling inserted-quartet response.        (3.4)
```

The `tau_n!=0` condition is a normality condition for the perturbed
orthogonality, not an estimate for the scalar in E101.068(6.2).

## 4. Geronimus transport: masses are not a free quartet

For a regular matrix polynomial `R`, the general Geronimus problem reverses
the Christoffel multiplication:

```text
dmu_check(x)R(x)=dmu(x).                            (4.1)
```

Manas--Rojas represent its solutions by a rational part involving
`R(x)^(-1)` together with masses and, for multiple roots, derivative jets at
the spectrum of `R`.  The canonical scalar case already contains a free
parameter.  Their Proposition 3.4 and Theorem 3.5 give the two directions of

```text
Geronimus-perturbed orthogonality exists
  <=> tau_n!=0 for every n.                          (4.2)
```

These masses resemble a boundary or quartet term only formally.  In the
Riemann problem they cannot be adjusted after the terminal test is known.
An admissible use of Geronimus theory must derive every mass and jet from the
same Gamma--Euler rule before selecting `p_(N,z)`, and it must show how the
rule changes under the controlled quartet build.  Otherwise the free masses
can fit the missing scalar and violate the source-first condition.

Consequently, the Christoffel--Geronimus apparatus may be used as a ready
factorization theorem after the arithmetic transformation has been derived.
It cannot derive that transformation.

## 5. Finite real-rooted approximants: Connes and CCM

Connes, Theorem 6.1, assumes a real convolution distribution on a finite
interval whose quadratic form defines a lower-bounded self-adjoint operator.
If the bottom eigenvalue is simple and isolated with an even eigenfunction
`theta_x`, then every zero of `hat theta_x` is real.

Connes, Fact 6.4, proves for the explicit prolate model

```text
k_lambda=E(h_lambda)                                (5.1)
```

that

```text
hat k_lambda -> Xi                                  (5.2)
```

uniformly on closed substrips of `|Im z|<1/2`.  His remaining-step section
states two missing assertions:

```text
the bottom eigenvalue of the restricted Weil form is simple with an even
eigenfunction;

k_lambda is a sufficiently accurate approximation to theta_x.         (5.3)
```

The CCM finite theorem has the same separation.  Their Theorem 1.1 and
Theorem 5.10 construct a selfadjoint rank-one perturbation and a real-zero
entire determinant after assuming the finite minimum is simple and even.
Their Corollary 3.8 states that if the decreasing global lower bound tends to
zero, RH follows.  Their final section identifies the approximation of the
true minimum by the prolate model as the main remaining obstacle.

Hence the finite selfadjoint construction is valid infrastructure.  The
locally uniform identification with `Xi` is not infrastructure: by Hurwitz it
forces RH.  This confirms E71.016--E71.017 and rules out any proof which
imports

```text
theta_x-k_lambda->0
```

as though it were a standard perturbation estimate.

Neither Connes nor CCM supplies a Pearson relation for the four-channel Abel
source of E101.068.

## 6. Screw-function realization: Suzuki

Suzuki gives a continuous-kernel realization of the finite Weil form.
Theorem 1.1 identifies its canonical operator `A_a` as the Friedrichs
extension of

```text
B_a=D^*G_aD,                                        (6.1)
```

where `G_a` is built from the explicit screw kernel.  This is an
unconditional bilinear representation and may be imported when a continuous
kernel is preferable to the distributional form.

Theorem 1.3 proves continuity of the lowest eigenvalue.  Combined with the
known small-support positivity, this makes global nondegeneracy of every
finite Weil form equivalent to RH.  Thus global nondegeneracy is a wall, not
a lemma available for E101.068.

Theorem 1.4 proves positivity, simplicity and evenness only for sufficiently
small support.  Theorem 1.5 constructs, for every finite support and every
selfadjoint boundary parameter, an entire characteristic function

```text
W(a,theta;z)                                        (6.2)
```

whose zeros are real.  The proof uses only finiteness of the prime
contribution at fixed support and is therefore build-neutral at the point
where E101.068 needs discrimination.

Suzuki's Corollary 1.6 says that a compact-uniform limit of suitably
normalized functions (6.2) toward `z^2 xi/xi'` would imply RH.  The
motivation for that limit is developed under RH.  The limit is therefore the
force-bearing step and cannot be used to control the Loewner boundary.

Suzuki supplies a useful continuous realization but no arithmetic
shift-back relation and no quartet noncancellation theorem.

## 7. Exact hypothesis comparison

The import boundary is now explicit.

```text
available:
  Gauss--Borel factorization after principal blocks are nonsingular;
  Christoffel polynomial transport of a moment matrix;
  Geronimus rational transport with prescribed masses and jets;
  Pearson-to-Laguerre--Freud implication after a Pearson equation is known;
  finite real-zero constructions after selfadjointness and the stated
  simplicity/parity hypotheses;
  the prolate model convergence hat k_lambda->Xi;
  the screw-kernel representation of each finite Weil form;

not available:
  a Pearson equation for the complete Gamma--Euler source;
  a proof that its boundary term is small on the actual terminal tests;
  preservation of that estimate under growing binomial order;
  a build-covariant formula preventing quartet cancellation;
  convergence of the actual finite minimum to the prolate model.       (7.1)
```

The missing assertions in the second block are not interchangeable.  The
last one belongs to the Connes finite-to-infinite route.  The middle three
belong to E101.068.  Proving either complete route with the required strength
would prove RH.

## 8. New-mathematics target after the gate

For the notation of E101.068, define the complete Loewner boundary vector

```text
H_(B,N,eta)(x)
=sum_(sigma=+,-){
   D_(B,eta)^sigma P_N^sigma x
  -G_eta^sigma(U)M_B(I-P_N^sigma)x}.                (8.1)
```

Then

```text
Bcal_(B,eta)(x,phi)=phi H_(B,N,eta)(x).             (8.2)
```

Equations (8.1)--(8.2) are exact algebra, not the sought theorem.  The only
Pearson-type statement which survives the literature gate must produce,
directly from the theta/Gamma--Euler formula, a prescribed flux
`Flux_(N,eta)` and a remainder `Err_(N,eta)` such that

```text
H_(Z,N,eta)(kappa_Z)
=Delta Flux_(N,eta)+Err_(N,eta),                   (8.3)
```

with all of the following proved independently:

```text
the coefficients and flux are fixed before the terminal row;
the discrete divergence in (8.3) has an explicit bilateral right-border
evaluation after pairing with every test in the declared module;
the paired Err tends to zero without using I_0 or the terminal Cauchy kernel;
the same construction in the controlled build gives a forced quartet term;
the boundary difference cannot cancel that quartet on the actual tests. (8.4)
```

Calling (8.3) a Pearson equation is not enough.  It must be derived from the
source and satisfy (8.4).  If `Flux` or `Err` is defined from the left side of
(8.3), the assertion is tautological.  If the discrete divergence is merely
integration by parts for the Fourier coefficients of `E(h)`, it must pass the
E101.048--E101.055 coboundary audits before further work.

E101.070 performs this source audit.  A fixed scalar polynomial Pearson law
is impossible because its coefficients would have to vanish at every
interior prime-power atom.  The theta heat equation projects instead to an
infinite dense Fourier hierarchy with a nonzero endpoint flux.  Therefore
(8.3) is no longer a live scalar-Pearson target.  The only retained flux law
is the nonlocal multiplicative Gamma--Euler commutator of
E83.004--E83.007, evaluated as one signed bilateral boundary pairing.

This is narrower than the former `RSB-SHIFT`: universal polynomial transport
has been removed, normality theory has been imported, and the force is placed
only in the arithmetic flux and build discriminant.

## 9. Primary sources

```text
A. Connes,
The Riemann Hypothesis: Past, Present and a Letter Through Time,
arXiv:2602.04022;

A. Connes, C. Consani, H. Moscovici,
Zeta Spectral Triples,
arXiv:2511.22755;

M. Suzuki,
Weil's quadratic form via the screw function,
arXiv:2606.09096;

A. Branquinho, A. Foulquie-Moreno, M. Manas,
Multiple orthogonal polynomials: Pearson equations and Christoffel formulas,
arXiv:2106.12707;

M. Manas, M. Rojas,
General Christoffel Perturbations for Mixed Multiple Orthogonal Polynomials,
arXiv:2405.11630;

M. Manas, M. Rojas,
General Geronimus Perturbations for Mixed Multiple Orthogonal Polynomials,
arXiv:2411.16022.                                      (9.1)
```

## 10. Status

```text
imported and frozen:
  Pearson consequences, Christoffel shift transport, Geronimus masses,
  formal multiple-orthogonality factorization, finite real-zero mechanisms;

identified as force-bearing known limits:
  true-minimum to prolate convergence, global Weil nondegeneracy,
  compact-uniform convergence of real-zero approximants to Xi or xi/xi';

new target:
  retain the nonlocal multiplicative Gamma--Euler flux after the scalar
  Pearson obstruction of E101.070;

subsequent reduction:
  E101.071 computes the controlled quartet exactly and reduces its complete
  response to one rational exterior current;

open:
  ARITHMETIC-LOEWNER-DISCRIMINANT, UNIFORM-BETA-ENDPOINT,
  DIRECTIONAL-IDENT and Omega7.
```
