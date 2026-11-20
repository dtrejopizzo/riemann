# POWER_THETA_REMAINDER_077 — One-valley criterion for the real Schur remainder

Status: **PROVED/APPROVED for the real Phi** by the analytic implication and the local verifications OUTER/COMPACT077, integrated in POWER_THETA_REMAINDER_AUDIT_077.md. Compact run 1589 exit0/PASS; independent reproduction 36038 finished exit0/FULL PASS, with matching hash. Positivity of the remainder kernel or of three generators is not claimed. Papers untouched.

## 1. Antecedents and difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, master grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; read THETA_TWO_COPY073, CONTACT_OSCILLATION065, THETA_SCHUR_DENSITY075 and the consultation 076 of STATE075. 073 proves a pair comparison and 075 constructs a positive Phi_u, but none of those positivities orders Z/H_u. 076 identified the zero-mass defect and a sufficient Wronskian still without proof.

The change here is to propose a hypothesis INDEPENDENT of the Schur parameter u, for the original density, and to prove that it implies the real sign of the remainder. It is not assumed that the forcing has a single crossing: in general it has TWO. Its two vanishing moments are kept to obtain the Green sign by convex interpolation, and only the Rolle zero count of 065 is used, without a total positivity property of other kernels. The final section gives a sufficient local condition for the hypothesis; its real verification is kept separate.

## 2. Data already proved and precise new hypothesis

Keep Phi, Z, M, Phi_u, H_u from 075. For u>0, set

    c=M(u), a=M'(0), beta=u²a/(ua-c),
    J(x)=int_|x|^infinity y Phi(y)dy,
    tau(x)=J(x)/Phi(x),
    F_u(x)=J(x)-beta Phi_u(x).

075/076 prove c>0, ua-c>0, Phi_u>0, tau'(x)<0 for x>0 and

    int_R F_u=0,
    Phi_u''-u²Phi_u=cPhi-uJ.

All relevant functions and derivatives decay faster than any exponential. V=-logPhi is even and smooth, with V'>0, V''>0, V'''>0 for x>0 and V'(x)/x->infinity. These are the specific data used below.

The new hypothesis is

    R(x)=[V'(x)+xV''(x)]/[-tau'(x)]
         strictly increasing for x>0,
    R(x)->infinity as x->infinity.                  (R-HYP)

075 and 073 do not by themselves prove R-HYP. The new and separate verifications POWER_THETA_RATIO_COMPACT_077 and POWER_THETA_RATIO_OUTER_077 discharge that hypothesis for the real Phi; below its explicit role in the proof of the implication is kept.

**Conditional conclusion.** If R-HYP holds for the real Phi, for ALL u>0 the function F_u has exactly ONE positive zero, SIMPLE, with negative sign before and positive after. Consequently, for ALL u,z>0,

    T_u(z)>0, G_u(z)>0,                                (REAL-REMAINDER)

with T_u, G_u defined in 076/075. It is a real statement; it does not automatically extend to a kernel inequality.

## 3. Exact forcing and two vanishing moments

Write lambda=u²c/(ua-c)>0. Since J'=-xPhi and J''=(xV'-1)Phi, the equation of 075 gives

    f_u:=(D_x²-u²)F_u=Phi(x) B_lambda(x),
    B_lambda(x)=xV'(x)-1+lambda[tau(x)-a].              (FORCING)

Here beta c=a lambda and beta u-u²=lambda. Both terms are kept; no individual sign is assigned to the forcing.

The boundary conditions F_u'(0)=0 and F_u, F_u' superexponentially small at infinity give

    int_0^infinity f_u(x)dx=0,
    int_0^infinity cosh(ux)f_u(x)dx=0.                 (TWO-MOMENTS)

For the first, integrate the equation and use int F_u=0 and parity. For the second, integrate by parts twice: the boundary expression is cosh(ux)F_u'(x)-u sinh(ux)F_u(x), zero at both ends. There is no delta at 0, by the result 075.

## 4. A valley forces the pattern +,-,+ of the forcing

Since tau'=V'tau-x and R-HYP,

    B_lambda'(x)=(-tau'(x))[R(x)-lambda].

The factor -tau' is positive. Therefore B_lambda first decreases and then increases, or only increases if lambda lies below the initial limit of R. It cannot have more than two positive roots. Moreover B_lambda(x)->infinity, since xV'(x)->infinity and tau>=0.

TWO-MOMENTS forces at least TWO sign changes on the half-line. Indeed, with no changes the first moment is contradicted. With a single crossing b, the product [cosh(ux)-cosh(ub)]f_u(x) would have a strict constant sign on both sides of b; its integral could not be zero, contradicting the two moments. The forcing is not identically zero because B_lambda' cannot vanish on a whole interval under R-HYP.

By the valley and the positive tail there exist exactly two roots 0<b1<b2 and

    f_u>0 on [0,b1), f_u<0 on (b1,b2), f_u>0 on (b2,infinity).

Both roots are simple: they lie on different sides of the single minimum, where R-lambda does not vanish. In particular f_u(0)>0. A single crossing of the forcing was not assumed.

## 5. Convex interpolation: sign of F_u at the origin

Set v=cosh(ux), vi=cosh(ubi)>1 and

    H(v)=v-sqrt(v²-1), v>=1.

One has H(cosh(ux))=exp(-ux). For v>1,

    H''(v)=(v²-1)^(-3/2)>0.

Let ell(v) be the line interpolating H at v1, v2. Strict convexity gives H-ell>0 outside [v1,v2] and H-ell<0 inside. The pattern of the forcing proves

    int_0^infinity exp(-ux) f_u(x)dx
      =int_0^infinity [H(cosh(ux))-ell(cosh(ux))]f_u(x)dx>0.

The affine part of ell vanishes by TWO-MOMENTS. Although H' is singular at v=1, it is neither integrated nor differentiated there; H is continuous at that endpoint and vi>1. All integrals are absolutely convergent.

The Green function of the operator D²-u² with the even boundary conditions and decay carries NEGATIVE sign:

    F_u(x)=-(1/(2u))int_0^infinity
       [exp(-u|x-y|)+exp(-u(x+y))]f_u(y)dy.

In particular

    F_u(0)=-(1/u)int_0^infinity exp(-uy)f_u(y)dy<0.      (ORIGIN)

## 6. Positive tail and exact number of zeros of the defect

The superexponential solution also has the anticausal representation

    F_u(x)=(1/u)int_x^infinity sinh(u(y-x))f_u(y)dy.

Differentiating it twice verifies the equation and the terminal boundary conditions; the difference with F_u would solve the homogeneous equation and have superexponential decay, so it is zero. For x>=b2, the integrand is positive except at the endpoint, so F_u(x)>0.

Extend f_u evenly to the whole line. It has exactly four simple zeros, at +-b1, +-b2. On the whole line,

    -F_u=C_1*f_u,
    C_1(x)=exp(-u|x|)/(2u)=e_+*e_-,
    e_+(x)=exp(-ux)1_(x>=0), e_-(x)=exp(ux)1_(x<=0).

The one-sided Rolle count of 065, used only in its upper direction, shows that this convolution cannot increase the number of zeros COUNTED WITH MULTIPLICITY. To make the application precise: if g=e_+*f, then (exp(ux)g)'=exp(ux)f and exp(ux)g tends to 0 at the left end. Rolle counts one zero between each pair, the reduced multiplicities at multiple zeros and an interior extremum before the first, as in 065. For e_- the argument is reflected and the right boundary is used. The data here are smooth and real analytic; there are no null intervals nor zeros of infinite order. The tails guarantee the boundary conditions, even though they are not polynomials times exponential. The vanishing of moments is not necessary for this upper bound on zeros.

Therefore F_u has at most four real zeros counted with multiplicity. It is even, F_u(0)<0 and it is positive in the tail. It must have an odd number of changes on the positive half-line. Three changes, an additional tangency or a single crossing of multiplicity greater than 1 would require at least six global zeros counted with multiplicity. One concludes that it has exactly ONE positive zero, SIMPLE, with signs negative/positive. This is an application of the mechanism 065 to the concrete forcing, not a generic sign statement about the remainder.

## 7. Positive transform and real Schur remainder

Since int_0^infinity F_u=0 and F_u has one negative/positive crossing at b, for any z>0,

    int_R F_u(x)exp(zx)dx
      =2int_0^infinity [cosh(zx)-cosh(zb)]F_u(x)dx>0.

The identity of 076 is

    t_u=(u/c)F_u,
    T_u(z)=Z(z)-[Z(0)/H_u(0)+z²/c]H_u(z)
          =(u/c)int_R F_u(x)exp(zx)dx,
    G_u(z)=c²T_u(z)/(uzH_u(z)).

075 proves H_u(z)>0 for real z. All factors are positive when u,z>0, so REAL-REMAINDER is obtained.

This does not identify G_u with a logarithmic derivative, does not prove positivity of its two-node kernel and does not claim positivity of three generators of the original form. The generic counterexample 074 still stands: it does not necessarily satisfy the additional hypothesis R-HYP.

## 8. Sufficient local criterion and verified application for the real Phi

For x>0, write only in this section

    p=V'(x), q=V''(x), r=V'''(x),
    D=xq-p>0,
    C=p³+xp²q-pq-xpr+xq²,
    L=D/C, w=1+xq/p.

A concrete sufficient condition for R-HYP is

    C>0,
    L strictly decreasing and L(x)->0,
    w(x)Phi(x)->0 as x->infinity.                  (LOCAL-HYP)

The last is the boundary condition that must be kept when using the theta tail; it is not omitted in an integration by parts.

Proof of the implication: integrating J=int_x^infinity (y/p(y))p(y)Phi(y)dy and using Phi'=-pPhi gives

    J(x)=xPhi(x)/p(x)-int_x^infinity [D(y)/p(y)²]Phi(y)dy.

Moreover a direct differentiation verifies

    -(wPhi)'=C Phi/p².

Therefore

    R(x)^(-1)
      =[int_x^infinity (D/p²)Phi]/[w(x)Phi(x)]
      =[int_x^infinity L(y)(C/p²)Phi(y)dy]
                    /[int_x^infinity (C/p²)Phi(y)dy].    (TAIL-AVERAGE)

The denominator is positive by LOCAL-HYP and the declared boundary condition. It is a tail average of L under a positive density. If L decreases strictly, that average decreases strictly as the lower endpoint increases: values larger than those that remain are removed. Moreover 0<R^(-1)<L(x)->0. This proves R increasing and infinite.

The separate verification of C>0 and L decreasing for the REAL Phi was completed in POWER_THETA_RATIO_COMPACT_077 and POWER_THETA_RATIO_OUTER_077, with the declared boundary conditions and L->0. The compact certificate 1589 finished exit0/PASS and was audited mathematically and at code level; run 36038 independently reproduced the certificate and finished exit0/FULL PASS, with the same hash. The exterior proof was read and its Fraction verifier reproduced independently with three PASS. Thus LOCAL-HYP is discharged and REAL-REMAINDER is **PROVED** for ALL u,z>0. TAIL-AVERAGE by itself was not the sign: it is supplied by these new specific inequalities. Positivity of the two-node kernel of the remainder or of three generators is not deduced.

## 9. Corollary anchored at the auxiliary node 0

Define N(u)=M(u)/u and B(u)=[a/N(u)−1]/u², a=M′(0). 073 gives N′<0 and B>0. Therefore

    (u²B)′=−aN′/N²>0, that is 2B+uB′>0.

Substituting M(u)=au/[1+u²B(u)] into the Schur formula 075 produces, for the pivot p>0,

    G_p(z)=az[B(p)−B(z)]/[B(p)(z²B(z)−p²B(p))].

The denominator only vanishes at z=p, since u²B increases. The removable value is

    G_p(p)=−aB′(p)/[B(p)(2B(p)+pB′(p))]>0.

REAL-REMAINDER implies B′<0. Hence −2<uB′/B<0; for F(u)=uB(u) one obtains −1<uF′/F<1. The exact criterion of CONE001 proves that the kernel K_F(u,v)=[F(u)+F(v)]/(u+v) has all its distinct pairs positive definite.

The auxiliary extension of the original kernel has K_M(0,0)=a and K_M(0,u)=N(u). Its Schur complement is exactly

    K_M(u,v)−N(u)N(v)/a
      =[uN(u)vN(v)/a]·[uB(u)+vB(v)]/(u+v).

It is a positive congruence of the kernel K_F. Therefore the matrix anchored at {0,u,v} is positive definite for distinct u,v>0. The node 0 corresponds to the original exponent a_orig=1/2, outside the class of convergent powers a_orig>1; it is NOT a third admissible W test. This corollary does not prove three arbitrary positive nodes nor positivity of the kernel of G.
