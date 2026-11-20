# POWER_DIMENSIONAL_CUTOFF_051 — Archimedean cutoff linear in the dimension

Status: **PROVED; independent audit APPROVED in POWER_DIMENSIONAL_AUDIT_051.md and further review, including the correction of the second-sector factor.** Effective bound for ARCH over ALL of Q^j V_n, simultaneous in n and j. It is not yet a sign cutoff for W. Papers untouched.

## 1. Antecedents and precise difference

Consulted ROUTES-TRIED-INDEX/README, master grid and CROSSWORD-TO-D; re-read HIGHPASS015, CENTERED_CUTOFF049 and STATE050. HIGHPASS015 proves an eventuality uniform in numerators for EACH fixed dimension, without an effective cutoff as a function of it. CENTERED_CUTOFF049 gives j>=14 in dimension12. The reduction by Jacobi sectors exists in JOINT_SCALE016 and is not presented as new.

The difference is an explicit inverse-moment bound for ALL n,j and ALL numerators, and from it a LINEAR cutoff j>=ceil(7n/6) with an archimedean lower bound independent of n. An explicit cutoff for any requested archimedean margin is also given. It is not claimed that the same cutoff controls the other terms of W.

## 2. General moment bound

Fix u=63/2 and Q(s)=s/(s+u). For integer n>=1, F!=0 in V_n={P(s)/(s+u)^n:degP<n}, and integer j>=1, take the normalized spectral probability of G=Q^jF. Put

    r=u² E_G[tau^-2], d=n-1, t=2j-1.

Then

    t r <= 1+2sqrt[d(d+2j)r].                            (GENERAL)

In particular,

    r <= [sqrt(d(d+2j))+sqrt(d(d+2j)+2j-1)]²/(2j-1)².   (ROOT)

Proof: on the circle z=(i tau-u)/(i tau+u), F is the base mode times a polynomial A(z) of degree<=d. Put z=exp(2ix), q=cos²x, y=sin x. Centring by exp(-idx) leaves frequencies of the same parity as d. For odd d there appear cos x R(y)+S(y), with R even of degree<=d-1 and S odd of degree<=d. For even d there appear S(y)+cos x R(y), with S even of degree<=d and R odd of degree<=d-1. If d=0, the second sector is omitted. In ALL cases the cross terms are odd and vanish in norm and moment.

The two sectors have weights (1-y²)^a and maximal degrees

    (a,Degree)=(j-1/2,d), (j+1/2,d-1).

Integration by parts and the polynomial bound proved in CENTERED_CUTOFF049§3 give for each sector

    2a r_sector <= 1+2sqrt[Degree(Degree+2a+1)r_sector].

The second sector has larger 2a and Degree(Degree+2a+1)=(d-1)(d+2j+1)<=d(d+2j): the difference between the latter majorant and that product is 2j+1>0. Hence it is dominated by the same root as the first. The total ratio is a positive mixture of the sector ratios; all lie below ROOT. This proves GENERAL and ROOT for ALL real or complex numerators. The integrations are finite because j>=1 implies a>0.

## 3. An explicit linear cutoff, with rational constant

For ALL n>=1 and ALL j>=ceil(7n/6),

    r<49/20,
    E_G[tau^-2]<1/405,
    ARCH[G]/||G||²>859/800.                              (LINEAR)

Proof: the coefficients1/(2j-1) and sqrt[d(d+2j)]/(2j-1) of the normalized GENERAL decrease with j; for the second it suffices to differentiate(d+2j)/(2j-1)², whose derivative is negative for d>=0,j>=1. When d=0, that coefficient is zero. Hence it suffices to verify at the REAL value j0=7n/6, even though j of the orbit is an integer.

With b=49/20,

    (2j0-1)b-1=(343n-207)/60>0,
    [(2j0-1)b-1]²-4b(n-1)(n-1+2j0)
      =(49n²+10878n+7569)/3600>0.

The positive root of the quadratic in sqrt r lies below sqrt b. GENERAL gives r<b for all indicated j. Dividing by u²=3969/4 gives E tau^-2<1/405. The same Jensen/digamma proof of CENTERED_CUTOFF049§6, which only uses that moment, gives ARCH>859/800. It does not depend on the dimension. For n=12 the cutoff recovers exactly j>=14.

## 4. Cutoff for any moment or archimedean margin

For any b>0 define

    T(n,b)=1/2+[(2n-1)+2sqrt((1+b)n(n-1))]/(2b),
    J(n,b)=floor(T(n,b))+1.

Then for ALL j>=J(n,b), GENERAL implies r<b. Indeed, setting t=2j-1 and requiring that b lie above ROOT is equivalent to

    bt-1>0,
    b²t²-2b(2n-1)t+1-4bn(n-1)>0.

The larger root of this last quadratic is[(2n-1)+2sqrt((1+b)n(n-1))]/b; the definition of J strictly exceeds it. This cutoff is O_b(n), and it is explicit, with no hidden convergence constant.

Consequently,

    ARCH[G]/||G||²
      > log[u/(2pi sqrt b)]-sqrt b/u-b/(2u²).            (ARCH-b)

For a prescribed margin h>=0 one may choose, for example,

    b_h=(u²/64)exp[-2(h+1)].

Then j>=J(n,b_h) guarantees ARCH[G]>h||G||²: the logarithm of ARCH-b is greater than h+1 because2pi<8, while the two errors sum to less than1/8+1/128<1. One thus obtains an explicit linear cutoff for any fixed archimedean margin.

## 5. What it does not provide as an induction from050

The result050 provides the complete block of twelve poles and a restricted space of thirteen poles with zero numerator. LINEAR does not certify the indices j<ceil(7n/6) of a new dimension and does not order the COMPLETE form when n changes. FULLTEL transports in one dimension n starting from an already positive base block V_n and restricted gains of dimension n+1; it does not create the positivity of V_(n+1) from V_n.

Therefore no sign recurrence in n is obtained from050 with the data proved here. Both the initial segment of each dimension and the joint control of the polar and ALL the contacts in the tail are missing. In particular, the weighted trace010 used to pay for the contacts in050 increases with the dimension; a constant lower bound on ARCH does not automatically pay that cost. The specific polar bound of dimension12 is not declared uniform in n either. HIGHPASS015 keeps its complete eventuality at each fixed dimension, but LINEAR is for now an effective cutoff of ARCH, not of W.

The complete table and the global sign remain OPEN. No new window T is certified and no paper is edited.
