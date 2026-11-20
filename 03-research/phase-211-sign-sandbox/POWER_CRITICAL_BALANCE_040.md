# POWER_CRITICAL_BALANCE_040 — Elementary factor of the infinite product and signs near the center

Status: **PROVED, core and CONSTANT-CUTOFF approved by independent audit**. See [POWER_CRITICAL_AUDIT_040.md](POWER_CRITICAL_AUDIT_040.md). Fixed rate u=63/2. Papers untouched.

Results: expansion of the COMPLETE arithmetic inverse with explicit remainder O(delta³+N^(-3/2)) and exponential tail; at delta=N^(-2), uniform OPPOSITE signs of h_N and K_N near the energy center. No sign of W is claimed.

## 1. Corpus and precise difference

Consulted ROUTES-TRIED-INDEX/README.md, the master grid and CROSSWORD-TO-D; read INVERSE_KERNEL020, UNIFORM_CUTOFF026, SIGNED_MOMENTS038 and INFINITE_SHOULDER039. The Euler–Maclaurin formulas and the main part of the Euler sum are known; they are not presented as new tools.

The difference with respect to038/039 is to keep the elementary FACTOR of the Euler reciprocal at sigma=1+delta before inverting Fourier. One does not center via divergent A_sigma and B_sigma when delta drops to scale1/N. The bound turns out ABSOLUTE for the complete quotient of the inverse and smaller than its scale1/N in the analyzed regime, instead of a relative error that does not decide the sign. Only the integral of the fractional part and absolutely convergent products at sigma>1 are used.

## 2. Local factor with explicit remainder

For Re z>0,

    zeta(1+z)=1/z+H(z),
    H(z)=1−(1+z)int_1^infty {x}x^(−2−z)dx.

This identity comes from the sum of floor(x) by integration by parts. Moreover H(0)=gamma: integrating up to an integer M gives int_1^M{x}x^(-2)dx=logM−H_M+1.

For Re z>=0, |z|<=1/8, the integral has modulus<=1 and its difference from the value at0 is<=|z|, because int_1^infty logx x^(-2)dx=1. Hence

    |H(z)|<=17/8,
    |H(z)−gamma|<=2|z|,
    |zH(z)|<=17/64<1.

Expanding a geometric fraction with controlled DENOMINATOR gives

    1/zeta(1+z)=z−gamma z²+R3(z),
    |R3(z)|<=9|z|³.                                    (LAURENT)

Indeed R3=−z²(H−gamma)+z³H²/(1+zH), and2+(17/8)²/(1−17/64)<9. No formal series without remainder is postulated.

## 3. Gamma profile and complete ratio of the inverse

Keep039: d=N−1, c in{1/2,3/2}, rho_N even, q=−rho'/rho for positive argument,

    g_c(t)=c rho_N(t)−rho_N'(t),
    v=1/2+delta, a_v=u²−v², t_v=2dv/a_v,
    f(ell)=exp(vell)g_c(t_v+ell)/g_c(t_v).

The left extension of f is not considered a probability. At sigma=1+delta>1, the corresponding COMPLETE inverse has ratio

    R_c(t_v)=sum_(n>=1)mu(n)n^(−sigma)f(logn).

For c1/2 this is h_N(e^t_v)/H_N(e^t_v); for c3/2 it is K_N(e^t_v)/G_N(e^t_v), with the normalizations039. f(0)=1.

Fourier039 keeps the exact formula and the uniform bounds, for v in[1/2,2]:

    |fhat(xi)|<=sqrt(N)exp(−Nxi²/1000), |xi|<=1,
    |fhat(xi)|<sqrt(N)/2 ·sqrt(1+xi²)
       [1+beta_v xi²/a_v²+xi^4/a_v²]^(-N/2),
    beta_v=2(u²+v²), beta_v/a_v²>1/500.

The normalization uses the norm of the original gamma atom. The infinite multiplier is1/zeta(1+delta−i xi); its Euler series is absolute because delta>0. No Möbius integer is discarded.

## 4. Inversion with linear and quadratic factor: uniform bound

Suppose N>=24 and0<delta<=1/16. On |xi|<=1/16, z=delta−i xi belongs to |z|<=1/8, and LAURENT applies. On inverting the polynomials z,z² there appear exactly

    delta f(0)−f'(0),
    delta²f(0)−2delta f'(0)+f''(0).

One obtains

    R_c(t_v)=delta−f'(0)
          −gamma[delta²−2delta f'(0)+f''(0)]+E_N,          (EXPANSION)
    |E_N|<=288delta³+9·10^6/N^(3/2)
                  +110000sqrt(N)delta^(-1)exp(−N/10^6). (REMAINDER)

Proof of the center. The inequality |delta−i xi|³<=2(delta³+|xi|³), LAURENT and the Gaussian integrals039 give

    int_R sqrt(N)exp(−Nxi²/1000)d xi/(2pi)<16,
    int_R sqrt(N)|xi|³exp(−Nxi²/1000)d xi/(2pi)
                                       <500000/N^(3/2).

Multiplying by18 proves the first two errors.

For the tail |xi|>=1/16, the absolute Euler sum gives |1/zeta|<=1+1/delta; the polynomial z−gamma z² is bounded together with it by(4/delta)(1+xi²). The gamma power is split into two halves and N/4>=6 is reserved. The extracted half is<=exp(−N/10^6), since log(1+(1/500)(1/16)²)>1/250000. The auxiliary integral of(1+|xi|)(1+xi²)(1+xi²/500)^(-6) over R is<110000. Its four monomials are bounded by92,100,46000,62500. Including the prefactor sqrt(N)/2 and2pi gives the last error of REMAINDER.

All integrations are absolute. The tail bound uses delta>0; that condition is not removed by an informal continuation.

## 5. New elementary gamma curvature inequality

In addition to q''<0 already proved031, one has

    −2q'(t)/t<q''(t)<0, t>0.                            (CURVATURE)

Proof. With P_N positive of degree d and weights p_jt^j/P_N(t),

    t²q'=EJ−Var(J)<d.

Define S=q''+2q'/t. Differentiating Riccati026 shows that at any point S=0,

    S'=2q'[q'−(2d+1)/t²]<0.

On the other hand P_N gives the algebraic expansion

    q=u−d/t+d(d+1)/(2ut²)+O(t^(-3)),
    S=d(d+1)/(ut^4)+O(t^(-5))>0 at infinity.

If S had some nonpositive value earlier, it would have to become positive again, but at EVERY contact S0 its derivative is negative; tangencies are also excluded. Hence S>0. This proves CURVATURE without a special Bessel inequality.

Differentiating Riccati and combining its two curvature bounds gives

    d q/[t(qt+d+1)]<q'<d q/[t(qt+d)].                    (SLOPE)

This provides an effective lower scale for comparing REMAINDER, not just a formal asymptotic.

## 6. Exact derivatives of the profile at the tilted center

Write q=q_N(t_v), b=q_N'(t_v), epsilon=q−v>0. Riccati factors:

    b=epsilon(q+u²/v),
    eta:=epsilon/b=v/(u²+vq).

By direct differentiation,

    f'(0)=b[1/(c+q)−eta],
    f''(0)=−b+q''/(c+q)
                    +b²[eta²−2eta/(c+q)].              (DERIVATIVES)

In the regime delta=N^(-2), N>=2^80, v<=1, q<2, eta<=1/u² and t_v>=N/(2·992). CURVATURE, b<=M_N<=u²/N and c+q>=1 prove

    −b(1+3970/N)<f''(0)<−b,
    0<f'(0)<b/(c+1/2),
    f'_(c=1/2)(0)>=b[1−2/N−1/u²].                     (BOUNDS)

For the lower bound of b, use SLOPE, q>=1/2, t_v<=2d/(u²−1)<d/400 and qt_v+d+1<3d. Hence

    b>50/N.                                            (LOWER-b)

The constants are deliberately loose; no concrete N is evaluated.

## 7. Sign pattern near the energy center

With delta=N^(-2), REMAINDER proves for ALL N>=2^80

    |E_N|<10^(-4)/N.

The first term is direct; for the exponential one uses exp(−x)<=6!x^(-6), so that N times the tail is bounded by110000·6!·10^36/N^(5/2). Everything is compared rationally at the monotone endpoint2^80.

The bounds57/100<gamma<3/5 and BOUNDS/LOWER-b, substituted in EXPANSION, give the signs

    h_N(e^t_v)/H_N(e^t_v)<−1/N,
    K_N(e^t_v)/G_N(e^t_v)>1/N,                           (CENTRAL-SIGNS)
    v=1/2+N^(-2), N>=2^80.

For c3/2, the terms delta and2gamma delta f' are favorable, −gamma f''>=gamma b and f'<=b/2; the benefit is at least(gamma−1/2)b, larger than the errors. For c1/2, the upper bound is

    delta+b{−1+1/u²+2/N+(3/5)(1+3970/N)
                    +(6/5)delta}+|E_N|,

strictly less than−1/N via b>50/N and the cited remainder. The term−gamma delta² only improves that upper bound.

These are signs of the COMPLETE inverse at a center satisfying t_v=d/992+O(1/N). The exact transition point in t is not yet identified nor is a sign of W claimed. The signed sums are kept before the remainder; no conclusion comes from a signed measure treated as a probability.

## 8. Uniform cutoff at constant distance

For ALL N>=2^80 and

    2000/N <= delta <= 1000/sqrt(N),

v<1, q<2, 0<f'<b and f''<−b hold by the same exact identities. Since 0<gamma<1, EXPANSION implies

    R_c(t_v)>=delta−u²/N−delta²−|E_N|.

The rational constants verified in the script give, uniformly on that interval,

    delta<1/1000,
    288delta³<delta/1000,
    9·10^6/N^(3/2)<1/(10000N),
    110000sqrt(N)delta^(-1)e^(−N/10^6)<1/(10000N).

For the last inequality exp(−x)<=6!x^(−6) and delta>=2000/N suffice: N times the term is at most 55·6!·10^36/N^(7/2). Hence

    R_c(t_v)> (998/1000)delta−(u²+1/5000)/N>0,

since delta>=2000/N. This covers both c and ALL centers t_v of that interval. At the upper endpoint it links with theorem039, valid for all later t. Therefore

    h_N(e^t)>0 and K_N(e^t)>0
    for ALL t>= (N−1)/992+5, N>=2^80.             (CONSTANT-CUTOFF)

Indeed, if delta0=2000/N, the exact difference between the first center and d/992 is

    t_(1/2+delta0)−d/992
       =d·delta0·(1985+delta0)/(992·[u²−(1/2+delta0)²])<5,

using d·delta0<2000, delta0<1 and u²−v²>=u²−1. The conclusion is a sufficient cutoff, not the exact location of any transition. It improves the shoulder O(sqrt(N)) of039 for the same complete objects h and K; nor does it decide W.

## 9. Scope and validation

The proof controls for the first time a scale1/N of the infinite inverse at the center, where039 only gave a sign on a shoulder O(sqrt(N)). CENTRAL-SIGNS and CONSTANT-CUTOFF were approved independently; the exact verifier reproduces PASS. The interior integral region and the balance with ARCH_sharp remain pending; a locally negative h_N does not imply negative W.

There are no campaigns over N, m or primes. The proof uses the explicit local factor, gamma integrals and uniform inequalities. The independent audit reviewed the LAURENT remainder, Fourier normalization, CURVATURE, the factors of DERIVATIVES, sign comparisons and the link with039. Papers untouched.
