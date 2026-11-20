# POWER — Compact design of the mixed system, round107

Status: **DESIGN AUDITED; RUN107 INCONCLUSIVE AT THE ORIGIN.** Independent reproduction 46719 finished with the same result. This document keeps the parameters fixed before data and does not claim the compact sign.

## 1. Object and difference relative to the corpus

Consulted the project rules, ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID and CROSSWORD-TO-D, and the sources103–106. The target is W_t(K,J,Phi,J'')>0 for0<t<64. The origin104 is positive without radius and the tail104 covers t>=64; neither closes the interval. This EVEN system is not the odd particular system093/095. Its positivity, together with CT3 of103, would allow the two-Rolle-operator argument for the second real pair of102. It is not an automatic consequence of099 nor a result on the complete form.

Write a=I2/I0, J(t)=integral_t^infinito s Phi(s)ds and K''=a Phi-J, with K even, positive and decreasing on the half-line. Ij=integral_0^infinito t^j Phi(t)dt. The formulas and normalizations of103 are used, not new moment data.

## 2. Budget fixed before data

Origin branch: t in[0,1/2], lambda=t^2 in[0,1/4]; precision1024bits;128 modes; t-jet of Phi with cap1025; lambda polynomials of degree512. Initial partition16 lambda cells of width1/64. Internal left-first subdivision, maximum depth10 and at most8192 cell evaluations.

Remaining branch: t in[1/2,64]; precision512bits; time jet cap4 for integrals, cap5 for the local theta logarithm. Gauss–Legendre64 on each of the ten v segments with endpoints0,1,2,4,8,16,32,64,128,256,512. Initial partition508 time cells of width1/8. Maximum depth10 and at most8192 cell evaluations, left first.

A cell is accepted only if the lower bound of the interval determinant is positive on the WHOLE cell. If its upper bound is negative that interval is reported. If undecided and depth or budget is exhausted, the result is INCONCLUSIVE. Parameters are not changed according to observed signs. Only a complete coverage allows claiming the compact sign.

## 3. Origin: holomorphic function and fixed tails

Let phi(lambda)=Phi(sqrt(lambda)); parity of Phi defines this holomorphic function in a neighbourhood of |lambda|<=1/2. On that disc |t|<3/4, Re(pi exp(2t))>3/80 and |pi exp(2t)|<20. We use cos(3/2)>1/16, exp(3/2)<5 and exp(15/8)<9. The absolute theta sum provides

 |phi| <=1548 sum_(m>=1) m^4 exp(-3m^2/80)
       <=1548*24*(83/3)^5 <2^40.

Keep modes1..128. From m=129 the ratio of the majorants is less than1/2, and the tail is less than2^-583: 129^4<2^29 and 3*129^2/80>624. Extracting EVEN coefficients of the t-jet is equivalent to symmetrizing the partial sum; it is not assumed that a theta partial sum is even. Cauchy in lambda radius1/2 gives a coefficient error <=2^-583*2^k for k0..512. It is added before products, recurrences or determinants.

For the complete Taylor polynomial of degree512, its remainders and derivatives of order0..4 on real lambda[0,1/4] are less than2^-426. For example N=513 and sum_(n>=N) n^4 2^-n<3N^4 2^-N, N^4<2^37; 2^40 and4^4 are also paid. No division by t^6 or by lambda is evaluated on an interval containing0.

## 4. Origin: moments, recurrences and matrix

The data of103 are entered as exact outward rational boxes:

 I1=0.02152870762556652324898962 +/-3.96e-27,
 I3=0.00191588830192231322996545 +/-4.90e-27.

For a, exclusively a fixed POINTWISE jet of the completed function E at0 at1024bits, cap3, is used, a=2E[2]/E[0]. E(u)=A[1+(A-1)zeta_deflated(A)] Gamma(A/2) exp(-A log(pi)/2), A=u+1/2. The deflation subtracts1/(A-1). Compatibility with the interval098 a=0.0462099862308379415778676 +/-3.74e-26 is checked; that wide interval does not replace the new pointwise enclosure. This computation is part of the future certificate; it has not been executed for107.

If phi_k are the lambda coefficients, build

 J_0=I1, K_0=a I1-I3/2,
 J_k=-phi_(k-1)/(2k),
 K_k=(a phi_(k-1)-J_(k-1))/(2k(2k-1)), k>=1.

All errors of I1,I3,a and phi_k are propagated by interval arithmetic before the determinant. The constants a,I1,K0<1 are checked as assertions.

To justify the tails of these recurrences, J_lambda'=-phi/2 and

 K(lambda)=K0-I1 lambda/2
 +a lambda integral_0^1 (1-s)phi(s^2 lambda)ds
 +(lambda^2/2) integral_0^1 s(1-s)^2 phi(s^2 lambda)ds.

This gives |J|,|K|<2^42 on |lambda|<=1/2. With the same tail computation as before, the error of entries differentiated up to4 is less than2^-420. A ball2^-400 is conservatively added to EACH matrix entry, after evaluating the known polynomials. Unknown coefficients are not filled with zeros without paying this error.

The matrix has columns K,J,phi,Q, rows lambda derivatives0..3, where Q=J''_t=-phi-2lambda phi'. Thus Q^(j)=-(2j+1)phi^(j)-2lambda phi^(j+1). Jet coefficients are multiplied by factorials to obtain derivatives. Its determinant is W_lambda; the exact bridge is W_t=64t^6 W_lambda. The matrix is evaluated on the ball of the whole cell.

## 5. Remainder: direct normalized integrals

Reuse the lemma of106, including its section8, without propagating data through an ODE. For t in a cell, y=pi exp(2t), r=Log(1+v/y)/2 and

 Theta16(y)=2y-3+sum_(m=2)^16 m^2(2m^2 y-3)exp(-(m^2-1)y),
 A16=exp(-v)/(2y)*(1+v/y)^(1/4)*Theta16(y+v)/Theta16(y).

Integrate together the jets of (t+r)A16 and [a r-(t+r)r^2/2]A16. The principal branch is holomorphic by106. For the real evaluations, check positive denominator and positive1+v/y. acb.integral is not used and no branch condition is omitted.

In each cell fix Yc=pi exp(2c), constant with respect to the jet. The columns are Yc^2 kappa,Yc tau,1,X/Yc, X=t p-1, p=-Phi'/Phi. The determinant is Yc^2 W_t/Phi^4. The constant column allows computing the3x3 minor of derivative rows1..3 and first, second and fourth columns, with positive sign. p is obtained from the local Theta16 with cap5, not by differentiating initial data of an ODE.

## 6. Gauss, mode and domain errors

The proof of106 section8 gives, for the time coefficient j, Gauss error <=2^(-83+5j), j0..3. The API arb.legendre_p_root(64,k,weight=True) provides enclosed nodes and weights; their rounding is additionally propagated by interval arithmetic. Check positivity of weights and that their sum encloses2 before transforming each segment.

The initial time half-width1/16 is admissible: the union of discs of radius1/32 around its points satisfies |z-c|<=3/32, Re z>=1/2-3/32>-1/16, |Im z|<=1/32 and |z|<65. Moreover Yc/Y<exp(3/16)<2 and Yc^2/Y^2<exp(3/8)<2. Hence the majorants4096 exp(-Re v)(1+|v|)^5 and2^34 of106 remain valid. Subdivided cells only shrink these domains.

Before the determinant, add coefficient errors2^-81*32^j to both integrated columns, including Gauss, tail v>512 and modes>16 according to106. For X/Yc use the local error of106 <=2^-687*32^j. The errors are for normalized coefficients; factorials are paid when converting to derivatives. |y+v|>=Y+v is not used, as it would be false for complex y.

## 7. Planned implementation and cost

Per cell, the15 jets exp(-(m^2-1)y) can be precomputed and the scalar factors exp(-(m^2-1)v) reused at the640 nodes. This is an exact identity that reduces cost, it does not change the rule or the precision. The maximum remainder is8192*640=5242880 vector evaluations cap4; it may take hours. The design does not guarantee termination with a sign and will not be executed before the independent review of the literal.

## 8. Exact pending items and scope

Pending: audit of the present design; literal implementation of origin theta/jet and Gauss rule with explicit errors; independent code review; single execution; reproduction and complete archive of output/hash if applicable. The origin budget here uses the robust bound2^40, not the finer bounds discussed informally. It must be checked literally that the entry tail2^-400 covers the combination Q, the recurrences and all factorials; the moment boxes are propagated without being absorbed into that tail.

GLOBAL SIGN OPEN. An INCONCLUSIVE output does not refute the sign. No part of this design adds coverage of W, of windows T or of all orders. Transfer to the next pair will be invoked only after proving the complete mixed system.


## 9. Audit and actual output of107

The complete design was approved. The payment of origin entries is justified explicitly: for J,K, the bound2^42 and the Taylor512 give, up to derivative4,

 2^42 * 4^4 * 3 * 513^4 * 2^-513 <2^-424.

For Phi one has2^-426; the combination Q and its derivatives up to3 cost less than8 times that error, hence less than2^-423. The payment2^-400 per entry is generous. The errors of modes, moments and a are still propagated before the products; they are not treated as correlated for free.

The approved literal was executed: session5594, exit2, INCONCLUSIVE at lambda=[0,1/65536], depth10,11 evaluations,0 accepted cells. The determinant ball had approximate radius0.00294; that approximation only describes the output, it does not certify a sign. The remaining branch was not executed. No parameters were changed. The independent reproduction46719 ended exit2 with exactly the same result; see section10.

The failure is one of enclosure, not a refutation. A later representation could first form the determinant as a polynomial in the SAME variable lambda and evaluate it afterwards. That requires explicitly paying tails and coefficient errors; it has not yet been proved or executed here.

## 10. Independent reproduction and final scope

Run5594 ended exit2: INCONCLUSIVE by maximum depth at the origin. The independent reproduction46719 likewise ended exit2. Both runs made11 evaluations,0 accepted leaves and reached depth10 at lambda[0,1/65536], with printed determinant[+/−2.94e−3]. This ball does not separate0: it is neither a proof of negative sign nor of failure of the hypothesis. REST was NOT executed, according to the audited main.

Complete logs:`tools/power_mixed_four_compact_107_root.log` and `tools/power_mixed_four_compact_107_audit.log`. Main hash:`2a7d147caf8181adb5aa29eb6fcbe356f625e2743ad6765e6ac543aacad23054`; origin hash:`15d6f12c197ef52c062a12c59ee4a7c5db94c74e0073e8463a7ce03dd613e553`. They coincided in both runs and after the reproduction. Scripts and parameters were not edited to obtain a different result.

Only insufficiency of the interval enclosure with THIS budget is recorded; there is no mathematical obstruction, decided Chebyshev4, finite U crossing, negative W nor new coverage. Another object or representation must be designed and audited before any new execution. The local signs of104 and all previous analytic proofs remain in force.
