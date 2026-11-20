# POWER CRITICAL AUDIT 040

Status: complete CRITICAL_BALANCE040 and verifier APPROVED. Papers untouched.

## 1. Corpus and difference

Re-consulted index, grid and crossword and the antecedents020/038/039. The main part of the Euler product and the floor formulas are classical. The difference040 is an expansion with explicit ABSOLUTE REMAINDER before inverting Fourier, small relative to the scale1/N of the complete inverse. It uses neither a formal series nor the divergent momentsA_sigma,B_sigma as if they remained controlled when delta drops toN^−2.

## 2. Local factor and complete inversion — APPROVED

Read `POWER_CRITICAL_BALANCE_040.md` in full. The floor identity for zeta(1+z) andH(0)=γ keeps the endpoints. On Re z≥0, the comparison ofI(z) withI(0) has modulus≤|z| andH−γ=−(I−I0)−zI(z), giving2|z|. The bounds|H|≤17/8 and|zH|≤17/64 control the geometric denominator. The explicit expressionR3=−z²(H−γ)+z³H²/(1+zH) gives the factor9 without resorting to a series without remainder.

The complete inverse product is kept at sigma1+delta>1, absolutely convergent. The uniform transform039 and its original gamma normalization are applicable. The multiplierz=delta−iξ inverts exactlyδf−f′ andδ²f−2δf′+f″, with correct signs.

In the band|ξ|≤1/16,|z|≤1/8 and|z|³≤2(δ³+|ξ|³). The Gaussian moments produce288δ³ and9·10^6/N^(3/2). Outside the band, the total multiplier is dominated by(4/δ)(1+ξ²); reservingN/4≥6 controls the integral and extractsexp(−N/10^6). The four auxiliary monomials sum to108692<110000; the factors√N/2 and2π leave the coefficient110000√N/δ. The tail is not missing nor is the conditionδ>0 removed.

## 3. Curvature and signs of scale1/N — APPROVED

With the positive weights ofP, t²q′=EJ−VarJ<d. ForS=q″+2q′/t, at every zeroS′=2q′[q′−(2d+1)/t²]<0. The algebraic expansion ofP givesS>0 at infinity, so there can be no earlier nonpositive value. Thus−2q′/t<q″<0 and the two SLOPE bounds are valid.

Direct differentiation of f gives the exact formulas for f′ and f″. At deltaN^−2, q<2, eta≤1/u² and t_v≥N/(2·992). The lower bound of f″ has3970/N=3968/N from the curvature term plus2/N from the quadratic term. The specific lower bound of f′ forc1/2 uses1/(1+δ+epsilon)≥1−2/N. SLOPE gives b>50/N with the declared loose bounds.

For N≥2^80, multiplying REMAINDER byN and using the sixth positive term of the exponential proves error<10^−4/N. At c3/2, the margin(γ−1/2)b leaves>3.5/N before errors; the negative costγδ² is kept. At c1/2, the upper bound has coefficient of b less than−.39, leaving a negative margin much larger than1/N. h/H<−1/N andK/G>1/N at the indicated tilted center, on their COMPLETE sums, are approved.

## 4. Scope

These are real opposite signs of the complete inverse near the energy center, not negative nor positive W. The shoulder039 and these bounds do not control the interior integral nor compensate ARCH_sharp by themselves. No new row or window T. All analytic steps were confirmed independently; the final verifier is recorded below.


## 5. Cutoff at constant distance — APPROVED

Read the final§8 and ran independently `tools/power_critical_balance_040_verify.py`: PASS for core and corollary. On ALLdelta∈[2000/N,1000/√N], the exact identities give0<f′<b and f″<−b becausev<1,q<2; the specific bounds for deltaN^−2 are not extrapolated without justification. With0<γ<1, the main part is bounded byδ−b−δ².

The cubic term is<.001δ; the other two errors are each<10^−4/N. For the tail, the boundδ^−1≤N/2000 and the sixth term of the exponential produce exactly55·6!·10^36/N^(7/2) after multiplying byN. Moreoverδ²<.001δ. The resulting lower bound(.998)δ−(u²+.0002)/N is strictly positive on the whole interval, with the constants checked rationally.

The monotonicity v→t_v covers the whole interval of centers and its upper endpoint coincides with the start of the shoulder039; hence the WHOLE later tail is controlled. The exact difference of the first center with respect to d/992 is dδ0(1985+δ0)/(992a_v)<5. h_N(e^t)>0 andK_N(e^t)>0 for ALLt≥(N−1)/992+5 and ALLN≥2^80 are approved. It is a sufficient cutoff, not an exact localization of the transition.

The result improves O(√N)039 to constant distance for the same complete inverses. The opposite central signs and this cutoff do not become a sign of the form W, of the interior pairing nor of a window T. No paper edits nor use of zeros/equivalence arguments.
