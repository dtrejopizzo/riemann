# The complete semiprime sector exceeds the root scale after any finite number of differences

We use the representatives S_h of 062, with fixed h≥0. All reduced products and all powers in their masks are included, without cutoff in pq. Let E_{d,h}(x) be the contribution of the products with exactly d distinct primes, d≥1 fixed, with the 2^d slopes per product. Then for every θ<1
     
    limsup_{j→∞} (−1)^d E_{d,h}(j⁴)/(j⁴)^θ = +∞.

In particular the positive excess of the semiprimes (d=2) persists when completing the sum for these representatives. For d=1 a negative excess is obtained. The proof of 066 with a prefix of the infinite average did not give this statement. Here h is finite, an essential condition in the proof.

**Transform.** Write M_G(u)=∫G(z)z^(−u)dz/z and a_p(s)=p^(−s)/(1+p^(−2s)). For real s>1, the integral of E_{d,h}(x) x^(−s) dx/x over (0,∞) equals
    
    2^(d+1) (−1)^d (4−4^s)^h M_G(2s) e_d((a_p(s))_p),

where e_d sums the products of d entries with distinct indices without order. Indeed, for each r and each n of the mask, substitute x=r n² z² in the integral. The powers of each prime give the alternating series in p^(−2s); the sign μ(r)=(−1)^d and the number of slopes are constant. The absolute interchange is obtained by replacing the denominators by 1−p^(−2s) and using Σp^(−s)<∞. G_h vanishes near zero and decreases rapidly at infinity.

**Real singularity.** Put t=s−1 and ℓ=log(1/t). The first power sum of the entries a_p is ℓ plus a function analytic at t=0: subtract log ζ(s), using the Euler product; the difference converges locally normally near 1 and tζ(1+t) is analytic and equals 1 at zero. The power sums of orders ≥2 are analytic there. By the Newton identities, e_d is a polynomial in ℓ with analytic coefficients and leading term ℓ^d/d!. By 062, M_G(2)>0. Taking (−1)^h times the derivative of order h of the transform of (−1)^d E_{d,h}, the main term is

    [2^(d+1) (4 log 4)^h M_G(2) h!/d!] ℓ^d.

Indeed (4−4^(1+t))^h=(−4 log 4)^h t^h+O(t^(h+1)). Each derivative falling on ℓ instead of t^h loses at least one logarithmic degree. The remainder is O(1+ℓ^(d−1)). In particular the integral weighted by (log x)^h tends to +∞ as s↓1. The part x<1 is bounded by the fixed lower threshold of G_h. An eventual upper bound C x^θ with θ<1 on the positive half-line would give a uniform upper bound for that integral, a contradiction.

**Fourth powers.** For any ε>0 the derivative with respect to log x of the sum of the sector has absolute value O_{h,d,ε}(x^(1+ε)): bound the logarithmic derivative of G_h(z) by C z^(2+2ε) and sum the absolutely convergent series above with s=1+ε. The mesh j⁴ has logarithmic step O(x^(−1/4)). An eventual bound on that mesh would imply on the continuum an upper bound of order x^θ+x^(3/4+ε), still sublinear as a power if ε<1/4. This proves the claim.

**Consequence for the method.** In particular no finite number of differences of 062 allows paying separately for the complete semiprime sector with the margin O(√x). In every truncation 1≤d≤D the term of logarithmic degree D dominates in the same argument, with sign (−1)^D. These excesses are subsequential; for the complete form all orders intervene with alternating signs. The infinite average of 063 has a flat zero and the finite derivative decisive here is not available for it.

The disappearance of the branches when summing all orders is seen exactly on Re s>1: including d=0, the arithmetic factor is ∏_p(1−2a_p)=∏_p(1−p^(−s))²/(1+p^(−2s))=ζ(4s)/(ζ(s)²ζ(2s)). Near 1 it has a double zero, while no nonconstant truncation is regular there. This identity explains why the sectorial excess is compatible with the regularity at 1 already established in 060; it does not provide a bound in the critical strip.
