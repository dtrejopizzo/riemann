# POWER_HIGHPASS_AUDIT_015 — Review of uniform eventual positivity and complete mixture

Status: PROVED. POWER_HIGHPASS_015.md and POWER_GEOMETRIC_TRANSFER_015.md reviewed in full. No numerical computation is required for their proofs. Papers untouched.

## 1. Rescaled Gram and uniformity in all coefficients

The substitution tau=sqrt(k)x and b_j=a_j k^(j/2) produces exactly the factor k^(N-1/2) in front of the norm². Weighting by e^(eta y) replaces s by -eta+i tau. The two constants are c_eta=(u-eta)^2 and d_eta=c_eta-eta²=u(u-2eta)>0, with 0<=eta<u/2. The powers of k, the shifted polynomial and all the factors of the GRAM formula are correct.

To justify uniformity, each of the N² entries is dominated independently of the coefficients. Near x0, writing y=x²+c_eta/k gives quotient^k<exp(-d_eta/y), and the product exp(-d_eta/y)y^-N is bounded for y>0. The shifted monomials are uniformly bounded on |x|<=1. On |x|>=1, each entry is dominated by C|x|^(i+j-2N), whose exponent is <=-2. This proves dominated convergence, also in L¹ for the matrix densities.

The limit matrix is positive definite because its weight is strictly positive away from 0 and a nonzero polynomial does not vanish almost everywhere. In fixed dimension N, the matrices converge in norm and their minimum/maximum eigenvalues stay uniformly bounded with the relevant sign. Since b depends invertibly on a for each k, this proves uniformity in EVERY numerator, even if its coefficients depend on k or the top-degree coefficient vanishes. No mere leading-term argument was used for that uniform part.

## 2. Archimedean form

The factor m(sqrt(k)x)-.5logk converges to log(|x|/(2pi)). The global bound by log(2+|tau|) and the comparability between 2/sqrt(k)+|x| and sqrt(x²+u²/k) produce C+|log y| near the origin. Its product with exp(-u²/y)y^-N remains bounded. Outside |x|<=1, the additional majorant 1+log|x| is integrable against |x|^-2. Thus the archimedean matrix, after subtracting .5logk times the norm matrix, has a finite limit in norm. Comparing it with the positive minimum of G0 proves ARCH/||f||²>=.5logk-C_N uniformly.

This step does not assume that the spectral measure of a fixed numerator controls the variable numerators: the matrix comparison is what provides this uniformity.

## 3. Complete comb and polar term

The correlation at a fixed time t>0 is obtained from the N² rescaled Fourier densities. Their L¹ limit is subtracted first; only afterwards is Riemann--Lebesgue used at frequency sqrt(k)t on each fixed limit density. Finiteness of N² and the positive minimum of G0 justify the convergence, uniform in the numerators, of the correlation quotient. RL is not applied directly to a moving sequence without that control.

The weighted limit matrix with 1/2<eta<u/2 gives a uniformly bounded weighted-norm quotient. Shifted Cauchy--Schwarz produces a majorant Cq^-eta for the normalized correlations. The series 2sum Lambda(q)q^(-eta-1/2) converges absolutely (Lambda<=logq suffices). Separating a finite segment and the dominated tail yields convergence to 0 of the COMPLETE comb, uniformly in P. No contribution was truncated without being estimated.

The polar term has the exact factor [-1/(4u²-1)]^k. The initial evaluations of the numerator are uniformly bounded in b and the norm² has lower bound c_N k^(1/2-N)||b||². Hence the polar quotient is <=C_N k^(N-1/2)(4u²-1)^-k and tends to 0 because u>1. The alternating signs are not needed for this bound.

The EVENTUAL theorem is proved: for each fixed N,u, there is K_N independent of P such that W>0 on ALL the subspaces Q^k V_N with k>=K_N.

## 4. Asymptotic constant for a fixed numerator

For fixed degree D, r=N-D, the limit integral over R is

    integral |x|^-2r exp(-u²/x²)dx=u^(1-2r)Gamma(r-1/2).

The Parseval factor 1/(2pi), the scale k^(1/2-r) and |a_D|² of the memo are correct. The same substitution t=u²/x² gives Elog|x|=logu-.5psi(r-.5); the symbol adds -log(2pi). The normalized comb and polar term tend to 0, so ASYM is the asymptotics of the complete W. The weighted ratio [u/(u-2eta)]^(r-.5) also agrees with the quotient of limit integrals.

## 5. Review of the final geometric mixture memo

POWER_GEOMETRIC_TRANSFER_015 was read in its complete version. Its residual indices agree with POWER_MIXTURE_AUDIT_015: the remainder is Q^(K+1)fv and its denominator has exponent N+K in s+u, besides s+v. The space X=H^t(R)+weighted L², although weaker than the weighted H^s norm proposed in that audit, is sufficient and its two contractions are verified directly via the multipliers on the corresponding lines.

Continuity of W controls arch, moments and the whole comb with their correct constants. Strong convergence removes the remainder and the uniform bound on the forms proves absolute convergence of the mixture. The normalized weights incorporate ||h_k||² and sum to 1 by the separate norm identity; functions and mixtures of forms are not confused.

In the product of filters all the H_j are contractions of X and commute with Q. This justifies absolute Fubini and the positive homogeneous weights w_k of the memo. The sum of the weights is 1, and the additional norms are the correct ones for a Rayleigh mixture.

## 6. Operational scope

TWO proved tools are obtained: the exact complete mixture and a complete high-pass tail uniformly positive for each fixed N. Together they reduce a SUFFICIENT transport condition for that N to the sign of a finite segment of initial blocks. No effective endpoint of that segment, nor its sign for all N, is yet provided. A mixture may contain negative initial terms; eventual positivity of its terms does not prove that the sum is nonnegative. Nothing in this approval closes the sign of all windows.
