# At the critical boundary the rows of each sign exceed the root margin

We use U_m, y, θ and B from 070. On the whole admissible boundary 1<B≤2, θ=1−B/2, control O(√x) by absolute values fails. If 1<B<2, for every sufficiently large x the mass of positive rows and the absolute value of the mass of negative rows each exceed
    
    √x exp(c log x / log log x)

for some constant c>0. If B=2, θ=0, the same bound is attained along sequences of fourth powers for each sign. The statements refer to the rows of the sector t_y(m)≤x^θ. One mass is not subtracted from the other.

Keep the physical interval [A,C] of 070 on which k₀ has constant sign and |k₀|≥c₀>0. In the following families the primes of the numerator tend uniformly to infinity and x/m belongs to that interval. By the exact identity of 070 each row equals μ(m)k₀(x/m).

**Large cofactor allowed.** Write L=log x, l=log L, f=B/2, y=L^B. Form s with k distinct primes in [y exp(−B),y]. Choose k of the desired parity as the smallest with k(B l−B)≥fL+|log A|. Thus
    
    k=fL/(B l−B)+O(1),    s≥x^f/A,    log s=fL+O(L/l).

For each s take all primes q in [x/(Cs),x/(As)]. The interval has fixed ratio >1, q≤x^θ, and its endpoints are x^(θ+o(1)), uniformly in s. Since θ>0, by PNT there are ≫x/(s L) primes there. They are larger than y and unique in the factorisation of m=sq. All constructed m have the same Möbius sign.

Let H=Σ_{y exp(−B)≤p≤y}1/p=(B+o(1))/log y by PNT and partial summation. Choosing k primes successively with weights 1/p, the maximal weight excluded at any step is k exp(B)/y=o(H). Therefore the sum of 1/s over distinct products is at least [H(1−o(1))]^k/k!. Stirling gives as a lower bound for the logarithm of the number of rows
    
    L−O(log L)+k[1+log(B/f)−l+o(1)].

Indeed log(H/k)=−l+log(B/f)+o(1). By the choice of k one has k(l−1)=L/2+O(l). The lower bound becomes L/2+k(log 2+o(1)). Changing the parity of k changes the sign of the family; the interval of q was chosen after s, so both families exist at the same x. This choice avoids the subexponential loss of a count at a ratio of powers like that of 070.

**Only small primes (B=2).** Here there is no adjusting prime q. Take an auxiliary scale X, L=log X, y=L² and k=L/(2 log L)+O(1) of prescribed parity. Form products s of k distinct primes in [y/16,y/2]. All satisfy log s∼L uniformly. Use weights 1/√p. Their sum by PNT is
     
    H∼2(1/√2−1/4) L/log y ∼ 2(1/√2−1/4) k.

The weight excluded at each step is at most 4k/√y=o(H); therefore Σ_s 1/√s≥[H(1−o(1))]^k/k!≥exp(c₁ k), since 2e(1/√2−1/4)>1. Split the range of s into O(log X) intervals of fixed ratio ρ<C/A. In one of them, [M,ρM], the sum of weights is ≥exp(c₂k) for fixed 0<c₂<c₁ and large X; this gives at least √M exp(c₂k) products. Choose x=j⁴ in [AρM,CM], as in 070. Then (log x)²∼y and all chosen primes lie below the threshold. The sign is fixed by the parity. The same x for both parities does not follow from this argument.

**Consequence.** For 1<B≤2 the strict condition θ<1−B/2 of 070 is exact for being able to remove the whole sector by summing absolute values at cost O(√x). In the equality case the factor that beats the root is subpolynomial, compatible with the limsup exponent 1/2 of 070. The signed balance of those masses and the sign of the whole form remain pending.
