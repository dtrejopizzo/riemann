# POWER_THETA_AUDIT_073 — Theta hazard, two copies and all real pairs

Status: **APPROVED** the assembly of POWER_THETA_HAZARD_COMPACT_073, the exterior range 10343 and POWER_THETA_TWO_COPY_073. Independent reproduction of the compact certificate: **exit0/PASS, 4096 panels**. Papers and phase 103 untouched.

Consulted the project rules, index/grid/crossword, CONE001, BRIDGE002, SCHUR003 and the antecedents 10334/10339/10342/10343. The targeted search did not previously find L''<0 and L−(a−1/2)L'>0 on ALL a>1, nor the closure of ALL pairs of powers in that range. CONE001 left that range below 32 open. The later high-rate blocks do not resolve that extension. The present application does not use the ferromagnetic model on primes of the old front J.

## Independent review of the exterior range

The constants 9–14 of 10343 were rederived explicitly, without taking their historical argument for granted. Write z=ax, a=m²−1>=3 and x>=9/2. For the log-derivatives of r_m one has:

    Dlogr_m=−2ax+6/(2m²x−3)−6/(2x−3),
    D²logr_m=−4ax+A(x)−A(m²x), A(y)=24y/(2y−3)²,
    D³logr_m=−8ax+B(m²x)−B(x), B(y)=48y(2y+3)/(2y−3)³.

A and B decrease for y>=9/2, with A(9/2)=3 and B(9/2)=12. This proves the declared bounds 3z, 5z, 10z; the exponential differentiation formulas then give 3zr_m, 10z²r_m, 35z³r_m because z>=27/2.

The bound r_m<=2m⁴exp(−ax) and m⁴<=16a²/9 allow extending the sum to ALL integers a>=3. The relevant powers of a are 3, 4, 5. Their first terms are 1296, 58320, 2755620 divided by 729000. Separating a=3 leaves initial ratio (4/3)^r/90 and later ratios <=(5/4)^r/90. The Taylor sum up to degree 14 giving exp(9/2)>90 and the three geometric majorants were checked independently with Fraction: they come out <19/10000, 83/1000, 397/100, respectively. The cubic combination in the derivative of log(1+R) is <4. The majorants decrease with x, since ax>=13.5 exceeds all degrees used.

The first mode satisfies ell_1'''<=−36+12=−24 by the same descent of B. Therefore (logPhi)'''<−20 for t>=1/4. No exterior gap or omitted tail was detected.

## Compact certificate and splice

Read in full POWER_THETA_HAZARD_COMPACT_073 and tools/power_theta_compact_073_verify.py. The factor pi exp(5t/2) has affine logarithm and does not contribute to the fourth derivative. The recurrence Q_(r+1)=2y(Q_r'−Q_r), its five polynomials and the numerator NUM of the fourth log-derivative are correct.

For m>=5, the majorant 9600·3⁵m¹²2^(−4m²) controls EACH derivative 0..4, using y>=3m² and the decrease of y⁵exp(−y). Its ratio from 5 is <1/2 and decreases afterwards. The complete remainder is exactly 4449462890625/4951760157141521099596496896 and is added two-sidedly to each sum before NUM.

The integer operations implement correct outward floor/ceiling, including products of arbitrary signs. Reciprocals are used only with positive intervals. Machin128 and the two-sided atan remainder are valid. For exp, the reduced argument is <=1, the Taylor128 tail lies between 0 and 2/129!, and seven squarings recover the original argument; all ranges are checked. The powers and the interval Horner keep enclosures even if they may be conservative.

My independent reproduction with python3 finished exit0: PASS on the 4096 fixed panels, with NUM.upper<0 and S.lower>0 on each closed interval. The union covers [0,1/4] without gaps. The output prints rational endpoints and the exact Q; it does not use floating-point signs. The smooth parity of Phi, already established through its modular identity, gives (logPhi)'''(0)=0. Integrating the negative fourth derivative proves (logPhi)'''<0 on 0<t<=1/4 and splices with the exterior range. One obtains V'''(t)>0 for ALL t>0, V=−logPhi.

## Two-copy argument

Reviewed POWER_THETA_TWO_COPY_073 in full under its explicit hypotheses: V even C³, V'''>0 on the positive half-line and superlinear growth. This growth ensures all tilted moments; no hidden hypotheses about the integrability of V' are introduced.

The factor of the identity M''=4Cov(S,D²) is correct. For 0<=s1<s2, Delta'(d)=integral_(s1)^(s2)[V''(t+d)−V''(t−d)]dt is strictly positive at d>0, because V'' increases strictly with |x|. Thus the ratio of conditional densities decreases strictly with |d| and g(s)=E[D²|S=s] decreases strictly with |s|. The argument uses covariances between functions of opposite monotonicities and finite moments; it does not differentiate an integral with uncontrolled V'.

The marginal of S has an even factor times exp(2us), so that E[S||S|=r]=r tanh(2ur), strictly increasing for r>0, u>0. Conditioning again gives Cov(S,D²)<0, with integrability of the product guaranteed by the third-order moments. Hence M''(u)<0. Finally M(0)=0 and (M−uM')'=−uM''>0 prove 0<uM'(u)<M(u). The strictness is justified by the positive densities on the whole line.

## Specific corollary and scope

The compact certificate and the exterior discharge the theta hypothesis that appeared CONDITIONAL in the two-copy memo. Positivity, parity, smoothness and superexponential decay are those of the SAME kernel Phi of CONE001. Its real identity gives M(u)=L(u+1/2). Therefore, for ALL a>1,

    L'(a)>0, L''(a)<0,
    L(a)−(a−1/2)L'(a)>0.

Integrating the quotient bound allows applying the exact criterion of CONE001 to ALL pairs a,b>1. For distinct exponents, its 2x2 matrix is positive definite; when exponents coincide the coefficients are combined first and positivity of the single nonzero generator remains. The arithmetic terms and the polar are included by the polarization identity of CONE001; it is not only an inequality for the archimedean symbol.

This resolves the range of pairs that CONE001 left open below 32. It does not prove matrices of arbitrary order, the complete sufficient table, a new time window or the global sign. The comparison of higher polynomial tilts 10343 remains another obligation. The approval does not turn the scalar concavity of L into a general Pick principle nor into an induction over all orders.
