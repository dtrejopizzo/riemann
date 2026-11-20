# A local inequality on the primes equivalent to the criterion of 039

Direct antecedent: [039, barrier and interpolation](ROUND_039_A.md). There one interpolates between contiguous samples and needs an accumulated sum or an infinite tail. Here one subtracts the homogeneous interpolation between two samples at macroscopic logarithmic distance. The subtraction annihilates both exteriors exactly and is inverted by comparison at the integer indices. The final equivalence with P47 uses the analytic bridge of 038–039.

For j≥2 let i=floor(j/2), m=2j, l=4 log i, r=4 log j, u=4 log m and b=3/2. Put
A=sinh(b(u−r))/sinh(b(u−l)), B=sinh(b(r−l))/sinh(b(u−l)). Define a weight w on [i⁴,m⁴] by

    w(t)=A(t/i⁶−i⁶/t²)          for i⁴≤t≤j⁴,
    w(t)=B(m⁶/t²−t/m⁶)          for j⁴≤t≤m⁴.

The two formulas agree at j⁴. The weight is positive in the interior and zero outside the band. The global sign is equivalent to the existence of a finite C such that eventually

    Σ_{i⁴<p<m⁴} w(p) log p ≥ ∫_{i⁴}^{m⁴} w(t) dt − C,

where p runs only over the primes. The integral equals exactly (3/2)(j²−Ai²−Bm²).

**Proof.** Write T f=f(r)−Af(l)−Bf(u). T annihilates exp(±bs) as functions of s. Applied to exp(−b|s−log t|)/√t, it gives zero outside the band. Inside, expanding the exponentials gives exactly w(t). Integrating the identity over t>0 gives the formula for the integral, since before applying T the integral is (3/2)exp(s/2). The pointwise identity of 039 therefore gives T E=∫w−Σ w(n)Λ(n), interpreting E in logarithmic coordinate.

The contribution of proper powers is O(1) uniformly. In the band t≥j⁴/81, and the difference of two positive terms gives w(t)≤1/√t≤9/j². For X=m⁴, Chebyshev gives Σ_{k≥2,p^k≤X}log p=O(√X+X^(1/3)log X)=O(j²).

If the sign holds, 038 gives |k(s)|≤k(0) and 039 gives E=3k+O(1) on the half-line. Since A,B≤1/64 (both distances to the centre are ≥log 16), T E stays bounded in absolute value.

Conversely the local inequality implies T E≤C. Write E_j=E(j⁴) in the original coordinate. Choose M≥0 dominating the initial samples and such that (1−2/64)M≥max(C,0). For ε>0 the sequence E_j−M−εj³ tends to minus infinity because E_j≤(3/2)j². In the tail, its image under T is ≤0, since Ai³+Bm³≤(1/8+8)j³/64. A positive maximum would be attained in the tail, where its image would be at least (1−A−B) times that maximum. The contradiction and ε↓0 give E_j≤M. Apply 039.

**Pending obligation.** The integral is of order j². The proof requires that the weighted deficit of the primes be bounded by one and the same constant for all bands. The cancellation of the tails and the elimination of the proper powers are exact and at bounded cost, respectively. Neither estimates that deficit. The argument does not certify an additional window.

## What happens when using the divisor identity on this band

In 040 a fixed profile lost the outer tail of the target. Here that tail was eliminated and that is why the question needed revisiting. For even j, x=j⁴, write w_j(xt)=x^(−1/2)W(t). The hat W is continuous, positive on (1/16,16) and zero outside. Its only corners are at 1/16, 1 and 16. In particular W'(1/16+)>0 by the formula of the left piece, and W'(1/16−)=0.

Let f be a signed continuous profile with compact support in (0,∞), fixed for all even j. Write Df(t)=Σ_{m≥1} f(mt). The identity Σ_{d|n}Λ(d)=log n allows evaluating the pairing with Df using log n. **Every minorant Df≤W of this class loses at least c_f√x in the normalised sum over the primes**, for every sufficiently large even j, with c_f>0 that may depend on f.

Indeed, the equality Df=W would force
f(t)=Σ_{m≥1} μ(m)W(mt) by finite inversion at each t>0. For each prime p, at t₀=1/(16p) only m=p,16p,256p can contribute a jump of the derivative: the three possible products mt₀ are precisely the three corners. The last two Möbius coefficients are zero by divisibility by 4. Therefore the jump of the derivative of the inverse is −pW'(1/16+)≠0. Only finitely many terms intervene in a neighbourhood of each t₀. There are such corners arbitrarily close to zero, where f would have to be identically zero. This excludes equality even for continuous profiles without differentiability hypotheses.

If Df≤W, the continuous difference then has an interval [a,b]⊂(0,∞) on which it is at least η>0. The primes in [ax,bx] cost, in the normalisation of 044, at least η(θ(bx)−θ(ax))/√x up to endpoints, of order √x by the prime number theorem. Even if minoration is required only at the prime samples of all large even j, the same theorem and continuity imply global minoration. The constant is not uniform over profiles. Outside this discard remain scale-dependent profiles and methods that evaluate the signed remainder.

Targeted cross-check with 040, P47 thm:band (moving band necessary), phase 200 SPEC_SIGN_OBJECT_003 (annihilators of the sum via Mellin) and POWER_INTERIOR_SCALE_030 (singularities under Möbius dilation). The proof specific to the band uses the collision of its three corners and divisibility by 4.

For fixed supports [a,b] with a>0 there is, moreover, an *integral* loss uniform in f. Denote by g the inverse of W above, and choose I=[l,h]⊂(0,a) with ∫_I|g|>0, possible by the corners and continuity. For V=W−Df≥0, B=max(b,16), the inversion of V on I equals g and only sums m≤B/l. By change of variable and positivity,
    
    ∫_I |g| ≤ Σ_{m≤B/l} (1/m) ∫_{mI} V ≤ H_floor(B/l) ∫_{l}^{Bh/l} V.

This bound avoids any question of integrability at zero. The transfer to the prime samples is pointwise for each fixed profile; the continuity argument does not give a uniform rate for profiles that change with j.
