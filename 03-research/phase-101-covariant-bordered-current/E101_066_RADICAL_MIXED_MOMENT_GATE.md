# E101.066 - Radical mixed-moment gate and the shifted-source obstruction

## 1. Decision point

E101.065 proves that the zeroth source-adapted Abel pairing is exactly the
terminal secant.  A possible way to add information is to organize all radial
shifts of that pairing into a block-Hankel system and seek a finite
biorthogonal concomitant.

This document performs the necessary gate before promoting that route:

```text
the raw shifted hierarchy is not implied by the radical identity;
it is false in the universal finite algebra;
the corrected shifted hierarchy is exact but reversible.               (1.1)
```

The only potentially new theorem is therefore an arithmetic, source-specific
backward relation which recovers the zeroth pairing from independently
controlled higher moments and has a nonzero inserted-quartet defect.

## 2. Block-Hankel coordinate

Assume first that the symbol is odd and the exterior source is even.  In the
notation of E101.060, write the parity-reduced coupled integrand as

```text
P_A(t)=A^+(t)-A^-(t)=sum_(r=0)^R a_r t^r,
P_B(t)=B^+(t)+B^-(t)=sum_(r=0)^R b_r t^r.           (2.1)
```

Let `C,D` be finite polynomials vanishing at zero.  More generally, the same
formulas hold when

```text
integral_0^1[|C(t)|+|D(t)|]dt/t<infinity.           (2.2)
```

Vanishing at zero alone is not sufficient for this abstract integral
condition.  The analytic source polynomials of E101.060 satisfy it.  Define

```text
mu_k^C=integral_0^1 t^(k-1)C(t)dt,
mu_k^D=integral_0^1 t^(k-1)D(t)dt,
k>=0.                                               (2.3)
```

For `m>=0`, put

```text
I_m=1/pi integral_0^1 t^(m-1)
                    [P_A(t)C(t)-P_B(t)D(t)]dt.      (2.4)
```

Then

```text
I_m=1/pi sum_(r=0)^R
             [a_r mu_(m+r)^C-b_r mu_(m+r)^D].      (2.5)
```

For `0<=m<=K`, define the Hankel blocks

```text
(H_C)_(m,r)=mu_(m+r)^C,
(H_D)_(m,r)=mu_(m+r)^D.                             (2.6)
```

Equation (2.5) becomes

```text
(I_0,...,I_K)^T
=1/pi [H_C  -H_D](a_0,...,a_R,b_0,...,b_R)^T.      (2.7)
```

This organization is exact and permits large individual dual polynomials.
It does not assert any orthogonality.  Without the parity assumptions there
are four blocks, one for each pair `(A^+,C^+)`, `(B^+,D^+)`,
`(A^-,C^-)`, `(B^-,D^-)`; the argument below applies channel by channel.

## 3. One-face shifted formula

Retain the lattice notation of E101.060 and consider the positive face.  Let

```text
V_z(d)=p_z(D_r-dI)^(-1)1_r.                         (3.1)
```

For a finitely supported coefficient sequence `c_j`, define

```text
I_m^+(c)
=1/pi sum_(r,j)
  c_j p_tilde_(N-r)[s_(N-r)-s_(N+j)]/(r+j+m),      (3.2)
```

where `p_tilde=p_z/b`.  The case `m=0` is the positive exterior pairing.

### Theorem 3.1 - Shifted-source obstruction

For every `m>=0`,

```text
I_m^+(c)
=sum_j c_j p_zm(d_(N+j+m))/b
 -a sum_j c_j[s_(N+j+m)-s_(N+j)]
                  V_z(d_(N+j+m))/b.                (3.3)
```

### Proof

The lattice difference is

```text
d_(N-r)-d_(N+j+m)=-h(r+j+m),
a/h=1/pi.                                           (3.4)
```

Split the numerator in (3.2) as

```text
s_(N-r)-s_(N+j)
=[s_(N-r)-s_(N+j+m)]
 +[s_(N+j+m)-s_(N+j)].                              (3.5)
```

The external-column transfer formula applied at `d_(N+j+m)` converts the
first bracket into the first term of (3.3).  Equation (3.1), with (3.4),
converts the second bracket into the second term, including its sign. `QED`

Thus multiplication of the Abel integrand by `t^m` does not keep the same
radical source.  It moves the source to different lattice columns and adds a
symbol-increment correction.  Moving the test instead produces the adjoint
correction together with interior terms.  Neither operation follows from the
single equation for the original source.

## 4. Exact finite falsifier

The family in E101.061 has row nodes `(-1,0,1)`, column nodes
`(-1,0,1,2)`, symbol

```text
s(x)=pi(7x-x^3)/6,                                  (4.1)
```

and an exact normalized kernel `y_delta` satisfying

```text
M_delta y_delta=0.                                  (4.2)
```

Use the positive right-border coordinate which appears as the `j=1` term in
the symmetric convention of E101.060:

```text
C^+(t)=3t/2,
D^+(t)=3pi t/2.                                     (4.3)
```

### Proposition 4.1

For every `m>=0`, the raw shifted pairing is

```text
I_m^+
=-3/(2b)[p_0/(m+2)+2p_(-1)/(m+3)].                 (4.4)
```

If

```text
P=p_(-1)+p_1,                                       (4.5)
```

then the coefficient of the singular mode `P` in (4.4) is

```text
-m/[2b(m+2)(m+3)].                                  (4.6)
```

Consequently the singular mode cancels at `m=0`, while for every `m>=1`

```text
|I_m^+| is comparable to 1/|delta|                  (4.7)
```

along the family.

### Proof

Insert (4.3), the one-face polynomials `A^+,B^+` from E101.060(2.1), and the
explicit dual row of E101.061 into (2.4).
The elementary moments

```text
integral_0^1 t^(m+r)dt=1/(m+r+1)                   (4.8)
```

give (4.4).  Decompose `p_(-1)` into its even and odd row modes.  The even
coefficient simplifies to (4.6).  E101.061(5.3)--(5.4) gives
`P` comparable to `1/delta`, while the odd mode remains bounded.  This proves
(4.7). `QED`

The `j=1` term is the selected right-border column rather than a member of the
actual positive exterior `T_N` from E101.065.  Thus the example falsifies raw
mixed orthogonality as a consequence of universal finite displacement, the
dual equation and exact kernel membership.  It does not by itself falsify an
arithmetic source-specific statement on the true exterior.

There is also a direct two-node independence witness.  At `delta=1` and
`z=i`, define

```text
F_m(j)=1/pi integral_0^1 t^(j+m-1)
                   [P_A(t)-s(1+j)P_B(t)]dt.         (4.9)
```

Direct substitution gives

```text
F_0(1)=-52/25-(64/25)i,
F_1(1)=-326/225-(382/225)i,

F_0(2)=452/225+(364/225)i,
F_1(2)=106/75+(92/75)i,                             (4.10)
```

and

```text
F_0(1)F_1(2)-F_0(2)F_1(1)
=6152/16875-(21008/50625)i!=0.                      (4.11)
```

Choosing two source coefficients proportional to
`(F_0(2),-F_0(1))` annihilates the zeroth pairing but not the first.  Hence
one scalar cancellation imposes no shifted hierarchy for freely chosen
finite sources.  This witness is not asserted to be the Riemann radical.

## 5. Corrected hierarchy is reversible

Equation (3.3) provides a corrected shifted hierarchy, but every row contains
the shifted source action and its exact symbol increment.  The shifted source
is not radical.  One may either use its ordinary residual decomposition, or
move the shift to the test and apply the original radical with all adjoint
symbol and interior corrections retained.  Reversing either construction
recovers (3.3).

Therefore

```text
raw block-Hankel orthogonality:       false universally;
corrected block-Hankel transport:     exact but reversible.             (5.1)
```

Neither statement is a proof mechanism for the zeroth terminal secant.

## 6. The non-circular arithmetic target

The surviving possibility is not to assume `I_0->0` as the first row of a
moment system.  It is to derive an independent backward relation from the
full arithmetic source.

Define the proposed package as follows.  The name is only a target label; no
semiclassical Pearson equation has been derived.

```text
RADICAL-SOURCE-BACKSHIFT:

RSB-1  construct, from the complete Gamma--Euler source before selecting
       p_(N,z), source-only coefficients gamma_(N,m), 1<=m<=K_N, together
       with linear functionals Bdry_N(phi) and Quartet_N(phi) on a fixed
       admissible test module;

RSB-2  prove for every test in that module the identity

       I_0(phi)=Bdry_N(phi)
        +sum_(m=1)^(K_N)gamma_(N,m)I_m(phi)
        +Quartet_N(phi);                                                (6.1)

RSB-3  derive (6.1) from the explicit formula, the full radical and the
       moving symbol increments in (3.3), not from I_0 itself;

RSB-4  give Bdry_N an explicit endpoint, border and shell formula which
       contains neither I_0 nor the terminal Cauchy kernel, and prove its
       decay by independently stated source estimates; control the weighted
       higher moments after the
       complete bilateral, border, shell and moving-level recombination;

RSB-5  define Quartet_N spectrally before the terminal test is selected; in
       the arithmetic build it vanishes, while in the controlled
       inserted-quartet build its limit is an explicit nonzero quartet
       evaluation for the actual selected tests.                         (6.2)
```

The objects in `RSB-1` may depend on the arithmetic source and cutoff, but not
on `p_(N,z)`, `I_0`, or a fitted safe point.  The universal identity must hold
on the fixed test module before specializing `phi` to the lifted dual row.
The explicit restriction in `RSB-4` prevents the vacuous choice
`Bdry_N=I_0`; source-first naming alone would not prevent it.

If `RSB-1`--`RSB-5` hold and the higher-moment sum tends to zero, then (6.1)
proves the terminal secant convergence by E101.065.  The implication is
one-way because the backward relation is asserted on an independently fixed
test class before the dual row is selected.

## 7. Relation to formal multiple orthogonality

The matrix in (2.7) is rectangular.  To invoke formal
multiple-orthogonality theory one must first choose an infinite moment matrix
or square truncations, a multi-index path, and normality or an appropriate
quasi-definiteness condition for the required principal blocks.  Under such
hypotheses, Gauss--Borel factorization supplies dual linear forms, recurrence
matrices and Christoffel--Darboux concomitants.  General references include

```text
Van Assche, Pade and Hermite--Pade approximation and orthogonality,
arXiv:math/0609094;

Daems--Kuijlaars, multiple orthogonal polynomials of mixed type,
arXiv:math/0511470;

Daems--Kuijlaars, a Christoffel--Darboux formula for multiple orthogonal
polynomials, arXiv:math/0402031;

Alvarez-Fernandez--Fidalgo--Manas, mixed multiple orthogonality and
Gauss--Borel factorization, arXiv:1004.3916.                           (7.1)
```

Those results begin after the moment relations, normality and factorization
have been established.  The cited sources do not derive `RSB-1`--`RSB-3`
from the CCM displacement law and the Riemann radical, and no such derivation
was found in the targeted searches used for this audit.

Within the archive, E101.051 contains two dual and two source moment towers,
and E101.060 already contains the Hilbert--Hankel kernel `1/(r+j)`.  The new
organization in (2.7) is specifically the full radial-shift hierarchy of the
two exterior Abel source channels coupled to the terminal dual coefficients.

Phases 72--73 contain adaptive mixed moments, arbitrary finite Hermite
windows and Mellin packet identities, but in different variables.  In
particular, E73.239 and E73.262 propose `EIG-COEFF`, a source-specific
eigenline orthogonality, while E73.277 already imposes source-first and
residual-slot antitautology rules.  The architecture of `RSB` therefore has a
clear precursor; its potentially new content is the right-bordered exterior
Abel backshift and the explicit quartet defect, not the general idea of
source-specific orthogonality.

The exact Abel and moment hierarchies in Phases 85--86 are further precedents:
they are reversible or too strong in their own spectral coordinate and do
not equal (2.7).  No earlier identity located in the audit uses exactly the
moments `mu_k^C,mu_k^D`, the terminal dual coefficients, the right-border
shift and the controlled quartet response together.

E101.067 tests the canonical universal realization of `RSB`, the binomial
backshift.  It gives an exact beta-product remainder but then proves that the
terminal action cancels from the proposed relation and that every fixed order
retains the singular dual mode.  Hence only a source-specific shift covariance
can advance (6.1).

E101.068 later proves the exact bilateral shifted-test covariance for every
finite linear choice and shows its radical conservation law: the complete
shifted sum moves into the boundary form without becoming smaller.  E101.069
then imports the classical Pearson--Christoffel--Geronimus skeleton.  The live
part of `RADICAL-SOURCE-BACKSHIFT` is therefore no longer formal transport;
it is the new Gamma--Euler flux estimate and controlled-build
noncancellation named `ARITHMETIC-LOEWNER-DISCRIMINANT`.

## 8. Stop rules

Abandon a proposed proof of `RADICAL-SOURCE-BACKSHIFT` immediately if any of
the following occurs:

```text
the first row is I_0->0 in disguised notation;
the coefficients gamma_(N,m) are fitted after p or z is known;
the derivation uses only pM=q and radical substitution;
the complete source is split before cancellation;
the theorem remains unchanged on the inserted-quartet build;
the argument replaces the signed moment sum by a uniform dual norm.      (8.1)
```

These conditions separate new arithmetic mathematics from another rotation
of DIRECTIONAL-IDENT.

## 9. Status

```text
proved:
  exact block-Hankel coordinate for the Abel shifts;
  exact shifted-source and symbol-increment formula;
  finite divergence of every nonzero raw shift in the symmetric falsifier;
  two-node independence of the zeroth and first pairings;

rejected:
  raw mixed orthogonality as universal finite algebra;
  corrected shifted transport as a non-reversible mechanism;

new force-bearing target:
  the proposed RADICAL-SOURCE-BACKSHIFT, whose quartet audit remains an
  explicit obligation;

open:
  RSB-1--RSB-5, DIRECTIONAL-IDENT and Omega7.
```
