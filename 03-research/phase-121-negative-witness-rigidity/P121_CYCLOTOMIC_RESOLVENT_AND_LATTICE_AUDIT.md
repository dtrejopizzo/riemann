# Phase 121 -- cyclotomic resolvent filtering and arithmetic-lattice audit

## Status

This note tests a nonlinear Euler-specific proposal at the equality state:
filter a degree-one local Euler resolvent by roots of unity, and then use
arithmetic discreteness of its parabolic monodromy to annihilate the critical
source coefficient.

The local filter is exact and retains the complete prime-power tower.  The
arithmetic-discreteness lemma is also exact.  They do **not** combine into a
proof of the global square.  The first-contact equation supplies the
untwisted scalar operator only, while the integral component of the
paper-42 gluing kills every nontrivial nuclear convolution.  Thus neither
the twisted equations nor preservation of a fixed lattice is available.

This is a typed no-go for this proposal, not a claim about row (d).

## 1. Exact cyclotomic filter on a causal Euler tower

Let `V` be a nilpotent operator, let `0<r<1`, and put

\[
 R(\omega)=(I-\omega rV)^{-1},\qquad
 A(\omega)=\omega rV(I-\omega rV)^{-1}.             \tag{1.1}
\]

For a localized prime tower one takes

\[
             V=P_TS_{\log p}P_T,\qquad r=p^{-1/2}. \tag{1.2}
\]

Nilpotence makes every expression below a finite polynomial, so no boundary
limit or convergence assertion is involved.

### Proposition 1.1 -- root-of-unity extraction

For every integer `m>=1`,

\[
 \boxed{
 {1\over m}\sum_{\omega^m=1}R(\omega)
       =(I-r^mV^m)^{-1},}                           \tag{1.3}
\]

and

\[
 \boxed{
 {1\over m}\sum_{\omega^m=1}A(\omega)
       =r^mV^m(I-r^mV^m)^{-1}.}                    \tag{1.4}
\]

#### Proof

Expand the finite geometric series.  The character orthogonality identity

\[
 {1\over m}\sum_{\omega^m=1}\omega^k
 =\begin{cases}1,&m\mid k,\\0,&m\nmid k\end{cases} \tag{1.5}
\]

retains precisely the powers `V^(mj)`.  Resumming that finite subsequence
gives (1.3) and (1.4).  QED.

Thus the filter really separates the sub-tower

\[
 p^m,p^{2m},p^{3m},\ldots                            \tag{1.6}
\]

without losing its physical weights.  In particular (1.4), multiplied by
`log p`, retains `(log p)p^(-mj/2)` exactly.  This differs from the real
norm--Tate cofiber rejected in phase 120: no finite-group cofiber is
realified, and the filtered operator is generally nonzero.

## 2. What first contact actually implies

Let `q_T` denote the nonnegative primitive form at a hypothetical first
contact, let `F` lie in its radical, and let `Pi_T` be any fixed bounded
projection onto the two-Tate primitive space.  Then

\[
                 q_T(F,G)=0\qquad(G\in\mathcal P_T). \tag{2.1}
\]

For a chosen active prime define the cyclotomic test family

\[
             G_\omega=\Pi_TR(\omega)F.              \tag{2.2}
\]

Every `G_omega` is a legitimate primitive test.  Hence

\[
 q_T(F,G_\omega)=0                                 \tag{2.3}
\]

for every root of unity, and averaging gives

\[
 q_T\left(F,\Pi_T(I-r^mV^m)^{-1}F\right)=0.        \tag{2.4}
\]

### Proposition 2.1 -- test-side cyclotomic filtering adds no law

Equations (2.3)--(2.4) are contained in (2.1).  In particular they do not
imply that the individual `p^(mj)` channel, its collar current, or its
critical conormal coefficient vanishes.

#### Proof

The map in (2.2) takes values in `P_T`; therefore (2.3) is a substitution
in (2.1).  Proposition 1.1 only evaluates the finite average of those
substitutions.  No equation for a twisted **source operator** has been
introduced.  QED.

The distinction is decisive.  Replacing the physical local connection
`A(1)` inside the Weil operator by `A(omega)` would produce genuinely new
equations and would allow Fourier inversion in the exponent `j`.  But
first contact is known only for the untwisted scalar row-(c) operator.
Twisting the test is allowed and tautological; twisting the source is a new
hypothesis.

The only global one-parameter twist induced by logarithmic translation is
the coherent family `omega_p=p^(-it)` for all primes simultaneously.  After
the two Tate corrections, phase 121's horizontal-modulation theorem proves
that testing along this family is again only (2.1).  Independent prime
phases do not descend from a character of the zeta source over `Q`.

## 3. The arithmetic-discreteness mechanism

There is nevertheless a sharp nonlinear closure lemma suggested by the
filter.  Let `N` be a fixed nonzero square-zero matrix and

\[
                         M_c=I+cN.                  \tag{3.1}
\]

### Proposition 3.1 -- a continuous radical line cannot preserve a fixed lattice

Let `L` be a full real lattice in a finite-dimensional complex vector space.
Then the subgroup

\[
 \{c\in\mathbb C:M_cL=L\}                           \tag{3.2}
\]

is discrete.  If a complex-linear functional `c_F` has the property that

\[
                         M_{c_{\lambda F}}L=L       \tag{3.3}
\]

for every `lambda in C`, then `c_F=0`.

#### Proof

The lattice stabilizer is a copy of `GL(L)` inside the real endomorphism
space and is discrete there.  Since `N!=0`, the map
`c -> I+cN` is injective and continuous, so its inverse image (3.2) is
discrete.  Complex linearity gives `c_(lambda F)=lambda c_F`.  The image of
the connected set `C` under `lambda -> lambda c_F` is connected and contains
zero.  If it lies in (3.2), it is the singleton `{0}`.  Hence `c_F=0`.  QED.

For the critical source connection of
`P121_PARABOLIC_COMMON_NILPOTENT_LIFT.md`,

\[
 c_{F,\rho}=2\pi i\,m_\rho K_F(i\gamma),            \tag{3.4}
\]

and the first-contact radical is complex linear.  Therefore preservation
of one fixed arithmetic lattice by the source monodromy for the whole
radical line would force

\[
                         K_F(i\gamma)=0              \tag{3.5}
\]

at every simple critical zero.  The already proved Cartwright descent would
then give `F=0` and close the global square.

This mechanism is not a positive lift, a contraction, or a norm estimate.
It is the incompatibility of a continuous complex scaling orbit with a
discrete arithmetic stabilizer.

## 4. Why rows (a)--(c) do not supply the premise

The premise (3.3) is not present in the current construction.  In the
intrinsic integral--real--nuclear gluing of paper 42, the arithmetic action
is explicitly typed as follows:

\[
 \rho_n^{\rm int}=0\quad\hbox{on the integral and real components for }n>1,
                                                               \tag{4.1}
\]

while its nuclear and periodic components are left convolution by
`delta_n`.  Compatibility holds because the augmentation sends

\[
                         \delta_n\longmapsto0\quad(n>1).       \tag{4.2}
\]

Consequently the nontrivial Euler directions live in the kernel of the
comparison to the integral lattice.  Their nuclear scalar extension is not
an automorphism of that lattice.  In particular the source monodromy
`I+c_(F,rho)N` is not known to preserve the free digit lattice of row (a).

This is not a missing verification of an asserted compatibility.  The
current categorical gluing was designed precisely so that the nontrivial
nuclear convolution has **zero** integral component.  Imposing (3.3) would
add a new integral lift of the equality-state conormal coefficient.  By
Proposition 3.1 that lift already has F2 force.

The same obstruction appears in the logarithmic coefficient.  Unique
factorization gives a free integral prime-label module, but the scalar
degree map evaluates its generators at `log p`.  Row (c) applies this scalar
evaluation before the first-contact equation.  Lifting a scalar cancellation
back to the free prime-label module is not injective and would repeat the
arithmetic-singularity label no-go.

## 5. Corpus comparison

The semantic audit found the following adjacent but distinct objects.

1. Phase 114, D.109 and D.237 already resum every prime tower with
   `(I-p^(-1/2)S_(log p))^(-1)`.  Proposition 1.1 acts on that exact
   resolvent; it is not a new realization of the von Mangoldt weights.
2. Phase 104 uses a roots-of-unity filter for residue classes in a
   Poissonized scalar counterexample.  It does not apply the filter to a
   localized Euler resolvent or to a first-contact radical.
3. Phase 120's cyclotomic norm--Tate no-go concerns realification of a
   finite-group Tate cofiber, which vanishes.  Proposition 1.1 survives
   realification, so that theorem does not reject it.
4. Phase 121's horizontal-modulation no-go already rejects the only coherent
   global phase family furnished by physical translation.
5. Phase 121's determinant-framing audit observes that integral residues on
   the whole radical line would force F2.  Proposition 3.1 isolates the exact
   lattice statement, while (4.1)--(4.2) show why paper 42 does not supply it.

No phase 1--120 occurrence of the combined propositions (1.1)--(1.4) and
(3.1)--(3.3) was found.  Their combination nevertheless fails at the typed
source bridge, not at an estimate.

## 6. Verdict

```text
cyclotomic extraction of every p^(mj) sub-tower       PROVED
preservation of exact von Mangoldt weights            PROVED
test-side filtered first-contact identities           PROVED, TAUTOLOGICAL
continuous-line versus discrete-lattice lemma         PROVED
fixed-lattice preservation of critical monodromy      NOT SUPPLIED
global square                                          OPEN
```

The proposal therefore cannot be used as the missing global-sign principle.
Its failure is informative: any successful nonlinear operation must act on
the physical scalar source without either (i) demanding unavailable
independent prime twists or (ii) lifting the nuclear equality state to an
integral lattice after row-(c) scalarization.
