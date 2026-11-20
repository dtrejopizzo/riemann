# POWER_VARIABLE_RATE_HIGHPASS_096 — Projection uniform in the rate

Status: **PROVED, independent audits approved.** See `POWER_VARIABLE_RATE_HIGHPASS_AUDIT_096.md`. Result: for r>=10^12n³, the projection of a fixed exponential onto Q_u^rV_n(u) has squared norm <=200n/sqrt(r), uniformly in EVERY rate u>0. Not claimed: negative sign of W, density of a linear envelope, or continuity of W in L². Papers untouched; no campaigns.

## 1. Consultation and difference

Consulted the project rules, ROUTES-TRIED-INDEX/README, grid R162_2300_MASTER_GRID and CROSSWORD-TO-D; reread 015–016, 053–054, 059–060 and 094. 016 prevents density in a common weighted exponential norm. 094 computes unweighted L² distances at fixed rate. None of those arguments uniformizes the comparison with a fixed target as u varies: the constant Cayley vector also changes with the rate.

Here f_0(t)=sqrt(2u_0)exp(−u_0t), u_0>0, is kept FIXED, and any u>0 is allowed in the approximant. The new object is the projection onto all numerators of Q_u^rV_n(u), not a scalar diagonal or a weighted norm. The proposed proof separates a real interior region via Gegenbauer and the remaining region via the exact Gram matrix 094.

## 2. Projection formula and notation

Use the unitary Cayley transform of 094 at rate u. The fixed target becomes

    H_a(z)=sqrt(1−a²)/(1+az), a=(u−u_0)/(u+u_0), −1<a<1.

The filtered space becomes S_(n,r)=(1+z)^r P_(n−1), where the factor 2^(−r) does not change the subspace. Set xi=−a. If G_ij=binom(2r,r+i−j), i,j=0,...,n−1 and v=(1,xi,...,xi^(n−1)), the squared norm of the projection is

    A_(n,r)(xi)=(1−xi²)(1+xi)^(2r) v^tG^(-1)v.     (PROJECTION)

Equivalently,

    A_(n,r)(xi)=(1−xi²)(1+xi)^(2r)
      ·sup_(degP<n) |P(xi)|²/int_T|(1+z)^rP(z)|²dtheta/(2pi).

This follows from <H_a,z^j(1+z)^r>=sqrt(1−a²)(1−a)^r(−a)^j and the projection formula in a Gram basis. All values xi∈(−1,1) correspond to a rate u>0. The endpoints are not included, but the following bounds are uniform up to them.

The bound to be proved is

    A_(n,r)(xi)<=200n/sqrt(r),
    ALL n>=1, r>=10^12n³, −1<xi<1.              (TARGET)

## 3. Gegenbauer lemma with its constants

For lambda>=1, let C_k^lambda be the polynomial defined by

    C_k^lambda(y)=sum_(j=0)^floor(k/2)
       (−1)^j (lambda)_(k−j)(2y)^(k−2j)/[j!(k−2j)!].

It is orthogonal for the weight (1−y²)^(lambda−1/2), and its squared norm is

    h_k=pi·2^(1−2lambda)Gamma(k+2lambda)
             /[k!(k+lambda)Gamma(lambda)²].

Self-contained verification: the Rodrigues formula is

    C_k^lambda(y)= (−1)^k(2lambda)_k
       /[2^k k!(lambda+1/2)_k]
       ·(1−y²)^(1/2−lambda) D^k(1−y²)^(k+lambda−1/2).

Comparing coefficients verifies Rodrigues. Integrating k times by parts proves orthogonality; all boundaries vanish for lambda>=1. For the norm, D^kC_k=2^k(lambda)_k, and one gets

    h_k=(2lambda)_k(lambda)_k/[k!(lambda+1/2)_k]
                  ·B(1/2,k+lambda+1/2),

equal to the previous formula by Gamma duplication. Thus no asymptotic bound with implicit constants is imported.

Write p_k=C_k/sqrt(h_k). The Gamma identities give

    |p_(2m)(0)|²=(2m+lambda)/pi
       ·Gamma(m+1/2)/Gamma(m+1)
       ·Gamma(m+lambda)/Gamma(m+lambda+1/2),

    |p_(2m+1)'(0)|²=4(2m+1+lambda)/pi
       ·Gamma(m+3/2)/Gamma(m+1)
       ·Gamma(m+lambda+1)/Gamma(m+lambda+1/2).

For x>1/2,

    sqrt(x−1/2)<=Gamma(x+1/2)/Gamma(x)<=sqrt(x).

The upper bound is Jensen for sqrt(T) under a Gamma(x) law; the lower follows from Cauchy–Schwarz Gamma(x)²<=Gamma(x−1/2)Gamma(x+1/2), together with Gamma(x+1/2)=(x−1/2)Gamma(x−1/2). Moreover Gamma(m+1/2)/Gamma(m+1)<=sqrt(pi), by the product of the ratios (j+1/2)/(j+1). Therefore, if the degrees considered are <n,

    |p_(2m)(0)|²<=4sqrt(lambda+n),
    |p_(2m+1)'(0)|²<=16n(lambda+n)^(3/2).          (BASE-VALUES)

For s>=0, the explicit coefficients also give

    |p_(2m)(is)|<=|p_(2m)(0)|
             ·exp[2s sqrt(m(lambda+2m))],
    |p_(2m+1)(is)|<=s|p_(2m+1)'(0)|
             ·exp[2s sqrt(m(lambda+2m+1))].        (IMAGINARY)

Indeed, in the even case the ratio to the value at 0 is the positive sum

    sum_(j=0)^m (lambda+m)_j m_fall_j (2s)^(2j)/(2j)!,

bounded by cosh(2s sqrt(m(lambda+2m))). In the odd case, after dividing by s p'(0), the same sum appears with (lambda+m+1)_j and (2j+1)!; it is bounded by sinh(X)/X<=exp(X), including X=0 by continuity. No cancellation is lost when evaluating at is: all terms have the same phase.

## 4. Centered polynomial and separation of parities

Set d=n−1 and T(theta)=exp(−idtheta/2)P(exp(itheta)). With y=sin(theta/2), if d is even,

    T=E(y)+i sqrt(1−y²)O(y),

where E is even of degree <=d and O odd of degree <=d−1. If d is odd,

    T=sqrt(1−y²)E(y)+iO(y),

with E even of degree <=d−1 and O odd of degree <=d. These are the polynomial identities of cos and sin of integer or half-integer frequencies; they also hold for complex coefficients.

The symmetry y↔−y eliminates the cross term in the norm. After extracting 4^r from |1+z|^(2r), the circular norm is

    (4^r/pi)(||E||_(lambda_E)²+||O||_(lambda_O)²),

with (lambda_E,lambda_O)=(r,r+1) for d even and (r+1,r) for d odd. Here ||.||_lambda uses the weight of §3 and dy, without factor 1/pi. The factor 1/pi comes from dtheta=2dy/sqrt(1−y²), over theta∈[−pi,pi].

## 5. Region xi=exp(−eta), 0<=eta<=1

For 0<xi<=1, set eta=−log xi and s=sinh(eta/2). Evaluating at theta=ieta gives y=is and

    P(xi)=xi^(d/2)T(ieta).

In this section eta<=1, so s<=eta<=1. Use the even and odd orthonormal polynomials of §3. The bounds BASE-VALUES/IMAGINARY, the number of terms <=n and lambda∈{r,r+1} give, when r>=1024n,

    K_E(is)<=8n sqrt(r) exp[8s sqrt(nr)],
    K_O(is)<=96n²r^(3/2)s² exp[8s sqrt(nr)].

K_E,K_O are the sums of squares of the evaluations of their orthonormal bases; absent degrees produce an empty sum. lambda+n<=3r and 4sqrt(3)<8 were used. The two parities of §4 and Cauchy–Schwarz give

    |T(ieta)|²/(||E||²+||O||²)
       <=[16n sqrt(r)+192n²r^(3/2)s²]
                          ·exp[8s sqrt(nr)].       (CENTER-KERNEL)

The factor 2 allows both K_E+(1+s²)K_O and (1+s²)K_E+K_O. This includes n=1: only the even constant polynomial remains.

In PROJECTION, pi<4, xi^d<=1 and 1−xi²<=2eta. Moreover

    ((1+xi)/2)^(2r)
       =exp(−r eta)cosh(eta/2)^(2r)
       <=exp(−3r eta/4),

because log cosh x<=x²/2 and eta<=1. Finally 8sqrt(nr)<=r/4 for r>=1024n. CENTER-KERNEL implies

    A_(n,r)(xi)
      <=128n sqrt(r) eta exp(−r eta/2)
          +1536n²r^(3/2)eta³exp(−r eta/2)
      <128n/sqrt(r)+41472n²/r^(3/2)
      <200n/sqrt(r).                              (NEAR)

Used: max_(eta>=0)eta exp(−r eta/2)=2/(er)<1/r and max eta³exp(−r eta/2)=(6/(er))³<27/r³, together with r>=1024n. The limit eta=0 of the bound is not interpreted as a Hardy vector at the endpoint; it only provides uniformity for xi<1.

## 6. Remaining region −1<xi<=exp(−1)

This region includes ALL negative xi. Set C=binom(2r,r). The determinant 094 and r>=n give

    det G>=C^n product_(j=0)^(n−1) j!/(2r)^j
          >=C^n(2r)^(−n(n−1)/2).

Indeed, each ratio of the factor j to C is j!(2r+1)_j/(r+1)_j²>=j!/(2r)^j. Since tr G=nC,

    lambda_min(G)>=det G/(nC)^(n−1).

For |xi|<=1 one has ||v||²<=n. Moreover C>=4^r/(2r+1), because it is the largest of the 2r+1 coefficients of (1+z)^(2r). Since 1+exp(−1)<3/2, PROJECTION is bounded by

    A_(n,r)(xi)
       <=(2r+1)(9/16)^r n^n(2r)^(n(n−1)/2).       (FAR-GRAM)

For r>=10^12n³, the logarithm of all factors except (9/16)^r is less than r/100. In detail:

    log(2r+1)<=2sqrt(r)<=r/500000,
    n log n<=n²<=r/10^12,
    [n(n−1)/2]log(2r)<=n²r^(1/3)<=r/10^8.

The last line uses log(2r)<2r^(1/3), obtained by maximizing log x/x^(1/3), and r^(2/3)>=10^8n². The sum of the three constants is less than 1/100. By e<3 and sqrt(3)<16/9 one has log(16/9)>1/2. Thus FAR-GRAM implies

    A_(n,r)(xi)<exp(−r/4)<1/sqrt(r)<=200n/sqrt(r).  (FAR)

The final comparison uses exp(r/4)>1+r/4>=sqrt(r). No asymptotic approximation in r or n is used.

## 7. Proved consequence and scope

NEAR and FAR prove TARGET for ALL u>0, u_0>0 and r>=10^12n³. Since r>=10^12n³ implies 200n/sqrt(r)<=1/5000, the distance of the normalized FIXED exponential to the UNION of ALL those spaces, allowing all rates, is at least

    sqrt(1−1/5000).

The positive cone 060, r>=10^12[n ceil(log_2(n+1))]^3, is included. This prevents using variation of the rate to repair the L² density of their UNION. It does not treat the addition of other continuous families of initial blocks, nor sums with uncertified cross terms, nor the linear envelope of the union. Nor does it refute the W sign of any member.

The Gegenbauer constants, the separation of parities, both ranges of xi and the interpretation of PROJECTION as a SQUARED NORM were audited independently. It is not recorded as a sign theorem nor as a global closure.
