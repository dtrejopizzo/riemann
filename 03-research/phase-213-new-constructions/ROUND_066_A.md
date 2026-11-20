# Two cutoffs of opposite sign for the semiprime total

Compared with the subfamilies of 061 and the rows of 065, here ALL products of two distinct primes under a macroscopic cutoff are included. Let x=L² and let A(c,x) be the sum of the filtered representative of 063 over p<q, pq≤cx, counting one slope per product (for the four, multiply by four). For every fixed c>0,
    
    A(c,x)/(x log log x / log x) → I(c) = ∫₀ᶜ J(1/√v) dv.

There are fixed cutoffs c₊, c₋ for which I(c₊)>0>I(c₋). In particular even a one-sided bound O(√x) fails on some complete prefix, also over x=j⁴.

**Counting.** The number B(y) of pq≤y with p<q is asymptotic to y log log y/log y. Indeed, sum π(y/p)−π(p) for p≤√y. The subtraction is O(y/log²y). For any fixed ε between 0 and 1/2 the part p>y^ε is O_ε(y/log y) by Chebyshev and partial summation. For p≤y^ε the PNT uniform in y/p and the reciprocal sum of primes (asymptotic to log log y by PNT and partial summation) confine the leading coefficient between 1 and 1/(1−ε); let ε↓0. Thus, normalising by B(x), the masses of the points pq/x converge on compact intervals of (0,∞) to length. By step approximation it also holds for the continuous weight J(1/√v).

**Mask and lower boundary.** Write T=√(x/pq). On δx≤pq≤cx, T≤1/√δ; replacing the mask of 060/063 by J(T) costs O_δ(p⁻²+q⁻²) per pair, applying |J(z)|≪z² and summing the two geometric series. The outer sign μ(pq) is positive. The aggregate cost is O_{δ,c}(x/log x), since p≤√(cx), π(cx/p)≪_c x/(p log x) and Σp⁻³ converges. For pq≤δx use |J(z)|≪z^(1/2) on the whole half-line. The complete series in powers of p and q has absolute value ≪T^(1/2), with a constant uniform in p,q≥2. Below √x the sum is O(x^(5/8)) counting all integers. Above, on each block y/2<pq≤y, B(y)≪ y log log x/log x; the cost divided by B(x) is O((y/x)^(3/4)). The dyadic sum up to δx gives O(δ^(3/4)). Taking first x→∞ and then δ↓0 yields the limit.

**The two signs.** Write w(v)=J(1/√v). The moments of orders zero and one of 063 give ∫w=∫w log v=0 after changing variables. Thus I(c)=−∫_c^∞ w, and integration by parts gives ∫₀^∞ I(c) dc/c=−∫w(v) log v dv=0. The boundary terms I(c)log c vanish by the decay of 063 at both ends. I is not identically zero since I'=w and J is nonzero. By continuity I takes both signs.

The result rules out extending 065 to all cutoffs pq≤cx through a uniform bound on the semiprime balance taken separately. The counterexample corresponds to the prefix of the filtered representative. The global representation includes both the rest of the products and the tail in pq; the identity ∫w=0 itself cancels the leading coefficient when completing the integral. The asymptotic for fixed c does not estimate the remainder of that cancellation at scale √x.
