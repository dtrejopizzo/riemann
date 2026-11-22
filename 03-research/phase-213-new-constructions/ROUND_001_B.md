# Scope of the PRIME–ARCH inequality recovered from phase138

Status: documentary correction; independent review completed (PASS). It is not a new sign result.

## Antecedent and selection decision

The master index, Parts VI (registro20_02, phase138) and VII.C, lists D.15.3(★)
as «PRIME ≤ ARCH + ½deg²» under PROVED. That synthesis is checked against
`../phase-138-row-d-detecting-cones/R138_001_ROUND1.md`, §0 and D.15.3(i),(ii),(v).
No construction is opened: reading the source suffices to decide that there is
no global inequality already available to transfer to Paper46.

## Exact scope

The source works with F in D^W (Paper47, Definition11.1). It defines

    deg⁺F = ∫F(t)e^(t/2)dt,
    deg⁻F = ∫F(t)e^(−t/2)dt,
    deg F = deg⁺F + deg⁻F,
    μ(F) = deg⁺F − deg⁻F.

This degree is a moment functional, not the degree of a polynomial nor the size
of a matrix. The primitive subspace requires both moments to vanish; deg F=0 by itself
does not express that double condition.

D.15.3(i),(ii) prove unconditionally the identity of the polar block:

    ½(deg F)² − B_pol(F,F) = ½μ(F)² ≥ 0.

D.15.3(v), for h=F⋆F^∨, proves the equivalence

    I_∞(F,F) ≤ ½(deg F)²
        ⇔ PRIME(h) ≤ ARCH(h) + ½(deg F)²,

using the identity I_∞(F,F)=PRIME(h)−ARCH(h).
The PROVED label corresponds to this equivalence. It does not assert either of its
sides for all F. Annihilating the moments removes the degree term, but does not
provide the missing inequality. Nor does the slack of the polar block sign
the full form.

## Result of the cross-check

The two operational syntheses are clarified and the decision is recorded in Part V.
The equivalence and the polar identity remain valid tools; their derivation is not
repeated, nor is its right-hand side presented as a new method.
The inequality is not refuted, no mathematical NO-GO is added and no
paper is altered. A reopening needs a concrete operation that proves the
full comparison, with the novelty filter of this phase. Global positivity OPEN.
