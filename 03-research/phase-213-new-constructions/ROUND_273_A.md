# Calibrated interpolation on both sides of a band of moduli

With N=⌊2x⌋, U=⌊√N⌋ and Y=⌊N^(1/3)⌋, there exists unconditionally a combination of variation O(√N log³(2N)) with entropy xh, exact at all integers m>U and at all prime powers q≤Y. It suffices to consider large N. The construction keeps the weight g of 257.

**Two discrete moments.** Let χ be smooth, zero up to 1/2 and one from 1 on. For t>0 form S₀(t)=χ(t/U)Σ_d μ(d)g(dt/x), extended by zero to t≤0. Add Aφ₁(t/U)+Bφ₂(t/U), with φ_i smooth nonnegative of integral one, supported respectively inside (1/4,1/3) and (2/3,3/4). Call the sum S. For w_j=j log j−(j−1)log(j−1), impose exactly

    Σ_j S(j)=0,      Σ_j S(j) w_j=xh       (j≥1).

On subtracting (log U+1) times the first row from the second, the columns of the two correctors, divided by U, converge to (1,∫φ_i(v)log v dv). The separated supports give different limits in the second component, so the inverse of the normalized matrix is bounded. Since |S₀(j)|≪x/j for U/2≤j≤N and w_j=O(log(2N)), one obtains |A|+|B|≪(x/U)log²(2N).

**Cost and entropy.** Take b_j=S(j)−S(j+1), 1≤j≤N. By telescoping the moments are Σ_j j b_j=0 and Σ_j (j log j)b_j=xh. The cyclic averaging of 261 converts Σ b_j F_j into rows at cost ≤2Σ|b_j|. Each summand of S₀ has variation O(1) by the product rule and only d≤4x/U are involved. The correctors therefore give total cost O((x/U)log²(2N)). The response is R(m)=Σ_(l≥1)S(lm). For m>U the sampling sees only the original inversion and gives g(m/x) exactly.

**Lower damping.** The third derivative of S, as a measure, has total variation K≪(x/U³)log²(2N). To see this, in the term with scale d/x the third derivative of g has measure norm O((d/x)²) after rescaling, since g is C¹ and g'' has bounded variation. The sum over d≤4x/U is O(x/U³). In the terms where χ is differentiated at least once, the integration is over an interval of length O(U); each derivative of order i≤2 of the copy of g is bounded by O((d/x)^i). Per term this costs O(U^(−2)) and there are O(x/U) terms. Each corrector costs O((|A|+|B|)/U²) in total.

By periodization of S, with |Ŝ(ξ)|≪K/|ξ|³, one has |R(m)−m^(−1)∫S|≪Km². The first discrete condition gives R(1)=0, whence |∫S|≪K. Consequently |R(m)|≪Km² also for the low moduli. The target there is zero.

**Repair preserving both ends.** Put r(q)=−R(q) at prime powers q≤Y and zero at the higher levels of each chain. Apply the consecutive differences of 271. They cost ≤2Σ_(q≤Y)|r(q)|≪KY³, even summing over all integers, and each added row has endpoint ≤Y. The change in entropy is O(KY³ log(2N)); the fixed relation of 262 corrects it at cost of the same order without affecting any prime atom, nor any modulus larger than U for large N. With the announced cutoffs the square-root budget results. Only the equations at the prime powers Y<q≤U remain. The simultaneous fit at both ends comes from the smoothness and the two discrete moments; the cost of 272 alone gave no control on the lower residue.
