# POWER_QUADRATIC_EXPLICIT_017 — Explicit quadratic cone, all N>=2, for P=1

Status: PROVED, reviewed independently; see POWER_INTERIOR_AUDIT_017 §9 and POWER_QUADRATIC_EXPLICIT_AUDIT_017. Separate extension: it does not modify the audited theorem POWER_QUADRATIC_017 nor any paper.

## Antecedents and new reason

The corpus/index/grid/crossword consultations documented in QUADRATIC017 are kept. That memo proves a quadratic cone with a conservative threshold N0(c) because it shifts the spectral density only to Im z=1. The difference here is to use a WIDER strip, Im z=15<u/2, and to split the integral so that its normalisation is preserved. Thus the cost of the comb is small and an EXPLICIT cone from N=2 is obtained, without assuming uniformity of the falsified time norms016. The numerator P=1 is not changed nor is it extrapolated to all numerators.

## 1. Theorem

For u=63/2, N>=2 and integer k with k>=10000N², let f have transform F(s)=s^k/(s+u)^(N+k). Then

    |c_f(t)|/||f||² <5 exp(−15|t|), for every real t,     (CORR15)
    W[f]>(49/50)||f||².                                  (CONE)

All contacts are included. The constant10000 is not meant to be optimal.

## 2. Shifted density and correct splitting of regions

Use rho(z)=z^(2k)/(u²+z²)^(N+k), I=∫rho(x)dx, eta=15, y=sqrt(x²+eta²), T=u²/(y²+u²), M=N+k. As in017,

    |rho(x+i eta)|=rho(y)(1−aT²)^(-M/2),
    a=4eta²/u²=400/441.

Now split into |x|>=eta and |x|<=eta. In the main region y>=sqrt(2)eta and dx/dy<=sqrt(2)<2. This splitting is important: using y>=2eta in the main region would give too crude a bound for the small region when employing only u²−eta² as denominator.

We have k>=100N, so M/k<=101/100. The inequality −log(1−z)<=z/(1−z) proves

    (1−aT²)^(-M/2)<=exp(5kT²),

because aM/[2k(1−a)]<=202/41<5.

## 3. Main part: two different uses of the logarithmic inequality

Under the real density rho/I, T~Beta(b,a0), with b=N−1/2 and a0=k+1/2. On T<=32N/k,

    exp(5kT²)<=exp(5120N²/k)<=exp(64/125)<=125/61.

The last bound uses exp(x)<=1/(1−x) for0<x<1.

For the tail T>32N/k exp(5kT) is not used: a better inequality of the ORIGINAL expression is kept. By convexity of −log(1−z),

    −log(1−aT²)<=−a log(1−T²)<=−a log(1−T).

Since aM/2<=202k/441<k/2,

    (1−aT²)^(-M/2)<=(1−T)^(-k/2).

The new beta parameter is a'=k/2+1/2. By the same gamma/Jensen inequalities as in017,

    B(a',b)/B(a0,b)<=exp(N²/k)2^N.

Markov with the integer moment N gives

    P_(a',b)(T>32N/k)
      <=(k/(32N))^N(2N/(k/2))^N=(1/8)^N.

The product of both bounds is less than

    exp(1/10000)(1/4)^N
      <=[10000/9999]/16=625/9999.

Hence the main contribution to the normalised shifted integral is less than2(125/61+625/9999).

## 4. Small region: its normalisation keeps the exponential gain

On |x|<=eta, |x+i eta|²<=2eta² and |u²+(x+i eta)²|>=u²−eta². Using the lower beta bound BL of017,

    ∫_(|x|<=eta)|rho(x+i eta)|dx/I
      <=(2eta/u) A^N r^k(2k/N)^(N−1/2)exp(2N),
    A=u²/(u²−eta²)=441/341<2,
    r=2eta²/(u²−eta²)=200/341<3/5.

Put t=k/N>=100. The function t/4−log(2t) is increasing from100, and log200<6, logA<1. Thus

    logA+log(2t)+2<t/4,

whence all factors except r^k and2eta/u are bounded by exp(k/4). Moreover log(5/3)>1/2 by the first strict term of its atanh series; hence r^k<exp(−k/2). Since2eta/u=20/21<1, the small contribution is <exp(−k/4)<1/100. The comparisons exp6>200 and exp5>100, used here, are verified with finite positive sums of their series; there are no numerical approximations.

Adding the two regions gives

    ∫|rho(x+15i)|dx/I
      <1/100+2(125/61+625/9999)<5.

Shifting the contour within |Im z|<u, as in017, proves CORR15. The factors of rho are not separated into two time norms.

## 5. Comb, ARCH and polar with explicit margins

CORR15 and Lambda(q)<=q imply

    |Comb[f]|/||f||²
      <10Σ(q>=2)q^-14
      <=10·2^-14(1+2/13)<1/1000.                         (PR)

q^-14.5 was replaced by q^-14 for simplicity. All contacts remain in the sum.

The beta law and the global lower bound m(tau)>=log(|tau|/(2pi))−4, audited in017, give

    Arch[f]/||f||²
      >=log[u/(2pi) sqrt(k/N)]−4−1/(2k).

Since pi<4, sqrt(k/N)>100 and u·100/8>3^5>exp5, the logarithm is >5. Moreover1/(2k)<1/100. Hence

    Arch[f]/||f||²>99/100.                              (AR)

The polar bound of017 holds unchanged for k>=4N:

    |Polar[f]|/||f||²<400^-k<1/1000.                     (PO)

Combining AR, PR and PO gives W[f]/||f||²>99/100−2/1000>49/50, as claimed.

## 6. Scope

CONE proves a sign in an EXPLICIT joint region of dimension and order, from N=2, for the numerator P=1. It improves the threshold of017 by means of the width of the analytic strip and keeps the infinite arithmetic sum. It does not imply the same cone for ALL P of degree<N; there one would need to control jointly the complex polynomial factor and its normalisation Gram. Nor does it prove the segment k<10000N² nor turn positivity of the tail into positivity of the whole geometric mixture.
