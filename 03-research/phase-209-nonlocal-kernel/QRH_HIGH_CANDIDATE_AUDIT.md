# QRH — high review of the candidate geometry

2026-10-19. Independent review. **PROVED: parameter computations and
failure of applicability of published hypotheses. CONDITIONAL: transport
of the high formula to another geometry. No new zero-free region.**

## Corpus, object and source

Consulted: the project rules, the ROUTES-TRIED-INDEX index, master grid and current
crossword. Written difference: verify the high hypotheses of a specific
geometry that so far had only a formal low template. No
source of sign for D is reopened, nor is an extension
of the external lemmas considered proved.

Primary source: OpenAI, manuscript 30Sept2026, §§18–20, read in
`/tmp/qrh-review/september.txt`. The following references are to the text
of the manuscript; no full audit of its proofs was carried out.

The candidate is

    ell=1/5, b=1/10, lx=7/20, ly=9/20, h=17/20.

## 1. Supply of primes: these inequalities do pass

The check of §20.5 requires ell/d>7/37 for the range with selection.
For 1/2≤d≤h, the candidate minimum is

    ell/h=4/17,     4/17−7/37=29/629>0.

Moreover 5ell−h=3/20>0. Hence any fixed extension
0<zeta<3/20 keeps ell/(h+zeta)>1/5>7/37. With a fixed even K
sufficiently large, the slot sizes ell_i/d≤2ell/K can
lie below any positive mesh threshold already available. This
computation does not prove that such a threshold is available for the new
parameters: that is a separate analytic requirement.

The normalisation of §20.1 does not introduce an additional power either:
Z^(-ell/6)∏P_i^(1/6)=1 when Σell_i=ell. Its sign and
subpower argument for the normaliser keeps the same formal arithmetic with even
K. This does not validate all contours nor the modified high identity.

## 2. The dynamic transplant is not the only choice of kappa

Lemma18.1 starts with **3/4≤kappa≤1**. Its mesh uniformity is also
declared only in that interval. In §19 the dynamic relation is used

    kappa=2beta*−1,

included in §20 as kappa=3/4+2Delta for Delta=beta*−7/8.

If an endpoint sigma0=13/15 and beta*=sigma0+Delta are attempted, one gets

    kappa=11/15+2Delta.

For 0<Delta<1/120, kappa<3/4: the published Lemma18.1 does not apply
with THAT dynamic choice.
At the target sigma0=4/5, kappa=3/5+2Delta and the same insufficiency
appears for 0<Delta<3/40. This prevents literally copying the
dynamic capacity, but does NOT force extending the moment theorem.

The actual condition of Lemma18.1 for positive slots and kappa<1 is
beta*≤(1+kappa)/2. If the published result 7/8 is taken as input,
with the declared scope for the whole relevant Hecke family, one can
conservatively use kappa=3/4 for beta*≤7/8. More generally,
kappa=max{3/4,2beta*−1} respects the range of the lemma and its zero
condition when beta*≤1. The published uniform mesh does cover that choice.
This does not independently verify the external input 7/8.

The capacity becomes z_P=(1−2m)/(6kappa); it is smaller than the formal dynamic
capacity when 2beta*−1<3/4. The witness crossings,
row counts and high margins must be recomputed for that effective capacity.
The finding is only an insufficiency of the literal DYNAMIC transplant,
not an unavoidable obstacle of the domain of Lemma18.1. The problem of the
row floor in the next section does not depend on this choice.

## 3. The row-floor certificate does not transfer intact either

Formally keeping the first line of (20.4), replacing the
geometry and the reference scale sigma0, gives at d=h

    E(h)=C_geom+(1/2+ell)delta+ell q−h(1−R),
    C_geom=lx/2−sigma0+5h/6.

Algebraic proof: substitute a=(1+delta)/2 and use
ly=lx+b, 2lx+b+ell=1, h=1+ell−lx. This identity is a computation of
the template, not a new high bound outside the published geometry.

For the candidate,

    C_geom=53/60−sigma0.

The floor of §20.2 uses delta0=1/50, R=1, q≤delta0/2, without a zero witness.
Applying that same majorisation gives

    E(h)≤C_geom+(4/5)delta0.

At sigma0=13/15, the right-hand side is

    1/60+2/125=49/1500>0.

When comparing with C(beta*) one subtracts Delta. Thus, the preserved certificate
does not give a negative margin for all Delta>0: for Delta≤49/1500 its
upper bound is not negative. This does NOT claim that the actual contribution
is positive nor that the bound is optimal. It identifies the published step
that no longer certifies the sign of the exponent.

At sigma0=4/5, the same bound would be 149/1500. Even taking the floor
delta0 to zero would leave C_geom=1/60>0 at sigma0=13/15; changing only
that floor would not recover the formal certificate either. A different
row estimate, or a reorganisation improving this majorisation,
requires additional proof.

## 4. Relaxed joint certificate: moving the slots is not enough

For a variable formal geometry, the same floor computation requires that
the reference scale exceed the threshold of its majorisation

    sigma_floor=2/3+b/6+ell+(1/2+3ell/2)delta0.

With the published delta0=1/50, this is

    sigma_floor=203/300+(103/100)ell+b/6.

Combining it with the low template of QRH_FOUR_FIFTHS_ATTEMPT gives the
purely algebraic problem of minimising, over ell,b≥0,

    max{11/12−ell/4+(5ell−1)_+/8,
        203/300+(103/100)ell+b/6}.

Relaxing b to zero can only reduce that maximum. Before ell=1/5 the
first function decreases and the second increases; they cross at ell=3/16, with
value 167/192. After ell=1/5 both increase. Hence the relaxed
infimum is exactly

    167/192 > 13/15 > 4/5.

In particular, for 0<b≤1 the crossing is
ell=3/16−25b/192 and the minimum increases to 167/192+25b/768. The case b=0
relaxes the applicability of Pa≥1 and is not declared realisable by the probe.
Nor is the infimum obtained a new zero-free region: it is only
the floor of this pair of preserved formal certificates. To obtain
a strict margin the analytic slacks and losses are additionally required.

If delta0 were allowed to go to zero, the relaxed problem would have
infimum 13/15 at ell=1/5, b=0. Thus not even that purely algebraic relaxation
authorises 4/5 while preserving these majorisations. Improving any of them or
their compatibility is an additional task; it is not excluded that it can be done.

## 5. Balance of the review

The scalar supply of slots does not block this candidate. On the other hand,
there are two concrete changes needed to reuse the high part: replace the
dynamic choice of kappa by an authorised one, recomputing its capacities,
and repair the loss of slack of the row floor in (20.5). The first
does not by itself require extending Lemma18.1 if the external input 7/8 is accepted.
The full adaptive certificate, the capacity comparisons and all the
contours have not been recomputed here: they remain pending, they are not declared approved.

The candidate geometry does not constitute a 13/15 proof, much less 4/5.
These findings delimit necessary mathematical tasks for this
extrapolation; they do not classify all external probes or methods and do not
contribute a sign of D.
