# R170_801 — Three Gates: focused audit and reusable material

Source: [Desogus, arXiv:2609.20367v1](https://arxiv.org/abs/2609.20367v1).
The requested attempt stopped due to usage limits and did
not deliver an audit. This review was done afterward, independently,
on §§6.13–6.14 and 8, reading the dependencies cited in those steps.
It is not a complete verification of the manuscript or of Arb.

## Provisional result

No claim of RH is validated here. Nor has a counterexample to its
arithmetic operator been constructed. There are correct Schur
identities and an essential transport that requires independent
checking. It is not legitimate to conflate these three states.

In addition, a window-interaction bound with a single common
complement was separately reconstructed in
[R170_805](R170_805_COMMON_COMPLEMENT_CAPACITY.md). This is the most
concrete auxiliary result salvaged in this review: its proof uses
neither the global induction nor the manuscript's certificates.

## Identities that can be reconstructed

For A=M_a−β|1><1|, with a>0, write J=∫a⁻¹ and δ=1−βJ.
If g=Ax and θ=∫x, then

    ∫g/a = δ θ.

If δ>0, the debit of its normalized scalar coordinate is

    D = δ |θ|²/J,

and, with E=∫a|x|², Cauchy–Schwarz gives |θ|²≤JE. Thus

    <x,Ax>−D = E−|θ|²/J ≥ 0.

The two-interval version of lemma 6.28 is obtained via Schur: if
I=∫_L a_-⁻¹, γ=β/(1−βI), the right block is
M_a+−γ|1_R><1_R|. Substitution checks formulas (127)–(134). Equality
requires x proportional to a⁻¹. This is valid algebra for the declared
model and under its sign hypotheses.

The evaluation of a scalar minimum is also correct:

    min_z {P|z|²−2 Re(z̄ω)} = −|ω|²/P = −P|z_min|²,  P>0.

This is the algebraic content of the response placement inherited from
lemma 8.1. Using the same metric on both sides is indispensable.

## What that algebra does NOT prove

1. **It does not give a uniform response bound as the gap closes.**
   Taking A_δ=δ, g=1 and x=1/δ satisfies g=A_δx, but the debit
   g*A_δ⁻¹g=1/δ diverges. The moment's divisibility by δ does not
   control its size if θ also depends on δ. Continuity at contact
   requires controlling the vector or specifying a form extension;
   canceling symbols is not enough. This limits an overly strong
   reading of corollary 6.29, without by itself refuting the remainder
   identity.
2. **The sign δ>0 is still a hypothesis.** Lemma 6.28 explicitly
   states Π_phys>0 to interpret the debit as a positive short. One
   must trace where it is guaranteed before the induction, without
   using the positivity one is trying to conclude.
3. **Defining a residual forcing does not identify its physical
   energy.** One can always write g=A_model x. It remains to prove
   that this g is precisely the coupling row of the complete operator,
   preserving the terms moved to the other side and their quadratic
   contribution.

## Step that needs further audit before accepting the closure

In lemma 8.4, equations (206)–(211), the two arms are represented with
the same block P and the same row b; completing the square gives twice
the debit of one arm. That completion is correct **if that form is the
actual transported form**. The earlier claim of identity between both
arms, and between the common cut and the folded cut, is not verified
by mere invariance under unitary congruence. A unitary preserves the
form, but does not force two arbitrary blocks to be equal.

The goal of a conclusive audit is to reconstruct (206) directly from
the complete form, including the polar term and the complement, and to
check the identification with the model of (124). The doubled debit of
the folded version must be distinguished from the final individual
debit. Theorem 8.5 depends on this identification to claim that no
reserve is used twice. This review does not declare that transport
proved or refuted.

## Insight worth carrying over to Paper 46

Work in the exact harmonic extension and carry source and metric
together. For a positive block B and a source g, a proposed response
x₀ has residual r=g−Bx₀ and satisfies exactly

    <g,B⁻¹g> = <x₀,Bx₀> + 2 Re<x₀,r> + <r,B⁻¹r>.

Hence an arithmetic comparator must control the residual in the
complete block's inverse metric, not just its L² norm. This identity
preserves the interaction that is lost when source, boundary, and
polar term are estimated separately. It is standard, but it specifies
a concrete missing proof: constructing x₀ from the integers and
bounding the **entire** right-hand side by the available budget. It
does not by itself supply that bound.
