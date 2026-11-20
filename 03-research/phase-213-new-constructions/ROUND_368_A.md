# A single comparison of parities, with cut and width fixed by x

Let y(x)=(log x)² for x≥e and g(u)=exp(u/2)φ₁(u). Put

    S^*(x;z)=Σ_{n without prime factors ≤z} μ(n) g(log(x/n)).

n=1 is included. Then **RH is equivalent to S^*(x;y(x))<0 for all sufficiently large x**. Even the weak inequality ≤0 suffices. Among squarefree integers without small primes the masses with odd and even number of primes are compared, without an exterior label log p. The exact cut and a single constant variance are used.

**Under RH.** The computation of 367 applies with the same K and the same Euler product, but the remaining factor is now F(s)=1/ζ(s), instead of B_z(s). At the real saddle F→1/ζ(1/2)<0. The local domination by the Gaussian, the intermediate damping by primes between z/2 and z and the ceiling for F under RH are the same as in 367. Hence S^*∼exp(K(s₀))/(ζ(1/2)√(2πK''(s₀))) at the cut z=y(x). In particular it is eventually strictly negative.

**Extending an inequality without paying for branches of arbitrary signs.** Suppose only S^*(t;y(t))≤0 for t≥t₀>e. For large x and y(x)≤z≤4y(x), change the frozen cut z to w=y(x) by the identity

    S^*(x;z)=Σ_{d with all its primes in (w,z]} S^*(x/d;w).

It includes powers and all transport coefficients are +1. It comes from the Euler identity of 358 and converges absolutely by Gaussian decay. When descending, stop the children with t<t₀ and, for the others, repeat only if the inherited cut exceeds y(t). The large leaves with correct cut are nonpositive; a branch with factor 1 terminates and each other step reduces the scale by at least half. For each total D there is at most one terminal branch: given the scale, the factor of that step must absorb all pending powers of D in the band of primes just opened, which will never reappear. This also holds when stopping at a small leaf. The depth is finite for fixed x; although a two-sided expansion has infinitely many small children, their absolute sums converge.

At the small leaves |S^*(t;U)|≪_(σ,t₀) t^σ for every σ>1/2, uniformly in the set of removed primes, by absolute counting and the Gaussian decay as t→0. Summing their costs, for 1/2<σ<1 one gets

    S^*(x;z) ≤ C x^σ ∏_{p≤z}(1−p^(−σ))^(−1) = x^(σ+o(1)) O(1).

Thus the sign at a single cut alone produces a one-sided ceiling O_η(x^(1/2+η)) on the whole corridor, for any η>0. The choice of μ without exterior prime is important: in this expansion there is no correcting term of the other sign.

**The ceiling prevents any exterior zero.** For v=log x fix z=2v². Convolve e^(−u/2)S^*(e^u;z) in u with φ_(av−1)(u−v), as in 367. One obtains the normalized diffusive average of the same unlabelled coefficients. On |u−v|≤v/5 the previous ceiling can be applied with any η>0, with upper cost O(exp(6ηv/5)); outside it the absolute cost is exponentially small for fixed 0<a<1/1000 by the same Gaussian bound of 367. Hence the unnormalized diffusive average has a one-sided ceiling x^(1/2+o(1)) in the sense of each fixed positive loss.

If there is a zero with β>1/2, choose one and take a>0 small enough that Re Φ_a(ρ)>1/2. The excursion proof of 365 applies to F(s)E_z(s), with z=2(log x)². To make the change explicit, at a zero of multiplicity m the pole has order m, and the amplitude in the block x=X exp(u) is X^Φ_a(ρ) E_(2(log X)²)(ρ) (log X)^(m−1) times a nonzero constant: the constant is m Φ_a'(ρ)^(m−1)/ζ^(m)(ρ). The relative control on the circle of radius 1/log X does not change; varying the cut in the block adds O(log X) candidates. The contour of 365 bounds the rest and its positive measure annihilates the complex modes. In particular **positive** excursions of size X^(M−o(1)) with M>1/2 are obtained, contradicting the ceiling. This concludes the inverse implication.

**Scope.** 367 employs all cuts of a corridor and weights the exterior prime. Here no uniformity in any parameter other than x is required. The one-sided estimate is transported because the successive bands of primes are disjoint and their transfer factors are positive. What is pending is an arithmetic proof of the eventual parity inequality; the saddle equivalent by itself requires RH when shifting the contour.
