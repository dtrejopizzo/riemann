# POWER_INFINITE_SHOULDER_039 — Positivity of the COMPLETE inverse on an energy shoulder

Status: **PROVED**, independent audit approved in POWER_SHOULDER_AUDIT_039.md and exact verifier PASS reproduced. FIXED rate u=63/2. Papers untouched.

Result: for ALL N>=4,000,000, the COMPLETE arithmetic inverses h_N and K_N are positive for ALL x>=exp(T_N), where

    d=N−1, L=1000,
    v_N=1/2+L/sqrt(N),
    T_N=2d v_N/(u²−v_N²).

The cutoff is T_N=d/992+O(sqrt(N)) and improves the K026 cutoff of scale d/330. No sign of W nor of the interior remainder is claimed.

## 1. Corpus and precise difference

Consulted ROUTES-TRIED-INDEX/README.md, master grid and CROSSWORD-TO-D; read INVERSE_KERNEL020, UNIFORM_CUTOFF026, ENERGY_GROUP037 and SIGNED_MOMENTS038. The Euler/Möbius identity and the centring of the main term are prior; they are not presented as new sign results.

The difference is passing from the FINITE group 038 to the INFINITE arithmetic product while keeping its signed multiplier. Work is done exclusively in sigma>1, where all products, series and moments used converge absolutely. A tilt v>1/2 of the gamma profile moves the centre to the energy shoulder; its moments are controlled through a proved Chebyshev bound. This controls for the first time the complete complement of the inverse in this region, not just a finite Q. There is no campaign over N nor lists of primes.

Two objects are distinguished: h_N is the inverse of H_N; K_N=J_N+xh_N is the compensated inverse of 026. Both are included below so that the comparison with the cutoff 026 refers to the SAME K_N.

## 2. Real objects and tilted profile

Let rho_N be the even normalized gamma autocorrelation and q_N=−rho_N'/rho_N for positive argument. Throughout the memo norm²=Gamma(N−1/2)/[2sqrt(pi)Gamma(N)u^(2N−1)] denotes the norm of the original gamma atom. For c in {1/2,3/2}, define

    g_c(t)=c rho_N(t)−rho_N'(t),
    H_N(x)=x^(-3/2)g_(1/2)(logx),
    G_N(x)=x^(-1/2)g_(3/2)(logx)=w_N−xw_N',
    w_N=x^(-1/2)rho_N(logx).

The COMPLETE inverses satisfy exactly

    h_N(x)/H_N(x)
      =sum_(n>=1)mu(n)n^(-1/2)
                       g_(1/2)(logx+logn)/g_(1/2)(logx),
    K_N(x)/G_N(x)
      =sum_(n>=1)mu(n)n^(-1/2)
                       g_(3/2)(logx+logn)/g_(3/2)(logx).

These formulas come from 019/022, with their Jacobians. For fixed N they are absolute.

For 1/2<=v<=2 put

    a_v=u²−v², t_v=2dv/a_v, sigma=v+1/2,
    f_(c,v)(ell)=exp(v ell)g_c(t_v+ell)/g_c(t_v).

The even extension of rho is used for Fourier. f_(c,v) may be negative on part of the left half-axis; it is not regarded as a positive density. At the physical arguments t_v+ell>=0 the original real profile is kept.

At x=exp(t_v), both inverse quotients are written, for the corresponding c,

    R_c(t_v)=sum_(n>=1)mu(n)n^(-sigma)f_(c,v)(logn).       (FULL)

## 3. Elementary control of ALL arithmetic moments

First, psi_Lambda(x)<=2x is proved for ALL real x>=1. For integer n,

    psi_Lambda(2n)−psi_Lambda(n)<=log binom(2n,n)<=2nlog2.

Each prime power in (n,2n] contributes 1 in Legendre's formula for the binomial, and all other floor differences are nonnegative. For integer M>=6 take n=ceil(M/2). By induction,

    psi_Lambda(M)<=psi_Lambda(n)+2nlog2
       <=2n(1+log2)<(17/10)(M+1)<=2M.

The cases 1<=M<=5 follow from psi_Lambda(M)<=MlogM<=Mlog5<2M; no table of primes needs to be consulted. Passing to floor(x) proves the real bound.

For sigma=1+delta>1, absolute integration by parts gives

    A_sigma=sum Lambda(n)n^(-sigma)
      =sigma int_1^infty psi_Lambda(x)x^(-sigma−1)dx
      <=2sigma/delta,
    B_sigma=sum Lambda(n)logn n^(-sigma)
      <=2sigma/delta².                                  (MOMENTS)

In the second bound one first subtracts the nonpositive term of the integration by parts, −int psi_Lambda(x)x^(-sigma−1)dx, and only afterwards applies psi<=2x to the term sigma logx. No upper bound on psi is used against a sign-changing kernel.

The infinite products are absolutely convergent:

    U_sigma=prod_p(1−p^(-sigma))=1/zeta(sigma)>0,
    V_sigma=prod_p(1+p^(-sigma)),
    V_sigma/U_sigma=zeta(sigma)^2/zeta(2sigma)
                    <=(1+1/delta)^2,
    U_sigma>=delta/(1+delta).                            (PRODUCTS)

Only the absolutely convergent Euler sum and zeta(sigma)<=1+1/delta are used. In 1/2<v<=2, sigma<=5/2 and (MOMENTS) gives A_sigma<=5/delta, B_sigma<=5/delta².

## 4. Gamma Fourier UNIFORM in c and v

The argument of 038 extends to c in {1/2,3/2}, v in [1/2,2] keeping its constants 12000 and 65. The necessary changes are detailed.

The auxiliary POSITIVE density is

    p_v(y)=exp(vy)rho_N(y)/L_v,
    L_v=1/(norm² a_v^N).

It has mean 2Nv/a_v and variance beta_v N/a_v², where beta_v=2(u²+v²). Its mode y_* satisfies q_N(y_*)=v and, by Riccati 026,

    y_*=2dv/[a_v+q_N'(y_*)],
    0<=t_v−y_*<=2dvM_N/a_v²<=4u²/(u²−4)²,
    M_N=u²/(2N−3).

The last bound uses dM_N<=u² and v<=2. The control 0<q'<M_N allows comparing p_v(t_v) with its maximum:

    p_v(t_v)>=p_v(y_*)exp[−M_N(t_v−y_*)²/2]
              >p_v(y_*)/2>=3/(32s_v),
    s_v²=beta_v N/a_v².

Chebyshev gives the last bound on the maximum; the localization and variation of the mode justify evaluating it at t_v. Uniformly, 8u^6/(u²−4)^4<1/100<log2 and s_v<sqrt(N)/22.

The EXACT transform is

    fhat_(c,v)(xi)=C_(c,v) exp(i xi t_v)
                (c+v−i xi)(a_v+xi²+2iv xi)^(-N),
    C_(c,v)=exp(−v t_v)/[norm² g_c(t_v)].

Riccati gives q_N(t_v)>v, so that

    (C_(c,v)a_v^(-N))(c+v)<=32s_v/3<sqrt(N)/2.

Thus the Fourier factor is absorbed by

    |c+v−i xi|/(c+v)<=sqrt(1+xi²),

since c+v>=1. No constant is lost when varying v or c. The squared modulus of the denominator is a_v²+beta_v xi²+xi^4.

With a_v in [3953/4,992], beta_v in [1985,3985/2], the same comparisons of 038 prove

    |fhat_(c,v)(xi)|<=sqrt(N)exp(−Nxi²/1000), |xi|<=1,
    int_(|xi|>=1)|fhat_(c,v)(xi)|d xi/(2pi)
                  <65sqrt(N)exp(−N/2000), N>=16.         (GAMMA)

The script checks the extreme bounds exactly: beta_v/(a_v²+beta_v+1)>1/500, beta_v/a_v²>1/500 and s_v<sqrt(N)/22. The proof of the tail reserves the power N/4>=4, as in 038.

## 5. Signed INFINITE product preserved

Define the absolutely convergent operator

    M_sigma f(ell)=U_sigma^(-1)sum_(n>=1)mu(n)n^(-sigma)
                                                   f(ell+logn).

The f_(c,v) are bounded and have integrable Fourier transform; sum n^(-sigma)<infinity justifies Fubini. The multiplier is the infinite Euler product Z_sigma(i xi)/U_sigma. Its centred logarithm admits the ABSOLUTE series

    log[Z_sigma(i xi)/U_sigma]+iA_sigma xi
      =−sum_p sum_(k>=1)
        [exp(ik xi logp)−1−ik xi logp]/[k p^(k sigma)].

By |exp(it)−1−it|<=t²/2 its modulus is <=B_sigma xi²/2. Applying exactly the Fourier cutoff of 038 and (GAMMA) proves

    |M_sigma f_(c,v)(0)−f_(c,v)(−A_sigma)|
      <=12000B_sigma/N
        +65sqrt(N)[(1+1/delta)^2+1]exp(−N/2000),          (INFINITE)

if N>=16 and B_sigma<=N/1000. There is no finite group Q nor any omitted coprime outer sum in this inequality. Jensen is not applied to a signed measure.

## 6. Shifted profile on its physical side

Put L=1000 and assume

    N>=4L²=4,000,000,
    L/sqrt(N)<=delta<=3/2,
    v=1/2+delta.

From (MOMENTS), A:=A_sigma<=5/delta and B_sigma<=5/delta². Moreover t_v>=d/992>=N/(2·992), while A<=5sqrt(N)/L. The inequality L²>5·992 proves t_v>A on the whole range. The shifted argument t_v−A is POSITIVE; the sign of the left extension of f is not taken.

Riccati, q'>0 and q'<M_N give

    f_(c,v)(−A)>=(1−M_N A)exp(−M_N A²/2).

Indeed q(t_v)>=v, q(t_v−s)>=v−M_Ns and the quotient (c+q(t_v−A))/(c+q(t_v))>=1−M_NA, because c+q(t_v)>=1. With M_N<=u²/N,

    f_(c,v)(−A)>1−15u²/L².

For the upper bound, q(t_v)−v<=M_Nv/(u²+v²)<=2M_N/u² and the previous quotient is <=1. Thus

    f_(c,v)(−A)<=exp(5/L²)<=1/(1−5/L²).

## 7. Complete sign of the inverse at all tilted centres

On the above range, B_sigma/N<=5/L²<1/1000 and the first error of (INFINITE) is <=60000/L²=.06. The second is <1/200. To prove this without numerical estimation of exponentials, use delta<=3/2 and delta>=L/sqrt(N):

    [(1+1/delta)^2+1]<=17/(2delta²),
    exp(−N/2000)<=6(2000/N)^3.

At N>=4L² this gives a majorant 3315·10^9/L^5<1/200. The final rational comparisons give

    9/10<M_sigma f_(c,v)(0)<11/10.

By (FULL), for each v in [1/2+1000/sqrt(N),2] and sigma=1/2+v,

    (9/10)U_sigma<h_N(e^t_v)/H_N(e^t_v)<(11/10)U_sigma,
    (9/10)U_sigma<K_N(e^t_v)/G_N(e^t_v)<(11/10)U_sigma.    (SHOULDER)

These are the COMPLETE inverses, with all Möbius integers. PRODUCTS also gives the explicit lower bound (9/10)delta/(1+delta)>0. It is not a sign of a truncated grouping.

## 8. Positivity on the WHOLE tail and correct comparison with 026

The function v->t_v=2dv/(u²−v²) is strictly increasing. Hence SHOULDER covers all t between T_N=t_(1/2+1000/sqrtN) and t_2.

For t>=t_2, q_N(t)>=2. The dilation quotient common to both inverses has logarithmic derivative

    d/dell log[e^(−ell/2)g_c(t+ell)/g_c(t)]
       =−1/2−q_N(t+ell)+q_N'(t+ell)/(c+q_N(t+ell))<-2,

because M_N<=u²/N<5/4 and c+q>=5/2. Each term n>=2 is bounded by n^(-2), and the absolute sum is <3/4. Hence both complete quotients are >1/4 for ALL t>=t_2.

We conclude for ALL N>=4,000,000 and ALL x>=exp(T_N):

    h_N(x)>0, K_N(x)>0.                                (TAIL)

For fixed L,

    T_N=(N−1)/992+(1985L/992²)sqrt(N)+O(1).

Moreover v_N<=1 on the declared range, so T_N<=2d/(u²−1)<d/330. The two cutoffs of K026 are >d/330: t_J directly and t_R because Q_d>3/2. Thus TAIL legitimately improves the cutoff of the SAME K_N; it also improves the previous cutoff 020 of h_N. A theorem that 026 only proved for K_N is not attributed to h_N.

## 9. Scope of the result

The new bound controls for the first time the signed infinite product on an energy shoulder and the subsequent tail. The inverse may still take signs in the uncovered interior region; no sign is claimed at the critical centre delta0, nor is the restriction sigma>1 removed.

The representation F_N=2int h_N B keeps a favourable tail since B<0, but its magnitude has not been compared with the adverse interior part or with ARCH_sharp. In particular W>=0, a new row or a new window T is not claimed. The precision of the polar−complete-comb residue remains an additional obligation; SHOULDER is not sold as a sufficient relative error for W.

Verifier: tools/power_infinite_shoulder_039_verify.py, Fraction/intervals for uniform constants, arithmetic bound and thresholds; PASS. It does not evaluate W at new N nor enumerate primes. The independent audit confirms c,v, normalization, infinite inversion, physical conditions and positivity of the whole tail. An additional adversarial check was also approved. Papers untouched.
