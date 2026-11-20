# What a subset of authentic primes with unaltered weights can contribute

Let S be a subset of the primes, θ_S(x)=Σ_(p∈S,p≤x)log p, and C_(k,j)(S) the sample of 224 using only those primes, with weight exactly log p. For 1/2<β<1 and fixed j one obtains the extremal law

    sup_(S: θ_S(x)∼x^β) limsup_k log(1+|C_(k,j)(S)|)/k
        = j log M_(β−1/2)(3).

The upper bound holds even for θ_S(x)=O(x^β). At the extreme θ_S(x)=O_ε(x^(1/2+ε)) for every ε, the rate is zero by 224. Thus every part of that last size can be removed without changing the rates of the criterion. Just above the exponent 1/2 there exist subsets of density zero, with asymptotically regular count, whose removal produces spurious growth for j=1. There are no fractional weights nor change of position of the primes.

**Ceiling.** Take a=β−1/2>0, N=jk, m=log M_a(3). The contour a gives |c_N(log p;u)|≤Cu exp(Nm)p^(−a) by 208. Since 1/2+a=β, partial summation gives Σ_(p∈S,p≤X) (log p)p^(−β)≤C(1+log X). At the cut of 210 log X=O(N), so the sum of moduli, even before integrating over u≤N, costs poly(N) exp(Nm). This proves the ceiling.

**A base set with the prescribed count.** For large n let h(n)=n^β(log n)^(β−1). Its increment lies in (0,1) eventually. Include the prime of rank n in S₀ when floor h(n)>floor h(n−1). The number selected up to x is h(π(x))+O(1)∼x^β/log x by PNT. By partial summation θ_(S₀)(x)∼x^β, because the boundary term counts as x^β and the integral of π_(S₀)(t)/t is O(x^β/log x). Using S₀ allows a regular counting law to be kept throughout the construction.

**Interval with controlled phase.** With v=∂_a log M_a(3)>0, X=exp(Nv), L=Nv+d, consider the coefficient I_k(L) of the sample without (log p)/√p. The proof of 226, now with s=−√k+ik and k/N=1/j, gives uniformly for compact d

    N^(3/2) I_k(Nv+d)/(3^(s−1) exp(Nm−aNv))
       = exp(−ad)[K exp(iφ+ixd) J₊ + conjugate(K) exp(−iφ−ixd) J₋]/2 + o(1),

with φ=Nθ, x=x_a(3)>0 and J₊,J₋=3/[v(a∓ix)−i/j]. Indeed u=3+r/N produces exp(ir/(3j)) and the two branches of the profile of 212 give these integrals; the domination is C exp(−cr) because a is fixed. The cut does not cut the endpoint layer, since v≤m'_3(1/2)<2log M₁(3). The main function cannot vanish identically in d, for any phase φ, by independence of the two frequencies and nonzero coefficients. Compactness and uniform derivatives give a subinterval of fixed length inside d∈[0,1], and a complex projection direction, on which the whole profile has real part ≥c>0 (rotation after the common prefactor). The constants depend on j,β, not on k.

**Reaching the rate without altering weights.** On that interval take floor(X^β/(k log X)) distinct primes outside S₀. There are enough, since PNT gives ≫ X/log X uniformly on these subintervals of fixed length, while S₀ has O(X^β/log X) on the whole cell. If all are added, the change of sample has modulus ≥exp(Nm−o(k)): the terms project in the same direction, p^(−1/2) is comparable to X^(−1/2) and X^(β−1/2) cancels exp(−aNv). The cost in added logarithmic mass is O(X^β/k).

Choose successively ever larger k, with X above all previous cuts and the mass of the blocks already added ≤X^β/k. At each step there are two options: add the whole block or not add it. By the triangle inequality, some option leaves the modulus of the sample (including ALL of S₀ and the previous additions) at least half of the computed change. Fix that option; no future block affects the datum. The accumulated perturbation is o(y^β) at every height: during the block and until the next one, the accumulated mass is O(X^β/k) and y≥X. A single S is obtained with θ_S(y)∼y^β and with the announced limsup.

**Consequence for the authentic cancellation.** At j=1 the total over all primes has rate zero by 224. By linearity the complement of this S has the same positive limsup as S, although it keeps density one among the primes. In particular a cut that discards a density-zero family solely by its global count can destroy even a sample of rate zero already proved. What is new relative to 221, 223 and 226 is a partition of the authentic set, with the original weights and law θ_S(x)∼x^β, and the optimal exponent for that size. The construction chooses S depending on j,β and claims nothing similar for a concrete congruence class.
