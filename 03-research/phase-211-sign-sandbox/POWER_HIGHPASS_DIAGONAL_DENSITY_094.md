# POWER_HIGHPASS_DIAGONAL_DENSITY_094 — Exact L² density threshold of a filtered union

Status: **PROVED, independent audits approved.** See `POWER_HIGHPASS_DIAGONAL_DENSITY_AUDIT_094.md`. An unweighted L² distance is computed and it is characterized when a diagonal UNION of spaces Q^rV_n is dense. Density of its linear span, continuity of W in L², and positivity of cross terms between different spaces are not claimed. Papers untouched.

## 1. Consultation and precise difference

Consulted: the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; reread BRIDGE002, THREE002§8, PACKET_SCOPE009, CONFLUENT_BRIDGE014, HIGHPASS015, JOINT_SCALE016, DESCENT_AUDIT016, 053–054 and 059–060.

DESCENT_AUDIT016§§2–3 already prevents density in L²_eta, common eta>0: even one filter Q kills a continuous moment, and filters of increasing order only allow a zero strong limit. That strong bridge is not retried. THREE002§8 proves an L² obstruction for another family, with exponentially growing rates and temporal concentration.

The difference here is an EXACT distance in UNWEIGHTED L², with FIXED rate u and ALL numerators of the block. It allows quantifying the joint regime r²/n, even when the spaces are not nested. The binomial determinant and Dodgson are classical algebra; no novelty of these tools is claimed.

## 2. Spaces and unitary change, with their constants

Fix u>0 and define, in Laplace transforms of causal functions,

    V_n(u)={P(s)/(s+u)^n: deg P<n}, n>=1,
    Q(s)=s/(s+u), E_(n,r)=Q^r V_n(u), r>=0 integer.

The time norm is the ordinary L² norm. Plancherel uses

    ||f||²=(1/(2pi))int_R |F(i tau)|²d tau.

Put z=(s−u)/(s+u). The unitary map between H² of the disc and the causal space is

    F(s)=sqrt(2u)/(s+u) H((s−u)/(s+u)).             (CAYLEY)

On the boundary, |z|=1 and |dtheta|=2u d tau/(u²+tau²), exactly the squared modulus of the prefactor. Hence ||f||²=int|H(e^(itheta))|²dtheta/(2pi). The map on polynomials gives the orthonormal Laguerre basis; its completeness also follows from the confluent density 014. Thus the isometry extends to all of causal L².

CAYLEY carries V_n onto the polynomials of degree<n, and Q=(1+z)/2. Consequently E_(n,r) corresponds exactly to the subspace

    S_(n,r)={(1+z)^r P(z): deg P<n} of H².

The scalar factor 2^(−r) of Q^r changes neither the subspace nor the distances. The constant vector 1 corresponds to f_0(t)=sqrt(2u)exp(−ut), which has norm 1. The whole argument also holds in the real subspaces.

## 3. Exact distance to the base vector

For ALL n>=1,r>=0,

    dist_H²(1,S_(n,r))²=1−A(n,r),
    A(n,r)=[(n+r−1)!]²/[(n−1)!(n+2r−1)!].        (EXACT-DISTANCE)

At r=0 the quotient is 1 and the distance is zero. To prove the formula, use the basis b_j=z^j(1+z)^r, j=0,...,n−1. Its Gram matrix is

    G_ij=binom(2r,r+i−j),

with out-of-range binomial coefficients equal to zero. G is positive definite by integration of |(1+z)^rP|². Moreover <1,b_j>=delta_(j,0), since the constant term of b_j is 1 only for j=0. The squared norm of the projection of 1 is therefore

    (G^(-1))_00=det G_(n−1)/det G_n.

The binomial determinant computed in §4 gives exactly A(n,r).

## 4. Binomial determinant: proof via Dodgson

For integers a,b>=0, define

    D_n(a,b)=det[binom(a+b,a+i−j)]_(i,j=0,...,n−1), D_0=1.

The identity is

    D_n(a,b)=product_(j=0)^(n−1)
                   j!(a+b+j)!/[(a+j)!(b+j)!].       (BINOMIAL-DET)

The cases n=0,1 are direct. If a=0 or b=0 the matrix is triangular with diagonal 1, equal to the product. For a,b>=1, the Desnanot–Jacobi identity applied to the four corners gives

    D_n(a,b)D_(n−2)(a,b)=D_(n−1)(a,b)²
       −D_(n−1)(a−1,b+1)D_(n−1)(a+1,b−1).

Assume by induction the formula for smaller sizes. The quotient of the cross product by D_(n−1)(a,b)² is

    product_(j=0)^(n−2) [(a+j)(b+j)]/[(a+j+1)(b+j+1)]
       =ab/[(a+n−1)(b+n−1)].

Hence the factor in the recurrence is

    1−ab/[(a+n−1)(b+n−1)]
       =(n−1)(a+b+n−1)/[(a+n−1)(b+n−1)].

It is precisely the quotient between the last two consecutive factors of BINOMIAL-DET. Since D_(n−2)>0 by the inductive formula, one may divide and the identity is proved. Taking a=b=r and dividing D_(n−1)/D_n proves EXACT-DISTANCE, including n=1 with D_0=1.

## 5. Quantitative regime r²/n

For r>=1,

    A(n,r)=product_(j=0)^(r−1)(n+j)/(n+r+j).

The inequalities log(1−y)<=−y and log(1−y)>=−y/(1−y), 0<y<1, give

    exp(−r²/n)<=A(n,r)<=exp[−r²/(n+2r−1)].        (TWO-SIDED)

The left bound also holds at r=0. In particular the distance to the base vector tends to zero along dimensions n→infinity IF AND ONLY IF r²/n→0. For necessity, if r>=n the exponent of the upper bound is larger than r/3; if r<n it is larger than r²/(3n). Thus it cannot tend to zero while r²/n stays away from zero.

There is also a quantitative approximation of any fixed polynomial P(z)=sum_(m=0)^M c_m z^m. If n>M,

    dist(P,S_(n,r))
       <=sum_(m=0)^M |c_m|sqrt[1−A(n−m,r)]
       <=r sum_(m=0)^M |c_m|/sqrt(n−m).             (POLYNOMIAL-APPROX)

Indeed z^m S_(n−m,r) is contained in S_(n,r), and multiplying by z^m preserves the H² norm. Approximating each monomial and summing inside the SAME linear space gives the first inequality. The second uses 1−exp(−y)<=y. Approximants belonging to different blocks are not being summed.

## 6. Exact criterion for the diagonal UNION, without monotonicity of r

Let r(n) be an arbitrary assignment of nonnegative integers, n=1,2,..., with no monotonicity assumed. Then

    closure_L²(union_(n>=1) E_(n,r(n)))=L²(0,infinity)
       IF AND ONLY IF liminf_(n→infinity) r(n)²/n=0.  (DIAGONAL-DENSITY)

This concerns the closure of the UNION, not its linear span.

Sufficiency: choose a subsequence n_k→infinity with r(n_k)²/n_k→0. POLYNOMIAL-APPROX shows that each fixed polynomial is approximated by elements of S_(n_k,r(n_k)). Polynomials are dense in H²; approximating first the target by a polynomial and then that polynomial by a single block proves density of the union. No nesting was used.

Necessity, including the finite cases r=0: if the liminf is not zero, there exist 0<delta<=1 and N such that r(n)²/n>=delta for all n>=N. TWO-SIDED and the two cases r<n/r>=n give

    dist(1,S_(n,r(n)))>=d=sqrt[1−exp(−delta/3)]>0, n>=N.

The exceptional blocks n<N are finitely many, even if some have r=0 and contain the vector 1. Choose M larger than ALL their maximal degrees n+r(n)−1, and epsilon=d/2. The vector

    H_*=1+epsilon z^M

is at distance at least epsilon from each exceptional block, because z^M is orthogonal to all their polynomials. For n>=N, the triangle inequality gives

    dist(H_*,S_(n,r(n)))>=d−epsilon=d/2.

Thus H_* has positive distance to the complete union. This avoids assuming that the vector 1 serves as a witness when finitely many unfiltered blocks have been added.

## 7. Uniform obstruction for the known positive cones

If r>=n>=1, TWO-SIDED implies

    A(n,r)<exp(−1/3)<3/4,
    dist(1,S_(n,r))>1/2.

The second comparison uses exp(1/3)>1+1/3=4/3. Hence the union of ALL the blocks E_(n,r) with r>=n is not dense even in unweighted L², with the uniform distance above. In particular this applies to the cone 060

    r>=10^12[n ceil(log_2(n+1))]^3,

which already requires r>=n. Its sign is not reproved, nor is this obstruction presented as a negative W sign.

Adding finitely many unfiltered confluent blocks at the SAME rate does not suffice either. If their degrees are less than M, the vector 1+z^M/4 has distance at least 1/4 from those blocks and more than 1/4 from the whole cone r>=n, by the triangle inequality. Its CAYLEY image provides an explicit causal witness. The statement does not include other continuous families of rates nor arbitrary sums of members of different blocks.

## 8. Scope with respect to the sign problem

016 already discarded the strong bridge in a common weighted norm. 094 adds the EXACT density threshold of the diagonal union in the WEAKER L² topology, and a quantitative obstruction for the current sign cones. If some future positive cone reached r=o(sqrt n) along a subsequence, DIAGONAL-DENSITY would give L² approximation; even then continuity of the COMPLETE form in the topology used would have to be justified. W is not deduced from that density here.

Nothing is claimed about density of the linear span of the union either. Positivity of each block does not automatically pay for the crossings between blocks. The routes of mixtures or descent with specific compensation remain open. No paper is modified and the global goal is not closed.
