# POWER_QUADRATIC_017 — Quadratic packet and the obligation to control the full comb

Status: PROVED uniform autocorrelation bound on the quadratic cone and eventual positivity for P=1; PROVED approximation of the WHOLE arithmetic sum by a modulated Gaussian series. Reviewed independently in POWER_INTERIOR_AUDIT_017.md. No numerical campaigns. Papers untouched.

## Antecedents and new reason recorded before building

Consulted the project rules, JOINT_SCALE016, HIGHPASS015 and TATE_CHAIN009; ROUTES-TRIED-INDEX index and its inventory R2/R5 (criticality, E_gamma, packets and modulated families); grid part3; CROSSWORD-TO-D (packets, Chebyshev fluctuation, Gaussian weights). A generic bound for packets is not relaunched nor is a sign attributed to a central limit theorem.

The concrete difference is the joint scale k~cN² of the SAME rational test P=1: its quantitative autocorrelation is sought and any passage to the infinite sum of the comb must be justified separately. The uniform weighted bounds falsified in016 will not be reused. A result on fixed contacts or truncations will not be declared control of the full comb.

## 1. Theorem: an analytic strip of the DENSITY keeps cancellation

Fix u=63/2, N>=2, k integer, and

    F_(N,k)(s)=s^k/(s+u)^(N+k),
    rho_(N,k)(z)=z^(2k)/(u²+z²)^(N+k),
    I_(N,k)=∫_R rho_(N,k)(x)dx>0,
    R_(N,k)(t)=c_f(N,k)(t)/||f_(N,k)||².

For any c>0, if k>=max(cN²,4N), one proves

    ∫_R |rho_(N,k)(x+i)|dx/I_(N,k) <=C(c),
    C(c)=1+2[exp(4/(25c))+exp(1/c)].                     (STRIP)

Shifting the contour within the pole-free strip |Im z|<u then gives

    |R_(N,k)(t)|<=C(c)exp(−|t|), for EVERY real t.       (CORR)

This bound does not contradict016: the full rational DENSITY is shifted, keeping the product of its two factors, not separated into the weighted norms of F and its conjugate. That separation lost an essential compensation.

## 2. Elementary proof of STRIP: main region

Put M=N+k, y=sqrt(x²+1), T=u²/(y²+u²). The exact algebraic identity is

    |rho(x+i)|=rho(y)[1−(4/u²)T²]^(-M/2).               (MOD)

On |x|>=sqrt(3), y>=2 and dx/dy=y/sqrt(y²−1)<=2. Since M<=2k and 4/(u²−4)<1/100, the inequality −log(1−a)<=a/(1−a) gives

    [1−(4/u²)T²]^(-M/2)<=exp(kT²/100).

Under the probability rho(y)dy/I on the whole line, T has distribution Beta(b,a), with b=N−1/2 and a=k+1/2. It suffices to bound E exp(kT²/100). Split into T<=4N/k and its complement.

On the first segment,

    exp(kT²/100)<=exp[4N²/(25k)]<=exp[4/(25c)].

On the complement, use T²<=T and exp(kT/100)<=(1−T)^(-k/100). The weight changes the beta to a'=99k/100+1/2. The contribution is bounded by

    [B(a',b)/B(a,b)] P_(a',b)(T>4N/k).                  (BT)

Two elementary gamma inequalities suffice. For b>=1,

    Gamma(a+b)/Gamma(a)<=(a+b)^b,
    Gamma(a'+b)/Gamma(a')>=(a')^b.

The first is obtained by integrating psi(x)<=log x; the latter is Jensen for log of a gamma variable. The second is Jensen for its power b. Hence

    B(a',b)/B(a,b)
       <=[(k+N)/(99k/100)]^N
       <=exp(N²/k)(100/99)^N.

By Markov using the integer moment N of the new beta,

    P_(a',b)(T>4N/k)
       <=(k/(4N))^N (b)_N/(a'+b)_N
       <=(50/99)^N.

Here (b)_N<(2N)^N and (a'+b)_N>=(99k/100)^N. Thus BT is less than

    exp(1/c)(5000/9801)^N<=exp(1/c).

The main region of the normalised integral of MOD is therefore <=2[exp(4/(25c))+exp(1/c)].

## 3. Small region and beta normalisation

On |x|<=sqrt(3), |x+i|²<=4 and |u²+(x+i)²|>=u²−1. The length of the segment is less than4. On the other hand,

    I=u^(1−2N)B(k+1/2,N−1/2).

Using the beta integral on T∈[N/(2k),N/k], valid because k>=4N and N>=2,

    B(k+1/2,N−1/2)
       >=[N/(2k)]^(N−1/2) exp(−2N).                    (BL)

We used T^(N−3/2) increasing and (1−N/k)^k>=exp(−2N). Define A=u²/(u²−1)<2 and r=4/(u²−1)<1/100. The normalised small contribution is less than

    (4/u) A^N r^k [2k/N]^(N−1/2)exp(2N).

For t=k/N>=4, (2t)^N<exp(k)<3^k and A^N exp(2N)<18^N<3^k. The expression is less than (4/u)(9r)^k<1. Combined with§2 this proves STRIP.

For CORR, the integrand rho(z)exp(izt) is rational and holomorphic between Im z=0 and1. The vertical sides vanish as Re z goes to infinity, by the decay O(|z|^(-2N)). Shifting upward for t>=0 introduces exp(−t). The symmetry of the autocorrelation covers t<0. No time norm was shifted nor was a false weighted constant assumed.

## 4. Control of the WHOLE comb and eventual sign on the cone

CORR implies, without an assumed sign of contacts,

    |Comb[f]|/||f||²
      <=2C(c)Σ(q>=2)Lambda(q)q^(-3/2)<14C(c).            (PRIME)

We used Lambda(q)<=logq and Σ(q>=2)(logq)q^-3/2<7. This last bound follows from f(2)+∫_2^infinito f(x)dx, since f(x)=(logx)x^-3/2 decreases from2, and log2<7/10. PRIME controls the full infinite sum uniformly in N,k of this cone.

The exact beta law016 gives

    E log|tau|=log u+(1/2)psi(k+1/2)−(1/2)psi(N−1/2).

With psi(x)>=logx−1/x, psi(x)<=logx and the global lower bound of the symbol m(tau)>=log(|tau|/(2pi))−4,

    Arch[f]/||f||²
       >=(1/2)logN+log[u sqrt(c)/(2pi)]−5.              (ARCH)

The polar has normalised absolute value

    (4pi/u)[u²/(u²−1/4)]^N
       [1/(4u²−1)]^k /B(k+1/2,N−1/2).

Applying BL as in§3, with A<2 and r=1/(4u²−1)=1/3968, shows

    |Polar[f]|/||f||²<400^-k,                            (POL)

because 4pi/u<1 and 9/3968<1/400. Thus

    W[f]/||f||²
      >(1/2)logN+log[u sqrt(c)/(2pi)]−5−14C(c)−400^-k.

**Sign theorem:** for each c>0 there exists an explicitly boundable N0(c) such that W[f_(N,k)]>0 for ALL N>=N0(c), ALL k>=cN². It suffices to require N>=max(2,4/c) and

    (1/2)logN+log[u sqrt(c)/(2pi)]>6+14C(c).

It is not a certificate for all numerators: P=1 is kept, as declared. The threshold is deliberately very conservative, but the proof is uniform and controls all contacts.

## 5. Quadratic autocorrelation: quantitative approximation of contacts

If k=ceil(cN²), put mu_N=u sqrt(k/N). The same beta is represented by independent variables X~Gamma(k+1/2,1),Y~Gamma(N−1/2,1): |tau|=u sqrt(X/Y). For any finite T,

    sup_(|t|<=T)|R_(N,k)(t)
        −exp(−u²ct²/8)cos(mu_N t)| <=C_(c,u,T)/sqrt(N)  (GAUSS)

for N large enough. It is proved elementarily as follows:

* The gamma moments up to order four show that, in L¹,
  |tau|=mu_N−(u sqrt(c)/2)(Y−N)/sqrt(N)+O(N^-1/2).
  On the event X/k,Y/N∈[1/2,3/2] one uses Taylor with quadratic remainder of sqrt(X/k)/sqrt(Y/N). Its expectation multiplied by sqrt(N) is O(N^-1/2). On the complement, the fourth moments give probability O(N^-2); Cauchy–Schwarz and E tau²=O(N) give the same error. The linear contribution of X is O(N^-1/2).
* The exact characteristic function of (Y−N)/sqrt(N) is exp(−iz sqrt(N))(1−iz/sqrt(N))^(-N+1/2). Taylor of log(1−iz/sqrt(N)) gives exp(−z²/2)+O_T(N^-1/2), uniformly for z in a compact.
* |exp(ita)−exp(itb)|<=|t||a−b| and the symmetry of tau turn those two estimates into GAUSS.

The same argument holds with k/N²->c, replacing the explicit error by o(1) uniform on compacts of t. In that case one can keep c_N=k/N² in the Gaussian amplitude before passing to the limit.

## 6. The approximation passes to the infinite sum, not only to fixed contacts

CORR, which is independent of GAUSS, provides the summable majorant that was missing in016. The Gaussian envelope is also summable against Lambda(q)q^-1/2. Separating a finite segment and its tail, one obtains for k=ceil(cN²)

    Comb[f]/||f||²
      =−2Σ(q>=2)Lambda(q)q^-1/2
          exp[−u²c(logq)²/8]cos(mu_N logq)+o(1).         (ALL)

The series of ALL is absolutely convergent and uniformly bounded in mu_N. It is not claimed that its sign is favourable, nor is it replaced by zero by means of an unproved oscillation. Control of its magnitude suffices, because ARCH grows logarithmically.

More precisely, E tau^-2=(N−1/2)/[u²(k−1/2)]=O(1/N). The elementary bounds already proved in Paper47, lem:mbounds, give |m(tau)−log(|tau|/(2pi))|<=1/|tau|+1/(2tau²) for tau different from0. By Cauchy--Schwarz and the beta formula, its expectation is O(N^-1/2), since E tau^-2=O(1/N). This and the formula for Elog give

    W[f]/||f||²=(1/2)logN+log[u sqrt(c)/(2pi)]
      −2Σ(q>=2)Lambda(q)q^-1/2
          exp[−u²c(logq)²/8]cos(mu_N logq)+o(1).         (PROFILE)

Thus the autocorrelation need not vanish at each contact; a bounded modulated series remains. The new tool does not need it to vanish.

## 7. Scope and precise limit

A tool was obtained that avoids the falsified uniform time norms016: shifting the rational spectral density jointly. The result proves an eventual sign on the quadratic cone for P=1 and sums all the arithmetic with a uniform majorant. It does not prove that cone for ALL numerators nor control the first dimensions, nor turn the series of PROFILE into a nonnegative object. Nor is criticality invoked as a discard: the necessary lower bound has been proved directly in this concrete family.


## Appendix A. Elementary global digamma bounds used in ARCH

A proof is incorporated here, reviewed independently. For a>0,t real, put g(x)=x/(x²+t²). The digamma series and the harmonic limit give

    Re psi(a+it)=lim_(n->infinito)[logn-sum_(j=0)^(n-1)g(a+j)].

On each unit interval, the difference between the value at the left endpoint and the integral is bounded in absolute value by the integral of |g'| over that interval. Hence the total error is<=integral_a^(a+n)|g'|. If |t|<=a, g decreases and its variation on[a,infinito) is g(a)<=1/a. If |t|>=a, g increases up to|t| and then decreases; its total variation is2g(|t|)-g(a)<=1/|t|<=1/a. In both cases

    Re psi(a+it)>=log|a+it|-1/a,

because integral_a^(a+n)g=(1/2)log[((a+n)²+t²)/(a²+t²)] and the term logn cancels its upper endpoint when passing to the limit. Applying to a1/4,t=tau/2 gives, for tau different from0,

    m(tau)>=log(|tau|/(2pi))-4.

At t0 it also produces psi(x)>=logx-1/x. The other bound psi(x)<=logx is obtained from the gamma integral: psi(x)=ElogX with X~Gamma(x,1), EX=x, and Jensen for log. These proofs justify the two gamma inequalities integrated in BT and the bounds of ARCH without an unverified special citation.
