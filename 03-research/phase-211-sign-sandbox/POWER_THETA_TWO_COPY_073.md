# POWER_THETA_TWO_COPY_073 — Concavity of the tilted mean via two copies

Status: **PROVED/APPROVED**, including the theta application and the two-generator corollary; independent audit in [POWER_THETA_AUDIT_073.md](POWER_THETA_AUDIT_073.md). The compact verification is incorporated via POWER_THETA_HAZARD_COMPACT_073. Papers untouched. No global sign of W is claimed.

## 1. Corpus and precise difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, master grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; read CONE001 and `phase-103-direct-a1-closure/103_43_THETA_HAZARD_CONVEXITY_GATE.md`, with their antecedents on covariances, cumulants and tilted measures. Positivity of an even measure and its log-convexity do not suffice for the upper bound of the two-generator criterion: CONE001§4 contains a concrete counterexample. 103_43 already proves the proposed differential hypothesis for the specific kernel outside the compact interval; that hypothesis is not presented as new, nor is its global version used without proof.

The difference is to prove a distinct consequence of that hypothesis: strict concavity of the MEAN under exponential tilting, via a conditional comparison of TWO copies. No attempt is made to order the five polynomial-tilt changes of 103_43, nor to derive a sign of cumulants of all orders. The argument is proved in full below via density ratios and covariances, without an external correlation inequality.

## 2. Sufficient hypotheses and statement

Let V:R->R be an even function of class C³ such that

    V'''(x)>0 for all x>0,
    V(x)/|x| -> +infinity as |x|->infinity.           (H)

The second condition pins down the superexponential decay needed here. For real u define

    Z(u)=int_R exp[-V(x)+ux]dx,
    p_u(x)=exp[-V(x)+ux]/Z(u),
    M(u)=E_u[X]=Z'(u)/Z(u).

Then, for all u>0,

    M''(u)<0,
    M(u)-uM'(u)>0,
    0<uM'(u)<M(u).                                      (RESULT)

All derivatives of Z exist: on any compact set of u, a power of |x| times exp[-V(x)+ux] is dominated by an integrable exponential. In particular M'=Var_u(X)>0 and M'' is the third central moment. There is no need to assume V convex near the origin: (H) only forces V'' to increase strictly with |x|.

## 3. Exact two-copy identity: the factor 4

Take X,Y independent with density p_u and set

    S=(X+Y)/2, D=(X-Y)/2.

By direct expansion,

    E[SD²]=(E[X³]-E[X²]E[X])/4,
    E[D²]=(E[X²]-E[X]²)/2,
    E[S]=E[X].

Thus

    4Cov(S,D²)=E[X³]-3E[X²]E[X]+2E[X]³=M''(u).          (TWO-COPY)

The joint density of S,D is proportional to

    exp[2us-V(s+d)-V(s-d)].

The constant Jacobian 2 does not affect the conditional densities. Conditioning on S=s removes the tilt and gives

    q_s(d)=exp[-W_s(d)]/int_R exp[-W_s(v)]dv,
    W_s(d)=V(s+d)+V(s-d).

Set g(s)=E[D²|S=s]. Its values are finite and do not depend on u. V even implies q_(-s)=q_s, so g is even.

## 4. The conditional variance decreases strictly with |S|

Since V is even, V'' is even. From V'''>0 on the positive half-line it follows that V'' increases strictly with |x|.

For 0<=s1<s2, define Delta(d)=W_s2(d)-W_s1(d). It is even and for d>0 satisfies

    Delta'(d)
      =int_(s1)^(s2) [V''(t+d)-V''(t-d)]dt >0.          (ORDER)

Indeed |t+d|>|t-d| for t,d>0. Even if s1=0, the interval (t>0) has positive length and the integrated inequality is strict. Therefore

    q_s2(d)/q_s1(d)=constant·exp[-Delta(d)]

is strictly decreasing in |d|. Under q_s1, set B(d)=exp[-Delta(d)]. Then

    g(s2)-g(s1)=Cov_(q_s1)(D²,B(D))/E_(q_s1)B(D)<0.     (g-ORDER)

The strict sign is proved with two copies of |D|: D² increases strictly with |D|, B decreases strictly, and the distribution has positive density on the whole line. The integrals of B and D²B are finite by the definition of q_s2 and (H); those of D² under q_s1 as well. This justifies the covariance identity even if B were unbounded.

This argument avoids differentiating integrals containing V': no growth hypothesis on its derivatives is hidden in (H). It has been proved directly that g(s) is strictly decreasing for s>=0, which is the property needed in the next step. There is no need to assert a differential formula for g.

## 5. Strict sign of the unconditional covariance

The marginal density of S has the form

    p_S(s)=constant·exp(2us)H(s),
    H(s)=int_R exp[-W_s(d)]dd,

with H even and strictly positive. Set R=|S|. For all r>0,

    E[S|R=r]=r tanh(2ur)=:a_u(r).

If u>0, a_u is strictly increasing in r>0, since

    a_u'(r)=tanh(2ur)+2ur sech²(2ur)>0.

By conditioning and because g is even,

    Cov(S,D²)=Cov(S,g(S))
             =Cov(a_u(R),g(R))<0.                      (NEGATIVE)

The last inequality is again the elementary two-copy identity for functions of opposite monotonicity. It is strict because R has positive density on (0,infinity) and both functions are strictly monotone. The products are integrable: E[|S|g(S)]=E[|S|D²] is finite by the order-3 moments of X,Y. No mixed covariance has been replaced by its modulus.

TWO-COPY and NEGATIVE prove M''(u)<0 for all u>0.

## 6. Consequence for the two-generator criterion

Evenness of V gives M(0)=0. For A(u)=M(u)-uM'(u),

    A(0)=0, A'(u)=-uM''(u)>0 for u>0.

Hence A(u)>0. Moreover M'=Var_u(X)>0, which completes RESULT. Integrating the inequality 0<uM'/M<1 gives, for u>v>0,

    1<M(u)/M(v)<u/v.

This is exactly the ratio comparison that CONE001 needs for its two-generator minors. It is a consequence under (H), not a claim about higher-order minors or about the full form on an envelope of families.

## 7. Theta application: verified hypothesis and scope

For the positive even kernel Phi of CONE001/103_43, take

    V(x)=-log Phi(x),
    Z(u)=int_R Phi(x)exp(ux)dx,
    M(u)=Z'(u)/Z(u).

Positivity, evenness, regularity and the required decay are checked in the antecedents. The additional hypothesis needed is

    V'''(x)=-(log Phi)'''(x)>0, ALL x>0.                (THETA-H)

103_43 proves that inequality for x>=1/4. The compact set 0<x<1/4 is now covered by [POWER_THETA_HAZARD_COMPACT_073.md](POWER_THETA_HAZARD_COMPACT_073.md): its rational certificate proves (logPhi)''''<0 on [0,1/4], and evenness gives (logPhi)'''(0)=0. Integration preserves the strict inequality and completes THETA-H for ALL x>0. The certificate was reproduced independently three times; the integrated audit [POWER_THETA_AUDIT_073.md](POWER_THETA_AUDIT_073.md) approves the two-copy proof, the compact set and the application. Therefore the application is promoted to **PROVED/APPROVED**, instead of CONDITIONAL. It is not deduced from log-concavity alone, and the historical source 103_43 is not modified.

With M(u)=L(u+1/2) in the normalization of CONE001, RESULT proves M-uM'>0 for ALL u>0. This surpasses the previous domain of the arithmetic comparison of CONE001§5, restricted to u+1/2>=32. The comparison of higher polynomial tilts of 103_43 remains a distinct obligation.

## 8. Explicit corollary: all real two-generator planes

For a>1 define, keeping the full constants and arithmetic of CONE001,

    L(a)=1/a+1/(a-1)-(log pi)/2+psi(a/2)/2
                         -sum_(m>=2)Lambda(m)m^(-a).

Let a1=a, a2=b, both greater than 1. If a!=b, the real symmetric matrix

    K_(i,j)=[L(ai)+L(aj)]/(ai+aj-1), i,j=1,2,

is POSITIVE DEFINITE. Consequently, for any real pair (c1,c2)!=(0,0),

    W[c1 exp(-(a-1/2)t)1_(t>0)
          +c2 exp(-(b-1/2)t)1_(t>0)] > 0.               (TWO-GENERATORS)

Proof: by symmetry assume u=a-1/2>v=b-1/2>0. RESULT and §6 give

    1<L(a)/L(b)<u/v.

The diagonal entries of K are positive, and the exact criterion of CONE001§3 states that the determinant is positive when

    v/u<L(a)/L(b)<u/v.

Both inequalities are strict here. Sylvester proves positive definiteness. The polarization formula of CONE001§1 identifies K EXACTLY as the matrix of W on the two exponentials, including ARCH, polar and ALL contacts; not merely the individual parts are transferred.

For the exterior powers rho(X)=c1 X^(-a)+c2 X^(-b), X>1, the map Z of CONE001 gives the coefficients d_i=c_i zeta(ai) of those exponentials. Since zeta(ai)>0 for ai>1, the matrix of the exterior form is an invertible diagonal congruence of K. It is also positive definite for distinct exponents.

If a=b, K is only positive semidefinite: the two generators coincide. The time function is nonzero exactly when c1+c2!=0, and in that case its W is strictly positive. The nonzero coefficient vector (c1,-c1) represents the zero function and has no positive energy. The same precision holds for coincident exterior powers.

This corollary does not claim positivity for three generators, all orders, their full linear envelope, or a new window T. It is a proved extension of the real comparison of TWO generators to all exponents a,b>1. Papers untouched; global sign OPEN.
