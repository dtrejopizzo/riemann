# POWER_RECIPROCAL_PFAFFIANS_AUDIT_083 — Independent audit

Status: **APPROVED / PROVED as an algebraic identity in all orders.** Source `POWER_RECIPROCAL_PFAFFIANS_083.md`, read in full. Approved after two independent checks. Papers untouched.

## Checks of signs and factors

With D=diag(u),E=diag(R),A=A_R and T=EKE, both DISPLACEMENT identities are verified entry by entry, including diagonals. UPDATE has the correct sign with Pf([[0,a],[-a,0]])=a: the rank-2 form is decomposable, the Pfaffian is affine in its parameter and the derivative at0 of the square fixes the coefficient Pf(V)b^tV^−1a.

In even size, the determinant of DA+re^t and UPDATE for DAD+ru^t−ur^t contain exactly the same factor1+e^tA^−1D^−1r. The congruences pay detD and productR only once. The result is detK=Pf(A_R)Pf(A_S)/productR. The extension from invertible A is legitimate: for distinct nodes, R_i=u_i produces the invertible Schur matrix. Its classical formula is Proposition2.2, equation(2.7), of Okada, https://arxiv.org/html/1706.01029; cross-checked directly. That classical formula is not presented as an original result. After clearing denominators the extension to coincident nodes is continuous.

In odd size, the cofactors v_i=(−1)^(i+1)Pf(A without i) satisfy Av=0 and the FINAL border has Pf=b^tv. adj(A)=vv^t extends correctly to lower rank; n=1 uses Pfempty=1. adj(DA)=detD·adj(A)D^−1 produces ODD-DET with the correct order of the factors. The congruence Q=[[I,u],[0,1]] adds ru^t−ur^t, so BORDER does not flip sign. The borders r=Ee and D^−1r pay productR and detD respectively. Again no extra product of u remains in detK. This also covers singular matrices.

Both factors change by the same sign when nodes are permuted, so the final product is invariant. n=1,2,3 recover the previous normalizations; those cases are not used to extrapolate the general proof.

## Antecedents and scope

Consulted the three records and003/074/079/081/082. The explicit attribution to classical Pfaffian algebra, Cayley/Knuth and Cauchy–Schur is accepted; no worldwide priority is claimed. The specialization that is new relative to the corpus organizes the determinant of the full kernel through A_R,A_S in all sizes, without removing arithmetic or components.

This is an IDENTITY, not a new signed inequality for the real Phi. For PSD the products of Pfaffians of ALL principal subsets must be controlled; a positive total determinant does not suffice. The signs of the Pfaffians in arbitrary orders are not proved. There is no new W coverage, no resolved order4 and no new windowT; the global target remains OPEN.


## Added classical appendix — later review

The interpolation/Rolle/Hankel appendix was read in full. The even specialization of Ishikawa–Okada–Tagawa–Zeng Theorem1.1(b) and the odd limit with flast=ulast preserve sigma_k and the final border of ones. The dominant order2k−1 and the positive final cofactor justify the limit. The classical identity was cross-checked in the linked primary source; no novelty is claimed.

The hierarchy Dk,j≠0 ensures extended Chebyshev via weighted Rolle, with regularityC^(2k−1) sufficient. Differentiating the polynomial system k times eliminates the first half and gives the even/odd zero counts. The basis translation and column reversal produce exactly TAYLOR-HANKEL and its factorials. The additional condition of shifted positive moments of mu_m=(−1)^m a_(m+1) gives the indicated signs by row/column factorization. It is only a sufficient condition NOT verified for the real quotients R,S; it is not inherited from the positivity ofJ/K. There is no discharge of higher Pfaffians.
