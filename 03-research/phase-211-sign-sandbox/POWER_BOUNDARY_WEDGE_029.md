# POWER_BOUNDARY_WEDGE_029 — Uniform region u>=64sqrt(N), including k=0

Status: PROVED infinite region in N,k,u; independent review APPROVED and verifier reproduced with PASS. Papers untouched.

## 1. Corpus, difference and theorem

Read the project rules, INTERIOR017/WRN, JOINT_SCALE016 and its weight obstructions, ROW_SPLIT028 and the previous rows; targeted searches in index/grid/crossword (bilateral weights/joint scale/variable u). There is no retry of uniformizing a single temporal norm at fixed u, which016 refuted.

The new difference is to keep the opposite weights +eta and−eta TOGETHER: their temporal shift factors cancel. One obtains a correlation constant controlled by N/u², not by N/u. This is combined with an elementary global lower bound of ARCH that also covers k0, without an individual certificate per dimension.

**Theorem.** For ALL integers N>=1,k>=0 and ALL real rates u>=64sqrt(N), let f have transform F(s)=s^k/(s+u)^(N+k). Then

    W[f]>(2/5)||f||².                                   (WEDGE)

The same sign for all N at a FIXED rate is not claimed, nor sufficiency of this wedge for the bridge to all tests.

## 2. An improvement of WRN via coefficients, valid in both directions

The coefficient of S_N(r) from INTERIOR017 is B_l=(N−1/2)_l/(1/2)_l. If C_l=(2N−1)_l/l!, then B0=C0=1 and for l>=1,

    (l−1/2)(2N+l−2)−l(N+l−3/2)=(N−1)(l−1)>=0.

By ratio comparison, B_l<=C_l and

    S_N(r)<=sum C_lr^l=(1−r)^(-(2N−1)), 0<=r<1.

The beta expansion proving WRN uses eta² and only requires a=u−eta>0 and eta²/a²<1. Hence the SAME proof holds for both eta and−eta when0<eta<u/2, and gives

    ||e^(eta y)f||²/||f||²
       <=[(u−eta)/(u−2eta)]^(2N−1),
    ||e^(-eta y)f||²/||f||²
       <=[(u+eta)/(u+2eta)]^(2N−1).

Neither of those two constants is forced separately to be uniform. Shifted Cauchy–Schwarz keeps their PRODUCT and gives

    |c_f(t)|/||f||²<=e^(-eta|t|)
       ·[(u²−eta²)/(u²−4eta²)]^(N−1/2).                (BILAT)

Indeed, for t>=0 one inserts e^(eta(y+t)) and e^(-eta y) into ∫f(y+t)f(y)dy; the factor e^-eta t remains. Symmetry covers t<0. This is the step that avoids the temporal-mean obstruction016.

## 3. Complete comb uniformly small in the wedge

Choose eta15. Since u²>=4096N, one has u>30. By log(1+x)<=x,

    log([(u²−225)/(u²−900)]^(N−1/2))
       <=675(N−1/2)/(4096N−900)<=675/4096.

The last comparison is equivalent to2048>=900. Moreover exp(675/4096)<=4096/3421<6/5. From BILAT one obtains

    |c_f(t)|/||f||²<(6/5)e^(-15|t|).

Using Lambda(q)<=q and sum-integral comparison,

    |Comb[f]|/||f||²
      <(12/5)sum_(q>=2)q^-14
      <=(12/5)2^-14(1+2/13)<1/5000.                    (PRIME)

The infinite comb is included in full, with no assumed sign of contacts.

## 4. Global lower bound of ARCH without problems at zero frequency

The inequality audited in QUADRATIC017, AppendixA, is Re psi(a+it)>=log|a+it|−1/a. Using the recurrence once from1/4 to5/4 gives, for tau!=0,

    m(tau)>=log|tau|−log(2pi)−4/5−1/(tau²+1/4).        (SYMBOL)

The reciprocal comes exactly from Re[1/(1/4+i tau/2)]=1/(tau²+1/4). No power of2 is lost.

The archimedean energy A_(N,k)(u) increases in k by covariance with Z=tau²/(u²+tau²), so k0 suffices. Its spectral probability has maximal density

    p_max=1/[uB(1/2,N−1/2)]<=sqrt(N)/(u sqrt(pi)).

The beta inequality is proved by Jensen for sqrt(X) with X~Gamma(N−1/2,1): Gamma(N)/Gamma(N−1/2)<=sqrt(N−1/2)<sqrtN. Therefore

    E[1/(tau²+1/4)]<=2pi p_max<4sqrtN/u.                (RECIP)

By the beta formula,

    Elog|tau|=logu+(1/2)psi(1/2)−(1/2)psi(N−1/2)
       >log(u/sqrtN)−1.

Here psi(1/2)=−gamma−2log2>−2 using gamma<3/5,log2<7/10, and psi(x)<=logx. Thus SYMBOL/RECIP give, in the wedge,

    A_(N,k)(u)>log(32/pi)−1−4/5−1/16>9/20.             (ARCH)

The last comparison is elementary: pi<22/7 and

    log(112/11)=3log2+log(14/11)
       >3(693/1000)+6/25=2319/1000.

The first atanh term was used for log(14/11); the bounds on log2 and gamma are already audited and the attached verifier checks them rationally. ARCH covers ALL N>=1, not a list of N endpoints.

## 5. Polar: even sign and small odd budget

Let a=u²−1/4. The beta formulas give polar sign (−1)^k and magnitude p_(N,k) from ROW_SPLIT028. The beta bound of§4 and sqrt(pi)<2 imply

    p_(N,0)<=4sqrt(pi)sqrtN/u·(1−1/(4u²))^-N
       <(1/8)·16384/16383<1/4.

Bernoulli (1−z)^N>=1−Nz and N/(4u²)<=1/16384 were applied. Moreover a>=4095N, so

    p_(N,1)=p_(N,0)N/(2a)<1/(4·8190)<1/1000.

For k>=1, the successive ratios of magnitudes are

    (k+N)/[(k+1/2)(4u²−1)]
      <=(N+1)/[(3/2)(16384N−1)]<1.

Thus all odd polars are >−1/1000. At k0 and at all even k the polar is nonnegative and is kept. Combining with ARCH and PRIME,

    W[f]/||f||²>9/20−1/5000−1/1000>2/5.

WEDGE is proved. The k0 limit does not need a singular bound E tau^-2: RECIP replaced it by an integrable maximal density.

## 6. Verification and scope

The file `tools/power_boundary_wedge_029_verify.py` checks the rational constants and the elementary bounds of gamma/log without sweeping N or k. The inequalities for all parameters are proved in the text.

This is a complete REAL sign region, uniform in three parameters, and includes the k0 edge. It complements the stronger region of ROW_PATTERN029 for k>=1. It is not claimed that variable u suffices for the fixed-rate bridge u31.5: for each N the lower bound on u grows. POWER_SCALE_BRIDGE_LIMIT_029 furthermore proves that positive mixtures of the densities of this region do NOT approximate certain concentrated fixed-rate atoms in L¹. Other mechanisms with additional information are not excluded. No new window T and no paper edits.
