# Second crossing of the union and a finite cut below the square root

**Status: PROVED, with independent review of the double marking, the profile and the exact interpolation.**

With the z,E,J,L of 384 let y=exp(L/u) with u in an interior compact subset of (2,3). Then the balance W of all integers that have some prime >y satisfies uniformly

    W(y)=(JxE/L²)[log(u−1)−1/(u−1)+o(1)].

The profile changes sign at u₀=1+w where w log w=1 (u₀≈2.7632). It is the negative of the derivative, with the appropriate scale factor, of the Buchstab density on the range (2,3). The consequence for the exact arithmetic sum uses the moments of the frozen sieve of 384.

**Inclusion and exclusion.** Let T₁ and T₂ be the balances marked with j and binom(j,2), respectively, when there are j large primes. The integers with j≥3 cost O(x exp(−cL²)), even with marks polynomial in log n, since y³ exceeds x by a fixed power. Thus W=T₁−T₂ with that error. As in 385, T₁∼JxE/L² by the frozen moment, valid here since log y and L−log y are comparable to L. In T₂ two primes are extracted and the positive sign of the double marking remains, multiplied by the balance of the cofactor f of 384. Allowing p=q or a marked prime dividing the cofactor costs O(x L³/y) for n≤x² by g(log(x/n))≪x/n, the square factor >y² and the harmonic sum of the remaining factors. For n>x² the Gaussian tail with multiplicity O(log² n) suffices.

Replace both prime measures by dt/log t as in 380, now with f in the integrand: |f(v)|+|f'(v)|≪exp v allows integration by parts on [y,x²] at cost O(x L³ exp(−c√L)) after summing or integrating the other factor. Extending the upper limits only affects the Gaussian tail of negative argument. Hence

    T₂=x ∫ exp(−v) f(v) H₂(L−v) dv + o(x/L²),
    H₂(D)=log((D−b)/b)/D for D>2b, zero below; b=log y.

For |v|≤L^(1/10), the interval between L and L−v stays at distance ≫L from the break 2b, and H₂''=O(L^(−3)) there. Outside that range the negative tail and the bound of 384 for f on v≥L^(1/10) apply; H₂ is O(1/L) globally. The constant Taylor term integrates to zero and the linear one to JE H₂'(L). The remainder costs O(L^(−2.7)) after integration, as in 384. Thus T₂=JxE[L/(L−b)−log((L−b)/b)]/L²+o(xE/L²), and subtracting gives the formula.

**Exact reduction with a single fractional weight.** Choose two fixed endpoints of u on both sides of u₀ inside (2,3). The two contiguous states of the first crossing of W in the list of primes enclose zero. The jump is bounded by O(x/p), hence is o(xE/L²) in the whole band. The uniform profile forces log p/L→1/u₀. If W takes the value zero that cut suffices. Otherwise let λ∈(0,1) be such that (1−λ)W(p−)+λW(p)=0. The same convex combination of C(p−) and C(p) equals S exactly. In the Mellin representation its product is

    (1−λ p^(−s)) ∏_{z<q<p}(1−q^(−s)).

The largest prime here is x^(1/u₀+o(1)), with 1/u₀≈0.362. Unlike the cut near √x, the trivial cost of rounding λ can exceed the square root. The equality requires keeping the weight; computing it requires the two arithmetic balances W. The asymptotic localization of the crossing does not determine that weight. A sign ceiling for the new product is still missing.

**Review record.** The marking T₂ carries binom(j,2), so the extraction of two primes is divided by2 and uses exactly the density H₂ of380. The linear term H₂(L−v)=H₂(L)−vH₂'(L)+… integrates to+JEH₂'(L), since the frozen first moment is−JE. The derivative is H₂'(L)=[L/(L−b)−log((L−b)/b)]/L²; subtracting it from T₁ gives log(u−1)−1/(u−1), with the announced sign. For Buchstab, uω(u)=1+log(u−1) on(2,3), so the profile is exactly−u²ω'(u). The break D=2b stays at distance≍L from the Taylor point for u in an interior compact set, and the bounds on f of384 uniformly justify completing the two moments. Terms with repeated marks cost xL³/y and the three-prime tail has y³≥x^(1+c) with c>0 uniform on that compact set.

The selection only needs the extreme states to have opposite signs and each jump to be o(xE/L²); monotonicity of W in this new band is not assumed. In increasing order of the primes the extreme signs here go from positive to negative. The localization log p/L→1/u₀ follows from the uniqueness of the zero of the profile and its uniformity, also for the left state of the jump. Finally C(p−) has product A(s)=∏_{z<q<p}(1−q^(−s)), while C(p) has(1−p^(−s))A(s). The combination with the same weights1−λ,λ is therefore exactly(1−λp^(−s))A(s), without inverting the terminal weight. Its integral equals S since the interpolated W equals0; λ is not replaced by an asymptotic formula nor by an endpoint.
