# An off-diagonal quadratic Möbius criterion

We start from 054–055. Keep y=4x, L=√x, K=C₀ L(log x)² and choose D=cL/(log x)² with c fixed and sufficiently small. Define β=ε*ε=1*α, where * is divisor convolution. Put

    H(d,m)=(1/2) Σ_w β(w)V(dmw/y)[log(d/L)U(dw)+log(m/L)U(mw)].

The global sign is equivalent to an **upper bound** C L, uniform for large x=j⁴, of

    Σ_{d,m>D, d≠m} μ(d)μ(m) H(d,m).

Only d,m between D and C L(log x)² and w≤C(log x)⁴ intervene. The constants are fixed before varying x. Symmetry allows summing over d<m and multiplying by two. The coefficient β and the logarithm can change sign.

**Elimination of the small divisors.** For q>1, Λ(q)=−Σ_{d|q}μ(d)log(d/L). Choose C₀ sufficiently large and c sufficiently small so that the uniform bound of 055 for each bounded periodic model with d≤D is O(x⁻²). This follows from the exponential estimate of its last paragraph and from the estimate of the small rows: any power of saving can be fixed in advance by increasing the constants of the exponents, and using a sufficiently large fixed order in the quadrature of the complete model. Therefore in 054 the terms with d≤D cost in total O(D log x/x²) when testing each divisibility indicator separately. It is not necessary to take their common period.

After this subtraction the sum over q>L can be extended to all positive q. For the added q≤L the truncated arithmetic weight has absolute value ≤τ(q)log L, and there is no term at q=1. By 054 each row with U costs O((y/q)exp(−c₁√(K/(4q)))); summing with the trivial bound τ(q)≤q and choosing C₀ large gives o(1).

Write q=dh and w=hv. Summing α(v) over the divisors v of w produces β(w). The lower sum of 054 is then the negative of the quadratic sum with weight log(d/L)U(dw)V(dmw/y)β(w), with d>D and error O(L) or smaller. When U(dw)≠0, dw<eK, and the support of V forces m≥y/(16eK)>D by the choice of c. Also m≤By/D, d≤eK and w≤eK/D. Swapping d and m in this common domain and averaging gives H. The minus sign turns the lower bound of 054 into the upper bound of the statement.

**Computation of the diagonal.** Before excluding d=m its contribution is

    Σ_{d>D} μ(d)² log(d/L) Σ_w β(w)U(dw)V(d²w/y).

For W=y/d²≥1, the inner sum is O_N(W^(1−N/2)log(2W)) for each fixed integer N≥2. Indeed, put w=ab, β(w)=Σ_{ab=w} ε(a)ε(b); in smooth dyadic boxes of sizes A,B' with AB' comparable to W, alternating in the larger variable gains max(A,B')^(−N). The derivatives of U and V in that variable are bounded uniformly at the scale of the box by their logarithmic formulas and the support. There are only O(log(2W)) nonempty boxes. For W<1 the sum is O(1); it vanishes if d>2√B L, with B=16e. These estimates give O(L) after summing the absolute values over d **after** the cancellation in w. For example N=4 suffices when grouping d≤L into dyadic intervals.

More precisely the diagonal equals C_diag L+o(L), where

    C_diag=(1/ζ(2))∫₀^∞ log u · [Σ_w β(w)V(u²w/4)] du.

For u=d/L in a compact set away from zero only finitely many w appear and U(dw)=1 eventually, uniformly. The density of squarefree integers gives the limit of this weighted Riemann sum. The uniform estimates above control the tail u↓0 both in the sum and in the integral (the same proof works with U=1). The integral is understood with the sum over w inside. The elimination of the diagonal thus costs the permitted order. The signed bound off it remains pending.

**Cross-check.** The exact inversion of 040, the balanced cutoff of 049 and the progression estimate of 055 are reused. Möbius decompositions and symmetrisation are classical. The reduction here allows the two coefficients to be the same function μ on a common domain, and estimates its diagonal for this weight. No positivity of the symmetric kernel is inferred.
