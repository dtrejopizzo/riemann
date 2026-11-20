# POWER_DISCRETE_BALANCE_027 — Positive joint tail with controlled gamma magnitude

Status: **PROVED** complete discrete mass and uniform inequality of the JOINT tail using the real gamma/logconcave cutoff; **PROVED** 0<joint tail N129 from4096<10^(-36). Interior and sign of W **OPEN**. Independent audit approved in POWER_JOINT_AUDIT_027.md, verifier PASS reproduced. Papers untouched;026 and its audit are not modified.

## 1. Corpus, new reason and limit of the masses

Read the project rules, CUMULATIVE_INVERSE022, ARCH_CELL026, UNIFORM_CUTOFF026 and STATE026. Consulted index/grid/crossword on sampling, Euler–Maclaurin, masses and Möbius. Divisor inversion and summation are classical. The additional mass identities are not presented as new sign inequalities.

The difference here is to combine the signed JOINT kernel Omega026 with the real cutoff and the logconcavity of D026 to prove a one-sided bound of a complete contribution of W, not only of ERR. Its magnitude is also controlled at the SAME N129 to avoid confusing favourable localization with compensation of the interior.

Brief limitation: two scalar masses, even with K>=0, do not suffice to force the positive pairing. A bump next to3/2, where Omega<−.1, can carry almost all the integral mass; ever narrower bumps at2 fix the mass of samples without a fixed integral cost, since the singularity of Omega is only logarithmic. This generic construction does NOT keep the real gamma form. No new route is devoted to that falsifier: the positive result below uses precisely the cutoff and gamma form that exclude choosing K arbitrarily.

## 2. Complete discrete mass and functional restriction

For each N>=2, the series of022 are absolutely convergent and

    sum_(n>=1)J_N(n)=1,
    sum_(n>=1)n h_N(n)
      =sum_(r>=1)rH_N(r)sum_(m|r)mu(m)=H_N(1)=1/2.

Hence

    sum_(n>=1)K_N(n)=3/2.                                (SAMPLE)

The stronger functional identity, by the same absolute inversion, is

    sum_(n>=1)K_N(nx)=G_N(x):=x^(-32)D_N(logx)>0, x>=1.   (SCALES)

Both are exact real restrictions; neither is used here as if it implied by itself positivity of int K Omega. The inverse adjoint of SCALES leaves the weight Omega intact on1<t<2, so it does not automatically eliminate its negative region either. The specific form D_N=33P_N−P_N' and its logconcavity proved025/026 are kept.

## 3. Complete formula of Omega by floors

Let n=floor(t), L_n=sum_(j=1)^n jlogj and c=−gamma−log(4pi). From OMEGA026 one obtains, for non-integer t,

    Omega(t)=H_n+[sum_(j=1)^n jlog((t+j)/(t−j))−2L_n
                      +(c−1)n(n+1)/2]/t².               (FLOOR)

Proof: T(t)=sum_(j<=t)j allows separating the sharp kernel as a sum of n copies of the integral I026, with cutoff t/j. Each copy contributes c+log((t+j)/(t−j)). Adding2C_B of022 gives FLOOR. All jumps and the one-sided logarithmic singularities at integers are kept. It is not an asymptotic approximation.

Define the constant

    ell=1+gamma/2−(1/2)log(4pi)>1/50.                      (ELL)

The bound is proved by rational intervals003. ell is a constant of the main continuous balance; uniform convergence Omega(t)->ell is NOT claimed, impossible in the presence of logarithmic peaks arbitrarily close to the integers.

## 4. Uniform inequality of the joint weight

**Theorem.** For non-integer t>=2,

    Omega(t)>=ell−[4logt+9]/t.

In particular Omega(t)>9/1000 for t>=4096, except at the isolated points of logarithmic singularity, which do not affect any integral.                   (OMEGA-TAIL)

Proof. The sequence H_n−logn decreases to gamma, and n>=t−1. Hence

    H_n>=logt+gamma−2/t.

The function f_t(y)=ylog((t+y)/(t−y)) increases on0<=y<t. Its right-endpoint sum satisfies

    t^(-2)sum_(j=1)^n f_t(j)
      >=int_0^(n/t) v log((1+v)/(1−v))dv
      >=1−[log(2t)+1]/t.

We used int_0^1 v log((1+v)/(1−v))dv=1 by the telescoping series; the missing stretch, of length delta=(t−n)/t<=1/t, is <=delta[log(2/delta)+1].

By monotonicity of ylogy,

    2L_n/t²<=logt−1/2+[3logt+1]/t+7/(2t²).

Indeed the sum is compared with int_1^(n+1)ylogy dy, using n+1<=t+1 and log(t+1)<=logt+1/t. Finally c−1<0 and n(n+1)/(2t²)<=1/2+1/(2t). Substituting into FLOOR gives ell as constant term and an error <=

    [4logt+4+log2+(1−c)/2+7/(2t)]/t
      <[4logt+9]/t.

The last inequality uses t>=2, gamma<1, log2<.7 and logpi<1.2. The function (4logt+9)/t decreases for t>=2. At4096, log4096=12log2<8.4 and ELL prove OMEGA-TAIL by rational arithmetic. QED.

## 5. Joint inequality for the REAL gamma K

Use the cutoff tau_N=min(t_J,t_R) of UNIFORM_CUTOFF026 (and its affine case N2). For x>=exp(tau_N), the logconcavity/cutoff proof provides on the COMPLETE Möbius sum

    G_N(x)/4<=K_N(x)<=7G_N(x)/4,
    G_N(x)=x^(-32)D_N(logx)>0,
    G_N'(x)/G_N(x)<=−2/x.

Thus, for ANY T>=max(4096,exp(tau_N)), the real joint balance satisfies

    0<(9/4000)int_T^infty G_N(t)dt
      <=int_T^infty K_N(t)Omega(t)dt
      <=(7/4)G_N(T){T(logT+2)+3T²}.                      (JOINT-TAIL)

The lower bound uses OMEGA-TAIL; it is a real signed inequality, not the isolated mass identity.

To prove the upper bound, FLOOR gives

    Omega(t)<=logt+1+t^(-2)sum_(j<=t)jlog((t+j)/(t−j)),

since −2L_n and (c−1)n(n+1)/2 are non-positive. Moreover G_N(t)<=G_N(T)(T/t)² by the cutoff. The first integrated term is G_N(T)T(logT+2). For the second a positive sum is interchanged and each integral is extended down to j:

    sum_(j>=1)j int_(max(T,j))^infty t^(-4)log((t+j)/(t−j))dt
      <=sum_(j>=1)j^(-2) int_1^infty z^(-4)log((z+1)/(z−1))dz
      <(2)(2log2)<3.

The integral is bounded by replacing z^(-4) by z^(-2), whose change v=1/z gives2log2. This proves JOINT-TAIL without numerical sampling or enumeration of new cells. The logarithmic singularities are integrated explicitly.

## 6. Magnitude at N129: the exterior guarantee does not resolve the interior

For the SAME N129,025 already proves the cutoff x>=exp(2/3)<2, so T4096 is admissible. Reconstructing D129 with its rational coefficients and evaluating only log4096=12log2 proves

    0<int_4096^infty K129(t)Omega(t)dt<10^(-36).           (SCALE)

No other N is verified nor is a campaign of cells enumerated. The majorant obtained is approximately6.46·10^(-37), but only the exact comparison SCALE is used.

The explicit lower certificate (9/4000)int_4096^infty G129 is positive and less than4·10^(-45). Its integral is computed by the polynomial recurrence31Q−Q'=D, already used024. The small scale of the certificate is NOT an independent upper bound of the real contribution; that upper bound is SCALE.

Consequently

    W[g129]/norm²=int_1^4096 K129 Omega + R,
    0<R<10^(-36).

The sign of the interior integral or of W has not been proved. The deficit of more than.15 observed026 is that of the COMPARATOR which uses only the guaranteed arithmetic benefit.66; it is not called the real interior deficit. SCALE only shows that this tail does not substantially improve that coarse budget. The remaining balance requires keeping the cancellation in the interior region and using the gamma form, not adding masses without an inequality between scales.

## 7. Evidence and scope

Exact verifier: tools/power_discrete_balance_027_verify.py, Fraction/rational intervals, PASS. It proves ELL, the constants of OMEGA-TAIL and the majorant SCALE of the single N129. The uniformity of JOINT-TAIL is proved in the text; it is not inferred from the script.

The exterior joint positivity is new with respect to the positivity of ERR in the cells025, but it does not close the interior pairing nor enlarge the already certified W region. Papers untouched and global sign OPEN.
