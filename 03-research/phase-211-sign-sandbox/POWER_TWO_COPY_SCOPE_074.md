# POWER_TWO_COPY_SCOPE_074 — The strong hypothesis 073 does not suffice for three generators

Status: **PROVED/APPROVED**, independent audit in [POWER_TWO_COPY_SCOPE_AUDIT_074.md](POWER_TWO_COPY_SCOPE_AUDIT_074.md); verifier reproduced independently three times with exit 0/PASS. Auxiliary ANALYTIC counterexample within the same class of potentials as 073. It is not the real theta kernel nor a negative direction of W. Papers untouched.

## 1. Consultation and exact difference

Read the project rules, ROUTES-TRIED-INDEX/README, master grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; cross-checked SCHUR003 and THETA_TWO_COPY073. 003 already refutes extending monotonicities and concavity to order-3 matrices, but its auxiliary functions are not presented as tilted means of an even C³ potential with V'''>0. The example 3+cosh does not satisfy those hypotheses either.

The difference here is to keep ALL the strong hypotheses 073 and produce an indefinite 3x3 matrix. The jet at 0 of the prescribed family V=x^6 was studied first; that jet does NOT produce the counterexample. The definitive counterexample is constructed analytically via a single explicit polynomial potential and three tilts fixed in advance. No parameter family is swept and no integrals are evaluated numerically.

## 2. Coalescent determinant condition at the origin

For any even potential with the moments and regularity of 073, write the cumulants of its untilted law as kappa2,kappa4,kappa6. Near 0,

    M(u)=alpha u+beta u³+gamma u^5+O(u^7),
    alpha=kappa2, beta=kappa4/6, gamma=kappa6/120.

For distinct nodes xi>0 and ui=epsilon xi, the kernel K(u,v)=(M(u)+M(v))/(u+v) satisfies

    det[K(epsilon xi,epsilon xj)]_(i,j=1)^3
      =epsilon^6 prod_(i<j)(xj-xi)²
                       ·(-beta)(alpha gamma-beta²)+O(epsilon^8).

This is verified by expanding (u^(2r+1)+v^(2r+1))/(u+v). In the monomial coordinates 0,1,2 the first coefficient minor is

    [[alpha,0,beta],[0,-beta,0],[beta,0,gamma]],

whose determinant is (-beta)(alpha gamma-beta²). The indices 0,1,2 are those of smallest sum in three distinct rows and columns, so they give the order-6 term. Parity excludes order 7.

If kappa4<0, the leading sign of this determinant is determined by

    3 kappa2 kappa6 - 10 kappa4².                       (JET)

For V(x)=x^6, the even moments are

    m_(2r)=Gamma((2r+1)/6)/Gamma(1/6).

Setting a=m2, gamma reflection gives m4=2a² and m6=1/6. Thus

    kappa4=-a², kappa6=1/6,
    JET=a/2-10a^4>0.

To justify the last sign without decimals, a<1/3 suffices. Indeed

    Gamma(1/6)=6 int_0^infinity exp(-x^6)dx
      >6[1-1/7+1/26-1/114]>3sqrt(pi).

The first inequality uses the lower Taylor polynomial 1-z+z²/2-z³/6 for exp(-z), integrated over [0,1], and discards a positive tail. If r=1-1/7+1/26-1/114, the verifier checks r²>11/14>pi/4 using pi<22/7. Therefore a=sqrt(pi)/Gamma(1/6)<1/3 and 1/2-10a³>1/2-10/27>0. This first coalescent test of x^6 is positive; it is not offered as a falsifier.

## 3. Explicit potential that does give the counterexample

Fix exactly

    p=1000000, A=400000000,
    v(x)=x²/2+x^(2p)/[2p·2^(2p-2)],
    V(x)=A v(x).

It is an even POLYNOMIAL potential, of class C-infinity, superlinear, and

    v''(x)=1+(2p-1)(x/2)^(2p-2)>=1,
    V'''(x)=A(2p-1)(2p-2)x^(2p-3)/2^(2p-2)>0, x>0.

Therefore it strictly satisfies ALL the hypotheses 073. Let M(u) be the mean of the density proportional to exp[-V(x)+ux], and take only the three nodes

    u1=A, u2=2A, u3=3A.

The potential is not modified between the three nodes.

## 4. Modes: analytic bounds without solving large equations

For i=1,2,3, let xi be the unique solution of v'(xi)=i. It exists and is unique by v''>=1 and the limits of v'. Set eta=1/20000. One has

    1-eta<x1<1,
    2-eta<x2<2,
    2-eta<x3<2.                                        (MODES)

Indeed v'(x)=x+x(x/2)^(2p-2). Since 2p-2>15 and 2^15>20000,

    v'(1-eta)<1-eta+2^(-(2p-2))<1<v'(1).

For the other end,

    v'(2-eta)
      <2-eta+2(1-eta/2)^(2p-2)
      <=2-eta+2exp[-(p-1)eta]<2,

since (p-1)eta>49 and exp49>49^4/24>40000, whence 2exp(-49)<eta. On the other hand v'(2)=4>3. Strict monotonicity of v' proves MODES for both indices 2,3.

## 5. From modes to means: uniform error via strong convexity

At the node ui=A i, the density is proportional to exp[-A(v(x)-i x)]. If Xi has that law and mi=M(A i), integration by parts of (x-xi) against the density gives EXACTLY

    E[(Xi-xi)(v'(Xi)-i)]=1/A.

The boundary term vanishes by the decay of an exponential of an even polynomial. Since v''>=1 and v'(xi)=i,

    (x-xi)(v'(x)-i)>=(x-xi)².

Hence E[(Xi-xi)²]<=1/A and, by Cauchy,

    |mi-xi|<=1/sqrt A=eta.

Combining with MODES gives

    |m1-1|<1/10000,
    |m2-2|<1/10000,
    |m3-2|<1/10000.                                    (MEANS)

This estimate controls the full real integrals; it is not a saddle-point approximation without remainder.

## 6. Rational negative vector and all pairs positive

The rescaled matrix B=A[K(ui,uj)] has entries

    B_(i,j)=(mi+mj)/(i+j).

By MEANS, each entry differs by less than delta=1/10000 from the rational matrix

    B0=[[1,1,3/4],[1,1,4/5],[3/4,4/5,2/3]].

Take c=(40,-40,3). An exact rational computation gives

    c^T B0 c=-6,
    |c^T(B-B0)c|<delta(40+40+3)²=6889/10000<1.

Therefore

    c^T B c < -53111/10000<0,
    c^T [K(ui,uj)] c < -53111/(10000 A)<0.              (NEGATIVE)

The matrix is indefinite, since its diagonals are positive. However, by the general theorem 073 applied to THIS V, ALL its minors of two distinct positive nodes are positive definite, not only the three pairs chosen here. Also M''<0 and M-uM'>0 on the whole positive half-line.

Thus the strong probabilistic control 073 and its strict concavity are not automatically preserved as an order-3 sign. The counterexample is analytic and belongs exactly to the proposed class, unlike the auxiliaries of 003.

## 7. Evidence and scope

Verifier `tools/power_two_copy_scope_074_verify.py`: Fraction arithmetic for MODES, the mean error, the matrix B0, the vector and the constants of the x^6 test. It does not evaluate the function M or the huge-degree potential; there is no quadrature or parameter search. The inequalities for the means and the entries are proved analytically above.

It is not the REAL theta potential and no negative direction of W is claimed. The result 073 on ALL real pairs remains intact. What is refuted is only the generic implication «hypothesis on V of 073 ⇒ 3x3 positivity of K». To advance on three generators of the real datum, an additional specific property of Phi or a concrete estimate of its cross term will be needed. Such properties are not excluded and no global impediment is inferred. Papers untouched.
