# Pairs sharing a large divisor already meet the square-root bound

With the Gram kernel G(d,e) of 281, for 1≤H≤V=x/U one has

    |lim_(L→∞) Σ_(d,e≤L; gcd(d,e)≥H) μ(d)μ(e)G(d,e)|
       ≪ (V²/H) log^C(2N)

with C absolute. In particular, fix H=V exp(−√log(2N)). That whole part, including the diagonal, costs x^(1/2+o(1)) unconditionally. Both indices can be arbitrarily large because of the calibration tail of 281. The bound uses cancellation in that tail.

**A progression of multiples in the Möbius variable.** Fix a sample y and write B_h(L)=Σ_(h|d≤L) μ(d)K_y(d). Uniformly in L and in h≥1,

    |B_h(L)| ≪ (V/h) log^C(2Nh).

Indeed, up to M=max(4V,2x/Y) each coefficient is bounded by O(log²(2N)) by 281. There are at most M/h multiples and M≪V log²(2N). Above M the local part disappears and, since χ(Vu/d)=0 for 1≤u≤2, the calibration formula is exactly K_y(d)=(V/d)(α_y+β_y log(d/V)), with |α_y|+|β_y|≪log²(2N).

If h is not squarefree, the sum is zero. Otherwise use μ(hj)=μ(h)μ(j)1_((j,h)=1). The partial sums of μ(j)1_((j,h)=1)/j and of the same sequence multiplied by log j are bounded, respectively, by O(log(2h)) and O(log²(2h)), independently of the endpoint. To see this, the restricted sequence is the convolution of μ with the indicator of the integers whose prime factors divide h. The two unrestricted partial sums are uniformly bounded by their convergence, recalled in 281. In the convolution, the sum of 1/r over those integers is ∏_(p|h)(1−1/p)^(−1)≤ζ(2)Σ_(r|rad h)1/r≪log(2h). For the weight log r one multiplies by Σ_(p|h)log(p)/(p−1)≤log h. This proves the uniform estimate, applicable also to differences of partial sums, and the convergence as L is sent to infinity by dominated convergence in r.

**Projection by greatest common divisor.** In a finite truncation the contribution of a single sample with gcd(d,e)=g is exactly Σ_(t≤L/g) μ(t) B_(gt)(L)² by divisor inversion. Hence the modulus of the sum over g≥H costs at most

    V² Σ_(g≥H,t≥1) log^C(2Ngt)/(g²t²) ≪ (V²/H)log^C(2NH),

absorbing logarithmic exponents into C. The last estimate follows by dyadic blocks in g/H and t. The same summable majorant, for fixed x, allows passing to the rectangular limit by dominated convergence. Summing over the O(log²N log log N) samples only changes C.

**Residue.** For H chosen above, the remaining terms have gcd(d,e)<H. Since both indices with nonzero coefficient are ≥V, the two coprime parts d/gcd(d,e) and e/gcd(d,e) exceed exp(√log(2N)). The one-sided bound of 281 is now needed only for that set. The diagonal lies entirely in the resolved part. The discard of 050 referred to a different bilinear form and used the squarefree part of the product. Here the projection onto multiples preserves the two infinite calibration tails and controls their joint signed contribution. The pairs whose common divisor is less than H remain to be estimated.
