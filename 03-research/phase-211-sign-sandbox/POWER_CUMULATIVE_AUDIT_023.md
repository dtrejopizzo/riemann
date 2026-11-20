# POWER CUMULATIVE AUDIT 023

Status: APPROVED conditional criterion, point128 and complete falsifier129. The universal hypothesis K≥0 is FALSIFIED. Papers untouched.

## 1. Primitive, mass and criterion — APPROVED

Reviewed `POWER_CUMULATIVE_INVERSE_022.md` (construction of round023) and `tools/power_cumulative_inverse_022_verify.py`. Independent run: PASS, including the complete intervals J128(1)∈(.665,.666), K128(1)∈(.003,.004) and the previous certificate h128(1)<−.66.

The formula J(x)=Σμ(m)w(mx) is the correct tail integral: the factor m of h cancels on integrating. The finite expansion of the polynomial in log x and log m proves uniform absolute convergence on x≥1 and the necessary decay. The double series of MASS is dominated by Σd(r)w(r), convergent with d(r)≤r; thus ΣJ(n)=1 is obtained without a positivity hypothesis.

K=J+xh=J−xJ′ gives (J/x)′=−K/x². Under the GLOBAL hypothesis K≥0, the limit J/x→0 implies J≥0 and J(x)≥xJ(n)/n on each [n−1,n]. The bound on the cell average is therefore valid.

Integration by parts of F/2=∫hB keeps B(1)=0 and the boundary JB→0. The jumps log n of B produce +log(n)J(n); the slopes produce −H_(n−1)∫J. All series converge absolutely. The bounds H_(n−1)−log n≥1−log2 and H_(n−1)/(2n)≤1/4 give the uniform constant log2−3/4. MASS together with J(n)≥0 implies 1−J(1)≥0. The conditional criterion F≤−2(3/4−log2)(1−J(1))≤0 is approved.

## 2. Kernel and certified point — APPROVED

D=33P−P′ has positive coefficients by the same recurrence020; K=x^−32Σμ(m)m^−32D(log x+log m). The application of the exterior lemma020 to D controls the COMPLETE sum, not prefixes. The POINT certificate uses K=J+h at x1 and sums both absolute tails; its intervals are correct. It gives no global K nor allows extrapolation in N.

Limited novelty: the criterion uses quantitatively the cell averages and the discrete mass1, tolerating negative h. The Möbius identities and integration by parts are classical antecedents; the global interior arithmetic compensation remains a premise, not a consequence of the reformulation.

## 3. Scope

Not even F≤0, should it be obtained, automatically compensates the ARCH_sharp deficit. The criterion and point128 certify neither W nor a new window T. The single neighboring point129 is reviewed below, without extending the test to a campaign.


## 4. Complete neighbor test129 — APPROVED

Reviewed `POWER_CUMULATIVE_TEST_023.md` and `tools/power_cumulative_test_023_verify.py`. Independent run PASS: −1/250<K129(1)<−1/251 and complete tail m≥65<10^−10. The rational recurrences correctly generate P129 and A129=32P129−P129′. The kernel evaluated is P+A=33P−P′, not A alone; at x1 no factor m or x is missing.

The computation of μ by factorization, the enclosed atanh logarithms and outward Horner are the same procedures audited022. The129 coefficients used are positive. For all degrees j≤128, log64>4≥j/32 ensures monotonicity from64; the positive integral from64 dominates the complete sum from65. The integral recurrence and the substitution log64<21/5 keep the direction. The sign is not inferred from the finite prefix.

The test refutes the UNIVERSAL hypothesis K_N(x)≥0 of the cumulative construction. The CELL theorem remains correct as a conditional implication; the positive point128 is not contradicted. The negative point129 implies neither J129<0, negative ERR nor negative W. It does not rule out a distinct integrated criterion controlling the adverse contribution. No new window T.

MASS, the cellular criterion with jumps and boundaries, OUT-K and the scope of POINT128 were reviewed independently, in agreement with this audit.

## 5. Final addition §7 of CUMULATIVE_INVERSE022 — APPROVED

Read the final section CB-ID/CB-POS/K-MASS/BOUNDARY. The formula J(x)=x∫_x∞K(t)t^−2dt keeps the limit at infinity and, by absolute Fubini, gives F=−2∫K C_B with C_B=−t^−2∫_1^t x dB(x). The jumps of B are included in this Stieltjes integral.

On complete cells, S(n)−S(n−1)≤−a n, a=3/4−log2, implies −S(n)/n²≥a/2 for n≥2. Between integers, the expression of C_B is a convex combination of C_B(n) and H_n/2, keeping the lower bound. On the initial cell C_B=(1−t^−2)/2; the formula is used for t<2 and does not eliminate the jump at2. CB-POS is correct.

Substituting J into MASS gives K-MASS with weight Σ_(n≤t)n/t²=floor(t)(floor(t)+1)/(2t²). The absolute convergence already proved allows swapping integral and sum despite the signs. That mass is not turned into a positive measure.

Finally C_B(t)≤t−1 on the first cell gives 2∫_1^(1+δ)K^-C_B≤δ²sup K^- for 0<δ≤1. The pointwise value at the endpoint2 does not alter the integral. The quadratic damping at the boundary does not by itself control the extent of the negative region nor the total adverse budget. The identities and bounds are approved, keeping open that balance and the compensation of ARCH_sharp. Confirmed in an independent review.
