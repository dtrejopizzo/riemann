# P121 -- paper 36 transfer audit

## 1. Reason for the audit

Paper 36 is the longest completed proof-chain audit in the corpus.  Its
fourteen closed links do not prove RH: they reduce the remaining input to
Step 5, and Step 5 to the all-order terminal defect

\[
 \delta_N\geq0\quad(N\geq1),
\]

equivalently Li--Keiper positivity and RH.  The relevant question for phase
121 is not whether that chain can be restarted.  It is which logical move
made its last input as hard as the original problem, and whether the
Euler--Bohr radical construction has silently repeated it.

## 2. The chain actually proved in paper 36

The proof path is:

```text
finite arithmetic source channels
 -> explicit formula in the absolutely convergent half-plane
 -> arithmetic Pick positivity for every finite source plane and node set
 -> Nevanlinna--Pick interpolation
 -> Montel/Vitali continuation
 -> removal of every nonreal pole detected by a source channel
 -> RH.
```

Every arrow after arithmetic Pick positivity is proved.  The open statement
is the positivity itself.  Paper 36 sharpens it several times:

1. all source planes can be reduced to one scalar channel;
2. all node sets can be reduced to all prefixes of one accumulating node
   sequence;
3. those prefixes can be serialized as one-point jets;
4. the jet defect is the Li--Keiper hierarchy at the boundary gauge;
5. the direct prime calculation reduces it to A0 plus the compact A1
   Chebyshev--Laguerre inequality.

A0 follows from the classical PNT remainder.  Uniform A1 remains open and
is RH-strength.  Fixed order, fixed bands, finite cutoffs and finite
certificates all close; the simultaneous all-order boundary limit does not.

## 3. The exact place where the quantifier inflated

The realization layer constructs positive finite spectral measures and
uniform source bounds.  To remove every possible off-line pole it then asks
for convergence or Pick positivity for **every** detecting source.  This is
unavoidable for that route: an off-line pole is detected by some source, not
by a source fixed in advance.

Thus paper 36 replaces

```text
one hypothetical off-line object
```

by

```text
positive continuation for every source and every finite prefix.
```

That is the master-quantifier wall of the paper.  The subsequent reductions
make it smaller syntactically, but Theorem `minimal scalar open input` proves
that even one accumulating scalar prefix family is still equivalent to RH.

The phase-121 first-loss branch has strictly more specificity.  It supplies
one particular vector `F_*` at one first window `T_*`.  Replacing that vector
by a theorem for all corona measures, all sources, or all boundary
characters would throw this advantage away and reproduce Step 5.

## 4. Boundary data are blind to the missing divisor

Paper 36 proves a second obstruction which applies directly to the current
corona formulation.  Its flag-residue identity has the form

\[
 B_n=\mathcal I_n^\partial(h)
   +\sum_{\Re\rho>1/2}
     \frac{m_\rho\mathcal F_n(w_\rho)}{\rho(\rho-1)}. \tag{4.1}
\]

A reciprocal off-line quartet leaves the real boundary symbol in
`I_n^partial` unchanged while altering the interior residue sum by the full
exponentially growing Li contribution.  In Hardy terminology, the missing
object is an inner divisor: its boundary modulus or real logarithmic
derivative does not determine its zeros.

The Euler--Bohr measure of `P121_RADICAL_DOMAIN_IDEAL_AND_CORONA.md` records
only boundary phases and positivity.  Conjugation invariance records the
Real symmetry, but no radial divisor or winding.  Consequently:

### Boundary-blindness rule

No exclusion theorem whose hypotheses factor only through

\[
 \mu\quad\hbox{on the Euler--Bohr torus},
 \qquad z_p\mapsto\overline{z_p},
\]

and real trigonometric boundary observables can be the missing theorem.  It
cannot distinguish two completed systems differing by a reciprocal inner
quartet.  A valid successor must retain a radial germ, an interior residue,
or an equivalent non-boundary datum.

This rule does not say that every measure equation is impossible.  It says
that the measure alone is an insufficient state variable.

## 5. What paper 36 already kills for phase 121

The following successors would be repetitions:

| proposed phase-121 move | paper-36 coordinate | verdict |
|---|---|---|
| positive measure whose Cauchy transform realizes the target | tower-ARP / measure bridge | requires target convergence; RH-strength |
| positivity for all corona characters | ARP-P for all channels | exact quantifier inflation |
| a fixed real boundary-symbol inequality | flag boundary term | blind to reciprocal off-line residues |
| transport from `Re s>1` to the critical boundary by a log derivative | complete phase homotopy | the flux is exactly the off-line residue sum |
| termwise use of `Lambda>=0` | whitened prime atoms | factorial loss; sign is cross-prime interference |
| pointwise PNT control | A1 partial summation | loses a factor of order `n` even with RH-size pointwise error |
| positive preconditioning or a Markov selector | A1 Cholesky/size-bias/Stein routes | optimizes back to the unknown signed moment or has zero gap |

## 6. What remains admissible

The only admissible use of the corona is **radical-only**:

```text
the specific first-loss equation for F_*
 -> a source-defined radial quantity for that same F_*
 -> a finite boundary slope / residue constraint
 -> F_* belongs to the nuclear graph domain
 -> equality-state annular gap transport would give F_*=0.
```

The quantifier must remain attached to `F_*` throughout.  No statement for
all sources or all corona measures is needed.  The radial quantity must see
more than the limiting positive phase measure.  The subsequent slope and
dyadic notes construct such a quantity, prove its exact relation to the
graph norm, and prove graph membership.  The audit after that proof shows
that co-Poisson radical lifting still needs (358)/(441); it was not already
contained in v94.

## 7. Binding lesson

Paper 36 did not fail because it lacked enough exact identities.  It failed
because it crossed from a finite/interior positive family to a uniform
all-order boundary assertion.  Phase 121 must not cross that bridge.

The new target is therefore not "exclude every Euler--Bohr measure".  It is:

> prove annular gap transport for the single graph vector generated by a
> first-loss radical.

The finite radial slope bound is now proved.  The transport statement can
still be false, but it is not the ARP-P quantifier and it has a concrete
pre-row-(d) kill condition.
