# Which part of the odd correction escapes the verified height

We use the same ε and the same density of 150, without recalibrating them for a finite interval. Let E(T)=∫yp(y)U(T+y)dy. For T≥0 one has unconditionally

    E(T) = Σ mρ B(ρ) exp((ρ−1/2)T) + b exp(−T/2) + O(exp(−T)),
    b = (ξ'/ξ)(0)/(2ξ(1/2)).

Here the sum runs over distinct zeros of ξ. The even part of F equals a+O(exp(−T/2)). In particular, if H≥2 is a height up to which RH is known, then

    F(T) ≤ 3a/4 + C exp(−T/2)
                  + C (1+H)^A exp(T/2−πH/4)

with absolute constants independent of T,H and a<0. One may use H=3·10¹² by Z2 of paper 47. We give no certified numerical interval: the constants of the remainder have not been evaluated.

**Proof.** The transform of E is B(z)ξ'(z)/ξ(z) in the conventions of 150. Shift to Re z=−1/2. All zeros lie to the right of that line independently of RH. The local expansion of the logarithmic derivative and Stirling give at most polynomial growth of the factor without gamma on the line and on a sequence of horizontals avoiding the ordinates by ≫1/log(|t|+2). The gamma decay allows passing to the limit for each fixed T. The apparent pole at z=1/2 disappears by ξ'(1/2)=0. The simple pole of Γ(z/2) at zero has residue 2 and ζ(0)=−1/2, giving b. In the same strip B(z)cosh(z−1/2) contributes only the residue a at 1/2 and a term O(exp(−T/2)) at zero. The remaining integrals are O(exp(−T)). In all of 0≤Re z≤1 and for |Im z|≥2, Stirling and the polynomial growth of ζ in fixed strips give |B(z)|≤C(1+|Im z|)^A exp(−π|Im z|/4). The count by unit bands absorbs a logarithmic factor by increasing A. The series converges absolutely for fixed T. Its tail beyond H has the announced bound using Re ρ≤1. The part up to H, multiplied by ε, costs at most |a|/4 by the choice in 150. This proves the inequality.

**Scope.** For T≤(π/2−δ)H with fixed δ>0, the unknown contribution is bounded by C(1+H)^A exp(−δH/2). The parameter T of this computation is the logarithm of the Liouville scale, distinct from the support of the tests of paper 47. The fixed-height estimate loses strength when T grows without bound. The formula localizes exactly that failure even for multiple zeros and gives no global bound.
