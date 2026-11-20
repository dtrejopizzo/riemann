# POWER_HIGHPASS_DIAGONAL_DENSITY_AUDIT_094 — Independent audit

Status: **APPROVED / PROVED**, source `POWER_HIGHPASS_DIAGONAL_DENSITY_094.md` read in full. Approved independently by two checks. Papers untouched.

## Isometry and object

The Cayley factor sqrt(2u)/(s+u) has squared modulus 2u/(u²+tau²), exactly |dtheta/dtau|. With Plancherel 1/(2pi), the map is unitary H² disc↔causal L². Its polynomial basis corresponds to Laguerre; completeness relies on the confluent bridge 014, not on a continuity claim for W. Vn corresponds to ALL polynomials of degree<n and Q=(1+z)/2. The factor 2^-r alters neither S nor distances. The statement holds for the UNION of spaces, not its linear span nor a cone of sums of different blocks.

## Projection and determinant

The binomial Gram matrix correctly includes the out-of-range zeros and is PD by the positive integral. The vector of pairings with 1 is delta0; hence the squared norm of the projection is (G^-1)00, the quotient of principal minors Dn−1/Dn. Dodgson has the correct shifted corners (a−1,b+1),(a+1,b−1). The triangular cases a0/b0 fix the boundaries without negative factorials. The cross product telescopes and the remaining factor is the precise quotient of consecutive factors. Dn−2>0, known by induction, allows dividing without circularity. Thus A(n,r) is exact, including n1/r0.

The product A=prod(n+j)/(n+r+j) gives the two log bounds with correct orientation. The upper bound is declared ONLY for r>=1: this avoids 0/0 at n1r0; at r0, A=1 directly. A→1 if and only if r²/n→0 along n→infinity, distinguishing r<n and r>=n.

## Density of the UNION

Sufficiency approximates each monomial through z^mS_(n−m,r(n)) inside the SAME S_(n,r(n)); they can be summed without leaving the block. The quantitative estimate keeps the isometric norm of the shift. A subsequence r²/n→0 and polynomial density give approximation by a single block for each target, without nesting.

For necessity, the uniform gap dist(1,S)>=d for n>=N is correctly deduced from the log upper bound. The finite exceptions, even r0 ones containing 1, are handled with H*=1+(d/2)zM, M larger than all their maximal degrees. zM is orthogonal to EACH exceptional block, so dist>=d/2; for n>=N the triangle inequality gives the same bound. Non-density of the WHOLE union is proved, not just a failure to approximate 1 outside the exceptions.

The uniform distance>1/2 for r>=n is correct. Adding finitely many confluent ranges at the same rate does not repair the UNION, with the causal Cayley witness of 1+zM/4. This does not include continuous variations of rate nor inter-block linear combinations.

## Difference and limits

Consulted the three records, 016/029/054/059/060/bridges. The object is UNWEIGHTED L², fixed rate, complete numerators, with EXACT distance and threshold r²/n. 016 treated the common weighted norm; that bridge is not retried. No strong W: even if the union were L² dense, continuity of THE COMPLETE form in a sufficient topology would be needed. Non-density of the current cone does not exclude its linear span, crossings/signed control/mixtures or compensated descent either. No new W/T nor global impossibility.
