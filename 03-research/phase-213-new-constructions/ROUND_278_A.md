# The part with small divisors already satisfies the square-root bound

For the scalar E of 275–277 use U=⌊√N⌋, Y=U/(C log²(2N)). There exists an explicit real weight B, equal to R at the integers of the band, with support [Y/2,U]. Take D=Y/(K log²(2N)) with K fixed and sufficiently large. Then unconditionally

    E(x)=−Σ_(l≤U/D) Σ_(D<d≤U/l) μ(d)log(d) B(ld) + O(U log⁵(2N)).

Only O(log⁴(2N)) values of the cofactor l appear in the pending term. The sign of 275 is equivalent to an UPPER BOUND of order x^(1/2+ε), for each ε>0, for the double sum written without the minus sign. The number of integers d in its inner sums is still large.

**Band weight.** For y≤U multiply the continuous function T of 276 by a cutoff that is zero up to Y/2 and one from Y on, of Gevrey order two like that of 274; for y>U put B=0. The extension is smooth at U: T(y)=w(y/x)=0 on the open interval (U,x), and T is smooth on both sides. On [Y/2,Y] the estimate of 276 gives |B|≪N^(−4) taking C sufficiently large from the outset. Thus ΣΛ(n)B(n)=E+O(N^(−2)), and ∫B=O(U log³(2N)) by 277.

**Distribution in progressions.** For every integer k≥0 the construction of 274 satisfies

    ||B^(k)||₁ ≤ x log⁴(2N) C₁^(k+1)(k!)² Y^(−k).

In detail, |S^(k)(t)|≪x log²(2N) C₂^(k+1)(k!)²/t^(k+1) for t≥U/4, and S is zero below. Indeed, in the inversion part there are O(x/t) summands at scale d/x≤2/t; if the cutoff is differentiated one is at t comparable to U. The same holds for the correctors by the bound on their amplitudes. In T(y)=Σ_l S(ly) each derivative gives l^k and the remaining sum costs Σ_(l≤2x/y)1/l. Multiplying by the cutoff at y comparable to Y and integrating using ∫_(Y/2)^U dy/y≪log(2N) gives the stated norm.

The optimized integration by parts of 274 gives |B̂(ξ)|≪x log⁴(2N) exp(−c√(Y|ξ|)). By periodization, for each integer 1≤d≤D and any residue a,

    |Σ_(n≡a mod d) B(n)−(1/d)∫B| ≪ N^(−5)/d.

The constant K is chosen to absorb x log⁴(2N) in the sum over nonzero frequencies. The error is uniform in a because its phase factors have modulus one.

**Arithmetic separation.** Use the elementary identity Λ(n)=−Σ_(d|n)μ(d)log d. For d≤D evaluate the progression a=0 with the above bound. This gives the term −(∫B)Σ_(d≤D)μ(d)log(d)/d plus error O(N^(−4)). Even by absolute summation of log(d)/d, the main term is O(U log⁵(2N)). For d>D interchange the two finite sums and write n=ld. This proves the statement. Unlike the relative balance of 277, the contribution of ALL divisors d≤D in this identity already has an absolute square-root bound with logarithmic factors. This precision has not been proved for the remaining divisors. The use of smoothing to shorten a sum already appears in 047; here it is applied to the progression of multiples within the arithmetic band, with the signed integral of 277 as the main term.
