# POWER_THETA_DENSITY_COMPACT_AUDIT_089 — Independent audit

Status: **APPROVED / PROVED with run 40406 exit0/FULL PASS** of the two branches. Independent reproduction 87911 exit0/FULL PASS 1024 origin + 8192 remainder and same hash; not duplicated unnecessarily. Source `POWER_THETA_DENSITY_COMPACT_089.md` complete and final code read; design and literal code audited BEFORE running. Hash checked locally:

    995ef292abf5a80a3d195b4e68a815e1b56f9b343531bc1c0786af682413d1aa

Papers untouched.

## 1. Two domains and bridge

rho=tPhi(1,A,B,C); in lambda=t², Psi=rho/t. The common multiplication by t and the change of variable of a 4-Wronskian give EXACTLY K=Wt(rho)=t4(2t)^6Wlambda(Psi)=64t10Wlambda(Psi). Thus origin lambda [0,1/256] and remainder t [1/16,1] cover 0<t<=1 without gap and avoid dividing by small quantities.

The expressions Psi=(phi,6phi'+4lambda phi'',−2phi',−12phi''−8lambda phi''') are correct. phi=Phi(sqrtlambda) is used WITHOUT normalizing; the sign does not need division by Phi0.

## 2. Analytic majorants and complete tails

The complex exp/cos comparisons of the source pay for |Phi_m|<152m4·4^−m² on |t|<=1/4, with geometric sum <1000. Holomorphic parity of the COMPLETE Phi gives phi holomorphic on the lambda disc. The Cauchy bounds on its derivatives, the columns of Psi and the 24-term determinant give B 1e48 on |lambda|<=1/32. The rounded column bound already suffices; an exponent error in the audit was corrected during design, without changing the parameters of the certificate.

For the remaining branch, the discs of radius 1/32 around t∈[1/16,1] give |Phi_m|<4288m4·8^−m² and |Phi|<10000. On inner discs 1/64 one obtains p_k=10000k!64^k. The raw rho columns require at most (2p3+3p2,2p5+5p4,p4,p6); their 24-fold product is 3936828360292381907930506017700508073984000000000000000000<1e60, reproduced with Fraction.

The tails m>=17 are paid COMPLETELY by 304·17⁴/4²⁸⁹ and 8576·17⁴/8²⁸⁹, respectively. Their ratios are <1/2. The errors of ALL coefficients are bounded by epsilon32^k using centred discs of radius 1/32 contained in the larger complex domain. They are incorporated BEFORE differentiating Psi/rho, not only in the final determinant. The theta tail and the Taylor tail of the determinant are distinct errors and both are included.

The final remainders are 1e48(1/8192)^17/(1−1/8192)<1e−18 and 1e60(15/4096)^41/(1−15/4096)<1e−39; checked by exact Fraction. No sampled functions are used to pay for intermediate points.

## 3. Literal code and execution

ORIGIN: 1024 bits/cap 23, 1024 dyadic lambda panels, evenpartial16=[Phi16(sqrtlambda)+Phi16(−sqrtlambda)]/2. The symmetrization is indispensable because a theta partial sum is NOT even. The centres are positive and their formal sqrt valid. Coefficient errors 0..22 are added; six maximal derivatives leave Wprec>=17.

REST: 512 bits/cap 47, 8192 dyadic t panels, Phi16 direct with coefficient errors 0..46; Wprec>=41. The two determinants are computed by six 2x2 products without divisions. Laplace sign (−1)^(i+j+1) correct. All necessary coefficients must be finite; the upper bound N0+sum|Nk|h^k+remainder must be strictly negative. Both domains/endpoints are covered with exact centres/radii.

Design, meshes, precisions, modes and degrees were audited and fixed before the single process 40406. It finished exit0/FULL PASS 1024 origin and 8192 remainder; no FAIL or adjustment. The script was not modified and the hash above matches locally. No unnecessary additional copy was run while the independent reproduction was in progress.

## 4. Global REAL-R transport

Read and approved the final section 8 of the source. An independent development is in `POWER_THETA_DENSITY_TRANSPORT_089.md`. BRIDGE+certificates+088 give Wt(1,A,B,C)<0 for ALL t>0. The correct ECT order is [1,B,A,C], with Wronskians 1, B'>0, (B')²J>0, −W original>0. A'>0 is not presupposed. Rolle in the coordinate B proves the original density determinant strictly negative for ALL four nodes.

The kernel L=sinh(sqrtlambda t)/sqrtlambda is TP4 also in confluent rows: positive series, Cauchy–Binet, monomials and strict term 0..3. Two-sided integration by parts keeps the boundary terms; Andreief admits signed densities because each term is absolutely integrable by the supertails. F=(Z'/u,uZ',Z,u²Z)=F0(1,lambda,R,lambdaR), F0>0; the confluent version gives W(F)<0, exactly −F0⁴T_R. Therefore T_R>0 POINTWISE at ALL lambda>0, not only a weak jet inequality.

## 5. Consequences and limits

090 no longer needs an unproved global theta input: global T_R applies its secant lemma and gives h=1/b strictly concave at ALL x>0. Together with 086 g_*=xb strictly concave and 078, all distinct pairs of the kernel Gp are proved for ALL p>0, including removable ones. This allows negative Gp' and does not contradict 081.

The other reciprocal curvature of the remainder and its subsequent Turán inequality are not discharged, nor general Schur inheritance. No global S4 transport, five/all orders, T or new W relative to 085. The structural result GLOBAL-R4/global T_R does not eliminate its certified antecedents: it is independent of the certificate 085 in the parameter u, but depends on 073/077/086/088 plus the fixed certificate 089.
