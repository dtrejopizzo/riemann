# How much of the cost of squares admits a divisibility certificate

Let 0≤λ≤1, S of 092 and U_λ(x)=S(x)+2λS(√x). A covering with weights a_n≥0 and cost Σa_n log n must pay at least U_λ if Σ_{p|n}a_n≥log(x/p) for each p≤x and Σ_{p²|n}a_n≥λlog(x/p²) for each p²≤x (in both sums n ranges). The claim follows from the factorization of each n. For real weights on n≤x the minimum is exactly U_λ: set a_(p²)=λlog(x/p²) and a_p=log(x/p)−a_(p²), taking zero for squares out of range. All are non-negative.

Let D=2+γ_E−log(4π). For λ<1−D/2 the eventual ceiling U_λ≤x is equivalent to the global sign. For λ≥1−(D/2)(1−1/392) that ceiling is FALSE unconditionally, even restricted to arbitrarily late scales. The width between the thresholds is D/784, less than 0.000060. The lower endpoint λ=1−D/2 remains open.

Indeed, without RH the ceiling would imply S≤x and contradicts 092. Under RH, with x=exp(2T),

    (U_λ(x)−x)/√x = −J(T)−2(1−λ)+o(1),

by 092 and PNT. Under this hypothesis J is almost periodic by absolute convergence of its series with real frequencies and |J|≤D. For the converse direction there exist arbitrarily large T at which J(T) approaches J(0), by simultaneous approximation of a finite number of phases to the identity and uniform control of the tail. At the identity,

    −J(0)=Σ (|ρ|^(−2)−½|ρ|^(−4)) > D(1−1/392),

since Reρ=1/2, |Imρ|>14 and Σ|ρ|⁻²=D. This forces excesses ≥c_λ√x along a sequence if λ reaches or exceeds the upper threshold. Without RH the normalized excesses of S are already unbounded by 092 and 088. The critical value as a supremum under RH is exactly 1−sup_T(−J(T))/2; contact at the boundary would require controlling the remainder.

**Application.** A covering that pays all the requirements of the squares in addition to the prime ones necessarily fails at root scale. The optimal covering above uses the primes themselves and does not give an independent construction with cost ≤x. Antecedents: 039 and 092 compute the bias of squares, 091 uses returns to the identity and 097 solves a different coprime maximum.

Update: [103](ROUND_103_A.md) keeps the term of the cubes and resolves the contact both at λ* under RH and at the explicit lower threshold.
