# QRH — 4/5 attempt and limit of the preserved geometric extrapolation

2026-10-19. **PROVED: local computation and algebraic obstruction in an explicit
class of extrapolations. OPEN: new estimates or a new probe.
No sign of D; no general impossibility of reaching 4/5.**

## Corpus and new object

Consulted: the project rules, ROUTES-TRIED-INDEX (L74 and QRH review), master grid
and CROSSWORD-TO-D.md. Source: manuscript OpenAI30Sept2026, local text
/tmp/qrh-review/september.txt, §§7,15,16,20. No route D is reopened.
Written difference: test the threshold 4/5 in the concrete hypotheses of this
source, computing what survives locally and what fails when preserving its
estimation geometry of ALL rescaled subsets. It is not assumed
that Prop15.3 is already proved for parameters other than the published ones.

## 1. The principal numerator is not the local blockage

**PROVED conditional on the local identities of the source; exponent
arithmetic verified. Not a full audit of the manuscript.**

In Lem7.1, eq7.17, enlarge only the second box to

    xr≥4/5, zr≥33/200, wr≥19/20.

The same estimate of Ep in the proof gives the good-prime exponents

    4−6xr−6zr ≤ −179/100,
    1−xr−wr−6zr ≤ −87/50.

Since wr>0 there is no additional cost from W. The other terms of 7.17 satisfy
DW=O(Q^(-7/4)) and VW=O(Q^(-97/50)); the local denominators remain
uniformly bounded away from zero, by the same positive exponents.
Thus Hp−1=O(Q^(-87/50)) for p∤u. For p|u, the worst exponent of the local
table is 1−xr−wr≤−3/4; the remaining ones are smaller. This gives a normal product
and divisor control O_ε((Nu)^ε) as in the original proof. For u=1, the tail
over primes NP>P0 is O(P0^(-37/50)) by ideal counting; in particular
O(P0^(-7/10)) can be used. Increasing the fixed cutoff brings Hη close to 1.
This does not extend the whole global proof nor its contours.

In the principal computation of §16, the four exponents are

    −xr, −6zr, 4−5xr−6zr, 1−wr−6zr.

In the enlarged box they are ≤−4/5. Hence the same local computation produces
Bp=−1+O(Q^(-4/5)). The contraction of the numerator does NOT by itself prevent 4/5.

## 2. Published geometry: 3/40 missing in the low bound

The source has lx=17/48, ly=23/48, ell=1/6, b=ly−lx=1/8 and h=13/16.
Prop15.3 proves the low exponent L=lx/2+b/12=3/16. The normalisation is
CII(s)=s−11/16, so CII(4/5)=9/80 and

    L−CII(4/5)=3/40.

With that bound alone, the criterion Prop2.1 is not verified for a hypothetical
β*∈(4/5,7/8]: one would need ω at least 3/40 to cover the low
exponent, but also ω<β*−4/5≤3/40. This is an insufficiency of the bound, not a
lower bound on the true probe. Improving cancellation may change it.

## 3. Extrapolation template and loss of the completed norm

The geometry satisfies ly=lx+b, 2lx+b+ell=1, h=1+ell−lx and
M=lx+ly=1−ell. Consider its extrapolation preserving the SAME chain
of bounds of §15, with b≥0, ell≥0, and their applicability conditions.
This is a conditional template of estimates; it is not claimed that the
analytic lemmas are already proved for unpublished geometries.

It is not correct to simply keep the completed norm Z^(M'+ε) of 15.1:
that closure uses ell=1/6. In its proof, for the rescaled subset of
length d∈[0,ell], M'=M−2d and ell'=ell−d. Before substituting the published
values, the second branch of equation (15.3), in the proof of Lemma15.1,
contains the loss

    (1+3ell'−2M')/4 = (5ell−1+d)/4.

The first branch gives M' without that loss. Repeating THIS majorisation of the
two branches yields the exponent template for the SQUARED norm

    M' + ((5ell−1+d)/4)_+.

This keeps the step M'+ell'−1=−3d used in the proof. It is not a
lower estimate nor a claim that the extreme of each branch is
attained; it is the cost of the bound being extrapolated.

## 4. Threshold of the preserved template (PROVED algebraically)

In Cauchy–Schwarz, the above loss is divided by two. The count of
tuples, coefficients and length X' of 15.8 still contributes −d. The additional
exponent for the subset d is therefore

    f(d)=−d+(5ell−1+d)_+/8.

It is decreasing in d, with slopes −1 or −7/8. Its maximum over [0,ell]
is f(0)=(5ell−1)_+/8. If the additive absorption of 15.7 is kept, the
total low-bound template is thus

    L=lx/2+b/12+(5ell−1)_+/8.

The principal normalisation is C(s)=lx/2+s−1+h/6. The formal threshold that
solves C(σ_low)=L is

    σ_low=11/12−ell/4+(5ell−1)_+/8
          =11/12−ell/4                 if 0≤ell≤1/5,
          =19/24+3ell/8                if ell≥1/5.

The first branch decreases and the second increases. Its minimum over ALL ell≥0,
even relaxing length restrictions, is

    σ_low(1/5)=13/15 > 4/5.

Hence the preserved template of bounds does not certify 4/5 by changing only
the geometry. The naive computation that omits the loss of the completed norm
gives 11/12−ell/4 and would ask for ell≥7/15; but for ell=7/15 the correct template
gives 29/30, not 4/5.

This is an algebraic obstruction to the extrapolation of these
MAJORISATIONS, not a universal 13/15 barrier of the method or of the probe.
Even in this relaxed template an additional saving of at least
13/15−4/5=1/15 in the exponent is missing to reach 4/5 (without counting positive
losses). That saving must come from a new estimate; it is not a
free parameter.

The minimum is not a new external result 13/15: it has not been verified
that its other hypotheses can be satisfied at ell=1/5.

A concrete candidate to test that formal minimum is

    ell=1/5, b=1/10, lx=7/20, ly=9/20, h=17/20.

It satisfies the geometric relations above. The low exponent of the
template is L=11/60 and C(s)=s−41/60, with C(13/15)=11/60.
Even in the fully rescaled subset, M'=2/5>0 and
ly−ell−11b/6=1/15>0. This verifies those SCALAR conditions;
it does not verify all the analytic hypotheses nor the detectors and the
high comparison. It is a candidate for a next test, not a
13/15 theorem nor a proved improvement of the free region.

## 5. Additional conditions and limits

To keep the absorption Pa²/Y'≲Pa^(1/6), with Pa≈Z^b and
Y'≈Z^(ly−d), one needs ly−ell−11b/6≥0. Substituting
ly=(1+b−ell)/2, one gets ell≤1/3−8b/9. It is an additional condition of the
chain of bounds, not an improvement of its previous formal minimum. b>0 ensures
Pa≥1 eventually when the fixed factor Nb*>1; allowing b=0 only relaxes
the necessary conditions. With exponents equal to zero one must
additionally check constant factors and margins of the applications.

To go below the limit of the template at least one bound must be improved:
the second branch of the completed norm, the additive estimate, or the
summation over subsets/structure of the probe. That improvement was not obtained
here. A finer bound showing that the extreme branches are
incompatible would also escape the computation, since it keeps their
separate majorisation and does not prove that it is attained.

The certificate of §20.4 does not transfer without recomputation either. Freezing all
the other parameters and changing the reference scale adds 3/40 to the
raw exponent; that does NOT prove failure of a different optimisation.
The high comparison, the detector counts and their margins are not
proved by the minimisation of the low template either.
The dynamic quantity κ=2β*−1, the capacities and the counts also change
when taking Δ=β*−4/5, and their hypotheses must be checked again.

No 4/5 proof nor a source of sign for D was constructed. The result
is more precise: H is not the local difficulty, and changing only the geometry
while preserving this chain of low bounds does not reach 4/5.
