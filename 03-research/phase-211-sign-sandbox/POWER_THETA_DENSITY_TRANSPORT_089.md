# POWER_THETA_DENSITY_TRANSPORT_089 — From the R4 sign to global Turán

Status: **PROVED using the audited certificate 089 FULL PASS; independent reproduction 87911 exit0/FULL PASS 1024+8192 and matching hash.** This file makes the transport explicit, separated from the computational bounds of `POWER_THETA_DENSITY_COMPACT_089.md`. No new W coverage; papers untouched.

## 1. Inputs and difference

Uses 073/077/086 and the sign Wt(1,A,B,C)<0 at ALL t>0 obtained by BRIDGE/certificate 089 on 0<t<=1 and the analytic proof 088 on t>=1. The new input over 086 is a fourth global Wronskian; it is not inherited from the previous three. 087 remains an independent pointwise check.

The notations are A=p²−q−2p/t, B=p/t, C=(p³−3pq+r)/t, with real Phi and rho=(tPhi,(tPhi)'',−Phi',−Phi''')=tPhi(1,A,B,C). 086 gives k=B'>0 and J=(A'/B')'>0.

## 2. The previous minors and the necessary order

The system used for Rolle is **[1,B,A,C]**. Its initial Wronskians are

    W1=1,
    W2=B'=k>0,
    W3=W(1,B,A)=k²J>0,
    W4=W(1,B,A,C)=−W(1,A,B,C)>0.

[1,A,B,C] is not used as the initial system: A' has not been assumed positive. Exchanging its two central columns fixes all signs.

Weighted Rolle proves that a smooth system with these strictly positive initial Wronskians is an extended Chebyshev system. One first divides by the nonzero initial function and differentiates; the Wronskians of the reduced system are quotients of the previous ones by positive powers. Repeating reduces the maximal number of zeros. A nontrivial combination of four functions has at most three zeros; therefore the evaluation determinant does not vanish for t1<...<t4. Its sign is fixed by the confluent limit and W4>0. Returning to the original order and multiplying rows by tiPhi(ti)>0,

    det[rho_j(t_i)]_(i,j=1)^4<0
    for ALL 0<t1<t2<t3<t4.

This is a sign for ALL density nodes, not only for the confluent jet.

## 3. Strict integral transformation

Sinh(ut) is strictly TP4 at positive nodes: expanding its series with positive coefficients and applying Cauchy–Binet produces determinants of positive monomials; the term with exponents 1,3,5,7 is strictly positive. Positivity of generalized determinants of monomials is proved by weighted Rolle and their positive Wronskians.

The bilateral transforms of rho are

    (Z',u²Z',uZ,u³Z).

Integrating by parts over ALL of R eliminates boundary terms by the supertails and avoids an artificial endpoint at 0. By oddness, they are 2∫sinh(ut)rho(t)dt on the half-line. Andreief, finite expansion and absolutely convergent Fubini, gives

    det[Z'(ui),ui²Z'(ui),uiZ(ui),ui³Z(ui)]<0

for all ordered distinct positive nodes. The factor 2⁴ is positive; the 4! of Andreief cancels when restricting to the ordered chamber. The densities may be signed: each term of the expansion is dominated by products of integrals of |rhoj|exp(Ut), finite by their tails. It is not assumed that each density is positive.

Dividing by Z'(ui)>0 gives det[1,ui²,R(ui²),ui²R(ui²)]<0. This proves signs of R4 Pfaffians at all nodes, but for the strict pointwise inequality the next confluent step is needed.

## 4. Global pointwise Turán

With lambda=u² and L(lambda,t)=sinh(sqrt(lambda)t)/sqrt(lambda), the kernel with derived rows 0,1,2,3 is strictly TP4. Cauchy–Binet applied to L=Σlambda^m t^(2m+1)/(2m+1)! has positive Wronskians of monomials in lambda and positive determinants of monomials in t; the term m 0,1,2,3 fixes strictness.

Define

    f=(Z'/u,uZ',Z,u²Z)
      =2∫L(lambda,t)rho(t)dt
      =f1(1,lambda,R(lambda),lambda R(lambda)), f1=Z'/u>0.

Derivatives up to three under the integral are legitimate on compact subsets of lambda>0 by uniform exponential domination. Confluent Andreief and the global density sign give W(f)<0. The Wronskian rule for a common factor gives exactly

    W(f)=f1⁴W(1,lambda,R,lambda R)
        =f1⁴[3(R'')²−2R'R''']
        =−f1⁴T_R.

One concludes **T_R=2R'R'''−3(R'')²>0 for ALL lambda>0**. A strict pointwise inequality is not inferred from distinct determinants alone.

## 5. Consequence 090 and limits

The already audited 090 now applies globally to R: R is C3 up to 0 with R'0>0 by 073/086. It gives h=1/b strictly concave for ALL x>0. With 086 g_*=xb strictly concave and the formulas 078, all distinct pairs of the regularized remainder Gp are PD for ALL p>0. The removable point x=P is treated by the second-order tangent errors; Gp increasing is not presupposed, so 081 is not contradicted.

This does not prove the concavity of both reciprocal data of the remainder Gp, its Turán inequalities nor preservation by a second Schur step. S4 is not transported here, nor five/all orders, nor new W/T. Four generators remain independently proved in 085. The independent reproduction 87911 of the certificate 089 finished exit0/FULL PASS 1024+8192, with matching hash.
