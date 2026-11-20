# POWER_STRIP_CUBIC_AUDIT_064

Status: **APPROVED** POWER_STRIP_CUBIC_NECESSITY_064, after rereading the project rules and a full reading of the source. Analytic proof; it requires no numerical tests. It only limits the declared uniform STRIP class. Papers untouched.

Antecedents cross-checked: index/grid/crossword, JOINT_SCALE016, STRIP_NECESSITY059 and UNIFORM_STRIP060. The effective difference relative to 059 is the use of a higher-degree numerator adapted to the exact Student weight, instead of the constant numerator. No global concentration is deduced from a Christoffel peak, and no unjustified complex Gaussian approximation is imported.

## Recurrence and degrees

The construction uses only degrees up to n+4 and moments up to n+5; all already exist under n>=4 and j>=10^6n. The Pearson boundary terms vanish. The subleading coefficient and beta_k of 060 remain correct in that extended range. For k<=n+4<=2n one has 2M−k>=2j and the two factors of the denominator are positive and at least j. Their majorants by 2M and M<=2j give exactly k/8<=beta_k<=4k.

Multiplying five times from degree d=n−1 requires MULT in input degrees up to n+3 and beta up to n+4, which are precisely those covered. The source does not use a recurrence outside its range of moments.

## Projection and constants

For R=e_d normalized, y²R′+yR has degree <=d+1 and is orthogonal to e_(d+3). The top component of y³e_d can only come from three raisings, so its coefficient is sqrt(beta_(d+1)beta_(d+2)beta_(d+3)). The lower bound exceeds n^(3/2)/24. The factor M/j>=1 keeps this bound for the leading term.

The rational decomposition SPLIT is exact. Its remainder has norm <=2·4^5(n+4)^(5/2)/j<=12288n^(5/2)/j. The hypotheses imply j>=589824n and allow this remainder to be paid by n^(3/2)/48. Reverse triangle inequality in a SINGLE unit projection proves ||AR||>=n^(3/2)/48. It is not assumed that the generator preserves the original space, nor are terms that could cancel inside it ignored.

## Real numerator and shift

The parity d of R ensures that p(z)=(z/a)^dR(a/z) has only nonnegative even powers and real coefficients. It is nonzero and of degree <n; P(s)=p(−is) is still real. The inverse change recovers exactly R and the norms of 060, without an extra factor 2. Hence ||H′||²/||H||²>=n³/(2304u²j).

Since p is real and even, P(iz)=P(−iz)=p(z), H is real on the line and the ORIGINAL analytic density is exactly H². This special property justifies converting its shifted modulus into the shifted norm² of H; that identification is not made for a generic complex numerator.

On every closed substrip of |Imz|<u, H and its derivatives have sufficient decay to differentiate and integrate by parts. N″(t)=4||H′(·+it)||² is correct. Both N and D(t)=||H′(·+it)||² are even, because H and H′ are real on the line. D is convex by D″=4||H″||²>=0, so D(t)>=D(0). Integrating twice yields N(eta)>=N(0)+2eta²||H′||². With the density H² one obtains the factor 1152 and exactly the LOWER of the source for each fixed height 0<eta<u.

## Refuted class and scope

For any p<3 and C>0, the integer sequence j_n=max(ceil(Cn^p),ceil(10^6n)) satisfies the construction hypotheses, belongs to the proposed cone and is o(n³). The STRIP lower bound diverges, ruling out a finite constant uniform in n, j and ALL numerators at that fixed height.

## Improvement of the construction threshold

After the first approval it was observed that the threshold 10^6n² was unnecessary. The SAME proof was revised step by step: only j>=n is used for M<=2j, j>=9 for 2j−9>=j, j>11/2 for the moments up to n+5, and j>=589824n for the remainder REM. The norm identity GEN requires at most j>=n+8; it is also covered. No shift step uses COARSE054 or a scalar contour that requires j>=10000n²: its integrability is verified directly by the analytic decay. Therefore LOWER is already valid for ALL j>=10^6n, without changing constants, object or lower bound. The approval of this audit includes that improved version.

It is not claimed that those tests have negative W, that their full arithmetic autocorrelations fail, nor that p>=3 is necessary for a W SIGN cone. Logarithmic optimality of 060 is not proved either. The result only excludes the uniform ABSOLUTE contour estimate described. Methods that keep signed cancellation and the interior problem remain open.
