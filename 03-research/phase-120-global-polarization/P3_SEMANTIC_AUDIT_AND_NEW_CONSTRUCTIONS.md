# Phase 120 — semantic complement of phases 1--120 and new constructions for row (d)

## Status

This is a design document, not a proof of row (d).  It records a semantic
search of the complete local corpus and proposes only mechanisms whose defining
vocabulary has zero occurrences in that corpus.  Lexical absence is not treated
as sufficient: candidates are also compared with the nearest existing no-go by
mathematical function.  Paper 42 is not modified.

The exact target remains

\[
 B_{\rm nuc}(f,f)\leq 0,
 \qquad \widehat f(0)=\widehat f(1)=0.                 \tag{0.1}
\]

Any successful construction below must be defined from rows (a)--(c) before
using the sign in (0.1), and must then identify its independently obtained
pairing with the row-(c) pairing.

**Correction.**  The initial version omitted G-125.B (Babaee--Huh) and T2
(non-continuity of signatures), and overclaimed what discrete Morse theory
would supply.  The corrected carrier, persistence mechanism and strengthened
gate are in `P3_G125_T2_AHK_CORRECTION.md`.  That document supersedes the
sign and cofinal claims in sections 2.2, 3.2, 3.3, 3.4 and 6 below.

## 1. Coverage and search rule

The search covered all 120 directories `03-research/phase-*`, comprising 3703
Markdown/TeX files, and the paper directories.  It used the consolidated
semantic audits for phases 1--25, 26--50, 51--75, 76--89 and 90--101, the
category/consolidated audits, and the phase conclusions for 102--120.  The
late row-(d) operator and geometry ledgers were then checked directly.

The following mechanism families are already present and are excluded even
when a new name could be attached to them:

1. Weil/operator positivity, Krein/Pontryagin, Herglotz, de Branges and
   canonical-system realizations;
2. Douglas/Schur/KYP/storage, colligations, scattering and Julia operators;
3. per-prime contact Grams, graphs, Cheeger/Poincare estimates, expanders and
   finite-channel sums of squares;
4. spectral divisors, Fredholm/index/Maslov/APS objects and zero-selected
   cohomology;
5. Arakelov heights, arithmetic Hodge index and theta/Rallis/Kudla mechanisms
   whose spectral parameter collapses to central-value data;
6. determinant/Fredholm/covolume/cross-effect/Fock packages whose virtual
   signed object exists but whose effectivity is row (d);
7. local prismatic or p-adic cohomology, KK/KMS/Bost--Connes, reflection
   positivity, modular/Lindblad/Doob, superconnections, tropical
   Monge--Ampere, total positivity and matroid Hodge packages;
8. the analytic families already exhausted in phases 102--106 (Li,
   Laguerre, Fejer, moment, Riccati, Markov/martingale, entropy/pressure,
   renewal, Blaschke/Poisson and prime-gap estimates).

Exact zero-hit checks were obtained for the following terms and their natural
variants:

```text
configuration category, configuration space, Ran space,
factorization algebra, factorization coalgebra, factorization homology,
discrete Morse, Morse matching, acyclic matching, matching complex,
higher Chow, Bloch group, Deligne regulator, Beilinson regulator,
Bridgeland stability, Harder--Narasimhan, Hall algebra,
microlocal sheaf, microsupport, characteristic cycle, Kashiwara index.
```

The zero-hit list produces three surviving constructions below.  It also
produces two false novelties that are rejected in section 5.

## 2. Candidate A — the arithmetic configuration surface

### 2.1 New object

Replace the formal square of divisor labels by a compactified space of actual
two-point configurations.  For a support window (I_T=[-T,T]), let

\[
 \overline{\operatorname{Conf}}^{\rm ar}_2(I_T)
\]

be a weighted Fulton--MacPherson-type compactification with the following
boundary colours:

* a collision colour ((p,k)) at relative displacement (k\log p), carrying
  the already constructed Witt contact line and its metric
  (w_{p^k}=(\log p)p^{-k/2});
* a continuous boundary colour (r>0), carrying the quarter-shift Gamma
  density from row (c);
* two outer faces carrying the two Tate degree characters.

The object is not the direct sum of these faces.  The compactification glues
them along nested collision strata.  In particular the strata for (p^i),
(p^j) and (p^{i+j}) meet according to the literal Frobenius composition
(\Gamma_{p^i}\Gamma_{p^j}=\Gamma_{p^{i+j}}).  Mixed-prime strata meet in the
interior but have no arithmetic collision residue, reflecting
(\Lambda(p^iq^j)=0) for (p\ne q).

Rows (a)--(b) should define a factorization cosheaf
(\mathscr F_T) on this compactification.  Its stalk on a collision stratum is
the derived Witt contact complex, its outer-face stalk is the periodic section
complex, and its gluing maps are the composition maps already proved in row
(b).  Define

\[
 H^i_{\rm conf}(D):=
 \mathbb H^i\!\left(
 \overline{\operatorname{Conf}}^{\rm ar}_2(I_T),
 \mathscr F_T(D)\right).                              \tag{2.1}
\]

The important type change is that (D) is a coefficient of a sheaf on a
two-dimensional configuration object; it is not itself a section.  Thus the
scale-invariance obstruction O1 does not apply.

### 2.2 The new theorem required

The proposed **configuration-square Riemann--Roch theorem** is the conjunction
of

\[
 \chi_{\rm conf}(nD)
 =\frac{n^2}{2}q_{\rm conf}(D,D)+O_D(n),               \tag{2.2}
\]

Verdier duality

\[
 H^2_{\rm conf}(D)\simeq H^0_{\rm conf}(-D)^\vee,     \tag{2.3}
\]

and the primitive cancellation estimate

\[
 h^0_{\rm conf}(nD)+h^0_{\rm conf}(-nD)=O_D(n)
 \quad\text{if }\deg_+(D)=\deg_-(D)=0.                \tag{2.4}
\]

Equation (2.4) is to be proved geometrically: the (n^2) interior
configuration cells factor through the one-particle charge, hence cancel when
both Tate charges vanish; only collision and outer-boundary cells, whose count
is linear in (n), survive.  This is the precise claim that has to be proved,
not assumed as a scalar property.

The trace comparison to be proved only after (2.1)--(2.4) is

\[
 q_{\rm conf}(D_f,D_g)=B_{\rm nuc,T}(f,g).             \tag{2.5}
\]

Then the already proved mixed-section forcing theorem gives finite-window row
(d), and compatibility of configuration compactifications gives the cofinal
limit.

### 2.3 Why it is not D.136--D.138

D.136 takes the trace of a graph profunctor; its fixed locus is an entire
circle and its mixed cross-effect is zero.  Here the primary object is the
compactified *two-point incidence space*, and the arithmetic contact is a
boundary orientation supplied by row (b), not a fixed-point trace.  D.137--138
construct a virtual determinant from the already known signed feature form;
here the cohomology and its effective filtration are defined before a metric
cross-effect is taken.  The proposed source of sign is the cancellation of
interior configuration cells plus Verdier duality, not a positive part of the
Fredholm defect.

### 2.4 First death gate

Use (S=\{2,3,4\}), the first threshold beyond the certified two-contact
case.  Construct the boundary poset without evaluating (B_{\rm nuc}).  It
must simultaneously satisfy

\[
 C_2\circ C_2\longrightarrow C_4,
 \qquad
 \operatorname{Res}(C_2\circ C_3)=0                  \tag{2.6}
\]

at that threshold, and its outer-boundary trace must equal the forced Gamma
compression with no fitted constant.  Failure of either equality kills the
candidate.  Passing this gate would be genuinely informative because neither
relation is built into a generic configuration compactification.

## 3. Candidate B — the prime--Gamma arithmetic Morse complex

### 3.1 New object

Construct a chain complex whose cells are finite coloured configurations of
prime-power and continuous Gamma contacts, rather than factorizing the target
operator.  The colours and weights come from rows (a)--(c).  The boundary has
two operations:

1. split a same-prime collision
   ((p,i+j)\mapsto((p,i),(p,j))), using Frobenius composition;
2. move a collision to the continuous boundary, using the row-(c) Tate/Gamma
   gluing map.

Mixed-prime mergers occur as combinatorial faces but carry zero residue.  The
associativity of row (b), together with the boundary orientation, is required
to prove (\partial^2=0) before any quadratic form is computed.

For a primitive test class (D_f), denote the resulting Hilbert chain complex
by

\[
 \mathcal M_T(D_f):
 C^0_T(D_f)\xrightarrow{\partial_0}
 C^1_T(D_f)\xrightarrow{\partial_1}C^2_T(D_f).         \tag{3.1}
\]

The new desired identity is an index formula, not a Douglas factorization:

\[
 B_{\rm nuc,T}(f,g)
 =\langle P_0f,P_0g\rangle
  -\langle P_1f,P_1g\rangle
  +\langle P_2f,P_2g\rangle,                          \tag{3.2}
\]

where the (P_i) are the independently defined cellular incidence maps of
(3.1).

### 3.2 Sign mechanism

Define a deterministic acyclic matching on the cells by the first unresolved
collision in the order

\[
 (p,k)<(q,j)quad\Longleftrightarrow\quad
 k\log p<j\log q,
\]

with the continuous Gamma colour filling the gaps.  The theorem to prove is
that on the two-Tate primitive sector this matching pairs every even cell and
leaves only degree-one critical cells.  Weighted discrete Morse reduction
would then give

\[
 B_{\rm nuc,T}(f,f)=-\|P^{\rm crit}_1 f\|^2\le0.       \tag{3.3}
\]

The matching rule uses only contact labels, Frobenius composition and the two
Tate augmentations.  It cannot inspect the sign or spectrum of
(B_{\rm nuc,T}).

### 3.3 Why it escapes the old SOS/graph no-go

The old graph forms are one-particle, fixed-cutoff Dirichlet energies and have
zero Cheeger constant.  The cells of (3.1) are configurations of arbitrary
collision depth; its differential mixes depths through
(p^ip^j=p^{i+j}) and mixes the finite and Gamma faces.  The proposed
positivity comes from an exact cancellation of chain groups, not a uniform
Poincare gap.  It therefore does not contradict D.120's amenability audit.

### 3.4 First death gate

Again use (S=\{2,3,4\}).  Before comparing with a matrix, verify

* (\partial^2=0) on the (2,2,4) fusion cell;
* the (2,3) mixed face cancels although the contact (6) is not active;
* the unmatched degree-one cell has the forced Gamma boundary coefficient.

Only then compute (3.2).  A defect in any of these three exact identities
kills the construction.  No numerical positivity test can repair it.

## 4. Candidate C — moving higher-Chow regulator cycles

### 4.1 New object

On the bi-relative arithmetic surface

\[
 ((\mathbb G_m)^2;\{0,\infty\}\times\mathbb G_m,
                    \mathbb G_m\times\{0,\infty\}),
\]

form moving graph cycles (Z_{p^k}) for the Witt/Frobenius correspondences
and complete their finite linear combinations with the test-function
coefficients.  The finite-place boundary map is required to be the tame
symbol, so its metrized degree is (\log p).  At infinity use a Deligne
regulator current with a Mellin local system (\mathcal L_\tau), not a
derivative evaluated only at the centre.  Thus the spectral variable (\tau)
is an internal monodromy parameter of the coefficient system.

The desired independently defined biextension pairing is

\[
 \langle Z_f,Z_g\rangle_{\rm reg,T},                  \tag{4.1}
\]

and the comparison target is

\[
 \langle Z_f,Z_g\rangle_{\rm reg,T}
 =B_{\rm nuc,T}(f,g).                                 \tag{4.2}
\]

The hoped-for sign would come from a new Hodge-index theorem for the
primitive part of these *moving regulator cycles*, not from the
Faltings--Hriljac height pairing.

### 4.2 What would make this different from phase 15

Phase 15 proves that a fixed arithmetic surface and its Mordell--Weil height
see central special values, not the distribution of zeros.  Candidate C
survives that objection only if (\mathcal L_\tau) remains nonconstant after
the regulator pairing and its local Fourier transform is exactly

\[
 \log\pi-\operatorname{Re}\psi(1/4+i\tau/2).          \tag{4.3}
\]

If the construction evaluates or differentiates at a single central
parameter, it is not a candidate and is immediately retired.

### 4.3 First death gate

Compute (4.1) for one graph cycle (Z_p) and one general Mellin local system,
before summing over primes.  It must yield both

\[
 (\log p)p^{-k/2}
 \quad\text{and the nonconstant multiplier (4.3)}      \tag{4.4}
\]

from the same normalization.  If it yields a height, a derivative at the
centre, or a block-diagonal prime pairing with no forced Green term, phase 15
applies and Candidate C dies.  This is the highest-risk of the three
candidates.

## 5. Zero-hit ideas rejected semantically

### 5.1 Bridgeland/Harder--Narasimhan/Hall package

The words are absent, but the standard support property requires a quadratic
form that is negative on the kernel of the central charge.  With the two Tate
degrees as central charge, that kernel is precisely the primitive space.  If
the support form is chosen as (B_{\rm nuc}), row (d) has been inserted as an
axiom; if another positive reference form is used, identifying it with
(B_{\rm nuc}) is the same missing intertwining as Douglas.  It is therefore
not pursued.

### 5.2 Microlocal sheaves/characteristic cycles

The vocabulary is absent, but a sheaf on the scaling flow whose Stokes or
characteristic-cycle data realize the Gamma scattering matrix is semantically
the phase-64/canonical-system construction.  Positivity of its transfer object
is free and realization of the exact zeta kernel is the old Floor theorem.
It is not pursued unless an actual configuration surface first exists; in
that event microlocal methods could be a proof tool for Candidate A, not a
fourth route.

## 6. Priority and work order

The candidates are ranked by how directly they address the missing type of
object rather than merely the target inequality:

| rank | candidate | genuinely new carrier | independent sign mechanism | main risk |
|---:|---|---|---|---|
| 1 | arithmetic configuration surface | two-point compactification plus factorization cosheaf | RR + primitive interior cancellation | constructing the arithmetic boundary orientation and proving (2.4) |
| 2 | prime--Gamma Morse complex | weighted collision configurations | acyclic matching leaves only degree one | (\partial^2=0) across discrete/continuous boundary |
| 3 | moving regulator cycles | bi-relative cycles with Mellin local systems | new regulator Hodge index | collapse to central-value height theory |

Candidate A is the recommended attack.  Candidate B is not merely a rival:
if its boundary poset agrees with Candidate A's first finite compactification,
it supplies a concrete proof engine for the primitive cancellation estimate
(2.4).  The first construction task is therefore one finite object, not an
open-ended theory:

\[
 \boxed{
 \text{build the }\{2,3,4\}\text{ configuration boundary complex and prove
 (2.6) plus }\partial^2=0.}                            \tag{6.1}
\]

Success at (6.1) would produce an object that was not defined by the Weil
form, escapes the fixed-trace and fixed-cutoff graph no-goes, and has a
nontrivial exact comparison waiting in row (c).  Failure would retire both A
and B cheaply and leave the moving-regulator construction as the only survivor
of this semantic complement.

## 7. Honest boundary of the claim

The audit establishes novelty relative to this corpus, not priority in the
world literature.  No claim that (2.2)--(2.5), (3.2)--(3.3), or the regulator
Hodge theorem is presently proved is made here.  Their value is that each is
a typed construction with an independent source of sign and an exact death
gate, rather than another name for the positive square whose existence is
equivalent to row (d).
