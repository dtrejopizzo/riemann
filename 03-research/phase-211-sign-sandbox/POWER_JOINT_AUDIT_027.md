# POWER JOINT AUDIT 027

Status: DISCRETE_BALANCE027 and INTERIOR_CONSTRAINT027 APPROVED. Papers untouched.

## 1. Joint kernel and uniform inequality

Reviewed `POWER_DISCRETE_BALANCE_027.md` and `tools/power_discrete_balance_027_verify.py`; independent run PASS. The verifier was also reproduced separately and the proof reviewed.

SAMPLE and SCALES are exact identities by absolute inversion, with no new sign inequality by themselves. The FLOOR formula for Omega agrees with026: the cell part is H_n−(2L_n+T(n))/t² and each copy of the sharp part adds j[c+log((t+j)/(t−j))]/t². The logarithmic peaks are kept; uniform convergence to ell is not presupposed.

The sum/integral comparisons are correct: H_n≥log t+γ−2/t; the function ylog((t+y)/(t−y)) is increasing; the missing segment of lengthδ≤1/t costs at mostδ[log(2/δ)+1]. The upper bound of2L_n is obtained by integrating up to n+1≤t+1 and using log(t+1)≤log t+1/t. The negative sign of c−1 correctly reverses the comparison of T(n)/t². The constants give Omega≥ell−(4log t+9)/t; ell>1/50 and the endpoint4096 certify Omega>.009 for the whole tail, except at isolated singular points.

## 2. Joint tail of the real gamma kernel

The cut of026 gives G/4≤K≤7G/4 and G′/G≤−2/x; here the concrete gamma constraint is indeed used, not only two masses. For admissible T, both factors are positive and the joint lower bound (.009/4)∫G is valid.

For the majorant, Omega≤log t+1+t^−2Σjlog((t+j)/(t−j)). Integrating G(T)(T/t)² gives T(log T+2). In the logarithmic part positive terms are interchanged and each integral is enlarged up to j. The change t=jz produces j^−2 and the integral z^−4log((z+1)/(z−1)), less than2log2. Σj^−2<2 gives the constant3. The singularities are integrated correctly; their maximum is not sampled.

The rational evaluation of the single N129,T4096 proves0<R<10^−36 for the REAL joint tail. Use of the cut exp(2/3) of025 is valid: it follows directly from its logarithmic bound, even though its summary used the weaker cut2. The small upper bound of the lower certificate is not confused with a majorant of R.

## 3. Corpus and scope

The divisor/sampling identities are antecedents and do not suffice for the sign. The bump scheme cited as a generic limitation does not preserve the real gamma form and is not recorded as a falsifier of W. The specific progress is a complete one-sided inequality for the exterior joint contribution, with magnitude certified at one atom. It does not control its interior.

The deficit.15 of026 belongs to the comparator that guarantees only.66 of arithmetic benefit, not to the real interior value. The result W/C0=∫_1^4096K Omega+R,0<R<10^−36 leaves the first term without sign. There is no new W coverage nor window T.


## 4. Real gamma interior constraint — APPROVED

Reviewed `POWER_INTERIOR_CONSTRAINT_027.md` and `tools/power_interior_constraint_027_verify.py`; independent run PASS. The normalized heat mixture has V=β/G, G gamma with parameter N−1/2 and β=u²/4; its mean is u²/[4(N−3/2)]. The indicated Gaussian phi_v has norm one and autocorrelation exp(−vt²). The Levy, polar and comb contributions have nonnegative integrands before applying their signs. Tonelli identifies their expectations with those of the real rho, finite by its exponential decay; WG does not eliminate the complete form.

The hinge weight L≥0 and its two formulas are correct. The Jensen representation delta=t⁴∫exp(−at²)L(a)da preserves the first moment. Its mass Var(V)/2 is used only for N≥3; N2 has infinite mass without invalidating GAP for t≠0. The variance formula agrees with the inverse gamma law.

A_sharp is strictly concave and its mixture lies strictly BELOW the value at the mean. This upper comparison is not turned into a favorable lower bound. For the complete form, the second derivative R contains a positive polar part and negative ARCH/comb parts. The interchange of GAP with each piece is absolute: their integrals are the respective finite Jensen gaps of the original pieces. Thus JOINT-GAP is exact with no invented sign for R.

The negative curvature for v≥65536 is proved. The original Levy K(t)=e^(t/2)/sinh t satisfies K≥1/[2sinh(t/2)]≥1/(2t) for0<t≤1. Its curvature contribution is less than−1/(8v²) for v≥2. The polar part is less than24v^−5/2; the primes add nonpositive curvature. With sqrt v≥256 the total is strictly negative. The script certifies the constants; the analytic proof provides the whole range.

Global convexity of the complete Gaussian functional is refuted, not the sign of its average against the real law L_N nor that of W. The gamma mixture was known; what is different here is the explicit positive weight of the remainder and the check of the direction of the possible comparisons. Positivity of complete matrices is not inferred from the diagonals g_N.

## 5. Closure

The round uses real gamma constraints and keeps W complete in JOINT-TAIL and JOINT-GAP. Neither of the two inequalities yet controls the interior pairing. The isolated masses do not supply that condition, the negative comparator is not a negative W, and the negative curvature is not a refutation of every joint comparison. There is no new window T nor certified table coverage.


## Extension§8: mixture and Gaussian inverses

Mathematical and literal reviews APPROVED. It is verified that H_a=x^(-3/2)e^(-a log²x)(.5+2a logx)>0 for x>=1. Differentiation under MIX in128/129 admits domination by1+V_N. The positive sums ABS-H/ABS-J are finite by the gamma polynomials and the power m^-32. Fubini gives exactly h_N=E h_a and K_N=E K_a at x1, with COMPLETE inverses. The previous NEG128 andNEG129 force existences a_h,a_K, possibly different. Neither convexity of W, an arbitrary mixture nor a new numerical value is used. The scope does not affect NStieltjes norheatH_A-P.
