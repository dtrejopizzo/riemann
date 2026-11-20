# Polynomial threshold for a counterexample on cells

Cross-check. 010 proves descent with profile-dependent error. P47 prop:nearfree already compresses the comb onto divisorial contacts and estimates by Schur with weights j⁻¹ᐟ². Here that control is applied to the jump of two consecutive replicas of any test on N cells, in order to choose a pair of replicas and a threshold uniform in the size N.

For H=N+1, define B=2 log H, R=2π exp(4) H², Q=⌈max(2H, HR(B+2−m(0)))⌉, d=log(1+1/Q), p=exp(−d/2). If r is the Rayleigh quotient of a nonzero primitive test F on the cells 1,...,N and

    r < τ_N := tanh(d/4)/N,

then U(f_Q+f_{Q+1}) has strictly negative energy, with f_q(x)=q⁻¹ᐟ²f(x/q). In particular the global sign requires that the smallest quotient of every nonempty primitive compression be ≥τ_N. The threshold is of order 1/(N⁴ log N) as N grows; no attempt is made to optimize the exponent.

**Exact jump.** Let a_j be the physical values of f, a_0=a_H=0. For g=V_dF−pF all nonzero pieces are copies of the same function −exp((u−d)/2)1_[0,d)(u), shifted to log j with coefficient √j(a_j−a_{j−1}). The supports are disjoint, since d<log(1+1/H). Thus ||g||²=(1−p²)J with J=Σ_{j=1}^H j|a_j−a_{j−1}|². Telescoping towards a_H and applying Cauchy–Schwarz, |a_i|²≤J Σ_{j=i+1}^H 1/j. Summing over i gives ||F||²≤NJ.

**Contacts.** A shift log n only connects two pulses if nj=l exactly: with 1≤l≤H every integer distinct from l is at logarithmic distance at least log(1+1/H) from l. For normalized pulses the compressed comb equals Λ(n)/√n at the two symmetric positions of the pair j,nj. The Schur weight j⁻¹ᐟ² gives in row j a weighted sum ≤Σ_{n≤H/j}Λ(n)/n+Σ_{n|j}Λ(n). The second is log j. For x≥1, with h=⌊x⌋, use ⌊h/n⌋≥h/(2n) when n≤h and Σ_{n≤h}Λ(n)⌊h/n⌋=log(h!) to bound the first by 2log x. Hence the norm is ≤B on these pulses.

**Floor and competitor.** By P47 lem:mbounds, m≥B+2 for |t|≥R and m≥m(0) for all t. The support of g has measure ≤Hd. The Fourier mass in [−R,R] with measure dt/(2π) is ≤RHd||g||²/π by Cauchy–Schwarz. With the choice of Q one gets (B+2−m(0))RHd/π≤1. The archimedean part dominates (B+1)||g||² and the full primitive form satisfies a(g)≥||g||². For the real crossing between F and V_dF, polarization gives the identity

    p a(F+V_dF)=(1+p)²a(F)−a(g).

The right-hand side is strictly negative if r<(1−p²)/(N(1+p)²)=τ_N. Translating by log Q gives the announced integer pair, with last possible cell (Q+1)H−1. The bounds Q of order H³ log H and tanh(d/4) of order 1/Q prove the rate. The estimate is conditional as a floor and unconditional as a construction rule starting from a certified violation. It does not establish that such a violation occurs nor that the continuous background of the same window has that floor. PROVED after independent mathematical audit.

## Threshold strengthened with the actual positions of the jumps

Adaptation of P47 prop:nearfree to the rectangular exponential pulses of 031. In the previous formulas Q can be replaced by ⌈e¹³ H log(2H)⌉ and the threshold by

    τ'_N = (1+log log(2H)) tanh(d/4)/N,     d=log(1+1/Q).

This gives order (log log N)/(N² log N) as N grows. The same explicit falsification rule is kept.

For the comb bound, ψ(x)=Σ_{n≤x}Λ(n)≤4(log 2)x for x≥1: each prime power in (h,2h] contributes its weight to log binom(2h,h), and summing over powers of two and rounding x up to the next power gives the bound. For h=⌊x⌋ the factorial identity implies h Σ_{n≤h}Λ(n)/n ≤ log(h!)+ψ(h). With the previous Schur weights this gives norm ≤log H+4log 2.

For a single pulse φ of length d normalized in L², ||φ||₁²≤d. P47 lem:mbounds gives m(t)≥log|t|−7 (use m(0)>−6 on |t|<1). When integrating log|dt| on its negative part, the estimate |φ̂|²≤d costs at most (1/π)∫₀¹−log u du=1/π. The archimedean diagonal is at least log(1/d)−7−1/π. For two pulses at distance u=|log(j/k)|≥|j−k|/H≥2d, the separated formula of P47 prop:nearfree and K(v)≤2/v give crossing of modulus ≤2d/u: the autocorrelation has L¹ norm ≤d and the kernel is evaluated at distance ≥u/2. (The bound for K follows from sinh(v/2)≥v/2 and cosh(v/2)≥v/2.) The off-diagonal archimedean row sums stay ≤4dH(1+log H)≤8e⁻¹³. This controls the block for arbitrary coefficients of the disjoint pulses. The arithmetic contacts remain exactly the divisorial ones.

Since log(1/d)≥13+log H+log log(2H), subtracting the previous bounds leaves a(g)≥(1+log log(2H))||g||² for H≥2. The polarization identity of 031 concludes. The improvement uses the geometric separation of the pulses and the sharp divisorial bound already present for other resonators in P47. The constants were chosen for simplicity. PROVED after independent mathematical audit.

## Threshold of order N⁻² with a second difference

The antecedent NEAR_CASES_RESULTS_2026_11_04 §1 removes the logarithm at the scale of smooth resonators fixed in advance. For the arbitrary test F of 031 one can manufacture a zero-mean pulse with two translations and recover control of F by two exact identities.

Take Q=⌈exp(13)H⌉, d=log(1+1/Q), p=exp(−d/2), V=V_d, g=(V−pI)F and h=(I−V)g. At each site log j the pulse of h is that of g minus a contiguous copy of it. It has zero mean, width 2d and squared norm twice that of the pulse of g. Since 2d<log(1+1/H), the sites are disjoint, the comb contacts remain exactly the divisorial ones and ||h||²=2(1−p²)J.

For its normalized pulse ψ, repeating the diagonal of 031 with width 2d gives floor log(1/d)−log 2−7−1/π. There remains the separated archimedean crossing at distance u≥1/H≥4d. One has ∫c_ψ=0, ||c_ψ||₁≤2d and support in [−2d,2d]. By decreasing convexity of the kernel K and K(x)≤2/x, |K'(x)|≤2K(x/2)/x≤8/x². In the separated integral subtract K(u) from K(u−v). The factor 1/2 of the crossing and the mean value theorem give bound 64d²/u². By u≥|j−k|/H and Σ_{n≥1} n⁻²≤2, the off-diagonal row sum is ≤256(dH)². The comb norm stays ≤log H+4log 2. Hence, after subtracting all these costs a floor ≥13−5log 2−7−1/π−256 exp(−26)>1 remains. Thus a(h)≥||h||².

If both tests Y₁=(I+V)F and Y₂=(I+V)g have nonnegative energy, then

    4(1+p)²a(F) ≥ 4a(g) = a(h)+a(Y₂) ≥ 2(1−p²)J,

using the identity of 031 for Y₁ in the first step. Hence the Rayleigh quotient of F is at or above

    τ''_N = tanh(d/4)/(2N),     Q=⌈exp(13)(N+1)⌉.

If the quotient is strictly smaller, at least one of those two tests has negative energy. Both are primitive and are realized on integer cells: translating by log Q² turns the factors 1, exp d and exp(2d) into Q², Q(Q+1) and (Q+1)² for the normalized replicas. The last possible cell is (Q+1)²H−1. The price of the threshold of order N⁻² is that three replicas may be needed and two energies compared; it is not the same two-replica competitor of the previous sections. PROVED after independent mathematical audit.

## What error scale on the jumps would preserve the sign

As a corollary of the cell approximation of 212-75 and of the reformulation of 212 ROUND_022_B, put β_N=max(0,sup(−a(Uf)/J_N(f))) over nonzero vectors of the N cells satisfying the two moments, with β_N=0 if there are no such vectors. Then the global sign is equivalent to liminf_{N→∞} β_N/N=0. In particular, a lower bound −o(N)J_N only on a cofinal subsequence would suffice. It is an equivalence; the sublinear estimate is not proved.

To see the decisive implication, if the sign fails choose f smooth real compactly supported in (0,b) with both moments zero and q=a(Uf)<0, by density in form norm. On the mesh of step 1/K sample by left endpoints f and two smooth corrector functions, all supported in an interior compact subset of (0,b). Choose the correctors with invertible matrix of the functionals ∫u dx, ∫u dx/x (for instance two positive bumps with separated supports). The two moments of the step approximations converge to the continuous ones with error O(1/K) by the mean value theorem. Solving the system of the two sampled moments gives coefficients O(1/K) that exactly repair the sampled profile.

Undoing the scaling, these repaired steps converge to f in form norm on a common compact logarithmic interval: they converge in L¹ and have uniformly bounded total variation, also after applying U. Their transforms are dominated by C/(1+|τ|); Plancherel weighted by log(2+|τ|) and dominated convergence suffice for the archimedean part, and the comb on that window is bounded. Dilating physically by K and multiplying by K^(−1/2) produces a vector on integer cells, with energy →q by invariance. Write f_K for f plus the two smooth correctors with their coefficients, before sampling. The identity

    K J_N = Σ_j (1/K)(j/K) |K(f_K(j/K)−f_K((j−1)/K))|²

and the uniform convergence of the derivatives give K J_N→I_f=∫x|f'(x)|²dx>0. Take K=⌊N/b⌋; the interior support allows filling the leftover cells with zero for all N sufficiently large. One obtains

    liminf β_N/N ≥ −q/(b I_f)>0.

In the direct sense β_N=0 under global positivity. The sublinear index of 025/026 counts dimensions and does not bound this energy quotient. The argument uses refinement and dilation of the smooth profile; adding zero cells to a single fixed vector would not produce the factor 1/N in J_N. PROVED after independent mathematical audit.
