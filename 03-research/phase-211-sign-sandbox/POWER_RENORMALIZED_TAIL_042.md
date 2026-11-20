# POWER_RENORMALIZED_TAIL_042 — Global cancellation of the affine part and tail at absolute scale

Status: **PROVED**, independent review approved in [POWER_RENORMALIZED_AUDIT_042.md](POWER_RENORMALIZED_AUDIT_042.md); exact verifier PASS. u=63/2 fixed. Papers untouched. Global sign of W OPEN.

## 1. Corpus and difference

Consulted ROUTES-TRIED-INDEX/README, master grid and CROSSWORD-TO-D; reread MASS022, ARCH_CELL026, INTERIOR_SCALE030, GAMMA_WEIGHT031, CRITICAL_BALANCE040 and ENERGY_BAND041§7. The exact mass and the cellwise Euler summation already exist; they are not offered as another sign proof.

The quantitative difference from041 is to eliminate GLOBALLY the affine part−gamma x via MASS before bounding the complement. It is proved that the tail of the renormalized residue, from the SAME cut close to the energy of040, is exponentially small at ABSOLUTE scale. The benefit041 was relative to a possibly exponential energy C_N; that benefit is not added here without its accounting of edges.

## 2. Global normalization without critical Fubini

Keep J_N,h_N from022, J'=−h, sum_(n>=1)J(n)=1 and J(x)->0. All the following integrals and sums are absolute for fixed N by022; no Euler series is integrated at sigma1. Let B1({x})={x}−1/2 off the integers and keep SAWTOOTH041

    B(x)=−gamma x−B1({x})logx+kappa+E(x),
    kappa=(1/2)log(2pi)−1/2, |E(x)|<=1/x.

The CELLULAR Euler summation with its edge1 gives

    int_1^infty J(x)dx=1−J(1)/2+int_1^infty B1({x})h(x)dx.

It can be proved without an external summation formula: on each(n,n+1), integrate B1 J'; the edges are[J(n)+J(n+1)]/2 and the integral−int J. Sum up to an integer and pass to the limit. The jumps of B1 are exactly included.

Integrating−xJ' and using xJ(x)->0,

    int_1^infty xh(x)dx
      =1+J(1)/2+int_1^infty B1({x})h(x)dx.

Consequently, with F_N=2int hB,

    F_N/2=−gamma+(kappa−gamma/2)J_N(1)+R_N,
    R_N=−int_1^infty h_N(x)B1({x})(logx+gamma)dx
                            +int_1^infty h_N(x)E(x)dx. (RENORMALIZED)

This identity by itself prescribes no sign. Next a part of R_N is controlled with absolute precision.

## 3. Quantitative result

For ALL N>=2^80, let

    T=(N−1)/992+5, X=exp(T),
    R_N^tail=−int_X^infty h_N B1({x})(logx+gamma)dx
                                  +int_X^infty h_N E dx.

Then

    |R_N^tail|<=N(T+2)exp(−3T/2)<exp(−N/1000).       (ABS-TAIL)

The full complement is therefore interior in the exact formula

    W[g_N]/norm²
      =ARCH_sharp+2gamma−(2kappa−gamma)J_N(1)
                 −2R_N^inside+epsilon_N,
    |epsilon_N|<2exp(−N/1000),

with inside integrated from1 toX and with the same REAL E041. No sign of that interior expression is claimed, nor that its margin exceeds the error.

## 4. Real dilation and full derivative of the inverse

Set delta0=2000/N, v0=1/2+delta0 and t0=2(N−1)v0/(u²−v0²). The corollary040 proves t0<T and q(t0)>v0. Monotonicity of q gives, for t>=T,

    q(t)>1/2+2000/N,
    rho(t+logm)<=rho(t)m^(−q(t)).

By the elementary integral of a decreasing series,

    sum_(m>=1)m^(−1/2)rho(t+logm)
       <=rho(t)[1+N/2000]<N rho(t)/1000.              (DILATION)

No Möbius cancellation is invoked for this estimate. It is valid AFTER eliminating the affine part; the residual weight allows exploiting its additional gain1/x.

Write g=rho/2−rho'=(1/2+q)rho, H=x^(−3/2)g(logx). One has0<q<u,0<q'<M=u²/(2N−3)<1 and rho<=1. Hence

    |g|<=32rho,
    |g'−(3/2)g|
      =rho |q'−q(1/2+q)−(3/2)(1/2+q)|
      <=rho[1+(u+3/2)(u+1/2)]=1057rho<1100rho.

Differentiating the absolute series022 h(x)=sum mu(m)mH(mx) is legitimate in the tail; the same majorant dominates its derivatives. DILATION produces

    |h_N(x)|<=N x^(−3/2),
    |h_N'(x)|<=2N x^(−5/2), x>=X.                    (REAL-DECAY)

These bounds keep ALL the divisors. h' negative is not presupposed nor is an unproved monotonicity of h deduced.

## 5. Periodic primitive and counted lower edge

Use Q2 from041, continuous and periodic, Q2'=B1 almost everywhere and||Q2||_infty=1/16. If V(x)=logx+gamma, integration by parts gives EXACTLY

    R_N^tail=h_N(X)V(X)Q2(X)
       +int_X^infty Q2(x)[h_N'(x)V(x)+h_N(x)/x]dx
       +int_X^infty h_N(x)E(x)dx.                    (TAIL-BOUNDARY)

The infinite edge vanishes by REAL-DECAY. Q2 has no jumps and the values of B1 at integers do not change the integrals. The edge X is kept, even if X were an integer. The error E is not assumed to have a favourable sign.

With0<gamma<1, REAL-DECAY and |E|<=1/x,

    |R_N^tail| <= (N X^(−3/2)/16)(T+1)
      +(N/16) int_X^infty x^(−5/2)[2(logx+1)+1]dx
      +N int_X^infty x^(−5/2)dx
    =N X^(−3/2)[(7/48)(T+1)+55/72]
    <N(T+2)exp(−3T/2).

Here all edges and variations have been counted, including those of the real periodic correction.

## 6. Absolute exponential constant and scope

T>N/992 and T+2<N for N>=2^80; hence the last bound is less than N²exp(−3N/1984). The positive inequality of the exponential

    exp(N/4000)> (N/4000)²/2>N

already holds for N>32000000. Thus N²<exp(N/2000), and

    3/1984−1/2000>1/1000

proves ABS-TAIL without evaluating an N or a prime sum.

The remaining obligation is the RENORMALIZED interior and its balance with ARCH_sharp and J_N(1). Unlike the energy cost041, the error here is absolute and exponentially decreasing; it is not identified with a global margin nor is the interior declared favourable. The cancellation of the affine part was carried out via exact MASS, not by a critical Fubini sum|mu|/m. There is no campaign of orders, contacts or precisions.
