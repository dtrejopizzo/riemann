# POWER_LOW_TABLE_018 — Exact budget of the absolute error in the row k=0

Status: PROVED formula for the budget and its three asymptotic regimes. OPEN sign of the interior family. It is neither a positive advance on the sign nor a new global NO-GO. Papers untouched.

## 1. Corpus, bounded difference and scope

Read: the project rules, TATE_CHAIN009, PACKET_SCOPE_AUDIT009, JOINT_SCALE016, QUADRATIC017 and its extension; index ROUTES-TRIED-INDEX/06 (R2/R5, prohibition of relaunching absolute errors psi−x with exponent>1/2), grid part3 (envelopes with absolute value) and CROSSWORD-TO-D (central criticality and fluctuation).

The polar–main term cancellation and the central residue E0 ARE ALREADY recorded: they are not presented as novelties. The only new contribution here is to compute EXACTLY the cost an absolute bound would have for THIS rational row k=0 and obtain its growth rate, including the endpoint theta=0 and the threshold theta=1/2. This quantification explains why the interior has not been closed using the band tool of017. No prime weight is modified and no falsifier foreign to the test is invoked.

## 2. Concrete row and monotonicity of its autocorrelation

Fix u=63/2, N>=2, g_N(y)=y^(N−1)e^-uy/(N−1)!·1_(y>0), and C_N(t)=c_gN(t). Write c0=C_N(0)=||g_N||². Its quadratic transform is (u²+tau²)^-N.

The gamma representation and the Gaussian integral give, for t>=0,

    C_N(t)=1/[2sqrt(pi)Gamma(N)]
       ·∫_0^infinito s^(N−3/2)exp(−u²s−t²/(4s))ds.

Hence C_N(t)>0 and C_N'(t)<0 for t>0. Moreover C_N(t)<=c0 by Cauchy–Schwarz and C_N(t)/c0->1 for each fixed t as N grows, by the central beta concentration already proved.

These properties allow computing an absolute budget WITHOUT losing a second cancellation between two parts of a signed derivative: the kernel after integrating by parts will be genuinely positive.

## 3. Endpoint and cancellation of the main term

Let psi_Lambda(x)=Σ(q<=x)Lambda(q). To fix the endpoint correctly define

    E0(x)=psi_Lambda(x)−x+1, x>=1; E0(1)=0,
    w_N(x)=x^-1/2 C_N(logx).

The normalized fluctuation is

    F_N=2/c0 ∫_[1,infinito) w_N(x)d(psi_Lambda(x)−x).

Adding1 to the residue does not change its derivative measure and annihilates the boundary term at1. At infinity, w_N E0 tends to0: C_N decays like e^-ut times polynomial, and the elementary bound psi_Lambda(x)=O(x logx) suffices. By integration by parts and x=e^t,

    F_N=2/c0 ∫_0^infinito E0(e^t)e^-t/2
                          [C_N(t)/2−C_N'(t)]dt.         (ERR)

The kernel in brackets is positive. If psi_Lambda(x)−x WITHOUT the+1 were used, its initial value would be−1 and an explicit term +2 would appear; omitting both would be an endpoint error.

The already known identity of cancellation of the main term is

    2AB−2∫_1^infinito x^-1/2 C_N(logx)dx
       =(1/2pi)∫ |ghat_N(tau)|²/(tau²+1/4)d tau.

Hence W[g_N]/c0=Arch_sharp[g_N]/c0−F_N, where Arch_sharp has symbol m(tau)+1/(tau²+1/4). Its limit is C0+4<0, the SAME central residue recorded in009 and the corpus. Neither this equality nor its value is presented as sign progress.

## 4. Exact budget D_N(theta)

Suppose ONLY an absolute bound |E0(x)|<=A x^theta is available, with

    0<=theta<u+1/2.

This range secures all boundary terms and the following integrals; for the usual application theta is near1/2 or1. Define

    b=theta−1/2,
    J_N(b)=∫_0^infinito e^(bt) C_N(t)/c0 dt.

ERR gives |F_N|<=A D_N(theta), and the budget of that bound is EXACTLY

    D_N(theta)=2/c0 ∫_0^infinito e^(bt)
                                  [C_N/2−C_N']dt
              =2+2theta J_N(theta−1/2).                 (D)

Proof: integrating −C_N' produces c0+b∫e^(bt)C_N, and b+1/2=theta. In particular

    D_N(0)=2 for ALL N.

There is no indeterminate term "0 times infinity": b=−1/2, J_N is finite. The equality D computes the integral of the positive majorant used by the method; it does not claim that the real arithmetic error attains that majorant.

## 5. The three regimes, with explicit growth

**Subcritical, 0<=theta<1/2.** Since C_N/c0<=1 and tends to1 locally, dominated convergence gives J_N(b)->−1/b. Then

    D_N(theta)->1/(1/2−theta).

This includes theta0, whose exact value is2. Not even this bounded budget prescribes the sign of F_N: it remains a two-sided magnitude bound.

**Critical, theta=1/2.** The bilateral transform of C_N at zero gives

    J_N(0)=1/[2u^(2N)c0],
    D_N(1/2)=2+1/[2u^(2N)c0]
             ~[sqrt(pi)/u]sqrt(N).

**Supercritical, 1/2<theta<u+1/2.** For b=theta−1/2>0,

    ∫_R e^(bt)C_N(t)dt=(u²−b²)^-N.

Parity of C_N and cosh(bt)<=e^(bt)<=2cosh(bt), t>=0, give

    1/[2c0(u²−b²)^N] <=J_N(b)<=1/[c0(u²−b²)^N].        (L)

The exact norm is

    c0=u^(1−2N)B(1/2,N−1/2)/(2pi)
       ~u^(1−2N)/[2sqrt(pi N)].

Consequently, for fixed theta>1/2,

    D_N(theta)=Theta_(u,theta)(sqrt(N)
                                  [1−b²/u²]^-N).       (GROWTH)

This is the new quantification: the absolute budget not only loses a constant, but grows exponentially in N for any exponent strictly above1/2. At the endpoint1/2 it grows like sqrt(N). The rates come from closed gamma integrals of the SAME test, without individually estimating a large number of contacts.

## 6. What is concluded and what is not

The corpus already excluded using absolute PNT-type errors as the decisive step in the central regime. D/GROWTH neither reopen nor rename that route: they measure exactly its loss for P=1,k=0 and separate the endpoints that a qualitative statement did not specify.

W[g_N]>=0 for all N was not proved. Nor was W[g_N]<0 proved. A positive proof needs a SIGNED ARITHMETIC inequality on ERR compensating the negative central residue; neither the budget D nor the Euler identity supplies that sign. The band tool of017 controls another scale, k>=10000N², and this analysis shows why its absolute control does not transplant to k=0 without an additional cancellation.
