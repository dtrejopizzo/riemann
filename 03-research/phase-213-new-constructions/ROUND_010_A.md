# Combinations of nearby translations of a step profile

Antecedents: BUILD084(1)–(2) signs lines of physical step profiles, P46 lem:transl gives the crossing matrix, and lem:mbounds and lem:compact provide growth of the symbol and boundedness of the comb on a fixed window. The operation here uses that all translations coincide up to a scalar outside tubes around the jumps. This allows handling cancellations of coefficients of arbitrary size. Targeted independent cross-check, with no claim of priority.

**Statement.** Let F(t)=exp(t/2)f(exp t), where f is a step function with finitely many jumps and compact support inside (0,∞). If the physical pole-free energy a(F) is strictly positive, there exists δ(F)>0 such that a is strictly positive on every nonzero vector of the span of V_d F, 0≤d≤δ(F). If F satisfies the primitive moments, the whole space satisfies them. Complex coefficients and any finite number of translations are allowed.

**Proof.** Fix a window containing the supports of the translations with 0≤d≤1, translating the set if necessary. The compressed comb is a bounded operator of norm B, being a finite sum of translations. We write a(g) as the integral of m|ĝ|² with measure dτ/(2π), minus the comb form. The real symbol has lower bound m₀ and tends to infinity as |τ| grows. Choose R with m≥B+2 outside [−R,R], taking m₀≤B+2. If g is supported on a set U of measure ℓ, Cauchy–Schwarz gives |ĝ|²≤ℓ||g||². By Plancherel

    a(g) ≥ [2−(B+2−m₀)Rℓ/π]||g||².

In particular a(g)≥||g||² for ℓ sufficiently small and g in the form domain, even if g does not satisfy the moments.

F is of bounded variation and compactly supported, so its transform is O((1+|τ|)⁻¹). Since m=O(log(2+|τ|)), the multiplier m applied to F lies in L². Subtracting the comb on the window we obtain h∈L² such that a(F,g)=〈h,g〉 for the g under consideration. Consequently |a(F,g)|≤||1_U h|| ||g||.

Let U be the union of the intervals [s,s+δ] where s runs over the logarithmic positions of the jumps, endpoints included. For 0≤d≤δ and outside U one has V_d F=exp(−d/2)F almost everywhere. Hence every combination Y is exactly cF+g, with c the sum of the coefficients weighted by exp(−d/2) and g supported on U. This g belongs to the domain by linearity. As δ tends to zero the measure of U tends to zero and ||1_U h|| tends to zero. Choose 0<δ≤1 so that the previous floor holds and ||1_U h||²<a(F). Then

    a(Y) ≥ a(F)|c|²−2||1_U h|| |c| ||g||+||g||².

The right-hand side is a positive definite form in (|c|,||g||). This proves the statement. Translations preserve the vanishing of both moments by P46 lem:transl.

**Scope.** BUILD084 allows applying the result to each f_k of that family, with k arbitrarily large. One obtains a radius that may depend on k. The proof uses the positive energy of the initial profile and the boundedness of the visible comb. Comparing translations with arbitrary separations and proving the sign of the full window remain pending. Status PROVED after independent mathematical review.

## Inertia of nearby replicas and application to BUILD084

Corollary for the amplification selection of the index after 212-84. Let F be a profile of this lemma with strictly negative energy for the weight considered. For any number r of distinct translations with shifts in a sufficiently short interval, the Gram has exactly one negative eigenvalue and r−1 positive ones. By common translation it suffices to consider [0,δ]. The translations are independent: the first left endpoint of the essential support leaves an interval where only the first profile intervenes and it is nonzero; iterate after removing it. The hyperplane of coefficients with Σc_j exp(−d_j/2)=0, of dimension r−1, produces functions supported in the small tubes of the previous proof. The floor there only requires finite norm of the visible comb and gives strict positivity. A single translation is negative. These dimensions exhaust the inertia.

With the same frozen profile of BUILD084 (16)–(17) and the same shifts one obtains, taking the smaller of the two radii, a positive definite Gram for Λ and one with exactly one negative for (11/10)Λ. In the latter case all diagonals are negative. This decides the inertia of a whole nearby group for every r without inverting matrices. The result restricts amplification by densification on a short interval; the interaction between separated groups remains open. In particular the amplification linear in T posed in the index, even if proved, is compatible with 026-A, whose majorant at the cell cut grows like X/(log X)² for T=(log(X+1))/2. PROVED after independent mathematical audit.

## Quantitative descent of the threshold of a profile by two translations

Let F be a real step profile in the physical variable as before, and a_c=A−cΠ the form with weights cΛ (Π is the comb contribution with its sign subtracted). Assume Π(F)>0. Write c*=A(F)/Π(F), J=Σ_s |F(s+)−F(s−)|², summing the jumps in the logarithmic variable. For Y_d=F+V_dF the individual threshold satisfies, as d tends to zero from the right,

    A(Y_d)/Π(Y_d) = c* − J d log(1/d)/(4Π(F)) + O_F(d).

The cross-check distinguishes this quotient from the minimal threshold over all profiles or windows of P46. The qualitative conclusion at c* also follows from the tubes of 010 and polarization; the leading term measures the descent.

Indeed, let H=V_dF−F. Separation of the jumps implies ||H||²=dJ+O_F(d²): on each interval [s,s+d) the difference is the jump with changed sign plus O_F(d); outside them the difference is O_F(d) on a support of bounded length. By bounded variation, |Ĥ(τ)|≤C_F min(d,1/(1+|τ|)) for 0<d<1/2, using the translation factor and the Fourier bound of F. P46 lem:mbounds gives m(τ)=log(2+|τ|)+O(1). By Plancherel,

    A(H)=log(1/d)||H||²+O_F(d).

To see the error, integrate the square of the bound on Ĥ against 1+|log(d(2+|τ|))|. With u=d(2+|τ|) one obtains at most C_F d times the finite integral of min(1,u⁻²)(1+|log u|) over (0,∞). On a fixed common window the comb is bounded, so Π(H)=O_F(d). The parallelogram law and translation invariance give a_{c*}(Y_d)=−a_{c*}(H)=−Jd log(1/d)+O_F(d), and Π(Y_d)=4Π(F)−Π(H)=4Π(F)+O_F(d). Dividing proves the formula.

BUILD084 (16)–(17) satisfies the hypothesis because a_1(F)>0>a_{1.1}(F); c* lies strictly between 1 and 1.1. For d sufficiently small the sum is also positive at c=1, by 010. The descent is local and preserves the two moments for primitive F. PROVED after independent mathematical audit.

## Local optimum over all positive averages of the fixed profile

Keep F real fixed with Π(F)>0 and write H_μ=∫V_sF dμ(s) for a probability on [0,δ], δ→0. This integral exists in form norm: translations are continuous in the Fourier norm with weight log(2+|τ|) by dominated convergence and the supports stay in a common window. For S,T independent with law μ and h=|S−T|, the quadratic variance identity and translation invariance give

    a_{c*}(H_μ)=−(1/2) E a_{c*}(V_hF−F),
    Π(H_μ)=Π(F)−(1/2) E Π(V_hF−F).

The identities follow by polarization and integration of continuous forms on that window. By the previous section, the first integrand on the right (before the factor −1/2) equals Jh log(1/h)+O_F(h), and the second O_F(h). At h=0 it is taken to be zero. The error of replacing h log(1/h) by h log(1/δ) lies between 0 and δ/e. Thus, uniformly in μ,

    A(H_μ)/Π(H_μ)=c*−[J/(2Π(F))] log(1/δ) E|S−T|+O_F(δ).

If G(t)=μ([0,t]), the identity |S−T|=∫|1_{S≤t}−1_{T≤t}| dt over [0,δ] gives E|S−T|=2∫G(t)(1−G(t))dt≤δ/2. The measure that splits its mass equally between 0 and δ attains equality. Hence the infimum over all these measures is

    c*−[J/(4Π(F))] δ log(1/δ)+O_F(δ).

The pair of endpoints attains the leading term. The formula admits atoms or continuous support and any number of successive positive averages of this F if their accumulated shifts stay in [0,δ]. It does not decide the exact minimizer at order δ.

In particular, for the F of BUILD084 and any ε between 0 and c*−1, choosing δ sufficiently small keeps all quotients above c*−ε. Even so there exist infinitely many strict descents within that budget. Starting from H_0=F form H_{n+1}=(H_n+V_d H_n)/2, choosing 0<d<δ2^(−n−1) small enough for the descent of the current profile and avoiding the finite set of differences between its jumps. Each H_n remains a step function in the physical variable, Π(H_n)>0 by the uniform bound on the denominator, and the two disjoint sets of jumps give J(H_{n+1})=J(H_n)/2. Their thresholds decrease to a limit ≥c*−ε>1. The choice of steps is existential. The behaviour with growing total diameter remains open. PROVED after independent mathematical audit.

## What a null test in a cell matrix would imply

Corollary of the previous jump expansion and of the integer replication of 212-75. Write λ=a(F)/||F||² for a fixed nonzero primitive physical profile, constant on the cells 1,...,N and zero outside. It may be taken real to decide the sign of the real matrix. Let f_q(x)=q^(−1/2)f(x/q) and Y_q=U(f_q+f_{q+1}). They are primitive tests on integer cells. Y_q reaches at most cell (q+1)(N+1)−1. Then

    a(Y_q)/||Y_q||² = λ − [J_F/(4||F||²)] (log q)/q + O_F(1/q).

Indeed, by common translation the computation corresponds to F+V_dF with d=log(1+1/q). The form a−λ||·||² vanishes at F. On H=V_dF−F, the expansion of 010 gives archimedean energy J_F d log(1/d)+O_F(d) and both the comb on the common window and the norm term cost O_F(d). By the parallelogram law the value of the shifted form at the sum is the opposite of the value at H. Its denominator is 4||F||²−||H||²=4||F||²+O_F(d). Substituting d gives the statement.

In particular, finding an exactly null energy at a nonzero primitive cell test would already suffice to refute the global sign: the consecutive replicas build strictly negative energies for q sufficiently large. By 212-75, positive definiteness of all finite physical matrices restricted to the moments is therefore equivalent to global semidefiniteness. Sufficiency uses the bridge of 212-75; strict necessity uses the jump cost J_F>0. No uniform bound on the required q is obtained when the profile changes. Cross-check with BUILD083 (136)–(137) and strict monotonicity in the window: the precision here is the cell test and its quantified descent. PROVED after independent mathematical audit.
