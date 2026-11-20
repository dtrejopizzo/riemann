# There is an auxiliary crossing in every interval of sufficiently large fixed ratio

For the weight φ of 283 there exist finite constants C>1 and X₀ such that every [X,CX], X≥X₀, contains L with

    F(L)=Σ_n Λ(n)φ(n/L)−L=0.

The statement is unconditional and provides no numerical values for C,X₀. Consequently, for EACH large scale x of 280 the two tails can be eliminated as in 283, choosing L in [V,CV], V=x/U. The new diagonal cost and the discard of pairs with large greatest common divisor remain of square-root size. The auxiliary scalar no longer restricts the scales at which the pairs must be studied.

**If there is a zero to the right.** Fix one, ρ₀=β₀+iγ₀, and 1/2<σ<β₀. Ingham's density estimate used in 230 implies Σ_(Re ρ≥σ) 1/|Im ρ|<∞, since its exponent in height is strictly less than one. For each other zero with real part ≥σ take a probability on 0 and h=π/|Im ρ| with mass ratio mass(h)/mass(0)=exp(−h Re ρ). Its moment at exp(ρv) vanishes. The convolution of all of them is a probability on [0,H] with H=Σh finite. Convolving it with the uniform distribution on [0,H+2] gives a probability ν on [0,2H+2] whose density is 1/(H+2) on [H,H+2] except at endpoints. It preserves all the vanishings.

The smooth explicit formula gives F(exp t)=−Σ_ρ Hφ(ρ)exp(ρt)+O(1) for large t, with absolute summation over the multipliers Hφ. Integrating in t+v against ν one obtains O(exp(σt)). On the other hand, on any logarithmic interval of length one with large origin T one has

    ∫₀¹ |F(exp(T+v))|dv ≫ exp(β₀T).

For this second claim use the fixed complex filter f of 230 with support [0,1], integral one and vanishing moments at ρ−ρ₀ for all other values with Re ρ≥σ. Integrate f(v)exp(−ρ₀(T+v))F(exp(T+v))dv. What remains is −mult(ρ₀)Hφ(ρ₀)+o(1), nonzero by 275. The lower bound follows from the fixed sup norm of f. If F had constant sign on [exp t,exp(t+2H+2)], the modulus of the ν-average would be ≥(H+2)^(−1)∫_H^(H+1)|F(exp(t+v))|dv. This contradicts the two different exponents for all large t. By continuity the interval contains a crossing.

**If all zeros are critical.** In this case exp(−t/2)F(exp t)=P(t)+o(1), with P(t)=−Σ_ρ Hφ(ρ)exp(i Im(ρ)t), a real almost periodic function by absolute uniform convergence. Its mean is zero and its coefficient at the first ordinate is nonzero. Hence it takes strictly positive and strictly negative values: a nonnegative continuous almost periodic function with a positive value would have positive mean, since copies of a positive interval recur with bounded gaps. To justify this recurrence it suffices to approximate uniformly by a finite trigonometric sum; the simultaneous almost periods of its phases are relatively dense by compactness of the orbit closure in the torus. Thus there exist δ>0 and a fixed length B such that every interval of length B contains values of P greater than δ and less than −δ (increase B to include both). The o(1) error preserves the signs from some point on. Returning to the multiplicative scale concludes the proof.

**Use in 283.** There a root was chosen first and then x=2L². The exact compensation identity only requires F(L)=0, and its support, cost and low-frequency bounds only require L comparable to V. Now any large x is fixed first and its L is chosen afterwards. The condition on pairs remains open even along a single subsequence. The earlier crossings of 237–238 and the filters of 230 give partial antecedents; here a positive average that eliminates all zeros to the right of σ and a local filter that retains one of them are combined to obtain bounded logarithmic gaps between the crossings of the calibrating weight.
