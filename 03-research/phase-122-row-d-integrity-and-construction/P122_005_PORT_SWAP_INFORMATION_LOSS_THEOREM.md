# P122.005 — port-swap information-loss theorem

## Purpose

Phase 121 isolates the missing quantity in the antisymmetric causal port,
while row C ends in a scalar nuclear character.  This note proves that an
antisymmetric equality-state law cannot be reconstructed functorially from
port-blind scalar data.  It identifies a necessary feature of any genuine
D construction.

## Abstract theorem

Let `V` be a complex vector space and let

\[
 \sigma(x_+,x_-)=(x_-,x_+)
\]

act on `V direct-sum V`.  Let `Q` be any observation which factors through
the orbit quotient by `sigma`.  Suppose `a:V direct-sum V -> W` is linear
and antisymmetric:

\[
 a\circ\sigma=-a.                                    \tag{1.1}
\]

There is no map `b` on the quotient data with `a=b circle Q`, unless `a=0`.

### Proof

If `a=b circle Q`, then `Q circle sigma=Q` gives

\[
 a\circ\sigma=b\circ Q\circ\sigma=b\circ Q=a.
\]

Together with (1.1), this gives `a=-a`, hence `a=0` over the complex
numbers.  QED.

The same proof applies to a natural transformation on a category with a
port-swap automorphism: a transformation out of the coinvariant/scalar
quotient is invariant and cannot recover a nonzero sign representation.

## Application to the phase-121 defect

At a simple critical zero, the two frozen normal jets have coefficients

\[
 (-K_F(i\gamma),+K_F(i\gamma)).                       \tag{2.1}
\]

Their symmetric scalar component is zero, while their antisymmetric
component is `2K_F(i gamma)`.  The normalized negative-half trace is the
positive square of this antisymmetric component:

\[
 8\pi |K_F(i\gamma)|^2.                               \tag{2.2}
\]

The local conormal model `E(z)=z`, `K(z)=c` realizes (2.1) for every
`c in C`, while preserving Real covariance and zero symmetric scalar
supertrace.  Hence the antisymmetric coordinate is not identically zero on
the pre-scalar local category.  By the abstract theorem it cannot be
recovered from the scalar quotient alone.

## Consequence for A/B/C

Row C's scalar character correctly remembers the sum needed for the
explicit formula.  But after passing to that scalar observation, a theorem
natural under exchange of the two causal orientations cannot force the
antisymmetric residue to vanish.  The equality equation

\[
 P_T\mathscr A_TF=0
\]

is itself scalar and port-swap invariant.  Therefore an implication from
that equation to oriented residue cancellation requires an additional
lift of the equality state which is **not determined by the row-C scalar
data**.

This does not prove row D impossible.  It proves that D must contain a
source-defined orientation-breaking datum and a compatibility theorem
before supertrace.  Choosing such a lift only on equality states would be
circular, because its compatibility is precisely F2.

## Falsifier for proposed D objects

A proposed D fails immediately if:

1. its input factors through `I_Delta^nuc` or `B_nuc` alone;
2. its construction is natural under causal port swap;
3. its conclusion is nonzero antisymmetric residue cancellation.

To survive, it must identify a pre-scalar operation already present on all
source objects, show that this operation distinguishes the two ports, and
prove its equality-state compatibility without using positivity of
`B_nuc`.
