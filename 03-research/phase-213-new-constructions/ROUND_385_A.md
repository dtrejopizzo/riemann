# Quantified transition and cut that neutralizes the one-prime sector

**Status: PROVED, with independent review of the profile, the signs and the selection by jumps.**

Let L=log x, z=L², v=κ log z, y=exp((L−v)/2), and V(y) the balance of the integers with exactly one prime >y in the sieve of 368. For κ in any compact subset of (0,1), uniformly,

    V(y) = (J x log z/L²) (exp(γ)−4κ+o(1)).

Consequently at each sufficiently large x one can choose a threshold y with κ=exp(γ)/4+o(1) for which |V(y)|≤x^(1/2+o(1)). The lower admissibility cut is still z. The selection-by-jumps step has an antecedent in 303 for another sum; here the transition profile is computed in the parity sum of the exact cut.

**First marking.** Let T be the complete sum with each term multiplied by its number of primes >y. As in 384, T=−Σ_{p>y}f(L−log p) up to the correction for p|m when marking n=mp. For n≤x² this correction costs O(x L Σ_{p>y}1/p²)=O(xL/y) in absolute value, since g(log(x/n))≪x/n and one sums over p²|n. Above x² the Gaussian tail with multiplicity O(log n) suffices. The integral and the two moments of 384 give T=(1+o(1))JxE/L²: now its endpoint L−log y=(L+v)/2 stays in [0.4L,0.6L]. All costs of 384 are uniform there.

**Double marking.** Three primes >y give n≥y³ and cost O(x exp(−cL²)) even weighting by log³ n. With two large primes and cofactor different from one, n≥y² z=x z^(1−κ); by Gaussian dyadic summation over all integers the cost is O(x exp(−c(log z)²)), negligible even relative to x/L². Thus the balance with two large primes is, to the required order, the positive mass of semiprimes pq with p,q>y. Substituting the two prime measures by dt/log t as in 380 costs O(x L² exp(−c√L)), and the diagonal O(x/y). Set b=log y. The continuous density computed in 380 is H(D)=log((D−b)/b)/D for D>2b. The mass is

    x ∫_{u<v} exp(−u) g(u) H(L−u) du.

For |u|≤v/2 one has H(L−u)=2(v−u)/L² ·(1+O(v/L)), by 2b=L−v. For all u<v one has H(L−u)≤(v−u)/(2b²), by log(1+t)≤t. The Gaussian tails outside |u|≤v/2 are therefore o(v/L²) after integration. The integral equals (2J+o(1))v/L². The balance of exactly one prime is T minus twice this sector, with negligible error from three or more primes. The Mertens equivalent E∼exp(γ)log z gives the formula.

**Selection to square-root precision.** When crossing a single prime p the indicator of exactly one large prime changes only on multiples of p; the variation of the balance is ≤Σ_m g(log(x/(pm)))≪x/p by dyadic counting. Choose a fixed interval [κ₋,κ₊]⊂(0,1) containing exp(γ)/4 in its interior. At the endpoints there are opposite signs for all large x. Some pair of successive values of the balance encloses zero (or zero is attained); one has absolute value O(x/y_min)=O(√x z^(κ₊/2)). Since the profile is uniform, any value so chosen has κ=exp(γ)/4+o(1). Deleting that adaptive sector preserves the one-sided ceilings of power 1/2+ε. The cancellation between the sectors with zero and two large primes is still needed; their sum is not decided.

**Review record.** The first marking counts S₁+2S₂ up to the sectors of three or more large primes and the correction for p|m; the latter is of square-root size by xL/y and does not require 2log y to exceed L. The application of384 only reuses its frozen moments and its PNT substitution at the endpoint u=(L+v)/2∈[0.4L,0.6L], uniformly. For κ in a compact set[κ₋,κ₊]⊂(0,1), the tails with non-trivial cofactor have minimal separation (1−κ₊)log z and the semiprime core has v≥κ₋log z→∞. This justifies both uniform Gaussian truncations. The main semiprime integral is2Jv/L²; the second marking subtracts it twice and produces exactly−4κ, while Mertens contributes+exp(γ). Selecting the cut does not presuppose monotonicity of V: there is a finite number of states between the endpoints and some jump must cross0. Its two states are realizable by thresholds adjacent to p, respecting the strict inequality p>y. The maximal jump is O(√x z^(κ₊/2)), smaller than x log z/L² by a power of x; hence the uniform profile forces κ=exp(γ)/4+o(1). Neither a sign nor a square-root ceiling for the complete sum is obtained from this adaptive cut.
