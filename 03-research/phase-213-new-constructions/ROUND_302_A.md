# Sign of the full block with a large prime as the frequency approaches zero

Use the full coefficients b_t of 292, including the prime 2. Fix 1/2≤α<1, L=log x, v=t²L, a=log 2 and b=(log 2)²/4. In the joint limit x→∞, t→0, with no restriction on v,

    Σ_(n≤x; P⁺(n)>x^α) b_t(n)
      = −2 U x/L⁵ · [24a²−12abv+2b²v²+o(1+v²)],    U>0.

The main bracket is 2(bv−3a)²+6a². This establishes a strictly negative sign, uniform over the transition v bounded, v→0 and v→∞. In particular at frequency exactly zero the contribution is asymptotic to −48 U a² x/L⁵. All cofactors of the large prime are included. By the ceiling of every logarithmic order for the full partial sum, the remaining block has the same term with positive sign. The error in the balance required by 299 remains uncontrolled at square-root scale.

**The factor that changes the order.** Write B_t(s)=Σ b_t(n)n^(−s) by continuation. With h=s−1 one has exactly, in a neighborhood of (0,0),

    B_t(1+h) = V(h,t) h² [1−(1+cos(t log 2)) 2^(−1−h)]²,

where V is analytic, even in t and U=V(0,0)>0. Indeed the two L factors of 292 are nonzero at (1,0), ζ^(−2) contributes h² and the other factors of the correcting product converge locally and are positive at the real point. The inner bracket is ah+bt²+O(h²+|h|t²+t⁴). Extracting the coefficients in h one obtains, with derivatives with respect to s evaluated at 1,

    B'' = 2U b² t⁴+O(t⁶),   B''' = 12U ab t²+O(t⁴),
    B'''' = 24U a²+O(t²),   B=B'=0.

**Uniform moments.** The proof of 294 for a single large prime holds uniformly in |t|≤1: χ is still nonprincipal at t=0, both in the twisted sums and in the PNT in progressions, and only upper bounds for the Euler correction are needed. Hence the block equals −2Σ b_t(m)li(x/m), with m≤x^(1−α), up to error O_R(x/L^R). To expand to order five apply the cutoff M=exp(√L) of 294; take 12 terms of li and expand the denominators up to degree 24. The absolute harmonic norm up to M costs O(L²), the integrated remainder is O(x/L⁶) and the moments can be extended to infinity with arbitrary logarithmic saving. The moments of degree j are (−1)^j B^(j)(1). The term with k=1 of li and j=2,3,4 gives respectively B''/L³, −B'''/L⁴ and B''''/L⁵ after extracting x. The other terms cost O(t⁴/L⁴+t²/L⁵+1/L⁶), in those same units. On substituting the three derivatives, the error relative to (1+v²)/L⁵ tends to zero for any sequence t→0. This estimate is necessary because the fixed-frequency asymptotic of 294 loses its main term exactly at t=0.

**What grouping compensates.** Row zero contains positive families larger than the square root (301). Gathering all those with a prime larger than x^α together with the terms of opposite sign in the same block gives the negative formula above. The complement is too positive to be discarded, even with the two additional powers of logarithmic saving at t=0.
