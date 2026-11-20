# Bands chosen by a harmonic crossing of Möbius

Let H_D=Σ_{d≤D}μ(d)/d. There is an unconditional sequence of integers D→∞, selectable with rational arithmetic by |H_D|≤1/D. In *each* of the bands [D,D²] so chosen, the linear drift of the exact quadratic formula for the Mertens increments has modulus ≤1 on all subintervals. The diagonal of that formula costs at most D. What remains is to control the differences of a single off-diagonal term.

**Existence of the cut.** For H(x)=H_floor(x), the one-sided Mellin transform ∫₁∞H(x)x^(−s−1)dx is 1/[sζ(1+s)] in Re s>0. The origin is removable, and the real segment (−1,∞) is regular (ζ has no real zeros between 0 and 1). A nontrivial zero ρ gives a pole at ρ−1, with real part greater than −1. If H had constant weak sign from some point on, Landau, after removing a finite segment and changing sign if needed, would require a real singularity at the abscissa. That abscissa is ≤0 and ≥Reρ−1 by the pole. Contradiction. There are, therefore, both signs arbitrarily far out. If it passes through zero the bound already holds; if it changes sign directly, the value after the jump has modulus ≤1/D by the size of the jump. No frequency of these crossings is postulated.

**Local identity.** Let M₀(x)=Σ_{a≤x}μ(a), g=μ·1_{a≤D}, e=μ−g. By Dirichlet convolution, μ=2g−g*g*1+e*e*1, because μ*1 is the convolution unit. The last term only has support from (D+1)² on. For D≤u≤v≤D² the increment of 2g is zero and there remains exactly

    M₀(v)−M₀(u)=−(v−u)H_D² + Q_D(v)−Q_D(u),
    Q_D(x)=Σ_{a,b≤D} μ(a)μ(b){x/(ab)}.

The endpoints may be real. The diagonal part of the difference of Q_D costs ≤Σ_{a≤D}μ(a)²≤D; the bound holds simultaneously on all subintervals. At the above crossings the drift costs ≤D²H_D²≤1. Hence the supremum of the moduli of the increments of the off-diagonal term and L(D,D²) differ by at most D+1.

**Target that remains open.** By 133 it would suffice, along a subsequence of these crossings, to have a bound D^(1+o(1)) for the supremum of the off-diagonal differences. Under RH the bound holds at all crossings by the identity and the classical Mertens ceiling. The mere fact of crossing controls a single linear sum of the μ and does not give the required quadratic cancellation. For Θ>1/2, 133 implies that at all large crossings the off-diagonal supremum has exponent 2Θ+o(1) in D; the drift and the diagonal could not generate that excess.

**Cross-check.** The truncated inversion identity, the floors and the Landau argument are classical ingredients; see also R162_801 for the factorial record and 129–132 for the moment compensations. What is used here is the effective choice of the band of 133 through crossings of H_D in order to pay simultaneously the whole drift of the two-factor identity. It is a sequence with that partial property, not an already proved sequence of bands with all increments small.
