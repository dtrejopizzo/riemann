# POWER_ENERGY_GROUP_037 — Critical dilation and signed grouping on the energy band

Status: **PROVED**, independent review approved in POWER_GROUP_AUDIT_037.md and verifier PASS reproduced. FIXED rate u=63/2. Papers untouched.

Results: (i) uniform bounds on the real gamma dilation at the energy centre; (ii) analytic falsifier of ABSOLUTE contraction of the Möbius inversion for ALL N>=2^16; (iii) quantitative SIGNED grouping inequality for any FINITE set of primes, with explicit error and sufficient sign condition. The infinite residue is not yet estimated and no sign of W is claimed.

## 1. Corpus and precise difference

Consulted ROUTES-TRIED-INDEX/README.md, R162_2300_MASTER_GRID.md, CROSSWORD-TO-D.md and STATE036; read LOW_TABLE018, SIGNED_MEAN019, INVERSE_KERNEL020, UNIFORM_CUTOFF026, GAMMA_WEIGHT031, PRIME_BALANCE033 and MOVING_BALANCE036.

The main polar–comb cancellation and the divisor identities already belong to018/019: they are not presented as new inequalities. The difference here is to evaluate their recovery on the SAME gamma profile, on the real ENERGY band localized036. There the dilation of the inversion is critical1/m, unlike the contractive regime m^(-2) of033. That limit is proved and, afterwards, the Möbius sign is grouped BEFORE the gamma error to obtain an explicit local inequality, not merely another representation.

The comparison does not introduce a polynomial relative error as if it compensated by itself the small difference between exponential components. The necessary precision of the complete residue remains an open obligation.

## 2. Real gamma profile and energy centre

With d=N−1>=1, keep rho_N(t)=C_N(t)/C_N(0), q_N=−rho_N'/rho_N and

    H_N(x)=−(d/dx)[x^(-1/2)rho_N(logx)]
          =x^(-3/2)rho_N(logx)[1/2+q_N(logx)]>0.

UNIFORM_CUTOFF026 and GAMMA_WEIGHT031 prove exactly

    q'=q²+(2d/t)q−u²,
    0<q'<M_N:=u²/(2N−3), q(0)=0.

Define

    t_N=d/(u²−1/4)=d/992,
    x_N=e^(t_N).

It is the natural critical centre of the energy e^(t/2)rho_N(t): the positive root of the Riccati equation without the term q' is1/2 at t_N. In general, for beta>0,

    q_N(d beta)=sqrt(beta^(-2)+u²)−beta^(-1)+O(M_N),

with error bounded by M_N divided by2sqrt(beta^(-2)+u²), on factoring the quadratic. Hence the mode of e^(t/2)rho_N(t), where q=1/2, satisfies t/d->1/992. This is compatible with m/d->1/32 in036: the positive Laplace integral conditioned on the index has time scale m/(u−1/2), and31·32=992. The centre is not a point chosen by a campaign.

More precisely, at t_N the Riccati equation factors:

    q'=(q−1/2)(q+1984+1/2).

Since q'>0 and q>0, one obtains the REAL bound

    1/2<q_N(t_N)<=1/2+M_N/1985.                          (CENTER)

## 3. Critical dilation with uniform remainder

For real m>=1, write ell=logm and

    D_N(m)=m H_N(mx_N)/H_N(x_N).

The exact identity is

    D_N(m)=m^(-1/2)rho_N(t_N+ell)/rho_N(t_N)
                    ·[1/2+q_N(t_N+ell)]/[1/2+q_N(t_N)].

CENTER and0<q'<M_N give for0<=s<=ell

    1/2<=q_N(t_N+s)<=1/2+M_N(1/1985+s),
    1<=[1/2+q_N(t_N+ell)]/[1/2+q_N(t_N)]<=1+M_Nell.

Integrating the first bound and combining both proves

    m^(-1)exp{−M_N[ell/1985+ell²/2]}
      <=D_N(m)<=m^(-1)(1+M_Nell).                        (DILATE)

In particular, for each fixed m, D_N(m)->1/m as N grows. No absolute value of the arithmetic residue is taken to deduce a sign.

Also, using exp(−z)>=1−z,

    |D_N(m)−1/m|
       <=(M_N/m)[a ell+ell²/2],
    a=1+1/1985.                                         (ERROR)

This is the gamma remainder that allows the signed grouping of§5.

## 4. Falsifier of the proposed ABSOLUTE contraction

The complete inverse019 is h_N(x)=sum_(m>=1)mu(m)mH_N(mx), absolutely convergent for each N. A natural sufficient step would be to require

    sum_(m>=2)|mu(m)|D_N(m)<1

at the energy centre. That step is FALSE uniformly for ALL N>=2^16.

Proof without a Möbius table. For INTEGER R, the number A(R) of squarefree integers<=R satisfies A(R)>R/4: the non-squarefree ones are contained in the union of multiples of k²,k>=2, whose number is <R sum_(k>=2)k^(-2)<3R/4. We used1/4+int_2^infty x^(-2)dx=3/4. DISCRETE summation by parts gives

    sum_(m=1)^R |mu(m)|/m
      =A(R)/R+sum_(n=1)^(R−1) A(n)/[n(n+1)]
      >H_R/4>logR/4.

Subtracting the term m1 proves

    sum_(m=2)^R |mu(m)|/m>(1/4)logR−1.

Fix R=2^18, WITHOUT enumerating its integers. For N>=2^16, the rational verifier proves

    M_N[(logR)/1985+(logR)²/2]<2/3<log2,
    (1/4)logR−1>2.

By DILATE, D_N(m)>1/(2m) for ALL2<=m<=R. Hence

    sum_(m>=2)|mu(m)|D_N(m)
      >=sum_(m=2)^R |mu(m)|D_N(m)>1.                     (ABS-FAIL)

In fact this absolute sum admits no bound uniform in N: for each fixed R its partial limit is sum_(m=2)^R|mu(m)|/m and these sums grow without bound. ABS-FAIL only refutes the contraction step by absolute values in this regime. It does not claim that the SIGNED sum does not contract, that h_N is negative or that W is negative.

## 5. FINITE arithmetic grouping before taking errors

Let Q be a FINITE product of distinct primes. Define on the REAL profile

    K_(N,Q)(m)=sum_(b|Q)mu(b)D_N(mb),
    U_Q=prod_(p|Q)(1−1/p)>0,
    V_Q=prod_(p|Q)(1+1/p),
    mu_Q=sum_(p|Q)logp/(p+1),
    sigma_Q²=sum_(p|Q)p(logp)²/(p+1)².

Here mu_Q is a logarithmic average, not the Möbius function. ERROR, applied AFTER keeping the sign of the main sum, proves

    |K_(N,Q)(m)−U_Q/m|
      <=(M_N V_Q/m) E_Q(logm),                           (SIGNED)
    E_Q(ell)=a(ell+mu_Q)
                    +(1/2)[(ell+mu_Q)²+sigma_Q²].

Proof. The main contribution is exactly sum_(b|Q)mu(b)/(mb)=U_Q/m. For the remainder ERROR is summed with1/b. The probability b|Q with weight(1/b)/V_Q includes each prime p independently with probability1/(p+1). Its moments are Elogb=mu_Q and Var(logb)=sigma_Q²; expanding the quadratic of ERROR gives SIGNED.

This is not merely the identity of an Euler product. It is an inequality with a gamma remainder UNIFORM in N,m and a checkable sign condition:

    M_N V_Q E_Q(logM)<=U_Q/2
      ⇒ U_Q/(2m)<=K_(N,Q)(m)<=3U_Q/(2m), 1<=m<=M.         (WINDOW)

E_Q increases in ell>=0, which justifies extending the condition at the endpoint to the whole interval. For fixed Q, WINDOW allows intervals logM of order sqrt(N) with sufficiently small constant. Translated to x=x_Nm, they are a right part of the real energy band. Positivity of the complete inverse is not concluded.

The concrete gain is that the main constant1/m is replaced by U_Q/m via exact Möbius cancellation, keeping an explicit error. The critical exponent m^(-1) does NOT change. For growing Q the degradation of U_Q/V_Q and of the remainder must also be verified; §8 analyzes an explicit choice without attributing a sign to FULL.

## 6. Where the infinite residue remains

The complete grouping, still with ALL arithmetic integers, is

    h_N(x_N)/H_N(x_N)
      =sum_((m,Q)=1)mu(m)K_(N,Q)(m).                    (FULL)

Each squarefree integer decomposes uniquely into a divisor b of Q and an m coprime with Q. The original series are absolute for fixed N, so this reordering is legitimate.

But the majorant of ERROR/SIGNED, of order(logm)²/m, is NOT summable over all m. Hence it cannot be summed to infinity nor used to erase the complement of WINDOW. Nor does the sign of K_(N,Q) on a window make the exterior sum of mu(m), which keeps its signs, non-negative.

The known identity of018/019 relates the joint residue to this inverse and B:

    P_N−Pi_N=2Lminus_N−F_N,
    F_N=2int_1^infty h_N(x)B(x)dx.

SIGNED is not recorded as an already obtained bound on F_N: one still needs to control the signed arithmetic complement, in addition to integrating the band with its real weights. The precision of the polar−comb difference is not deduced from a polynomial relative error against components of phase lambda^N.

## 7. Result and next obligation

Two substantial facts about a concrete proposal are proved: the ABSOLUTE contraction step fails at the real energy centre for an infinite family of N; the signed FINITE grouping does have a positive main term and an explicit gamma error that preserves its sign under WINDOW. No fictitious model was introduced and Lambda or mu were not altered.

The infinite residue remains open. The constructive continuation must combine that cancellation with a signed bound on the complement, without summing a non-summable error nor converting the sign of a finite group into that of FULL. No sign of W, new coverage or global closure is claimed.

Verifier: tools/power_energy_group_037_verify.py; Fraction/exact intervals for constants and thresholds, PASS. The divisor identities and the uniform bounds are proved analytically. W is not evaluated at any new N nor is a Möbius campaign enumerated. The independent review confirms the core and the adversarial extension of§8. Papers untouched.

## 8. A growing choice of Q: positive groups, absolute remainder still dominant

Complementary adversarial review, on the SAME proposal SIGNED. Letting Q grow does preserve a local cancellation for an explicit choice, but does not pay the complement by the triangle inequality. This result does not invalidate a further SIGNED grouping.

For ALL N>=2^80 take

    K=floor(N^(1/8)), Q=prod_(p<=K)p,
    ell=3N^(1/4), M=exp(ell).

Here K>=1024. The elementary bounds (without asymptotic prime estimates) are

    U_Q>=prod_(n=2)^K(1−1/n)=1/K,
    V_Q<=prod_(n=2)^K(1+1/n)=(K+1)/2,
    U_Q V_Q=prod_(p<=K)(1−1/p²)<=1,
    U_Q<=1/2,
    logQ<=KlogK<=K²<=N^(1/4),
    mu_Q<=logQ, sigma_Q²<=log²Q.

Hence V_Q/U_Q<=K(K+1)/2<=N^(1/4). SIGNED implies, UNIFORMLY in1<=m<=M,

    |K_(N,Q)(m)−U_Q/m|<=epsilon_N U_Q/m,
    epsilon_N<=u²[4a N^(-1/2)+(17/2)N^(-1/4)]<1/100.     (GROW)

Indeed ell+mu_Q<=4N^(1/4), sigma_Q²<=N^(1/2), M_N<=u²/N and a<2. At N>=2^80 the rational comparison suffices

    u²[8·2^-40+(17/2)2^-20]<1/100.

Thus ALL the groups of that window are really POSITIVE. The growth of Q is not invoked only formally.

However,

    sum_((m,Q)=1,m>=2)|mu(m)| |K_(N,Q)(m)| >37/25=1.48,
    0<K_(N,Q)(1)<101/200=.505.                          (GROW-ABS)

The sum on the left keeps ALL the infinite residue; it is bounded below by a finite positive subset of the window.

Proof. Define the FINITE harmonic masses

    S(M)=sum_(m<=M,(m,Q)=1)1/m,
    T(M)=sum_(m<=M,(m,Q)=1)mu(m)²/m.

Since M>Q, all divisors b of Q satisfy M/b>=1. For z>=1,

    H_floor(z)=logz+e(z), 0<=e(z)<=1.

Inclusion–exclusion, BEFORE estimating the error, gives

    S(M)=sum_(b|Q)mu(b)H_floor(M/b)/b
         >=U_Q logM−sum_(b|Q)mu(b)logb/b−V_Q
         >=U_Q ell−V_Q.                                (COPRIME)

The logarithmic term that has been kept has an exact favourable sign:

    sum_(b|Q)mu(b)logb/b
      =−U_Q sum_(p<=K)logp/(p−1)<=0.

The m coprime with Q that are not squarefree are divisible by p² for some prime p>K. Dividing by p² preserves the coprimality condition. By a union of those events with POSITIVE weights,

    S(M)−T(M)
      <=sum_(p>K) p^-2 S(M/p²)
      <=S(M)sum_(n>K)n^-2<=S(M)/K.

Hence T(M)>=(1−1/K)S(M). GROW, applied only to m<=M, proves

    sum_((m,Q)=1,m>=2)|mu(m)| |K_(N,Q)(m)|
      >=(1−epsilon_N)U_Q[T(M)−1]
      >=(1−epsilon_N)
           [(1−1/K)(U_Q²ell−U_QV_Q)−U_Q]
      >=(99/100)[2(1−1/1024)−1/2]>37/25.

We used U_Q²ell>=3N^(1/4)/K²>=3, U_QV_Q<=1 and U_Q<=1/2. The subtraction of1 inside T(M) removes m1, not an uncounted arithmetic contact. On the other hand GROW at m1 gives K_(N,Q)(1)<(101/100)U_Q<=101/200. This proves GROW-ABS with rational constants.

Specific conclusion: THIS growing choice of groups has a positive main term and controlled local error, but the sum of moduli of the remaining groups is even larger than the main group. Hence it does not allow deducing the sign of FULL by diagonal dominance or by a new ABSOLUTE contraction after grouping. The exterior SIGNED sum may still cancel; no sign of h_N, F_N or W is claimed, nor are other choices or signed estimates of the complement excluded.
