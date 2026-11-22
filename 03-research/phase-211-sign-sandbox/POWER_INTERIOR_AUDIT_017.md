# POWER_INTERIOR_AUDIT_017 — Review of the scalar table, complete row and quadratic cone

Status: the specific results reviewed below are PROVED; sign of the WHOLE scalar table still OPEN. Papers untouched.

## 1. Corpus and relative novelty

Reviewed index/grid/crossword and the E0/E_gamma antecedents: Paper46 lem:wit-conc, prop:Egamma-exact and rem:critical; phase188/L2_BUILD_008_GROUND_STATE_AND_T0, L2_BUILD_009_ARITHMETIC_INPUT_FOR_T0 and N_BUILD_013_E_GAMMA_C_COLLAPSES. The Tate chain of 008/009 concentrates at frequency 0 and recovers that same threshold C0+4; it did not provide new slack. The current row N1 moves to increasing frequencies as k grows, and the cone k~cN² has centre u sqrt(cN) and finite width. Its uniform control of the WHOLE arithmetic sum via a density shift, not separate time norms, changes an essential point of the previous argument.

The Bernstein instruments have concrete local antecedents in phase114/114_d_180_BERNSTEIN_DIRECTED_ENDPOINT_GATE§1 and phase72/E72_259_RATIONAL_BERNSTEIN_LM8_CERTIFICATE. Degree elevation and positive coefficients are not new. The bridge from rational densities to monomial atoms with explicit preservation of the polar term was not found in those antecedents. The novelty is limited to that exact application, not to a general principle of positive polynomials.

## 2. Scalar bridge 017: FORMAL review approved

POWER_SCALAR_BRIDGE_017 was read in full. For real P of degree<M, S(x)=P(i sqrtx)P(-i sqrtx) is a real nonnegative polynomial on x>=0, with all crossings already included. The formula R(q) with respect to the common weight F1 has degree<=M-1 and extends nonnegatively to [0,1]; if degP=M-1, the final value is exactly the square of its leading coefficient, with the factors of u correctly cancelled.

The Bernstein expansion of degree D is EXACT. The uniform bound l(l-1)/(2D) on the quotient of falling factorials is proved by conditioning on non-repetition: the two probabilities differ by at most the probability of some collision. D>=degree guarantees that this condition has positive probability. Therefore the explicit threshold D>C_R/epsilon does produce strictly positive coefficients, including the extremes.

Each factor q^j(1-q)^(D-j)|F1|² is the density of a positive multiple of the atom h_(D+1-j,j), whose index N is always >=1. The rational identity in x is legitimately evaluated at x=-1/4 because u>1 and there is no pole there. Multiplying by 2 produces EXACTLY the equality of polar terms, even though q is negative at that point. The contact sums of each function are absolutely convergent and the identity is finite; no limit in D is interchanged with a series without a majorant.

Thus W[f]+epsilon W[f1] is a sum of atomic values with positive coefficients. If ALL atoms have nonnegative sign, epsilon->0 implies W[f]>=0. Neither uniformity of the norms of the atoms nor strong approximation of the functions is needed. The argument also extracts a finite negative atom from any hypothetical negative direction, as the memo states.

Conclusion: unlike a mere list of positive diagonals, this special family of ALL pairs (N,k) does control complete matrices through a conic representation of DENSITIES that retains their crossings. This is not claimed for a single row, a partial cone or a union of vectors. The moment obstruction 016 remains correct because there functions were approximated, not these combinations of autocorrelations. The antecedents 114/72 were explicitly added to the main memo.

## 3. The whole row N1: certificate reviewed and reproduced

POWER_INTERIOR_017§§1–6 and tools/power_interior_017_verify.py: APPROVED; script run with PASS. The generating function of weighted norms is the exact geometric integral 1/[2sqrt((1-z)(a²-b²z))]. Its coefficients and the inequality c_(k-j)c_j<=c_k by Vandermonde produce the quotient (u-eta)/(u-2eta), uniform in ALL k. With eta15 its maximum for u>=31.5 is 11.

The archimedean monotonicity by reweighted covariance and the bound psi16-logpi>3/2 are correct. The exact polar term has an alternating factor and its worst normalized magnitude is bounded by 63/496 using c_k>=2^-k. The COMPLETE comb is controlled by 2sqrt11<7, Lambda<=q and the sum q^-14; the cost 105/(13*2^14)<1/2000 keeps all contacts. The final subtraction is 42547/31000>4/3.

W[h_(1,k)]>(4/3)||h_(1,k)||² is proved for ALL k>=0, u>=31.5. It is a genuine infinite row; it does not prove the rows N>=2.

## 4. Additional WRN: effective constant per row, without threshold in k

INTERIOR017§7 is also APPROVED. Expanding (tau²+b²)^k and applying beta gives the declared factors and powers a^(1-2N). The quotient of beta coefficients factors exactly as [c_(k-l)c_l/c_k]B_l^(N), with B_l^(N)=prod_(r0..N-2)(2l+2r+1)/(2r+1). Vandermonde removes only the bracket and leaves a positive series convergent for rho<1.

The operator prod(2rho d/drho+2r+1)/(2r+1) on (1-rho)^-1 reproduces that series exactly; hence S_N is rational and computable through finitely many operations. For N1 it recovers the previous bound. WRN controls the complete comb uniformly in k for each N, but its increasing dependence on N is not a proof of the sign of all rows nor does it contradict the weight lower bounds of 016.

## 5. Quadratic cone: audit of STRIP and of its constant

POWER_QUADRATIC_017 was read in full. The modulus identity after y=sqrt(x²+1) is exact: the denominator has square (u²+y²)^2-4u². The main Jacobian <=2 and M<=2k give exp(kT²/100) with the correct constant. Under the real density, T has beta(N-.5,k+.5).

The part T<=4N/k costs exp(4/(25c)). On the other part, changing the weight by (1-T)^(-k/100) gives the beta with a'=.99k+.5. The ratio of normalizers is bounded by exp(N²/k)(100/99)^N: the Gamma upper bound comes from psi<=log, and the Gamma lower bound from Jensen for x^b, with b=N-.5>=1.5. Markov for the integer moment N gives (50/99)^N. The product (5000/9801)^N<1 and k>=cN² produce the declared constant.

The lower beta bound of the small region is obtained by integrating T∈[N/(2k),N/k], with T^(N-1.5) increasing and (1-N/k)^k>=exp(-2N). The majorant of that region is (4/u)A^N r^k(2k/N)^(N-.5)e^(2N). For k/N>=4, log(2k/N)<k/N and 18^N<3^k justify the bound < (4/u)(9r)^k<1. All inequalities are valid for N>=2, k>=max(cN²,4N).

The rational density is holomorphic on the pole-free strip and its vertical sides vanish by O(|z|^-2N). The shift gives CORR with C(c)e^(-|t|). This is NOT a uniform weighted time norm of F; it shifts the complete analytic product of the density and does not contradict 016.

## 6. Quadratic cone: complete comb, polar term and eventual sign

CORR dominates the whole sum by 2C(c)sum Lambda(q)q^-1.5<14C(c); the majorant converges and its constant is valid by integral comparison. The beta formula for Elog and the bounds psi(x)>=logx-1/x, psi(x)<=logx give ARCH>=.5logN+log(u sqrt(c)/(2pi))-5. An appendix was added to the memo with the elementary proof of the lower bound m>=log(|tau|/(2pi))-4, checked from the total variation of x/(x²+t²). Thus that input does not remain as an unproved citation.

The normalized polar magnitude has the exact factor and beta of the memo. The same beta lower bound of §5 and 9/3968<1/400 give POL<400^-k. Eventual positivity for P1 is proved on the WHOLE cone k>=cN², N>=N0(c), with an explicitly boundable N0. No favourable sign of the contacts is presupposed and their tails have not been omitted.

## 7. Gaussian profile and passage to the WHOLE series

The independent Gamma representation X,Y is correct. On the event of quotients inside [1/2,3/2], the quadratic Taylor remainder has expectation O(N^-1/2) after multiplying by the scale sqrtN. The linear term in X is also O(N^-1/2). The complement has probability O(N^-2) by fourth moments; Cauchy--Schwarz and E tau²=O(N) give the same error. The exact Gamma characteristic function produces the amplitude exp(-u²ct²/8), with error O_T(N^-1/2). Its constant and the centre mu_N are correct.

To pass the approximation to the complete series, CORR independent of GAUSS and the summable Gaussian majorant are used. Separating finitely many contacts and two uniformly summable tails justifies ALL even when mu_N oscillates. The modulated series is not declared to vanish.

The stronger precision initially mentioned for the symbol is not necessary. It was replaced by the bound already proved in Paper46, lem:mbounds: |m-log(|tau|/(2pi))|<=1/|tau|+1/(2tau²). Since E tau^-2=O1/N, its expectation is O(N^-1/2), sufficient for PROFILE. The sign and factor 2 of the arithmetic contribution in PROFILE agree with W=ARCH+POLAR+Comb.

## 8. Approved final scope

The COMPLETE scalar table would be sufficient by the new Bernstein bridge. Its row N1 and an eventual quadratic region have been proved, not the WHOLE table. In particular none of these results certifies an additional window of Paper46 beyond the range already declared: to transfer them to all tests, that sufficient condition must be completed. No sign proof for all numerators in the quadratic cone is claimed, nor an extension of T from these particular families.

## 9. SEPARATE audited extension: explicit cone from N2

POWER_QUADRATIC_EXPLICIT_017.md and tools/power_quadratic_explicit_017_verify.py were reviewed separately and the script was run with PASS. The band eta15<u/2 is admissible. The modulus identity has a400/441, and the two DIFFERENT estimates of the factor are correct: exp(5kT²) for the small-T part, and (1-T)^(-k/2) for the tail, keeping the convexity of the original logarithm. The too-weak first bound exp(5kT) is not used on the tail.

The threshold 32N/k produces exp(64/125)<=125/61. The normalizing beta ratio is <=exp(N²/k)2^N and Markov for the moment N contributes (1/8)^N, leaving exp(1/10000)(1/4)^N<=625/9999. The main Jacobian is <2 when splitting at |x|>=eta. On the complementary region, the prefactor 2eta/u, A441/341, r200/341 and the lower beta bound of 017 have their correct factors. For t=k/N>=100, t/4-log(2t) is increasing and its initial value exceeds logA+2; hence the remaining growth is <exp(k/4). The inequality log(5/3)>1/2 and r<3/5 leave a contribution <exp(-k/4)<1/100. This gives normalized shifted integral <5 and CORR15 for all t.

The infinite tail of contacts is <1/1000 using Lambda<=q and the sum q^-14. For ARCH, k/N>=10000N implies sqrt(k/N)>100; pi<4 and e<3 give u*100/8>3^5>exp5, so the global lower bound of 017 produces ARCH>.99. The polar term 400^-k is <.001 on the whole domain. The final subtraction >.988>.98 is correct.

W>(49/50)||f||² is approved for ALL N>=2, k>=10000N², u31.5, P1. It is an explicit scalar region and not a theorem for all numerators of each block. Nor does it decide the remaining part of the scalar table or, by itself, a new window T of Paper46. This extension neither replaces nor modifies the hypotheses of the main theorem of §§5–7.
