# POWER_COEFFICIENT_BALANCE_033 — Finite gamma mixture, adverse Erlang prefix and weighted Abel

Status: **PROVED**, independent review approved in POWER_BALANCE_AUDIT_033.md and verifier PASS reproduced: finite mixture and nonnegative Abel coefficients; **PROVED** complete negative Erlang22 functional. **FALSIFIED in034** the premise of nonnegative sign of ALL weighted prefixes T_m (see follow-up at the end). No new W region nor closure is claimed. Papers untouched.

## 1. Corpus and new reason

Read the project rules, ARCH_EXACT032, ROW_PATTERN029 and GAIN, INTERIOR_CONSTRAINT027 (gamma–Gaussian mixture), GAMMA_BALANCE030 and their audits; consulted ROUTES-TRIED-INDEX, the master grid and CROSSWORD-TO-D.md on Euler/Möbius, partial sums of coefficients, Riesz means and mixtures. Targeted searches for Erlang/survival/truncated exponential found no previous POWER construction of the finite object used here.

The difference with respect to the Gaussian mixture027 is that the representation is FINITE in Erlang survival profiles and its weights come directly from the decreasing gamma coefficients. It does not depend on convexity of the complete form, refuted for the Gaussian mixture030. Abel summation and Erlang profiles are classical; the new bounded information is which concrete component inequality fails on the arithmetic datum and which weighted prefixes would be compatible with the real weights.

Only cutoff22 is studied, motivated by ulog2≈22 and the first arithmetic contact. No sequence of new cutoffs nor another campaign over N is launched. The Abel criterion is declared sufficient and OPEN; it is not called sign progress for being an identity.

## 2. Linear autocorrelation functional and EXACT finite mixture

Fix u=63/2. For a real even function rho with rho(0)=1 and the decays present here, define the linear extension of the explicit functional by

    L[rho]=m0+int_0^infty k_gamma(t)[1−rho(t)]dt
             −2sum_(q>=2)Lambda(q)q^(−1/2)rho(logq)
             +4int_0^infty cosh(t/2)rho(t)dt,
    k_gamma(t)=2e^(−t/2)/(1−e^(−2t)), m0=psi(1/4)−logpi.

The homogeneous extension using m0rho(0) and rho(0)−rho(t) is understood when rho is not normalized. For the REAL gamma autocorrelation rho_N, L[rho_N]=W[g_N]/norm². A rho positive as a temporal function NEED not be an admissible autocorrelation.

With d=N−1, write

    rho_N(t)=e^(−ut)sum_(j=0)^d p_jt^j,
    a_Nj=p_j j!/u^j,
    a_N0=a_N1=1,
    a_N,j+1/a_Nj=2(d−j)/(2d−j),
    a_N,d+1=0.

Hence a_Nj decreases and the weights

    w_Nj=a_Nj−a_N,j+1=a_Nj·j/(2d−j)>=0, j0..d,
    sum_(j=0)^d w_Nj=1

are exact. For S_j(t)=e^(−ut)sum_(r=0)^j (ut)^r/r!, swapping two FINITE sums gives

    rho_N=sum_(j=0)^d w_Nj S_j,
    W[g_N]/norm²=sum_(j=1)^d w_Nj E_j,
    E_j=L[S_j].                                          (MIX)

The term j0 has weight0. MIX keeps ALL contacts and the polar; neither positivity of the E_j nor positive definiteness of each S_j is assumed.

## 3. Coefficients before bounding and the single cutoff22

ARCH_EXACT032, applied to the coefficients u^r/r!, gives EXACTLY

    ARCH[S_J]=a(u)−sum_(r=1)^J (u/2)^r S_(r+1)(16),
    a(u)=psi(16)−logpi.

Here S_p(16) denotes the Hurwitz sum, distinct from the temporal profile S_j; the index p is kept to distinguish them. The linear polar contribution is

    POLAR[S_J]=2sum_(r=0)^J u^r[(u−1/2)^(−r−1)+(u+1/2)^(−r−1)],

while the complete comb is

    PRIME[S_J]=−2sum_(q>=2)Lambda(q)q^(−32)
                         sum_(r=0)^J (ulogq)^r/r!.

All these series are absolute. Each nonzero contact of the comb is NEGATIVE because S_J(t)>0. The signs are kept before estimating.

For J22 the rational certificate proves

    −1/100<E_22<−3/500.                                  (ERLANG-FAIL)

The upper bound uses the ARCH interval of032, the exact rational polar and only contacts2,3, whose real values are Lambda=log2,log3. ALL remaining contacts are adverse and omitting them is legitimate only for that upper bound.

For the lower bound the COMPLETE tail q>=4 is bounded using Lambda(q)<=logq. Each x^(−32)(logx)^ell,1<=ell<=23, decreases for x>=4. Thus its sum is bounded by the endpoint4 plus the integral from4, computed with

    I0=4^(−31)/31,
    I_ell=4^(−31)(log4)^ell/31+(ell/31)I_(ell−1).

The positive sum of those majorants with2u^r/r! proves the lower bound of ERLANG-FAIL. The sign of an arithmetic prefix is not taken for that of the tail.

## 4. Why it is NOT a counterexample to real W

The profile S22 is NOT positive definite. For xi=tau/u>0, its even transform is

    Fourier(S_J)(tau)=[2/(u xi)] Im(1−i xi)^(−J−1).

At J22,xi1, the rational complex computation gives Im((1+i)/2)^23=−1/4096, hence

    Fourier(S22)(u)=−1/(2048u)<0.

Thus ERLANG-FAIL refutes only the premise «each component of the Erlang mixture contributes a nonnegative functional». It is not an admissible direction with W<0 and refutes neither MIX nor the sign of the real gamma function.

There is moreover a uniform bound on the damage of THIS component to the real mixture: for all N>=23,d=N−1,

    w_N,22<=22/d,
    −11/(50d)<w_N,22 E_22<0.                              (WEIGHT)

One used a_N,22<=1 and2d−22>=d. This particular loss is O(1/N); WEIGHT does not control the sum of ALL adverse components, which are not identified via a campaign. Nor does it say that the rest compensates it automatically.

## 5. Weighted grouping that does respect the gamma weights

The stronger condition E_j>=0 fails. A distinct SUFFICIENT condition keeps negative components inside weighted prefixes:

    T_m=sum_(j=1)^m j E_j.

Define v_Nj=w_Nj/j=a_Nj/(2d−j),j>=1 and v_N,d+1=0. For1<=j<d,

    v_N,j+1/v_Nj=2(d−j)/(2d−j−1)<=1.

The difference between denominator and numerator is j−1>=0; for d>=2 the first difference v_N1−v_N2 is exactly0. For d1 there is only one positive coefficient and the result is immediate. FINITE Abel summation gives exactly

    W[g_N]/norm²
      =sum_(m=1)^d [v_Nm−v_N,m+1]T_m,                   (ABEL)
    v_Nm−v_N,m+1>=0.

Hence proving T_m>=0 for ALL m would imply the sign of the WHOLE gamma row k0. It is a SUFFICIENT criterion for that row, NOT for all k nor for the complete Paper46. ERLANG-FAIL does not refute it: jE_j can be negative and be compensated in T_m.

The profile of T_m before applying L is explicit:

    sum_(j=1)^m j S_j(t)
      =e^(−ut)sum_(r=0)^m [m(m+1)−r(r−1)](ut)^r/(2r!).

Also, in a convergent neighborhood of z0, with v=u(1−z) and E0(v)=L[e^(−vt)]=2L_power(v+1/2) in the notation of CONE001,

    sum_(m>=1)T_m z^m
       =z[E0(v)−vE0'(v)]/(1−z)^3.

The exterior real positivity of E0(v)−vE0'(v) from CONE001 does NOT prove positivity of all coefficients of this function. No such inference is recorded. These formulas describe the arithmetic obligation of T_m; they do not settle it.

## 6. Scope and next missing inequality

It remains **OPEN** whether ALL T_m are nonnegative for the real Lambda. No uniform elementary inequality proving that sign has been obtained here; the generating identity is not sold as such. Nor have new diagnostics been added in a sequence of m.

The firm results are MIX with explicit gamma weights, ERLANG-FAIL with the complete comb, the individual uniform loss WEIGHT, and ABEL as a correctly limited implication. The constructive continuation must control the compensations of T_m with the real arithmetic or find a more precise integrated criterion that keeps the gamma weight, without again assuming the already refuted positivity of each component.

Exact verifier: tools/power_coefficient_balance_033_verify.py, Fraction/rational intervals and EM remainder032; PASS. A single cutoff22, two explicit contacts and a complete analytic tail. No new W region nor windowT. Papers untouched.


## Follow-up034

POWER_WEIGHTED_COEFFICIENT_034, reviewed in POWER_COMPARISON_AUDIT_034, proves infinitely many positive and negative terms in T_m. The sufficient premise this note left open is refuted, even up to finitely many exceptions. MIX and ABEL remain valid identities; the sign of their gamma combinations is not decided by this oscillation. Do not relaunch positivity of all T_m as a lemma without changing the grouping or introducing a real compensation.
