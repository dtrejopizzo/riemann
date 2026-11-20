# POWER_THREE_002 — Three powers via elementary concentration

Status: PROVED (large explicit range); gives no uniformity in the number of generators. Papers untouched.

Antecedents consulted: POWER_CONE_001, PROPOSAL_POWER_CASES_2026_11_04; index README:393,655, NODE_001:195, grid part3:12 and part5:7, crossword (theta/cosh/Pick). New reason relative to the general Pick positivity already recorded: a finite range is proved via quantitative concentration of an explicit subspace of three exponentials. No other general characterization is proposed.

## 1. Audit of the cross term

Write u=a-1/2, v=b-1/2, h_u(y)=exp(-uy)1_{y>0}, g(a)=(psi(a/2)-log pi)/2 and D(a)=zeta'(a)/zeta(a). The symmetrized correlation is

    [exp(-ut)+exp(-vt)]/[2(u+v)].

The direct integral of the archimedean multiplier gives [g(a)+g(b)]/(u+v), and the comb gives [D(a)+D(b)]/(u+v). The full bilinear polar term is

    1/[(a-1)b]+1/[a(b-1)].

With R(a)=1/a+1/(a-1), this is EXACTLY [R(a)+R(b)]/(a+b-1), since 1/a+1/(b-1)=(a+b-1)/[a(b-1)], and analogously for the other pair. Therefore K_ab=[L(a)+L(b)]/(a+b-1) is correct; it does not require inferring the cross term from diagonals. The archimedean integration uses Re psi as a harmonic function on Re z>0 and its Poisson integral, or its absolutely convergent series after subtracting psi(1/4).

## 2. Three-generator theorem

Let A>=2^31 and 0<h<=A/2. For any real c_0,c_1,c_2 not all zero,

    rho(X)=Σ_{j=0}² c_j X^{-(A+jh)}

satisfies Q[rho]>0. More precisely, with f(y)=Σ c_j zeta(A+jh)exp(-(A+jh-1/2)y), y>0,

    Q[rho]>=9 ||f||_2².

The constant is deliberately very conservative. Proof below. In particular P3 holds in this range, without computing an ill-conditioned determinant.

## 3. Rational basis and frequency concentration

Consider any space of three exponentials with distinct rates u<=u_j<=3u, u>=2^30. It has an orthonormal basis whose Fourier transforms are

    F_j(tau)=sqrt(2u_j)/(u_j+i tau) Π_{k<j}(i tau-u_k)/(i tau+u_k).

Orthonormality is checked by integration of rational fractions (close the contour in the pole-free half-plane); equivalently each factor (s-u_k)/(s+u_k) preserves the norm on the imaginary axis and kills the Laplace evaluation at s=u_k. Parseval uses d tau/(2pi). Since each factor has modulus one,

    |fhat(tau)|² <=||f||² Σ_j 2u_j/(u_j²+tau²)<=6||f||²/u.

The probability density p=|fhat|²/(2pi||f||²) is bounded by M=3/(pi u). Among mass-one densities bounded by M, the integral of log|tau| is minimized by M 1_{|tau|<=1/(2M)}. By direct integration,

    ∫ log|tau| p(tau)d tau >= log(pi u/6)-1.

Note the factor TWO: the length of the extremal interval is 1/M, its radius 1/(2M). This is the normalization used in the following bounds.

## 4. Archimedean bound without numerical special constants

The digamma series gives, setting y=tau/2,

    Re psi(1/4+iy)=psi(1/4)+Σ_{k>=0} y²/[(k+1/4)((k+1/4)²+y²)].

The summand decreases in k; integral comparison gives sum >=(1/2)log(1+4tau²). Moreover psi(1/4)=-gamma-pi/2-3log2>-6, and log pi<2. Therefore

    m(tau)>=log|tau|-8.

Combining with §3,

    <m(D)f,f>/||f||² >= log(pi u/6)-9
       > log u-10 >10,

because pi>3, log2<1 and log u>=30log2>20. All inequalities are strict in the declared range.

## 5. Tail and polar bounds

The inverse transform of each all-pass factor is delta_0-2u_k exp(-u_k y)1_{y>0}. Expanding the convolution of up to two factors and using u_j<=3u gives

    |f(y)|<=sqrt(6u)||f|| exp(-uy)[3+18uy+18(uy)²].

Cauchy--Schwarz was used on the three orthonormal coefficients and then a sum of absolute values; coefficients larger than necessary make the bounds easier. For z>=0, z<=2exp(z/2), z²<=16exp(z/2), so that

    |f(y)|<=327sqrt(6u)||f||exp(-uy/2),
    ||f 1_{y>=t}||<=327sqrt6 exp(-ut/2)||f||.

Consequently |c_f(t)|<=327sqrt6 exp(-ut/2)||f||². The absolute value of the comb is at most

    654sqrt6 Σ_{n>=2} Lambda(n)n^{-(u+1)/2}||f||²
       <=1602 Σ_{n>=2}n^{-(u-1)/2}||f||² < ||f||²/10.

The last inequality already holds if (u-1)/2>=16, using Σ n^{-p}<=2^{-p}(1+2/(p-1)).

For the two polar moments, integrating the original polynomial bound, using u-1/2>=u/2, gives

    |∫ f(y)exp(±y/2)dy| <=366sqrt(6/u)||f||.

In detail the three integrated terms are at most 6/u, 72/u and 288/u. Therefore

    |2AB|<=12*366² ||f||²/u <||f||²/10

for u>=2^30. Summing §§4--5 gives Q[rho]>(10-1/10-1/10)||f||²>9||f||².

## 6. Scope and next order

For the triple of the theorem u=A-1/2>=2^30 and u_2=A+2h-1/2<=3u. The proof covers even unequal triples contained in [u,3u]. It requires no minimal separation; by continuity it covers confluent limits and exponentials multiplied by polynomials of degree <=2.

## 7. All orders with growing threshold (PROVED)

For each integer n>=1, any family of n distinct rates u_i in [u,3u], with u>=2^{40n}, satisfies

    W[Σ_i d_i exp(-u_i y)1_{y>0}]>=9||Σ_i d_i exp(-u_i y)||².

This proves positivity of all order-n matrices of the kernel of §1 whose exponents a_i=u_i+1/2 lie in that range. It is not uniformity in n.

Proof with constants: the same rational basis gives p(tau)<=n/(pi u), hence

    arch/||f||² >=log(pi u/(2n))-9 >log u-log n-9 >10.

The last inequality uses log u> (80/3)n and log n<=n-1. The convolution expansion gives

    |f(y)|<=sqrt(6u)||f|| exp(-uy) P_n(uy),
    P_n(z)=Σ_{k=0}^{n-1}binom(n,k+1)6^k z^k/k!.

Here the identity Σ_{j=k}^{n-1}binom(j,k)=binom(n,k+1) was used. Since z^k/k!<=2^k exp(z/2), one gets P_n(z)<=13^n exp(z/2). Therefore

    tailnorm(t)<=sqrt6 13^n exp(-ut/2)||f||,
    |∫ f exp(±y/2)dy|<=2sqrt6 13^n ||f||/sqrt u.

The second bound integrates P_n exactly against exp(-uy/2): Σ binom(n,k+1)12^k<13^n. Hence

    |polar|/||f||² <=48*169^n/u <1/10.

For the comb, p=(u-1)/2>=u/4>=20n+10 and

    |comb|/||f||² <=2sqrt6 13^n Σ_{q>=2}q^{-p}
       <=6sqrt6 13^n 2^{-p}<15*16^n*2^{-(20n+10)}<1/10.

Also 48*169^n/u<48*2^{-32n}<1/10, as used above. Sum of terms: W>9.8||f||²>9||f||². The exponential dependence 2^{40n} is very crude and explicit; it has not been optimized.

## 8. Quantitative obstruction to extrapolating these ranges

For normalized f in the family of the order-n theorem,

    ||f 1_{y>=delta}||<=sqrt6 13^n exp(-2^{40n}delta/2).

In particular for delta=1 this is less than 1/100 for all n>=1: use log13<3 and 2^{40n}/2>3n+10. Thus the union of these families is NOT dense in L²(0,infinity): every unit function supported in [1,2] lies at distance at least sqrt(2-2/100)>1.4 from each normalized member, by Cauchy--Schwarz. Even with arbitrary scalars the distance to the line generated by each f is >=sqrt(1-10^{-4}).

Translating the packets can remove this localization around zero, but the theorem only proves the sign of each packet separately; it does not control the cross terms of sums of translated packets. One cannot pass from a positive union to its linear envelope.

Therefore this result, although valid at every order with growing threshold, does not give a positive dense domain for the form. The threshold must come down to allow a common family of exponents, or the cross terms between packets must be controlled explicitly. The result does not resolve the sign of the paper.
