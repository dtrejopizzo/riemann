# POWER_THETA_DENSITY_CONCAVITY_086 — Global curvature via linear densities

Status: **PROVED, independent audit approved.** See `POWER_THETA_DENSITY_CONCAVITY_AUDIT_086.md`. For the real Phi, R(lambda)=sqrt(lambda)/M(sqrt(lambda)) satisfies R''(lambda)<0 for ALL lambda>0. The proof uses the real inequalities already proved in 077 and an integral transformation of three densities. It does not need the certificate 080. It does not claim arbitrary order nor the global sign of W. Papers untouched.

## 1. Consultation and precise difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked 073–085 and antecedents SCHUR003/074. 079 reduced three generators to a real curvature; 078 proved its tail, 080 offers an independent compact discharge. 083 and its appendix make an abstract hierarchy explicit, but do not prove its real signs.

Here the object changes: the quotients are eliminated by multiplying each row by Z'(u)>0 and THREE LINEAR densities of Phi are studied. Their pointwise determinant is controlled EXACTLY by N>0 of 077, a specific datum that the generic hypotheses refuted in 074 do not contain. This link discharges the curvature on the whole half-line, without new certificates, campaigns or assumptions about moments of the quotient.

## 2. Real data already proved and statement

Let Phi be the real even density of 073–077, Z(u)=int_R exp(ut)Phi(t)dt and M=Z'/Z. Phi is positive, smooth, and its relevant derivatives decay faster than any exponential. Set, for t>0,

    V=−logPhi, p=V', q=V'', r=V''',
    D=tq−p,
    C=p³+tp²q−pq−tpr+tq²,
    N=DC'−trC.

077 proves p>0, D>0, C>0, N>0 at ALL t>0. Only p, D, N enter the following sign. The theorem is

    R(lambda)=u/M(u)=uZ(u)/Z'(u), lambda=u²,
    R''(lambda)<0, ALL lambda>0.                  (GLOBAL-CURVATURE)

The primes of R mean derivatives with respect to lambda; those of p, C, etc. with respect to t. Z'(u)>0 for u>0 because Phi is even and positive.

## 3. The density determinant and the new cancellation

Consider the three odd densities

    rho_1=tPhi, rho_2=(tPhi)'', rho_3=−Phi'.

For t>0, dividing them by tPhi>0 gives

    (rho_1,rho_2,rho_3)=tPhi·(1,A,B),
    A=p²−q−2p/t, B=p/t.

One has B'=D/t²>0. Write A0=p²−q, so that A0'=2pq−r. Direct expansion of C gives

    C=tp A0'−D A0,
    C'=2p A0'+tp A0''−tr A0,
    N=p{D[2A0'+tA0'']−t²rA0'}.

On the other hand,

    A'/B'=t²A0'/D−2,
    (A'/B')'=t{D[2A0'+tA0'']−t²rA0'}/D²
               =tN/(pD²)>0.                       (DENSITY-CURVATURE)

It is the same N certified in 077, with no residual term. Therefore A, viewed as a function of the strictly increasing coordinate B, is strictly convex. For ALL 0<t1<t2<t3,

    det[(1,A(t_i),B(t_i))]_(i=1)^3<0,
    det[(rho_1(t_i),rho_2(t_i),rho_3(t_i))]_(i=1)^3<0. (DENSITY-SIGN)

The sign is fixed by exchanging the last two columns: det[1,B,A]>0 is the strict secant inequality of a convex function.

## 4. Strict positivity of the sinh kernel

For positive and strictly increasing u_i, t_j,

    det[sinh(u_i t_j)]_(i,j=1)^3>0.                (SINH-TP3)

Elementary proof: truncate the sinh series and apply Cauchy–Binet. Each term is a product of determinants of monomials with strictly increasing odd exponents and positive coefficients. These determinants are positive at ordered positive nodes. To justify that property of monomials, weighted Rolle shows by induction that a combination of j distinct powers has at most j−1 positive zeros; its Wronskian has positive sign, fixed by the Vandermonde of its exponents. The confluent limit then fixes the positive sign of the evaluation determinant. The truncations converge on each set of nodes; already the term with exponents 1,3,5 is strictly positive. This proves SINH-TP3.

The confluent version in lambda=u² is also needed:

    L(lambda,t)=sinh(sqrt(lambda)t)/sqrt(lambda)
                =sum_(m>=0)lambda^m t^(2m+1)/(2m+1)!,
    det[(partial_lambda)^i L(lambda,t_j)]_(i=0,1,2;j=1,2,3)>0
        for lambda>0, 0<t1<t2<t3.                (CONFLUENT-TP3)

The same Cauchy–Binet expansion applies. The determinants of the derivatives of lambda^(m_j) are their Wronskians: positive for m1<m2<m3. The other determinants are of the powers t^(2m+1) and also positive. The term m=0,1,2 guarantees the strict inequality. The series of derivatives converge on compact subsets of lambda>0, which justifies passing to the limit.

## 5. Integral transfer and boundary terms

Integrating by parts over ALL of R, without introducing an artificial boundary at 0, gives

    LT(rho_1)=Z'(u),
    LT(rho_2)=u²Z'(u),
    LT(rho_3)=uZ(u).

All boundary terms at infinity vanish. Since the three densities are odd, their transforms fold exactly as

    (Z',u²Z',uZ)=2int_0^infinity sinh(ut)(rho_1,rho_2,rho_3)dt. (ODD-LT)

One does not integrate by parts on the half-line and no value at 0 is lost. The real smoothness and parity make all densities regular there; normalizing them by tPhi in §3 was only done for t>0.

Andreief, which here is just expanding two determinants and applying Fubini, gives for u1<u2<u3

    det[(Z'(u_i),u_i²Z'(u_i),u_iZ(u_i))]
      =8int_(0<t1<t2<t3)
          det[sinh(u_i t_j)]det[rho_l(t_j)]_(j,l=1)^3 dt1dt2dt3<0.

The integral is absolutely convergent: for nodes u in a compact set, each density and its polynomial factors are integrable against exp(Ut), by the real tails of Phi and its derivatives. Each term of the expansion of the determinants is dominated by a product of three of those integrals. The signs SINH-TP3 and DENSITY-SIGN are strict on the whole chamber, of positive measure.

Dividing each row by Z'(u_i)>0 proves det[1,u_i²,R(u_i²)]<0. This already proves strict secant concavity on the whole half-line. By itself, that statement would NOT suffice to ensure R''<0 at each point; the next section justifies the pointwise version.

## 6. Strict pointwise curvature via the confluent kernel

Define the three functions of lambda>0

    (f_1,f_2,f_3)(lambda)
       =(Z'(u)/u,uZ'(u),Z(u))
       =2int_0^infinity L(lambda,t)(rho_1,rho_2,rho_3)dt.

Differentiating up to twice under the integral is legitimate by the same domination, uniformly on compact subsets of lambda>0. Andreief applied to the three rows of derivatives, CONFLUENT-TP3 and DENSITY-SIGN give

    W(f_1,f_2,f_3)(lambda)<0.

But f_1>0 and exactly

    (f_1,f_2,f_3)=f_1·(1,lambda,R(lambda)).

The Wronskian rule when multiplying all functions by the same function gives

    W(f_1,f_2,f_3)=f_1³ W(1,lambda,R)=f_1³R''.

Thus R''(lambda)<0 for ALL lambda>0, proving GLOBAL-CURVATURE without improperly inferring it from strict secant concavity.

## 7. Consequence and scope

With a=M'(0), g(lambda)=aR(lambda)−1 satisfies g''<0 on ALL lambda>0. Together with BASE073 and the criterion 079, this proves matrices of three distinct positive nodes positive definite. For original exponents ai=ui+1/2>1, the complete form and its transfer by congruence are kept exactly; repeated nodes only allow asserting PSD of the coefficient matrix, with strict energy for the nonzero represented function.

080 and the exterior bounds 078 remain valid as independent proofs; 086 supplies a different global mechanism and does not require their certificates for the curvature. Nor does it prove that the same argument controls the higher densities of 083. For larger orders there are more functions and Wronskians; the sign of their determinant is not obtained from this three-row minor. There is no conclusion for all orders, nor global closure of W.
