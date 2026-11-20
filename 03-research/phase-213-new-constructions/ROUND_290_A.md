# Separation of nearby divisors by congruences and minimum rank cost

In the filter of 288 fix an odd prime P. For d≥1 assign the multiplicative mark

    c(d)=(d/P^v mod P, v mod 2),    v=v_P(d),

in the group (ℤ/Pℤ)^× × ℤ/2ℤ. In the original definition of Q add the indicator c(d)c(e)=c(n) inside the sum; keep putting zero outside the squarefree integers. Call the result Q_P. If κ≤√3 P then Q_P≥μ pointwise on n≤N and

    Σ_(n≤N)(Q_P(n)−μ(n)) ≪ √N/log log N,

with a constant independent of P. For κ≤P one obtains exactly μ. Thus power widths can be taken with P comparable to κ. The construction exchanges resolution in logarithms for resolution in arithmetic classes.

**Proof.** After replacing e by n/e, the mark requires c(d)=c(e). With the notation of 288, by cancellation in the group one requires c(a)=c(b). Since a,b are coprime and squarefree, the parity of v_P prevents exactly one of them from containing P. Hence both are units and a≡b mod P. Conversely these two conditions suffice. An active term with a<b has h=b−a a multiple of P and h√m<κ. For κ≤√3 P only h=P and m=1 or 2 remain. If m=2, a and b must be odd but their difference P is odd. The remaining terms have positive sign and only affect n=a(a+P), at most one unordered pair per n. If κ≤P not even that pair is active.

To sum the excess use the primes up to z=c log N as in 288. For p≠P there are two classes in which p divides a(a+P); for p=P there is only one. The average of the truncated product is ≤2∏_(p≤z)(1−1/p), since at most one factor changes and P≥3. Bounding the remainder of the period as in 288 proves uniformity. By orthogonality the mark is equivalent to an average of 2(P−1) characters of the group, inserting χ(c(d))χ(c(e)) overline(χ(c(n))) into the original expression. The correction of the factor P is necessary if P divides n.

**What it costs to suppress the semiprime barrier.** Consider any rule whose value on n=pq with p≠q large primes is

    1+(1/2)Wδ(log(p/q))⟨v_p,v_q⟩,

with real unit vectors in dimension r; one may afterwards add any correction that only increases that value until it majorizes μ. The equal/distinct marks are a special case, taking vectors from the orthonormal basis. If C r log N≤κ≤N^(1/4), the sum of excesses of the majorant on the semiprimes is ≫κ√N/(r log²N). Hence for κ=N^α a rank N^o(1) does not suffice in this class of rules.

Divide [.6√N,.8√N] into boxes of length ≤κ/10 and comparable to κ as in 289. Within each box Wδ≥1/2. For k primes in a box, their Gram matrix has trace k and rank ≤r, whence Σ_(i,j)⟨v_i,v_j⟩²≥k²/r. Moreover Σ_(i,j)⟨v_i,v_j⟩≥0, being the squared norm of the sum. Since |u|≥u² for |u|≤1, the sum of the positive parts of the entries is ≥k²/(2r). Removing the diagonal and passing to unordered pairs gives ≥k²/(4r)−k/2. On those pairs with positive inner product the forced excess is at least a quarter of the inner product. Summing over boxes and applying Cauchy to the number of primes per box, using only the ordinary PNT, gives the stated floor. Outside the boxes the final excess is nonnegative.

**Scope for the sign.** For 1≤κ≤N^(1/4) one can choose odd P with κ≤P≪κ+1 and obtain even pointwise equality using O(κ+1) characters. One can also work with P<κ≤√3 P and a majorant of square-root cost. The rank floor shows that compression to few vectors while keeping that precision would require a different mechanism on the semiprimes. The congruence restriction avoids the excess of 289; it does not yet give a signed estimate for the sum of Q_P nor enlarge the window T.
