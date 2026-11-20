# POWER_ARCH_CELL_026 — Sharp deficit and signed joint kernel

Status: **PROVED** deficit not covered by the bound ERR025; **PROVED** exact joint grouping and falsifier of pointwise positivity of its kernel. Sign W129 **OPEN**. Independent review approved, including the grouping/Fubini and verifier PASS. Papers untouched.

## 1. Corpus and precise difference

Read: the project rules, LOW_TABLE018, SIGNED_BALANCE020, CONTACT_BALANCE021, CUMULATIVE_INVERSE022, CELL_BALANCE024 and INVERSE_LOGCONCAVITY025. Consulted index/grid/crossword (absolute errors, limits of component bounds and the latest balance025). The polar cancellation with the principal term predates 018. It is not presented as new.

The difference from 020 is to combine ARCH_sharp and the cellular pairing BEFORE bounding either. One obtains a joint kernel on the compensated inverse K, and it is proved that the natural lemma "that kernel is nonnegative" is false at an exact point. This is not a reason to abandon the sign: it identifies which pointwise inequality does NOT supply the missing structure. The constraint of being the real gamma kernel remains available and is not eliminated through an abstract class.

## 2. What deficit remains at the SAME N129,k0

The sharp symbol of 018 simplifies exactly by the recurrence of psi:

    m(tau)+1/(tau²+1/4)=Re psi(5/4+i tau/2)−logpi.

The spectral probability of g_N has E(tau/2)²=V_N=u²/[4(2N−3)]. The same complex Euler summation and Jensen proved in 020 are used, now shifting THREE steps from 5/4 to a=17/4. With b_j=5/4+j, j0..2,

    ARCH_sharp[g_N]/norm²<=U_N
      =(1/2)log(a²+V_N)−a/[2(a²+V_N)]+1/(2a)
       −sum_(j=0)^2 b_j/(b_j²+V_N)−logpi.

For N129, u63/2 the rational comparison of logarithms proves

    ARCH_sharp[g129]/norm²<−81/100.                       (DEFICIT)

By 025 one has ERR129<−33/50, which guarantees a benefit of at least .66, NOT an upper bound on its actual benefit. Substituting only that guarantee leaves

    ARCH_sharp[g129]/norm²+33/50<−15/100.

Thus the bound proved in 025 is not enough for W>=0. This inequality is NOT W<0: the full value of −ERR may be larger than .66. The directions of the bounds are not confused.

## 3. Joint grouping that preserves the cancellation

With the normalisations of 022, w_N(x)=x^(−1/2)rho_N(logx), rho_N(0)=1, and

    J_N(x)=x int_x^infty K_N(t)/t²dt,
    w_N(x)=sum_(n>=1)J_N(nx).

The last identity uses mu*1 and absolute Fubini, as in MASS022. Write T(y)=floor(y)[floor(y)+1]/2, including T(y)=0 if 0<=y<1, and

    D(t)=T(t)/t²,
    E_x(t)=T(t/x)/t².

Then

    1=int_1^infty K_N(t)D(t)dt,
    rho_N(logx)=x^(3/2)int_1^infty K_N(t)E_x(t)dt.          (RHO)

The elementary representation of psi gives, with d_*=psi(5/4)−logpi and k(x)=x^(−7/2)/(1−x^(−2)),

    ARCH_sharp[g_N]/norm²
      =d_*+2int_1^infty k(x)[1−rho_N(logx)]dx.

The full pairing ERR=−2int K_N C_B of 022 is kept, with ALL the jumps of B. Substituting (RHO) and grouping before integrating gives

    W[g_N]/norm²=int_1^infty K_N(t)Omega(t)dt,             (JOINT)
    Omega(t)=d_*D(t)+2C_B(t)
       +2int_1^infty k(x)[D(t)−x^(3/2)E_x(t)]dx.          (OMEGA)

These identities are not presented by themselves as a proof of sign. The terms inside the last bracket must remain TOGETHER near x1.

Justification of Fubini. For x close to 1, split T(t)−x^(3/2)T(t/x) into (1−x^(3/2))T(t)+x^(3/2)[T(t)−T(t/x)]. The first part is O(x−1) after integrating against |K|/t². The second only counts crossings n<=t<nx; its absolute integral is O(x−1) by the smooth decay K(t)=O_N(t^(−32)(1+logt)^(N−1)). That cancels the singularity k(x)=O((x−1)^−1). At x infinity one uses k=O(x^(−7/2)) and the same decay. Therefore the grouped double integral is absolute. At integer t, OMEGA may have a one-sided logarithmic singularity; the value at those isolated points plays no role and the singularities are integrable against K. A kernel bounded pointwise at the integers is not required.

## 4. Exact falsifier of the joint pointwise lemma

In the first cell 1<t<2, D(t)=1/t² and E_x(t)=1/t² for 1<=x<=t, 0 for x>t. Moreover C_B(t)=(1−t^(−2))/2. Thus

    Omega(t)=1+t^(−2)[log((t+1)/(t−1))−1−gamma−log(4pi)].   (FIRST)

To verify the simplification without a quadrature, set

    I(t)=int_1^t k(x)(1−x^(3/2))dx+int_t^infty k(x)dx.

Then I'(t)=−1/(t²−1), and

    2I(infty)=psi(1/2)−psi(5/4),
    2I(t)=psi(1/2)−psi(5/4)+log((t+1)/(t−1)).

Using psi(1/2)=−gamma−2log2 proves FIRST. At t=3/2,

    Omega(3/2)=(4/9)[5/4+log5−gamma−log(4pi)]<−1/10.       (FAIL-OMEGA)

The last comparison is certified with the rational intervals of 003. No decimal approximation is used as proof.

Therefore the concrete lemma "after grouping exactly the principal term, ARCH_sharp and all the cellular jumps, the kernel Omega is nonnegative on the whole half-line" is FALSE. The grouping does preserve the cancellation, but its kernel remains signed.

This does not falsify W on the actual datum: K_N is the inverse of the gamma autocorrelation kernel, not an arbitrary function that can be chosen to concentrate at t=3/2. For example, taking a positive K concentrated inside (1,2), normalised by int KD=1, would produce rho(logx)=x^(3/2)>1 for x barely larger than 1, violating the elementary bound of a normalised autocorrelation. The gamma/positive-definiteness information may be essential to control the JOINT pairing, and it is not declared useless because the positivity of Omega fails.

## 5. Result and next concrete obligation

It was proved that the benefit .66 of 025 leaves more than .15 of deficit against the actual sharp term. A true grouping from the outset was also obtained, and a natural uniform inequality for its kernel was refuted by exact computation. It is not claimed that no grouping can work, that W129 is negative, or that the coverage of the table has regressed.

The remaining obligation on this route is a one-sided bound on int K_N Omega that uses the constraints of the real gamma kernel and the arithmetic mass, without replacing K or Omega by assumed signs. The JOINT identity alone does not supply it; FAIL-OMEGA prevents closing by universal pointwise positivity of the new weight.

Exact verifier: tools/power_arch_cell_026_verify.py, PASS. Only N129 for DEFICIT and t3/2 for the analytic falsifier; no parameter campaign or massive precision.
