# POWER_TWO_COPY_SCOPE_AUDIT_074

Status: **APPROVED** POWER_TWO_COPY_SCOPE_074 after a complete reading of seven sections and of the verifier. Independent reproduction: **exit 0/PASS**. Auxiliary counterexample to a generic implication, not to the real kernel Phi nor to W. Papers untouched.

Antecedents cross-checked: index/grid/crossword, SCHUR003 and THETA_TWO_COPY073. The earlier scalar counterexamples did not verify the full potential hypothesis 073. The declared difference is legitimate: keep that hypothesis, even with a strongly convex polynomial potential, and refute its automatic promotion to three generators.

## Initial jet and proof for x^6

The expansion of (M(u)+M(v))/(u+v) gives the coefficient matrix in degrees 0,1,2 written in the source. Its determinant is (−beta)(alpha gamma−beta²), and the smallest sum of degrees in rows and columns produces epsilon^6 by Vandermonde². Parity eliminates order 7. If kappa4<0, the leading-sign condition is exactly 3kappa2kappa6−10kappa4²; the factors 6 and 120 are correctly included.

For V=x^6, the Gamma moments and reflection give m4=2a², m6=1/6, kappa4=−a² and kappa6=1/6. The lower Taylor integral over [0,1] proves Gamma(1/6)>3sqrtpi; the rational comparison r²>11/14>pi/4 is correct. Therefore a<1/3 and the jet is positive. It is explicitly kept as a test that did NOT give the counterexample, without attributing to it a nonexistent negative sign.

## Potential, modes and means

V=A[x²/2+x^(2p)/(2p·2^(2p−2))], with the declared integers, is even analytic, superlinear and satisfies V″>=A and V‴>0 for all x>0. V is not changed between the three fields Ai.

The modes are the unique roots of v′(x)=i. The comparisons at 1−eta, 1, 2−eta, 2 are strict and valid: 2p−2>15, 2^15>20000, (p−1)eta>49 and exp49>49^4/24>40000. In particular 2exp(−49)<eta, not merely a decimal approximation. Modes 2 and 3 both lie in (2−eta,2), and the first in (1−eta,1).

Integration by parts of (x−xi) against the tilted density gives exactly E[(X−xi)(v′(X)−i)]=1/A. The boundaries and all terms are integrable by the even polynomial potential. Convexity v″>=1 produces the global quadratic bound and the mean error <=1/sqrtA=eta. No asymptotic Laplace expansion is used. Thus the three means are within 1/10000 of (1,2,2).

## Negative matrix and exact class

In the rescaled matrix B=A K, the denominator is i+j; hence the error of each entry is <1/10000. The vector (40,−40,3) was verified exactly: its energy on B0 is −6 and the maximal error loss is 6889/10000<1. The strict negative bound −53111/10000 and its division by A follow. The diagonals are positive because the means are positive. The Fraction verifier reproduces those comparisons and finished PASS independently.

Theorem 073 does apply to THIS V: all its pairs of positive nodes are positive definite and its tilted mean is strictly concave. The negative 3x3 block therefore refutes exactly the implication «potential hypothesis 073 ⇒ all 3x3 blocks positive». It does not refute 073, the positivity of ALL pairs of the real datum, or the possibility of exploiting an additional structure specific to Phi.

The form W is not evaluated, its arithmetic is not modified and no global impossibility is obtained. The potential of the counterexample is an explicit auxiliary that delimits the scope of the two-copy tool; it does not replace the theta kernel of the project.
