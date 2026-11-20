# A single binomial top reproduces the octave and damps the small atoms

For integer x≥2 take n=2x and g(y)=y^(−1/2)(1−cos(2π log(y)/log 2)) on [1,2], extended by zero. There is a combination of rows with this same upper endpoint, coefficients summing to zero and variation bounded independently of x, whose response R(m) coincides with g(m/x) at all integers x<m≤2x. In the lower part it satisfies

    |R(m)| ≪ (m/x)² dist((2x+1)/m, ℤ),     2≤m≤x.

**Construction.** Define A(t)=g((n+1−t)/x) on the whole line with the stated extension. Its support is [1,x+1] and it vanishes at both endpoints. For 1≤k≤x take a_k=A(k)−A(k+1); the sum telescopes to zero and Σ|a_k|≤∫|g'|. Put R(m)=Σ a_k c_(n,k)(m). Counting multiples in (n−k,n] and subtracting ⌊k/m⌋ one obtains, for all m≥2,

    R(m)=Σ_(j∈ℤ) [A(n+1−jm)−A(jm)].

Indeed, the first term sums the coefficients with k≥n+1−jm for each positive multiple jm≤n; multiples outside that range give zero in the extended formula. The second uses the tails with k≥jm. For m>x, m≤2x, only the first term with j=1 survives, including the endpoint m=x+1 where A(m)=0.

**Error on the small atoms.** With the Fourier transform of phase −2πiξt, |Â(ξ)|≪x min(1,|xξ|^(−3)). Indeed g is C¹, and its piecewise second derivative has finite variation including the boundary jumps. Periodize A with period m and evaluate the difference between the phases n+1 and zero. The constant term disappears; the term of frequency l≠0 has size at most m^(−1)|Â(l/m)|·2π|l|dist((n+1)/m,ℤ). Summing Σ|l|^(−2) proves the estimate. In particular all divisors of 2x+1 have zero response. Using Σ_(m≤y)Λ(m)≪y, the absolute error over all prime powers up to y≤x is O(y³/x²). Up to y=x^(5/6) it costs at most O(√x).

**Where a large error persists.** If 2x/3<m<x the response is exactly g(2m/x)−g((2x+1−m)/x). At r=m/x=1−δ the limit as x→∞ is g(2−2δ)−g(1+δ). If b=2π/log 2, the latter equals (b²/2)(1/√2−1)δ²+O(δ³). Choose a fixed interval of sufficiently small positive δ, separated from zero. On that interval R(p)≤−c<0 uniformly for large x; by the prime number theorem Σ log(p)|R(p)| there is ≫x. The approximation thus has an absolute error of linear order on a concrete band of primes. For the goal of 262 it remains to compensate the error at intermediate scales and to calibrate the continuous mass. The construction imposes the octave values on a deterministic endpoint and works at all its integers; the shift law of 266 is not used.
