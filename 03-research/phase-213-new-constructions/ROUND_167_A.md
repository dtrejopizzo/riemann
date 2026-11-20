# Critical precision of the weights on the actual primes

The energy of 162 and its Gaussian version of 166 tolerate any relative error O(p^(−1/2)) in the weight log p. On the other hand for each 1/2<β<1 there are relative changes O(p^(β−1)), on the same primes and vanishing on an arbitrary prefix, that preserve the counting and pair-sieve estimates of 163–165 but whose Gaussian average violates the ceiling of 166. This is an obstruction to deducing it from those estimates alone. No counterexample for the exact weights is inferred.

**Stability.** If |f(p)−1|≤C p^(−1/2), the difference in S(x) is O(√x) by bounded K, p≤exp(A)x and Chebyshev with partial summation. The difference in F(t) is O(exp(t/2)) by convolution. In both two-sided energy criteria the ceiling for one weight implies that for the other by the triangle inequality in L². This holds without assuming the ceiling for either of them.

**Arithmetic perturbation.** Fix P large, 0<ε<1/2 and τ>0, and put f(p)=1 up to P, and f(p)=1+εp^(β−1)cos(τ log p) beyond. One can choose τ above any prescribed height so that ζ(β+iτ)≠0 and B(β+iτ)≠0, by excluding discrete sets. Extend f to a positive completely multiplicative function. The convolution identity (fΛ)*f=f log is even preserved, term by term by Σ_{l|n}Λ(l)=log n. This is the twisted identity, distinct from the exact case f=1.

The change in θ(x) is O(x^β) by Chebyshev. Both pairs and diagonal remain on the same primes with comparable positive weights, and the relative weight tends to one on macroscopic intervals. Thus the main coefficient of the diagonal and the macroscopic limits of 162, the pigeonholes and the two-sided sieve of 165 are preserved (the bound on negative products uses only comparability). The unconditional ceiling of the smoothed sum in 164 also admits an O(x^β) perturbation.

**Observable effect.** Let D(s)=Σ_p log p p^(−s). For the modified prime sum the factor D of the Mellin transform becomes
    D(s)+(ε/2)[D(s+1−β−iτ)+D(s+1−β+iτ)]+entire,
where the entire part removes the prefix. At s=β+iτ there is a simple pole of residue ε/2, since D has residue one at 1 and is regular at 1+2iτ by the classical absence of zeros on Re s=1. The continuation at the points used comes from −ζ'/ζ by removing the higher powers, as in 153. Both B and the Gaussian multiplier are nonzero at that point. If the model satisfied 166, the interpolation proved there would imply holomorphy of the Mellin transform on Re s>1/2, a contradiction. This proves the failure for the individual model without assuming anything about the energy of the original weights.

The difference with respect to the original sum moreover admits the unconditional expression
    S_f(x)−S(x)=ε Re[B(β+iτ)x^(β+iτ)]+o(x^β).
Indeed use PNT scaled in p/x with profile t^(β−1+iτ)K(1/t), continuous down to zero by the decay of 160 and with bounded support. The integral is B(β+iτ) by Mellin. The size of the deviation does not come from a change in the set of primes nor from an error in counting individual gaps.

**Route decision.** Theorem B of R167_102_SIEVE_CONSTRUCTION already modulated Λ by a cosine to show limits of the sieve. Here the amplitude decreases, PNT and an arbitrary prefix are preserved, and the specific failure of 166 is obtained. Rounds 135–137 already built countermodels for Möbius observables; here the true prime support is kept and the stability threshold of the energy of 162/166 is located. The sieve estimate on pairs can close the size of the near block and still admit this oscillation. A closure along this route needs a property that uses the exact arithmetic normalization or directly excludes such oscillations. This result does not verify the ceiling on any additional block of the original sum.
