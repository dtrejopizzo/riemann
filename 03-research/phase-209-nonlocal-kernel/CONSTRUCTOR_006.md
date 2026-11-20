# CONSTRUCTOR_006 — Exact FE of Π and explicit defect after deletion

2026-10-18. Constructive continuation. **PROVED, favourable audit in AUDIT_006:** exact inversion identity for the term Π of the positive kernel −R; its parameter is fixed at α=1/4. The identity that changes after removing primes is also computed. **The form Q_T is not yet obtained.**

## 0. Corpus before building

Targeted searches in the ROUTES-TRIED-INDEX index, grid and crossword: co-Poisson, fractional lattices, Hamburger, self-duality defect and exterior carrier. Pertinent references: SPEC005 (origin of the removed theta), Z_CARRIER, COMPOSE_EF_001, CELL_001, FE/Helson transport and the P1 barriers.

No other Hamburger identification argument is proposed, nor a quadratic defect whose zero identifies ζ. No new abstract factorisation nor Bohr lift is used. **New reason:** Π is already a concrete term of the PSD equality proved in CONSTRUCTOR_005; its complete nonlinear FE is computed, with denominator and fractional dilations, before attempting a link. The positivity of −R and the classical self-duality of theta are not sold as a proof of D. The Mellin representation of the profile m used below is classical; what is recorded is its exact action on this Π and the defect of the same deleted scheme.

The finite pushforward of −R with Möbius coefficients and translations was discarded before building: it would still be a convolutive symbol of P1. The existence of a new PSD kernel does not remove the reason for that barrier.

## 1. Mass-defect profile and Poisson

Let c(y)=y^(−1/2), τ(y)=θ(y)−1 and

`m(y)=c(y)−τ(y)`.

For y>0,

`0<m(y)<1`, `m(y)=y^(−1/2)m(1/y)`,

`τ(1/y)=√y[1−m(y)]`.                              (1)

**Proof.** Comparison with the integral of the decreasing Gaussian gives τ(y)<c(y); by Poisson `m(y)=1−c(y)τ(1/y)<1`. The second identity is obtained by substituting Poisson again. The third follows from the definition of m at 1/y. ∎

The Mellin of m is `∫m(y)y^(α−1)dy=−Z_α` on 0<α<1/2, according to CONSTRUCTOR_005. It is not by itself a second bridge to the node.

## 2. The positive term Π that is kept

I define for d≥2

`W_d(y)=τ(d²y)−τ(y)/d`.

The kernel already obtained is

`Π_α(d,e)=∫_0^∞ y^(α−1) W_d(y)W_e(y)/τ(y)dy`.

It is a convergent integral for 0<α<1/2; in fact its convergence at zero admits more, but enlarging the interval is not needed.

Using τ=c−m one has the **forward** identity

`W_d(y)=m(y)/d−m(d²y)`.                            (2)

The c part cancels exactly. No remainder was eliminated.

## 3. Exact transformation: two scales and fixed critical parameter

**Theorem 1 (PROVED).** For d,e≥2 and 0<α<1/2,

`Π_α(d,e)=1/(de) ∫_0^∞ y^((1/2−α)−1)`

` ·[m(y)−m(y/d²)][m(y)−m(y/e²)]/[1−m(y)] dy`.      (3)

**Proof.** Replace y by 1/u in the definition. By (1) and (2),

`W_d(1/u)=√u/d [m(u)−m(u/d²)]`,

`τ(1/u)=√u[1−m(u)]`.

The Jacobian and the quotient leave the power u^((1/2−α)−1); rename u. All integrals converge and the change of variable is ordinary. ∎

At α=1/4 the exponent does not change: **the inversion preserves the critical parameter of the same positive kernel**, and transforms forward dilations d² into backward dilations d^(−2), with denominator 1−m.

The representation keeps both scales inside the differences. This does not by itself prove that the integrated Π at fixed α differs from w(de), nor that it leaves an effective height algebra. That reduction has been neither proved nor refuted here; it remains pending to build and analyse the effective operator, as O1 requires.

### Where the origin term went

If written directly with tau, the same formula is

`W_d(1/u)=√u/d[τ(u/d²)−τ(u)]−(1−1/d)`.

The constant term did not disappear by an approximation: it was incorporated exactly into the differences of m. Hence the rank one v_s of −R cannot be identified with the pole of Q_T by omitting this contribution.

## 4. Finite deletion: two distinct profiles, not the same self-duality

Let P>1 be squarefree, `δ_P=∏_{p|P}(1−1/p)`,

`τ_P(y)=Σ_{a|P}μ(a)τ(a²y)`,

`m_P(y)=δ_P c(y)−τ_P(y)`.

The PSD completion of −R_P was proved in CONSTRUCTOR_005 §10. To compute its FE, I define its exact dual profile

`m_P^∨(y):=y^(−1/2)m_P(1/y)`.

By inclusion–exclusion and Poisson,

`m_P^∨(y)=−Σ_{a|P} μ(a)/a ·τ(y/a²)`, P>1,        (4)

`τ_P(1/y)=√y[δ_P−m_P^∨(y)]`.                     (5)

It is not claimed that m_P or m_P^∨ are positive, nor that they lie between 0 and 1.

The exact discrepancy is

`Δ_P(y)=m_P^∨(y)−m_P(y)`

`=Σ_{a|P}μ(a)τ(a²y)−Σ_{a|P}μ(a)/a·τ(y/a²)−δ_P c(y)`. (6)

It has limits certifying its non-vanishing:

`Δ_P(y)→δ_P` as y↓0,

`Δ_P(y)=−δ_P y^(−1/2)+o(y^(−1/2))` as y→∞.

Indeed τ_P(y)=δ_P c(y)+exponential error at zero, because the constant cancels; and τ_P decays exponentially at infinity. The same properties in (4) give the dual limits. Hence **the deleted profile is not self-dual in the manner of (1)**. The defect changes sign between both ends; no quadratic sign is attributed to it.

For d coprime to P,

`W_d^P(y)=τ_P(d²y)−τ_P(y)/d=m_P(y)/d−m_P(d²y)`.

Its exact FE is

`W_d^P(1/u)=√u/d[m_P^∨(u)−m_P^∨(u/d²)]`.

Hence the same change of variable produces

`Π_α^P(d,e)=1/(de)∫_0^∞u^((1/2−α)−1)`

` ·[m_P^∨(u)−m_P^∨(u/d²)][m_P^∨(u)−m_P^∨(u/e²)]`

` /[δ_P−m_P^∨(u)]du`.                            (7)

The denominator is strictly positive by (5), since τ_P>0. The deleted law still gives a positive Gram, but the forward profile m_P and the backward m_P^∨ are different. Substituting one for the other without Δ_P would be a false equality.

**Precise specificity achieved:** the *single-profile* identity (2)–(3), with the same m in both orientations and the pair of masses τ and 1−m, uses the complete FE and fails after deletion by the explicit defect (6). This does not yet prove that this identity produces a sign for Q_T.

## 5. Remaining concrete link step

The full kernel now has the proved formula

`−R_(1/4)=(-Z_(1/4))G_(1/2)+(-Z_(1/4))v_(1/2)v_(1/2)*+Π_(1/4)`.

The FE of Π is (3), while G and v have explicit coefficients of weight 1/2. A useful link must build a map U_T from the tests of the node to divisibility observables and **verify** three identities:

1. The contribution of `G_(1/2)` and the two representations of Π must produce the comb linear in Λ, with all quotient/lcm terms treated.
2. The origin term inside (3) and the rank one v must give exactly the polar part and its vanishing under the declared constraint, without identifying them by resemblance.
3. The remaining continuous part must give the conductor-1 gamma with a proved positive sign of the remainder, not a free symbol defined to complete Q_T.

These are not three new assumptions taken for granted. They are the concrete verifications of a **single link not yet built**. The candidate available for that computation is the forward/backward equality of Π, not a new list of programmes.

The mere choice `a_d=Λ(d)F(log d)/√d` does not prove those identities: it produces a form in finite evaluations, while Q_T acts on the continuous domain. The choice by autocorrelations would give degree four. Neither is adopted as a map without resolving that difference.

## 6. Exact residue

There is already an independent positive renormalised kernel and a computed internal FE distinguishing the complete profile from the deleted profile. **There is not yet an effective operator K(t,t′) on the domain of Q_T nor an identity of its form with −R.** It has not been proved that (3) turns the sign of −R into the sign of the node.

The pending identity is not "some root of Q_T exists": it must use (2) and (3) to produce the concrete terms of the paper. If an attempt only invokes PSD of −R, it fails the specificity test because that PSD survived deletion; precisely the single-profile identity and its defect (6) must intervene.

**Status:** FE of Π and deleted defect PROVED, favourable audit in AUDIT_006; non-Hankel scope precision incorporated. Q_T link OPEN, target D active. No impossibility conclusion nor closure of O1.


## Precision of scope of the link criterion — 2026-10-19

The later review of the link (round011, direct cross-check with P47) corrects
the reading of §5: the three correspondences listed there are a possible
scheme for computing a candidate, NOT necessary conditions of every
proof. A TOTAL identity, or a domination of forms,

    a_T(F) >= K_(1/4)(U_T F) >=0,

on a core dense for the norm of the target form, with all
remainders and domains justified, suffices. It is not required that G produce separately
the comb, v separately the polar part, nor Π separately gamma. There may be
cancellations between pieces. The step from the core uses continuity in the
norm of the target form; L² density is not enough. For complete D the
sectors and polar terms must be treated according to P47. This precision
does not yet supply the required domination or map.
